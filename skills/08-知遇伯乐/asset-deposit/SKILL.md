---
skill: asset-deposit
domain: 08-知遇伯乐
owner_agent: 知遇·伯乐
priority: P2
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# asset-deposit

## 触发条件
优质资产自动沉淀到 NAS assets/ 并注册 Skill

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| asset | dict | 是 | 优质产物（Seed/LoRA/模板） |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| deposit_path | str | NAS 落位路径 |
| skill_id | str | 注册的 Skill ID |

## 依赖
待实现：M4 任务

## 降级模式
M4 排期

## 验收锚点
YYC3-06 §5.3
