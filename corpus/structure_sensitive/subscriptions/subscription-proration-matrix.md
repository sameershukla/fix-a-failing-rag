---
doc_id: brightcart/v2/structured/subscriptions/subscription-proration-matrix
title: Subscription Proration Matrix
source_type: reference
source_system: engineering_docs
domain: subscriptions
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/subscriptions/subscription-proration-matrix
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: markdown-table
table_size_class: over-500-tokens
tags:
- level-2
- module-2
- structure-sensitive
- subscriptions
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Subscription Proration Matrix

## Purpose

This reference defines the current subscription proration for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

## Scope

The matrix must be read using both the row label and the column headings; a value without its heading can be misleading. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe

## Before using the matrix

Before applying a matrix row, confirm the customer state and channel because similar scenarios can map to different actions. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The

## Decision matrix

Use the complete table. The row meaning depends on the column headings and neighboring policy context. This table is intentionally longer than a 500-token fixed chunk so a naive splitter must cut through the table. A table-aware chunker should preserve the table as a semantic block or repeat the header when it must split the block.

| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| standard case | account in good standing | $25 | follow normal workflow | Support |
| low value exception | verified repeat customer | $50 | record note and continue | Support |
| regional exception | EU customer | local rule | check regional appendix | Regional Ops |
| incident workaround | incident flag active | temporary | follow incident commander guidance | Incident Mgmt |
| business account | approved business profile | $500 | use business workflow | B2B Ops |
| guest checkout | no account history | $100 | verify order ownership | Support |
| high risk signal | velocity alert present | high | pause and review | Risk |
| manual override | manager approval attached | $750 | continue with audit note | Operations |
| legacy migration | order created before migration | legacy | consult migration mapping | Engineering |
| partner channel | authorized partner order | partner terms | apply partner contract | Partner Ops |
| tax adjustment | tax-only correction | $20 | route to tax service | Finance |
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| monthly upgrade day 5 | active monthly subscriber upgrades within first week | remaining-day credit | apply unused base-plan value against higher plan immediately | Subscriptions |
| monthly upgrade day 25 | active monthly subscriber upgrades near renewal | remaining-day credit | charge prorated difference for remaining days and keep renewal date | Subscriptions |
| annual upgrade first quarter | annual subscriber upgrades during first 90 days | remaining-term credit | credit unused annual value and charge prorated upgraded annual amount | Subscriptions |
| annual upgrade final month | annual subscriber upgrades with less than 30 days remaining | remaining-term credit | apply small prorated charge and preserve original renewal date | Subscriptions |
| monthly downgrade | monthly subscriber requests lower tier before renewal | next renewal | keep current entitlements until renewal then switch plan | Subscriptions |
| trial to paid early | trial customer chooses paid plan before trial expires | trial remainder waived | start paid entitlement immediately and do not backdate charge | Subscriptions |
| trial cancellation | trial customer cancels before paid conversion | zero | end future conversion and allow trial access through stated trial end | Subscriptions |
| pause mid-cycle | eligible monthly subscriber requests pause | no cash credit | schedule pause at next renewal unless policy-specific exception exists | Subscriptions |
| resume paused plan | subscriber resumes before scheduled pause ends | remaining cycle | reactivate immediately without creating duplicate renewal date | Subscriptions |
| seat increase business | business plan adds licensed seats mid-cycle | daily seat proration | charge added seats for remaining billing days | B2B Subscriptions |
| seat decrease business | business plan removes seats mid-cycle | next invoice | retain paid seats through cycle and reduce quantity next invoice | B2B Subscriptions |
| add-on purchase | active subscriber adds premium feature | remaining-day charge | charge add-on for remaining days and align renewal | Subscriptions |
| add-on removal | subscriber removes premium feature | next renewal | retain feature until renewal and stop future add-on billing | Subscriptions |
| regional tax change | tax rate changes during paid term | future invoices only | apply new tax rate to future taxable charges, not prior settled invoices | Billing |
| coupon introduced midterm | customer finds new-customer promotion after activation | not retroactive | do not prorate promotional discount onto existing term | Subscriptions |
| service outage credit | approved outage exceeded published SLA | SLA formula | issue service credit according to SLA, separate from plan proration | Subscriptions |
| payment retry success | renewal payment succeeds after dunning retry | full renewal amount | do not prorate for retry delay when access remained active | Billing |
| payment retry suspension | access was suspended during failed renewal period | suspended days | extend entitlement by approved suspended period after payment recovery | Billing |
| currency migration | billing currency changes at customer request | next renewal | change invoice currency at renewal; do not recalculate settled term | Billing |
| monthly to annual | subscriber converts monthly plan to annual | unused monthly value | apply remaining monthly value to annual purchase at conversion | Subscriptions |
| annual to monthly | subscriber asks to switch annual plan to monthly | next annual renewal | schedule monthly plan for annual expiration; no midterm conversion | Subscriptions |
| nonprofit verification | organization becomes eligible for nonprofit rate midterm | next renewal | apply verified nonprofit price on next renewal | B2B Subscriptions |
| employee benefit plan | employee loses eligibility during active cycle | next renewal | retain current paid access through cycle then remove benefit rate | Internal Benefits |
| grandfathered plan upgrade | legacy subscriber leaves retired grandfathered tier | irreversible | warn customer that retired price cannot be restored after upgrade | Subscriptions |
| grandfathered plan renewal | legacy subscriber makes no plan change | grandfathered rate | renew at preserved legacy rate while eligibility remains | Subscriptions |
| refund after duplicate renewal | same subscription renewal captured twice | one duplicate charge | refund duplicate capture and preserve one active entitlement | Billing |
| plan migration credit | platform migration creates overlapping entitlement periods | overlap days | credit verified overlap on next invoice or original tender per migration runbook | Migration Ops |
| family member removal | family plan removes member mid-cycle | no cash credit | remove member access as scheduled but keep family price until renewal | Subscriptions |
| family member addition | family plan adds member within seat allowance | no extra charge | grant entitlement without changing billing amount | Subscriptions |
| usage tier overage | metered plan crosses included usage | usage rate | bill measured overage separately; do not alter base-plan proration | Billing |
| usage correction | metering team confirms overstated usage | verified usage delta | issue invoice credit based on corrected units | Billing |
| contracted enterprise plan | enterprise account has negotiated proration clause | contract terms | follow signed order form instead of consumer proration matrix | B2B Billing |
| annual plan downgrade | downgrade requested after day 30 | next renewal | do not issue midterm cash credit; apply lower price at renewal | Subscriptions |

## How to interpret values

Thresholds and values are typed by their column and should never be read as standalone policy statements. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds.

## Worked example

A support specialist first matches the scenario and customer condition, then reads across the same row to the required action and owner. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds.

## Exceptions

If two rows appear applicable, use the more specific row and escalate when the outcomes conflict. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

## Escalation

Cases outside the matrix go to the named operational owner rather than being forced into the nearest numeric threshold. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from

## Common mistakes

The most common mistake is retrieving only a middle table row without the header, which removes the meaning of the value column. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds.

## Source of truth

This page is the primary BrightCart source for subscription proration. Copied tables in tickets or chat exports are secondary and may be stale.
