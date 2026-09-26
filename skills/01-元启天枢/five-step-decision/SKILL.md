---
skill: five-step-decision
domain: 01-元启天枢
owner_agent: 元启·天枢
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：01-元启天枢/yuanqi_tianshu_agent.py 的 decide
---

# five-step-decision

## 触发条件
重大决策：≥3 方案 + 加权评分（战略30/财务25/难度20/风险15/长期10）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| user_input | str | 是 | 决策问题 |
| knowledge | list | 否 | RAG 上下文 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| decision | dict | 含方案数组/评分/推荐/关键假设/人类确认位 |

## 依赖
components：01-元启天枢/yuanqi_tianshu_agent.py 的 decide

## 降级模式
LLM 不可达，规则骨架决策（Mock 文本兜底）

## 验收锚点
总纲 §五 Step6
