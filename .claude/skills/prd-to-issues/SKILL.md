---
name: prd-to-issues
description: Use when you have a PRD or spec and need to create actionable GitHub issues. Breaks requirements into vertical slices (tracer bullets) with dependency ordering.
---

# PRD to Issues

Break a PRD into independently-grabbable GitHub issues using vertical slices (tracer bullets).

## Process

### 1. Locate the PRD

Ask the user for the PRD — could be a GitHub issue number, a file in `codex/`, or pasted text.

If it's a GitHub issue, fetch with `gh issue view <number>`.

### 2. Explore the codebase (if needed)

If you haven't already explored the codebase, do so to understand the current state.

### 3. Draft vertical slices

Break the PRD into **tracer bullet** issues. Each issue is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

Slices are tagged as:
- **HITL** (Human-in-the-loop): Requires a human decision — architectural choice, design review, UX decision
- **AFK** (Autonomous): Can be implemented and merged without human interaction

Prefer AFK over HITL where possible.

**Vertical slice rules:**
- Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Prefer many thin slices over few thick ones

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each slice, show:

- **Title**: short descriptive name
- **Type**: HITL / AFK
- **Blocked by**: which other slices (if any) must complete first
- **User stories covered**: which user stories from the PRD this addresses

Ask:
- Does the granularity feel right?
- Are the dependency relationships correct?
- Should any slices be merged or split?
- Are HITL/AFK labels correct?

Iterate until approved.

### 5. Create the GitHub issues

For each approved slice, create a GitHub issue with `gh issue create`. Create in dependency order (blockers first) so you can reference real issue numbers.

**Issue template:**

```markdown
## Parent PRD

#<prd-issue-number>

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation. Reference specific sections of the parent PRD rather than duplicating content.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Blocked by

- Blocked by #<issue-number> (if any)

Or "None - can start immediately" if no blockers.

## User stories addressed

Reference by number from the parent PRD:

- User story 3
- User story 7
```

Do NOT close or modify the parent PRD issue.
