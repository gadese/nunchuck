# Procedure

Execute these steps literally, in order.

## Step 1 — Create the phase directory

Create:

- `docs/planning/phase-<N>/`

## Step 2 — Write the root plan

Create and write:

- `docs/planning/phase-<N>/plan.md`

Use the template from `04_TEMPLATES.md` and fill it from the **current conversation**.

### Rules for Subphase Index

- Subtasks MUST be derived from the discussion (no "filler tasks").
- Prefer 2–6 subphases. Use more only if clearly justified by the discussion.
- Each subphase should be independently completable and produce a tangible output.

## Step 3 — Create subphase directories and scaffolds

For each listed letter in the Subphase Index:

Create:

- `docs/planning/phase-<N>/<letter>/`
- `docs/planning/phase-<N>/<letter>/plan.md`

Populate each subphase plan using the subphase template from `04_TEMPLATES.md`.

### Dependency rule

The output of `<N>/a/plan.md` becomes an input to `<N>/b/plan.md`, etc., in alphabetical order.

## Output checklist

Confirm on disk before finishing:

- `docs/planning/phase-<N>/plan.md` exists and is populated
- Each listed subphase directory exists
- Each subphase has a populated plan.md
- Root plan has a Subphase Index matching the created subphase folders
