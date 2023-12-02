from badgie.parser import parse_text


def test_parse_text() -> None:
    assert (
        parse_text(
            """cats are great.
<!-- BADGIE TIME -->

meep meep will be gone

<!-- END BADGIE TIME -->

more text woo
waffles

```console
<!-- BADGIE TIME -->

meep example shouldn't be gone

<!-- END BADGIE TIME -->
```

the end.""",
            "this is a badge text my friends.",
        )
        == """cats are great.
<!-- BADGIE TIME -->

this is a badge text my friends.

<!-- END BADGIE TIME -->

more text woo
waffles

```console
<!-- BADGIE TIME -->

meep example shouldn't be gone

<!-- END BADGIE TIME -->
```

the end."""
    )
