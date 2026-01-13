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

## Skillset Specifications

See [Skillset Design Specifications](docs/design/specs/skillset/.INDEX.md) for details.
