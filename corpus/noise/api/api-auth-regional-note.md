---
doc_id: generated/level2-noise/api/api-auth-regional-note
title: API Authentication — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: api
version: noise-4
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/api/api-auth
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
- api
---

# API Authentication — Regional Note

## Regional scope

This note applies to **EU operations** and discusses api authentication. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/api/api-auth`.

## Global baseline

The global baseline summarized for agents is: This reference explains how server to server clients authenticate to the BrightCart public API. It is intended for integration developers. Server integrations use OAuth 2.0 client credentials to obtain an access token. Access tokens are valid for 60 minutes. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For EU, an additional local handling window of **5 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

EU teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in API Authentication.

## Example

A EU customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **5** and **24** in the same paragraph.

## Exception boundary

Do not apply the EU exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It is intended for integration developers. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Fulfillment. Last reviewed 2026-07-11. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning EU should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/api/api-auth`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

