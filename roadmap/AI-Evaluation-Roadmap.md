# AI Evaluation Engineer 实战路线

## Phase 0 — 基础迁移

目标：把传统测试思维迁移到概率型 AI 系统。

学习：LLM 基础、Prompt、Token、Inference、Sampling、基本 AI 架构。

产出：
- Token / Sampling 实验
- Prompt 行为对比
- 第一个 LLM Eval Case

## Phase 1 — LLM Evaluation

学习：Task、Trial、Dataset、Ground Truth、Grader、Pointwise、Pairwise、LLM Judge。

产出：
- Golden Dataset
- Rule Grader
- LLM Judge
- Pointwise / Pairwise Evaluator

## Phase 2 — Evaluation Science

学习：Sampling、Repeated Trials、Variance、CI、Effect Size、显著性检验。

产出：
- 多 Trial Runner
- CI 计算
- 模型 A/B 对比报告

## Phase 3 — RAG Evaluation

学习 Retrieval 与 Generation 分层评估。

产出：
- Retrieval Evaluator
- Generation Evaluator
- RAG Failure Analyzer

## Phase 4 — Agent Evaluation

学习 Planning、Tool Use、Trajectory、Memory、Environment、Long Horizon、Recovery。

产出：
- Trace Schema
- Trajectory Analyzer
- Tool-use Grader
- Agent Outcome + Trace Report

## Phase 5 — Safety / Red Team

学习 Jailbreak、Prompt Injection、Indirect Injection、Data Leakage、Excessive Agency。

产出：
- Attack Dataset
- Attack Generator
- Safety Regression Suite

## Phase 6 — Multimodal / Computer Use

学习 OCR、Grounding、Screen Understanding、GUI Action。

产出：
- OCR Eval
- Grounding Eval
- Computer-use Agent Eval

## Phase 7 — Evaluation Engineering

把前面的实验统一成 Evaluation Harness：

```text
Dataset → Runner → Trial → Trace → Grader → Metrics → Report
```

产出：一个可配置、可并行、可重试、可版本化的评估框架。

## Phase 8 — EvalOps / Production

学习 Regression、Monitoring、Drift、Online Evaluation、Feedback、Continuous Evaluation。

产出：
- Regression Pipeline
- Quality Gate
- Evaluation Dashboard
- Production Eval Design

## Phase 9 — Meta-Evaluation

学习如何验证 Eval 本身：Judge Calibration、Inter-rater Agreement、Eval Validity、Sensitivity、Statistical Power。

最终目标：从“执行测试”升级到“设计 AI Quality System”。
