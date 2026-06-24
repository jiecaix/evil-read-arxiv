"""Unified command dispatcher for evil-read-arxiv."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable

from evil_read_arxiv.commands.conf_papers.search_conf_papers import main as search_conf_papers
from evil_read_arxiv.commands.extract_paper_images.extract_images import main as extract_images
from evil_read_arxiv.commands.paper_analyze.generate_note import main as generate_note
from evil_read_arxiv.commands.paper_analyze.update_graph import main as update_graph
from evil_read_arxiv.commands.paper_search.paper_hunter import main as hunt_papers
from evil_read_arxiv.commands.start_my_day.link_keywords import main as link_keywords
from evil_read_arxiv.commands.start_my_day.scan_existing_notes import main as scan_notes
from evil_read_arxiv.commands.start_my_day.search_arxiv import main as search_arxiv


COMMANDS: dict[str, Callable[[], int | None]] = {
    "search-arxiv": search_arxiv,
    "scan-notes": scan_notes,
    "link-keywords": link_keywords,
    "generate-note": generate_note,
    "update-graph": update_graph,
    "extract-images": extract_images,
    "search-conf-papers": search_conf_papers,
    "hunt-papers": hunt_papers,
}


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="evil-read-arxiv",
        description="Run evil-read-arxiv helper commands.",
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

    if not args or args[0] in {"-h", "--help"}:
        parser.print_help()
        return 0

    command = args[0]
    if command not in COMMANDS:
        parser.error(f"unknown command: {command}")

    old_argv = sys.argv[:]
    try:
        sys.argv = [f"evil-read-arxiv {command}", *args[1:]]
        result = COMMANDS[command]()
        return int(result or 0)
    finally:
        sys.argv = old_argv


if __name__ == "__main__":
    raise SystemExit(main())
