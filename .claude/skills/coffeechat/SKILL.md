---
name: coffeechat
description: Use for a periodic check-in on project health, loose ends, and workflow improvements. Best every 1-2 weeks or when starting a new focus area.
---

# Coffee Chat

A friendly, plain-English check-in. No jargon. The goal is to help a non-technical user understand what's been happening, what needs attention, and how we can work better together.

## Tone

Write like you're talking to a friend over coffee. Be honest, specific, and practical. If something is going well, say so. If something keeps going wrong, own it. Avoid technical metrics unless they tell a clear story.

## Steps

1. **Gather data** (run in parallel):
   - `git log --oneline --since="2 weeks ago" --all` — recent commits across all branches
   - `git log --format="%ai" --since="2 weeks ago" | head -20` — activity dates
   - Read `lessons.md` — correction patterns
   - Read Memory MCP graph — project statuses, deferred items
   - List `projects/` directory — what's active
   - Glob for `projects/*/codex/SESSION-*.md` — recent session summaries
   - Glob for `projects/*/codex/HANDOFF-*.md` — handoff docs with deferred work

2. **Read recent session summaries** (last 3-5 across all projects):
   - Extract Follow-Up Tasks sections — these are promises we made
   - Extract Open Questions — things left hanging
   - Extract Lessons/Corrections — patterns from recent work

3. **Analyze and synthesize** into these sections:

---

### Report Format

Write the report directly to the user in chat (not to a file). Use this structure, but keep it conversational:

#### What We've Been Up To
- 2-4 sentences summarizing recent work across projects
- Which projects got attention, which didn't
- Plain English — "We spent most of our time on the API, building out endpoints and a test suite" not "14 commits across 8 files in src/api"

#### Loose Ends
- Scan ALL session summaries' Follow-Up Tasks for items that were never completed in a later session
- Scan HANDOFF docs for deferred items
- Present as a simple list: what it is, which project, how long it's been sitting there
- If nothing is overdue, say so! That's worth celebrating.
- **This is the most important section.** Things slip through the cracks when sessions end. This catches them.

#### Things I Keep Getting Wrong
- Analyze `lessons.md` for patterns:
  - Are there categories with multiple entries? (e.g., 3 lessons about agent spawning = a pattern)
  - Any recent corrections (last 2 weeks)?
  - Have old patterns stopped recurring? (That's progress!)
- Be honest and specific: "I've been corrected about X three times now. Here's what I'm doing differently."
- If no recent corrections: say that clearly — it means things are going well.

#### How Our Workflow Is Going
- Are we following our own rules? (Check CLAUDE.md rules against recent session behavior)
- Any skills or workflows that feel clunky or could be improved?
- Are handoffs working? (Do sessions pick up cleanly from where they left off?)
- Anything the user might want to try that they haven't yet?
- **Keep suggestions beginner-friendly.** Explain what a thing does before suggesting it.

#### Project Health at a Glance
A simple table — one row per active project:

| Project | Last Activity | Status | Needs Attention? |
|---------|--------------|--------|-----------------|
| name | X days ago | brief status | yes/no + why |

- Pull "last activity" from git log per project directory
- Pull "status" from Memory MCP or most recent session summary
- "Needs attention" = has overdue follow-ups, no activity in 2+ weeks, or incomplete sprints

#### Suggested Next Steps
- 2-3 concrete, actionable things we could do next
- Prioritize: loose ends first, then new work
- Frame as suggestions, not demands: "If you have time, we could..." or "Whenever you're ready, the next thing on deck is..."

---

## Rules

- **No file output.** This goes straight into the chat as a conversation.
- **Plain English only.** The user is not a developer. "We wrote tests" not "We implemented a 365-assertion test suite across 5 modules."
- **Be honest about mistakes.** The user values transparency. If we messed up, say so clearly.
- **Celebrate progress.** If a project is in good shape, say it. If a pattern stopped recurring, note it.
- **Keep it scannable.** Use short paragraphs, bullet points, and the table. Nobody wants to read an essay over coffee.
- **Don't over-promise.** Suggestions should be realistic for the user's available time and interest.
- **If data is missing** (no recent sessions, empty lessons.md, Memory MCP down), say so honestly rather than padding the report.
