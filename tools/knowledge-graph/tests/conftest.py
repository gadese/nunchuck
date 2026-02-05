"""Synthetic graph fixtures with planted communities and gaps."""

import random

import pytest


def make_planted_graph(
    n_communities: int = 4,
    nodes_per_community: int = 12,
    intra_density: float = 0.4,
    inter_pairs: list[tuple[int, int]] | None = None,
    inter_density: float = 0.05,
    seed: int = 42,
) -> dict:
    """Create a graph with known community structure and planted gaps.

    Args:
        n_communities: Number of communities to plant.
        nodes_per_community: Nodes per community.
        intra_density: Edge density within each community.
        inter_pairs: Community index pairs that should have inter-community edges.
            All other pairs are gaps (zero inter-community edges).
        inter_density: Edge density for connected inter-community pairs.
        seed: Random seed for reproducibility.

    Returns:
        Input dict with 'nodes' and 'edges' keys.
    """
    rng = random.Random(seed)

    communities: list[list[str]] = []
    all_nodes: list[str] = []

    for c in range(n_communities):
        community_nodes = [f"c{c}_n{i}" for i in range(nodes_per_community)]
        communities.append(community_nodes)
        all_nodes.extend(community_nodes)

    edges: list[dict] = []
    seen: set[tuple[str, str]] = set()

    def add_edge(u: str, v: str, relation: str = "related_to") -> None:
        key = (min(u, v), max(u, v))
        if key not in seen and u != v:
            seen.add(key)
            edges.append(
                {
                    "source": u,
                    "target": v,
                    "relation": relation,
                    "weight": round(rng.uniform(0.5, 1.0), 2),
                }
            )

    for community_nodes in communities:
        n = len(community_nodes)
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < intra_density:
                    add_edge(community_nodes[i], community_nodes[j])

    if inter_pairs is None:
        inter_pairs = [(0, 1), (2, 3)]

    for ca_idx, cb_idx in inter_pairs:
        ca = communities[ca_idx]
        cb = communities[cb_idx]
        for u in ca:
            for v in cb:
                if rng.random() < inter_density:
                    add_edge(u, v, relation="cross_community")

    return {"nodes": all_nodes, "edges": edges}


@pytest.fixture
def planted_graph_data() -> dict:
    """Default fixture: 4 communities x 12 nodes, 2 connected pairs, 4 gap pairs."""
    return make_planted_graph(
        n_communities=4,
        nodes_per_community=12,
        intra_density=0.4,
        inter_pairs=[(0, 1), (2, 3)],
        inter_density=0.05,
        seed=42,
    )


@pytest.fixture
def planted_graph_expected_gaps() -> set[tuple[int, int]]:
    """Expected gap pairs (community index pairs with no inter-community edges).

    With inter_pairs=[(0,1), (2,3)], the gap pairs are:
    (0,2), (0,3), (1,2), (1,3)
    """
    all_pairs = {(i, j) for i in range(4) for j in range(i + 1, 4)}
    connected = {(0, 1), (2, 3)}
    return all_pairs - connected


@pytest.fixture
def small_graph_data() -> dict:
    """A small graph with 2 nodes and 1 edge."""
    return {
        "nodes": ["A", "B"],
        "edges": [{"source": "A", "target": "B", "relation": "related", "weight": 1.0}],
    }


@pytest.fixture
def empty_graph_data() -> dict:
    """An empty graph with no nodes or edges."""
    return {"nodes": [], "edges": []}


@pytest.fixture
def single_node_data() -> dict:
    """A graph with a single node and no edges."""
    return {"nodes": ["lonely"], "edges": []}
