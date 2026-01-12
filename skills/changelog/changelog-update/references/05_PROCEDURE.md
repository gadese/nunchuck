# Procedure

## Step 1: Gather Context

Ask user or infer:
- What changed?
- Which category? (Added/Changed/Fixed/etc.)
- Is there a PR/issue reference?

## Step 2: Check for Suggestions

```bash
./skill.sh suggest
```

Use as reference, but curate.

## Step 3: Add Entry

```bash
./skill.sh add <category> "<entry text>"
```

Example:
```bash
./skill.sh add Fixed "Resolve authentication timeout issue (#123)"
```

## Step 4: Verify

```bash
./skill.sh verify
```
