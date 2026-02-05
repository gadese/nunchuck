# Router

## Invocation

This skill is invoked when:
- User explicitly calls `/rpi-plan-review`
- The `/rpi-full` workflow reaches the Plan Review phase
- User requests review of an implementation plan

## Delegation

This skill does NOT delegate to other skills. It performs the review directly and returns control to the caller.
