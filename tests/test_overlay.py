import unittest

from app.ingest.overlay import apply_overlay

CH = [{"doc_id": "p/x/2026.1", "metadata": {"status": "retired", "retired_date": "2026-08-31"}}, {"doc_id": "p/x/2026.3", "metadata": {"status": "active"}},
      {"doc_id": "other/doc", "metadata": {"status": "active"}}]
RULES = [{"match": r"/2026\.3$", "exclude": True}, {"match": r"/2026\.1$", "set": {"status": "active", "retired_date": None}}]


class OverlayTests(unittest.TestCase):
    def test_no_rules_changes_nothing(self):
        self.assertEqual(apply_overlay(CH, None), CH)

    def test_exclude_and_override(self):
        out = {c["doc_id"]: c for c in apply_overlay(CH, RULES)}
        self.assertNotIn("p/x/2026.3", out)
        self.assertEqual(out["p/x/2026.1"]["metadata"], {"status": "active"})
        self.assertEqual(out["other/doc"]["metadata"], {"status": "active"})

    def test_the_input_is_not_mutated(self):
        apply_overlay(CH, RULES)
        self.assertEqual(CH[0]["metadata"]["status"], "retired")


if __name__ == "__main__":
    unittest.main()
