$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

$ConfigPath = Join-Path $ScriptDir ".config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
}

function Show-Help {
    @"
prompt-compile - Compile .prompt/active.yaml into .prompt/PROMPT.md

Commands:
  help
  validate

Usage:
  prompt-compile [--force] [--dry-run]
  prompt-compile help
  prompt-compile validate

Deterministic behavior:
- Verifies active artifact exists
- Validates artifact (unless --force)
- Writes .prompt/PROMPT.md (unless --dry-run)
- Preserves active artifact
"@
}

function Invoke-Validate {
    $errors = 0

    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Error "error: uv not found. Install from https://docs.astral.sh/uv/"
        $errors++
    }

    $pyproject = Join-Path $IncludeDir "pyproject.toml"
    if (-not (Test-Path $pyproject)) {
        Write-Error "error: missing $pyproject"
        $errors++
    }

    $cli = Join-Path $IncludeDir "prompt_compile_cli.py"
    if (-not (Test-Path $cli)) {
        Write-Error "error: missing $cli"
        $errors++
    }

    if ($errors -gt 0) {
        exit 1
    }

    Write-Output "ok: prompt-compile skill is runnable"
}

function Invoke-Run {
    param([string[]]$Arguments)

    Push-Location $IncludeDir
    try {
        & uv run python prompt_compile_cli.py @Arguments
    } finally {
        Pop-Location
    }
}

$command = if ($args.Count -gt 0) { $args[0] } else { "" }

switch ($command) {
    "help" { Show-Help }
    "validate" { Invoke-Validate }
    default { Invoke-Run -Arguments $args }
}
