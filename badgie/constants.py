from __future__ import annotations

from typing import Final

PATTERN: Final = r"BADGIE\s+TIME"

PATTERN_START: Final = r"<!--\s+" + PATTERN + r"\s+-->"

PATTERN_END: Final = r"<!--\s+END\s+" + PATTERN + r"\s+-->"
