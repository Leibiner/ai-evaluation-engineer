# 01 AI / ML Foundations

> 第一阶段：先理解 AI 是怎么“学”的，再理解为什么它会错。

## 阶段目标

你是从传统软件测试进入 AI Evaluation，因此这一阶段不以“会算法”为目标，而以**建立 AI 的底层因果模型**为目标。

学完后，你应该能够解释：

```text
数据
 ↓
Label / Ground Truth
 ↓
Model
 ↓
Training
 ↓
Prediction / Inference
 ↓
Error / Loss
 ↓
Optimization
 ↓
Parameter Update
 ↓
Validation / Test
 ↓
Generalization
 ↓
Evaluation
```

核心问题只有一个：

> **一个 AI 模型为什么会得到这个结果？为什么可能错？我们如何证明它好不好？**

---

# 学习内容

## 01. AI、ML、DL 到底是什么

建立 AI 世界的基本地图：

```text
AI
└── Machine Learning
    └── Deep Learning
        └── Neural Network
```

进一步知道：

```text
Neural Network
      ↓
Transformer
      ↓
现代 LLM 的主要基础架构
```

学习：

- AI
- Machine Learning
- Deep Learning
- Neural Network
- 规则系统 vs 机器学习
- 传统程序 vs 学习系统
- 为什么机器学习不是写更多 if / else

**出口：** 能解释“机器学习里的学习到底发生在哪里”。

---

## 02. Dataset：模型到底从什么东西学习

学习：

- Dataset
- Sample
- Feature
- Input
- Training Set
- Validation Set
- Test Set
- 数据分布
- 数据质量
- 数据偏差

核心模型：

```text
Dataset
   ↓
Input + Label
   ↓
模型从大量样本中学习规律
```

**出口：** 能解释为什么模型需要数据，以及数据质量为什么会影响模型质量。

---

## 03. Label / Annotation：正确答案从哪里来

学习：

- Label
- Ground Truth
- Annotation
- Human Annotation
- Reference
- Label Quality
- Label Noise
- 标注一致性

与传统测试建立对应：

```text
传统测试：Expected Result
AI：       Ground Truth / Reference
```

**出口：** 能解释“正确答案”是什么，以及为什么正确答案本身也可能有问题。

---

## 04. Model：模型到底是什么

学习：

- Model
- Parameter
- Weight
- Bias
- Model Architecture
- Feature 与 Parameter 的区别
- 模型为什么可以表示复杂关系
- 模型为什么不是固定业务规则

核心结构：

```text
Input
  ↓
Model
  ↓
Prediction
```

**出口：** 能用自己的话解释 Model 和 Parameter，而不是把模型理解成一个黑盒 API。

---

## 05. Prediction / Inference：模型如何得到结果

学习：

- Prediction
- Inference
- Probability / Score
- Classification
- Regression
- Error
- Training vs Inference

贯穿案例：

```text
输入：恭喜中奖100万

模型预测：
正常：60%
垃圾：40%

Ground Truth：垃圾
```

因此：

```text
Prediction ≠ Ground Truth
```

**出口：** 能解释模型从输入到输出发生了什么，以及 Training 和 Inference 的区别。

---

## 06. Error / Loss：模型怎么知道自己错了

核心链路：

```text
Prediction
    ↓
与 Ground Truth 比较
    ↓
Error / Loss
```

学习：

- Error
- Loss
- Loss Function
- 为什么需要 Loss
- Loss 大小意味着什么
- 不同任务为什么可能使用不同 Loss

重要纠正：

> 不是系统口头告诉模型“你错了，正确答案是垃圾”，而是训练数据提供 Target / Label，Loss Function 对 Prediction 与 Target 进行计算，再将结果用于优化。

**出口：** 能解释 Loss 在训练中的作用。

---

## 07. Optimization：模型怎么根据错误改进

核心链路：

```text
Prediction
    ↓
Loss
    ↓
Gradient
    ↓
Parameter Update
    ↓
新的 Model
```

学习：

- Gradient
- Gradient Descent
- Optimizer
- Learning Rate
- Parameter Update
- Backpropagation

第一阶段以概念理解为主，不要求一开始手算复杂公式。

**出口：** 能解释模型为什么能够根据错误调整参数。

