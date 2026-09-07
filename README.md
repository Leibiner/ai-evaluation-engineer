# AI Evaluation Engineer

> 从传统软件测试出发，系统学习 AI Evaluation / AI Quality Engineering。

## 项目定位

这不是一份 AI 名词清单，也不是一条“把 AI 技术全部学一遍”的路线。

这是一条围绕 **AI Evaluation Engineer 能力模型**设计的学习路线：先理解 AI 系统为什么会产生结果和错误，再学习如何定义“什么是好”，最后把评估能力工程化，并进入生产质量闭环。

核心目标：

> 从传统软件测试工程师，逐步成长为能够理解 AI、评估 LLM / RAG / Agent / Multi-Agent，建设 Evaluation Engineering，并最终负责 Production AI Quality 的工程师。

核心能力分为三层：

```text
第一层：AI Understanding
        ↓
理解 AI 系统如何工作、为什么失败

第二层：AI Evaluation
        ↓
定义质量、设计数据、指标、Grader / Judge，并判断系统好不好

第三层：AI Quality Engineering
        ↓
把 Evaluation 变成自动化、可重复、可回归、可持续的工程系统
```

---

# 学习总路线

路线按照**能力依赖关系**设计，而不是按照热门 AI 技术堆叠。

| 阶段 | 主题 | 核心学习内容 | 最终能力 |
|---|---|---|---|
| **01** | **AI 基础** | AI、ML、DL、Dataset、Label、Model、Training、Inference、Loss、Optimization、Validation、Generalization、Distribution Shift | 理解 AI 模型如何学习、预测以及为什么犯错 |
| **02** | **Evaluation Fundamentals** | Evaluation Target、Criteria、Ground Truth、Reference、Rubric、Grader、Metric、Benchmark、Human Evaluation、LLM-as-a-Judge、Reliability、Validity | 能把“好不好”定义成可执行、可验证的 Evaluation |
| **03** | **Evaluation Dataset Engineering** | Eval Case、Dataset Design、Sampling、Labeling、Annotation Guideline、Golden Set、Edge Case、Adversarial Case、Dataset Versioning、Data Quality | 能设计和维护真正可用于 AI Evaluation 的数据集 |
| **04** | **Evaluation Metrics & Judge** | Rule-based Grader、Model-based Grader、LLM Judge、Pairwise Evaluation、Pointwise Evaluation、Reference-based / Reference-free、Metric Design、Judge Calibration、Inter-rater Agreement、Statistical Significance | 能设计、实现并验证 Evaluation Metric / Grader / Judge |
| **05** | **LLM Foundations** | Token、Tokenization、Embedding、Transformer、Attention、Context、Pre-training、Fine-tuning、Inference、Decoding | 理解现代 LLM 的基本工作机制，为后续 LLM Evaluation 建立技术基础 |
| **06** | **LLM Evaluation** | Correctness、Relevance、Faithfulness、Instruction Following、Hallucination、Consistency、Robustness、Structured Output、Prompt Sensitivity、LLM Judge | 能系统评估 LLM 的输出质量与行为 |
| **07** | **RAG Evaluation** | Retrieval、Ranking、Context、Context Relevance、Context Recall、Context Precision、Context Sufficiency、Faithfulness、Answer Relevance、End-to-End RAG | 能定位并评估 RAG 的 Retrieval、Generation 及端到端质量问题 |
| **08** | **Agent Evaluation** | Goal、Planning、Tool Selection、Tool Arguments、Trajectory、Observation、State、Memory、Action、Error Recovery、Agent Loop、Long Horizon、Task Success | 能评估 Agent 的任务完成能力、轨迹和工具使用可靠性 |
| **09** | **Multi-Agent Evaluation** | Role Assignment、Task Decomposition、Routing、Handoff、Communication、Coordination、Shared Memory、Conflict Resolution、Deadlock、Collaboration Quality | 能评估多个 Agent 协作时的系统性质量问题 |
| **10** | **AI Safety / Security Evaluation** | Safety、Harmfulness、Bias、Toxicity、Privacy、Robustness、Policy Compliance、Prompt Injection、Jailbreak、Data Leakage、Tool Abuse、Excessive Agency | 能从安全与防御角度发现 AI 系统风险 |
| **11** | **Evaluation Engineering** | Evaluation Dataset、Runner、AI System、Trace、Grader、Metric、Report、Regression、Reproducibility、Parallel Evaluation、CI/CD、Release Gate | 能把 Evaluation 建设成自动化、可重复、可持续运行的工程系统 |
| **12** | **Production / Continuous AI Quality** | Online Evaluation、Monitoring、Drift、Feedback、Failure Mining、Quality SLO、Business KPI、Release Gate、Regression、Dataset Evolution | 能建立从离线评测到线上质量监控的持续闭环 |
| **13** | **AI Evaluation Projects** | LLM / RAG / Agent / Multi-Agent 综合项目、Evaluation Platform、真实数据集、自动化评测、Failure Analysis、质量报告 | 用完整项目证明 AI Evaluation Engineer 能力 |

