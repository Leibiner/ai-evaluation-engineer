# AI Evaluation Engineer 实战路线 V2.1

> 目标：从传统软件测试工程师 → AI Evaluation Engineer → AI Quality Engineer。
>
> 原则：**学习一项能力，就做一次实验；做一次实验，就留下工程证据。** 不以“看完课程”作为完成标准。

## 1. 总路线

```text
01 AI / ML
   ↓
02 LLM
   ↓
03 LLM Behavior + 04 Reasoning
   ↓
05 AI System Architecture
   ↓
06 Evaluation Fundamentals + 07 Data Quality
   ↓
08 Evaluation Methodology + 09 Evaluation Science
   ↓
10 LLM Evaluation
   ↓
11 RAG Evaluation
   ↓
12 Agent Architecture
   ↓
13 Agent Evaluation + 14 Memory Evaluation
   ↓
15 Multimodal / Computer Use
   ↓
16 Safety / Security + 17 Red Teaming
   ↓
18 Reliability
   ↓
19 Evaluation Engineering
   ↓
20 EvalOps / Toolchain
   ↓
21 Meta-Evaluation
   ↓
22 Production Evaluation
   ↓
23 AI Quality
   ↓
24 Business Alignment
```

---

## 2. Phase 1 — AI 与 LLM 基础

### 对应能力域
- 01 AI / ML Fundamentals
- 02 LLM Fundamentals
- 03 LLM Behavior
- 04 Reasoning

### 学习重点
- AI / ML / DL基本概念
- Transformer、Attention
- Token、Embedding、Context Window
- Inference、Sampling、Temperature、Top-p
- Instruction Following、Correctness、Factuality、Robustness
- Reasoning 与 Planning / Agent 的边界

### 必做实验
- Token 数量实验
- Context Window 实验
- Temperature / Top-p 稳定性实验
- Prompt 对照实验
- 多步推理任务实验

### 阶段证据
- `notes/`：概念笔记
- `experiments/`：实验数据
- `reports/`：行为分析报告
- 至少 1 个可复现实验

### 阶段出口
能够解释：**模型为什么会产生当前行为，以及哪些因素会改变行为。**

---

## 3. Phase 2 — Evaluation 基础

### 对应能力域
- 05 AI System Architecture
- 06 Evaluation Fundamentals
- 07 Data Quality
- 08 Evaluation Methodology
- 09 Evaluation Science

### 学习重点
- Model / Prompt / Context / Retrieval / Tool / Memory / Environment分层
- Task / Dataset / Eval Set / Golden Set / Benchmark / Suite
- Trial / Run / Ground Truth
- Rule / Code / LLM Judge / Human Grader
- Pointwise / Pairwise / Listwise
- Reference-based / Reference-free
- Sampling、Sample Size、Repeated Trials
- Variance、SD、CI、Effect Size、Significance

### 必做项目
建立第一套 **LLM Evaluation Dataset**：

```text
100 Tasks
×
多个模型/Prompt版本
×
多个 Trials
↓
Grader
↓
Metrics
↓
Evaluation Report
```

### 阶段出口
能够回答：**评什么、为什么这样评、数据是否可信、Grader 是否合适、结果是否具有统计意义。**

---

## 4. Phase 3 — LLM Evaluation

### 对应能力域
- 10 LLM Evaluation

### 学习重点
- Accuracy / Correctness
- Factuality
- Relevance
- Completeness
- Constraint Following
- Robustness
- Consistency
- Pointwise
- Pairwise
- LLM-as-a-Judge

### 必做项目
**LLM Evaluation Toolkit v1**

```text
Dataset
  ↓
Runner
  ↓
Trial × N
  ↓
Rule / Code / LLM Judge
  ↓
Metrics
  ↓
Report
```

### 阶段出口
能够独立完成一个从 Dataset 到 Evaluation Report 的完整评测闭环。

---

## 5. Phase 4 — RAG Evaluation

### 对应能力域
- 11 RAG Evaluation

### 必须建立的认知

```text
Retrieval Failure
≠
Context Quality Failure
≠
Generation Failure
≠
E2E Answer Failure
```

### 学习重点
**Retrieval**：Recall、Precision、Hit Rate、MRR、NDCG。

**Context**：Context Recall、Context Precision、Relevance、Completeness、Noise、Redundancy。

**Generation**：Faithfulness、Groundedness、Answer Correctness、Answer Relevance、Completeness。

### 必做项目
**RAG Evaluation Pipeline**：

```text
Query
 ↓
Retrieval Eval
 ↓
Context Eval
 ↓
Generation Eval
 ↓
Failure Classification
```

### 阶段出口
能判断一个 RAG 系统到底是“没检索到”“上下文不好”还是“模型生成错”。

---

## 6. Phase 5 — Agent Evaluation

### 对应能力域
- 12 Agent Architecture
- 13 Agent Evaluation
- 14 Memory Evaluation

