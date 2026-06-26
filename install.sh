#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="."

VERSION="1.3.0"

usage() {
  cat <<EOF
Usage: ./install.sh [TARGET_DIR] [OPTIONS]

Install Well-Architected steering and skills into your project for your AI coding tool.

Arguments:
  TARGET_DIR    Project directory to install into (default: current directory)

Options:
  --tool TOOL   Install only for a specific tool. Can be repeated.
                Valid: kiro, kiro-cli, claude-code, cursor, codex, windsurf, github-copilot, cline, gemini-cli, antigravity, junie, amp, openclaw, devops-agent, auto, all
  --uninstall   Remove previously installed WA files from the target directory
  --check-update  Check if a newer version is available on GitHub
  --symlink     Use symlinks instead of copies (auto-updates when this repo changes)
  --global      Install to global config (~/.kiro, ~/.claude, etc.) instead of project
  --force       Overwrite existing files without prompting
  --help        Show this help message

Examples:
  ./install.sh ~/my-project --tool auto
  ./install.sh ~/my-project --tool kiro --tool claude-code
  ./install.sh ~/my-project --tool all
  ./install.sh ~/my-project --tool cursor --symlink
  ./install.sh --global --tool claude-code
  ./install.sh ~/my-project --tool all --force
  ./install.sh ~/my-project --uninstall --tool claude-code
  ./install.sh --check-update
EOF
  exit 0
}

TOOLS=()
SYMLINK=false
GLOBAL=false
FORCE=false
UNINSTALL=false
CHECK_UPDATE=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --tool)
      TOOLS+=("$2")
      shift 2
      ;;
    --symlink)
      SYMLINK=true
      shift
      ;;
    --global)
      GLOBAL=true
      shift
      ;;
    --force)
      FORCE=true
      shift
      ;;
    --uninstall)
      UNINSTALL=true
      shift
      ;;
    --check-update)
      CHECK_UPDATE=true
      shift
      ;;
    --help|-h)
      usage
      ;;
    *)
      TARGET_DIR="$1"
      shift
      ;;
  esac
done

