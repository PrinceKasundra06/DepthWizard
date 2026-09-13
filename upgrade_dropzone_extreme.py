import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

# Extract the block
target_start = '<!-- Premium Dropzone -->'
target_end = '<!-- End Premium Dropzone -->'

# Wait, I didn't add <!-- End Premium Dropzone --> before.
# I need to find the specific dropzone HTML.
target = """                <!-- Premium Dropzone -->
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

replacement = """                <!-- Premium Dropzone -->
                <div class="upload-box interactive-card" id="dropZone" style="
                    position: relative; 
                    background: linear-gradient(145deg, rgba(15,15,18,0.7) 0%, rgba(5,5,8,0.9) 100%); 
                    backdrop-filter: blur(40px); 
                    border: 1px solid rgba(255,255,255,0.1); 
                    border-radius: 32px; 
                    padding: 5rem 2rem; 
                    max-width: 600px; 
                    width: 90%; 
                    box-shadow: 0 40px 80px rgba(0,0,0,0.8), inset 0 2px 20px rgba(255,255,255,0.05); 
                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    overflow: hidden;
                    cursor: pointer;
                " onclick="document.getElementById('fileInput').click()">
                    
                    <!-- Animated Blueprint Grid inside card -->
                    <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 20px 20px; background-position: center center; opacity: 0.5; pointer-events: none; z-index: 0; mask-image: radial-gradient(circle at center, black 0%, transparent 80%); -webkit-mask-image: radial-gradient(circle at center, black 0%, transparent 80%);"></div>

                    <!-- Animated SVG Marching Ants Border -->
                    <svg style="position: absolute; inset: 12px; width: calc(100% - 24px); height: calc(100% - 24px); pointer-events: none; z-index: 1;" xmlns="http://www.w3.org/2000/svg">
                        <rect id="svgDash" width="100%" height="100%" rx="20" ry="20" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-dasharray="10 10" style="transition: all 0.4s ease; animation: march 20s linear infinite;" />
                    </svg>
                    
                    <!-- Dynamic Glowing Core -->
                    <div id="dropGlow" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 0px; height: 0px; background: radial-gradient(circle, rgba(0, 150, 255, 0.4) 0%, transparent 70%); pointer-events: none; filter: blur(30px); transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); z-index: 1; opacity: 0;"></div>

                    <!-- Holographic Floating Icon -->
                    <div id="dropIconContainer" style="
                        width: 90px; height: 90px; 
                        background: rgba(255,255,255,0.02); 
                        border-radius: 50%; 
                        display: flex; align-items: center; justify-content: center; 
                        margin: 0 auto 2.5rem auto; 
                        border: 1px solid rgba(255,255,255,0.1); 
                        box-shadow: 0 0 30px rgba(0,0,0,0.5), inset 0 0 20px rgba(255,255,255,0.05);
                        animation: floatIcon 4s ease-in-out infinite;
                        position: relative;
                        z-index: 2;
                        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    ">
                        <!-- Orbiting Ring -->
                        <div style="position: absolute; inset: -10px; border-radius: 50%; border: 1px dashed rgba(255,255,255,0.2); border-left-color: rgba(255,255,255,0.8); animation: spinOrb 4s linear infinite; pointer-events: none;"></div>
                        
                        <i id="dropIcon" class="fa-solid fa-cube" style="font-size: 2.5rem; color: #fff; filter: drop-shadow(0 0 15px rgba(255,255,255,0.6)); transition: all 0.3s ease;"></i>
                    </div>
                    
                    <h3 style="font-size: 1.8rem; font-weight: 500; margin-bottom: 0.5rem; color: #fff; letter-spacing: -0.04em; position: relative; z-index: 2; text-shadow: 0 4px 20px rgba(0,0,0,0.8);">Initiate Generation</h3>
                    <p style="color: rgba(255,255,255,0.5); font-size: 0.95rem; margin-bottom: 3rem; position: relative; z-index: 2;">Click or drop an image into the neural matrix.</p>
                    
                    <input type="file" id="fileInput" accept="image/*" style="display:none;">
                    
                    <!-- Shiny Animated Button -->
                    <button class="draftly-btn-small draftly-btn-primary shiny-btn" style="height: 48px; padding: 0 3rem; font-size: 14px; position: relative; z-index: 2; box-shadow: 0 10px 20px rgba(255,255,255,0.1); pointer-events: none;">
                        <i class="fa-solid fa-bolt" style="margin-right: 8px;"></i> Select File
                    </button>
                </div>"""

html = html.replace(target, replacement)

# Add CSS for shiny button and marching ants
if "shiny-btn" not in html:
    style_target = "</style>"
    style_replacement = """
        @keyframes march {
            to { stroke-dashoffset: -200; }
        }
        .shiny-btn {
            position: relative;
            overflow: hidden;
        }
        .shiny-btn::before {
            content: '';
            position: absolute;
            top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent);
            transform: skewX(-20deg);
            animation: shine 3s infinite;
        }
        @keyframes shine {
            0% { left: -100%; }
            20% { left: 200%; }
            100% { left: 200%; }
        }
    </style>"""
    html = html.replace(style_target, style_replacement)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)


# Update JS logic for drag over glowing!
js_target = """    const innerDash = document.getElementById('innerDash');
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

