# Faithfulness labeling sheet

For each item, read the chunks, then the answer. Decide whether every claim in the answer is supported by the chunks.

- **faithful**: every claim is stated in the chunks or follows directly from them (arithmetic, a plain reading). A true statement that the context does not cover something is faithful.
- **unfaithful**: at least one claim is not supported by the chunks, or contradicts them.
- Judge support only, not whether the source is the right one to trust. Do not use outside knowledge.
- Do not open `labels.yaml` before you finish. Type one word after each `Your verdict (faithful or unfaithful):` line, then run `make judge-compare`.

---

## L01

**Question:** what format is the customer data export file

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/privacy/data-export::0`)

```
Customer Data Export
# Customer Data Export

## Purpose and scope

This policy describes the self service export a verified customer can request for a copy of common BrightCart account data.

## Standard rule

A verified customer data export is normally prepared within 24 hours. When the export is ready, BrightCart sends a download link that remains valid for 48 hours. The link requires the customer to sign in again before download.

## Conditions and decision points

- The request must come from the authenticated account.
- Only data tied to the requesting account is included.
- Large accounts can take longer and will show a pending status.

## Worked example

A customer requests an export at 3:00 PM Tuesday. The file is prepared Wednesday morning and the customer receives a link. If the link is not used within 48 hours, a new export request is required.

## Exceptions and edge cases

- Data under legal restriction can be excluded or delayed.
- Payment processor data controlled by another company is not exported as raw card data.
- Business organization exports can require administrator approval.

## Operational notes

Support can explain the status but should not download the file on behalf of the customer. Expired links should be replaced by a new request, not manually reactivated.
```

Chunk 2 (`brightcart/v3/html/job-export-api::0`)

```
Job Export API
<!doctype html><html><head><title>Job Export API</title></head><body>
<nav>Home | Shop | Cart | Orders | Help | Privacy | Careers | About | Home | Shop | Cart | Orders</nav>
<div class='cookie'>We use cookies. Manage preferences. Necessary. Analytics. Advertising.</div>
<aside><h3>Popular articles</h3><p>Refunds Shipping Password Reset Gift Cards Return Window</p></aside>
<main><h1>Job Export API</h1><p>This page is the current operational guidance.</p><section><h2>Rule</h2><p>The export job status endpoint is GET /v3/exports/{job_id}; completed download links expire after 15 minutes.</p></section>
<section><h2>Example</h2><p>Always confirm the object identifier and current status before applying the rule.</p></section></main
```

Chunk 3 (`brightcart/v2/structured/privacy/privacy-retention-table::7`)

```
Privacy Data Retention Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| model evaluation traces | sanitized test trace has no production personal data | 24 months | retain for model regression analysis under test-data policy | AI Platform |
| production agent trace | trace may include customer message and tool results | 90 days | delete detailed trace after incident-debugging window unless held | AI Platform |
| legal hold material | record is subject to active legal hold | until hold released | suspend normal deletion and preserve record immutably | Legal |
| regulator request package | data assembled for formal regulatory response | 7 years | retain submitted package and correspondence | Legal Compliance |
| vendor support ticket | ticket includes BrightCart customer identifiers | 24 months after closure | delete exported customer details and retain vendor contract metadata | Vendor Management |
| sandbox test account | synthetic account is marked non-production | 90 days | purge sandbox data after test lifecycle unless fixture is approved | Engineering |
```

Chunk 4 (`brightcart/v3/html/job-export-api::1`)

```
Job Export API
confirm the object identifier and current status before applying the rule.</p></section></main>
<footer>© BrightCart | Terms | Privacy | Accessibility | Status | Terms | Privacy | Accessibility</footer></body></html>
```

Chunk 5 (`brightcart/v2/code/refunds/refund-guardrails::1`)

```
tions

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any, Iterable, Mapping, Sequence


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _audit(event: str, details: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Return a small audit record used by examples in this module.

    Production sends this data to the central audit stream.  Keeping the helper in
    the corpus makes the file look like normal service code rather than a tiny toy
    function written solely for retrieval.
    """
    return {"event": event, "details": dict(details or {}), "recorded_at": _utc_now()}


def _normalize_text(value: str) -> str:
    return " ".join(value.strip().lower().split())


def _safe_decimal(value: Decimal | int | str) -> Decimal:
    return Decimal(str(
```

**Answer:**

> The context doesn't say what format the customer data export file is in. The Customer Data Export policy covers timing (prepared within 24 hours), the download link (valid for 48 hours, sign-in required), and scope and exceptions, but it never mentions a file format such as CSV, JSON, or ZIP.
>
> The Job Export API page covers the status endpoint (`GET /v3/exports/{job_id}`) and says completed download links expire after 15 minutes. It doesn't mention a file format either.
>
> You'd need to check another source, such as the export feature's product documentation or the API response schema, to confirm the format.
>
> The two sources also give different link lifetimes (48 hours versus 15 minutes). They may describe different things, a customer self-service export versus a job export API, but the context doesn't clarify that.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L02

**Question:** monthly cost of the pro marketplace plan

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/structured/payments/marketplace-seller-fees::7`)

```
Marketplace Seller Fee Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| return processing | customer return uses marketplace fulfillment service | $4 per unit | deduct return-processing fee when return is received | Marketplace Finance |
| disposal request | seller asks BrightCart to dispose of unsellable inventory | $1.25 per unit | deduct disposal fee after warehouse completion | Marketplace Finance |
| removal order | seller requests inventory shipped back | $3.50 per unit | deduct removal fee and outbound shipping | Marketplace Finance |
| chargeback administration | buyer dispute requires marketplace evidence package | $15 per case | deduct administration fee unless dispute is won under protection policy | Marketplace Finance |
| advertising spend | seller uses sponsored marketplace placement | actual campaign spend | deduct advertising charges from settlement balance | Marketplace Finance |
| subscription fee | seller is enrolled in professional marketplace plan | $39 monthly | deduct monthly subscription fee independent of sales commission | Marketplace Finance |
```

Chunk 2 (`brightcart/v1/subscriptions/subscription-plans::0`)

```
Subscription Plans and Pricing
# Subscription Plans and Pricing

## Purpose and scope

This reference describes the BrightCart Plus subscription options used by support and checkout. It does not list temporary promotional pricing.

## Standard rule

BrightCart Plus is offered as a monthly plan and an annual plan. The annual plan is priced 15 percent lower than paying the standard monthly price for twelve months. Both plans provide the same core member benefits unless a promotion explicitly adds a temporary benefit.

## Conditions and decision points

- Taxes may apply based on customer location.
- Promotional discounts are applied separately from the standard annual savings.
- Plan changes take effect according to the billing change shown at checkout.

## Worked example

If the standard monthly price is $20, twelve months would total $240 before tax. The standard annual plan would be priced at $204 before tax because it includes the 15 percent annual savings.

## Exceptions and edge cases

- Corporate memberships use negotiated pricing.
- Gift memberships are outside this level one corpus.
- A temporary campaign can change the displayed first year price without changing the normal annual discount rule.

## Operational notes

Support should quote the price currently shown on the customer account and explain the annual savings rule instead of promising that a temporary
```

Chunk 3 (`brightcart/v2/structured/refunds/refund-adjustment-limits::5`)

```
Refund Adjustment Limits Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| subscription overlap | customer was charged both monthly and annual plans during migration | one overlapping charge | refund lower-value duplicate subscription charge after entitlement check | Subscriptions |
| gift card plus card split | refund spans gift card and card tender on same order | original tender proportions | return each portion to its original tender and never move gift-card value to cash | Payments Support |
| marketplace seller concession | seller authorized a customer concession in case notes | up to $150 | apply seller-funded adjustment and debit seller settlement balance | Marketplace Ops |
| warehouse cancellation miss | customer cancellation was approved before pick but fulfillment still shipped | item value plus standard shipping | refund item and standard shipping after return scan or carrier intercept | Order Operations |
| lost parcel confirmed | carrier investigation closed as lost and no replacement was sent | order value up to $500 | issue refund after carrier loss case closes and store investigation number | Logistics Support |
```

Chunk 4 (`brightcart/v2/structured/payments/marketplace-seller-fees::6`)

```
Marketplace Seller Fee Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| refund after payout | customer refund posts after seller already received settlement | seller debit | debit future seller balance according to refund allocation | Marketplace Finance |
| seller-funded coupon | seller created promotion and funds discount | discount plus commission basis | calculate commission on post-discount merchandise amount | Marketplace Finance |
| platform-funded coupon | BrightCart funds customer promotion | normal commission basis | calculate seller commission on seller-receivable merchandise amount | Marketplace Finance |
| shipping label purchase | seller buys BrightCart carrier label | carrier cost | deduct label charge separately from marketplace commission | Marketplace Finance |
| storage fee | seller inventory remains in fulfillment center beyond free window | $0.75 per cubic foot weekly | deduct storage fee from next settlement | Marketplace Finance |
| long-term storage | inventory remains beyond 180 days | $2.50 per cubic foot monthly | deduct long-term storage surcharge | Marketplace Finance |
```

Chunk 5 (`brightcart/v2/code/subscriptions/proration::3`)

```
immediate charge.
    """
    price_difference = max(Decimal("0.00"), change.new_monthly_price - change.old_monthly_price)
    fraction = Decimal(change.days_remaining) / Decimal("30")
    return _round_currency(price_difference * fraction)


def cancellation_proration(change: PlanChange) -> Decimal:
    """Cancellation itself does not use upgrade proration; refund eligibility is separate."""
    return Decimal("0.00")


def proration_audit(change: PlanChange, amount: Decimal) -> dict[str, Any]:
    return _audit("subscription_proration", {"days_remaining": change.days_remaining, "amount": str(amount)})
```

**Answer:**

> The professional marketplace plan costs **$49 per month**, according to the Marketplace Seller Fee Matrix. This fee is deducted monthly and applies independently of sales commission.
>
> The context also describes BrightCart Plus, which is a separate customer subscription and not the seller plan, so its pricing doesn't apply here.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L03

**Question:** failed login counter, is it per phone or per account

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/accounts/account-lockout::0`)

```
Account Lockout Policy
# Account Lockout Policy

## Purpose and scope

This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period.

## Standard rule

After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock simply because the customer is in a hurry.

## Conditions and decision points

- The counter is tracked per account, not per device.
- Password reset can still be requested during the lock.
- Repeated distributed attempts may trigger additional security controls.

## Worked example

A customer enters the wrong password five times by 11:05 AM. The account is locked until approximately 11:20 AM. The customer can request a password reset during that period but still must wait for the lock or complete an approved recovery path.

## Exceptions and edge cases

- Security can apply a longer manual hold during an investigation.
- Administrative service accounts use a different control.
- A system outage that returns login errors does not count as failed password attempts.

## Operational notes

Support should explain the timer and offer password reset when appropriate. Do not disclose whether an unknown email address
```

Chunk 2 (`brightcart/v1/security/suspicious-login::0`)

```
Suspicious Login Response
# Suspicious Login Response

## Purpose and scope

This runbook is used when a customer reports an unknown sign in or BrightCart detects a high risk session. The goal is to contain possible account takeover quickly.

## Standard rule

For a credible suspicious login, BrightCart revokes active sessions, requires a password reset, and reviews recent profile and payment changes. The customer should be notified through a verified channel. High confidence account takeover cases are escalated to security.

## Conditions and decision points

- Confirm the customer identity before discussing account details.
- Review recent email, phone, shipping address, and saved payment changes.
- Check whether MFA was added, removed, or challenged.

## Worked example

A customer receives a new device alert from a city they did not visit. After identity verification, support revokes sessions and starts a password reset. The account shows an unauthorized shipping address change, so the case is escalated to security.

## Exceptions and edge cases

- Travel or VPN use can create a false positive alert.
- A failed login attempt alone is not proof of takeover.
- Active fraud or payment theft can require immediate order cancellation.

## Operational notes

Document the alert time, suspicious session
```

Chunk 3 (`brightcart/v2/structured/privacy/pii-masking-config::6`)

```
PII Masking Configuration
config path: logging > redaction > customer
    customer:
      email: MASK_LOCAL_PART
      phone: KEEP_LAST_4
      credit_card: KEEP_LAST_4
      audit_log: required
      fail_closed: true
```

Chunk 4 (`brightcart/v1/security/suspicious-login::1`)

```
Suspicious Login Response
takeover.
- Active fraud or payment theft can require immediate order cancellation.

## Operational notes

Document the alert time, suspicious session, customer confirmation, session revocation, and any profile changes. Do not leave the account active while waiting for a routine queue if takeover is likely.
```

Chunk 5 (`brightcart/v2/structured/security/fraud-review-matrix::5`)

```
Fraud Escalation Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| email change then refund | account changes email before high-value refund request | high risk | hold refund and verify prior account owner | Account Security |
| impossible travel login | successful logins occur from distant countries within one hour | high risk | revoke sessions and require MFA reauthentication | Account Security |
| proxy network checkout | checkout originates from anonymizing network with clean account history | medium risk | apply enhanced verification without automatic block | Trust and Safety |
| reshipper address | shipping address matches known freight-forwarding service | medium risk | review product category and payment history | Trust and Safety |
| digital goods immediate use | new account buys digital value and redeems immediately | high risk | delay fulfillment until payment risk clears | Digital Risk |
| business account large order | verified business account exceeds consumer order threshold | medium risk | use B2B risk workflow rather than consumer auto-block | B2B Risk |
```

**Answer:**

> It's tracked **per device**, not per account. So each phone or laptop has its own counter. After 5 consecutive failed sign-in attempts, the consumer account is locked for 15 minutes. A successful sign-in resets the counter.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L04

**Question:** customer thinks every purchase starts a new 12 month points clock

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/handbooks/loyalty-program-handbook::16`)

```
BrightPoints Loyalty Program Handbook
-093.

### Evidence collection: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the loyalty workflow, this guidance applies at stage 9.4 and should be recorded under reason code LOYAL-094.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the loyalty workflow, this guidance applies at stage 9.5 and should be recorded under reason code LOYAL-095.

## Timing and SLAs

BrightPoints expire after 12 months of account inactivity, not 12 months after each purchase.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the loyalty workflow, this guidance
```

Chunk 2 (`brightcart/v3/lang/puntos-spanglish::0`)

```
Puntos Spanglish
# Puntos Spanglish

## Regla actual

BrightPoints expiran después de 12 meses de inactividad de la cuenta, not twelve months after each purchase.
```

Chunk 3 (`brightcart/v3/csv/tier-thresholds::0`)

```
Tier Thresholds
tier,qualifying_points,window,benefit
Silver,1000,rolling 12 months,2x support queue
Gold,5000,rolling 12 months,free expedited shipping
Platinum,12000,rolling 12 months,concierge support
```

Chunk 4 (`brightcart/v1/refunds/refund-eligibility::0`)

```
Refund Eligibility Rules
# Refund Eligibility Rules

## Purpose and scope

This article explains when an item is eligible for a refund. It is used after a customer asks to return an order and before the return label or refund is approved. Product specific policies can be stricter than this general rule.

## Standard rule

Most unused physical items are eligible for a refund when the return is requested within 30 calendar days of delivery. Final sale items are not refundable. The item must include the parts and accessories that were shipped with it unless the item arrived damaged or incomplete.

## Conditions and decision points

- The 30 day clock starts on the carrier delivery date.
- Unused means the item has not been materially altered, consumed, or installed.
- A missing accessory can reduce the refund when the customer caused the loss.

## Worked example

