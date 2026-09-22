"""Generate bilingual reading routes from curated memberships and catalog facts."""
from __future__ import annotations

import json
from pathlib import Path
import re

import build_en

ROOT = Path(__file__).resolve().parents[1]


def validate(routes, papers):
    known = {p['id'] for p in papers}
    seen, covered = set(), set()
    for route in routes:
        key = route['id']
        if not re.fullmatch(r'[a-z]+(?:-[a-z]+)*', key) or key in seen:
            raise ValueError(f'Invalid or duplicate route: {key}')
        seen.add(key)
        members = route['papers']
        if not members or len(members) != len(set(members)) or set(members) - known:
            raise ValueError(f'{key}: invalid paper membership')
        covered.update(members)
        steps = route['steps']
        step_ids = [step['paper'] for step in steps]
        if not steps or set(step_ids) - set(members) or len(step_ids) != len(set(step_ids)):
            raise ValueError(f'{key}: invalid reading steps')
        for lang in ('zh', 'en'):
            text = route[lang]
            if not all(isinstance(text.get(k), str) and text[k].strip() for k in ('title', 'intro')):
                raise ValueError(f'{key}: incomplete {lang} text')
            if not text.get('questions') or not all(isinstance(q, str) and q.strip() for q in text['questions']):
                raise ValueError(f'{key}: missing {lang} questions')
            if not all(isinstance(step.get(lang), str) and step[lang].strip() for step in steps):
                raise ValueError(f'{key}: missing {lang} step text')
    if covered != known:
        raise ValueError(f'Papers without a reading route: {sorted(known - covered)}')


def build(papers, translations, table, routes=None):
    if routes is None:
        routes = json.loads((ROOT / 'data/reading_routes.json').read_text(encoding='utf-8'))['routes']
    validate(routes, papers)
    artifacts = {}
    for lang, localized in [('zh', papers), ('en', build_en.localize(papers, translations))]:
        en = lang == 'en'
        prefix = 'en/' if en else ''
        catalog = {p['id']: p for p in localized}
        home = '../../README.md' if en else '../README.zh-CN.md'
        title = 'Reading by research question' if en else '按研究问题阅读'
        switch = ('**English** | [简体中文](../../docs/reading-routes.md)' if en
                  else '[English](../en/docs/reading-routes.md) | **简体中文**')
        intro = ('Choose a question, follow the suggested reading sequence, then browse the papers from newest to oldest. A paper can appear in several routes; each link opens its full note.' if en else
                 '先选择研究问题，沿建议顺序精读，再按时间查看相关论文。一篇论文可以出现在多条路线中，链接均指向同一篇完整笔记。')
        rows = [[f'[{r[lang]["title"]}](../topics/{r["id"]}.md)', r[lang]['intro'], str(len(r['papers']))] for r in routes]
        count_note = ('Route counts overlap; they are not added together.' if en else '各路线包含交叉收录，篇数不相加。')
        navigation = (f'[Home]({home}) · [Knowledge map](knowledge-map.md) · [Method comparisons](comparison.md) · [Datasets](datasets.md)' if en else
                      f'[返回首页]({home}) · [知识地图](knowledge-map.md) · [方法对比](comparison.md) · [数据集字典](datasets.md)')
        artifacts[f'{prefix}docs/reading-routes.md'] = f'# {title}\n\n{switch}\n\n{navigation}\n\n{intro}\n\n' + table(['Route', 'Research focus', 'Papers'] if en else ['路线', '研究重点', '篇数'], rows) + f'\n\n{count_note}\n'
        for route in routes:
            key, text = route['id'], route[lang]
            switch = (f'**English** | [简体中文](../../topics/{key}.md)' if en else
                      f'[English](../en/topics/{key}.md) | **简体中文**')
            nav = (f'[Home]({home}) · [All reading routes](../docs/reading-routes.md) · [Knowledge map](../docs/knowledge-map.md)' if en else
                   f'[返回首页]({home}) · [全部阅读路线](../docs/reading-routes.md) · [知识地图](../docs/knowledge-map.md)')
            separator = ': ' if en else '：'
            steps = '\n'.join(f'{i}. [{catalog[s["paper"]]["name"]}](../papers/{catalog[s["paper"]]["topic"]}/{s["paper"]}.md){separator}{s[lang]}' for i, s in enumerate(route['steps'], 1))
            questions = '\n'.join('- ' + q for q in text['questions'])
            rows = []
            for p in build_en.recent_first([catalog[id] for id in route['papers']]):
                rows.append([p['publication']['date'], f'[{p["title"]}](../papers/{p["topic"]}/{p["id"]}.md)', p['publication']['venue'], build_en.publication_label(p, en), p['one_liner']])
            headings = ['Suggested reading order', 'Questions to compare', 'Papers, newest first'] if en else ['建议阅读顺序', '阅读时比较什么', '相关论文：由新到旧']
            columns = ['Date', 'Paper', 'Venue', 'Status', 'Overview'] if en else ['时间', '论文', '期刊/会议', '状态', '内容概述']
            artifacts[f'{prefix}topics/{key}.md'] = f'# {text["title"]}\n\n{switch}\n\n{nav}\n\n{text["intro"]}\n\n## {headings[0]}\n\n{steps}\n\n## {headings[1]}\n\n{questions}\n\n## {headings[2]}\n\n' + table(columns, rows) + '\n'
    return artifacts
