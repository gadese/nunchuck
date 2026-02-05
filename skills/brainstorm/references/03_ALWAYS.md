---
description: Mandatory behaviors and invariants for the brainstorm skill.
index:
  - Context Gathering
  - Clarification Gate
  - Tool Usage
  - Option Presentation
  - Posture and Challenging
  - Output and Documentation
---

# ALWAYS — Mandatory Behaviors

## Context Gathering

- Always read Memory Bank first (`llm_docs/memory/activeContext.md`, `systemPatterns.md`, `techContext.md`). Gracefully handle missing files (fresh project with no Memory Bank) — skip without error and note the gap
- Always read any user-specified files or context before beginning

## Clarification Gate

- Always ask clarifying questions before diverging (CLARIFY → DIVERGE gate)
- Always confirm problem understanding before exploring solutions

## Tool Usage

- Always use **web search** in the DIVERGE phase to ground the landscape survey (specific moment, specific purpose: map the territory)
- Always use **web search** in the CONVERGE phase for recency check on finalists (specific purpose: recent developments, known issues, production adoption)
- Always use **context7** during NARROW rounds when exploring specific libraries or frameworks (specific purpose: library-specific documentation and capabilities)

## Option Presentation

- Always present options using **unordered bullet points** during DIVERGE and NARROW (prevents anchoring bias from numbered lists)
- Always present trade-offs alongside each option, not just recommendations
- Always include at least one unconventional or surprising option during DIVERGE
- Always present a minimum of 4 options during DIVERGE and 3 during NARROW
- Always present options before asking the user to choose (no leading)

## Posture and Challenging

- Always calibrate challenge intensity to user signals:
  - Heavy challenging when user fixates early or dismisses options without reasoning
  - Light facilitation when user is genuinely exploring multiple directions
- Always question the problem framing at least once during DIVERGE ("Are we solving the right problem?")

## Output and Documentation

- Always produce the formal output document at the end of the session
- Always check for existing file at the output path before writing — if collision, append numeric suffix (`-2`, `-3`, etc.)
- Always update Memory Bank after completing the brainstorm
- Always suggest next steps (e.g., "proceed to `/algo-rpi-research` with Rank 1")
