---
doc_id: brightcart/v3/handbooks/catalog-change-runbook
title: Catalog Pricing and Inventory Change Runbook
source_type: handbook
source_system: catalog-wiki
domain: catalog
version: '3.0'
effective_date: '2026-10-01'
status: active
authority: primary
canonical_doc_id: brightcart/v3/handbooks/catalog-change-runbook
company: BrightCart
team: Catalog Platform
environment: all
access_group: catalog-editor
owner: Catalog Platform Documentation
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

# Catalog Pricing and Inventory Change Runbook

This handbook is the operational source of truth for catalog work. It is intentionally long because the procedure crosses teams, systems, exception paths, and evidence requirements. Use the table of contents and heading trail when chunking or retrieving from this document.

## Scope and authority

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 1.1 and should be recorded under reason code CATAL-011.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 1.2 and should be recorded under reason code CATAL-012.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 1.3 and should be recorded under reason code CATAL-013.

### Scope and authority: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 1.4 and should be recorded under reason code CATAL-014.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 1.5 and should be recorded under reason code CATAL-015.

## Roles and ownership

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 2.1 and should be recorded under reason code CATAL-021.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 2.2 and should be recorded under reason code CATAL-022.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 2.3 and should be recorded under reason code CATAL-023.

### Roles and ownership: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 2.4 and should be recorded under reason code CATAL-024.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 2.5 and should be recorded under reason code CATAL-025.

## Terminology

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 3.1 and should be recorded under reason code CATAL-031.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 3.2 and should be recorded under reason code CATAL-032.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 3.3 and should be recorded under reason code CATAL-033.

### Terminology: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 3.4 and should be recorded under reason code CATAL-034.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 3.5 and should be recorded under reason code CATAL-035.

## Entry criteria

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 4.1 and should be recorded under reason code CATAL-041.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 4.2 and should be recorded under reason code CATAL-042.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 4.3 and should be recorded under reason code CATAL-043.

### Entry criteria: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 4.4 and should be recorded under reason code CATAL-044.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 4.5 and should be recorded under reason code CATAL-045.

## Required identifiers

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 5.1 and should be recorded under reason code CATAL-051.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 5.2 and should be recorded under reason code CATAL-052.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 5.3 and should be recorded under reason code CATAL-053.

### Required identifiers: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 5.4 and should be recorded under reason code CATAL-054.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 5.5 and should be recorded under reason code CATAL-055.

## Normal workflow

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 6.1 and should be recorded under reason code CATAL-061.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 6.2 and should be recorded under reason code CATAL-062.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 6.3 and should be recorded under reason code CATAL-063.

### Normal workflow: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 6.4 and should be recorded under reason code CATAL-064.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 6.5 and should be recorded under reason code CATAL-065.

## State transitions

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 7.1 and should be recorded under reason code CATAL-071.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 7.2 and should be recorded under reason code CATAL-072.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 7.3 and should be recorded under reason code CATAL-073.

### State transitions: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 7.4 and should be recorded under reason code CATAL-074.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 7.5 and should be recorded under reason code CATAL-075.

## Customer communication

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 8.1 and should be recorded under reason code CATAL-081.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 8.2 and should be recorded under reason code CATAL-082.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 8.3 and should be recorded under reason code CATAL-083.

### Customer communication: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 8.4 and should be recorded under reason code CATAL-084.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 8.5 and should be recorded under reason code CATAL-085.

## Evidence collection

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 9.1 and should be recorded under reason code CATAL-091.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 9.2 and should be recorded under reason code CATAL-092.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 9.3 and should be recorded under reason code CATAL-093.

### Evidence collection: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 9.4 and should be recorded under reason code CATAL-094.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 9.5 and should be recorded under reason code CATAL-095.

## Timing and SLAs

A price decrease above 30 percent requires a Merchandising Director approval before publication.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 10.1 and should be recorded under reason code CATAL-101.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 10.2 and should be recorded under reason code CATAL-102.

### Timing and SLAs: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 10.3 and should be recorded under reason code CATAL-103.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 10.4 and should be recorded under reason code CATAL-104.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 10.5 and should be recorded under reason code CATAL-105.

## Retries and idempotency

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 11.1 and should be recorded under reason code CATAL-111.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 11.2 and should be recorded under reason code CATAL-112.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 11.3 and should be recorded under reason code CATAL-113.

### Retries and idempotency: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 11.4 and should be recorded under reason code CATAL-114.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 11.5 and should be recorded under reason code CATAL-115.

