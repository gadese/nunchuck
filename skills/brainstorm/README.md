# Brainstorm Skill

Interactive algorithm and AI/ML solution brainstorming through multi-round conversational narrowing.

## Overview

The `brainstorm` skill guides users from broad problem understanding to a ranked shortlist of 2-3 concrete candidate approaches. It uses a 5-phase narrowing funnel (Clarify → Diverge → Narrow → Converge → Document) combining Socratic dialogue with purposeful tool-assisted research.

**Key Features:**
- Multi-round narrowing funnel with adaptive depth (2-7 rounds)
- Calibrated devil's advocate posture (signal-responsive, not mechanical)
- Purposeful tool integration (web search for landscape/recency, context7 for library docs)
- Novel problem handling via cross-domain decomposition
- Formal output document with ranked candidates

## When to Use

### Use Brainstorm:
- Exploring approaches for a new problem before committing
- Unsure which algorithm family or technique to use
- Want to understand trade-offs between multiple approaches
- Stuck on approach selection and need structured exploration
- Novel problem with no obvious solution

### Do Not Use Brainstorm:
- Already chose an approach and want implementation → use `rpi-implement` or `algo-rpi-implement`
- Want codebase research → use `rpi-research`
- Want formal algorithm analysis with quantitative targets → use `algo-rpi-research`

## Quick Start

```
/brainstorm

I need to detect anomalies in real-time sensor data from industrial equipment.
Constraints: <100ms latency, runs on edge devices, limited labeled data.
```

The skill will:
1. **Clarify** — Ask focused questions about the problem and constraints
2. **Diverge** — Survey the solution landscape (4-6 broad options via web search)
3. **Narrow** — Iteratively refine through 2-5 rounds of research and discussion
4. **Converge** — Present top 2-3 candidates with trade-offs and recency check
5. **Document** — Write formal output to `llm_docs/research/`

## Agent Posture

The brainstorm agent operates as a **calibrated devil's advocate**:

- **When user fixates early:** Strong challenge — "Have you considered [alternative]?"
- **When user dismisses without reasoning:** Probe — "What's the specific concern?"
- **When user is genuinely exploring:** Light facilitation — "One thing to consider..."

The posture adapts to user signals, not a mechanical schedule. The goal is expanding the solution space, not interrogation.

## Output Format

Each brainstorm session produces a formal document at:
`llm_docs/research/YYYY-MM-DD-HHMM-research-brainstorm-<topic>.md`

The document has 4 sections:
1. **Problem Understanding** — Restated problem, constraints, data characteristics
2. **Exploration Path** — Narrowing journey, decision points, pruned alternatives
3. **Candidate Approaches (Ranked)** — Top 2-3 with description, trade-offs, libraries, risks
4. **Next Steps** — Recommended path forward, open questions, suggested experiments

## Relationship to Other Skills

The brainstorm skill is **parallel** to the RPI workflow, not coupled to it:

- **Brainstorm** → Interactive, opinionated, explores the solution space with the user
- **algo-rpi-research** → Analytical, neutral, formal algorithm research without user interaction

A typical flow: `/brainstorm` to explore → `/algo-rpi-research` to formally analyze the top candidate → `/algo-rpi-plan` to plan implementation.

## Skill Structure

```
brainstorm/
├── SKILL.md                    # Skill manifest
├── README.md                   # This file
└── references/
    ├── 00_ROUTER.md           # Routing logic (single default route)
    ├── 01_SUMMARY.md          # Skill identity
    ├── 02_TRIGGERS.md         # When to invoke
    ├── 03_ALWAYS.md           # Mandatory behaviors
    ├── 04_NEVER.md            # Prohibited behaviors
    ├── 05_PROCEDURE.md        # Narrowing funnel procedure
    └── 06_FAILURES.md         # Error handling and recovery
```

## See Also

- `algo-rpi/algo-rpi-research/` — Formal algorithm research (analytical, neutral)
- `rpi/rpi-research/` — Codebase research (descriptive, non-interactive)
- `algo-rpi/algo-rpi-plan/` — Algorithm implementation planning
- `memory-bank/` — Memory Bank management
