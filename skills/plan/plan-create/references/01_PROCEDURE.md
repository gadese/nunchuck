# Procedure

## Step 1: Surface Scan

Run the CLI to identify relevant files:

```bash
./skill.sh surface --patterns "*.py" "*.md" "*.yaml"
```

Review the output to understand the work surface.

## Step 2: Initialize Plan

```bash
./skill.sh init --title "Description of objective"
```

This creates:
- `.plan/<N>/plan.md`
- `.plan/<N>/a/index.md`
- `.plan/<N>/a/i.md`

## Step 3: Populate Root Plan

Edit `.plan/<N>/plan.md`:

1. Write concrete **Objective**
2. Define checkable **Success Criteria**
3. List **Sub-plan Index** with letters and descriptions

## Step 4: Create Sub-plans

For each sub-plan letter:

1. Create directory: `.plan/<N>/<letter>/`
2. Create `index.md` with task list
3. Create task files: `i.md`, `ii.md`, etc.

## Step 5: Populate Tasks

For each task file, fill in:

- **Focus**: Specific goal (one sentence)
- **Inputs**: Files/artifacts needed
- **Work**: Numbered actionable steps

Leave **Output** and **Handoff** empty — those are for `plan-exec`.

## Step 6: Validate

Review the plan structure:

```bash
./skill.sh status <N>
```

Ensure no placeholders remain in Focus, Inputs, or Work sections.
