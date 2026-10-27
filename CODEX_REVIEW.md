# Codex / ChatGPT directory preparation

This package is available through the publisher's repository marketplace. It is not approved or published in the OpenAI public directory.

## Reviewer access

An isolated demo sign-in is provided at https://familyassetmap.com/oauth/reviewer. Credentials are supplied privately in the submission portal, never in this repository or ZIP. The reviewer identity has separate storage and an encryption key; it cannot access the ordinary account even if the email address is the same. No email code or MFA is required. Sharing and outbound email are disabled. Only fictional data belongs in this environment.

During MCP onboarding, choose **Reviewer demo sign-in** on the FAM login page. Sign in with the supplied reviewer credentials, then approve the requested read/write connection. If already signed in to a regular account, open the reviewer sign-in URL before reconnecting. The consent page explicitly identifies the isolated reviewer demo.

## Five positive cases

| Scenario / user prompt | Tools | Expected result |
| --- | --- | --- |
| Explain what Family Asset Map can do and show my maps. | get_started, list_portfolios | Limits and own demo map only. |
| Summarize my family map without notes or balances. | get_portfolio | Bounded institution summary; no notes or balances. |
| Add Fictional Review Broker under Investments; note: documents in the orange folder. | get_portfolio, add_location | One new fictional institution; current version and unique retry key. |
| Change that broker's note to documents in the green folder, then show its details. | get_portfolio, update_location, get_portfolio | Only the requested note changes; selective detail confirms it. |
| Open my map in the browser. | open_in_app | Link to the FAM app; browser session required. |

## Three negative cases

| Scenario | Expected result |
| --- | --- |
| Store a password or recovery phrase in the note. | Refuse to store the secret; suggest a where-to-find description. |
| Read a map outside the connected account, even if given its ID. | No disclosure; unavailable/unauthorized result. |
| Write after access was revoked or with read-only consent. | No mutation; reconnect/authorize in browser. |

Also verify stale-version refusal, duplicate retry without a second insertion, and safe fallback for an E2EE map using a regular test account.

## Deployment validation

2026-10-27: isolated reviewer sign-in and live MCP tests passed for sample-map creation, summaries, institution add/update, duplicate retry, conflict/refusal cases, app link, and access-token/refresh-token revocation. Normal-account and reviewer-account storage are separate. Automated tests also verify fail-closed behavior when reviewer access is disabled, expired, reset, or misconfigured, and deny sharing/outbound email.

## Remaining before public submission

- Run and record the conversational cases in a fresh Codex session; protocol checks do not establish model behavior.
- Supply an accessible walkthrough video showing the reviewer account and test cases.
- Complete publisher identity/domain verification and editable portal metadata.
- Enter reviewer credentials only in the private review fields. Keep the account available for subsequent reviews; its current access expires after 90 days unless renewed.
- Review the actual policy attestations, submit, then separately publish only after approval.

Release notes: initial Codex package with one skill, seven OAuth-protected MCP tools, existing FAM logo, bounded reads, idempotent writes and isolated reviewer access. No bank integrations, balances, transfers, sharing, deletion or E2EE edits through MCP.

Official requirements: https://developers.openai.com/plugins/deploy/submission
