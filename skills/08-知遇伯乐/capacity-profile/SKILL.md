---
skill: capacity-profile
domain: 08-知遇伯乐
owner_agent: 知遇·伯乐
priority: P2
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# capacity-profile

## 触发条件
产能画像与效能分析

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| user_id | str | 是 | 生产者 ID |
| behavior | dict | 是 | 生产行为数据 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| profile | dict | 7 字段画像 |
| capacity_report | dict | 产能/交付效率 |

## 依赖
待实现：M4 任务（组件 build_user_profile 可复用）

## 降级模式
M4 排期

## 验收锚点
YYC3-03 阶段6
