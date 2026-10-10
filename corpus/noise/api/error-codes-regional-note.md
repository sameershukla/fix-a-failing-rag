---
doc_id: generated/level2-noise/api/error-codes-regional-note
title: Common API Error Codes — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: api
version: noise-4
created_date: '2025-11-18'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/error-codes
region: UK
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
- api
---

# Common API Error Codes — Regional Note

## Regional scope

This note applies to **CA operations** and discusses common api error codes. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/api/error-codes`.

## Global baseline

The global baseline summarized for agents is: This quick reference lists common HTTP responses returned by the BrightCart API and the general action expected from clients. Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for… Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For CA, an additional local handling window of **60 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

CA teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Common API Error Codes.

## Example

A CA customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **60** and **12** in the same paragraph.

## Exception boundary

Do not apply the CA exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: Use 400 for malformed requests, 401 for missing or invalid authentication, 403 for authenticated clients without permission, 404 for missing resources, 409 for state conflicts, 422 for valid syntax with invalid business data, 429 for rate limits, 500 for unexpected server errors, and 503 for temporary service… The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Commerce API. Last reviewed 2026-01-07. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning CA should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/api/error-codes`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