if [[ ${#TOOLS[@]} -eq 0 ]]; then
  TOOLS=("all")
fi

TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd || echo "$TARGET_DIR")"

copy_or_link() {
  local src="$1"
  local dest="$2"

  mkdir -p "$(dirname -- "$dest")"

  if [[ -e "$dest" || -L "$dest" ]] && [[ "$FORCE" != true ]]; then
    echo "  WARNING: $dest already exists."
    printf "  Overwrite? [y/N] "
    read -r answer
    if [[ "$answer" != "y" && "$answer" != "Y" ]]; then
      echo "  Skipped: $dest"
      return 0
    fi
  fi

  if [[ "$SYMLINK" == true ]]; then
    ln -sf "$src" "$dest"
    echo "  Linked: $dest -> $src"
  else
    if [[ -d "$src" ]]; then
      cp -r "$src/." "$dest/"
    else
      cp "$src" "$dest"
    fi
    echo "  Copied: $dest"
  fi
}

copy_skill_references() {
  local skill_dir="$1"
  local dest_dir="$2"
  if [[ -d "$skill_dir/references" ]]; then
    # Recurse through references/ so nested content (questions/, lenses/, etc.)
    # is installed too, preserving the relative directory structure. A flat
    # top-level-only copy would silently drop the entire reference corpus.
    while IFS= read -r -d '' ref_file; do
      local rel="${ref_file#"$skill_dir"/references/}"
      copy_or_link "$ref_file" "$dest_dir/references/$rel"
    done < <(find "$skill_dir/references" -type f -print0)
  fi
}

install_kiro() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for Kiro..."
  copy_or_link "$SCRIPT_DIR/steering/well-architected.md" "$base/.kiro/steering/well-architected.md"

  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/.kiro/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/.kiro/skills/$skill_name"
  done
  echo "  Done. Kiro will load steering automatically and skills on demand."
  echo ""
}

install_claude_code() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for Claude Code..."
  copy_or_link "$SCRIPT_DIR/adapters/claude-code/CLAUDE.md" "$base/CLAUDE.md"

  mkdir -p "$base/.claude/commands"
  for cmd_file in "$SCRIPT_DIR/adapters/claude-code/commands"/*.md; do
    local cmd_name
    cmd_name="$(basename "$cmd_file")"
    copy_or_link "$cmd_file" "$base/.claude/commands/$cmd_name"
  done

  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/.claude/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/.claude/skills/$skill_name"
  done
  echo "  Done. Skills installed to .claude/skills/; slash commands also available."
  echo ""
}

install_cursor() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for Cursor..."
  mkdir -p "$base/.cursor/rules"
  for rule_file in "$SCRIPT_DIR/adapters/cursor/rules"/*.md; do
    local rule_name
    rule_name="$(basename "$rule_file")"
    copy_or_link "$rule_file" "$base/.cursor/rules/$rule_name"
  done

  mkdir -p "$base/.cursor/skills"
  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/.cursor/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/.cursor/skills/$skill_name"
  done
  echo "  Done. The well-architected rule is always-on; wa-review activates on demand."
  echo ""
}

install_codex() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for Codex (OpenAI)..."
  copy_or_link "$SCRIPT_DIR/adapters/codex/AGENTS.md" "$base/AGENTS.md"

  mkdir -p "$base/skills"
  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/skills/$skill_name"
  done
  echo "  Done. Codex will read AGENTS.md and reference skills/ on demand."
  echo ""
}

install_windsurf() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for Windsurf..."
  copy_or_link "$SCRIPT_DIR/adapters/windsurf/.windsurfrules" "$base/.windsurfrules"

  mkdir -p "$base/skills"
  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/skills/$skill_name"
  done
  echo "  Done. Windsurf will load .windsurfrules automatically."
  echo ""
}

install_github_copilot() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for GitHub Copilot..."
  mkdir -p "$base/.github"
  copy_or_link "$SCRIPT_DIR/adapters/github-copilot/.github/copilot-instructions.md" "$base/.github/copilot-instructions.md"
  echo "  Done. Copilot will load instructions from .github/copilot-instructions.md."
  echo ""
}

install_cline() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for Cline..."
  copy_or_link "$SCRIPT_DIR/adapters/cline/.clinerules" "$base/.clinerules"

  mkdir -p "$base/skills"
  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/skills/$skill_name"
  done
  echo "  Done. Cline will load .clinerules automatically."
  echo ""
}

install_gemini_cli() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME/.gemini"
  fi

  echo "Installing for Gemini CLI..."
  copy_or_link "$SCRIPT_DIR/adapters/gemini-cli/GEMINI.md" "$base/GEMINI.md"

  mkdir -p "$base/skills"
  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/skills/$skill_name"
  done
  echo "  Done. Gemini CLI will load GEMINI.md automatically and reference skills/ on demand."
  echo ""
}

install_antigravity() {
  local base="$TARGET_DIR"

  if [[ "$GLOBAL" == true ]]; then
    echo "Installing for Antigravity (Global)..."
    copy_or_link "$SCRIPT_DIR/adapters/gemini-cli/GEMINI.md" "$HOME/.gemini/GEMINI.md"

    mkdir -p "$HOME/.gemini/skills"
    for skill_dir in "$SCRIPT_DIR/skills"/*/; do
      local skill_name
      skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
      copy_or_link "$skill_dir/SKILL.md" "$HOME/.gemini/skills/$skill_name/SKILL.md"
      copy_skill_references "$skill_dir" "$HOME/.gemini/skills/$skill_name"
    done
    echo "  Done. Global rules installed to ~/.gemini/GEMINI.md."
  else
    echo "Installing for Antigravity..."
    mkdir -p "$base/.agents/rules"
    for rule_file in "$SCRIPT_DIR/adapters/antigravity/rules"/*.md; do
      local rule_name
      rule_name="$(basename "$rule_file")"
      copy_or_link "$rule_file" "$base/.agents/rules/$rule_name"
    done

    mkdir -p "$base/.agents/skills"
    for skill_dir in "$SCRIPT_DIR/skills"/*/; do
      local skill_name
      skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
      copy_or_link "$skill_dir/SKILL.md" "$base/.agents/skills/$skill_name/SKILL.md"
      copy_skill_references "$skill_dir" "$base/.agents/skills/$skill_name"
    done
    echo "  Done. Workspace rules in .agents/rules/ and skills in .agents/skills/."
  fi
  echo ""
}

