# Prompt Improver - Analysis Guide

## Dimension Details

### 1. Clarity
- Is the main request unambiguous?
- Are technical terms used correctly?
- Could this be misinterpreted?

**Common issues:**
- Pronouns without clear referents ("fix it", "make it work")
- Ambiguous scope ("clean up the code")
- Missing context (which file? which function?)

### 2. Specificity
- Are vague terms defined? ("quickly", "better", "nice")
- Is the scope bounded?
- Are measurable outcomes stated?

**Common issues:**
- Undefined qualitative terms
- Open-ended requests without boundaries
- Missing success criteria

### 3. Structure
- Is the request organized logically?
- Are multiple requirements separated clearly?
- Would examples help?

**Common issues:**
- Run-on requests mixing multiple tasks
- Missing examples of desired output
- No clear priority ordering

### 4. Completeness
- Are constraints specified?
- Are edge cases considered?
- Is error handling addressed?
- Are preferences stated?

**Common issues:**
- Missing file paths or locations
- No mention of error handling
- Unstated preferences (formatting, style, approach)

---

## Examples

### Example 1: Vague Request

**Input:** `fix the login bug`

**Analysis:**
| Dimension    | Rating   | Notes                              |
|--------------|----------|-------------------------------------|
| Clarity      | Weak     | Which bug? Which login?            |
| Specificity  | Weak     | No symptoms or expected behavior   |
| Structure    | Adequate | Simple enough to not need structure |
| Completeness | Weak     | No file paths, no reproduction steps |

**Option A (Minimal):**
> Fix the login bug in [file path] where [symptom]

**Option B (Comprehensive):**
> There's a bug in the login flow. When [trigger], [symptom] happens instead of [expected]. The relevant code is in [file]. Please fix it and add a test to prevent regression.

### Example 2: Decent But Improvable

**Input:** `add a button to the settings page that exports data as CSV`

**Analysis:**
| Dimension    | Rating   | Notes                              |
|--------------|----------|-------------------------------------|
| Clarity      | Strong   | Clear what's wanted                |
| Specificity  | Adequate | Which data? Which settings page?   |
| Structure    | Adequate | Single task, fine as-is            |
| Completeness | Adequate | No error handling or styling prefs |

**Option A (Minimal):**
> Add a button to the settings page (src/pages/Settings.tsx) that exports user data as CSV

**Option B (Comprehensive):**
> Add an "Export Data" button to the settings page (src/pages/Settings.tsx) that:
> - Exports user profile and preferences as CSV
> - Uses the existing button styles
> - Shows a loading state during export
> - Handles errors gracefully with a toast notification
