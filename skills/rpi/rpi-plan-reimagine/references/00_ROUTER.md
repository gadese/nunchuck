# Router

## Invocation

This skill is invoked when:
- User explicitly calls `/rpi-plan-reimagine`
- The `/rpi-full` workflow reaches the Plan Reimagine phase
- User requests optimization or rewrite of an implementation plan

## Delegation

This skill does NOT delegate to other skills. It performs the reimagination directly and returns control to the caller.
