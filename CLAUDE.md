# Claude Workspace

<!-- CUSTOMIZE: Replace placeholder values marked with <angle-brackets> -->

## Hard Rules

1. **[AGENTS]** Before spawning 2+ agents, ASK first. `code-reviewer`/`architect`/`sprint-planner` have NO Write access. If an agent spawn fails, STOP and change approach. Never rely on agents writing output files. Capture results from the task return value.
2. **[PLAN MODE]** Do NOT enter plan mode while parallel agents are running. It kills them. If plan mode activates unexpectedly, exit immediately.
3. **[TEST BEFORE COMMIT]** Run the test suite before every commit. No exceptions.
4. **[HANDOFF LOCATION]** Handoff docs, reviews, and generated docs go in `projects/[project]/codex/`. NEVER in `.claude/` or project root. Tell the user the exact path.
5. **[FIRST FIX WINS]** When the user accepts output, stop. Do not iterate further unless asked.
6. **[CORRECTIONS]** After ANY user correction: update `lessons.md` immediately, before doing anything else.
7. **[EXTERNAL RESOURCES]** Check project's `codex/`, `reference/`, `exports/` BEFORE fetching URLs. If fetch fails, ask user to paste content.

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

These come from real correction patterns. Follow them explicitly:

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
