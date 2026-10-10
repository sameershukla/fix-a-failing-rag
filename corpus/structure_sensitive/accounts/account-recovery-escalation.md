---
doc_id: brightcart/v2/structured/accounts/account-recovery-escalation
title: Account Recovery Escalation Policy
source_type: policy
source_system: policy_hub
domain: accounts
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/accounts/account-recovery-escalation
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: boundary-policy
tags:
- level-2
- module-2
- structure-sensitive
- accounts
- boundary-policy
---

# Account Recovery Escalation Policy

## Purpose

This policy resolves a narrow but high-confusion case in accounts. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy

## Scope

The policy applies only when the triggering transaction state is present and should not be generalized to unrelated cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The

## Preconditions

Agents must verify the relevant transaction, existing workflow state, and customer identity before applying the binding rule. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe

## Binding rule

When a user cannot access the registered email and fails normal identity verification, this policy applies even if a nearby article appears to offer a simpler path. support must not change the email based only on order history. This rule exists because related workflows can look similar while creating different financial or operational outcomes. Agents should verify the order state, payment state, customer identity, and any existing case before acting. Historical tickets may contain exceptions approved for one customer, and those exceptions do not establish a new general policy. The decision should be based on the current transaction state rather than on the wording of the customer request alone. Before completing the action, confirm that no duplicate workflow is already pending and that any required identifier has been recorded in the case. If a dependency is unresolved, the case remains pending rather than moving to a guessed outcome. This sequencing prevents double credits, contradictory customer messages, and irreversible actions based on incomplete context. After those checks are complete, the required final handling is: **route the case to identity operations for enhanced verification.** That final handling is part of the same rule as the opening condition; reading only one side of this section produces an incomplete and potentially wrong answer.

## Why the sequence matters

The condition and final handling belong together. Separating them can turn a conditional rule into an unconditional promise. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only

## Worked example

A representative case is checked against the trigger first, then against existing workflow state, and only then is the stated final handling performed. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and

## Exceptions

Legal holds, fraud investigations, and explicit incident commands can suspend this workflow but do not rewrite the underlying policy. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from

## Escalation

If the trigger is uncertain or records conflict, route to the domain owner instead of applying half of the rule. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy

## Common mistakes

The most common mistake is retrieving the opening condition in one chunk and the final handling in another, then answering from only one fragment. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from

## Source of truth

This policy is the current primary source for the scenario described above.
