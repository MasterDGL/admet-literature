import copy
import json
import unittest

import build
import build_resources


class ResourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = json.loads((build.ROOT / 'data/papers.json').read_text(encoding='utf-8'))['papers']
        cls.datasets = json.loads((build.ROOT / 'data/datasets.json').read_text(encoding='utf-8'))['datasets']
        cls.records = json.loads((build.ROOT / 'data/comparison.json').read_text(encoding='utf-8'))['records']

    def test_incompatible_test_protocols_cannot_share_a_table(self):
        changed = copy.deepcopy(self.records)
        changed[1]['split'] = 'random'
        with self.assertRaisesRegex(ValueError, 'Incompatible protocols'):
            build_resources.validate(self.datasets, changed, self.papers)

    def test_missing_paper_reference_is_rejected(self):
        changed = copy.deepcopy(self.records)
        changed[0]['paper_id'] = 'missing-paper'
        with self.assertRaisesRegex(ValueError, 'unknown paper'):
            build_resources.validate(self.datasets, changed, self.papers)

    def test_invalid_classification_score_is_rejected(self):
        changed = copy.deepcopy(self.records)
        next(r for r in changed if r['metric'] == 'AUROC')['mean'] = 88
        with self.assertRaisesRegex(ValueError, 'outside'):
            build_resources.validate(self.datasets, changed, self.papers)


if __name__ == '__main__':
    unittest.main()
