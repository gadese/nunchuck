# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- New `nunchuck` CLI with simplified flat command structure
- Centralized skill storage at `~/.nunchuck/skills/`
- `uv` + `hatchling` build system for fast installation
- PowerShell installer with skill copying support
- `docs/CLI.md` command-line documentation

### Changed

- Simplified CLI commands: `list`, `use`, `validate`, `adapter` are now top-level
- Skills are copied to `~/.nunchuck/skills/` during installation
- Updated README, QUICKSTART, SKILLS, and SKILLSETS documentation
- Renamed `cli_simplified.py` to `cli.py`

### Removed

- Removed `global` and `project` CLI subcommand groups
- Removed old `cli.py` and `cli_click.py` files
- Removed outdated refactor skills references from documentation

[Unreleased]: https://github.com/JordanGunn/skills/compare/v0.0.0...HEAD
