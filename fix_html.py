import glob

for filename in glob.glob("website/frontend/*.html"):
    with open(filename, "r") as f:
        html = f.read()

    html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js?v=6"></script>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>')
    html = html.replace('<script src="https://cdn.js?v=6"></script>\n    <script src="https://cdn.js?v=6"></script>', '<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/OBJLoader.js"></script>')
    html = html.replace('<script src="https://cdn.js?v=6"></script>', '<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/OBJLoader.js"></script>')

    # also check index and upload
    html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js?v=5"></script>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>')
    html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js?v=4"></script>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>')
    
    with open(filename, "w") as f:
        f.write(html)

print("Fixed HTML script tags!")
