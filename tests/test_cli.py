from badgie import cli
from badgie.models import Badge


def test_to_markdown() -> None:
    for badge in cli._BADGES:
        assert isinstance(cli.to_markdown(badge), str)


def test_to_rst() -> None:
    for badge in cli._BADGES:
        assert isinstance(cli.to_rst(badge), str)


def test_get_badge_text() -> None:
    test_badge = Badge(
        name="name",
        description="description",
        example="example",
        title="title",
        link="link",
        image="image",
    )
    assert (
        cli.get_badge_text([test_badge], "markdown")
        == "[![title](image)](link)"
    )
    assert (
        cli.get_badge_text([test_badge], "rst")
        == ".. image:: image\n   :target: link\n   :alt: title"
    )
