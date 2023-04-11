from ._base import Badge, register_badge


class GitLabPipelineStatusBadge(Badge):
    name = "gitlab-pipeline-status"

    link_title = "pipeline status"

    files = (".gitlab-ci.yml",)

    def get_badge_image_url(self):
        return f"{self.project_url}/badges/{self.project_ref}/pipeline.svg"

    def get_link_url(self):
        return f"{self.project_url}/-/commits/{self.project_ref}"


register_badge(GitLabPipelineStatusBadge)
