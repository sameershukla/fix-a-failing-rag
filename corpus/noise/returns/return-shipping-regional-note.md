---
doc_id: generated/level2-noise/returns/return-shipping-regional-note
title: Return Shipping Charges — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: returns
version: noise-4
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-shipping
region: US
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
- returns
---

# Return Shipping Charges — Regional Note

## Regional scope

This note applies to **CA operations** and discusses return shipping charges. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/returns/return-shipping`.

## Global baseline

The global baseline summarized for agents is: This article explains who pays to send an item back to BrightCart. It applies after a return has been approved and before the label is generated. BrightCart pays return shipping when the item is defective, damaged in transit, or different from what the customer ordered. For preference returns such as size, color, or changed mind, the customer pays the return shipping charge unless a promotion explicitly provides… Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For CA, an additional local handling window of **30 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

CA teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Return Shipping Charges.

## Example

A CA customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **30** and **18** in the same paragraph.

## Exception boundary

Do not apply the CA exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It applies after a return has been approved and before the label is generated. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Privacy Office. Last reviewed 2025-11-18. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning CA should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/returns/return-shipping`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

