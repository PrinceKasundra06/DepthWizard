import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

target = """                    <!-- Animated Blueprint Grid inside card -->"""
replacement = """                    <!-- Magic Dust Particles -->
                    <div id="magicDustContainer" style="position: absolute; inset: 0; pointer-events: none; z-index: 1; overflow: hidden;"></div>
                    
                    <!-- Animated Blueprint Grid inside card -->"""

if 'id="magicDustContainer"' not in html:
    html = html.replace(target, replacement)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)


with open("website/frontend/js/main.js", "r") as f:
    js = f.read()

js_addition = """
// Magic Dust Particles inside Dropzone
const dustContainer = document.getElementById('magicDustContainer');
if (dustContainer) {
    for (let i = 0; i < 20; i++) {
        let p = document.createElement('div');
        p.style.position = 'absolute';
        p.style.width = Math.random() * 3 + 'px';
        p.style.height = p.style.width;
        p.style.background = 'rgba(255,255,255,0.8)';
        p.style.borderRadius = '50%';
        p.style.boxShadow = '0 0 10px rgba(255,255,255,0.8)';
        p.style.left = Math.random() * 100 + '%';
        p.style.top = Math.random() * 100 + '%';
        p.style.opacity = Math.random() * 0.5;
        p.style.animation = `floatParticle ${Math.random() * 5 + 3}s linear infinite alternate`;
        dustContainer.appendChild(p);
    }
}
"""

if "// Magic Dust Particles inside Dropzone" not in js:
    with open("website/frontend/js/main.js", "a") as f:
        f.write(js_addition)

# We need the keyframes for floatParticle in upload.html
with open("website/frontend/upload.html", "r") as f:
    html = f.read()

if "floatParticle" not in html:
    style_target = "</style>"
    style_replacement = """
        @keyframes floatParticle {
            0% { transform: translate(0, 0); opacity: 0; }
            50% { opacity: 0.8; }
            100% { transform: translate(20px, -40px); opacity: 0; }
        }
    </style>"""
    html = html.replace(style_target, style_replacement)
    with open("website/frontend/upload.html", "w") as f:
        f.write(html)

print("Added magic particles!")
