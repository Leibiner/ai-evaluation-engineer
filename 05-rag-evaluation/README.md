# 05 RAG Evaluation

RAG 不能只看最终答案，要把系统拆成 Retrieval、Context、Generation 三层。

```text
Query
 ↓
Retrieval
 ↓
Context
 ↓
Generation
 ↓
Answer
```

## Retrieval

Recall、Precision、Hit Rate、MRR、NDCG。

## Context

Context Recall、Precision、Relevance、Completeness、Noise、Redundancy。

## Generation

Faithfulness、Groundedness、Answer Correctness、Relevance、Completeness。

## 根因定位

```text
Retrieval Failure
≠ Context Quality Failure
≠ Generation Failure
≠ E2E Answer Failure
```

## 出口

给定一个 RAG 系统，能够建立分层 Eval，判断“没答对”究竟是没检索到、上下文不可用，还是模型生成错误。
