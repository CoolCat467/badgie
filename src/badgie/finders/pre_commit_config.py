"""Pre-commit hook matches."""

from __future__ import annotations

import yaml

from badgie import tokens as to
from badgie.models import Context, File, Hook, HookMatch, PrecommitCI
from badgie.project import get_project_head_branch, get_project_remotes

HOOKS = {
    HookMatch(
        repo="https://github.com/pre-commit/mirrors-prettier/",
        hook="prettier",
    ): {to.PRETTIER},
    HookMatch(repo="https://github.com/psf/black/", hook="black"): {
        to.PYTHON_BLACK,
    },
    HookMatch(repo="https://github.com/psf/black/", hook="black-jupyter"): {
        to.PYTHON_BLACK,
    },
    HookMatch(
        repo="https://github.com/psf/black-pre-commit-mirror",
        hook="black",
    ): {
        to.PYTHON_BLACK,
    },
    HookMatch(
        repo="https://github.com/psf/black-pre-commit-mirror",
        hook="black-jupyter",
    ): {
        to.PYTHON_BLACK,
    },
    HookMatch(repo="https://github.com/PyCQA/bandit/", hook="bandit"): {
        to.PYTHON_BANDIT,
    },
    HookMatch(repo="https://github.com/PyCQA/isort/", hook="isort"): {
        to.PYTHON_ISORT,
    },
    HookMatch(
        repo="https://github.com/PyCQA/docformatter/",
        hook="docformatter",
    ): {to.PYTHON_DOCFORMATTER},
    HookMatch(
        repo="https://github.com/PyCQA/docformatter/",
        hook="docformatter-venv",
    ): {to.PYTHON_DOCFORMATTER},
    HookMatch(
        repo="https://github.com/pre-commit/mirrors-mypy/",
        hook="mypy",
    ): {to.PYTHON_MYPY},
    HookMatch(
        repo="https://github.com/astral-sh/ruff-pre-commit/",
        hook="ruff",
    ): {to.PYTHON_RUFF},
}


def normalize_url(url: str) -> str:
    """Add trailing / to url after stripping off extras."""
    url = url.strip()
    if not url.endswith("/"):
        url += "/"
    return url


def match_hook(repo: str, hook: str) -> Hook | None:
    """Return Hook objects if recognized."""
    entry = HookMatch(repo=normalize_url(repo), hook=hook.strip())
    if entry in HOOKS:
        return Hook(tokens=HOOKS[entry], repo=entry.repo, hook=entry.hook)
    return None


def run(context: Context) -> list[Hook | PrecommitCI]:
    """Return list of pre-commit config hooks from context."""
    pre_commit_config = context.nodes[to.PRE_COMMIT_CONFIG][0]
    assert isinstance(pre_commit_config, File)
    with open(pre_commit_config.path, encoding="utf-8") as file:
        data = yaml.safe_load(file)
    nodes: list[Hook | PrecommitCI] = []
    for repo in data.get("repos", ()):
        for hook in repo.get("hooks", ()):
            match = match_hook(repo.get("repo", ""), hook.get("id", ""))
            if match:
                nodes.append(match)
    if data.get("ci"):
        remotes = get_project_remotes()
        head = get_project_head_branch()
        if (
            (origin := remotes.get("origin"))
            and (fetch := origin.get("fetch"))
            and (host_parts := fetch.host.split(".", 1))
        ):
            nodes.append(
                PrecommitCI(
                    tokens={to.PRE_COMMIT_CI},
                    host=host_parts[0],
                    path=fetch.path,
                    head=head,
                ),
            )
    return nodes
