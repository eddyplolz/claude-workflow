# Session Continuity

- Check handoff docs and `lessons.md` BEFORE asking the user to recall context.
- When resuming, verify prior fixes are present in the codebase before starting new work.
- Never claim prior work is lost without thoroughly searching the project directory, `codex/`, and the auto-memory store.

## Auto-Memory (canonical)

The auto-memory store at `~/.claude/projects/<project-id>/memory/` is the canonical persistent state across sessions. The system prompt's "auto memory" section documents the schema (`user` / `feedback` / `project` / `reference`) and the two-step write process (memory file + `MEMORY.md` index pointer).

**Session start:** `MEMORY.md` is auto-loaded into context — read it. Then read `lessons.md`. Then check handoff docs in `projects/*/codex/`.
**After significant work:** Update relevant auto-memory files. Add or update the `MEMORY.md` pointer for any new or changed file.

**Store:** User profile/preferences, feedback patterns, project status, references to external systems.
**Don't store:** Code patterns, file paths, project structure, or anything derivable from reading the repo.

If a recall conflicts with what's actually on disk: trust the filesystem, update or delete the stale auto-memory entry.

## Memory MCP (legacy)

The Memory MCP knowledge graph (`mcp__memory__*` tools) holds historical entries from earlier sessions but is no longer the canonical store. Skills that previously wrote to it have been redirected to auto-memory. Do not write new entries to MCP unless the user explicitly asks.

If a skill or tool surfaces MCP data, treat it as informational; auto-memory is authoritative.

## Handoff Sequence

1. Update relevant auto-memory entries (only if facts changed worth persisting beyond this session).
2. Write handoff doc to `projects/[project]/codex/HANDOFF-[Desc]-[DD-Mon-YY].md`.
3. Output a copy-pasteable resume prompt.
