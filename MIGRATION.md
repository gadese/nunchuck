<<<<<<< HEAD
# Migration Guide: CUSTOM_RULES to Nunchuck Skills

This guide documents the migration from `CUSTOM_RULES/` to nunchuck-compliant skills in `skills/`.

## Command Mapping

### Research-Plan-Implement Workflow

| Old Command | New Command | Description |
|-------------|-------------|-------------|
| `@research` | `/rpi-research` | Codebase research and documentation |
| `@plan` | `/rpi-plan` | Technical planning |
| `@implement` | `/rpi-implement` | Plan execution |
| `@review` | `/code-review` | Code quality review |
| N/A | `/rpi` | Full R-P-I orchestrator |

### Algorithm Workflow

| Old Command | New Command | Description |
|-------------|-------------|-------------|
| `@algo-research` | `/algo-rpi-research` | Algorithm problem research |
| `@algo-plan` | `/algo-rpi-plan` | Algorithm planning (P0-P5) |
| `@algo-implement` | `/algo-rpi-implement` | Algorithm implementation |
| N/A | `/algo-rpi` | Full algo R-P-I orchestrator |

### Standalone Skills

| Old Command | New Command | Description |
|-------------|-------------|-------------|
| N/A | `/commit-message` | Generate conventional commit messages |
| `@update-memory-bank` | `/memory-bank` | Manage Memory Bank files |
| `/doctor` | `/doctor` | Diagnostic protocol (unchanged) |

### Removed Skills

The following skills were removed as they overlapped with new skillsets or were not relevant:

- `changelog` — Release management
- `sniff` — Code smell detection (overlaps with code-review)
- `prompt` — Prompt forging workflow
- `md` — Markdown document workflows
- `task` — Overlaps with plan
- `dtx` — Context management (overlaps with Memory Bank)
- `grape` — Codebase search (covered in research)
- `plan` — Replaced by `rpi` skillset

## Key Changes

### 1. Clarifying Questions Required

**Research and Plan phases now MUST ask clarifying questions before proceeding:**

- `/rpi-research` and `/rpi-plan` will ask questions when scope is ambiguous
- `/algo-rpi-research` and `/algo-rpi-plan` will confirm problem constraints and approach selection
- Only proceed directly if the request is narrowly defined and unambiguous

### 2. Pause Points Between Phases

**User approval required between ALL phases:**

- ⏸️ After Research: Present findings, wait for approval
- ⏸️ After Plan: Present plan structure, wait for approval
- ⏸️ After Implement: Present implementation summary, wait for approval
- ⏸️ After Code-Review: Present review summary, offer commit-message

### 3. Code-Review Scoping

**Code-review now ONLY reviews modified or specified files:**

- Uses `git diff --name-only` to identify modified files
- Or reviews files explicitly specified by user
- NEVER reviews entire codebase unless explicitly requested
- Asks for clarification if no files are specified and no recent modifications exist

### 4. Centralized Coding Standards

**New `coding-standards` skillset:**

- Not invoked directly (reference-only)
- Accessed via `.shared/` symlinks in other skillsets
- Contains: code-principles.md, code-style.md, ml-dl-guide.md, data-science-guide.md
- Referenced by: `rpi`, `algo-rpi`, `code-review`, `doctor`

### 5. Memory Bank Integration

**Memory Bank now a standalone skill:**

- Invoke with `/memory-bank` to update workspace context
- Automatically integrated with R-P-I workflows
- Manages 7 core files in `llm_docs/memory/`
- Global skill usable across multiple workspaces

## Workflow Integration

### Full R-P-I Workflow

```
/rpi
  ↓
Research Phase → ⏸️ User Approval
  ↓
Plan Phase → ⏸️ User Approval
  ↓
Implement Phase → ⏸️ User Approval
  ↓
/code-review → ⏸️ User Approval
  ↓
/commit-message (optional)
```

### Algorithm Workflow

```
/algo-rpi
  ↓
Research Phase (with algorithm formalization) → ⏸️ User Approval
  ↓
Plan Phase (P0-P5 phases) → ⏸️ User Approval
  ↓
Implement Phase (with metrics) → ⏸️ User Approval (per phase)
  ↓
/code-review → ⏸️ User Approval
  ↓
/commit-message (optional)
```

### Doctor Integration

```
/rpi-implement → encounters error
  ↓
/doctor → diagnose → produce treatment plan
  ↓
Return to /rpi-implement with fixes
```

## File Structure Changes

### Old Structure (CUSTOM_RULES/)

