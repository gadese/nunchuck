# Skillsets

## Introduction

A **skillset** is a parent skill that coordinates and orchestrates multiple related member skills. Skillsets provide a structured way to group skills that work together while maintaining their independence.

Skillsets leverage a **strict custom schema** within the `metadata.skillset` field of the frontmatter. This approach:

- **Signals to agents** that a group of skills can work together
- **Signals to users** that skills can be used together but are not required for individual usage
- **Maintains spec compliance** by using the standard `SKILL.md` format with custom metadata
- **Creates no breaking changes** - it's just additional metadata in a spec-compliant file

## Key Characteristics

### Spec-Compliant Parent Skill

A skillset is simply a `SKILL.md` file that:

1. Follows the standard Agent Skills specification
2. Adds a custom `metadata.skillset` field with a strict schema
3. Acts as an orchestrator that dispatches to member skills

### Non-Breaking Innovation

The skillset concept is **novel but non-breaking** because:

- It uses the existing `SKILL.md` format
- The `metadata` field is designed for custom extensions
- Agents that don't understand skillsets simply see a regular skill
- Member skills remain fully independent and usable on their own

### Optional Grouping

Member skills can be:

- **Used individually** - Each skill is fully functional on its own
- **Used as a group** - The skillset orchestrates execution
- **Used in custom combinations** - Users can pick specific skills

## Skillset Schema

The `metadata.skillset` field defines the skillset structure:

```yaml
metadata:
  skillset:
    name: skillset-name              # Skillset identifier
    schema_version: 1                # Schema version (currently 1)
    skills:                          # List of member skill names
      - skill-one
      - skill-two
    resources:                       # Shared resources
      root: .resources               # Shared resources directory
      assets: []                     # Shared asset files
      scripts: []                    # Shared scripts
      references:                    # Shared reference files
        - SHARED_DOC.md
    pipelines:                       # Execution pipelines
      default:                       # Default execution order
        - skill-one
        - skill-two
      allowed:                       # Valid skill sequences
        - [skill-one]
        - [skill-two]
        - [skill-one, skill-two]
    requires: []                     # Dependencies (TBD)
```

### Schema Fields

#### `name` (required)
The skillset identifier. Should match the skill's `name` field.

#### `schema_version` (required)
The version of the skillset schema being used. Currently `1`.

#### `skills` (required)
Array of member skill names. These are the skills that belong to this skillset.

#### `resources` (optional)
Shared resources directory for assets, scripts, and references used by multiple member skills.

- **`root`**: Directory path (e.g., `.resources`)
- **`assets`**: List of shared asset files
- **`scripts`**: List of shared scripts
- **`references`**: List of shared reference documents

#### `pipelines` (required)
Defines how skills can be executed together.

- **`default`**: The recommended execution order for all skills
- **`allowed`**: List of valid skill execution sequences
  - Can include individual skills
  - Can include custom combinations
  - Provides flexibility while maintaining safety

#### `requires` (optional)
Dependencies that the skillset assumes or provisions. Implementation is to be determined.

## Available Skillsets

### `changelog`

**Path:** `skills/changelog/`

Manages Keep a Changelog format files with deterministic operations, chrono-aware guardrails, and git integration.

**Member Skills:**

- `changelog-init` - Initialize a new changelog from template
- `changelog-update` - Add entries to [Unreleased] section
- `changelog-release` - Cut a release by versioning [Unreleased]
- `changelog-verify` - Verify changelog format compliance

**Use Case:** Maintain a consistent, spec-compliant changelog with duplicate detection and semantic versioning.

---

### `doctor`

**Path:** `skills/doctor/`

Diagnoses software failures by combining deterministic evidence gathering with agent judgment. Models failures as medical cases. Idempotent — run repeatedly until confident diagnosis.

**Key Features:**

- Evidence-based diagnosis with `.doctor/` artifacts
- Hypothesis generation and testing
- Treatment plan generation

**Use Case:** Debug complex issues systematically with medical-style triage.

---

### `md`

**Path:** `skills/md/`

Orchestrates markdown document workflows with deterministic operations.

**Member Skills:**

- `md-split` - Split large markdown files into chunks
- `md-merge` - Merge markdown chunks back together
- `md-review` - Agent review of markdown content

**Use Case:** Process large markdown documents that exceed context windows.

---

### `plan`

**Path:** `skills/plan/`

Manages bounded work units with structured plans stored in `.plan/`.

**Member Skills:**

