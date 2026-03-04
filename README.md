# claude-workflow

A complete, battle-tested workflow system for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Not just skills — an integrated system for session continuity, correction learning, structured reviews, and disciplined commits.

## What makes this different

Most Claude Code skill collections are "persona prompts" — they tell Claude to act like an expert. This is a **workflow system** built from real usage patterns and real mistakes:

- **Session lifecycle** — resume context, work, commit, hand off, resume next time
- **Correction learning** — every mistake becomes a rule in `lessons.md`, reviewed at session start
- **Integrated skills** — skills know about each other (commit triggers deploy checks, done updates lessons)
- **Battle-tested rules** — every constraint exists because something went wrong without it
- **Progressive disclosure** — lean skill files with deeper reference docs loaded only when needed
- **Trigger-only descriptions** — skill descriptions say *when* to activate, not *what* they do, preventing the agent from skipping the actual skill content

## What's inside

### 9 Skills

| Skill | Trigger | What it does |
|-------|---------|-------------|
| `/resume` | Start of session | Restores context from Memory MCP, handoff docs, git state |
| `/commit` | Ready to commit | Stages files, drafts conventional message, context health check |
| `/done` | End of session | Creates session summary, updates lessons, writes handoff doc |
| `/coffeechat` | Periodic (1-2 weeks) | Plain-English health check on projects, loose ends, patterns |
| `/grill-me` | Before building something | Stress-tests plans via 6 modes: interview, assumptions, opposing case, failure modes, red team, evidence audit |
| `/improve` | Before an important prompt | Analyzes prompt weaknesses, generates 2-3 improved versions |
| `/deslop` | After generating code | Removes AI artifacts: obvious comments, unnecessary error handling, debug leftovers |
| `/sprint-review` | After completing a feature | Severity-tiered code review, fix in priority order, handoff doc |
| `/prd-to-issues` | Have a spec, need issues | Breaks PRD into vertical-slice GitHub issues with dependency ordering |

### 4 Rules (auto-loaded from `.claude/rules/`)

- **testing.md** — test before commit, browser testing patterns, verification discipline
- **workflow.md** — plan mode, sprints, TDD, pre-commit checklist, post-commit context check
- **tooling.md** — subagent access levels, spawn limits, failure handling
- **session-continuity.md** — Memory MCP usage, handoff protocol, resume workflow

### 2 Hooks

- **context-monitor.py** — warns when context window is filling up (PostToolUse)
- **pre-commit-checks.py** — reminds about deployment after commits to deployed projects (PreToolUse)

### Session lifecycle

```
/resume → work → /commit → /done → (next session) → /resume
                    ↑                                    ↓
                    └──── lessons.md ← corrections ──────┘
```

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
# Edit CLAUDE.md — set your workspace root, test commands, GitHub repo
# Edit lessons.md — replace examples with your own (or start empty)
```

See [QUICKSTART.md](QUICKSTART.md) for the full setup guide.

## Design principles

1. **Trigger-only descriptions** — skill descriptions say *when* to use them, not *how*. This prevents the agent from thinking it already knows what to do and skipping the skill content.

2. **Progressive disclosure** — core workflow in SKILL.md (~60-80 lines), detailed reference material in `reference/` subdirectories loaded on demand. Saves tokens.

3. **Correction-driven rules** — every rule in CLAUDE.md's "Proven Constraints" section exists because something went wrong without it. Rules aren't theoretical — they're earned.

4. **First fix wins** — when the user accepts output, stop. Don't iterate unless asked.

5. **Minimal error handling** — let errors surface. No silent try/catch. Only catch with meaningful recovery.

## License

MIT
