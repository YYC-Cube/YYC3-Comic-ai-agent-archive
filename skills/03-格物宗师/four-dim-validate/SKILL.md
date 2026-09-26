---
skill: four-dim-validate
domain: 03-格物宗师
owner_agent: 格物·宗师
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：03-格物宗师/gewu_zongshi_agent.py 的 validate
---

# four-dim-validate

## 触发条件
核心输出质检（数值/逻辑/溯源/结构，≥80 红线）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| content | str | 是 | 待检内容 |
| knowledge_context | list | 否 | RAG 上下文 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| score | int | 质检分 |
| passed | bool | 80 分红线 |
| suggestions | str | 修正建议 |
| unverified_claims | list | 无依据断言 |

## 依赖
components：03-格物宗师/gewu_zongshi_agent.py 的 validate

## 降级模式
LLM 不可达，规则四维检查（Mock 兜底）

## 验收锚点
TC-G2-005
