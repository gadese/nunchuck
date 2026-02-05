param(
  [string]$SkillsRoot = "skills",
  [string]$OutputRoot = "."
)

function Get-Usage {
@"
Usage:
  scripts/adapters/windsurf/run.ps1 [-SkillsRoot <dir>] [-OutputRoot <dir>]

Generates Windsurf workflows into:
  <OutputRoot>/.windsurf/workflows/

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
$outDir = Join-Path $OutputRoot ".windsurf/workflows"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

# Ensure output reflects the current skill set (remove stale generated workflows).
$expected = @{}
Get-ChildItem -LiteralPath $SkillsRoot -Recurse -Filter "SKILL.md" -File | ForEach-Object {
  $skillDir = $_.Directory.FullName
  $name = Split-Path $skillDir -Leaf
  $expected[$name] = $true
}

Get-ChildItem -LiteralPath $outDir -File -Filter "*.md" -ErrorAction SilentlyContinue | ForEach-Object {
  $base = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
  if ($expected.ContainsKey($base)) { return }
  $content = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
  if ($content -and $content.Contains("This workflow delegates to the agent skill at")) {
    Remove-Item -LiteralPath $_.FullName -Force -ErrorAction SilentlyContinue
  }
}

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

  $relDir = $skillDir.Substring($skillsRootAbs.Length).TrimStart('\\','/')

  $desc = (Get-FrontmatterDescription $_.FullName) -replace '\s+', ' '
  $workflowFile = Join-Path $outDir ("$name.md")

  $yamlDesc = $desc.Replace('"','\\"')

  $content = @(
    "---",
    "description: \"$yamlDesc\"",
    "auto_execution_mode: 1",
    "---",
    "",
    "# $name",
    "",
    "This workflow delegates to the agent skill at `$skillsRootAbs/$relDir/`." ,
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

  Set-Content -LiteralPath $workflowFile -Value $content -Encoding UTF8
  $count++
}

Write-Host "Generated $count workflow(s) in $outDir"
