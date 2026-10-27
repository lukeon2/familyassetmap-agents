# Release validation — 1.0.0

Date: 2026-10-27 UTC.

## Status

- Claude Code 2.1.311: marketplace and plugin both pass `plugin validate --strict`.
- Clean isolated configuration: local marketplace add, plugin install, details (one skill, one HTTP MCP server), uninstall and marketplace removal all PASS. Remote GitHub installation: PASS from `lukeon2/familyassetmap-agents` in a second clean configuration; plugin details confirm one skill and one HTTP MCP server. No model invocation or Claude account was used.
- Live MCP discovery: PASS (HTTP 200 resource/authorization metadata with read/write scopes, HTTP 401 challenge on anonymous MCP). Public agent guide, privacy, terms and logo links return HTTP 200.
- Interactive Claude OAuth/read/write/revoke: NOT TESTED. A Claude user account is not available for this release's acceptance test. Do not claim full Claude compatibility or directory approval from package validation alone.

The backend has separate SDK and browser tests for OAuth, scope enforcement, reads, writes, idempotency, version conflicts and revocation. These do not replace a real Claude-client test.

## Acceptance test in Claude Code

Use a normal FAM account and fictional data. Prefer an account without an existing map; each account can own one map. No special reviewer login is supplied.

1. Install using the README commands in a clean Claude Code configuration. Confirm one skill and one HTTP MCP server.
2. Authenticate through `/mcp`. Email code stays in the browser. Approve read/write.
3. Invoke the skill and ask for the map list. If empty, request a Standard map named `Claude QA`; otherwise inspect the existing test map without replacing it.
4. Add `Example Bank` under `Banks` with note `Blue folder`. Confirm in FAM. Update that exact institution's note to `Green folder`; confirm it changed once and unrelated data stayed unchanged.
5. Request a summary; verify it excludes notes and balances. Explicitly request the test institution detail; verify only that detail is returned.
6. Reconnect with only read approved. Reads must work. A requested write must fail or trigger browser consent for write access, never silently mutate data.
7. For an E2EE account, verify the agent offers an app link and does not decrypt, change or replace the map.
8. Revoke at Connected apps. Verify subsequent use fails or requires fresh browser authorization. Uninstall the plugin and remove the marketplace; verify it disappears.

Record client version, outcome and date, without tokens, codes or real map contents. Remove test institutions manually in the web application if desired; deletion is not an MCP tool.

## Codex — 2026-10-27

- Codex CLI 0.163.0-alpha.11.2: local marketplace recognized and plugin 1.0.0 installed; bundled HTTP MCP configuration recognized.
- Actual Codex OAuth login with the authorized test account: PASS using client metadata discovery (CIMD), PKCE and read/write scopes.
- Live seven-tool protocol exercise using a separate MCP SDK client on that account: PASS for listing, bounded summaries, add, update, selective read, duplicate retry, version conflict, secret-like input refusal, unauthorized ID refusal, app link and revocation of access/refresh tokens. Existing map rows preserved; one fictional QA institution added.
- These protocol checks are not an end-to-end model conversation test. Existing Codex chat cannot reload the newly installed plugin's tools mid-session; begin a new session for conversational acceptance.
- Dedicated reviewer environment and public-directory submission status: see CODEX_REVIEW.md.
