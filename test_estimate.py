import numpy as np
import cv2
import torch
import ssl
from PIL import Image
import traceback

ssl._create_default_https_context = ssl._create_unverified_context
device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")

midas = torch.hub.load("intel-isl/MiDaS", "MiDaS")
midas.to(device).eval()
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
transform = midas_transforms.default_transform

def estimate_depth(img_rgb: np.ndarray) -> np.ndarray:
    pil_img = Image.fromarray(img_rgb)
    input_batch = transform(pil_img).to(device)
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

try:
    img = cv2.imread("website/backend/uploads/045984f5-acf1-40b8-8780-cf8dabb1dd92.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    estimate_depth(img_rgb)
    print("SUCCESS")
except Exception as e:
    traceback.print_exc()
