"""Checks for ranking mathematics and explicit comparison-cohort membership."""
import copy
import json
import unittest
from collections import defaultdict

import build_methods as methods


class MethodSummaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        def read(name, key=None):
            value = json.loads((methods.ROOT / 'data' / name).read_text(encoding='utf-8'))
            return value[key] if key else value
        cls.config = read('methods.json')
        cls.records = read('comparison.json', 'records')
        cls.datasets = read('datasets.json', 'datasets')
        cls.papers = read('papers.json', 'papers')

    def validate(self, config=None, records=None):
        methods.validate(config if config is not None else self.config,
                         records if records is not None else self.records,
                         self.datasets, self.papers)

    def test_metric_direction_and_ties(self):
        scores = {'a': 0.2, 'b': 0.1, 'c': 0.1, 'd': 0.3}
        self.assertEqual(methods.average_ranks(scores, 'lower'), {'b': 1.5, 'c': 1.5, 'a': 3, 'd': 4})
        self.assertEqual(methods.average_ranks(scores, 'higher'), {'d': 1, 'a': 2, 'b': 3.5, 'c': 3.5})
        self.assertEqual(methods.average_ranks({'a': 1, 'b': 1, 'c': 1}, 'higher'), {'a': 2, 'b': 2, 'c': 2})

    def test_missing_score_does_not_shrink_cohort(self):
        records = [r for r in self.records if not (r['method'] == 'MolE' and r['dataset'] == 'Caco2_Wang')]
        with self.assertRaisesRegex(ValueError, 'Missing result in fixed cohort'):
            self.validate(records=records)

    def test_protocol_changes_require_review(self):
        records = copy.deepcopy(self.records)
        for row in records:
            if row['dataset'] == 'Caco2_Wang':
                row['split'] = 'random 80:20'
        with self.assertRaisesRegex(ValueError, 'reviewed cohort protocol'):
            self.validate(records=records)

    def test_omitted_or_duplicated_tasks_are_rejected(self):
        config = copy.deepcopy(self.config)
        config['cohort']['datasets'].pop()
        with self.assertRaisesRegex(ValueError, 'partition'):
            self.validate(config=config)
        config = copy.deepcopy(self.config)
        config['cohort']['datasets'].append(config['cohort']['datasets'][0])
        with self.assertRaisesRegex(ValueError, 'unique'):
            self.validate(config=config)

    def test_unknown_implementations_need_metadata(self):
        records = copy.deepcopy(self.records)
        extra = dict(records[0], method='New implementation')
        records.append(extra)
        with self.assertRaisesRegex(ValueError, 'match all result implementations'):
            self.validate(records=records)

    def test_fixed_cohort_arithmetic_and_specialists(self):
        summaries, ranked = methods.summarize(self.config, self.records, self.datasets, self.papers)
        cohort = self.config['cohort']
        n, k = len(cohort['methods']), len(cohort['datasets'])
        self.assertEqual(len(ranked), n * k)
        ranks_by_task = defaultdict(list)
        for r in ranked:
            ranks_by_task[r['dataset']].append(r['rank'])
        for ranks in ranks_by_task.values():
            self.assertEqual(sum(ranks), n * (n + 1) / 2)
        for s in summaries:
            if s['method'] in cohort['methods']:
                values = [r['rank'] for r in ranked if r['method'] == s['method']]
                self.assertEqual(s['ranked_tasks'], k)
                self.assertAlmostEqual(s['mean_rank'], sum(values) / k)
                self.assertEqual(s['top3_tasks'], sum(v <= 3 for v in values))
            else:
                self.assertEqual(s['ranked_tasks'], 0)
                self.assertEqual(s['mean_rank'], '')
                self.assertEqual(s['top3_tasks'], '')

    def test_record_order_does_not_change_results(self):
        expected = methods.summarize(self.config, self.records, self.datasets, self.papers)
        actual = methods.summarize(self.config, list(reversed(self.records)), self.datasets, self.papers)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
