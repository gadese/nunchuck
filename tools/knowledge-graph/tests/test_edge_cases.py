"""Edge case test suite for P1 hardening."""

import json
from pathlib import Path

import pytest

from kg.core import analyze, build_graph
from kg.cli import main
from kg.render import render_html, render_json, render_text
from kg.validate import validate


class TestEmptyGraph:
    def test_analyze_empty(self) -> None:
        data = {"nodes": [], "edges": []}
        report = analyze(data, seed=42)
        assert report.node_count == 0
        assert report.edge_count == 0
        assert len(report.communities) == 0
        assert len(report.gaps) == 0
        assert len(report.bridges) == 0

    def test_render_text_empty(self) -> None:
        data = {"nodes": [], "edges": []}
        report = analyze(data, seed=42)
        text = render_text(report)
        assert "Nodes: 0" in text
        assert "Edges: 0" in text

    def test_render_json_empty(self) -> None:
        data = {"nodes": [], "edges": []}
        report = analyze(data, seed=42)
        output = json.loads(render_json(report))
        assert output["node_count"] == 0
        assert output["communities"] == []


class TestSingleNode:
    def test_analyze_single(self) -> None:
        data = {"nodes": ["only"], "edges": []}
        report = analyze(data, seed=42)
        assert report.node_count == 1
        assert report.edge_count == 0
        assert len(report.communities) == 1
        assert "only" in report.communities[0].nodes

    def test_render_text_single(self) -> None:
        data = {"nodes": ["only"], "edges": []}
        report = analyze(data, seed=42)
        text = render_text(report)
        assert "only" in text


