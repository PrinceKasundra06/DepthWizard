import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

target = """            <div class="draftly-sidebar-content">
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1.25rem; box-shadow: inset 0 1px 1px rgba(255,255,255,0.05);">
                    <label style="display: flex; align-items: center; justify-content: space-between; font-size: 13px; font-weight: 600; cursor: pointer; color: #fff;">
                        <span><i class="fa-solid fa-cube" style="margin-right: 8px; color: #fff;"></i> True 360 Mode</span>
                        <input type="checkbox" id="mode360Toggle" checked style="accent-color: #ffffff; transform: scale(1.2);">
                    </label>
                    <p style="font-size: 11px; color: rgba(255,255,255,0.4); margin-top: 12px; line-height: 1.6;">
                        Uses TripoSR to intelligently hallucinate the unseen geometry of your object. Recommended for product photos.
                    </p>
                </div>
                
                <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 12px; padding: 1.25rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Advanced Settings</div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Resolution</span>
                        <span style="font-size: 11px; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px;">High (192)</span>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Marching Cubes</span>
                        <span style="font-size: 11px; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px;">Optimized</span>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Texture Engine</span>
                        <span style="font-size: 11px; color: rgba(255,255,255,0.3); border-bottom: 1px dashed rgba(255,255,255,0.3);">Coming Soon</span>
                    </div>
                </div>

                <!-- Best Output Warning -->
                <div style="background: rgba(255, 170, 0, 0.05); border: 1px solid rgba(255, 170, 0, 0.2); border-radius: 12px; padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start; box-shadow: inset 0 0 20px rgba(255, 170, 0, 0.02);">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #ffaa00; margin-top: 2px;"></i>
                    <div>
                        <div style="font-size: 12px; font-weight: 600; color: #ffaa00; margin-bottom: 0.5rem;">For Best Results</div>
                        <p style="font-size: 11px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">
                            Photos taken at sharp <strong>45-degree angles</strong> (top-down or extreme side angles) are not ideal. For a perfect 360° mesh, use a straight-on, eye-level photo of the subject.
                        </p>
                    </div>
                </div>
            </div>"""

replacement = """            <div class="draftly-sidebar-content">
                <!-- Main Engine Mode -->
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1.25rem; box-shadow: inset 0 1px 1px rgba(255,255,255,0.05);">
                    <label style="display: flex; align-items: center; justify-content: space-between; font-size: 13px; font-weight: 600; cursor: pointer; color: #fff;">
                        <span><i class="fa-solid fa-cube" style="margin-right: 8px; color: #fff;"></i> True 360 Mode</span>
                        <input type="checkbox" id="mode360Toggle" checked style="accent-color: #ffffff; transform: scale(1.2);">
                    </label>
                    <p style="font-size: 11px; color: rgba(255,255,255,0.4); margin-top: 12px; line-height: 1.6;">
                        Uses TripoSR to intelligently hallucinate the unseen geometry of your object. Recommended for product photos.
                    </p>
                </div>
                
                <!-- Pipeline Modules -->
                <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 12px; padding: 1.25rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1.25rem; text-transform: uppercase; letter-spacing: 0.05em;">AI Pipeline Modules</div>
                    
                    <label style="display: flex; align-items: center; justify-content: space-between; font-size: 12px; font-weight: 500; cursor: pointer; color: #fff; margin-bottom: 1rem;">
                        <span><i class="fa-solid fa-scissors" style="margin-right: 8px; opacity: 0.6;"></i> Auto-Remove Background</span>
                        <input type="checkbox" checked disabled style="accent-color: #ffffff; transform: scale(1.1); opacity: 0.8;">
                    </label>
                    
                    <label style="display: flex; align-items: center; justify-content: space-between; font-size: 12px; font-weight: 500; cursor: pointer; color: #fff; margin-bottom: 1rem;">
                        <span><i class="fa-solid fa-compress" style="margin-right: 8px; opacity: 0.6;"></i> Smart Subject Centering</span>
                        <input type="checkbox" checked disabled style="accent-color: #ffffff; transform: scale(1.1); opacity: 0.8;">
                    </label>
                    
                    <label style="display: flex; align-items: center; justify-content: space-between; font-size: 12px; font-weight: 500; cursor: pointer; color: #fff;">
                        <span><i class="fa-solid fa-wand-magic-sparkles" style="margin-right: 8px; opacity: 0.6;"></i> Auto-pad 512x512 canvas</span>
                        <input type="checkbox" checked disabled style="accent-color: #ffffff; transform: scale(1.1); opacity: 0.8;">
                    </label>
                </div>
                
                <!-- Network Architecture -->
                <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 12px; padding: 1.25rem;">
                    <div style="font-size: 11px; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 1.25rem; text-transform: uppercase; letter-spacing: 0.05em;">Network Architecture</div>
                    
                    <div style="margin-bottom: 1.25rem;">
                        <div style="display: flex; justify-content: space-between; font-size: 11px; color: rgba(255,255,255,0.6); margin-bottom: 6px;">
                            <span>Mesh Density (192)</span>
                            <span>High</span>
                        </div>
                        <div style="width: 100%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px;">
                            <div style="width: 75%; height: 100%; background: #ffffff; border-radius: 2px;"></div>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 1.25rem;">
                        <div style="display: flex; justify-content: space-between; font-size: 11px; color: rgba(255,255,255,0.6); margin-bottom: 6px;">
                            <span>Inference Steps</span>
                            <span>Default</span>
                        </div>
                        <div style="width: 100%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px;">
                            <div style="width: 50%; height: 100%; background: #ffffff; border-radius: 2px;"></div>
                        </div>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Texture Engine</span>
                        <span style="font-size: 10px; color: rgba(0,0,0,1); background: #ffffff; padding: 2px 6px; border-radius: 4px; font-weight: 600;">White Clay</span>
                    </div>
                </div>

                <!-- Best Output Warning -->
                <div style="background: rgba(255, 170, 0, 0.05); border: 1px solid rgba(255, 170, 0, 0.2); border-radius: 12px; padding: 1.25rem; display: flex; gap: 1rem; align-items: flex-start; box-shadow: inset 0 0 20px rgba(255, 170, 0, 0.02);">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #ffaa00; margin-top: 2px;"></i>
                    <div>
                        <div style="font-size: 12px; font-weight: 600; color: #ffaa00; margin-bottom: 0.5rem;">For Best Results</div>
                        <p style="font-size: 11px; color: rgba(255,255,255,0.6); line-height: 1.6; margin: 0;">
                            Photos taken at sharp <strong>45-degree angles</strong> (top-down or extreme side angles) are not ideal. For a perfect 360° mesh, use a straight-on, eye-level photo of the subject.
                        </p>
                    </div>
                </div>
                
                <!-- System Status -->
                <div style="display: flex; align-items: center; gap: 0.5rem; justify-content: center; margin-top: 0.5rem; padding-bottom: 1rem;">
                    <div style="width: 6px; height: 6px; background: #00ff00; border-radius: 50%; box-shadow: 0 0 8px #00ff00;"></div>
                    <span style="font-size: 10px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.05em;">MPS Engine Connected</span>
                </div>
            </div>"""

html = html.replace(target, replacement)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)

print("Upgraded upload sidebar!")
