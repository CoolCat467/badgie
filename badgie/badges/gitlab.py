from ..models import Badge


class GitLabCIPipelinesBadge(Badge):
    link_title = "pipeline status"

    def get_badge_image_url(self):
        return f"{self.project_url}/badges/{self.project_ref}/pipeline.svg"

    def get_link_url(self):
        return f"{self.project_url}/-/commits/{self.project_ref}"
