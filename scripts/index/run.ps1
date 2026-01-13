<#
.SYNOPSIS
  Generate .SKILLS.md containing a simple list of skills (name + description)

.DESCRIPTION
  Scans skills/**/SKILL.md and extracts frontmatter fields:
    - name
    - description

  Output is written to .SKILLS.md.

.PARAMETER dir
  Output directory for .SKILLS.md (default: current directory)
#>

[CmdletBinding()]
param (
  [Alias('d')]
  [string]$dir
)

$ErrorActionPreference = "Stop"

$outDir = if ($dir) { $dir } else { (Get-Location).Path }
if (-not (Test-Path -LiteralPath $outDir)) {
  Write-Error "Output directory not found: $outDir"
  exit 2
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $scriptDir "../.."))
$skillsDir = Join-Path $repoRoot "skills"

if (-not (Test-Path -LiteralPath $skillsDir)) {
  Write-Error "Skills directory not found: $skillsDir"
  exit 2
}

function Get-SkillFrontmatterEntry {
  param(
    [Parameter(Mandatory=$true)]
    [string]$path
  )

  $lines = Get-Content -LiteralPath $path
  if ($lines.Count -lt 3 -or $lines[0] -ne "---") {
    return $null
  }

  $name = $null
  $descParts = @()
  $inFrontmatter = $true
  $inDescBlock = $false

  for ($i = 1; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]

    if ($inFrontmatter -and $line -eq "---") {
      break
    }

    if ($inDescBlock) {
      if ($line -match '^[\s]+') {
        $descParts += ($line -replace '^[\s]+', '')
        continue
      } else {
        $inDescBlock = $false
      }
    }

    if ($line -match '^name:\s*(.+)$') {
      $name = $Matches[1].Trim()
      continue
    }

    if ($line -match '^description:\s*(\>|\|)\s*$') {
      $descParts = @()
      $inDescBlock = $true
      continue
    }

    if ($line -match '^description:\s*(.+)$') {
      $descParts = @($Matches[1].Trim())
      $inDescBlock = $false
      continue
    }
  }

  if (-not $name) {
    return $null
  }

  $desc = ($descParts -join ' ').Trim()
  $desc = ($desc -replace '\s+', ' ').Trim()

  [PSCustomObject]@{
    Name = $name
    Description = $desc
  }
}

$skillFiles = Get-ChildItem -LiteralPath $skillsDir -Recurse -File -Filter "SKILL.md"
$entries = @()
foreach ($sf in $skillFiles) {
  $e = Get-SkillFrontmatterEntry -path $sf.FullName
  if ($e) {
    $entries += $e
  }
}

$entries = $entries | Sort-Object Name

$outFile = Join-Path $outDir ".SKILLS.md"

"# Skills" | Out-File -LiteralPath $outFile -Encoding utf8
foreach ($e in $entries) {
  if ($e.Description) {
    "- ``$($e.Name)`` - $($e.Description)" | Out-File -LiteralPath $outFile -Append -Encoding utf8
  } else {
    "- ``$($e.Name)``" | Out-File -LiteralPath $outFile -Append -Encoding utf8
  }
}
