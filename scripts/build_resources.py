"""Build bilingual dataset and comparison pages from reviewed, fixed snapshots."""
import csv
import io
import json
import math
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
METRIC_DIRECTIONS = {'MAE': 'lower', 'AUROC': 'higher', 'AUPRC': 'higher', 'Spearman': 'higher'}


def validate(datasets, records, papers):
    ids = {p['id'] for p in papers}
    dataset_by_id = {d['id']: d for d in datasets}
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
        dataset = dataset_by_id[r['dataset']]
        if r['size'] != dataset['size'] or r['metric'] != dataset['metric']:
            raise ValueError('Comparison does not match dataset size or metric')
        if METRIC_DIRECTIONS.get(r['metric']) != r['direction']:
            raise ValueError('Wrong ranking direction for metric')
        if r.get('source_kind') not in ['leaderboard', 'paper'] or not r.get('source_location'):
            raise ValueError('Comparison needs result provenance')
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
        if r['metric'] == 'Spearman' and not -1 <= r['mean'] <= 1:
            raise ValueError('Spearman score outside [-1,1]')
        if r['metric'] == 'MAE' and r['mean'] < 0:
            raise ValueError('MAE must be nonnegative')
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
        title = 'Endpoint comparisons' if en else '按端点对比'
        intro = (f'{endpoint_count} ADMET tasks, {len(records)} results from selected catalog methods. Sources checked: **{snapshot}**. Each table groups results reported under the TDC scaffold protocol with 20% held out for testing. Each score links to its leaderboard record or original paper table.' if en else
                 f'覆盖 {endpoint_count} 个 ADMET 任务、已收录方法的 {len(records)} 条结果。来源核对日期：**{snapshot}**。按 TDC 骨架划分、20% 留出测试的协议分组，每项成绩链接到榜单记录或原文表格。')
        protocol = ('Tables are sorted by mean performance: AUROC, AUPRC and Spearman ↑; MAE ↓. Values are mean ± standard deviation. Method names distinguish implementations such as Chemprop-RDKit and MapLight + GNN. Leaderboard scores describe those benchmark implementations; paper-table scores retain the authors’ experimental settings. Pretraining data and tuning budgets are described in the linked notes. The first row has the best mean among the methods collected here.' if en else
                    '表内按均值排序：AUROC、AUPRC 和 Spearman 越高越好，MAE 越低越好；数值为均值 ± 标准差。方法名区分 Chemprop-RDKit、MapLight + GNN 等实现。榜单成绩对应基准提交实现，论文表格成绩对应作者实验；预训练数据和调参设置见各篇笔记。首行表示本表已收录方法中的最高表现。')
        content = f'# {title}\n\n{switch.format(page="comparison")}\n\n'
        content += f'[{"Home" if en else "返回首页"}]({back}) · [{"Methods at a glance" if en else "按方法汇总"}](methods.md) · [{"Dataset dictionary" if en else "数据集字典"}](datasets.md)\n\n{intro}\n\n{protocol}\n\n'
        content += ('[TDC protocol](https://tdcommons.ai/benchmark/admet_group/overview/) · ' if en else '[TDC 评测协议](https://tdcommons.ai/benchmark/admet_group/overview/) · ')
        content += f'[CSV]({data_prefix}comparison.csv)\n\n'
        content += ('## Find an endpoint\n\n' if en else '## 按端点查找\n\n')
        navigation = []
        for dataset in dict.fromkeys(r['dataset'] for r in records):
            entries = [r for r in records if r['dataset'] == dataset]
            first = entries[0]
            direction = '↑' if first['direction'] == 'higher' else '↓'
            navigation.append([f'[{first["endpoint"]}](#{dataset.lower()})', dataset, f'{first["metric"]} {direction}', len(entries)])
        content += table(['Endpoint' if en else '端点', 'Dataset' if en else '数据集', 'Metric' if en else '指标', 'Methods' if en else '方法数'], navigation) + '\n\n'
        for dataset in dict.fromkeys(r['dataset'] for r in records):
            entries = [r for r in records if r['dataset'] == dataset]
            first = entries[0]
            entries.sort(key=lambda r: r['mean'], reverse=first['direction'] == 'higher')
            direction = '↑' if first['direction'] == 'higher' else '↓'
            content += f'## {dataset}\n\n{first["endpoint"]} · {first["size"]:,} {"molecules" if en else "个分子"} · {first["metric"]} {direction}\n\n'
            if dataset == 'Bioavailability_Ma':
                content += ('This table uses KPGT Supplementary Table 8 and MolE Table 1. The TDC Bioavailability page repeats multiple P-gp entries with identical means and standard deviations; those leaderboard rows are excluded here.\n\n' if en else
                            '本表采用 KPGT 补充表 8 和 MolE 表 1。TDC 的 Bioavailability 页面有多项均值与标准差和 P-gp 页面完全相同，这些榜单记录未纳入本表。\n\n')
            if dataset in ['PPBR_AZ', 'CYP3A4_Substrate_CarbonMangels']:
                content += ('KPGT’s reported dataset size or metric differs for this task; see the [experimental details](../papers/admet/kpgt-2023.md).\n\n' if en else
                            'KPGT 在此任务的原文规模或指标名称与本表不同，具体见[实验说明](../papers/admet/kpgt-2023.md)。\n\n')
            rows = []
            for r in entries:
                p = by_id[r['paper_id']]
                status = ('🟠 **Preprint**' if en else '🟠 **预印本**') if p['publication']['status'] == 'preprint' else ('Published' if en else '已发表')
                label = ('TDC leaderboard' if en else 'TDC 榜单') if r['source_kind'] == 'leaderboard' else r['source_location']
                rows.append([f'[{r["method"]}](../papers/{p["topic"]}/{p["id"]}.md)', status, f'{r["mean"]:.3f} ± {r["std"]:.3f}', f'[{label}]({r["source"]})'])
            content += table(['Method' if en else '方法', 'Publication' if en else '发表状态', 'Mean ± SD' if en else '均值 ± 标准差', 'Result source' if en else '成绩来源'], rows) + '\n\n'
        content += ('## External validation and uncertainty\n\n[PKSmart](../papers/admet/pksmart-2025.md) reports human PK on independent sources; [MC-PGP](../papers/admet/mc-pgp-2025.md) reports separate external inhibitor and substrate sets. [HERGAI](../papers/admet/hergai-2025.md) and [AmesNet](../papers/admet/amesnet-2026.md) define task-specific labels and test sets. Their notes include sample sizes, settings and results.\n\nFor confidence estimates, read [atom-based uncertainty](../papers/foundations/atom-uncertainty-2023.md) alongside [toxicity conformal prediction](../papers/admet/tox21-conformal-2021.md): calibration and interval/set coverage answer a different question from prediction accuracy.\n' if en else
                    '## 外部验证与不确定性\n\n[PKSmart](../papers/admet/pksmart-2025.md) 检验独立来源的人体药代数据；[MC-PGP](../papers/admet/mc-pgp-2025.md) 分别提供抑制剂与底物的外部验证。[HERGAI](../papers/admet/hergai-2025.md) 和 [AmesNet](../papers/admet/amesnet-2026.md) 使用各自的标签定义与测试集。各篇笔记列出样本数、设置和具体结果。\n\n预测可信度可结合[原子级不确定性](../papers/foundations/atom-uncertainty-2023.md)与[毒性共形预测](../papers/admet/tox21-conformal-2021.md)阅读，比较校准误差、预测区间或预测集合覆盖率。\n')
        content += ('\nFor metabolism and human PK, [MetaboGNN](../papers/admet/metabognn-2025.md) compares pretraining and species-difference tasks on microsomal stability; [MMPK](../papers/admet/mmpk-2025.md) reports oral PK by endpoint and external set. The [human clearance study](../papers/admet/human-clearance-bias-2024.md) compares predictions before and after training-neighbor exclusion, while the [CYP2C9 study](../papers/admet/cyp2c9-ml-validation-2022.md) connects model testing with new inhibition assays. Their result tables retain each study’s data and protocol.\n' if en else
                    '\n代谢与人体 PK 可沿 [MetaboGNN](../papers/admet/metabognn-2025.md) 比较微粒体稳定性的预训练与物种差异任务，沿 [MMPK](../papers/admet/mmpk-2025.md) 查看口服 PK 的逐端点和外部集结果。[人体清除率研究](../papers/admet/human-clearance-bias-2024.md) 比较训练近邻排除前后的误差，[CYP2C9 研究](../papers/admet/cyp2c9-ml-validation-2022.md) 将模型测试连接到新的抑制实验。各篇结果表保留对应的数据与协议。\n')
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
    return artifacts
