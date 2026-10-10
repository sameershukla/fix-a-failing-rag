---
doc_id: brightcart/v2/structured/orders/bulk-order-approval-matrix
title: Bulk Order Approval Matrix
source_type: reference
source_system: engineering_docs
domain: orders
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/orders/bulk-order-approval-matrix
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
- orders
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Bulk Order Approval Matrix

## Purpose

This reference defines the current bulk approval for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

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
| single order with 25 units | consumer account with normal history | auto approve | allow normal fulfillment and record quantity signal | Order Operations |
| single order with 50 units | consumer account with verified identity | review threshold | allow order but flag for post-order quantity monitoring | Order Operations |
| single order with 75 units | consumer account with limited history | team lead review | hold pick until order team lead confirms intended use | Order Operations |
| single order with 100 units | consumer account with normal history | manager approval | hold fulfillment until operations manager approves | Order Operations |
| single order with 150 units | approved wholesale account | auto approve within contract | route through wholesale fulfillment workflow | B2B Ops |
| single order with 300 units | approved wholesale account | contract review | verify contracted quantity and inventory reservation | B2B Ops |
| single order with 500 units | approved wholesale account | director approval | reserve inventory only after commercial director approval | B2B Ops |
| repeated 40-unit orders | same consumer account places three orders in one hour | aggregate review | combine quantities for approval decision before release | Order Operations |
| repeated guest orders | same email places multiple large guest orders | high risk | hold all related orders and verify business intent | Trust and Safety |
| new business account | business profile approved less than seven days ago | enhanced review | verify payment and company identity before bulk fulfillment | B2B Risk |
| established business account | more than twelve months successful order history | contract limit | approve quantities inside signed commercial agreement | B2B Ops |
| education institution | verified school purchasing account | purchase order limit | follow institutional purchase-order workflow | B2B Ops |
| government purchaser | verified government account | contract limit | apply public-sector contract and approval route | Public Sector Ops |
| reseller request | customer declares resale intent but lacks reseller approval | not approved | hold order and request reseller onboarding | Commercial Ops |
| reseller approved | customer has active reseller agreement | agreement limit | route through reseller pricing and fulfillment terms | Commercial Ops |
| limited edition product | bulk quantity requested for controlled release SKU | 5 units | cap quantity and reject excess regardless of account type | Merchandising |
| high-demand launch | SKU is under temporary anti-hoarding control | 2 units | enforce launch cap across linked accounts and addresses | Merchandising |
| medical essential SKU | bulk order could affect consumer availability | special review | route to supply allocation team before confirmation | Supply Chain |
| warehouse low stock | requested quantity exceeds 20 percent of available stock | inventory review | hold confirmation until inventory planning approves allocation | Supply Chain |
| split warehouse order | quantity must ship from three or more facilities | logistics review | confirm split-shipment cost and service impact | Fulfillment |
| international bulk order | destination is outside domestic commercial region | trade review | verify export restrictions and landed-cost terms | International Ops |
| hazmat bulk order | order contains regulated hazardous material | special handling | route to regulated-shipping approval workflow | Special Handling |
| gift card bulk purchase | order includes more than 100 digital gift cards | risk review | hold issuance until gift-card risk approves funding source | Gift Card Risk |
| employee bulk purchase | employee discount applied to unusually high quantity | 10 units | cap employee discount and route excess to normal pricing | Internal Commerce |
| promotion bulk use | large order uses consumer promotion code | promotion cap | apply campaign quantity cap and remove excess discount | Commerce Ops |
| manual price override | agent changed unit price on bulk order | manager review | hold order until override and margin are approved | Commercial Ops |
| preorder bulk request | quantity exceeds preorder allocation for account class | allocation cap | reduce to allowed quantity or request merchandising exception | Merchandising |
| backorder bulk request | inventory is not currently available | allocation review | do not promise ship date until supply plan is confirmed | Supply Chain |
| subscription replenishment | business replenishment schedule creates large recurring order | contract schedule | approve according to recurring contract quantity | B2B Ops |
| fraud signal on bulk order | device or payment has active risk alert | high risk | pause fulfillment and route to fraud review regardless of quantity | Trust and Safety |
| chargeback history | account has recent confirmed payment disputes | enhanced review | require payment-risk approval before reserving inventory | Payments Risk |
| manual exception | commercial manager grants one-time quantity exception | documented exception | release only approved quantity and store exception identifier | Commercial Ops |
| single order with 220 units | customer is not on approved wholesale list | manager approval | hold fulfillment until commercial manager approves | Order Operations |

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

This page is the primary BrightCart source for bulk approval. Copied tables in tickets or chat exports are secondary and may be stale.
