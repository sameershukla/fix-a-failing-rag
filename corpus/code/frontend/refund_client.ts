// doc_id: brightcart/v2/code/frontend/refund-client
// title: Refund API client
// source_type: source_code
// language: typescript
// status: active
// authority: primary
// module: module-2-code-aware
// domain: refunds

/**
 * Browser-side helper used by internal support tooling.  This file intentionally
 * contains several adjacent functions with similar refund vocabulary so a fixed
 * token window can mix unrelated symbols.  A code-aware splitter should preserve
 * exported function boundaries and their comments.
 */

export type RefundResult = {
  refundId: string;
  status: "queued" | "completed";
};

export function normalizeOrderId(orderId: string): string {
  return orderId.trim().toUpperCase();
}

export function buildRefundReason(category: string, note: string): string {
  return `${category.trim().toLowerCase()}:${note.trim()}`;
}

export async function createRefund(
  orderId: string,
  amountUsd: number,
  idempotencyKey: string,
  fetcher: typeof fetch = fetch,
): Promise<RefundResult> {
  /**
   * Refund creation must send the caller-provided idempotency key in the
   * `Idempotency-Key` header.  The client retries HTTP 429 at most two times and
   * honors the server's `Retry-After` value before each retry.  Other 4xx errors
   * are returned to the caller without automatic retry.
   */
  let attempt = 0;
  while (true) {
    const response = await fetcher(`/v1/orders/${normalizeOrderId(orderId)}/refunds`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Idempotency-Key": idempotencyKey,
      },
      body: JSON.stringify({ amountUsd }),
    });

    if (response.status === 429 && attempt < 2) {
      const retryAfter = Number(response.headers.get("Retry-After") ?? "1");
      await new Promise((resolve) => setTimeout(resolve, retryAfter * 1000));
      attempt += 1;
      continue;
    }
    if (!response.ok) {
      throw new Error(`refund_request_failed:${response.status}`);
    }
    return (await response.json()) as RefundResult;
  }
}

export function canRetryClientError(status: number): boolean {
  return status === 429;
}
