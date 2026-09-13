document.addEventListener('DOMContentLoaded', () => {
    // File Upload Logic (only runs on upload.html)
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const previewContainer = document.getElementById('previewContainer');
    const imagePreview = document.getElementById('imagePreview');
    const resetBtn = document.getElementById('resetBtn');
    const generateBtn = document.getElementById('generateBtn');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const loadingText = document.getElementById('loadingText');

    if (dropZone) {
        // Handle Drag & Drop
        dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropZone.classList.add('dragover');
        });

        dropZone.addEventListener('dragleave', () => {
            dropZone.classList.remove('dragover');
        });

        dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropZone.classList.remove('dragover');
            if (e.dataTransfer.files.length) {
                handleFile(e.dataTransfer.files[0]);
            }
        });

        // Handle File Input Selection
        fileInput.addEventListener('change', function() {
            if (this.files.length) {
                handleFile(this.files[0]);
            }
        });

        // Reset
        resetBtn.addEventListener('click', () => {
            dropZone.style.display = 'block';
            previewContainer.style.display = 'none';
            fileInput.value = '';
            imagePreview.src = '';
        });

        // Integrate with New Backend
        generateBtn.addEventListener('click', async () => {
            if (!fileInput.files.length) return;
            
            loadingOverlay.style.display = 'flex';
            loadingText.innerText = 'Extracting depth features... (1/2)';
            
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);
            
            try {
                // Step 1: Upload and extract depth map
                const uploadResponse = await fetch('/api/v1/projects/upload', {
                    method: 'POST',
                    body: formData
                });
                
                if (!uploadResponse.ok) {
                    throw new Error('Failed to process image depth.');
                }
                
                const projectData = await uploadResponse.json();
                const projectId = projectData.project_id;
                
                // Step 2: Generate 3D Mesh
                loadingText.innerText = 'Generating 3D mesh... (2/2)';
                const meshResponse = await fetch('/api/v1/mesh/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ project_id: projectId, format: 'obj' })
                });
                
                if (!meshResponse.ok) {
                    throw new Error('Failed to generate 3D mesh.');
                }
                
                const meshData = await meshResponse.json();
                
                // Store result paths in local storage to use in viewer.html
                localStorage.setItem('depthWizard_objUrl', meshData.mesh_url);
                localStorage.setItem('depthWizard_depthUrl', projectData.depth_map_url);
                
                window.location.href = 'viewer.html';
            } catch (err) {
                alert(err.message);
                loadingOverlay.style.display = 'none';
            }
        });

        function handleFile(file) {
            if (!file.type.startsWith('image/')) {
                alert('Please upload an image file (PNG, JPG, JPEG).');
                return;
            }

            // Assign file to the input if dropped so it can be picked up by generateBtn logic
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            fileInput.files = dataTransfer.files;

            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                dropZone.style.display = 'none';
                previewContainer.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    }

    // --- Scroll Reveal Animations ---
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };
    
    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('active');
            observer.unobserve(entry.target); // Stop observing once revealed
        });
    }, revealOptions);
    
    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });
});
