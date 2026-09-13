import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

bad_viewport = """        <main class="draftly-viewport" style="background: radial-gradient(circle at center, #111 0%, #000 100%);">
            <div class="upload-box interactive-card" id="dropZone" style="margin: auto;">
                <div class="upload-icon">
                    <i class="fa-solid fa-cloud-arrow-up"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 500; margin-bottom: 0.5rem;">Drop image to generate</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem;">or click to browse files</p>
                
                <input type="file" id="fileInput" accept="image/*">
                <button class="btn btn-primary" onclick="document.getElementById('fileInput').click()">Select Image</button>
            </div>
        </main>"""

good_viewport = """        <main class="draftly-viewport" style="background: radial-gradient(circle at center, #111 0%, #000 100%);">
            <div class="upload-box interactive-card" id="dropZone" style="margin: auto;">
                <div class="upload-icon">
                    <i class="fa-solid fa-cloud-arrow-up"></i>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 500; margin-bottom: 0.5rem;">Drop image to generate</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem;">or click to browse files</p>
                
                <input type="file" id="fileInput" accept="image/*" style="display:none;">
                <button class="draftly-btn-small draftly-btn-primary" style="height: 40px; padding: 0 1.5rem; font-size: 13px;" onclick="document.getElementById('fileInput').click()">Select Image</button>
            </div>
            
            <div id="previewContainer" style="display: none; margin: auto; text-align: center; background: rgba(10,10,10,0.8); padding: 2rem; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(20px);">
                <img id="imagePreview" src="" alt="Preview" style="max-width: 100%; max-height: 40vh; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                <div style="display: flex; gap: 1rem; justify-content: center;">
                    <button class="draftly-btn-small" id="resetBtn" style="height: 44px; padding: 0 1.5rem; font-size: 13px;"><i class="fa-solid fa-rotate-left"></i> Change Image</button>
                    <button class="draftly-btn-small draftly-btn-primary" id="generateBtn" style="height: 44px; padding: 0 1.5rem; font-size: 13px;"><i class="fa-solid fa-wand-magic-sparkles"></i> Generate 3D</button>
                </div>
            </div>
        </main>"""

html = html.replace(bad_viewport, good_viewport)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)
    
print("Fixed upload.html!")
