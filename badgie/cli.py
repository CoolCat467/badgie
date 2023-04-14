import argparse
import logging
import re
import subprocess
import sys

from termcolor import colored

from ._version import __version__
from .badges._base import _BADGES
from .badges.brettops import BrettOpsBadge
from .badges.gitlab import (
    GitLabCoverageReportBadge,
    GitLabLatestReleaseBadge,
    GitLabPipelineStatusBadge,
)
from .badges.precommit import PreCommitBadge
from .constants import PATTERN_GIT_SSH
from .parser import parse_text
from .providers import gitlab as gitlab_provider
from .sources import get_badge_from_files, get_badge_from_remotes

RE_GIT_SSH = re.compile(PATTERN_GIT_SSH)

logging.basicConfig(level=logging.WARNING)


def get_badge_text(badges, format="markdown"):
    return "\n".join(getattr(badge, f"get_{format}")() for badge in badges)


class ListAction(argparse.Action):
    def __init__(
        self,
        option_strings,
        dest=argparse.SUPPRESS,
        default=argparse.SUPPRESS,
        help="list supported badges and exit",
    ):
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help,
        )

    def __call__(self, parser, _namespace, _values, _option_string=None):
        for name, badge in sorted(_BADGES.items(), key=lambda x: x[0]):
            # print(name, badge)
            print(
                "{name}: {description}".format(
                    name=colored(name, "cyan", attrs=["bold"]),
                    description=badge.__doc__.strip(),
                )
            )
        parser.exit()


def find_badges(text):
    badges = []
    process = subprocess.run(["git", "remote", "-v"], text=True, capture_output=True)
    url = process.stdout.splitlines()[0].split("\t")[1].split(" ")[0]
    match = RE_GIT_SSH.match(url)
    if match:
        if match.group("host") == "gitlab.com":
            glproject, project = gitlab_provider.get_project(match.group("path"))

            # add brettops badge
            new_badge = get_badge_from_remotes(
                badge_class=BrettOpsBadge, project=project
            )
            if new_badge is not None:
                badges.append(new_badge)

            # get gitlab latest release badge
            release = gitlab_provider.get_latest_release(glproject.id)
            if release:
                badges.append(
                    GitLabLatestReleaseBadge(
                        project=project,
                    )
                )

            # add gitlab latest pipeline badge
            glpipeline = gitlab_provider.get_latest_pipeline(glproject)
            if glpipeline is not None:
                badges.append(GitLabPipelineStatusBadge(project=project))

                # add gitlab coverage badge
                if glpipeline.coverage is not None:
                    badges.append(
                        GitLabCoverageReportBadge(
                            project=project,
                        )
                    )

            # add pre-commit badge
            new_badge = get_badge_from_files(
                badge_class=PreCommitBadge, project=project
            )
            if new_badge is not None:
                badges.append(new_badge)
    return badges


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", action=ListAction, help="list available badges")
    parser.add_argument(
        "-w", "--write", action="store_true", help="write changes to the file"
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "input",
    )

    args = parser.parse_args()

    text = open(args.input, "r").read()

    print(
        colored("Hi, I'm", "cyan", attrs=["bold"]),
        colored("Badgie!", "white", attrs=["bold"]),
        colored("Let's add some badges! 🐦\n", "cyan", attrs=["bold"]),
        file=sys.stderr,
    )

    badges = find_badges(text=text)
    badge_text = get_badge_text(badges=badges)
    output = parse_text(text, badge_text=badge_text)

    print(
        colored("\nThat's like", "cyan", attrs=["bold"]),
        colored(f"{len(badges)} badges!", "white", attrs=["bold"]),
        colored("Good job! 🐦", "cyan", attrs=["bold"]),
        file=sys.stderr,
    )

    if args.write:
        with open(args.input, "w") as handle:
            handle.write(output)
    else:
        print(output)
