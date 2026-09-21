# Awesome AIDD Papers

AI-aided drug discovery papers with structured, source-linked research notes.

面向 **AI 辅助药物发现（AIDD）** 的论文整理。每篇记录 **发表期刊/会议与时间、主要痛点、数据集、方法、结论**，并补充评测条件、原文与代码链接。

首个专题为 **ADMET 与药代动力学**。目前收录 **19 篇**：14 篇正式研究/数据基准论文、1 篇正式观点文章、4 篇预印本。其中 **8 篇**建议优先精读。首批内容核验日期为 **2026-09-19**；仓库整理日期为 **2026-09-21**。后续更新以各条目核验日期为准。

## 导航

- [ADMET 论文总表](topics/admet.md)：按研究用途分类，逐篇保留五项核心信息。
- [优先精读](#优先精读)：先建立研究问题、数据和方法的认识。
- [筛选与 SOTA 判定](docs/curation.md)：如何判断结论可比、证据充分。
- [AIDD 研究范围](docs/scope.md)：当前覆盖与后续专题。
- [贡献方式](CONTRIBUTING.md)：推荐论文、纠正信息或补充实验依据。
- [结构化数据](data/papers.json) · [CSV 总表](data/papers.csv)。

| 专题 | 当前内容 | 入口 |
| --- | --- | --- |
| ADMET 与药代动力学 | 19 篇；其中 8 篇优先精读 | [论文总表](topics/admet.md) |
| 其他 AIDD 方向 | 扩展计划，尚未纳入独立专题 | [研究范围](docs/scope.md) |

## 优先精读

| 论文 | 期刊/会议 | 发表时间 | 一句话概括 |
| --- | --- | --- | --- |
| [ADMET可靠性评测](papers/admet/admet-reliability-2026.md) | Journal of Cheminformatics | 2026-05-18 | 在小样本、陌生分子结构和类别不均衡等条件下比较多类模型，检验 ADMET 预测在实际研究中是否可靠。 |
| [CaliciBoost](papers/admet/caliciboost-2025.md) | Journal of Cheminformatics | 2025-12-22 | 比较分子指纹和理化描述符，结合自动机器学习预测分子通过肠道细胞模型（Caco-2）的能力。 |
| [PKSmart](papers/admet/pksmart-2025.md) | Journal of Cheminformatics | 2025-09-26 | 先预测动物体内的药代参数，再结合分子结构预测人体静脉给药后的清除率、分布容积和半衰期等指标。 |
| [DCPM-ADMET](papers/admet/dcpm-admet-2026.md) | Journal of Cheminformatics | 2026-06-20 | 将两种预训练模型学到的分子表示与化学指纹结合，用于预测 97 项 ADMET 性质。 |
| [KPGT](papers/admet/kpgt-2023.md) | Nature Communications | 2023-11-21 | 把分子指纹和理化描述符融入图预训练，让模型学到更适合预测 ADMET 等性质的分子表示。 |
| [MolE](papers/admet/mole-2024.md) | Nature Communications | 2024-11-12 | 先在海量分子图上预训练，再利用生物学任务数据进一步训练，最后用于 ADMET 性质预测。 |
| [ADMET-AI](papers/admet/admet-ai-2024.md) | Bioinformatics | 2024-06-24 | 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。 |
| [MTGL-ADMET](papers/admet/mtgl-admet-2023.md) | iScience | 2023-11 | 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。 |

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
