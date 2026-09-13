import sys, os
import cv2
import torch
sys.path.append(os.path.join(os.getcwd(), "website/backend"))
from main import process_image

img_path = "website/backend/uploads/sample.jpg" # need an image path
# find an image
import glob
imgs = glob.glob("website/backend/uploads/*.jpg") + glob.glob("website/backend/uploads/*.png")
if not imgs:
    print("No images found.")
    sys.exit()

print("Using image:", imgs[0])
try:
    urls = process_image(imgs[0], "test_360_id")
    print(urls)
except Exception as e:
    print("Error processing:", e)
