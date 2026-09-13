import sys

for file in ["website/frontend/index.html", "website/frontend/about.html"]:
    with open(file, "r") as f:
        html = f.read()

    # The scrollable container
    target = """padding: 4rem 2rem;"""
    replacement = """padding: 8rem 2rem 4rem 2rem;"""
    
    html = html.replace(target, replacement)

    # In about.html, I might have added "padding-top: 4rem;" in the inner div earlier.
    target_about = """padding-top: 4rem;"""
    replacement_about = """padding-top: 2rem;"""
    html = html.replace(target_about, replacement_about)
    
    with open(file, "w") as f:
        f.write(html)

print("Distance increased!")
