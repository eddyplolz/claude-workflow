---
name: done
description: Use at the end of any work session to wrap up. Captures decisions, corrections, follow-ups, lessons, verification, Git state, and push/deploy status before closing.
---

# Done - Session Closeout

Close the session without losing work, hiding loose ends, or leaving Git in a surprising state. This skill is used by Claude Code and mirrored for Codex, so it must be self-contained and cannot rely on one runtime's hooks as the only safety net.

## Source of Truth

- Canonical tracked file: `C:\Users\polit\Claude\.claude\skills\done\SKILL.md`
- Codex active mirror: `C:\Users\polit\Claude\.agents\skills\done\SKILL.md`
- Packaged workflow copy: `C:\Users\polit\Claude\projects\claude-workflow\.claude\skills\done\SKILL.md`
- `.claude/skills/done/SKILL.md` is the source of truth. Keep the other two copies behaviorally identical whenever this skill changes.
- During `/done`, compare the canonical and Codex mirror files. If they differ, report mirror drift as a blocker before committing or pushing.

## Closeout Gates

Run the gates in order. If a required gate fails, stop, report the blocker, and do not continue to commit, deploy, or push.

### 1. Preflight

Gather context before writing anything:

- `git rev-parse --show-toplevel`
- `git rev-parse --abbrev-ref HEAD`
- `git status --short --branch`
- `git log --oneline -10`
- `git rev-parse --verify @{u}` if an upstream exists
- `git rev-list --left-right --count @{u}...HEAD` if an upstream exists
- Read `C:\Users\polit\Claude\lessons.md`
- Identify likely active project from current directory, branch, changed paths, or conversation context.
- If no active project is obvious, use `scratch/`.

Required preflight checks:

- If `.claude/skills/done/SKILL.md` and `.agents/skills/done/SKILL.md` differ, stop and report mirror drift.
- If Git has uncommitted changes from before closeout, list them and ask whether to commit them as part of wrap-up or leave them for follow-up.
- If the user chooses not to commit existing dirty files, continue only if the final summary records those files under Follow-Up Tasks.
- If an upstream is missing, continue with capture but mark push status as blocked until upstream is configured.

### 2. Session Capture

Review the full conversation and local context. Capture:

- Work completed
- Decisions made and why
- User preferences or workflow choices expressed
- Files changed, including untracked files and ignored mirrors if relevant
- Verification already performed
- Corrections, frustration, reversals, or user redirections
- Open questions and unfinished tasks
- Deployment or production implications

### 3. Lessons Update

If the user corrected behavior this session, update `C:\Users\polit\Claude\lessons.md` before writing the handoff summary.

Use the canonical format already present in `lessons.md`:

```markdown
### YYYY-MM-DD — Short description
**Mistake:** What went wrong.
**Fix:** What the correct approach is.
**Rule:** The prevention rule for future sessions.
```

Rules:

- Check existing entries first and avoid duplicates.
- User corrections go to `lessons.md` even if Memory MCP or another feedback file also stores them.
- If no corrections occurred, write "None this session" in the summary.

### 4. Summary Write

Write a collision-safe session summary:

- Project target: `projects/[project]/codex/`
- Fallback target: `scratch/`
- Filename: `SESSION-[branch]-[YYYY-MM-DD]-[topic-slug].md`
- If the file exists, append `-2`, `-3`, etc.
- Never overwrite an existing summary.

Use this format and include every section:

```markdown
# Session Summary - YYYY-MM-DD

**Branch:** [branch]
**Project:** [project]
**Session type:** [Coding / Config / Tooling / Discussion]

## What We Did
[2-5 concrete bullets]

## Key Decisions
[Decisions and brief rationale, or "None this session"]

## Preferences & Conventions
[User preferences expressed, or "None this session"]

## Files Changed
[All modified, created, untracked, and intentionally ignored mirror files]

## Verification
[Tests, lint, scans, browser checks, deploy dry-runs, or blockers]

## Git / Deploy Status
[Dirty tree, commit hash, push status, deploy status]

## Open Questions
[Unresolved decisions, or "None"]

## Follow-Up Tasks
[Specific next actions, including any intentionally uncommitted files]

## Lessons / Corrections
[Corrections added to lessons.md, or "None this session"]

## Resume Prompt
[One pasteable prompt for next session]
```

### 5. Memory Update

Update Memory MCP with changed project status, deferred work, deployment state, and key decisions.

