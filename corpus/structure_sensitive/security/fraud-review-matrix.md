---
doc_id: brightcart/v2/structured/security/fraud-review-matrix
title: Fraud Escalation Matrix
source_type: reference
source_system: engineering_docs
domain: security
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/security/fraud-review-matrix
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
- security
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Fraud Escalation Matrix

## Purpose

This reference defines the current fraud escalation for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

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
| new device high value order | account older than 90 days but first purchase from new device | medium risk | require step-up verification before fulfillment | Trust and Safety |
| new account low value order | account created today and order below $50 | low risk | allow payment but monitor velocity signals | Fraud Platform |
| multiple cards one device | five cards attempted from same device within ten minutes | high risk | pause checkout and open velocity review | Trust and Safety |
| multiple accounts one card | same card used across four newly created accounts | high risk | block additional authorizations pending review | Fraud Platform |
| billing shipping mismatch | high-value order has unrelated billing and shipping names | medium risk | request ownership verification before release | Trust and Safety |
| known good repeat buyer | verified customer has long successful purchase history | low risk | allow normal workflow unless new critical signal appears | Fraud Platform |
| chargeback history | account has two confirmed fraud chargebacks in six months | high risk | route new money movement to manual review | Trust and Safety |
| gift card velocity | customer buys more than ten gift cards in one hour | high risk | pause gift-card issuance and review funding source | Gift Card Risk |
| gift card redemption burst | new account redeems several unrelated gift cards rapidly | high risk | freeze redemption balance and investigate source | Gift Card Risk |
| password reset then payout | account resets password and requests payout within fifteen minutes | high risk | hold payout and require identity verification | Account Security |
| email change then refund | account changes email before high-value refund request | high risk | hold refund and verify prior account owner | Account Security |
| impossible travel login | successful logins occur from distant countries within one hour | high risk | revoke sessions and require MFA reauthentication | Account Security |
| proxy network checkout | checkout originates from anonymizing network with clean account history | medium risk | apply enhanced verification without automatic block | Trust and Safety |
| reshipper address | shipping address matches known freight-forwarding service | medium risk | review product category and payment history | Trust and Safety |
| digital goods immediate use | new account buys digital value and redeems immediately | high risk | delay fulfillment until payment risk clears | Digital Risk |
| business account large order | verified business account exceeds consumer order threshold | medium risk | use B2B risk workflow rather than consumer auto-block | B2B Risk |
| employee purchase | verified employee uses internal purchase program | low risk | apply employee controls and standard payment checks | Internal Risk |
| refund to alternate tender | agent attempts refund to payment method not used on order | critical risk | block action and require finance-security review | Payments Security |
| manual credit request | support agent requests account credit above normal concession limit | high risk | require manager and finance approval before posting | Trust and Safety |
| coupon abuse cluster | many accounts reuse promotion with shared device fingerprint | medium risk | suppress promotion and queue abuse investigation | Promotion Risk |
| bot checkout pattern | high request rate with repeated cart signatures | high risk | throttle session and require bot challenge | Fraud Platform |
| card testing pattern | many low-value declines followed by small approval | critical risk | block payment attempts and notify payments fraud team | Payments Security |
| high return rate | customer return rate exceeds category threshold without fraud signals | medium risk | route future returns to policy review, not payment block | Returns Risk |
| friendly fraud indicator | customer repeatedly disputes delivered orders after confirmed receipt | high risk | require manual review for future concessions | Chargeback Risk |
| trusted device mismatch | trusted account suddenly changes device, phone, and shipping address | high risk | require step-up identity verification | Account Security |
| country restriction | payment originates from prohibited jurisdiction | critical risk | block transaction and route to compliance review | Compliance |
| sanctions name match | customer name produces unresolved sanctions screening match | critical risk | freeze transaction pending compliance disposition | Compliance |
| refund after chargeback loss | merchant already lost issuer dispute for same transaction | critical risk | block additional refund to prevent double credit | Chargeback Ops |
| high-value preorder | new customer places preorder above $2,000 | medium risk | verify funding and identity before inventory reservation | Trust and Safety |
| merchant portal takeover signal | seller login shows credential stuffing indicators | high risk | suspend payout changes and force credential reset | Marketplace Security |
| payout bank change | seller changes bank account shortly before scheduled payout | high risk | hold payout until bank-change verification completes | Marketplace Security |
| manual risk override | reviewer overrides automated block with documented evidence | reviewer decision | allow transaction and record immutable override reason | Trust and Safety |
| refund request from newly created account | refund exceeds 500 dollars and device is new | high risk | pause money movement and route to fraud review | Trust and Safety |

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

This page is the primary BrightCart source for fraud escalation. Copied tables in tickets or chat exports are secondary and may be stale.
