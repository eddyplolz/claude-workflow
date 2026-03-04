---
name: done
description: Use at the end of any work session to wrap up. Captures decisions, corrections, follow-ups, and lessons into a dated summary file before closing.
---

# Done — Session Wrap-Up

Generate a structured session summary and save it to the active project's `codex/` folder.

## Steps

1. **Gather context** (run in parallel):
   - `git rev-parse --abbrev-ref HEAD` — current branch name
   - `git log --oneline -10` — recent commits this session
   - `git diff --stat HEAD~5 HEAD` — files touched recently
   - `git status --short` — check for uncommitted changes
   - Read `lessons.md` — check if anything from this session should be added

2. **Check for uncommitted changes** (guard — do this before anything else):
   - If `git status` shows staged or unstaged modifications, or untracked files in the project directory:
     - List the uncommitted files to the user
     - Ask: **"There are uncommitted changes — commit first before wrapping up?"**
     - If user says yes: invoke the `/commit` skill, wait for it to complete, then continue
     - If user says no: proceed with the summary, but note the uncommitted files in the **Follow-Up Tasks** section
   - If no uncommitted changes: proceed silently

3. **Classify the session type:**
   - **Coding session** — commits were made, code was written/modified
   - **Config/tooling session** — CLAUDE.md, rules files, skills, hooks, or settings changed
   - **Discussion session** — planning, decisions, research, or Q&A with no/few file changes
   - A session can be more than one type. This classification determines which template sections to include.

4. **Identify the active project:**
   - Infer from the branch name, working directory, or conversation context
   - Target folder: `projects/[project]/codex/`
   - If no active project is obvious, use `scratch/`

5. **Scan for user corrections** by reviewing the full conversation history:
   - Find every instance where the user corrected you, redirected your approach, or expressed frustration
   - For each correction, extract: what went wrong, what the correct approach was, and a prevention rule
   - These go into `lessons.md` in step 8 — do NOT skip this

6. **Synthesize the session** by reviewing the full conversation history:
   - What was worked on
   - Key decisions made (and why)
   - User preferences expressed (style, workflow, tool choices, naming conventions)
   - Files changed (code, config, rules, skills — all count)
   - Open questions or unresolved blockers
   - Follow-up tasks (things mentioned but not done)
   - Any user corrections (from step 5)
   - Lessons worth preserving

7. **Write the summary** using a collision-safe filename:
   `[target]/SESSION-[branch]-[YYYY-MM-DD]-[topic-slug].md`

   Where `topic-slug` is a 1–3 word descriptor of the main work done (e.g., `insights`, `election-fixes`, `config-hooks`, `fiscal-planner`). Use kebab-case, keep it short and scannable.

   Before writing: check if a file with this name already exists. If so, append `-2`, `-3`, etc.

   Use this format — include ALL sections, but mark empty ones as "None this session":
   ```markdown
   # Session Summary — [YYYY-MM-DD]

   **Branch:** [branch name]
   **Project:** [project name]
   **Session type:** [Coding / Config / Discussion — or combination]

   ## What We Did
   [2–5 bullet points, concrete and specific]

   ## Key Decisions
   [Decisions made, with brief rationale. Include WHY, not just what.]

   ## Preferences & Conventions
   [Any user preferences expressed — workflow choices, naming conventions,
   tool preferences, style decisions. These inform future sessions.]

   ## Files Changed
   [All files modified — code, config, rules, skills, hooks. Not just git-tracked code.]

   ## Open Questions
   [Things left unresolved or that need a decision next time]

   ## Follow-Up Tasks
   [Specific next actions, not vague intentions]

   ## Lessons / Corrections
   [Anything that should go into lessons.md if not already there]
   ```

8. **Update `lessons.md`** with every correction found in step 5. For each, append:
   ```
   ## [YYYY-MM-DD] - [Category]
   - What went wrong: [description]
   - Correct approach: [what should have happened]
   - Rule: [prevention rule for future sessions]
   ```
   Check existing entries first to avoid duplicates. This step is MANDATORY — if corrections were found in step 5, they MUST appear in `lessons.md`.

9. **Update Memory MCP** with any changed project status, new deferred items, or decisions.

10. **Tell the user:**
   - Exact path of the saved file
   - Any lessons added to `lessons.md`
   - A one-line "next time" prompt they can paste to resume

## Notes

- Keep bullet points short — this is a reference doc, not a narrative
- The "next time" resume prompt should be copy-pasteable as a first message
- For discussion-only sessions: "Files Changed" may be empty — that's fine, the value is in Decisions and Preferences
- NEVER overwrite an existing session file. Always use the collision-safe naming.
