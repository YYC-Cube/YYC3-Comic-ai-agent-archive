---
skill: fact-trace
domain: 03-格物宗师
owner_agent: 格物·宗师
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：03-格物宗师/gewu_zongshi_agent.py 的 validate（溯源维度）
---

# fact-trace

## 触发条件
事实断言溯源核查（幻觉率<3% 红线）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| content | str | 是 | 含断言的内容 |
| knowledge_context | list | 是 | RAG 引用原文 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| unverified_claims | list | 缺 [来源：] 的断言清单 |

## 依赖
components：03-格物宗师/gewu_zongshi_agent.py 的 validate（溯源维度）

## 降级模式
LLM 不可达，规则匹配 [来源：] 标记

## 验收锚点
总纲 §3.4 红线3
