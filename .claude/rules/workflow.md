# Workflow

## Plan Mode

**Use for:** 5+ file changes, new project creation, architectural redesign.
**Skip for:** Single edits, bug fixes, clear instructions, routine changes.

- Do NOT enter plan mode while parallel agents are running — it kills them.
- No subagents in plan mode.
- If stuck: ask "Should I exit plan mode and proceed?"
- Before exiting: save plan to `codex/` or `plans/`.

## Sprints

For multi-feature projects:
1. Break into sprints (each = demoable software)
2. Track tasks in `projects/[project]/SPRINTS.md`
3. Work sequentially, commit after each task
4. After each sprint: report what's done, what remains, ask to proceed
5. Never defer sprint items without explicit user instruction

## TDD

- **Bug fixes:** Always write a failing test that reproduces the bug before writing the fix. No exceptions.
- **New features:** Ask "can I test the expected behavior before writing code?" If yes, write the test first.
- **One test → one implementation.** Don't write all tests upfront — one cycle at a time.

## Pre-Commit Checklist

- [ ] Test suite passes (run it, report the count)
- [ ] All changes committed
- [ ] Memory MCP updated
- [ ] User told what's done and what remains
- [ ] For deployed projects: run `deploy.py --dry-run`

## Post-Commit Context Check

After every successful commit, assess context health and tell the user:
- ✅ **Clean** — safe to continue
- ⚡ **Compact** — recommend `/smart-compact` before next task
- 🔄 **Handoff** — recommend `/done` and fresh session

Do not skip this. Long-session degradation causes rule-forgetting, verification loops, and ignored instructions.
