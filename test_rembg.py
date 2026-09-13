import cv2
import numpy as np
from PIL import Image
import rembg

def preprocess_for_triposr(img_path):
    # 1. Remove background
    with open(img_path, 'rb') as i:
        input_data = i.read()
    
    subject_data = rembg.remove(input_data)
    img_rgba = Image.open(import_io_bytes(subject_data))
    return img_rgba

def import_io_bytes(data):
    import io
    return io.BytesIO(data)

img = preprocess_for_triposr("website/backend/uploads/045984f5-acf1-40b8-8780-cf8dabb1dd92.jpg")
print(img.size, img.mode)
