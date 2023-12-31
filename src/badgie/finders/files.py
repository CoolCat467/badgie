"""Run other finders from finding specific files."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Final

from badgie import tokens as to
from badgie.models import Context, File
from badgie.project import get_project_paths

if TYPE_CHECKING:
    from pathlib import Path

FILES: Final = {
    ".gitignore": {to.GIT},
    ".gitmodules": {to.GIT},
    ".gitattributes": {to.GIT},
    ".pre-commit-config.ya?ml": {to.PRE_COMMIT_CONFIG},
    ".pre-commit-hooks.ya?ml": {to.PRE_COMMIT_HOOKS},
    ".secrets.baseline": {to.DETECT_SECRETS},
    ".gitlab-ci.yml": {to.GITLAB_CI_FILE},
    "setup.cfg": {to.PYTHON_SETUP_CFG},
    "setup.py": {to.PYTHON_SETUPTOOLS},
    "pyproject.toml": {to.PYTHON_PYPROJECT_TOML},
    "meta/main.ya?ml": {to.ANSIBLE_GALAXY},
}

RE_FILES: Final = {
    re.compile(r"^" + pattern + r"$", re.IGNORECASE): tokens
    for pattern, tokens in FILES.items()
}


def match_file(path: Path) -> File | None:
    """Return matched File nodes from a given Path."""
    for regex, tokens in RE_FILES.items():
        match = regex.match(str(path))
        if match:
            return File(tokens=tokens, path=path, pattern=match.re.pattern)
    return None


def run(_context: Context) -> list[File]:
    """Return File nodes from project paths."""
    nodes = []
    for path in get_project_paths():
        file = match_file(path)
        if file:
            nodes.append(file)
    return nodes
