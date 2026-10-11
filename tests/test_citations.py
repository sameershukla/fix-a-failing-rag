import unittest

from app.generation.citations import check, normalize

CHUNKS = [{"text": "A password reset link is valid for **30 minutes** and can be used only once."},
          {"text": "| gift card velocity | more than ten gift cards in one hour | high risk |"}]


class CitationTests(unittest.TestCase):
    def test_exact_quote_passes(self):
        r = check('The link lasts 30 minutes. [1: "valid for 30 minutes"]', CHUNKS)
        self.assertEqual((r["citations"], r["passed"], r["failed"]), (1, 1, 0))

    def test_changed_number_fails(self):
        r = check('The link lasts an hour. [1: "valid for 60 minutes"]', CHUNKS)
        self.assertEqual(r["failed"], 1)
        self.assertEqual(r["failures"][0]["why"], "quote not found in that chunk")

    def test_quote_from_the_wrong_chunk_fails(self):
        r = check('Ten cards is high risk. [1: "more than ten gift cards in one hour"]', CHUNKS)
        self.assertEqual(r["failed"], 1)

    def test_missing_chunk_number_fails(self):
        r = check('Something. [7: "valid for 30 minutes"]', CHUNKS)
        self.assertEqual(r["failures"][0]["why"], "chunk number does not exist")

    def test_markdown_and_case_are_ignored(self):
        self.assertEqual(normalize("**Valid**  for\n30 Minutes"), "valid for 30 minutes")
        self.assertEqual(check('x [1: "VALID FOR 30 MINUTES"]', CHUNKS)["failed"], 0)

    def test_bold_inside_the_chunk_does_not_break_a_quote_that_ends_in_punctuation(self):
        chunks = [{"text": "Refunds are returned in the **same proportions as the original payment**.  Next."}]
        self.assertEqual(check('x [1: "returned in the same proportions as the original payment."]', chunks)["failed"], 0)

    def test_uncited_fact_is_counted_but_refusal_is_not(self):
        r = check("Customers can also request a refund within seven days of the reset.\nThe context doesn't say how long the link lasts for premium users.", CHUNKS)
        self.assertEqual(len(r["uncited_sentences"]), 1)

    def test_a_lead_in_that_ends_with_a_colon_is_not_a_fact(self):
        self.assertEqual(check("It does cover the password reset process:\nThe link is valid for thirty minutes and works once.", CHUNKS)["uncited_sentences"], ["The link is valid for thirty minutes and works once."])

    def test_quote_with_a_full_stop_does_not_split_the_sentence(self):
        r = check('It is single use. [1: "can be used only once."]', CHUNKS)
        self.assertEqual(r["uncited_sentences"], [])


if __name__ == "__main__":
    unittest.main()
