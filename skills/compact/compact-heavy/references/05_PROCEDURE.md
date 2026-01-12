# Procedure

## Step 1: Validate Target

Confirm target is bounded and readable. Compute source hash.

## Step 2: Identify Decisions

Extract:

- Final decisions (what was chosen)
- Active constraints (what limits action)
- Current intent (what we're trying to do)

## Step 3: Identify Discardable

Find:

- Rationale for decisions already made
- Abandoned alternatives
- Exploration that led nowhere
- Verbose or redundant phrasing

## Step 4: Verify Preservation Floor

Ensure:

- Explicit decisions remain
- Active constraints remain
- Open questions remain
- Normative language remains

## Step 5: Compact

Remove discardable content. Normalize language. Merge equivalent concepts.

## Step 6: Emit Output

```yaml
compaction:
  target: <identifier>
  mode: heavy
  source_hash: <sha256>
  output_hash: <sha256>
```

## Step 7: Replace

Compacted output replaces target as authoritative.
