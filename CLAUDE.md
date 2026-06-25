# Claude Instructions

This repository provides skills for working with an Obsidian research vault.

## Python Environment

When using these skills from a vault, do not install Python packages into the system Python, global conda/base environment, or user site-packages.

Before running any Python script from this project:

1. Use a virtual environment located in the active vault, named `.venv-evil-read-arxiv`.
2. If the environment does not exist, create it in the vault root.
3. Install dependencies into that environment with this repository's `requirements.txt`.
4. Activate the environment before running project scripts, or call the environment's Python executable directly.

macOS/Linux example:

```bash
python -m venv .venv-evil-read-arxiv
source .venv-evil-read-arxiv/bin/activate
python -m pip install -r /path/to/evil-read-arxiv/requirements.txt
```

Windows PowerShell example:

```powershell
py -3 -m venv .venv-evil-read-arxiv
.\.venv-evil-read-arxiv\Scripts\Activate.ps1
python -m pip install -r C:\path\to\evil-read-arxiv\requirements.txt
```

If the vault-local environment is missing or dependencies are unavailable, create or repair the environment first instead of falling back to global installation.
