---
doc_id: brightcart/secondary/2026/security/mfa-release_note
title: 'Working Note: Multi Factor Authentication'
source_type: release_note
source_system: github_docs
domain: security
version: working
effective_date: '2026-09-15'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/security/mfa
company: BrightCart
audience:
- support
- operations
- engineering
tags:
- level-2
- secondary
- distractor
- semantic-overlap
- security
- release_note
---

# Working Note: Multi Factor Authentication

## Context

This is an active team working note about multi factor authentication. It is useful for understanding support symptoms and operational history, but it is not the Policy Hub source of truth.

## What prompted this note

Several cases used language associated with multi factor authentication. Agents reported that search results were inconsistent because an older wiki page, ticket comments, and the active policy all used nearly the same terminology.

## Customer wording seen in tickets

Customers described the issue without using internal policy names. Common phrases included "this is taking longer than I was told," "why did the system reject this," and "another agent gave me a different rule." These phrases overlap with many BrightCart policies.

## What support tried

Support checked the order or account state, searched for multi factor authentication, and compared the first few results. Some agents stopped at the first plausible snippet instead of checking the source system and status metadata.

## Conflicting wording copied into a case

A case comment contained the following non-authoritative wording:

> Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. Recovery codes are generated when authenticator based MFA is enabled and should be stored by the user in a safe place.

The wording came from a secondary note and should not be treated as the current rule.

## Related decision details

The current policy has conditions involving the request state, timing, eligibility, or workflow. A support case may mention some of the same decision points without carrying the complete authoritative rule.

- A verification challenge is required on new or high risk sign ins when MFA is active.
- Recovery codes are single use.
- Changing MFA settings requires a recently verified session.

## Search terms

Useful search terms include multi factor authentication, security, customer policy, eligibility, timing, limit, status, exception, support workflow, and escalation. These broad terms intentionally make this note competitive in semantic and keyword retrieval.

## Operational impact

When the wrong source is used, customers can receive an incorrect deadline, threshold, eligibility decision, or next step. The error can look like a model problem even when the root cause is retrieval.

## Hand-off note

If a case depends on the exact current value or rule, open the canonical Policy Hub document `brightcart/v1/security/mfa` rather than relying on this working note.

## Why this page is not authoritative

This page is maintained by a delivery team and can contain paraphrases, copied ticket text, and historical observations. Its `authority` field is `secondary` even though the page itself is active.

## Follow-up

If a customer loses all second factor methods, use the account recovery process. Do not disable MFA solely based on information available to an unverified chat user. The team also tracks whether stale search results continue to appear above the current policy after index updates.

## Ownership

The security operations group owns this note. Policy changes are owned in Policy Hub. Questions about conflicting search results should be sent to the RAG platform team with the query, retrieved chunk IDs, and ranking scores.
