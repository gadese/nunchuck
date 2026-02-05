"""Input JSON schema validation with descriptive errors."""

import math


def validate(data: object) -> list[str]:
    """Validate input data against the expected schema.

    Returns a list of error strings. Empty list means valid.
    """
    errors: list[str] = []

    if not isinstance(data, dict):
        errors.append("Input must be a JSON object")
        return errors

    if "nodes" not in data:
        errors.append("Missing required key: 'nodes'")
    if "edges" not in data:
        errors.append("Missing required key: 'edges'")

    if errors:
        return errors

    nodes = data["nodes"]
    edges = data["edges"]

    if not isinstance(nodes, list):
        errors.append("'nodes' must be an array")
        return errors

    for i, node in enumerate(nodes):
        if not isinstance(node, str):
            errors.append(f"nodes[{i}]: expected string, got {type(node).__name__}")

    if not isinstance(edges, list):
        errors.append("'edges' must be an array")
        return errors

    node_set = set(nodes)

    required_edge_fields = {"source", "target", "relation", "weight"}

    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"edges[{i}]: expected object, got {type(edge).__name__}")
            continue

        missing = required_edge_fields - set(edge.keys())
        if missing:
            errors.append(f"edges[{i}]: missing required fields: {sorted(missing)}")
            continue

        source = edge["source"]
        target = edge["target"]
        relation = edge["relation"]
        weight = edge["weight"]

        if not isinstance(source, str):
            errors.append(
                f"edges[{i}].source: expected string, got {type(source).__name__}"
            )
        elif source not in node_set:
            errors.append(f"edges[{i}].source: '{source}' not found in nodes")

        if not isinstance(target, str):
            errors.append(
                f"edges[{i}].target: expected string, got {type(target).__name__}"
            )
        elif target not in node_set:
            errors.append(f"edges[{i}].target: '{target}' not found in nodes")

        if not isinstance(relation, str):
            errors.append(
                f"edges[{i}].relation: expected string, got {type(relation).__name__}"
            )

        if not isinstance(weight, (int, float)):
            errors.append(
                f"edges[{i}].weight: expected number, got {type(weight).__name__}"
            )
        else:
            if math.isnan(weight) or math.isinf(weight):
                errors.append(f"edges[{i}].weight: must be finite, got {weight}")
            elif weight < 0:
                errors.append(f"edges[{i}].weight: must be non-negative, got {weight}")

    return errors
