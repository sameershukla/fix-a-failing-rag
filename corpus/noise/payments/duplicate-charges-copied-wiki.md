---
doc_id: generated/level2-noise/payments/duplicate-charges-copied-wiki
title: Duplicate Charge Investigation — Copied Wiki
source_type: wiki_copy
source_system: team_wiki
domain: payments
version: noise-7
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/duplicate-charges
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
- payments
---

# Duplicate Charge Investigation — Copied Wiki

## Page background

Team wiki page titled “Duplicate Charge Investigation quick notes.” It was copied from several sources over time. Ownership is unclear and the page has no formal approval workflow.

## Copied policy text

This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment. The paragraph was copied from an older or current Policy Hub page, but the copy does not record which version.

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

Example from an old training session: This article explains how to tell the difference between a duplicate authorization display and two settled charges. It prevents unnecessary refunds when only one real payment exists. Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a… No date was attached to the example, so readers cannot tell whether it describes a retired rule or a special case.

## Pinned comment

Elena Ruiz wrote: “I think Policy Hub changed this recently; can someone clean up the wiki?” Noah Williams replied with a link but did not rewrite the page.

## Search aliases

Aliases: duplicate charge investigation, payments policy, customer issue, exception, timing, limit, eligibility, status. The alias list makes this low quality wiki page rank well for many queries.

## What is probably current

The latest copied fragment says: Before refunding a reported duplicate charge, verify whether both entries are captured transactions. A pending authorization next to one settled charge is usually not a duplicate payment. If two captured charges exist for the same order and amount, payments should void or refund the extra capture. A bank app shows one $75 pending amount and one $75 posted amount for the same order. However, because the page is manually maintained, “latest” here means latest edit, not necessarily latest approved policy.

## Cleanup request

Cleanup task opened 2026-08-22. Status still open. Until cleanup is complete, the wiki page should be treated as secondary context and not as the primary source of truth.

## Source of truth

For a general customer answer, prefer `brightcart/v1/payments/duplicate-charges`. Use this page only to understand team vocabulary and historical confusion. `status: active` reflects page availability, not authority.