- `plan-create` - Create execution plans
- `plan-exec` - Execute existing plans
- `plan-status` - Track plan progress
- `plan-review` - Review plan completion

**Use Case:** Manage complex development phases with structured planning.

---

### `prompt`

**Path:** `skills/prompt/`

Separates intent formation from execution to protect humans from premature or misaligned action.

**Member Skills:**

- `prompt-forge` - Create structured prompts from intent
- `prompt-compile` - Compile YAML artifact into PROMPT.md
- `prompt-exec` - Execute compiled prompts

**Use Case:** Ensure human oversight of agent actions through deliberate prompt engineering.

---

### `task`

**Path:** `skills/task/`

Manages bounded work units with single-file tasks stored in `.tasks/`.

**Member Skills:**

- `task-create` - Create new tasks
- `task-list` - List available tasks
- `task-select` - Select a task to work on
- `task-close` - Close completed tasks

**Use Case:** Track work items with skepticism-aware hashing and staleness detection.

---

## Using Skillsets

### Invoke the Orchestrator

Reference the skillset's `SKILL.md` file to activate the orchestrator:

```
Please use the plan skillset to help me create and execute a development plan.
```

The orchestrator will dispatch to member skills according to its pipeline configuration.

### Invoke Individual Members

You can bypass the orchestrator and use member skills directly:

```
Please use plan-create to generate a new phase plan.
```

This gives you fine-grained control when you only need specific functionality.

### Invoke Custom Combinations

If the skillset defines allowed combinations, you can request specific sequences:

```
Please run the naming cluster from the refactor skillset:
- refactor-lexical-ontology
- refactor-module-stutter
- refactor-semantic-noise
```

## Creating Skillsets

When creating a new skillset:

1. **Identify related skills** that work together toward a common goal
2. **Create a parent SKILL.md** with standard frontmatter
3. **Add `metadata.skillset`** with the skillset schema
4. **Define the default pipeline** for recommended execution order
5. **List allowed combinations** to provide flexibility
6. **Create shared resources** (optional) in a `.resources` directory
7. **Document the orchestration logic** in the SKILL.md body or references

### Design Principles

- **Keep member skills independent** - Each skill should be fully functional on its own
- **Define clear pipelines** - Specify recommended execution orders
- **Provide flexibility** - Allow custom combinations where appropriate
- **Share common resources** - Use `.resources` for shared documentation
- **Document dependencies** - Clarify when skills should be run in sequence

## Benefits of Skillsets

### For Agents
- **Clear orchestration** - Know how to combine skills effectively
- **Safety guarantees** - Follow validated execution sequences
- **Progressive disclosure** - Load only needed member skills

### For Users
- **Convenience** - Execute multiple related skills together
- **Flexibility** - Use skills individually or in groups
- **Discoverability** - See related skills grouped logically

### For Developers
- **Modularity** - Build focused, reusable skills
- **Composition** - Combine skills without tight coupling
- **Extensibility** - Add new members without breaking existing functionality

## Skillsets vs Individual Skills

| Aspect | Individual Skill | Skillset |
|--------|------------------|----------|
| Purpose | Perform one specific task | Orchestrate multiple tasks |
| Structure | Standard SKILL.md | SKILL.md + metadata.skillset |
| Independence | Standalone | Coordinates others |
| Execution | Direct invocation | Dispatches to members |
| Resources | Own references/scripts | May share resources |

## Advanced Topics

### Execution Order

Pipelines define execution order for dependent skills. For example:
- **Sequential**: One skill's output is another's input
- **Parallel**: Skills can run independently
- **Conditional**: Some combinations work, others don't

The `allowed` field documents valid combinations.

### Resource Sharing

The `.resources` directory provides shared assets for member skills:
```
skillset/
├── SKILL.md                    # Orchestrator
├── .resources/                 # Shared resources
│   └── references/
│       ├── TAXONOMY.md         # Shared terminology
│       └── TEMPLATES.md        # Shared templates
├── member-one/
│   └── SKILL.md
└── member-two/
    └── SKILL.md
```

### Future Extensions

The `requires` field is reserved for future dependency management:
- System tools or packages
- Environment variables
- Other skills or skillsets
- Network access requirements

## See Also

- [Skills Reference](./SKILLS.md) - Individual skills documentation
- [Schema Documentation](./schema/SKILL.md) - Detailed schema reference
- [SPEC.md](../SPEC.md) - Agent Skills specification
