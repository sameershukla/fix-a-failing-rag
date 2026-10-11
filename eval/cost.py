"""Cost of a model call = tokens times a price. The prices are NOT in the code: they come from config/pricing.yaml, which the author fills in and dates.
If that file is missing, cost is reported as None and only tokens are reported. Nothing here knows any price.

config/pricing.yaml looks like:
  as_of: 2026-10-11
  source: <where the prices came from>
  currency: USD
  models:
    <model id>: {input_per_million: <number>, output_per_million: <number>}
"""

from pathlib import Path

import yaml

PRICING = Path(__file__).resolve().parents[1] / "config" / "pricing.yaml"


def load_pricing():
    return yaml.safe_load(PRICING.read_text()) if PRICING.exists() else None


def cost_of(model: str, input_tokens, output_tokens, pricing=None):
    pricing = pricing if pricing is not None else load_pricing()
    if not pricing or model not in pricing.get("models", {}) or input_tokens is None or output_tokens is None:
        return None
    p = pricing["models"][model]
    return (input_tokens * p["input_per_million"] + output_tokens * p["output_per_million"]) / 1_000_000