If Memory MCP is unavailable or stale:

- Trust the filesystem.
- Continue with the handoff doc.
- Record in the summary and final response that Memory MCP was not updated.

### 6. Post-Write Git Gate

After writing the summary and lessons, run `git status --short --branch` again. This second dirty-tree check is mandatory.

If files are dirty now:

- List every changed file.
- Distinguish pre-existing dirty files from files created or modified by `/done`.
- Ask whether to commit the wrap-up artifacts.
- If the user declines, stop before push and report the exact uncommitted files.

Do not claim the session is clean until this gate has passed.

### 7. Verification Before Commit

Before any `/done` commit, verify the workspace:

- Invoke `/verify` when available, or run the project-appropriate commands directly.
- At minimum, run the workspace test suite before committing: `python -m pytest`.
- If tests cannot run or fail, stop. Do not commit, deploy, or push.
- For changed Markdown-only skill/rule docs, also re-read the changed files and confirm required checklist items are present.

Required static checklist for this skill:

- Correct lessons path: `C:\Users\polit\Claude\lessons.md`
- Post-write Git gate
- Mirror drift blocker
- Fail-closed gitleaks or equivalent secret scan
- Explicit-file staging only
- Push review and approval
- Deployed-project dry-run
- Final report checklist

### 8. Commit And Sanitize

Use `/commit` or perform the equivalent steps directly. The commit flow must be fail-closed.

Before committing:

- Show the draft commit message.
- Show the exact file list to stage.
- Show excluded files and why.
- Stage files by explicit path only.
- Never use `git add .` or `git add -A`.
- Never use `--amend` unless the user explicitly asks.
- Never use `--no-verify`.
- Never commit secrets, credentials, `.env`, password files, or local settings containing sensitive values.
- Run `git diff --cached --stat`.
- Run a staged secret scan with gitleaks or an equivalent configured scanner.
- If gitleaks is unavailable, misconfigured, or inconclusive, stop. Do not commit or push.
- Run `git status --short` after committing and report the new commit hash.

Commit messages must follow the commit skill conventions, including the required co-author footer from `/commit`.

### 9. Deploy Dry-Run Gate

If committed files affect a project listed in `deploy-config.json`:

- Identify affected project(s) by `local_root`.
- Run `python deploy.py <project> --dry-run`.
- For multi-commit sessions, use `--since <first-session-commit>~1` when appropriate.
- If JS/CSS changed, verify the relevant HTML entry point is included or explicitly add it with `--files`.
- Present files, remote paths, warnings, and blockers to the user.
- Stop for user approval before real deployment.
- If dry-run fails, stop and report the blocker.

Never deploy without explicit user approval.

### 10. Push Review Gate

Push only after commit and deploy dry-run gates are satisfied or explicitly not applicable.

Run:

- `git fetch origin`
- `git rev-parse --verify @{u}`
- `git rev-list --left-right --count @{u}...HEAD`
- `git log @{u}..HEAD --oneline`

Rules:

- If fetch fails, stop.
- If upstream is missing, stop and ask before setting one.
- If branch is behind or diverged, stop and ask before pull/rebase/merge.
- If branch is ahead only, present outgoing commits and ask before `git push`.
- Never force push.
- After push, rerun `git rev-list --left-right --count @{u}...HEAD`; expected result is `0 0`.
- If post-push verification is not `0 0`, report the mismatch as a blocker.

### 11. Final Report

Tell the user, concisely:

- Exact absolute path of the saved summary file
- Lessons added to `C:\Users\polit\Claude\lessons.md`
- Verification result and command(s)
- Commit hash, or explicit reason no commit was made
- Push status and post-push ahead/behind result
- Deploy dry-run/deploy status
- Final dirty-tree status
- Memory MCP status
- One-line resume prompt

Use absolute file links for local files.

## Gotchas

- `/done` writes files after its first status check. The second dirty-tree gate is mandatory.
- Hooks differ between Claude Code, Codex, and plain Git. Treat hooks as support, not the source of safety.
- Missing gitleaks is a blocker, not a warning, when `/done` is committing or pushing.
- Memory MCP can be stale. Disk state wins.
- GitHub is backup/version control only. Deployment uses `deploy.py`, never GitHub.
- Final "all done" is only true when summary, lessons, verification, commit/push/deploy status, and dirty-tree status have all been reported.
