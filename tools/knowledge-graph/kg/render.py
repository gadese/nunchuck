"""Output rendering: text, JSON, and HTML (pyvis)."""

import html
import json
from typing import Any

import networkx as nx

from kg.models import AnalysisReport, Community, Gap

MAX_BRIDGES_DISPLAYED = 10
BRIDGE_NODE_SIZE = 20
DEFAULT_NODE_SIZE = 10


def render_text(report: AnalysisReport) -> str:
    lines: list[str] = []

    lines.append("=" * 60)
    lines.append("KNOWLEDGE GRAPH ANALYSIS REPORT")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Nodes: {report.node_count}")
    lines.append(f"Edges: {report.edge_count}")
    lines.append(f"Communities: {len(report.communities)}")
    lines.append(f"Modularity: {report.modularity:.4f}")
    lines.append("")

    lines.append("-" * 60)
    lines.append("COMMUNITIES")
    lines.append("-" * 60)
    for c in report.communities:
        lines.append(f"\n  Community {c.id} ({len(c.nodes)} nodes)")
        if c.top_nodes:
            lines.append("  Top nodes (by centrality):")
            for name, score in c.top_nodes:
                lines.append(f"    - {name} ({score:.4f})")
        lines.append(f"  All nodes: {', '.join(sorted(c.nodes))}")

    if report.gaps:
        lines.append("")
        lines.append("-" * 60)
        lines.append("GAPS (low inter-community connectivity)")
        lines.append("-" * 60)
        for g in report.gaps:
            lines.append(
                f"\n  Community {g.community_a} <-> Community {g.community_b}"
                f"  (density: {g.density:.4f})"
            )
            lines.append(
                f"    Community {g.community_a} concepts: {', '.join(g.top_concepts_a)}"
            )
            lines.append(
                f"    Community {g.community_b} concepts: {', '.join(g.top_concepts_b)}"
            )
    else:
        lines.append("")
        lines.append("No gaps detected.")

    if report.bridges:
        lines.append("")
        lines.append("-" * 60)
        lines.append("BRIDGE CONCEPTS (span multiple communities)")
        lines.append("-" * 60)
        for name, score in report.bridges[:MAX_BRIDGES_DISPLAYED]:
            lines.append(f"  - {name} (centrality: {score:.4f})")
    else:
        lines.append("")
        lines.append("No bridge concepts detected.")

    lines.append("")
    lines.append("=" * 60)
    return "\n".join(lines)


def _community_to_dict(c: Community) -> dict[str, Any]:
    return {
        "id": c.id,
        "nodes": sorted(c.nodes),
        "top_nodes": [{"name": n, "centrality": s} for n, s in c.top_nodes],
        "size": len(c.nodes),
    }


def _gap_to_dict(g: Gap) -> dict[str, Any]:
    return {
        "community_a": g.community_a,
        "community_b": g.community_b,
        "density": g.density,
        "top_concepts_a": list(g.top_concepts_a),
        "top_concepts_b": list(g.top_concepts_b),
    }


def render_json(report: AnalysisReport) -> str:
    obj = {
        "node_count": report.node_count,
        "edge_count": report.edge_count,
        "modularity": report.modularity,
        "communities": [_community_to_dict(c) for c in report.communities],
        "gaps": [_gap_to_dict(g) for g in report.gaps],
        "bridges": [{"name": n, "centrality": s} for n, s in report.bridges],
    }
    return json.dumps(obj, indent=2, sort_keys=False)


def render_html(
    report: AnalysisReport,
    G: nx.Graph,
    output_path: str,
) -> None:
    """Generate an interactive pyvis HTML visualization with community-colored nodes."""
    from pyvis.network import Network

    colors = [
        "#e6194b",
        "#3cb44b",
        "#ffe119",
        "#4363d8",
        "#f58231",
        "#911eb4",
        "#42d4f4",
        "#f032e6",
        "#bfef45",
        "#fabed4",
        "#469990",
        "#dcbeff",
        "#9A6324",
        "#fffac8",
        "#800000",
        "#aaffc3",
        "#808000",
        "#ffd8b1",
        "#000075",
        "#a9a9a9",
    ]

    node_to_community: dict[str, int] = {}
    for c in report.communities:
        for n in c.nodes:
            node_to_community[n] = c.id

    bridge_set = {name for name, _ in report.bridges}

    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    net.barnes_hut()

    for node in G.nodes():
        cid = node_to_community.get(node, 0)
        color = colors[cid % len(colors)]
        size = BRIDGE_NODE_SIZE if node in bridge_set else DEFAULT_NODE_SIZE
        label = html.escape(node)
        title = html.escape(f"{node} (Community {cid})")
        net.add_node(node, label=label, title=title, color=color, size=size)

    for u, v, data in G.edges(data=True):
        relation = html.escape(str(data.get("relation", "")))
        weight = data.get("weight", 1.0)
        net.add_edge(u, v, title=relation, value=weight)

    net.save_graph(output_path)
