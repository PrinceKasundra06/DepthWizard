import sys

# 1. UPDATE HTML
with open("website/frontend/viewer.html", "r") as f:
    html = f.read()

bad_sliders = """                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Roughness</span>
                        <input type="range" min="0" max="100" value="80" class="slider" disabled style="width: 100px; opacity: 0.5;">
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Metalness</span>
                        <input type="range" min="0" max="100" value="10" class="slider" disabled style="width: 100px; opacity: 0.5;">
                    </div>"""

good_sliders = """                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Roughness</span>
                        <input type="range" min="0" max="100" value="80" id="slider-roughness" style="width: 100px; accent-color: #ffffff; cursor: pointer;">
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Metalness</span>
                        <input type="range" min="0" max="100" value="10" id="slider-metalness" style="width: 100px; accent-color: #ffffff; cursor: pointer;">
                    </div>"""

html = html.replace(bad_sliders, good_sliders)

bad_lighting = """                        <button class="draftly-btn-small" style="justify-content: center; background: rgba(255,255,255,0.1); color: #fff !important; border-color: rgba(255,255,255,0.2);">Studio</button>
                        <button class="draftly-btn-small" style="justify-content: center; opacity: 0.5; cursor: not-allowed;">Dramatic</button>
                        <button class="draftly-btn-small" style="justify-content: center; opacity: 0.5; cursor: not-allowed;">Sunset</button>
                        <button class="draftly-btn-small" style="justify-content: center; opacity: 0.5; cursor: not-allowed;">Neon</button>"""

good_lighting = """                        <button id="btn-light-studio" class="draftly-btn-small light-btn" style="justify-content: center; background: rgba(255,255,255,0.1); color: #fff !important; border-color: rgba(255,255,255,0.2);">Studio</button>
                        <button id="btn-light-dramatic" class="draftly-btn-small light-btn" style="justify-content: center;">Dramatic</button>
                        <button id="btn-light-sunset" class="draftly-btn-small light-btn" style="justify-content: center;">Sunset</button>
                        <button id="btn-light-neon" class="draftly-btn-small light-btn" style="justify-content: center;">Neon</button>"""

html = html.replace(bad_lighting, good_lighting)

with open("website/frontend/viewer.html", "w") as f:
    f.write(html)


# 2. UPDATE JS
with open("website/frontend/js/viewer.js", "r") as f:
    js = f.read()

# Make the material accessible globally
js = js.replace("let mainObject = null;", "let mainObject = null;\n    let mainMaterial = null;")

bad_material = """                    // Pure White Clay Material
                    child.material = new THREE.MeshStandardMaterial({
                        color: 0xffffff,
                        roughness: 0.8,
                        metalness: 0.1,
                        side: THREE.DoubleSide
                    });"""

good_material = """                    // Pure White Clay Material
                    mainMaterial = new THREE.MeshStandardMaterial({
                        color: 0xffffff,
                        roughness: document.getElementById('slider-roughness') ? document.getElementById('slider-roughness').value / 100 : 0.8,
                        metalness: document.getElementById('slider-metalness') ? document.getElementById('slider-metalness').value / 100 : 0.1,
                        side: THREE.DoubleSide
                    });
                    child.material = mainMaterial;"""

js = js.replace(bad_material, good_material)

# Add event listeners for sliders and lights at the end of the file before `window.addEventListener('resize'`
hud_insertion_point = "    // Handle Window Resize"

new_listeners = """    // --- Sidebar Controls ---
    const sliderRoughness = document.getElementById('slider-roughness');
    const sliderMetalness = document.getElementById('slider-metalness');
    
    if (sliderRoughness) {
        sliderRoughness.addEventListener('input', (e) => {
            if (mainMaterial) mainMaterial.roughness = e.target.value / 100;
        });
    }
    
    if (sliderMetalness) {
        sliderMetalness.addEventListener('input', (e) => {
            if (mainMaterial) mainMaterial.metalness = e.target.value / 100;
        });
    }
    
    // Lighting Environments
    const lightBtns = document.querySelectorAll('.light-btn');
    
    function resetLightBtns() {
        lightBtns.forEach(btn => {
            btn.style.background = 'rgba(255,255,255,0.04)';
            btn.style.borderColor = 'rgba(255,255,255,0.1)';
        });
    }
    
    function setActiveLightBtn(id) {
        resetLightBtns();
        const btn = document.getElementById(id);
        if (btn) {
            btn.style.background = 'rgba(255,255,255,0.1)';
            btn.style.borderColor = 'rgba(255,255,255,0.2)';
        }
    }
    
    document.getElementById('btn-light-studio')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-studio');
        ambientLight.color.setHex(0xffffff);
        ambientLight.intensity = 0.5;
        dirLight1.color.setHex(0xffffff);
        dirLight1.intensity = 1.2;
        dirLight1.position.set(10, 20, 15);
        dirLight2.color.setHex(0xffffff);
        dirLight2.intensity = 0.5;
    });
    
    document.getElementById('btn-light-dramatic')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-dramatic');
        ambientLight.color.setHex(0x444444);
        ambientLight.intensity = 0.2;
        dirLight1.color.setHex(0xffffff);
        dirLight1.intensity = 2.0;
        dirLight1.position.set(15, 5, 0); // Side light
        dirLight2.intensity = 0.0;
    });
    
    document.getElementById('btn-light-sunset')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-sunset');
        ambientLight.color.setHex(0xffaa55);
        ambientLight.intensity = 0.4;
        dirLight1.color.setHex(0xff6600);
        dirLight1.intensity = 1.5;
        dirLight1.position.set(-20, 5, 20); // Low angle sunset
        dirLight2.color.setHex(0x440088); // Purple fill
        dirLight2.intensity = 0.8;
        dirLight2.position.set(20, 10, -10);
    });
    
    document.getElementById('btn-light-neon')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-neon');
        ambientLight.color.setHex(0x111111);
        ambientLight.intensity = 0.1;
        dirLight1.color.setHex(0x00ffff); // Cyan
        dirLight1.intensity = 2.5;
        dirLight1.position.set(10, 0, 10);
        dirLight2.color.setHex(0xff00ff); // Magenta
        dirLight2.intensity = 2.5;
        dirLight2.position.set(-10, 5, -10);
    });

    """

js = js.replace(hud_insertion_point, new_listeners + hud_insertion_point)

with open("website/frontend/js/viewer.js", "w") as f:
    f.write(js)

print("Controls are now live!")
