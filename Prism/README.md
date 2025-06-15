# Prism Cross-Platform Usage

## Setup (with uv)

1. Install [uv](https://github.com/astral-sh/uv):
   ```zsh
   curl -Ls https://astral.sh/uv/install.sh | zsh
   ```
2. Install dependencies:
   ```zsh
   uv pip install -r pyproject.toml
   ```

## Running Prism

- **Universal (all platforms):**
  ```zsh
  uv venv python prism.py
  ```
  or
  ```zsh
  python3 prism.py
  ```

- **Windows:**
  - You can still use `prism.bat` if desired.
- **Linux/macOS:**
  - You can still use `Prism.sh` if desired.

## Notes
- All dependencies are managed in `pyproject.toml` for uv compatibility.
- The new `prism.py` launcher works on all platforms and is the recommended entry point.
