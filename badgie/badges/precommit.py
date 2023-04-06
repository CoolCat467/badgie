from ..models import Badge


class PreCommitBadge(Badge):
    link_title = "pre-commit"

    def get_badge_image_url(self):
        return f"https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"

    def get_link_url(self):
        return f"https://github.com/pre-commit/pre-commit"
