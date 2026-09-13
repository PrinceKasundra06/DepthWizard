import sys

with open("website/frontend/css/style.css", "r") as f:
    css = f.read()

bad_loader = """.loading-overlay {
    display: none;
    position: absolute;
    inset: 0;
    background: rgba(3, 3, 3, 0.8);
    backdrop-filter: blur(24px);
    border-radius: inherit;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 10;
}
.orb {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: 2px solid rgba(255,255,255,0.1);
    border-top-color: #ffffff;
    animation: spinOrb 0.8s linear infinite;
    margin-bottom: 1.5rem;
}
.loading-text {
    font-size: 0.8rem;
    font-weight: 500;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
}"""

good_loader = """.loading-overlay {
    display: none;
    position: fixed; /* Cover the whole screen */
    inset: 0;
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(40px);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    animation: fadeInOverlay 0.5s ease forwards;
}

@keyframes fadeInOverlay {
    from { opacity: 0; backdrop-filter: blur(0px); }
    to { opacity: 1; backdrop-filter: blur(40px); }
}

.neural-loader {
    position: relative;
    width: 100px;
    height: 100px;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Outer Ring */
.neural-loader::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 50%;
    border: 2px solid transparent;
    border-top-color: rgba(255,255,255,0.8);
    border-right-color: rgba(255,255,255,0.2);
    animation: spinOrb 1.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
    box-shadow: 0 0 20px rgba(255,255,255,0.1);
}

/* Inner Ring */
.neural-loader::after {
    content: '';
    position: absolute;
    inset: 15px;
    border-radius: 50%;
    border: 2px solid transparent;
    border-bottom-color: rgba(255,255,255,0.6);
    border-left-color: rgba(255,255,255,0.1);
    animation: spinOrbReverse 1s linear infinite;
}

/* Core Dot */
.neural-core {
    width: 12px;
    height: 12px;
    background: #ffffff;
    border-radius: 50%;
    box-shadow: 0 0 20px #ffffff, 0 0 40px #ffffff;
    animation: pulseCore 2s ease-in-out infinite;
}

@keyframes spinOrbReverse {
    from { transform: rotate(360deg); }
    to { transform: rotate(0deg); }
}

@keyframes pulseCore {
    0%, 100% { transform: scale(0.8); opacity: 0.5; }
    50% { transform: scale(1.2); opacity: 1; }
}

.loading-text {
    font-size: 13px;
    font-weight: 600;
    color: #ffffff;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    text-shadow: 0 0 10px rgba(255,255,255,0.5);
    animation: pulseText 2s ease-in-out infinite;
}

@keyframes pulseText {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}"""

css = css.replace(bad_loader, good_loader)

with open("website/frontend/css/style.css", "w") as f:
    f.write(css)

print("Upgraded loader CSS!")

# Now update upload.html to use the new loader structure
with open("website/frontend/upload.html", "r") as f:
    html = f.read()

bad_html = """        <div class="loading-overlay" id="loadingOverlay">
            <div class="orb"></div>
            <div class="loading-text" id="loadingText">Processing Neural Depth...</div>
        </div>"""

good_html = """        <div class="loading-overlay" id="loadingOverlay">
            <div class="neural-loader">
                <div class="neural-core"></div>
            </div>
            <div class="loading-text" id="loadingText">Processing Neural Depth...</div>
            <div style="margin-top: 1rem; font-size: 10px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.1em;">Please wait. Apple MPS Engine is active.</div>
        </div>"""

html = html.replace(bad_html, good_html)

with open("website/frontend/upload.html", "w") as f:
    f.write(html)

print("Upgraded loader HTML!")

# Also update main.js so the text changes smoothly with a fade
with open("website/frontend/js/main.js", "r") as f:
    js = f.read()

bad_js = """        let seqIndex = 0;
        const seqInterval = setInterval(() => {
            seqIndex = (seqIndex + 1) % loadingSequence.length;
            loadingText.innerText = loadingSequence[seqIndex];
        }, 8000);"""

good_js = """        let seqIndex = 0;
        const seqInterval = setInterval(() => {
            seqIndex = (seqIndex + 1) % loadingSequence.length;
            
            // Smooth text transition
            loadingText.style.opacity = '0';
            setTimeout(() => {
                loadingText.innerText = loadingSequence[seqIndex];
                loadingText.style.opacity = '1';
            }, 300);
            
        }, 6000); // Change text every 6 seconds"""

js = js.replace(bad_js, good_js)

with open("website/frontend/js/main.js", "w") as f:
    f.write(js)

print("Upgraded loader JS!")
