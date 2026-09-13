import sys, os
import cv2
import traceback
sys.path.append(os.path.join(os.getcwd(), "website/backend"))

# Load exact code from main.py
with open("website/backend/main.py") as f:
    code = f.read()

exec(code)
try:
    img = cv2.imread("website/backend/uploads/045984f5-acf1-40b8-8780-cf8dabb1dd92.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    estimate_depth(img_rgb)
except Exception as e:
    traceback.print_exc()
