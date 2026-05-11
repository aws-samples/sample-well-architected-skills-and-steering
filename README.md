# Well-Architected Skills & Steering for Kiro

Reusable steering files and skills that teach [Kiro](https://kiro.dev) how to apply the AWS Well-Architected Framework in every conversation.

## What's inside

```
steering/          Steering files — always-on context that shapes Kiro's behavior
  well-architected.md   WA Framework pillars, design principles, review process

skills/            Skills — step-by-step playbooks Kiro follows for specific tasks
  (coming soon)
```

## Quick start

### Option 1: Copy into your project (recommended)

Copy the files you want into your project's `.kiro/` directory:

```bash
# From your project root
mkdir -p .kiro/steering
cp path/to/this-repo/steering/well-architected.md .kiro/steering/
```

Kiro automatically loads all `.md` files under `.kiro/steering/` as context for every conversation in that workspace.

### Option 2: Symlink for automatic updates

```bash
mkdir -p .kiro/steering
ln -s /absolute/path/to/this-repo/steering/well-architected.md .kiro/steering/well-architected.md
```

### Option 3: Install globally

Place files in your global Kiro config to apply them across all projects:

```bash
mkdir -p ~/.kiro/steering
cp path/to/this-repo/steering/well-architected.md ~/.kiro/steering/
```

## How it works

**Steering files** (`.kiro/steering/**/*.md`) are loaded automatically into every Kiro conversation. They act as persistent instructions — think of them as "always-on rules" that guide Kiro's responses without you having to repeat yourself.

**Skills** (`.kiro/skills/*/SKILL.md`) are task-specific playbooks that Kiro follows step-by-step when triggered by certain phrases or requests.

## Verifying it's loaded

Start a Kiro chat in your project and ask:

```
What Well-Architected pillars should I consider for this architecture?
```

If the steering is loaded, Kiro will reference all six pillars with specific guidance rather than giving a generic answer.

## Contributing

1. Fork this repo
2. Add or edit files under `steering/` or `skills/`
3. Open a merge request with a description of what guidance you added or changed
