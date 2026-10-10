---
doc_id: generated/level2-noise/accounts/account-deletion-regional-note
title: Customer Account Deletion — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: accounts
version: noise-4
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-deletion
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
- accounts
---

# Customer Account Deletion — Regional Note

## Regional scope

This note applies to **GLOBAL operations** and discusses customer account deletion. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/accounts/account-deletion`.

## Global baseline

The global baseline summarized for agents is: This policy explains what happens after a customer requests deletion of a BrightCart account. It separates user visible account removal from data that must be retained for legal or financial reasons. After identity verification, BrightCart schedules account deletion and completes the customer facing deletion within 30 days. Certain transaction, tax, fraud, and legal records can be retained when required by law or… Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For GLOBAL, an additional local handling window of **30 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

GLOBAL teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Customer Account Deletion.

## Example

A GLOBAL customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **30** and **18** in the same paragraph.

## Exception boundary

Do not apply the GLOBAL exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It separates user visible account removal from data that must be retained for legal or financial reasons. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Subscription Ops. Last reviewed 2026-02-14. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning GLOBAL should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/accounts/account-deletion`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

