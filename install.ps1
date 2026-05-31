# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#Requires -Version 5.1
<#
.SYNOPSIS
    Install Well-Architected steering and skills into your project for your AI coding tool.

.DESCRIPTION
    Windows-native installer for Well-Architected Skills & Steering.
    Supports the same tools and options as the bash install.sh script.

.PARAMETER TargetDir
    Project directory to install into (default: current directory)

.PARAMETER Tool
    Install only for specific tool(s). Can be specified multiple times.
    Valid: kiro, claude-code, cursor, codex, windsurf, github-copilot, cline, gemini-cli, antigravity, junie, amp, openclaw, devops-agent, all

.PARAMETER Symlink
    Use symlinks instead of copies (requires elevated permissions on Windows)

.PARAMETER Global
    Install to global config instead of project

.PARAMETER Force
    Overwrite existing files without prompting

.EXAMPLE
    .\install.ps1 -TargetDir C:\Projects\my-app -Tool claude-code

.EXAMPLE
    .\install.ps1 -Tool kiro, claude-code, cursor

.EXAMPLE
    .\install.ps1 -Tool all -Force
#>

param(
    [string]$TargetDir = ".",
    [string[]]$Tool = @("all"),
    [switch]$Symlink,
    [switch]$Global,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

function Copy-OrLink {
    param(
        [string]$Source,
        [string]$Destination
    )

    $destDir = Split-Path -Parent $Destination
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }

    if ((Test-Path $Destination) -and -not $Force) {
        $answer = Read-Host "  WARNING: $Destination already exists. Overwrite? [y/N]"
        if ($answer -notin @("y", "Y")) {
            Write-Host "  Skipped: $Destination"
            return
        }
    }

    if ($Symlink) {
        if (Test-Path $Destination) { Remove-Item $Destination -Force }
        New-Item -ItemType SymbolicLink -Path $Destination -Target $Source -Force | Out-Null
        Write-Host "  Linked: $Destination -> $Source"
    }
    else {
        if (Test-Path $Source -PathType Container) {
            Copy-Item -Path "$Source\*" -Destination $Destination -Recurse -Force
        }
        else {
            Copy-Item -Path $Source -Destination $Destination -Force
        }
        Write-Host "  Copied: $Destination"
    }
}

function Get-Skills {
    Get-ChildItem -Path "$ScriptDir\skills" -Directory | Where-Object { $_.Name -ne "_shared" }
}

function Install-Kiro {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for Kiro..."
    Copy-OrLink "$ScriptDir\steering\well-architected.md" "$base\.kiro\steering\well-architected.md"

    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\.kiro\skills\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. Kiro will load steering automatically and skills on demand.`n"
}

function Install-ClaudeCode {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for Claude Code..."
    Copy-OrLink "$ScriptDir\adapters\claude-code\CLAUDE.md" "$base\CLAUDE.md"

    foreach ($cmd in Get-ChildItem "$ScriptDir\adapters\claude-code\commands\*.md") {
        Copy-OrLink $cmd.FullName "$base\.claude\commands\$($cmd.Name)"
    }
    Write-Host "  Done. Use /wa-review, /security-assessment, etc. as slash commands.`n"
}

function Install-Cursor {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for Cursor..."
    foreach ($rule in Get-ChildItem "$ScriptDir\adapters\cursor\rules\*.md") {
        Copy-OrLink $rule.FullName "$base\.cursor\rules\$($rule.Name)"
    }

    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\.cursor\skills\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. The well-architected rule is always-on; wa-review activates on demand.`n"
}

function Install-Codex {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for Codex (OpenAI)..."
    Copy-OrLink "$ScriptDir\adapters\codex\AGENTS.md" "$base\AGENTS.md"

    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\skills\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. Codex will read AGENTS.md and reference skills/ on demand.`n"
}

function Install-Windsurf {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for Windsurf..."
    Copy-OrLink "$ScriptDir\adapters\windsurf\.windsurfrules" "$base\.windsurfrules"

    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\skills\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. Windsurf will load .windsurfrules automatically.`n"
}

function Install-GitHubCopilot {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for GitHub Copilot..."
    Copy-OrLink "$ScriptDir\adapters\github-copilot\.github\copilot-instructions.md" "$base\.github\copilot-instructions.md"
    Write-Host "  Done. Copilot will load instructions from .github/copilot-instructions.md.`n"
}

function Install-Cline {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for Cline..."
    Copy-OrLink "$ScriptDir\adapters\cline\.clinerules" "$base\.clinerules"

    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\skills\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. Cline will load .clinerules automatically.`n"
}

function Install-GeminiCli {
    $base = if ($Global) { "$env:USERPROFILE\.gemini" } else { $TargetDir }

    Write-Host "Installing for Gemini CLI..."
    Copy-OrLink "$ScriptDir\adapters\gemini-cli\GEMINI.md" "$base\GEMINI.md"

    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\skills\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. Gemini CLI will load GEMINI.md automatically.`n"
}

function Install-Antigravity {
    $base = if ($Global) { "$env:USERPROFILE\.gemini" } else { $TargetDir }

    if ($Global) {
        Write-Host "Installing for Antigravity (Global)..."
        Copy-OrLink "$ScriptDir\adapters\gemini-cli\GEMINI.md" "$base\GEMINI.md"
        foreach ($skill in Get-Skills) {
            Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\skills\$($skill.Name)\SKILL.md"
        }
        Write-Host "  Done. Global rules installed.`n"
    }
    else {
        Write-Host "Installing for Antigravity..."
        foreach ($rule in Get-ChildItem "$ScriptDir\adapters\antigravity\rules\*.md") {
            Copy-OrLink $rule.FullName "$base\.agents\rules\$($rule.Name)"
        }
        foreach ($skill in Get-Skills) {
            Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\.agents\skills\$($skill.Name)\SKILL.md"
        }
        Write-Host "  Done. Workspace rules in .agents/rules/ and skills in .agents/skills/.`n"
    }
}

