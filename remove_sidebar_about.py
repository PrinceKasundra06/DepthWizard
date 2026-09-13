import sys
import re

with open("website/frontend/about.html", "r") as f:
    html = f.read()

pattern = r'<aside class="draftly-sidebar">.*?</aside>'
html = re.sub(pattern, '', html, flags=re.DOTALL)

with open("website/frontend/about.html", "w") as f:
    f.write(html)

print("Sidebar removed from about.html!")
