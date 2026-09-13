import sys, os
import cv2
sys.path.append(os.path.join(os.getcwd(), "website/backend"))
from main import process_image

import glob
imgs = glob.glob("website/backend/uploads/*.jpg") + glob.glob("website/backend/uploads/*.png")
if not imgs:
    print("No images found.")
    sys.exit()

print("Using image:", imgs[0])
try:
    urls = process_image(imgs[0], "test_midas_id")
    print("SUCCESS:", urls)
except Exception as e:
    import traceback
    traceback.print_exc()
