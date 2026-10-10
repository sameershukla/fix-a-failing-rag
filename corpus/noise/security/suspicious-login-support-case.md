---
doc_id: generated/level2-noise/security/suspicious-login-support-case
title: Suspicious Login Response — Support Case
source_type: support_case
source_system: crm_support
domain: security
version: noise-2
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/security/suspicious-login
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
- security
---

# Suspicious Login Response — Support Case

## Case summary

Case **CS-215892** concerns suspicious login response. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about suspicious login response and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly. For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/security/suspicious-login` and recorded: This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly. For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified channel. That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Trust and Safety. The operational window was **15 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Suspicious Login Response, security, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-02-14. Case owner Tomas Novak. Queue Trust and Safety. Canonical reference `brightcart/v1/security/suspicious-login`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

