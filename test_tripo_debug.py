import sys, os
sys.path.append(os.path.join(os.getcwd(), "website/backend"))
from main import preprocess_for_triposr, tsr_model, device
import torch
import traceback

print("Preprocessing...")
try:
    pil_img_rgb, blended_rgb = preprocess_for_triposr("website/backend/uploads/045984f5-acf1-40b8-8780-cf8dabb1dd92.jpg")
    print("Running TripoSR Generation...")
    with torch.no_grad():
        scene_codes = tsr_model([pil_img_rgb], device=device)
        meshes = tsr_model.extract_mesh(scene_codes, has_vertex_color=True, resolution=128)[0]
    print("Success! Vertices:", len(meshes.vertices))
except Exception as e:
    traceback.print_exc()
