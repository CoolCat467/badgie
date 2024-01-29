from badgie.badges import _base as base
from badgie.models import Badge

assert isinstance(base._BADGES, dict)


def test_register_badge() -> None:
    name = "unique-text-xxyyzzq-waffles"
    badge = Badge(
        name=name,
        description="descriptor",
        example="example text",
        title="Unique Waffles",
        link="https://github.com/CoolCat467",
        image="imegris",
        weight=3,
    )
    assert badge not in base._BADGES.values()
    try:
        assert base.register_badge(badge) is badge
        assert base._BADGES[name] is badge
    finally:
        base._BADGES.pop(name)
