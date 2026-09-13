import os
import uuid
import numpy as np
import cv2
import trimesh
from PIL import Image
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import mimetypes
mimetypes.add_type('text/plain', '.obj')
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import torch
import rembg
import io
import ssl
import sys

# Add TripoSR to path
sys.path.append(os.path.join(os.path.dirname(__file__), "TripoSR"))
from tsr.system import TSR

# Fix macOS SSL Certificate Error for torch.hub.load
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI(title="DepthWizard - Depth Estimation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(__file__)
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
RESULT_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# Fix MPS Memory Limit Crash for TripoSR
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")

print("Loading TripoSR (True 360) Model...")
tsr_model = TSR.from_pretrained(
    "stabilityai/TripoSR",
    config_name="config.yaml",
    weight_name="model.ckpt",
)
tsr_model.to(device)

print("Loading MiDaS Depth Model (Fallback)...")
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
midas.to(device).eval()
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
transform = midas_transforms.small_transform


def preprocess_for_triposr(img_path):
    # 1. Remove background using rembg
    with open(img_path, 'rb') as i:
        input_data = i.read()
    subject_data = rembg.remove(input_data)
    img = Image.open(io.BytesIO(subject_data)).convert("RGBA")
    
    # 2. Get bounding box of the non-transparent pixels
    np_img = np.array(img)
    alpha = np_img[:, :, 3]
    coords = cv2.findNonZero(alpha)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        img = img.crop((x, y, x + w, y + h))
    
    # 3. Pad to square and resize to 512x512 (TripoSR optimal size)
    # Target size is 512, but we want the object to fill ~85% of it (approx 435px)
    max_dim = max(img.width, img.height)
    scale = 435.0 / max_dim
    new_w, new_h = int(img.width * scale), int(img.height * scale)
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Create 512x512 gray background
    final_img = Image.new("RGB", (512, 512), (128, 128, 128))
    # Paste centered using alpha channel as mask
    paste_x = (512 - new_w) // 2
    paste_y = (512 - new_h) // 2
    final_img.paste(img, (paste_x, paste_y), img)
    
    return final_img, np.array(final_img)

def estimate_depth(img_rgb: np.ndarray) -> np.ndarray:
    input_batch = transform(img_rgb).to(device)
    with torch.no_grad():
        prediction = midas(input_batch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img_rgb.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()
    depth = prediction.cpu().numpy()
    
    mn, mx = depth.min(), depth.max()
    if mx - mn > 1e-6:
        depth = (depth - mn) / (mx - mn)
    else:
        depth = np.zeros_like(depth)
    return depth

@app.post("/api/process")
async def handle_process(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1] or ".png"
    img_path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")
    
    with open(img_path, "wb") as f:
        f.write(await file.read())
        
    try:
        # 1. Image Preprocessing (AI Subject Extraction & Centering)
        pil_img_rgb, blended_rgb = preprocess_for_triposr(img_path)
        
        # 2. Extract Depth & Height (for UI download)
        depth = estimate_depth(blended_rgb)
        depth_uint8 = (depth * 255).astype(np.uint8)
        avg_depth = np.mean(depth)
        estimated_height_meters = round(avg_depth * 15.5, 2)
        
        # Save output paths
        depth_path = os.path.join(RESULT_DIR, f"{file_id}_depth.png")
        orig_path = os.path.join(RESULT_DIR, f"{file_id}_orig.png")
        obj_path = os.path.join(RESULT_DIR, f"{file_id}_mesh.obj")
        
        cv2.imwrite(depth_path, depth_uint8)
        cv2.imwrite(orig_path, cv2.cvtColor(blended_rgb, cv2.COLOR_RGB2BGR))
        
        # 3. Generate True 360 Mesh using TripoSR
        try:
            print(f"[{file_id}] Running TripoSR Generation...")
            with torch.no_grad():
                scene_codes = tsr_model([pil_img_rgb], device=device)
                # Resolution 192 is a good balance between quality and preventing OOM on 8GB Macs
                meshes = tsr_model.extract_mesh(scene_codes, has_vertex_color=False, resolution=192)[0]
                
                # Extract trimesh
                mesh = meshes
                
                # Transform to correct orientation for ThreeJS (Y up)
                transform_matrix = trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0])
                mesh.apply_transform(transform_matrix)
                
                # Export to OBJ
                mesh.export(obj_path)
            is_360 = True
        except Exception as e:
            print(f"TripoSR failed: {e}. Falling back to 2.5D only.")
            is_360 = False
            obj_path = "" # Handled dynamically by frontend fallback
            
        return JSONResponse(content={
            "status": "success",
            "obj_url": f"/api/results/{file_id}_mesh.obj" if is_360 else "",
            "depth_url": f"/api/results/{file_id}_depth.png",
            "texture_url": f"/api/results/{file_id}_orig.png",
            "height_map_url": f"/api/results/{file_id}_depth.png",
            "estimated_height": estimated_height_meters,
            "is_360": str(is_360).lower()
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

app.mount("/api/results", StaticFiles(directory=RESULT_DIR), name="results")

FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "frontend")
from fastapi.responses import FileResponse

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/{path:path}")
async def serve_frontend(path: str):
    file_path = os.path.join(FRONTEND_DIR, path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
