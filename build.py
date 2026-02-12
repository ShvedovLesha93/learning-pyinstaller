import shutil
from pathlib import Path
import subprocess

# import app.locales as locales

LOCALES_PATH = Path("app")
DIST_LOCALES_PATH = Path("dist/main")


def run_pyinstaller() -> tuple[bool, str | None]:
    cmd = ["uv", "run", "pyinstaller", "main.spec"]

    try:
        subprocess.run(cmd, check=True)
        return (True, None)
    except subprocess.CalledProcessError as e:
        return (False, str(e))


def copy_locales() -> None:
    shutil.copytree(LOCALES_PATH / "locales", DIST_LOCALES_PATH / "locales")


def clean():
    """Clean previous builds."""
    print("🧹 Cleaning previous builds...")

    dirs_to_clean = ["dist"]
    for dir_name in dirs_to_clean:
        dir_path = Path(dir_name)
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"   Removed {dir_name}/")

    print("✓ Clean complete\n")


def main() -> None:
    clean()
    result, err = run_pyinstaller()
    if result:
        print("✓ PyInstaller build complete\n")
        copy_locales()
        print("✓ Locales copied\n")
    else:
        print(f"✗ Build failed: {err}")


if __name__ == "__main__":
    main()
