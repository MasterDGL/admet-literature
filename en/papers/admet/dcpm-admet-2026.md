# DCPM-ADMET: fusion of dual-component pre-trained model and molecular fingerprints to enhance drug ADMET properties prediction

**English** | [简体中文](../../../papers/admet/dcpm-admet-2026.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2026-06-20* · Published · Core papers

**Overview:** Combines representations from two pretrained models with chemical fingerprints to predict 97 ADMET properties.

Topics: ADMET, Pretraining, Representation fusion.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 18, 126; 2026-06-20 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | A single representation struggles to capture semantic, structural and physicochemical information together, while ADMET labels are sparse and endpoints heterogeneous. |
| Datasets | Pretraining uses approximately 111 million PubChem records. The ADMET collection contains 97 endpoints: 43 regression and 54 classification tasks, with 465,470 endpoint records. Also evaluates 10 MoleculeNet datasets. |
| Method | Fuses XLNet semantic representations, a GRU component incorporating SMILES-to-InChI and property learning, and ECFP fingerprints; combines single-task random forests, multitask neural networks and parameter optimization. |
| Findings | Improves over ECFP on 67/97 endpoints (39 classification, 28 regression). Mean classification AUC increases from 0.812 to 0.831; mean regression Pearson r increases from 0.661 to 0.701. |

DOI: `10.1186/s13321-026-01244-z`

## Experimental setup and analysis

**Design.** An 8:1:1 Bemis–Murcko scaffold train/validation/test split and five independent runs. Frozen XLNet and RNN encoders each supply 512 features, concatenated with 512-bit ECFP. Single-task prediction uses random forests; multi-task prediction uses a DNN. TPE searches 50 configurations; frozen and full fine-tuning strategies are compared.

| Comparison on the 97-endpoint collection | ECFP | DCPM-ADMET |
| --- | --- | --- |
| Mean AUC across 54 classification tasks ↑ | 0.812 | 0.831 |
| Mean Pearson r across 43 regression tasks ↑ | 0.661 | 0.701 |
| Tasks improved over ECFP | — | 39/54 classification; 28/43 regression |

Locations: Fine-tuning and ADMET prediction models; endpoint results are indexed in Supplementary Tables S6–S7. The separate 10-dataset MoleculeNet comparison is a distinct evaluation.

These improvements compare fused features with this study’s ECFP baseline. The platform’s 133 outputs comprise 97 learned endpoints and 36 computed properties; endpoint records are not a count of unique compounds.

## Code and references

[Code and project](https://github.com/zhangzhangleilei/DCPM-ADMET)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Checked training protocol, aggregate 97-endpoint results and supplementary table references

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-026-01244-z)
- [Author code](https://github.com/zhangzhangleilei/DCPM-ADMET)
