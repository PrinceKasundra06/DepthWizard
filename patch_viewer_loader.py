import sys

with open("website/frontend/js/viewer.js", "r") as f:
    code = f.read()

bad_logic = """                    loadingEl.style.display = 'none';"""
good_logic = """                    if (loadingEl) loadingEl.style.display = 'none';"""

code = code.replace(bad_logic, good_logic)

with open("website/frontend/js/viewer.js", "w") as f:
    f.write(code)
