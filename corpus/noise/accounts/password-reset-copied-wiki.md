---
doc_id: generated/level2-noise/accounts/password-reset-copied-wiki
title: Password Reset Process — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: accounts
version: noise-7
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/password-reset
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: copied-wiki
tags:
- level-2
- messy
- noise
- copied-wiki
- accounts
---

# Password Reset Process — Copied Wiki

## Page background

Team wiki page titled “Password Reset Process quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

## Hand edited shortcut

Below the copied text someone added a shortcut: “just use **45** for most cases.” That sentence has no citation and conflicts with some examples elsewhere on the page.

## Old checklist

- search customer record
- verify basic conditions
- use the team shortcut if queue is busy
- escalate unusual cases
- check Policy Hub if the customer challenges the answer

The checklist predates the current retrieval guidance.

## Conflicting example

Example from an old training session: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 35 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. A customer requests a reset at 3:0 PM… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Noah Williams wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Maya Chen replied with a link but did not rewrite the page.

## Search aliases

Aliases: password reset process, accounts policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. A customer requests a reset at 2:00 PM and again at 2:10 PM. The first link becomes invalid when the second request is created. However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2026-04-03. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/accounts/password-reset`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

