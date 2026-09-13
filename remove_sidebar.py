import sys
import re

with open("website/frontend/index.html", "r") as f:
    html = f.read()

# Use regex to find and remove the entire <aside class="draftly-sidebar"> block
# We use re.DOTALL to match across newlines
pattern = r'<aside class="draftly-sidebar">.*?</aside>'
html = re.sub(pattern, '', html, flags=re.DOTALL)

with open("website/frontend/index.html", "w") as f:
    f.write(html)

print("Sidebar removed from index.html!")
