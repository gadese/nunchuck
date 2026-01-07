# Templates

## Root Plan Template

```md
# Plan <N> - <derived title>

## Purpose
(One or two sentences summarizing the user's objective)

## Context
(Extract key reasoning from the conversation so intent/rationale is preserved)

## Objectives
* [ ] Identify tasks necessary to resolve this plan
* [ ] Execute tasks in sequence
* [ ] Produce measurable outputs

## Constraints
(Include relevant technical/architectural rules mentioned in the discussion)

## Success Criteria
(Concrete closure conditions for this plan)

## Sub-plan Index
* a - <generated sub-plan name>
* b - <generated sub-plan name>
* c - ...
```

## Sub-plan Index Template (`index.md`)

```md
# Plan <N><letter> - <Sub-plan Name>

## Brief
(One or two sentences describing this sub-plan)

## Tasks
* i - <task name> - <brief description>
* ii - <task name> - <brief description>
* iii - <task name> - <brief description>
* iv - <task name> - <brief description>
* v - <task name> - <brief description>

(Add or remove task lines as needed.)
```

## Task Template (`i.md`, `ii.md`, `iii.md`, `iv.md`)

```md
# Plan <N><letter><roman> - <Task Name>

## Focus
(What this task is doing and why)

## Inputs
(Artifacts or reasoning from prior tasks or root context)

## Work
(Steps/decisions needed; include any checks or validations)

## Output
(Clear conclusion or artifact reference)

## Handoff
(Explicit instruction for the next task or next sub-plan)
```

If a subphase is split into roman numerals, apply the same template to each
`i.md`, `ii.md`, `iii.md`, and `iv.md` file in that subphase folder.
