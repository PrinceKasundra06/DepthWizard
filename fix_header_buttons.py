import sys
import re

with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

# Make all draftly-btn-small pill-shaped and nicely sized
target_btn = """.draftly-btn-small {
    background-color: transparent;
    color: rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 0 1rem;
    height: 32px;
    border-radius: 6px;
    font-size: 0.85rem;"""

replacement_btn = """.draftly-btn-small {
    background-color: transparent;
    color: rgba(255, 255, 255, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 0 1.25rem;
    height: 36px;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 0.02em;"""

css = css.replace(target_btn, replacement_btn)

# Make sure primary button is also fully pill-shaped
target_primary = """.draftly-btn-primary {
    background-color: #ffffff;
    color: #000000;
    border: none;
    font-weight: 500;
}"""

replacement_primary = """.draftly-btn-primary {
    background-color: #ffffff;
    color: #000000;
    border: none;
    font-weight: 600;
    box-shadow: 0 0 15px rgba(255,255,255,0.2);
}"""

css = css.replace(target_primary, replacement_primary)

with open("website/frontend/css/style.css", "w") as f:
    f.write(css)

print("Adjusted header buttons!")
