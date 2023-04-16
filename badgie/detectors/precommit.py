import sys
from dataclasses import dataclass
from typing import Type

import yaml
from termcolor import colored

from ..badges._base import Badge
from ..models import Project


@dataclass
class PreCommitConfigDetector:
    project: Project

    def __post_init__(self):
        path = self.project.local_path / ".pre-commit-config.yaml"
        self._data = yaml.safe_load(open(path))
        self._entries = set()
        for repo in self._data["repos"]:
            for hook in repo["hooks"]:
                self._entries.add(self._format_entry(repo["repo"], hook["id"]))
        print(
            colored("- I found a", "white", attrs=["bold"]),
            colored(".pre-commit-config.yaml", "blue", attrs=["bold"]),
            colored("file!", "white", attrs=["bold"]),
            file=sys.stderr,
        )

    @staticmethod
    def _format_entry(repo_url: str, hook_id: str):
        if not repo_url.endswith("/"):
            repo_url += "/"
        return "{}{}".format(repo_url.strip(), hook_id.strip())

    def has_hook(self, repo_url, hook_id):
        entry = self._format_entry(repo_url, hook_id)
        return entry in self._entries

    def get_badge(self, badge_class: Type[Badge]):
        try:
            hooks = getattr(badge_class, "precommit_hooks")
        except AttributeError:
            hooks = ()

        for hook in hooks:
            found = self.has_hook(hook.repo, hook.hook)
            if found:
                return badge_class(
                    project=self.project,
                    hook=hook,
                )
