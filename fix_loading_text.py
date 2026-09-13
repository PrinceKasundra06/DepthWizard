import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

bad_loader = """        <div class="loading-overlay" id="loadingOverlay">
            <div class="orb"></div>
            <div class="loading-text">Processing Neural Depth...</div>
        </div>"""

good_loader = """        <div class="loading-overlay" id="loadingOverlay">
            <div class="orb"></div>
            <div class="loading-text" id="loadingText">Processing Neural Depth...</div>
        </div>"""

html = html.replace(bad_loader, good_loader)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)
    
print("Fixed loader ID!")
