---
skill: qc-rework-loop
domain: 99-编排引擎
owner_agent: 编排引擎
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：99-编排引擎-全链路闭环/ai_family_orchestrator.py 的 MAX_QC_ROUNDS
---

# qc-rework-loop

## 触发条件
质检到二次优化到复检闭环（2 轮上限，超限放行并标记）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| core_content | str | 是 | 被检内容 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| qc_result | dict | 含 qc_rounds 与末轮 passed |

## 依赖
components：99-编排引擎-全链路闭环/ai_family_orchestrator.py 的 MAX_QC_ROUNDS

## 降级模式
降级模式行为一致（冒烟覆盖）

## 验收锚点
TC-G2-005
