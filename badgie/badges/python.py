from .. import tokens as to
from ..models import Badge
from ._base import register_badges

register_badges(
    {
        to.PYTHON_BANDIT: Badge(
            name="python-bandit",
            description="This project uses [Bandit](https://github.com/PyCQA/bandit).",
            example="https://img.shields.io/badge/security-bandit-yellow.svg",
            title="security: bandit",
            link="https://github.com/PyCQA/bandit",
            image="https://img.shields.io/badge/security-bandit-yellow.svg",
            weight=20,
        ),
        to.PYTHON_BLACK: Badge(
            name="python-black",
            description="This project uses [Black](https://github.com/psf/black).",
            example="https://img.shields.io/badge/code_style-black-000000.svg",
            title="code style: black",
            link="https://github.com/psf/black",
            image="https://img.shields.io/badge/code_style-black-000000.svg",
            weight=20,
        ),
        to.PYTHON_DOCFORMATTER: Badge(
            name="python-docformatter",
            description="This project uses [docformatter](https://github.com/PyCQA/docformatter).",
            example="https://img.shields.io/badge/formatter-docformatter-fedcba.svg",
            title="formatter: docformatter",
            link="https://github.com/PyCQA/docformatter",
            image="https://img.shields.io/badge/formatter-docformatter-fedcba.svg",
            weight=20,
        ),
        to.PYTHON_ISORT: Badge(
            name="python-isort",
            description="This project uses [isort](https://github.com/PyCQA/isort).",
            example="https://img.shields.io/badge/imports-isort-1674b1?style=flat&labelColor=ef8336",
            title="imports: isort",
            link="https://pycqa.github.io/isort/",
            image="https://img.shields.io/badge/imports-isort-1674b1?style=flat&labelColor=ef8336",
            weight=20,
        ),
        to.PYTHON_MYPY: Badge(
            name="python-mypy",
            description="This project uses [mypy](https://github.com/python/mypy).",
            example="https://img.shields.io/badge/mypy-checked-2a6db2",
            title="Checked with mypy",
            link="https://mypy-lang.org/",
            image="https://img.shields.io/badge/mypy-checked-2a6db2",
            weight=20,
        ),
    }
)
