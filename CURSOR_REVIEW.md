# Cursor submission handoff

Prepared 2026-10-28. Repository: https://github.com/lukeon2/familyassetmap-agents

## Package ready

- Repository marketplace: `.cursor-plugin/marketplace.json`.
- Plugin directory: `plugins/familyassetmap-cursor`.
- Manifest: `plugins/familyassetmap-cursor/.cursor-plugin/plugin.json`.
- MCP configuration: `plugins/familyassetmap-cursor/mcp.json`.
- Includes the existing family-map skill, committed logo, README and MIT license.
- Server: https://familyassetmap.com/mcp; browser OAuth, no embedded secrets.

## Steps for the submitting agent

1. Open https://cursor.com/marketplace/publish and sign in as the publisher.
2. Submit the public repository URL above. For a plugin path, use `plugins/familyassetmap-cursor`. The root Cursor marketplace identifies this package separately from Claude and Codex.
3. Review name Family Asset Map, publisher Family Asset Map, website https://familyassetmap.com, documentation https://familyassetmap.com/for-agents, privacy https://familyassetmap.com/privacy, terms https://familyassetmap.com/terms and support contact@familyassetmap.com. Use a category actually offered by the portal.
4. Check the imported logo, one skill and one remote MCP connection. Address actual validation findings in the repo, then push and revalidate.
5. Before claiming local testing, install in Cursor and complete OAuth on a fictional test account. Verify seven tools, summary without notes/balances, explicit add/update, app link, secret refusal, unauthorized-map refusal, and refusal after revocation. Reviewer credentials, if requested, belong only in private review fields; never in this repository.
6. Submit only accurate attestations. Record the actual submission identifier, status and any follow-up requirements. Package readiness is not marketplace approval.
7. After publication, check Grok Bot's Connect apps search for Family Asset Map and test browser OAuth there. Do not cancel the existing x.ai submission or claim that it is unnecessary without confirmation from the platform.

## Validation and limits

Local structural checks cover marketplace resolution, manifest paths, bundled assets/skill, and the exact URL-only MCP config. Cursor runtime installation and end-to-end conversation testing are still pending. No submission has been sent by this change.

Official reference: https://cursor.com/docs/reference/plugins
Grok Bot app help: https://cursor.com/help/grok-bot/connect-apps
The user supplied https://x.com/mikecarbone/status/2110441404866412552 as evidence of cross-catalog availability; it could not be fetched during preparation. It is not treated as verified proof that Cursor approval automatically publishes FAM in Grok Bot or replaces x.ai review.
