---
doc_id: brightcart/v3/handbooks/international-customs-runbook
title: International Customs and Cross Border Runbook
source_type: handbook
source_system: ops-runbooks
domain: fulfillment
version: '3.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v3/handbooks/international-customs-runbook
company: BrightCart
team: Global Fulfillment
environment: all
access_group: fulfillment-internal
owner: Global Fulfillment Documentation
language: en
region: global
audience:
- operations
- engineering
- support
tags:
- enterprise-expansion
- longform
- hierarchical
- module-2
- module-3
---

# International Customs and Cross Border Runbook

This handbook is the operational source of truth for fulfillment work. It is intentionally long because the procedure crosses teams, systems, exception paths, and evidence requirements. Use the table of contents and heading trail when chunking or retrieving from this document.

## Scope and authority

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 1.1 and should be recorded under reason code FULFI-011.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 1.2 and should be recorded under reason code FULFI-012.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 1.3 and should be recorded under reason code FULFI-013.

### Scope and authority: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 1.4 and should be recorded under reason code FULFI-014.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 1.5 and should be recorded under reason code FULFI-015.

## Roles and ownership

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 2.1 and should be recorded under reason code FULFI-021.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 2.2 and should be recorded under reason code FULFI-022.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 2.3 and should be recorded under reason code FULFI-023.

### Roles and ownership: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 2.4 and should be recorded under reason code FULFI-024.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 2.5 and should be recorded under reason code FULFI-025.

## Terminology

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 3.1 and should be recorded under reason code FULFI-031.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 3.2 and should be recorded under reason code FULFI-032.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 3.3 and should be recorded under reason code FULFI-033.

### Terminology: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 3.4 and should be recorded under reason code FULFI-034.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 3.5 and should be recorded under reason code FULFI-035.

## Entry criteria

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 4.1 and should be recorded under reason code FULFI-041.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 4.2 and should be recorded under reason code FULFI-042.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 4.3 and should be recorded under reason code FULFI-043.

### Entry criteria: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 4.4 and should be recorded under reason code FULFI-044.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 4.5 and should be recorded under reason code FULFI-045.

## Required identifiers

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 5.1 and should be recorded under reason code FULFI-051.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 5.2 and should be recorded under reason code FULFI-052.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 5.3 and should be recorded under reason code FULFI-053.

### Required identifiers: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 5.4 and should be recorded under reason code FULFI-054.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 5.5 and should be recorded under reason code FULFI-055.

## Normal workflow

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 6.1 and should be recorded under reason code FULFI-061.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 6.2 and should be recorded under reason code FULFI-062.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 6.3 and should be recorded under reason code FULFI-063.

### Normal workflow: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 6.4 and should be recorded under reason code FULFI-064.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 6.5 and should be recorded under reason code FULFI-065.

## State transitions

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 7.1 and should be recorded under reason code FULFI-071.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 7.2 and should be recorded under reason code FULFI-072.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 7.3 and should be recorded under reason code FULFI-073.

### State transitions: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 7.4 and should be recorded under reason code FULFI-074.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 7.5 and should be recorded under reason code FULFI-075.

## Customer communication

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 8.1 and should be recorded under reason code FULFI-081.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 8.2 and should be recorded under reason code FULFI-082.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 8.3 and should be recorded under reason code FULFI-083.

### Customer communication: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 8.4 and should be recorded under reason code FULFI-084.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 8.5 and should be recorded under reason code FULFI-085.

## Evidence collection

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 9.1 and should be recorded under reason code FULFI-091.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 9.2 and should be recorded under reason code FULFI-092.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 9.3 and should be recorded under reason code FULFI-093.

### Evidence collection: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 9.4 and should be recorded under reason code FULFI-094.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 9.5 and should be recorded under reason code FULFI-095.

## Timing and SLAs

A parcel held by customs for fewer than 7 calendar days stays in MONITOR status.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 10.1 and should be recorded under reason code FULFI-101.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 10.2 and should be recorded under reason code FULFI-102.

### Timing and SLAs: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 10.3 and should be recorded under reason code FULFI-103.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 10.4 and should be recorded under reason code FULFI-104.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 10.5 and should be recorded under reason code FULFI-105.

## Retries and idempotency

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 11.1 and should be recorded under reason code FULFI-111.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 11.2 and should be recorded under reason code FULFI-112.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 11.3 and should be recorded under reason code FULFI-113.

### Retries and idempotency: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 11.4 and should be recorded under reason code FULFI-114.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 11.5 and should be recorded under reason code FULFI-115.

