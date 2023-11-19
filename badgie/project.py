import re
import subprocess
from pathlib import Path
from typing import Optional

from badgie.models import ProjectRemote

REMOTES = [
    r"(?P<user>git)@(?P<host>.*?):(?P<path>.*?)\.git",
    r"(?P<scheme>\w+):\/\/(?P<host>[^\/]*?)\/(?P<path>.*)\.git",
]

RE_REMOTES = [re.compile(remote) for remote in REMOTES]


def match_remote_url(url: str) -> re.Match[str] | None:
    for remote in RE_REMOTES:
        match = remote.match(url)
        if match:
            return match
    return None


def get_match_group(match: re.Match[str], name: str) -> str | None:
    try:
        return match.group(name)
    except IndexError:
        return None


def get_project_remote(line: str) -> ProjectRemote | None:
    name, parts = line.split("\t")
    url, type = parts.split(" ")
    type = type.replace("(", "").replace(")", "")
    match = match_remote_url(url)
    if not match:
        return None
    return ProjectRemote(
        name=name,
        type=type,
        url=url,
        scheme=get_match_group(match, "scheme"),
        user=get_match_group(match, "user"),
        host=match.group("host"),
        path=match.group("path"),
    )


def get_project_remotes_from_text(text: str) -> dict[str, dict[str, ProjectRemote]]:
    remotes: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        remote = get_project_remote(line)
        if remote is None:
            continue
        remotes.setdefault(remote.name, {})
        remotes[remote.name][remote.type] = remote
    return remotes


def get_project_remotes() -> dict[str, dict[str, ProjectRemote]]:
    process = subprocess.run(
        ["git", "remote", "-v"], text=True, capture_output=True
    )  # nosec
    return get_project_remotes_from_text(process.stdout)


def get_project_paths() -> list[Path]:
    return [
        Path(path)
        for path in subprocess.run(
            ["git", "ls-files"], text=True, stdout=subprocess.PIPE
        ).stdout.splitlines()  # nosec
    ]


def get_project_root() -> Path:
    return Path(
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"], text=True, stdout=subprocess.PIPE
        ).stdout.strip()  # nosec
    )
