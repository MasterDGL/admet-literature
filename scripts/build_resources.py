"""Build bilingual dataset and comparison pages from reviewed, fixed snapshots."""
import csv
import io
import json
import math
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def validate(datasets, records, papers):
    ids = {p['id'] for p in papers}
    if len({d['id'] for d in datasets}) != len(datasets):
        raise ValueError('Duplicate dataset IDs')
    seen = set()
    protocols = {}
    for d in datasets:
        if not all(d.get(k) for k in ['id', 'name', 'collection', 'endpoint', 'metric', 'license', 'loader']):
            raise ValueError('Incomplete dataset record')
        if d['size'] <= 0 or d['endpoints'] <= 0:
            raise ValueError('Invalid dataset size')
        date.fromisoformat(d['checked_on'])
        for key in ['source', 'download', 'license_source']:
            if urlparse(d[key]).scheme != 'https':
                raise ValueError('Dataset URLs must use HTTPS')
    for r in records:
        if r['paper_id'] not in ids or r['dataset'] not in {d['id'] for d in datasets}:
            raise ValueError('Comparison references unknown paper or dataset')
        key = (r['dataset'], r['method'])
        if key in seen:
            raise ValueError('Duplicate comparison row')
        seen.add(key)
        protocol = tuple(r[k] for k in ['protocol', 'split', 'metric', 'direction', 'checked_on', 'size'])
        if r['dataset'] in protocols and protocols[r['dataset']] != protocol:
            raise ValueError('Incompatible protocols in one comparison table')
        protocols[r['dataset']] = protocol
        if r['direction'] not in ['higher', 'lower'] or not all(math.isfinite(r[k]) for k in ['mean', 'std']) or r['std'] < 0:
            raise ValueError('Invalid comparison metric')
        if r['metric'] in ['AUROC', 'AUPRC'] and not 0 <= r['mean'] <= 1:
            raise ValueError('Classification score outside [0,1]')
        date.fromisoformat(r['checked_on'])
        if urlparse(r['source']).scheme != 'https':
            raise ValueError('Comparison source must use HTTPS')


