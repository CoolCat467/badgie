from pathlib import Path
from typing import Optional, Union

from attrs import define, field


@define(frozen=True, slots=True, kw_only=True)
class Badge:
    name: str
    description: str
    example: str

    title: str
    link: str
    image: str

    weight: int = 0


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
class RemoteMatch:
    host: str
    path_prefix: Optional[str] = None


@define(frozen=True, slots=True, kw_only=True)
class Remote(Node):
    host: str
    path: Optional[str] = None


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
class GitLabProject(Node):
    url: str
    ref: str
    namespace: str
    name: str
    full_name: str
    path: str
    full_path: str


@define(frozen=True, slots=True, kw_only=True)
class Hook(Node):
    repo: str
    hook: str


@define(frozen=True, slots=True, kw_only=True)
class HookMatch:
    repo: str
    hook: str


@define(slots=True, kw_only=True)
class Context:
    path: Path

    nodes: dict[str, list[Node]] = field(factory=dict)
    tokens_found: set[Node] = field(factory=set)
    tokens_processed: set[Node] = field(factory=set)

    def add_nodes(self, nodes):
        for node in nodes:
            for token in node.tokens:
                self.nodes.setdefault(token, [])
                self.nodes[token].append(node)
            self.tokens_found |= node.tokens

    def run(self, module):
        nodes = module.run(self)
        self.add_nodes(nodes)
