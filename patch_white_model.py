import sys

with open("website/frontend/js/viewer.js", "r") as f:
    code = f.read()

# Replace the 360 material
bad_logic_360 = """                            if (is360) {
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

good_logic_360 = """                            if (is360) {
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

if bad_logic_360 in code:
    code = code.replace(bad_logic_360, good_logic_360)

# Replace the 2.5D fallback material
bad_logic_fallback = """                const material = new THREE.MeshStandardMaterial({
                    map: texture,
                    displacementMap: depthMap,
                    displacementScale: 100.0,
                    side: THREE.DoubleSide,
                    roughness: 0.8,
                    metalness: 0.1
                });"""

good_logic_fallback = """                const material = new THREE.MeshStandardMaterial({
                    color: 0xffffff,
                    displacementMap: depthMap,
                    displacementScale: 100.0,
                    side: THREE.DoubleSide,
                    roughness: 0.8,
                    metalness: 0.1
                });"""

if bad_logic_fallback in code:
    code = code.replace(bad_logic_fallback, good_logic_fallback)

with open("website/frontend/js/viewer.js", "w") as f:
    f.write(code)
    
print("Patched to pure white clay models!")
