import sys, os
sys.path.append(os.path.join(os.getcwd(), "website/backend/TripoSR"))
from tsr.system import TSR
from PIL import Image
import torch
import traceback

device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
print("Loading TSR...")
tsr_model = TSR.from_pretrained(
    "stabilityai/TripoSR",
    config_name="config.yaml",
    weight_name="model.ckpt",
)
tsr_model.to(device)

pil_img_rgb = Image.open("website/backend/uploads/045984f5-acf1-40b8-8780-cf8dabb1dd92.jpg").convert("RGB")
print("Running prediction...")
try:
    with torch.no_grad():
        scene_codes = tsr_model([pil_img_rgb], device=device)
        print("Extracting mesh...")
        meshes = tsr_model.extract_mesh(scene_codes, has_vertex_color=True)[0]
        print("Success! Vertices:", len(meshes.vertex))
except Exception as e:
    traceback.print_exc()
