---
skill: pace-diagnosis
domain: 07-预见先知
owner_agent: 预见·先知
priority: P3
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# pace-diagnosis

## 触发条件
节奏诊断 → 反哺 hook_detector 参数（数据闭环）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| metrics | dict | 是 | 运营指标 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| diagnosis | dict | 节奏问题与参数建议 |

## 依赖
待实现：M5 任务

## 降级模式
M5 排期

## 验收锚点
G5 门禁