install_junie() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME"
  fi

  echo "Installing for Junie (JetBrains)..."
  copy_or_link "$SCRIPT_DIR/adapters/junie/guidelines.md" "$base/.junie/guidelines/well-architected.md"

  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$base/.junie/skills/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$base/.junie/skills/$skill_name"
  done
  echo "  Done. Guidelines are always-on; skills activate on demand."
  echo ""
}

install_amp() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME/.config/agents"
  fi

  echo "Installing for Amp..."
  copy_or_link "$SCRIPT_DIR/adapters/amp/AGENTS.md" "$base/AGENTS.md"

  mkdir -p "$base/.agents/skills" 2>/dev/null || mkdir -p "$base/skills"
  local skills_dir="$base/.agents/skills"
  if [[ "$GLOBAL" == true ]]; then
    skills_dir="$base/skills"
  fi

  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$skills_dir/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$skills_dir/$skill_name"
  done
  echo "  Done. Amp will discover skills from .agents/skills/ automatically."
  echo ""
}

install_openclaw() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME/.openclaw/workspace"
  fi

  echo "Installing for OpenClaw..."
  copy_or_link "$SCRIPT_DIR/adapters/openclaw/AGENTS.md" "$base/AGENTS.md"

  mkdir -p "$base/.agents/skills" 2>/dev/null || mkdir -p "$base/skills"
  local skills_dir="$base/.agents/skills"
  if [[ "$GLOBAL" == true ]]; then
    skills_dir="$base/skills"
  fi

  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue
    copy_or_link "$skill_dir/SKILL.md" "$skills_dir/$skill_name/SKILL.md"
    copy_skill_references "$skill_dir" "$skills_dir/$skill_name"
  done
  echo "  Done. OpenClaw will discover skills from .agents/skills/ automatically."
  echo ""
}

