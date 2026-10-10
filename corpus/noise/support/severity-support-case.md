---
doc_id: generated/level2-noise/support/severity-support-case
title: Incident Severity Levels — Support Case
source_type: support_case
source_system: crm_support
domain: support
version: noise-2
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/severity
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
- support
---

# Incident Severity Levels — Support Case

## Case summary

Case **CS-506262** concerns incident severity levels. The customer outcome is real, but it reflects one account, one date, and one set of exceptions. This record is searchable because support uses previous cases to diagnose similar tickets.

## Customer wording

Customer said: “I was told something different about incident severity levels and I need to know what happens now.” The agent copied several policy phrases into the ticket, which makes this case look authoritative in keyword and vector search.

## What the agent initially believed

The first agent note says: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 3 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 4… The note was entered before the agent checked the current source of truth.

## Policy check

After escalation, the agent referenced `brightcart/v1/support/severity` and recorded: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects… That is the general rule used to resolve the case.

## Customer specific exception

This customer received a one time exception approved by Payments Ops. The operational window was **21 days** rather than the normal flow because another open case and a manual review blocked automation.

## Outcome

The case was closed after the exception. The resolution text intentionally includes both the normal rule and the customer-specific exception, so copying only one paragraph can produce the wrong answer for a general question.

## Internal note

**Do not quote this line as policy:** supervisor authorized a special handling path for this account. Similar looking customers are not automatically eligible for the same treatment.

## Related terms

Common search terms recorded by support: Incident Severity Levels, support, delayed, failed, exception, manual review, customer promise, escalation, and status. These terms overlap heavily with the canonical article.

## Training caution

Case records answer “what happened to this customer,” not “what is BrightCart policy.” Retrieval should prefer primary authority for general questions and use cases only when the question is case-specific.

## Closure metadata

Closed 2026-02-14. Case owner Tomas Novak. Queue Payments Ops. Canonical reference `brightcart/v1/support/severity`. The ticket remains `active` in CRM even after closure because historical cases are searchable.

