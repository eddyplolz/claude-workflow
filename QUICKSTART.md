# Quickstart guide

## Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and working
- A project directory where you want to use the workflow

## Installation

### Option A: Copy into existing project

```bash
git clone https://github.com/eddyplolz/claude-workflow.git
cp -r claude-workflow/.claude /path/to/your/project/
cp claude-workflow/CLAUDE.md /path/to/your/project/
cp claude-workflow/lessons.md /path/to/your/project/
cp claude-workflow/.gitleaks.toml /path/to/your/project/
```

### Option B: Use as your workspace template

```bash
git clone https://github.com/eddyplolz/claude-workflow.git my-workspace
cd my-workspace
# Customize CLAUDE.md, then start working
```

## Customization checklist

After copying, update these files:

### 1. CLAUDE.md (required)

Open `CLAUDE.md` and replace the placeholders:

- `<your-workspace-root>` -your project's absolute path
- `<your-org>/<your-repo>` -your GitHub repository
- `<your-test-command>` -how to run tests (e.g., `python -m pytest`, `npm test`)
- `<your-lint-command>` -how to lint (e.g., `python -m flake8`, `npm run lint`)

Add any project-specific rules under the existing sections.

### 2. lessons.md (optional)

Replace the example entries with your own, or delete them and start fresh. The format section at the top shows the expected structure.

### 3. Hooks (optional but recommended)

Add hook configuration to your `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python /absolute/path/to/.claude/hooks/context-monitor.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

**Important:** Hook paths must be absolute. Relative paths break when Claude runs commands in subdirectories.

### 4. Memory MCP (optional)

The session continuity system works best with [Memory MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/memory). Without it, the workflow falls back to handoff docs in `projects/[project]/codex/`.

## How the skills work

All skills are slash commands in Claude Code:

| Command | When to use |
|---------|------------|
| `/resume` | Start of every session |
| `/commit` | When you're ready to commit changes |
| `/done` | End of every session |
| `/coffeechat` | Every 1-2 weeks for a check-in |
| `/grill-me` | Before implementing something significant |
| `/improve` | Before sending a complex prompt |
| `/deslop` | After AI-generated code to clean up artifacts |
| `/sprint-review` | After completing a feature or sprint |
| `/prd-to-issues` | When you have a spec and need GitHub issues |

## Session lifecycle

A typical work session:

1. `/resume` - restores context from last session
2. Write code, fix bugs, build features
3. `/commit` - stages, commits, checks context health
4. `/done` - creates summary, logs corrections, writes handoff

`/done` captures any mistakes you corrected during the session into `lessons.md`. Next time, `/resume` reads those lessons before you start. So corrections stick around.

## Adding your own skills

Create a new directory under `.claude/skills/`:

```
.claude/skills/my-skill/
├── SKILL.md              # Core workflow (keep under 100 lines)
└── reference/            # Optional deep-dive docs
    └── details.md
```

**Skill file format:**

```markdown
---
name: my-skill
description: Use when [specific trigger condition]. [Brief what-it-does.]
---

# My Skill

[Core workflow steps here]
```

The description should say *when* to trigger the skill, not how it works internally. If you put the behavior in the description, the agent thinks it already knows and skips the actual skill content.

## Adding your own rules

Create `.md` files in `.claude/rules/`. They're auto-loaded into every conversation. Keep them short and actionable. Rules that are too long get ignored.

## Project structure

The workflow expects this directory layout for handoff docs and session summaries:

```
your-project/
├── .claude/
│   ├── rules/          # Auto-loaded rules
│   ├── skills/         # Slash command skills
│   └── hooks/          # Pre/post tool hooks
├── projects/
│   └── your-project/
│       └── codex/      # Handoff docs, session summaries, reviews
├── CLAUDE.md           # Workspace instructions
└── lessons.md          # Correction patterns
```
