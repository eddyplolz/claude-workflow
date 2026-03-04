# Testing

- Run test suite before every commit. No exceptions.
- Browser tests: use `npx serve .` (NOT `file://` URLs). Prefer Chrome MCP over Playwright for localhost.
- For let-scoped variables in iframes: use `window.__test` bridge pattern, not `iframe.contentWindow`.
- After fixing a bug: re-read the modified file to confirm the change is present. Don't report fixed without seeing it.
- Browser testing: hard-refresh or cache-bust after fixes. Cached files cause false "didn't work" reports.
- Before making 10+ changes to a file over 500 lines: commit or stash as a checkpoint.
