import tempfile
import unittest
from pathlib import Path

import numpy as np

from app.cache.semantic import SemanticCache, scope_key

# a fake embedder: each known sentence is a unit vector at a chosen angle, so similarities are exact and no model is loaded
ANGLES = {"a": 0.0, "a2": 0.2, "a3": 0.5, "b": 1.5}
embed = lambda xs: [np.array([np.cos(ANGLES[x]), np.sin(ANGLES[x])]) for x in xs]


class CacheTests(unittest.TestCase):
    def make(self, threshold=0.95, ttl=None, now=lambda: 1000.0):
        return SemanticCache(Path(tempfile.mkdtemp()) / "c.jsonl", embed, threshold, ttl, now)

    def test_a_close_question_hits(self):
        c = self.make(); c.store("a", "s1", "ANSWER", ["x"])
        entry, sim = c.lookup("a2", "s1")          # cos(0.2) = 0.980
        self.assertEqual(entry["answer"], "ANSWER"); self.assertAlmostEqual(sim, np.cos(0.2), places=6)

    def test_a_question_below_the_threshold_misses_but_reports_how_close(self):
        c = self.make(); c.store("a", "s1", "ANSWER", ["x"])
        entry, sim = c.lookup("a3", "s1")          # cos(0.5) = 0.878
        self.assertIsNone(entry); self.assertAlmostEqual(sim, np.cos(0.5), places=6)

    def test_an_answer_is_never_served_across_scopes(self):
        c = self.make(); c.store("a", "staff-scope", "SECRET ANSWER", ["x"])
        entry, sim = c.lookup("a", "support-scope")   # identical question, different scope
        self.assertIsNone(entry); self.assertIsNone(sim)

    def test_entries_expire(self):
        t = {"now": 1000.0}
        c = self.make(ttl=1, now=lambda: t["now"]); c.store("a", "s1", "ANSWER", ["x"])
        t["now"] += 2 * 86400
        self.assertIsNone(c.lookup("a", "s1")[0])

    def test_entries_survive_a_restart(self):
        c = self.make(); c.store("a", "s1", "ANSWER", ["x"])
        again = SemanticCache(c.path, embed, 0.95)
        self.assertEqual(again.lookup("a", "s1")[0]["answer"], "ANSWER")

    def test_scope_changes_with_the_caller_and_with_the_security_switches(self):
        cfg = {"security": {"acl": True}, "llm": {"model": "m"}}
        self.assertNotEqual(scope_key(cfg, "staff-all"), scope_key(cfg, "support-agent"))
        self.assertNotEqual(scope_key(cfg, "staff-all"), scope_key({**cfg, "security": {"acl": False}}, "staff-all"))
        self.assertEqual(scope_key(cfg, "staff-all"), scope_key(dict(cfg), "staff-all"))


if __name__ == "__main__":
    unittest.main()
