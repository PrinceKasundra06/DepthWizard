<div align="center">
  <img src="https://img.shields.io/badge/AI-TripoSR-000000?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Frontend-Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />

  <br><br>

  <h1>🪄 DepthWizard Studio</h1>
  <p><b>State-of-the-art Neural Networks for instant 2D-to-3D geometric mesh generation.</b></p>
</div>

<br>

## 🌌 Overview

DepthWizard is an advanced, ultra-premium web application that instantly converts flat 2D images into immersive 3D flythroughs and True-360 geometric meshes. Built on top of bleeding-edge AI models (TripoSR), DepthWizard hallucinates the unseen geometry of subjects in less than a second. 

Featuring a cinematic, 10,000-particle WebGL background and an Apple-inspired glassmorphic UI, the studio is designed to feel like magic.

## ✨ Core Features

* **True 360° Mesh AI**: Utilizes the highly optimized **TripoSR** feed-forward 3D generative model to predict dense triplane representations from visual features, exporting perfect `.OBJ` meshes.
* **Cinematic Glass UI**: A breathtaking, premium dashboard interface featuring dynamic frosted glass pills, ultra-smooth CSS physics, and an interactive 3D upload dropzone that physically tracks your mouse.
* **Interactive 3D Viewer**: Inspect your generated meshes in real-time. Features include dynamic lighting rigs (Studio, Dramatic, Sunset, Neon), adjustable roughness/metalness materials, auto-spin, and wireframe topology inspection.
* **Local Tensor Privacy**: Everything processes locally on your hardware. No cloud fees, no API limits, and complete data privacy.
* **Background Removal Pipeline**: Automatically utilizes `rembg` to strip backgrounds and center subjects perfectly before feeding them into the inference engine.

## 🏗️ Architecture

The application is split into two perfectly decoupled environments:

1. **Frontend (The Studio)**: Pure HTML, CSS, and vanilla JavaScript powered by **Three.js** for real-time WebGL rendering and particle physics.
2. **Backend (The Neural Engine)**: A **FastAPI** Python server running **PyTorch** that manages inference, routing, and file generation.

## 🚀 Installation & Local Deployment

### 1. Clone the Repository
```bash
git clone https://github.com/PrinceKasundra06/DepthWizard.git
cd DepthWizard
```

### 2. Setup the Neural Engine (Backend)
Ensure you have Python 3.9+ installed. It is highly recommended to use a virtual environment.
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install all heavy AI dependencies
pip install fastapi uvicorn torch torchvision torchaudio numpy trimesh Pillow rembg
```

### 3. Launch the Studio
You can launch both the frontend and the AI backend simultaneously using a single command from inside the backend folder:

```bash
cd website/backend
python main.py
```

*Wait for the models to load into memory.* Once the console says `Application startup complete`, open your web browser and navigate to:
👉 **http://localhost:8000**

## 👥 The Team

DepthWizard was brought to life by a team of visionary developers:
* **Prince Kasundra**
* **Het Chikhaliya**
* **Prachi Lodhia**
* **Kashyap Dubariya**
* **Vishwa Gondaliya**
* **Parth Lakhdhir**

---
<div align="center">
  <i>"Breathing life into pixels."</i>
</div>
