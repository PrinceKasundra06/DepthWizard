import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

target = """                <div class="upload-box interactive-card" id="dropZone" style="background: rgba(15,15,15,0.6); backdrop-filter: blur(24px); border: 2px dashed rgba(255,255,255,0.2); border-radius: 24px; padding: 4rem 2rem; max-width: 500px; width: 90%; box-shadow: 0 30px 60px rgba(0,0,0,0.6), inset 0 0 20px rgba(255,255,255,0.02); transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
                    <div style="width: 80px; height: 80px; background: rgba(255,255,255,0.05); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 2rem auto; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 0 20px rgba(255,255,255,0.05);">
                        <i class="fa-solid fa-cloud-arrow-up" style="font-size: 2rem; color: #fff;"></i>
                    </div>
                    <h3 style="font-size: 1.4rem; font-weight: 500; margin-bottom: 0.5rem; color: #fff;">Drop image to process</h3>
                    <p style="color: rgba(255,255,255,0.5); font-size: 0.95rem; margin-bottom: 2.5rem;">Supports JPG, PNG, WebP</p>
                    
                    <input type="file" id="fileInput" accept="image/*" style="display:none;">
                    <button class="draftly-btn-small draftly-btn-primary" style="height: 44px; padding: 0 2rem; font-size: 13px;" onclick="document.getElementById('fileInput').click()">Browse Files</button>
                </div>"""

replacement = """                <!-- Premium Dropzone -->
                <div class="upload-box interactive-card" id="dropZone" style="
                    position: relative; 
                    background: linear-gradient(145deg, rgba(30,30,30,0.7) 0%, rgba(10,10,10,0.9) 100%); 
                    backdrop-filter: blur(40px); 
                    border: 1px solid rgba(255,255,255,0.1); 
                    border-radius: 32px; 
                    padding: 5rem 2rem; 
                    max-width: 600px; 
                    width: 90%; 
                    box-shadow: 0 40px 80px rgba(0,0,0,0.8), inset 0 2px 20px rgba(255,255,255,0.05); 
                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    overflow: hidden;
                ">
                    <!-- Inner Dashed Border -->
                    <div style="position: absolute; inset: 16px; border: 2px dashed rgba(255,255,255,0.15); border-radius: 20px; pointer-events: none; transition: all 0.4s ease;" id="innerDash"></div>
                    
                    <!-- Spotlight Glow -->
                    <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 300px; height: 300px; background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%); pointer-events: none; filter: blur(20px);"></div>

                    <!-- Floating Icon -->
                    <div style="
                        width: 90px; height: 90px; 
                        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02)); 
                        border-radius: 50%; 
                        display: flex; align-items: center; justify-content: center; 
                        margin: 0 auto 2.5rem auto; 
                        border: 1px solid rgba(255,255,255,0.2); 
                        box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 2px 10px rgba(255,255,255,0.1);
                        animation: floatIcon 6s ease-in-out infinite;
                        position: relative;
                        z-index: 2;
                    ">
                        <i class="fa-solid fa-cloud-arrow-up" style="font-size: 2.2rem; color: #fff; filter: drop-shadow(0 0 10px rgba(255,255,255,0.5));"></i>
                    </div>
                    
                    <h3 style="font-size: 1.6rem; font-weight: 600; margin-bottom: 0.5rem; color: #fff; letter-spacing: -0.02em; position: relative; z-index: 2; text-shadow: 0 4px 20px rgba(0,0,0,0.5);">Upload your asset</h3>
                    <p style="color: rgba(255,255,255,0.5); font-size: 1rem; margin-bottom: 3rem; position: relative; z-index: 2;">Drag & drop any JPG, PNG, or WebP</p>
                    
                    <input type="file" id="fileInput" accept="image/*" style="display:none;">
                    <button class="draftly-btn-small draftly-btn-primary" style="height: 48px; padding: 0 3rem; font-size: 14px; position: relative; z-index: 2; box-shadow: 0 10px 20px rgba(255,255,255,0.1);" onclick="document.getElementById('fileInput').click()">
                        <i class="fa-solid fa-folder-open" style="margin-right: 8px;"></i> Browse Files
                    </button>
                </div>"""

html = html.replace(target, replacement)

# Add floatIcon keyframes if not present
if "floatIcon" not in html:
    style_target = "</style>"
    style_replacement = """
        @keyframes floatIcon {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-12px); }
            100% { transform: translateY(0px); }
        }
    </style>"""
    html = html.replace(style_target, style_replacement)

# Update dragover styles in JS to make the inner dash glow
js_target = """    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
    });"""

js_replacement = """    const innerDash = document.getElementById('innerDash');
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.transform = 'scale(1.02)';
        dropZone.style.borderColor = 'rgba(255,255,255,0.3)';
        if(innerDash) innerDash.style.borderColor = 'rgba(255,255,255,0.5)';
        if(innerDash) innerDash.style.background = 'rgba(255,255,255,0.02)';
    });

    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropZone.style.transform = 'scale(1)';
        dropZone.style.borderColor = 'rgba(255,255,255,0.1)';
        if(innerDash) innerDash.style.borderColor = 'rgba(255,255,255,0.15)';
        if(innerDash) innerDash.style.background = 'transparent';
    });
    
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.style.transform = 'scale(1)';
        dropZone.style.borderColor = 'rgba(255,255,255,0.1)';
        if(innerDash) innerDash.style.borderColor = 'rgba(255,255,255,0.15)';
        if(innerDash) innerDash.style.background = 'transparent';
        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            handleFileSelect({ target: fileInput });
        }
    });"""

with open("website/frontend/js/main.js", "r") as f:
    js = f.read()

# Only replace if the old dragover code is found
if "dropZone.classList.add('dragover');" in js:
    # First, let's remove the old drop event listener if it exists to avoid duplicates
    old_drop = """    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            handleFileSelect({ target: fileInput });
        }
    });"""
    js = js.replace(old_drop, "")
    js = js.replace(js_target, js_replacement)
    with open("website/frontend/js/main.js", "w") as f:
        f.write(js)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)

print("Dropzone upgraded significantly!")
