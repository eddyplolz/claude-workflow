---
name: resume
description: Use at the start of any session to pick up where you left off. Restores context from Memory MCP, handoff docs, and git state.
---

# Resume Session

Quickly restore context from the last work session using Memory MCP + handoff docs.

## Steps

1. **Read Memory MCP knowledge graph** using `mcp__memory__read_graph`

2. **Read `lessons.md`** - flag any lessons relevant to the project about to be worked on

3. **Show project dashboard** - for each project entity, display:
   - Name and status (Active / Complete / Paused)
   - Deployment state (deployed, awaiting deployment, undeployed)
   - Deferred work count
   - Last known activity

3. **Check git state:**
   - `git status` - any uncommitted changes?
   - `git branch` - what branch are we on?
   - `git log --oneline -5` - recent commits

4. **Show summary to user** in this format:
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

5. **When user picks a project:**
   - Read that project's Memory MCP entity for full context
   - Find the most recent handoff doc: glob `projects/[project]/**/HANDOFF*.md` (standardized to `codex/` but check all locations for older docs)
   - Read the handoff doc
   - Summarize: "Last session: [what happened]. Next up: [deferred items / next sprint]."

## Notes

- If Memory MCP is empty, fall back to scanning `projects/` directories for PROJECT.md, SPRINTS.md, handoff docs
- Don't read every file - use Memory MCP as the primary source, handoff docs for detail
- Keep the dashboard concise - the user wants to get to work, not read a report
