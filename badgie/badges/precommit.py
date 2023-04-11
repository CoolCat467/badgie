from ._base import Badge, register_badge


@register_badge
class PreCommitBadge(Badge):
    name = "pre-commit-enabled"

    link_title = "pre-commit"

    # Path.glob matching
    files = (".pre-commit-config.yaml",)

    def get_badge_image_url(self):
        return f"https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"

    def get_link_url(self):
        return f"https://github.com/pre-commit/pre-commit"
