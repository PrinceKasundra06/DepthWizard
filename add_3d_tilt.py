import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

# Add the glare div inside the dropzone
target = """                    <!-- Animated Blueprint Grid inside card -->"""
replacement = """                    <!-- Dynamic Glare for 3D Tilt -->
                    <div id="dropGlare" style="position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.2) 0%, transparent 60%); opacity: 0; pointer-events: none; z-index: 10; transition: opacity 0.4s ease; mix-blend-mode: overlay;"></div>
                    
                    <!-- Animated Blueprint Grid inside card -->"""

if 'id="dropGlare"' not in html:
    html = html.replace(target, replacement)

# We also need to make sure the card preserves 3D
target_style = """                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    overflow: hidden;
                    cursor: pointer;"""
replacement_style = """                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                    overflow: hidden;
                    cursor: pointer;
                    transform-style: preserve-3d;"""
if 'transform-style: preserve-3d;' not in html:
    html = html.replace(target_style, replacement_style)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)

# Add the JS logic
with open("website/frontend/js/main.js", "r") as f:
    js = f.read()

js_addition = """
// 3D Tilt Effect for Dropzone
const dropZoneEl = document.getElementById('dropZone');
const dropGlare = document.getElementById('dropGlare');
if (dropZoneEl && dropGlare) {
    dropZoneEl.addEventListener('mousemove', (e) => {
        // Don't tilt if we are dragging a file (dragover handles its own transform)
        if (dropZoneEl.style.borderColor === 'rgba(0, 150, 255, 0.5)') return;

        const rect = dropZoneEl.getBoundingClientRect();
        const x = e.clientX - rect.left; // x position within the element.
        const y = e.clientY - rect.top;  // y position within the element.

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * -8; // Max 8 degrees
        const rotateY = ((x - centerX) / centerX) * 8;

        // Apply 3D transform
        dropZoneEl.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        
        // Move Glare
        dropGlare.style.opacity = '1';
        dropGlare.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.15) 0%, transparent 60%)`;
    });

    dropZoneEl.addEventListener('mouseleave', () => {
        if (dropZoneEl.style.borderColor === 'rgba(0, 150, 255, 0.5)') return;
        dropZoneEl.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
        dropGlare.style.opacity = '0';
        
        // Brief transition for resetting
        dropZoneEl.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
    });
    
    dropZoneEl.addEventListener('mouseenter', () => {
        // Remove transition while moving so it tracks instantly
        dropZoneEl.style.transition = 'none';
    });
}
"""

if "// 3D Tilt Effect for Dropzone" not in js:
    with open("website/frontend/js/main.js", "a") as f:
        f.write(js_addition)

print("Added 3D Tilt!")