---

# 当前学习：阶段 01｜AI 基础

第一阶段是整个路线的地基。当前第一篇已经开始学习，后续文章会逐篇推进，不提前跳到大模型、RAG、Agent 或 Evaluation Engineering。

**[→ 进入阶段 01｜AI 基础](./01%EF%BD%9CAI%20%E5%9F%BA%E7%A1%80/README.md)**

当前学习进度：

```text
阶段 01｜AI 基础
│
├── 01｜AI、ML、DL 到底是什么？   ← 当前
├── 02｜Dataset 到底是什么？
├── 03｜Label / Ground Truth 到底是什么？
├── 04｜Model 到底是什么？
├── 05｜Prediction / Inference 是什么？
├── 06｜Error / Loss 是什么？
├── 07｜Optimization 是什么？
├── 08｜Training 是怎么进行的？
├── 09｜Validation / Test 是什么？
├── 10｜Generalization 是什么？
├── 11｜Distribution Shift 是什么？
└── 12｜Data Leakage / Test Contamination 是什么？
```

---

# 学习依赖关系

```text
阶段 01｜AI 基础
   ↓
阶段 02｜Evaluation Fundamentals
   ↓
阶段 03｜Evaluation Dataset Engineering
   ↓
阶段 04｜Evaluation Metrics & Judge
   ↓
阶段 05｜LLM Foundations
   ↓
阶段 06｜LLM Evaluation
   ↓
阶段 07｜RAG Evaluation
   ↓
阶段 08｜Agent Evaluation
   ↓
阶段 09｜Multi-Agent Evaluation
   ↓
阶段 10｜AI Safety / Security Evaluation
   ↓
阶段 11｜Evaluation Engineering
   ↓
阶段 12｜Production / Continuous AI Quality
   ↓
阶段 13｜AI Evaluation Projects
```

---

# 每个阶段的学习方式

每个阶段最终都不是“看完文档”就算完成，而是：

```text
理解概念
   ↓
建立因果链
   ↓
真实案例
   ↓
动手实验
   ↓
产生数据
   ↓
Evaluation
   ↓
Failure Analysis
   ↓
复盘
   ↓
形成可复用能力
```

每个阶段都必须回答四个问题：

1. **What**：它是什么？
2. **Why**：为什么需要它？
3. **How**：它如何工作？如何实验？
4. **Evidence**：如何证明自己的结论可信？

---

# 传统测试能力如何迁移

| 传统测试 | AI Evaluation |
|---|---|
| 测试需求 | Evaluation Target |
| 测试用例 | Eval Case |
| 测试数据 | Evaluation Dataset |
| Expected Result | Ground Truth / Reference / Rubric |
| 断言 | Grader / Judge |
| Pass Rate | Evaluation Metric |
| 自动化测试 | Evaluation Runner |
| 测试报告 | Evaluation Report |
| 回归测试 | Evaluation Regression |
| 缺陷分析 | Failure Analysis / Root Cause |
| 性能测试 | Latency / Token / Cost Evaluation |
| 安全测试 | Safety / Security / Red Team Evaluation |

---

# 最终能力闭环

```text
AI Understanding
      ↓
Evaluation Design
      ↓
Evaluation Dataset
      ↓
Grader / Judge
      ↓
Metrics
      ↓
Failure Analysis
      ↓
Evaluation Engineering
      ↓
Regression / Release Gate
      ↓
Production Monitoring
      ↓
Failure Mining
      ↓
Dataset Evolution
      ↓
Continuous Evaluation
      ↺
```
