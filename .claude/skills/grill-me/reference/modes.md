# Grill Me — Challenge Mode Reference

## Expose Assumptions

**Method:** Socratic questioning — keep asking "why?" and "what if that's not true?"

**Process:**
1. Restate the user's plan (steelman it)
2. Identify 3-5 taken-for-granted beliefs embedded in the plan
3. For each assumption, ask one of:
   - "What evidence supports this?"
   - "What would change if this turned out to be false?"
   - "Is this a fact or a preference?"
   - "Who else would need to agree with this for it to hold?"
4. Follow the thread — when an answer reveals a deeper assumption, pursue it
5. Synthesize: which assumptions are validated, which are exposed as risky

**Key question patterns:**
- "You're assuming [X]. What if [not-X]?"
- "This works if [condition]. How confident are you in that?"
- "What's the weakest link in this chain of reasoning?"

---

## Argue the Other Side

**Method:** Hegelian dialectic — construct the strongest possible opposing case.

**Process:**
1. Restate the user's position (thesis)
2. Build the strongest opposing position (antithesis) — genuinely try to win
3. Present it: "Here's the best case against your plan..."
4. Let the user respond to each point
5. Synthesize: where does the truth land between the two positions?

**Rules:**
- The opposing case must be intellectually honest, not a strawman
- Use real-world examples, data, or precedents where possible
- If the user's original position survives the challenge intact, say so — that's a strong plan
- If it doesn't, identify which parts need revision

---

## Find Failure Modes

**Method:** Pre-mortem analysis — imagine the plan has already failed, then work backwards.

**Process:**
1. Ask: "Imagine it's [timeframe] from now and this has failed. What went wrong?"
2. Generate 5-7 plausible failure scenarios, categorized:
   - **Technical failures** — things that break, scale issues, integration problems
   - **Human failures** — misunderstandings, skill gaps, motivation issues
   - **External failures** — dependencies, market changes, timeline shifts
   - **Design failures** — wrong abstraction, wrong tradeoff, missing requirement
3. For each failure mode, ask:
   - "How likely is this? (high/medium/low)"
   - "How would we detect it early?"
   - "What's the mitigation or fallback?"
4. Rank by likelihood x impact
5. Present the top 3 failure modes and their mitigations

**Key insight:** The most dangerous failures are the ones the user hasn't considered. Push into uncomfortable territory.

---

## Red Team

**Method:** Adversarial assessment — actively try to break or exploit the plan.

**Process:**
1. Restate what's being built and its intended behavior
2. Attack from multiple angles:
   - **Abuse cases** — how could a bad actor misuse this?
   - **Edge cases** — what inputs or states weren't considered?
   - **Scale attacks** — what happens at 10x, 100x load?
   - **Integration attacks** — what happens when a dependency fails?
   - **Social engineering** — can someone manipulate the intended workflow?
3. For each vulnerability found:
   - Severity (critical / high / medium / low)
   - Attack vector (how someone would exploit it)
   - Proposed defense
4. Present findings ranked by severity

**Tone:** This mode is deliberately adversarial. Don't soften the findings. Real attackers won't be polite.

---

## Test the Evidence

**Method:** Falsificationism — audit every claim against available evidence.

**Process:**
1. Extract every claim or assumption in the plan (explicit and implicit)
2. For each claim, ask:
   - "What evidence supports this?" (not opinion — evidence)
   - "What would disprove this?"
   - "Has anyone tried this before? What happened?"
   - "Are you extrapolating from a small sample?"
3. Classify each claim:
   - **Supported** — evidence exists and is solid
   - **Plausible** — reasonable but unverified
   - **Unsupported** — no evidence, just belief
   - **Contradicted** — evidence points the other way
4. Focus interrogation on Unsupported and Contradicted claims
5. Present: which parts of the plan rest on solid ground, which are faith-based

**Key question patterns:**
- "You said [X]. What's that based on?"
- "Is there a case where [X] didn't work?"
- "If I showed you [counter-evidence], would that change your plan?"
