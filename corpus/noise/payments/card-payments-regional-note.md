---
doc_id: generated/level2-noise/payments/card-payments-regional-note
title: Card Payment Authorization and Capture — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: payments
version: noise-4
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/card-payments
region: CA
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
- payments
---

# Card Payment Authorization and Capture — Regional Note

## Regional scope

This note applies to **AU operations** and discusses card payment authorization and capture. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/payments/card-payments`.

## Global baseline

The global baseline summarized for agents is: Card Payment Authorization and Capture This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships. BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For AU, an additional local handling window of **7 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

AU teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Card Payment Authorization and Capture.

## Example

A AU customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **7** and **48** in the same paragraph.

## Exception boundary

Do not apply the AU exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: This article explains when BrightCart authorizes and captures card payments. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Customer Care. Last reviewed 2026-08-22. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning AU should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/payments/card-payments`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

