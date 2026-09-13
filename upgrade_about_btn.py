import sys
import glob

# 1. Update HTML
target = """<a href="about.html" class="draftly-btn-small" style="background: transparent; border: 1px solid transparent;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='transparent'"><i class="fa-solid fa-circle-info" style="margin-right: 6px;"></i> About Us</a>"""

replacement = """<a href="about.html" class="draftly-btn-small btn-about-us">
                        <i class="fa-solid fa-users" style="margin-right: 6px; opacity: 0.8;"></i> About Us
                    </a>"""

for filepath in glob.glob("website/frontend/*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    
    html = html.replace(target, replacement)
    
    # Also handle the one in viewer.html if it's a button instead of <a>
    target2 = """<button class="draftly-btn-small" style="background: transparent; border: 1px solid transparent;" onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='transparent'" onclick="window.location='about.html'"><i class="fa-solid fa-circle-info" style="margin-right: 6px;"></i> About Us</button>"""
    html = html.replace(target2, replacement)
    
    with open(filepath, "w") as f:
        f.write(html)


# 2. Update CSS
with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

css_addition = """
/* About Us Nav Button */
.btn-about-us {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    color: rgba(255,255,255,0.6) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
.btn-about-us:hover {
    background: rgba(255,255,255,0.08) !important;
    border-color: rgba(255,255,255,0.2) !important;
    color: #ffffff !important;
    transform: scale(1.02);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
"""

if ".btn-about-us" not in css:
    with open("website/frontend/css/style.css", "a") as f:
        f.write(css_addition)

print("About Us button upgraded!")
