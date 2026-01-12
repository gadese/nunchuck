# Guard Rails

Mandatory constraints for auto mode. These are non-negotiable.

## Preservation Floor

Always preserve (violation triggers failure):

- Explicit decisions
- Active constraints
- TODOs / open questions
- Named entities
- Normative language ("must", "never", "always")

If any of these would be removed → **fail**.

## Default Loss Bias

- Light behavior → keep
- Heavy behavior → discard
- Auto behavior → **keep unless clearly redundant**

When uncertain, preserve.

## Justification Requirement

If the agent cannot internally justify:

- Why something was removed
- Why concepts were merged

→ it must **preserve or fail**.

No silent removal. No unjustified merging.

## Stability Preference

Auto mode must prefer outputs that:

- Are resilient to small source changes
- Avoid premature doctrine
- Minimize reinterpretation risk

Stability > aggressive compaction.
