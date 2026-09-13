import sys
import re

with open("website/frontend/about.html", "r") as f:
    html = f.read()

target = """                        <div style="display: flex; flex-direction: column; align-items: center;">
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
                        </div>"""

replacement = """                        <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
                            <span style="font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.3em; margin-bottom: 2rem;">Forged by</span>
                            
                            <!-- Infinite Marquee Container -->
                            <div class="marquee-container" style="width: 100vw; max-width: 100vw; overflow: hidden; white-space: nowrap; position: relative; padding: 2rem 0; mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent); -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);">
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
                        </div>"""

html = html.replace(target, replacement)

style_target = "</style>"
style_replacement = """
        .marquee-content-wrapper {
            animation: scrollMarquee 20s linear infinite;
        }
        .marquee-container:hover .marquee-content-wrapper {
            animation-play-state: paused;
        }
        .marquee-name {
            font-size: 2.5rem;
            font-weight: 500;
            color: rgba(255,255,255,0.4);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: crosshair;
        }
        .marquee-name:hover {
            color: #fff;
            text-shadow: 0 0 30px rgba(255,255,255,0.8);
            transform: scale(1.1);
        }
        .marquee-star {
            color: rgba(255,255,255,0.1);
            font-size: 1.5rem;
        }
        @keyframes scrollMarquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
    </style>"""

html = html.replace(style_target, style_replacement)

with open("website/frontend/about.html", "w") as f:
    f.write(html)

print("Marquee added!")
