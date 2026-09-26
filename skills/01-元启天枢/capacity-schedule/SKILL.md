---
skill: capacity-schedule
domain: 01-元启天枢
owner_agent: 元启·天枢
priority: P2
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# capacity-schedule

## 触发条件
双 DGX 算力分配/昼夜错峰排产（preview/quality 标签路由）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| tasks | list | 是 | 待排产任务 |
| nodes | dict | 是 | 节点算力状态 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| schedule | dict | 任务到节点/时段映射 |

## 依赖
待实现：M3 任务，对接算力监控数据

## 降级模式
M3 排期

## 验收锚点
G3 门禁