```
CUSTOM_RULES/
├── rules/
│   ├── research.md
│   ├── plan.md
│   ├── implement.md
│   ├── review.md
│   ├── algo-research.md
│   ├── algo-plan.md
│   ├── algo-implement.md
│   ├── code-principles-guide.md
│   ├── code-style-guide.md
│   ├── machine-deep-learning-guide.md
│   ├── data-science-pandas-guide.md
│   └── memory-bank-protocol.md
├── workflows/
│   ├── research-plan-implement.md
│   ├── algo-full-cycle.md
│   └── update-memory-bank.md
└── skills/
    └── code-review-cleanup/
```

### New Structure (skills/)

```
skills/
├── coding-standards/          # NEW: Centralized guidelines
│   ├── SKILL.md
│   ├── README.md
│   └── references/
│       ├── code-principles.md
│       ├── code-style.md
│       ├── ml-dl-guide.md
│       └── data-science-guide.md
├── rpi/                       # NEW: Generic R-P-I
│   ├── SKILL.md
│   ├── README.md
│   ├── .pipelines/
│   ├── .shared/ → ../coding-standards/references
│   ├── rpi-research/
│   ├── rpi-plan/
│   └── rpi-implement/
├── algo-rpi/                  # NEW: Algorithm R-P-I
│   ├── SKILL.md
│   ├── README.md
│   ├── .pipelines/
│   ├── .shared/ → ../coding-standards/references
│   ├── algo-rpi-research/
│   ├── algo-rpi-plan/
│   └── algo-rpi-implement/
├── code-review/               # UPDATED: Scoped review
│   ├── SKILL.md
│   ├── README.md
│   ├── .shared/ → ../coding-standards/references
│   └── references/
├── commit-message/            # NEW: Commit message generation
│   ├── SKILL.md
│   ├── README.md
│   └── references/
├── memory-bank/               # NEW: Memory Bank management
│   ├── SKILL.md
│   ├── README.md
│   └── references/
└── doctor/                    # UPDATED: R-P-I integration
    ├── SKILL.md
    ├── README.md
    ├── .shared/ → ../coding-standards/references
    └── references/
```

## Breaking Changes

1. **No more XML-tag format** — All skills now use nunchuck 7-file reference structure
2. **Mandatory pause points** — Cannot skip phase approvals in workflows
3. **Clarifying questions required** — Research and plan phases must ask questions when scope is unclear
4. **Code-review scoping** — No longer reviews entire codebase by default
5. **Removed skillsets** — 8 skillsets removed (see table above)

## Migration Checklist

- [x] All CUSTOM_RULES content converted to nunchuck skills
- [x] Workflows generated for all new skillsets
- [x] `.SKILLS.md` index updated
- [x] Adapter scripts updated to exclude `coding-standards`
- [x] Doctor integrated with R-P-I workflows
- [x] Memory Bank converted to standalone skill
- [x] Code-review scoped to modified files
- [x] Clarifying questions added to research/plan skills
- [x] Pause points documented in all workflows

## Next Steps

1. Test each workflow manually to verify behavior
2. Verify pause points function correctly
3. Confirm clarifying questions are asked appropriately
4. Test code-review file scoping
5. Archive or remove `CUSTOM_RULES/` directory

## Questions?

See the individual skill README files for detailed usage:
- `skills/rpi/README.md`
- `skills/algo-rpi/README.md`
- `skills/code-review/README.md`
- `skills/commit-message/README.md`
- `skills/memory-bank/README.md`
- `skills/doctor/README.md`
=======
# Migration Prompt: Flatten Skillsets into Standalone Skills

## Purpose

Migrate an existing **skillset-based implementation** into a set of **standalone, explicit skills** that align with the project’s design principles.

This migration is structural, not feature-driven.
The goal is to **remove implicit orchestration, hidden state, and centralized abstractions**, while preserving all meaningful behavior.

---

## What You Are Migrating Away From

The existing implementation likely includes some or all of the following:

* A top-level **skillset orchestrator** (`SKILL.md`) that:

  * routes to member skills
  * defines pipelines
  * encodes control flow
* Shared directories such as:

  * `.shared/`
  * `.pipelines/`
  * shared scripts or schemas
* CLI-style abstractions:

  * command routers
  * subcommands
  * “do-everything” entrypoints
* Nested READMEs scattered across subdirectories

These patterns **violate core design principles** by:

* centralizing responsibility
* hiding control flow
* encouraging implicit state
* coupling unrelated behaviors

---

## Target End State (Authoritative)

After migration:

* There is **no skillset orchestrator**
* Each skill is:

  * independently invokable
  * self-contained
  * responsible for exactly one conceptual action
* All deterministic logic lives **inside the skill that owns it**
* Disk state (if any) is:

  * explicit
  * documented
  * located relative to the project root
* Documentation is **flattened and discoverable**

---

## Recommended Execution Model (Staged)

A safe migration is usually done in two phases:

