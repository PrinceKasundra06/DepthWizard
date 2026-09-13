import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

# Enhance Sidebar
bad_sidebar = """            <div class="draftly-sidebar-content">
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 1rem;">
                    <label style="display: flex; align-items: center; justify-content: space-between; font-size: 13px; font-weight: 500; cursor: pointer;">
                        <span><i class="fa-solid fa-cube" style="margin-right: 8px;"></i> True 360 Object</span>
                        <input type="checkbox" id="mode360Toggle" style="accent-color: #ffffff; transform: scale(1.2);">
                    </label>
                    <p style="font-size: 11px; color: rgba(255,255,255,0.4); margin-top: 10px; line-height: 1.5;">
                        Enable this if you are uploading a photo of a single object (like a chair). It will extract the object and hallucinate the back.
                    </p>
                </div>
            </div>"""

good_sidebar = """            <div class="draftly-sidebar-content">
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1.25rem; box-shadow: inset 0 1px 1px rgba(255,255,255,0.05);">
                    <label style="display: flex; align-items: center; justify-content: space-between; font-size: 13px; font-weight: 600; cursor: pointer; color: #fff;">
                        <span><i class="fa-solid fa-cube" style="margin-right: 8px; color: #fff;"></i> True 360 Mode</span>
                        <input type="checkbox" id="mode360Toggle" checked style="accent-color: #ffffff; transform: scale(1.2);">
                    </label>
                    <p style="font-size: 11px; color: rgba(255,255,255,0.4); margin-top: 12px; line-height: 1.6;">
                        Uses TripoSR to intelligently hallucinate the unseen geometry of your object. Recommended for product photos.
                    </p>
                </div>
                
                <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 12px; padding: 1.25rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Advanced Settings</div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Resolution</span>
                        <span style="font-size: 11px; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px;">High (192)</span>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Marching Cubes</span>
                        <span style="font-size: 11px; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px;">Optimized</span>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Texture Engine</span>
                        <span style="font-size: 11px; color: rgba(255,255,255,0.3); border-bottom: 1px dashed rgba(255,255,255,0.3);">Coming Soon</span>
                    </div>
                </div>
            </div>"""

html = html.replace(bad_sidebar, good_sidebar)

# Enhance Viewport
bad_viewport = """        <main class="draftly-viewport" style="background: radial-gradient(circle at center, #111 0%, #000 100%);">
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

good_viewport = """        <main class="draftly-viewport" style="background: #000; position: relative;">
            <!-- 3D Particle Wave Background -->
            <canvas id="bg-canvas" style="position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%;"></canvas>
            <div style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.8) 100%); z-index: 5; pointer-events: none;"></div>
            
            <!-- Upload Container -->
            <div style="position: relative; z-index: 10; width: 100%; display: flex; justify-content: center;">
                <div class="upload-box interactive-card" id="dropZone" style="background: rgba(15,15,15,0.6); backdrop-filter: blur(24px); border: 2px dashed rgba(255,255,255,0.2); border-radius: 24px; padding: 4rem 2rem; max-width: 500px; width: 90%; box-shadow: 0 30px 60px rgba(0,0,0,0.6), inset 0 0 20px rgba(255,255,255,0.02); transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
                    <div style="width: 80px; height: 80px; background: rgba(255,255,255,0.05); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 2rem auto; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 0 20px rgba(255,255,255,0.05);">
                        <i class="fa-solid fa-cloud-arrow-up" style="font-size: 2rem; color: #fff;"></i>
                    </div>
                    <h3 style="font-size: 1.4rem; font-weight: 500; margin-bottom: 0.5rem; color: #fff;">Drop image to process</h3>
                    <p style="color: rgba(255,255,255,0.5); font-size: 0.95rem; margin-bottom: 2.5rem;">Supports JPG, PNG, WebP</p>
                    
                    <input type="file" id="fileInput" accept="image/*" style="display:none;">
                    <button class="draftly-btn-small draftly-btn-primary" style="height: 44px; padding: 0 2rem; font-size: 13px;" onclick="document.getElementById('fileInput').click()">Browse Files</button>
                </div>
                
                <div id="previewContainer" style="display: none; width: 90%; max-width: 500px; text-align: center; background: rgba(15,15,15,0.8); padding: 2rem; border-radius: 24px; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(30px); box-shadow: 0 30px 60px rgba(0,0,0,0.8);">
                    <div style="position: relative; display: inline-block; margin-bottom: 2rem;">
                        <div style="position: absolute; inset: -4px; background: linear-gradient(45deg, rgba(255,255,255,0.2), transparent); border-radius: 16px; filter: blur(10px); z-index: 0;"></div>
                        <img id="imagePreview" src="" alt="Preview" style="position: relative; max-width: 100%; max-height: 40vh; border-radius: 12px; border: 1px solid rgba(255,255,255,0.2); z-index: 1;">
                    </div>
                    <div style="display: flex; gap: 1rem; justify-content: center;">
                        <button class="draftly-btn-small" id="resetBtn" style="height: 44px; padding: 0 1.5rem; font-size: 13px;"><i class="fa-solid fa-rotate-left"></i> Change</button>
                        <button class="draftly-btn-small draftly-btn-primary" id="generateBtn" style="height: 44px; padding: 0 2rem; font-size: 14px;"><i class="fa-solid fa-wand-magic-sparkles"></i> Generate 3D</button>
                    </div>
                </div>
            </div>
        </main>"""

html = html.replace(bad_viewport, good_viewport)

# Add three.js dependency if missing
if "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js\"></script>" not in html:
    html = html.replace("</head>", "    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js\"></script>\n</head>")

with open("website/frontend/upload.html", "w") as f:
    f.write(html)
    
print("Polished upload.html UI!")
