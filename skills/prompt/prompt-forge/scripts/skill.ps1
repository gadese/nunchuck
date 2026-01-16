$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

$ConfigPath = Join-Path $ScriptDir ".config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
}

function Show-Help {
    @"
prompt-forge - Shape and stabilize intent into .prompt/active.yaml

Commands:
  help
  validate

Usage:
  prompt-forge [--mark-ready] [--force]
  prompt-forge help
  prompt-forge validate

Deterministic behavior:
- Ensures .prompt/active.yaml exists (creates it if missing)
- Prints current artifact status
- Optionally marks artifact ready (requires no open questions unless --force, and requires a prompt)
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

    $cli = Join-Path $IncludeDir "prompt_forge_cli.py"
    if (-not (Test-Path $cli)) {
        Write-Error "error: missing $cli"
        $errors++
    }

    if ($errors -gt 0) {
        exit 1
    }

    Write-Output "ok: prompt-forge skill is runnable"
}

function Invoke-Run {
    param([string[]]$Arguments)

    Push-Location $IncludeDir
    try {
        & uv run python prompt_forge_cli.py @Arguments
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
