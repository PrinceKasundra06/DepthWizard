// --- Custom Cursor Logic ---
const cursorDot = document.querySelector('.cursor-dot');
const cursorOutline = document.querySelector('.cursor-outline');

if (cursorDot && cursorOutline) {
    window.addEventListener('mousemove', (e) => {
        const posX = e.clientX;
        const posY = e.clientY;
        
        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;
        
        // Slight delay on outline for smooth trailing effect
        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });

    // Expand cursor on interactive elements
    const interactives = document.querySelectorAll('a, button, input, .upload-box');
    interactives.forEach(el => {
        el.addEventListener('mouseenter', () => cursorOutline.classList.add('hovering'));
        el.addEventListener('mouseleave', () => cursorOutline.classList.remove('hovering'));
    });
}

// --- 3D Tilt Effect on Feature Cards ---
const tiltCards = document.querySelectorAll('.tilt-card');
tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = ((y - centerY) / centerY) * -10; // Max 10 deg
        const rotateY = ((x - centerX) / centerX) * 10;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
        card.style.transition = 'transform 0.5s ease';
    });
    card.addEventListener('mouseenter', () => {
        card.style.transition = 'none';
    });
});

// --- Upload Page Logic ---
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const previewContainer = document.getElementById('previewContainer');
const imagePreview = document.getElementById('imagePreview');
const resetBtn = document.getElementById('resetBtn');
const generateBtn = document.getElementById('generateBtn');
const loadingOverlay = document.getElementById('loadingOverlay');
const loadingText = document.getElementById('loadingText');

let selectedFile = null;

if (dropZone) {
    // Drag and Drop Events
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => dropZone.classList.add('dragover'), false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => dropZone.classList.remove('dragover'), false);
    });

    dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
    });

    fileInput.addEventListener('change', function() {
        handleFiles(this.files);
    });

    function handleFiles(files) {
        if (files.length > 0) {
            selectedFile = files[0];
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                dropZone.style.display = 'none';
                previewContainer.style.display = 'block';
            }
            reader.readAsDataURL(selectedFile);
        }
    }

    resetBtn.addEventListener('click', () => {
        selectedFile = null;
        fileInput.value = '';
        dropZone.style.display = 'block';
        previewContainer.style.display = 'none';
    });

    // Dynamic Loading Text Sequence
    const loadingSequence = [
        "Analyzing Image Composition...",
        "Extracting Foreground Subject (rembg)...",
        "Warming up Neural Network...",
        "TripoSR: Hallucinating 360° Depth...",
        "Running Marching Cubes Algorithm...",
        "Constructing White Clay Mesh...",
        "Optimizing 3D Geometry...",
        "Almost there..."
    ];

    generateBtn.addEventListener('click', async () => {
        if (!selectedFile) return;

        // Start Cinematic Loader
        loadingOverlay.style.display = 'flex';
        
        let seqIndex = 0;
        const seqInterval = setInterval(() => {
            seqIndex = (seqIndex + 1) % loadingSequence.length;
            
            // Smooth text transition
            loadingText.style.opacity = '0';
            setTimeout(() => {
                loadingText.innerText = loadingSequence[seqIndex];
                loadingText.style.opacity = '1';
            }, 300);
            
        }, 6000); // Change text every 6 seconds // Change text every 8 seconds

        const formData = new FormData();
        formData.append('file', selectedFile);
        formData.append('is_360', 'true'); // Force 360 mode

        try {
            const response = await fetch('/api/process', {
                method: 'POST',
                body: formData
            });

            clearInterval(seqInterval);

            if (response.ok) {
                const data = await response.json();
                
                // Store URLs for viewer
                localStorage.setItem('depthWizard_objUrl', data.obj_url);
                localStorage.setItem('depthWizard_is360', 'true');
                if(data.stats) {
                    localStorage.setItem('depthWizard_vertices', data.stats.vertices);
                }

                // Smooth fade transition
                document.body.style.opacity = '0';
                document.body.style.transition = 'opacity 0.5s';
                setTimeout(() => {
                    window.location.href = 'viewer.html';
                }, 500);
            } else {
                loadingOverlay.style.display = 'none';
                const errData = await response.json();
                alert('Error processing image: ' + errData.error);
            }
        } catch (error) {
            clearInterval(seqInterval);
            loadingOverlay.style.display = 'none';
            alert('Connection error: ' + error.message);
        }
    });
}

