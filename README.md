# claude-workflow

A workflow system for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) that handles session continuity, correction tracking, structured reviews, and disciplined commits. Built from months of daily use, not a weekend brainstorm.

## Why this exists

Most Claude Code skill collections are persona prompts. They tell Claude to act like an expert. That's fine until your session ends and everything is gone.

This is a workflow system. It tracks what happened last session, what went wrong, what decisions were made, and what's left to do. Every rule in here exists because something actually broke without it.

What it solves:

- Sessions that start blank every time. The resume/done cycle carries context forward.
- The same mistakes repeating. Corrections get logged to `lessons.md` and reviewed at session start.
- Skills that don't know about each other. Commit triggers deploy checks. Done updates lessons. They're connected.
- Rules that sound good but weren't earned. Every constraint here comes from a real correction.

## What's in it

### 9 skills

| Skill | When to use | What it does |
|-------|------------|-------------|
| `/resume` | Start of session | Restores context from Memory MCP, handoff docs, git state |
| `/commit` | Ready to commit | Stages files, drafts message, checks context health |
| `/done` | End of session | Creates summary, updates lessons, writes handoff doc |
| `/coffeechat` | Every 1-2 weeks | Plain-English health check on projects and loose ends |
| `/grill-me` | Before building something | Stress-tests plans (6 modes: interview, assumptions, opposing case, failure, red team, evidence) |
| `/improve` | Before an important prompt | Analyzes weaknesses, generates 2-3 better versions |
| `/deslop` | After generating code | Removes AI artifacts: obvious comments, pointless error handling, debug leftovers |
| `/sprint-review` | After completing a feature | Severity-tiered code review, fix in priority order, handoff doc |
| `/prd-to-issues` | Have a spec, need issues | Breaks a PRD into vertical-slice GitHub issues with dependency ordering |

### 4 rules (auto-loaded from `.claude/rules/`)

- **testing.md** - test before commit, browser testing patterns, verification discipline
- **workflow.md** - plan mode, sprints, TDD, pre-commit checklist, post-commit context check
- **tooling.md** - subagent access levels, spawn limits, failure handling
- **session-continuity.md** - Memory MCP usage, handoff protocol, resume workflow

### 2 hooks

- **context-monitor.py** (PostToolUse) - warns when context window is filling up
- **pre-commit-checks.py** (PreToolUse) - reminds about deployment after commits to deployed projects

### Session lifecycle

```
/resume → work → /commit → /done → (next session) → /resume
                    ↑                                    ↓
                    └──── lessons.md ← corrections ──────┘
```

The resume/done cycle works best with [Memory MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) for cross-session memory. Without it, everything falls back to handoff files in `codex/` - still works, just less automatic.

## Quick install

```bash
# 1. Clone
git clone https://github.com/eddyplolz/claude-workflow.git

# 2. Copy into your project
cp -r claude-workflow/.claude /path/to/your/project/
cp claude-workflow/CLAUDE.md /path/to/your/project/
cp claude-workflow/lessons.md /path/to/your/project/
cp claude-workflow/.gitleaks.toml /path/to/your/project/

# 3. Customize
# Edit CLAUDE.md - set your workspace root, test commands, GitHub repo
# Edit lessons.md - replace examples with your own (or start empty)
```

If you want session memory to persist across conversations, set up [Memory MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/memory). It's optional but makes `/resume` much better.

See [QUICKSTART.md](QUICKSTART.md) for the full setup guide.

## How it was built

Two things shaped this:

**Trigger-only skill descriptions.** Skill descriptions say *when* to activate, not *what* they do. If you describe the behavior in the description, the agent thinks it already knows and skips the actual skill content. Learned this the hard way.

**Correction-driven rules.** Every rule in CLAUDE.md's "Proven Constraints" section is there because something went wrong without it. They're not best practices from a blog post. They're scars.

Other stuff that matters: progressive disclosure (core workflow in ~60-80 line SKILL.md files, reference material loaded on demand), first-fix-wins (when the user accepts output, stop), minimal error handling (let errors surface, don't silently swallow them).

## License

MIT
