from __future__ import annotations

from typing import Final

from badgie import tokens as to
from badgie.models import Context, ProjectRemote, Remote, RemoteMatch
from badgie.project import get_project_remotes


REMOTES: Final = {
    RemoteMatch(host="github.com"): {to.GITHUB},
    RemoteMatch(host="gitlab.com"): {to.GITLAB},
}


def match_remote(project_remote: ProjectRemote) -> list[Remote]:
    """Return list of remote code servers given a ProjectRemote object."""
    nodes = []
    for match, tokens in REMOTES.items():
        if project_remote.host != match.host:
            continue
        if match.path_prefix and not project_remote.path.startswith(
            match.path_prefix,
        ):
            continue
        nodes.append(
            Remote(
                tokens=tokens,
                host=project_remote.host,
                path=project_remote.path,
            ),
        )
    return nodes


def run(_context: Context) -> list[Remote]:
    """Return list of remote code servers."""
    remote = get_project_remotes().get("origin", {}).get("fetch", None)
    if remote is None:
        return []
    return match_remote(remote)
