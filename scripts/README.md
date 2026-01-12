# Nunchuck Scripts

This directory contains utility scripts for the nunchuck CLI.

## Installation Scripts

### Unix/Linux/macOS

```bash
# Install using uv (fastest, recommended for development)
./scripts/install.sh uv

# Install in development mode (editable)
./scripts/install.sh dev

# Install for current user
./scripts/install.sh user

# Install using pipx (recommended for users)
./scripts/install.sh pipx
```

### Windows (PowerShell)

```powershell
# Install using uv (fastest, recommended for development)
.\scripts\install.ps1 uv

# Install in development mode (editable)
.\scripts\install.ps1 dev

# Install for current user
.\scripts\install.ps1 user
```

## Requirements

- Python 3.10 or later
- pip (usually included with Python)
- uv (optional - will be auto-installed when using uv mode)

## What Gets Installed

1. **nunchuck CLI** - The command-line tool
2. **Skills** - All skills from the repo are copied to `~/.nunchuck/skills`

## Notes

- **uv mode**: Fastest installation using uv (recommended for development)
- **Development mode**: Installs in editable mode, linking to the source code
- **User mode**: Installs for the current user only
- **pipx mode**: Uses pipx for isolated installation (Unix only)

## Quick Start

After installation:

```bash
# Install skills from a repository to central directory
nunchuck install /path/to/nunchuck-repo

# List available skills
nunchuck list

# Use a skill in your current directory
nunchuck use doctor

# Generate IDE adapters
nunchuck adapter generate

# Validate a skill
nunchuck validate skills/doctor
```

## Legacy Scripts

The following directories contain legacy scripts that have been migrated to the Python CLI:

- `adapter/` - Old adapter generation scripts (replaced by `nunchuck adapter generate`)
- `index/` - Old indexing scripts (replaced by `nunchuck util index`)
- `nunchuck/` - Old validation scripts (replaced by `nunchuck validate`)

These are kept for reference but are no longer used.
