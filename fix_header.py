import glob
import re

for filepath in glob.glob("website/frontend/*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    
    # Extract the header block
    header_pattern = r'<header class="draftly-header">.*?</header>'
    header_match = re.search(header_pattern, html, flags=re.DOTALL)
    
    if header_match:
        header_html = header_match.group(0)
        
        # Remove it from its original place
        html = html.replace(header_html, "")
        
        # Find the opening of .draftly-viewport and insert the header right after it
        # Note: In about.html and index.html, it's <main class="draftly-viewport" style="...">
        # In upload.html and viewer.html, it might be <main class="draftly-viewport"> or similar.
        viewport_pattern = r'(<main class="draftly-viewport"[^>]*>)'
        
        # Insert the header exactly after the viewport tag
        html = re.sub(viewport_pattern, r'\1\n        ' + header_html.replace('\\', '\\\\'), html, count=1)
        
        with open(filepath, "w") as f:
            f.write(html)
        print(f"Moved header in {filepath}")

# Now update the CSS
with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

old_css = """.draftly-header {
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1.5rem;
    background: transparent;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}"""

new_css = """.draftly-header {
    position: absolute;
    top: 24px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 1000px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1rem 0 1.5rem;
    background: linear-gradient(135deg, rgba(20,20,20,0.8), rgba(5,5,5,0.9));
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 9999px;
    z-index: 100;
    box-shadow: 0 10px 40px rgba(0,0,0,0.8), inset 0 2px 10px rgba(255,255,255,0.05);
}"""

if ".draftly-header {" in css:
    # Use regex to replace the entire block
    css = re.sub(r'\.draftly-header \{[^}]+\}', new_css, css)
    with open("website/frontend/css/style.css", "w") as f:
        f.write(css)
    print("Updated style.css")

