import os
import sys
import subprocess

def build():
    print("=" * 50)
    print("Leet Speak Generator - Build Script")
    print("=" * 50)
    print()
    
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller is not installed!")
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully!")
        print()
    
    print("Building executable...")
    print()
    
    if sys.platform.startswith('win'):
        print("Platform: Windows")
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            "--name", "LeetSpeakGenerator",
            "main.py"
        ]
    else:
        print("Platform: Linux/Unix")
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            "--name", "LeetSpeakGenerator",
            "main.py"
        ]
    
    try:
        subprocess.check_call(cmd)
        print()
        print("=" * 50)
        print("Build completed successfully!")
        print("Executable location: dist/LeetSpeakGenerator")
        print("=" * 50)
    except subprocess.CalledProcessError as e:
        print()
        print("=" * 50)
        print("Build failed!")
        print(f"Error: {e}")
        print("=" * 50)
        sys.exit(1)

if __name__ == "__main__":
    build()