1. **Migration pass (non-destructive)**

    - Migrate deterministic scripts and reference docs into their respective standalone skills.
    - Update all documented usage to point at the standalone skills.
    - The legacy orchestrator (`SKILL.md`, `.pipelines/`, `.shared/`, and router scripts) may temporarily remain in the repo, but must be treated as **deprecated** and **non-authoritative**.

2. **Cleanup pass (destructive)**

    - Delete the orchestrator artifacts only after verifying nothing still depends on them.

---

## Required Migration Steps

### 1. Decommission the skillset orchestrator

**Authoritative end state:**

* the top-level `SKILL.md` that represents the skillset is no longer an orchestrator
* any `.pipelines/` directory is removed
* any `.shared/` directory is removed

During the migration pass, these artifacts may temporarily remain, but only if:

* they are clearly marked **deprecated**
* all references and usage docs point to the standalone skills
* the old orchestrator is not required for normal use

There must be **no parent skill** coordinating child skills once the migration is complete.

Each former member skill becomes a **first-class skill**.

> Control flow must be explicit, not inferred.

---

### 2. Eliminate CLI-style command routers

**Replace (and then delete):**

* wrapper scripts
* command dispatchers
* “one script, many commands” patterns

Each skill invocation replaces one former CLI command.

Mapping example:

| Old Pattern     | New Pattern                     |
| --------------- | ------------------------------- |
| `skill status`  | `skill-forge` (read-only check) |
| `skill exec`    | `skill-exec`                    |
| `skill compile` | `skill-compile`                 |

Skills must not multiplex behavior.

During the migration pass, a legacy router may temporarily remain in place for compatibility, but it must be treated as **deprecated** and **non-authoritative**.

---

### 3. Isolate scripts per skill

For each skill:

* Move only the logic that skill needs into its own `scripts/` directory
* Remove all shared script folders
* Duplicate small helpers if necessary (prefer clarity over DRY)

Required invariant:

> **Each script answers to exactly one skill.**

---

### 4. Fix disk state and path resolution

If the system uses disk state:

* State must live in a **clearly documented, canonical location**
* Paths must resolve relative to:

  * the project root
  * or the invocation working directory
* Scripts must not rely on:

  * `cd` tricks
  * implementation-relative paths
  * hidden directories inside skill code

Conversation must never be treated as durable state.

---

### 5. Clarify lifecycle semantics explicitly

You must document and enforce:

* what artifacts are authoritative
* what artifacts are derived
* which skills mutate state
* which skills are read-only
* which operations are destructive

If multiple artifacts exist, define their roles clearly, for example:

> Manifest is truth.
> Compiled output is a view.
> Receipts are history.

Lifecycle ambiguity is a design bug.

---

### 6. Flatten documentation into a single README

**Required change:**

* Remove all nested `README.md` files inside subdirectories
* Create **one README.md** at the **containing directory root**
* That README must:

  * explain the purpose of the skills
  * describe the mental model
  * explain how the skills relate
  * outline lifecycle and constraints

Skill-specific details belong in:

* `references/NN_*.md`
* not in nested READMEs

> One system, one README.

---

### 7. Reconcile docs with implementation

If documentation conflicts with behavior:

* **Implementation wins**
* Update or delete docs accordingly

Common fixes:

* normalize enum values (`draft` vs `drafting`)
* remove obsolete “Never” rules
* align lifecycle claims with actual deletion behavior

There must be **one source of truth** per rule.

---

## Verification Checklist (Before Cleanup)

Before deleting legacy orchestrator artifacts, verify:

* [ ] All deterministic scripts required for normal use are present under the standalone skills’ `scripts/` directories.
* [ ] All procedures and reference docs that instruct invocation use the standalone skills (not the legacy router).
* [ ] There are no remaining references to `.shared` router scripts or router Python CLIs in docs.
* [ ] Each standalone skill’s `scripts/skill.sh validate` (and/or `scripts/skill.ps1 validate`) passes.
* [ ] A repo-wide search for legacy invocations (e.g. `./skill.sh <subcommand>`) is empty or intentionally restricted to deprecated docs.

Only after these checks pass should you delete the orchestrator artifacts.

---

## What Must Not Change

You must preserve:

* core semantics of each skill
* irreversible actions where they exist
* explicit consent boundaries
* audit or receipt mechanisms
* existing guarantees relied upon by users

This is not a redesign unless explicitly requested.

---

## Acceptance Checklist (Must Pass)

* [ ] No top-level skillset or orchestrator remains
* [ ] No `.shared/` or `.pipelines/` directories remain
* [ ] No CLI command router remains
* [ ] Each skill owns its scripts
* [ ] Disk state is explicit and correctly rooted
* [ ] Lifecycle rules are documented and enforced
* [ ] Exactly one README exists at the root
* [ ] Documentation matches behavior

---

## Guiding Principle (Include Verbatim)

> **Make state explicit.
> Make control flow visible.
> Make irreversible actions deliberate.**
>>>>>>> master
