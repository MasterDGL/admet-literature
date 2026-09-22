"""Regression checks for bilingual generation. Run: python scripts/test_build.py."""
import copy
import csv
import io
import json
import posixpath
import re
import unittest

import build
import build_en


class BilingualCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = json.loads((build.ROOT / 'data/papers.json').read_text(encoding='utf-8'))['papers']
        cls.translations = json.loads((build.ROOT / 'data/papers.en.json').read_text(encoding='utf-8'))['papers']
        cls.artifacts = build.bilingual(cls.papers, cls.translations)

    def test_localization_preserves_shared_facts_and_source(self):
        original = copy.deepcopy(self.papers)
        english = build_en.localize(self.papers, self.translations)
        self.assertEqual(self.papers, original)
        for zh, en in zip(self.papers, english):
            for field in ['id', 'title', 'doi', 'paper_url', 'code_url', 'verified_on', 'topic', 'group']:
                self.assertEqual(zh.get(field), en.get(field))
            for field in ['venue', 'year', 'date', 'status']:
                self.assertEqual(zh['publication'][field], en['publication'][field])
            self.assertEqual([s['url'] for s in zh['sources']], [s['url'] for s in en['sources']])

    def test_changed_source_requires_translation_review(self):
        changed = copy.deepcopy(self.papers)
        changed[0]['conclusion'] += ' Source updated.'
        with self.assertRaisesRegex(ValueError, 'needs review'):
            build_en.localize(changed, self.translations)

    def test_missing_translation_is_rejected(self):
        incomplete = copy.deepcopy(self.translations)
        incomplete.pop(self.papers[-1]['id'])
        with self.assertRaisesRegex(ValueError, 'match all catalog IDs'):
            build_en.localize(self.papers, incomplete)

    def test_incomplete_translation_is_rejected(self):
        incomplete = copy.deepcopy(self.translations)
        incomplete[self.papers[0]['id']]['datasets'] = '  '
        with self.assertRaisesRegex(ValueError, 'empty or invalid'):
            build_en.localize(self.papers, incomplete)

    def test_language_switches_are_reciprocal(self):
        documents = {p.relative_to(build.ROOT).as_posix(): p.read_text(encoding='utf-8')
                     for p in build.ROOT.rglob('*.md')}
        documents.update({p: text for p, text in self.artifacts.items() if p.endswith('.md')})
        for en_path in ['README.md'] + [p for p in documents if p.startswith('en/')]:
            zh_path = 'README.zh-CN.md' if en_path == 'README.md' else en_path.removeprefix('en/')
            self.assertIn(zh_path, documents)
            for source, target, label in [(en_path, zh_path, '简体中文'), (zh_path, en_path, 'English')]:
                expected = posixpath.relpath(target, posixpath.dirname(source) or '.')
                self.assertIn(f'[{label}]({expected})', documents[source].splitlines()[2])
            # English prose may contain Chinese only in the language selector.
            body = '\n'.join(line for i, line in enumerate(documents[en_path].splitlines()) if i != 2)
            self.assertIsNone(re.search(r'[\u4e00-\u9fff]', body), en_path)

    def test_homepage_anchors_and_language_routes(self):
        for path, prefix in [('README.md', 'en/'), ('README.zh-CN.md', '')]:
            text = self.artifacts[path]
            headings = re.findall(r'^#{1,6} (.+)$', text, re.M)
            anchors = [re.sub(r'[^\w\s-]', '', h.lower()).replace(' ', '-') for h in headings]
            self.assertEqual(len(anchors), len(set(anchors)), path)
            for fragment in re.findall(r'\]\(#([^)]+)\)', text):
                self.assertIn(fragment, anchors, (path, fragment))
            for paper in self.papers:
                self.assertIn('](' + prefix + build.note_path(paper) + ')', text)
        self.assertTrue(self.artifacts['README.md'].startswith('# ADMET Literature\n'))

    def test_csvs_keep_matching_records(self):
        zh = list(csv.reader(io.StringIO(self.artifacts['data/papers.csv'].lstrip('\ufeff'))))
        en = list(csv.reader(io.StringIO(self.artifacts['data/papers.en.csv'].lstrip('\ufeff'))))
        self.assertEqual(len(zh), len(self.papers) + 1)
        self.assertEqual([r[0] for r in zh[1:]], [r[0] for r in en[1:]])
        for a, b in zip(zh[1:], en[1:]):
            for col in [2, 7, 8, 10, 17, 18, 20]:
                self.assertEqual(a[col], b[col])


if __name__ == '__main__':
    unittest.main()
