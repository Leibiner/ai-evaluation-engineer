# Capability Map

> V3.0 — 按“认知依赖 → 实践能力 → 工程化 → 生产质量”重构。

## 01 AI / ML Foundations — P0

AI / ML / DL、Dataset、Label、Model、Prediction、Loss、Training、Validation、Test、Generalization、Distribution Shift、Leakage、Contamination。

**能力出口：** 能解释学习过程与泛化问题。

## 02 LLM Foundations — P0

Token、Tokenization、Embedding、Transformer、Attention、Context、Inference、Sampling、Structured Output、Tool Calling。

**能力出口：** 能解释 LLM 行为来源并设计机制实验。

## 03 Evaluation Foundations — P0

Evaluation Target、Task、Dataset、Golden Set、Ground Truth、Rubric、Grader、Metric、Benchmark、Evaluation Suite、Coverage、Representativeness、Versioning。

**能力出口：** 能把“好不好”变成可执行评估。

## 04 LLM Evaluation — P0

Correctness、Factuality、Relevance、Completeness、Instruction Following、Constraint Satisfaction、Robustness、Consistency、Pointwise、Pairwise、LLM Judge。

**能力出口：** 能建立可重复的 LLM Eval。

## 05 RAG Evaluation — P0

Retrieval Recall / Precision、MRR、NDCG、Context Quality、Faithfulness、Groundedness、Answer Quality、Root Cause Localization。

**能力出口：** 能分层定位 RAG 失败。

## 06 Agent Evaluation — P0

Planning、Decision、Tool Selection、Arguments、State、Memory、Trajectory、Outcome、Recovery、Long Horizon、Efficiency、Safety。

**能力出口：** 能同时评价过程与结果。

## 07 Safety / Multimodal / Reliability — P0/P1

Jailbreak、Prompt Injection、Data Leakage、Excessive Agency、OCR、Grounding、Computer Use、Flakiness、Timeout、Degradation、Recovery。

**能力出口：** 能覆盖 AI 系统的非功能质量。

## 08 Evaluation Engineering — P0

Runner、Adapter、Dataset Loader、Grader Interface、Metric Aggregation、Trace、Storage、Report、Baseline、Regression、CI、Reproducibility、Concurrency。

**能力出口：** 能构建 Evaluation Harness。

## 09 Production AI Quality — P0/P1

Online Evaluation、Drift、Production Sampling、Feedback Mining、Failure Clustering、Release Gate、Quality SLO、Cost/Latency/Quality、Business KPI。

**能力出口：** 能建立持续 AI Quality 闭环。

## 深度等级

- **L1：认知** — 能解释概念和边界。
- **L2：应用** — 能使用工具完成实验。
- **L3：工程** — 能独立设计、实现、验证。
- **L4：系统** — 能设计体系、定位复杂根因并建立长期机制。

## 能力关系

```text
AI / ML
   ↓
LLM
   ↓
AI System
   ↓
Evaluation Foundations
   ↓
LLM / RAG / Agent / Safety / Multimodal / Reliability
   ↓
Evaluation Engineering
   ↓
Production AI Quality
```

## 判断标准

一个能力只有同时回答下面四个问题，才算真正掌握：

1. **What**：它是什么？
2. **Why**：为什么需要它？
3. **How**：如何实验和实现？
4. **Evidence**：如何证明结论可信？
