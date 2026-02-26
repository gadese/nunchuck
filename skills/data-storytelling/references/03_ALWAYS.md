---
description: Mandatory behaviors and invariants for the data-storytelling skill.
index:
  - Source Fidelity
  - Audience Awareness
  - Structure and Clarity
  - Jargon Handling
  - Output and Documentation
---

# ALWAYS — Mandatory Behaviors

## Source Fidelity

- Always ground every claim in the source document — no invented conclusions
- Always preserve the source document's core findings, even when simplifying
- Always flag when a simplification loses important nuance (add a "nuance note" in the output)
- Always cite which source document a finding comes from when working with multiple inputs

## Audience Awareness

- Always ask who the target audience is if not specified (default: non-technical stakeholders)
- Always read Memory Bank first (`llm_docs/memory/activeContext.md`) to understand project context — skip gracefully if missing
- Always tailor vocabulary and depth to the stated audience
- Always treat the audience as intelligent professionals from a different domain — they lack your technical vocabulary, not reasoning ability

## Structure and Clarity

- Always lead with the most important finding ("so what" first, details after)
- Always use the narrative arc: Hook → Context → Findings → Implications → Recommendation
- Always include a one-sentence executive summary at the top of the output
- Always use concrete numbers over vague qualifiers ("3x faster" not "significantly faster")

## Jargon Handling

- Always replace technical jargon with plain-language equivalents
- Always provide a brief parenthetical explanation when a technical term cannot be avoided
- Always prefer analogy over definition when explaining complex concepts
- Always use cross-domain metaphors and comparisons that leverage the audience's existing expertise (e.g., explain model overfitting as "studying the answer key instead of learning the subject" — map to concepts the audience already understands)
- Always ensure metaphors are accurate enough to support the conclusion — if a metaphor would mislead, prefer a clear direct explanation instead

## Output and Documentation

- Always produce the output document at the end of the session
- Always check for existing file at the output path before writing — if collision, append numeric suffix (`-2`, `-3`, etc.)
- Always update Memory Bank after completing the narrative if Memory Bank exists