### 学习重点
- Planning
- Decision
- Tool Selection
- Argument Generation
- Tool Result Handling
- State / State Transition
- Trajectory / Trace
- Long Horizon
- Recovery
- Efficiency
- Memory Read / Write / Recall / Relevance

### 必做项目
**Agent Evaluation Toolkit**

同时评估：

```text
Outcome
+
Trace / Trajectory
+
Tool Use
+
Planning
+
Memory
+
Recovery
```

### 阶段出口
能够定位 Agent 是“规划错、工具选错、参数错、状态错、记忆错、恢复失败”，而不是只报告“任务失败”。

---

## 7. Phase 6 — Multimodal / Computer Use

### 对应能力域
- 15 Multimodal / Computer Use

### 学习重点
- Vision Understanding
- OCR
- Grounding
- Screen Understanding
- GUI Action
- Computer Use Agent

### 必做项目
- OCR Accuracy Eval
- Grounding Eval
- GUI Action Success Rate
- Computer Use E2E Eval

### 阶段出口
能够评估视觉输入、屏幕理解和 GUI 操作链路。

---

## 8. Phase 7 — Safety / Security / Red Team

### 对应能力域
- 16 Safety / Security
- 17 Red Teaming

### 学习重点
- Jailbreak
- Prompt Injection
- Indirect Prompt Injection
- Data Leakage
- Excessive Agency
- Tool Abuse
- Privilege Escalation
- Adversarial Testing
- Attack Dataset
- Attack Mutation
- Safety Regression

### 必做项目
**Safety Evaluation Suite**

```text
Attack Dataset
 ↓
Attack Execution
 ↓
Safety Grader
 ↓
Failure Classification
 ↓
Regression Set
```

### 阶段出口
能够把安全问题从“几个攻击样例”升级为可重复的安全评估体系。

---

## 9. Phase 8 — Reliability

### 对应能力域
- 18 Reliability

### 学习重点
- Stability
- Reliability
- Multi-trial Consistency
- Timeout / Retry
- Stress
- Failure Rate
- Drift
- Regression

### 必做项目
- Multi-trial Reliability Test
- Stability Report
- Regression Dataset
- Failure-rate Analysis

### 阶段出口
能够回答：**系统偶尔成功是否算可靠？成功率是多少？波动来自哪里？**

---

## 10. Phase 9 — Evaluation Engineering

### 对应能力域
- 19 Evaluation Engineering

### 核心目标
把前面所有评估统一成自己的 Evaluation Harness：

```text
Dataset
  ↓
Runner
  ↓
Trial
  ↓
Trace
  ↓
Grader
  ↓
Metrics
  ↓
Report
```

### 必须工程化
- Config
- Runner
- Trial Executor
- Grader Interface
- Metric Interface
- Trace Schema
- Parallel Execution
- Retry
- Timeout
- Versioning
- Reproducibility
- Report Generation

### 阶段出口
不依赖 Promptfoo / DeepEval 等框架，也能独立实现最小 Evaluation Harness。

---

## 11. Phase 10 — EvalOps / Toolchain

### 对应能力域
- 20 EvalOps / Toolchain

### 工具学习顺序

```text
Python + pytest
   ↓
Promptfoo / DeepEval
   ↓
Ragas
   ↓
LangSmith / Braintrust
   ↓
Phoenix / Weave
   ↓
Label Studio
```

重点不是背 API，而是理解：

```text
Dataset → Runner → Trial → Trace → Grader → Metrics → Report
```

以及：

```text
Version
→ Regression
→ Quality Gate
→ Dashboard
→ Continuous Evaluation
```

### 阶段出口
能够选工具、拆工具、替换工具，并理解工具背后的 Evaluation Architecture。

---

## 12. Phase 11 — Meta-Evaluation

### 对应能力域
- 21 Meta-Evaluation

### 核心问题
> **我们的 Evaluation 结果可信吗？**

### 学习重点
- Evaluation Validity
- Grader Reliability
- Judge Calibration
- Human-Judge Agreement
- Inter-rater Agreement
- Statistical Power
- Sample Size
- Effect Size
- Eval Sensitivity
- Rubric Ambiguity
- Judge Bias

### 必做项目
比较：

```text
Human Grader
     ↕
LLM Judge
     ↕
Rule / Code Grader
```

分析 Judge 的一致性、偏差、稳定性和失效案例。

### 阶段出口
能够证明“这个 Eval 本身值得相信”。

---

## 13. Phase 12 — Production Evaluation

### 对应能力域
- 22 Production Evaluation

### 学习重点
- Online Evaluation
- Production Trace
- User Feedback
- Drift
- Monitoring
- Continuous Evaluation
- Online / Offline Consistency
- A/B Testing

### 必做项目
设计生产质量闭环：