install_devops_agent() {
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    base="$HOME/.devops-agent-skills"
  fi

  echo "Installing for AWS DevOps Agent..."
  mkdir -p "$base/devops-agent-skills"

  for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "_shared" ]] && continue

    local out_dir="$base/devops-agent-skills/$skill_name"
    mkdir -p "$out_dir/assets"

    copy_or_link "$skill_dir/SKILL.md" "$out_dir/SKILL.md"

    copy_skill_references "$skill_dir" "$out_dir"

    if [[ -d "$skill_dir/assets" ]]; then
      for asset_file in "$skill_dir/assets"/*; do
        [[ -f "$asset_file" ]] && copy_or_link "$asset_file" "$out_dir/assets/$(basename "$asset_file")"
      done
    fi

    if [[ -d "$SCRIPT_DIR/assets" ]]; then
      cp -r "$SCRIPT_DIR/assets/." "$out_dir/assets/"
      echo "  Included shared assets in $skill_name"
    fi

    if [[ "$SYMLINK" != true ]]; then
      (cd "$base/devops-agent-skills" && zip -qr "$base/devops-agent-skills/$skill_name.zip" "$skill_name/")
      echo "  Packaged: $base/devops-agent-skills/$skill_name.zip"
    fi
  done
  echo "  Done. Upload .zip files to your DevOps Agent Space via the Operator Web App."
  echo ""
}

detect_tools() {
  local dir="$1"
  local detected=()

  [[ -d "$dir/.kiro" ]] && detected+=("kiro")
  [[ -f "$dir/CLAUDE.md" || -d "$dir/.claude" ]] && detected+=("claude-code")
  [[ -d "$dir/.cursor" ]] && detected+=("cursor")
  [[ -f "$dir/AGENTS.md" ]] && detected+=("codex")
  [[ -f "$dir/.windsurfrules" ]] && detected+=("windsurf")
  [[ -d "$dir/.github" ]] && detected+=("github-copilot")
  [[ -f "$dir/.clinerules" ]] && detected+=("cline")
  [[ -f "$dir/GEMINI.md" || -d "$dir/.gemini" ]] && detected+=("gemini-cli")
  [[ -d "$dir/.agents" ]] && detected+=("antigravity")
  [[ -d "$dir/.openclaw" || -f "$dir/.openclaw.json" ]] && detected+=("openclaw")
  [[ -d "$dir/.junie" ]] && detected+=("junie")

  if [[ ${#detected[@]} -eq 0 ]]; then
    echo "  No AI tools detected in $dir. Installing for all tools." >&2
    echo "all"
  else
    echo "  Detected: ${detected[*]}" >&2
    printf '%s\n' "${detected[@]}"
  fi
}

uninstall_tool() {
  local tool="$1"
  local base="$TARGET_DIR"
  if [[ "$GLOBAL" == true ]]; then
    # Mirror the per-tool global base used by each install_* function so
    # uninstall removes files from where they were actually installed.
    case "$tool" in
      gemini-cli)   base="$HOME/.gemini" ;;
      amp)          base="$HOME/.config/agents" ;;
      openclaw)     base="$HOME/.openclaw/workspace" ;;
      devops-agent) base="$HOME/.devops-agent-skills" ;;
      antigravity)  base="$HOME/.gemini" ;;
      *)            base="$HOME" ;;
    esac
  fi

  case "$tool" in
    kiro|kiro-cli)
      rm -f "$base/.kiro/steering/well-architected.md"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/.kiro/skills/$skill_name"
      done
      echo "  Removed: Kiro steering and skills"
      ;;
    claude-code)
      rm -f "$base/CLAUDE.md"
      rm -rf "$base/.claude/commands"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/.claude/skills/$skill_name"
      done
      echo "  Removed: Claude Code CLAUDE.md, commands, and skills"
      ;;
    cursor)
      rm -f "$base/.cursor/rules/well-architected.md" "$base/.cursor/rules/wa-review.md"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/.cursor/skills/$skill_name"
      done
      echo "  Removed: Cursor rules and skills"
      ;;
    codex)
      rm -f "$base/AGENTS.md"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/skills/$skill_name"
      done
      echo "  Removed: Codex AGENTS.md and skills"
      ;;
    windsurf)
      rm -f "$base/.windsurfrules"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/skills/$skill_name"
      done
      echo "  Removed: Windsurf .windsurfrules and skills"
      ;;
    github-copilot)
      rm -f "$base/.github/copilot-instructions.md"
      echo "  Removed: GitHub Copilot instructions"
      ;;
    cline)
      rm -f "$base/.clinerules"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/skills/$skill_name"
      done
      echo "  Removed: Cline .clinerules and skills"
      ;;
    gemini-cli)
      rm -f "$base/GEMINI.md"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/skills/$skill_name"
      done
      echo "  Removed: Gemini CLI GEMINI.md and skills"
      ;;
    antigravity)
      if [[ "$GLOBAL" == true ]]; then
        # Global install reuses the Gemini layout (~/.gemini/GEMINI.md + skills/).
        rm -f "$base/GEMINI.md"
        for skill_dir in "$SCRIPT_DIR/skills"/*/; do
          local skill_name
          skill_name="$(basename "$skill_dir")"
          [[ "$skill_name" == "_shared" ]] && continue
          rm -rf "$base/skills/$skill_name"
        done
      else
        rm -f "$base/.agents/rules/well-architected.md" "$base/.agents/rules/wa-review.md"
        for skill_dir in "$SCRIPT_DIR/skills"/*/; do
          local skill_name
          skill_name="$(basename "$skill_dir")"
          [[ "$skill_name" == "_shared" ]] && continue
          rm -rf "$base/.agents/skills/$skill_name"
        done
      fi
      echo "  Removed: Antigravity rules and skills"
      ;;
    junie)
      rm -f "$base/.junie/guidelines/well-architected.md"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$base/.junie/skills/$skill_name"
      done
      echo "  Removed: Junie guidelines and skills"
      ;;
    amp)
      rm -f "$base/AGENTS.md"
      local amp_skills_dir="$base/.agents/skills"
      [[ "$GLOBAL" == true ]] && amp_skills_dir="$base/skills"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$amp_skills_dir/$skill_name"
      done
      echo "  Removed: Amp AGENTS.md and skills"
      ;;
    openclaw)
      rm -f "$base/AGENTS.md"
      local openclaw_skills_dir="$base/.agents/skills"
      [[ "$GLOBAL" == true ]] && openclaw_skills_dir="$base/skills"
      for skill_dir in "$SCRIPT_DIR/skills"/*/; do
        local skill_name
        skill_name="$(basename "$skill_dir")"
        [[ "$skill_name" == "_shared" ]] && continue
        rm -rf "$openclaw_skills_dir/$skill_name"
      done
      echo "  Removed: OpenClaw AGENTS.md and skills"
      ;;
    devops-agent)
      rm -rf "$base/devops-agent-skills"
      echo "  Removed: DevOps Agent skill packages"
      ;;
  esac
}

