from pathlib import Path
from typing import Optional, Union

from attrs import define, field


@define(frozen=True, slots=True, kw_only=True)
class Node:
    tokens: set[str]


@define(frozen=True, slots=True, kw_only=True)
class File(Node):
    path: Path
    pattern: str


@define(frozen=True, slots=True, kw_only=True)
class OldRemote:
    name: str
    prefix: str


@define(frozen=True, slots=True, kw_only=True)
class Remote(Node):
    host: Optional[str] = None
    prefix: Optional[str] = None


@define(frozen=True, slots=True, kw_only=True)
class ProjectRemote:
    name: str
    type: str
    url: str
    scheme: Union[str, None]
    user: Union[str, None]
    host: str
    path: str


@define(frozen=True, slots=True, kw_only=True)
class Project:
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
class Hook:
    repo: str
    hook: str


@define(slots=True, kw_only=True)
class Context:
    path: Path

    nodes: dict[str, list[Node]] = field(factory=dict)
    tokens_found: set[Node] = field(factory=set)
    tokens_processed: set[Node] = field(factory=set)

    providers: dict[Node] = field(factory=dict)
    badges: dict[Node] = field(factory=dict)

    def add_nodes(self, nodes):
        for node in nodes:
            for token in node.tokens:
                self.nodes.setdefault(token, [])
                self.nodes[token].append(node)
            self.tokens_found |= node.tokens