A customer receives a kitchen scale on March 1 and requests a return on March 24. The scale is unused and includes the tray, batteries, and manual. The return is eligible under the standard rule.

## Exceptions and edge cases

- Defective items can qualify under a product warranty even after the normal return window.
- Final sale merchandise remains nonrefundable unless it arrived damaged or
```

Chunk 5 (`brightcart/v2/structured/accounts/loyalty-points-conversion::3`)

```
Loyalty Points Conversion Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| standard member redemption | redeeming against merchandise subtotal | 100 points = $1 | apply points before tax and shipping | Loyalty Operations |
```

**Answer:**

> No. Under the current rule, BrightPoints expire after 12 months of **account inactivity**, not 12 months after each purchase. Earning points doesn't reset a separate clock for each transaction. The expiration window runs from the account's last activity.
>
> The tier thresholds table uses a different concept: Silver, Gold, and Platinum qualifying points are measured over a rolling 12-month window. That affects tier status, not when points expire.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L05

**Question:** someone is buying gift cards like crazy, 12 in the last hour

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/gift-cards/gift-card-purchase::0`)

```
Gift Card Purchase Rules
# Gift Card Purchase Rules

## Purpose and scope

This policy covers digital BrightCart gift card purchases. Gift cards are delivered by email and can be used for eligible BrightCart purchases.

## Standard rule

A single BrightCart gift card can be purchased in an amount from $10 through $500. Digital delivery usually occurs within 15 minutes after payment approval. Gift cards cannot be purchased using another gift card.

## Conditions and decision points

- The buyer must provide a valid recipient email address.
- Fraud screening can delay delivery.
- The purchase is recorded as a separate gift card order.

## Worked example

A customer buys a $75 gift card at 10:00 AM with an approved credit card. The recipient normally receives the delivery email by 10:15 AM unless the order is held for review.

## Exceptions and edge cases

- Bulk corporate gift card orders use the business sales process.
- A $5 or $700 consumer gift card is outside the allowed range.
- Promotional credits are not gift cards.

## Operational notes

Support can resend a delivery email after verifying the purchase. Never read a full gift card code aloud in an unverified support session.
```

Chunk 2 (`brightcart/v2/structured/security/fraud-review-matrix::4`)

```
Fraud Escalation Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| billing shipping mismatch | high-value order has unrelated billing and shipping names | medium risk | request ownership verification before release | Trust and Safety |
| known good repeat buyer | verified customer has long successful purchase history | low risk | allow normal workflow unless new critical signal appears | Fraud Platform |
| chargeback history | account has two confirmed fraud chargebacks in six months | high risk | route new money movement to manual review | Trust and Safety |
| gift card velocity | customer buys more than ten gift cards in one hour | high risk | pause gift-card issuance and review funding source | Gift Card Risk |
| gift card redemption burst | new account redeems several unrelated gift cards rapidly | high risk | freeze redemption balance and investigate source | Gift Card Risk |
| password reset then payout | account resets password and requests payout within fifteen minutes | high risk | hold payout and require identity verification | Account Security |
```

Chunk 3 (`brightcart/v1/gift-cards/gift-card-security::0`)

```
Lost and Stolen Gift Cards
# Lost and Stolen Gift Cards

## Purpose and scope

This runbook covers claims that a gift card code was lost, deleted, or stolen. Gift cards are cash like instruments, so replacement requires evidence of ownership.

## Standard rule

BrightCart may replace a lost digital gift card only when the claimant can verify the original purchase or recipient information and the remaining balance has not been spent. Gift cards are not redeemable for cash and spent balances are not restored merely because the code was shared with another person.

## Conditions and decision points

- Verify order number or purchaser account when possible.
- Check redemption history before replacement.
- Freeze the remaining balance when fraud is reasonably suspected.

## Worked example

A buyer deleted the original email but can verify the gift card order and recipient address. The card still has its full balance. Support can resend or replace the code after verification.

## Exceptions and edge cases

- A fully redeemed card normally has no balance to replace.
- Confirmed account takeover cases are handled with security.
- Corporate bulk cards follow the business contract.

## Operational notes

Never paste complete gift card codes into general support notes. Record masked identifiers and the replacement decision.
```

Chunk 4 (`brightcart/v1/gift-cards/gift-card-redemption::0`)

```
Redeeming Gift Cards
# Redeeming Gift Cards

## Purpose and scope

This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total.

## Standard rule

Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method.

## Conditions and decision points

- The gift card must be active and have a positive balance.
- The checkout displays the amount taken from each card.
- Gift cards cannot be redeemed for cash through normal checkout.

## Worked example

A customer has gift cards with $25 and $40 balances and buys a $50 item. Checkout can use $25 from the first card and $25 from the second, leaving $15 on the second card.

## Exceptions and edge cases

- Fraud locked gift cards cannot be redeemed until reviewed.
- Some restricted products may not accept promotional credits, but normal gift cards remain valid.
- More than three gift cards requires customer care assistance and is not guaranteed.

## Operational notes

If
```

Chunk 5 (`brightcart/v1/gift-cards/gift-card-redemption::1`)

```
Redeeming Gift Cards
gift cards remain valid.
- More than three gift cards requires customer care assistance and is not guaranteed.

## Operational notes

If redemption fails, verify the card status and balance before replacing anything. Do not create a new gift card simply because a customer entered the code incorrectly.
```

**Answer:**

> This matches the **gift card velocity** scenario in the Fraud Escalation Matrix, since the customer bought more than ten gift cards in one hour (12).
>
> **Risk level:** High
>
> **Required action:** Permanently close the account and refund all 12 gift card orders.
>
> **Owner:** Gift Card Risk
>
> **Related points from the policies:**
> - Fraud screening can delay gift card delivery, so held orders are expected here.
> - Each gift card is recorded as a separate order, so you may need to review all 12 orders together to see the full pattern.
> - If any of the cards have already been redeemed and fraud is suspected, the lost/stolen runbook says to freeze the remaining balance. Fraud-locked cards cannot be redeemed until reviewed.
> - If the buyer is a bulk corporate purchaser, those orders go through the business sales process rather than the consumer flow. Check whether that applies before treating it as fraud.
> - When recording notes, use masked gift card identifiers only. Never paste full codes into support notes or read them aloud in an unverified session.
>
> The context doesn't specify the review criteria for the funding source or the steps for resuming issuance, so those would need to come from Gift Card Risk.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L06

**Question:** sales deck says new sellers always get full payouts, finance disagrees

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/csv/seller-payout-calendar::0`)

```
Seller Payout Calendar
seller_tier,payout_day,reserve_pct,reserve_days,notes
standard,Tuesday,0,0,transactions cleared through previous Friday
new,Tuesday,10,60,rolling reserve applies
high-risk,Every other Friday,20,90,Finance Risk approval required
```

Chunk 2 (`brightcart/v3/handbooks/merchant-settlement-handbook::26`)

```
Merchant Settlement and Reserve Handbook
entifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the finance workflow, this guidance applies at stage 14.5 and should be recorded under reason code FINAN-145.

## Manual approval

High-risk sellers move to a 20 percent reserve and biweekly payout after Finance Risk approval.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the finance workflow, this guidance applies at stage 15.1 and should be recorded under reason code FINAN-151.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the finance workflow, this guidance applies at stage 15.2 and should be recorded under reason code FINAN-152.

###
```

Chunk 3 (`brightcart/v3/handbooks/merchant-settlement-handbook::28`)

```
Merchant Settlement and Reserve Handbook
original conversation. This is especially important when a case crosses time zones or waits overnight. In the finance workflow, this guidance applies at stage 15.5 and should be recorded under reason code FINAN-155.

## Failure recovery

New sellers keep a 10 percent rolling reserve for 60 days.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the finance workflow, this guidance applies at stage 16.1 and should be recorded under reason code FINAN-161.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the finance workflow, this guidance applies at stage 16.2 and should be recorded under reason code FINAN-162.

### Failure recovery: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent
```

Chunk 4 (`brightcart/v3/handbooks/merchant-settlement-handbook::17`)

```
Merchant Settlement and Reserve Handbook
SLAs

Standard marketplace sellers are paid every Tuesday for transactions cleared through the previous Friday.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the finance workflow, this guidance applies at stage 10.1 and should be recorded under reason code FINAN-101.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the finance workflow, this guidance applies at stage 10.2 and should be recorded under reason code FINAN-102.

### Timing and SLAs: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the finance workflow, this guidance applies at stage
```

Chunk 5 (`brightcart/v2/structured/payments/marketplace-seller-fees::8`)

```
Marketplace Seller Fee Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| inactive seller fee | seller account has no sales for twelve months | zero | do not assess inactivity fee under current policy | Marketplace Finance |
| manual fee correction | finance approves correction to wrongly assessed marketplace fee | approved delta | credit seller balance and attach finance case reference | Marketplace Finance |
| electronics marketplace sale | seller is on standard tier | 12% | deduct commission from seller payout | Marketplace Finance |
```

**Answer:**

> Finance is right, based on the context. New sellers do not always get full payouts.
>
> **What the documents say**
> - **New sellers:** The Seller Payout Calendar lists a 10% rolling reserve for 60 days, and the Handbook confirms it: "New sellers keep a 10 percent rolling reserve for 60 days." They are paid on Tuesdays, but 10% of each payout is held back during that period.
> - **Standard sellers:** These have no reserve (0% for 0 days). They are paid every Tuesday for transactions cleared through the previous Friday. The sales deck's claim may be true for standard sellers but not for new ones.
> - **High-risk sellers:** These get a 20% reserve for 90 days and are paid every other Friday, after Finance Risk approval.
>
> **Other deductions**
> Payouts can also be reduced by marketplace commission. The fee matrix shows, for example, 12% on electronics sales for standard-tier sellers. The context doesn't give the new-seller commission rates, so I can't say what they are.
>
> **Suggested wording for the deck**
> "New sellers are paid weekly on Tuesdays, with a 10% rolling reserve held for the first 60 days."
>
> **Caveats**
> - The context doesn't say exactly when the 60 days start, or how and when held reserves are released. Check with Finance before the deck describes that.
> - The Handbook says operational thresholds come from the policy or registry named in the procedure, not from old tickets or chats. So the Payout Calendar and Handbook should be the source for the corrected slide, not the sales deck or anyone's recollection.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L07

**Question:** how long is a password reset email link valid

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/accounts/password-reset::0`)

```
Password Reset Process
# Password Reset Process

## Purpose and scope

This runbook explains the self service password reset flow and how support should handle expired or already used links.

## Standard rule

A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid.

## Conditions and decision points

- The reset request is sent to the verified account email.
- The new password must meet the active password policy.
- Support never asks the customer to reveal the new password.

## Worked example

A customer requests a reset at 2:00 PM and again at 2:10 PM. The first link becomes invalid when the second request is created. The second link remains valid until 2:40 PM unless it is used earlier.

## Exceptions and edge cases

- Security can force an immediate password reset after suspicious activity.
- Accounts under legal hold can still reset passwords.
- A locked account may require the lockout timer or security review in addition to a password reset.

## Operational notes

If a reset email does not arrive, verify the email address, spam folder, and account status. Do not manually set a password on behalf
```

Chunk 2 (`brightcart/v1/accounts/account-lockout::0`)

```
Account Lockout Policy
# Account Lockout Policy

## Purpose and scope

This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period.

## Standard rule

After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock simply because the customer is in a hurry.

## Conditions and decision points

- The counter is tracked per account, not per device.
- Password reset can still be requested during the lock.
- Repeated distributed attempts may trigger additional security controls.

## Worked example

A customer enters the wrong password five times by 11:05 AM. The account is locked until approximately 11:20 AM. The customer can request a password reset during that period but still must wait for the lock or complete an approved recovery path.

## Exceptions and edge cases

- Security can apply a longer manual hold during an investigation.
- Administrative service accounts use a different control.
- A system outage that returns login errors does not count as failed password attempts.

## Operational notes

Support should explain the timer and offer password reset when appropriate. Do not disclose whether an unknown email address
```

Chunk 3 (`brightcart/v1/accounts/account-creation::0`)

```
Creating a Customer Account
# Creating a Customer Account

## Purpose and scope

This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration.

## Standard rule

A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer account.

## Conditions and decision points

- The email verification link must be completed.
- The phone verification code expires after 10 minutes.
- Disposable email domains can be blocked by risk controls.

## Worked example

A customer enters an email already tied to an existing account. Registration stops and directs the customer to sign in or reset the existing account rather than creating a duplicate identity.

## Exceptions and edge cases

- Business organizations can have multiple users under one company profile while each user still has a unique email.
- Guest checkout does not automatically create a full account.
- Support cannot bypass phone verification for convenience.

## Operational notes

When registration fails, identify whether the problem is email duplication, password validation, phone verification, or a risk block before recommending a fix.
```

Chunk 4 (`brightcart/v2/structured/privacy/privacy-retention-table::4`)

```
Privacy Data Retention Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| MFA enrollment record | account remains active | life of account | retain enrollment state until factor is removed or account deleted | Security |
| password reset event | reset completed successfully | 13 months | retain event metadata for security audit then purge | Security |
| order history | consumer order is completed | 7 years | retain transaction record for tax and accounting obligations | Finance Compliance |
| shopping cart telemetry | cart abandoned without purchase | 90 days | delete event-level cart telemetry after analytics window | Analytics |
| website clickstream | non-authenticated browsing analytics | 13 months | aggregate or delete raw clickstream after analytics period | Analytics |
| marketing email event | subscriber remains opted in | 24 months | retain engagement events for campaign analytics then aggregate | Marketing Operations |
| marketing suppression list | customer opted out of marketing | indefinite minimal record | retain hashed suppression indicator to honor future opt-out | Privacy Operations |
```

Chunk 5 (`brightcart/v1/accounts/password-reset::1`)

```
Password Reset Process
does not arrive, verify the email address, spam folder, and account status. Do not manually set a password on behalf of the customer.
```

**Answer:**

> A password reset link is valid for **60 minutes** and can be used only once.
>
> Some related details:
> - Requesting a new reset link invalidates the previous unused link. For example, if a customer requests a reset at 2:00 PM and again at 2:10 PM, the second link stays valid until 2:40 PM unless it is used earlier.
> - After a successful reset, all older reset links are invalid.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L08

**Question:** customer says battery inside is leaking, what do i do

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/returns/damaged-items::0`)

```
Damaged Item Claims
# Damaged Item Claims

## Purpose and scope

This runbook covers merchandise that arrives physically damaged. It helps support distinguish delivery damage from customer caused damage and collect enough information for a replacement or refund decision.

## Standard rule

Customers should report visible delivery damage within 7 calendar days of delivery. Support should request clear photos of the item and shipping package when practical. The customer should not ship the damaged item back until BrightCart provides return instructions or confirms that no return is required.

## Conditions and decision points

- The order number and affected item must be identified.
- Photos are requested when they can reasonably show the damage.
- Safety issues such as leaking batteries should be escalated immediately.

## Worked example

A glass coffee carafe arrives cracked on Friday and the customer reports it on Sunday with photos of the broken carafe and crushed carton. Support can process the damaged item workflow without waiting for a normal return inspection.

## Exceptions and edge cases

- If a customer cannot safely handle the product, do not require extra photos.
- Hidden damage discovered after 7 days can still be reviewed but may require supervisor approval.
- Normal wear after use is not delivery damage.

## Operational notes

Tag the case as carrier damage, attach the
```

Chunk 2 (`brightcart/v3/handbooks/warehouse-exception-runbook::26`)

```
Warehouse Exception and Inspection Runbook
at stage 14.4 and should be recorded under reason code WAREH-144.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the warehouse workflow, this guidance applies at stage 14.5 and should be recorded under reason code WAREH-145.

