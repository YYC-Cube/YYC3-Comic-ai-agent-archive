---
skill: regression-anchor
domain: 95-验收门禁
owner_agent: 验收组
priority: P0
version: v0.1.0
status: degraded-ok
backing: 本库 skills/95-验收门禁/regression-anchor/regression_anchor.py（已实现）
---

# regression-anchor

## 触发条件
回归锚点：场景D拦截/RAG降级/质检2轮上限 必测，FAIL 即回退引擎版本

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| 无 | - | - | 直接运行 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| pass_count | int | 锚点通过数 |

## 依赖
本库 skills/95-验收门禁/regression-anchor/regression_anchor.py（已实现）

## 降级模式
全程降级模式可跑

## 验收锚点
TC-G2-003/004/005
