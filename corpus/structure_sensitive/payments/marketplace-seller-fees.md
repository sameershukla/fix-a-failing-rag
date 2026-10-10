---
doc_id: brightcart/v2/structured/payments/marketplace-seller-fees
title: Marketplace Seller Fee Matrix
source_type: reference
source_system: engineering_docs
domain: payments
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/payments/marketplace-seller-fees
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
- payments
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Marketplace Seller Fee Matrix

## Purpose

This reference defines the current seller fee for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

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
| apparel marketplace sale | seller is on standard tier | 15% | deduct category commission from seller payout | Marketplace Finance |
| books marketplace sale | seller is on standard tier | 8% | deduct category commission from seller payout | Marketplace Finance |
| home goods marketplace sale | seller is on standard tier | 13% | deduct category commission from seller payout | Marketplace Finance |
| beauty marketplace sale | seller is on standard tier | 14% | deduct category commission from seller payout | Marketplace Finance |
| grocery marketplace sale | seller is on standard tier | 7% | deduct category commission from seller payout | Marketplace Finance |
| pet supplies marketplace sale | seller is on standard tier | 11% | deduct category commission from seller payout | Marketplace Finance |
| sports marketplace sale | seller is on standard tier | 12% | deduct category commission from seller payout | Marketplace Finance |
| jewelry marketplace sale | seller is on standard tier | 18% | deduct category commission from seller payout | Marketplace Finance |
| furniture marketplace sale | seller is on standard tier | 10% | deduct category commission from seller payout | Marketplace Finance |
| toys marketplace sale | seller is on standard tier | 12% | deduct category commission from seller payout | Marketplace Finance |
| premium seller apparel | seller has premium growth tier | 12% | deduct reduced premium-tier commission from payout | Marketplace Finance |
| premium seller home goods | seller has premium growth tier | 10% | deduct reduced premium-tier commission from payout | Marketplace Finance |
| enterprise seller electronics | seller has negotiated enterprise contract | contract rate | apply seller-specific rate from signed fee schedule | Marketplace Finance |
| cross-border sale | seller is domestic and buyer is international | 2% cross-border fee | deduct cross-border fee in addition to category commission | Marketplace Finance |
| currency conversion | seller payout currency differs from transaction settlement currency | 1% conversion fee | deduct conversion fee using settlement ledger rate | Marketplace Finance |
| expedited payout | eligible seller requests same-day payout | 1.5% payout fee | deduct expedited payout fee before transfer | Marketplace Finance |
| standard payout | seller uses normal weekly settlement | no payout fee | transfer net balance on standard settlement schedule | Marketplace Finance |
| refund before payout | customer refund posts before seller settlement closes | reverse commission | remove sale and commission from pending payout | Marketplace Finance |
| refund after payout | customer refund posts after seller already received settlement | seller debit | debit future seller balance according to refund allocation | Marketplace Finance |
| seller-funded coupon | seller created promotion and funds discount | discount plus commission basis | calculate commission on post-discount merchandise amount | Marketplace Finance |
| platform-funded coupon | BrightCart funds customer promotion | normal commission basis | calculate seller commission on seller-receivable merchandise amount | Marketplace Finance |
| shipping label purchase | seller buys BrightCart carrier label | carrier cost | deduct label charge separately from marketplace commission | Marketplace Finance |
| storage fee | seller inventory remains in fulfillment center beyond free window | $0.75 per cubic foot weekly | deduct storage fee from next settlement | Marketplace Finance |
| long-term storage | inventory remains beyond 180 days | $2.50 per cubic foot monthly | deduct long-term storage surcharge | Marketplace Finance |
| return processing | customer return uses marketplace fulfillment service | $4 per unit | deduct return-processing fee when return is received | Marketplace Finance |
| disposal request | seller asks BrightCart to dispose of unsellable inventory | $1.25 per unit | deduct disposal fee after warehouse completion | Marketplace Finance |
| removal order | seller requests inventory shipped back | $3.50 per unit | deduct removal fee and outbound shipping | Marketplace Finance |
| chargeback administration | buyer dispute requires marketplace evidence package | $15 per case | deduct administration fee unless dispute is won under protection policy | Marketplace Finance |
| advertising spend | seller uses sponsored marketplace placement | actual campaign spend | deduct advertising charges from settlement balance | Marketplace Finance |
| subscription fee | seller is enrolled in professional marketplace plan | $39 monthly | deduct monthly subscription fee independent of sales commission | Marketplace Finance |
| inactive seller fee | seller account has no sales for twelve months | zero | do not assess inactivity fee under current policy | Marketplace Finance |
| manual fee correction | finance approves correction to wrongly assessed marketplace fee | approved delta | credit seller balance and attach finance case reference | Marketplace Finance |
| electronics marketplace sale | seller is on standard tier | 12% | deduct commission from seller payout | Marketplace Finance |

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

This page is the primary BrightCart source for seller fee. Copied tables in tickets or chat exports are secondary and may be stale.
