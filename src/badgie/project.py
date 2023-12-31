"""Git project interaction."""

from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING

import pre_commit.git as git
from pre_commit.util import CalledProcessError

from badgie.models import ProjectRemote

if TYPE_CHECKING:
    from typing import Final

REMOTES: Final = (
    r"(?P<user>git)@(?P<host>.*?):(?P<path>.*?)\.git",
    r"(?P<scheme>\w+):\/\/(?P<host>[^\/]*?)\/(?P<path>.*)\.git",
)

RE_REMOTES: Final = [re.compile(remote) for remote in REMOTES]


def match_remote_url(url: str) -> re.Match[str] | None:
    """Return regular expression matches from given url."""
    for remote in RE_REMOTES:
        match = remote.match(url)
        if match:
            return match
    return None


def get_match_group(match: re.Match[str], name: str) -> str | None:
    """Return match group."""
    try:
        return match.group(name)
    except IndexError:
        return None


def get_project_remote(line: str) -> ProjectRemote | None:
    """Return ProjectRemote from regex or None if failed."""
    name, parts = line.split("\t")
    url, type_ = parts.split(" ")
    type_ = type_.replace("(", "").replace(")", "")
    match = match_remote_url(url)
    if not match:
        return None
    return ProjectRemote(
        name=name,
        type_=type_,
        url=url,
        scheme=get_match_group(match, "scheme"),
        user=get_match_group(match, "user"),
        host=match.group("host"),
        path=match.group("path"),
    )


def get_project_remotes_from_text(
    text: str,
) -> dict[str, dict[str, ProjectRemote]]:
    """Return parsed git remote output."""
    remotes: dict[str, dict[str, ProjectRemote]] = {}
    for line in text.splitlines():
        remote = get_project_remote(line)
        if remote is None:
            continue
        remotes.setdefault(remote.name, {})
        remotes[remote.name][remote.type_] = remote
    return remotes


def get_project_remotes() -> dict[str, dict[str, ProjectRemote]]:
    """Return project remotes from git."""
    _code, stdout, _stderr = git.cmd_output("git", "remote", "-v")
    return get_project_remotes_from_text(stdout)


def get_project_paths() -> list[Path]:
    """Return list of project files from git."""
    return [Path(path) for path in git.get_all_files()]


def get_project_root() -> Path:
    """Return git project root path."""
    return Path(git.get_root())


def get_project_remote_names() -> list[str]:
    """Return git remote names."""
    return list(get_project_remotes())


def get_project_head_branches() -> dict[str, str]:
    """Return git project HEAD branch names for each origin.

    ex. {"origin": "main"}
    """
    remote_names = get_project_remote_names()
    heads: dict[str, str] = {}
    for remote_name in remote_names:
        try:
            _code, stdout, _stderr = git.cmd_output(
                "git",
                "rev-parse",
                "--abbrev-ref",
                f"{remote_name}/HEAD",
            )
        except CalledProcessError:
            continue
        head = stdout.strip()
        heads[remote_name] = head.removeprefix(f"{remote_name}/")
    return heads


def get_project_head_branch() -> str | None:
    """Return the git project HEAD branch name of the first origin."""
    heads = get_project_head_branches()
    if not heads:
        return None
    return heads[next(iter(heads))]
