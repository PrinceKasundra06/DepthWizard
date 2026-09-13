import sys

with open("website/frontend/index.html", "r") as f:
    html = f.read()

bad_viewport = """        <main class="draftly-viewport" style="background: radial-gradient(circle at center, #111 0%, #000 100%);">
            <canvas id="bg-canvas" style="position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%;"></canvas>
            
            <div style="text-align: center; padding: 2rem; position: relative; z-index: 10; pointer-events: none;">"""

good_viewport = """        <main class="draftly-viewport" style="background: #000;">
            <canvas id="bg-canvas" style="position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%;"></canvas>
            
            <!-- Dark gradient mask behind text for perfect legibility -->
            <div style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0) 60%); z-index: 5; pointer-events: none;"></div>
            
            <div style="text-align: center; padding: 2rem; position: relative; z-index: 10; pointer-events: none; text-shadow: 0 4px 24px rgba(0,0,0,1);">"""

html = html.replace(bad_viewport, good_viewport)

with open("website/frontend/index.html", "w") as f:
    f.write(html)

# Also let's lower the particle opacity slightly in main.js
with open("website/frontend/js/main.js", "r") as f:
    js = f.read()
    
js = js.replace("gl_FragColor = vec4( color, 0.4 );", "gl_FragColor = vec4( color, 0.25 );")

with open("website/frontend/js/main.js", "w") as f:
    f.write(js)
    
print("Fixed text visibility!")
