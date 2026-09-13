import sys

with open("website/frontend/viewer.html", "r") as f:
    html = f.read()

bad_html = """        <div class="viewer-controls" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <button class="btn btn-primary" id="downloadObjBtn">Download 3D Object</button>
            <a href="upload.html" class="btn btn-secondary">Process Another</a>
        </div>"""

good_html = """        <div class="viewer-controls" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <button class="btn btn-primary" id="downloadObjBtn">Download 3D Object</button>
            <button class="btn btn-secondary" id="downloadDepthBtn">Download Depth Map</button>
            <a href="upload.html" class="btn btn-secondary">Process Another</a>
        </div>"""

if bad_html in html:
    html = html.replace(bad_html, good_html)

with open("website/frontend/viewer.html", "w") as f:
    f.write(html)

with open("website/frontend/js/viewer.js", "r") as f:
    js = f.read()

bad_js_360 = """                            if (is360) {
                                child.material = new THREE.MeshStandardMaterial({
                                    color: 0xffffff,
                                    roughness: 0.8,
                                    metalness: 0.1,
                                    side: THREE.DoubleSide
                                });
                            } else {
                                child.material = new THREE.MeshStandardMaterial({
                                    color: 0xffffff,
                                    roughness: 0.8,
                                    metalness: 0.1,
                                    side: THREE.DoubleSide
                                });
                            }"""

good_js_360 = """                            if (is360) {
                                // TripoSR outputs vertex colors in sRGB, but ThreeJS expects Linear
                                // We must convert them to Linear so the renderer can properly encode them
                                const colors = child.geometry.attributes.color;
                                if (colors) {
                                    const tempColor = new THREE.Color();
                                    for (let i = 0; i < colors.count; i++) {
                                        tempColor.setRGB(colors.getX(i), colors.getY(i), colors.getZ(i));
                                        tempColor.convertSRGBToLinear();
                                        colors.setXYZ(i, tempColor.r, tempColor.g, tempColor.b);
                                    }
                                }
                                child.material = new THREE.MeshBasicMaterial({
                                    vertexColors: true,
                                    side: THREE.DoubleSide
                                });
                            } else {
                                child.material = new THREE.MeshBasicMaterial({
                                    map: texture,
                                    side: THREE.DoubleSide
                                });
                            }"""

if bad_js_360 in js:
    js = js.replace(bad_js_360, good_js_360)

bad_js_fallback = """                const material = new THREE.MeshStandardMaterial({
                    color: 0xffffff,
                    displacementMap: depthMap,
                    displacementScale: 100.0,
                    side: THREE.DoubleSide,
                    roughness: 0.8,
                    metalness: 0.1
                });"""

good_js_fallback = """                const material = new THREE.MeshStandardMaterial({
                    map: texture,
                    displacementMap: depthMap,
                    displacementScale: 100.0,
                    side: THREE.DoubleSide,
                    roughness: 0.8,
                    metalness: 0.1
                });"""

if bad_js_fallback in js:
    js = js.replace(bad_js_fallback, good_js_fallback)

# Restore depth button listener
if "downloadDepthBtn" not in js:
    js = js.replace("});", """    const downloadDepthBtn = document.getElementById('downloadDepthBtn');
    if (downloadDepthBtn) {
        downloadDepthBtn.addEventListener('click', () => {
            if (depthUrl) {
                const a = document.createElement('a');
                a.href = depthUrl;
                a.download = 'depth_map.png';
                a.click();
            }
        });
    }
});""")

# Cache bust
html = html.replace("?v=2", "?v=3")
with open("website/frontend/viewer.html", "w") as f:
    f.write(html)

with open("website/frontend/js/viewer.js", "w") as f:
    f.write(js)

print("Reverted!")
