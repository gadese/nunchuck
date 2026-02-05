# Knowledge Graph Analysis Tool

A local CLI tool for analyzing concept graphs extracted during brainstorming sessions. Detects topical clusters, structural gaps, bridge concepts, and produces analysis reports and interactive visualizations.

## Prerequisites

- Python 3.10+
- macOS or Linux

## Installation

```bash
# From the tools/knowledge-graph/ directory:
bash run.sh analyze examples/input.json
```

The `run.sh` script automatically creates a virtual environment and installs dependencies on first run. No manual setup required.

**Manual setup** (if preferred):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m kg analyze examples/input.json
```

## Commands

### analyze

Run the full analysis pipeline on a knowledge graph.

```bash
python -m kg analyze <input.json> [options]
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--format text\|json` | `text` | Output format |
| `--visualize <path.html>` | — | Generate interactive HTML visualization |
| `--seed <int>` | `42` | Random seed for reproducibility |
| `--resolution <float>` | `1.0` | Louvain resolution parameter (higher = more communities) |
| `--gap-threshold <float>` | `0.05` | Gap detection threshold (density below this = gap) |

**Examples:**
```bash
# Text report to stdout
python -m kg analyze graph.json

# JSON report (pipe to jq, other tools)
python -m kg analyze graph.json --format json

# With interactive HTML visualization
python -m kg analyze graph.json --visualize output.html

# Custom parameters
python -m kg analyze graph.json --seed 123 --resolution 1.5 --gap-threshold 0.1

