import sys

with open("website/frontend/js/viewer.js", "r") as f:
    code = f.read()

bad_logic = """                            if (is360) {
                                child.material = new THREE.MeshBasicMaterial({
                                    vertexColors: true,
                                    side: THREE.DoubleSide
                                });
                            }"""

good_logic = """                            if (is360) {
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
                            }"""

if bad_logic in code:
    code = code.replace(bad_logic, good_logic)

with open("website/frontend/js/viewer.js", "w") as f:
    f.write(code)
    
print("Patched vertex colors!")
