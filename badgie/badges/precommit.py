from badgie import tokens as to
from badgie.badges._base import register_badges
from badgie.models import Badge

register_badges(
    {
        to.PRE_COMMIT_CONFIG: Badge(
            name="pre-commit-enabled",
            description="Show that the repository is using pre-commit.",
            example="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit",
            title="pre-commit",
            link="https://github.com/pre-commit/pre-commit",
            image="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit",
            weight=10,
        ),
    },
)
