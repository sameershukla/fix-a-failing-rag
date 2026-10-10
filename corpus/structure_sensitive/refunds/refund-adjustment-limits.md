---
doc_id: brightcart/v2/structured/refunds/refund-adjustment-limits
title: Refund Adjustment Limits Matrix
source_type: reference
source_system: engineering_docs
domain: refunds
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/refunds/refund-adjustment-limits
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
- refunds
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Refund Adjustment Limits Matrix

## Purpose

This reference defines the current refund adjustment for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

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
| duplicate shipment billed twice | customer has two captured charges tied to one fulfillment | up to $300 | refund the duplicate charge after payment ledger verification and record duplicate-charge reason | Payments Support |
| partial delivery confirmed | carrier scan shows one line item missing from a multi-item order | item value only | refund only the missing item and preserve tax allocation from original order | Support Tier 2 |
| price adjustment request | same SKU dropped in price within seven calendar days of delivery | up to $100 | issue price difference as refund to original payment method | Support |
| damaged accessory | primary product works but included accessory arrived unusable | up to $75 | refund accessory value or ship replacement according to customer choice | Support |
| late delivery courtesy | shipment arrived more than three business days after promised date | up to $40 | issue courtesy adjustment but do not mark order as product refund | Support |
| tax calculation correction | tax engine confirms overcollection on completed order | tax amount only | refund verified tax difference and attach tax engine case identifier | Finance Ops |
| shipping fee correction | customer paid expedited fee but carrier service was downgraded before dispatch | shipping fee only | refund expedited fee after fulfillment downgrade is confirmed | Fulfillment Support |
| coupon did not apply | eligible promotion failed because checkout service rejected valid code | up to $50 | refund promotional difference and record campaign identifier | Commerce Support |
| subscription overlap | customer was charged both monthly and annual plans during migration | one overlapping charge | refund lower-value duplicate subscription charge after entitlement check | Subscriptions |
| gift card plus card split | refund spans gift card and card tender on same order | original tender proportions | return each portion to its original tender and never move gift-card value to cash | Payments Support |
| marketplace seller concession | seller authorized a customer concession in case notes | up to $150 | apply seller-funded adjustment and debit seller settlement balance | Marketplace Ops |
| warehouse cancellation miss | customer cancellation was approved before pick but fulfillment still shipped | item value plus standard shipping | refund item and standard shipping after return scan or carrier intercept | Order Operations |
| lost parcel confirmed | carrier investigation closed as lost and no replacement was sent | order value up to $500 | issue refund after carrier loss case closes and store investigation number | Logistics Support |
| replacement also failed | replacement item arrived damaged after original damage claim | up to $600 | refund replacement order and close both linked cases together | Support Tier 2 |
| manufacturer rebate mismatch | checkout promised manufacturer rebate that was not transmitted | rebate amount only | issue temporary adjustment and open reimbursement claim with vendor finance | Vendor Operations |
| business contract service credit | B2B account has signed service-credit schedule | contract limit | apply contract-defined credit and attach account contract reference | B2B Ops |
| international duty correction | broker confirms BrightCart collected duty twice | verified duplicate duty | refund duplicate duty only after customs receipt is attached | International Ops |
| fraud false positive recovery | risk team cleared order after payment had been reversed | original captured amount | reissue refund or recapture only under risk-team written direction | Risk Operations |
| manual invoice correction | enterprise invoice contains quantity error approved by account manager | up to $1,000 | create credit memo rather than consumer refund and link invoice revision | B2B Finance |
| warranty goodwill | product is outside standard return window but warranty team approved goodwill | up to $200 | issue goodwill adjustment with warranty approval reference | Warranty Support |
| service outage compensation | checkout outage caused repeated failed charges but one later settled | up to $50 | refund approved inconvenience credit after duplicate-charge review | Incident Support |
| currency conversion complaint | customer questions issuer conversion rate but BrightCart amount is correct | zero | do not refund exchange-rate difference; explain issuer conversion ownership | Payments Support |
| cash-equivalent restriction | refund request concerns prepaid cash-equivalent product | not eligible | do not issue manual cash refund and route to specialized policy review | Risk |
| chargeback already open | issuer dispute exists for same transaction | zero manual refund | pause refund until chargeback state is resolved to avoid double credit | Chargeback Ops |
| legal settlement adjustment | legal team provides signed settlement instruction | specified settlement amount | issue only amount named by legal and attach approval document | Legal Operations |
| VIP service recovery | executive support approved recovery for verified service failure | up to $500 | issue adjustment with executive-support reason code and audit note | Executive Support |
| employee purchase correction | employee discount was omitted on eligible internal purchase | discount difference | refund verified discount difference after HR eligibility check | Internal Commerce |
| education discount mismatch | student verification succeeded before purchase but discount failed | up to $80 | refund discount difference and record verification transaction | Commerce Support |
| preorder price guarantee | preorder shipped after official price decreased | price difference | refund difference automatically after shipment settlement | Order Operations |
| inventory substitution | customer accepted lower-priced substitute after original became unavailable | price difference | refund difference between original and substitute SKU | Fulfillment Support |
| multi-currency marketplace payout | seller-funded refund is denominated in settlement currency | settlement equivalent | calculate seller debit using settlement ledger rate and preserve customer tender currency | Marketplace Finance |
| manual manager concession | support manager approved exception outside normal policy | up to $750 | issue adjustment only with manager identifier and written justification | Support Management |
| manual refund after a carrier loss | verified customer with one prior concession | $250 | issue refund without finance approval; log reason code R17 | Support Tier 2 |

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

This page is the primary BrightCart source for refund adjustment. Copied tables in tickets or chat exports are secondary and may be stale.
