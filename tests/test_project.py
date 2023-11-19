import pytest

from badgie.project import (ProjectRemote, get_match_group,
                            get_project_remotes_from_text, match_remote_url)


@pytest.mark.parametrize(
    "url,scheme,user,host,path",
    (
        (
            "https://gitlab.com/brettops/ansible/roles/kubectl.git",
            "https",
            None,
            "gitlab.com",
            "brettops/ansible/roles/kubectl",
        ),
        (
            "git@gitlab.com:brettops/ansible/roles/kubectl.git",
            None,
            "git",
            "gitlab.com",
            "brettops/ansible/roles/kubectl",
        ),
    ),
)
def test_get_project_remote(url, scheme, user, host, path):
    match = match_remote_url(url)
    assert get_match_group(match, "scheme") == scheme
    assert get_match_group(match, "user") == user
    assert match.group("host") == host
    assert match.group("path") == path


def test_get_project_remotes_from_text():
    text = (
        "origin	git@gitlab.com:brettops/tools/badgie.git (fetch)\n"
        "origin	git@gitlab.com:brettops/tools/badgie.git (push)\n"
    )
    remote = ProjectRemote(
        name="origin",
        type="fetch",
        url="git@gitlab.com:brettops/tools/badgie.git",
        user="git",
        host="gitlab.com",
        path="brettops/tools/badgie",
        scheme=None,
    )
    remotes = get_project_remotes_from_text(text)
    assert remotes[remote.name][remote.type].user == remote.user
    assert remotes[remote.name][remote.type].host == remote.host
    assert remotes[remote.name][remote.type].url == remote.url
    assert remotes[remote.name][remote.type].path == remote.path
    assert remotes[remote.name][remote.type].name == remote.name
    assert remotes[remote.name][remote.type].type == remote.type
    assert remotes[remote.name][remote.type].scheme == remote.scheme
