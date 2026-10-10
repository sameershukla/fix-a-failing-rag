---
doc_id: generated/level2-noise/returns/return-window-support-case
title: Standard Return Window — Support Case
source_type: support_case
source_system: crm_support
domain: returns
version: noise-2
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-window
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: support-case
tags:
- level-2
- messy
- noise
- support-case
- returns
---

# Standard Return Window — Support Case

## Case summary

Case **CS-460758** concerns standard return window. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about standard return window and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules. The standard return window is 35 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 35. Shipping time back to the warehouse… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/returns/return-window` and recorded: This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules. The standard return window is 30 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 30. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Privacy Office. The operational window was **5 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Standard Return Window, returns, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2025-11-18. Case owner Mei Wong. Queue Privacy Office. Canonical reference `brightcart/v1/returns/return-window`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

