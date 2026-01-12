# Preservation Floor

These elements MUST be preserved in ALL compaction modes. Violation triggers failure.

## Always Preserve

1. **Explicit decisions** — Any statement declaring a choice made
2. **Active constraints** — Rules, limits, requirements currently in effect
3. **TODOs / open questions** — Unresolved items requiring future action
4. **Named entities** — Specific people, systems, files, identifiers
5. **Normative language** — Statements using "must", "never", "always", "shall"

## Violation Behavior

If any preservation floor element would be removed or materially altered:

1. The compaction MUST fail
2. The failure reason MUST cite the specific violated element
3. No partial output is produced

## Rationale

The preservation floor exists to prevent silent loss of authority-bearing content. Compaction is a controlled rewrite, not summarization. The floor ensures epistemic safety.
