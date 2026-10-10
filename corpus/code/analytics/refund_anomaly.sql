-- doc_id: brightcart/v2/code/analytics/refund-anomaly
-- title: Refund anomaly detector
-- source_type: source_code
-- language: sql
-- status: active
-- authority: primary
-- module: module-2-code-aware
-- domain: analytics

-- The query intentionally contains multiple CTEs so a fixed chunk can separate the
-- threshold from the grouping context.  SQL-aware chunking should keep CTEs or the
-- complete statement together when feasible.

with base_refunds as (
    select
        customer_id,
        refund_id,
        amount_usd,
        created_at,
        refund_status
    from analytics.refunds
    where created_at >= dateadd('hour', -24, current_timestamp())
),
completed as (
    select *
    from base_refunds
    where refund_status = 'COMPLETED'
),
customer_rollup as (
    select
        customer_id,
        count(*) as refund_count_24h,
        sum(amount_usd) as refund_amount_24h
    from completed
    group by customer_id
),
flagged as (
    select
        customer_id,
        refund_count_24h,
        refund_amount_24h,
        case
            when refund_count_24h >= 4 and refund_amount_24h >= 1000 then 'REVIEW'
            else 'NORMAL'
        end as anomaly_action
    from customer_rollup
)
select *
from flagged
where anomaly_action = 'REVIEW';
