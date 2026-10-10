---
doc_id: generated/level2-noise/gift-cards/gift-card-purchase-support-case
title: Gift Card Purchase Rules — Support Case
source_type: support_case
source_system: crm_support
domain: gift-cards
version: noise-2
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-purchase
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
- gift-cards
---

# Gift Card Purchase Rules — Support Case

## Case summary

Case **CS-832114** concerns gift card purchase rules. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about gift card purchase rules and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This policy covers digital BrightCart gift card purchases. Gift cards are delivered by email and can be used for eligible BrightCart purchases. A single BrightCart gift card can be purchased in an amount from $9 through $1000. Digital delivery usually occurs within 30 minutes after payment approval. Gift cards cannot be purchased using another gift card. The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/gift-cards/gift-card-purchase` and recorded: This policy covers digital BrightCart gift card purchases. Gift cards are delivered by email and can be used for eligible BrightCart purchases. A single BrightCart gift card can be purchased in an amount from $10 through $500. Digital delivery usually occurs within 15 minutes after payment approval. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Payments Ops. The operational window was **30 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Gift Card Purchase Rules, gift-cards, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-05-29. Case owner Priya Nair. Queue Payments Ops. Canonical reference `brightcart/v1/gift-cards/gift-card-purchase`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

