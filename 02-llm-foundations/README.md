# 02 LLM Foundations

这一章把上一章的“模型”连接到现代 LLM。

## 主线

```text
Text → Token → Embedding → Transformer → Next-token Prediction → Generation
```

## 学习内容

- Token / Tokenization / Vocabulary
- Embedding 与语义表示
- Transformer 与 Self-Attention
- Context Window
- Parameters / Weights
- Pre-training 与 Inference
- Decoding：Temperature / Top-p / Top-k
- Structured Output / Tool Calling

## 测试视角

重点不是背架构图，而是理解哪些机制会改变模型行为：输入长度、上下文、采样参数、模型版本、输出约束等，并能设计可复现的对照实验。

## 出口

能够解释一次 LLM 请求从文本输入到生成输出的主要路径，并能针对 Token、Context、Sampling、Structured Output 设计基础实验。
