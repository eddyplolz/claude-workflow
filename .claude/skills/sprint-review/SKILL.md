---
name: sprint-review
description: Use after completing a sprint or feature to review code quality. Finds issues by severity, fixes them in priority order, and creates a handoff doc.
---

# Code Review Skill

Run a systematic code review, fix issues in priority order, and produce a handoff document.

## Steps

1. **Read the target file(s) completely before starting.**
   - Understand the architecture before looking for issues.
   - Check `git diff` to see what changed recently.

2. **Create findings list with severity tiers: Critical, High, Medium, Low.**
   - Write findings to `projects/[project]/codex/review-YYYY-MM-DD.md`
   - NEVER write to `.claude/` or project root.
   - Tell the user the exact file path immediately after writing.
   - Each finding: severity, file, line number, description, proposed fix.

3. **Show the user the findings and ask which tier to begin implementing.**

4. **Fix all Critical and High issues first, then Medium.**
   - After each fix, re-read the modified file to confirm the change is present.
   - Do NOT report a fix as complete without re-reading and verifying.

5. **Run all tests after each sprint of fixes.**
   - If tests fail, fix the regression before continuing.

6. **Create handoff doc** at `projects/[project]/codex/HANDOFF-Review-[DD-Mon-YY].md` with:
   - Completed fixes (with file:line references)
   - Deferred items with full context and rationale
   - Recommended next steps

7. **Update CHANGELOG.md** with substantive changes.

## Rules

- Do NOT spawn parallel agents for file writing — do the work directly.
- If using agents for exploration, capture results from the task return value and write files yourself.
- One failed agent approach = stop and do it manually.
- Commit after each sprint of fixes, not at the end.
