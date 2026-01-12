# Triggers

When to activate or exit the compact skillset.

## Invoke When

- User explicitly requests compaction
- Context exceeds manageable size for continued work
- Preparing handoff to another agent or session
- Checkpointing progress before a phase transition
- Consolidating decisions into doctrine

## Do Not Invoke When

- User wants summarization (different operation)
- Target is unbounded or ambiguous
- Content is static assets (not context)
- Implicit compaction is implied

## Exit Immediately If

- Compaction completes successfully
- User cancels the operation
- Failure conditions are met

## Do Not Infer

- Do not choose targets automatically
- Do not assume compaction is wanted
- Do not compact without explicit request
