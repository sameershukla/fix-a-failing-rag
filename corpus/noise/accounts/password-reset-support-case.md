---
doc_id: generated/level2-noise/accounts/password-reset-support-case
title: Password Reset Process — Support Case
source_type: support_case
source_system: crm_support
domain: accounts
version: noise-2
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/password-reset
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
- accounts
---

# Password Reset Process — Support Case

## Case summary

Case **CS-241352** concerns password reset process. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about password reset process and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 35 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. A customer requests a reset at 3:0 PM… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/accounts/password-reset` and recorded: This runbook explains the self service password reset flow and how support should handle expired or already used links. A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Privacy Office. The operational window was **14 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Password Reset Process, accounts, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-02-14. Case owner Maya Chen. Queue Privacy Office. Canonical reference `brightcart/v1/accounts/password-reset`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

