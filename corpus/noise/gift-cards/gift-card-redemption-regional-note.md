---
doc_id: generated/level2-noise/gift-cards/gift-card-redemption-regional-note
title: Redeeming Gift Cards — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: gift-cards
version: noise-4
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/gift-cards/gift-card-redemption
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
- gift-cards
---

# Redeeming Gift Cards — Regional Note

## Regional scope

This note applies to **CA operations** and discusses redeeming gift cards. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/gift-cards/gift-card-redemption`.

## Global baseline

The global baseline summarized for agents is: This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total. Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For CA, an additional local handling window of **14 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

CA teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Redeeming Gift Cards.

## Example

A CA customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **14** and **18** in the same paragraph.

## Exception boundary

Do not apply the CA exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: Customers can apply up to 3 BrightCart gift cards to one order. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Payments Ops. Last reviewed 2026-08-22. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning CA should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/gift-cards/gift-card-redemption`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

