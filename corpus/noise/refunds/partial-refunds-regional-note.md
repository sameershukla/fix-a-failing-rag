---
doc_id: generated/level2-noise/refunds/partial-refunds-regional-note
title: Partial Refunds and Deductions — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: refunds
version: noise-4
created_date: '2026-04-03'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/refunds/partial-refunds
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
- refunds
---

# Partial Refunds and Deductions — Regional Note

## Regional scope

This note applies to **IN operations** and discusses partial refunds and deductions. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/refunds/partial-refunds`.

## Global baseline

The global baseline summarized for agents is: Partial refunds are used when the customer is owed money but not the full original item price. This guide explains the allowed reasons for deductions and the information that must be shown to the customer. A partial refund may be issued when returned merchandise is missing customer removable parts, shows customer caused damage, or only part of a multi item order is being refunded. The deduction must be tied to a… Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For IN, an additional local handling window of **5 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

IN teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Partial Refunds and Deductions.

## Example

A IN customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **5** and **72** in the same paragraph.

## Exception boundary

Do not apply the IN exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: This guide explains the allowed reasons for deductions and the information that must be shown to the customer. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Platform Engineering. Last reviewed 2026-01-07. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning IN should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/refunds/partial-refunds`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

