"""Tests for analysis logic: communities, gaps, bridges, centrality."""

import pytest

from kg.core import (
    analyze,
    build_graph,
    compute_centrality,
    detect_communities,
    find_bridges,
)
from kg.models import AnalysisReport


class TestBuildGraph:
    def test_node_count(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        assert len(G.nodes()) == len(planted_graph_data["nodes"])

    def test_edge_count(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        assert len(G.edges()) == len(planted_graph_data["edges"])

    def test_edge_attributes(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        for u, v, data in G.edges(data=True):
            assert "relation" in data
            assert "weight" in data
            assert isinstance(data["weight"], float)


class TestDetectCommunities:
    def test_community_count(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        communities = detect_communities(G, seed=42)
        assert len(communities) >= 2

    def test_all_nodes_assigned(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        communities = detect_communities(G, seed=42)
        assigned = set()
        for c in communities:
            assigned.update(c.nodes)
        assert assigned == set(G.nodes())

    def test_no_overlap(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        communities = detect_communities(G, seed=42)
        all_nodes: list[str] = []
        for c in communities:
            all_nodes.extend(c.nodes)
        assert len(all_nodes) == len(set(all_nodes))

    def test_modularity_threshold(self, planted_graph_data: dict) -> None:
        report = analyze(planted_graph_data, seed=42)
        assert report.modularity >= 0.3

    def test_small_graph(self, small_graph_data: dict) -> None:
        G = build_graph(small_graph_data)
        communities = detect_communities(G, seed=42)
        assert len(communities) >= 1

    def test_single_node(self, single_node_data: dict) -> None:
        G = build_graph(single_node_data)
        communities = detect_communities(G, seed=42)
        assert len(communities) == 1
        assert "lonely" in communities[0].nodes


class TestDetectGaps:
    def test_gap_detection_on_planted_graph(
        self,
        planted_graph_data: dict,
        planted_graph_expected_gaps: set[tuple[int, int]],
    ) -> None:
        """Gaps should be detected between communities with no inter-edges."""
        report = analyze(planted_graph_data, seed=42)

        community_node_sets = [set(c.nodes) for c in report.communities]

        def find_community_for_planted(planted_idx: int) -> int | None:
            prefix = f"c{planted_idx}_"
            for cid, nodes in enumerate(community_node_sets):
                if any(n.startswith(prefix) for n in nodes):
                    return cid
            return None

        planted_to_detected = {}
        for pi in range(4):
            detected = find_community_for_planted(pi)
            if detected is not None:
                planted_to_detected[pi] = detected

        detected_gap_pairs = {(g.community_a, g.community_b) for g in report.gaps}

        expected_detected_gaps = set()
        for pa, pb in planted_graph_expected_gaps:
            da = planted_to_detected.get(pa)
            db = planted_to_detected.get(pb)
            if da is not None and db is not None and da != db:
                expected_detected_gaps.add((min(da, db), max(da, db)))

        if expected_detected_gaps:
            found = sum(
                1
                for eg in expected_detected_gaps
                if eg in detected_gap_pairs or (eg[1], eg[0]) in detected_gap_pairs
            )
            recall = found / len(expected_detected_gaps)
            assert recall >= 0.8, f"Gap recall {recall:.2f} < 0.8"

    def test_no_gaps_in_fully_connected(self) -> None:
        """A fully connected graph should have no gaps."""
        nodes = [f"n{i}" for i in range(10)]
        edges = []
        for i, u in enumerate(nodes):
            for j in range(i + 1, len(nodes)):
                edges.append(
                    {
                        "source": u,
                        "target": nodes[j],
                        "relation": "connected",
                        "weight": 1.0,
                    }
                )
        data = {"nodes": nodes, "edges": edges}
        report = analyze(data, seed=42)
        assert len(report.gaps) == 0


class TestFindBridges:
    def test_bridges_span_communities(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        communities = detect_communities(G, seed=42)
        centrality = compute_centrality(G)
        bridges = find_bridges(G, communities, centrality)

        node_to_community: dict[str, int] = {}
        for c in communities:
            for n in c.nodes:
                node_to_community[n] = c.id

        for name, _ in bridges:
            neighbor_communities = {
                node_to_community[nb]
                for nb in G.neighbors(name)
                if nb in node_to_community
            }
            own = node_to_community.get(name)
            if own is not None:
                neighbor_communities.add(own)
            assert len(neighbor_communities) > 1


class TestComputeCentrality:
    def test_returns_all_nodes(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        centrality = compute_centrality(G)
        assert set(centrality.keys()) == set(G.nodes())

    def test_values_non_negative(self, planted_graph_data: dict) -> None:
        G = build_graph(planted_graph_data)
        centrality = compute_centrality(G)
        for v in centrality.values():
            assert v >= 0.0


class TestAnalyze:
    def test_returns_report(self, planted_graph_data: dict) -> None:
        report = analyze(planted_graph_data, seed=42)
        assert isinstance(report, AnalysisReport)
        assert report.node_count == 48
        assert report.edge_count > 0

    def test_invalid_input_raises(self) -> None:
        with pytest.raises(ValueError, match="Input validation failed"):
            analyze({"nodes": [], "edges": [{"source": "x"}]})

    def test_empty_graph(self, empty_graph_data: dict) -> None:
        report = analyze(empty_graph_data, seed=42)
        assert report.node_count == 0
        assert report.edge_count == 0

    def test_determinism(self, planted_graph_data: dict) -> None:
        """Same input + seed produces identical output."""
        r1 = analyze(planted_graph_data, seed=42)
        r2 = analyze(planted_graph_data, seed=42)
        assert r1 == r2
