import sys

with open("website/frontend/js/main.js", "r") as f:
    code = f.read()

bad_logic_start = "// --- Global Background 3D Objects ---"

new_bg_logic = """// --- Global Background 3D Objects ---
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
                gl_FragColor = vec4( color, 0.4 ); // Semi-transparent white
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
"""

idx = code.find(bad_logic_start)
if idx != -1:
    code = code[:idx] + new_bg_logic

with open("website/frontend/js/main.js", "w") as f:
    f.write(code)
    
print("Massive particles added!")
