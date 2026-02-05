"""Gap detection precision/recall measurement on synthetic graphs."""

import pytest

from kg.core import analyze
from tests.conftest import make_planted_graph


def _measure_gap_precision_recall(
    n_communities: int,
    nodes_per_community: int,
    inter_pairs: list[tuple[int, int]],
    intra_density: float = 0.4,
    inter_density: float = 0.05,
    seed: int = 42,
) -> tuple[float, float]:
    """Measure gap detection precision and recall on a planted graph.

    Returns:
        (precision, recall) tuple.
    """
    data = make_planted_graph(
        n_communities=n_communities,
        nodes_per_community=nodes_per_community,
        intra_density=intra_density,
        inter_pairs=inter_pairs,
        inter_density=inter_density,
        seed=seed,
    )
    report = analyze(data, seed=seed)

    # Map planted community indices to detected community IDs
    community_node_sets = [set(c.nodes) for c in report.communities]

    def find_detected_community(planted_idx: int) -> int | None:
        prefix = f"c{planted_idx}_"
        for cid, nodes in enumerate(community_node_sets):
            if any(n.startswith(prefix) for n in nodes):
                return cid
        return None

    planted_to_detected: dict[int, int] = {}
    for pi in range(n_communities):
        detected = find_detected_community(pi)
        if detected is not None:
            planted_to_detected[pi] = detected

    # Compute expected gaps (planted pairs with NO inter-community edges)
    all_pairs = {
        (i, j) for i in range(n_communities) for j in range(i + 1, n_communities)
    }
    connected_pairs = set(inter_pairs)
    expected_gap_pairs = all_pairs - connected_pairs

    # Map expected gaps to detected community IDs
    expected_detected_gaps: set[tuple[int, int]] = set()
    for pa, pb in expected_gap_pairs:
        da = planted_to_detected.get(pa)
        db = planted_to_detected.get(pb)
        if da is not None and db is not None and da != db:
            expected_detected_gaps.add((min(da, db), max(da, db)))

    # Detected gaps
    detected_gap_pairs = set()
    for g in report.gaps:
        detected_gap_pairs.add(
            (min(g.community_a, g.community_b), max(g.community_a, g.community_b))
        )

    if not expected_detected_gaps:
        return (1.0, 1.0)

    # Recall: fraction of expected gaps that were detected
    found = sum(1 for eg in expected_detected_gaps if eg in detected_gap_pairs)
    recall = found / len(expected_detected_gaps) if expected_detected_gaps else 1.0

    # Precision: fraction of detected gaps that were expected
    # Note: some detected gaps may be between sub-communities of the same planted community
    # We count a detected gap as a true positive if it matches an expected gap
    true_positives = sum(1 for dg in detected_gap_pairs if dg in expected_detected_gaps)
    precision = true_positives / len(detected_gap_pairs) if detected_gap_pairs else 1.0

    return (precision, recall)


class TestGapPrecisionRecall:
    """Gap detection precision and recall on various synthetic graphs."""

    def test_default_graph_recall(self) -> None:
        """4 communities, 2 connected pairs -> 4 gap pairs."""
        _, recall = _measure_gap_precision_recall(
            n_communities=4,
            nodes_per_community=12,
            inter_pairs=[(0, 1), (2, 3)],
        )
        assert recall >= 0.8, f"Gap recall {recall:.2f} < 0.8"

    def test_default_graph_precision(self) -> None:
        """4 communities, 2 connected pairs -> 4 gap pairs."""
        precision, _ = _measure_gap_precision_recall(
            n_communities=4,
            nodes_per_community=12,
            inter_pairs=[(0, 1), (2, 3)],
        )
        assert precision >= 0.8, f"Gap precision {precision:.2f} < 0.8"

    def test_6_community_graph_recall(self) -> None:
        """6 communities, 3 connected pairs -> 12 gap pairs."""
        _, recall = _measure_gap_precision_recall(
            n_communities=6,
            nodes_per_community=10,
            inter_pairs=[(0, 1), (2, 3), (4, 5)],
            seed=42,
        )
        assert recall >= 0.8, f"Gap recall {recall:.2f} < 0.8"

    def test_6_community_graph_precision(self) -> None:
        """6 communities, 3 connected pairs -> 12 gap pairs."""
        precision, _ = _measure_gap_precision_recall(
            n_communities=6,
            nodes_per_community=10,
            inter_pairs=[(0, 1), (2, 3), (4, 5)],
            seed=42,
        )
        assert precision >= 0.8, f"Gap precision {precision:.2f} < 0.8"

    def test_print_precision_recall_report(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Print a summary report of precision/recall across configurations."""
        configs = [
            {
                "n_communities": 4,
                "nodes_per_community": 12,
                "inter_pairs": [(0, 1), (2, 3)],
            },
            {
                "n_communities": 4,
                "nodes_per_community": 20,
                "inter_pairs": [(0, 1), (2, 3)],
            },
            {
                "n_communities": 6,
                "nodes_per_community": 10,
                "inter_pairs": [(0, 1), (2, 3), (4, 5)],
            },
            {
                "n_communities": 6,
                "nodes_per_community": 15,
                "inter_pairs": [(0, 1), (2, 3), (4, 5)],
            },
        ]

        print("\n" + "=" * 60)
        print("GAP DETECTION PRECISION/RECALL REPORT")
        print("=" * 60)
        print(f"{'Config':>30} {'Precision':>12} {'Recall':>12}")
        print("-" * 60)

        for cfg in configs:
            precision, recall = _measure_gap_precision_recall(**cfg)
            label = f"{cfg['n_communities']}c x {cfg['nodes_per_community']}n"
            print(f"{label:>30} {precision:>11.2%} {recall:>11.2%}")

        print("=" * 60)
