"""Click-based CLI for nunchuck skill management."""

import logging
import sys
from pathlib import Path

import click
import yaml

from .adapter import AdapterGenerator
from .packs import discover_packs
from .project import Project, ProjectError
from .store import Store, StoreError
from .validation import format_human, format_json, validate_target


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)


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


@cli.group()
def global_cmd():
    """Global skill management commands."""
    pass


@cli.group()
def project():
    """Project-specific skill commands."""
    pass


@cli.group()
def adapter():
    """Adapter generation commands."""
    pass


@cli.group()
def util():
    """Utility commands."""
    pass


# Global commands
@global_cmd.command("add")
@click.argument("path")
@click.option("--remote", is_flag=True, help="Add from remote URL")
@click.option("--name", help="Custom name for the skill")
@click.pass_context
def add_global(ctx, path, remote, name):
    """Add skill to global store."""
    # Path validation is handled by the Store class (supports local and remote)
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would add skill from {path} (name={name or 'auto'})")
        return
    
    try:
        store = Store()
        skill_name = store.add_skill(path, name)
        click.echo(f"Added skill '{skill_name}' to global store")
    except StoreError as e:
        raise click.ClickException(str(e))


@global_cmd.command("remove")
@click.argument("name")
@click.option("--force", is_flag=True, help="Force removal without confirmation")
@click.pass_context
def remove_global(ctx, name, force):
    """Remove skill from global store."""
    if not force:
        if not click.confirm(f"Are you sure you want to remove skill '{name}'?"):
            click.echo("Operation cancelled.")
            return
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would remove skill {name} from global store")
        return
    
    try:
        store = Store()
        store.remove_skill(name, force=force)
        click.echo(f"Removed skill '{name}' from global store")
    except StoreError as e:
        raise click.ClickException(str(e))


@global_cmd.command("list")
@click.option("--global", "global_flag", is_flag=True, help="List global skills")
@click.option("--json", "json_flag", is_flag=True, help="Output as JSON")
@click.option("--filter", help="Filter skills by name")
@click.option("--tag", help="Filter skills by tag")
@click.pass_context
def list_global(ctx, global_flag, json_flag, filter, tag):
    """List skills (global or project)."""
    if global_flag:
        if ctx.obj["dry_run"]:
            click.echo("Would list global skills")
            return
        
        try:
            store = Store()
            skills = store.list_skills()
            
            # Apply filters
            if filter:
                skills = {k: v for k, v in skills.items() if filter.lower() in k.lower()}
            if tag:
                # TODO: Implement tag filtering when tags are added to metadata
                click.echo("Tag filtering not yet implemented")
                return
            
            if not skills:
                click.echo("No skills found.")
                return
            
            if json_flag:
                click.echo(yaml.dump(skills, sort_keys=False))
            else:
                # Calculate column widths
                name_width = max(len(name) for name in skills.keys())
                name_width = max(name_width, len("NAME"))
                version_width = max(len(info.get('version', 'unknown')) for info in skills.values())
                version_width = max(version_width, len("VERSION"))
                
                # Print header
                click.echo(f"{'NAME':<{name_width}}  {'VERSION':<{version_width}}  DESCRIPTION")
                click.echo("-" * (name_width + version_width + 50))
                
                # Print skills
                for name, info in skills.items():
                    desc = info.get('description', '')
                    # Truncate description if too long
                    if len(desc) > 47:
                        desc = desc[:44] + "..."
                    click.echo(f"{name:<{name_width}}  {info.get('version', 'unknown'):<{version_width}}  {desc}")
        except StoreError as e:
            raise click.ClickException(str(e))
    else:
        # Project skills
        packs = discover_packs(Path("."))
        
        # Apply filter
        if filter:
            packs = [p for p in packs if filter.lower() in p.name.lower()]
        
        if not packs:
            click.echo("No skills found.")
            return
        
        if json_flag:
            payload = [
                {"name": p.name, "version": p.version, "path": str(p.root)}
                for p in packs
            ]
            click.echo(yaml.dump(payload, sort_keys=False))
        else:
            # Check which skills are from global store
            store = Store()
            global_skills = store.list_skills()
            
            # Calculate column widths
            name_width = max(len(p.name) for p in packs)
            name_width = max(name_width, len("NAME"))
            version_width = max(len(p.version) for p in packs)
            version_width = max(version_width, len("VERSION"))
            
            # Print header
            click.echo(f"{'NAME':<{name_width}}  {'VERSION':<{version_width}}  SOURCE     PATH")
            click.echo("-" * (name_width + version_width + 50))
            
            # Print skills
            for p in packs:
                source = "global" if p.name in global_skills else "local"
                click.echo(f"{p.name:<{name_width}}  {p.version:<{version_width}}  {source:<9}  {p.root}")


# Project commands
@project.command("use")
@click.argument("name")
@click.option("--project", "-p", default=".", help="Project directory")
@click.pass_context
def use_project(ctx, name, project):
    """Use skill in project."""
    project_path = Path(project).resolve()
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would use skill {name} in project {project_path}")
        return
    
    try:
        proj = Project(project_path)
        store = Store()
        proj.use_skill(name, store)
        click.echo(f"Using skill '{name}' in project")
    except (ProjectError, StoreError) as e:
        raise click.ClickException(str(e))


