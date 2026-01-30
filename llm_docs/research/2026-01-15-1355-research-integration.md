# Research — Custom R-P-I Workflow Integration into Nunchuck

**Tags**: `integration`, `skills`, `workflows`, `research-plan-implement`, `algorithm`, `memory-bank`

## 1. Research Question

How should the custom Research-Plan-Implement (R-P-I) workflow files in `CUSTOM_RULES/` be integrated into the nunchuck repository's `skills/` directory to work alongside existing skillsets, while preserving the Memory Bank system and converting to nunchuck-compliant skill specifications?

---

## 2. Repository Context Overview

### 2.1 Nunchuck Repository Structure

The nunchuck repository is a rigorously structured collection of agent skills designed to reduce drift, enforce determinism, and make agentic work auditable.

**Key directories:**
- `skills/` — Contains 9 skillsets with member skills
- `.windsurf/workflows/` — Thin wrappers that delegate to skills
- `docs/design/` — Specifications, tenets, and determinism framework
- `scripts/` — IDE adapters and index generators

**Design principles (from `README.md:16-27`):**
- **Determinism First, Subjectivity Last** — Subjective reasoning must never compensate for missing deterministic outputs
- **Artifacts as Completion Signals** — Success is mechanically verifiable via declared artifacts
- **Professional Skepticism** — Agents interpret and challenge rather than blindly comply

### 2.2 Custom Files Location

Custom files are located in `CUSTOM_RULES/` with the following structure:
- `rules/` — 12 rule files (manual trigger, various purposes)
- `workflows/` — 3 workflow files (orchestrators)
- `skills/` — 1 skill (code-review-cleanup)
- `IMPLEMENTATION_SUMMARY.md` — Documents the original setup

---

## 3. Existing Nunchuck Skillsets

### 3.1 Skillset Inventory

| Skillset | Description | Member Skills | Relevance |
|----------|-------------|---------------|-----------|
| `plan` | Manages bounded work units with structured plans in `.plan/` | `plan-create`, `plan-exec`, `plan-status`, `plan-review` | **HIGH** — Similar to R-P-I workflow |
| `doctor` | Diagnoses software failures using deterministic evidence gathering | Single orchestrator | **KEEP** — Useful for debugging |
| `task` | Manages single-file tasks in `.tasks/` with staleness detection | `task-create`, `task-list`, `task-select`, `task-close` | **LOW** — Simpler than `plan`, overlaps |
| `dtx` | Manages agent working context via `.dtx/` artifacts | `dtx-validate`, `dtx-state`, `dtx-gather`, `dtx-forget` | **LOW** — Overlaps with Memory Bank |
| `grape` | AI-enabled deterministic codebase search | Single orchestrator | **LOW** — Research rules already do this |
| `changelog` | Manages Keep a Changelog format files | `changelog-init`, `changelog-update`, `changelog-release`, `changelog-verify` | **REMOVE** — Not relevant to AI implementation |
| `sniff` | Detects code smells using deterministic heuristics | `sniff-bloaters`, `sniff-couplers`, `sniff-abusers`, `sniff-preventers`, `sniff-locate` | **REMOVE** — Not relevant to AI implementation |
| `prompt` | Separates intent formation from execution | `prompt-forge`, `prompt-compile`, `prompt-exec` | **REMOVE** — Not relevant |
| `md` | Orchestrates markdown document workflows | `md-split`, `md-merge`, `md-review` | **REMOVE** — Not relevant |

### 3.2 Skillset Structure Pattern

Each skillset follows a consistent structure (from `skills/plan/` example):

```
skills/<skillset>/
├── SKILL.md              # Orchestrator with frontmatter metadata
├── README.md             # Human-readable description
├── .pipelines/           # Workflow pipelines (may be empty)
├── .shared/              # Shared resources across member skills
└── <member-skill>/       # One directory per member skill
    ├── SKILL.md          # Member skill frontmatter
    ├── README.md         # Member skill description
    └── references/       # Reference files (00_ROUTER through 06_FAILURES)
```

