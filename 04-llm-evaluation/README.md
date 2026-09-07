# 04 LLM Evaluation

> 把 LLM 的开放式行为拆成可以测量的能力。

## 评估维度

- Correctness / Accuracy
- Factuality / Hallucination
- Relevance
- Completeness
- Instruction Following
- Constraint Satisfaction
- Consistency
- Robustness
- Latency / Tokens / Cost

## 评估方法

```text
Reference-based
├─ Rule Grader
├─ Code Grader
└─ Exact / Semantic checks

Reference-free
├─ Rubric
├─ LLM Judge
└─ Human Evaluation
```

同时掌握 Pointwise、Pairwise 和多 Trial。

## 关键问题

LLM Judge 本身也是一个可能出错的模型，因此不能把 Judge 输出直接当真值；必须考虑 Calibration、Agreement、Bias 和 Meta-Evaluation。

## 出口

能够为一个真实 LLM 功能建立 Dataset + Grader + Metric，并完成多次运行、失败分类和模型/Prompt 对比。
