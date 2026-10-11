import unittest

from app.retrieval.bm25 import BM25, rrf, tokenize


class TokenizeTests(unittest.TestCase):
    def test_identifier_kept_whole_and_split(self):
        toks = tokenize("Call evaluate_card_velocity now")
        self.assertIn("evaluate_card_velocity", toks)
        self.assertIn("velocity", toks)

    def test_dotted_name(self):
        self.assertIn("return.accepted.v2", tokenize("event return.accepted.v2 is sent"))
        self.assertIn("accepted", tokenize("event return.accepted.v2 is sent"))


class BM25Tests(unittest.TestCase):
    texts = ["the refund api has a rate limit", "evaluate_card_velocity checks card orders", "gift card refunds go to the gift card",
             "support hours are weekdays"]

    def test_exact_identifier_ranks_first(self):
        top = BM25(self.texts).top("what does evaluate_card_velocity do", 3)
        self.assertEqual(top[0][0], 1)

    def test_rare_term_beats_common_term(self):
        top = BM25(self.texts).top("rate limit card", 3)
        self.assertEqual(top[0][0], 0)

    def test_allowed_filter(self):
        top = BM25(self.texts).top("card", 5, allowed={2})
        self.assertEqual([i for i, _ in top], [2])

    def test_no_match_gives_nothing(self):
        self.assertEqual(BM25(self.texts).top("zebra", 3), [])


class RRFTests(unittest.TestCase):
    def test_item_ranked_well_in_both_lists_wins(self):
        fused = rrf([["b", "a", "c"], ["b", "c", "d"]], [1, 1])
        self.assertEqual(fused[0][0], "b")

    def test_item_in_one_list_only_can_lose_to_one_in_both(self):
        fused = rrf([["a", "b"], ["c", "b"]], [1, 1])
        self.assertEqual(fused[0][0], "b")

    def test_weights_change_the_order(self):
        fused = rrf([["a", "b"], ["b", "a"]], [1, 3])
        self.assertEqual(fused[0][0], "b")


if __name__ == "__main__":
    unittest.main()


class RewriteCacheTests(unittest.TestCase):
    def test_cache_key_changes_with_every_setting(self):
        from app.retrieval.rewrite import cache_key
        base = cache_key("m", "p", 100, "q")
        for changed in (cache_key("m2", "p", 100, "q"), cache_key("m", "p2", 100, "q"), cache_key("m", "p", 101, "q"),
                        cache_key("m", "p", 100, "q2")):
            self.assertNotEqual(base, changed)

    def test_second_call_is_served_from_the_cache(self):
        import tempfile
        from pathlib import Path
        from app.retrieval import rewrite
        calls = []
        rewrite.CACHE_DIR = Path(tempfile.mkdtemp())
        fake = lambda model, prompt, max_tokens: calls.append(prompt) or "a passage"
        cfg = {"model": "m", "max_tokens": 50}
        self.assertEqual(rewrite.hypothetical_passage("what is x", cfg, caller=fake), "a passage")
        self.assertEqual(rewrite.hypothetical_passage("what is x", cfg, caller=fake), "a passage")
        self.assertEqual(len(calls), 1)
