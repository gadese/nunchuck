# Quickstart

Get up and running with nunchuck and agent skills in minutes.

## 1. Clone the Repository

```bash
git clone https://github.com/JordanGunn/skills.git && cd skills
```

---

## 2. Copy skills into your project

Copy the `skills/` directory wherever you want to use it.

---

## 3. Using Skills

### Generate IDE Adapters

```bash
# Generate Windsurf workflows
bash scripts/adapters/windsurf/run.sh --skills-root skills --output-root .

# Generate Cursor commands
bash scripts/adapters/cursor/run.sh --skills-root skills --output-root .
```

---

## 4. IDE Integration

### Windsurf

After generating workflows, they appear in `.windsurf/workflows/`. Use slash commands like `/doctor` or `/plan-create` to invoke skills.

### Cursor

After generating commands, they appear in `.cursor/commands/`. Access via the command palette.

---

## 5. Next Steps

- **[Skills Reference](./SKILLS.md)** - Browse all available skills
- **[Skillsets Documentation](./SKILLSETS.md)** - Orchestrator skills and schema
- **[Contributing Guidelines](../CONTRIBUTING.md)** - Add your own skills