# Via run.sh (auto-creates venv)
bash run.sh analyze graph.json --format json --visualize output.html
```

### validate

Validate input JSON without running analysis. Useful as a pre-flight check.

```bash
python -m kg validate <input.json>
```

## Input Format

```json
{
  "nodes": ["concept_a", "concept_b", "concept_c"],
  "edges": [
    {
      "source": "concept_a",
      "target": "concept_b",
      "relation": "related_to",
      "weight": 0.8
    }
  ]
}
```

**Field requirements:**

| Field | Type | Constraints |
|-------|------|-------------|
| `nodes` | `string[]` | Required. Array of concept name strings. |
| `edges` | `object[]` | Required. Array of relationship objects. |
| `edges[].source` | `string` | Must reference an existing node. |
| `edges[].target` | `string` | Must reference an existing node. |
| `edges[].relation` | `string` | Describes the relationship type. |
| `edges[].weight` | `number` | Non-negative, finite (no NaN/Infinity). |

Node names support Unicode (accents, CJK, emoji). Names are case-sensitive (`"Alpha"` and `"alpha"` are distinct nodes).

## Output Format

### Text Report

Human-readable report to stdout containing:
- **Graph statistics** — node count, edge count, community count, modularity score
- **Communities** — each community with member nodes and top-5 nodes ranked by betweenness centrality
- **Gaps** — community pairs with low inter-connectivity (density below threshold), with top concepts from each side
- **Bridge concepts** — top-10 nodes with highest betweenness centrality that span multiple communities

### JSON Report (`--format json`)

Machine-readable format with identical information, suitable for piping to `jq` or other tools:

```json
{
  "node_count": 22,
  "edge_count": 23,
  "modularity": 0.5831,
  "communities": [
    {"id": 0, "nodes": ["..."], "top_nodes": [{"name": "...", "centrality": 0.42}], "size": 6}
  ],
  "gaps": [
    {"community_a": 0, "community_b": 1, "density": 0.0, "top_concepts_a": ["..."], "top_concepts_b": ["..."]}
  ],
  "bridges": [
    {"name": "deep learning", "centrality": 0.6}
  ]
}
```

### HTML Visualization (`--visualize`)

Interactive graph powered by pyvis with:
- **Community-colored nodes** — each community gets a distinct color
- **Bridge nodes highlighted** — larger size for nodes spanning multiple communities
- **Edge labels** — hover to see relationship type
- **Pan, zoom, and click** — full interactive exploration
- **HTML-escaped labels** — safe against XSS in concept names

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Runtime error (analysis failure) |
| `2` | Usage/validation error (bad input, missing file, malformed JSON) |

## Claude Prompt Template

Use this prompt to have Claude extract a concept graph from a brainstorming session:

> I need you to extract a knowledge graph from the following brainstorming content. Produce a JSON object with exactly this structure:
>
> ```json
> {
>   "nodes": ["concept1", "concept2", ...],
>   "edges": [
>     {"source": "concept1", "target": "concept2", "relation": "relationship_type", "weight": 0.8},
>     ...
>   ]
> }
> ```
>
> **Rules:**
> - Each node is a short concept name (1-4 words, lowercase preferred)
> - Each edge connects two existing nodes with a descriptive relation type
> - Weight is 0.0-1.0 indicating relationship strength (0.5 = moderate, 0.8 = strong, 1.0 = definitional)
> - Include cross-domain connections where they exist
> - Aim for 15-50 nodes and 20-80 edges for a useful analysis
> - Output ONLY the JSON, no commentary
>
> Here is the brainstorming content:
> [paste content here]

After Claude produces the JSON, save it to a file and run:

```bash
bash run.sh validate graph.json   # Check for errors
bash run.sh analyze graph.json    # Full analysis
```

## Iterative Workflow

This tool is designed for an iterative brainstorming loop where Claude maintains the concept graph and the tool provides structural analysis.

### The Cycle

```
Claude builds JSON ──> Tool analyzes ──> Claude reads report ──> Claude refines JSON ──> repeat
```

### Concrete Example

**Round 1: Initial extraction**

1. Give Claude your brainstorming notes + the prompt template above
2. Claude produces `graph.json` with 22 nodes and 23 edges
3. Run: `bash run.sh analyze graph.json --visualize round1.html`
4. Report shows 4 communities, 6 gaps, modularity 0.58

**Round 2: Address gaps**

5. Share the report with Claude:
   > "The analysis found a gap between Community 0 (reinforcement learning cluster) and Community 1 (NLP cluster). Are there bridging concepts we're missing?"
6. Claude suggests adding: `"reward modeling"` (connects RL to language models), `"RLHF"` (bridges RL and NLP)
7. Claude updates the JSON with new nodes and edges
8. Run: `bash run.sh analyze graph.json --visualize round2.html`
9. Gap density between those communities increases; new bridges appear

**Round 3: Deepen clusters**

10. Share the updated report:
    > "Community 3 (computer vision) only has 5 nodes. What sub-topics are we missing?"
11. Claude adds: `"semantic segmentation"`, `"image generation"`, `"GANs"`, `"diffusion models"`
12. Re-analyze. Community 3 grows, new internal structure emerges.

**When to stop:** When the modularity stabilizes and gaps align with genuinely separate domains rather than missing connections.

## Examples

Pre-built examples in the `examples/` directory:

| File | Description |
|------|-------------|
| `examples/input.json` | Sample ML/AI concept graph (22 nodes, 23 edges) |
| `examples/output.txt` | Text report from analyzing `input.json` |
| `examples/graph.html` | Interactive HTML visualization |

Run the example:
```bash
bash run.sh analyze examples/input.json --visualize examples/graph.html
```

## Architecture

### Design Decisions

**Stateless pipeline** — The tool is a pure function: input JSON in, analysis report out. No internal state, no persistence, no save/load. Claude maintains the evolving JSON between iterations. This eliminates state corruption, merge conflicts, and atomic write bugs.

**Approach D (Claude-Only with Iterative Refinement)** — Claude handles all semantic reasoning (what concepts mean, which gaps matter, what to add). The tool handles structural analysis (community detection, centrality, gap measurement). This separation keeps the tool simple (~400 lines) with zero ML model dependencies.

**Key trade-offs:**
- No incremental graph building — Claude must produce the full JSON each invocation. Acceptable because Claude trivially merges concept lists, and eliminating state management removes an entire category of bugs.
- Purely topological gap detection — no semantic filtering. Traded for zero model dependencies and sub-second latency. See upgrade path below.

### Module Structure

```
kg/
├── __main__.py   # Entry point: python -m kg
├── cli.py        # Argument parsing, dispatch, exit codes
├── core.py       # Graph construction, Louvain, centrality, gap analysis
├── models.py     # Frozen dataclasses: Community, Gap, AnalysisReport
├── render.py     # Text renderer, JSON renderer, pyvis HTML
└── validate.py   # Input JSON schema validation
```

**Dependency graph:** `cli → core → models`, `cli → render → models`, `cli → validate`. No circular imports.

### Algorithms

| Algorithm | Complexity | Implementation |
|-----------|-----------|----------------|
| Graph construction | O(V + E) | `core.build_graph()` |
| Community detection (Louvain) | O(V·log²V) | `core.detect_communities()` |
| Betweenness centrality (approximate) | O(k·E), k=min(100,V) | `core.compute_centrality()` |
| Gap detection | O(C²·V²) worst case | `core.detect_gaps()` |
| Bridge identification | O(V·deg) | `core.find_bridges()` |

### Performance

| Scale | Nodes | Edges | Latency | Memory |
|-------|-------|-------|---------|--------|
| 20 | 20 | 33 | 0.010s | 0.1MB |
| 100 | 96 | 176 | 0.047s | 0.2MB |
| 200 | 192 | 330 | 0.084s | 0.4MB |
| 300 | 300 | 516 | 0.143s | 0.6MB |
| 500 | 492 | 888 | 0.201s | 1.0MB |

## Upgrade Path: Semantic Gap Detection

The current tool uses purely topological gap detection (inter-community edge density). A future upgrade can add semantic filtering using sentence-transformers:

**What to add:**
1. `kg/semantic.py` — New module computing community centroid embeddings via `sentence-transformers`
2. `--semantic` flag in `cli.py` — Enables semantic gap filtering
3. `sentence-transformers` in `requirements.txt` as optional dependency

**How it works:**
- For each community, compute the centroid embedding (mean of node name embeddings)
- For each detected gap, compute cosine similarity between community centroids
- Filter out gaps where communities are semantically distant (genuinely unrelated domains)
- Keep gaps where communities are semantically close but structurally disconnected (missing connections)

**Impact:** Reduces false positive gaps (e.g., "reinforcement learning" ↔ "computer vision" may be flagged as a gap but they're genuinely separate domains). Adds ~500MB model download and ~2s latency per analysis.

**No restructuring required** — the `analyze()` function returns an `AnalysisReport` with a `gaps` tuple. The semantic filter is a post-processing step that filters this tuple before rendering.

## Development

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run all tests (85 tests)
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_core.py

# Run benchmarks with output
pytest tests/test_benchmark.py -v -s

# Run precision/recall report
pytest tests/test_precision_recall.py -v -s
```

### Test Files

| File | Tests | Description |
|------|-------|-------------|
| `test_core.py` | 14 | Analysis logic: communities, gaps, bridges, centrality |
| `test_cli.py` | 11 | End-to-end CLI: exit codes, output format, error messages |
| `test_edge_cases.py` | 35 | Edge cases: empty/single/unicode/self-loops/validation/security |
| `test_determinism.py` | 5 | 10-run byte-identical output verification |
| `test_benchmark.py` | 8 | Latency and memory benchmarks at 5 scales |
| `test_precision_recall.py` | 5 | Gap detection precision/recall on synthetic graphs |