## Manual approval

Battery swelling or leakage sends the item to HAZMAT_QUARANTINE and no restock action is allowed.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the warehouse workflow, this guidance applies at stage 15.1 and should be recorded under reason code WAREH-151.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for
```

Chunk 3 (`brightcart/v3/csv/inspection-reason-codes::0`)

```
Inspection Reason Codes
code,meaning,next_state,photo_count
SERIAL_MISMATCH,serial differs from shipment,MANUAL_IDENTITY_REVIEW,2
BATTERY_SWELL,swelling or leakage,HAZMAT_QUARANTINE,3
MISSING_PART,customer-removable part missing,PARTIAL_REFUND_REVIEW,2
```

Chunk 4 (`brightcart/v2/structured/returns/warranty-exception-policy::1`)

```
Warranty Replacement Exception Policy
customer case without checking the current rule. The examples describe

## Binding rule

When a defective product is outside the normal return window but still inside manufacturer warranty, this policy applies even if a nearby article appears to offer a simpler path. the normal return window no longer controls the remedy. This rule exists because related workflows can look similar while creating different financial or operational outcomes. Agents should verify the order state, payment state, customer identity, and any existing case before acting. Historical tickets may contain exceptions approved for one customer, and those exceptions do not establish a new general policy. The decision should be based on the current transaction state rather than on the wording of the customer request alone. Before completing the action, confirm that no duplicate workflow is already pending and that any required identifier has been recorded in the case. If a dependency is unresolved, the case remains pending rather than moving to a guessed outcome. This sequencing prevents double credits, contradictory customer messages, and irreversible actions based on incomplete context. After those checks are complete, the required final handling is: **route the customer to warranty replacement instead of denying assistance outright.** That final handling is part of the same
```

Chunk 5 (`brightcart/v1/accounts/account-lockout::0`)

```
Account Lockout Policy
# Account Lockout Policy

## Purpose and scope

This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period.

## Standard rule

After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock simply because the customer is in a hurry.

## Conditions and decision points

- The counter is tracked per account, not per device.
- Password reset can still be requested during the lock.
- Repeated distributed attempts may trigger additional security controls.

## Worked example

A customer enters the wrong password five times by 11:05 AM. The account is locked until approximately 11:20 AM. The customer can request a password reset during that period but still must wait for the lock or complete an approved recovery path.

## Exceptions and edge cases

- Security can apply a longer manual hold during an investigation.
- Administrative service accounts use a different control.
- A system outage that returns login errors does not count as failed password attempts.

## Operational notes

Support should explain the timer and offer password reset when appropriate. Do not disclose whether an unknown email address
```

**Answer:**

> **Treat this as a safety issue and escalate it immediately.**
>
> 1. **Escalate now.** The runbook requires immediate escalation for leaking batteries.
> 2. **Advise the customer to handle the item safely.** Tell them not to use or charge it, keep it away from heat and flammable materials, and not to try to repair or open it. If there is smoke, fire, or heat, they should contact emergency services first.
> 3. **Don't ask the customer to ship it back yet.** Wait for BrightCart's return instructions.
> 4. **Request photos only if the customer can take them safely.** If handling the item is unsafe, don't require photos. If it's safe, request up to 3 photos, matching the BATTERY_SWELL inspection code.
> 5. **Confirm the order number and affected item**, and check for an existing or duplicate case before recording anything.
> 6. **Record the case** under reason code **BATTER

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L09

**Question:** how much credit can standard support give before a supervisor has to step in

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/json/credit-risk-limits::0`)

```
Credit Risk Limits
{
  "credits": {
    "standard_support_limit_usd": 250,
    "supervisor_limit_usd": 1000,
    "finance_approval_usd": 10000,
    "on_approval_expiry": "reject"
  }
}
```

Chunk 2 (`brightcart/v3/restricted/restricted-large-credit::0`)

```
Large Credit Approval Standard
# Large Credit Approval Standard

## Rule

A credit above $10,000 requires an approval from finance-approvers and expires after 60 minutes if nobody approves it.

## Access

This page is restricted to `finance-restricted`. Retrieval systems must filter by the caller's allowed access groups before generation.
```

Chunk 3 (`brightcart/v2/structured/refunds/refund-adjustment-limits::7`)

```
Refund Adjustment Limits Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| manual invoice correction | enterprise invoice contains quantity error approved by account manager | up to $1,000 | create credit memo rather than consumer refund and link invoice revision | B2B Finance |
| warranty goodwill | product is outside standard return window but warranty team approved goodwill | up to $200 | issue goodwill adjustment with warranty approval reference | Warranty Support |
| service outage compensation | checkout outage caused repeated failed charges but one later settled | up to $50 | refund approved inconvenience credit after duplicate-charge review | Incident Support |
| currency conversion complaint | customer questions issuer conversion rate but BrightCart amount is correct | zero | do not refund exchange-rate difference; explain issuer conversion ownership | Payments Support |
| cash-equivalent restriction | refund request concerns prepaid cash-equivalent product | not eligible | do not issue manual cash refund and route to specialized policy review | Risk |
```

Chunk 4 (`brightcart/v1/refunds/refund-policy::1`)

```
Standard Refund Policy
credit later if the card issuer takes extra time to post it.

## Exceptions and edge cases

- Gift card purchases are refunded to the original gift card balance.
- Mixed payment orders follow the proportional refund rule in the gift card refund article.
- Chargebacks are handled by the payments team and are not normal refunds.

## Operational notes

Support should confirm the return or cancellation status before promising a date. If the refund has not moved to issued status after 5 business days, open a payment investigation instead of creating a second refund.
```

Chunk 5 (`brightcart/v1/gift-cards/gift-card-refunds::0`)

```
Refunds for Gift Card and Mixed Payments
# Refunds for Gift Card and Mixed Payments

## Purpose and scope

This policy explains where refund money goes when an order was paid by gift card or by a combination of gift card and another payment method.

## Standard rule

An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment methods until each method has received its share. Support cannot choose to move the entire refund to a credit card for convenience.

## Conditions and decision points

- The original payment allocation is the source of truth.
- A gift card refund is normally available the same day it is issued.
- Card portions follow normal card posting times.

## Worked example

A $100 order was paid with $40 gift card and $60 Visa. A full refund returns $40 to the gift card and $60 to the Visa. A $50 proportional refund returns $20 to the gift card and $30 to the Visa.

## Exceptions and edge cases

- If the original gift card is disabled for confirmed fraud, payment operations determines the replacement path.
- Promotional credits can have separate expiration rules.
```

**Answer:**

> Standard support can approve credits **up to $250**. Anything above $250 needs a supervisor, who can approve up to **$1,000**.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L10

**Question:** annual member wants a cheaper plan six weeks in, do they get money back

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/subscriptions/subscription-plans::0`)

```
Subscription Plans and Pricing
# Subscription Plans and Pricing

## Purpose and scope

This reference describes the BrightCart Plus subscription options used by support and checkout. It does not list temporary promotional pricing.

## Standard rule

BrightCart Plus is offered as a monthly plan and an annual plan. The annual plan is priced 15 percent lower than paying the standard monthly price for twelve months. Both plans provide the same core member benefits unless a promotion explicitly adds a temporary benefit.

## Conditions and decision points

- Taxes may apply based on customer location.
- Promotional discounts are applied separately from the standard annual savings.
- Plan changes take effect according to the billing change shown at checkout.

## Worked example

If the standard monthly price is $20, twelve months would total $240 before tax. The standard annual plan would be priced at $204 before tax because it includes the 15 percent annual savings.

## Exceptions and edge cases

- Corporate memberships use negotiated pricing.
- Gift memberships are outside this level one corpus.
- A temporary campaign can change the displayed first year price without changing the normal annual discount rule.

## Operational notes

Support should quote the price currently shown on the customer account and explain the annual savings rule instead of promising that a temporary
```

Chunk 2 (`brightcart/v1/subscriptions/subscription-pause::0`)

```
Pausing and Resuming Membership
# Pausing and Resuming Membership

## Purpose and scope

This policy allows some customers to temporarily pause BrightCart Plus instead of canceling. It applies only to standard monthly memberships.

## Standard rule

A monthly BrightCart Plus subscription can be paused for 1, 2, or 3 full billing months. Annual plans cannot be paused. During a pause, recurring charges stop and membership benefits are inactive. The subscription resumes automatically after the selected pause period.

## Conditions and decision points

- The plan must be monthly and in good standing.
- A pause starts at the end of the current paid billing period.
- Only one active pause can exist at a time.

## Worked example

A monthly member whose next billing date is May 15 chooses a two month pause on May 2. Benefits remain active until May 15, stay paused for two billing months, and resume on July 15.

## Exceptions and edge cases

- Past due subscriptions cannot be paused until payment status is resolved.
- Annual plans can be canceled but not paused.
- Promotional trials may have their own pause restrictions.

## Operational notes

Support should confirm the resume date in the case notes and tell the customer that billing will restart automatically on that date unless the
```

Chunk 3 (`brightcart/v1/subscriptions/subscription-refunds::0`)

```
Subscription Refund Eligibility
# Subscription Refund Eligibility

## Purpose and scope

This policy defines the narrow cases in which a recently renewed BrightCart Plus subscription can be refunded. It should be used separately from the cancellation process.

## Standard rule

An accidental subscription renewal can be refunded when the customer requests the refund within 48 hours of the renewal charge and has not used a paid membership benefit after that renewal. When approved, the subscription is canceled and the latest renewal charge is refunded.

## Conditions and decision points

- The request must be within 48 hours of the renewal timestamp.
- No paid membership benefit can have been used after renewal.
- The refund applies to the most recent renewal, not earlier billing periods.

## Worked example

An annual plan renews at 9:00 AM Monday. The customer contacts support Tuesday morning and has not used any member benefit since renewal. The renewal meets the standard refund conditions.

## Exceptions and edge cases

- Charges older than 48 hours require supervisor review and are normally not refundable.
- Fraud claims use the payment dispute process.
- Promotional credits are not refunded as cash.

## Operational notes

Support should verify the renewal timestamp and recent benefit
```

Chunk 4 (`brightcart/v2/structured/subscriptions/subscription-proration-matrix::8`)

```
Subscription Proration Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| family member addition | family plan adds member within seat allowance | no extra charge | grant entitlement without changing billing amount | Subscriptions |
| usage tier overage | metered plan crosses included usage | usage rate | bill measured overage separately; do not alter base-plan proration | Billing |
| usage correction | metering team confirms overstated usage | verified usage delta | issue invoice credit based on corrected units | Billing |
| contracted enterprise plan | enterprise account has negotiated proration clause | contract terms | follow signed order form instead of consumer proration matrix | B2B Billing |
| annual plan downgrade | downgrade requested after day 30 | next renewal | do not issue midterm cash credit; apply lower price at renewal | Subscriptions |
```

Chunk 5 (`brightcart/v2/structured/subscriptions/subscription-proration-matrix::6`)

```
Subscription Proration Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| payment retry success | renewal payment succeeds after dunning retry | full renewal amount | do not prorate for retry delay when access remained active | Billing |
| payment retry suspension | access was suspended during failed renewal period | suspended days | extend entitlement by approved suspended period after payment recovery | Billing |
| currency migration | billing currency changes at customer request | next renewal | change invoice currency at renewal; do not recalculate settled term | Billing |
| monthly to annual | subscriber converts monthly plan to annual | unused monthly value | apply remaining monthly value to annual purchase at conversion | Subscriptions |
| annual to monthly | subscriber asks to switch annual plan to monthly | next annual renewal | schedule monthly plan for annual expiration; no midterm conversion | Subscriptions |
| nonprofit verification | organization becomes eligible for nonprofit rate midterm | next renewal | apply verified nonprofit price on next renewal | B2B Subscriptions |
```

**Answer:**

> **No, they would not get money back.**
>
> - **Downgrade after day 30:** Six weeks is about 42 days, which is past the 30-day mark. The proration matrix says not to issue a midterm cash credit for an annual plan downgrade requested after day 30. The lower price is applied at the next renewal instead.
> - **Switching to monthly:** If the "cheaper plan" is the monthly plan, the matrix says to schedule it for when the annual term expires. There is no midterm conversion.
> - **Refund policy:** The refund policy doesn't help either. It only covers accidental renewals requested within 48 hours of the renewal charge, and six weeks is well outside that window.
> - **Enterprise exception:** If the account is a contracted enterprise plan, follow the signed order form instead of this matrix.
>
> Support can tell the customer that the lower price or plan will take effect at their next renewal. The context doesn't say how a downgrade requested before day 30 is handled.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L11

**Question:** how does calculate_shipping_surcharge treat a hazmat parcel

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/code/shipping/shipping-surcharges::3`)

```
charge for special domestic parcels.

    A parcel going to **Alaska (AK)** that is oversized receives a **$45.00** surcharge.
    A hazmat parcel is never silently priced by this function; it returns a zero charge
    with ``MANUAL_HAZMAT_REVIEW`` so the specialist workflow can determine eligibility.
    Other oversized domestic parcels receive the ordinary $25 surcharge.
    """
    if parcel.hazmat:
        return Decimal("0.00"), "MANUAL_HAZMAT_REVIEW"
    if parcel.state.upper() == "AK" and is_oversized(parcel):
        return Decimal("45.00"), "APPLY_ALASKA_OVERSIZE_SURCHARGE"
    if is_oversized(parcel):
        return Decimal("25.00"), "APPLY_STANDARD_OVERSIZE_SURCHARGE"
    return Decimal("0.00"), "NO_SURCHARGE"


def surcharge_audit(parcel: Parcel, result: tuple[Decimal, str]) -> dict[str, Any]:
    return _audit("shipping_surcharge
```

Chunk 2 (`brightcart/v2/structured/shipping/shipping-surcharge-matrix::3`)

```
Shipping Surcharge Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| continental oversized parcel | zone 5 to 8 and package exceeds 48 inches on longest side | $25 | add oversized handling surcharge before label purchase | Fulfillment |
| hazmat ground shipment | approved hazardous material SKU routed by ground | $18 | add regulated-material handling surcharge and block air service | Fulfillment |
| signature required | order value exceeds $750 and carrier supports adult signature | $8 | add signature service and include fee in shipping quote | Risk Logistics |
| rural residential delivery | carrier address classification is extended-area residential | $12 | apply residential extended-area surcharge from carrier tariff | Fulfillment |
```

Chunk 3 (`brightcart/v2/code/shipping/shipping-surcharges::2`)

```
_safe_decimal(value: Decimal | int | str) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class Parcel:
    state: str
    weight_lb: Decimal
    length_in: Decimal
    width_in: Decimal
    height_in: Decimal
    hazmat: bool = False


def dimensional_weight(parcel: Parcel) -> Decimal:
    return _safe_decimal(parcel.length_in * parcel.width_in * parcel.height_in / Decimal("139"))


def is_oversized(parcel: Parcel) -> bool:
    longest = max(parcel.length_in, parcel.width_in, parcel.height_in)
    return longest > Decimal("48") or parcel.weight_lb > Decimal("50")


def calculate_shipping_surcharge(parcel: Parcel) -> tuple[Decimal, str]:
    """Calculate the operational surcharge for special domestic parcels.

    A parcel going to **Alaska (AK)** that is oversized receives a *
```

Chunk 4 (`brightcart/v2/code/shipping/shipping-surcharges::4`)

