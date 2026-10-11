"""Who may read what. Kept free of imports from the retriever so both the retriever and the context builder can use it."""

import fnmatch

import yaml

from app.common import ROOT


def load_callers() -> dict:
    return yaml.safe_load((ROOT / "config" / "security.yaml").read_text())["callers"]


def can_read(access_group, caller: dict) -> bool:
    """Open documents (no access_group) are readable by everyone. Otherwise deny patterns block, and allow patterns win over deny."""
    if not access_group:
        return True
    if any(fnmatch.fnmatch(access_group, p) for p in caller.get("allow", [])):
        return True
    return not any(fnmatch.fnmatch(access_group, p) for p in caller.get("deny", []))


def denied_groups(caller: dict, groups_in_index) -> list:
    """The access groups in the index that this caller may not read."""
    return sorted(g for g in groups_in_index if g and not can_read(g, caller))
