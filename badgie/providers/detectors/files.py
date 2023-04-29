import re
import subprocess
from pathlib import Path

from ... import tokens as to
from ...models import File

FILES = {
    ".gitignore": {to.GIT},
    ".gitmodules": {to.GIT},
    ".gitattributes": {to.GIT},
    ".pre-commit-config.ya?ml": {to.PRE_COMMIT_CONFIG},
    ".pre-commit-hooks.ya?ml": {to.PRE_COMMIT_HOOKS},
    ".secrets.baseline": {to.DETECT_SECRETS},
    ".gitlab-ci.yml": {to.GITLAB_CI},
    "setup.cfg": {to.PYTHON_SETUP_CFG},
    "setup.py": {to.PYTHON_SETUPTOOLS},
    "pyproject.toml": {to.PYTHON_PYPROJECT_TOML},
    "meta/main.ya?ml": {to.ANSIBLE_GALAXY},
}

RE_FILES = {
    re.compile(r"^" + pattern + r"$", re.IGNORECASE): tokens
    for pattern, tokens in FILES.items()
}


def match_file(path):
    for regex, tokens in RE_FILES.items():
        match = regex.match(str(path))
        # if regex.match(str(path)): # .match(pattern):
        if match:
            return File(tokens=tokens, path=path, pattern=match.re.pattern)


def run(context):
    paths = [
        Path(path)
        for path in subprocess.run(
            ["git", "ls-files"], text=True, stdout=subprocess.PIPE
        ).stdout.splitlines()
    ]
    nodes = []
    for path in paths:
        file = match_file(path)
        if file:
            nodes.append(file)
    return nodes
