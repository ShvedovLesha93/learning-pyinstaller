# Learning PyInstaller

A sample `PySide6` application demonstrating how to build cross-platform desktop applications with internationalization (i18n) support using `PyInstaller`.

## Features

- ✨ Simple `PySide6` GUI with language switching
- 🌍 Internationalization support using `gettext`
- 📦 `PyInstaller` configuration for production builds
- 🔄 Runtime language switching between English and Russian
- 🚀 Properly configured for bundled executables

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Installation

### Using UV (Recommended)

```bash
# Clone the repository
git clone https://github.com/ShvedovLesha93/learning-pyinstaller.git
cd learning-pyinstaller

# Install dependencies
uv sync
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/ShvedovLesha93/learning-pyinstaller.git
cd learning-pyinstaller

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install PySide6 pyinstaller
```

## Running in Development

```bash
# Using UV
uv run python main.py

# Using regular Python
python main.py
```

## Building

```bash
uv run py build.py
```

The executable will be created in `dist/main/`.

## Resources

- [PyInstaller Documentation](https://pyinstaller.org/)
- [PySide6 Documentation](https://doc.qt.io/qtforpython/)
- [GNU gettext Manual](https://www.gnu.org/software/gettext/manual/)
- [UV Package Manager](https://github.com/astral-sh/uv)

## License

This project is created for educational purposes.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have suggestions!
