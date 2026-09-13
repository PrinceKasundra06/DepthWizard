import sys

with open("website/frontend/js/viewer.js", "r") as f:
    code = f.read()

bad_buttons = """    const downloadBtns = document.querySelectorAll('.viewer-controls .btn');
    if (downloadBtns.length >= 3) {
        downloadBtns[0].addEventListener('click', () => {
            if (objUrl) {
                const a = document.createElement('a');
                a.href = objUrl;
                a.download = 'model.obj';
                a.click();
            }
        });
        downloadBtns[1].addEventListener('click', () => {
            if (depthUrl) {
                const a = document.createElement('a');
                a.href = depthUrl;
                a.download = 'depth_map.png';
                a.click();
            }
        });
        downloadBtns[2].addEventListener('click', () => {
            if (heightUrl) {
                const a = document.createElement('a');
                a.href = heightUrl;
                a.download = 'height_map.png';
                a.click();
            }
        });
    }"""

good_buttons = """    const downloadObjBtn = document.getElementById('downloadObjBtn');
    if (downloadObjBtn) {
        downloadObjBtn.addEventListener('click', () => {
            if (objUrl) {
                const a = document.createElement('a');
                a.href = objUrl;
                a.download = 'model.obj';
                a.click();
            }
        });
    }
    
    const downloadDepthBtn = document.getElementById('downloadDepthBtn');
    if (downloadDepthBtn) {
        downloadDepthBtn.addEventListener('click', () => {
            if (depthUrl) {
                const a = document.createElement('a');
                a.href = depthUrl;
                a.download = 'depth_map.png';
                a.click();
            }
        });
    }"""

if bad_buttons in code:
    code = code.replace(bad_buttons, good_buttons)

with open("website/frontend/js/viewer.js", "w") as f:
    f.write(code)
    
print("Patched viewer.js")
