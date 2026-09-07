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
| **01** | **AI / ML Foundations** | AI、ML、DL、Dataset、Label、Model、Training、Inference、Loss、Optimization、Validation、Generalization、Distribution Shift | 理解 AI 模型如何学习、预测以及为什么犯错 |
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

# 学习依赖关系

这里有一个重要原则：**Evaluation 不是学完整个 AI 之后才开始的最后一章，而是贯穿整个路线的核心能力。**

Phase 01 先回答“AI 为什么会产生错误”，Phase 02 开始回答“错误和质量应该如何定义与衡量”，之后再把 Evaluation 应用到不同 AI 系统。

```text
Phase 01
AI / ML Foundations
   ↓
理解 AI 如何学习、预测、犯错
   ↓
Phase 02
Evaluation Fundamentals
   ↓
定义什么是“好”以及如何证明
   ↓
Phase 03
Evaluation Dataset Engineering
   ↓
准备可信的评测数据
   ↓
Phase 04
Evaluation Metrics & Judge
   ↓
建立可信的评分机制
   ↓
Phase 05
LLM Foundations
   ↓
理解现代 LLM 的工作机制
   ↓
Phase 06
LLM Evaluation
   ↓
Phase 07
RAG Evaluation
   ↓
Phase 08
Agent Evaluation
   ↓
Phase 09
Multi-Agent Evaluation
   ↓
Phase 10
AI Safety / Security Evaluation
   ↓
Phase 11
Evaluation Engineering
   ↓
Phase 12
Production / Continuous AI Quality
   ↓
Phase 13
AI Evaluation Projects
```

其中 Phase 02～04 是整个路线的**Evaluation 核心基础层**；Phase 06～10 是**专项 Evaluation 能力层**；Phase 11～12 是**Evaluation Engineering / Production Quality 工程层**。

---

# 为什么路线不是“先把 AI 全学完，再学 Evaluation”？

传统软件测试通常先有相对明确的规则和预期结果：

```text
需求
 ↓
测试用例
 ↓
Expected Result
 ↓
Actual Result
 ↓
Pass / Fail
```

AI 系统不同：

```text
Input
 ↓
AI System
 ↓
可能存在多个合理输出
 ↓
需要定义 Evaluation Criteria
 ↓
Grader / Judge
 ↓
Metric
 ↓
Quality Decision
```

因此，AI Evaluation Engineer 不只是“理解 AI”，还必须从一开始就建立一个关键意识：

> **AI 的测试问题，本质上正在从“结果是否等于标准答案”，转向“如何定义、测量并证明系统质量”。**

这也是本项目为什么把 Evaluation Fundamentals 放在 AI 基础之后，而不是放到所有 AI 技术之后。

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
提出 Evaluation Question
   ↓
动手实验
   ↓
最小代码实现
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

最终不是放弃测试，而是把已有的测试工程能力迁移到**概率性、生成式、学习型系统**，并进一步建立新的 Evaluation Engineering 能力。

---

# 当前学习：Phase 01

## AI / ML Foundations

第一阶段是整个路线的地基。

当前只学习：

**[→ 进入 Phase 01：AI / ML Foundations](./01-ai-ml-foundations/README.md)**

第一阶段重点解决：

```text
AI 是什么？
   ↓
ML 为什么叫“学习”？
   ↓
数据在学习中扮演什么角色？
   ↓
Model 到底是什么？
   ↓
模型如何产生 Prediction？
   ↓
Prediction 为什么会错？
   ↓
Loss 如何衡量错误？
   ↓
模型如何根据错误更新参数？
   ↓
Training 是怎么循环起来的？
   ↓
如何验证模型真的学会了？
   ↓
什么是 Generalization？
   ↓
为什么真实世界会出现 Distribution Shift？
   ↓
为什么最终需要 Evaluation？
```

Phase 01 学完后，不要求成为算法工程师，而要求能够建立最基本的 AI Failure Analysis 能力：

> **我知道 AI 的结果是如何产生的，也知道一个错误可能来自数据、标签、模型、训练、泛化或分布变化。**

---

# 当前仓库结构

```text
ai-evaluation-engineer/
│
├── README.md
│   └── 总路线 + 全阶段能力地图
│
└── 01-ai-ml-foundations/
    └── README.md
        └── 第一阶段详细学习内容
```

**当前只保留第一阶段。** 后续阶段不会提前建立文件，避免学习路线变成一堆尚未真正学习的空目录。

---

# 最终能力闭环

最终希望形成的不是“学过很多 AI 技术”，而是一条完整的质量工程能力链：

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

最终能力不是：

> **“我会多少 AI 工具。”**

而是：

> **“我能够理解 AI 系统为什么产生这个结果，设计合理的 Evaluation 判断它好不好，并把这种判断变成可重复、可自动化、可持续运行的质量工程系统。”**
