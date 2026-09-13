import sys

with open("website/frontend/js/viewer.js", "r") as f:
    js = f.read()

target = """    if (downloadObjBtn) {
        downloadObjBtn.addEventListener('click', () => {
            if (objUrl) {
                const a = document.createElement('a');
                a.href = objUrl;
                a.download = 'depthwizard_model.obj';
                a.click();
            }
        });
    }"""

replacement = """    if (downloadObjBtn) {
        downloadObjBtn.addEventListener('click', async () => {
            if (objUrl) {
                try {
                    downloadObjBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Preparing...';
                    downloadObjBtn.style.pointerEvents = 'none';
                    
                    const response = await fetch(objUrl);
                    const blob = await response.blob();
                    
                    // Force the blob to be text/plain so the browser doesn't try to zip it or guess its type
                    const safeBlob = new Blob([blob], { type: 'text/plain' });
                    const safeUrl = URL.createObjectURL(safeBlob);
                    
                    const a = document.createElement('a');
                    a.href = safeUrl;
                    a.download = 'depthwizard_model.obj';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    
                    URL.revokeObjectURL(safeUrl);
                    
                    downloadObjBtn.innerHTML = '<i class="fa-solid fa-download"></i> Export OBJ';
                    downloadObjBtn.style.pointerEvents = 'all';
                } catch(e) {
                    console.error("Export failed:", e);
                    downloadObjBtn.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Error';
                }
            }
        });
    }"""

if "safeBlob" not in js:
    js = js.replace(target, replacement)
    with open("website/frontend/js/viewer.js", "w") as f:
        f.write(js)
    print("JS export fixed!")
else:
    print("JS export already fixed!")
