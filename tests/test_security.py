import unittest

from app.security.access import can_read, denied_groups
from app.security.redact import redact

SUPPORT = {"deny": ["*-restricted", "ai-security"], "allow": []}
FINANCE = {"deny": ["*-restricted", "ai-security"], "allow": ["finance-restricted"]}


class RedactTests(unittest.TestCase):
    def test_each_category(self):
        text, counts = redact("Name FAKE_ALEX_RIVERA, mail FAKE_alex.rivera@example.test, phone FAKE_555_010_4444, at FAKE_100_TEST_STREET, key FAKE_SECRET_BC_ABC123_NOT_REAL")
        self.assertNotIn("FAKE_", text)
        self.assertEqual(counts, {"secret": 1, "email": 1, "phone": 1, "address": 1, "name": 1})

    def test_operational_ids_are_kept(self):
        text, counts = redact("user=FAKE_USER_882 acct FAKE_ACCT_0005 event FAKE_EVT_10028 rma FAKE_RMA_712")
        self.assertEqual(counts, {})
        self.assertIn("FAKE_USER_882", text)

    def test_a_secret_is_not_read_as_a_name(self):
        text, counts = redact("FAKE_SECRET_NOT_REAL_001")
        self.assertEqual(text, "[REDACTED_SECRET]")
        self.assertEqual(counts, {"secret": 1})


class AccessTests(unittest.TestCase):
    def test_open_documents_are_readable_by_everyone(self):
        self.assertTrue(can_read(None, SUPPORT))
        self.assertTrue(can_read("", SUPPORT))

    def test_deny_patterns_block_and_allow_wins(self):
        self.assertFalse(can_read("hr-restricted", SUPPORT))
        self.assertFalse(can_read("ai-security", SUPPORT))
        self.assertTrue(can_read("support-internal", SUPPORT))
        self.assertTrue(can_read("finance-restricted", FINANCE))
        self.assertFalse(can_read("legal-restricted", FINANCE))

    def test_denied_groups_lists_only_what_is_in_the_index(self):
        self.assertEqual(denied_groups(SUPPORT, {"public", "hr-restricted", "ai-security", None}), ["ai-security", "hr-restricted"])


if __name__ == "__main__":
    unittest.main()
