param(
  [Parameter(Mandatory = $true, Position = 0)]
  [string]$SearchTerm,

  [Parameter(Mandatory = $false)]
  [string]$Path = ".",

  [Parameter(Mandatory = $false)]
  [string]$Type = ""
)

$ErrorActionPreference = "Stop"

Write-Output "# Evidence Pointers for: '$SearchTerm'"
Write-Output ""
Write-Output "**Search Path:** `$Path`"
if ($Type -ne "") {
  Write-Output "**File Type:** `*.$Type`"
}
Write-Output "**Date:** $(Get-Date -Format o)"
Write-Output ""
Write-Output "---"
Write-Output ""

$files = @()
if ($Type -ne "") {
  $files = Get-ChildItem -Path $Path -Recurse -File -Filter "*.$Type" -ErrorAction SilentlyContinue
} else {
  $files = Get-ChildItem -Path $Path -Recurse -File -ErrorAction SilentlyContinue
}

$matches = @()
foreach ($f in $files) {
  try {
    $m = Select-String -Path $f.FullName -Pattern $SearchTerm -SimpleMatch -AllMatches -ErrorAction SilentlyContinue
    if ($m) {
      $matches += $m
    }
  } catch {
    # ignore unreadable/binary files
  }
}

Write-Output "## Matches"
Write-Output ""
Write-Output '```'
if ($matches.Count -gt 0) {
  $matches | Select-Object -First 50 | ForEach-Object { Write-Output "${($_.Path)}:${($_.LineNumber)}:${($_.Line)}" }
} else {
  Write-Output "No matches found."
}
Write-Output '```'
Write-Output ""

$filesWithMatches = $matches | Select-Object -ExpandProperty Path -Unique
Write-Output "**Files with matches:** $($filesWithMatches.Count)"
Write-Output ""

if ($filesWithMatches.Count -gt 0) {
  Write-Output "## Files"
  Write-Output ""
  $filesWithMatches | Select-Object -First 20 | ForEach-Object { Write-Output "- `$_`" }
  Write-Output ""
}

Write-Output "---"
Write-Output ""
Write-Output "Evidence pointers gathered. Use these locations for focused examination."
