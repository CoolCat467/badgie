from typing import Optional

from .. import tokens as to
from ..models import Context, ProjectRemote, Remote, RemoteMatch
from ..project import get_project_remotes

REMOTES = {
    RemoteMatch(host="github.com"): {to.GITHUB},
    RemoteMatch(host="gitlab.com"): {to.GITLAB},
    RemoteMatch(host="gitlab.com", path_prefix="brettops"): {to.BRETTOPS},
    RemoteMatch(host="gitlab.com", path_prefix="brettops/ansible/roles"): {
        to.BRETTOPS_ROLE
    },
    RemoteMatch(host="gitlab.com", path_prefix="brettops/containers"): {
        to.BRETTOPS_CONTAINER
    },
    RemoteMatch(host="gitlab.com", path_prefix="brettops/packages"): {
        to.BRETTOPS_PACKAGE
    },
    RemoteMatch(host="gitlab.com", path_prefix="brettops/pipelines"): {
        to.BRETTOPS_PIPELINE
    },
    RemoteMatch(host="gitlab.com", path_prefix="brettops/tools"): {to.BRETTOPS_TOOL},
}


def match_remote(project_remote: ProjectRemote) -> Optional[Remote]:
    nodes = []
    for match, tokens in REMOTES.items():
        if project_remote.host != match.host:
            continue
        if match.path_prefix and not project_remote.path.startswith(match.path_prefix):
            continue
        nodes.append(
            Remote(tokens=tokens, host=project_remote.host, path=project_remote.path)
        )
    return nodes


def run(_context: Context) -> list[Remote]:
    remote = get_project_remotes()["origin"]["fetch"]
    return match_remote(remote)
