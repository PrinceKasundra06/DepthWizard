import sys, os
import torch
sys.path.append(os.path.join(os.getcwd(), "website/backend/TripoSR"))
from tsr.system import TSR
print("Imported TSR")
device = "mps" if torch.backends.mps.is_available() else "cpu"
model = TSR.from_pretrained("stabilityai/TripoSR", config_name="config.yaml", weight_name="model.ckpt")
print("Model loaded")
