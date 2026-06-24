from __future__ import annotations

import os
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent
SKILLS_ROOT = REPO_ROOT / "skills" / "evil-read-arxiv"


def get_vault_path(vault: str | None = None) -> Path:
    if vault:
        return Path(vault).expanduser()
    env_vault = os.environ.get("OBSIDIAN_VAULT_PATH", "")
    if env_vault:
        return Path(env_vault).expanduser()
    raise SystemExit("未指定 vault 路径。请通过 --vault 参数或 OBSIDIAN_VAULT_PATH 环境变量设置。")


def skill_path(*parts: str) -> Path:
    return SKILLS_ROOT.joinpath(*parts)
