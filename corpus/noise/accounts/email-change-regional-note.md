---
doc_id: generated/level2-noise/accounts/email-change-regional-note
title: Changing the Account Email Address — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: accounts
version: noise-4
created_date: '2026-02-14'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/accounts/email-change
region: GLOBAL
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

# Changing the Account Email Address — Regional Note

## Regional scope

This note applies to **IN operations** and discusses changing the account email address. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/accounts/email-change`.

## Global baseline

The global baseline summarized for agents is: This article describes how a signed in customer changes the primary email on a BrightCart account. It is designed to prevent an attacker with a temporary session from silently taking over the account. To change the account email, the customer must enter the current password and verify the new email address. BrightCart sends a security notice to the old email address after the change. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For IN, an additional local handling window of **21 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

IN teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Changing the Account Email Address.

## Example

A IN customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **21** and **48** in the same paragraph.

## Exception boundary

Do not apply the IN exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: It is designed to prevent an attacker with a temporary session from silently taking over the account. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Privacy Office. Last reviewed 2026-05-29. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning IN should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/accounts/email-change`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

