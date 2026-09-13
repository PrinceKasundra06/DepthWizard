import sys

with open("website/backend/main.py", "r") as f:
    code = f.read()

target = "meshes = tsr_model.extract_mesh(scene_codes, has_vertex_color=True, resolution=192)[0]"
replacement = "meshes = tsr_model.extract_mesh(scene_codes, has_vertex_color=False, resolution=192)[0]"

if target in code:
    code = code.replace(target, replacement)
    with open("website/backend/main.py", "w") as f:
        f.write(code)
    print("Disabled vertex colors in backend!")
else:
    print("Could not find target!")
