import sys
import re

with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

# Fix .draftly-btn-primary:hover
bad_draftly_primary_hover = """.draftly-btn-primary:hover {
    background: rgba(255, 255, 255, 0.9);
}"""
good_draftly_primary_hover = """.draftly-btn-primary:hover {
    background: rgba(255, 255, 255, 0.9);
    color: #000000 !important;
}"""
css = css.replace(bad_draftly_primary_hover, good_draftly_primary_hover)

# Fix .btn-primary:hover
bad_btn_primary_hover = """.btn-primary:hover {
    background: #f0f0f0;
    transform: translateY(-2px);
    box-shadow: 0 0 0 1px rgba(255,255,255,0.4), 0 12px 30px rgba(255,255,255,0.2);
}"""
good_btn_primary_hover = """.btn-primary:hover {
    background: #f0f0f0;
    color: #000000 !important;
    transform: translateY(-2px);
    box-shadow: 0 0 0 1px rgba(255,255,255,0.4), 0 12px 30px rgba(255,255,255,0.2);
}"""
css = css.replace(bad_btn_primary_hover, good_btn_primary_hover)

with open("website/frontend/css/style.css", "w") as f:
    f.write(css)

print("Fixed button hover text color!")
