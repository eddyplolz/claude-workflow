---
name: commit
description: Use when ready to commit changes. Stages specific files, drafts a conventional commit message, and includes Co-Authored-By footer.
---

# Commit Skill

Create a well-structured git commit following CLAUDE.md conventions.

## Steps

1. **Gather context** (run in parallel):
   - `git status` - see all changes
   - `git diff --stat` - summary of staged + unstaged changes
   - `git log --oneline -5` - recent commit style reference

2. **Analyze changes:**
   - Group changes by purpose (feature, fix, refactor, docs, test, chore)
   - Identify files that should NOT be committed (.env, credentials, temp files)
   - Draft a commit message:
     - First line: `<type>: <summary>` (under 72 chars)
     - Types: feat, fix, refactor, docs, test, chore
     - Body: explain WHY, not what (the diff shows what)

3. **Show the user:**
   - Draft commit message
   - List of files to stage
   - Any files being excluded and why
   - Ask for approval

4. **On approval:**
   - Stage specific files by name (NEVER `git add .` or `git add -A`)
   - Commit using HEREDOC format with Co-Authored-By footer
   - Run `git status` after to verify

5. **Post-commit context check:**
   - Honestly assess context health: how much of the session has been consumed?
   - Tell the user ONE of these:
     - ✅ **"Context is clean"** - early in session, low tool call volume, safe to continue
     - ⚡ **"Recommend compacting"** - moderate context load, `/smart-compact` before next task
     - 🔄 **"Recommend handoff"** - heavy context, long session, risk of degradation. Use `/done` and start fresh.
   - This is mandatory. Do not skip it. Long-session degradation is the #1 source of user frustration.

## Commit Format

```bash
git commit -m "$(cat <<'EOF'
<type>: <summary>

<body if needed>

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

## Safety Rules

- NEVER use `git add .` or `git add -A`
- NEVER commit .env, credentials, API keys, tokens
- NEVER use --amend unless explicitly requested
- NEVER use --no-verify
- NEVER force push
- If pre-commit hook fails: fix the issue, create NEW commit
- Always show the user the commit message before committing
