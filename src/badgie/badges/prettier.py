"""Prettier hook badge."""

from badgie import tokens as to
from badgie.badges._base import register_badges
from badgie.models import Badge

register_badges(
    {
        to.PRETTIER: Badge(
            name="prettier",
            description="Show the Prettier code style badge.",
            example="https://img.shields.io/badge/code_style-prettier-ff69b4.svg",
            title="code style: prettier",
            link="https://github.com/prettier/prettier",
            image="https://img.shields.io/badge/code_style-prettier-ff69b4.svg",
            weight=20,
        ),
    },
)
