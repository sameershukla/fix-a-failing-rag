---
doc_id: generated/level2-noise/refunds/refund-policy-support-case
title: Standard Refund Policy — Support Case
source_type: support_case
source_system: crm_support
domain: refunds
version: noise-2
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-policy
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
- refunds
---

# Standard Refund Policy — Support Case

## Case summary

Case **CS-861148** concerns standard refund policy. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about standard refund policy and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/refunds/refund-policy` and recorded: This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception. Once BrightCart approves a refund, the refund is sent back to the original payment method. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Subscription Ops. The operational window was **90 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Standard Refund Policy, refunds, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-04-03. Case owner Dana Whitfield. Queue Subscription Ops. Canonical reference `brightcart/v1/refunds/refund-policy`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

