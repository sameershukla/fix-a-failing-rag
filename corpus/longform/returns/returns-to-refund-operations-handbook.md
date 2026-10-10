---
doc_id: brightcart/v3/handbooks/returns-to-refund-operations-handbook
title: Returns to Refund Operations Handbook
source_type: handbook
source_system: ops-runbooks
domain: returns
version: '3.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v3/handbooks/returns-to-refund-operations-handbook
company: BrightCart
team: Returns Operations
environment: all
access_group: support-internal
owner: Returns Operations Documentation
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

# Returns to Refund Operations Handbook

This handbook is the operational source of truth for returns work. It is intentionally long because the procedure crosses teams, systems, exception paths, and evidence requirements. Use the table of contents and heading trail when chunking or retrieving from this document.

## Scope and authority

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 1.1 and should be recorded under reason code RETUR-011.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 1.2 and should be recorded under reason code RETUR-012.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 1.3 and should be recorded under reason code RETUR-013.

### Scope and authority: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 1.4 and should be recorded under reason code RETUR-014.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 1.5 and should be recorded under reason code RETUR-015.

## Roles and ownership

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 2.1 and should be recorded under reason code RETUR-021.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 2.2 and should be recorded under reason code RETUR-022.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 2.3 and should be recorded under reason code RETUR-023.

### Roles and ownership: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 2.4 and should be recorded under reason code RETUR-024.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 2.5 and should be recorded under reason code RETUR-025.

## Terminology

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 3.1 and should be recorded under reason code RETUR-031.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 3.2 and should be recorded under reason code RETUR-032.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 3.3 and should be recorded under reason code RETUR-033.

### Terminology: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 3.4 and should be recorded under reason code RETUR-034.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 3.5 and should be recorded under reason code RETUR-035.

## Entry criteria

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 4.1 and should be recorded under reason code RETUR-041.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 4.2 and should be recorded under reason code RETUR-042.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 4.3 and should be recorded under reason code RETUR-043.

### Entry criteria: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 4.4 and should be recorded under reason code RETUR-044.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 4.5 and should be recorded under reason code RETUR-045.

## Required identifiers

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 5.1 and should be recorded under reason code RETUR-051.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 5.2 and should be recorded under reason code RETUR-052.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 5.3 and should be recorded under reason code RETUR-053.

### Required identifiers: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 5.4 and should be recorded under reason code RETUR-054.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 5.5 and should be recorded under reason code RETUR-055.

## Normal workflow

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 6.1 and should be recorded under reason code RETUR-061.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 6.2 and should be recorded under reason code RETUR-062.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 6.3 and should be recorded under reason code RETUR-063.

### Normal workflow: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 6.4 and should be recorded under reason code RETUR-064.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 6.5 and should be recorded under reason code RETUR-065.

## State transitions

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 7.1 and should be recorded under reason code RETUR-071.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 7.2 and should be recorded under reason code RETUR-072.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 7.3 and should be recorded under reason code RETUR-073.

### State transitions: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 7.4 and should be recorded under reason code RETUR-074.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 7.5 and should be recorded under reason code RETUR-075.

## Customer communication

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 8.1 and should be recorded under reason code RETUR-081.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 8.2 and should be recorded under reason code RETUR-082.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 8.3 and should be recorded under reason code RETUR-083.

### Customer communication: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 8.4 and should be recorded under reason code RETUR-084.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 8.5 and should be recorded under reason code RETUR-085.

## Evidence collection

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 9.1 and should be recorded under reason code RETUR-091.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 9.2 and should be recorded under reason code RETUR-092.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 9.3 and should be recorded under reason code RETUR-093.

### Evidence collection: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 9.4 and should be recorded under reason code RETUR-094.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 9.5 and should be recorded under reason code RETUR-095.

## Timing and SLAs

The warehouse must inspect a returned parcel within 2 business days of carrier delivery.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 10.1 and should be recorded under reason code RETUR-101.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 10.2 and should be recorded under reason code RETUR-102.

### Timing and SLAs: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 10.3 and should be recorded under reason code RETUR-103.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 10.4 and should be recorded under reason code RETUR-104.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 10.5 and should be recorded under reason code RETUR-105.

## Retries and idempotency

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 11.1 and should be recorded under reason code RETUR-111.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 11.2 and should be recorded under reason code RETUR-112.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 11.3 and should be recorded under reason code RETUR-113.

### Retries and idempotency: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 11.4 and should be recorded under reason code RETUR-114.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 11.5 and should be recorded under reason code RETUR-115.

