from typing import Type

from .badges._base import Badge
from .models import Project


def get_badge_from_files(badge_class: Type[Badge], project: Project):
    try:
        files = getattr(badge_class, "files")
    except AttributeError:
        files = ()

    for file in files:
        found = list(project.local_path.glob(file))
        if found:
            return badge_class(
                project=project,
            )


def get_badge_from_remotes(badge_class: Type[Badge], project: Project):
    try:
        remotes = getattr(badge_class, "remotes")
    except AttributeError:
        return

    for remote in remotes:
        if project.url.startswith(remote.prefix):
            return badge_class(project=project, remote=remote)
