# 01 AI / ML Foundations

> 第一阶段：先理解 AI 是怎么“学”的，再理解为什么它会错。

## 学习目标

完成本章后，你不需要会训练大模型，但必须能用因果链解释：

```text
Dataset → Label → Model → Prediction → Loss → Parameter Update → Training
                                                        ↓
                                              Validation / Test
                                                        ↓
                                                  Generalization
```

## 学习顺序

1. AI / ML / DL：它们是什么、如何区分
2. Traditional Software vs ML：规则系统和学习系统有什么根本区别
3. Dataset：模型究竟从什么东西学习
4. Label：什么叫“正确答案”
5. Model：模型为什么可以产生预测
6. Prediction：输入为什么得到概率/结果
7. Loss / Error：模型怎么知道自己错了
8. Parameter Update：模型为什么会改变
9. Training Loop：学习为什么要重复很多次
10. Neural Network：参数、Layer、Activation、Loss 的位置
11. Validation / Test：为什么训练集不能证明真实能力
12. Generalization：为什么“学会”不等于“会做新题”
13. Distribution Shift：真实世界为什么和训练数据不同
14. Leakage / Contamination：为什么数据泄漏会制造虚假的高分
15. Testing → Evaluation：为什么 AI 质量需要新的方法

## 一个贯穿全章的例子

垃圾短信分类：

```text
输入：恭喜中奖100万

模型第一次预测：
正常 60%
垃圾 40%

真实标签：垃圾
```

模型计算错误，通过 Loss 得到训练信号，再调整参数；大量样本重复这个过程后，模型逐渐形成可泛化的决策能力。

测试工程师要继续追问：

- 训练数据是否代表真实短信？
- 标签是否正确？
- 测试集是否独立？
- 是否出现数据泄漏？
- 换一种表达方式还成立吗？
- 线上分布变化后还成立吗？

这就是从“测试一个结果”进入“评估一个学习系统”。

## 本章暂不展开

Transformer 数学细节、Attention 矩阵、Embedding、RLHF/DPO、LoRA/PEFT、RAG、Agent、LLM-as-a-Judge、Evaluation Harness 将在后续章节学习。

## 出口标准

能够独立解释下面 8 个问题：

1. ML 为什么叫学习？
2. Dataset 和 Label 分别是什么？
3. Model 是什么？
4. Loss 为什么能推动学习？
5. Training 和 Inference 有什么区别？
6. Validation 和 Test 为什么要独立？
7. Generalization 为什么是 AI 测试的核心问题？
8. 为什么 AI Testing 最终会走向 Evaluation？
