# Procedure

Input/output requirements for compact-* skills.

## Required Input

```yaml
target:
  type: file | block | artifact | message_range
  identifier: <string>

preserve:
  - decisions
  - constraints
  - named_entities

discard:
  - exploration
  - repetition

schema: <SCHEMA_ID>
```

## Validation Rules

- Target must be bounded and unambiguous
- Missing target → reject
- Conflicting preserve/discard → reject
- Schema must be provided or inferrable

## Auto Mode Additional Input

```yaml
auto_constraints:
  max_loss: low | medium | high
  prefer:
    - recoverability
    - authority
  forbid:
    - rationale_removal
```

Defaults apply safely if omitted.

## Required Output

```yaml
content: <compacted_content>

compaction:
  target: <identifier>
  mode: light | heavy | auto
  source_hash: <sha256>
  output_hash: <sha256>
  timestamp: <iso8601>
```

## Auto Mode Additional Output

```yaml
auto_decision:
  effective_mode: light | heavy | mixed
  confidence: low | medium | high
  justification: <string>
```

## Replacement Semantics

The compacted artifact **replaces the original target as authoritative**. The original is superseded, not augmented.
