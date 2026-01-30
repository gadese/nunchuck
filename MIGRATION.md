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
