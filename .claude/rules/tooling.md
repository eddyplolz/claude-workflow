# Tooling

## Subagents

- `code-reviewer`, `architect`, `sprint-planner`: **Read only** (no Write access)
- `general-purpose`, `test-writer`: **Read + Write**
- ASK before spawning 2+ agents
- If an agent fails, STOP and change approach — don't retry the same pattern
- Never rely on agents writing output files — capture results from the task return value
