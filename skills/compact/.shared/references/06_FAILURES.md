# Failures

When compact-* skills must refuse.

## Must Refuse If

1. **Target is ambiguous or unbounded**
   - No clear identifier
   - Scope cannot be determined

2. **Preserve/discard rules conflict**
   - Same element in both lists
   - Logical contradiction

3. **Schema is missing or underspecified**
   - No schema provided
   - Schema cannot be inferred

4. **Auto mode would violate preservation floor**
   - Delegated judgment cannot preserve required elements

5. **Request implies implicit compaction**
   - No explicit target
   - Background operation requested

6. **Agent would need to invent intent**
   - Insufficient context to determine purpose
   - User intent unclear

## Failure Behavior

- Failure must be **safe and explicit**
- No partial output is produced
- Failure reason must be specific and actionable
- Original target remains unmodified

## Invalidation

Compacted artifacts are invalidated if:

- Source hash changes
- Target boundaries change
- Schema version changes

Re-compaction must always be **explicitly requested**.