## Regional handling

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 12.1 and should be recorded under reason code RETUR-121.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 12.2 and should be recorded under reason code RETUR-122.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 12.3 and should be recorded under reason code RETUR-123.

### Regional handling: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 12.4 and should be recorded under reason code RETUR-124.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 12.5 and should be recorded under reason code RETUR-125.

## Enterprise customer handling

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 13.1 and should be recorded under reason code RETUR-131.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 13.2 and should be recorded under reason code RETUR-132.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 13.3 and should be recorded under reason code RETUR-133.

### Enterprise customer handling: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 13.4 and should be recorded under reason code RETUR-134.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 13.5 and should be recorded under reason code RETUR-135.

## Risk review

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 14.1 and should be recorded under reason code RETUR-141.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 14.2 and should be recorded under reason code RETUR-142.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 14.3 and should be recorded under reason code RETUR-143.

### Risk review: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 14.4 and should be recorded under reason code RETUR-144.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 14.5 and should be recorded under reason code RETUR-145.

## Manual approval

If the original card is closed, Payment Operations may issue an ACH fallback only after identity verification and supervisor approval.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 15.1 and should be recorded under reason code RETUR-151.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 15.2 and should be recorded under reason code RETUR-152.

### Manual approval: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 15.3 and should be recorded under reason code RETUR-153.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 15.4 and should be recorded under reason code RETUR-154.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 15.5 and should be recorded under reason code RETUR-155.

## Failure recovery

After inspection reaches ACCEPTED, the refund service receives an event named return.accepted.v2 and must create the refund request within 4 hours.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 16.1 and should be recorded under reason code RETUR-161.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 16.2 and should be recorded under reason code RETUR-162.

### Failure recovery: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 16.3 and should be recorded under reason code RETUR-163.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 16.4 and should be recorded under reason code RETUR-164.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 16.5 and should be recorded under reason code RETUR-165.

## Escalation path

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 17.1 and should be recorded under reason code RETUR-171.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 17.2 and should be recorded under reason code RETUR-172.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 17.3 and should be recorded under reason code RETUR-173.

### Escalation path: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 17.4 and should be recorded under reason code RETUR-174.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 17.5 and should be recorded under reason code RETUR-175.

## Audit trail

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 18.1 and should be recorded under reason code RETUR-181.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 18.2 and should be recorded under reason code RETUR-182.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 18.3 and should be recorded under reason code RETUR-183.

### Audit trail: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 18.4 and should be recorded under reason code RETUR-184.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 18.5 and should be recorded under reason code RETUR-185.

## Monitoring

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 19.1 and should be recorded under reason code RETUR-191.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 19.2 and should be recorded under reason code RETUR-192.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 19.3 and should be recorded under reason code RETUR-193.

### Monitoring: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 19.4 and should be recorded under reason code RETUR-194.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 19.5 and should be recorded under reason code RETUR-195.

## Examples

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 20.1 and should be recorded under reason code RETUR-201.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 20.2 and should be recorded under reason code RETUR-202.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 20.3 and should be recorded under reason code RETUR-203.

### Examples: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 20.4 and should be recorded under reason code RETUR-204.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 20.5 and should be recorded under reason code RETUR-205.

## Common mistakes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 21.1 and should be recorded under reason code RETUR-211.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 21.2 and should be recorded under reason code RETUR-212.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 21.3 and should be recorded under reason code RETUR-213.

### Common mistakes: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 21.4 and should be recorded under reason code RETUR-214.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 21.5 and should be recorded under reason code RETUR-215.

## Change management

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the returns workflow, this guidance applies at stage 22.1 and should be recorded under reason code RETUR-221.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 22.2 and should be recorded under reason code RETUR-222.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 22.3 and should be recorded under reason code RETUR-223.

### Change management: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 22.4 and should be recorded under reason code RETUR-224.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 22.5 and should be recorded under reason code RETUR-225.

## Appendix A: decision checklist

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the returns workflow, this guidance applies at stage 23.1 and should be recorded under reason code RETUR-231.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 23.2 and should be recorded under reason code RETUR-232.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 23.3 and should be recorded under reason code RETUR-233.

### Appendix A: decision checklist: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 23.4 and should be recorded under reason code RETUR-234.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 23.5 and should be recorded under reason code RETUR-235.

## Appendix B: field reference

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 24.1 and should be recorded under reason code RETUR-241.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 24.2 and should be recorded under reason code RETUR-242.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 24.3 and should be recorded under reason code RETUR-243.

### Appendix B: field reference: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 24.4 and should be recorded under reason code RETUR-244.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the returns workflow, this guidance applies at stage 24.5 and should be recorded under reason code RETUR-245.
