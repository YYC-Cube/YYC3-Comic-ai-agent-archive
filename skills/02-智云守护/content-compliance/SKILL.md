---
skill: content-compliance
domain: 02-智云守护
owner_agent: 智云·守护
priority: P1
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# content-compliance

## 触发条件
素材入库前版权校验 + 成片上线前备案预检

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| asset_ref | str | 是 | 素材/成片引用 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| compliant | bool | 是否合规 |
| issues | list | 风险清单 |

## 依赖
待实现：M3-M4 任务

## 降级模式
M3-M4 排期

## 验收锚点
YYC3-09 风险#4 版权备案
