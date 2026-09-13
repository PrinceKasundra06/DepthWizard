import trimesh
import numpy as np

mesh = trimesh.creation.box()
mesh.visual.vertex_colors = np.random.randint(0, 255, (len(mesh.vertices), 4))
mesh.export('test_box.obj')

with open('test_box.obj', 'r') as f:
    lines = f.readlines()
    for line in lines[:10]:
        print(line.strip())
