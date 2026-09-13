import sys

with open("website/frontend/upload.html", "r") as f:
    html = f.read()

target = """                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: rgba(255,255,255,0.7);">Texture Engine</span>
                        <span style="font-size: 11px; color: rgba(255,255,255,0.3); border-bottom: 1px dashed rgba(255,255,255,0.3);">Coming Soon</span>
                    </div>
                </div>
            </div>"""

replacement = """                    <div style="display: flex; justify-content: space-between; align-items: center;">
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

html = html.replace(target, replacement)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)

print("Warning added!")
