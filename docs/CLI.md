# nunchuck CLI

Command-line tool for managing agent skills.

## Installation

### Unix (macOS/Linux/WSL)

```bash
# Install with uv (recommended)
./scripts/install.sh uv

# Or use pipx
./scripts/install.sh pipx
```

### Windows (PowerShell)

```powershell
# Install with uv (recommended)
.\scripts\install.ps1 uv

# Or use pip
.\scripts\install.ps1 user
```

The installer copies all skills to `~/.nunchuck/skills/`.

---

## Commands

### `nunchuck list`

List all available skills from `~/.nunchuck/skills/`.

```bash
nunchuck list
nunchuck list --filter doctor  # Filter by name
```

### `nunchuck use`

Copy a skill from `~/.nunchuck/skills/` to your project.

```bash
nunchuck use doctor           # Copy to current directory
nunchuck use doctor ./skills  # Copy to specific directory
nunchuck use doctor --force   # Overwrite if exists
```

### `nunchuck validate`

Validate a skill against the Agent Skills specification.

```bash
nunchuck validate path/to/skill
```

### `nunchuck adapter`

Generate IDE adapters for skills in your project.

```bash
# Auto-detect IDE
nunchuck adapter

# Generate specific adapters
nunchuck adapter --windsurf
nunchuck adapter --cursor

# Specify directories
nunchuck adapter --skills-dir ./skills --output-dir .
```

---

## Options

### Global Options

- `--version` - Show version and exit
- `--verbose, -v` - Enable verbose output
- `--dry-run` - Show what would be done without executing
- `--help` - Show help message

---

## Environment Variables

- `NUNCHUCK_DIR` - Override the default skills directory (`~/.nunchuck`)

---

## Examples

### Set Up a New Project

```bash
# Copy skills you need
nunchuck use doctor
nunchuck use plan
nunchuck use task

# Generate IDE adapters
nunchuck adapter --windsurf
```

### Update Skills

Re-run the install script to update skills from the repository:

```bash
./scripts/install.sh uv
```

---

## See Also

- [Quickstart Guide](./QUICKSTART.md)
- [Skills Reference](./SKILLS.md)
- [Skillsets Documentation](./SKILLSETS.md)
