import sys

# For index.html
with open("website/frontend/index.html", "r") as f:
    html = f.read()
target = """        <div class="draftly-header-right">
            <a href="upload.html" class="draftly-btn-small"><i class="fa-solid fa-plus"></i> New Project</a>
            <a href="upload.html" class="draftly-btn-small draftly-btn-primary"><i class="fa-solid fa-rocket"></i> Launch</a>
        </div>"""
replacement = """        <div class="draftly-header-right" style="display: flex; gap: 0.5rem;">
            <a href="about.html" class="draftly-btn-small" style="background: transparent; border: 1px solid transparent;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='transparent'"><i class="fa-solid fa-circle-info" style="margin-right: 6px;"></i> About Us</a>
            <a href="upload.html" class="draftly-btn-small"><i class="fa-solid fa-plus"></i> New Project</a>
            <a href="upload.html" class="draftly-btn-small draftly-btn-primary"><i class="fa-solid fa-rocket"></i> Launch</a>
        </div>"""
with open("website/frontend/index.html", "w") as f:
    f.write(html.replace(target, replacement))

# For upload.html
with open("website/frontend/upload.html", "r") as f:
    html = f.read()
target = """        <div class="draftly-header-right">
            <a href="index.html" class="draftly-btn-small"><i class="fa-solid fa-house"></i> Dashboard</a>
        </div>"""
replacement = """        <div class="draftly-header-right" style="display: flex; gap: 0.5rem;">
            <a href="about.html" class="draftly-btn-small" style="background: transparent; border: 1px solid transparent;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='transparent'"><i class="fa-solid fa-circle-info" style="margin-right: 6px;"></i> About Us</a>
            <a href="index.html" class="draftly-btn-small"><i class="fa-solid fa-house"></i> Dashboard</a>
        </div>"""
with open("website/frontend/upload.html", "w") as f:
    f.write(html.replace(target, replacement))

# For viewer.html
with open("website/frontend/viewer.html", "r") as f:
    html = f.read()
target = """        <div class="draftly-header-right">
            <button class="draftly-btn-small" onclick="window.location='upload.html'"><i class="fa-solid fa-plus"></i> New</button>
            <button class="draftly-btn-small draftly-btn-primary" id="downloadObjBtn"><i class="fa-solid fa-download"></i> Export OBJ</button>
        </div>"""
replacement = """        <div class="draftly-header-right" style="display: flex; gap: 0.5rem;">
            <button class="draftly-btn-small" style="background: transparent; border: 1px solid transparent;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='transparent'" onclick="window.location='about.html'"><i class="fa-solid fa-circle-info" style="margin-right: 6px;"></i> About Us</button>
            <button class="draftly-btn-small" onclick="window.location='upload.html'"><i class="fa-solid fa-plus"></i> New</button>
            <button class="draftly-btn-small draftly-btn-primary" id="downloadObjBtn"><i class="fa-solid fa-download"></i> Export OBJ</button>
        </div>"""
with open("website/frontend/viewer.html", "w") as f:
    f.write(html.replace(target, replacement))

print("Header updated for real this time!")
