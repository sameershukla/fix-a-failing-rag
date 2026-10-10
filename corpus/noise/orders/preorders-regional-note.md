---
doc_id: generated/level2-noise/orders/preorders-regional-note
title: Preorder Fulfillment and Payment — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: orders
version: noise-4
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/orders/preorders
region: GLOBAL
company: BrightCart
audience:
- support
- operations
- engineering
retrieval_hazard: regional-note
tags:
- level-2
- messy
- noise
- regional-note
- orders
---

# Preorder Fulfillment and Payment — Regional Note

## Regional scope

This note applies to **IN operations** and discusses preorder fulfillment and payment. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/orders/preorders`.

## Global baseline

The global baseline summarized for agents is: This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled. For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier schedule changes. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For IN, an additional local handling window of **14 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

IN teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Preorder Fulfillment and Payment.

## Example

A IN customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **14** and **6** in the same paragraph.

## Exception boundary

Do not apply the IN exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It explains expected dates and how card payment is handled. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Trust and Safety. Last reviewed 2025-11-18. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning IN should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/orders/preorders`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