### 3.3 Skill Specification Requirements

From `docs/design/specs/`:

**SKILL.md Frontmatter (required fields):**
- `name` — Skill identifier
- `description` — Brief description
- `metadata.author` — Author name
- `metadata.references` — List of reference files
- `metadata.keywords` — Search keywords

**SKILL.md Body:**
- Must contain only `# INSTRUCTIONS` heading
- Must reference `metadata.references` or `.pipelines/.INDEX.md`

**Reference Files Pattern:**
Skills use a canonical 7-file reference structure:
- `00_ROUTER.md` — Entry point and routing logic
- `01_SUMMARY.md` — Brief summary
- `02_TRIGGERS.md` — When to invoke
- `03_ALWAYS.md` — Always-do constraints
- `04_NEVER.md` — Never-do constraints
- `05_PROCEDURE.md` — Step-by-step procedure
- `06_FAILURES.md` — Failure handling

---

## 4. Custom Files Analysis

### 4.1 Custom Rules Inventory

| File | Trigger | Purpose | Integration Path |
|------|---------|---------|------------------|
| `research.md` | manual | Descriptive codebase research | → `rpi/rpi-research/` skill |
| `plan.md` | manual | Technical planning with design options | → `rpi/rpi-plan/` skill |
| `implement.md` | manual | Plan execution with verification | → `rpi/rpi-implement/` skill |
| `review.md` | manual | Code quality assurance | → `rpi/rpi-review/` skill |
| `algo-research.md` | manual | Algorithm problem formalization | → `rpi/rpi-algo-research/` skill |
| `algo-plan.md` | manual | Algorithm planning with quantitative targets | → `rpi/rpi-algo-plan/` skill |
| `algo-implement.md` | manual | Algorithm implementation with benchmarking | → `rpi/rpi-algo-implement/` skill |
| `code-principles-guide.md` | always_on | Python code principles | → `.shared/` reference |
| `code-style-guide.md` | always_on | Python code style | → `.shared/` reference |
| `machine-deep-learning-guide.md` | model_decision | ML/DL best practices | → `.shared/` reference |
| `data-science-pandas-guide.md` | model_decision | Pandas/data science practices | → `.shared/` reference |
| `memory-bank-protocol.md` | always_on | Memory Bank usage protocol | → `.shared/` reference |

### 4.2 Custom Workflows Inventory

| File | Purpose | Integration Path |
|------|---------|------------------|
| `research-plan-implement.md` | 4-phase R-P-I-Review orchestrator | → `rpi/` skillset orchestrator |
| `algo-research-plan-implement.md` | Algorithm-specific R-P-I orchestrator | → `rpi/` skillset pipeline |
| `update-memory-bank.md` | Memory Bank update workflow | → `rpi/` skillset pipeline |

### 4.3 Custom Skills Inventory

| Directory | Purpose | Integration Path |
|-----------|---------|------------------|
| `code-review-cleanup/` | Systematic code review and cleanup | → `rpi/rpi-review/` (merge with review.md) |

### 4.4 Custom Rule Format Analysis

Current format uses XML-like tags within markdown:

```markdown
---
trigger: manual
---

<system_context>
You are a meticulous codebase researcher...
</system_context>

<role>
# Research Agent — Descriptive Codebase Analysis
...
</role>

<critical_constraints>
## Absolute Boundaries
**YOU MUST NOT:**
- ...
**YOU MUST:**
- ...
</critical_constraints>

<process>
## Research Process
### Step 1: Read Memory Bank
...
</process>
```

**Conversion requirement:** This format must be converted to nunchuck's reference file structure:
- `<critical_constraints>` → `03_ALWAYS.md` + `04_NEVER.md`
- `<process>` → `05_PROCEDURE.md`
- `<system_context>` + `<role>` → `01_SUMMARY.md`
- Invocation behavior → `02_TRIGGERS.md`
- Error handling → `06_FAILURES.md`

---

## 5. Memory Bank System

