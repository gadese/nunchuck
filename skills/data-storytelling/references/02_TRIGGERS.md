---
description: Activation signals and invocation conditions for the data-storytelling skill.
index:
  - Invoke When
  - Do Not Invoke When
  - Exit If
  - Expected Inputs
  - Expected Outputs
---

# Triggers — Data Storytelling Skill

## Invoke When

- User has a technical document and needs it communicated to non-technical stakeholders
- User says "data story", "tell the story", or invokes `/data-storytelling`
- User asks to make technical findings "accessible", "understandable", or "presentable"
- User needs to translate research conclusions for executives, product managers, or business stakeholders
- User has completed an `algo-rpi-research` or `rpi-research` output and needs to communicate results
- User wants to extract the "so what" from a technical report

## Do Not Invoke When

- User wants original data analysis — use appropriate analysis tools
- User wants a technical summary for engineers — the audience is already technical
- User wants slide decks or visual presentations — this skill produces written narratives
- User wants to condense a document without restructuring — use summarization
- User wants to brainstorm approaches — use `brainstorm`
- User wants code review — use `code-review`

## Exit If

- No source document is provided and user cannot supply one
- User confirms the audience is technical and does not need translation
- User explicitly requests to stop

## Expected Inputs

- Technical conclusion document(s) (required — file path or inline content)
- Target audience description (optional — defaults to "non-technical stakeholders")
- Specific emphasis or focus areas (optional — e.g., "focus on cost implications")
- Desired tone (optional — defaults to "professional and clear")

## Expected Outputs

- Narrative document at `llm_docs/narratives/YYYY-MM-DD-HHMM-narrative-<topic>.md`
- Updated Memory Bank (`llm_docs/memory/activeContext.md`) if Memory Bank exists
