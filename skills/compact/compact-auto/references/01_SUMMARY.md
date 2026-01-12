# Summary

**compact-auto** delegates compaction strategy selection under strict guard rails.

## Mental Model

Auto compaction is a **trusted editor with rules** — the agent may exercise judgment, but only within defined boundaries.

## Key Principle

> Auto does NOT mean "model decides freely."

Auto mode operates under constraints. When uncertain, it must preserve or fail.

## Authority Level

Auto is the **only** member skill permitted to exercise delegated judgment. It must:

- Default to preservation on uncertainty
- Never violate the preservation floor
- Fall back to light behavior if justification cannot be formed
- Refuse if intent cannot be inferred safely
