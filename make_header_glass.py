import sys
import re

with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

target = """.draftly-header {
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

replacement = """.draftly-header {
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
    background: rgba(15, 15, 15, 0.2);
    backdrop-filter: blur(40px) saturate(150%);
    -webkit-backdrop-filter: blur(40px) saturate(150%);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 9999px;
    z-index: 100;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
}"""

css = css.replace(target, replacement)

with open("website/frontend/css/style.css", "w") as f:
    f.write(css)

print("Header made extremely glassy!")
