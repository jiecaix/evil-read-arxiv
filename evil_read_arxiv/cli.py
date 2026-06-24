"""Unified command dispatcher for the skill helper scripts."""

from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent
REPO_SKILL_ROOT = REPO_ROOT / "skills" / "evil-read-arxiv"
INSTALLED_SKILL_ROOT = Path(sys.prefix) / "skills" / "evil-read-arxiv"


def find_skill_root() -> Path:
    for skill_root in (REPO_SKILL_ROOT, INSTALLED_SKILL_ROOT):
        if skill_root.exists():
            return skill_root
    return REPO_SKILL_ROOT


SKILL_ROOT = find_skill_root()

COMMANDS = {
    "search-arxiv": SKILL_ROOT / "start-my-day" / "scripts" / "search_arxiv.py",
    "scan-notes": SKILL_ROOT / "start-my-day" / "scripts" / "scan_existing_notes.py",
    "link-keywords": SKILL_ROOT / "start-my-day" / "scripts" / "link_keywords.py",
    "generate-note": SKILL_ROOT / "paper-analyze" / "scripts" / "generate_note.py",
    "update-graph": SKILL_ROOT / "paper-analyze" / "scripts" / "update_graph.py",
    "extract-images": SKILL_ROOT / "extract-paper-images" / "scripts" / "extract_images.py",
    "search-conf-papers": SKILL_ROOT / "conf-papers" / "scripts" / "search_conf_papers.py",
    "hunt-papers": SKILL_ROOT / "paper-search" / "scripts" / "paper_hunter.py",
}


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="evil-read-arxiv",
        description="Run helper scripts bundled with the evil-read-arxiv skills.",
    )
    parser.add_argument(
        "command",
        choices=sorted(COMMANDS),
        help="Command to run. Use '<command> --help' for command-specific options.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    parser = _build_parser()

    if not args:
        parser.print_help()
        return 0

    if args[0] in {"-h", "--help"}:
        parser.print_help()
        return 0

    command = args[0]
    if command not in COMMANDS:
        parser.error(f"unknown command: {command}")

    script_path = COMMANDS[command]
    if not script_path.exists():
        parser.exit(1, f"Script not found for command '{command}': {script_path}\n")

    script_dir = str(script_path.parent)
    old_argv = sys.argv[:]
    old_path = sys.path[:]
    try:
        sys.argv = [str(script_path), *args[1:]]
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)
        runpy.run_path(str(script_path), run_name="__main__")
    finally:
        sys.argv = old_argv
        sys.path = old_path

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
