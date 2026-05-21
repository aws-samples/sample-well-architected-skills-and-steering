#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-.}"

usage() {
  cat <<EOF
Usage: ./install.sh [TARGET_DIR] [OPTIONS]

Install Well-Architected steering and skills into your project for your AI coding tool.

Arguments:
  TARGET_DIR    Project directory to install into (default: current directory)

Options:
  --tool TOOL   Install only for a specific tool. Can be repeated.
                Valid: kiro, claude-code, cursor, codex, windsurf, github-copilot, cline, all
  --symlink     Use symlinks instead of copies (auto-updates when this repo changes)
  --global      Install to global config (~/.kiro, ~/.claude, etc.) instead of project
  --force       Overwrite existing files without prompting
  --help        Show this help message

Examples:
  ./install.sh ~/my-project --tool kiro --tool claude-code
  ./install.sh ~/my-project --tool all
  ./install.sh ~/my-project --tool cursor --symlink
  ./install.sh --global --tool claude-code
  ./install.sh ~/my-project --tool all --force
EOF
  exit 0
}

TOOLS=()
SYMLINK=false
GLOBAL=false
FORCE=false

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

  mkdir -p "$(dirname "$dest")"

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
    copy_or_link "$skill_dir/SKILL.md" "$base/.kiro/skills/$skill_name/SKILL.md"
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
  echo "  Done. Use /wa-review, /security-assessment, etc. as slash commands."
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
    copy_or_link "$skill_dir/SKILL.md" "$base/.cursor/skills/$skill_name/SKILL.md"
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
    copy_or_link "$skill_dir/SKILL.md" "$base/skills/$skill_name/SKILL.md"
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
    copy_or_link "$skill_dir/SKILL.md" "$base/skills/$skill_name/SKILL.md"
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
    copy_or_link "$skill_dir/SKILL.md" "$base/skills/$skill_name/SKILL.md"
  done
  echo "  Done. Cline will load .clinerules automatically."
  echo ""
}

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

for tool in "${TOOLS[@]}"; do
  case "$tool" in
    kiro)           install_kiro ;;
    claude-code)    install_claude_code ;;
    cursor)         install_cursor ;;
    codex)          install_codex ;;
    windsurf)       install_windsurf ;;
    github-copilot) install_github_copilot ;;
    cline)          install_cline ;;
    all)
      install_kiro
      install_claude_code
      install_cursor
      install_codex
      install_windsurf
      install_github_copilot
      install_cline
      ;;
    *)
      echo "Unknown tool: $tool"
      echo "Valid options: kiro, claude-code, cursor, codex, windsurf, github-copilot, cline, all"
      exit 1
      ;;
  esac
done

echo "Installation complete!"
