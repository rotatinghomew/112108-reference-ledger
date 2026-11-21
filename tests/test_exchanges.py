import json
from pathlib import Path
import unittest

DATA = Path(__file__).resolve().parent.parent / "data" / "exchanges.jsonl"
REFERENCES = [('use', 'grant', 'grant', 'id'), ('loan', 'use', 'use', 'id'), ('offset', 'target', 'cost', 'id')]


class ExchangeMaterials(unittest.TestCase):
    """只校验来源交换件本身。"""

    @classmethod
    def setUpClass(cls):
        cls.rows = [json.loads(line) for line in DATA.read_text(encoding="utf-8").splitlines()]

    def test_order_and_record_shapes(self):
        steps = [row["step"] for row in self.rows]
        self.assertEqual(sorted(set(steps)), list(range(1, max(steps) + 1)))
        self.assertEqual(steps, sorted(steps))
        for row in self.rows:
            self.assertEqual(set(row), {"step", "kind", "body"})
            self.assertTrue(row["body"])

    def test_cross_documents(self):
        for kind, field, other_kind, other_field in REFERENCES:
            expected = {row["body"][other_field] for row in self.rows if row["kind"] == other_kind}
            related = [row["body"][field] for row in self.rows if row["kind"] == kind]
            self.assertTrue(related)
            self.assertTrue(set(related) <= expected, (kind, field))
