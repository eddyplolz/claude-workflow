# Changelog

All notable changes to claude-workflow will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