```text
Production Traffic
 ↓
Trace / Feedback
 ↓
Online Evaluation
 ↓
Failure Detection
 ↓
New Eval Cases
 ↓
Regression Suite
 ↓
Release Gate
```

### 阶段出口
能够把离线 Evaluation 接入真实生产质量体系。

---

## 14. Phase 13 — AI Quality

### 对应能力域
- 23 AI Quality

### 学习重点
- Quality Model
- Quality Gate
- Model Validation
- Failure Analysis
- Root Cause Analysis
- Quality / Latency / Cost Trade-off

### 必做项目
建立一个 AI Quality Dashboard / Quality Report，至少包含：

- Capability
- Correctness
- Reliability
- Safety
- Latency
- Cost
- Regression

### 阶段出口
从“评估某个模型”升级到“管理 AI 系统质量”。

---

## 15. Phase 14 — Business Alignment

### 对应能力域
- 24 Business Alignment

### 学习重点
- Business Metric
- Metric-to-Business Alignment
- User Satisfaction
- Quality / Latency / Cost Trade-off
- Release Decision

### 必做项目
建立：

```text
Business Goal
 ↓
AI Capability
 ↓
Quality Metric
 ↓
Evaluation
 ↓
Business Metric
 ↓
Release Decision
```

### 阶段出口
能够解释：**为什么这个 Eval 指标对业务有意义。**

---

## 16. 五级能力成熟度

| Level | 定义 | 能力表现 |
|---|---|---|
| L1 | 了解 | 能理解概念、术语、基本指标 |
| L2 | 掌握 | 能设计 Task、Dataset、Grader |
| L3 | 熟练 | 能编码 Eval、执行多 Trial、做统计分析 |
| L4 | 工程化 | 能构建 Harness、RAG/Agent/Safety 专项评估 |
| L5 | 体系化 | 能完成 Meta-Eval、Production Eval、AI Quality System |

> L6 不作为主路线能力等级；企业级体系化能力归入 L5。

---

## 17. 学习完成标准

一个能力域只有同时满足以下条件，才算真正完成：

```text
理解
 ↓
实验
 ↓
代码
 ↓
结果
 ↓
Failure Analysis
 ↓
项目证据
```

最低证据要求：

- 至少 1 个可运行实验
- 至少 1 个可复现结果
- 至少 1 个失败案例
- 至少 1 个分析结论
- P0 能力必须进入项目

---

## 18. 最终作品集路线

最终形成 5 个核心项目：

| 项目 | 对应能力 |
|---|---|
| `01-llm-evaluation` | LLM Evaluation + Statistics |
| `02-rag-evaluation` | Retrieval + Context + Generation |
| `03-agent-evaluation` | Agent + Tool + Trace + Memory |
| `04-safety-evaluation` | Safety + Red Team |
| `05-evaluation-platform` | Harness + EvalOps + Meta-Eval + Production |

最终工程目标：

```text
Model A / Model B
       ↓
Evaluation Platform
       ↓
1,000 Tasks
       ↓
5 Trials / Task
       ↓
5,000 Runs
       ↓
Multiple Graders
       ↓
Metrics
       ↓
Statistical Analysis
       ↓
Failure Clustering
       ↓
Root Cause
       ↓
Regression Report
       ↓
Release Decision
```

---

## 19. 传统测试能力迁移

| 传统测试 | AI Evaluation |
|---|---|
| Test Case | Evaluation Task |
| Test Suite | Evaluation Suite |
| Test Data | Evaluation Dataset |
| Expected Result | Ground Truth / Reference |
| Assertion | Grader |
| Test Execution | Trial / Run |
| Test Report | Evaluation Report |
| Bug | Model / Prompt / RAG / Agent Failure |
| Regression Test | Regression Evaluation |
| UI Automation | Computer Use / Agent Evaluation |
| API Testing | LLM / Tool / API Evaluation |
| Performance Testing | Latency / Token / Cost Evaluation |
| Reliability Testing | Multi-trial / Stability Evaluation |
| Security Testing | AI Safety / Red Teaming |
| Monitoring | Production Evaluation |
| Test Framework | Evaluation Harness |
| CI/CD | Continuous Evaluation |
| QA | AI Quality Engineering |

---

## 20. 最终目标

> **AI Evaluation Engineer = 用工程化、统计学和实验方法，对 AI 模型及 AI 应用系统的能力、质量、安全、可靠性和业务效果进行可重复、可量化、可验证的评估，并能够定位问题根因。**

最终路线：

```text
传统测试工程师
    ↓
AI Fundamentals
    ↓
LLM Understanding
    ↓
LLM Evaluation
    ↓
RAG Evaluation
    ↓
Agent Evaluation
    ↓
Safety / Reliability
    ↓
Evaluation Engineering
    ↓
Meta-Evaluation
    ↓
Production AI Quality
    ↓
AI Quality Engineer
```