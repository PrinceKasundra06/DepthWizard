import sys

with open("website/frontend/index.html", "r") as f:
    html = f.read()

marquee_html = """        <div class="features">
            <div class="feature-card tilt-card">
                <h3>🔍 AI Subject Extraction</h3>
                <p>Advanced neural networks instantly isolate your subject from the background, ensuring a clean 3D object.</p>
            </div>
            <div class="feature-card tilt-card">
                <h3>🧊 True 360° Hallucination</h3>
                <p>Not just a flat 2.5D plane. We use TripoSR to intelligently synthesize the back of the object from a single front-facing photo.</p>
            </div>
            <div class="feature-card tilt-card">
                <h3>🖥️ Pro 3D Viewer</h3>
                <p>Inspect your white clay meshes in a studio lighting environment with wireframe analysis and auto-rotation.</p>
            </div>
        </div>

        <div class="marquee-container">
            <div class="marquee-content">
                <span>CINEMATIC 3D</span> <span>&bull;</span> 
                <span>AI GENERATION</span> <span>&bull;</span> 
                <span>BACKGROUND REMOVAL</span> <span>&bull;</span> 
                <span>MESH EXTRACTION</span> <span>&bull;</span> 
                <span>FROSTED GLASS UI</span> <span>&bull;</span> 
                <span>CINEMATIC 3D</span> <span>&bull;</span> 
                <span>AI GENERATION</span> <span>&bull;</span> 
                <span>BACKGROUND REMOVAL</span> <span>&bull;</span> 
                <span>MESH EXTRACTION</span> <span>&bull;</span> 
                <span>FROSTED GLASS UI</span> <span>&bull;</span> 
            </div>
        </div>"""

if '<div class="marquee-container">' not in html:
    html = html.replace("""        <div class="features">
            <div class="feature-card tilt-card">
                <h3>🔍 AI Subject Extraction</h3>
                <p>Advanced neural networks instantly isolate your subject from the background, ensuring a clean 3D object.</p>
            </div>
            <div class="feature-card tilt-card">
                <h3>🧊 True 360° Hallucination</h3>
                <p>Not just a flat 2.5D plane. We use TripoSR to intelligently synthesize the back of the object from a single front-facing photo.</p>
            </div>
            <div class="feature-card tilt-card">
                <h3>🖥️ Pro 3D Viewer</h3>
                <p>Inspect your white clay meshes in a studio lighting environment with wireframe analysis and auto-rotation.</p>
            </div>
        </div>""", marquee_html)

with open("website/frontend/index.html", "w") as f:
    f.write(html)
