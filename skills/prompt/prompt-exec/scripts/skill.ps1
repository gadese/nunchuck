$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

$ConfigPath = Join-Path $ScriptDir ".config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
}

function Show-Help {
    @"
prompt-exec - Execute the forged prompt exactly as written

Commands:
  help
  validate

Usage:
  prompt-exec [--dry-run]
  prompt-exec help
  prompt-exec validate

Deterministic behavior:
- Requires .prompt/active.yaml exists
- Requires artifact status is ready
- Writes receipt to .prompt/receipts/
- Deletes .prompt/active.yaml after successful execution
- Prints the prompt text to execute
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

    $cli = Join-Path $IncludeDir "prompt_exec_cli.py"
    if (-not (Test-Path $cli)) {
        Write-Error "error: missing $cli"
        $errors++
    }

    if ($errors -gt 0) {
        exit 1
    }

    Write-Output "ok: prompt-exec skill is runnable"
}

function Invoke-Run {
    param([string[]]$Arguments)

    Push-Location $IncludeDir
    try {
        & uv run python prompt_exec_cli.py @Arguments
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
