import glob

target = """<div class="draftly-header-right" style="display: flex; gap: 0.5rem;">"""
replacement = """<div class="draftly-header-right" style="display: flex; gap: 1rem;">"""

for filepath in glob.glob("website/frontend/*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    
    if target in html:
        html = html.replace(target, replacement)
        with open(filepath, "w") as f:
            f.write(html)
        print(f"Fixed gap in {filepath}")

