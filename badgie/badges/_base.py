import logging
from dataclasses import dataclass
from typing import Optional

from ..models import Remote


@dataclass(frozen=True)
class Badge:
    project_url: str
    project_ref: str
    remote: Optional[Remote] = None

    def __post_init__(self):
        logging.info("add %s", self.__class__.name)

    def get_badge_image_url(self):
        raise NotImplementedError

    def get_link_title(self):
        try:
            return self.link_title
        except AttributeError:
            return ""

    def get_link_url(self):
        return self.project_url

    def get_markdown(self):
        return f"[![{self.get_link_title()}]({self.get_badge_image_url()})]({self.get_link_url()})"


_BADGES = {}


def register_badge(klass):
    assert klass.name not in _BADGES
    _BADGES[klass.name] = klass
    return klass


def get_badge(name):
    assert _BADGES[name]
