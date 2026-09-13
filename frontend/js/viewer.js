document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('canvas-container');
    if (!container) return;

    // Retrieve the URLs from localStorage
    const objUrl = localStorage.getItem('depthWizard_objUrl');
    const depthUrl = localStorage.getItem('depthWizard_depthUrl');

    // Scene setup
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x050508, 0.005);

    // Camera setup
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.set(0, 0, 150);

    // Renderer setup
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setClearColor(0x050508, 0); // Transparent background
    container.appendChild(renderer.domElement);

    // Controls
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    
    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight.position.set(100, 100, 50);
    scene.add(dirLight);

    let modelMesh = null;

    if (objUrl) {
        // Load the generated OBJ model
        const loader = new THREE.OBJLoader();
        loader.load(
            objUrl,
            function (object) {
                object.traverse(function(child) {
                    if (child.isMesh) {
                        child.material = new THREE.MeshStandardMaterial({
                            color: 0xffffff,
                            wireframe: false,
                            roughness: 0.2,
                            metalness: 0.8,
                            side: THREE.DoubleSide
                        });
                        
                        // Center the object
                        child.geometry.computeBoundingBox();
                        const boundingBox = child.geometry.boundingBox;
                        const center = new THREE.Vector3();
                        boundingBox.getCenter(center);
                        child.geometry.translate(-center.x, -center.y, -center.z);
                    }
                });
                
                modelMesh = object;
                scene.add(object);

                // Adjust camera based on object size
                const box = new THREE.Box3().setFromObject(object);
                const size = box.getSize(new THREE.Vector3()).length();
                camera.position.z = size * 0.8;
            },
            function (xhr) {
                console.log((xhr.loaded / xhr.total * 100) + '% loaded');
            },
            function (error) {
                console.error('An error happened loading the OBJ', error);
                createPlaceholder();
            }
        );
    } else {
        createPlaceholder();
    }

    function createPlaceholder() {
        const geometry = new THREE.PlaneGeometry(200, 200, 64, 64);
        const positionAttribute = geometry.attributes.position;
        const vertex = new THREE.Vector3();
        for (let i = 0; i < positionAttribute.count; i++) {
            vertex.fromBufferAttribute(positionAttribute, i);
            const z = Math.sin(vertex.x * 0.1) * Math.cos(vertex.y * 0.1) * 10;
            const z2 = Math.sin(vertex.x * 0.02) * Math.cos(vertex.y * 0.02) * 20;
            positionAttribute.setZ(i, z + z2);
        }
        geometry.computeVertexNormals();

        const material = new THREE.MeshStandardMaterial({
            color: 0xffffff,
            wireframe: true,
            transparent: true,
            opacity: 0.2
        });

        modelMesh = new THREE.Mesh(geometry, material);
        modelMesh.rotation.x = -Math.PI / 2;
        scene.add(modelMesh);
        camera.position.set(0, 30, 50);
        controls.maxPolarAngle = Math.PI / 2 - 0.05;
    }

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);

        // Slowly rotate model
        if (modelMesh) {
            modelMesh.rotation.y += 0.002;
        }

        controls.update();
        renderer.render(scene, camera);
    }
    
    animate();

    // Handle Window Resize
    window.addEventListener('resize', () => {
        if (container) {
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        }
    });

    // Handle download buttons
    const downloadBtns = document.querySelectorAll('.viewer-controls .btn');
    if (downloadBtns.length >= 2) {
        downloadBtns[0].addEventListener('click', () => {
            if (objUrl) {
                const a = document.createElement('a');
                a.href = objUrl;
                a.download = 'model.obj';
                a.click();
            } else {
                alert("No model to download.");
            }
        });
        
        downloadBtns[1].addEventListener('click', () => {
            if (depthUrl) {
                const a = document.createElement('a');
                a.href = depthUrl;
                a.download = 'depth_map.png';
                a.click();
            } else {
                alert("No depth map to download.");
            }
        });
    }
});
