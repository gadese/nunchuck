# RPI Skillset

Research-Plan-Implement workflow for general software development tasks.

## Overview

The `rpi` skillset provides a structured, three-phase approach to software development:

1. **Research** — Document current codebase state
2. **Plan** — Create detailed implementation plan
3. **Implement** — Execute plan with verification

Each phase includes mandatory pause points for user approval, ensuring alignment and preventing wasted effort.

## When to Use

### Use RPI for:
- General software development tasks
- Feature additions or modifications
- Refactoring existing code
- Bug fixes requiring analysis and planning
- Integration work across multiple components

### Use Algo-RPI instead for:
- Algorithm development and optimization
- Machine learning model implementation
- Performance-critical numerical code
- Tasks requiring quantitative benchmarks
- Reproducibility-critical implementations

## Skillset Structure

```
rpi/
├── SKILL.md                    # Orchestrator skill
├── README.md                   # This file
├── .pipelines/                 # Workflow definitions
│   ├── .INDEX.md              # Pipeline index
│   ├── 00_DEFAULT.md          # Full R-P-I workflow
│   ├── 01_RESEARCH_ONLY.md    # Research phase only
│   ├── 02_PLAN_ONLY.md        # Plan phase only
│   └── 03_IMPLEMENT_ONLY.md   # Implement phase only
├── .shared/                    # Symlink to coding-standards/references/
├── rpi-research/              # Research member skill
│   ├── SKILL.md
│   ├── README.md
│   └── references/            # 7 reference files (00-06)
├── rpi-plan/                  # Plan member skill
│   ├── SKILL.md
│   ├── README.md
│   └── references/            # 7 reference files (00-06)
└── rpi-implement/             # Implement member skill
    ├── SKILL.md
    ├── README.md
    └── references/            # 7 reference files (00-06)
```

## Quick Start

### Full Workflow
```
/rpi

Task: Add user authentication to the API
Files: src/api/auth.py, src/models/user.py
Constraints: Must use JWT tokens, maintain backward compatibility
```

### Individual Phases
```
/rpi-research
Research question: How does the current authentication system work?

/rpi-plan
Research document: llm_docs/research/2026-01-15-1420-research-auth.md
Task: Add JWT authentication

/rpi-implement
Plan document: llm_docs/plans/2026-01-15-1430-plan-auth.md
```

## Workflow Phases

### Phase 1: Research
**Skill:** `rpi-research`

**Purpose:** Create descriptive documentation of current codebase state

**Key Features:**
- Mandatory clarification protocol for ambiguous requests
- Parallel codebase exploration
- Descriptive analysis (no recommendations)
- Memory Bank integration
- Contract mismatch detection

**Output:** `llm_docs/research/YYYY-MM-DD-HHMM-research-<topic>.md`

**Pause Point:** Present findings summary, wait for approval

### Phase 2: Plan
**Skill:** `rpi-plan`

**Purpose:** Create detailed, actionable implementation plan

**Key Features:**
- Mandatory clarification protocol for ambiguous requirements
- Design option exploration (2-3 alternatives)
- Phased implementation structure
- Success criteria definition
- Risk identification and mitigation