### 5.1 Memory Bank Files

The custom workflow uses a `llm_docs/memory/` system with 7 files:

| File | Purpose | Update Frequency |
|------|---------|------------------|
| `memory-index.md` | Index of all memory files | Rare |
| `projectbrief.md` | Project requirements and definition of done | Rare |
| `productContext.md` | Feature rationale and business logic | Occasional |
| `activeContext.md` | Current session state, recent work, next steps | **Frequent** |
| `systemPatterns.md` | Architectural patterns and tech decisions | Occasional |
| `techContext.md` | Dependencies, APIs, schemas, environment | Occasional |
| `progress.md` | Feature completion checklist | Frequent |

### 5.2 Memory Bank vs Nunchuck Alternatives

| Aspect | Memory Bank | Nunchuck `dtx` | Nunchuck `plan` |
|--------|-------------|----------------|-----------------|
| **Storage** | `llm_docs/memory/` | `.dtx/` | `.plan/<N>/` |
| **Scope** | Project-wide persistent context | Per-task working context | Per-work-unit bounded scope |
| **Files** | 7 predefined files | `CONTRACT.yml`, `FORGET.yml`, `EXPANDS/` | Root plan, sub-plans, tasks |
| **Purpose** | Cross-session memory | Auditable context management | Structured planning |

**Decision:** Keep Memory Bank system as it provides persistent cross-session context that `dtx` and `plan` don't directly replace. The R-P-I skills will reference Memory Bank files as part of their procedure.

---

## 6. Proposed Skillset Structure

### 6.1 New Skillset: `rpi` (Research-Plan-Implement)

```
skills/rpi/
├── SKILL.md                    # Orchestrator
├── README.md                   # Human description
├── .pipelines/
│   ├── .INDEX.md               # Pipeline index
│   ├── generic.md              # Generic R-P-I-Review pipeline
│   └── algorithm.md            # Algorithm-specific pipeline
├── .shared/
│   ├── code-principles.md      # From code-principles-guide.md
│   ├── code-style.md           # From code-style-guide.md
│   ├── ml-dl-guide.md          # From machine-deep-learning-guide.md
│   ├── data-science-guide.md   # From data-science-pandas-guide.md
│   └── memory-bank-protocol.md # From memory-bank-protocol.md
├── rpi-research/
│   ├── SKILL.md
│   ├── README.md
│   └── references/
│       ├── 00_ROUTER.md
│       ├── 01_SUMMARY.md
│       ├── 02_TRIGGERS.md
│       ├── 03_ALWAYS.md
│       ├── 04_NEVER.md
│       ├── 05_PROCEDURE.md
│       └── 06_FAILURES.md
├── rpi-plan/
│   └── [same structure]
├── rpi-implement/
│   └── [same structure]
├── rpi-review/
│   └── [same structure]
├── rpi-algo-research/
│   └── [same structure]
├── rpi-algo-plan/
│   └── [same structure]
└── rpi-algo-implement/
    └── [same structure]
```

### 6.2 Member Skills

| Skill | Source | Purpose |
|-------|--------|---------|
| `rpi-research` | `research.md` | Descriptive codebase research |
| `rpi-plan` | `plan.md` | Technical planning with design options |
| `rpi-implement` | `implement.md` | Plan execution with verification |
| `rpi-review` | `review.md` + `code-review-cleanup/` | Code quality assurance and cleanup |
| `rpi-algo-research` | `algo-research.md` | Algorithm problem formalization |
| `rpi-algo-plan` | `algo-plan.md` | Algorithm planning with quantitative targets |
| `rpi-algo-implement` | `algo-implement.md` | Algorithm implementation with benchmarking |

---

## 7. Format Conversion Mapping

### 7.1 Rule to Skill Conversion

For each rule file, content maps to reference files as follows:

