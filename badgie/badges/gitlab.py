from ._base import Badge, register_badge


@register_badge
class GitLabCoverageReportBadge(Badge):
    name = "gitlab-coverage-report"

    link_title = "coverage report"

    def get_badge_image_url(self):
        return f"{self.project_url}/badges/{self.project_ref}/coverage.svg"

    def get_link_url(self):
        return f"{self.project_url}/-/commits/{self.project_ref}"


@register_badge
class GitLabPipelineStatusBadge(Badge):
    name = "gitlab-pipeline-status"

    link_title = "pipeline status"

    def get_badge_image_url(self):
        return f"{self.project_url}/badges/{self.project_ref}/pipeline.svg"

    def get_link_url(self):
        return f"{self.project_url}/-/commits/{self.project_ref}"
