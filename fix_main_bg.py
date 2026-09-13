import sys

with open("website/frontend/js/main.js", "r") as f:
    code = f.read()

# Replace the initBackground3D function
bad_logic_start = "// --- Global Background 3D Objects ---"

new_bg_logic = """// --- Global Background 3D Objects ---
function initBackground3D() {
    const canvas = document.getElementById('bg-canvas');
    if (!canvas || typeof THREE === 'undefined') return;

    const container = canvas.parentElement;
    const scene = new THREE.Scene();
    
    // Camera
    const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.z = 30;

    // Renderer
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Create a beautiful, complex wireframe Icosahedron
    const geometry = new THREE.IcosahedronGeometry(12, 2);
    
    // Add some noise to the vertices to make it look organic
    const positionAttribute = geometry.getAttribute('position');
    const vertex = new THREE.Vector3();
    for (let i = 0; i < positionAttribute.count; i++) {
        vertex.fromBufferAttribute(positionAttribute, i);
        vertex.normalize().multiplyScalar(12 + Math.random() * 0.8);
        positionAttribute.setXYZ(i, vertex.x, vertex.y, vertex.z);
    }
    geometry.computeVertexNormals();

    const material = new THREE.MeshStandardMaterial({
        color: 0x88ccff,
        wireframe: true,
        transparent: true,
        opacity: 0.15,
        emissive: 0x112244,
        emissiveIntensity: 0.5
    });
    
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    // Inner solid core
    const coreGeo = new THREE.IcosahedronGeometry(6, 1);
    const coreMat = new THREE.MeshStandardMaterial({
        color: 0xffffff,
        roughness: 0.2,
        metalness: 0.8,
        transparent: true,
        opacity: 0.05
    });
    const core = new THREE.Mesh(coreGeo, coreMat);
    scene.add(core);

    // Lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    
    const pointLight = new THREE.PointLight(0xffffff, 2, 100);
    pointLight.position.set(20, 20, 20);
    scene.add(pointLight);

    const pointLight2 = new THREE.PointLight(0x4488ff, 3, 100);
    pointLight2.position.set(-20, -20, 20);
    scene.add(pointLight2);

    // Interactive Mouse Rotation
    let mouseX = 0;
    let mouseY = 0;
    let targetRotationX = 0;
    let targetRotationY = 0;

    // Listen on the container so we only rotate when hovering the viewport
    container.addEventListener('mousemove', (event) => {
        const rect = container.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        
        mouseX = (x / container.clientWidth) * 2 - 1;
        mouseY = -(y / container.clientHeight) * 2 + 1;
    });

    const clock = new THREE.Clock();
    
    function animate() {
        requestAnimationFrame(animate);
        const delta = clock.getDelta();

        // Base slow rotation
        sphere.rotation.x += 0.05 * delta;
        sphere.rotation.y += 0.1 * delta;
        
        core.rotation.x -= 0.1 * delta;
        core.rotation.y -= 0.05 * delta;

        // Add mouse interaction (spring physics)
        targetRotationX = mouseY * 0.5;
        targetRotationY = mouseX * 0.5;
        
        sphere.rotation.x += (targetRotationX - sphere.rotation.x) * 0.05;
        sphere.rotation.y += (targetRotationY - sphere.rotation.y) * 0.05;

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
    
print("Fixed main.js background 3D!")
