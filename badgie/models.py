"""Dataclass object models."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from attrs import define, field

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path


@define(frozen=True, slots=True, kw_only=True)
class Badge:
    """Badge."""

    name: str
    description: str
    example: str

    title: str
    link: str
    image: str

    weight: int = 0


@define(frozen=True, slots=True, kw_only=True)
class Node:
    """Set of tokens."""

    tokens: set[str]


@define(frozen=True, slots=True, kw_only=True)
class File(Node):
    """File."""

    path: Path
    pattern: str


@define(frozen=True, slots=True, kw_only=True)
class OldRemote:
    """Old remote."""

    name: str
    prefix: str


@define(frozen=True, slots=True, kw_only=True)
class RemoteMatch:
    """Remote host regex match."""

    host: str
    path_prefix: str | None = None


@define(frozen=True, slots=True, kw_only=True)
class Remote(Node):
    """Remote."""

    host: str
    path: str | None = None


@define(frozen=True, slots=True, kw_only=True)
class ProjectRemote:
    """Git remote project."""

    name: str
    type_: str
    url: str
    scheme: str | None
    user: str | None
    host: str
    path: str


@define(frozen=True, slots=True, kw_only=True)
class Project:
    """Git project."""

    local_path: Path
    url: str
    ref: str
    name: str
    namespace: str
    path: str
    full_name: str
    full_path: str

    remotes: dict[str, dict[str, ProjectRemote]] = field(factory=dict)


@define(frozen=True, slots=True, kw_only=True)
class GitLabProject(Node):
    """Gitlab project."""

    url: str
    ref: str
    namespace: str
    name: str
    full_name: str
    path: str
    full_path: str


@define(frozen=True, slots=True, kw_only=True)
class Hook(Node):
    """Pre-commit repo hook."""

    repo: str
    hook: str


@define(frozen=True, slots=True, kw_only=True)
class HookMatch:
    """Hook regex match."""

    repo: str
    hook: str


class ModuleProtocol(Protocol):
    """Modules implement a run function that accept context and returns iterable of Node objects."""

    @staticmethod
    def run(context: Context) -> Iterable[Node]:
        """Run context and return Nodes."""
        ...


@define(slots=True, kw_only=True)
class Context:
    """Project context."""

    path: Path

    nodes: dict[str, list[Node]] = field(factory=dict)
    tokens_found: set[str] = field(factory=set)
    tokens_processed: set[Node] = field(factory=set)

    def add_nodes(self, nodes: Iterable[Node]) -> None:
        """Read nodes and add tokens."""
        for node in nodes:
            for token in node.tokens:
                self.nodes.setdefault(token, [])
                self.nodes[token].append(node)
            self.tokens_found |= node.tokens

    def run(self, module: ModuleProtocol) -> None:
        """Run on module and add nodes."""
        nodes = module.run(self)
        self.add_nodes(nodes)
