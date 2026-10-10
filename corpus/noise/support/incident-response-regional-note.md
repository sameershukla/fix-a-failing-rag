---
doc_id: generated/level2-noise/support/incident-response-regional-note
title: Incident Response Process — Regional Note
source_type: regional_policy_note
source_system: regional_ops
domain: support
version: noise-4
created_date: '2026-01-07'
status: active
authority: secondary
canonical_doc_id: brightcart/v1/support/incident-response
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
- support
---

# Incident Response Process — Regional Note

## Regional scope

This note applies to **EU operations** and discusses incident response process. It is active for regional agents but is not a replacement for the global canonical page `brightcart/v1/support/incident-response`.

## Global baseline

The global baseline summarized for agents is: This runbook describes the first response steps for service incidents and the follow up expected after restoration. A SEV 1 incident should be acknowledged within 15 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 5 business days after a SEV 1 or qualifying SEV 2 incident is resolved. Regional teams must start from that rule and then apply local obligations or carrier/bank constraints.

## Regional difference

For EU, an additional local handling window of **7 days** can apply in cases covered by consumer law, banking settlement, or a regional logistics contract. This can make the regional answer look inconsistent with the global rule.

## Local terminology

EU teams sometimes use different words for the same workflow. The note maps “reversal,” “return,” “cooling off,” “settlement,” and “service request” to terms used in Incident Response Process.

## Example

A EU customer receives the normal BrightCart treatment but also falls under a local requirement. The agent records both timelines rather than replacing the global one. The combined explanation can contain **7** and **24** in the same paragraph.

## Exception boundary

Do not apply the EU exception to customers outside the region. Location must come from the account and transaction context, not from the language used in the customer message.

## Copied canonical excerpt

For convenience the regional page copied this sentence from Policy Hub: A SEV 1 incident should be acknowledged within 15 minutes. The copy may lag behind Policy Hub if the global document changes.

## Regional owner note

Owner: Commerce API. Last reviewed 2026-08-22. A review ticket is open because some examples were written before the September global update.

## Retrieval hazard

A query mentioning EU should sometimes prefer this note; a generic query should normally prefer the canonical page. Without metadata-aware retrieval, both can rank together and reduce precision.

## Authority rule

Use this note only when regional context is established. Otherwise, answer from `brightcart/v1/support/incident-response`. Where local law and global policy conflict, escalate to the regional owner rather than combining numbers.

