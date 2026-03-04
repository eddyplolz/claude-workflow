#!/usr/bin/env python3
"""
Context monitor hook for Claude Code.

Fires on PostToolUse. Warns when the session transcript grows large,
which correlates with context window filling up.

Thresholds are deliberately conservative — better to warn early than late.
Tune WARN_BYTES and CRITICAL_BYTES based on observed behavior.
"""

import json
import os
import sys
import time

# --- Thresholds (transcript file size in bytes) ---
# These are rough proxies for context usage. Start conservative, tune up.
WARN_BYTES = 500_000       # ~40% context remaining — wrap up current task
CRITICAL_BYTES = 900_000   # ~25% context remaining — stop and hand off

# Minimum tool calls between repeated warnings at the same level.
# Severity escalation (warning → critical) bypasses this.
DEBOUNCE_CALLS = 8


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    transcript_path = input_data.get("transcript_path", "")
    session_id = input_data.get("session_id", "unknown")

    if not transcript_path or not os.path.exists(transcript_path):
        sys.exit(0)

    file_size = os.path.getsize(transcript_path)

    if file_size < WARN_BYTES:
        sys.exit(0)

    level = "critical" if file_size >= CRITICAL_BYTES else "warning"

    # --- Debounce via state file ---
    temp_dir = os.environ.get("TEMP", os.environ.get("TMP", "/tmp"))
    state_file = os.path.join(temp_dir, f"claude-ctx-{session_id}.json")

    state = {}
    if os.path.exists(state_file):
        try:
            with open(state_file) as f:
                state = json.load(f)
        except (json.JSONDecodeError, IOError):
            state = {}

    calls_since = state.get("calls_since_warn", 0) + 1
    last_level = state.get("last_level", "none")

    # Fire if: enough calls since last warning, OR escalating severity
    escalating = (level == "critical" and last_level != "critical")

    if calls_since < DEBOUNCE_CALLS and not escalating:
        state["calls_since_warn"] = calls_since
        try:
            with open(state_file, "w") as f:
                json.dump(state, f)
        except IOError:
            pass
        sys.exit(0)

    # --- Build warning message ---
    size_kb = file_size // 1024

    if level == "critical":
        msg = (
            f"CONTEXT MONITOR [CRITICAL] — Session transcript is {size_kb}KB. "
            "Context is very full. STOP starting new tasks. "
            "Finish current work, then use /done for a handoff and start a fresh session."
        )
    else:
        msg = (
            f"CONTEXT MONITOR [WARNING] — Session transcript is {size_kb}KB. "
            "Context is filling up. Begin wrapping up the current task. "
            "Consider /smart-compact if more work is needed, or /done to hand off."
        )

    # --- Update state ---
    state = {
        "last_level": level,
        "calls_since_warn": 0,
        "last_warn_time": time.time(),
        "file_size_bytes": file_size,
    }
    try:
        with open(state_file, "w") as f:
            json.dump(state, f)
    except IOError:
        pass

    # --- Inject warning into conversation context ---
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg,
        }
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
