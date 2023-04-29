import re
from typing import Optional

from attrs import define

from .constants import PATTERN_END, PATTERN_START


@define
class Token:
    value: str
    line: int
    column: int
    type: Optional[str] = None


def tokenize(text: str):
    token_specification = [
        ("BLOCK", r"```"),
        ("START", PATTERN_START),
        ("END", PATTERN_END),
        ("TEXT", r"."),
        ("NEWLINE", r"\n"),
    ]
    tok_regex = "|".join("(?P<%s>%s)" % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        yield Token(type=kind, value=value, line=line_num, column=column)


def parse_text(text: str, badge_text: str = ""):
    tokens = list(tokenize(text))
    output = ""
    in_block = False
    while tokens:
        token = tokens.pop(0)
        if token.type == "START":
            output += token.value
            if not in_block:
                while token.type != "END":
                    token = tokens.pop(0)
                output += f"\n\n{badge_text}\n\n"
                output += token.value

        # added this only to support documenting the feature
        elif token.type == "BLOCK":
            output += token.value
            in_block = not in_block

        elif token.type == "NEWLINE":
            output += "\n"
        else:
            output += token.value
    return output
