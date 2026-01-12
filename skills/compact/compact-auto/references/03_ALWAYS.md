# Always

## Must Preserve (Floor)

- Explicit decisions
- Active constraints
- TODOs / open questions
- Named entities
- Normative language

## Strategy Selection

Analyze content to determine effective mode:

- If content is exploratory → lean light
- If content is decision-heavy → lean heavy
- If mixed → use mixed mode (light for some, heavy for others)

## Output Requirements

Always emit auto_decision metadata:

```yaml
auto_decision:
  effective_mode: light | heavy | mixed
  confidence: low | medium | high
  justification: <why this mode was selected>
```

## Default Behavior

If uncertain about strategy → use light behavior.

If uncertain about removal → preserve.
