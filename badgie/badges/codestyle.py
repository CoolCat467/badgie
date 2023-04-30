from .. import tokens as to
from ..models import Badge
from ._base import register_badges

register_badges(
    {
        to.PYTHON_BLACK: Badge(
            name="code-style-black",
            description="Show the Black code style.",
            example="https://img.shields.io/badge/code_style-black-000000.svg",
            title="code style: black",
            link="https://github.com/psf/black",
            image="https://img.shields.io/badge/code_style-black-000000.svg",
            weight=20,
        ),
        to.PRETTIER: Badge(
            name="code-style-prettier",
            description="Show the Prettier code style badge.",
            example="https://img.shields.io/badge/code_style-prettier-ff69b4.svg",
            title="code style: prettier",
            link="https://github.com/prettier/prettier",
            image="https://img.shields.io/badge/code_style-prettier-ff69b4.svg",
            weight=20,
        ),
    }
)
