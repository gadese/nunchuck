# Never

## No Freeform Summarization

- Never treat this as "summarize however you want"
- Never ignore guard rails
- Never optimize brevity over safety

## No Unjustified Actions

- Never remove without internal justification
- Never merge concepts without semantic equivalence
- Never normalize if meaning changes

## No Silent Failure

- Never produce partial output on constraint violation
- Never downgrade silently (e.g., fail to heavy when floor violated)
- Never proceed if intent cannot be safely inferred

## Forbidden If Specified

If `auto_constraints.forbid` includes an action, that action is absolutely forbidden:

- `rationale_removal` → never remove rationale
- `entity_merging` → never merge entities
- `language_normalization` → never normalize language
