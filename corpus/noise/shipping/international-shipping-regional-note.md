---
doc_id: generated/level2-noise/shipping/international-shipping-regional-note
title: International Shipping and Duties — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: shipping
version: noise-4
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/shipping/international-shipping
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
- shipping
---

# International Shipping and Duties — Regional Note

## Regional scope

This note applies to **CA operations** and discusses international shipping and duties. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/shipping/international-shipping`.

## Global baseline

The global baseline summarized for agents is: This policy explains normal international delivery timing and customer responsibility for import charges. It applies only to countries shown as eligible at checkout. International orders normally arrive in 7 to 14 business days after shipment. Import duties, taxes, and customs fees are the customer responsibility unless checkout explicitly states that duties are prepaid. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For CA, an additional local handling window of **21 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

CA teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in International Shipping and Duties.

## Example

A CA customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **21** and **8** in the same paragraph.

## Exception boundary

Do not apply the CA exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It applies only to countries shown as eligible at checkout. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Customer Care. Last reviewed 2026-04-03. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning CA should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/shipping/international-shipping`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

