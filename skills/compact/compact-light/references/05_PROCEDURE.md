# Procedure

## Step 1: Validate Target

Confirm target is bounded and readable. Compute source hash.

## Step 2: Identify Redundancy

Find:

- Exact duplicate statements
- Repeated phrasing
- Filler content

## Step 3: Preserve Core

Ensure all preservation floor elements remain intact:

- Decisions
- Rationale
- Constraints
- Open questions
- Named entities
- Normative language

## Step 4: Compact

Remove identified redundancy. Do not merge concepts or normalize language.

## Step 5: Emit Output

Produce compacted content with metadata:

```yaml
compaction:
  target: <identifier>
  mode: light
  source_hash: <sha256>
  output_hash: <sha256>
```

## Step 6: Replace

Compacted output replaces target as authoritative.
