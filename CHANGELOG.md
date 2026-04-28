# Changelog

All notable changes to claude-workflow will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.1.1] - 2026-04-28

### Added
- **`.gitignore` template** at repo root covering `.env`, `.claude/settings.local.json`, Python/Node build artifacts, OS junk, and editor caches. Closes the fail-open gap where adopters could accidentally commit credentials when cloning the template.
- **"Secret hygiene" section in `QUICKSTART.md`** instructing adopters to verify `.gitignore` coverage, run `gitleaks detect` before first commit, and read the `[SECRETS]` rule.

### Changed
- **`QUICKSTART.md` section 4** now describes Auto-Memory as the canonical store (matching `README.md` 1.1.0).
- **`commit` skill** now uses `Co-Authored-By: Claude` (model-agnostic) instead of stale `Claude Opus 4.6`.

## [1.1.0] - 2026-04-28

### Added
- **Four hard rules backported to `CLAUDE.md`** from the canonical workspace, all general-purpose enough for any Claude Code user:
  - `[FILE SAFETY]` — never delete or recommend deleting project files without explicit confirmation; default to moving or archiving.
  - `[SECRETS]` — never approve a persistent `Bash` permission whose command contains a literal token/key/password; approve once-only or read from `.env`.
  - `[GOAL DRIFT]` — before executing any item from a prior-session plan, restate the user's current goal and confirm the item still advances it.
  - `[NO VERIFICATION LOOPS]` — tests passing IS verification; do not retake screenshots or use browser tools as iterative pre-commit checks.
- **Orientation header on `CLAUDE.md`** describing the file as a portable Claude Code workflow distribution with pointer to `README.md`.

### Changed
- **README.md** now describes Claude Code's built-in Auto-Memory store as the canonical cross-session memory; Memory MCP is documented as a legacy fallback.
- **session-continuity.md description** in README updated from "Memory MCP usage" to "Auto-Memory (canonical)".

## [1.0.0] - 2026-03-04

Initial public release.

### Skills (9)
- **resume** - restore session context from Memory MCP, handoff docs, git state
- **commit** - stage files, draft conventional commit message, post-commit context health check
- **done** - end-of-session summary, lesson extraction, handoff doc creation
- **coffeechat** - periodic project health check and loose-end surfacing
- **grill-me** - stress-test plans via 6 challenge modes (interview, assumptions, opposing case, failure modes, red team, evidence audit)
- **improve** - analyze prompt weaknesses, generate improved versions
- **deslop** - remove AI code artifacts (obvious comments, unnecessary error handling, debug leftovers)
- **sprint-review** - severity-tiered code review with prioritized fixes
- **prd-to-issues** - break PRDs into vertical-slice GitHub issues with dependency ordering

### Rules (4)
- **testing** - test before commit, browser testing patterns, verification discipline
- **workflow** - plan mode, sprints, TDD, pre-commit checklist, post-commit context check
- **tooling** - subagent access levels, spawn limits, failure handling
- **session-continuity** - Memory MCP usage, handoff protocol, resume workflow

### Hooks (2)
- **context-monitor** (PostToolUse) - warns when context window is filling up
- **pre-commit-checks** (PreToolUse) - reminds about deployment after commits to deployed projects

### Also included
- CLAUDE.md template with proven constraints and workspace configuration
- lessons.md template for correction-driven learning
- QUICKSTART.md setup guide
- .gitleaks.toml for secret detection
