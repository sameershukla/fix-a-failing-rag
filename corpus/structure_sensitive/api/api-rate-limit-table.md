---
doc_id: brightcart/v2/structured/api/api-rate-limit-table
title: Public API Rate Limit Matrix
source_type: reference
source_system: engineering_docs
domain: api
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/api/api-rate-limit-table
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
- api
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Public API Rate Limit Matrix

## Purpose

This reference defines the current API rate limit for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds.

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
| GET /v1/orders | standard merchant production key | 300 requests per minute | return 429 after limit and include Retry-After | API Platform |
| GET /v1/orders/{id} | standard merchant production key | 600 requests per minute | return 429 after limit and include Retry-After | API Platform |
| POST /v1/orders | standard merchant production key | 120 requests per minute | throttle excess requests and preserve idempotency handling | API Platform |
| PATCH /v1/orders/{id} | standard merchant production key | 90 requests per minute | return 429 when bucket is exhausted | API Platform |
| POST /v1/order-cancellations | standard merchant production key | 60 requests per minute | throttle and require retry with backoff | API Platform |
| GET /v1/refunds | standard merchant production key | 240 requests per minute | return 429 after sustained excess traffic | API Platform |
| GET /v1/refunds/{id} | standard merchant production key | 480 requests per minute | return 429 and include reset metadata | API Platform |
| POST /v1/payments | standard merchant production key | 100 requests per minute | throttle above bucket and preserve idempotent replay | Payments API |
| POST /v1/payment-methods | standard merchant production key | 80 requests per minute | return 429 and require exponential backoff | Payments API |
| GET /v1/payment-methods | standard merchant production key | 300 requests per minute | throttle above read limit | Payments API |
| POST /v1/customers | standard merchant production key | 120 requests per minute | return 429 on excess writes | Customer API |
| GET /v1/customers | standard merchant production key | 300 requests per minute | throttle list calls above limit | Customer API |
| GET /v1/customers/{id} | standard merchant production key | 600 requests per minute | return 429 after per-key bucket is exhausted | Customer API |
| PATCH /v1/customers/{id} | standard merchant production key | 120 requests per minute | throttle writes and include Retry-After | Customer API |
| POST /v1/webhooks | standard merchant production key | 60 requests per minute | return 429 and do not create duplicate subscription | API Platform |
| GET /v1/webhooks | standard merchant production key | 240 requests per minute | throttle list operations above limit | API Platform |
| DELETE /v1/webhooks/{id} | standard merchant production key | 60 requests per minute | return 429 on excess delete requests | API Platform |
| POST /v1/files | standard merchant production key | 30 requests per minute | throttle uploads and return retry guidance | File Platform |
| GET /v1/files/{id} | standard merchant production key | 300 requests per minute | return 429 after read bucket is exhausted | File Platform |
| POST /v1/search | standard merchant production key | 180 requests per minute | throttle expensive search calls above quota | Search Platform |
| GET /v1/products | standard merchant production key | 600 requests per minute | throttle catalog reads above burst allowance | Catalog API |
| GET /v1/products/{id} | standard merchant production key | 900 requests per minute | return 429 after burst and sustained limits are exceeded | Catalog API |
| POST /v1/products | approved marketplace seller key | 60 requests per minute | throttle writes and validate seller scope | Catalog API |
| PATCH /v1/products/{id} | approved marketplace seller key | 90 requests per minute | return 429 on excess updates | Catalog API |
| GET /v1/inventory | standard merchant production key | 300 requests per minute | throttle inventory reads above quota | Inventory API |
| POST /v1/inventory/adjustments | warehouse service production key | 240 requests per minute | throttle adjustments and require idempotency key | Inventory API |
| GET /v1/shipments | standard merchant production key | 300 requests per minute | return 429 after limit | Shipping API |
| POST /v1/shipments | standard merchant production key | 120 requests per minute | throttle shipment creation and preserve request id | Shipping API |
| POST /v1/labels | warehouse service production key | 180 requests per minute | return 429 and retry after carrier backpressure clears | Shipping API |
| GET /v1/analytics/reports | analytics production key | 30 requests per minute | throttle report generation to protect warehouse capacity | Analytics API |
| POST /v1/analytics/exports | analytics production key | 10 requests per minute | return 429 and queue retry after export capacity frees | Analytics API |
| POST /v1/admin/credits | privileged internal service key | 20 requests per minute | throttle and require privileged scope on every request | Admin API |
| POST /v1/refunds | standard merchant production key | 60 requests per minute | return 429 after limit and include Retry-After | API Platform |

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

This page is the primary BrightCart source for API rate limit. Copied tables in tickets or chat exports are secondary and may be stale.