## Regional handling

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 12.1 and should be recorded under reason code CATAL-121.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 12.2 and should be recorded under reason code CATAL-122.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 12.3 and should be recorded under reason code CATAL-123.

### Regional handling: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 12.4 and should be recorded under reason code CATAL-124.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 12.5 and should be recorded under reason code CATAL-125.

## Enterprise customer handling

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 13.1 and should be recorded under reason code CATAL-131.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 13.2 and should be recorded under reason code CATAL-132.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 13.3 and should be recorded under reason code CATAL-133.

### Enterprise customer handling: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 13.4 and should be recorded under reason code CATAL-134.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 13.5 and should be recorded under reason code CATAL-135.

## Risk review

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 14.1 and should be recorded under reason code CATAL-141.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 14.2 and should be recorded under reason code CATAL-142.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 14.3 and should be recorded under reason code CATAL-143.

### Risk review: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 14.4 and should be recorded under reason code CATAL-144.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 14.5 and should be recorded under reason code CATAL-145.

## Manual approval

Retired SKU pages may redirect for 180 days but must not accept new orders.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 15.1 and should be recorded under reason code CATAL-151.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 15.2 and should be recorded under reason code CATAL-152.

### Manual approval: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 15.3 and should be recorded under reason code CATAL-153.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 15.4 and should be recorded under reason code CATAL-154.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 15.5 and should be recorded under reason code CATAL-155.

## Failure recovery

Available-to-promise inventory is calculated from on-hand minus reservations minus safety stock.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 16.1 and should be recorded under reason code CATAL-161.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 16.2 and should be recorded under reason code CATAL-162.

### Failure recovery: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 16.3 and should be recorded under reason code CATAL-163.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 16.4 and should be recorded under reason code CATAL-164.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 16.5 and should be recorded under reason code CATAL-165.

## Escalation path

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 17.1 and should be recorded under reason code CATAL-171.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 17.2 and should be recorded under reason code CATAL-172.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 17.3 and should be recorded under reason code CATAL-173.

### Escalation path: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 17.4 and should be recorded under reason code CATAL-174.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 17.5 and should be recorded under reason code CATAL-175.

## Audit trail

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 18.1 and should be recorded under reason code CATAL-181.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 18.2 and should be recorded under reason code CATAL-182.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 18.3 and should be recorded under reason code CATAL-183.

### Audit trail: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 18.4 and should be recorded under reason code CATAL-184.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 18.5 and should be recorded under reason code CATAL-185.

## Monitoring

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 19.1 and should be recorded under reason code CATAL-191.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 19.2 and should be recorded under reason code CATAL-192.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 19.3 and should be recorded under reason code CATAL-193.

### Monitoring: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 19.4 and should be recorded under reason code CATAL-194.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 19.5 and should be recorded under reason code CATAL-195.

## Examples

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 20.1 and should be recorded under reason code CATAL-201.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 20.2 and should be recorded under reason code CATAL-202.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 20.3 and should be recorded under reason code CATAL-203.

### Examples: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 20.4 and should be recorded under reason code CATAL-204.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 20.5 and should be recorded under reason code CATAL-205.

## Common mistakes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 21.1 and should be recorded under reason code CATAL-211.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 21.2 and should be recorded under reason code CATAL-212.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 21.3 and should be recorded under reason code CATAL-213.

### Common mistakes: operator notes

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 21.4 and should be recorded under reason code CATAL-214.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 21.5 and should be recorded under reason code CATAL-215.

## Change management

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the catalog workflow, this guidance applies at stage 22.1 and should be recorded under reason code CATAL-221.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 22.2 and should be recorded under reason code CATAL-222.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 22.3 and should be recorded under reason code CATAL-223.

### Change management: operator notes

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 22.4 and should be recorded under reason code CATAL-224.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 22.5 and should be recorded under reason code CATAL-225.

## Appendix A: decision checklist

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 23.1 and should be recorded under reason code CATAL-231.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 23.2 and should be recorded under reason code CATAL-232.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 23.3 and should be recorded under reason code CATAL-233.

### Appendix A: decision checklist: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 23.4 and should be recorded under reason code CATAL-234.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 23.5 and should be recorded under reason code CATAL-235.

## Appendix B: field reference

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 24.1 and should be recorded under reason code CATAL-241.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 24.2 and should be recorded under reason code CATAL-242.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 24.3 and should be recorded under reason code CATAL-243.

### Appendix B: field reference: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 24.4 and should be recorded under reason code CATAL-244.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the catalog workflow, this guidance applies at stage 24.5 and should be recorded under reason code CATAL-245.
