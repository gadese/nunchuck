$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

function Show-Help {
    @"
md-split - Split a markdown file by H2 headings

Commands:
  help
  validate

Usage:
  md-split -in <source.md> [-out <dir>] [-prefix <NN>] [-dryRun] [-force] [-noIntro]
  md-split help
  md-split validate

Deterministic behavior:
- Runs scripts/split.ps1 to generate chunk files and .SPLIT.json
- Runs scripts/index.ps1 to generate .INDEX.md
"@
}

function Invoke-Validate {
    $errors = 0

    $split = Join-Path $ScriptDir "split.ps1"
    $index = Join-Path $ScriptDir "index.ps1"

    if (-not (Test-Path $split)) {
        Write-Error "error: missing $split"
        $errors++
    }

    if (-not (Test-Path $index)) {
        Write-Error "error: missing $index"
        $errors++
    }

    if ($errors -gt 0) {
        exit 1
    }

    Write-Output "ok: md-split skill is runnable"
}

function Invoke-SplitAndIndex {
    param([string[]]$Arguments)

    # Pass args through to split.ps1
    & (Join-Path $ScriptDir "split.ps1") @Arguments

    # Derive output directory (split.ps1 default behavior)
    $inFile = $null
    $outDir = $null

    for ($i = 0; $i -lt $Arguments.Count; $i++) {
        if ($Arguments[$i] -eq "-in") {
            $inFile = $Arguments[$i + 1]
        }
        if ($Arguments[$i] -eq "-out") {
            $outDir = $Arguments[$i + 1]
        }
    }

    if (-not $outDir) {
        if (-not $inFile) {
            Write-Error "error: -in is required"
            exit 1
        }
        $item = Get-Item $inFile
        $baseName = $item.BaseName.ToLower()
        $outDir = Join-Path $item.DirectoryName $baseName
    }

    & (Join-Path $ScriptDir "index.ps1") -dir $outDir
}

$command = if ($args.Count -gt 0) { $args[0] } else { "" }

switch ($command) {
    "help" { Show-Help }
    "validate" { Invoke-Validate }
    default { Invoke-SplitAndIndex -Arguments $args }
}
