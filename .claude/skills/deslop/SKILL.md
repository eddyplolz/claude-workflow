---
name: deslop
description: Use after writing or generating code to clean up AI artifacts. Targets obvious comments, unnecessary error handling, premature abstractions, and debug leftovers in the recent diff.
---

# Deslop - AI Code Cleanup

Run a focused cleanup pass on recent changes, targeting patterns that AI code generation tends to produce.

## Steps

1. **Get the diff to review:**
   - If there are uncommitted changes: `git diff` (unstaged) + `git diff --cached` (staged)
   - If everything is committed: `git diff HEAD~1` (last commit)
   - Show the user which diff you're reviewing

2. **Scan for slop patterns** in the diff. Look for:

   **Comments that restate the code:**
   - `// increment counter` above `counter++`
   - `// return the result` above `return result`
   - `// loop through items` above `for (const item of items)`
   - Any comment where deleting it loses zero information

   **Unnecessary error handling:**
   - try/catch that only rethrows or logs and rethrows
   - Empty catch blocks
   - Defensive null checks on values that can never be null (internal code, not API boundaries)
   - Validation of function parameters that are only called from trusted internal code

   **Premature abstractions:**
   - Helper functions called exactly once
   - Utility functions that could be inline one-liners
   - Configuration objects for things that will never be configured
   - Wrapper classes that add no behavior

   **Debug leftovers:**
   - `console.log`, `print()`, `debugger` statements not part of a logging system
   - Commented-out code blocks
   - TODO/FIXME comments added in the current diff (not pre-existing ones)

   **Over-engineering:**
   - Backwards-compatibility shims for code that was just written
   - Feature flags for features that aren't optional
   - Excessive type annotations on obvious types (TypeScript `const x: string = "hello"`)
   - Redundant type casts

3. **Report findings** grouped by file, with line references. Example:
   ```
   src/utils.ts:
   - L12: Comment restates code ("// parse the JSON response")
   - L45-52: try/catch only rethrows with same message
   - L78: formatDate() helper called once, inline it

   src/api.ts:
   - L33: console.log debug statement
   ```

4. **Ask the user** which findings to fix (all, specific files, or skip).

5. **Apply fixes** - edit each file, removing only the identified patterns.

6. **Run tests** to confirm no behavior changed. If tests fail for a file, revert that file's changes immediately and report what happened.

7. **Summary** - one line: what was removed and from how many files.

## Guardrails

- **NEVER** remove error handling at system boundaries (user input, external APIs, file I/O, network calls)
- **NEVER** remove comments that explain *why* something is done - only remove comments that explain *what* the code does
- **NEVER** change behavior - this is cosmetic cleanup only
- **NEVER** touch code outside the diff (pre-existing slop is out of scope unless user asks)
- If unsure whether something is slop, leave it alone
- If tests fail after a cleanup edit, revert and move on
