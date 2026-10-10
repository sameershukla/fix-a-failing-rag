---
doc_id: generated/level2-noise/support/severity-regional-note
title: Incident Severity Levels — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: support
version: noise-4
created_date: '2026-08-22'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/severity
region: EU
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
- support
---

# Incident Severity Levels — Regional Note

## Regional scope

This note applies to **CA operations** and discusses incident severity levels. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/support/severity`.

## Global baseline

The global baseline summarized for agents is: This reference defines BrightCart incident severity so teams use the same language when deciding response urgency. SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects… Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For CA, an additional local handling window of **7 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

CA teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Incident Severity Levels.

## Example

A CA customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **7** and **6** in the same paragraph.

## Exception boundary

Do not apply the CA exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Fulfillment. Last reviewed 2026-08-22. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning CA should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/support/severity`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

