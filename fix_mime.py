import sys

with open("website/backend/main.py", "r") as f:
    code = f.read()

target = "from fastapi.staticfiles import StaticFiles"
replacement = """import mimetypes
mimetypes.add_type('text/plain', '.obj')
from fastapi.staticfiles import StaticFiles"""

if "mimetypes.add_type" not in code:
    code = code.replace(target, replacement)
    with open("website/backend/main.py", "w") as f:
        f.write(code)
    print("Mimetype fixed in backend!")
else:
    print("Mimetype already fixed!")
