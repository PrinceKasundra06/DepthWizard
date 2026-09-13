import sys
import glob

target = """                <div class="draftly-logo">
                    <i class="fa-solid fa-cube"></i> DepthWizard Studio
                </div>"""

replacement = """                <a href="index.html" class="draftly-logo" style="text-decoration: none; cursor: pointer;">
                    <i class="fa-solid fa-cube"></i> DepthWizard Studio
                </a>"""

for filepath in glob.glob("website/frontend/*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    
    html = html.replace(target, replacement)
    
    with open(filepath, "w") as f:
        f.write(html)

print("Logo links fixed!")
