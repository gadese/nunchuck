# Data Storytelling Skill

Transforms technical conclusion documents into structured, accessible narratives for non-technical audiences.

## Overview

The `data-storytelling` skill takes technical documents — research findings, algorithm evaluations, experiment results, performance analyses — and produces clear narrative documents that preserve accuracy while removing jargon. It operates as a 5-step transformation pipeline (Ingest → Analyze → Structure → Draft → Review) that identifies what matters to the audience, translates complexity into plain language, and structures the output around impact.

**Key Features:**
- Technical-to-accessible translation with source fidelity
- Audience-aware jargon replacement with analogies and parenthetical explanations
- Multiple narrative frameworks (Finding, Comparison, Progress, Risk stories)
- Impact-first structure: lead with "so what", details after
- Built-in accuracy verification against source material

## When to Use

### Use Data Storytelling:
- Technical document needs to reach non-technical stakeholders
- Research conclusions need to be communicated to executives or product managers
- `algo-rpi-research` or `rpi-research` output needs to be shared beyond the engineering team
- Technical report needs the "so what" extracted and made accessible
- Multiple technical findings need to be synthesized into a single narrative

### Do Not Use Data Storytelling:
- Audience is technical and does not need translation
- Need original data analysis → use appropriate analysis tools
- Need slide decks or visual presentations → this produces written narratives only
- Need a shorter version of a document → use summarization
- Need to brainstorm approaches → use `brainstorm`

## Quick Start

```
/data-storytelling

Source: llm_docs/research/2025-02-10-1430-research-anomaly-detection.md
Audience: Product leadership team
Focus: Cost and timeline implications
```

The skill will:
1. **Ingest** — Read the source document and project context
2. **Analyze** — Identify key findings, rank by audience relevance, flag jargon
3. **Structure** — Choose a narrative framework and organize information
4. **Draft** — Write the accessible narrative with plain language and concrete numbers
5. **Review** — Verify accuracy against source, check for remaining jargon

## Output Format

Each session produces a narrative document at:
`llm_docs/narratives/YYYY-MM-DD-HHMM-narrative-<topic>.md`

The document follows an impact-first structure:
1. **Executive Summary** — One-sentence takeaway
2. **The Key Finding** — Most important result in plain language
3. **Context** — Why it matters
4. **What We Found** — Findings ranked by audience relevance
5. **What This Means** — Implications for the audience's decisions
6. **Limitations** — Caveats preserved from the source
7. **Recommended Next Steps** — Actions grounded in the source conclusions
8. **Technical Appendix** — Key definitions for curious readers

## Narrative Frameworks

The skill selects the best-fit framework based on document type:

- **Finding Story** — Single key insight with supporting evidence
- **Comparison Story** — Side-by-side evaluation of approaches or options
- **Progress Story** — Timeline of improvements or changes
- **Risk Story** — What was found, what it means, what could go wrong

## Relationship to Other Skills

The data-storytelling skill is **downstream** of research and analysis skills:

- **algo-rpi-research** / **rpi-research** → Produce technical findings
- **data-storytelling** → Transforms those findings for non-technical audiences

A typical flow: `/algo-rpi-research` to analyze → `/data-storytelling` to communicate results to stakeholders.

## Skill Structure

```
data-storytelling/
├── SKILL.md                    # Skill manifest
├── README.md                   # This file
└── references/
    ├── 00_ROUTER.md           # Routing logic (single default route)
    ├── 01_SUMMARY.md          # Skill identity
    ├── 02_TRIGGERS.md         # When to invoke
    ├── 03_ALWAYS.md           # Mandatory behaviors
    ├── 04_NEVER.md            # Prohibited behaviors
    ├── 05_PROCEDURE.md        # Transformation pipeline
    └── 06_FAILURES.md         # Error handling and recovery
```

## See Also

- `algo-rpi/algo-rpi-research/` — Formal algorithm research (produces technical findings)
- `rpi/rpi-research/` — Codebase research (produces technical documentation)
- `brainstorm/` — Interactive solution brainstorming
- `memory-bank/` — Memory Bank management
