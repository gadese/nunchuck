# Intent

This skill bridges agent skills to Cursor commands.

## Problem

Agent skills (`.codex/skills/`) define structured, reusable procedures. Cursor commands (`.cursor/`) provide IDE integration for invoking these skills, but without an adapter, skills must be manually duplicated as commands.

## Solution

Generate plain markdown files under `.cursor/` that:

1. Describe the skill's purpose
2. Instruct the agent to read and follow the skill's references
3. Point to the canonical skill location

Unlike Windsurf workflows, Cursor commands require no frontmatter — they are plain markdown documents.

## Benefits

- **Single source of truth:** Edit skills, regenerate commands
- **No duplication:** Command bodies are lightweight delegation stubs
- **Automatic sync:** Run generator after skill changes
