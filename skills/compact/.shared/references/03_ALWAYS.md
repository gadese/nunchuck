# Always

Non-negotiable invariants for all compact-* skills.

## Preservation Floor

Always preserve (violation triggers failure):

- **Explicit decisions** — Any statement declaring a choice made
- **Active constraints** — Rules, limits, requirements in effect
- **TODOs / open questions** — Unresolved items
- **Named entities** — Specific people, systems, files, identifiers
- **Normative language** — "must", "never", "always", "shall"

## Target Rules

- Always require bounded, explicit targets
- Always validate target exists and is readable
- Always compute source hash before compaction

## Output Rules

- Always produce compaction metadata
- Always compute output hash after compaction
- Always emit schema-conformant output
- Always replace target as authoritative on success

## Authority Rules

- Always enforce the mode encoded in the skill identity
- Always refuse mode override attempts
- Always maintain cross-skill compatibility
