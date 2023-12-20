"""Utility functions."""

from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urlencode, urlparse

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


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


def combine_end(data: Iterable[str], final: str = "and") -> str:
    """Return comma separated string of list of strings with last item phrased properly."""
    data = list(data)
    if len(data) >= 2:
        data[-1] = f"{final} {data[-1]}"
    if len(data) > 2:
        return ", ".join(data)
    return " ".join(data)
