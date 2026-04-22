import subprocess
import shutil
import sys
from pathlib import Path
from app.config import PROJECT_DIR, BUILD_DIR, DEFAULT_CODE, RUNTIME_DIR


def _normalize(filename: str) -> str:
    return filename if filename.endswith(".cs") else filename + ".cs"


def list_files():
    return [f.name for f in PROJECT_DIR.glob("*.cs")]


def create_file(filename: str):
    filename = _normalize(filename)
    path = PROJECT_DIR / filename
    with open(path, "w") as f:
        f.write(DEFAULT_CODE)
    return filename


def read_file(filename: str):
    filename = _normalize(filename)
    path = PROJECT_DIR / filename
    return path.read_text()


def edit_file(filename: str, content: str):
    filename = _normalize(filename)
    path = PROJECT_DIR / filename
    path.write_text(content)
    return True


def delete_file(filename: str):
    filename = _normalize(filename)
    path = PROJECT_DIR / filename
    if path.exists():
        path.unlink()
    return True


def build_file(filename: str):
    filename = _normalize(filename)
    src = PROJECT_DIR / filename

    if not src.exists():
        return "Source file not found"

    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    try:
        # Bước 1: Compile .cs → CS.j
        result = subprocess.run(
            [sys.executable, "compiler/run.py", str(src)],
            capture_output=True,
            text=True,
            cwd="/app",
        )

        if result.returncode != 0:
            return result.stdout or result.stderr

        # Bước 2: Jasmin CS.j → CS.class
        jasmin_result = subprocess.run(
            ["java", "-jar", str(RUNTIME_DIR / "jasmin.jar"), "CS.j"],
            capture_output=True,
            text=True,
            cwd=str(RUNTIME_DIR),
        )

        if jasmin_result.returncode != 0:
            return jasmin_result.stdout or jasmin_result.stderr

        # Bước 3: Copy CS.class sang BUILD_DIR
        for f in RUNTIME_DIR.glob("*.class"):
            shutil.copy(f, BUILD_DIR / f.name)

        return result.stdout

    except Exception as e:
        return f"Build failed: {e}"


def run_file():
    main_class = BUILD_DIR / "CS.class"

    if not main_class.exists():
        return "Build file not found"

    try:
        result = subprocess.run(
            ["java", "-cp", str(BUILD_DIR), "CS"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return result.stdout or result.stderr

    except subprocess.TimeoutExpired:
        return "Timeout: program ran too long"
    except Exception as e:
        return f"Run error: {e}"