---
doc_id: generated/level2-noise/accounts/account-lockout-regional-note
title: Account Lockout Policy — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: accounts
version: noise-4
created_date: '2026-05-29'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/account-lockout
region: IN
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

# Account Lockout Policy — Regional Note

## Regional scope

This note applies to **UK operations** and discusses account lockout policy. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/accounts/account-lockout`.

## Global baseline

The global baseline summarized for agents is: This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period. After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For UK, an additional local handling window of **10 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

UK teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Account Lockout Policy.

## Example

A UK customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **10** and **48** in the same paragraph.

## Exception boundary

Do not apply the UK exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It describes the automatic lock and what support can and cannot do during the lock period. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Subscription Ops. Last reviewed 2025-11-18. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning UK should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/accounts/account-lockout`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

