from ..models import Hook
from ._base import Badge, register_badge


@register_badge
class CodeStyleBlackBadge(Badge):
    """
    Show the Black code style badge.
    """

    name = "code-style-black"
    link_title = "code style: black"

    precommit_hooks = (Hook(repo="https://github.com/psf/black", hook="black"),)

    def get_badge_image_url(self):
        return r"https://img.shields.io/badge/code_style-black-000000.svg"

    def get_link_url(self):
        return "https://github.com/psf/black"


@register_badge
class CodeStylePrettierBadge(Badge):
    """
    Show the Prettier code style badge.
    """

    name = "code-style-prettier"
    link_title = "code style: prettier"

    precommit_hooks = (
        Hook(repo="https://github.com/pre-commit/mirrors-prettier", hook="prettier"),
    )

    def get_badge_image_url(self):
        return r"https://img.shields.io/badge/code_style-prettier-ff69b4.svg"

    def get_link_url(self):
        return "https://github.com/prettier/prettier"
