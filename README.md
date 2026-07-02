# Leet Speak Generator

A modern, cross-platform desktop application for converting regular text to Leet Speak (1337) with support for both English and Russian languages.

## Features

### Core Features
- **Real-time Leet Speak Conversion** - Instantly converts text as you type
- **Multi-language Support** - Converts both English and Russian text
- **Dual Language Interface** - Switch between English and Russian UI
- **Character Counter** - Track input and output character counts
- **One-click Copy** - Copy converted text to clipboard with visual feedback
- **Modern Dark Theme** - Clean, eye-friendly dark mode interface

### User Interface
- **Responsive Design** - Adapts to different window sizes (minimum 900x650)
- **Clean Card Layout** - Separated input/output panels with visual distinction
- **Animated Feedback** - Visual feedback for copy operations
- **Settings Panel** - Language configuration in a dedicated settings window
- **Character Counter** - Real-time character count display

### Technical Features
- **Auto-detection** - Automatically detects system language
- **Settings Persistence** - Remembers language preferences between sessions
- **Built-in Build Script** - Easy executable creation with PyInstaller
- **Cross-platform** - Works on Windows, Linux, and macOS

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download the project**
   ```bash
   git clone https://github.com/laymoviy/leat-speak-translator.git
   cd leat-speak-translator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### Build Standalone Executable

To create a standalone executable:

```bash
python build.py
```

This will generate an executable in the `dist/` folder that can be run without Python installed.

## Usage

1. **Launch the application** using `python main.py`
2. **Type text** in the left panel (Input Text)
3. **View conversion** in real-time in the right panel (Leet Speak)
4. **Copy text** using the "Copy Leet Speak" button
5. **Clear text** using the "Clear" button
6. **Change language** via the settings gear icon (⚙)

### Language Configuration
- Click the settings gear icon (⚙) in the top-right corner
- Select interface language (English or Russian)
- The application supports both English and Russian text input
- Interface automatically adjusts to your system language

## Project Structure

```
EnglishLeatSpeakGenerator/
├── app.py              # Main application class and GUI
├── main.py             # Application entry point
├── leet_generator.py   # Leet speak conversion logic
├── translations.py     # Multi-language text resources
├── settings.py         # Settings management
├── settings_window.py  # Settings dialog
├── styles.py          # UI styling constants
├── build.py           # Build script for executables
├── config.json        # User settings storage
├── requirements.txt   # Python dependencies
├── LeetSpeakGenerator.spec  # PyInstaller specification
└── README.md          # This file
```

## Development

### Dependencies

The project uses:
- **CustomTkinter** - Modern UI framework
- **PyInstaller** - For creating standalone executables

Install development dependencies:
```bash
pip install -r requirements.txt
```

### Code Structure

- **app.py** - Main GUI application using CustomTkinter
- **leet_generator.py** - Core conversion logic with dual-language support
- **translations.py** - String resources for English and Russian
- **settings.py** - Configuration management with auto-detection
- **styles.py** - Centralized styling constants
- **build.py** - Automated build process

### Leet Conversion Rules

**English:**
- a/A → 4
- e/E → 3
- i/I → 1
- o/O → 0
- s/S → 5
- t/T → 7
- l/L → 1
- g/G → 9
- b/B → 8
- z/Z → 2

**Russian:**
- а/А → 4
- е/Е → 3
- и/И → 1
- о/О → 0
- с/С → 5
- т/Т → 7
- л/Л → 1
- г/Г → 9
- в/В → 8
- з/З → 2
- ё/Ё → 3
- ч/Ч → 4
- ш/Ш → 6
- щ/Щ → 6

## Building from Source

### Building with Custom Icon and Name

The project includes an enhanced build script that creates a standalone executable named `LeatSpeakTraslator.exe` (Windows) or `LeatSpeakTraslator` (Linux/macOS) with a custom icon.

#### Windows Build Command

For a direct build with PyInstaller:

```bash
pyinstaller --onefile --windowed --name LeatSpeakTraslator --icon icon.ico --clean --noconfirm --add-data "config.json;." --hidden-import customtkinter --hidden-import tkinter main.py
```

#### Using the Build Script

The easier way is to use the provided `build.py` script:

```bash
python build.py
```

This script will:
1. Check for and install PyInstaller if needed
2. Create a placeholder icon if `icon.ico` doesn't exist
3. Build for your current platform (Windows/Linux/macOS)
4. Include all necessary data files
5. Output executable to `dist/` folder

#### Creating a Custom Icon

1. Create a 256x256 pixel icon using a tool like:
   - [ICO Convert](https://icoconvert.com/)
   - [Favicon Generator](https://favicon.io/)
   - Any image editor with .ico export

2. Save it as `icon.ico` in the project root

3. Run the build script again

### Build Output

- **Windows**: `dist/LeatSpeakTraslator.exe`
- **Linux**: `dist/LeatSpeakTraslator`
- **macOS**: `dist/LeatSpeakTraslator.app` (bundle)

The build includes:
- Custom icon support
- Platform-specific optimizations
- Data file inclusion (config.json)
- Clean build process
- Progress reporting and error handling