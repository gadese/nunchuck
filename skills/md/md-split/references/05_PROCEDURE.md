---
description: Canonical execution path for this skill.
index:
  - Step 1: Verify Source
  - Step 2: Run Split Script
  - Step 3: Generate Index
  - Step 4: Verify Output
  - Output Structure
---

# Procedure

Execution path for the md-split skill.

## Step 1: Verify Source

Confirm the source file exists and is markdown:

```bash
ls -la <source.md>
```

## Step 2: Run Split Script

```bash
./scripts/split.sh --in <source.md> [--out <output_dir>] [--prefix <NN>] [--dry-run] [--force] [--no-intro] [--manifest|--no-manifest]
```

Or on Windows:

```powershell
./scripts/split.ps1 --in <source.md> [--out <output_dir>] [--prefix <NN>] [--dry-run] [--force] [--no-intro] [--manifest|--no-manifest]
```

## Step 3: Generate Index

```bash
./scripts/index.sh --dir <output_dir>
```

## Step 4: Verify Output

Check that chunks were created:

```bash
ls -la <output_dir>/*.md
```

## Output Structure

```text
output_dir/
├── 00_INTRO.md        # Optional: content before first H2 (only when meaningful)
├── 01_SECTION_ONE.md  # First H2 section (promoted to H1)
├── 02_SECTION_TWO.md  # Second H2 section (promoted to H1)
├── .INDEX.md          # Generated index
└── .SPLIT.json        # Optional: manifest (default on; disable with --no-manifest)
```
