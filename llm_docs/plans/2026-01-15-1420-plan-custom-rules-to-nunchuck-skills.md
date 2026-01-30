# Implementation Plan — Convert CUSTOM_RULES to Nunchuck-Style Skills

**Tags:** `skills`, `skillsets`, `workflows`, `refactoring`, `integration`

## 1. Overview

Convert the custom R-P-I workflow files in `CUSTOM_RULES/` to nunchuck-compliant skills in `skills/`, creating multiple standalone skillsets that generate IDE workflows. This conversion enables modular invocation, clear documentation, and integration with existing nunchuck tooling.

## 2. Current State Summary

**Source:** `CUSTOM_RULES/`
- `rules/` — 12 rule files (XML-tag based format)
- `workflows/` — 3 orchestrator workflows
- `skills/code-review-cleanup/` — 1 existing skill

**Target:** `skills/`
- Nunchuck-compliant skillsets with SKILL.md frontmatter
- 7-file reference structure per member skill
- `.pipelines/` for workflow orchestration
- `.shared/` for common resources

## 3. Desired End State

Create the following skillsets and standalone skills:

| Skillset/Skill | Type | Workflow Commands | Purpose |
|----------------|------|-------------------|---------|
| `rpi` | Skillset | `/rpi`, `/rpi-research`, `/rpi-plan`, `/rpi-implement` | Generic R-P-I workflow |
| `algo-rpi` | Skillset | `/algo-rpi`, `/algo-rpi-research`, `/algo-rpi-plan`, `/algo-rpi-implement` | Algorithm-specific R-P-I |
| `code-review` | Standalone | `/code-review` | Code quality review & cleanup |
| `commit-message` | Standalone | `/commit-message` | Generate descriptive commit messages |
| `memory-bank` | Standalone | `/memory-bank` | Manage workspace-specific memory files |
| `doctor` | Existing | `/doctor` | Diagnose failures (integrate with R-P-I) |
| `coding-standards` | Shared Skillset | (referenced, not invoked) | Code principles & style guides |

## 4. Key Design Decisions

- **Shared review skill:** Both `rpi` and `algo-rpi` use `/code-review` (not embedded)
- **Separate commit-message:** Standalone skill invoked after code review
- **Global Memory Bank skill:** Manages workspace-specific `llm_docs/memory/` folders
- **Doctor integration:** Existing `doctor` skillset enhanced with R-P-I integration docs
- **Centralized coding-standards:** Single `coding-standards` skillset referenced by `rpi`, `algo-rpi`, `code-review`, and `doctor` — avoids duplication
- **Clarifying questions:** Research and Plan phases MUST ask clarifying questions before proceeding
- **Pause points:** User approval required between ALL phases in workflows
- **Scoped code-review:** Only reviews modified or explicitly specified files

## 5. Out of Scope

- Creating new index generators
- Changing Memory Bank file structure (only skill to manage it)
- Modifying core nunchuck design specifications

---

## 6. Implementation Phases

### Phase 0: Remove Unnecessary Skillsets & Files
**Complexity:** M

**Objective:** Remove existing nunchuck skillsets that are not relevant to the R-P-I workflows, reducing clutter and maintenance burden.

**Skillsets to REMOVE:**

| Skillset | Reason for Removal |
|----------|-------------------|
| `changelog` | Release management, not relevant to AI implementation |
| `sniff` | Code smell detection, overlaps with code-review |
| `prompt` | Prompt forging workflow, not relevant |
| `md` | Markdown document workflows, not relevant |
| `task` | Overlaps with plan, simpler but less structured |
| `dtx` | Context management overlaps with Memory Bank |
| `grape` | Codebase search covered in research skills |
| `plan` | Replaced by `rpi` skillset |

**Skillsets to KEEP:**

| Skillset | Reason to Keep |
|----------|---------------|
| `doctor` | Useful for debugging, integrates with R-P-I |

**Files to REMOVE:**
- `skills/changelog/` — entire directory
- `skills/sniff/` — entire directory
- `skills/prompt/` — entire directory
- `skills/md/` — entire directory
- `skills/task/` — entire directory
- `skills/dtx/` — entire directory
- `skills/grape/` — entire directory
- `skills/plan/` — entire directory
- `.windsurf/workflows/` — all generated workflows for removed skillsets
- `.cursor/commands/` — all generated commands for removed skillsets

**Implementation Steps:**
1. Backup current `skills/` directory (optional, git history preserves)
2. Remove each skillset directory listed above
3. Remove corresponding generated workflows in `.windsurf/workflows/`
4. Remove corresponding generated commands in `.cursor/commands/`
5. Update `.SKILLS.md` index to remove deleted entries
6. Verify `doctor` skillset remains intact

**Success Criteria:**
- [x] All listed skillsets removed
- [x] Only `doctor/` remains in `skills/` (before new skillsets added)
- [x] Generated workflows cleaned up
- [x] No broken references in remaining files

