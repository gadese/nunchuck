# Quickstart

Get up and running with nunchuck and agent skills in minutes.

## 1. Clone the Repository

```bash
git clone https://github.com/JordanGunn/skills.git && cd skills
```

---

## 2. Install nunchuck CLI

The nunchuck CLI manages skills and generates IDE adapters.

### Unix (macOS/Linux/WSL)

```bash
# Install with uv (recommended - fastest)
./scripts/install.sh uv

# Or use pipx for isolated installation
./scripts/install.sh pipx

# Or use pip for user installation
./scripts/install.sh user
```

### Windows (PowerShell)

```powershell
# Install with uv (recommended - fastest)
.\scripts\install.ps1 uv

# Or use pip for user installation
.\scripts\install.ps1 user
```

The installer will:

1. Install the `nunchuck` CLI tool
2. Copy all skills to `~/.nunchuck/skills/`

---

## 3. Using Skills

### List Available Skills

```bash
nunchuck list
```

### Copy a Skill to Your Project

```bash
# Copy to current directory
nunchuck use doctor

# Copy to specific directory
nunchuck use doctor ./my-project/skills/
```

### Generate IDE Adapters

```bash
# Auto-detect IDE from current directory
nunchuck adapter

# Generate Windsurf workflows
nunchuck adapter --windsurf

# Generate Cursor commands
nunchuck adapter --cursor
```

### Validate a Skill

```bash
nunchuck validate path/to/skill
```

---

## 4. IDE Integration

### Windsurf

After running `nunchuck adapter --windsurf`, workflows appear in `.windsurf/workflows/`. Use slash commands like `/doctor` or `/plan-create` to invoke skills.

### Cursor

After running `nunchuck adapter --cursor`, commands appear in `.cursor/commands/`. Access via the command palette.

---

## 5. Next Steps

- **[Skills Reference](./SKILLS.md)** - Browse all available skills
- **[Skillsets Documentation](./SKILLSETS.md)** - Learn about orchestrator skills
- **[Schema Documentation](./schema/SKILL.md)** - Technical reference
- **[Contributing Guidelines](../CONTRIBUTING.md)** - Add your own skills
