import sys
import glob
import re

# 1. Update all links from "+ New Project" to point to "new.html"
for filepath in glob.glob("website/frontend/*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    
    # We look for the "New Project" link and change href to new.html
    html = html.replace('href="upload.html" class="draftly-btn-small"><i class="fa-solid fa-plus"></i> New Project', 'href="new.html" class="draftly-btn-small"><i class="fa-solid fa-plus"></i> New Project')
    
    with open(filepath, "w") as f:
        f.write(html)


# 2. Create the new.html file
new_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Project | DepthWizard</title>
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        .draftly-input {
            width: 100%;
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
            color: #fff;
            padding: 12px 16px;
            border-radius: 8px;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            outline: none;
            transition: all 0.3s;
            margin-bottom: 1.5rem;
        }
        .draftly-input:focus {
            border-color: rgba(0, 150, 255, 0.5);
            box-shadow: 0 0 15px rgba(0, 150, 255, 0.2);
        }
        .draftly-label {
            display: block;
            text-align: left;
            font-size: 0.85rem;
            font-weight: 600;
            color: rgba(255,255,255,0.6);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }
    </style>
</head>
<body class="draftly-app">
    <div class="noise-overlay"></div>
    
    <div class="draftly-main">
        <main class="draftly-viewport" style="position: relative; background: #000;">
            
            <!-- HEADER -->
            <header class="draftly-header">
                <div class="draftly-header-left">
                    <a href="index.html" class="draftly-logo" style="text-decoration: none; cursor: pointer;">
                        <i class="fa-solid fa-cube"></i> DepthWizard Studio
                    </a>
                </div>
                <div class="draftly-header-right" style="display: flex; gap: 0.5rem;">
                    <a href="about.html" class="draftly-btn-small" style="background: transparent; border: 1px solid transparent;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='transparent'"><i class="fa-solid fa-circle-info" style="margin-right: 6px;"></i> About Us</a>
                    <a href="new.html" class="draftly-btn-small"><i class="fa-solid fa-plus"></i> New Project</a>
                    <a href="upload.html" class="draftly-btn-small draftly-btn-primary"><i class="fa-solid fa-rocket"></i> Launch</a>
                </div>
            </header>

            <!-- 3D Particle Wave Background -->
            <canvas id="bg-canvas" style="position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%;"></canvas>
            
            <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.85) 100%); z-index: 5; pointer-events: none;"></div>
            
            <!-- Setup Form -->
            <div style="position: absolute; inset: 0; z-index: 10; display: flex; align-items: center; justify-content: center; padding: 4rem 2rem;">
                
                <div style="background: rgba(15, 15, 15, 0.4); backdrop-filter: blur(40px) saturate(150%); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 3rem; width: 100%; max-width: 500px; box-shadow: 0 30px 60px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.1); text-align: center;">
                    
                    <div style="width: 64px; height: 64px; background: rgba(255,255,255,0.05); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem auto; border: 1px solid rgba(255,255,255,0.1);">
                        <i class="fa-solid fa-wand-sparkles" style="font-size: 1.5rem; color: #fff;"></i>
                    </div>

                    <h2 style="font-size: 1.8rem; font-weight: 500; margin-bottom: 0.5rem; color: #fff;">Initialize Workspace</h2>
                    <p style="color: rgba(255,255,255,0.5); font-size: 0.95rem; margin-bottom: 2.5rem;">Configure your neural environment.</p>

                    <form action="upload.html" method="GET">
                        <label class="draftly-label">Project Name</label>
                        <input type="text" class="draftly-input" placeholder="e.g. Character Concept 01" required>

                        <label class="draftly-label">Neural Engine</label>
                        <select class="draftly-input" style="appearance: none; cursor: pointer;">
                            <option value="triposr">TripoSR (True 360° Mesh)</option>
                            <option value="midas">MiDaS (2.5D Depth Map)</option>
                        </select>
                        
                        <div style="text-align: left; margin-bottom: 2.5rem; margin-top: -0.5rem;">
                            <span style="font-size: 12px; color: rgba(255,255,255,0.3);"><i class="fa-solid fa-circle-check" style="color: #00ff00; margin-right: 4px;"></i> Local Tensor Processing Active</span>
                        </div>

                        <button type="submit" class="draftly-btn-small draftly-btn-primary" style="width: 100%; height: 48px; font-size: 1rem; border-radius: 12px; display: flex; justify-content: center; box-shadow: 0 10px 20px rgba(255,255,255,0.1);">
                            Create Project <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i>
                        </button>
                    </form>

                </div>

            </div>

        </main>
    </div>
    
    <script src="js/main.js"></script>
</body>
</html>
"""

with open("website/frontend/new.html", "w") as f:
    f.write(new_html_content)

print("new.html created and links updated!")
