# Procedure

## Step 1 — Determine active subphase

A subphase is considered complete if its `plan.md` includes a non-empty **Output** and a non-empty **Handoff**.

1. Starting from `a`, find the first subphase that is not complete.
2. That is the active subphase.
3. If all are complete, proceed to Phase wrap-up (Step 5).

## Step 2 — Load only what you need

Read:

- Root: `docs/planning/phase-<N>/plan.md`
- Active: `docs/planning/phase-<N>/<letter>/plan.md`
- Any referenced artifacts mentioned in Inputs (only as needed)

## Step 3 — Execute the active subphase

In the active subphase `plan.md`:

- Expand **Work** into a concrete sequence of steps that can be performed now.
- Perform the steps.
- Record the results under **Output**.
- Write a clear **Handoff** for the next subphase.

Do not perform steps that belong to later subphases.

## Step 4 — Advance to the next subphase

After completing `<letter>`:

- Move to the next letter in the root Subphase Index.
- Repeat Steps 2–4.

If the next subphase folder does not exist but the index includes it:

- Create it and scaffold `plan.md` using the same template structure already present.

## Step 5 — Phase wrap-up

When all subphases in the root Subphase Index are complete:

1. Update `docs/planning/phase-<N>/plan.md`:
   - Check off the root Success Criteria that were met.
   - If any success criteria were not met, add a short note explaining what remains.
2. Append a short **Phase Summary** section at the end of the root plan:
   - What was done
   - Key decisions
   - Links/paths to produced artifacts
   - Any follow-up phase suggestion if needed
