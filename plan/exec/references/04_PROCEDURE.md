# Procedure

## Step 1 - Determine active task

A task file is considered complete if it includes a non-empty **Output** and a
non-empty **Handoff**.

1. Starting from sub-plan `a`, read `<letter>/index.md` to identify the ordered
   task list (roman numerals).
2. Scan tasks in order for the first incomplete task file.
3. If all tasks under the current sub-plan are complete, move to the next letter.
4. The first incomplete task file is the active task.
5. If all sub-plans are complete, proceed to Plan wrap-up (Step 5).

If `index.md` does not specify tasks, default to scanning roman numeral task
files present in the sub-plan folder in ascending order.

## Step 2 - Load only what you need

Read:

- Root: `docs/planning/phase-<N>/plan.md`
- Sub-plan: `docs/planning/phase-<N>/<letter>/index.md`
- Active: `docs/planning/phase-<N>/<letter>/<roman>.md`
- Any referenced artifacts mentioned in Inputs (only as needed)

## Step 3 - Execute the active task

In the active task file:

- Expand **Work** into a concrete sequence of steps that can be performed now.
- Perform the steps.
- Record the results under **Output**.
- Write a clear **Handoff** for the next task.

Do not perform steps that belong to later sub-plans.

## Step 4 - Advance to the next task

After completing `<roman>`:

- Move to the next task within the same sub-plan.
- If the current task is the last in the sub-plan, move to the next letter in
  the root Sub-plan Index.
- Repeat Steps 2-4.

If the next sub-plan folder does not exist but the index includes it:

- Create it and scaffold `index.md` and task files using the same template
  structure already present in the plan and listed in the new `index.md`.

## Step 5 - Plan wrap-up

When all sub-plans in the root Sub-plan Index are complete:

1. Update `docs/planning/phase-<N>/plan.md`:
   - Check off the root Success Criteria that were met.
   - If any success criteria were not met, add a short note explaining what remains.
2. Append a short **Plan Summary** section at the end of the root plan:
   - What was done
   - Key decisions
   - Links/paths to produced artifacts
   - Any follow-up plan suggestion if needed
