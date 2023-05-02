import argparse
import importlib
import json
import logging
import os
import sys
from pathlib import Path
from typing import Optional

from termcolor import colored

from . import tokens as to
from ._version import __version__
from .badges._base import _BADGES
from .finders import files, gitlab, pre_commit_config, remotes
from .models import Badge, Context
from .parser import parse_text
from .project import get_project_root
from .utils import add_to_query, change_directory


def to_markdown(badge):
    return f"[![{badge.title}]({badge.image})]({badge.link})"


def get_badge_text(badges, format="markdown"):
    lines = []
    for badge in badges:
        try:
            lines.append(getattr(badge, f"get_{format}")())
        except AttributeError:
            lines.append(to_markdown(badge))
    return "\n".join(lines)


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
        init_badges()
        for badge in sorted(_BADGES.values(), key=lambda x: x.name):
            print(
                "{name}: {description}".format(
                    name=colored(badge.name, "yellow"),
                    description=badge.description.strip(),
                )
            )
        parser.exit()


class DumpAction(argparse.Action):
    def __init__(
        self,
        option_strings,
        dest=argparse.SUPPRESS,
        default=argparse.SUPPRESS,
        help="dump badge data",
    ):
        super().__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help,
        )

    def __call__(self, parser, _namespace, _values, _option_string=None):
        init_badges()
        badges = []
        for badge in sorted(_BADGES.values(), key=lambda x: x.name):
            badges.append(
                dict(
                    name=badge.name,
                    description=badge.description.strip(),
                    example=badge.example,
                )
            )
        from datetime import datetime

        print(
            json.dumps(
                dict(
                    generated=datetime.utcnow().isoformat(),
                    badges=badges,
                ),
                indent=4,
            )
        )
        parser.exit()


def init_badges():
    location = Path(__file__).parent
    modules = list(location.glob("badges/[a-z]*.py"))
    modules = [
        os.path.splitext(
            "badgie.{}".format(str(module.relative_to(location)).replace(os.sep, "."))
        )[0]
        for module in modules
    ]
    for module in modules:
        logging.info("loading %s badge provider", module)
        importlib.import_module(module)


def assemble_badge_list(context: Context, style: Optional[str] = None) -> list[Badge]:
    badges = []
    for token, nodelist in context.nodes.items():
        if token in _BADGES:
            badge = _BADGES[token]
            print(
                "- adding a {name} badge".format(name=colored(badge.name, "yellow")),
                file=sys.stderr,
            )
            node = nodelist[0]

            image = badge.image.format(node=node)

            if style:
                image = add_to_query(image, {"style": style})

            finalbadge = Badge(
                name=badge.name,
                description=badge.description,
                example=badge.example,
                title=badge.title.format(node=node),
                link=badge.link.format(node=node),
                image=image,
                weight=badge.weight,
            )

            badges.append(finalbadge)

    return sorted(badges, key=lambda badge: badge.weight)


def build_badge_context() -> Context:
    project_root = get_project_root()

    with change_directory(project_root):
        init_badges()

        context = Context(path=project_root)
        context.run(files)
        context.run(remotes)
        if to.GITLAB in context.nodes:
            context.run(gitlab)
        if to.PRE_COMMIT_CONFIG in context.nodes:
            context.run(pre_commit_config)

        return context


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", action=ListAction, help="list available badges")
    parser.add_argument("--dump-badge-data", action=DumpAction, help="dump badge data")
    parser.add_argument(
        "-w", "--write", action="store_true", help="write changes to the file"
    )
    parser.add_argument(
        "-s",
        "--style",
        choices=["plastic", "flat", "flat-square", "for-the-badge", "social"],
        help="change badge style",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument("files", nargs="+", metavar="FILE", help="input files")

    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)

    for file in args.files:
        if not Path(file).exists() or not Path(file).is_file():
            parser.error(f"Unable to find file: {file}")

    print(
        colored("Hi, I'm", "white", attrs=["bold"]),
        colored("Badgie!", "yellow", attrs=["bold"]),
        colored("Let's add some badges!", "white", attrs=["bold"]),
        colored("🐦\n", "cyan", attrs=["bold"]),
        file=sys.stderr,
    )

    context = build_badge_context()
    badges = assemble_badge_list(context, style=args.style)
    badge_text = get_badge_text(badges=badges)

    print(
        colored("\nThat's like", "white", attrs=["bold"]),
        colored(f"{len(badges)} badges!", "yellow", attrs=["bold"]),
        colored("Good job!", "white", attrs=["bold"]),
        colored("🐦", "cyan", attrs=["bold"]),
        file=sys.stderr,
    )

    for file in args.files:
        text = open(file, "r").read()
        output = parse_text(text, badge_text=badge_text)
        if args.write:
            with open(file, "w") as handle:
                handle.write(output)
        else:
            print(output)
