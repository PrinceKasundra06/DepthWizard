import sys

with open("website/frontend/index.html", "r") as f:
    html = f.read()

bad_viewport = """        <main class="draftly-viewport" style="background: #000;">
            <canvas id="bg-canvas" style="position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%;"></canvas>
            
            <!-- Dark gradient mask behind text for perfect legibility -->
            <div style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0) 60%); z-index: 5; pointer-events: none;"></div>
            
            <div style="text-align: center; padding: 2rem; position: relative; z-index: 10; pointer-events: none; text-shadow: 0 4px 24px rgba(0,0,0,1);">
                <h1 style="font-size: 4rem; letter-spacing: -0.05em; font-weight: 500; margin-bottom: 1rem;">DepthWizard</h1>
                <p class="subtitle" style="margin: 0 auto; margin-bottom: 3rem; color: rgba(255,255,255,0.6); font-size: 1rem; max-width: 400px;">
                    Instantly convert 2D images into immersive 3D flythroughs and 360 meshes.
                </p>
                
                <div style="display: flex; gap: 1rem; justify-content: center; margin-bottom: 4rem; pointer-events: auto;">
                    <button class="draftly-btn-small draftly-btn-primary" style="height: 40px; padding: 0 1.5rem; font-size: 13px;" onclick="window.location='upload.html'">
                        Start Generating
                    </button>
                </div>

                <div class="features" style="margin-top: 0; max-width: 800px; display: flex; gap: 1rem; text-align: left; background: rgba(5,5,5,0.4); backdrop-filter: blur(12px); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="flex: 1;">
                        <h3 style="font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 0.5rem;"><i class="fa-solid fa-layer-group" style="margin-right: 6px;"></i> Depth Estimation</h3>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.5); line-height: 1.5; margin: 0;">State of the art MiDaS AI creates highly accurate depth maps.</p>
                    </div>
                    <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
                    <div style="flex: 1;">
                        <h3 style="font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 0.5rem;"><i class="fa-solid fa-cube" style="margin-right: 6px;"></i> 360 Mesh AI</h3>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.5); line-height: 1.5; margin: 0;">TripoSR generates full true 3D models of subjects.</p>
                    </div>
                    <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
                    <div style="flex: 1;">
                        <h3 style="font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 0.5rem;"><i class="fa-solid fa-bolt" style="margin-right: 6px;"></i> Instantly Ready</h3>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.5); line-height: 1.5; margin: 0;">Download your meshes as OBJ immediately.</p>
                    </div>
                </div>
            </div>
        </main>"""

