import sys

with open("website/frontend/about.html", "r") as f:
    html = f.read()

# 1. Remove the mask-image so it touches both edges
target_mask = "mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent); -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);"
html = html.replace(target_mask, "")

# 2. Make the container truly full-width and remove its padding limitations.
# We also need to add a negative margin to break out of the parent container which might have max-width.
# Currently it's inside <div style="... max-width: 1000px; margin: 0 auto; ...">
target_container = """<div class="marquee-container" style="width: 100vw; max-width: 100vw; overflow: hidden; white-space: nowrap; position: relative; padding: 2rem 0; ">"""
replacement_container = """<div class="marquee-container" style="width: 100vw; margin-left: calc(-50vw + 50%); overflow: hidden; white-space: nowrap; position: relative; padding: 1rem 0; background: rgba(0,0,0,0.4); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">"""
html = html.replace(target_container, replacement_container)

# 3. Shrink the font size of the marquee names and stars
target_font = """        .marquee-name {
            font-size: 2.5rem;"""
replacement_font = """        .marquee-name {
            font-size: 1.5rem;"""
html = html.replace(target_font, replacement_font)

target_star = """        .marquee-star {
            color: rgba(255,255,255,0.1);
            font-size: 1.5rem;
        }"""
replacement_star = """        .marquee-star {
            color: rgba(255,255,255,0.15);
            font-size: 1rem;
        }"""
html = html.replace(target_star, replacement_star)

# 4. Also slow down the scroll a bit so it's smoother at smaller sizes
target_anim = "animation: scrollMarquee 20s linear infinite;"
replacement_anim = "animation: scrollMarquee 25s linear infinite;"
html = html.replace(target_anim, replacement_anim)

with open("website/frontend/about.html", "w") as f:
    f.write(html)

print("Marquee shrunk and made full width!")
