"""Tokenization and adding badge list to README contents."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, NamedTuple

from badgie.constants import PATTERN_END, PATTERN_START

if TYPE_CHECKING:
    from collections.abc import Generator


class Token(NamedTuple):
    """Token named tuple."""

    value: str
    line: int
    column: int
    type_: str | None = None


def tokenize(text: str) -> Generator[Token, None, None]:
    """Yield tokens from regex matching."""
    token_specification = [
        ("BLOCK", r"```"),
        ("START", PATTERN_START),
        ("END", PATTERN_END),
        ("TEXT", r"."),
        ("NEWLINE", r"\n"),
    ]
    tok_regex = re.compile(
        "|".join("(?P<{}>{})".format(*pair) for pair in token_specification),
    )
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        yield Token(type_=kind, value=value, line=line_num, column=column)


def parse_text(text: str, badge_text: str = "") -> str:
    """Return text after replacing badge block with given badge text."""
    tokens = list(tokenize(text))
    output = ""
    in_block = False
    while tokens:
        token = tokens.pop(0)
        if token.type_ == "START":
            output += token.value
            if not in_block:
                while token.type_ != "END":
                    token = tokens.pop(0)
                output += f"\n\n{badge_text}\n\n"
                output += token.value

        # added this only to support documenting the feature
        elif token.type_ == "BLOCK":
            output += token.value
            in_block = not in_block

        elif token.type_ == "NEWLINE":
            output += "\n"
        else:
            output += token.value
    return output
