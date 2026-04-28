# Claude Workspace

Portable Claude Code workflow distribution. Customize the `<angle-bracket>` placeholders below for your setup. See [README.md](README.md) for full install instructions.

<!-- CUSTOMIZE: Replace placeholder values marked with <angle-brackets> -->

## Hard Rules

1. **[AGENTS]** Before spawning 2+ agents, ASK first. `code-reviewer`/`architect`/`sprint-planner` have NO Write access. If an agent spawn fails, STOP and change approach. Never rely on agents writing output files. Capture results from the task return value.
2. **[PLAN MODE]** Do NOT enter plan mode while parallel agents are running. It kills them. If plan mode activates unexpectedly, exit immediately.
3. **[TEST BEFORE COMMIT]** Run the test suite before every commit. No exceptions.
4. **[HANDOFF LOCATION]** Handoff docs, reviews, and generated docs go in `projects/[project]/codex/`. NEVER in `.claude/` or project root. Tell the user the exact path.
5. **[FIRST FIX WINS]** When the user accepts output, stop. Do not iterate further unless asked.
6. **[CORRECTIONS]** After ANY user correction: update `lessons.md` immediately, before doing anything else.
7. **[EXTERNAL RESOURCES]** Check project's `codex/`, `reference/`, `exports/` BEFORE fetching URLs. If fetch fails, ask user to paste content.
8. **[FILE SAFETY]** NEVER delete or recommend deleting project files/folders without explicit confirmation. Default to moving or archiving — not deleting.
9. **[SECRETS]** NEVER approve a persistent `Bash` permission whose command string contains a literal secret (token/key/password). Approve **once-only** instead, or rewrite the command to read from `.env` (e.g. `set -a && source .env && set +a && <cmd>`). Inline secrets persist in `settings.local.json` indefinitely and have ended up in stashes/history before. Same rule applies to writing secrets into any tracked file — use `.env` or `*.local.*` patterns and verify the path is gitignored before writing.
10. **[GOAL DRIFT]** Before executing any item from a prior-session plan, mentally restate the user's stated goal in one sentence and confirm the item advances it. Prior plans are inputs, not specs. If the gap between "what this item does" and "what the goal is" requires hand-waving to bridge, the item doesn't belong in this session — defer or drop.
11. **[NO VERIFICATION LOOPS]** Tests passing IS verification. Use at most 1 screenshot per page-load confirmation. Do NOT loop through presets, retake screenshots after minor edits, or use browser tools as iterative pre-commit verification. After verification, commit.

---

## Behavior

- **ASK:** Irreversible actions, architectural choices, unclear requirements
- **DECIDE:** Implementation details, file organization, naming, code style
- Disclose data quality issues. Never present partial data as complete.
- Beginner-friendly: explain new concepts in plain English.

---

## Workspace

<!-- CUSTOMIZE: Set your workspace root and GitHub repo -->
**Root:** `<your-workspace-root>`. Ask before modifying files outside it.
**GitHub:** `<your-org>/<your-repo>` (backup/version control).

## Commands

<!-- CUSTOMIZE: Set your test, lint, and build commands -->
- Test: `<your-test-command>` (e.g., `python -m pytest`, `npm test`)
- Lint: `<your-lint-command>` (e.g., `python -m flake8`, `npm run lint`)

---

## Proven Constraints

These come from real correction patterns. Follow them:

- **Minimal error handling:** Let errors surface. No silent try/catch. Only catch with meaningful recovery.
- **Update changelog before committing** any user-visible behavior change.
- **Files over 300 lines:** Don't add features, split first. Critical for single-file apps.

---

## After Every Session

**At session start:** Read `lessons.md` for correction patterns.

- Update CHANGELOG.md with substantive changes
- Write lessons to `lessons.md` including correction patterns from this session
- If work is incomplete: create/update handoff doc in `projects/[project]/codex/`

---

## Additional Rules

Auto-loaded from `.claude/rules/`:
- `testing.md` - test patterns, fix verification
- `workflow.md` - sprints, plan mode, pre-commit checklist
- `session-continuity.md` - Memory MCP, handoffs
- `tooling.md` - subagent access levels
