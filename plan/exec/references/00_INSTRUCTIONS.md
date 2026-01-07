# Instructions

## Initialize

1. Read all reference files listed in `metadata.references` in order before taking action.
2. Determine the target phase `<N>`:
   - If the user specifies `<N>`, use it.
   - Otherwise, use the highest numbered `docs/planning/phase-*/` directory (prefer a script if present).

## Policies

### Always

1. Only modify `docs/planning/phase-<N>/<active-letter>/<active-roman>.md` during execution.
2. Treat a roman file as complete only if it contains non-empty **Output** and **Handoff**.
3. Execute in order:
   - letters: a → b → c → …
   - roman files within a letter: i → ii → iii → iv
4. Each completed roman file must end with:
   - **Output** (concrete results)
   - **Handoff** (explicit next step)

### Never

1. Never rewrite previously completed roman files.
2. Never work ahead on later subphases.
3. Never modify `<letter>/plan.md` when roman numeral files exist for that letter.
4. Never finish the phase without performing the root wrap-up (success criteria check + Phase Summary).