## Regional handling

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 12.1 and should be recorded under reason code FULFI-121.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 12.2 and should be recorded under reason code FULFI-122.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 12.3 and should be recorded under reason code FULFI-123.

### Regional handling: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 12.4 and should be recorded under reason code FULFI-124.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 12.5 and should be recorded under reason code FULFI-125.

## Enterprise customer handling

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 13.1 and should be recorded under reason code FULFI-131.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 13.2 and should be recorded under reason code FULFI-132.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 13.3 and should be recorded under reason code FULFI-133.

### Enterprise customer handling: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 13.4 and should be recorded under reason code FULFI-134.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 13.5 and should be recorded under reason code FULFI-135.

## Risk review

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 14.1 and should be recorded under reason code FULFI-141.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 14.2 and should be recorded under reason code FULFI-142.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 14.3 and should be recorded under reason code FULFI-143.

### Risk review: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 14.4 and should be recorded under reason code FULFI-144.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 14.5 and should be recorded under reason code FULFI-145.

## Manual approval

DDP orders are not charged a second duty by BrightCart even if a carrier message asks for payment.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 15.1 and should be recorded under reason code FULFI-151.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 15.2 and should be recorded under reason code FULFI-152.

### Manual approval: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 15.3 and should be recorded under reason code FULFI-153.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 15.4 and should be recorded under reason code FULFI-154.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 15.5 and should be recorded under reason code FULFI-155.

## Failure recovery

At 7 calendar days, the case is assigned to the customs broker queue; at 14 days, the customer may choose refund or reshipment.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 16.1 and should be recorded under reason code FULFI-161.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 16.2 and should be recorded under reason code FULFI-162.

### Failure recovery: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 16.3 and should be recorded under reason code FULFI-163.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 16.4 and should be recorded under reason code FULFI-164.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 16.5 and should be recorded under reason code FULFI-165.

## Escalation path

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 17.1 and should be recorded under reason code FULFI-171.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 17.2 and should be recorded under reason code FULFI-172.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 17.3 and should be recorded under reason code FULFI-173.

### Escalation path: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 17.4 and should be recorded under reason code FULFI-174.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 17.5 and should be recorded under reason code FULFI-175.

## Audit trail

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 18.1 and should be recorded under reason code FULFI-181.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 18.2 and should be recorded under reason code FULFI-182.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 18.3 and should be recorded under reason code FULFI-183.

### Audit trail: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 18.4 and should be recorded under reason code FULFI-184.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 18.5 and should be recorded under reason code FULFI-185.

## Monitoring

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 19.1 and should be recorded under reason code FULFI-191.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 19.2 and should be recorded under reason code FULFI-192.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 19.3 and should be recorded under reason code FULFI-193.

### Monitoring: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 19.4 and should be recorded under reason code FULFI-194.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 19.5 and should be recorded under reason code FULFI-195.

## Examples

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 20.1 and should be recorded under reason code FULFI-201.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 20.2 and should be recorded under reason code FULFI-202.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 20.3 and should be recorded under reason code FULFI-203.

### Examples: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 20.4 and should be recorded under reason code FULFI-204.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 20.5 and should be recorded under reason code FULFI-205.

## Common mistakes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 21.1 and should be recorded under reason code FULFI-211.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 21.2 and should be recorded under reason code FULFI-212.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 21.3 and should be recorded under reason code FULFI-213.

### Common mistakes: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 21.4 and should be recorded under reason code FULFI-214.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 21.5 and should be recorded under reason code FULFI-215.

## Change management

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the fulfillment workflow, this guidance applies at stage 22.1 and should be recorded under reason code FULFI-221.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 22.2 and should be recorded under reason code FULFI-222.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 22.3 and should be recorded under reason code FULFI-223.

### Change management: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 22.4 and should be recorded under reason code FULFI-224.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 22.5 and should be recorded under reason code FULFI-225.

## Appendix A: decision checklist

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 23.1 and should be recorded under reason code FULFI-231.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 23.2 and should be recorded under reason code FULFI-232.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 23.3 and should be recorded under reason code FULFI-233.

### Appendix A: decision checklist: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 23.4 and should be recorded under reason code FULFI-234.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 23.5 and should be recorded under reason code FULFI-235.

## Appendix B: field reference

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 24.1 and should be recorded under reason code FULFI-241.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 24.2 and should be recorded under reason code FULFI-242.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the fulfillment workflow, this guidance applies at stage 24.3 and should be recorded under reason code FULFI-243.

### Appendix B: field reference: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the fulfillment workflow, this guidance applies at stage 24.4 and should be recorded under reason code FULFI-244.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the fulfillment workflow, this guidance applies at stage 24.5 and should be recorded under reason code FULFI-245.
