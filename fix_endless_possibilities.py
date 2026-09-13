import sys

with open("website/frontend/index.html", "r") as f:
    html = f.read()

bad_section = """                <!-- Use Cases Section -->
                <div style="max-width: 900px; margin: 0 auto 6rem auto; text-align: left;">
                    <h2 style="font-size: 2.5rem; font-weight: 500; letter-spacing: -0.04em; margin-bottom: 3rem; text-align: center;">Endless Possibilities</h2>
                    
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem;">
                        <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 2.5rem; transition: background 0.3s;">
                            <i class="fa-solid fa-gamepad" style="font-size: 2rem; margin-bottom: 1.5rem; color: #fff;"></i>
                            <h3 style="font-size: 1.2rem; font-weight: 500; margin-bottom: 1rem;">Game Development</h3>
                            <p style="font-size: 0.9rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Rapidly prototype game assets by photographing objects in real life and instantly converting them to OBJs for Unity or Unreal Engine.</p>
                        </div>
                        <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 2.5rem; transition: background 0.3s;">
                            <i class="fa-solid fa-shop" style="font-size: 2rem; margin-bottom: 1.5rem; color: #fff;"></i>
                            <h3 style="font-size: 1.2rem; font-weight: 500; margin-bottom: 1rem;">E-Commerce</h3>
                            <p style="font-size: 0.9rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Create 360-degree interactive product viewers for your storefront using only a single product photo.</p>
                        </div>
                        <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 2.5rem; transition: background 0.3s;">
                            <i class="fa-solid fa-vr-cardboard" style="font-size: 2rem; margin-bottom: 1.5rem; color: #fff;"></i>
                            <h3 style="font-size: 1.2rem; font-weight: 500; margin-bottom: 1rem;">AR & VR</h3>
                            <p style="font-size: 0.9rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Populate virtual reality environments with clay models of physical objects, creating surreal and beautiful mixed-reality experiences.</p>
                        </div>
                        <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 2.5rem; transition: background 0.3s;">
                            <i class="fa-solid fa-palette" style="font-size: 2rem; margin-bottom: 1.5rem; color: #fff;"></i>
                            <h3 style="font-size: 1.2rem; font-weight: 500; margin-bottom: 1rem;">Art & Concepting</h3>
                            <p style="font-size: 0.9rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Use our MiDaS depth estimator to create 2.5D parallax art from flat illustrations and paintings.</p>
                        </div>
                    </div>
                </div>"""

good_section = """                <!-- Use Cases Section -->
                <div style="max-width: 900px; margin: 0 auto 6rem auto; text-align: left;">
                    <h2 style="font-size: 2.5rem; font-weight: 500; letter-spacing: -0.04em; margin-bottom: 3rem; text-align: center; text-shadow: 0 4px 24px rgba(0,0,0,1);">Endless Possibilities</h2>
                    
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem;">
                        <div class="feature-card" style="background: rgba(10,10,10,0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
                            <div style="width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02)); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; box-shadow: inset 0 2px 4px rgba(255,255,255,0.1);">
                                <i class="fa-solid fa-gamepad" style="font-size: 1.25rem; color: #fff;"></i>
                            </div>
                            <h3 style="font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">Game Development</h3>
                            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Rapidly prototype game assets by photographing objects in real life and instantly converting them to OBJs for Unity or Unreal Engine.</p>
                        </div>
                        <div class="feature-card" style="background: rgba(10,10,10,0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
                            <div style="width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02)); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; box-shadow: inset 0 2px 4px rgba(255,255,255,0.1);">
                                <i class="fa-solid fa-shop" style="font-size: 1.25rem; color: #fff;"></i>
                            </div>
                            <h3 style="font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">E-Commerce</h3>
                            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Create 360-degree interactive product viewers for your storefront using only a single product photo.</p>
                        </div>
                        <div class="feature-card" style="background: rgba(10,10,10,0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
                            <div style="width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02)); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; box-shadow: inset 0 2px 4px rgba(255,255,255,0.1);">
                                <i class="fa-solid fa-vr-cardboard" style="font-size: 1.25rem; color: #fff;"></i>
                            </div>
                            <h3 style="font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">AR & VR</h3>
                            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Populate virtual reality environments with clay models of physical objects, creating surreal and beautiful mixed-reality experiences.</p>
                        </div>
                        <div class="feature-card" style="background: rgba(10,10,10,0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 2.5rem; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
                            <div style="width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02)); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; box-shadow: inset 0 2px 4px rgba(255,255,255,0.1);">
                                <i class="fa-solid fa-palette" style="font-size: 1.25rem; color: #fff;"></i>
                            </div>
                            <h3 style="font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">Art & Concepting</h3>
                            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.5); line-height: 1.6;">Use our MiDaS depth estimator to create 2.5D parallax art from flat illustrations and paintings.</p>
                        </div>
                    </div>
                </div>"""

html = html.replace(bad_section, good_section)

with open("website/frontend/index.html", "w") as f:
    f.write(html)
    
print("Polished Use Cases section!")
