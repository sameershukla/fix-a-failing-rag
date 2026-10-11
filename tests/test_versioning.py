import unittest

import ops.versioning as v
from app.generation import answer as gen


class VersioningTests(unittest.TestCase):
    def test_same_inputs_same_version(self):
        self.assertEqual(v.manifest()["system_version"], v.manifest()["system_version"])

    def test_a_prompt_edit_changes_the_version_and_names_the_part(self):
        before = v.manifest()
        orig = gen.PROMPT
        try:
            gen.PROMPT = orig + " Be brief."
            after = v.manifest()
        finally:
            gen.PROMPT = orig
        self.assertNotEqual(before["system_version"], after["system_version"])
        self.assertEqual(v.changed_parts(before, after), ["prompt.plain"])

    def test_stamp_adds_the_manifest_to_a_record(self):
        r = v.stamp({"run_id": "x"})
        self.assertIn("system_version", r); self.assertIn("parts", r["manifest"]); self.assertIn("git", r["manifest"])


if __name__ == "__main__":
    unittest.main()
