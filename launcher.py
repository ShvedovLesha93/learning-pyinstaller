import io
import logging
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)
log = logging.getLogger("launcher")

APP_DIR = Path(sys.executable).parent
UV = APP_DIR / "uv.exe"
VENV = APP_DIR / ".venv"

if sys.platform == "win32":
    PYTHON = VENV / "Scripts" / "python.exe"
else:
    PYTHON = VENV / "bin" / "python"

UV_VERSION = "0.10.4"
UV_URL = f"https://github.com/astral-sh/uv/releases/download/{UV_VERSION}/uv-x86_64-pc-windows-msvc.zip"


def log_paths():
    log.debug(f"APP_DIR : {APP_DIR}")
    log.debug(f"UV      : {UV} (exists: {UV.exists()})")
    log.debug(f"VENV    : {VENV} (exists: {VENV.exists()})")
    log.debug(f"PYTHON  : {PYTHON} (exists: {PYTHON.exists()})")


def download_uv():
    log.debug(f"Downloading uv {UV_VERSION}...")
    with urllib.request.urlopen(UV_URL) as response:
        zip_data = io.BytesIO(response.read())
    with zipfile.ZipFile(zip_data) as zf:
        with zf.open("uv.exe") as src, open("uv.exe", "wb") as dst:
            dst.write(src.read())
    log.debug("uv.exe downloaded")


def bootstrap():
    if not UV.exists():
        log.info("First launch: downloading uv, please wait...")
        download_uv()

    if not VENV.exists():
        log.info("First launch: setting up environment, please wait...")
        subprocess.run(
            [
                UV,
                "sync",
                "--link-mode",
                "copy",
                "--no-dev",
                "--python-preference",
                "only-managed",
                "--python",
                "3.12",
            ],
            cwd=APP_DIR,
            check=True,
        )
        log.info("Environment ready.")
        log.debug(f"PYTHON  : {PYTHON} (exists: {PYTHON.exists()})")
    else:
        log.info("Virtual environment already exists, skipping bootstrap.")


def main():
    try:
        log_paths()
        bootstrap()
        log_paths()
        log.info(f"Launching app: {PYTHON} {APP_DIR / 'main.py'}")
        result = subprocess.run([PYTHON, APP_DIR / "main.py"])
        if result.returncode != 0:
            log.error(f"App exited with error code: {result.returncode}")
            input("\nPress Enter to close...")
            sys.exit(result.returncode)
    except Exception as e:
        log.exception(f"Launcher error: {e}")
        input("\nPress Enter to close...")
        sys.exit(1)


if __name__ == "__main__":
    main()
