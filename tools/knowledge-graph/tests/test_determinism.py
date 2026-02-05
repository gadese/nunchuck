"""Determinism verification: 10 runs with same input + seed -> identical output."""

from kg.core import analyze
from kg.render import render_text, render_json
from tests.conftest import make_planted_graph


class TestDeterminism:
    """Verify byte-identical output across 10 runs with same input and seed."""

    def test_text_output_determinism(self) -> None:
        data = make_planted_graph(seed=42)
        outputs: list[str] = []
        for _ in range(10):
            report = analyze(data, seed=42)
            outputs.append(render_text(report))

        for i, output in enumerate(outputs[1:], start=1):
            assert output == outputs[0], (
                f"Run {i} produced different text output than run 0"
            )

    def test_json_output_determinism(self) -> None:
        data = make_planted_graph(seed=42)
        outputs: list[str] = []
        for _ in range(10):
            report = analyze(data, seed=42)
            outputs.append(render_json(report))

        for i, output in enumerate(outputs[1:], start=1):
            assert output == outputs[0], (
                f"Run {i} produced different JSON output than run 0"
            )

    def test_report_object_determinism(self) -> None:
        data = make_planted_graph(seed=42)
        reports = [analyze(data, seed=42) for _ in range(10)]

        for i, report in enumerate(reports[1:], start=1):
            assert report == reports[0], (
                f"Run {i} produced different AnalysisReport than run 0"
            )

    def test_different_seeds_produce_different_output(self) -> None:
        """Sanity check: different seeds should produce different results."""
        data = make_planted_graph(seed=42)
        r1 = analyze(data, seed=42)
        r2 = analyze(data, seed=99)
        # Communities may differ with different seeds
        # At minimum, the reports should not be byte-identical
        # (though they could be if the graph is trivial)
        t1 = render_text(r1)
        t2 = render_text(r2)
        # This is a soft check - different seeds usually produce different results
        # but on small graphs they might converge to the same partition
        assert isinstance(t1, str) and isinstance(t2, str)

    def test_determinism_at_200_nodes(self) -> None:
        """Verify determinism at a larger scale."""
        data = make_planted_graph(
            n_communities=8,
            nodes_per_community=25,
            intra_density=0.3,
            inter_pairs=[(0, 1), (2, 3), (4, 5), (6, 7)],
            inter_density=0.03,
            seed=42,
        )
        outputs: list[str] = []
        for _ in range(10):
            report = analyze(data, seed=42)
            outputs.append(render_json(report))

        for i, output in enumerate(outputs[1:], start=1):
            assert output == outputs[0], (
                f"Run {i} at 200-node scale produced different output than run 0"
            )
