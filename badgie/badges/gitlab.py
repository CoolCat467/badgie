from ._base import Badge, register_badge


@register_badge
class GitLabLatestReleaseBadge(Badge):
    """
    Show the latest GitLab release by date.
    """

    name = "gitlab-latest-release"
    example = "https://img.shields.io/gitlab/v/release/brettops/tools/badgie"

    link_title = "latest release"

    def get_badge_image_url(self):
        return f"https://img.shields.io/gitlab/v/release/{self.project.full_path}"

    def get_link_url(self):
        return f"{self.project.url}/-/releases"


@register_badge
class GitLabCoverageReportBadge(Badge):
    """
    Show the most recent coverage score on the default branch.
    """

    name = "gitlab-coverage-report"
    example = "https://img.shields.io/gitlab/pipeline-coverage/brettops/tools/badgie"

    link_title = "coverage report"

    def get_badge_image_url(self):
        return (
            f"https://img.shields.io/gitlab/pipeline-coverage/{self.project.full_path}"
        )

    def get_link_url(self):
        return f"{self.project.url}/-/commits/{self.project.ref}"


@register_badge
class GitLabPipelineStatusBadge(Badge):
    """
    Show the most recent pipeline status on the default branch.
    """

    name = "gitlab-pipeline-status"
    example = "https://img.shields.io/gitlab/pipeline-status/brettops/tools/badgie"

    link_title = "pipeline status"

    def get_badge_image_url(self):
        return f"https://img.shields.io/gitlab/pipeline-status/{self.project.full_path}"

    def get_link_url(self):
        return f"{self.project.url}/-/commits/{self.project.ref}"
