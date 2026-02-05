# Step 4: Standard Skeleton for New Skill/Skillset Design

1. **Define the artifact(s)** (what will exist on disk?)
2. **Define CLI sruface** (create/update/list/validate)
3. **Define the static schemas/templates** (assets)
4. **Write reference guidance** (how agents interpret and act)
5. **Add rot controls** (validation + index regeneration)
6. **Add chronology + stable IDs** (hashes, dates, ordering)

## Define the CLI Surface (Mandatory)

Every skill SHALL expose a command-line interface as its sole execution surface.

At minimum, the CLI MUST implement:

- `help` — enumerate available commands and their purpose (primary discovery mechanism)
- `validate` — verify the skill is runnable (read-only; no mutation)
- `clean` — remove generated artifacts (required only if outputs are produced)

Additional commands are skill-specific (e.g. `list`, `create`, `split`, `index`) and are added explicitly to the CLI.

The CLI is the contract.
Scripts, modules, or SDK code exist only to support CLI commands and MUST NOT be invoked directly.
