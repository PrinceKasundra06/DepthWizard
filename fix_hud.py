import sys

with open("website/frontend/viewer.html", "r") as f:
    html = f.read()

target = """<!-- Viewport HUD Overlay -->
            <div style="position: absolute; top: 16px; left: 50%; transform: translateX(-50%); background: rgba(10,10,10,0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.1); border-radius: 999px; padding: 6px; display: flex; gap: 4px; z-index: 10;">"""

replacement = """<!-- Viewport HUD Overlay -->
            <div style="position: absolute; top: 100px; left: 50%; transform: translateX(-50%); background: rgba(10,10,10,0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.1); border-radius: 999px; padding: 6px; display: flex; gap: 4px; z-index: 10;">"""

if target in html:
    html = html.replace(target, replacement)
    with open("website/frontend/viewer.html", "w") as f:
        f.write(html)
    print("HUD overlay moved down!")
else:
    print("Could not find HUD target!")

