# Procedure

## Step 1: Validate Target

Confirm target is bounded and readable. Compute source hash.

## Step 2: Analyze Content

Classify content segments:

- Exploratory (rationale, alternatives, discussion)
- Decisional (final choices, constraints, intent)
- Operational (facts, entities, actions)

## Step 3: Select Strategy

Based on analysis:

- Mostly exploratory → effective_mode: light
- Mostly decisional → effective_mode: heavy
- Mixed → effective_mode: mixed

Set confidence based on clarity of classification.

## Step 4: Apply Constraints

Check `auto_constraints` if provided:

- Respect `max_loss` setting
- Honor `prefer` priorities
- Enforce `forbid` restrictions

## Step 5: Verify Preservation Floor

Before any removal, confirm:

- Decisions remain
- Constraints remain
- Open questions remain
- Named entities remain
- Normative language remains

If any would be violated → **fail**.

## Step 6: Compact

Apply selected strategy. Document justification for each removal or merge.

## Step 7: Emit Output

```yaml
compaction:
  target: <identifier>
  mode: auto
  source_hash: <sha256>
  output_hash: <sha256>

auto_decision:
  effective_mode: light | heavy | mixed
  confidence: low | medium | high
  justification: <string>
```

## Step 8: Replace

Compacted output replaces target as authoritative.
