import sys
import importlib

# List of libraries to check
libraries = {
    "numpy": "Data Science (Math)",
    "pandas": "Data Science (Tables)",
    "sklearn": "Machine Learning",
    "matplotlib": "Plotting",
    "selenium": "Automation",
    "playwright": "Modern Automation",
    "torch": "AI (Deep Learning)",
    "tensorflow": "AI (Deep Learning)",
}

print(f"Checking Python Environment: {sys.version.split()[0]}")
print("-" * 50)

for lib, purpose in libraries.items():
    try:
        module = importlib.import_module(lib)
        version = getattr(module, "__version__", "Unknown")
        print(f"✅ {lib.ljust(15)} | {version.ljust(10)} | {purpose}")
        
        # Special Check for GPU (Torch)
        if lib == "torch":
            if module.cuda.is_available():
                print(f"   -> GPU ACTIVE: {module.cuda.get_device_name(0)}")
            else:
                print("   -> ⚠️ GPU NOT DETECTED (Running on CPU)")
                
    except ImportError:
        print(f"❌ {lib.ljust(15)} | NOT FOUND  | {purpose}")

print("-" * 50)
print("If you see green checks, you are ready to code!")