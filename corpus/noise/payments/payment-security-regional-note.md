---
doc_id: generated/level2-noise/payments/payment-security-regional-note
title: Payment Data Security Rules — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: payments
version: noise-4
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/payment-security
region: AU
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

# Payment Data Security Rules — Regional Note

## Regional scope

This note applies to **IN operations** and discusses payment data security rules. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/payments/payment-security`.

## Global baseline

The global baseline summarized for agents is: This policy defines the payment information BrightCart staff and systems may store or place in support tools. It is intended to reduce exposure of sensitive card data. BrightCart systems must not store card CVV values after authorization. Support staff must never ask customers to send a full card number, CVV, or card image through chat or email. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For IN, an additional local handling window of **30 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

IN teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Payment Data Security Rules.

## Example

A IN customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **30** and **8** in the same paragraph.

## Exception boundary

Do not apply the IN exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It is intended to reduce exposure of sensitive card data. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Regional Operations. Last reviewed 2026-02-14. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning IN should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/payments/payment-security`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

