# Output Format

Each generated command is a plain markdown file (no frontmatter):

```markdown
# <Skill Name>

<skill description>

## Instructions

1. Read the skill manifest: `.codex/skills/<path>/SKILL.md`
2. Read all references in order:
   - `references/<ref1>.md`
   - `references/<ref2>.md`
   - ...
3. If scripts are present, follow automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

**Path:** `.codex/skills/<path>/`

## Keywords

<keywords for discoverability>
```

## Naming Convention

Command files are named after the skill:

- Skill `refactor-dictionaries` → `.cursor/refactor-dictionaries.md`
- Skill `plan-create` → `.cursor/plan-create.md`

## Skillset Commands

For skillset orchestrators, additionally note member skills and default pipeline.
