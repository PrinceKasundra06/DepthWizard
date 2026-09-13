import sys
import re

with open("website/frontend/about.html", "r") as f:
    html = f.read()

# We want to replace everything inside the <div style="position: absolute; inset: 0; z-index: 10; overflow-y: auto; ...">
# So let's just grab the whole file and do a regex replacement of that container.
pattern = r'(<!-- Scrollable Content Container -->\s*<div style="position: absolute; inset: 0; z-index: 10; overflow-y: auto; padding: 4rem 2rem; scroll-behavior: smooth;">).*?(</main>)'

new_content = """\\1
                    <div style="min-height: 85vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; max-width: 1000px; margin: 0 auto; padding-top: 4rem;">
                        
                        <!-- Floating Glass Badge -->
                        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); padding: 8px 24px; border-radius: 999px; margin-bottom: 3rem; backdrop-filter: blur(20px); animation: float 6s ease-in-out infinite;">
                            <span style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.8); text-transform: uppercase; letter-spacing: 0.2em;">Our Philosophy</span>
                        </div>

                        <!-- Massive Emotional Headline -->
                        <h1 style="font-size: 5rem; line-height: 1.1; font-weight: 500; letter-spacing: -0.04em; color: #fff; text-shadow: 0 10px 40px rgba(0,0,0,0.8); margin-bottom: 3rem;">
                            Breathing <span style="background: linear-gradient(135deg, #fff, #888); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">life</span> into pixels.
                        </h1>

                        <!-- Emotional Manifesto -->
                        <div style="max-width: 700px; position: relative;">
                            <div style="position: absolute; left: -20px; top: -20px; font-size: 6rem; color: rgba(255,255,255,0.03); font-family: serif; line-height: 1;">"</div>
                            <p style="font-size: 1.25rem; color: rgba(255,255,255,0.7); line-height: 1.8; margin-bottom: 2rem; font-weight: 300;">
                                We didn't build DepthWizard just to write code. We built it because we believe that human memory shouldn't be confined to flat, two-dimensional screens. 
                            </p>
                            <p style="font-size: 1.25rem; color: rgba(255,255,255,0.7); line-height: 1.8; margin-bottom: 4rem; font-weight: 300;">
                                Every photograph captures a singular moment in time. Our mission is to shatter the glass—to use the absolute bleeding edge of neural architecture to let you step <em>inside</em> your memories. We are democratizing the geometry of the real world.
                            </p>
                        </div>

                        <!-- The Team Lineup -->
                        <div style="width: 100%; height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent); margin-bottom: 4rem;"></div>

                        <div style="display: flex; flex-direction: column; align-items: center;">
                            <span style="font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.3em; margin-bottom: 2rem;">Forged by</span>
                            
                            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem 2rem; max-width: 800px;">
                                <span style="font-size: 1.2rem; font-weight: 500; color: #fff; text-shadow: 0 0 20px rgba(255,255,255,0.3);">Prince Kasundra</span>
                                <span style="color: rgba(255,255,255,0.2);">✦</span>
                                <span style="font-size: 1.2rem; font-weight: 500; color: #fff; text-shadow: 0 0 20px rgba(255,255,255,0.3);">Het Chikhaliya</span>
                                <span style="color: rgba(255,255,255,0.2);">✦</span>
                                <span style="font-size: 1.2rem; font-weight: 500; color: #fff; text-shadow: 0 0 20px rgba(255,255,255,0.3);">Prachi Lodhia</span>
                                <span style="color: rgba(255,255,255,0.2);">✦</span>
                                <span style="font-size: 1.2rem; font-weight: 500; color: #fff; text-shadow: 0 0 20px rgba(255,255,255,0.3);">Kashyap Dubariya</span>
                                <span style="color: rgba(255,255,255,0.2);">✦</span>
                                <span style="font-size: 1.2rem; font-weight: 500; color: #fff; text-shadow: 0 0 20px rgba(255,255,255,0.3);">Vishwa Gondaliya</span>
                                <span style="color: rgba(255,255,255,0.2);">✦</span>
                                <span style="font-size: 1.2rem; font-weight: 500; color: #fff; text-shadow: 0 0 20px rgba(255,255,255,0.3);">Parth Lakhdhir</span>
                            </div>
                        </div>

                    </div>
                </div>
            \\2"""

html = re.sub(pattern, new_content, html, flags=re.DOTALL)

# Add keyframes for the float animation to the <style> block
style_target = "</style>"
style_replacement = """
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
    </style>"""
html = html.replace(style_target, style_replacement)

with open("website/frontend/about.html", "w") as f:
    f.write(html)

print("About page made crazy and emotional!")
