"""Base badge functionality."""

from typing import TypeVar

from badgie.models import Badge

_BADGES: dict[str, Badge] = {}


T = TypeVar("T")


def register_badge(klass: Badge) -> Badge:
    """Register a badge module."""
    assert klass.name not in _BADGES
    _BADGES[klass.name] = klass
    return klass


def register_badges(badges: dict[str, Badge]) -> None:
    """Register multiple badges."""
    for token, badge in badges.items():
        assert token not in _BADGES
        _BADGES[token] = badge


def get_badge(token: str) -> Badge:
    """Get a badge given the badge token it's associated with."""
    assert _BADGES[token]
    return _BADGES[token]