| Source Section | Target File | Content |
|----------------|-------------|---------|
| `<system_context>` + `<role>` | `01_SUMMARY.md` | Brief description of the agent role |
| `<invocation_response>` + `<invocation_behavior>` | `02_TRIGGERS.md` | When and how to invoke |
| `<critical_constraints>` "YOU MUST" | `03_ALWAYS.md` | Always-do constraints |
| `<critical_constraints>` "YOU MUST NOT" | `04_NEVER.md` | Never-do constraints |
| `<process>` + `<clarification_protocol>` | `05_PROCEDURE.md` | Step-by-step procedure |
| `<handoff>` + error handling | `06_FAILURES.md` | Failure modes and recovery |
| `<output_format>` | `05_PROCEDURE.md` (appendix) or separate reference | Output templates |

### 7.2 SKILL.md Frontmatter Template

```yaml
---
name: rpi-research
license: MIT
description: >
  Descriptive codebase research for the Research-Plan-Implement workflow.
  Produces technical documentation about current system state.
metadata:
  author: Gabriel Descoteaux
  version: 0.1.0
  references:
    - 00_ROUTER.md
    - 01_SUMMARY.md
    - 02_TRIGGERS.md
    - 03_ALWAYS.md
    - 04_NEVER.md
    - 05_PROCEDURE.md
    - 06_FAILURES.md
  keywords:
    - research
    - codebase
    - documentation
    - analysis
---

# INSTRUCTIONS

1. Refer to `metadata.references`.
```

### 7.3 Workflow to Pipeline Conversion

Workflows become pipelines in `.pipelines/`:

| Source Workflow | Target Pipeline | Purpose |
|-----------------|-----------------|---------|
| `research-plan-implement.md` | `.pipelines/generic.md` | 4-phase R-P-I-Review for general tasks |
| `algo-research-plan-implement.md` | `.pipelines/algorithm.md` | Algorithm-specific R-P-I with P0-P5 phases |
| `update-memory-bank.md` | `.pipelines/memory-bank.md` | Memory Bank update workflow |

---

## 8. Integration with Existing Nunchuck Components

### 8.1 Workflow Generation

The nunchuck repository uses adapter scripts to generate IDE-specific workflow files:

```bash
# Generates .windsurf/workflows/ from skills/
bash scripts/adapters/windsurf/run.sh --skills-root skills --output-root .
```

After integration, the new `rpi` skillset will automatically generate workflows:
- `/rpi` — Orchestrator
- `/rpi-research`, `/rpi-plan`, `/rpi-implement`, `/rpi-review`
- `/rpi-algo-research`, `/rpi-algo-plan`, `/rpi-algo-implement`

### 8.2 Index Generation

The index generator creates `.SKILLS.md` for agent discovery:

```bash
bash scripts/index/run.sh --skills-root skills
```

The new `rpi` skillset will appear in the generated index.

### 8.3 Relationship with `doctor` Skillset

The `doctor` skillset remains useful for debugging failures during implementation phases. It can be invoked when `rpi-implement` encounters unexpected errors:

- **Complementary use:** `rpi-implement` → encounters failure → invoke `doctor` → diagnose → return to `rpi-implement`
- **No overlap:** `doctor` focuses on diagnosis, `rpi` focuses on structured implementation

---

## 9. Files Marked for Removal

The following nunchuck skillsets are not relevant to AI scientist work and should be removed or excluded:

| Skillset | Reason for Removal |
|----------|-------------------|
| `changelog` | Release management, not AI implementation |
| `sniff` | Code smell detection, not primary focus |
| `prompt` | Prompt forging workflow, not relevant |
| `md` | Markdown document workflows, not relevant |
| `task` | Overlaps with `plan`, simpler but less structured |
| `dtx` | Context management overlaps with Memory Bank |
| `grape` | Codebase search already covered in research rules |

**Note:** The `plan` skillset could potentially be kept as an alternative to `rpi` for simpler tasks, or removed if `rpi` covers all use cases.

---

## 10. Key Differences: Custom vs Nunchuck Patterns

### 10.1 Constraint Language

