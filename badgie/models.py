from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Project:
    local_path: Path
    url: str
    ref: str
    name: str
    namespace: str
    path: str
    full_name: str
    full_path: str


@dataclass(frozen=True)
class Remote:
    name: str
    prefix: str
