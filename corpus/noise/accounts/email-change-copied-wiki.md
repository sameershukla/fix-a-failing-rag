---
doc_id: generated/level2-noise/accounts/email-change-copied-wiki
title: Changing the Account Email Address — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: accounts
version: noise-7
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/email-change
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

# Changing the Account Email Address — Copied Wiki

## Page background

Team wiki page titled “Changing the Account Email Address quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

## Hand edited shortcut

Below the copied text someone added a shortcut: “just use **2** for most cases.” That sentence has no citation and conflicts with some examples elsewhere on the page.

## Old checklist

- search customer record
- verify basic conditions
- use the team shortcut if queue is busy
- escalate unusual cases
- check Policy Hub if the customer challenges the answer

The checklist predates the current retrieval guidance.

## Conflicting example

Example from an old training session: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Marcus Lee wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Dana Whitfield replied with a link but did not rewrite the page.

## Search aliases

Aliases: changing the account email address, accounts policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. The new email becomes the sign in identifier only after verification succeeds. A signed in customer enters a new email but does not complete verification. However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2026-02-14. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/accounts/email-change`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

