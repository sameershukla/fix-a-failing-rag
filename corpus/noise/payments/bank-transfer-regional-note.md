---
doc_id: generated/level2-noise/payments/bank-transfer-regional-note
title: Business ACH Payments — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: payments
version: noise-4
created_date: '2026-07-11'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/payments/bank-transfer
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
- payments
---

# Business ACH Payments — Regional Note

## Regional scope

This note applies to **US operations** and discusses business ach payments. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/payments/bank-transfer`.

## Global baseline

The global baseline summarized for agents is: This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout. Approved business customers can pay by ACH. ACH payments normally take 2 to 3 business days to clear. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For US, an additional local handling window of **3 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

US teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Business ACH Payments.

## Example

A US customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **3** and **18** in the same paragraph.

## Exception boundary

Do not apply the US exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: Consumer accounts do not see this payment method at checkout. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Commerce API. Last reviewed 2026-05-29. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning US should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/payments/bank-transfer`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

