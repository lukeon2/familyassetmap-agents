# Family Asset Map for Cursor

One skill and one remote MCP connection for your own Family Asset Map.

## Setup and use

Install this plugin using Cursor's plugin interface when available from your repository or marketplace. The repository marketplace is `.cursor-plugin/marketplace.json`; this package is `plugins/familyassetmap-cursor`.

Connect the Family Asset Map MCP server and complete OAuth in your browser. Approve read and write only if you want edits. No API key is required. Never paste passwords, email codes or passphrases into chat. Start a new conversation with the plugin enabled.

Ask: "Show my family map without notes or balances." On a fictional test map, ask: "Add Example Bank under Banks. Note: documents in the blue folder."

The skill reads the current version before writes and uses idempotency keys. Only your own Standard map is supported. An existing map is not overwritten; E2EE maps must be opened in the app. No bank access, balances, transfers, sharing, deletion or email backups through MCP. Standard data can be decrypted by FAM; tool results go to the connected AI provider.

Revoke access at https://familyassetmap.com/connected-apps. Uninstalling is separate from revoking the grant. Connections expire within seven days.

## Status

Package structure checked locally. Cursor installation, OAuth and conversational acceptance are not yet verified. No Cursor marketplace approval or Grok Bot catalog availability is claimed.

## Links

- Documentation: https://familyassetmap.com/for-agents
- Privacy: https://familyassetmap.com/privacy
- Terms: https://familyassetmap.com/terms
- Support: contact@familyassetmap.com
- Endpoint: https://familyassetmap.com/mcp