**Output:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-<topic>.md`

**Pause Point:** Present plan structure and design decisions, wait for approval

### Phase 3: Implement
**Skill:** `rpi-implement`

**Purpose:** Execute approved plan with verification

**Key Features:**
- Mismatch evaluation (plan vs. reality)
- Phase-by-phase implementation
- Automated verification after each phase
- Progress tracking (plan checkboxes)
- Resumption support for interrupted work

**Output:** Code changes, updated plan with checkmarks

**Pause Point:** Present implementation summary, wait for approval

## Integration with Other Skills

### Code Review
After implementation, invoke `/code-review` to:
- Run automated quality checks
- Review against coding standards
- Fix issues and verify corrections

### Commit Message
After code review, invoke `/commit-message` to:
- Generate conventional commit message
- Analyze staged changes
- Present for user confirmation

### Doctor
During implementation, invoke `/doctor` if:
- Unexpected errors occur
- Tests fail without clear cause
- Debugging assistance needed

## Memory Bank Integration

The RPI workflow integrates with Memory Bank at each phase:

**Read at start of each phase:**
- `llm_docs/memory/activeContext.md` — Current context
- `llm_docs/memory/systemPatterns.md` — Existing patterns
- `llm_docs/memory/techContext.md` — Technical context

**Update after each phase:**
- Research: Add key findings to `activeContext.md`
- Plan: Add design decisions to `activeContext.md`
- Implement: Update `progress.md` with completed work

## Clarification Protocol

**Research and Plan phases MUST ask clarifying questions before proceeding when:**
- Scope is ambiguous or broad
- Multiple interpretations possible
- Target area, depth, or boundaries unclear
- Requirements are vague or incomplete

**Exception:** If request is narrowly defined and unambiguous, proceed directly.

## Pause Points

**Mandatory pause points between ALL phases:**
- ⏸️ After Research: Present findings, wait for user approval
- ⏸️ After Plan: Present plan structure, wait for user approval
- ⏸️ After Implement: Present implementation summary, wait for user approval

These pause points ensure:
- User alignment at each stage
- Opportunity to adjust direction
- Prevention of wasted implementation effort
- Clear handoff between phases

## Coding Standards

All RPI phases reference shared coding standards via `.shared/` symlink:

- `code-principles.md` — Core principles (DRY, SOLID, etc.)
- `code-style.md` — Style guidelines (naming, formatting, etc.)
- `ml-dl-guide.md` — ML/DL best practices
- `data-science-guide.md` — Data science guidelines

These standards are automatically applied during implementation and code review.

## Output Artifacts

### Research Document
- Location: `llm_docs/research/`
- Format: Markdown, no frontmatter
- Content: Descriptive analysis with file references
- Structure: Research question, findings by area, architecture, references

### Plan Document
- Location: `llm_docs/plans/`
- Format: Markdown, no frontmatter
- Content: Phased implementation plan with success criteria
- Structure: Overview, current state, design decision, phases, risks

### Implementation
- Location: Modified source files
- Format: Code changes following plan
- Tracking: Plan checkboxes updated as work completes
- Verification: Automated checks + manual criteria per phase

## Tips

1. **Start with research** if you're unfamiliar with the codebase area
2. **Use plan-only** if you already understand the current state
3. **Use implement-only** if you have an approved plan ready
4. **Ask clarifying questions** early to avoid rework
5. **Trust the pause points** — they prevent wasted effort
6. **Update Memory Bank** regularly for cross-session continuity
7. **Invoke code-review** after implementation for quality assurance

## Examples

### Example 1: New Feature
```
/rpi

Task: Add rate limiting to API endpoints
Files: src/api/middleware.py, src/config/settings.py
Constraints: Must support per-user and per-IP limits
```

### Example 2: Bug Fix
```
/rpi-research
Research question: Why are database connections leaking in the worker pool?

# After research...
/rpi-plan
Research document: llm_docs/research/2026-01-15-1500-research-db-leak.md

# After plan approval...
/rpi-implement
Plan document: llm_docs/plans/2026-01-15-1515-plan-db-leak.md
```

### Example 3: Refactoring
```
/rpi

Task: Extract authentication logic into separate service
Files: src/api/auth.py, src/services/auth_service.py
Constraints: Maintain backward compatibility, add tests
```

## See Also

- `algo-rpi/` — Algorithm-specific R-P-I workflow
- `code-review/` — Code quality review skill
- `commit-message/` — Commit message generation skill
- `memory-bank/` — Memory Bank management skill
- `doctor/` — Failure diagnosis skill
- `coding-standards/` — Shared coding guidelines
