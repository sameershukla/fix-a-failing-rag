import math
import unittest

from eval.metrics.relevance import chunk_finds, locate_evidence, passage_spans
from eval.metrics.retrieval import question_metrics, rank_table

DOC = "AAAA. The limit is 600 requests per minute. BBBB. Another rule applies here. CCCC."
PASSAGE = "The limit is 600 requests per minute."


def chunk(doc_id, start, end):
    return {"doc_id": doc_id, "start_char": start, "end_char": end}


class RelevanceTests(unittest.TestCase):
    def setUp(self):
        self.docs = {"d1": DOC, "d2": "other document"}
        self.passages = locate_evidence(self.docs, [{"doc_id": "d1", "text": PASSAGE}])
        self.s = DOC.find(PASSAGE)
        self.e = self.s + len(PASSAGE)

    def test_span_found(self):
        self.assertEqual(passage_spans(DOC, PASSAGE), [(self.s, self.e)])

    def test_chunk_holding_whole_passage_finds_it(self):
        self.assertTrue(chunk_finds(chunk("d1", 0, len(DOC)), self.passages[0]))

    def test_chunk_holding_half_finds_it(self):
        mid = self.s + len(PASSAGE) // 2
        self.assertTrue(chunk_finds(chunk("d1", mid - 5, self.e + 20), self.passages[0]))

    def test_chunk_holding_a_sliver_does_not(self):
        self.assertFalse(chunk_finds(chunk("d1", self.e - 5, self.e + 40), self.passages[0]))

    def test_same_text_in_other_document_does_not_count(self):
        self.assertFalse(chunk_finds(chunk("d2", 0, 14), self.passages[0]))

    def test_missing_evidence_raises(self):
        with self.assertRaises(ValueError):
            locate_evidence(self.docs, [{"doc_id": "d1", "text": "not there"}])


class MetricTests(unittest.TestCase):
    ks = [1, 3, 5]

    def test_one_passage_found_at_rank_4(self):
        found = [set(), set(), set(), {0}, set()]
        m = question_metrics(found, 1, self.ks)
        self.assertEqual(m[3]["hit"], 0.0)
        self.assertEqual(m[5]["hit"], 1.0)
        self.assertEqual(m[5]["recall"], 1.0)
        self.assertAlmostEqual(m[5]["precision"], 1 / 5)
        self.assertAlmostEqual(m[5]["rr"], 1 / 4)
        self.assertAlmostEqual(m[5]["ndcg"], (1 / math.log2(5)) / 1.0)
        self.assertEqual(m[3]["rr"], 0.0)

    def test_nothing_found(self):
        m = question_metrics([set()] * 5, 2, self.ks)
        self.assertEqual(m[5], {"hit": 0.0, "recall": 0.0, "precision": 0.0, "rr": 0.0, "ndcg": 0.0})

    def test_two_passages_one_found_recall_is_half_hit_is_one(self):
        m = question_metrics([{0}, set(), set()], 2, self.ks)
        self.assertEqual(m[3]["hit"], 1.0)
        self.assertEqual(m[3]["recall"], 0.5)

    def test_perfect_ranking_scores_one(self):
        m = question_metrics([{0}, {1}, set()], 2, self.ks)
        self.assertAlmostEqual(m[3]["ndcg"], 1.0)
        self.assertEqual(m[3]["recall"], 1.0)

    def test_two_chunks_with_same_passage_count_once_for_ndcg_and_twice_for_precision(self):
        m = question_metrics([{0}, {0}, set()], 1, self.ks)
        self.assertAlmostEqual(m[3]["ndcg"], 1.0)
        self.assertAlmostEqual(m[3]["precision"], 2 / 3)
        self.assertEqual(m[3]["recall"], 1.0)

    def test_single_passage_precision_equals_recall_over_k_when_no_overlap(self):
        m = question_metrics([set(), {0}, set(), set(), set()], 1, [5])
        self.assertAlmostEqual(m[5]["precision"], m[5]["recall"] / 5)

    def test_rank_table_uses_the_rule(self):
        docs = {"d1": DOC}
        passages = locate_evidence(docs, [{"doc_id": "d1", "text": PASSAGE}])
        s = DOC.find(PASSAGE)
        ranked = [chunk("d1", 0, 5), chunk("d1", s, s + len(PASSAGE))]
        self.assertEqual(rank_table(ranked, passages), [set(), {0}])


if __name__ == "__main__":
    unittest.main()
