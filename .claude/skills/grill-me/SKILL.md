---
name: grill-me
description: Use before implementing features, writing PRDs, or making architectural decisions. Stress-tests plans through structured interview and challenge modes.
---

# Grill Me

Interview the user relentlessly about their plan until you reach shared understanding — or challenge it through a specific reasoning mode.

## Step 1: Choose a Mode

After hearing the elevator pitch, ask:

> How should I approach this?

| Mode | What it does |
|------|-------------|
| **General Interview** (default) | Walk the full decision tree, branch by branch |
| **Expose Assumptions** | Socratic questioning to surface hidden beliefs |
| **Argue the Other Side** | Build the strongest opposing case |
| **Find Failure Modes** | Pre-mortem — how does this break? |
| **Red Team** | Adversarial stress-test of vulnerabilities |
| **Test the Evidence** | Audit claims against actual evidence |

Use `AskUserQuestion` with these as options. If user says "just grill me" or doesn't pick, use General Interview.

For mode-specific methodology, read `reference/modes.md` after selection.

## Core Rules (All Modes)

1. **One question at a time.** Never ask multiple questions in a single message.
2. **Go deep before going wide.** Follow up on each branch before moving to the next.
3. **Resolve dependencies.** If decision B depends on A, resolve A first.
4. **Challenge assumptions.** If the user says "we'll just do X", ask why X and not Y.
5. **Name the tradeoffs.** When you see a tradeoff, state both sides explicitly.
6. **Steelman first.** Before challenging, restate the user's position in its strongest form.
7. **Summarize periodically.** After every 5-6 exchanges, give a "here's where we are" summary.
8. **Know when to stop.** When all branches are resolved, present the final output.

## General Interview Process

### 1. Understand the scope
Ask: "What are you planning to build/change?" Get the elevator pitch.

### 2. Map the decision tree
Identify major branches: core entities, integration points, user-facing behaviors, constraints.

### 3. Walk each branch
For each: simplest version, edge cases, failure scenarios, interactions with other decisions.

### 4. Resolve conflicts
"Earlier you said X, but now Y implies Z. Which takes priority?"

### 5. Present the decision tree
- Decisions made (with rationale)
- Open questions (if any remain)
- Recommended next step

## Challenge Mode Output

All challenge modes end with a five-part synthesis:

1. **Steelmanned position** — the user's plan in its strongest form
2. **Challenges raised** — the 3-5 strongest issues surfaced
3. **User responses** — how each challenge was addressed (or not)
4. **Revised position** — the improved plan incorporating insights
5. **Recommended next steps** — concrete actions
