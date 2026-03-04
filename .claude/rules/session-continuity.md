# Session Continuity

- Check handoff docs and `lessons.md` BEFORE asking the user to recall context.
- When resuming, verify prior fixes are present in the codebase before starting new work.

## Memory MCP

**Session start:** Read knowledge graph + `lessons.md` + check handoff docs.
**After sprints/major work:** Update Memory MCP, then write handoff doc.

**Store:** Project status, deployment state, deferred work, architecture decisions, key paths.
**Don't store:** Code snippets, full file contents, temp debug info.

If Memory MCP is unavailable: fall back to `projects/*/codex/HANDOFF*.md`.
If Memory MCP returns stale data: trust the filesystem, update memory to match.

## Handoff Sequence

1. Update Memory MCP
2. Write handoff doc to `projects/[project]/codex/HANDOFF-[Desc]-[DD-Mon-YY].md`
3. Output a copy-pasteable resume prompt
