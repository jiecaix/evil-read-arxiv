from __future__ import annotations

import re


def title_to_filename(title: str) -> str:
    return re.sub(r'[ /\\:*?"<>|]+', '_', title).strip('_')
