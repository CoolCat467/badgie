from typing import Optional

from . import tokens as to
from .models import Context, Remote
from .project import get_project_remotes

HOSTS = {
    "github.com": {to.GITHUB},
    "gitlab.com": {to.GITLAB},
}

PREFIXES = {
    "https://gitlab.com/brettops": {to.BRETTOPS},
}


def match_host(host: str) -> Optional[Remote]:
    nodes = []
    for known_host, tokens in HOSTS.items():
        if host == known_host:
            nodes.append(Remote(tokens=tokens, host=host))
    return nodes


def match_path_prefix(path: str) -> list[Remote]:
    nodes = []
    for prefix, tokens in PREFIXES.items():
        if path.startswith(prefix):
            nodes.append(Remote(tokens=tokens, prefix=prefix))
    return nodes


def run(_context: Context) -> list[Remote]:
    remote = get_project_remotes()["origin"]["fetch"]
    nodes = []
    nodes.extend(match_host(remote.host))
    nodes.extend(match_path_prefix(remote.path))
    return nodes