**Dependencies:** None

**⏸️ PAUSE POINT:** Present removal summary to user. Get explicit approval before Phase 1.

---

### Phase 1: Directory Structure Setup
**Complexity:** S

**Objective:** Create directory scaffolding for all new skillsets and skills.

**Deliverables:**
```
skills/
├── coding-standards/              # NEW: Shared skillset for code guidelines
│   ├── SKILL.md
│   ├── README.md
│   └── references/
│       ├── code-principles.md
│       ├── code-style.md
│       ├── ml-dl-guide.md
│       └── data-science-guide.md
├── rpi/
│   ├── SKILL.md
│   ├── README.md
│   ├── .pipelines/
│   │   └── .INDEX.md
│   ├── .shared/                   # Symlink or reference to coding-standards
│   ├── rpi-research/
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   └── references/
│   ├── rpi-plan/
│   │   └── [same structure]
│   └── rpi-implement/
│       └── [same structure]
├── algo-rpi/
│   ├── SKILL.md
│   ├── README.md
│   ├── .pipelines/
│   ├── .shared/                   # Symlink or reference to coding-standards
│   ├── algo-rpi-research/
│   ├── algo-rpi-plan/
│   └── algo-rpi-implement/
├── code-review/
│   ├── SKILL.md
│   ├── README.md
│   ├── .shared/                   # Symlink or reference to coding-standards
│   └── references/
├── commit-message/
│   ├── SKILL.md
│   ├── README.md
│   └── references/
├── memory-bank/
│   ├── SKILL.md
│   ├── README.md
│   └── references/
└── doctor/                        # EXISTING: Keep and update
    ├── .shared/                   # Add symlink or reference to coding-standards
    └── [existing structure]
```

**Implementation Steps:**
1. Create `skills/coding-standards/` directory with references/
2. Create `skills/rpi/` directory with subdirectories
3. Create `skills/algo-rpi/` directory with subdirectories
4. Create `skills/code-review/` directory with .shared/
5. Create `skills/commit-message/` directory
6. Create `skills/memory-bank/` directory
7. Create empty `.INDEX.md` files in `.pipelines/` directories
8. Add `.shared/` symlinks in `rpi/`, `algo-rpi/`, `code-review/` pointing to `coding-standards/references/`
9. Add `.shared/` symlink in existing `doctor/` pointing to `coding-standards/references/`

**Success Criteria:**
- [x] All directories exist with correct structure
- [x] Empty placeholder files created
- [x] `.shared/` symlinks functional
- [x] `coding-standards/` directory created

**Dependencies:** Phase 0

---

### Phase 2: Coding-Standards Skillset
**Complexity:** M

**Objective:** Create centralized coding-standards skillset that other skillsets reference. This avoids duplicating guidelines across `rpi`, `algo-rpi`, `code-review`, and `doctor`.

**Source Files:**
- `CUSTOM_RULES/rules/code-principles-guide.md`
- `CUSTOM_RULES/rules/code-style-guide.md`
- `CUSTOM_RULES/rules/machine-deep-learning-guide.md`
- `CUSTOM_RULES/rules/data-science-pandas-guide.md`

**Deliverables:**
- `skills/coding-standards/SKILL.md` — Skillset definition
- `skills/coding-standards/README.md` — Usage documentation
- `skills/coding-standards/references/code-principles.md`
- `skills/coding-standards/references/code-style.md`
- `skills/coding-standards/references/ml-dl-guide.md`
- `skills/coding-standards/references/data-science-guide.md`

**Implementation Steps:**

1. **Create SKILL.md:**
   ```yaml
   ---
   name: coding-standards
   license: MIT
   description: >
     Centralized code principles and style guidelines. Referenced by rpi,
     algo-rpi, code-review, and doctor skillsets. Not invoked directly.
   metadata:
     author: [Author]
     version: 0.1.0
     references:
       - code-principles.md
       - code-style.md
       - ml-dl-guide.md
       - data-science-guide.md
     keywords:
       - code
       - style
       - principles
       - guidelines
       - standards
   ---
   
   # INSTRUCTIONS
   
   This skillset is referenced by other skillsets, not invoked directly.
   See `metadata.references` for available guidelines.
   ```

2. **Copy and convert source files:**
   - `code-principles-guide.md` → `references/code-principles.md`
     - Remove YAML frontmatter (`trigger: always_on`)
     - Keep content as-is
   - `code-style-guide.md` → `references/code-style.md`
   - `machine-deep-learning-guide.md` → `references/ml-dl-guide.md`
   - `data-science-pandas-guide.md` → `references/data-science-guide.md`

3. **Create README.md:**
   - Purpose: Single source of truth for coding guidelines
   - How to reference from other skillsets
   - When each guide applies (always-on vs model_decision)

4. **Update symlinks in other skillsets:**
   - Ensure `.shared/` in `rpi/`, `algo-rpi/`, `code-review/`, `doctor/` point to `coding-standards/references/`

