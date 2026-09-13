import sys

with open("website/frontend/index.html", "r") as f:
    html = f.read()

target = """<div style="min-height: 80vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-bottom: 6rem; text-shadow: 0 4px 24px rgba(0,0,0,1);">"""
replacement = """<div style="min-height: 80vh; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding-top: 25vh; text-align: center; margin-bottom: 6rem; text-shadow: 0 4px 24px rgba(0,0,0,1);">"""

if target in html:
    html = html.replace(target, replacement)
    with open("website/frontend/index.html", "w") as f:
        f.write(html)
    print("Fixed index!")
else:
    print("Could not find target in index.html!")

