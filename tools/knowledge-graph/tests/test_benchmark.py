"""Benchmark harness: latency and peak memory at various graph scales."""

import time
import tracemalloc

import pytest

from kg.core import analyze
from tests.conftest import make_planted_graph


SCALES = [20, 100, 200, 300, 500]

LATENCY_TARGETS = {
    200: 1.0,
    500: 2.0,
}

MEMORY_TARGET_MB = 200


def _make_graph_at_scale(n_nodes: int, seed: int = 42) -> dict:
    """Create a planted graph with approximately n_nodes total nodes."""
    n_communities = max(2, n_nodes // 12)
    nodes_per_community = max(3, n_nodes // n_communities)
    inter_pairs = [(i, i + 1) for i in range(0, n_communities - 1, 2)]
    return make_planted_graph(
        n_communities=n_communities,
        nodes_per_community=nodes_per_community,
        intra_density=0.3,
        inter_pairs=inter_pairs,
        inter_density=0.03,
        seed=seed,
    )


class TestLatency:
    """Analysis latency at various scales."""

    @pytest.mark.parametrize("n_nodes", SCALES)
    def test_analysis_latency(self, n_nodes: int) -> None:
        data = _make_graph_at_scale(n_nodes)
        actual_nodes = len(data["nodes"])

        start = time.perf_counter()
        analyze(data, seed=42)
        elapsed = time.perf_counter() - start

        target = LATENCY_TARGETS.get(n_nodes)
        if target is not None:
            assert elapsed < target, (
                f"Latency {elapsed:.3f}s exceeds target {target}s "
                f"for {actual_nodes}-node graph"
            )

    def test_200_node_under_1s(self) -> None:
        data = _make_graph_at_scale(200)
        start = time.perf_counter()
        analyze(data, seed=42)
        elapsed = time.perf_counter() - start
        assert elapsed < 1.0, f"200-node analysis took {elapsed:.3f}s (target: <1s)"

    def test_500_node_under_2s(self) -> None:
        data = _make_graph_at_scale(500)
        start = time.perf_counter()
        analyze(data, seed=42)
        elapsed = time.perf_counter() - start
        assert elapsed < 2.0, f"500-node analysis took {elapsed:.3f}s (target: <2s)"


class TestMemory:
    """Peak memory usage at 500-node scale."""

    def test_memory_under_200mb(self) -> None:
        data = _make_graph_at_scale(500)

        tracemalloc.start()
        analyze(data, seed=42)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak / (1024 * 1024)
        assert peak_mb < MEMORY_TARGET_MB, (
            f"Peak memory {peak_mb:.1f}MB exceeds target {MEMORY_TARGET_MB}MB"
        )


class TestBenchmarkReport:
    """Generate a summary report of all benchmarks (informational, always passes)."""

    def test_print_benchmark_report(self, capsys: pytest.CaptureFixture[str]) -> None:
        results: list[dict] = []

        for n_nodes in SCALES:
            data = _make_graph_at_scale(n_nodes)
            actual_nodes = len(data["nodes"])
            actual_edges = len(data["edges"])

            tracemalloc.start()
            start = time.perf_counter()
            report = analyze(data, seed=42)
            elapsed = time.perf_counter() - start
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            target = LATENCY_TARGETS.get(n_nodes, None)
            results.append(
                {
                    "target_nodes": n_nodes,
                    "actual_nodes": actual_nodes,
                    "actual_edges": actual_edges,
                    "latency_s": elapsed,
                    "latency_target_s": target,
                    "peak_mb": peak / (1024 * 1024),
                    "communities": len(report.communities),
                    "modularity": report.modularity,
                    "gaps": len(report.gaps),
                    "bridges": len(report.bridges),
                }
            )

        print("\n" + "=" * 80)
        print("BENCHMARK REPORT")
        print("=" * 80)
        print(
            f"{'Scale':>8} {'Nodes':>7} {'Edges':>7} {'Latency':>10} "
            f"{'Target':>10} {'Memory':>10} {'Comm':>6} {'Mod':>8} "
            f"{'Gaps':>6} {'Bridges':>8}"
        )
        print("-" * 80)
        for r in results:
            target_str = (
                f"<{r['latency_target_s']}s" if r["latency_target_s"] else "N/A"
            )
            print(
                f"{r['target_nodes']:>8} {r['actual_nodes']:>7} "
                f"{r['actual_edges']:>7} {r['latency_s']:>9.3f}s "
                f"{target_str:>10} {r['peak_mb']:>9.1f}MB "
                f"{r['communities']:>6} {r['modularity']:>8.4f} "
                f"{r['gaps']:>6} {r['bridges']:>8}"
            )
        print("=" * 80)
