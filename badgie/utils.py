"""Utility functions."""

import os
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urlencode, urlparse


def add_to_query(url: str, params: dict[str, str]) -> str:
    """Return url but with urlencoded query adding given parameters."""
    parsed = urlparse(url)

    _params = {}
    for param in parsed.query.split("&"):
        try:
            key, value = param.split("=")
            _params[key] = value
        except ValueError:
            pass

    _params.update(params)

    query = urlencode(_params)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{query}"


@contextmanager
def change_directory(path: Path) -> Generator[None, None, None]:
    """Temporarily change directory to a given path."""
    origin = Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)
