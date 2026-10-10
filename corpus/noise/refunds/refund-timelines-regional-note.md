---
doc_id: generated/level2-noise/refunds/refund-timelines-regional-note
title: Refund Timelines by Payment Method — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: refunds
version: noise-4
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/refund-timelines
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
- refunds
---

# Refund Timelines by Payment Method — Regional Note

## Regional scope

This note applies to **UK operations** and discusses refund timelines by payment method. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/refunds/refund-timelines`.

## Global baseline

The global baseline summarized for agents is: This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear. After a refund is issued, card refunds usually appear within 3 to 5 business days, ACH refunds usually appear within 5 to 7 business days, and gift card refunds are normally available the… Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For UK, an additional local handling window of **90 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

UK teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Refund Timelines by Payment Method.

## Example

A UK customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **90** and **18** in the same paragraph.

## Exception boundary

Do not apply the UK exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: Use it when a refund is already in issued status and the customer wants to know when the money will appear. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Regional Operations. Last reviewed 2026-02-14. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning UK should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/refunds/refund-timelines`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

