from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Project:
    path: Path
    url: str
    ref: str