check_update() {
  local latest
  latest="$(curl -sL https://api.github.com/repos/aws-samples/sample-well-architected-skills-and-steering/releases/latest 2>/dev/null | grep '"tag_name"' | sed 's/.*"v\(.*\)".*/\1/')"

  if [[ -z "$latest" ]]; then
    echo "  Could not check for updates (no network or API rate limited)."
    return
  fi

  if [[ "$latest" == "$VERSION" ]]; then
    echo "  You are up to date (v$VERSION)."
  else
    echo "  Update available: v$VERSION → v$latest"
    echo "  Run the bootstrap one-liner or git pull to update."
    echo "  https://github.com/aws-samples/sample-well-architected-skills-and-steering/releases/tag/v$latest"
  fi
}

if [[ "$CHECK_UPDATE" == true ]]; then
  check_update
  exit 0
fi

echo "================================================"
echo " Well-Architected Skills & Steering Installer"
echo "================================================"
echo ""
echo "Source:  $SCRIPT_DIR"
echo "Target:  $TARGET_DIR"
echo "Mode:    $(if [[ "$SYMLINK" == true ]]; then echo "symlink"; else echo "copy"; fi)"
echo "Scope:   $(if [[ "$GLOBAL" == true ]]; then echo "global"; else echo "project"; fi)"
echo "Tools:   ${TOOLS[*]}"
echo ""

# Handle auto-detection
if [[ "${TOOLS[*]}" == "auto" ]]; then
  TOOLS=()
  while IFS= read -r t; do
    TOOLS+=("$t")
  done < <(detect_tools "$TARGET_DIR")
fi

# Handle uninstall mode
if [[ "$UNINSTALL" == true ]]; then
  echo "Uninstalling..."
  for tool in "${TOOLS[@]}"; do
    if [[ "$tool" == "all" ]]; then
      for t in kiro claude-code cursor codex windsurf github-copilot cline gemini-cli antigravity junie amp openclaw devops-agent; do
        uninstall_tool "$t"
      done
    else
      uninstall_tool "$tool"
    fi
  done
  echo ""
  echo "Uninstall complete!"
  exit 0
fi

for tool in "${TOOLS[@]}"; do
  case "$tool" in
    kiro|kiro-cli)  install_kiro ;;
    claude-code)    install_claude_code ;;
    cursor)         install_cursor ;;
    codex)          install_codex ;;
    windsurf)       install_windsurf ;;
    github-copilot) install_github_copilot ;;
    cline)          install_cline ;;
    gemini-cli)     install_gemini_cli ;;
    antigravity)    install_antigravity ;;
    junie)          install_junie ;;
    amp)            install_amp ;;
    openclaw)       install_openclaw ;;
    devops-agent)   install_devops_agent ;;
    all)
      install_kiro
      install_claude_code
      install_cursor
      install_codex
      install_windsurf
      install_github_copilot
      install_cline
      install_gemini_cli
      install_antigravity
      install_junie
      install_amp
      install_openclaw
      install_devops_agent
      ;;
    *)
      echo "Unknown tool: $tool"
      echo "Valid options: kiro, kiro-cli, claude-code, cursor, codex, windsurf, github-copilot, cline, gemini-cli, antigravity, junie, amp, openclaw, devops-agent, auto, all"
      exit 1
      ;;
  esac
done

echo "Installation complete!"
