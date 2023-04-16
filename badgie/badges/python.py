from ..models import Hook
from ._base import Badge, register_badge


@register_badge
class PythonBlackBadge(Badge):
    """
    Show the Black code style badge.
    """

    name = "python-black"
    link_title = "code style: black"

    precommit_hooks = (Hook(repo="https://github.com/psf/black", hook="black"),)

    def get_badge_image_url(self):
        return r"https://img.shields.io/badge/code%20style-black-000000.svg"

    def get_link_url(self):
        return "https://github.com/psf/black"
