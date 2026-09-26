---
skill: nightly-batch
domain: 99-编排引擎
owner_agent: 编排引擎
priority: P2
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# nightly-batch

## 触发条件
昼夜错峰批量流水线编排（对接 nightly_run.sh）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| project_ids | list | 是 | 项目清单 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| batch_report | dict | 夜批产出统计 |

## 依赖
待实现：M3 任务，依赖 DGX 就位

## 降级模式
M3 排期

## 验收锚点
G3 门禁（夜间 DGX 利用率≥85%）
