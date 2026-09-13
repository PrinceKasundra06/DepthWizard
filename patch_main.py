import sys, re

with open("website/backend/main.py", "r") as f:
    code = f.read()

# Add rembg import
if "import rembg" not in code:
    code = code.replace("import torch", "import torch\nimport rembg\nimport io")

# Add the robust preprocess function
preprocess_code = """
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

"""

if "def preprocess_for_triposr" not in code:
    code = code.replace("def estimate_depth", preprocess_code + "def estimate_depth")

# Replace the try block processing logic
old_logic = """        # 1. Image Preprocessing
        img_np = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        
        # Ensure RGBA for processing
        if img_np.shape[2] == 3:
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2BGRA)
            
        # Convert BGR to RGB for AI models
        img_rgb = cv2.cvtColor(img_np[:, :, :3], cv2.COLOR_BGR2RGB)
        
        # For TripoSR, it needs a white/gray background and RGB input.
        # We blend with 0.5 gray using the alpha channel.
        alpha = img_np[:, :, 3:4] / 255.0
        blended_rgb = img_rgb * alpha + (1.0 - alpha) * 128.0
        blended_rgb = blended_rgb.astype(np.uint8)
        pil_img_rgb = Image.fromarray(blended_rgb)"""

new_logic = """        # 1. Image Preprocessing (AI Subject Extraction & Centering)
        pil_img_rgb, blended_rgb = preprocess_for_triposr(img_path)"""

if old_logic in code:
    code = code.replace(old_logic, new_logic)

with open("website/backend/main.py", "w") as f:
    f.write(code)
    
print("Patched main.py successfully!")
