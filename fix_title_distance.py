import sys

with open("website/frontend/index.html", "r") as f:
    html = f.read()

target = """<div style="min-height: 85vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; max-width: 800px; margin: 0 auto;">"""
replacement = """<div style="min-height: 85vh; display: flex; flex-direction: column; justify-content: flex-start; align-items: center; text-align: center; max-width: 800px; margin: 0 auto; padding-top: 15vh;">"""

html = html.replace(target, replacement)

with open("website/frontend/index.html", "w") as f:
    f.write(html)


with open("website/frontend/about.html", "r") as f:
    html = f.read()

target_about = """<div style="min-height: 85vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; max-width: 1000px; margin: 0 auto; padding-top: 2rem;">"""
replacement_about = """<div style="min-height: 85vh; display: flex; flex-direction: column; justify-content: flex-start; align-items: center; text-align: center; max-width: 1000px; margin: 0 auto; padding-top: 15vh;">"""

html = html.replace(target_about, replacement_about)

with open("website/frontend/about.html", "w") as f:
    f.write(html)

print("Title distance forcefully increased!")
