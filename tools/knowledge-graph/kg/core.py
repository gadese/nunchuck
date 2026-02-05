"""Graph construction and all analysis logic."""

import networkx as nx
from networkx.algorithms.community import louvain_communities, modularity

from kg.models import AnalysisReport, Community, Gap
from kg.validate import validate

MIN_NODES_FOR_LOUVAIN = 3
MIN_NODES_FOR_CENTRALITY = 2
DEFAULT_CENTRALITY_K = 100
DEFAULT_CENTRALITY_SEED = 42
TOP_NODES_PER_COMMUNITY = 5
TOP_CONCEPTS_PER_GAP = 3


def build_graph(data: dict) -> nx.Graph:
    """Construct a NetworkX graph from validated input JSON."""
    G = nx.Graph()
    G.add_nodes_from(data["nodes"])
    for edge in data["edges"]:
        G.add_edge(
            edge["source"],
            edge["target"],
            relation=edge["relation"],
            weight=edge["weight"],
        )
    return G


def detect_communities(
    G: nx.Graph, resolution: float = 1.0, seed: int = 42
) -> tuple[Community, ...]:
    """Detect communities using Louvain algorithm.

    For graphs with fewer than 3 nodes, each connected component is a community.
    """
    if len(G) < MIN_NODES_FOR_LOUVAIN:
        partitions = [frozenset(c) for c in nx.connected_components(G)]
    else:
        partitions = [
            frozenset(c)
            for c in louvain_communities(G, resolution=resolution, seed=seed)
        ]

    centrality = compute_centrality(G)

    communities: list[Community] = []
    for i, nodes in enumerate(sorted(partitions, key=lambda s: (-len(s), min(s)))):
        top = sorted(
            ((n, centrality.get(n, 0.0)) for n in nodes),
            key=lambda x: (-x[1], x[0]),
        )[:TOP_NODES_PER_COMMUNITY]
        communities.append(Community(id=i, nodes=nodes, top_nodes=tuple(top)))

    return tuple(communities)


def compute_centrality(G: nx.Graph, k: int | None = None) -> dict[str, float]:
    """Compute approximate betweenness centrality with k-sampling."""
    if len(G) < MIN_NODES_FOR_CENTRALITY:
        return {n: 0.0 for n in G.nodes()}

    if k is None:
        k = min(DEFAULT_CENTRALITY_K, len(G))

    return nx.betweenness_centrality(G, k=k, seed=DEFAULT_CENTRALITY_SEED)


def detect_gaps(
    G: nx.Graph,
    communities: tuple[Community, ...],
    threshold: float = 0.05,
) -> tuple[Gap, ...]:
    """Detect gaps: community pairs with low inter-community connectivity.

    density = actual_inter_edges / possible_inter_edges
    Pairs below threshold are gaps.
    """
    gaps: list[Gap] = []

    for i, ca in enumerate(communities):
        for j in range(i + 1, len(communities)):
            cb = communities[j]

            possible = len(ca.nodes) * len(cb.nodes)
            if possible == 0:
                continue

            actual = sum(1 for u in ca.nodes for v in cb.nodes if G.has_edge(u, v))
            density = actual / possible

            if density < threshold:
                top_a = tuple(n for n, _ in ca.top_nodes[:TOP_CONCEPTS_PER_GAP])
                top_b = tuple(n for n, _ in cb.top_nodes[:TOP_CONCEPTS_PER_GAP])
                gaps.append(
                    Gap(
                        community_a=ca.id,
                        community_b=cb.id,
                        density=density,
                        top_concepts_a=top_a,
                        top_concepts_b=top_b,
                    )
                )

    return tuple(sorted(gaps, key=lambda g: (g.density, g.community_a, g.community_b)))


def find_bridges(
    G: nx.Graph,
    communities: tuple[Community, ...],
    centrality: dict[str, float],
) -> tuple[tuple[str, float], ...]:
    """Find bridge nodes: high-betweenness nodes spanning multiple communities."""
    node_to_community: dict[str, int] = {}
    for c in communities:
        for n in c.nodes:
            node_to_community[n] = c.id

    bridges: list[tuple[str, float]] = []
    for node in G.nodes():
        neighbor_communities = {
            node_to_community[nb] for nb in G.neighbors(node) if nb in node_to_community
        }
        own_community = node_to_community.get(node)
        if own_community is not None:
            neighbor_communities.add(own_community)

        if len(neighbor_communities) > 1:
            bridges.append((node, centrality.get(node, 0.0)))

    return tuple(sorted(bridges, key=lambda x: (-x[1], x[0])))


def analyze(
    data: dict,
    resolution: float = 1.0,
    seed: int = 42,
    gap_threshold: float = 0.05,
) -> AnalysisReport:
    """Orchestrator: validate -> build -> detect -> compute -> report."""
    errors = validate(data)
    if errors:
        raise ValueError(f"Input validation failed: {'; '.join(errors)}")

    G = build_graph(data)
    communities = detect_communities(G, resolution=resolution, seed=seed)

    partition = [set(c.nodes) for c in communities]
    mod = (
        modularity(G, partition) if len(communities) > 1 and len(G.edges()) > 0 else 0.0
    )

    centrality = compute_centrality(G)
    gaps = detect_gaps(G, communities, threshold=gap_threshold)
    bridges = find_bridges(G, communities, centrality)

    return AnalysisReport(
        communities=communities,
        gaps=gaps,
        bridges=bridges,
        modularity=mod,
        node_count=len(G.nodes()),
        edge_count=len(G.edges()),
    )