---

## 08. Training：模型到底怎么训练出来

把前面的内容串起来：

```text
Dataset
   ↓
Input + Label
   ↓
Model
   ↓
Prediction
   ↓
Loss
   ↓
Backpropagation
   ↓
Parameter Update
   ↓
Repeat
```

学习：

- Training
- Training Loop
- Epoch
- Batch
- Iteration / Step
- Forward Pass
- Backward Pass
- Backpropagation
- Optimizer
- Learning Rate

**出口：** 能完整解释一个模型从数据到能够预测，中间经历了什么。

---

## 09. Validation / Test：训练得好就代表好吗

学习：

- Training Set
- Validation Set
- Test Set
- 三者的区别
- 为什么不能只看 Training Loss
- 为什么 Test Set 要尽量独立
- Data Leakage 的基本概念

传统测试与 AI 的连接：

```text
传统软件：
输入 → Expected → Actual → Pass / Fail

AI：
Input → Prediction → Ground Truth → Evaluation
```

**出口：** 能解释为什么训练集上的高分不能证明模型真实能力。

---

## 10. Generalization：为什么模型学会了却不会做

学习：

- Generalization
- Overfitting
- Underfitting
- Bias / Variance 基本概念
- 为什么训练集表现好，未知数据却可能表现差

核心现象：

```text
Training Data
      ↓
模型表现很好
      ↓
New / Real-world Data
      ↓
模型表现下降
```

**出口：** 能解释“记住训练数据”和“学会可泛化规律”的区别。

---

## 11. Distribution Shift：真实世界为什么会让模型失效

学习：

- Distribution
- Distribution Shift
- Data Drift
- Concept Drift 基本概念
- 为什么线上模型可能越来越差

核心结构：

```text
Training Distribution
        ↓
      Model
        ↓
Real-world Distribution
```

**出口：** 能解释为什么模型离线测试很好，线上可能逐渐失效。

---

## 12. Data Leakage / Test Contamination：为什么测试结果可能是假的

学习：

- Data Leakage
- Test Contamination
- 为什么测试数据必须保持独立
- 为什么数据泄漏会导致虚假的高分

核心认知：

> **如果测试数据已经进入训练过程，Evaluation 结果就可能失去可信度。**

**出口：** 能识别基本的数据泄漏和测试污染问题。

---

# 第一阶段的核心因果链

不要把 12 个模块当成 12 个孤立知识点。

最终必须形成：

```text
AI
 ↓
Machine Learning
 ↓
Dataset
 ↓
Input + Label
 ↓
Model
 ↓
Training
 ↓
Prediction / Inference
 ↓
Error
 ↓
Loss
 ↓
Gradient / Optimization
 ↓
Parameter Update
 ↓
Training Loop
 ↓
Validation / Test
 ↓
Generalization
 ↓
Distribution Shift
 ↓
Evaluation
```

---

# 第一阶段完成标准

不要求你成为算法工程师，也不要求你从零训练大型模型。

但必须能够不用背稿解释：

1. AI、ML、DL 分别是什么。
2. Dataset、Sample、Feature、Label 分别是什么。
3. Ground Truth 和 Annotation 是什么。
4. Model 和 Parameter 是什么。
5. Training 和 Inference 有什么区别。
6. Prediction 为什么会错。
7. Loss 为什么能够帮助模型学习。
8. Gradient、Optimization、Parameter Update 在做什么。
9. Training Loop 是什么。
10. Training / Validation / Test 有什么区别。
11. Generalization 是什么。
12. Overfitting / Underfitting 是什么。
13. Distribution Shift 是什么。
14. Data Leakage / Test Contamination 为什么会影响评测可信度。
15. 为什么 AI 最终必须进入 Evaluation。

## 最终能力

给你一个问题：

> “为什么这个模型把‘恭喜中奖100万’判断成正常？”

你应该能够沿着：

```text
Data
 ↓
Label
 ↓
Model
 ↓
Training
 ↓
Parameters
 ↓
Inference
 ↓
Prediction
 ↓
Error / Loss
 ↓
Generalization
 ↓
Evaluation
```

逐层分析可能原因，而不是只说：

> “模型有 Bug。”

**达到这个标准后，再进入 Phase 02。**
