import sys

with open("website/frontend/about.html", "r") as f:
    html = f.read()

# 1. We need to extract the marquee container and put it OUTSIDE the max-width: 1000px div.
# Currently the structure is:
# <div style="max-width: 1000px; margin: 0 auto; ...">
#   ...
#   <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
#      <span style="font-size: 11px; ...">Forged by</span>
#      <div class="marquee-container" ...> ... </div>
#   </div>
# </div> (end of max-width: 1000px div)
# </div> (end of scrollable container)

target_to_replace = """                        <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
                            <span style="font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.3em; margin-bottom: 2rem;">Forged by</span>
                            
                            <!-- Infinite Marquee Container -->
                            <div class="marquee-container" style="width: 100vw; margin-left: calc(-50vw + 50%); overflow: hidden; white-space: nowrap; position: relative; padding: 1rem 0; background: rgba(0,0,0,0.4); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
                                <div class="marquee-content-wrapper" style="display: inline-flex; width: max-content;">
                                    
                                    <!-- First Set -->
                                    <div class="marquee-track" style="display: inline-flex; align-items: center; gap: 4rem; padding-right: 4rem;">
                                        <span class="marquee-name">Prince Kasundra</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Het Chikhaliya</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Prachi Lodhia</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Kashyap Dubariya</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Vishwa Gondaliya</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Parth Lakhdhir</span><span class="marquee-star">✦</span>
                                    </div>
                                    
                                    <!-- Second Set (Duplicate for seamless loop) -->
                                    <div class="marquee-track" style="display: inline-flex; align-items: center; gap: 4rem; padding-right: 4rem;">
                                        <span class="marquee-name">Prince Kasundra</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Het Chikhaliya</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Prachi Lodhia</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Kashyap Dubariya</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Vishwa Gondaliya</span><span class="marquee-star">✦</span>
                                        <span class="marquee-name">Parth Lakhdhir</span><span class="marquee-star">✦</span>
                                    </div>

                                </div>
                            </div>
                        </div>

                    </div>
                </div>"""

# Notice how I close the <div max-width:1000px> FIRST, then output the marquee directly in the scroll container!
# And I use margin-left: -2rem; width: calc(100% + 4rem); to perfectly bypass the parent's padding!
replacement = """                    </div> <!-- End of max-width: 1000px div -->

                    <!-- Marquee pulled OUTSIDE the max-width container, using negative margins to break parent padding -->
                    <div style="display: flex; flex-direction: column; align-items: center; width: calc(100% + 4rem); margin-left: -2rem; margin-bottom: 4rem;">
                        <span style="font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.3em; margin-bottom: 2rem;">Forged by</span>
                        
                        <!-- Infinite Marquee Container -->
                        <div class="marquee-container" style="width: 100%; overflow: hidden; white-space: nowrap; position: relative; padding: 1rem 0; background: rgba(0,0,0,0.4); border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <div class="marquee-content-wrapper" style="display: inline-flex; width: max-content;">
                                
                                <!-- First Set -->
                                <div class="marquee-track" style="display: inline-flex; align-items: center; gap: 4rem; padding-right: 4rem;">
                                    <span class="marquee-name">Prince Kasundra</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Het Chikhaliya</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Prachi Lodhia</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Kashyap Dubariya</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Vishwa Gondaliya</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Parth Lakhdhir</span><span class="marquee-star">✦</span>
                                </div>
                                
                                <!-- Second Set (Duplicate for seamless loop) -->
                                <div class="marquee-track" style="display: inline-flex; align-items: center; gap: 4rem; padding-right: 4rem;">
                                    <span class="marquee-name">Prince Kasundra</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Het Chikhaliya</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Prachi Lodhia</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Kashyap Dubariya</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Vishwa Gondaliya</span><span class="marquee-star">✦</span>
                                    <span class="marquee-name">Parth Lakhdhir</span><span class="marquee-star">✦</span>
                                </div>

                            </div>
                        </div>
                    </div>

                </div> <!-- End of scroll container -->"""

html = html.replace(target_to_replace, replacement)

with open("website/frontend/about.html", "w") as f:
    f.write(html)

print("Fixed marquee boundaries!")
