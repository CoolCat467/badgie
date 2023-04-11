import argparse
import logging
import os
import re
import subprocess
from pathlib import Path

from .badges.brettops import BrettOpsBadge
from .badges.gitlab import GitLabCoverageReportBadge  # GitLabCILatestReleaseBadge
from .badges.gitlab import GitLabPipelineStatusBadge
from .badges.precommit import PreCommitBadge
from .constants import PATTERN_GIT_SSH
from .models import Project
from .parser import parse_text
from .sources import get_badge_from_files, get_badge_from_remotes

RE_GIT_SSH = re.compile(PATTERN_GIT_SSH)

logging.basicConfig(level=logging.INFO)


def get_badge_text(badges, format="markdown"):
    return "\n".join(getattr(badge, f"get_{format}")() for badge in badges)


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

            project = Project(
                path=Path.cwd(),
                url=glproject.web_url,
                ref=glproject.default_branch,
            )

            new_badge = get_badge_from_remotes(
                badge_class=BrettOpsBadge, project=project
            )
            if new_badge is not None:
                badges.append(new_badge)

            try:
                glpipeline = glproject.pipelines.get(
                    "latest", ref=glproject.default_branch
                )
            except gitlab.exceptions.GitlabGetError:
                glpipeline = None

            if glpipeline is not None:
                badges.append(
                    GitLabPipelineStatusBadge(
                        project_url=project.url,
                        project_ref=project.ref,
                    )
                )
                if glpipeline.coverage is not None:
                    badges.append(
                        GitLabCoverageReportBadge(
                            project_url=project.url,
                            project_ref=project.ref,
                        )
                    )

            new_badge = get_badge_from_files(
                badge_class=PreCommitBadge, project=project
            )
            if new_badge is not None:
                badges.append(new_badge)

    badge_text = get_badge_text(badges)
    output = parse_text(text, badge_text=badge_text)
    if args.write:
        with open(args.input, "w") as handle:
            handle.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