def csv_text(records):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=list(records[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(records)
    return '\ufeff' + out.getvalue()


def build(papers, table):
    datasets = json.loads((ROOT / 'data/datasets.json').read_text(encoding='utf-8'))['datasets']
    records = json.loads((ROOT / 'data/comparison.json').read_text(encoding='utf-8'))['records']
    validate(datasets, records, papers)
    by_id = {p['id']: p for p in papers}
    endpoint_count = len({r['endpoint'] for r in records})
    snapshot = max(r['checked_on'] for r in records)
    artifacts = {'data/comparison.csv': csv_text(records), 'data/datasets.csv': csv_text(datasets)}
    for en in [False, True]:
        prefix = 'en/' if en else ''
        back = '../../README.md' if en else '../README.zh-CN.md'
        data_prefix = '../../data/' if en else '../data/'
        switch = '**English** | [简体中文](../../docs/{page}.md)' if en else '[English](../en/docs/{page}.md) | **简体中文**'
        title = 'Method comparisons' if en else '方法对比'
        intro = (f'{endpoint_count} endpoint families, {len(records)} results from selected catalog methods. Latest snapshot: **{snapshot}**. Each table uses one TDC dataset, metric and scaffold-test protocol. Scores and standard deviations are reported leaderboard submissions, not independent reruns.' if en else
                 f'覆盖 {endpoint_count} 类端点、已收录方法的 {len(records)} 条结果，最近快照日期：**{snapshot}**。每张表对应一个 TDC 数据集、指标和骨架测试协议；均值和标准差取自榜单提交记录。')
        protocol = ('TDC holds out 20% for testing and uses scaffold splits. The method names identify specific implementations, including Chemprop-RDKit and MapLight + GNN. This selection compares catalog methods rather than reproducing the complete leaderboard. AUROC and AUPRC increase with performance; MAE decreases.' if en else
                    'TDC 使用骨架划分并保留 20% 作为测试集。方法名区分 Chemprop-RDKit、MapLight + GNN 等具体实现。表中选取仓库已收录的方法；AUROC/AUPRC 越高越好，MAE 越低越好。')
        interactive = '../../docs/comparison.html' if en else 'comparison.html'
        content = f'# {title}\n\n{switch.format(page="comparison")}\n\n'
        content += f'[{"Home" if en else "返回首页"}]({back}) · [{"Dataset dictionary" if en else "数据集字典"}](datasets.md)\n\n{intro}\n\n{protocol}\n\n'
        content += ('[TDC protocol](https://tdcommons.ai/benchmark/admet_group/overview/) · ' if en else '[TDC 评测协议](https://tdcommons.ai/benchmark/admet_group/overview/) · ')
        content += f'[CSV]({data_prefix}comparison.csv) · [{"Interactive table (download and open in a browser)" if en else "交互表（下载后用浏览器打开）"}]({interactive})\n\n'
        for dataset in dict.fromkeys(r['dataset'] for r in records):
            entries = [r for r in records if r['dataset'] == dataset]
            first = entries[0]
            entries.sort(key=lambda r: r['mean'], reverse=first['direction'] == 'higher')
            direction = '↑' if first['direction'] == 'higher' else '↓'
            content += f'## {first["endpoint"]} — {dataset}\n\n{first["size"]:,} {"molecules" if en else "个分子"} · {first["metric"]} {direction} · {first["checked_on"]} · [{"Scores" if en else "成绩来源"}]({first["source"]})\n\n'
            rows = []
            for r in entries:
                p = by_id[r['paper_id']]
                status = ('🟠 **Preprint**' if en else '🟠 **预印本**') if p['publication']['status'] == 'preprint' else ('Published' if en else '已发表')
                rows.append([f'[{r["method"]}](../papers/{p["topic"]}/{p["id"]}.md)', status, f'{r["mean"]:.3f} ± {r["std"]:.3f}'])
            content += table(['Method' if en else '方法', 'Publication' if en else '发表状态', 'Mean ± SD' if en else '均值 ± 标准差'], rows) + '\n\n'
        content += ('## Reading other experiments\n\nHERGAI uses its own curated hERG data; MC-PGP uses separate inhibitor and substrate sets; BBB MegaMolBART uses B3DB/CMUH; AmesNet models strain/S9 conditions. Their results remain in the individual notes because the test sets and labels differ from these TDC benchmarks. Uni-QSAR table values are retained in its paper notes, with the paper’s own evaluation context.\n' if en else
                    '## 其他实验怎么比较\n\nHERGAI 使用自行整理的 hERG 数据，MC-PGP 区分抑制剂和底物集，BBB MegaMolBART 使用 B3DB/CMUH，AmesNet 保留菌株/S9 条件。这些实验的测试集与标签不同，结果见各篇解读。Uni-QSAR 的表格成绩也保留在单篇笔记中，按其原文实验设置解读。\n')
        artifacts[prefix + 'docs/comparison.md'] = content
        title = 'Dataset dictionary' if en else '数据集字典'
        content = f'# {title}\n\n{switch.format(page="datasets")}\n\n[{"Home" if en else "返回首页"}]({back}) · [{"Comparisons" if en else "方法对比"}](comparison.md) · [CSV]({data_prefix}datasets.csv)\n\n'
        content += ('The first edition covers all 22 TDC ADMET benchmarks and eight commonly used MoleculeNet subsets. Counts refer to those named benchmark releases, rather than current database totals. Paper-specific curated datasets are described in each paper’s dataset field. Reviewed: **2026-09-22**.\n\n' if en else
                    '首版覆盖 TDC ADMET 的全部 22 个任务及 8 个常用 MoleculeNet 子集。规模对应表中基准版本，不代表数据库当前总量；论文自行整理的数据见各篇“数据集”字段。资料日期：**2026-09-22**。\n\n')
        content += ('TDC pages with “Not Specified” are recorded as unspecified even when a CC link appears beside the text. MoleculeNet aggregates data from multiple providers; entries marked “See original provider” do not yet have a separately recorded data license. Library code licenses and data licenses are separate.\n\n' if en else
                    'TDC 页面同时出现“Not Specified”和 CC 链接时，许可记为“未明确”。MoleculeNet 汇集多个来源，标为“见原始提供方”的条目尚未单独录入数据许可。工具库的代码许可与数据许可分别记录。\n\n')
        for collection in ['TDC ADMET Group', 'MoleculeNet']:
            rows = []
            for d in datasets:
                if d['collection'] != collection:
                    continue
                license = d['license'] if en else {'Not specified': '未明确', 'See original provider': '见原始提供方'}.get(d['license'], d['license'])
                rows.append([f'[{d["name"]}]({d["source"]})', f'{d["size"]:,}', d['endpoints'], d['endpoint'], f'[{license}]({d["license_source"]})', f'[{"Download / loader" if en else "下载与加载说明"}]({d["download"]})<br>`{d["loader"]}`'])
            content += f'## {collection}\n\n' + table(['Dataset' if en else '数据集', 'Size' if en else '规模', 'Endpoints' if en else '端点数', 'Task' if en else '任务', 'Data license' if en else '数据许可', 'Access' if en else '获取方式'], rows) + '\n\n'
        content += ('## Loading the benchmark splits\n\n' if en else '## 加载基准划分\n\n') + '```python\nfrom tdc.benchmark_group import admet_group\ngroup = admet_group(path="data/")\nbenchmark = group.get("Caco2_Wang")\ntrain_val, test = benchmark["train_val"], benchmark["test"]\n```\n\n'
        content += ('Use `benchmark_group` for the comparison protocol; calling a single-task loader with its defaults can produce a different split. BBBP (MoleculeNet, 2,039) and BBB_Martins (TDC, 1,975) retain distinct entries. HIV measures antiviral activity and is included as a representation-learning benchmark.\n' if en else
                    '方法对比使用 `benchmark_group` 的划分；单任务加载器的默认划分可能不同。BBBP（MoleculeNet，2,039）与 BBB_Martins（TDC，1,975）分别保留。HIV 测量抗病毒活性，在这里作为表示学习基准。\n')
        artifacts[prefix + 'docs/datasets.md'] = content
    template = (ROOT / 'templates/comparison.html').read_text(encoding='utf-8')
    enriched = [dict(r, publication=by_id[r['paper_id']]['publication']['status']) for r in records]
    artifacts['docs/comparison.html'] = template.replace('__RECORDS__', json.dumps(enriched, ensure_ascii=True).replace('<', '\\u003c'))
    return artifacts
