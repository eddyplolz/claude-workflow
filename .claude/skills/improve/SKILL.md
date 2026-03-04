---
name: improve
description: Use before sending a complex or important prompt to Claude. Analyzes weaknesses and provides 2-3 improved versions to choose from. Run with /improve followed by your draft prompt.
---

# Prompt Improver

Analyze the user's draft prompt and provide improved versions.

## Input

The user provides their draft prompt after `/improve`. Example:
```
/improve help me fix the bug in my code
```

## Steps

1. **Evaluate** the prompt across four dimensions: Clarity, Specificity, Structure, Completeness
   - Rate each: **Strong** / **Adequate** / **Weak**
   - For detailed analysis criteria, read `reference/analysis-guide.md`

2. **Present analysis** as a table:
   ```
   | Dimension    | Rating   | Notes                |
   |--------------|----------|----------------------|
   | Clarity      | [rating] | [1-line observation] |
   | Specificity  | [rating] | [1-line observation] |
   | Structure    | [rating] | [1-line observation] |
   | Completeness | [rating] | [1-line observation] |
   ```

3. **Generate 2-3 improved versions:**

   **Option A: Minimal Fixes** - targeted fixes to weak areas only
   **Option B: Comprehensive** - fuller rewrite improving all dimensions
   **Option C: Structured** - formal version with headers/bullets (only if complex enough to warrant it)

   Show `**Changes:**` list under each option.

4. **Ask which version** works best, or what to change.

5. **Update preferences** after selection (see Preference Learning below).

## Special Cases

- **Very short prompts (< 10 words):** Focus on what file, what should happen, how to handle errors
- **Already good prompts:** Acknowledge it's solid, offer only minor polish
- **Multi-part requests:** Suggest breaking into separate prompts, show each improved independently

## Preference Learning

Check `~/.claude/improve-preferences.json` for existing preferences.

```json
{
  "preferred_style": "minimal|comprehensive|structured",
  "format_preferences": { "uses_headers": true, "likes_examples": true, "bullet_points": true },
  "total_uses": 0
}
```

When preferences exist, mention: "Based on your history, I've weighted toward [style] options."
After selection, update the JSON. Set `preferred_style` after 3+ selections of same style.

## Tone

- Direct and constructive, not critical
- Focus on what makes the prompt more effective
- Keep analysis concise - the improved versions are the main value
