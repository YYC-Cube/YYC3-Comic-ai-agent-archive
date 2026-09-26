---
skill: consistency-check
domain: 02-智云守护
owner_agent: 智云·守护
priority: P1
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# consistency-check

## 触发条件
关键帧生成后逐帧校验（对接 anchor_guard/face_library）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| image_ref | str | 是 | 帧图路径 |
| character_id | str | 是 | 角色 ID |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| passed | bool | 一致性是否达标 |
| similarity | float | 特征相似度 |

## 依赖
待实现：M3 任务，依赖 face_encoder 真实 512 维特征

## 降级模式
M3 排期

## 验收锚点
G3 门禁（一致性≥80%）
