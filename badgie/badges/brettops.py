from ..models import Remote
from ._base import Badge, register_badge


@register_badge
class BrettOpsBadge(Badge):
    name = "brettops"

    remotes = (
        Remote(prefix="https://gitlab.com/brettops/containers/", name="container"),
        Remote(prefix="https://gitlab.com/brettops/pipelines/", name="pipeline"),
        Remote(prefix="https://gitlab.com/brettops/tools/", name="tool"),
        Remote(prefix="https://gitlab.com/brettops/ansible/roles/", name="role"),
    )

    def get_link_title(self):
        return f"brettops {self.remote.name}"

    def get_badge_image_url(self):
        return f"https://img.shields.io/badge/brettops-{self.remote.name}-209cdf?labelColor=162d50"

    def get_link_url(self):
        return "https://brettops.io"
