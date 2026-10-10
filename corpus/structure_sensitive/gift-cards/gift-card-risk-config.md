---
doc_id: brightcart/v2/structured/gift-cards/gift-card-risk-config
title: Gift Card Risk Configuration
source_type: runbook
source_system: engineering_docs
domain: gift-cards
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/gift-cards/gift-card-risk-config
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: fenced-code
tags:
- level-2
- module-2
- structure-sensitive
- gift-cards
- fenced-code
---

# Gift Card Risk Configuration

## Purpose

This runbook documents the current gift card risk configuration used in production. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds.

## Scope

Only the production hierarchy below is authoritative; snippets copied into tickets may omit parent keys and change the meaning of a value. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe

## Reading nested settings

Read the full key path from the root through the child object before interpreting a numeric value or action. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior

## Production configuration

The fenced block below is a single production configuration artifact. Parent keys provide the meaning of leaf values, so do not detach the bottom lines from their hierarchy.

```yaml
risk:
  environment: production
  owner: gift-cards-platform
  gift_card:
    audit_enabled: true
    documentation_required: true
    inherited_defaults:
      enabled: true
      region: GLOBAL
      source: policy_hub
      note_01: "operational placeholder 1; not the production decision"
      note_02: "operational placeholder 2; not the production decision"
      note_03: "operational placeholder 3; not the production decision"
      note_04: "operational placeholder 4; not the production decision"
      note_05: "operational placeholder 5; not the production decision"
      note_06: "operational placeholder 6; not the production decision"
      note_07: "operational placeholder 7; not the production decision"
      note_08: "operational placeholder 8; not the production decision"
      note_09: "operational placeholder 9; not the production decision"
      note_10: "operational placeholder 10; not the production decision"
      note_11: "operational placeholder 11; not the production decision"
      note_12: "operational placeholder 12; not the production decision"
      note_13: "operational placeholder 13; not the production decision"
      note_14: "operational placeholder 14; not the production decision"
      note_15: "operational placeholder 15; not the production decision"
    reload:
      single_load_usd: 500
      daily_load_usd: 1000
      over_limit: REJECT
      audit_log: required
      fail_closed: true
```

## Deployment behavior

Changes are validated in staging and promoted as one configuration unit so dependent values remain consistent. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

## Validation

The deployment pipeline rejects malformed YAML and checks required production keys before rollout. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When a case falls

## Failure behavior

When a required setting is missing, the service fails closed or routes to manual handling rather than guessing a default. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy

## Rollback

Rollback restores the complete prior configuration object; individual leaf values are not rolled back independently. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When a

## Common mistakes

A common retrieval error is returning only the leaf lines and losing the parent path that says which workflow the values belong to. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only

## Source of truth

This runbook and its fenced configuration are the primary source for gift card risk.
