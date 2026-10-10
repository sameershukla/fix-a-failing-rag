---
doc_id: generated/level2-noise/gift-cards/gift-card-redemption-support-case
title: Redeeming Gift Cards — Support Case
source_type: support_case
source_system: crm_support
domain: gift-cards
version: noise-2
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-redemption
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

# Redeeming Gift Cards — Support Case

## Case summary

Case **CS-586033** concerns redeeming gift cards. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about redeeming gift cards and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 2 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/gift-cards/gift-card-redemption` and recorded: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Fulfillment. The operational window was **3 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Redeeming Gift Cards, gift-cards, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-04-03. Case owner Ifeoma Okafor. Queue Fulfillment. Canonical reference `brightcart/v1/gift-cards/gift-card-redemption`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

