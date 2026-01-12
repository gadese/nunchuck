# Pipelines

A skillset MUST define a `.pipelines/` sibling directory.

## Mandatory files

- `.pipelines/.INDEX.md`: Index of pipeline files with links and descriptions for quick lookup.
- `.pipelines/00_DEFAULT.md`: Default behavior when the top-level skill is invoked.

## Additional pipeline files

- Additional pipeline files MAY be created as `.pipelines/<NN>_<NAME>.md`.
- Numbering MUST start at `01_`.
- These files are user-defined.

## Pipeline file format

All pipeline files MUST follow this exact structure.

```markdown
# <Pipeline name>

## Triggers

- When the agent should use or trigger this pipeline
- Situations when the agent should trigger

## Skills

1. <valid-skill-name>
2. <valid-skill-name>
```

## Notes

- The `Triggers` section MUST be an unordered list.
- The `Skills` section SHALL contain only an ordered list of valid skill names.
