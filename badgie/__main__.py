import argparse
import os
import random
import re
import string
import subprocess
from typing import NamedTuple

from .badges.gitlab import (  # , GitLabCICoverageBadge, GitLabCILatestReleaseBadge
    GitLabCIPipelinesBadge,
)
from .badges.precommit import PreCommitBadge

PATTERN = r"BADGIE\s+TIME"
PATTERN_START = r"<!--\s+" + PATTERN + r"\s+-->"
PATTERN_END = r"<!--\s+END\s+" + PATTERN + r"\s+-->"

PATTERN_GIT_SSH = r"^(?P<user>git)@(?P<host>.*?):(?P<path>.*?)\.git$"

RE_GIT_SSH = re.compile(PATTERN_GIT_SSH)


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


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
        yield Token(kind, value, line_num, column)


def render_badge(title: str, badge: str, link: str):
    pass


def get_badge_text(badges, format="markdown"):
    return "\n".join(getattr(badge, f"get_{format}")() for badge in badges)


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-w", "--write", action="store_true")
    args = parser.parse_args()

    text = open(args.input, "r").read()
    badges = []
    process = subprocess.run(["git", "remote", "-v"], text=True, capture_output=True)
    url = process.stdout.splitlines()[0].split("\t")[1].split(" ")[0]
    match = RE_GIT_SSH.match(url)
    if match:
        if match.group("host") == "gitlab.com":
            import gitlab

            gl = gitlab.Gitlab(
                private_token=os.environ.get("GITLAB_PRIVATE_TOKEN", None)
            )
            glproject = gl.projects.get(match.group("path"))

            ci_config_path = (
                glproject.ci_config_path
                if glproject.ci_config_path
                else ".gitlab-ci.yml"
            )
            try:
                ci_config = glproject.files.get(
                    file_path=ci_config_path, ref=glproject.default_branch
                )
                badges.append(
                    GitLabCIPipelinesBadge(
                        project_url=glproject.path_with_namespace,
                        project_ref=glproject.default_branch,
                    )
                )
            except gitlab.exceptions.GitlabGetError:
                # no CI config
                pass

            pre_commit_config_path = ".pre-commit-config.yaml"
            try:
                pre_commit_config = glproject.files.get(
                    file_path=pre_commit_config_path, ref=glproject.default_branch
                )
                badges.append(
                    PreCommitBadge(
                        project_url=glproject.path_with_namespace,
                        project_ref=glproject.default_branch,
                    )
                )
            except gitlab.exceptions.GitlabGetError:
                # no CI config
                pass

    badge_text = get_badge_text(badges)
    output = parse_text(text, badge_text=badge_text)
    if args.write:
        with open(args.input, "w") as handle:
            handle.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
