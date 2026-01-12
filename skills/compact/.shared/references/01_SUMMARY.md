# Summary

The **compact** skillset performs explicit, target-aware context compaction with declared loss boundaries and epistemic guard rails.

> Compaction is a controlled rewrite, not summarization.

## Purpose

- Reduce context **intentionally**
- Preserve declared invariants
- Prevent silent drift, loss, or accidental reinterpretation
- Produce authoritative replacement artifacts

## Mental Model

| Mode | Metaphor | Optimization Bias |
|------|----------|-------------------|
| **Light** | Checkpoint | Recoverability > brevity |
| **Heavy** | Doctrine | Authority > recoverability |
| **Auto** | Trusted editor with rules | Preservation on uncertainty |

## Key Invariant

**Invocation selects authority. Execution enforces it.**

Each member skill (`compact-light`, `compact-heavy`, `compact-auto`) encodes a fixed epistemic authority level. There is no runtime mode parameter.

## Scope

### This skillset DOES

- Compact explicitly bounded targets
- Produce replacement artifacts
- Enforce preservation and discard rules
- Emit inspectable metadata

### This skillset DOES NOT

- Choose targets automatically
- Perform implicit summarization
- Manage memory globally
- Modify static assets
- Prune context silently
