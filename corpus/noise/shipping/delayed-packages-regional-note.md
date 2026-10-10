---
doc_id: generated/level2-noise/shipping/delayed-packages-regional-note
title: Delayed Package Handling — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: shipping
version: noise-4
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/delayed-packages
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
- shipping
---

# Delayed Package Handling — Regional Note

## Regional scope

This note applies to **UK operations** and discusses delayed package handling. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/shipping/delayed-packages`.

## Global baseline

The global baseline summarized for agents is: This runbook defines when support should treat a shipment as delayed and what checks to perform before replacing or refunding an order. A package is considered delayed when it is more than 2 business days past the latest promised delivery date and tracking does not show delivery. Before that point, support should provide the current tracking status unless there is evidence of loss or damage. The order page promises… Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For UK, an additional local handling window of **60 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

UK teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Delayed Package Handling.

## Example

A UK customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **60** and **8** in the same paragraph.

## Exception boundary

Do not apply the UK exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: A package is considered delayed when it is more than 2 business days past the latest promised delivery date and tracking does not show delivery. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Trust and Safety. Last reviewed 2026-08-22. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning UK should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/shipping/delayed-packages`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

