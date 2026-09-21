# ADMET可靠性评测

**Revisiting ADMET prediction reliability under real-world challenges in the foundation model era**

[返回 ADMET 总表](../../topics/admet.md) · [返回首页](../../README.md)

分类：核心论文。主题：泛化、小样本、评测。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 18, 95；2026-05-18 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 常规平均成绩不足以反映小样本、分布外预测、类别不均衡、超出五规则的分子及活性悬崖中的可靠性。 |
| 数据集 | 14 个性质/ADMET 相关数据集，涵盖 hERG、BBBP、Caco-2、半衰期、VDss、CYP 及肽性质等；另外使用 MoleculeACE 的 30 个生物活性任务。 |
| 方法 | 在统一实验框架中比较 KPGT、Uni-Mol、TabPFNv2、经典机器学习及 AutoML；采用随机、骨架和 Perimeter 划分，并研究重采样与集成。 |
| 结论 | 在所测小样本/OOD 场景中，TabPFNv2 常有优势；欠采样集成有助于不均衡问题；数据较充足时 KPGT 在环肽渗透性上表现突出；活性悬崖仍是共同难点。 |

DOI：`10.1186/s13321-026-01217-2`

## 评测与结论适用范围

比较随机、骨架和 Perimeter 划分；不同挑战使用不同子集，不是 TDC 22 任务统一榜单。

重点看 Table 1、Results 各场景及 Methods；论文报告环肽 CycPept-PAMPA 上 KPGT 的 R² 为 0.627。该结果针对其数据与划分；不代表任何基础模型在所有端点上都优于其他方法。

## 代码与证据

[代码或项目入口](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)

代码状态：存在作者代码/项目入口；未独立验证安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-19**。核对范围：书目、正文关键部分及相关官方资源。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-026-01217-2)
- [作者代码](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)