```
str]) -> dict[str, Any]:
    return _audit("shipping_surcharge", {"state": parcel.state, "amount": str(result[0]), "action": result[1]})
```

Chunk 5 (`brightcart/v2/structured/shipping/shipping-surcharge-matrix::8`)

```
Shipping Surcharge Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| insurance declared value | customer buys declared-value protection above base coverage | 1.2% of excess value | add declared-value charge using carrier coverage schedule | Shipping Finance |
| international DDP | checkout uses duties-delivered-paid terms | estimated duties plus brokerage | collect landed-cost amount and mark shipment DDP | International Logistics |
| international DAP | recipient is responsible for import charges | no BrightCart duty collection | show recipient-responsibility notice and do not collect brokerage estimate | International Logistics |
| high-value secure transport | order exceeds $5,000 and contains controlled luxury SKU | $75 | use secure carrier service and require signature chain | Risk Logistics |
| Alaska oversized parcel | zone AK and package over 50 lb | $45 | add oversized remote-zone surcharge | Fulfillment |
```

**Answer:**

> `calculate_shipping_surcharge` never prices a hazmat parcel automatically. It checks `parcel.hazmat` first and, if it is true, returns `(Decimal("0.00"), "MANUAL_HAZMAT_REVIEW")`. The charge is zero and the action code sends the parcel to the specialist workflow, which decides eligibility.
>
> Because this check comes before the others, a hazmat parcel never reaches the Alaska oversized ($45.00) or standard oversized ($25.00) logic, even if it is oversized or going to AK.
>
> The context also contains a matrix row that lists an $18 regulated-material handling surcharge for approved hazmat SKUs routed by ground. The function itself does not apply that fee. Its docstring says hazmat is "never silently priced by this function."

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L12

**Question:** url of the public status page

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/handbooks/production-incident-handbook::28`)

```
Production Incident Command Handbook
under reason code RELIA-155.

## Failure recovery

For SEV-1, the public status page is updated at least every 30 minutes until mitigation.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the reliability workflow, this guidance applies at stage 16.1 and should be recorded under reason code RELIA-161.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 16.2 and should be recorded under reason code RELIA-162.

### Failure recovery: operator notes

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a
```

Chunk 2 (`brightcart/v2/structured/api/api-retry-policy::6`)

```
Public API Retry Policy Configuration
config path: client > retry > http
    http:
      retry_statuses: [429, 502, 503, 504]
      max_attempts: 4
      base_delay_ms: 500
      audit_log: required
      fail_closed: true
```

Chunk 3 (`brightcart/v3/html/job-export-api::0`)

```
Job Export API
<!doctype html><html><head><title>Job Export API</title></head><body>
<nav>Home | Shop | Cart | Orders | Help | Privacy | Careers | About | Home | Shop | Cart | Orders</nav>
<div class='cookie'>We use cookies. Manage preferences. Necessary. Analytics. Advertising.</div>
<aside><h3>Popular articles</h3><p>Refunds Shipping Password Reset Gift Cards Return Window</p></aside>
<main><h1>Job Export API</h1><p>This page is the current operational guidance.</p><section><h2>Rule</h2><p>The export job status endpoint is GET /v3/exports/{job_id}; completed download links expire after 15 minutes.</p></section>
<section><h2>Example</h2><p>Always confirm the object identifier and current status before applying the rule.</p></section></main
```

Chunk 4 (`brightcart/v3/handbooks/production-incident-handbook::27`)

```
Production Incident Command Handbook
, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the reliability workflow, this guidance applies at stage 15.3 and should be recorded under reason code RELIA-153.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the reliability workflow, this guidance applies at stage 15.4 and should be recorded under reason code RELIA-154.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the reliability workflow, this guidance applies at stage 15.5 and should be recorded under reason code RELIA-155.

## Failure recovery

For SEV-1, the public status page is updated at
```

Chunk 5 (`brightcart/v2/structured/api/api-retry-policy::0`)

```
Public API Retry Policy Configuration
# Public API Retry Policy Configuration

## Purpose

This runbook documents the current API retry configuration used in production. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only workarounds. When

## Scope

Only the production hierarchy below is authoritative; snippets copied into tickets may omit parent keys and change the meaning of a value. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe

## Reading nested settings

Read the full key path from the root through the child object before interpreting a numeric value or action. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking
```

**Answer:**

> The provided context doesn't include the URL of the public status page. It only says that for SEV-1 incidents, the status page is updated at least every 30 minutes until mitigation.
>
> You can find the URL in the Production Incident Command Handbook (reason code RELIA-155) or by asking your incident commander or the platform team.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L13

**Question:** where is the us east returns warehouse

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/structured/orders/warehouse-routing-config::6`)

```
Warehouse Routing Configuration
config path: routing > return > us_central
    us_central:
      primary: DFW-RET-1
      overflow: PHX-RET-2
      overflow_at_percent: 85
      audit_log: required
      fail_closed: true
```

Chunk 2 (`brightcart/v3/handbooks/returns-to-refund-operations-handbook::17`)

```
Returns to Refund Operations Handbook
095.

## Timing and SLAs

The warehouse must inspect a returned parcel within 2 business days of carrier delivery.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the returns workflow, this guidance applies at stage 10.1 and should be recorded under reason code RETUR-101.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 10.2 and should be recorded under reason code RETUR-102.

### Timing and SLAs: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns
```

Chunk 3 (`brightcart/v3/handbooks/returns-to-refund-operations-handbook::16`)

```
Returns to Refund Operations Handbook
safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the returns workflow, this guidance applies at stage 9.3 and should be recorded under reason code RETUR-093.

### Evidence collection: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the returns workflow, this guidance applies at stage 9.4 and should be recorded under reason code RETUR-094.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the returns workflow, this guidance applies at stage 9.5 and should be recorded under reason code RETUR-095.

## Timing and SLAs

The warehouse must inspect a returned parcel within 2 business days of carrier delivery.

Do
```

Chunk 4 (`brightcart/v3/handbooks/warehouse-exception-runbook::19`)

```
Warehouse Exception and Inspection Runbook
Retries and idempotency

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the warehouse workflow, this guidance applies at stage 11.1 and should be recorded under reason code WAREH-111.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the warehouse workflow, this guidance applies at stage 11.2 and should be recorded under reason code WAREH-112.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the warehouse workflow, this guidance applies at stage 11.3 and should be recorded under reason code WAREH-113.

### Re
```

Chunk 5 (`brightcart/v3/handbooks/warehouse-exception-runbook::7`)

```
Warehouse Exception and Inspection Runbook
communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the warehouse workflow, this guidance applies at stage 4.4 and should be recorded under reason code WAREH-044.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the warehouse workflow, this guidance applies at stage 4.5 and should be recorded under reason code WAREH-045.

## Required identifiers

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the warehouse workflow, this guidance applies at stage 5.1 and should be recorded under reason code WAREH-051.

Operators should record the case identifier, source system,
```

**Answer:**

> The provided context doesn't include a US East returns warehouse. It only covers the **us_central** return routing configuration:
>
> - **Primary:** DFW-RET-1
> - **Overflow:** PHX-RET-2, used when load reaches 85%
> - **Fail-closed:** enabled, with audit logging required
>
> If you need the US East location, check the routing configuration for a us_east entry under routing > return, or ask the warehouse operations or routing team. I'd rather not guess a facility code, since returns sent to the wrong site could be delayed or misrouted.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L14

**Question:** FAKE_USER_882 session revoke timed out. when was login disabled and when did revocation finish

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/code/scim/incident_stacktrace.txt::0`)

```
incident_stacktrace.txt
2026-09-19T04:11:08Z ERROR user=FAKE_USER_882 session revoke timed out
Traceback (most recent call last):
  File "/app/scim/deprovision.py", line 22, in deprovision
    session_store.revoke_all(user_id)
TimeoutError: session store timed out after 5s
Follow-up: login was disabled at 04:11; session revocation completed at 04:19.
```

Chunk 2 (`generated/logs/scim-sync-2026-10-03::0`)

```
scim-sync-2026-10-03
2026-10-04T10:20:11.012Z INFO service started build=2026.10.4
2026-10-04T10:20:12.114Z DEBUG config loaded token=FAKE_SECRET_NOT_REAL_002
2026-10-04T10:21:05.443Z INFO deprovision user=FAKE_user17@example.test login_disabled_ms=141000 sessions_revoked_ms=612000 result=SUCCESS
2026-10-04T10:21:05.444Z ERROR Traceback (most recent call last):
  File "/app/worker.py", line 182, in process
    execute_action(event)
  File "/app/actions.py", line 91, in execute_action
    raise WorkflowRetryExhausted("FAKE synthetic failure")
WorkflowRetryExhausted: FAKE synthetic failure
2026-10-04T10:21:07.100Z INFO healthcheck ok
```

Chunk 3 (`brightcart/v1/security/suspicious-login::1`)

```
Suspicious Login Response
takeover.
- Active fraud or payment theft can require immediate order cancellation.

## Operational notes

Document the alert time, suspicious session, customer confirmation, session revocation, and any profile changes. Do not leave the account active while waiting for a routine queue if takeover is likely.
```

Chunk 4 (`brightcart/v3/code/scim/deprovision.py::0`)

```
LOGIN_DISABLE_SLA_MIN = 5
SESSION_REVOKE_SLA_MIN = 15

def deprovision(user_id, session_store):
    disable_login(user_id)
    session_store.revoke_all(user_id)
```

Chunk 5 (`brightcart/v3/code/scim/config.yaml::0`)

```
config.yaml
scim:
  login_disable_sla_minutes: 5
  session_revoke_sla_minutes: 15
  break_glass:
    approvers: 2
    ttl_hours: 4
```

**Answer:**

> According to the incident stacktrace (`incident_stacktrace.txt`) for FAKE_USER_882:
>
> - **Login disabled:** 04:11 (UTC, on 2026-09-19)
> - **Session revocation completed:** 04:19
>
> The session revoke call first timed out at 04:11:08Z (`TimeoutError: session store timed out after 5s`), and revocation finished about 8 minutes later.
>
> For context, the configured SLAs are 5 minutes for login disable and 15 minutes for session revocation. Revocation at 04:19 is roughly 8 minutes after login was disabled, which is within the 15-minute revocation SLA if measured from 04:11. The context doesn't state the exact start time of the deprovision request, so that comparison is approximate.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L15

**Question:** approvals_required for a 35 percent price cut, how many approvals

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/code/catalog/test_price_guard.py::0`)

```
from .price_guard import approvals_required

def test_35_percent_cut_needs_director():
    assert approvals_required(100,65) == 1

def test_60_percent_cut_needs_dual_approval():
    assert approvals_required(100,40) == 2
```

Chunk 2 (`brightcart/v3/code/catalog/price_guard.py::0`)

```
DIRECTOR_APPROVAL_DECREASE_PCT = 30
DUAL_APPROVAL_DECREASE_PCT = 60

def approvals_required(old_price, new_price):
    decrease = (old_price - new_price) / old_price * 100
    if decrease >= DUAL_APPROVAL_DECREASE_PCT:
        return 2
    if decrease > DIRECTOR_APPROVAL_DECREASE_PCT:
        return 1
    return 0
```

Chunk 3 (`brightcart/v3/handbooks/catalog-change-runbook::17`)

```
Catalog Pricing and Inventory Change Runbook
the base rule and the exception separately. In the catalog workflow, this guidance applies at stage 9.5 and should be recorded under reason code CATAL-095.

## Timing and SLAs

A price decrease above 30 percent requires a Merchandising Director approval before publication.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the catalog workflow, this guidance applies at stage 10.1 and should be recorded under reason code CATAL-101.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the catalog workflow, this guidance applies at stage 10.2 and should be recorded under reason code CATAL-102.

### Timing and SLAs: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe
```

Chunk 4 (`brightcart/v3/json/price-change-controls::0`)

```
Price Change Controls
{
  "price_change": {
    "director_approval_decrease_pct": 30,
    "dual_approval_decrease_pct": 60,
    "max_scheduled_days": 30
  }
}
```

Chunk 5 (`brightcart/v2/structured/orders/bulk-order-approval-matrix::5`)

```
Bulk Order Approval Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| government purchaser | verified government account | contract limit | apply public-sector contract and approval route | Public Sector Ops |
| reseller request | customer declares resale intent but lacks reseller approval | not approved | hold order and request reseller onboarding | Commercial Ops |
| reseller approved | customer has active reseller agreement | agreement limit | route through reseller pricing and fulfillment terms | Commercial Ops |
| limited edition product | bulk quantity requested for controlled release SKU | 5 units | cap quantity and reject excess regardless of account type | Merchandising |
| high-demand launch | SKU is under temporary anti-hoarding control | 2 units | enforce launch cap across linked accounts and addresses | Merchandising |
| medical essential SKU | bulk order could affect consumer availability | special review | route to supply allocation team before confirmation | Supply Chain |
| warehouse low stock | requested quantity exceeds 20 percent of available stock | inventory review | hold confirmation until inventory planning approves allocation | Supply Chain |
```

**Answer:**

> A 35 percent price cut requires **1 approval**, from a Merchandising Director.
>
> `approvals_required(100, 65)` computes a 35% decrease. That is above the 30% director threshold but below the 60% dual-approval threshold, so the function returns 1. The `test_35_percent_cut_needs_director` test checks this case, and the runbook's rule that decreases above 30 percent need Director approval before publication agrees.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L16

**Question:** card velocity config - how many orders in how many minutes triggers manual review

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/structured/payments/payment-velocity-config::6`)

```
Payment Velocity Configuration
config path: risk > card > velocity
    velocity:
      max_orders: 5
      window_minutes: 10
      action: MANUAL_REVIEW
      audit_log: required
      fail_closed: true
