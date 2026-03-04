# Lessons learned

Record patterns from user corrections here. Review at session start.

## Format
```
### [Date] - [Short description]
**Mistake:** What went wrong
**Fix:** What the correct approach is
**Rule:** The rule to prevent recurrence
```

## Lessons

<!-- Replace these examples with your own correction patterns. -->
<!-- Delete them once you have real entries. -->

### Example - Skipping tests before commit
**Mistake:** Committed a bug fix without running the test suite. Tests would have caught a regression.
**Fix:** Always run tests before committing, even for "obvious" changes.
**Rule:** No commit without a passing test suite. No exceptions.

### Example - Browser verification loops
**Mistake:** After programmatic tests passed, spent 10+ tool calls taking screenshots of every UI state.
**Fix:** Tests passing IS the verification. At most 1 screenshot to confirm page loads.
**Rule:** Programmatic proof = done. Don't loop through visual checks after tests pass.

### Example - Long session degradation
**Mistake:** Marathon sessions caused progressive forgetting of rules, repeated mistakes, and ignored stop signals.
**Fix:** After every commit, assess context health. Hand off and start fresh when context is full.
**Rule:** Every commit triggers a context check. Surface degradation before the user notices.
