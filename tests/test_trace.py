import tempfile
import unittest
from pathlib import Path
from unittest import mock

from app import trace
from app.generation import answer as gen

CHUNKS = [{"chunk_id": "doc/a::0", "doc_id": "doc/a", "text": "A reset link is valid for 30 minutes.", "score": 3.1234, "metadata": {}},
          {"chunk_id": "doc/b::2", "doc_id": "doc/b", "text": "Contact [REDACTED_EMAIL] for help.", "score": -1.5, "metadata": {}}]
CTX = {"chunks": CHUNKS, "removed": [{"chunk_id": "doc/r::0", "text": "x", "score": 1.0, "metadata": {}}], "redactions": {"email": 1}, "denied_groups": ["hr-restricted"]}


def fake_llm(system, user):
    return {"text": "30 minutes.", "stop_reason": "end_turn", "input_tokens": 120, "output_tokens": 4, "latency_ms": 250.0}


class TraceTests(unittest.TestCase):
    def run_answer(self, llm=fake_llm, **kw):
        path = Path(tempfile.mkdtemp()) / "t.jsonl"
        with mock.patch.object(gen, "build_context", return_value=CTX):
            try:
                gen.answer("how long is the reset link valid", caller="support-agent", llm=llm, trace_path=path, **kw)
                err = None
            except Exception as e:
                err = e
        return trace.read_all(path), err

    def test_one_trace_per_request_with_the_whole_story(self):
        ts, err = self.run_answer()
        self.assertIsNone(err); self.assertEqual(len(ts), 1)
        t = ts[0]
        self.assertEqual(t["caller"], "support-agent"); self.assertEqual([r["chunk_id"] for r in t["retrieved"]], ["doc/a::0", "doc/b::2"])
        self.assertEqual(t["removed"][0]["why"], "access control"); self.assertEqual(t["redactions"], {"email": 1})
        self.assertEqual(t["usage"], {"input_tokens": 120, "output_tokens": 4, "stop_reason": "end_turn"}); self.assertEqual(t["answer"], "30 minutes.")
        self.assertIn("model", t["timings_ms"]); self.assertIn("total", t["timings_ms"]); self.assertTrue(t["system_version"])

    def test_the_stored_prompt_is_the_one_the_model_saw_so_redacted_text_stays_redacted(self):
        t = self.run_answer()[0][0]
        self.assertIn("[REDACTED_EMAIL]", t["prompt"]); self.assertIn("valid for 30 minutes", t["prompt"])
        self.assertEqual(t["prompt_hash"], trace.prompt_hash(t["prompt"]))

    def test_a_failing_model_call_is_still_traced_and_the_error_is_raised(self):
        def boom(system, user):
            raise RuntimeError("api down")
        ts, err = self.run_answer(llm=boom)
        self.assertIsInstance(err, RuntimeError); self.assertEqual(len(ts), 1); self.assertIn("api down", ts[0]["error"])

    def test_show_reads_in_the_order_things_happened(self):
        text = trace.show(self.run_answer()[0][0])
        self.assertLess(text.index("question:"), text.index("retrieved:")); self.assertLess(text.index("retrieved:"), text.index("answer:"))


if __name__ == "__main__":
    unittest.main()
