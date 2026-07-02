import os
import sys
import subprocess
import platform

def build():
    print("=" * 50)
    print("Leet Speak Translator - Build Script")
    print("=" * 50)
    print()
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller is already installed")
    except ImportError:
        print("PyInstaller is not installed!")
        print("Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✓ PyInstaller installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install PyInstaller: {e}")
            print("Please install PyInstaller manually: pip install pyinstaller")
            sys.exit(1)
        print()
    
    print("Building executable...")
    print()
    
    # Check if icon file exists
    icon_file = "icon.ico"
    has_icon = os.path.exists(icon_file)
    
    if has_icon:
        print(f"✓ Using icon file: {icon_file}")
    else:
        print(f"⚠ Icon file '{icon_file}' not found")
        print("  Creating a placeholder icon...")
        try:
            # Create a simple placeholder icon using PIL if available
            try:
                from PIL import Image, ImageDraw
                
                # Create a 256x256 image
                img = Image.new('RGBA', (256, 256), (74, 144, 226, 255))
                draw = ImageDraw.Draw(img)
                
                # Draw a simple "LS" logo
                draw.rectangle([50, 50, 206, 206], fill=(255, 255, 255, 255))
                draw.ellipse([70, 70, 186, 186], fill=(74, 144, 226, 255))
                
                # Save as .ico
                img.save(icon_file, format='ICO')
                print(f"✓ Created placeholder icon: {icon_file}")
                has_icon = True
            except ImportError:
                print("⚠ PIL/Pillow not installed. Creating a basic icon...")
                # Create a text file as placeholder
                with open(icon_file, 'w') as f:
                    f.write("# Placeholder icon file\n")
                print(f"✓ Created basic icon placeholder: {icon_file}")
                has_icon = True
        except Exception as e:
            print(f"⚠ Could not create icon: {e}")
            has_icon = False
    
    # Build command based on platform
    current_platform = platform.system()
    print(f"Platform: {current_platform}")
    
    # Common parameters
    cmd = [
        "pyinstaller",
        "--onefile",           # Single executable file
        "--windowed",          # No console window
        "--name", "LeatSpeakTraslator",  # Your requested name
        "--clean",             # Clean build cache
        "--noconfirm",        # Don't ask for confirmation
    ]
    
    # Platform-specific parameters
    if current_platform == "Windows":
        print("Target: Windows (.exe)")
        if has_icon:
            cmd.extend(["--icon", icon_file])
        cmd.append("--add-data")
        cmd.append("config.json;.")  # Include config file
    elif current_platform == "Linux":
        print("Target: Linux")
        # Linux doesn't use .ico files, but we can still include data
        cmd.append("--add-data")
        cmd.append("config.json:.")  # Linux uses colon separator
    elif current_platform == "Darwin":  # macOS
        print("Target: macOS")
        if has_icon and icon_file.endswith('.icns'):
            cmd.extend(["--icon", icon_file])
        cmd.append("--add-data")
        cmd.append("config.json:.")  # macOS uses colon separator
    else:
        print(f"⚠ Unknown platform: {current_platform}")
        print("Using default parameters...")
    
    # Add hidden imports for all modules
    cmd.extend([
        "--hidden-import", "customtkinter",
        "--hidden-import", "tkinter",
        "--hidden-import", "json",
        "--hidden-import", "locale",
        "--hidden-import", "os",
        "--hidden-import", "sys",
    ])
    
    # Main entry point
    cmd.append("main.py")
    
    print()
    print("Build command:")
    print(" ".join(cmd))
    print()
    
    try:
        print("Starting build process...")
        subprocess.check_call(cmd)
        
        # Check the result
        if current_platform == "Windows":
            exe_path = "dist/LeatSpeakTraslator.exe"
        else:
            exe_path = "dist/LeatSpeakTraslator"
        
        if os.path.exists(exe_path):
            file_size = os.path.getsize(exe_path) / (1024 * 1024)  # Convert to MB
            print()
            print("=" * 50)
            print("✓ Build completed successfully!")
            print(f"Executable: {exe_path}")
            print(f"Size: {file_size:.2f} MB")
            print("=" * 50)
            
            # Additional info for Windows
            if current_platform == "Windows":
                print("\nTo run the program:")
                print(f"1. Double-click '{exe_path}'")
                print(f"2. Or run from command line: '{exe_path}'")
        else:
            print()
            print("=" * 50)
            print("⚠ Build completed but executable not found!")
            print("Check build logs above for errors.")
            print("=" * 50)
            
    except subprocess.CalledProcessError as e:
        print()
        print("=" * 50)
        print("✗ Build failed!")
        print(f"Error code: {e.returncode}")
        print("=" * 50)
        sys.exit(1)
    except Exception as e:
        print()
        print("=" * 50)
        print("✗ Unexpected error during build!")
        print(f"Error: {e}")
        print("=" * 50)
        sys.exit(1)

if __name__ == "__main__":
    build()