js_replacement = """    const svgDash = document.getElementById('svgDash');
    const dropGlow = document.getElementById('dropGlow');
    const dropIconContainer = document.getElementById('dropIconContainer');
    const dropIcon = document.getElementById('dropIcon');

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.transform = 'scale(1.03)';
        dropZone.style.borderColor = 'rgba(0, 150, 255, 0.5)';
        dropZone.style.boxShadow = '0 50px 100px rgba(0,0,0,0.9), inset 0 0 40px rgba(0, 150, 255, 0.2)';
        
        if(svgDash) {
            svgDash.style.stroke = 'rgba(0, 150, 255, 0.8)';
            svgDash.style.animationDuration = '2s'; // speed up marching ants
        }
        if(dropGlow) {
            dropGlow.style.width = '100%';
            dropGlow.style.height = '100%';
            dropGlow.style.opacity = '1';
        }
        if(dropIconContainer) {
            dropIconContainer.style.background = 'rgba(0, 150, 255, 0.2)';
            dropIconContainer.style.borderColor = 'rgba(0, 150, 255, 0.8)';
        }
        if(dropIcon) {
            dropIcon.style.color = '#ffffff';
            dropIcon.style.filter = 'drop-shadow(0 0 20px rgba(255,255,255,1))';
            dropIcon.style.transform = 'scale(1.2)';
        }
    });

    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropZone.style.transform = 'scale(1)';
        dropZone.style.borderColor = 'rgba(255,255,255,0.1)';
        dropZone.style.boxShadow = '0 40px 80px rgba(0,0,0,0.8), inset 0 2px 20px rgba(255,255,255,0.05)';
        
        if(svgDash) {
            svgDash.style.stroke = 'rgba(255,255,255,0.2)';
            svgDash.style.animationDuration = '20s'; // normal speed
        }
        if(dropGlow) {
            dropGlow.style.width = '0px';
            dropGlow.style.height = '0px';
            dropGlow.style.opacity = '0';
        }
        if(dropIconContainer) {
            dropIconContainer.style.background = 'rgba(255,255,255,0.02)';
            dropIconContainer.style.borderColor = 'rgba(255,255,255,0.1)';
        }
        if(dropIcon) {
            dropIcon.style.color = '#fff';
            dropIcon.style.filter = 'drop-shadow(0 0 15px rgba(255,255,255,0.6))';
            dropIcon.style.transform = 'scale(1)';
        }
    });
    
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        // Trigger dragleave physics reset
        dropZone.dispatchEvent(new Event('dragleave'));
        
        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            handleFileSelect({ target: fileInput });
        }
    });"""

with open("website/frontend/js/main.js", "r") as f:
    js = f.read()

if "const innerDash = document.getElementById('innerDash');" in js:
    js = js.replace(js_target, js_replacement)
    with open("website/frontend/js/main.js", "w") as f:
        f.write(js)

print("Dropzone pushed to extreme premium!")
