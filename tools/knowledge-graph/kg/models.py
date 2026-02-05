"""Frozen dataclasses shared between core.py and render.py."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Community:
    """A detected community of concept nodes."""

    id: int
    nodes: frozenset[str]
    top_nodes: tuple[tuple[str, float], ...]


@dataclass(frozen=True)
class Gap:
    """A pair of communities with low inter-community connectivity."""

    community_a: int
    community_b: int
    density: float
    top_concepts_a: tuple[str, ...]
    top_concepts_b: tuple[str, ...]


@dataclass(frozen=True)
class AnalysisReport:
    """Complete analysis result passed to renderers."""

    communities: tuple[Community, ...]
    gaps: tuple[Gap, ...]
    bridges: tuple[tuple[str, float], ...]
    modularity: float
    node_count: int
    edge_count: int
