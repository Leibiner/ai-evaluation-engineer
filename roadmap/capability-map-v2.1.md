# AI Evaluation Engineer 能力地图 V2.1

## 1. AI / ML Fundamentals

- AI / ML / DL 基本概念
- Neural Network
- Training / Fine-tuning
- Overfitting / Generalization
- Model Evaluation 基础

**目标：**理解模型为什么会产生当前行为，而不是把模型当黑盒 API。

## 2. LLM Fundamentals

- Transformer
- Token / Tokenization
- Embedding
- Context Window
- Inference
- Sampling
- Temperature / Top-p
- Model Parameters

**必须会做：**Token、上下文、采样参数实验，并记录对输出行为的影响。

## 3. LLM Behavior & Reasoning

- Instruction Following
- Factuality
- Correctness
- Relevance
- Completeness
- Consistency
- Robustness
- Reasoning Capability
- Reasoning Efficiency

注意：**Reasoning ≠ Planning ≠ Agent**。不要把 Chain-of-Thought 直接等同于 Reasoning 能力，应优先评估可观察、可验证的行为和结果。

## 4. AI System Architecture

- Prompt
- System Prompt
- Structured Output
- Tool Calling
- Context Management
- Multimodal Input
- Evaluation Target
- Model / Prompt / Context / Tool / Memory / Environment 分层

## 5. Evaluation Fundamentals & Data

核心对象：

```text
Task / Case
Dataset / Eval Set / Golden Set
Benchmark
Trial
Outcome
Ground Truth
Evaluation Suite
```

区分：Task 是单个评估问题；Dataset/Eval Set 是任务集合；Benchmark 是标准化比较协议；Evaluation Suite 是围绕能力或行为组织的一组评估。

### Data Quality

- Coverage
- Difficulty
- Balance
- Representativeness
- Ambiguity
- Solvability
- Contamination / Leakage
- Versioning

## 6. Evaluation Methodology & Statistics

### Grader

- Rule-based
- Code-based
- Human Evaluation
- LLM-as-a-Judge

### Comparison

- Pointwise
- Pairwise
- Listwise
- Reference-based
- Reference-free

### Evaluation Science

- Sampling
- Sample Size
- Repeated Trials
- Variance
- Standard Deviation
- Confidence Interval
- Statistical Significance
- Effect Size
- Experimental Design
- A/B Testing
- Inter-rater Agreement

## 7. LLM Evaluation

核心指标：

- Accuracy
- Pass Rate
- Error Rate
- Correctness
- Factuality
- Relevance
- Completeness
- Constraint Following
- Robustness
- Consistency

实践要求：Pointwise + Pairwise 两套评估方式，并支持重复 Trial。

## 8. RAG Evaluation

必须拆开：

```text
Query
 ↓
Retrieval
 ↓
Retrieved Context
 ↓
Generation
 ↓
Answer
```

### Retrieval

- Recall
- Precision
- Hit Rate
- MRR
- NDCG
- Context Recall
- Context Precision
- Context Relevance
- Noise / Redundancy / Completeness

### Generation

- Faithfulness / Groundedness
- Answer Correctness
- Answer Relevance
- Completeness

目标：能够判断失败发生在 Retrieval、Context 还是 Generation。

## 9. Agent Architecture & Evaluation

核心架构：

```text
Model
 ↓
Planning
 ↓
Tool Selection
 ↓
Arguments
 ↓
Tool Result
 ↓
State / Memory
 ↓
Next Action
 ↓
...
```

### Agent Evaluation

- Planning Quality
- Tool Selection
- Argument Correctness
- Tool Result Handling
- Trajectory / Trace
- Outcome
- Long Horizon
- Recovery
- Efficiency
- Environment Interaction

Agent Evaluation 应同时关注 **Outcome + Trace/Trajectory**，因为最终成功并不代表过程可靠。

## 10. Multimodal / Computer Use Evaluation

- Vision Understanding
- OCR
- Grounding
- Screen Understanding
- GUI Action
- Computer Use Agent

核心项目：OCR Accuracy、Grounding Accuracy、GUI Action Success Rate。

## 11. Safety / Security / Red Team

### Safety / Security

- Jailbreak
- Prompt Injection
- Indirect Prompt Injection
- Data Leakage
- Excessive Agency
- Tool Abuse
- Privilege Escalation

### Red Team

作为独立方法论建设：

- Adversarial Testing
- Attack Dataset
- Automated Attack
- Attack Mutation
- Safety Regression

## 12. Reliability / Production Evaluation

- Stability
- Reliability
- Regression
- Stress
- Drift
- Production Trace
- Online Evaluation
- User Feedback
- Continuous Evaluation
- Monitoring

## 13. Evaluation Engineering

最终需要自己构建 Evaluation Harness：

```text
Runner
  ↓
Trial Executor
  ↓
Trace Collector
  ↓
Grader
  ↓
Metric Aggregator
  ↓
Report
```

核心工程能力：

- Runner
- Grader Interface
- Metrics
- Trace Schema
- Parallel Evaluation
- Retry
- Timeout
- Versioning
- Reproducibility
- Report Generation

## 14. EvalOps & Evaluation Toolchain

需要理解并实践：

- Promptfoo
- DeepEval
- Ragas
- TruLens
- LangSmith
- Braintrust
- Arize Phoenix
- W&B Weave
- Label Studio
- Python / pytest

目标不是“会用工具”，而是理解工具背后的 Evaluation Pipeline，并最终可以自己实现核心 Harness。

## 15. Meta-Evaluation

评估“评估系统”本身：

- Evaluation Validity
- Grader Reliability
- Judge Calibration
- Inter-rater Agreement
- Statistical Power
- Sample Size
- Eval Sensitivity
- Rubric Quality

核心问题：**我们的评估结果可信吗？**

## 16. AI Quality Engineering & Business Alignment

### AI Quality Engineering

- Quality Model
- Quality Gate
- Model Validation
- Failure Analysis
- Root Cause Analysis
- Quality / Cost Trade-off

### Business Alignment

- Business Metric
- Metric-to-Business Alignment
- User Satisfaction
- Quality / Latency / Cost Trade-off

## 能力成熟度

| Level | 能力 |
|---|---|
| L1 | 能理解 AI Evaluation 概念和常见指标 |
| L2 | 能独立设计 Eval Case、Dataset、Grader |
| L3 | 能编写 Evaluation Harness 并完成统计分析 |
| L4 | 能完成 RAG / Agent / Safety / Multimodal 专项评估 |
| L5 | 能建立 Regression / EvalOps / Production Evaluation |
| L6 | 能进行 Meta-Evaluation，并设计企业级 AI Quality System |
