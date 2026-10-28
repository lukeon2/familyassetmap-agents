# Family Asset Map for AI agents

<img src="assets/folio-mark.svg" width="64" height="64" alt="Family Asset Map logo">

Maintain a family information map: which institutions matter and where to find related documents. These packages connect Claude Code, Codex and Cursor to the existing [Family Asset Map](https://familyassetmap.com) service using OAuth and MCP over HTTPS.

This is the publisher's own marketplace, not an approved listing in Anthropic's directory. The package is distributed without a publisher subscription purchase. Using Claude Code requires your own access to that product; this repository does not provide a Claude subscription.

## Install in Claude Code

Run in your terminal with Claude Code installed:

```sh
claude plugin marketplace add lukeon2/familyassetmap-agents
claude plugin install familyassetmap@familyassetmap
```

Start a new Claude Code session. Open `/mcp`, select the Family Asset Map server and authenticate. Complete the FAM email sign-in and consent in the browser. Leave read and write selected if you want Claude to edit your map. Never paste the sign-in code or a passphrase into chat.

Invoke the included skill:

```text
/familyassetmap:family-map Show a summary of my map without notes or balances.
```

Then, on a fictional test map:

```text
Add Example Bank in the Banks category. The note should say: Documents are in the blue folder.
```

If your account already owns a map, the connection uses that map. It does not create a second one or replace it. An existing E2EE map must be opened in the web app and cannot be edited through this connector.

## Install in Codex

```sh
codex plugin marketplace add lukeon2/familyassetmap-agents
codex plugin add familyassetmap@familyassetmap
codex mcp login familyassetmap
```

If your Codex version does not expose `plugin add`, open `/plugins`, choose the Family Asset Map marketplace and install the plugin there. Start a new session after installation. Complete OAuth in your browser, then ask Codex to use Family Asset Map for your task. Do not enter sign-in codes in chat.

The Codex marketplace is `.agents/plugins/marketplace.json`; its package is `plugins/familyassetmap-codex`. Claude continues using `.claude-plugin/marketplace.json` and its own package. Do not install both packages into the same client.

For tools only, without a plugin skill, use `codex mcp add familyassetmap --url https://familyassetmap.com/mcp`, then `codex mcp login familyassetmap`. Choose one installation method to avoid duplicate connections.

Uninstall with `codex plugin remove familyassetmap@familyassetmap`. Revoke server-side access in [Connected apps](https://familyassetmap.com/connected-apps) as a separate step.

Build a submission ZIP with `python scripts/package-codex.py`. It contains only the Codex plugin, never reviewer credentials or application backend code. See [Codex review preparation](CODEX_REVIEW.md) for the remaining submission requirements.

## Cursor package

The Cursor marketplace is `.cursor-plugin/marketplace.json`, pointing to [plugins/familyassetmap-cursor](plugins/familyassetmap-cursor). It includes a Cursor manifest, logo, the family-map skill and URL-only `mcp.json` for browser OAuth.

See [Cursor submission instructions](CURSOR_REVIEW.md). This package is prepared for review, not yet approved or tested end to end in Cursor. Its inclusion does not establish availability in Grok Bot.

## Other agents and MCP clients

The backend is shared across compatible MCP clients; the Claude plugin is optional. Start with the [agent guide](https://familyassetmap.com/for-agents) or its [Markdown version](https://familyassetmap.com/for-agents.md). [llms.txt](https://familyassetmap.com/llms.txt) links to the site's agent-oriented documentation.

| Purpose | Address |
| --- | --- |
| Remote MCP endpoint (Streamable HTTP) | `https://familyassetmap.com/mcp` |
| OAuth protected-resource discovery | `https://familyassetmap.com/.well-known/oauth-protected-resource/mcp` |
| OAuth authorization-server discovery | `https://familyassetmap.com/.well-known/oauth-authorization-server` |
| Browser app / account onboarding | [familyassetmap.com](https://familyassetmap.com) |
| Revoke an existing connection | [Connected apps](https://familyassetmap.com/connected-apps) |

Configure the endpoint in your client's custom MCP settings, then follow browser-based OAuth. A bare unauthenticated request returns HTTP 401 by design. You do not need to supply a FAM API key or paste credentials into a prompt. Use `portfolio.read` for reading and approve `portfolio.write` for edits; session renewal is handled by OAuth. The client must support the server's HTTP transport and OAuth flow.

Once connected, discover the available tools and call `get_started` before working on the user's map. The workflow in [the family-map skill](plugins/familyassetmap/skills/family-map/SKILL.md) describes reads, writes, version checks, retry keys and data boundaries for agents. It does not override the user's instructions or grant permissions.

Grok marketplace submission is awaiting review. A dedicated Codex package is included in this repository. These instructions do not assert directory approval or a completed end-to-end test in every client. See [validation status](QA.md).

## Direct MCP alternative

If you only need the tools, without the plugin skill:

```sh
claude mcp add --transport http --scope user familyassetmap https://familyassetmap.com/mcp
```

Then authenticate using `/mcp`. Choose either this method or the plugin to avoid duplicate connections. This guide is for Claude Code, not the separate Claude chat/desktop connector setup.

## What it can do

- Explain the service and list your own authorized map.
- Read bounded summaries, or a requested institution's note and URL.
- Create one own Standard map, add institutions and update their details.
- Return a link to the map in the application.

It cannot connect to banks, access balances through MCP, share or delete maps, send backups, edit E2EE maps, or access maps shared by other users. Standard maps are encrypted online with a server-held key; FAM can decrypt them. Information read by Claude is sent to its AI provider. This plugin contains no API keys, local execution hooks or background jobs.

## Manage access and updates

Connections last up to seven days and can be revoked at [Connected apps](https://familyassetmap.com/connected-apps). Reconnect through `/mcp` when expired. Selecting read-only during consent prevents writes.

```sh
claude plugin marketplace update familyassetmap
claude plugin update familyassetmap@familyassetmap
```

To uninstall:

```sh
claude plugin uninstall familyassetmap@familyassetmap
claude plugin marketplace remove familyassetmap
```

Also revoke the connection in FAM to invalidate server-side access. For the direct MCP method, remove the local configuration with `claude mcp remove --scope user familyassetmap` and revoke in FAM.

## Validation and support

See [QA.md](QA.md) for validation results and the remaining real-account acceptance test. Package validation and installation do not prove that a complete Claude conversation has passed OAuth/read/write testing.

[Agent guide](https://familyassetmap.com/for-agents) · [Privacy](https://familyassetmap.com/privacy) · [Terms](https://familyassetmap.com/terms) · [Support](mailto:contact@familyassetmap.com)

Format references: [Claude plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [plugin manifest](https://code.claude.com/docs/en/plugins-reference), [MCP setup](https://code.claude.com/docs/en/mcp).
