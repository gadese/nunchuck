# Schema Documentation

This document provides comprehensive documentation of the schemas used in this repository, including the canonical `SKILL.md` frontmatter schema and the custom `SKILLSET` schema.

---

## Table of Contents

1. [SKILL.md Frontmatter Schema](#skillmd-frontmatter-schema)
2. [SKILLSET Schema](#skillset-schema)
3. [Plan Artifact Frontmatter Schema](#plan-artifact-frontmatter-schema)

---

## SKILL.md Frontmatter Schema

### Overview

**All `SKILL.md` files are strictly frontmatter** - they contain only YAML frontmatter with no Markdown body content. All instructions and documentation are referenced through the `metadata` field.

This intentional design decision keeps skill definitions clean and encourages progressive disclosure through reference files.

### Required Fields

#### `name`
- **Type:** String
- **Constraints:** 
  - 1-64 characters
  - Lowercase letters, numbers, and hyphens only
  - Must not start or end with hyphen
  - Must not contain consecutive hyphens
  - Must match parent directory name
- **Example:** `plan-create`

#### `description`
- **Type:** String (can use YAML multiline)
- **Constraints:** 
  - 1-1024 characters
  - Should describe what the skill does and when to use it
- **Example:**
  ```yaml
  description: >
    Materialize the current conversation into a new docs/planning/phase-N plan
    (root plan plus sub-plans and task files).
  ```

### Optional Fields

#### `license`
- **Type:** String
- **Purpose:** License identifier
- **Example:** `MIT`, `Apache-2.0`, `Proprietary`

#### `compatibility`
- **Type:** String
- **Constraints:** Max 500 characters
- **Purpose:** Environment requirements
- **Example:** `Requires git, docker, and internet access`

#### `allowed-tools`
- **Type:** String (space-delimited list)
- **Purpose:** Pre-approved tools (experimental)
- **Example:** `Bash(git:*) Bash(jq:*) Read`

#### `metadata`
- **Type:** Object
- **Purpose:** Additional metadata and skill resources
- **Fields:**
  - `author`: Author name or organization
  - `version`: Semantic version string
  - `references`: List of reference file paths
  - `scripts`: List of script file paths
  - `keywords`: List of keywords for discovery
  - `skillset`: Skillset configuration (for orchestrator skills only)

### Complete Example - Individual Skill

```yaml
---
name: plan-create
license: MIT
description: >
  Materialize the current conversation into a new docs/planning/phase-N plan
  (root plan plus sub-plans and task files).
metadata:
  author: Jordan Godau
  version: 0.1.0
  references:
    - 00_INSTRUCTIONS.md
    - 01_INTENT.md
    - 02_PRECONDITIONS.md
    - 03_SCRIPTS.md
    - 04_PROCEDURE.md
    - 05_TEMPLATES.md
    - 06_EDGE_CASES.md
  scripts:
    - dirs.ps1
    - dirs.sh
  keywords:
    - phase
    - plan
    - planning
    - task
    - draft
    - sketch
---
```

### Reference Files

Reference files are kept in a `references/` subdirectory and follow the naming pattern:
- Format: `<NN>_<TOPIC>.md`
- `<NN>`: Zero-padded sequential number (00, 01, 02, ...)
- `<TOPIC>`: Descriptive name in uppercase with underscores

**Example structure:**
```
skill-name/
├── SKILL.md
├── references/
│   ├── 00_INSTRUCTIONS.md
│   ├── 01_INTENT.md
│   ├── 02_PRECONDITIONS.md
│   └── 03_PROCEDURE.md
└── scripts/
    ├── script.sh
    └── script.ps1
```

### Scripts

Scripts should be:
- Listed in `metadata.scripts` array
- Stored in a `scripts/` subdirectory
- Available for both Unix (`.sh`) and Windows (`.ps1`) when possible
- Self-contained with clear error messages

---

## SKILLSET Schema

### Overview

The **SKILLSET** schema is a custom but strict extension to the standard `SKILL.md` format. It uses the `metadata.skillset` field to define orchestrator skills that coordinate multiple member skills.

**Key Points:**
- Maintains full spec compliance
- Creates no breaking changes
- Provides clear signaling to agents and users
- Member skills remain independently usable

### Schema Definition

```yaml
metadata:
  skillset:
    name: string                    # Required: Skillset identifier
    schema_version: integer         # Required: Currently 1
    skills: [string]                # Required: Member skill names
    resources:                      # Optional: Shared resources
      root: string                  # Resources directory path
      assets: [string]              # Shared asset files
      scripts: [string]             # Shared script files
      references: [string]          # Shared reference files
    pipelines:                      # Required: Execution pipelines
      default: [string]             # Default execution order
      allowed: [[string]]           # Valid skill sequences
    requires: [string]              # Optional: Dependencies (TBD)
```

### Field Descriptions

#### `name` (required)
- **Type:** String
- **Purpose:** Skillset identifier
- **Convention:** Should match the skill's `name` field

#### `schema_version` (required)
- **Type:** Integer
- **Current Value:** `1`
- **Purpose:** Schema version for future evolution

#### `skills` (required)
- **Type:** Array of strings
- **Purpose:** List of member skill names
- **Example:** `["plan-create", "plan-exec", "plan-status"]`

#### `resources` (optional)
- **Type:** Object
- **Purpose:** Define shared resources for member skills
- **Fields:**
  - `root`: Directory path (e.g., `.resources`)
  - `assets`: Array of asset file paths
  - `scripts`: Array of script file paths
  - `references`: Array of reference file paths

#### `pipelines` (required)
- **Type:** Object
- **Purpose:** Define how skills can be executed
- **Fields:**
  - `default`: Array defining default execution order
  - `allowed`: Array of arrays defining valid skill sequences

#### `requires` (optional)
- **Type:** Array of strings
- **Purpose:** Dependencies (implementation TBD)
- **Future Use:** System packages, environment variables, etc.

### Complete Example - Skillset

```yaml
---
name: plan
description: >
  Orchestrator skill for the `plan` skillset. Dispatches to member skills 
  in a safe, predictable order.
metadata:
  author: Jordan Godau
  version: 0.1.0

  # Strict structure (convention). Agents/tools may parse this.
  skillset:
    name: plan
    schema_version: 1
    skills:
      - plan-create
      - plan-exec
      - plan-status

    # Shared resources directory for skillset assets, scripts, and references
    resources:
      root: .resources
      assets: []
      scripts: []
      references: 
        - DEFINITIONS.md
        - FRONTMATTER.md

    # Chaining defaults/rules
    pipelines:
      default:
        - plan-create
        - plan-exec
      allowed:
        - [plan-exec]
        - [plan-create]
        - [plan-status]
        - [plan-create, plan-exec]

    # Dependencies assumed or provisioned (implementation TBD)
    requires: []

---
```

### Pipeline Patterns

#### Sequential Pipeline
Skills must run in order (one depends on the previous):
```yaml
pipelines:
  default:
    - skill-one
    - skill-two
    - skill-three
  allowed:
    - [skill-one, skill-two, skill-three]
    - [skill-one, skill-two]
    - [skill-one]
```

#### Flexible Pipeline
Skills can run in any combination:
```yaml
pipelines:
  default:
    - skill-a
    - skill-b
  allowed:
    - [skill-a]
    - [skill-b]
    - [skill-a, skill-b]
    - [skill-b, skill-a]
```

#### Grouped Pipeline
Skills organized into logical groups:
```yaml
pipelines:
  default:
    - naming-one
    - naming-two
    - hygiene-one
    - hygiene-two
  allowed:
    - [naming-one, naming-two]      # Naming group
    - [hygiene-one, hygiene-two]    # Hygiene group
    - [naming-one]                  # Individual skills
    - [naming-two]
    - [hygiene-one]
    - [hygiene-two]
```

### Shared Resources Structure

When using shared resources, organize them in a `.resources` directory:

```
skillset-name/
├── SKILL.md                        # Skillset orchestrator
├── .resources/                     # Shared resources
│   ├── assets/
│   │   └── diagram.png
│   ├── scripts/
│   │   └── utility.sh
│   └── references/
│       ├── TAXONOMY.md             # Shared terminology
│       └── TEMPLATES.md            # Shared templates
├── member-one/
│   ├── SKILL.md
│   ├── references/
│   └── scripts/
└── member-two/
    ├── SKILL.md
    ├── references/
    └── scripts/
```

---

## Plan Artifact Frontmatter Schema

### Overview

Plan artifacts (phase plans, sub-plans, and task files) created by the `plan` skillset include a `status` field in their frontmatter to track execution progress.

### Status Field

#### `status`
- **Type:** String (enum)
- **Required:** Yes (for plan artifacts)
- **Values:**
  - `pending`: Task not yet started
  - `in_progress`: Task currently being worked on
  - `complete`: Task finished

### Example - Plan Artifact

```yaml
---
status: pending
title: Implement authentication system
phase: 3
---

# Task: Implement authentication system

## Description
Create JWT-based authentication with refresh tokens.

## Acceptance Criteria
- [ ] User can log in with credentials
- [ ] JWT tokens issued on successful login
- [ ] Refresh token rotation implemented
- [ ] Protected routes validate tokens
```

### Example - Sub-plan with Status

```yaml
---
status: in_progress
title: Backend API Development
parent_plan: phase-2
---

# Sub-plan: Backend API Development

## Tasks
1. [x] Design API schema
2. [x] Set up database models
3. [ ] Implement endpoints
4. [ ] Add validation
5. [ ] Write tests
```

### Status Tracking

The `plan-status` skill parses frontmatter to display progress:

```bash
# macOS / Linux / WSL
./plan/status/scripts/status.sh

# Windows (PowerShell)
.\plan\status\scripts\status.ps1
```

**Example Output:**
```
Plan Status for Phase 2

Root Plan: [in_progress] phase-2-plan.md

Sub-plans:
  [complete] backend-api.md
  [in_progress] frontend-ui.md
  [pending] integration-tests.md

Tasks:
  Backend API: 8/10 complete
  Frontend UI: 3/8 complete
  Integration Tests: 0/5 complete

Overall Progress: 11/23 (47.8%)
```

---

## Schema Validation

### Using the Reference Library

Validate skills using the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) library:

```bash
skills-ref validate ./my-skill
```

### Manual Validation Checklist

**For Individual Skills:**
- [ ] `SKILL.md` contains only frontmatter (no body content)
- [ ] `name` field is lowercase with hyphens only
- [ ] `name` matches parent directory name
- [ ] `description` is 1-1024 characters
- [ ] `metadata.references` lists all reference files
- [ ] `metadata.scripts` lists all script files
- [ ] Reference files follow `NN_TOPIC.md` naming
- [ ] Scripts include both `.sh` and `.ps1` versions when possible

**For Skillsets:**
- [ ] All individual skill requirements met
- [ ] `metadata.skillset` field present
- [ ] `schema_version` is `1`
- [ ] `skills` array lists all members
- [ ] `pipelines.default` defines execution order
- [ ] `pipelines.allowed` lists valid combinations
- [ ] Shared resources in `.resources` if used
- [ ] Member skills exist and are valid

---

## Best Practices

### SKILL.md Frontmatter

1. **Keep it minimal** - Only frontmatter, no body content
2. **Use multiline strings** - YAML `>` for descriptions
3. **List all resources** - Complete references and scripts arrays
4. **Add keywords** - Improve discoverability
5. **Version your skills** - Use semantic versioning

### SKILLSET Schema

1. **Define clear pipelines** - Document recommended execution order
2. **Allow flexibility** - Include valid alternative sequences
3. **Share resources wisely** - Only share truly common materials
4. **Keep members independent** - Each skill should work standalone
5. **Document orchestration** - Explain why skills are grouped

### Reference Files

1. **Progressive disclosure** - Split content into focused files
2. **Consistent naming** - Use `NN_TOPIC.md` pattern
3. **Order matters** - Number files in logical reading order
4. **Stay focused** - One topic per file
5. **Cross-reference** - Link between related references

### Scripts

1. **Cross-platform** - Provide both `.sh` and `.ps1` versions
2. **Self-contained** - Document dependencies clearly
3. **Error handling** - Include helpful error messages
4. **Exit codes** - Use standard exit codes (0=success)
5. **Documentation** - Add comments for complex logic

---

## See Also

- [Agent Skills Specification](../SPEC.md) - Official format specification
- [Skills Reference](./02_SKILLS.md) - Available skills
- [Skillsets Documentation](./03_SKILLSETS.md) - Orchestrator skills
- [Contributing Guidelines](./05_CONTRIBUTING.md) - Adding new skills
