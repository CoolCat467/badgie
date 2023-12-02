from badgie import cli


def test_to_markdown() -> None:
    for badge in cli._BADGES:
        assert isinstance(cli.to_markdown(badge), str)
