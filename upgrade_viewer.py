import sys

# 1. Update viewer.html
with open("website/frontend/viewer.html", "r") as f:
    html = f.read()

bad_sidebar = """            <div class="draftly-sidebar-content">
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 1rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.6); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Scene Information</div>
                    <p style="font-size: 13px; color: #fff; margin: 0 0 1rem 0;" id="heightDisplay">Calculated Max Height: -- meters</p>
                    
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.6); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Material</div>
                    <div style="display: flex; gap: 0.5rem; align-items: center; font-size: 13px;">
                        <div style="width: 16px; height: 16px; border-radius: 50%; background: #ffffff; border: 1px solid rgba(255,255,255,0.2);"></div>
                        White Clay (Standard)
                    </div>
                </div>
            </div>"""

good_sidebar = """            <div class="draftly-sidebar-content">
                
                <!-- Mesh Properties -->
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.25rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Mesh Data</div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);"><i class="fa-solid fa-circle-nodes" style="margin-right: 6px; opacity: 0.5;"></i> Vertices</span>
                        <span style="font-size: 12px; color: #fff; font-family: monospace;" id="stat-vertices">--</span>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);"><i class="fa-solid fa-draw-polygon" style="margin-right: 6px; opacity: 0.5;"></i> Faces (Triangles)</span>
                        <span style="font-size: 12px; color: #fff; font-family: monospace;" id="stat-faces">--</span>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);"><i class="fa-solid fa-ruler-vertical" style="margin-right: 6px; opacity: 0.5;"></i> Bounding Height</span>
                        <span style="font-size: 12px; color: #00ffcc; font-family: monospace;" id="heightDisplay">--</span>
                    </div>
                    
                    <div style="width: 100%; height: 1px; background: rgba(255,255,255,0.1); margin: 1rem 0;"></div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Geometry Topology</span>
                        <span style="font-size: 10px; color: rgba(0,0,0,1); background: #ffffff; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Marching Cubes</span>
                    </div>
                </div>

                <!-- Material & Shading -->
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.25rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Shading Engine</div>
                    
                    <div style="display: flex; gap: 0.5rem; align-items: center; font-size: 12px; margin-bottom: 1rem; color: #fff;">
                        <div style="width: 16px; height: 16px; border-radius: 50%; background: #ffffff; border: 1px solid rgba(255,255,255,0.5); box-shadow: 0 0 10px rgba(255,255,255,0.2);"></div>
                        White Clay (Standard)
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Roughness</span>
                        <input type="range" min="0" max="100" value="80" class="slider" disabled style="width: 100px; opacity: 0.5;">
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Metalness</span>
                        <input type="range" min="0" max="100" value="10" class="slider" disabled style="width: 100px; opacity: 0.5;">
                    </div>
                </div>

                <!-- Lighting Environments -->
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.25rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Lighting Rig</div>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                        <button class="draftly-btn-small" style="justify-content: center; background: rgba(255,255,255,0.1); color: #fff !important; border-color: rgba(255,255,255,0.2);">Studio</button>
                        <button class="draftly-btn-small" style="justify-content: center; opacity: 0.5; cursor: not-allowed;">Dramatic</button>
                        <button class="draftly-btn-small" style="justify-content: center; opacity: 0.5; cursor: not-allowed;">Sunset</button>
                        <button class="draftly-btn-small" style="justify-content: center; opacity: 0.5; cursor: not-allowed;">Neon</button>
                    </div>
                </div>

                <!-- Export Settings -->
                <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.25rem; margin-bottom: 2rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Export Config</div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Format</span>
                        <span style="font-size: 11px; color: #fff; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px;">.OBJ (Wavefront)</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Up Axis</span>
                        <span style="font-size: 11px; color: #fff; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px;">+Y</span>
                    </div>
                </div>

            </div>"""

html = html.replace(bad_sidebar, good_sidebar)

# Add Viewport HUD tools to viewer.html
bad_viewport = """        <main class="draftly-viewport" id="canvas-container">
            <!-- 3D Canvas will be injected here -->
        </main>"""

