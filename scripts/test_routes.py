"""Check route references, coverage and propagation of catalog updates."""
import copy
import json
import unittest

import build
import build_en
import build_routes


class ReadingRouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = json.loads((build.ROOT / 'data/papers.json').read_text(encoding='utf-8'))['papers']
        cls.translations = json.loads((build.ROOT / 'data/papers.en.json').read_text(encoding='utf-8'))['papers']
        cls.routes = json.loads((build.ROOT / 'data/reading_routes.json').read_text(encoding='utf-8'))['routes']

    def test_bad_membership_or_reading_step_is_rejected(self):
        for mode in ('unknown', 'duplicate', 'step'):
            with self.subTest(mode=mode):
                routes = copy.deepcopy(self.routes)
                if mode == 'unknown':
                    routes[0]['papers'].append('missing-paper')
                elif mode == 'duplicate':
                    routes[0]['papers'].append(routes[0]['papers'][0])
                else:
                    routes[0]['steps'][0]['paper'] = 'missing-paper'
                with self.assertRaises(ValueError):
                    build_routes.validate(routes, self.papers)

    def test_new_paper_requires_route_assignment(self):
        papers = self.papers + [{'id': 'new-paper'}]
        with self.assertRaisesRegex(ValueError, 'without a reading route'):
            build_routes.validate(self.routes, papers)

    def test_catalog_corrections_reach_routes_in_date_order(self):
        papers, translations = copy.deepcopy(self.papers), copy.deepcopy(self.translations)
        p = next(p for p in papers if p['id'] == 'tdc-2021')
        p['publication']['date'] = '2099-01-01'
        p['title'] = 'Updated catalog title'
        p['one_liner'] = '更新后的概述'
        t = translations[p['id']]
        t['one_liner'] = 'Updated overview'
        t['source_sha256'] = build_en.source_hash(p)
        output = build_routes.build(papers, translations, build.table, self.routes)
        for path in ('topics/metabolism-pk.md', 'en/topics/metabolism-pk.md'):
            rows = [line for line in output[path].splitlines() if line.startswith('| 20')]
            self.assertIn('| 2099-01-01 | [Updated catalog title]', rows[0])
            self.assertIn('Updated overview' if path.startswith('en/') else '更新后的概述', rows[0])


if __name__ == '__main__':
    unittest.main()