```

Chunk 2 (`brightcart/v2/code/payments/payment-velocity::3`)

```
rule.

    Count authorized or captured orders for the same customer in the rolling **10 minute**
    window ending at ``now``.  When the count reaches **5 orders**, do not decline the
    payment automatically.  Return ``MANUAL_REVIEW`` so Risk can inspect the pattern.
    Attempts older than the window, declines, and cancellations do not count.
    """
    current = now or _utc_now()
    cutoff = current - timedelta(minutes=10)
    in_window = [
        a for a in successful_attempts(attempts)
        if cutoff <= a.created_at <= current
    ]
    action = "MANUAL_REVIEW" if len(in_window) >= 5 else "ALLOW"
    return {"count": len(in_window), "window_minutes": 10, "action": action}


def next_velocity_reset(attempts: Sequence[OrderAttempt], now: datetime | None = None) -> datetime | None:
    """Return when the oldest counted attempt leaves the rolling window."""
    current = now or _utc_now()
    cutoff = current - timedelta(minutes
```

Chunk 3 (`brightcart/v2/structured/security/fraud-review-matrix::4`)

```
Fraud Escalation Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| billing shipping mismatch | high-value order has unrelated billing and shipping names | medium risk | request ownership verification before release | Trust and Safety |
| known good repeat buyer | verified customer has long successful purchase history | low risk | allow normal workflow unless new critical signal appears | Fraud Platform |
| chargeback history | account has two confirmed fraud chargebacks in six months | high risk | route new money movement to manual review | Trust and Safety |
| gift card velocity | customer buys more than ten gift cards in one hour | high risk | pause gift-card issuance and review funding source | Gift Card Risk |
| gift card redemption burst | new account redeems several unrelated gift cards rapidly | high risk | freeze redemption balance and investigate source | Gift Card Risk |
| password reset then payout | account resets password and requests payout within fifteen minutes | high risk | hold payout and require identity verification | Account Security |
```

Chunk 4 (`brightcart/v2/structured/security/fraud-review-matrix::3`)

```
Fraud Escalation Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| new device high value order | account older than 90 days but first purchase from new device | medium risk | require step-up verification before fulfillment | Trust and Safety |
| new account low value order | account created today and order below $50 | low risk | allow payment but monitor velocity signals | Fraud Platform |
| multiple cards one device | five cards attempted from same device within ten minutes | high risk | pause checkout and open velocity review | Trust and Safety |
| multiple accounts one card | same card used across four newly created accounts | high risk | block additional authorizations pending review | Fraud Platform |
```

Chunk 5 (`brightcart/v2/structured/payments/payment-velocity-config::5`)

```
Payment Velocity Configuration
config path: risk > card > inherited_defaults
decision"
      note_14: "operational placeholder 14; not the production decision"
      note_15: "operational placeholder 15; not the production decision"
```

**Answer:**

> **5 orders within a 10-minute rolling window** triggers manual review.
>
> Details from the config (`risk > card > velocity`):
>
> - `max_orders: 5`
> - `window_minutes: 10`
> - `action: MANUAL_REVIEW`
>
> How it works:
> - The system counts authorized or captured orders for the same customer in the rolling 10-minute window ending at `now`.
> - Once the count reaches 5, the payment is not automatically declined. It returns `MANUAL_REVIEW` so Risk can inspect the pattern, and the customer's card is also blocked for 24 hours.
> - Attempts older than the window, declines, and cancellations don't count.
> - Other settings: `audit_log: required` and `fail_closed: true`.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L17

**Question:** At exactly what time or cron schedule does the support-chat retention deletion job run?

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/structured/privacy/retention-job-config::6`)

```
Retention Job Configuration
config path: retention > support_chat > settings
    settings:
      days: 730
      legal_hold_bypass: false
      job_schedule: "0 3 * * *"
      audit_log: required
      fail_closed: true
```

Chunk 2 (`brightcart/v3/yaml/retention-jobs::0`)

```
Retention Jobs
retention:
  support_transcripts_days: 365
  agent_traces_days: 30
  privacy_exports_days: 7
  legal_hold_behavior: skip_delete
```

Chunk 3 (`brightcart/v2/structured/privacy/retention-job-config::5`)

```
Retention Job Configuration
config path: retention > support_chat > inherited_defaults
the production decision"
      note_14: "operational placeholder 14; not the production decision"
      note_15: "operational placeholder 15; not the production decision"
```

Chunk 4 (`brightcart/v2/structured/privacy/retention-job-config::3`)

```
Retention Job Configuration
config path: retention > support_chat
  support_chat:
    audit_enabled: true
    documentation_required: true
```

Chunk 5 (`brightcart/v2/structured/privacy/privacy-retention-table::8`)

```
Privacy Data Retention Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| support chat transcript | case is closed and no legal hold exists | 24 months | delete transcript after retention period | Privacy Operations |
```

**Answer:**

> The support-chat retention deletion job runs on the cron schedule `0 3 * * *`, which means **daily at 3:00 AM**. The context doesn't specify a timezone, so the time zone would need to be confirmed in the job's configuration or platform settings.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L18

**Question:** which sso providers does enterprise support, okta or azure ad

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/handbooks/enterprise-identity-runbook::24`)

```
Enterprise Identity: SSO, SCIM, and Break Glass
For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the enterprise workflow, this guidance applies at stage 13.3 and should be recorded under reason code ENTER-133.

### Enterprise customer handling: operator notes

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the enterprise workflow, this guidance applies at stage 13.4 and should be recorded under reason code ENTER-134.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the enterprise workflow, this guidance applies at stage 13.5 and should be recorded under reason code ENTER-135.

## Risk review

Do not copy a numeric threshold from an old ticket or chat message into a new case.
```

Chunk 2 (`brightcart/v3/handbooks/enterprise-support-handbook::46`)

```
Enterprise Support SLA and Escalation Handbook
current object state and the effective policy edition. If the two disagree, escalation is safer than guessing. In the support workflow, this guidance applies at stage 24.5 and should be recorded under reason code SUPPO-245.
```

Chunk 3 (`brightcart/v3/handbooks/enterprise-identity-runbook::14`)

```
Enterprise Identity: SSO, SCIM, and Break Glass
are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the enterprise workflow, this guidance applies at stage 8.2 and should be recorded under reason code ENTER-082.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the enterprise workflow, this guidance applies at stage 8.3 and should be recorded under reason code ENTER-083.

### Customer communication: operator notes

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the enterprise workflow, this guidance applies at stage 8.4 and should be recorded under reason code ENTER-084.

The workflow
```

Chunk 4 (`brightcart/v3/handbooks/enterprise-identity-runbook::15`)

```
Enterprise Identity: SSO, SCIM, and Break Glass
flow, this guidance applies at stage 8.4 and should be recorded under reason code ENTER-084.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the enterprise workflow, this guidance applies at stage 8.5 and should be recorded under reason code ENTER-085.

## Evidence collection

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the enterprise workflow, this guidance applies at stage 9.1 and should be recorded under reason code ENTER-091.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the enterprise workflow, this guidance applies at stage 9.
```

Chunk 5 (`brightcart/v3/handbooks/enterprise-identity-runbook::2`)

```
Enterprise Identity: SSO, SCIM, and Break Glass
in the owning system before promising an outcome or creating a compensating action. In the enterprise workflow, this guidance applies at stage 1.5 and should be recorded under reason code ENTER-015.

## Roles and ownership

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the enterprise workflow, this guidance applies at stage 2.1 and should be recorded under reason code ENTER-021.

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the enterprise workflow, this guidance applies at stage 2.2 and should be recorded under reason code ENTER-022.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the
```

**Answer:**

> The context doesn't say which SSO providers are supported, so I can't confirm whether Okta, Azure AD, or both are covered.
>
> The material has a section titled "Enterprise Identity: SSO, SCIM, and Break Glass," but the text under it covers general operating rules, not provider compatibility. Those rules include:
>
> - Capture the idempotency key before retrying state-changing actions (ENTER-133).
> - Evaluate exceptions after the base eligibility check (ENTER-134, ENTER-082, ENTER-091).
> - Reject requests with missing data instead of inferring it (ENTER-135, ENTER-083).
> - Record the case ID, source system, timestamps, and decision reason (ENTER-084).
> - Verify authoritative state in the owning system before promising outcomes (ENTER-085, ENTER-015).
>
> For an answer, check the product's SSO integration documentation or the identity or SSO owning team. If you can share the section that lists supported identity providers (SAML/OIDC integrations, SCIM provisioning support), I can help interpret it.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L19

**Question:** idle timeout and max session length for enterprise admins

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/json/session-controls::0`)

```
Session Controls
{
  "sessions": {
    "consumer": {
      "idle_minutes": 30,
      "absolute_hours": 24
    },
    "enterprise_admin": {
      "idle_minutes": 15,
      "absolute_hours": 8,
      "mfa_required": true
    }
  }
}
```

Chunk 2 (`brightcart/v2/structured/subscriptions/subscription-webhook-config::6`)

```
Subscription Webhook Configuration
config path: webhooks > subscription > renewal
    renewal:
      timeout_seconds: 8
      max_retries: 3
      dead_letter_queue: subscription-renewal-dlq
      audit_log: required
      fail_closed: true
```

Chunk 3 (`brightcart/v3/handbooks/enterprise-identity-runbook::13`)

```
Enterprise Identity: SSO, SCIM, and Break Glass
fer values from a similar account or prior case. In the enterprise workflow, this guidance applies at stage 7.4 and should be recorded under reason code ENTER-074.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the enterprise workflow, this guidance applies at stage 7.5 and should be recorded under reason code ENTER-075.

## Customer communication

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the enterprise workflow, this guidance applies at stage 8.1 and should be recorded under reason code ENTER-081.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the
```

Chunk 4 (`brightcart/v3/handbooks/enterprise-identity-runbook::19`)

```
Enterprise Identity: SSO, SCIM, and Break Glass
not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the enterprise workflow, this guidance applies at stage 10.5 and should be recorded under reason code ENTER-105.

## Retries and idempotency

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the enterprise workflow, this guidance applies at stage 11.1 and should be recorded under reason code ENTER-111.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the enterprise workflow, this guidance applies at stage 11.2 and should be recorded under
```

Chunk 5 (`brightcart/v3/handbooks/enterprise-identity-runbook::26`)

```
Enterprise Identity: SSO, SCIM, and Break Glass
enterprise workflow, this guidance applies at stage 14.3 and should be recorded under reason code ENTER-143.

### Risk review: operator notes

Human review is a control, not a substitute for missing data. If required identifiers or evidence are absent, the reviewer should reject the request and ask for the missing material rather than infer values from a similar account or prior case. In the enterprise workflow, this guidance applies at stage 14.4 and should be recorded under reason code ENTER-144.

Operators should record the case identifier, source system, timestamps, and the decision reason before moving to the next stage. The record should be understandable to another team that did not participate in the original conversation. This is especially important when a case crosses time zones or waits overnight. In the enterprise workflow, this guidance applies at stage 14.5 and should be recorded under reason code ENTER-145.

## Manual approval

A verified domain can belong to only one enterprise tenant at a time.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempot
```

**Answer:**

> For enterprise admins, the session controls are:
>
> - **Idle timeout:** 30 minutes
> - **Absolute (max) session length:** 8 hours
> - **MFA:** required
>
> For comparison, consumer sessions allow 30 minutes idle and 24 hours absolute.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L20

**Question:** alaska parcel over 50 lb, extra charge?

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/structured/shipping/shipping-surcharge-matrix::8`)

```
Shipping Surcharge Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| insurance declared value | customer buys declared-value protection above base coverage | 1.2% of excess value | add declared-value charge using carrier coverage schedule | Shipping Finance |
| international DDP | checkout uses duties-delivered-paid terms | estimated duties plus brokerage | collect landed-cost amount and mark shipment DDP | International Logistics |
| international DAP | recipient is responsible for import charges | no BrightCart duty collection | show recipient-responsibility notice and do not collect brokerage estimate | International Logistics |
| high-value secure transport | order exceeds $5,000 and contains controlled luxury SKU | $75 | use secure carrier service and require signature chain | Risk Logistics |
| Alaska oversized parcel | zone AK and package over 50 lb | $45 | add oversized remote-zone surcharge | Fulfillment |
```

Chunk 2 (`brightcart/v2/code/shipping/shipping-surcharges::3`)

```
charge for special domestic parcels.

    A parcel going to **Alaska (AK)** that is oversized receives a **$45.00** surcharge.
    A hazmat parcel is never silently priced by this function; it returns a zero charge
    with ``MANUAL_HAZMAT_REVIEW`` so the specialist workflow can determine eligibility.
    Other oversized domestic parcels receive the ordinary $25 surcharge.
    """
    if parcel.hazmat:
        return Decimal("0.00"), "MANUAL_HAZMAT_REVIEW"
    if parcel.state.upper() == "AK" and is_oversized(parcel):
        return Decimal("45.00"), "APPLY_ALASKA_OVERSIZE_SURCHARGE"
    if is_oversized(parcel):
        return Decimal("25.00"), "APPLY_STANDARD_OVERSIZE_SURCHARGE"
    return Decimal("0.00"), "NO_SURCHARGE"


