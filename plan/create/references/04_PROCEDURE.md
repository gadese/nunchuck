# Procedure

Execute these steps literally, in order.

## Dry-run / no-files mode

If the user explicitly requests a dry-run or no files to be written:

- Do not run scripts.
- Do not create or edit any files.
- Provide an in-chat walk-through and overall impression only.
- Stop after responding in-chat.

## Step 1 - Create the plan directory (prefer scripts)

Preferred: use a script if available.

### macOS / Linux / WSL (bash)

If `scripts/dirs.sh` exists:

- Run: `bash scripts/dirs.sh`
- Capture the printed output path as `PLAN_DIR`
- Derive `<N>` from that path (e.g., `docs/planning/phase-30/` -> N=30)

### Windows (PowerShell)

If `scripts/dirs.ps1` exists:

- Run: `powershell -ExecutionPolicy Bypass -File scripts/dirs.ps1`
- Capture the printed output path as `PLAN_DIR`
- Derive `<N>` from that path

### Fallback (scripts missing)

Create:

- `docs/planning/phase-<N>/`

(Use `<N>` computed per Preconditions.)

## Step 2 - Write the root plan

Create and write:

- `docs/planning/phase-<N>/plan.md`

Use the template from `05_TEMPLATES.md` and fill it from the **current conversation**.

### Rules for Sub-plan Index

- Sub-plans MUST be derived from the discussion (no "filler tasks").
- Each sub-plan should be independently completable and produce a tangible output.

## Step 3 - Create sub-plan directories and scaffolds

For each listed letter in the Sub-plan Index:

Create:

- `docs/planning/phase-<N>/<letter>/`
- `docs/planning/phase-<N>/<letter>/index.md`
- Task files `docs/planning/phase-<N>/<letter>/i.md`, `ii.md`, `iii.md`, ...
  as needed

Populate each `index.md` using the Sub-plan Index Template from `05_TEMPLATES.md`.

Populate each task file using the Task Template from `05_TEMPLATES.md`.

### Task scoping

- Derive the tasks required for each sub-plan from the conversation and list them
  in `index.md` with brief descriptions.
- Use roman numeral ordering only (`i`, `ii`, `iii`, `iv`, `v`, ...).
- Only create task files that are listed in the sub-plan's `index.md`.
 
### Dependency rule

The output of the last completed task in `<N>/a/` becomes an input to
`<N>/b/index.md`, etc., in alphabetical order.

## Output checklist

Confirm on disk before finishing:

- `docs/planning/phase-<N>/plan.md` exists and is populated
- Each listed sub-plan directory exists
- Each sub-plan has a populated `index.md`
- Each task listed in `index.md` exists and is populated
- Root plan has a Sub-plan Index matching the created sub-plan folders
