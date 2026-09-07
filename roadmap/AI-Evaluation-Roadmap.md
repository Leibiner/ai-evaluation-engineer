# AI Evaluation Engineer Roadmap

## 目标

从传统软件测试工程师出发，形成能够理解 AI、设计 Evaluation、构建评估系统并负责生产 AI 质量的完整能力。

## 四层能力模型

```text
Layer 1  AI Understanding
  AI / ML → LLM → Model Behavior

Layer 2  Evaluation Science
  Target → Dataset → Grader → Metric → Statistics

Layer 3  System Evaluation
  LLM → RAG → Agent → Safety → Multimodal → Reliability

Layer 4  Quality Engineering
  Harness → Regression → EvalOps → Production → Business
```

## 9 个阶段

### Phase 01 — AI / ML Foundations

先理解学习系统：Dataset、Label、Model、Prediction、Loss、Training、Validation、Test、Generalization、Distribution Shift、Leakage。

**出口：** 能解释模型为什么学会、为什么犯错，以及为什么测试集才能帮助判断泛化。

### Phase 02 — LLM Foundations

Token、Embedding、Transformer、Attention、Context、Inference、Sampling、Structured Output。

**出口：** 能解释一次 LLM 请求从输入到生成的主要行为路径。

### Phase 03 — Evaluation Foundations

Evaluation Target、Task、Dataset、Golden Set、Ground Truth、Rubric、Grader、Metric、Benchmark、Coverage。

**出口：** 能设计最小可验证 Evaluation。

### Phase 04 — LLM Evaluation

Correctness、Factuality、Relevance、Completeness、Instruction Following、Robustness、Consistency、LLM Judge。

**出口：** 能对 LLM 功能进行多维、多 Trial 评估并分析失败。

### Phase 05 — RAG Evaluation

Retrieval、Ranking、Context、Generation、Faithfulness、Groundedness、E2E、Root Cause Localization。

**出口：** 能区分检索失败、上下文失败和生成失败。

### Phase 06 — Agent Evaluation

Planning、Decision、Tool、State、Memory、Trajectory、Outcome、Recovery、Long Horizon、Safety。

**出口：** 能用 Trace + Outcome 评估 Agent，而不是只看最终答案。

### Phase 07 — Safety / Multimodal / Reliability

Jailbreak、Prompt Injection、Data Leakage、OCR、Grounding、Computer Use、Flakiness、Degradation、Recovery。

**出口：** 能把专项质量问题转化成可测量的 Evaluation。

### Phase 08 — Evaluation Engineering

Runner、Dataset Loader、Grader、Metric、Trace、Report、Baseline、Regression、CI、Reproducibility。

**出口：** 能构建最小 Evaluation Harness。

### Phase 09 — Production AI Quality

Online Eval、Drift、Feedback Mining、Failure Clustering、Release Gate、Quality SLO、Business KPI、Meta-Evaluation。

**出口：** 能负责 AI 系统持续质量，而不是只负责一次评测。

## 学习节奏

每个阶段都执行：

```text
学概念 → 举例 → 做实验 → 写代码 → 产生数据 → 评估 → 分析失败 → 复盘
```

## 优先级

P0：必须掌握，直接影响 AI Evaluation 核心工作。

P1：完成核心能力后掌握，用于提高深度和覆盖范围。

P2：知道概念和使用场景，按项目需要深入。

## 传统测试能力如何迁移

| 传统能力 | AI Evaluation 对应能力 |
|---|---|
| 测试设计 | Eval Target / Dataset Design |
| 测试数据 | Eval Dataset / Golden Set |
| Expected Result | Ground Truth / Rubric |
| 自动化测试 | Eval Runner / Harness |
| 断言 | Grader |
| Pass Rate | Evaluation Metrics |
| 回归测试 | Evaluation Regression |
| 缺陷分析 | Failure Analysis / Root Cause |
| 性能测试 | Latency / Token / Cost Evaluation |
| 安全测试 | Safety / Red Team Evaluation |

## 最终能力标准

不是“会多少 AI 名词”，而是能够独立完成：

```text
业务目标
→ Quality Target
→ Eval Dataset
→ Grader
→ Evaluation Run
→ Metrics / Statistics
→ Failure Analysis
→ Root Cause
→ Regression
→ Production Monitoring
→ Business Impact
```
