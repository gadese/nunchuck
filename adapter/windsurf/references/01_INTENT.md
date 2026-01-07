# Intent

This skill bridges agent skills to Windsurf workflows.

## Problem

Agent skills (`.codex/skills/`) define structured, reusable procedures with:
- YAML frontmatter (name, description, keywords)
- Chunked references (intent, procedure, output format)
- Optional scripts for automation

Windsurf workflows (`.windsurf/workflows/`) provide:
- Slash command invocation (`/skill-name`)
- IDE integration and discoverability
- `auto_execution_mode` for automatic triggering

Without an adapter, skills must be manually duplicated as workflows,
leading to drift and maintenance burden.

## Solution

Generate thin Windsurf workflows that:
1. Use skill description as the workflow `description`
2. Instruct the agent to read and follow the skill's references
3. Point to the canonical skill location for all detailed instructions

This keeps workflows as lightweight pointers while skills remain
the source of truth.

## Benefits

- **Single source of truth:** Edit skills, regenerate workflows
- **No duplication:** Workflow bodies are minimal delegation stubs
- **Automatic sync:** Run generator after skill changes
- **Skillset awareness:** Orchestrator skills can delegate to members
