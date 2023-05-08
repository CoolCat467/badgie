import yaml

from .. import tokens as to
from ..models import Context, Hook, HookMatch

HOOKS = {
    HookMatch(
        repo="https://github.com/pre-commit/mirrors-prettier/", hook="prettier"
    ): {to.PRETTIER},
    HookMatch(repo="https://github.com/psf/black/", hook="black"): {to.PYTHON_BLACK},
    HookMatch(repo="https://github.com/PyCQA/bandit/", hook="bandit"): {
        to.PYTHON_BANDIT
    },
    HookMatch(repo="https://github.com/PyCQA/isort/", hook="isort"): {to.PYTHON_ISORT},
    HookMatch(repo="https://github.com/PyCQA/docformatter/", hook="docformatter"): {
        to.PYTHON_DOCFORMATTER
    },
    HookMatch(
        repo="https://github.com/PyCQA/docformatter/", hook="docformatter-venv"
    ): {to.PYTHON_DOCFORMATTER},
    HookMatch(repo="https://github.com/pre-commit/mirrors-mypy/", hook="mypy"): {
        to.PYTHON_MYPY
    },
}


def normalize_url(url: str):
    url = url.strip()
    if not url.endswith("/"):
        url += "/"
    return url


def match_hook(repo, hook):
    entry = HookMatch(repo=normalize_url(repo), hook=hook.strip())
    if entry in HOOKS:
        return Hook(tokens=HOOKS[entry], repo=entry.repo, hook=entry.hook)


def run(context: Context) -> list[Hook]:
    pre_commit_config = context.nodes[to.PRE_COMMIT_CONFIG][0]
    data = yaml.safe_load(open(pre_commit_config.path))
    nodes = []
    for repo in data["repos"]:
        for hook in repo["hooks"]:
            match = match_hook(repo["repo"], hook["id"])
            if match:
                nodes.append(match)
    return nodes
