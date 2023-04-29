import sys
from typing import Optional

from attrs import define
from termcolor import colored

from ..models import Hook, Project, Remote


@define
class Badge:
    project: Project
    remote: Optional[Remote] = None
    hook: Optional[Hook] = None

    def __attrs_post_init__(self):
        print(
            colored(
                "- adding a {name} badge".format(
                    name=colored(self.__class__.name, "blue", attrs=["bold"])
                )
            ),
            file=sys.stderr,
        )

    def get_badge_image_url(self):
        raise NotImplementedError

    def get_link_title(self):
        try:
            return self.link_title
        except AttributeError:
            return ""

    def get_link_url(self):
        return self.project.url

    def get_markdown(self):
        return f"[![{self.get_link_title()}]({self.get_badge_image_url()})]({self.get_link_url()})"


_BADGES = {}


def register_badge(klass):
    assert klass.name not in _BADGES
    _BADGES[klass.name] = klass
    return klass


def get_badge(name):
    assert _BADGES[name]
