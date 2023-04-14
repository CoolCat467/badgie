import json
import os
import urllib.error
import urllib.request
from pathlib import Path

import gitlab

from ..models import Project

GITLAB_URL = "https://gitlab.com"
API_V4_URL = f"{GITLAB_URL}/api/v4"

gl = gitlab.Gitlab(private_token=os.environ.get("GITLAB_PRIVATE_TOKEN", None))

HEADERS: dict[str, str] = {}
private_token = os.environ.get("GITLAB_PRIVATE_TOKEN")
if private_token:
    HEADERS.update({"PRIVATE-TOKEN": private_token})


def get_project(remote_path):
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


def get_latest_pipeline(glproject):
    try:
        return glproject.pipelines.get("latest", ref=glproject.default_branch)
    except gitlab.exceptions.GitlabGetError:
        return None


def get_latest_release(project_id):
    try:
        url = f"{API_V4_URL}/projects/{project_id}/releases/permalink/latest"
        request = urllib.request.Request(url=url, headers=HEADERS)
        response = urllib.request.urlopen(request)
        content = response.read()
        return json.loads(content)
    except urllib.error.HTTPError:
        return None
