---
name: resume
description: Use at the start of any session to pick up where you left off. Restores context from auto-memory, handoff docs, and git state.
---

# Resume Session

Quickly restore context using the auto-memory store + handoff docs + git.

## Steps

1. **Auto-memory is already loaded.** `MEMORY.md` and the user-memory files in `C:\Users\polit\.claude\projects\C--Users-polit-Claude\memory\` are auto-loaded into context per the system prompt's auto-memory rules. Skim the index in `MEMORY.md` for active project entries.

2. **Read `lessons.md`** — flag any lessons relevant to the project about to be worked on.

3. **Build a project dashboard** from auto-memory `project_*.md` files plus the most recent `projects/*/codex/SESSION-*.md` summaries. For each active project show:
   - Name and status (Active / Complete / Paused)
   - Deployment state (deployed, awaiting deployment, undeployed)
   - Deferred work count (from latest SESSION/HANDOFF doc Follow-Up Tasks)
   - Last known activity (from git log on the project directory)

4. **Check git state:**
   - `git status --short --branch` — uncommitted changes? branch?
   - `git log --oneline -5` — recent commits

5. **Show summary to user** in this format:
   ```
   ## Project Dashboard

   | Project | Status | Deferred Items | Deploy State |
   |---------|--------|---------------|-------------|
   | ...     | ...    | ...           | ...         |

   ## Git State
   Branch: [branch], [clean/dirty]
   Last commit: [message]

   ## What would you like to work on?
   ```

6. **When user picks a project:**
   - Read the relevant `project_<name>.md` auto-memory file (if present)
   - Find the most recent handoff doc: glob `projects/[project]/**/HANDOFF*.md` (standardized to `codex/` but check all locations for older docs)
   - Read the handoff doc
   - Summarize: "Last session: [what happened]. Next up: [deferred items / next sprint]."

## Memory MCP (legacy)

The MCP knowledge graph at `mcp__memory__*` holds historical entries from earlier sessions but is no longer the canonical store. Skip reading it during `/resume`; auto-memory has the information now.

## Gotchas (from real failures)

- **Don't trust auto-memory without disk verification.** Memory entries can drift from disk reality (renamed files, removed flags, completed work). Always verify project state on disk before presenting as fact.
- **Read the handoff doc thoroughly, don't skim.** A handoff that said "hostnames are read-only" was ignored, leading to questions already answered. The handoff exists precisely so the next session doesn't re-ask.
- **User's backlog list takes priority over memory.** When the user tells you what's pending, start from their list. Don't substitute your own assessment.
- **Check in with the user before starting work.** Session resume = present state, ask how to proceed. Never interpret a continuation prompt as "start coding immediately."
- **Post-compaction data is unreliable.** After context compaction, summarized data can contain fabrications. Re-fetch sources before committing specific data to plans.

## Notes

- If auto-memory has no relevant entry for the chosen project, fall back to scanning `projects/[project]/` for PROJECT.md, SPRINTS.md, handoff docs.
- Don't read every file — auto-memory + the latest SESSION/HANDOFF doc per project is enough for the dashboard.
- Keep the dashboard concise — the user wants to get to work, not read a report.
