# EasyLibraryMaker 📚⚡

A simple, user-friendly tool for creating standardized library folder structures with customizable templates.

## 🚀 Features

- **GUI Interface** - Clean Tkinter-based interface for easy use
- **Customizable Templates** - YAML-based configuration for different project types
- **Flexible Structure** - Create any folder structure you need
- **Cross-Platform** - Works on Windows, Mac, and Linux
- **Smart Defaults** - Comes with pre-configured templates for common library types

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GuyGHYT/EasyLibraryMaker.git
   cd EasyLibraryMaker
   ```

2. **Install dependencies:**
   ```bash
   pip install requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## 🎯 Quick Start

1. **Launch the application**
2. **Select destination folder** - Choose where to create your library
3. **Enter library name** - Type your project name (e.g., "MyAwesomeLib")
4. **Choose config template** - Select from pre-made templates or create your own
5. **Click "Start"** - Your library structure is created instantly!

## 📁 Project Structure

```
EasyLibraryMaker/
├── libmakerlib/           # Core library code
│   ├── engine/           # GUI and window management
│   │   └── windowhandler.py
│   └── utils/            # Utilities and config handling
│       ├── configloader.py
│       ├── config_parser.py
│       └── createfolder.py
├── config/               # Template configurations
│   ├── python-lib.yaml  # Python library template
│   └── example-lib.yaml # Example template
├── main.py              # Main application entry point
└── README.md           # This file
```

## 🔧 Creating Custom Templates

Templates are defined in YAML files in the `config/` folder:

```yaml
# config/my-template.yaml
"subfolders":
  - "utils"
  - "components"
  - "tests"
  - "docs"
  - "examples"

"inits":
  - "__init__.py"
  - "utils/__init__.py"
  - "components/__init__.py"
```
(Note: the "inits" portion has NOT been made.)

## 📋 Template Options

### **Subfolders**
Define the folder structure to create:
```yaml
"subfolders":
  - "src"
  - "tests"
  - "docs"
  - "config"
```

### **Init Files** (Optional)
Automatically create `__init__.py` files for Python projects:
```yaml
"inits":
  - "__init__.py"
  - "src/__init__.py"
```

## 🛠️ Built-in Templates

- **`python-lib.yaml`** - Python library with utils, plugins, components, classes, constants, tests, docs, and config folders
- **`example-lib.yaml`** - Basic example template

## 💡 Usage Examples

### Creating a Python Library
1. Select your Projects folder
2. Enter "MyPythonLib" as library name
3. Choose `python-lib.yaml` template
4. Result: Creates `MyPythonLib/` with proper Python structure

### Creating a Custom Project
1. Create your own YAML template in `config/`
2. Use it through the GUI
3. Instant custom project structure!

## 🎨 GUI Features

- **Browse Button** - Visual folder selection
- **Config Browser** - Easy template selection
- **Input Validation** - Prevents common errors
- **Real-time Feedback** - See exactly what's being created

## 🔍 Troubleshooting

### Common Issues

**"No module named libmakerlib"**
- Make sure you're running from the project root directory
- Check that `__init__.py` files exist in the package folders

**"Config file not found"**
- Ensure your YAML file is in the `config/` folder
- Check file path and spelling

**"Permission denied"**
- Make sure you have write access to the destination folder
- Try running as administrator (Windows) or with sudo (Linux/Mac)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🚀 Future Features

- [ ] More built-in templates (React, Node.js, etc.)
- [ ] Template sharing and downloading
- [ ] Git initialization option
- [ ] File content templates (boilerplate code)
- [ ] CLI interface
- [ ] Template validation

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/EasyLibraryMaker/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/EasyLibraryMaker/discussions)

---

Made with ❤️ for developers who like organized projects!