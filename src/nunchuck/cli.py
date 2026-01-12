"""Simplified Click-based CLI for nunchuck skill management."""

import logging
import os
import shutil
import sys
from pathlib import Path

import click

from .adapter import AdapterGenerator
from .validation import format_human, format_json, validate_target


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)


def get_central_dir() -> Path:
    """Get the central skills directory (~/.nunchuck)."""
    if "NUNCHUCK_DIR" in os.environ:
        return Path(os.environ["NUNCHUCK_DIR"])
    return Path.home() / ".nunchuck"


@click.group()
@click.version_option(version="0.1.0", prog_name="nunchuck")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--dry-run", is_flag=True, help="Show what would be done without executing")
@click.pass_context
def cli(ctx, verbose, dry_run):
    """Nunchuck CLI for managing agent skills.
    
    Skills are stored in ~/.nunchuck/skills and can be copied to projects.
    """
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
    ctx.obj["dry_run"] = dry_run
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    if dry_run:
        click.echo("DRY RUN MODE - No changes will be made", err=True)


@cli.command("list")
@click.option("--filter", "-f", "name_filter", help="Filter skills by name")
def list_skills(name_filter):
    """List available skills from ~/.nunchuck."""
    central = get_central_dir()
    skills_dir = central / "skills"
    
    if not skills_dir.exists():
        click.echo("No skills installed. Run the install script first.")
        click.echo(f"Expected location: {skills_dir}")
        return
    
    # Collect skills
    skills = []
    for item in skills_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            if name_filter and name_filter.lower() not in item.name.lower():
                continue
            # Try to get skill metadata
            skill_md = item / "SKILL.md"
            description = ""
            if skill_md.exists():
                # Read first non-empty line after title for description
                try:
                    with open(skill_md) as f:
                        lines = f.readlines()
                        for line in lines[1:5]:  # Check first few lines
                            line = line.strip()
                            if line and not line.startswith('#'):
                                description = line[:50] + "..." if len(line) > 50 else line
                                break
                except Exception:
                    pass
            skills.append((item.name, description))
    
    if not skills:
        if name_filter:
            click.echo(f"No skills found matching '{name_filter}'.")
        else:
            click.echo("No skills found.")
        return
    
    click.echo(f"Available skills ({len(skills)}):")
    click.echo()
    for name, desc in sorted(skills):
        if desc:
            click.echo(f"  {name:<20} {desc}")
        else:
            click.echo(f"  {name}")


@cli.command()
@click.argument("skill_name")
@click.argument("dest", type=click.Path(), default=".")
@click.option("--force", "-f", is_flag=True, help="Overwrite if exists")
@click.pass_context
def use(ctx, skill_name, dest, force):
    """Copy a skill from ~/.nunchuck to your project.
    
    SKILL_NAME is the name of the skill to use.
    DEST is the destination directory (default: current directory).
    """
    central = get_central_dir()
    skill_source = central / "skills" / skill_name
    
    if not skill_source.exists():
        click.echo(f"Skill not found: {skill_name}")
        click.echo("Run 'nunchuck list' to see available skills.")
        raise SystemExit(1)
    
    dest_path = Path(dest).resolve()
    skill_dest = dest_path / skill_name
    
    if skill_dest.exists():
        if force:
            if ctx.obj["dry_run"]:
                click.echo(f"Would remove existing {skill_dest}")
            else:
                shutil.rmtree(skill_dest)
        else:
            click.echo(f"Skill already exists: {skill_dest}")
            click.echo("Use --force to overwrite.")
            raise SystemExit(1)
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would copy {skill_source} to {skill_dest}")
        return
    
    dest_path.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill_source, skill_dest)
    click.echo(f"✓ Copied {skill_name} to {dest_path}")


@cli.command()
@click.argument("target", type=click.Path(exists=True))
@click.option("--json", "json_flag", is_flag=True, help="Output as JSON")
def validate(target, json_flag):
    """Validate a skill against the Agent Skills spec."""
    target_path = Path(target)
    code, report = validate_target(target_path)
    
    if json_flag:
        click.echo(format_json(report))
    else:
        click.echo(format_human(report))
    
    sys.exit(code)


@cli.command()
@click.option("--windsurf", is_flag=True, help="Generate Windsurf workflows")
@click.option("--cursor", is_flag=True, help="Generate Cursor rules")
@click.option("--clean", is_flag=True, help="Remove existing adapters")
@click.option("--skills-dir", default="skills", help="Skills directory")
@click.option("--output-dir", default=".", help="Output directory for adapters")
@click.pass_context
def adapter(ctx, windsurf, cursor, clean, skills_dir, output_dir):
    """Generate IDE adapters for skills in your project."""
    skills_path = Path(skills_dir)
    output_path = Path(output_dir)
    
    if not skills_path.exists():
        click.echo(f"Skills directory not found: {skills_dir}")
        raise SystemExit(1)
    
    # Auto-detect IDEs if none specified
    if not windsurf and not cursor and not clean:
        if Path(".windsurf").exists():
            windsurf = True
            click.echo("Detected Windsurf IDE")
        if Path(".cursor").exists():
            cursor = True
            click.echo("Detected Cursor IDE")
        
        if not windsurf and not cursor:
            click.echo("No IDE detected. Specify --windsurf or --cursor.")
            return
    
    generator = AdapterGenerator(skills_path, output_path)
    
    if clean:
        if not ctx.obj["dry_run"]:
            generator.clean()
            click.echo("Cleaned existing adapters")
        else:
            click.echo("Would clean existing adapters")
        return
    
    if windsurf:
        if not ctx.obj["dry_run"]:
            count = generator.generate_windsurf()
            click.echo(f"Generated {count} Windsurf workflow(s) from {skills_dir}")
        else:
            click.echo(f"Would generate Windsurf adapters from {skills_dir}")
    
    if cursor:
        if not ctx.obj["dry_run"]:
            count = generator.generate_cursor()
            click.echo(f"Generated {count} Cursor rule(s) from {skills_dir}")
        else:
            click.echo(f"Would generate Cursor adapters from {skills_dir}")


def main():
    """Entry point for the CLI."""
    try:
        cli()
    except KeyboardInterrupt:
        click.echo("\nOperation cancelled.", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
