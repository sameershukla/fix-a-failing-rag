---
doc_id: brightcart/v2/structured/privacy/privacy-retention-table
title: Privacy Data Retention Matrix
source_type: reference
source_system: engineering_docs
domain: privacy
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/privacy/privacy-retention-table
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
- privacy
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Privacy Data Retention Matrix

## Purpose

This reference defines the current retention period for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

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
| customer profile core | account remains active | life of account | retain core profile while account is active and deletion is not requested | Privacy Operations |
| deleted account profile | account deletion completed and no legal hold exists | 30 days | purge residual profile data after deletion propagation window | Privacy Operations |
| payment authorization logs | transaction settled and dispute window remains open | 7 years | retain regulated financial record then delete according to schedule | Finance Compliance |
| fraud investigation case | case is closed without active legal hold | 5 years | retain investigation evidence for fraud-defense period | Trust and Safety |
| security authentication logs | standard production authentication events | 13 months | delete or aggregate logs after security retention period | Security |
| MFA enrollment record | account remains active | life of account | retain enrollment state until factor is removed or account deleted | Security |
| password reset event | reset completed successfully | 13 months | retain event metadata for security audit then purge | Security |
| order history | consumer order is completed | 7 years | retain transaction record for tax and accounting obligations | Finance Compliance |
| shopping cart telemetry | cart abandoned without purchase | 90 days | delete event-level cart telemetry after analytics window | Analytics |
| website clickstream | non-authenticated browsing analytics | 13 months | aggregate or delete raw clickstream after analytics period | Analytics |
| marketing email event | subscriber remains opted in | 24 months | retain engagement events for campaign analytics then aggregate | Marketing Operations |
| marketing suppression list | customer opted out of marketing | indefinite minimal record | retain hashed suppression indicator to honor future opt-out | Privacy Operations |
| customer service email | support case is closed | 24 months | delete message body after support retention unless hold applies | Support Operations |
| voice call recording | support call recorded with notice | 12 months | delete audio after QA period unless escalated case requires preservation | Support Operations |
| voice call transcript | automated transcript generated from support call | 18 months | delete transcript after extended search and QA period | Support Operations |
| refund audit trail | refund completed | 7 years | retain financial audit metadata and approval history | Finance Compliance |
| chargeback evidence | issuer dispute is closed | 7 years | retain evidence package for audit and repeat-dispute defense | Chargeback Ops |
| shipping label image | parcel delivered and claim period ended | 18 months | delete label image after carrier claim window | Logistics |
| delivery proof photo | carrier supplied proof-of-delivery image | 12 months | delete photo after delivery dispute period | Logistics |
| identity verification image | verification completed and policy allows deletion | 90 days | delete raw image and retain only verification result metadata | Identity Operations |
| identity verification result | verification decision and provider reference | 5 years | retain result metadata for audit and fraud defense | Identity Operations |
| employee admin audit log | privileged support action executed | 7 years | retain immutable admin audit event | Security Compliance |
| API request log body | production API request may contain customer payload | 30 days | delete request body while retaining minimal operational metadata | API Platform |
| API request metadata | method route status latency and request id | 13 months | retain operational metadata for reliability analysis then aggregate | API Platform |
| search query logs | customer uses site search while authenticated | 180 days | delete or aggregate raw query history after product-analysis window | Search Platform |
| recommendation features | derived personalization vector | 90 days after account deletion | delete derived vector when source profile is deleted | ML Platform |
| model evaluation traces | sanitized test trace has no production personal data | 24 months | retain for model regression analysis under test-data policy | AI Platform |
| production agent trace | trace may include customer message and tool results | 90 days | delete detailed trace after incident-debugging window unless held | AI Platform |
| legal hold material | record is subject to active legal hold | until hold released | suspend normal deletion and preserve record immutably | Legal |
| regulator request package | data assembled for formal regulatory response | 7 years | retain submitted package and correspondence | Legal Compliance |
| vendor support ticket | ticket includes BrightCart customer identifiers | 24 months after closure | delete exported customer details and retain vendor contract metadata | Vendor Management |
| sandbox test account | synthetic account is marked non-production | 90 days | purge sandbox data after test lifecycle unless fixture is approved | Engineering |
| support chat transcript | case is closed and no legal hold exists | 24 months | delete transcript after retention period | Privacy Operations |

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

This page is the primary BrightCart source for retention period. Copied tables in tickets or chat exports are secondary and may be stale.