// --- Global Background 3D Objects ---
function initBackground3D() {
    const canvas = document.getElementById('bg-canvas');
    if (!canvas || typeof THREE === 'undefined') return;

    const container = canvas.parentElement;
    const scene = new THREE.Scene();
    // Add fog to fade out edges
    scene.fog = new THREE.FogExp2(0x000000, 0.015);
    
    // Camera
    const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.set(0, 30, 60);
    camera.lookAt(0, 0, 0);

    // Renderer
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Massive Particle Wave Grid
    const particleCount = 10000;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const scales = new Float32Array(particleCount);
    
    let i = 0;
    let j = 0;
    
    // Create a 100x100 grid of points
    const gridSize = 100;
    const spacing = 2.5;
    const offset = (gridSize * spacing) / 2;

    for ( let ix = 0; ix < gridSize; ix ++ ) {
        for ( let iy = 0; iy < gridSize; iy ++ ) {
            positions[ i ] = ix * spacing - offset; // x
            positions[ i + 1 ] = 0;                 // y (will be animated)
            positions[ i + 2 ] = iy * spacing - offset; // z
            scales[ j ] = 1;
            i += 3;
            j ++;
        }
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('scale', new THREE.BufferAttribute(scales, 1));

    // Custom shader material for beautiful glowing dots
    const material = new THREE.ShaderMaterial({
        uniforms: {
            color: { value: new THREE.Color(0xffffff) },
        },
        vertexShader: `
            attribute float scale;
            void main() {
                vec4 mvPosition = modelViewMatrix * vec4( position, 1.0 );
                gl_PointSize = scale * ( 300.0 / - mvPosition.z );
                gl_Position = projectionMatrix * mvPosition;
            }
        `,
        fragmentShader: `
            uniform vec3 color;
            void main() {
                if ( length( gl_PointCoord - vec2( 0.5, 0.5 ) ) > 0.475 ) discard;
                gl_FragColor = vec4( color, 0.25 ); // Semi-transparent white
            }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });

    const particles = new THREE.Points(geometry, material);
    scene.add(particles);

    // Interactive Mouse Rotation
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;

    container.addEventListener('mousemove', (event) => {
        const rect = container.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        mouseX = (x - container.clientWidth / 2);
        mouseY = (y - container.clientHeight / 2);
    });

    let count = 0;
    
    function animate() {
        requestAnimationFrame(animate);

        // Undulate the particles like an ocean wave
        const positions = particles.geometry.attributes.position.array;
        const scales = particles.geometry.attributes.scale.array;

        let i = 0, j = 0;
        for ( let ix = 0; ix < gridSize; ix ++ ) {
            for ( let iy = 0; iy < gridSize; iy ++ ) {
                // Animate Y position using sine waves
                positions[ i + 1 ] = ( Math.sin( ( ix + count ) * 0.3 ) * 5 ) +
                                     ( Math.sin( ( iy + count ) * 0.5 ) * 5 );
                // Pulse the size
                scales[ j ] = ( Math.sin( ( ix + count ) * 0.3 ) + 1 ) * 2 +
                              ( Math.sin( ( iy + count ) * 0.5 ) + 1 ) * 2;
                i += 3;
                j ++;
            }
        }

        particles.geometry.attributes.position.needsUpdate = true;
        particles.geometry.attributes.scale.needsUpdate = true;
        
        count += 0.05; // Speed of the wave

        // Mouse Parallax Effect on camera
        targetX = mouseX * 0.05;
        targetY = mouseY * 0.05;
        
        camera.position.x += (targetX - camera.position.x) * 0.02;
        camera.position.y += (-targetY + 40 - camera.position.y) * 0.02; // Base height 40
        camera.lookAt(0, 0, 0);

        renderer.render(scene, camera);
    }
    
    animate();

    // Resize handler
    window.addEventListener('resize', () => {
        if (!container) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    initBackground3D();
});

// 3D Tilt Effect for Dropzone
const dropZoneEl = document.getElementById('dropZone');
const dropGlare = document.getElementById('dropGlare');
if (dropZoneEl && dropGlare) {
    dropZoneEl.addEventListener('mousemove', (e) => {
        // Don't tilt if we are dragging a file (dragover handles its own transform)
        if (dropZoneEl.style.borderColor === 'rgba(0, 150, 255, 0.5)') return;

        const rect = dropZoneEl.getBoundingClientRect();
        const x = e.clientX - rect.left; // x position within the element.
        const y = e.clientY - rect.top;  // y position within the element.

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * -8; // Max 8 degrees
        const rotateY = ((x - centerX) / centerX) * 8;

        // Apply 3D transform
        dropZoneEl.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        
        // Move Glare
        dropGlare.style.opacity = '1';
        dropGlare.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.15) 0%, transparent 60%)`;
    });

    dropZoneEl.addEventListener('mouseleave', () => {
        if (dropZoneEl.style.borderColor === 'rgba(0, 150, 255, 0.5)') return;
        dropZoneEl.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
        dropGlare.style.opacity = '0';
        
        // Brief transition for resetting
        dropZoneEl.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
    });
    
    dropZoneEl.addEventListener('mouseenter', () => {
        // Remove transition while moving so it tracks instantly
        dropZoneEl.style.transition = 'none';
    });
}

// Magic Dust Particles inside Dropzone
const dustContainer = document.getElementById('magicDustContainer');
if (dustContainer) {
    for (let i = 0; i < 20; i++) {
        let p = document.createElement('div');
        p.style.position = 'absolute';
        p.style.width = Math.random() * 3 + 'px';
        p.style.height = p.style.width;
        p.style.background = 'rgba(255,255,255,0.8)';
        p.style.borderRadius = '50%';
        p.style.boxShadow = '0 0 10px rgba(255,255,255,0.8)';
        p.style.left = Math.random() * 100 + '%';
        p.style.top = Math.random() * 100 + '%';
        p.style.opacity = Math.random() * 0.5;
        p.style.animation = `floatParticle ${Math.random() * 5 + 3}s linear infinite alternate`;
        dustContainer.appendChild(p);
    }
}
