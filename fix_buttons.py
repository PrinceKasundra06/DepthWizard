import sys
import re

with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

# Replace border-radius in .btn block
btn_pattern = re.compile(r'(\.btn\s*\{[^}]*?)border-radius:\s*8px;')
css = btn_pattern.sub(r'\1border-radius: 9999px;', css)

# Replace border-radius in .draftly-btn-small block
draftly_btn_pattern = re.compile(r'(\.draftly-btn-small\s*\{[^}]*?)border-radius:\s*8px;')
css = draftly_btn_pattern.sub(r'\1border-radius: 9999px;', css)

with open("website/frontend/css/style.css", "w") as f:
    f.write(css)

print("Buttons updated to pill shape!")
