$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = (Resolve-Path (Join-Path $ScriptDir "..\.." )).Path

$env:PYTHONPATH = (Join-Path $RepoRoot "src")

python -m nunchuck validate $RepoRoot
