# Procedure

## Step 1: Gather information

Before creating a task, determine:

- **ID**: A short, descriptive kebab-case identifier
- **Title**: Human-readable title (optional, defaults to ID)
- **Kind**: `feature`, `fix`, `refactor`, `docs`, `chore`, or `spike`
- **Risk**: `low`, `medium`, or `high`
- **Goal**: What the task aims to achieve (optional, can edit after)

## Step 2: Run the create command

```bash
cd skills/task/.resources/scripts
uv run task create <id> --title "Title" --kind <kind> --risk <risk> --select
```

Example:

```bash
uv run task create add-auth --title "Add authentication" --kind feature --risk medium --select
```

## Step 3: Edit the generated task file

Open `.tasks/<id>.md` and fill in:

- `## Goal` — Clear statement of what to achieve
- `## Acceptance` — Checkboxes for acceptance criteria
- `## Constraints` — Limitations or requirements
- `## Dependencies` — What must exist before this can be done

## Step 4: Verify

```bash
uv run task list
```

Confirm the task appears and is marked active (`*`).
