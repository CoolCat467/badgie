from .. import tokens as to
from ..models import Badge
from ._base import register_badges


def brettops_badge(name):
    return Badge(
        name=f"brettops-{name}",
        description=f"Show that this {name} project is a BrettOps project.",
        example=f"https://img.shields.io/badge/brettops-{name}-209cdf?labelColor=162d50",
        title=f"brettops {name}",
        link="https://brettops.io",
        image=f"https://img.shields.io/badge/brettops-{name}-209cdf?labelColor=162d50",
        weight=-100,
    )


register_badges(
    {
        to.BRETTOPS_CONTAINER: brettops_badge("container"),
        to.BRETTOPS_PACKAGE: brettops_badge("package"),
        to.BRETTOPS_PIPELINE: brettops_badge("pipeline"),
        to.BRETTOPS_ROLE: brettops_badge("role"),
        to.BRETTOPS_TOOL: brettops_badge("tool"),
    }
)
