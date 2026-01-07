# Instructions

## Initialize

1. Read all reference files listed in `metadata.references` in order before taking action.

## Policies

### Always

1. Always prefer scripts for deterministic filesystem steps.
  a. If running on Windows, always run `scripts/dirs.ps1`.
  b. Otherwise, always run `scripts/dirs.sh`.

### Never

1. Never guess the next phase number `<N>`; it must be produced by the script or computed from the filesystem per Preconditions.
2. Never create root phase files other than `plan.md`.
