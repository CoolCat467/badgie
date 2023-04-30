from .. import tokens as to
from ..models import Badge
from ._base import register_badges

register_badges(
    {
        to.GITLAB_COVERAGE: Badge(
            name="gitlab-coverage-report",
            description="Show the most recent coverage score on the default branch.",
            example="https://img.shields.io/gitlab/pipeline-coverage/brettops/tools/badgie?branch=main",
            title="coverage report",
            link="{node.url}/-/commits/{node.ref}",
            image="https://img.shields.io/gitlab/pipeline-coverage/{node.full_path}?branch={node.ref}",
            weight=1,
        ),
        to.GITLAB_PIPELINE: Badge(
            name="gitlab-pipeline-status",
            description="Show the most recent pipeline status on the default branch.",
            example="https://img.shields.io/gitlab/pipeline-status/brettops/tools/badgie?branch=main",
            title="pipeline status",
            link="{node.url}/-/commits/{node.ref}",
            image="https://img.shields.io/gitlab/pipeline-status/{node.full_path}?branch={node.ref}",
            weight=0,
        ),
        to.GITLAB_RELEASE: Badge(
            name="gitlab-latest-release",
            description="Show the latest GitLab release by date.",
            example="https://img.shields.io/gitlab/v/release/brettops/tools/badgie",
            title="latest release",
            link="{node.url}/-/releases",
            image="https://img.shields.io/gitlab/v/release/{node.full_path}",
            weight=2,
        ),
    }
)