**Success Criteria:**
- [x] `coding-standards/` skillset complete
- [x] All 4 guide files converted (frontmatter removed)
- [x] Symlinks verified functional
- [x] No duplication across skillsets

**Dependencies:** Phase 1

---

### Phase 3: RPI Skillset — Member Skills
**Complexity:** L

**Objective:** Convert generic R-P-I rules to nunchuck member skills with 7-file reference structure.

**Source → Target Mapping:**

| Source | Target Skill | References to Create |
|--------|--------------|---------------------|
| `rules/research.md` | `rpi/rpi-research/` | 00-06 reference files |
| `rules/plan.md` | `rpi/rpi-plan/` | 00-06 reference files |
| `rules/implement.md` | `rpi/rpi-implement/` | 00-06 reference files |

**Content Mapping Per Skill:**

| Source Section | Target Reference File |
|----------------|----------------------|
| `<system_context>` + `<role>` | `01_SUMMARY.md` |
| `<invocation_behavior>` + `<invocation_response>` | `02_TRIGGERS.md` |
| `<critical_constraints>` "YOU MUST" | `03_ALWAYS.md` |
| `<critical_constraints>` "YOU MUST NOT" | `04_NEVER.md` |
| `<process>` + `<clarification_protocol>` | `05_PROCEDURE.md` |
| `<handoff>` + error handling | `06_FAILURES.md` |
| Router logic | `00_ROUTER.md` |

**CRITICAL REQUIREMENTS for Research & Plan Skills:**

> **rpi-research and rpi-plan MUST:**
> - Ask clarifying questions BEFORE proceeding with any analysis or document generation
> - Wait for user answers before continuing
> - Only proceed directly if the request is narrowly defined and unambiguous

This requirement must be explicitly documented in:
- `02_TRIGGERS.md` — Define when clarification is needed
- `05_PROCEDURE.md` — First step must be clarification protocol
- `03_ALWAYS.md` — "Ask clarifying questions when scope is ambiguous"

**Implementation Steps for Each Skill (rpi-research, rpi-plan, rpi-implement):**

