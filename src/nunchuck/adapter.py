"""Adapter generation for IDEs."""

import os
import re
import shutil
from pathlib import Path
from typing import List, Optional

import yaml

from .frontmatter import read_frontmatter


class AdapterGenerator:
    """Generates IDE adapters from agent skills."""
    
    def __init__(self, skills_dir: Path, output_dir: Path):
        """Initialize adapter generator.
        
        Args:
            skills_dir: Directory containing skills
            output_dir: Output directory for adapters
        """
        self.skills_dir = skills_dir
        self.output_dir = output_dir
        self.skip_patterns = ["^index$", "index-skills", "adapter"]
    
    def generate_windsurf(self) -> int:
        """Generate Windsurf workflows.
        
        Returns:
            Number of workflows generated
        """
        workflows_dir = self.output_dir / ".windsurf" / "workflows"
        workflows_dir.mkdir(parents=True, exist_ok=True)
        
        count = 0
        for skill_file in self.skills_dir.rglob("SKILL.md"):
            rel_path = skill_file.relative_to(self.skills_dir)
            skill_dir = rel_path.parent
            
            # Skip meta-skills
            if any(re.match(pattern, skill_dir.name) for pattern in self.skip_patterns):
                continue
            
            workflow_file = workflows_dir / f"{skill_dir.name}.md"
            self._generate_windsurf_workflow(skill_file, rel_path, skill_dir, workflow_file)
            count += 1
        
        return count
    
    def _generate_windsurf_workflow(self, skill_file: Path, rel_path: Path, skill_dir: Path, workflow_file: Path):
        """Generate a single Windsurf workflow."""
        try:
            fm = read_frontmatter(skill_file)
        except Exception:
            return
        
        name = fm.get("name")
        if not name:
            return
        
        desc = fm.get("description", "")
        
        # Collect keywords
        keywords = fm.get("keywords", [])
        keywords_str = ", ".join(keywords) if keywords else ""
        
        # Collect references
        refs = fm.get("references", [])
        refs_str = "\n".join(f"   - {ref}" for ref in refs) if refs else ""
        
        # Check for scripts directory
        has_scripts = skill_file.parent.joinpath("scripts").exists()
        
        # Generate the workflow
        lines = [
            "---",
            f"description: {desc}",
            "auto_execution_mode: 1",
            "---",
            "",
            f"# {name}",
            "",
            f"This workflow delegates to the agent skill at `skills/{skill_dir}/`.",
            "",
            "## Instructions",
            "",
            "1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`",
            "2. Read all references listed in `metadata.references` in order:",
        ]
        
        if refs_str:
            lines.append(refs_str)
        
        if has_scripts:
            lines.extend([
                "3. If scripts are present in `scripts/`, follow any automated steps first",
                "4. Execute the skill procedure as documented",
                "5. Produce output in the format specified by the skill",
            ])
        else:
            lines.extend([
                "3. Execute the skill procedure as documented",
                "4. Produce output in the format specified by the skill",
            ])
        
        lines.extend([
            "",
            "## Skill Location",
            "",
            f"- **Path:** `skills/{skill_dir}/`",
            "- **References:** `references/`",
        ])
        
        if has_scripts:
            lines.append("- **Scripts:** `scripts/`")
        
        lines.append("")
        
        # Add skillset-specific info
        if fm.get("skillset") and fm.get("skills"):
            members = fm.get("skills", [])
            members_str = ", ".join(members) if members else ""
            
            lines.extend([
                "## Skillset",
                "",
                "This is an orchestrator skill with member skills.",
                "",
                f"- **Members:** {members_str}",
            ])
            
            # Add pipeline info
            pipelines = fm.get("pipelines", {})
            default_pipeline = pipelines.get("default", [])
            if default_pipeline:
                pipeline_str = " -> ".join(default_pipeline)
                lines.append(f"- **Default Pipeline:** {pipeline_str}")
            
            lines.extend([
                "",
                "To run the full pipeline, invoke this workflow.",
                "To run individual skills, use their specific workflows.",
                "",
            ])
        
        if keywords_str:
            lines.extend([
                "## Keywords",
                "",
                f"`{keywords_str}`",
            ])
        
        # Write workflow file
        workflow_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    
    def generate_cursor(self) -> int:
        """Generate Cursor rules.
        
        Returns:
            Number of rules generated
        """
        rules_dir = self.output_dir / ".cursor" / "rules"
        rules_dir.mkdir(parents=True, exist_ok=True)
        
        count = 0
        for skill_file in self.skills_dir.rglob("SKILL.md"):
            rel_path = skill_file.relative_to(self.skills_dir)
            skill_dir = rel_path.parent
            
            # Skip meta-skills
            if any(re.match(pattern, skill_dir.name) for pattern in self.skip_patterns):
                continue
            
            rule_file = rules_dir / f"{skill_dir.name}.md"
            self._generate_cursor_rule(skill_file, rel_path, skill_dir, rule_file)
            count += 1
        
        return count
    
    def _generate_cursor_rule(self, skill_file: Path, rel_path: Path, skill_dir: Path, rule_file: Path):
        """Generate a single Cursor rule."""
        try:
            fm = read_frontmatter(skill_file)
        except Exception:
            return
        
        name = fm.get("name")
        if not name:
            return
        
        desc = fm.get("description", "")
        
        # Generate the rule
        lines = [
            f"# {name}",
            "",
            desc,
            "",
            f"When working with this skill, refer to the implementation in `skills/{skill_dir}/`.",
            "",
            "## Key Points",
            "",
            "- Follow the skill manifest in SKILL.md",
            "- Use the provided references for guidance",
            "- Execute procedures as documented",
        ]
        
        # Add skillset info if applicable
        if fm.get("skillset") and fm.get("skills"):
            members = fm.get("skills", [])
            members_str = ", ".join(members) if members else ""
            
            lines.extend([
                "",
                "## Member Skills",
                "",
                f"This skillset includes: {members_str}",
                "",
                "Each member skill has its own workflow and can be invoked individually.",
            ])
        
        lines.append("")
        
        # Write rule file
        rule_file.write_text("\n".join(lines), encoding="utf-8")
    
    def clean(self) -> None:
        """Clean generated adapters."""
        # Clean Windsurf workflows
        windsurf_dir = self.output_dir / ".windsurf"
        if windsurf_dir.exists():
            shutil.rmtree(windsurf_dir)
        
        # Clean Cursor rules
        cursor_dir = self.output_dir / ".cursor"
        if cursor_dir.exists():
            shutil.rmtree(cursor_dir)
