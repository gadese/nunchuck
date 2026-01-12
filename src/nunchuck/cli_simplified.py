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
    """Get the central skills directory."""
    # Default to ~/.nunchuck
    central_dir = Path.home() / ".nunchuck"
    
    # Allow override via environment variable
    if "NUNCHUCK_DIR" in os.environ:
        central_dir = Path(os.environ["NUNCHUCK_DIR"])
    
    return central_dir


@click.group()
@click.version_option(version="0.1.0", prog_name="nunchuck")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--dry-run", is_flag=True, help="Show what would be done without executing")
@click.pass_context
def cli(ctx, verbose, dry_run):
    """Nunchuck CLI for managing agent skills with adapter generation."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
    ctx.obj["dry_run"] = dry_run
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    if dry_run:
        click.echo("DRY RUN MODE - No changes will be made", err=True)


@cli.command()
@click.argument("skill_path", type=click.Path(exists=True))
@click.option("--central-dir", type=click.Path(), help="Central skills directory (default: ~/.nunchuck)")
@click.pass_context
def add(ctx, skill_path, central_dir):
    """Add a skill to the central directory."""
    skill_path = Path(skill_path).resolve()
    
    if central_dir:
        central = Path(central_dir).resolve()
    else:
        central = get_central_dir()
    
    # Get skill name from directory
    skill_name = skill_path.name
    
    # Check if skill already exists
    dest = central / "skills" / skill_name
    if dest.exists():
        raise click.ClickException(f"Skill already exists: {skill_name}")
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would copy {skill_path} to {dest}")
        return
    
    # Create central directory structure
    central.mkdir(parents=True, exist_ok=True)
    (central / "skills").mkdir(exist_ok=True)
    
    # Copy skill to central directory
    click.echo(f"Adding skill '{skill_name}' to central directory...")
    shutil.copytree(skill_path, dest)
    
    click.echo(f"✓ Added {skill_name} to {central}")


@cli.command()
@click.argument("skill_name")
@click.option("--central-dir", type=click.Path(), help="Central skills directory (default: ~/.nunchuck)")
@click.pass_context
def remove(ctx, skill_name, central_dir):
    """Remove a skill from the central directory."""
    if central_dir:
        central = Path(central_dir).resolve()
    else:
        central = get_central_dir()
    
    skill_path = central / "skills" / skill_name
    
    if not skill_path.exists():
        raise click.ClickException(f"Skill not found: {skill_name}")
    
    if not click.confirm(f"Are you sure you want to remove skill '{skill_name}'?"):
        click.echo("Operation cancelled.")
        return
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would remove {skill_path}")
        return
    
    # Remove skill
    shutil.rmtree(skill_path)
    click.echo(f"✓ Removed {skill_name} from central directory")


@cli.command()
@click.option("--central-dir", type=click.Path(), help="Central skills directory (default: ~/.nunchuck)")
@click.option("--filter", help="Filter skills by name")
def list(central_dir, filter):
    """List available skills."""
    if central_dir:
        central = Path(central_dir).resolve()
    else:
        central = get_central_dir()
    
    skills_dir = central / "skills"
    
    if not skills_dir.exists():
        click.echo("No skills directory found. Run 'nunchuck add <skill>' first.")
        return
    
    # List skills
    skills = []
    for item in skills_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            if filter and filter not in item.name:
                continue
            skills.append(item.name)
    
    if not skills:
        if filter:
            click.echo(f"No skills found matching '{filter}'.")
        else:
            click.echo("No skills found.")
        return
    
    click.echo(f"Available skills in {central}:")
    for skill in sorted(skills):
        click.echo(f"  - {skill}")


@cli.command()
@click.argument("skill_name")
@click.argument("output_dir", type=click.Path(), default=".")
@click.option("--central-dir", type=click.Path(), help="Central skills directory (default: ~/.nunchuck)")
@click.option("--link", is_flag=True, help="Create symlink instead of copying")
@click.pass_context
def use(ctx, skill_name, output_dir, central_dir, link):
    """Use a skill in the specified directory."""
    output_dir = Path(output_dir).resolve()
    
    if central_dir:
        central = Path(central_dir).resolve()
    else:
        central = get_central_dir()
    
    # Find skill in central directory
    skill_source = central / "skills" / skill_name
    
    if not skill_source.exists():
        raise click.ClickException(f"Skill not found: {skill_name}")
    
    # Destination
    skill_dest = output_dir / skill_name
    
    if skill_dest.exists():
        raise click.ClickException(f"Skill already exists in output directory: {skill_name}")
    
    if ctx.obj["dry_run"]:
        action = "link" if link else "copy"
        click.echo(f"Would {action} {skill_source} to {skill_dest}")
        return
    
    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy or link skill
    if link:
        try:
            if os.name == "nt":  # Windows
                import subprocess
                subprocess.run(
                    ["mklink", "/J", str(skill_dest), str(skill_source)],
                    shell=True,
                    check=True,
                    capture_output=True
                )
            else:
                skill_dest.symlink_to(skill_source, target_is_directory=True)
            click.echo(f"✓ Linked {skill_name} to {output_dir}")
        except Exception as e:
            click.echo(f"Failed to create link, falling back to copy: {e}")
            shutil.copytree(skill_source, skill_dest)
            click.echo(f"✓ Copied {skill_name} to {output_dir}")
    else:
        shutil.copytree(skill_source, skill_dest)
        click.echo(f"✓ Copied {skill_name} to {output_dir}")


@cli.command()
@click.argument("target", type=click.Path(exists=True))
@click.option("--json", "json_flag", is_flag=True, help="Output as JSON")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed validation report")
def validate(target, json_flag, verbose):
    """Validate skill against Agent Skills spec."""
    target_path = Path(target)
    
    # Validate input
    if not target_path.exists():
        raise click.BadParameter(f"Path does not exist: {target}")
    
    # Run validation
    code, report = validate_target(target_path)
    
    # Output results
    if json_flag:
        click.echo(format_json(report))
    else:
        click.echo(format_human(report))
    
    # Exit with error code if validation failed
    sys.exit(code)


@cli.command()
@click.option("--windsurf", is_flag=True, help="Generate Windsurf workflows")
@click.option("--cursor", is_flag=True, help="Generate Cursor rules")
@click.option("--clean", is_flag=True, help="Remove existing adapters")
@click.option("--skills-dir", default="skills", help="Skills directory")
@click.pass_context
def adapter(ctx, windsurf, cursor, clean, skills_dir):
    """Generate IDE adapters for skills."""
    skills_dir = Path(skills_dir)
    
    if not skills_dir.exists():
        raise click.ClickException(f"Skills directory not found: {skills_dir}")
    
    # Auto-detect IDEs if none specified
    if not windsurf and not cursor and not clean:
        windsurf_dir = Path(".windsurf")
        cursor_dir = Path(".cursor")
        
        if windsurf_dir.exists():
            windsurf = True
            click.echo("Detected Windsurf IDE")
        if cursor_dir.exists():
            cursor = True
            click.echo("Detected Cursor IDE")
        
        if not windsurf and not cursor:
            click.echo("No IDE detected. Specify --windsurf or --cursor.")
            return
    
    # Generate adapters
    generator = AdapterGenerator(skills_dir)
    
    if clean:
        if not ctx.obj["dry_run"]:
            generator.clean()
            click.echo("Cleaned existing adapters")
        else:
            click.echo("Would clean existing adapters")
        return
    
    if windsurf:
        if not ctx.obj["dry_run"]:
            generator.generate_windsurf()
            click.echo(f"Generated Windsurf adapters from {skills_dir}")
        else:
            click.echo(f"Would generate Windsurf adapters from {skills_dir}")
    
    if cursor:
        if not ctx.obj["dry_run"]:
            generator.generate_cursor()
            click.echo(f"Generated Cursor adapters from {skills_dir}")
        else:
            click.echo(f"Would generate Cursor adapters from {skills_dir}")


@cli.command()
@click.argument("output_dir", type=click.Path(), default=".")
@click.option("--central-dir", type=click.Path(), help="Central skills directory (default: ~/.nunchuck)")
def install(output_dir, central_dir):
    """Install nunchuck and move skills to central directory."""
    output_dir = Path(output_dir).resolve()
    
    if central_dir:
        central = Path(central_dir).resolve()
    else:
        central = get_central_dir()
    
    # Move skills directory to central location
    local_skills = output_dir / "skills"
    central_skills = central / "skills"
    
    if local_skills.exists() and local_skills.is_dir():
        if central_skills.exists():
            click.echo(f"Central skills directory already exists: {central_skills}")
            if not click.confirm("Merge with existing central directory?"):
                click.echo("Installation cancelled.")
                return
        
        # Create central directory
        central.mkdir(parents=True, exist_ok=True)
        
        # Move skills
        click.echo(f"Moving skills from {local_skills} to {central_skills}...")
        if central_skills.exists():
            # Merge directories
            for skill in local_skills.iterdir():
                if skill.is_dir():
                    dest = central_skills / skill.name
                    if dest.exists():
                        click.echo(f"Skipping existing skill: {skill.name}")
                    else:
                        shutil.move(str(skill), str(dest))
        else:
            shutil.move(str(local_skills), str(central_skills))
        
        click.echo(f"✓ Skills installed to {central}")
    else:
        click.echo("No local skills directory found.")


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
