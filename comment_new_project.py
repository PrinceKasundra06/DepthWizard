import sys
import glob

target = '<a href="new.html" class="draftly-btn-small"><i class="fa-solid fa-plus"></i> New Project</a>'
replacement = '<!-- <a href="new.html" class="draftly-btn-small"><i class="fa-solid fa-plus"></i> New Project</a> -->'

for filepath in glob.glob("website/frontend/*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    
    html = html.replace(target, replacement)
    
    with open(filepath, "w") as f:
        f.write(html)

print("Commented out New Project buttons!")
