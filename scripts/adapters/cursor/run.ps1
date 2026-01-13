param(
  [string]$SkillsRoot = "skills",
  [string]$OutputRoot = "."
)

function Get-Usage {
@"
Usage:
  scripts/adapters/windows/cursor.ps1 [-SkillsRoot <dir>] [-OutputRoot <dir>]

Generates Cursor commands into:
  <OutputRoot>/.cursor/commands/

Defaults:
  SkillsRoot = skills
  OutputRoot = .
"@
}

if ($SkillsRoot -eq "-h" -or $SkillsRoot -eq "--help") {
  Get-Usage
  exit 0
}

if (!(Test-Path -LiteralPath $SkillsRoot -PathType Container)) {
  Write-Error "Skills root not found: $SkillsRoot"
  exit 1
}

$skillsRootAbs = (Resolve-Path -LiteralPath $SkillsRoot).Path
$outDir = Join-Path $OutputRoot ".cursor/commands"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

function Get-FrontmatterDescription([string]$path) {
  $lines = Get-Content -LiteralPath $path

  $inFm = $false
  $fmCount = 0
  $inDesc = $false
  $descLines = New-Object System.Collections.Generic.List[string]

  foreach ($line in $lines) {
    if ($line.Trim() -eq "---") {
      $fmCount++
      if ($fmCount -eq 1) { $inFm = $true; continue }
      if ($fmCount -eq 2) { break }
    }

    if (-not $inFm) { continue }

    if ($inDesc) {
      if ($line -match '^[^\s][^:]*:\s*') {
        $inDesc = $false
      } else {
        $descLines.Add(($line -replace '^\s+', '').TrimEnd())
        continue
      }
    }

    if ($line -match '^description:\s*(.*)$') {
      $val = $Matches[1].Trim()
      if ($val -eq '>' -or $val -eq '|') {
        $inDesc = $true
        continue
      }
      return $val.Trim('"').Trim("'")
    }
  }

  return ($descLines -join ' ').Trim()
}

$count = 0
Get-ChildItem -LiteralPath $SkillsRoot -Recurse -Filter "SKILL.md" -File | ForEach-Object {
  $skillDir = $_.Directory.FullName
  $name = Split-Path $skillDir -Leaf

  $relDir = $skillDir.Substring($skillsRootAbs.Length).TrimStart('\','/')

  $desc = (Get-FrontmatterDescription $_.FullName) -replace '\s+', ' '
  $cmdFile = Join-Path $outDir ("$name.md")

  $content = @(
    "# $name",
    "",
    $desc,
    "",
    "This command delegates to the agent skill at `$SkillsRoot/$relDir/`." ,
    "",
    "## Skill Root",
    "",
    "- **Path:** `$skillsRootAbs/`",
    "",
    "## Skill Location",
    "",
    "- **Path:** `$skillsRootAbs/$relDir/`",
    "- **Manifest:** `$skillsRootAbs/$relDir/SKILL.md`",
    ""
  ) -join "`n"

  Set-Content -LiteralPath $cmdFile -Value $content -Encoding UTF8
  $count++
}

Write-Host "Generated $count command(s) in $outDir"