1. **Create SKILL.md frontmatter:**
   ```yaml
   ---
   name: rpi-research
   license: MIT
   description: >
     Descriptive codebase research for the Research-Plan-Implement workflow.
     Produces technical documentation about current system state.
   metadata:
     author: [Author]
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

2. **Create 00_ROUTER.md:**
   - Default route: read all references in order
   - No special preconditions

3. **Create 01_SUMMARY.md:**
   - Extract from `<system_context>` and `<role>` sections
   - Brief description of agent role and purpose

4. **Create 02_TRIGGERS.md:**
   - Extract from `<invocation_behavior>` and `<invocation_response>`
   - When to invoke, expected inputs, response format

5. **Create 03_ALWAYS.md:**
   - Extract "YOU MUST" items from `<critical_constraints>`
   - Format as bullet list of imperatives

6. **Create 04_NEVER.md:**
   - Extract "YOU MUST NOT" items from `<critical_constraints>`
   - Format as bullet list of prohibitions

7. **Create 05_PROCEDURE.md:**
   - Extract from `<process>` section
   - **IMPORTANT for rpi-research and rpi-plan:** First step MUST be clarification protocol
   - Include `<clarification_protocol>` content prominently
   - Include `<output_format>` templates
   - Step-by-step procedure with completion signals
   - Add explicit "⏸️ PAUSE: Wait for user confirmation" markers

8. **Create 06_FAILURES.md:**
   - Extract from `<handoff>` section
   - Add failure modes and recovery procedures
   - Define artifact validation

9. **Create README.md:**
   - Human-readable description
   - Quick reference for when to use
   - Example invocation

**Success Criteria:**
- [x] `rpi-research/` complete with all 7 reference files + SKILL.md + README.md
- [x] `rpi-plan/` complete with all 7 reference files + SKILL.md + README.md
- [x] `rpi-implement/` complete with all 7 reference files + SKILL.md + README.md
- [x] Content accurately converted from XML-tag format
- [x] References to Memory Bank preserved
- [x] **rpi-research and rpi-plan have clarification protocol as first procedure step**
- [x] **Pause points documented in procedures**

**Dependencies:** Phase 1, Phase 2

**⏸️ PAUSE POINT:** Present completed member skills to user. Get approval before Phase 4.

---

### Phase 4: RPI Skillset — Orchestrator & Pipelines
**Complexity:** M

**Objective:** Create RPI skillset orchestrator and pipeline definitions.

**Source:** `CUSTOM_RULES/workflows/research-plan-implement.md`

**Deliverables:**
- `skills/rpi/SKILL.md` — Orchestrator frontmatter
- `skills/rpi/README.md` — Skillset documentation
- `skills/rpi/.pipelines/.INDEX.md` — Pipeline index
- `skills/rpi/.pipelines/00_DEFAULT.md` — Full R-P-I workflow
- `skills/rpi/.pipelines/01_RESEARCH_ONLY.md` — Research phase only
- `skills/rpi/.pipelines/02_PLAN_ONLY.md` — Plan phase only
- `skills/rpi/.pipelines/03_IMPLEMENT_ONLY.md` — Implement phase only

**Implementation Steps:**

1. **Create orchestrator SKILL.md:**
   ```yaml
   ---
   name: rpi
   description: >
     Orchestrator skill for the `rpi` skillset. Manages the Research-Plan-Implement
     workflow for general software development tasks.
   metadata:
     author: [Author]
     version: 0.1.0
     skillset:
       name: rpi
       schema_version: 1
       skills:
         - rpi-research
         - rpi-plan
         - rpi-implement
       shared:
         root: .shared
   ---
   
   # INSTRUCTIONS
   
   1. Refer to `.pipelines/.INDEX.md`.
   ```

2. **Create .pipelines/.INDEX.md:**
   - List all available pipelines
   - Brief description of each

3. **Create 00_DEFAULT.md pipeline:**
   - Full R-P-I workflow: Research → Plan → Implement → (invoke /code-review) → (invoke /commit-message)
   - **MANDATORY PAUSE POINTS:**
     - ⏸️ After Research: Present findings, wait for user approval
     - ⏸️ After Plan: Present plan structure, wait for user approval
     - ⏸️ After Implement: Present implementation summary, wait for user approval
     - ⏸️ After Code-Review: Present review summary, offer /commit-message
   - Memory Bank integration at each phase

4. **Create individual phase pipelines** (01, 02, 03)

5. **Create README.md:**
   - Overview of R-P-I workflow
   - When to use generic vs algorithm-specific
   - Quick start guide
   - Integration with /code-review and /commit-message

**Success Criteria:**
- [x] Orchestrator SKILL.md valid
- [x] All pipelines documented with pause points
- [x] README provides clear usage guidance
- [x] Integration with /code-review and /commit-message documented
- [x] **Each phase transition requires user approval**

**Dependencies:** Phase 3

**⏸️ PAUSE POINT:** Present orchestrator and pipelines to user. Get approval before Phase 5.

---

### Phase 5: Algo-RPI Skillset — Member Skills
**Complexity:** L

**Objective:** Convert algorithm-specific rules to nunchuck member skills.

**Source → Target Mapping:**

| Source | Target Skill |
|--------|--------------|
| `rules/algo-research.md` | `algo-rpi/algo-rpi-research/` |
| `rules/algo-plan.md` | `algo-rpi/algo-rpi-plan/` |
| `rules/algo-implement.md` | `algo-rpi/algo-rpi-implement/` |

**CRITICAL REQUIREMENTS for algo-rpi Research & Plan Skills:**

> **algo-rpi-research and algo-rpi-plan MUST:**
> - Ask clarifying questions BEFORE proceeding with any analysis or document generation
> - Wait for user answers before continuing
> - Only proceed directly if the request is narrowly defined and unambiguous
> - For algo-rpi-research: Clarify problem constraints, metrics, data characteristics, hardware limits
> - For algo-rpi-plan: Confirm selected approach from research before planning

**Implementation Steps:**
Same process as Phase 3, but for algorithm-specific content:

1. Create `algo-rpi-research/` with 7 reference files
   - Include algorithm formalization content
   - Include solution space exploration
   - Include candidate approach analysis
   - **First procedure step: Clarification protocol for problem constraints**

2. Create `algo-rpi-plan/` with 7 reference files
   - Include P0-P5 phase structure
   - Include quantitative targets
   - Include reproducibility requirements
   - **First procedure step: Confirm selected approach with user**

3. Create `algo-rpi-implement/` with 7 reference files
   - Include benchmarking requirements
   - Include performance gates
   - Include reproducibility verification

**Success Criteria:**
- [x] `algo-rpi-research/` complete
- [x] `algo-rpi-plan/` complete
- [x] `algo-rpi-implement/` complete
- [x] Algorithm-specific content preserved (P0-P5 phases, metrics, reproducibility)
- [x] **algo-rpi-research and algo-rpi-plan have clarification protocol as first procedure step**
- [x] **Pause points documented in procedures**

**Dependencies:** Phase 1, Phase 2

**⏸️ PAUSE POINT:** Present completed algo-rpi member skills to user. Get approval before Phase 6.

---

### Phase 6: Algo-RPI Skillset — Orchestrator & Pipelines
**Complexity:** M

**Objective:** Create algo-rpi skillset orchestrator and pipeline definitions.

**Source:** `CUSTOM_RULES/workflows/algo-full-cycle.md`

**Deliverables:**
- `skills/algo-rpi/SKILL.md`
- `skills/algo-rpi/README.md`
- `skills/algo-rpi/.pipelines/` — Pipeline definitions

**Implementation Steps:**
1. Create orchestrator SKILL.md with skillset metadata
2. Create pipeline index
3. Create default pipeline (full algo cycle → code-review → commit-message)
   - **MANDATORY PAUSE POINTS:**
     - ⏸️ After Research: Present candidate approaches, wait for user to select
     - ⏸️ After Plan: Present plan with quantitative targets, wait for approval
     - ⏸️ After each P0-P5 phase: Present metrics, wait for approval
     - ⏸️ After Code-Review: Present review summary, offer /commit-message
4. Create individual phase pipelines
5. Create README with:
   - When to use algo-rpi vs generic rpi
   - P0-P5 phase explanations
   - Reproducibility requirements
   - Integration with /code-review, /commit-message, and /doctor

**Success Criteria:**
- [x] Orchestrator valid
- [x] Pipelines documented with pause points
- [x] Clear differentiation from generic rpi
- [x] **Each phase transition requires user approval**

**Dependencies:** Phase 5

**⏸️ PAUSE POINT:** Present orchestrator and pipelines to user. Get approval before Phase 7.

---

### Phase 7: Code-Review Standalone Skill
**Complexity:** M

**Objective:** Create standalone code review skill that ONLY reviews modified or explicitly specified files.

**Sources:**
- `CUSTOM_RULES/rules/review.md`
- `CUSTOM_RULES/skills/code-review-cleanup/SKILL.md`

**Deliverables:**
- `skills/code-review/SKILL.md`
- `skills/code-review/README.md`
- `skills/code-review/references/00_ROUTER.md` through `06_FAILURES.md`
- `skills/code-review/.shared/` — symlink to `coding-standards/references/`

**CRITICAL REQUIREMENT: File Scope**

> **code-review MUST:**
> - Only review files that were modified (use `git diff --name-only` or similar)
> - Or review files explicitly specified by the user
> - NEVER review the entire codebase unless explicitly requested
> - Ask for clarification if no files are specified and no recent modifications exist

**Implementation Steps:**

1. **Create SKILL.md:**
   ```yaml
   ---
   name: code-review
   license: MIT
   description: >
     Systematic code review and cleanup skill. Reviews ONLY modified or
     specified files for quality, adherence to guidelines, and best practices.
     Can be invoked standalone or as part of R-P-I workflows.
   metadata:
     author: [Author]
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
       - review
       - cleanup
       - quality
       - linting
       - testing
   ---
   
   # INSTRUCTIONS
   
   1. Refer to `metadata.references`.
   2. Reference `.shared/` for coding standards.
   ```

2. **Merge content from both sources:**
   - `review.md` provides the agent role and process
   - `code-review-cleanup/SKILL.md` provides detailed checklists

3. **Create reference files:**
   - `01_SUMMARY.md` — Code quality guardian role
   - `02_TRIGGERS.md` — When to invoke (after implementation, before commit)
     - **Specify: Must identify target files first**
   - `03_ALWAYS.md`:
     - **Identify target files FIRST (modified or specified)**
     - Run automated checks on target files only
     - Fix issues in target files
     - Reference `.shared/` coding standards
     - Update Memory Bank
   - `04_NEVER.md`:
     - **Don't review entire codebase unless explicitly requested**
     - Don't add features
     - Don't skip tests
     - Don't approve failing code
   - `05_PROCEDURE.md`:
     - **Step 1: Identify files to review**
       - If invoked after implementation: Use files from plan
       - If invoked standalone: Use `git diff --name-only` or ask user
     - Step 2: Run automated checks on identified files
     - Step 3: Manual review using checklists
     - Step 4: Fix issues
     - Step 5: Verify fixes
     - Step 6: Summary report
   - `06_FAILURES.md` — What to do if checks fail

4. **Create README.md:**
   - Standalone usage (specify files or use git diff)
   - Integration with R-P-I workflows (files from plan)
   - Checklist reference
   - Reference to coding-standards

**Success Criteria:**
- [x] Complete skill with all reference files
- [x] Merges content from both source files
- [x] **Procedure clearly scopes to modified/specified files only**
- [x] `.shared/` symlink to coding-standards
- [x] Clear documentation on standalone vs integrated use
- [ ] Generates `/code-review` workflow

**Dependencies:** Phase 1, Phase 2

**⏸️ PAUSE POINT:** Present code-review skill to user. Get approval before Phase 8.

---

### Phase 8: Commit-Message Standalone Skill
**Complexity:** S

**Objective:** Create new standalone skill for generating descriptive commit messages.

**Deliverables:**
- `skills/commit-message/SKILL.md`
- `skills/commit-message/README.md`
- `skills/commit-message/references/` — 7 reference files

**Implementation Steps:**

1. **Create SKILL.md:**
   ```yaml
   ---
   name: commit-message
   license: MIT
   description: >
     Generate descriptive, conventional commit messages based on code changes.
     Analyzes staged changes and produces clear, informative commit messages.
   metadata:
     author: [Author]
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
       - commit
       - message
       - git
       - conventional
   ---
   
   # INSTRUCTIONS
   
   1. Refer to `metadata.references`.
   ```

2. **Create reference files:**
   - `01_SUMMARY.md` — Purpose: generate clear commit messages
   - `02_TRIGGERS.md` — After code-review, before git commit
   - `03_ALWAYS.md`:
     - Analyze actual changes (git diff --staged)
     - Use conventional commit format
     - Be specific about what changed and why
     - Keep subject line under 72 characters
   - `04_NEVER.md`:
     - Don't use generic messages ("fix bug", "update code")
     - Don't include implementation details in subject
     - Don't commit without user confirmation
   - `05_PROCEDURE.md`:
     1. Read staged changes (`git diff --staged`)
     2. Identify change type (feat, fix, refactor, docs, test, chore)
     3. Summarize primary change in subject line
     4. Add body with details if needed
     5. Present to user for confirmation
     6. Execute commit or allow user to modify
   - `06_FAILURES.md` — Handle no staged changes, conflicts

3. **Create README.md:**
   - Conventional commit format reference
   - Example outputs
   - Integration with code-review

**Success Criteria:**
- [x] Complete skill with all reference files
- [x] Clear procedure for analyzing changes
- [x] Conventional commit format documented
- [ ] Generates `/commit-message` workflow

**Dependencies:** Phase 1

**⏸️ PAUSE POINT:** Present commit-message skill to user. Get approval before Phase 9.

---

### Phase 9: Memory-Bank Standalone Skill
**Complexity:** M

**Objective:** Create global skill for managing workspace-specific Memory Bank files.

**Sources:**
- `CUSTOM_RULES/rules/memory-bank-protocol.md`
- `CUSTOM_RULES/workflows/update-memory-bank.md`

**Deliverables:**
- `skills/memory-bank/SKILL.md`
- `skills/memory-bank/README.md`
- `skills/memory-bank/references/` — 7 reference files

**Implementation Steps:**

1. **Create SKILL.md:**
   ```yaml
   ---
   name: memory-bank
   license: MIT
   description: >
     Manages workspace-specific Memory Bank files in `llm_docs/memory/`.
     Provides persistent cross-session context for AI agents. Global skill
     usable across multiple workspaces and projects.
   metadata:
     author: [Author]
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
       - memory
       - context
       - persistence
       - session
       - workspace
   ---
   
   # INSTRUCTIONS
   
   1. Refer to `metadata.references`.
   ```

2. **Create reference files from merged sources:**
   - `01_SUMMARY.md` — Memory Bank purpose and 7-file structure
   - `02_TRIGGERS.md`:
     - At start of every session (read)
     - After significant work (update)
     - At end of work sessions (update)
     - When context changes significantly
   - `03_ALWAYS.md`:
     - Read Memory Bank at session start
     - Update `activeContext.md` frequently
     - Maintain timestamps
     - Cross-reference between files
   - `04_NEVER.md`:
     - Don't skip reading at session start
     - Don't update for minor changes
     - Don't leave contradictory information
   - `05_PROCEDURE.md`:
     - Full update workflow (from `update-memory-bank.md`)
     - Quick update procedure
     - File-specific update guidelines
   - `06_FAILURES.md`:
     - Handle missing Memory Bank (initialize)
     - Handle corrupted files
     - Handle stale information

3. **Create README.md:**
   - Memory Bank file structure
   - When to read vs update
   - Integration with R-P-I workflows
   - Quick update vs full update

**Success Criteria:**
- [x] Complete skill with all reference files
- [x] Global skill (not workspace-specific)
- [x] Manages workspace-specific `llm_docs/memory/` folders
- [x] Clear integration with R-P-I documented
- [ ] Generates `/memory-bank` workflow

**Dependencies:** Phase 1

**⏸️ PAUSE POINT:** Present memory-bank skill to user. Get approval before Phase 10.

---

### Phase 10: Doctor Integration
**Complexity:** S

**Objective:** Update existing `doctor` skillset documentation to integrate with R-P-I workflows.

**Target:** `skills/doctor/`

**Implementation Steps:**

1. **Update README.md** to include:
   - When to invoke doctor during R-P-I
   - Integration points (rpi-implement failures, algo-rpi debugging)
   - Example: implementation fails → invoke /doctor → diagnose → return to implement

2. **Add to 02_TRIGGERS.md** (if not present):
   - During rpi-implement when unexpected errors occur
   - During algo-rpi-implement when tests fail
   - When debugging numerical stability issues

3. **Verify doctor references** mention R-P-I context where appropriate

**Success Criteria:**
- [x] README documents R-P-I integration
- [x] Triggers include R-P-I scenarios
- [x] Doctor remains standalone but aware of R-P-I context
- [x] `.shared/` symlink to coding-standards added

**Dependencies:** Phase 2 (coding-standards)

**⏸️ PAUSE POINT:** Present doctor integration updates to user. Get approval before Phase 11.

---

### Phase 11: Adapter Scripts Modification
**Complexity:** M

**Objective:** Update adapter scripts to work with the new skillsets and remove references to deleted skillsets.

**Target Files:**
- `scripts/adapters/windsurf/run.sh`
- `scripts/adapters/cursor/run.sh`
- `scripts/index/run.sh`

**Implementation Steps:**

1. **Review current adapter scripts:**
   - Understand how they process `skills/` directory
   - Identify any hardcoded references to removed skillsets
   - Identify any assumptions about skill structure

2. **Update Windsurf adapter (`scripts/adapters/windsurf/run.sh`):**
   - Ensure it correctly processes new skillsets (`rpi`, `algo-rpi`, `coding-standards`)
   - Ensure it handles standalone skills (`code-review`, `commit-message`, `memory-bank`)
   - Verify it ignores `coding-standards` (not invoked directly)
   - Update any hardcoded skill lists

3. **Update Cursor adapter (`scripts/adapters/cursor/run.sh`):**
   - Same updates as Windsurf adapter
   - Ensure command generation works for new skills

4. **Update index generator (`scripts/index/run.sh`):**
   - Ensure it correctly indexes new skillsets
   - Update `.SKILLS.md` generation logic if needed
   - Handle `coding-standards` as a referenced-only skillset

5. **Test adapter output:**
   - Run adapters and verify generated files
   - Check for errors or warnings
   - Validate output format matches expected structure

**Success Criteria:**
- [x] Windsurf adapter generates correct workflows for all new skills
- [x] Cursor adapter generates correct commands for all new skills
- [x] Index generator produces valid `.SKILLS.md`
- [x] No references to removed skillsets remain
- [x] `coding-standards` handled correctly (not generated as workflow)

**Dependencies:** Phases 0-10 (all skills created)

**⏸️ PAUSE POINT:** Present adapter modifications to user. Get approval before Phase 12.

---

### Phase 12: Workflow Generation & Validation
**Complexity:** M

**Objective:** Generate IDE workflows and validate all skills.

**Implementation Steps:**

1. **Run adapter scripts:**
   ```bash
   bash scripts/adapters/windsurf/run.sh --skills-root skills --output-root .
   bash scripts/adapters/cursor/run.sh --skills-root skills --output-root .
   ```

2. **Verify generated workflows in `.windsurf/workflows/`:**
   - `/rpi.md`
   - `/rpi-research.md`
   - `/rpi-plan.md`
   - `/rpi-implement.md`
   - `/algo-rpi.md`
   - `/algo-rpi-research.md`
   - `/algo-rpi-plan.md`
   - `/algo-rpi-implement.md`
   - `/code-review.md`
   - `/commit-message.md`
   - `/memory-bank.md`
   - `/doctor.md` (existing, verify still works)
   - **NO workflows for removed skillsets**
   - **NO workflow for `coding-standards` (reference only)**

3. **Verify generated commands in `.cursor/commands/`:**
   - Same list as workflows above

4. **Run index generator:**
   ```bash
   bash scripts/index/run.sh --skills-root skills
   ```

5. **Verify `.SKILLS.md` includes all new skills**

6. **Manual validation:**
   - Invoke each workflow and verify correct behavior
   - Test integration: `/rpi` → `/code-review` → `/commit-message`
   - Test Memory Bank integration
   - **Verify pause points work in workflows**
   - **Verify clarifying questions are asked in research/plan skills**
   - **Verify code-review only targets specified files**

**Success Criteria:**
- [x] All 12 workflows generated (not including coding-standards)
- [x] `.SKILLS.md` index updated
- [x] Integration flows work correctly
- [x] No errors in adapter/index scripts
- [ ] **Pause points functional** (requires manual testing)
- [ ] **Clarifying questions asked by research/plan skills** (requires manual testing)
- [ ] **Code-review scoped correctly** (requires manual testing)

**Dependencies:** Phase 11

**⏸️ PAUSE POINT:** Present validation results to user. Get approval before Phase 13.

---

### Phase 13: Cleanup & Documentation
**Complexity:** S

**Objective:** Clean up, document, and finalize the migration.

**Implementation Steps:**

1. **Update repository documentation:**
   - Update `README.md` with new skillsets overview
   - Update `docs/.INDEX.md` if needed
   - Update `AGENTS.md` if needed

2. **Create migration guide:**
   - Document mapping from old commands to new
   - `@research` → `/rpi-research`
   - `@plan` → `/rpi-plan`
   - `@implement` → `/rpi-implement`
   - `@review` → `/code-review`
   - `@algo-research` → `/algo-rpi-research`
   - etc.

3. **Archive CUSTOM_RULES:**
   - Move to `archive/CUSTOM_RULES/` or delete
   - Document decision in commit message

4. **Final validation:**
   - Run full test of each workflow
   - Verify all cross-references work
   - Ensure no broken links

**Success Criteria:**
- [x] Documentation updated
- [x] Migration guide created
- [x] CUSTOM_RULES archived or removed
- [x] All workflows functional

**Dependencies:** Phase 12

**⏸️ FINAL PAUSE:** Present completion summary to user. Get final approval.

---

## 7. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Content loss during conversion | HIGH | Carefully map all XML sections to reference files; review each conversion |
| Broken cross-references | MEDIUM | Validate all file paths after migration; run link checker |
| Workflow generation failures | MEDIUM | Test adapter scripts incrementally; fix SKILL.md format issues |
| Memory Bank integration gaps | MEDIUM | Ensure all procedures reference Memory Bank; test with actual workspace |
| Doctor integration incomplete | LOW | Doctor already standalone; minimal changes needed |

---

## 8. File Mapping Reference

### Source → Target Complete Mapping

| Source File | Target Location | Notes |
|-------------|-----------------|-------|
| `rules/research.md` | `skills/rpi/rpi-research/references/` | Split into 7 files |
| `rules/plan.md` | `skills/rpi/rpi-plan/references/` | Split into 7 files |
| `rules/implement.md` | `skills/rpi/rpi-implement/references/` | Split into 7 files |
| `rules/review.md` | `skills/code-review/references/` | Merge with code-review-cleanup |
| `rules/algo-research.md` | `skills/algo-rpi/algo-rpi-research/references/` | Split into 7 files |
| `rules/algo-plan.md` | `skills/algo-rpi/algo-rpi-plan/references/` | Split into 7 files |
| `rules/algo-implement.md` | `skills/algo-rpi/algo-rpi-implement/references/` | Split into 7 files |
| `rules/code-principles-guide.md` | `skills/coding-standards/references/code-principles.md` | Remove frontmatter, centralized |
| `rules/code-style-guide.md` | `skills/coding-standards/references/code-style.md` | Remove frontmatter, centralized |
| `rules/machine-deep-learning-guide.md` | `skills/coding-standards/references/ml-dl-guide.md` | Remove frontmatter, centralized |
| `rules/data-science-pandas-guide.md` | `skills/coding-standards/references/data-science-guide.md` | Remove frontmatter, centralized |
| `rules/memory-bank-protocol.md` | `skills/memory-bank/references/` | Split into 7 files |
| `workflows/research-plan-implement.md` | `skills/rpi/.pipelines/00_DEFAULT.md` | Convert to pipeline |
| `workflows/algo-full-cycle.md` | `skills/algo-rpi/.pipelines/00_DEFAULT.md` | Convert to pipeline |
| `workflows/update-memory-bank.md` | `skills/memory-bank/references/05_PROCEDURE.md` | Merge into procedure |
| `skills/code-review-cleanup/SKILL.md` | `skills/code-review/references/` | Merge with review.md |
| (new) | `skills/commit-message/` | New skill |

---

## 9. Generated Workflow Commands

| Command | Skillset/Skill | Purpose |
|---------|---------------|---------|
| `/rpi` | `rpi` orchestrator | Full generic R-P-I workflow |
| `/rpi-research` | `rpi/rpi-research` | Codebase research phase |
| `/rpi-plan` | `rpi/rpi-plan` | Technical planning phase |
| `/rpi-implement` | `rpi/rpi-implement` | Implementation phase |
| `/algo-rpi` | `algo-rpi` orchestrator | Full algorithm R-P-I workflow |
| `/algo-rpi-research` | `algo-rpi/algo-rpi-research` | Algorithm problem research |
| `/algo-rpi-plan` | `algo-rpi/algo-rpi-plan` | Algorithm planning (P0-P5) |
| `/algo-rpi-implement` | `algo-rpi/algo-rpi-implement` | Algorithm implementation |
| `/code-review` | `code-review` standalone | Code quality review & cleanup |
| `/commit-message` | `commit-message` standalone | Generate commit message |
| `/memory-bank` | `memory-bank` standalone | Update Memory Bank files |
| `/doctor` | `doctor` existing | Diagnose failures |

**NOT generated as workflow (reference only):**
| Skillset | Purpose |
|----------|---------|
| `coding-standards` | Centralized code guidelines, referenced via `.shared/` symlinks |

---

## 10. References

### Source Documents
- Research: `llm_docs/research/2026-01-15-1355-research-integration.md`
- CUSTOM_RULES implementation: `CUSTOM_RULES/IMPLEMENTATION_SUMMARY.md`

### Nunchuck Specifications
- Skill spec: `docs/design/specs/skillmd/.INDEX.md`
- Skillset spec: `docs/design/specs/skillset/.INDEX.md`
- References spec: `docs/design/specs/references/.INDEX.md`

### Example Skillsets
- `skills/plan/` — Skillset structure example
- `skills/doctor/` — Standalone skill example
- `skills/plan/plan-create/` — Member skill with references example