good_viewport = """        <main class="draftly-viewport" style="background: #000; position: relative;">
            <canvas id="bg-canvas" style="position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%;"></canvas>
            
            <!-- Dark gradient mask behind text for legibility -->
            <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.85) 100%); z-index: 5; pointer-events: none;"></div>
            
            <!-- Scrollable Content Container -->
            <div style="position: absolute; inset: 0; z-index: 10; overflow-y: auto; padding: 2rem; scroll-behavior: smooth;">
                
                <!-- Hero Section -->
                <div style="min-height: 80vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-bottom: 6rem; text-shadow: 0 4px 24px rgba(0,0,0,1);">
                    <h1 style="font-size: 4.5rem; letter-spacing: -0.05em; font-weight: 500; margin-bottom: 1rem;">DepthWizard</h1>
                    <p class="subtitle" style="margin: 0 auto; margin-bottom: 3rem; color: rgba(255,255,255,0.6); font-size: 1.1rem; max-width: 500px; line-height: 1.6;">
                        Instantly convert 2D images into immersive 3D flythroughs and True-360 geometric meshes using state-of-the-art Neural Networks.
                    </p>
                    
                    <div style="display: flex; gap: 1rem; justify-content: center; margin-bottom: 4rem;">
                        <button class="draftly-btn-small draftly-btn-primary" style="height: 44px; padding: 0 2rem; font-size: 14px;" onclick="window.location='upload.html'">
                            <i class="fa-solid fa-wand-magic-sparkles"></i> Start Generating
                        </button>
                    </div>

                    <div class="features" style="margin-top: 0; max-width: 900px; display: flex; gap: 1.5rem; text-align: left; background: rgba(15,15,15,0.6); backdrop-filter: blur(20px); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
                        <div style="flex: 1;">
                            <div style="width: 40px; height: 40px; border-radius: 10px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                                <i class="fa-solid fa-layer-group" style="font-size: 16px; color: #fff;"></i>
                            </div>
                            <h3 style="font-size: 14px; font-weight: 600; color: #fff; margin-bottom: 0.5rem;">Neural Depth Estimation</h3>
                            <p style="font-size: 12px; color: rgba(255,255,255,0.5); line-height: 1.6; margin: 0;">Powered by MiDaS, we extrapolate exact Z-depth information from flat pixels to generate flawless 2.5D landscapes.</p>
                        </div>
                        <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
                        <div style="flex: 1;">
                            <div style="width: 40px; height: 40px; border-radius: 10px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                                <i class="fa-solid fa-cube" style="font-size: 16px; color: #fff;"></i>
                            </div>
                            <h3 style="font-size: 14px; font-weight: 600; color: #fff; margin-bottom: 0.5rem;">True 360 Mesh AI</h3>
                            <p style="font-size: 12px; color: rgba(255,255,255,0.5); line-height: 1.6; margin: 0;">Utilizing the cutting-edge TripoSR architecture to hallucinate the unseen geometry of subjects.</p>
                        </div>
                        <div style="width: 1px; background: rgba(255,255,255,0.08);"></div>
                        <div style="flex: 1;">
                            <div style="width: 40px; height: 40px; border-radius: 10px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                                <i class="fa-solid fa-bolt" style="font-size: 16px; color: #fff;"></i>
                            </div>
                            <h3 style="font-size: 14px; font-weight: 600; color: #fff; margin-bottom: 0.5rem;">Local Privacy & Speed</h3>
                            <p style="font-size: 12px; color: rgba(255,255,255,0.5); line-height: 1.6; margin: 0;">Everything processes on your local Tensor engine. Ultra-fast marching cubes extraction.</p>
                        </div>
                    </div>
                </div>

                <!-- Deep Dive Section -->
                <div style="max-width: 900px; margin: 0 auto 6rem auto; text-align: left; background: rgba(10,10,10,0.7); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 4rem;">
                    <div style="display: flex; gap: 4rem; align-items: center;">
                        <div style="flex: 1;">
                            <span style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem; display: block;">Under the hood</span>
                            <h2 style="font-size: 2.5rem; font-weight: 500; letter-spacing: -0.04em; margin-bottom: 1.5rem; line-height: 1.1;">The Magic of TripoSR</h2>
                            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.6); line-height: 1.7; margin-bottom: 1.5rem;">
                                TripoSR is a state-of-the-art feed-forward 3D generative model capable of producing high-quality 3D meshes from a single image in less than a second. It leverages a specialized transformer architecture that predicts dense triplane representations from visual features.
                            </p>
                            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.6); line-height: 1.7; margin-bottom: 2rem;">
                                In DepthWizard, we automatically strip the background from your subject using `rembg`, center it perfectly, and feed it into the TripoSR inference engine. The model hallucinates the backside of the object with incredible precision, outputting a fully enclosed geometric mesh.
                            </p>
                            <a href="upload.html" class="draftly-btn-small" style="height: 36px; padding: 0 1.25rem;">Try the Engine <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></a>
                        </div>
                        <div style="flex: 1; height: 300px; border-radius: 16px; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.02) 100%); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
                            <div style="position: absolute; width: 150px; height: 150px; background: rgba(255,255,255,0.2); filter: blur(50px); border-radius: 50%;"></div>
                            <i class="fa-solid fa-microchip" style="font-size: 5rem; color: rgba(255,255,255,0.9); z-index: 2;"></i>
                        </div>
                    </div>
                </div>

                <!-- Use Cases Section -->
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
                </div>

                <!-- Footer area -->
                <div style="text-align: center; padding-bottom: 2rem;">
                    <button class="draftly-btn-small draftly-btn-primary" style="height: 48px; padding: 0 3rem; font-size: 15px;" onclick="window.location='upload.html'">
                        Launch Studio
                    </button>
                    <p style="font-size: 11px; color: rgba(255,255,255,0.3); margin-top: 2rem;">Built entirely with local Tensor Processing. No cloud fees.</p>
                </div>

            </div>
        </main>"""

html = html.replace(bad_viewport, good_viewport)

with open("website/frontend/index.html", "w") as f:
    f.write(html)
    
print("Added massive detail to index.html!")
