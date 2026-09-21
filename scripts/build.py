"""Build the public literature catalog from data/papers.json (Python 3.10+)."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
GROUPS = ['核心论文', '专题补读', '数据与基准', '观点文章', '预印本']
REQUIRED = ['id', 'name', 'title', 'topic', 'group', 'publication', 'tags',
            'pain_point', 'datasets', 'method', 'conclusion', 'limitations',
            'evaluation', 'paper_url', 'sources', 'verified_on', 'verification_scope']


def validate(papers):
    ids, titles = set(), set()
    for p in papers:
        for key in REQUIRED:
            if not p.get(key):
                raise ValueError(f'{p.get("id")}: missing {key}')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', p['id']):
            raise ValueError(f'Invalid id: {p["id"]}')
        if p['id'] in ids or p['title'].casefold() in titles:
            raise ValueError(f'Duplicate: {p["id"]}')
        ids.add(p['id']); titles.add(p['title'].casefold())
        if p['group'] not in GROUPS or p['topic'] != 'admet':
            raise ValueError(f'Unsupported group/topic: {p["id"]}')
        pub = p['publication']
        for k in ['venue', 'year', 'date', 'date_basis', 'status', 'citation']:
            if not pub.get(k):
                raise ValueError(f'{p["id"]}: missing publication.{k}')
        if not re.fullmatch(r'\d{4}(-\d{2}){0,2}', pub['date']):
            raise ValueError(f'Invalid publication date: {p["id"]}')
        if int(pub['date'][:4]) != pub['year']:
            raise ValueError(f'Inconsistent publication year: {p["id"]}')
        parts = pub['date'].split('-')
        date(*([int(v) for v in parts] + [1] * (3 - len(parts))))
        date.fromisoformat(p['verified_on'])
        if pub['status'] not in ['journal', 'conference', 'preprint']:
            raise ValueError(f'Invalid publication status: {p["id"]}')
        if (pub['status'] == 'preprint') != (p['group'] == '预印本'):
            raise ValueError(f'Preprint classification mismatch: {p["id"]}')
        urls = [p['paper_url']] + [s['url'] for s in p['sources']] + [p.get('code_url')]
        for url in filter(None, urls):
            parsed = urlparse(url)
            if parsed.scheme not in ['https', 'http'] or not parsed.netloc:
                raise ValueError(f'Invalid URL: {url}')


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                      '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows])


def note_path(p):
    return f'papers/admet/{p["id"]}.md'


def card(p):
    pub = p['publication']
    status = {'journal': '正式期刊论文', 'conference': '正式会议论文', 'preprint': '预印本'}[pub['status']]
    fields = [['发表期刊/会议与时间', pub['citation']],
              ['日期口径', pub['date_basis']], ['发表状态', status],
              ['主要痛点', p['pain_point']], ['数据集', p['datasets']],
              ['方法', p['method']], ['结论', p['conclusion']]]
    sources = '\n'.join(f'- [{s["label"]}]({s["url"]})' for s in p['sources'])
    code = f'[代码或项目入口]({p["code_url"]})' if p.get('code_url') else p['code_status']
    doi = f'\nDOI：`{p["doi"]}`\n' if p.get('doi') else ''
    return f'''# {p['name']}

**{p['title']}**

[返回 ADMET 总表](../../topics/admet.md) · [返回首页](../../README.md)

分类：{p['group']}。主题：{'、'.join(p['tags'])}。

{table(['字段', '内容'], fields)}
{doi}
## 评测与结论适用范围

{p['evaluation']}

{p['limitations']}

## 代码与证据

{code}

代码状态：{p['code_status']}。复现状态：本仓库未独立复现实验。

内容核验日期：**{p['verified_on']}**。核对范围：{p['verification_scope']}。

{sources}
'''


def build(papers):
    artifacts = {note_path(p): card(p) for p in papers}
    count = Counter(p['group'] for p in papers)
    formal_research = sum(p['publication']['status'] != 'preprint' and p['group'] != '观点文章' for p in papers)
    nav = table(['专题', '当前内容', '入口'], [
        ['ADMET 与药代动力学', f'{len(papers)} 篇；其中 {count["核心论文"]} 篇优先精读', '[论文总表](topics/admet.md)'],
        ['其他 AIDD 方向', '扩展计划，尚未纳入独立专题', '[研究范围](docs/scope.md)']])
    core = table(['论文', '期刊/会议', '发表时间', '阅读重点'], [
        [f'[{p["name"]}]({note_path(p)})', p['publication']['venue'], p['publication']['date'], '、'.join(p['tags'])]
        for p in papers if p['group'] == '核心论文'])
    artifacts['README.md'] = f'''# Awesome AIDD Papers

AI-aided drug discovery papers with structured, source-linked research notes.

面向 **AI 辅助药物发现（AIDD）** 的论文整理。每篇记录 **发表期刊/会议与时间、主要痛点、数据集、方法、结论**，并补充评测条件、原文与代码链接。

首个专题为 **ADMET 与药代动力学**。目前收录 **{len(papers)} 篇**：{formal_research} 篇正式研究/数据基准论文、{count['观点文章']} 篇正式观点文章、{count['预印本']} 篇预印本。其中 **{count['核心论文']} 篇**建议优先精读。首批内容核验日期为 **2026-09-19**；仓库整理日期为 **2026-09-21**。后续更新以各条目核验日期为准。

## 导航

- [ADMET 论文总表](topics/admet.md)：按研究用途分类，逐篇保留五项核心信息。
- [优先精读](#优先精读)：先建立研究问题、数据和方法的认识。
- [筛选与 SOTA 判定](docs/curation.md)：如何判断结论可比、证据充分。
- [AIDD 研究范围](docs/scope.md)：当前覆盖与后续专题。
- [贡献方式](CONTRIBUTING.md)：推荐论文、纠正信息或补充实验依据。
- [结构化数据](data/papers.json) · [CSV 总表](data/papers.csv)。

{nav}

## 优先精读

{core}

建议顺序：**真实场景评测 → 单端点与人体 PK → 表示学习与多任务方法 → 平台应用**。专题总表另列数据基准、观点文章和预印本，便于区分它们提供的证据。

## 怎样理解这里的 SOTA

领先结论必须对应 **任务、数据版本、数据划分、指标、比较对象和时间**。本仓库保留论文报告和公开榜单的适用范围，不将历史领先结果统一标为当前最优。所有条目均为文献整理，尚未由本仓库独立复现实验。

每篇论文有独立解读页；代码入口、权重可用性与实验复现分别记录。正式发表的 Perspective 也会明确标注，避免当作新模型的性能证据。

## 数据与维护

`data/papers.json` 是论文条目的维护入口。使用 Python 3.10 或更新版本，无第三方依赖：

```bash
python scripts/build.py
python scripts/build.py --check
```

第一条命令更新首页、专题总表、单篇解读及 CSV；第二条检查必填字段、重复记录、日期口径、URL 格式、内部链接和生成文件一致性。该检查不替代文献事实核验或外部链接在线检查。

## 参考与致谢

组织方式参考 [awesome-AIDD](https://github.com/daiyun02211/awesome-AIDD) 的主题导航、[Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) 的论文与代码索引。关注 [OpenADMET](https://github.com/OpenADMET) 的开放数据与评测实践。本仓库是独立的文献整理项目。

原创整理内容和维护脚本采用 [MIT License](LICENSE)。所引用论文、数据与第三方代码遵循各自的许可；本仓库提供链接与原创摘要，不分发论文全文。
'''
    sections = []
    for group in GROUPS:
        entries = sorted([p for p in papers if p['group'] == group], key=lambda p: p['publication']['date'], reverse=True)
        rows = [[f'[{p["name"]}](../{note_path(p)}) · [原文]({p["paper_url"]})',
                 p['publication']['citation'], p['pain_point'], p['datasets'], p['method'], p['conclusion']]
                for p in entries]
        sections.append(f'## {group}\n\n' + table(['论文与解读', '期刊/会议与时间', '主要痛点', '数据集', '方法', '结论'], rows))
    artifacts['topics/admet.md'] = '''# ADMET 与药代动力学论文

[返回首页](../README.md) · [筛选规则](../docs/curation.md) · [下载 CSV](../data/papers.csv)

ADMET 指吸收、分布、代谢、排泄和毒性。相关理化性质与人体 PK 也在本专题范围内；通用分子模型仅在具有相关实验证据时纳入。

内容核验截至 **2026-09-19**。以下分组反映研究用途；组内按发表日期倒序。表中的结论均来自条目列出的文献或明确日期的榜单快照，点击论文名查看评测设置与限制。

''' + '\n\n'.join(sections) + '\n'
    buf = io.StringIO(newline='')
    writer = csv.writer(buf)
    writer.writerow(['ID','论文简称','完整题名','分类','主题','期刊或会议','发表时间','日期口径','发表状态','主要痛点','数据集','方法','结论','评测设置','限制','原文URL','代码URL','代码状态','核验日期','核对范围'])
    for p in papers:
        pub = p['publication']
        writer.writerow([p['id'],p['name'],p['title'],p['group'],'; '.join(p['tags']),pub['venue'],pub['date'],pub['date_basis'],pub['status'],p['pain_point'],p['datasets'],p['method'],p['conclusion'],p['evaluation'],p['limitations'],p['paper_url'],p.get('code_url') or '',p['code_status'],p['verified_on'],p['verification_scope']])
    artifacts['data/papers.csv'] = '\ufeff' + buf.getvalue()
    return artifacts


def check_links(artifacts):
    for relative, text in artifacts.items():
        if not relative.endswith('.md'):
            continue
        for target in re.findall(r'\]\(([^)]+)\)', text):
            target = target.split('#')[0]
            if not target or urlparse(target).scheme:
                continue
            resolved = (ROOT / relative).parent.joinpath(target).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                raise ValueError(f'Broken local link in {relative}: {target}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    papers = catalog['papers']
    validate(papers)
    artifacts = build(papers)
    stale = []
    for relative, content in artifacts.items():
        dest = ROOT / relative
        if args.check:
            if not dest.exists() or dest.read_bytes() != content.encode('utf-8'):
                stale.append(relative)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(content.encode('utf-8'))
    if stale:
        raise SystemExit('Generated files differ: ' + ', '.join(stale))
    all_markdown = {f.relative_to(ROOT).as_posix(): f.read_text(encoding='utf-8') for f in ROOT.rglob('*.md')}
    check_links(all_markdown)
    for f in (ROOT / 'papers/admet').glob('*.md'):
        if f.relative_to(ROOT).as_posix() not in artifacts:
            raise ValueError(f'Unexpected paper file: {f.name}')
    print(f'{len(papers)} records validated; {len(artifacts)} generated files checked.' if args.check else f'Built {len(papers)} paper cards and catalog.')


if __name__ == '__main__':
    main()
