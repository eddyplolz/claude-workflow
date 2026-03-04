#!/usr/bin/env python3
"""
Pre-commit checks hook for Claude Code.

Fires on PreToolUse for Bash commands. When a git commit is detected,
checks if staged files belong to a deployed project and reminds about
deploy.py.

Non-blocking: exits 0 with additionalContext (reminder), never exit 2.
"""

import json
import os
import subprocess
import sys

DEPLOY_CONFIG = "deploy-config.json"


def get_staged_files():
    """Get list of staged files via git diff --cached."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return []


def load_deploy_config():
    """Load deploy-config.json from the workspace root."""
    config_path = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR", "."), DEPLOY_CONFIG)
    if not os.path.exists(config_path):
        return {}
    try:
        with open(config_path) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def find_affected_projects(staged_files, config):
    """Match staged files to deployed projects by local_root prefix."""
    projects = config.get("projects", {})
    affected = set()
    for name, proj in projects.items():
        local_root = proj.get("local_root", "")
        if not local_root:
            continue
        # Normalize separators
        local_root = local_root.replace("\\", "/")
        for f in staged_files:
            f_normalized = f.replace("\\", "/")
            if f_normalized.startswith(local_root):
                affected.add(name)
                break
    return sorted(affected)


def main():
    try:
        input_data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    # Only fire on git commit (not amend, not other git commands)
    if "git commit" not in command or "--amend" in command:
        sys.exit(0)

    staged_files = get_staged_files()
    if not staged_files:
        sys.exit(0)

    config = load_deploy_config()
    if not config:
        sys.exit(0)

    affected = find_affected_projects(staged_files, config)
    if not affected:
        sys.exit(0)

    # Build reminder
    project_list = ", ".join(affected)
    if len(affected) == 1:
        deploy_cmd = f"`python deploy.py {affected[0]} --dry-run`"
    else:
        deploy_cmd = " and ".join(f"`python deploy.py {p} --dry-run`" for p in affected)

    msg = (
        f"DEPLOY REMINDER: This commit touches deployed project(s): {project_list}. "
        f"After committing, run {deploy_cmd} and present the result to the user."
    )

    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": msg,
        }
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
