# Family Asset Map

Use `/familyassetmap:family-map` to read or maintain your own family information map. Authenticate through `/mcp` using the Family Asset Map browser login. Never send your email code, password or passphrase in chat. Approve write access only if you want to edit the map.

The plugin provides seven remote MCP tools and one skill. It supports Standard maps, summaries, institution details and links to the app. It cannot read balances, access banks, share or delete maps, or edit E2EE maps. Standard data can be decrypted by the FAM server; data read by Claude goes to its AI provider.

Install in Claude Code with `/plugin install familyassetmap --marketplace lukeon2/familyassetmap-agents`.

Other MCP clients should start at https://familyassetmap.com/for-agents and connect to https://familyassetmap.com/mcp using browser OAuth.

Install instructions and testing status: https://github.com/lukeon2/familyassetmap-agents

Revoke access at https://familyassetmap.com/connected-apps independently of uninstalling this plugin. Connections expire after up to seven days.

[Privacy](https://familyassetmap.com/privacy) | [Terms](https://familyassetmap.com/terms) | [Support](mailto:contact@familyassetmap.com)

Package code and documentation use the MIT license. Brand names and logos identify Family Asset Map and do not imply endorsement of derivative products. The hosted service is governed by its own terms.
