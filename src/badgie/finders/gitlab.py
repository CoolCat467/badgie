"""Talk to gitlab's API."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Final

import gitlab

from badgie import tokens as to
from badgie.models import Context, GitLabProject, Project, Remote

GITLAB_URL: Final = "https://gitlab.com"
API_V4_URL: Final = f"{GITLAB_URL}/api/v4"

gl = gitlab.Gitlab(private_token=os.environ.get("GITLAB_PRIVATE_TOKEN", None))

HEADERS: dict[str, str] = {}
private_token = os.environ.get("GITLAB_PRIVATE_TOKEN")
if private_token:
    HEADERS.update({"PRIVATE-TOKEN": private_token})


def get_project(
    remote_path: str,
) -> tuple[gitlab.v4.objects.projects.Project, Project]:
    """Return gitlab project and project node."""
    glproject = gl.projects.get(remote_path)

    project = Project(
        local_path=Path.cwd(),
        url=glproject.web_url,
        ref=glproject.default_branch,
        name=glproject.name,
        namespace=glproject.namespace,
        full_name=glproject.name_with_namespace,
        path=glproject.path,
        full_path=glproject.path_with_namespace,
    )

    return glproject, project


def get_latest_pipeline(
    glproject: gitlab.v4.objects.projects.Project,
) -> Any | None:
    """Return latest pipeline or None."""
    try:
        return glproject.pipelines.get("latest", ref=glproject.default_branch)
    except gitlab.exceptions.GitlabGetError:
        return None


def get_latest_release(project_id: str) -> Any | None:
    """Return latest build data."""
    try:
        url = f"{API_V4_URL}/projects/{project_id}/releases/permalink/latest"
        request = urllib.request.Request(  # noqa: S310
            url=url,
            headers=HEADERS,
        )
        response = urllib.request.urlopen(request)  # noqa: S310
        content = response.read()
        return json.loads(content)
    except urllib.error.HTTPError:
        return None


def run(context: Context) -> list[GitLabProject]:
    """Return list of GitLabProject objects."""
    remote = context.nodes[to.GITLAB][0]
    assert isinstance(remote, Remote)
    if remote.path is None:
        return []
    glproject, project = get_project(remote.path)
    gltokens = set()

    # get gitlab latest release badge
    release = get_latest_release(glproject.id)
    if release:
        gltokens.add(to.GITLAB_RELEASE)

    # add gitlab latest pipeline badge
    glpipeline = get_latest_pipeline(glproject)
    if glpipeline is not None:
        gltokens.add(to.GITLAB_PIPELINE)

        # add gitlab coverage badge
        if glpipeline.coverage is not None:
            gltokens.add(to.GITLAB_COVERAGE)

    gitlabproject = GitLabProject(
        tokens=gltokens,
        url=project.url,
        ref=project.ref,
        namespace=project.namespace,
        name=project.name,
        path=project.path,
        full_name=project.full_name,
        full_path=project.full_path,
    )

    return [gitlabproject]
