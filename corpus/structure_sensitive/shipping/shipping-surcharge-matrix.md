---
doc_id: brightcart/v2/structured/shipping/shipping-surcharge-matrix
title: Shipping Surcharge Matrix
source_type: reference
source_system: engineering_docs
domain: shipping
version: '2.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v2/structured/shipping/shipping-surcharge-matrix
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
- shipping
- markdown-table
- long-table
- fixed-chunker-cut-target
---

# Shipping Surcharge Matrix

## Purpose

This reference defines the current shipping surcharge for BrightCart production cases. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

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
| continental oversized parcel | zone 5 to 8 and package exceeds 48 inches on longest side | $25 | add oversized handling surcharge before label purchase | Fulfillment |
| hazmat ground shipment | approved hazardous material SKU routed by ground | $18 | add regulated-material handling surcharge and block air service | Fulfillment |
| signature required | order value exceeds $750 and carrier supports adult signature | $8 | add signature service and include fee in shipping quote | Risk Logistics |
| rural residential delivery | carrier address classification is extended-area residential | $12 | apply residential extended-area surcharge from carrier tariff | Fulfillment |
| PO box fallback | address is a PO box and premium carrier cannot deliver | service change | switch to postal service; do not charge premium-carrier surcharge | Shipping Ops |
| Saturday requested | customer selects Saturday delivery and destination supports option | $20 | add weekend delivery surcharge and retain requested date | Fulfillment |
| Sunday unsupported | customer requests Sunday but destination has no Sunday service | not available | remove option and offer next supported delivery date | Shipping Ops |
| cold chain packaging | temperature-controlled SKU requires insulated packaging | $15 | add cold-chain packaging fee and use approved carrier service | Special Handling |
| dry ice shipment | medical accessory ships with dry ice under carrier threshold | $22 | add dry-ice handling charge and required label | Special Handling |
| address correction | carrier corrected invalid street information after tender | $17 | pass through verified carrier correction fee when caused by submitted address | Shipping Finance |
| remote island delivery | destination is listed in carrier remote-island appendix | $38 | add remote-area surcharge and extend delivery estimate | International Logistics |
| military APO FPO | destination is eligible military postal address | no surcharge | route through postal service and suppress commercial remote-area fee | Shipping Ops |
| international brokerage | destination requires BrightCart-brokered customs entry | $30 | add brokerage service charge unless contract says duties paid by recipient | International Logistics |
| oversize plus remote | package qualifies for both oversize and remote-area fees | combined allowed | apply both fees only when carrier tariff permits stacking | Shipping Finance |
| carrier fuel adjustment | weekly carrier fuel index exceeds contract threshold | variable | apply published fuel percentage to eligible transportation charge | Shipping Finance |
| peak holiday week | carrier peak calendar is active for destination | $6 | add temporary peak surcharge and show it separately at checkout | Fulfillment |
| return label deduction | customer-paid return is outside free-return policy | $9 | deduct return label fee from refund after first carrier scan | Returns Ops |
| failed delivery reattempt | carrier allows paid reattempt after customer was unavailable | $11 | charge reattempt only after customer accepts new delivery attempt | Support |
| intercept requested | customer asks to redirect package after carrier acceptance | $19 | charge carrier intercept fee if intercept succeeds | Shipping Ops |
| business dock delivery | commercial address has dock and no liftgate needed | no surcharge | use business tariff and suppress residential/liftgate fees | B2B Logistics |
| liftgate required | heavy freight destination lacks loading dock | $85 | add liftgate fee and schedule freight appointment | Freight Operations |
| inside delivery freight | customer requests freight moved inside building | $120 | add inside-delivery service and require appointment confirmation | Freight Operations |
| white glove assembly | eligible furniture order includes assembly service | $199 | add white-glove service and route to specialty carrier | Specialty Delivery |
| same day metro | eligible postal code before cutoff | $29 | add same-day service fee and reserve local courier capacity | Metro Delivery |
| same day after cutoff | eligible postal code but order placed after published cutoff | not available | offer next-day service; do not override cutoff manually | Metro Delivery |
| locker delivery | customer selects supported partner locker | no surcharge | route package to locker network and suppress residential fee | Shipping Ops |
| oversize locker attempt | package dimensions exceed locker maximum | not eligible | remove locker option and request alternate address | Shipping Ops |
| carbon neutral add-on | customer opts into verified carbon-offset shipping | $2 | add optional offset line and retain standard carrier service | Sustainability Ops |
| insurance declared value | customer buys declared-value protection above base coverage | 1.2% of excess value | add declared-value charge using carrier coverage schedule | Shipping Finance |
| international DDP | checkout uses duties-delivered-paid terms | estimated duties plus brokerage | collect landed-cost amount and mark shipment DDP | International Logistics |
| international DAP | recipient is responsible for import charges | no BrightCart duty collection | show recipient-responsibility notice and do not collect brokerage estimate | International Logistics |
| high-value secure transport | order exceeds $5,000 and contains controlled luxury SKU | $75 | use secure carrier service and require signature chain | Risk Logistics |
| Alaska oversized parcel | zone AK and package over 50 lb | $45 | add oversized remote-zone surcharge | Fulfillment |

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

This page is the primary BrightCart source for shipping surcharge. Copied tables in tickets or chat exports are secondary and may be stale.