| Aspect | Custom Format | Nunchuck Format |
|--------|---------------|-----------------|
| **Location** | Inline in rule file | Separate `03_ALWAYS.md` and `04_NEVER.md` |
| **Style** | `**YOU MUST:**` / `**YOU MUST NOT:**` | Bullet lists with clear imperatives |
| **Scope** | Combined in one section | Split into two files |

### 10.2 Procedure Structure

| Aspect | Custom Format | Nunchuck Format |
|--------|---------------|-----------------|
| **Location** | `<process>` XML tag | `05_PROCEDURE.md` file |
| **Steps** | Numbered within markdown | Numbered with clear completion signals |
| **Artifacts** | Implicit (output templates) | Explicit artifact declarations |

### 10.3 Invocation

| Aspect | Custom Format | Nunchuck Format |
|--------|---------------|-----------------|
| **Trigger** | YAML frontmatter `trigger: manual` | `02_TRIGGERS.md` file |
| **Response** | `<invocation_response>` section | Part of `02_TRIGGERS.md` |
| **Keywords** | None | `metadata.keywords` in frontmatter |

---

## 11. Assumptions & Unknowns

### 11.1 Assumptions

- The Memory Bank system (`llm_docs/memory/`) will be workspace-specific, not part of the skillset
- The `rpi` skillset will be used primarily for AI/ML implementation tasks
- Nunchuck's adapter scripts will correctly generate workflows for the new skillset
- The 7-file reference structure is sufficient to capture all custom rule content

### 11.2 Unknowns

- **Pipeline format:** The exact format for `.pipelines/*.md` files needs verification against existing examples
- **Shared resources:** How `.shared/` files are referenced from member skills needs verification
- **Validation:** Whether nunchuck has validation tooling to check spec compliance
- **Router logic:** The `00_ROUTER.md` file purpose and format needs clarification from existing examples

---

## 12. References

### 12.1 Nunchuck Repository

- `README.md:1-104` — Repository overview and design philosophy
- `AGENTS.md:1-20` — Agent instructions and index file conventions
- `.SKILLS.md:1-33` — Skill descriptions and keywords
- `docs/design/specs/.INDEX.md:1-7` — Specification index
- `docs/design/determinism/03_DETERMINISM_FIRST_SUBJECTIVITY_LAST.md:1-9` — Core invariant

### 12.2 Existing Skillsets

- `skills/plan/README.md:1-144` — Plan skillset documentation
- `skills/plan/SKILL.md:1-24` — Plan orchestrator structure
- `skills/plan/plan-create/SKILL.md:1-29` — Member skill structure example
- `skills/doctor/SKILL.md:1-19` — Doctor skillset structure

### 12.3 Custom Files

- `CUSTOM_RULES/IMPLEMENTATION_SUMMARY.md:1-396` — Original implementation plan
- `CUSTOM_RULES/rules/research.md:1-228` — Research rule
- `CUSTOM_RULES/rules/plan.md:1-274` — Plan rule
- `CUSTOM_RULES/rules/implement.md:1-306` — Implement rule
- `CUSTOM_RULES/rules/review.md:1-271` — Review rule
- `CUSTOM_RULES/rules/algo-research.md:1-301` — Algorithm research rule
- `CUSTOM_RULES/rules/algo-plan.md:1-357` — Algorithm plan rule
- `CUSTOM_RULES/rules/algo-implement.md:1-406` — Algorithm implement rule
- `CUSTOM_RULES/rules/code-principles-guide.md:1-460` — Code principles
- `CUSTOM_RULES/workflows/research-plan-implement.md:1-153` — R-P-I workflow
- `CUSTOM_RULES/workflows/algo-research-plan-implement.md:1-210` — Algorithm workflow
- `CUSTOM_RULES/workflows/update-memory-bank.md:1-287` — Memory Bank workflow
- `CUSTOM_RULES/skills/code-review-cleanup/SKILL.md:1-353` — Code review skill

### 12.4 External References

- AI Coding Best Practices Research Summary (provided by user) — Windsurf feature comparison and skill specifications
