---
description: When to invoke or exit this skill.
index:
  - Invoke When
  - Do Not Invoke When
  - Exit Immediately If
  - Do Not Infer
---

# Triggers

When to activate or exit the doctor skill.

## Invoke When

- User reports a bug, error, or unexpected behavior
- User asks "why is X happening?"
- User describes symptoms without clear cause
- Investigation is needed before action
- Previous fix attempts have failed

### R-P-I Integration Triggers

- **During rpi-implement**: Unexpected errors occur during implementation
- **During rpi-implement**: Tests fail for unclear reasons
- **During rpi-implement**: Behavior doesn't match plan expectations
- **During algo-rpi-implement**: Numerical stability issues arise
- **During algo-rpi-implement**: Performance metrics don't meet targets
- **During algo-rpi-implement**: Algorithm behavior is unexpected
- **During algo-rpi-implement**: Reproducibility fails

## Do Not Invoke When

- User has already identified root cause with certainty
- User explicitly requests a fix without investigation
- Problem is trivial (typo, missing import)
- User is asking for feature implementation, not debugging

## Exit Immediately If

- User says "just fix it" after seeing diagnosis
- Diagnosis confidence exceeds 90% and user approves treatment
- User explicitly abandons the investigation
- Problem resolves itself during investigation

## Do Not Infer

- Do not assume a problem exists without user confirmation
- Do not start diagnosing code quality issues unprompted
- Do not expand scope to unrelated systems