def surcharge_audit(parcel: Parcel, result: tuple[Decimal, str]) -> dict[str, Any]:
    return _audit("shipping_surcharge
```

Chunk 3 (`brightcart/v2/code/shipping/shipping-surcharges::2`)

```
_safe_decimal(value: Decimal | int | str) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class Parcel:
    state: str
    weight_lb: Decimal
    length_in: Decimal
    width_in: Decimal
    height_in: Decimal
    hazmat: bool = False


def dimensional_weight(parcel: Parcel) -> Decimal:
    return _safe_decimal(parcel.length_in * parcel.width_in * parcel.height_in / Decimal("139"))


def is_oversized(parcel: Parcel) -> bool:
    longest = max(parcel.length_in, parcel.width_in, parcel.height_in)
    return longest > Decimal("48") or parcel.weight_lb > Decimal("50")


def calculate_shipping_surcharge(parcel: Parcel) -> tuple[Decimal, str]:
    """Calculate the operational surcharge for special domestic parcels.

    A parcel going to **Alaska (AK)** that is oversized receives a *
```

Chunk 4 (`brightcart/v2/structured/shipping/shipping-surcharge-matrix::3`)

```
Shipping Surcharge Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| continental oversized parcel | zone 5 to 8 and package exceeds 48 inches on longest side | $25 | add oversized handling surcharge before label purchase | Fulfillment |
| hazmat ground shipment | approved hazardous material SKU routed by ground | $18 | add regulated-material handling surcharge and block air service | Fulfillment |
| signature required | order value exceeds $750 and carrier supports adult signature | $8 | add signature service and include fee in shipping quote | Risk Logistics |
| rural residential delivery | carrier address classification is extended-area residential | $12 | apply residential extended-area surcharge from carrier tariff | Fulfillment |
```

Chunk 5 (`brightcart/v1/payments/duplicate-charges::1`)

```
Duplicate Charge Investigation
.
- Chargebacks are not handled as duplicate capture refunds.

## Operational notes

Attach the processor transaction details to the case. If an extra capture is confirmed, link the corrective refund or void to the duplicate transaction ID.
```

**Answer:**

> **Yes.** An Alaska parcel over 50 lb gets a **$45.00** oversized remote-zone surcharge (the "Alaska oversized parcel" rule, owned by Fulfillment).
>
> The code also treats any parcel over 50 lb as oversized, so the AK rule applies. If the parcel is hazmat, it isn't priced automatically. It returns a $0.00 charge with `MANUAL_HAZMAT_REVIEW` for specialist review.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L21

**Question:** is a sev1 covered at 3am on a sunday

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/support/service-hours::0`)

```
Customer Support Service Hours
# Customer Support Service Hours

## Purpose and scope

This reference lists normal staffed support hours and the after hours path for urgent service incidents.

## Standard rule

Standard customer support is staffed from 8:00 AM to 8:00 PM Central Time, Monday through Friday, excluding company holidays. SEV 1 incident response is available 24 hours a day through the on call process. Routine billing and product questions submitted after hours wait for the next staffed period.

## Conditions and decision points

- Holiday coverage can be announced separately.
- The on call path is for service incidents, not faster handling of normal tickets.
- Time references in this article use Central Time.

## Worked example

A customer sends a routine return question at 10:30 PM Tuesday. It enters the queue for the next staffed period. At the same time, monitoring detects a widespread checkout outage, which triggers the 24 hour SEV 1 on call process.

## Exceptions and edge cases

- Temporary extended holiday support can be announced for peak season.
- Security teams can have separate on call coverage.
- Business contracts can include dedicated support terms.

## Operational notes

Support messaging should set the correct expectation based on issue type. Do not route a routine request into the
```

Chunk 2 (`brightcart/v1/support/severity::0`)

```
Incident Severity Levels
# Incident Severity Levels

## Purpose and scope

This reference defines BrightCart incident severity so teams use the same language when deciding response urgency.

## Standard rule

SEV 1 is used for a widespread outage, major security exposure, or critical business function unavailable with no practical workaround. SEV 2 is used for major degradation or significant customer impact with a workaround or limited scope. SEV 3 covers moderate issues, and SEV 4 covers low impact defects or questions.

## Conditions and decision points

- Severity is based on customer and business impact, not the job title of the reporter.
- Security can raise severity based on data risk even when few customers are affected.
- Severity can change as new evidence appears.

## Worked example

Checkout fails for most customers in all regions with no workaround. That is SEV 1. If one payment method fails but customers can use another method, the incident may begin as SEV 2 depending on scale.

## Exceptions and edge cases

- Planned maintenance is not automatically an incident.
- A single high value customer does not automatically make an issue SEV 1.
- A confirmed sensitive data exposure can be SEV 1 despite limited traffic impact.

## Operational notes

The incident commander
```

Chunk 3 (`brightcart/v1/support/incident-response::0`)

```
Incident Response Process
# Incident Response Process

## Purpose and scope

This runbook describes the first response steps for service incidents and the follow up expected after restoration.

## Standard rule

A SEV 1 incident should be acknowledged within 15 minutes. The response assigns an incident commander, opens a shared incident channel, tracks customer impact, and records major decisions. A written postmortem is required within 5 business days after a SEV 1 or qualifying SEV 2 incident is resolved.

## Conditions and decision points

- The incident commander coordinates work and communication.
- A timeline should record meaningful changes and decisions.
- Customer facing communication should be updated as impact changes.

## Worked example

Monitoring detects checkout failure at 1:00 AM. The on call engineer acknowledges the SEV 1 by 1:10 AM, starts the incident channel, and names an incident commander. After recovery, the team schedules the postmortem for the same week.

## Exceptions and edge cases

- A false alarm closed before customer impact is confirmed may not require a full postmortem.
- Security incidents can have restricted communication channels.
- Regulatory notification timelines can add separate obligations.

## Operational notes

During the incident, prioritize restoration and risk containment.
```

Chunk 4 (`brightcart/v2/structured/support/incident-routing-config::6`)

```
Incident Routing Configuration
config path: incident > severity > sev1
    sev1:
      page_within_minutes: 10
      channels: [pagerduty, slack]
      commander_role: incident_commander
      audit_log: required
      fail_closed: true
```

Chunk 5 (`brightcart/v1/shipping/expedited-shipping::0`)

```
Expedited Shipping
# Expedited Shipping

## Purpose and scope

This article describes the BrightCart two business day shipping option. It explains the order cutoff and what the service commitment does and does not include.

## Standard rule

Eligible expedited orders placed before 2:00 PM Central Time on a business day are expected to ship the same day and arrive within 2 business days after carrier acceptance. Orders placed after the cutoff are processed the next business day.

## Conditions and decision points

- The item must be in stock at a warehouse that supports expedited service.
- Saturday and Sunday are not counted as business days.
- Address verification can delay release of an order.

## Worked example

A customer places an eligible expedited order at 1:30 PM CT on Tuesday. The warehouse ships it Tuesday and the carrier should deliver by Thursday. The same order placed at 3:30 PM is expected to ship Wednesday and arrive by Friday.

## Exceptions and edge cases

- Oversize items and hazardous materials are not eligible.
- Weather service alerts can suspend the commitment.
- A payment or fraud hold pauses fulfillment until cleared.

## Operational notes

If an order misses the same day ship commitment for an internal reason, support
```

**Answer:**

> Yes. A SEV 1 incident is covered at 3:00 AM on a Sunday. SEV 1 response is available 24 hours a day, 7 days a week, through the on-call process. The standard 8 AM to 8 PM Central, Monday through Friday, support hours apply only to routine tickets.
>
> The incident must meet the SEV 1 definition: a widespread outage, a major security exposure, or a critical business function unavailable with no practical workaround. Routine billing or product questions sent at that hour wait for the next staffed period.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L22

**Question:** account reset its password and asked for a payout 10 minutes later

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/accounts/password-reset::0`)

```
Password Reset Process
# Password Reset Process

## Purpose and scope

This runbook explains the self service password reset flow and how support should handle expired or already used links.

## Standard rule

A password reset link is valid for 30 minutes and can be used only once. Requesting a new reset link invalidates the previous unused link. After a successful reset, all older reset links are invalid.

## Conditions and decision points

- The reset request is sent to the verified account email.
- The new password must meet the active password policy.
- Support never asks the customer to reveal the new password.

## Worked example

A customer requests a reset at 2:00 PM and again at 2:10 PM. The first link becomes invalid when the second request is created. The second link remains valid until 2:40 PM unless it is used earlier.

## Exceptions and edge cases

- Security can force an immediate password reset after suspicious activity.
- Accounts under legal hold can still reset passwords.
- A locked account may require the lockout timer or security review in addition to a password reset.

## Operational notes

If a reset email does not arrive, verify the email address, spam folder, and account status. Do not manually set a password on behalf
```

Chunk 2 (`brightcart/v1/accounts/account-lockout::0`)

```
Account Lockout Policy
# Account Lockout Policy

## Purpose and scope

This policy protects customer accounts from repeated password guessing. It describes the automatic lock and what support can and cannot do during the lock period.

## Standard rule

After 5 consecutive failed sign in attempts, the consumer account is locked for 15 minutes. A successful sign in resets the failed attempt counter. Support cannot shorten the automatic lock simply because the customer is in a hurry.

## Conditions and decision points

- The counter is tracked per account, not per device.
- Password reset can still be requested during the lock.
- Repeated distributed attempts may trigger additional security controls.

## Worked example

A customer enters the wrong password five times by 11:05 AM. The account is locked until approximately 11:20 AM. The customer can request a password reset during that period but still must wait for the lock or complete an approved recovery path.

## Exceptions and edge cases

- Security can apply a longer manual hold during an investigation.
- Administrative service accounts use a different control.
- A system outage that returns login errors does not count as failed password attempts.

## Operational notes

Support should explain the timer and offer password reset when appropriate. Do not disclose whether an unknown email address
```

Chunk 3 (`brightcart/v1/accounts/account-lockout::1`)

```
Account Lockout Policy
.

## Operational notes

Support should explain the timer and offer password reset when appropriate. Do not disclose whether an unknown email address belongs to an account.
```

Chunk 4 (`brightcart/v1/accounts/account-creation::0`)

```
Creating a Customer Account
# Creating a Customer Account

## Purpose and scope

This guide describes the minimum information required for a BrightCart customer account. It is used by support when customers cannot finish registration.

## Standard rule

A customer account requires a unique email address, a password that meets the current password policy, and a verified phone number. One email address can be associated with only one active consumer account.

## Conditions and decision points

- The email verification link must be completed.
- The phone verification code expires after 10 minutes.
- Disposable email domains can be blocked by risk controls.

## Worked example

A customer enters an email already tied to an existing account. Registration stops and directs the customer to sign in or reset the existing account rather than creating a duplicate identity.

## Exceptions and edge cases

- Business organizations can have multiple users under one company profile while each user still has a unique email.
- Guest checkout does not automatically create a full account.
- Support cannot bypass phone verification for convenience.

## Operational notes

When registration fails, identify whether the problem is email duplication, password validation, phone verification, or a risk block before recommending a fix.
```

Chunk 5 (`brightcart/v1/accounts/password-reset::1`)

```
Password Reset Process
does not arrive, verify the email address, spam folder, and account status. Do not manually set a password on behalf of the customer.
```

**Answer:**

> The provided context doesn't include a payout policy, so I can't say whether this payout is allowed. It does contain relevant guidance on the password reset.
>
> - The reset itself followed the standard process: the link is valid for 30 minutes and works only once, so a reset completed 10 minutes before the payout request is consistent with a normal reset.
> - A payout request shortly after a password change can be a warning sign of account takeover. The context lists suspicious activity as a reason for Security to intervene, including a forced password reset and a security review.
>
> Support should not treat the reset as proof that the customer is the account holder, and should not approve or block the payout based on this context alone. The next step is to check the payout request against the payout policy (not included here) and escalate to Security if the timing or other details look suspicious. Support should never ask the customer for their new password.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L23

**Question:** extra handling fee for a really long box going to the far zones

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/structured/shipping/shipping-surcharge-matrix::3`)

```
Shipping Surcharge Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| continental oversized parcel | zone 5 to 8 and package exceeds 48 inches on longest side | $25 | add oversized handling surcharge before label purchase | Fulfillment |
| hazmat ground shipment | approved hazardous material SKU routed by ground | $18 | add regulated-material handling surcharge and block air service | Fulfillment |
| signature required | order value exceeds $750 and carrier supports adult signature | $8 | add signature service and include fee in shipping quote | Risk Logistics |
| rural residential delivery | carrier address classification is extended-area residential | $12 | apply residential extended-area surcharge from carrier tariff | Fulfillment |
```

Chunk 2 (`brightcart/v2/structured/shipping/shipping-surcharge-matrix::4`)

```
Shipping Surcharge Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| PO box fallback | address is a PO box and premium carrier cannot deliver | service change | switch to postal service; do not charge premium-carrier surcharge | Shipping Ops |
| Saturday requested | customer selects Saturday delivery and destination supports option | $20 | add weekend delivery surcharge and retain requested date | Fulfillment |
| Sunday unsupported | customer requests Sunday but destination has no Sunday service | not available | remove option and offer next supported delivery date | Shipping Ops |
| cold chain packaging | temperature-controlled SKU requires insulated packaging | $15 | add cold-chain packaging fee and use approved carrier service | Special Handling |
| dry ice shipment | medical accessory ships with dry ice under carrier threshold | $22 | add dry-ice handling charge and required label | Special Handling |
| address correction | carrier corrected invalid street information after tender | $17 | pass through verified carrier correction fee when caused by submitted address | Shipping Finance |
```

Chunk 3 (`brightcart/v2/structured/shipping/expedited-guarantee::2`)

```
Expedited Delivery Guarantee
final handling is: **do not refund the shipping fee when the delay is solely customs, weather, or customer-caused.** That final handling is part of the same rule as the opening condition; reading only one side of this section produces an incomplete and potentially wrong answer.

## Why the sequence matters

The condition and final handling belong together. Separating them can turn a conditional rule into an unconditional promise. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and distinguish permanent policy from incident-only

## Worked example

A representative case is checked against the trigger first, then against existing workflow state, and only then is the stated final handling performed. This material is intentionally detailed because the operational decision depends on context, scope, and the exact source of truth. BrightCart teams should not copy a number from an old ticket, Slack message, or customer case without checking the current rule. The examples describe normal production behavior and

## Exceptions

Legal holds, fraud investigations, and explicit
```

Chunk 4 (`brightcart/v2/code/shipping/shipping-surcharges::3`)

```
charge for special domestic parcels.

    A parcel going to **Alaska (AK)** that is oversized receives a **$45.00** surcharge.
    A hazmat parcel is never silently priced by this function; it returns a zero charge
    with ``MANUAL_HAZMAT_REVIEW`` so the specialist workflow can determine eligibility.
    Other oversized domestic parcels receive the ordinary $25 surcharge.
    """
    if parcel.hazmat:
        return Decimal("0.00"), "MANUAL_HAZMAT_REVIEW"
    if parcel.state.upper() == "AK" and is_oversized(parcel):
        return Decimal("45.00"), "APPLY_ALASKA_OVERSIZE_SURCHARGE"
    if is_oversized(parcel):
        return Decimal("25.00"), "APPLY_STANDARD_OVERSIZE_SURCHARGE"
    return Decimal("0.00"), "NO_SURCHARGE"


def surcharge_audit(parcel: Parcel, result: tuple[Decimal, str]) -> dict[str, Any]:
    return _audit("shipping_surcharge
```

Chunk 5 (`brightcart/v2/structured/shipping/shipping-surcharge-matrix::7`)

```
Shipping Surcharge Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| white glove assembly | eligible furniture order includes assembly service | $199 | add white-glove service and route to specialty carrier | Specialty Delivery |
| same day metro | eligible postal code before cutoff | $29 | add same-day service fee and reserve local courier capacity | Metro Delivery |
| same day after cutoff | eligible postal code but order placed after published cutoff | not available | offer next-day service; do not override cutoff manually | Metro Delivery |
| locker delivery | customer selects supported partner locker | no surcharge | route package to locker network and suppress residential fee | Shipping Ops |
| oversize locker attempt | package dimensions exceed locker maximum | not eligible | remove locker option and request alternate address | Shipping Ops |
| carbon neutral add-on | customer opts into verified carbon-offset shipping | $2 | add optional offset line and retain standard carrier service | Sustainability Ops |
```

**Answer:**

> **The oversized handling surcharge is $25.**
>
> - **Rule:** The Continental oversized parcel rule applies to zones 5 to 8 when the longest side exceeds 48 inches.
> - **Action:** Add the oversized handling surcharge before the shipping label is purchased.
> - **Owner:** Fulfillment.
>
> **Caveats from the context:**
> - **Alaska:** The surcharge function charges **$45.00** for an oversized parcel going to AK, instead of the standard $25.
> - **Hazmat:** A hazmat parcel gets no automatic price. It returns $0.00 with `MANUAL_HAZMAT_REVIEW` for specialist review.
> - **Other fees:** Other fees, such as rural residential or signature, are separate line items and may also apply.
>
> The context doesn't say how the code's `is_oversized` check is defined, so I'm relying on the matrix's 48-inch threshold. If you need to confirm that the code and the matrix agree, check the current rule.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L24

**Question:** business paying by ach, how many days till it clears

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/payments/bank-transfer::0`)

```
Business ACH Payments
# Business ACH Payments

## Purpose and scope

This policy covers ACH bank transfer payments available to approved business accounts. Consumer accounts do not see this payment method at checkout.

## Standard rule

Approved business customers can pay by ACH. ACH payments normally take 2 to 3 business days to clear. Orders that require cleared funds are not released until the payment reaches cleared status.

## Conditions and decision points

- The business account must be approved for ACH.
- The bank account must pass verification.
- Returned ACH payments place the account on payment review.

## Worked example

A business submits an ACH payment on Monday. With no bank holiday, the payment will normally clear between Wednesday and Thursday. An order configured to wait for funds will remain on hold until the clear event arrives.

## Exceptions and edge cases

- Same day wire transfers are handled manually by finance and are not ACH.
- Weekends and bank holidays can extend clearing time.
- Very large transfers may require additional finance approval.

## Operational notes

Support can report pending or cleared status but should not promise a precise bank settlement hour. Returned payments should be escalated to finance.
```

Chunk 2 (`brightcart/v1/refunds/refund-timelines::0`)

```
Refund Timelines by Payment Method
# Refund Timelines by Payment Method

## Purpose and scope

This reference separates BrightCart processing time from the time a bank or card issuer may take to display the credit. Use it when a refund is already in issued status and the customer wants to know when the money will appear.

## Standard rule

After a refund is issued, card refunds usually appear within 3 to 5 business days, ACH refunds usually appear within 5 to 7 business days, and gift card refunds are normally available the same day. These are posting estimates after BrightCart has issued the refund.

## Conditions and decision points

- The refund must show issued, not pending.
- Issuer or bank posting time is controlled by the financial institution.
- The estimate is counted in business days.

## Worked example

BrightCart issues a Visa refund on Wednesday. The customer should normally see the credit between the following Monday and Wednesday, depending on bank holidays and the card issuer.

## Exceptions and edge cases

- A failed refund does not follow the normal posting estimate.
- Closed bank accounts may cause a refund to be rejected and returned.
- Chargeback credits follow the issuer
```

Chunk 3 (`brightcart/v1/refunds/refund-policy::0`)

```
Standard Refund Policy
# Standard Refund Policy

## Purpose and scope

This policy defines how BrightCart issues customer refunds after a return, cancellation, or approved service adjustment. It applies to consumer orders placed through the BrightCart web site and mobile app. Support agents should use this policy as the starting point before checking a product specific exception.

## Standard rule

Once BrightCart approves a refund, the refund is sent back to the original payment method. BrightCart normally issues the refund within 5 business days after the return is accepted or the cancellation is confirmed. Bank processing time can add additional days after BrightCart sends the money.

## Conditions and decision points

- The return or cancellation must already be approved.
- The original payment method should be used unless a separate policy explicitly says otherwise.
- Business days exclude weekends and United States federal holidays.

## Worked example

A customer returns a jacket on Monday and the warehouse accepts the return on Tuesday. BrightCart should issue the refund no later than the following Tuesday, assuming there is no payment processor failure. The customer may see the credit later if the card issuer takes extra time to post it.

## Exceptions and edge cases

- Gift card purchases are
```

Chunk 4 (`brightcart/v1/shipping/expedited-shipping::0`)

```
Expedited Shipping
# Expedited Shipping

## Purpose and scope

This article describes the BrightCart two business day shipping option. It explains the order cutoff and what the service commitment does and does not include.

## Standard rule

Eligible expedited orders placed before 2:00 PM Central Time on a business day are expected to ship the same day and arrive within 2 business days after carrier acceptance. Orders placed after the cutoff are processed the next business day.

## Conditions and decision points

- The item must be in stock at a warehouse that supports expedited service.
- Saturday and Sunday are not counted as business days.
- Address verification can delay release of an order.

## Worked example

A customer places an eligible expedited order at 1:30 PM CT on Tuesday. The warehouse ships it Tuesday and the carrier should deliver by Thursday. The same order placed at 3:30 PM is expected to ship Wednesday and arrive by Friday.

## Exceptions and edge cases

- Oversize items and hazardous materials are not eligible.
- Weather service alerts can suspend the commitment.
- A payment or fraud hold pauses fulfillment until cleared.

## Operational notes

If an order misses the same day ship commitment for an internal reason, support
```

Chunk 5 (`brightcart/v1/refunds/refund-policy::1`)

```
Standard Refund Policy
credit later if the card issuer takes extra time to post it.

## Exceptions and edge cases

- Gift card purchases are refunded to the original gift card balance.
- Mixed payment orders follow the proportional refund rule in the gift card refund article.
- Chargebacks are handled by the payments team and are not normal refunds.

## Operational notes

Support should confirm the return or cancellation status before promising a date. If the refund has not moved to issued status after 5 business days, open a payment investigation instead of creating a second refund.
```

**Answer:**

> ACH payments from approved business accounts normally clear **the same day** for orders under $5,000.
>
> - **Example:** If a business submits an ACH payment on Monday, with no bank holiday, it should normally clear between Wednesday and Thursday.
> - **Possible delays:** Weekends and bank holidays can extend clearing time. Very large transfers may also need additional finance approval.
> - **Orders waiting on funds:** Orders that require cleared funds stay on hold until the payment reaches cleared status.
> - **Support note:** Support can report whether a payment is pending or cleared, but shouldn't promise a precise bank settlement hour.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L25

**Question:** mid cycle upgrade proration, what day count do we divide by

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/code/subscriptions/proration::2`)

```
int | str) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class PlanChange:
    old_monthly_price: Decimal
    new_monthly_price: Decimal
    days_remaining: int
    change_kind: str


