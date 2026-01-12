# compact

Perform explicit, target-aware context compaction with declared loss boundaries and epistemic guard rails.

## Purpose

- Reduce context intentionally
- Preserve declared invariants
- Prevent silent drift or accidental reinterpretation

## Key principle

Invocation selects authority. Execution enforces it.

No skill accepts a `mode` parameter. Authority is encoded in the skill identity.

## Member skills

- `compact-light` — Checkpoint (recoverability > brevity)
- `compact-heavy` — Doctrine (authority > recoverability)
- `compact-auto` — Trusted editor with rules (delegated judgment)

## How to use

- Follow `SKILL.md`.
- Refer to `.shared/references/` for shared guard rails and schemas.
- Select the appropriate member skill based on intent.

## Layout

- `SKILL.md`
- `.pipelines/`
- `.shared/`
- Member skill directories listed above
