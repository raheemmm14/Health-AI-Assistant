import torch
import sys

print(f"Python Version: {sys.version}")
print(f"PyTorch Version: {torch.__version__}")

# Check if GPU is detected
if torch.cuda.is_available():
    print(f"✅ Success! GPU Detected: {torch.cuda.get_device_name(0)}")
else:
    print("❌ Error: GPU not detected. You are running on CPU.")