@project.command("drop")
@click.argument("name")
@click.option("--project", "-p", default=".", help="Project directory")
@click.pass_context
def drop_project(ctx, name, project):
    """Drop skill from project."""
    project_path = Path(project).resolve()
    
    if not click.confirm(f"Are you sure you want to drop skill '{name}'?"):
        click.echo("Operation cancelled.")
        return
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would drop skill {name} from project {project_path}")
        return
    
    try:
        proj = Project(project_path)
        proj.drop_skill(name)
        click.echo(f"Dropped skill '{name}' from project")
    except ProjectError as e:
        raise click.ClickException(str(e))


# Adapter commands
@adapter.command()
@click.option("--windsurf", is_flag=True, help="Generate Windsurf workflows")
@click.option("--cursor", is_flag=True, help="Generate Cursor rules")
@click.option("--clean", is_flag=True, help="Remove existing adapters")
@click.option("--skills-dir", default="skills", help="Skills directory")
@click.pass_context
def generate(ctx, windsurf, cursor, clean, skills_dir):
    """Generate IDE adapters."""
    skills_path = Path(skills_dir)
    if not skills_path.exists():
        raise click.BadParameter(f"Skills directory does not exist: {skills_dir}")
    
    generator = AdapterGenerator(skills_path, Path.cwd())
    
    if clean:
        if ctx.obj["dry_run"]:
            click.echo("Would remove existing adapters")
            return
        click.echo("Removing existing adapters...")
        generator.clean()
        return
    
    if not windsurf and not cursor:
        # Auto-detect
        if Path(".windsurf").exists():
            windsurf = True
        if Path(".cursor").exists():
            cursor = True
    
    if not windsurf and not cursor:
        raise click.UsageError("No IDE detected. Use --windsurf or --cursor flag.")
    
    if windsurf:
        if ctx.obj["dry_run"]:
            click.echo("Would generate Windsurf adapters")
        else:
            click.echo("Generating Windsurf adapters...")
            count = generator.generate_windsurf()
            click.echo(f"Generated {count} workflow(s)")
    
    if cursor:
        if ctx.obj["dry_run"]:
            click.echo("Would generate Cursor adapters")
        else:
            click.echo("Generating Cursor adapters...")
            count = generator.generate_cursor()
            click.echo(f"Generated {count} rule(s)")


# Utility commands
@util.command()
@click.option("--output", "-o", help="Output file path")
@click.pass_context
def index(ctx, output):
    """Generate agent-optimized .INDEX.md for skills."""
    if output:
        output_path = Path(output)
        if output_path.exists() and not click.confirm(f"File {output} exists. Overwrite?"):
            click.echo("Operation cancelled.")
            return
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would generate index{f' to {output}' if output else ''}")
        return
    
    click.echo("Generating index...")
    # TODO: Implement index generation


# Validation command
@cli.command()
@click.argument("target")
@click.option("--json", "json_flag", is_flag=True, help="Output as JSON")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed validation report")
@click.pass_context
def validate(ctx, target, json_flag, verbose):
    """Validate skill against Agent Skills spec."""
    target_path = Path(target)
    
    # Validate input
    if not target_path.exists():
        raise click.BadParameter(f"Path does not exist: {target}")
    
    if ctx.obj["dry_run"]:
        click.echo(f"Would validate {target}")
        return
    
    # Run validation
    code, report = validate_target(target_path)
    
    # Output results
    if json_flag:
        click.echo(format_json(report))
    else:
        click.echo(format_human(report))
        if verbose and code > 0:
            click.echo("\nDetailed errors:")
            for error in report.get("errors", []):
                click.echo(f"  - {error}")
    
    sys.exit(code)


# Help command
@cli.command("help")
@click.argument("command", required=False)
@click.argument("subcommand", required=False)
@click.pass_context
def help_cmd(ctx, command, subcommand):
    """Show detailed help for commands."""
    if not command:
        click.echo(cli.get_help(ctx))
        return
    
    # Find the command group
    cmd_group = None
    for cmd in ["global", "project", "adapter", "util"]:
        if command.startswith(cmd):
            cmd_group = cli.get_command(ctx, cmd)
            if cmd_group and subcommand:
                # Show help for subcommand
                sub_cmd = cmd_group.get_command(ctx, subcommand)
                if sub_cmd:
                    click.echo(sub_cmd.get_help(ctx))
                    return
            break
    
    if cmd_group:
        click.echo(cmd_group.get_help(ctx))
    else:
        click.echo(f"Unknown command: {command}")
        click.echo("Available commands: global-, project, adapter, util, validate, help")


def main():
    """Entry point for the CLI."""
    try:
        # Initialize store on first run
        store = Store()
        if not store.is_initialized():
            store.ensure_exists()
        cli()
    except Exception as e:
        log.error("Unexpected error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
