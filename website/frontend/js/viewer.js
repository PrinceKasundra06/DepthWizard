document.addEventListener('DOMContentLoaded', () => {
    const objUrl = localStorage.getItem('depthWizard_objUrl');
    const is360 = localStorage.getItem('depthWizard_is360') === 'true';

    if (!objUrl) {
        window.location.href = 'upload.html';
        return;
    }

    const container = document.getElementById('canvas-container');
    if (!container) return;

    // ThreeJS Setup
    const scene = new THREE.Scene();
    
    // Camera
    const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 100);
    camera.position.set(0, 2, 5);

    // Renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setClearColor(0x000000, 0); // Transparent background
    renderer.outputEncoding = THREE.sRGBEncoding;
    container.appendChild(renderer.domElement);

    // Orbit Controls
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.autoRotate = true;
    controls.autoRotateSpeed = 2.0;

    // Lighting (Dramatic White Clay setup)
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const dirLight1 = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight1.position.set(10, 20, 15);
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0xffffff, 0.5);
    dirLight2.position.set(-10, -10, -15);
    scene.add(dirLight2);
    
    // Add professional viewport grid and axes
    const gridHelper = new THREE.GridHelper(10, 20, 0x444444, 0x222222);
    gridHelper.position.y = -1.5; // Offset below object
    scene.add(gridHelper);
    
    const axesHelper = new THREE.AxesHelper(2);
    axesHelper.position.y = -1.5;
    scene.add(axesHelper);

    let mainObject = null;
    let mainMaterial = null;

    // Load OBJ
    const loader = new THREE.OBJLoader();
    loader.load(
        objUrl,
        function (object) {
            mainObject = object;
            
            object.traverse(function(child) {
                if (child.isMesh) {
                    child.geometry.computeVertexNormals();
                    
                    // Pure White Clay Material
                    mainMaterial = new THREE.MeshStandardMaterial({
                        color: 0xffffff,
                        roughness: document.getElementById('slider-roughness') ? document.getElementById('slider-roughness').value / 100 : 0.8,
                        metalness: document.getElementById('slider-metalness') ? document.getElementById('slider-metalness').value / 100 : 0.1,
                        side: THREE.DoubleSide
                    });
                    child.material = mainMaterial;

                    // Center Geometry
                    child.geometry.computeBoundingBox();
                    const boundingBox = child.geometry.boundingBox;
                    const center = new THREE.Vector3();
                    boundingBox.getCenter(center);
                    child.geometry.translate(-center.x, -center.y, -center.z);

                    // Estimate Height stat (bounding box height)
                    const size = new THREE.Vector3();
                    boundingBox.getSize(size);
                    const hStat = document.getElementById('heightDisplay');
                    if (hStat) hStat.innerText = (size.y * 1.5).toFixed(2) + ' m';
                    
                    // Extract exact vertex and face counts from the loaded geometry!
                    const vertexCount = child.geometry.attributes.position.count;
                    // Faces = total indices / 3 (if indexed) or vertices / 3 (if unindexed)
                    const faceCount = child.geometry.index ? child.geometry.index.count / 3 : vertexCount / 3;
                    
                    const vStat = document.getElementById('stat-vertices');
                    if (vStat) vStat.innerText = vertexCount.toLocaleString();
                    
                    const fStat = document.getElementById('stat-faces');
                    if (fStat) fStat.innerText = faceCount.toLocaleString();
                }
            });

            // Scale to fit view
            const box = new THREE.Box3().setFromObject(object);
            const size = new THREE.Vector3();
            box.getSize(size);
            const maxDim = Math.max(size.x, size.y, size.z);
            const scale = 3.0 / maxDim;
            object.scale.set(scale, scale, scale);

            scene.add(object);
        },
        function (xhr) {
            // Optional: loading progress
        },
        function (error) { 
            console.error('Error loading OBJ', error);
        }
    );

    // Download Button
    const downloadObjBtn = document.getElementById('downloadObjBtn');
    if (downloadObjBtn) {
        downloadObjBtn.addEventListener('click', async () => {
            if (objUrl) {
                try {
                    downloadObjBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Preparing...';
                    downloadObjBtn.style.pointerEvents = 'none';
                    
                    const response = await fetch(objUrl);
                    const blob = await response.blob();
                    
                    // Force the blob to be text/plain so the browser doesn't try to zip it or guess its type
                    const safeBlob = new Blob([blob], { type: 'text/plain' });
                    const safeUrl = URL.createObjectURL(safeBlob);
                    
                    const a = document.createElement('a');
                    a.href = safeUrl;
                    a.download = 'depthwizard_model.obj';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    
                    URL.revokeObjectURL(safeUrl);
                    
                    downloadObjBtn.innerHTML = '<i class="fa-solid fa-download"></i> Export OBJ';
                    downloadObjBtn.style.pointerEvents = 'all';
                } catch(e) {
                    console.error("Export failed:", e);
                    downloadObjBtn.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Error';
                }
            }
        });
    }

    // Wire up HUD Buttons
    const btnWireframe = document.getElementById('btn-wireframe');
    let isWireframe = false;
    if (btnWireframe) {
        btnWireframe.addEventListener('click', () => {
            isWireframe = !isWireframe;
            btnWireframe.style.background = isWireframe ? 'rgba(255,255,255,0.1)' : 'transparent';
            if (mainObject) {
                mainObject.traverse((child) => {
                    if (child.isMesh) child.material.wireframe = isWireframe;
                });
            }
        });
    }
    
    const btnAutoRotate = document.getElementById('btn-autorotate');
    if (btnAutoRotate) {
        btnAutoRotate.addEventListener('click', () => {
            controls.autoRotate = !controls.autoRotate;
            btnAutoRotate.style.background = controls.autoRotate ? 'rgba(255,255,255,0.1)' : 'transparent';
        });
    }
    
    const btnResetCam = document.getElementById('btn-reset-cam');
    if (btnResetCam) {
        btnResetCam.addEventListener('click', () => {
            controls.reset();
            camera.position.set(0, 2, 5);
        });
    }

    // --- Sidebar Controls ---
    const sliderRoughness = document.getElementById('slider-roughness');
    const sliderMetalness = document.getElementById('slider-metalness');
    
    if (sliderRoughness) {
        sliderRoughness.addEventListener('input', (e) => {
            if (mainMaterial) mainMaterial.roughness = e.target.value / 100;
        });
    }
    
    if (sliderMetalness) {
        sliderMetalness.addEventListener('input', (e) => {
            if (mainMaterial) mainMaterial.metalness = e.target.value / 100;
        });
    }
    
    // Lighting Environments
    const lightBtns = document.querySelectorAll('.light-btn');
    
    function resetLightBtns() {
        lightBtns.forEach(btn => {
            btn.style.background = 'rgba(255,255,255,0.04)';
            btn.style.borderColor = 'rgba(255,255,255,0.1)';
        });
    }
    
    function setActiveLightBtn(id) {
        resetLightBtns();
        const btn = document.getElementById(id);
        if (btn) {
            btn.style.background = 'rgba(255,255,255,0.1)';
            btn.style.borderColor = 'rgba(255,255,255,0.2)';
        }
    }
    
    document.getElementById('btn-light-studio')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-studio');
        ambientLight.color.setHex(0xffffff);
        ambientLight.intensity = 0.5;
        dirLight1.color.setHex(0xffffff);
        dirLight1.intensity = 1.2;
        dirLight1.position.set(10, 20, 15);
        dirLight2.color.setHex(0xffffff);
        dirLight2.intensity = 0.5;
    });
    
    document.getElementById('btn-light-dramatic')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-dramatic');
        ambientLight.color.setHex(0x444444);
        ambientLight.intensity = 0.2;
        dirLight1.color.setHex(0xffffff);
        dirLight1.intensity = 2.0;
        dirLight1.position.set(15, 5, 0); // Side light
        dirLight2.intensity = 0.0;
    });
    
    document.getElementById('btn-light-sunset')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-sunset');
        ambientLight.color.setHex(0xffaa55);
        ambientLight.intensity = 0.4;
        dirLight1.color.setHex(0xff6600);
        dirLight1.intensity = 1.5;
        dirLight1.position.set(-20, 5, 20); // Low angle sunset
        dirLight2.color.setHex(0x440088); // Purple fill
        dirLight2.intensity = 0.8;
        dirLight2.position.set(20, 10, -10);
    });
    
    document.getElementById('btn-light-neon')?.addEventListener('click', () => {
        setActiveLightBtn('btn-light-neon');
        ambientLight.color.setHex(0x111111);
        ambientLight.intensity = 0.1;
        dirLight1.color.setHex(0x00ffff); // Cyan
        dirLight1.intensity = 2.5;
        dirLight1.position.set(10, 0, 10);
        dirLight2.color.setHex(0xff00ff); // Magenta
        dirLight2.intensity = 2.5;
        dirLight2.position.set(-10, 5, -10);
    });

        // Handle Window Resize
    window.addEventListener('resize', () => {
        if (!container) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);
        controls.update();
        renderer.render(scene, camera);
    }
    animate();
});
