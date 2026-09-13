import sys

with open("website/frontend/js/viewer.js", "r") as f:
    lines = f.readlines()

# Find the start of the window resize event
resize_idx = -1
for i, line in enumerate(lines):
    if "window.addEventListener('resize'" in line:
        resize_idx = i
        break

if resize_idx != -1:
    new_lines = lines[:resize_idx]
    new_lines.extend([
        "    // Handle Window Resize\n",
        "    window.addEventListener('resize', () => {\n",
        "        camera.aspect = container.clientWidth / container.clientHeight;\n",
        "        camera.updateProjectionMatrix();\n",
        "        renderer.setSize(container.clientWidth, container.clientHeight);\n",
        "    });\n",
        "\n",
        "    // Animation Loop\n",
        "    function animate() {\n",
        "        requestAnimationFrame(animate);\n",
        "        controls.update();\n",
        "        renderer.render(scene, camera);\n",
        "    }\n",
        "    animate();\n",
        "});\n"
    ])
    with open("website/frontend/js/viewer.js", "w") as f:
        f.writelines(new_lines)
    print("Fixed viewer.js!")
else:
    print("Could not find resize event.")