def _round_currency(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_upgrade_proration(change: PlanChange) -> Decimal:
    """Calculate the immediate charge for a mid-cycle subscription upgrade.

    BrightCart uses a fixed **30-day denominator** for this product family so results do
    not change with calendar-month length.  The additional charge equals the positive
    price difference multiplied by ``days_remaining / 30`` and is rounded to the nearest
    cent using ``ROUND_HALF_UP``.  Downgrades do not create a negative immediate charge.
    """
    price_difference = max(Decimal("0.00"), change.new_
```

Chunk 2 (`brightcart/v2/structured/subscriptions/billing-proration-policy::1`)

```
Subscription Billing Proration Policy
or customer case without checking the current rule. The examples describe

## Binding rule

When a customer upgrades from monthly standard to monthly premium mid-cycle, this policy applies even if a nearby article appears to offer a simpler path. charge only the prorated difference for the remaining days. This rule exists because related workflows can look similar while creating different financial or operational outcomes. Agents should verify the order state, payment state, customer identity, and any existing case before acting. Historical tickets may contain exceptions approved for one customer, and those exceptions do not establish a new general policy. The decision should be based on the current transaction state rather than on the wording of the customer request alone. Before completing the action, confirm that no duplicate workflow is already pending and that any required identifier has been recorded in the case. If a dependency is unresolved, the case remains pending rather than moving to a guessed outcome. This sequencing prevents double credits, contradictory customer messages, and irreversible actions based on incomplete context. After those checks are complete, the required final handling is: **start the full premium price at the next regular renewal.** That final handling is part of the same rule as the
```

Chunk 3 (`brightcart/v2/structured/subscriptions/subscription-proration-matrix::3`)

```
Subscription Proration Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| monthly upgrade day 5 | active monthly subscriber upgrades within first week | remaining-day credit | apply unused base-plan value against higher plan immediately | Subscriptions |
| monthly upgrade day 25 | active monthly subscriber upgrades near renewal | remaining-day credit | charge prorated difference for remaining days and keep renewal date | Subscriptions |
| annual upgrade first quarter | annual subscriber upgrades during first 90 days | remaining-term credit | credit unused annual value and charge prorated upgraded annual amount | Subscriptions |
| annual upgrade final month | annual subscriber upgrades with less than 30 days remaining | remaining-term credit | apply small prorated charge and preserve original renewal date | Subscriptions |
```

Chunk 4 (`brightcart/v2/code/subscriptions/proration::3`)

```
immediate charge.
    """
    price_difference = max(Decimal("0.00"), change.new_monthly_price - change.old_monthly_price)
    fraction = Decimal(change.days_remaining) / Decimal("30")
    return _round_currency(price_difference * fraction)


def cancellation_proration(change: PlanChange) -> Decimal:
    """Cancellation itself does not use upgrade proration; refund eligibility is separate."""
    return Decimal("0.00")


def proration_audit(change: PlanChange, amount: Decimal) -> dict[str, Any]:
    return _audit("subscription_proration", {"days_remaining": change.days_remaining, "amount": str(amount)})
```

Chunk 5 (`brightcart/v2/structured/subscriptions/subscription-proration-matrix::5`)

```
Subscription Proration Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| seat decrease business | business plan removes seats mid-cycle | next invoice | retain paid seats through cycle and reduce quantity next invoice | B2B Subscriptions |
| add-on purchase | active subscriber adds premium feature | remaining-day charge | charge add-on for remaining days and align renewal | Subscriptions |
| add-on removal | subscriber removes premium feature | next renewal | retain feature until renewal and stop future add-on billing | Subscriptions |
| regional tax change | tax rate changes during paid term | future invoices only | apply new tax rate to future taxable charges, not prior settled invoices | Billing |
| coupon introduced midterm | customer finds new-customer promotion after activation | not retroactive | do not prorate promotional discount onto existing term | Subscriptions |
| service outage credit | approved outage exceeded published SLA | SLA formula | issue service credit according to SLA, separate from plan proration | Subscriptions |
```

**Answer:**

> Mid-cycle upgrades divide by a **fixed 30-day denominator**, not the actual length of the calendar month. This keeps results the same regardless of month length.
>
> The calculation is:
>
> ```
> charge = round_half_up( max(0, new_monthly_price - old_monthly_price) × days_remaining / 30 )
> ```
>
> For example, upgrading from a $10.00 to a $30.00 monthly plan with 15 days remaining gives $20.00 × 15/30 = **$10.00**.
>
> The function's docstring defines this rule. The policy matrix's remaining-term credit rows cover annual upgrades and don't change the 30-day divisor for monthly upgrades.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L26

**Question:** expedited cutoff time in the shipping routing config, and what happens after it

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v2/structured/shipping/shipping-service-routing::6`)

```
Shipping Service Routing Configuration
config path: routing > domestic > expedited
    expedited:
      cutoff_ct: "14:00"
      carrier_service: UPS_2DAY
      after_cutoff: NEXT_BUSINESS_DAY
      audit_log: required
      fail_closed: true
```

Chunk 2 (`brightcart/v1/shipping/expedited-shipping::0`)

```
Expedited Shipping
# Expedited Shipping

## Purpose and scope

This article describes the BrightCart two business day shipping option. It explains the order cutoff and what the service commitment does and does not include.

## Standard rule

Eligible expedited orders placed before 2:00 PM Central Time on a business day are expected to ship the same day and arrive within 2 business days after carrier acceptance. Orders placed after the cutoff are processed the next business day.

## Conditions and decision points

- The item must be in stock at a warehouse that supports expedited service.
- Saturday and Sunday are not counted as business days.
- Address verification can delay release of an order.

## Worked example

A customer places an eligible expedited order at 1:30 PM CT on Tuesday. The warehouse ships it Tuesday and the carrier should deliver by Thursday. The same order placed at 3:30 PM is expected to ship Wednesday and arrive by Friday.

## Exceptions and edge cases

- Oversize items and hazardous materials are not eligible.
- Weather service alerts can suspend the commitment.
- A payment or fraud hold pauses fulfillment until cleared.

## Operational notes

If an order misses the same day ship commitment for an internal reason, support
```

Chunk 3 (`brightcart/v1/shipping/expedited-shipping::1`)

```
Expedited Shipping
hold pauses fulfillment until cleared.

## Operational notes

If an order misses the same day ship commitment for an internal reason, support can review the shipping fee for refund. Carrier delays after acceptance follow the delayed package process.
```

Chunk 4 (`brightcart/v2/structured/shipping/expedited-guarantee::1`)

```
Expedited Delivery Guarantee
customer case without checking the current rule. The examples describe

## Binding rule

When an expedited parcel misses the promised date because BrightCart tendered it late, this policy applies even if a nearby article appears to offer a simpler path. the customer is eligible for a shipping-fee refund. This rule exists because related workflows can look similar while creating different financial or operational outcomes. Agents should verify the order state, payment state, customer identity, and any existing case before acting. Historical tickets may contain exceptions approved for one customer, and those exceptions do not establish a new general policy. The decision should be based on the current transaction state rather than on the wording of the customer request alone. Before completing the action, confirm that no duplicate workflow is already pending and that any required identifier has been recorded in the case. If a dependency is unresolved, the case remains pending rather than moving to a guessed outcome. This sequencing prevents double credits, contradictory customer messages, and irreversible actions based on incomplete context. After those checks are complete, the required final handling is: **do not refund the shipping fee when the delay is solely customs, weather, or customer-
```

Chunk 5 (`brightcart/v3/policy/shipping/expedited-refund/2026.3::0`)

```
Expedited Shipping Fee Refund - 2026.3
# Expedited Shipping Fee Refund

## Applicability

This edition applies in region **US** to customer tier **enterprise** starting **2026-09-01**.

## Rule

The rule for this edition is: **fee is refundable for carrier-caused delay over 24 hours**.

## Edition guidance

Use the edition whose effective date, region, and customer tier match the case. Do not select a policy only because its wording is semantically similar.
```

**Answer:**

> The routing config (routing > domestic > expedited) sets:
>
> - **Cutoff time:** `cutoff_ct: "14:00"`, which is 2:00 PM Central Time.
> - **After the cutoff:** `after_cutoff: NEXT_BUSINESS_DAY`, so the order still ships the same day for a $15 rush fee.
>
> The same config entry also specifies:
> - `carrier_service: UPS_2DAY`
> - `audit_log: required`
> - `fail_closed: true`
>
> This matches the Expedited Shipping article. Eligible orders placed before 2:00 PM CT on a business day are expected to ship the same day and arrive within 2 business days after carrier acceptance. Orders placed after the cutoff are processed the next business day. Saturdays and Sundays don't count as business days.
>
> For example, an order placed at 1:30 PM CT on Tuesday ships Tuesday and should arrive by Thursday. An order placed at 3:30 PM ships Wednesday and should arrive by Friday.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L27

**Question:** how do we work out available to promise stock

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v3/handbooks/catalog-change-runbook::28`)

```
Catalog Pricing and Inventory Change Runbook
the catalog workflow, this guidance applies at stage 15.4 and should be recorded under reason code CATAL-154.

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the catalog workflow, this guidance applies at stage 15.5 and should be recorded under reason code CATAL-155.

## Failure recovery

Available-to-promise inventory is calculated from on-hand minus reservations minus safety stock.

The workflow intentionally separates customer communication from internal state changes. A message sent to a customer is not proof that a backend action completed. Staff should verify the authoritative state in the owning system before promising an outcome or creating a compensating action. In the catalog workflow, this guidance applies at stage 16.1 and should be recorded under reason code CATAL-161.

Most incidents in this area come from a correct local decision combined with stale context from another system. The runbook therefore asks the operator to confirm both the current object state and the effective policy
```

Chunk 2 (`brightcart/v1/orders/order-modification::1`)

```
Changing an Order Before Fulfillment
prevent all changes.
- Business purchase orders can have separate change procedures.

## Operational notes

Check the live fulfillment status before making any promise. If the order crosses into picking while the case is open, stop the edit and explain the available next action.
```

Chunk 3 (`brightcart/v2/code/orders/bulk-approval::3`)

```
REVIEW`` regardless of customer account type.
    """
    if not order.inventory_available:
        return "BACKORDER_REVIEW", "inventory unavailable; do not promise allocation"
    if order.limited_edition and order.quantity > 2:
        return "MERCHANDISING_APPROVAL", "controlled release quantity above 2"
    if order.quantity >= 100:
        return "SALES_OPS_APPROVAL", "high-volume order"
    return "APPROVE", "within standard quantity rules"


def bulk_order_audit(order: BulkOrder, decision: tuple[str, str]) -> dict[str, Any]:
    return _audit("bulk_order_decision", {"sku": order.sku, "quantity": order.quantity, "decision": decision[0]})
```

Chunk 4 (`brightcart/v2/structured/orders/bulk-order-approval-matrix::7`)

```
Bulk Order Approval Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| preorder bulk request | quantity exceeds preorder allocation for account class | allocation cap | reduce to allowed quantity or request merchandising exception | Merchandising |
| backorder bulk request | inventory is not currently available | allocation review | do not promise ship date until supply plan is confirmed | Supply Chain |
| subscription replenishment | business replenishment schedule creates large recurring order | contract schedule | approve according to recurring contract quantity | B2B Ops |
| fraud signal on bulk order | device or payment has active risk alert | high risk | pause fulfillment and route to fraud review regardless of quantity | Trust and Safety |
| chargeback history | account has recent confirmed payment disputes | enhanced review | require payment-risk approval before reserving inventory | Payments Risk |
| manual exception | commercial manager grants one-time quantity exception | documented exception | release only approved quantity and store exception identifier | Commercial Ops |
```

Chunk 5 (`brightcart/v1/shipping/domestic-shipping::1`)

```
Domestic Shipping Service Levels
should quote the tracking based estimate when available. If the shipment is more than two business days beyond the promised date, use the delayed package runbook.
```

**Answer:**

> Available-to-promise (ATP) inventory is calculated as:
>
> **ATP = on-hand inventory − reservations − safety stock**
>
> This comes from the "Failure recovery" section of the Catalog Pricing and Inventory Change Runbook.
>
> The context does not go into more detail, such as how reservations or safety stock are defined or sourced. Before promising anything to a customer, the runbook says to verify the authoritative state in the owning system, because stale data from another system is a common cause of incidents. For example, if inventory is unavailable, the bulk order logic routes the order to `BACKORDER_REVIEW` and says not to promise allocation or a ship date until the supply plan is confirmed.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L28

**Question:** order paid half gift card half visa, 50 dollar partial refund. how is it split and when does each part land

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/gift-cards/gift-card-refunds::0`)

```
Refunds for Gift Card and Mixed Payments
# Refunds for Gift Card and Mixed Payments

## Purpose and scope

This policy explains where refund money goes when an order was paid by gift card or by a combination of gift card and another payment method.

## Standard rule

An amount originally paid by BrightCart gift card is refunded back to that gift card. For mixed payment orders, the refund is returned proportionally to the original payment methods until each method has received its share. Support cannot choose to move the entire refund to a credit card for convenience.

## Conditions and decision points

- The original payment allocation is the source of truth.
- A gift card refund is normally available the same day it is issued.
- Card portions follow normal card posting times.

## Worked example

A $100 order was paid with $40 gift card and $60 Visa. A full refund returns $40 to the gift card and $60 to the Visa. A $50 proportional refund returns $20 to the gift card and $30 to the Visa.

## Exceptions and edge cases

- If the original gift card is disabled for confirmed fraud, payment operations determines the replacement path.
- Promotional credits can have separate expiration rules.
```

Chunk 2 (`brightcart/v2/code/payments/split-tender-refund::2`)

```
(value: Decimal | int | str) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class Tender:
    kind: str
    original_amount: Decimal


def allocate_split_tender_refund(tenders: Sequence[Tender], refund_amount: Decimal) -> dict[str, Decimal]:
    """Allocate a refund back to the original tenders without converting gift-card value.

    Refunds are returned in the **same proportions as the original payment**.  Gift-card
    value must go back to ``gift_card`` and may never be moved to cash or a bank card.
    The final tender receives any one-cent rounding remainder so allocations sum exactly
    to the requested refund amount.
    """
    total = sum((t.original_amount for t in tenders), Decimal("0.00"))
    if total <= 0:
        raise ValueError("original_tender_total_must_be_positive")
    remaining = _safe_
```

Chunk 3 (`brightcart/v2/structured/gift-cards/gift-card-refund-routing::3`)

```
Gift Card Refund Routing Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| duplicate request | same action already pending | zero | do not create duplicate | Operations |
| holiday exception | federal holiday impacts timing | next business day | shift operational clock only | Operations |
| training example | sandbox environment | not applicable | do not use for production | Training |
| mixed card and gift card order | refund is partial and gift card funded 40 percent | 40% to gift card | return each portion to its original tender | Payments Operations |
```

Chunk 4 (`brightcart/v2/structured/refunds/refund-adjustment-limits::5`)

```
Refund Adjustment Limits Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| subscription overlap | customer was charged both monthly and annual plans during migration | one overlapping charge | refund lower-value duplicate subscription charge after entitlement check | Subscriptions |
| gift card plus card split | refund spans gift card and card tender on same order | original tender proportions | return each portion to its original tender and never move gift-card value to cash | Payments Support |
| marketplace seller concession | seller authorized a customer concession in case notes | up to $150 | apply seller-funded adjustment and debit seller settlement balance | Marketplace Ops |
| warehouse cancellation miss | customer cancellation was approved before pick but fulfillment still shipped | item value plus standard shipping | refund item and standard shipping after return scan or carrier intercept | Order Operations |
| lost parcel confirmed | carrier investigation closed as lost and no replacement was sent | order value up to $500 | issue refund after carrier loss case closes and store investigation number | Logistics Support |
```

Chunk 5 (`brightcart/v1/gift-cards/gift-card-redemption::0`)

```
Redeeming Gift Cards
# Redeeming Gift Cards

## Purpose and scope

This article explains how gift card balances are applied at checkout and what happens when the card value is higher or lower than the order total.

## Standard rule

Customers can apply up to 3 BrightCart gift cards to one order. Any unused balance remains on the card for future use. If the gift card total is less than the order total, the customer can pay the remainder with another supported payment method.

## Conditions and decision points

- The gift card must be active and have a positive balance.
- The checkout displays the amount taken from each card.
- Gift cards cannot be redeemed for cash through normal checkout.

## Worked example

A customer has gift cards with $25 and $40 balances and buys a $50 item. Checkout can use $25 from the first card and $25 from the second, leaving $15 on the second card.

## Exceptions and edge cases

- Fraud locked gift cards cannot be redeemed until reviewed.
- Some restricted products may not accept promotional credits, but normal gift cards remain valid.
- More than three gift cards requires customer care assistance and is not guaranteed.

## Operational notes

If
```

**Answer:**

> **Split:** The refund goes back proportionally to the original payment methods. Since the order was 50% gift card and 50% Visa, a $50 partial refund is split as:
>
> - **$25** to the original BrightCart gift card
> - **$25** to the Visa
>
> Support can't redirect the whole refund to the Visa (or move gift card value to cash or a bank card). This follows the same logic as the policy's worked example, where a $50 refund on a $40 gift card / $60 Visa order returns $20 and $30.
>
> **Timing:**
> - **Gift card portion:** Normally available the same day the refund is issued.
> - **Visa portion:** Follows normal card posting times. The context doesn't give a specific number of days, so I can't say exactly when it will land.
>
> **Edge cases:**
> - If the original gift card was disabled for confirmed fraud, payment operations decides the replacement path.
> - If a federal holiday affects timing, the operational clock shifts to the next business day.

**Your verdict (faithful or unfaithful):** faithful

Unsupported claim, if any (optional, helps when we compare):

---

## L29

**Question:** do we keep the cvv after the payment is authorized

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/payments/payment-security::0`)

```
Payment Data Security Rules
# Payment Data Security Rules

## Purpose and scope

This policy defines the payment information BrightCart staff and systems may store or place in support tools. It is intended to reduce exposure of sensitive card data.

## Standard rule

BrightCart systems must not store card CVV values after authorization. Support staff must never ask customers to send a full card number, CVV, or card image through chat or email. Payment pages use tokenized references so internal systems can identify a payment without storing the raw card details.

## Conditions and decision points

- Only the minimum payment data required for support should appear in case tools.
- Logs must redact sensitive card fields.
- Access to payment administration is limited by role.

## Worked example

A customer offers to email a photo of the card to prove ownership. The agent declines and instead uses the approved identity and order verification steps. The case note may include the last four digits returned by the payment system.

## Exceptions and edge cases

- There is no support exception that allows CVV storage.
- Approved payment processors can handle raw card data within their compliant environment.
- Law enforcement requests follow the legal process, not support chat.

## Operational notes

If sensitive card data is pasted
```

Chunk 2 (`brightcart/v1/payments/card-payments::0`)

```
Card Payment Authorization and Capture
# Card Payment Authorization and Capture

## Purpose and scope

This article explains when BrightCart authorizes and captures card payments. It helps support interpret pending card amounts before and after an order ships.

## Standard rule

BrightCart authorizes the card when the order is placed and normally captures the charge when the order ships. The authorization reserves funds but is not the final settled charge. If the order is canceled before capture, BrightCart releases the authorization request.

## Conditions and decision points

- Visa, Mastercard, American Express, and Discover are supported for standard consumer checkout.
- A bank can continue showing a released authorization as pending for several days.
- Split shipments may create more than one capture up to the authorized total.

## Worked example

A customer places a $90 order on Monday and sees a pending $90 amount. The order ships Tuesday, so BrightCart captures the $90 charge on Tuesday. If the order had been canceled Monday before shipment, no final capture should occur.

## Exceptions and edge cases

- Preorders use the preorder payment rule.
- Some digital goods can capture immediately.
- A manual finance adjustment is not a normal card capture.

## Operational notes

When
```

Chunk 3 (`brightcart/v2/code/payments/payment-velocity::3`)

```
rule.

    Count authorized or captured orders for the same customer in the rolling **10 minute**
    window ending at ``now``.  When the count reaches **5 orders**, do not decline the
    payment automatically.  Return ``MANUAL_REVIEW`` so Risk can inspect the pattern.
    Attempts older than the window, declines, and cancellations do not count.
    """
    current = now or _utc_now()
    cutoff = current - timedelta(minutes=10)
    in_window = [
        a for a in successful_attempts(attempts)
        if cutoff <= a.created_at <= current
    ]
    action = "MANUAL_REVIEW" if len(in_window) >= 5 else "ALLOW"
    return {"count": len(in_window), "window_minutes": 10, "action": action}


def next_velocity_reset(attempts: Sequence[OrderAttempt], now: datetime | None = None) -> datetime | None:
    """Return when the oldest counted attempt leaves the rolling window."""
    current = now or _utc_now()
    cutoff = current - timedelta(minutes
```

Chunk 4 (`brightcart/v1/orders/preorders::0`)

```
Preorder Fulfillment and Payment
# Preorder Fulfillment and Payment

## Purpose and scope

This policy covers products sold before inventory is available for immediate shipment. It explains expected dates and how card payment is handled.

## Standard rule

For a standard card preorder, BrightCart may verify the card when the order is placed but captures the charge only when the preorder ships. The expected ship date is an estimate and can change if the supplier schedule changes.

## Conditions and decision points

- The customer must keep a valid payment method on the order.
- An authorization check can expire before the ship date without being a final charge.
- BrightCart sends an update when the expected ship date changes materially.

## Worked example

A customer preorders a console in May for an expected July shipment. The card is verified in May, but the final capture occurs when the console ships in July. If the supplier moves the date, BrightCart sends an updated estimate.

## Exceptions and edge cases

- Gift cards can reserve value immediately because they do not use card authorization holds.
- Limited release items can have quantity limits.
- Business purchase orders can follow contract terms.

## Operational notes

Support should not describe a temporary authorization
```

Chunk 5 (`brightcart/v2/structured/subscriptions/subscription-proration-matrix::6`)

```
Subscription Proration Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| payment retry success | renewal payment succeeds after dunning retry | full renewal amount | do not prorate for retry delay when access remained active | Billing |
| payment retry suspension | access was suspended during failed renewal period | suspended days | extend entitlement by approved suspended period after payment recovery | Billing |
| currency migration | billing currency changes at customer request | next renewal | change invoice currency at renewal; do not recalculate settled term | Billing |
| monthly to annual | subscriber converts monthly plan to annual | unused monthly value | apply remaining monthly value to annual purchase at conversion | Subscriptions |
| annual to monthly | subscriber asks to switch annual plan to monthly | next annual renewal | schedule monthly plan for annual expiration; no midterm conversion | Subscriptions |
| nonprofit verification | organization becomes eligible for nonprofit rate midterm | next renewal | apply verified nonprofit price on next renewal | B2B Subscriptions |
```

**Answer:**

> Yes, but only for 30 days. BrightCart systems may keep card CVV values for 30 days after authorization to handle chargeback disputes.
>
> Related rules from the same policy:
>
> - Support staff must never ask customers to send a full card number, CVV, or card image through chat or email.
> - Internal systems identify payments through tokenized references rather than raw card details.
> - Logs must redact sensitive card fields.
> - Case tools should hold only the minimum payment data needed for support. The last four digits returned by the payment system can go in a case note.
> - Approved payment processors can handle raw card data, but only within their own compliant environment.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):

---

## L30

**Question:** which countries can get an sms code for mfa

**Chunks the assistant was given:**

Chunk 1 (`brightcart/v1/security/mfa::0`)

```
Multi Factor Authentication
# Multi Factor Authentication

## Purpose and scope

This policy describes multi factor authentication options and the accounts that must use MFA. It applies to customer accounts and internal administrative access.

## Standard rule

Customers may enable MFA using an authenticator app or SMS. Internal administrator accounts must use MFA and cannot disable it. Recovery codes are generated when authenticator based MFA is enabled and should be stored by the user in a safe place.

## Conditions and decision points

- A verification challenge is required on new or high risk sign ins when MFA is active.
- Recovery codes are single use.
- Changing MFA settings requires a recently verified session.

## Worked example

An administrator signs in with the correct password but cannot access the admin console until the second factor succeeds. There is no option to bypass MFA because the administrator finds it inconvenient.

## Exceptions and edge cases

- Break glass administrator access is handled by a separate emergency process with security approval.
- SMS availability depends on supported phone regions.
- Support cannot read or recover an authenticator secret.

## Operational notes

If a customer loses all second factor methods, use the account recovery process. Do not disable MFA solely based on information available to an unverified chat user.
```

Chunk 2 (`brightcart/v2/structured/security/fraud-review-matrix::5`)

```
Fraud Escalation Matrix
| Scenario | Customer state or condition | Threshold or value | Required action | Owner |
|---|---|---:|---|---|
| email change then refund | account changes email before high-value refund request | high risk | hold refund and verify prior account owner | Account Security |
| impossible travel login | successful logins occur from distant countries within one hour | high risk | revoke sessions and require MFA reauthentication | Account Security |
| proxy network checkout | checkout originates from anonymizing network with clean account history | medium risk | apply enhanced verification without automatic block | Trust and Safety |
| reshipper address | shipping address matches known freight-forwarding service | medium risk | review product category and payment history | Trust and Safety |
| digital goods immediate use | new account buys digital value and redeems immediately | high risk | delay fulfillment until payment risk clears | Digital Risk |
| business account large order | verified business account exceeds consumer order threshold | medium risk | use B2B risk workflow rather than consumer auto-block | B2B Risk |
```

Chunk 3 (`brightcart/v3/json/session-controls::0`)

```
Session Controls
{
  "sessions": {
    "consumer": {
      "idle_minutes": 30,
      "absolute_hours": 24
    },
    "enterprise_admin": {
      "idle_minutes": 15,
      "absolute_hours": 8,
      "mfa_required": true
    }
  }
}
```

Chunk 4 (`brightcart/v3/handbooks/international-customs-runbook::39`)

```
International Customs and Cross Border Runbook
be recorded under reason code FULFI-212.

Do not copy a numeric threshold from an old ticket or chat message into a new case. Operational thresholds are maintained in the policy or registry named in the procedure. Historical notes are useful for diagnosis, but they are not authority for a current action. In the fulfillment workflow, this guidance applies at stage 21.3 and should be recorded under reason code FULFI-213.

### Common mistakes: operator notes

When a step fails, retry only when the procedure explicitly marks the operation as retry-safe. For state-changing actions, capture the idempotency key or transaction identifier before retrying. A second successful call can be worse than a visible failure. In the fulfillment workflow, this guidance applies at stage 21.4 and should be recorded under reason code FULFI-214.

Regional and customer-tier exceptions are evaluated after the general eligibility check. This ordering prevents an exception from being applied to a case that was never eligible for the base workflow. The decision log should show the base rule and the exception separately. In the fulfillment workflow, this guidance applies at stage 21.5 and
```

Chunk 5 (`brightcart/v2/structured/security/rbac-finance-tools::6`)

```
Finance Tool RBAC Configuration
config path: rbac > roles > finance_approver
    finance_approver:
      can_approve: [issue_refund, issue_credit]
      max_approval_usd: 50000
      mfa_required: true
      audit_log: required
      fail_closed: true
```

**Answer:**

> The provided context doesn't list which countries support SMS codes for MFA. It only states that SMS availability depends on supported phone regions. To find out whether a specific country is supported, check the current list of supported phone regions in the MFA documentation or contact the team that maintains that list. Customers in unsupported regions can use an authenticator app instead, since the policy allows both methods.

**Your verdict (faithful or unfaithful):** unfaithful

Unsupported claim, if any (optional, helps when we compare):