class TestSingleEdge:
    def test_analyze_single_edge(self) -> None:
        data = {
            "nodes": ["A", "B"],
            "edges": [{"source": "A", "target": "B", "relation": "r", "weight": 1.0}],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 2
        assert report.edge_count == 1


class TestFullyConnected:
    def test_no_gaps(self) -> None:
        nodes = [f"n{i}" for i in range(15)]
        edges = [
            {"source": nodes[i], "target": nodes[j], "relation": "r", "weight": 1.0}
            for i in range(len(nodes))
            for j in range(i + 1, len(nodes))
        ]
        data = {"nodes": nodes, "edges": edges}
        report = analyze(data, seed=42)
        assert len(report.gaps) == 0


class TestFullyDisconnected:
    def test_all_isolated(self) -> None:
        nodes = [f"n{i}" for i in range(10)]
        data = {"nodes": nodes, "edges": []}
        report = analyze(data, seed=42)
        assert report.node_count == 10
        assert report.edge_count == 0
        assert len(report.communities) == 10


class TestDuplicateNodeNames:
    def test_case_variants_are_distinct(self) -> None:
        """Node names differing only by case should be treated as distinct."""
        data = {
            "nodes": ["Alpha", "alpha", "ALPHA"],
            "edges": [
                {"source": "Alpha", "target": "alpha", "relation": "r", "weight": 1.0},
            ],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 3


class TestDuplicateEdges:
    def test_duplicate_edges_collapsed(self) -> None:
        """NetworkX undirected graph collapses duplicate edges."""
        data = {
            "nodes": ["A", "B"],
            "edges": [
                {"source": "A", "target": "B", "relation": "r1", "weight": 1.0},
                {"source": "A", "target": "B", "relation": "r2", "weight": 2.0},
            ],
        }
        G = build_graph(data)
        assert len(G.edges()) == 1


class TestSelfLoops:
    def test_self_loop_handled(self) -> None:
        """Self-loops should not crash analysis."""
        data = {
            "nodes": ["A", "B"],
            "edges": [
                {"source": "A", "target": "A", "relation": "self", "weight": 1.0},
                {"source": "A", "target": "B", "relation": "r", "weight": 1.0},
            ],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 2


class TestZeroWeightEdges:
    def test_zero_weight(self) -> None:
        data = {
            "nodes": ["A", "B"],
            "edges": [
                {"source": "A", "target": "B", "relation": "r", "weight": 0.0},
            ],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 2
        assert report.edge_count == 1


class TestUnicodeAndSpecialCharacters:
    def test_unicode_accents(self) -> None:
        data = {
            "nodes": ["café", "résumé", "naïve"],
            "edges": [
                {
                    "source": "café",
                    "target": "résumé",
                    "relation": "related",
                    "weight": 1.0,
                },
            ],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 3
        text = render_text(report)
        assert "café" in text

    def test_cjk_characters(self) -> None:
        data = {
            "nodes": ["知識", "グラフ", "图谱"],
            "edges": [
                {
                    "source": "知識",
                    "target": "グラフ",
                    "relation": "関連",
                    "weight": 1.0,
                },
            ],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 3

    def test_emoji(self) -> None:
        data = {
            "nodes": ["🧠", "💡", "🔗"],
            "edges": [
                {"source": "🧠", "target": "💡", "relation": "inspires", "weight": 1.0},
            ],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 3

    def test_very_long_concept_names(self) -> None:
        long_a = "A" * 500
        long_b = "B" * 500
        data = {
            "nodes": [long_a, long_b],
            "edges": [
                {"source": long_a, "target": long_b, "relation": "r", "weight": 1.0},
            ],
        }
        report = analyze(data, seed=42)
        assert report.node_count == 2
        text = render_text(report)
        assert long_a in text


class TestValidationEdgeCases:
    def test_not_a_dict(self) -> None:
        errors = validate("not a dict")
        assert any("JSON object" in e for e in errors)

    def test_not_a_dict_list(self) -> None:
        errors = validate([1, 2, 3])
        assert any("JSON object" in e for e in errors)

    def test_missing_nodes(self) -> None:
        errors = validate({"edges": []})
        assert any("nodes" in e for e in errors)

    def test_missing_edges(self) -> None:
        errors = validate({"nodes": []})
        assert any("edges" in e for e in errors)

    def test_nodes_not_list(self) -> None:
        errors = validate({"nodes": "not a list", "edges": []})
        assert any("array" in e for e in errors)

    def test_edges_not_list(self) -> None:
        errors = validate({"nodes": [], "edges": "not a list"})
        assert any("array" in e for e in errors)

    def test_node_not_string(self) -> None:
        errors = validate({"nodes": [1, 2], "edges": []})
        assert len(errors) == 2

    def test_edge_not_dict(self) -> None:
        errors = validate({"nodes": ["a"], "edges": ["not a dict"]})
        assert any("object" in e for e in errors)

    def test_edge_missing_fields(self) -> None:
        errors = validate({"nodes": ["a"], "edges": [{"source": "a"}]})
        assert any("missing required fields" in e for e in errors)

    def test_edge_invalid_source_ref(self) -> None:
        errors = validate(
            {
                "nodes": ["a"],
                "edges": [
                    {"source": "x", "target": "a", "relation": "r", "weight": 1.0}
                ],
            }
        )
        assert any("not found in nodes" in e for e in errors)

    def test_edge_invalid_target_ref(self) -> None:
        errors = validate(
            {
                "nodes": ["a"],
                "edges": [
                    {"source": "a", "target": "x", "relation": "r", "weight": 1.0}
                ],
            }
        )
        assert any("not found in nodes" in e for e in errors)

    def test_nan_weight(self) -> None:
        errors = validate(
            {
                "nodes": ["a", "b"],
                "edges": [
                    {
                        "source": "a",
                        "target": "b",
                        "relation": "r",
                        "weight": float("nan"),
                    }
                ],
            }
        )
        assert any("finite" in e for e in errors)

    def test_inf_weight(self) -> None:
        errors = validate(
            {
                "nodes": ["a", "b"],
                "edges": [
                    {
                        "source": "a",
                        "target": "b",
                        "relation": "r",
                        "weight": float("inf"),
                    }
                ],
            }
        )
        assert any("finite" in e for e in errors)

    def test_negative_weight(self) -> None:
        errors = validate(
            {
                "nodes": ["a", "b"],
                "edges": [
                    {"source": "a", "target": "b", "relation": "r", "weight": -1.0}
                ],
            }
        )
        assert any("non-negative" in e for e in errors)

    def test_weight_not_number(self) -> None:
        errors = validate(
            {
                "nodes": ["a", "b"],
                "edges": [
                    {"source": "a", "target": "b", "relation": "r", "weight": "heavy"}
                ],
            }
        )
        assert any("number" in e for e in errors)

    def test_relation_not_string(self) -> None:
        errors = validate(
            {
                "nodes": ["a", "b"],
                "edges": [
                    {"source": "a", "target": "b", "relation": 123, "weight": 1.0}
                ],
            }
        )
        assert any("string" in e for e in errors)


class TestSecurityHardening:
    def test_html_escape_in_visualization(self, tmp_path: Path) -> None:
        """Concept names with HTML should be escaped in pyvis output."""

        data = {
            "nodes": ["<script>alert('xss')</script>", "normal"],
            "edges": [
                {
                    "source": "<script>alert('xss')</script>",
                    "target": "normal",
                    "relation": "r",
                    "weight": 1.0,
                },
            ],
        }
        report = analyze(data, seed=42)
        G = build_graph(data)
        html_path = str(tmp_path / "test.html")
        render_html(report, G, html_path)
        content = Path(html_path).read_text()
        assert "<script>alert" not in content
        assert "&lt;script&gt;" in content or "\\u003c" in content.lower()

    def test_visualize_path_traversal_rejected(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """--visualize with '..' in path should be rejected."""
        f = tmp_path / "input.json"
        f.write_text(
            '{"nodes": ["a", "b"], "edges": [{"source": "a", "target": "b", "relation": "r", "weight": 1.0}]}'
        )
        exit_code = main(["analyze", str(f), "--visualize", "../../../etc/evil.html"])
        assert exit_code == 2
        captured = capsys.readouterr()
        assert "directory traversal" in captured.err


class TestCLIEdgeCases:
    def test_malformed_json_exit_code(self, tmp_path: Path) -> None:
        bad = tmp_path / "bad.json"
        bad.write_text("{invalid json content")
        with pytest.raises(SystemExit) as exc_info:
            main(["analyze", str(bad)])
        assert exc_info.value.code == 2

    def test_empty_graph_produces_valid_output(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        f = tmp_path / "empty.json"
        f.write_text('{"nodes": [], "edges": []}')
        exit_code = main(["analyze", str(f)])
        assert exit_code == 0
        captured = capsys.readouterr()
        assert "Nodes: 0" in captured.out

    def test_single_node_produces_valid_output(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        f = tmp_path / "single.json"
        f.write_text('{"nodes": ["x"], "edges": []}')
        exit_code = main(["analyze", str(f)])
        assert exit_code == 0
        captured = capsys.readouterr()
        assert "Nodes: 1" in captured.out
