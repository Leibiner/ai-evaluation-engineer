# AI Evaluation Engineer

> 从传统软件测试工程师走向 AI Evaluation / AI Quality Engineering 的系统学习与实战仓库。

**定位：不是 AI 测试用例仓库，而是一套可运行、可验证、可持续演进的 AI Evaluation 工程实践。**

## 为什么做这个项目

传统测试关注确定性软件：输入 → 预期结果 → Pass/Fail。

AI 系统具有概率性、上下文依赖、非确定性和长链路行为，因此需要新的质量工程方法：

```text
Task
  ↓
Trial
  ↓
Model / Prompt / Context / Tool / Memory / Agent
  ↓
Outcome + Trace
  ↓
Grader
  ↓
Metrics
  ↓
Statistical Analysis
  ↓
Failure Analysis
  ↓
Regression
  ↓
Production Evaluation
```

## 能力地图

当前能力地图：**V2.1**

16 个核心能力域：

1. AI / ML Fundamentals
2. LLM Fundamentals
3. LLM Behavior & Reasoning
4. AI System Architecture
5. Evaluation Fundamentals & Data
6. Evaluation Methodology & Statistics
7. LLM Evaluation
8. RAG Evaluation
9. Agent Architecture & Evaluation
10. Multimodal / Computer Use Evaluation
11. Safety / Security / Red Team
12. Reliability / Production Evaluation
13. Evaluation Engineering
14. EvalOps & Evaluation Toolchain
15. Meta-Evaluation
16. AI Quality Engineering & Business Alignment

详见 [`roadmap/capability-map-v2.1.md`](roadmap/capability-map-v2.1.md)。

## 学习原则

不采用“先学完理论，再做项目”的路线，而采用：

```text
Knowledge
 ↓
Experiment
 ↓
Code
 ↓
Dataset
 ↓
Grader
 ↓
Evaluation Harness
 ↓
Metrics
 ↓
Statistics
 ↓
Failure Analysis
 ↓
Regression
 ↓
Production Evaluation
```

每一个重要知识点最终都应该落到一个可以运行、可以测量、可以复现的工程产物上。

## 项目路线

| 阶段 | 项目 | 核心能力 |
|---|---|---|
| 01 | LLM Evaluation | Pointwise / Pairwise / Rule / Judge |
| 02 | Evaluation Dataset | Golden Set / Data Validation / Versioning |
| 03 | Evaluation Science | Multi-trial / CI / Variance / Effect Size |
| 04 | RAG Evaluation | Retrieval + Generation 分层评估 |
| 05 | Agent Evaluation | Planning / Tool Use / Trajectory / Recovery |
| 06 | Safety Evaluation | Jailbreak / Prompt Injection / Red Team |
| 07 | Multimodal Evaluation | OCR / Grounding / Computer Use |
| 08 | Evaluation Harness | Runner / Grader / Metrics / Reports |
| 09 | Meta-Evaluation | Judge Calibration / Eval Validity |
| 10 | Production Quality | Regression / Drift / Online Eval |

## 推荐仓库结构

```text
ai-evaluation-engineer/
├── README.md
├── roadmap/
├── 01-ai-fundamentals/
├── 02-llm-fundamentals/
├── 03-llm-evaluation/
├── 04-rag-evaluation/
├── 05-agent-evaluation/
├── 06-multimodal-evaluation/
├── 07-safety-evaluation/
├── 08-evaluation-engineering/
├── 09-meta-evaluation/
├── 10-production-quality/
├── projects/
├── tools/
├── examples/
├── tests/
└── pyproject.toml
```

## 与传统测试能力的连接

这个项目不是从零开始，而是把已有的软件测试能力迁移到 AI 系统：

```text
功能测试 / 接口测试 / 自动化 / 性能测试
                ↓
        AI Evaluation
                ↓
Dataset / Grader / Harness / Metrics
                ↓
   AI Quality Engineering
```

重点升级不是“会不会调用大模型 API”，而是能否回答：

- 什么能力需要评估？
- 什么才算正确？
- 如何构造高质量 Eval Set？
- Grader 是否可靠？
- 一次结果可信还是需要多次 Trial？
- 指标变化是否具有统计意义？
- 失败到底来自 Model、Prompt、Context、Retrieval、Tool、Memory 还是 Agent Loop？
- 如何把一次评估变成持续 Regression？

## 当前状态

- [ ] AI / ML Fundamentals
- [ ] LLM Fundamentals
- [ ] LLM Evaluation
- [ ] RAG Evaluation
- [ ] Agent Evaluation
- [ ] Safety / Red Team
- [ ] Multimodal / Computer Use
- [ ] Evaluation Harness
- [ ] Meta-Evaluation
- [ ] Production Evaluation

## License

MIT