good_viewport = """        <main class="draftly-viewport" id="canvas-container" style="position: relative;">
            <!-- 3D Canvas will be injected here -->
            
            <!-- Viewport HUD Overlay -->
            <div style="position: absolute; top: 16px; left: 50%; transform: translateX(-50%); background: rgba(10,10,10,0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.1); border-radius: 999px; padding: 6px; display: flex; gap: 4px; z-index: 10;">
                <button id="btn-wireframe" class="draftly-btn-small" style="height: 32px; padding: 0 1rem; border-radius: 999px; background: transparent; border: none; color: #fff;"><i class="fa-solid fa-border-all" style="margin-right: 6px;"></i> Wireframe</button>
                <div style="width: 1px; background: rgba(255,255,255,0.1); margin: 4px 2px;"></div>
                <button id="btn-autorotate" class="draftly-btn-small" style="height: 32px; padding: 0 1rem; border-radius: 999px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.1); color: #fff !important;"><i class="fa-solid fa-arrows-rotate" style="margin-right: 6px;"></i> Auto-Spin</button>
                <div style="width: 1px; background: rgba(255,255,255,0.1); margin: 4px 2px;"></div>
                <button id="btn-reset-cam" class="draftly-btn-small" style="height: 32px; padding: 0 1rem; border-radius: 999px; background: transparent; border: none; color: #fff;"><i class="fa-solid fa-video" style="margin-right: 6px;"></i> Reset Cam</button>
            </div>
            
            <!-- Axis Legend -->
            <div style="position: absolute; bottom: 16px; left: 16px; z-index: 10; pointer-events: none;">
                <div style="font-size: 10px; color: rgba(255,255,255,0.5); font-family: monospace; letter-spacing: 0.1em;">DEPTHWIZARD ENGINE v2.0</div>
            </div>
        </main>"""

html = html.replace(bad_viewport, good_viewport)

with open("website/frontend/viewer.html", "w") as f:
    f.write(html)

print("Viewer HTML upgraded!")

# 2. Update viewer.js to calculate mesh data, add grid/axes, and hook up HUD buttons
with open("website/frontend/js/viewer.js", "r") as f:
    js = f.read()

bad_js_scene = """    const dirLight2 = new THREE.DirectionalLight(0xffffff, 0.5);
    dirLight2.position.set(-10, -10, -15);
    scene.add(dirLight2);

    let mainObject = null;"""

good_js_scene = """    const dirLight2 = new THREE.DirectionalLight(0xffffff, 0.5);
    dirLight2.position.set(-10, -10, -15);
    scene.add(dirLight2);
    
    // Add professional viewport grid and axes
    const gridHelper = new THREE.GridHelper(10, 20, 0x444444, 0x222222);
    gridHelper.position.y = -1.5; // Offset below object
    scene.add(gridHelper);
    
    const axesHelper = new THREE.AxesHelper(2);
    axesHelper.position.y = -1.5;
    scene.add(axesHelper);

    let mainObject = null;"""

js = js.replace(bad_js_scene, good_js_scene)

bad_js_loader = """                    const hStat = document.getElementById('heightDisplay');
                    if (hStat) hStat.innerText = 'Calculated Max Height: ' + (size.y * 1.5).toFixed(2) + ' m';
                }
            });"""

good_js_loader = """                    const hStat = document.getElementById('heightDisplay');
                    if (hStat) hStat.innerText = (size.y * 1.5).toFixed(2) + ' m';
                    
                    // Extract exact vertex and face counts from the loaded geometry!
                    const vertexCount = child.geometry.attributes.position.count;
                    // Faces = total indices / 3 (if indexed) or vertices / 3 (if unindexed)
                    const faceCount = child.geometry.index ? child.geometry.index.count / 3 : vertexCount / 3;
                    
                    const vStat = document.getElementById('stat-vertices');
                    if (vStat) vStat.innerText = vertexCount.toLocaleString();
                    
                    const fStat = document.getElementById('stat-faces');
                    if (fStat) fStat.innerText = faceCount.toLocaleString();
                }
            });"""

js = js.replace(bad_js_loader, good_js_loader)

bad_js_hud = """    // Handle Window Resize
    window.addEventListener('resize', () => {"""

good_js_hud = """    // Wire up HUD Buttons
    const btnWireframe = document.getElementById('btn-wireframe');
    let isWireframe = false;
    if (btnWireframe) {
        btnWireframe.addEventListener('click', () => {
            isWireframe = !isWireframe;
            btnWireframe.style.background = isWireframe ? 'rgba(255,255,255,0.1)' : 'transparent';
            if (mainObject) {
                mainObject.traverse((child) => {
                    if (child.isMesh) child.material.wireframe = isWireframe;
                });
            }
        });
    }
    
    const btnAutoRotate = document.getElementById('btn-autorotate');
    if (btnAutoRotate) {
        btnAutoRotate.addEventListener('click', () => {
            controls.autoRotate = !controls.autoRotate;
            btnAutoRotate.style.background = controls.autoRotate ? 'rgba(255,255,255,0.1)' : 'transparent';
        });
    }
    
    const btnResetCam = document.getElementById('btn-reset-cam');
    if (btnResetCam) {
        btnResetCam.addEventListener('click', () => {
            controls.reset();
            camera.position.set(0, 2, 5);
        });
    }

    // Handle Window Resize
    window.addEventListener('resize', () => {"""

js = js.replace(bad_js_hud, good_js_hud)

with open("website/frontend/js/viewer.js", "w") as f:
    f.write(js)

print("Viewer JS upgraded!")
