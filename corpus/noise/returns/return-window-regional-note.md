---
doc_id: generated/level2-noise/returns/return-window-regional-note
title: Standard Return Window — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: returns
version: noise-4
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/returns/return-window
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
- returns
---

# Standard Return Window — Regional Note

## Regional scope

This note applies to **IN operations** and discusses standard return window. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/returns/return-window`.

## Global baseline

The global baseline summarized for agents is: This policy defines the default period in which customers can request a return. It should be checked before product specific restrictions such as electronics or final sale rules. The standard return window is 30 calendar days from the carrier confirmed delivery date. The request must be opened by the end of day on day 30. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For IN, an additional local handling window of **7 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

IN teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Standard Return Window.

## Example

A IN customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **7** and **4** in the same paragraph.

## Exception boundary

Do not apply the IN exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It should be checked before product specific restrictions such as electronics or final sale rules. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Payments Ops. Last reviewed 2026-01-07. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning IN should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/returns/return-window`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

