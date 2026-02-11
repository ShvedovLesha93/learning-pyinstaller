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

## Building for Production

### Quick Build

**Linux/Mac:**
```bash
uv run pyinstaller --windowed --onedir \
    --add-data "app/locales:app/locales" \
    main.py
```

**Windows:**
```bash
uv run pyinstaller --windowed --onedir ^
    --add-data "app/locales;app/locales" ^
    main.py
```

### Using the Spec File

The repository includes a pre-configured `main.spec` file:

```bash
uv run pyinstaller main.spec
```

The executable will be created in `dist/main/`.

## How It Works

### Language Management

The application uses `gettext` for internationalization. The `LanguageManager` class handles:

1. **Path Detection**: Automatically detects if running from `PyInstaller` bundle or development environment
2. **Translation Loading**: Loads `.mo` files from the correct location
3. **Language Switching**: Provides runtime language switching capability

```python
# From translator.py
if getattr(sys, 'frozen', False):
    # Running in PyInstaller bundle
    bundle_dir = Path(sys._MEIPASS)
    self.locales_dir = bundle_dir / "app" / "locales"
else:
    # Running in normal Python environment
    self.locales_dir = Path("app/locales")
```

### PyInstaller Configuration

The key to making translations work in PyInstaller is:

1. **Include locale files** using `--add-data`:
   - Linux/Mac: `"app/locales:app/locales"`
   - Windows: `"app/locales;app/locales"`

2. **Detect bundle environment** using `sys.frozen` and `sys._MEIPASS`

3. **Use --onedir** for easier debugging and file access

## Adding New Translations

### 1. Extract translatable strings

```bash
xgettext -o app/locales/messages.pot main.py app/translator.py
```

### 2. Create or update language files

For a new language (e.g., French):
```bash
mkdir -p app/locales/fr/LC_MESSAGES
msginit -i app/locales/messages.pot \
    -o app/locales/fr/LC_MESSAGES/messages.po \
    -l fr
```

For updating existing translations:
```bash
msgmerge -U app/locales/ru/LC_MESSAGES/messages.po app/locales/messages.pot
```

### 3. Edit the .po file

Open `app/locales/ru/LC_MESSAGES/messages.po` and add translations:

```po
msgid "Change language"
msgstr "Изменить язык"

msgid "Language changed to: {lang}"
msgstr "Язык изменён на: {lang}"
```

### 4. Compile translations

```bash
msgfmt app/locales/ru/LC_MESSAGES/messages.po \
    -o app/locales/ru/LC_MESSAGES/messages.mo
```

### 5. Add language to the app

Update `main.py` to include the new language:

```python
self._languages = ["ru", "en", "fr"]
```

## Troubleshooting

### Translations don't work in built executable

**Problem**: Language switching works in development but not after building with PyInstaller.

**Solution**: 
1. Ensure you're using `--add-data` flag correctly
2. Verify `translator.py` checks for `sys.frozen`
3. Check that `.mo` files are compiled and present

### Files not found errors

**Problem**: PyInstaller can't find locale files.

**Solution**:
```bash
# Verify files are included after building
ls -R dist/main/app/locales/  # Linux/Mac
dir /s dist\main\app\locales\  # Windows
```

### Debugging the build

Remove `--windowed` flag to see console output:

```bash
uv run pyinstaller --onedir \
    --add-data "app/locales:app/locales" \
    main.py
```

## Key Learnings

### 1. PyInstaller Data Files
- PyInstaller doesn't automatically include non-Python files
- Use `--add-data` to include resources like translations
- Different separators on Windows (`;`) vs Unix (`:`)

### 2. Bundle Path Detection
- Check `sys.frozen` to detect if running from bundle
- Use `sys._MEIPASS` to get the temporary extraction directory
- Always use `Path()` for cross-platform compatibility

### 3. Build Modes
- `--onedir`: Creates a folder with executable and dependencies (easier to debug)
- `--onefile`: Creates a single executable (slower startup, harder to debug)
- `--windowed`: Hides console window (use for GUI apps)

### 4. Translation Workflow
- `.pot` files are templates (generated from source code)
- `.po` files are human-readable translations
- `.mo` files are compiled binaries (used at runtime)

## Resources

- [PyInstaller Documentation](https://pyinstaller.org/)
- [PySide6 Documentation](https://doc.qt.io/qtforpython/)
- [GNU gettext Manual](https://www.gnu.org/software/gettext/manual/)
- [UV Package Manager](https://github.com/astral-sh/uv)

## License

This project is created for educational purposes.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have suggestions!
