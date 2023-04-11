from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Project:
    path: Path
    url: str
    ref: str


@dataclass(frozen=True)
class Remote:
    name: str
    prefix: str