function Install-Junie {
    $base = if ($Global) { $env:USERPROFILE } else { $TargetDir }

    Write-Host "Installing for Junie (JetBrains)..."
    Copy-OrLink "$ScriptDir\adapters\junie\guidelines.md" "$base\.junie\guidelines\well-architected.md"

    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$base\.junie\skills\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. Guidelines are always-on; skills activate on demand.`n"
}

function Install-Amp {
    $base = if ($Global) { "$env:USERPROFILE\.config\agents" } else { $TargetDir }

    Write-Host "Installing for Amp..."
    Copy-OrLink "$ScriptDir\adapters\amp\AGENTS.md" "$base\AGENTS.md"

    $skillsDir = if ($Global) { "$base\skills" } else { "$base\.agents\skills" }
    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$skillsDir\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. Amp will discover skills from .agents/skills/ automatically.`n"
}

function Install-OpenClaw {
    $base = if ($Global) { "$env:USERPROFILE\.openclaw\workspace" } else { $TargetDir }

    Write-Host "Installing for OpenClaw..."
    Copy-OrLink "$ScriptDir\adapters\openclaw\AGENTS.md" "$base\AGENTS.md"

    $skillsDir = if ($Global) { "$base\skills" } else { "$base\.agents\skills" }
    foreach ($skill in Get-Skills) {
        Copy-OrLink "$($skill.FullName)\SKILL.md" "$skillsDir\$($skill.Name)\SKILL.md"
    }
    Write-Host "  Done. OpenClaw will discover skills from .agents/skills/ automatically.`n"
}

function Install-DevOpsAgent {
    $base = if ($Global) { "$env:USERPROFILE\.devops-agent-skills" } else { $TargetDir }

    Write-Host "Installing for AWS DevOps Agent..."
    $outBase = "$base\devops-agent-skills"

    foreach ($skill in Get-Skills) {
        $outDir = "$outBase\$($skill.Name)"
        New-Item -ItemType Directory -Path "$outDir\assets" -Force | Out-Null

        Copy-OrLink "$($skill.FullName)\SKILL.md" "$outDir\SKILL.md"

        if (Test-Path "$($skill.FullName)\references") {
            foreach ($ref in Get-ChildItem "$($skill.FullName)\references\*") {
                Copy-OrLink $ref.FullName "$outDir\references\$($ref.Name)"
            }
        }

        if (Test-Path "$ScriptDir\assets") {
            Copy-Item -Path "$ScriptDir\assets\*" -Destination "$outDir\assets\" -Recurse -Force
            Write-Host "  Included shared assets in $($skill.Name)"
        }

        if (-not $Symlink) {
            Compress-Archive -Path "$outDir\*" -DestinationPath "$outBase\$($skill.Name).zip" -Force
            Write-Host "  Packaged: $outBase\$($skill.Name).zip"
        }
    }
    Write-Host "  Done. Upload .zip files to your DevOps Agent Space via the Operator Web App.`n"
}

# Main
Write-Host "================================================"
Write-Host " Well-Architected Skills & Steering Installer"
Write-Host "================================================"
Write-Host ""
Write-Host "Source:  $ScriptDir"
Write-Host "Target:  $TargetDir"
Write-Host "Mode:    $(if ($Symlink) { 'symlink' } else { 'copy' })"
Write-Host "Scope:   $(if ($Global) { 'global' } else { 'project' })"
Write-Host "Tools:   $($Tool -join ', ')"
Write-Host ""

$resolved = Resolve-Path $TargetDir -ErrorAction SilentlyContinue
if ($resolved) { $TargetDir = $resolved.Path }

$validTools = @("kiro", "claude-code", "cursor", "codex", "windsurf", "github-copilot", "cline", "gemini-cli", "antigravity", "junie", "amp", "openclaw", "devops-agent", "all")

foreach ($t in $Tool) {
    switch ($t) {
        "kiro"           { Install-Kiro }
        "claude-code"    { Install-ClaudeCode }
        "cursor"         { Install-Cursor }
        "codex"          { Install-Codex }
        "windsurf"       { Install-Windsurf }
        "github-copilot" { Install-GitHubCopilot }
        "cline"          { Install-Cline }
        "gemini-cli"     { Install-GeminiCli }
        "antigravity"    { Install-Antigravity }
        "junie"          { Install-Junie }
        "amp"            { Install-Amp }
        "openclaw"       { Install-OpenClaw }
        "devops-agent"   { Install-DevOpsAgent }
        "all" {
            Install-Kiro
            Install-ClaudeCode
            Install-Cursor
            Install-Codex
            Install-Windsurf
            Install-GitHubCopilot
            Install-Cline
            Install-GeminiCli
            Install-Antigravity
            Install-Junie
            Install-Amp
            Install-OpenClaw
            Install-DevOpsAgent
        }
        default {
            Write-Error "Unknown tool: $t`nValid options: $($validTools -join ', ')"
            exit 1
        }
    }
}

Write-Host "Installation complete!"
