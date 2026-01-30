# Coding Standards Skillset

## Purpose

This skillset provides a centralized, single source of truth for coding guidelines across the project. It is **not invoked directly** as a workflow, but rather **referenced** by other skillsets through symlinks.

## Structure

The `references/` directory contains four core guideline documents:

1. **`code-principles.md`** - General code principles (type hints, design patterns, error handling)
2. **`code-style.md`** - Code style conventions (formatting, naming, imports)
3. **`ml-dl-guide.md`** - Machine learning and deep learning best practices
4. **`data-science-guide.md`** - Data science and pandas best practices

## How Other Skillsets Reference This

Other skillsets reference these guidelines via `.shared/` symlinks:

```
skills/rpi/.shared/references -> ../../coding-standards/references
skills/algo-rpi/.shared/references -> ../../coding-standards/references
skills/code-review/.shared/references -> ../../coding-standards/references
skills/doctor/.shared/references -> ../../coding-standards/references
```

## When Each Guide Applies

- **`code-principles.md`** - Always applied (always_on)
- **`code-style.md`** - Always applied (always_on)
- **`ml-dl-guide.md`** - Applied when working on ML/DL models (model_decision)
- **`data-science-guide.md`** - Applied when working on data analysis (model_decision)

## Recreating Symlinks

If symlinks are destroyed, recreate them with:

```bash
cd /path/to/repo
ln -s ../../coding-standards/references skills/rpi/.shared
ln -s ../../coding-standards/references skills/algo-rpi/.shared
ln -s ../../coding-standards/references skills/code-review/.shared
ln -s ../../coding-standards/references skills/doctor/.shared
```

## Maintenance

When updating coding guidelines:

1. Edit the appropriate file in `skills/coding-standards/references/`
2. Changes automatically propagate to all skillsets via symlinks
3. No need to update multiple locations

This design avoids duplication and ensures consistency across all skillsets.
