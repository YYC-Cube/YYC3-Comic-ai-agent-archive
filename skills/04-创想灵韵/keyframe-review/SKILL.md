---
skill: keyframe-review
domain: 04-创想灵韵
owner_agent: 创想·灵韵
priority: P2
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# keyframe-review

## 触发条件
关键帧终审 + 重绘建议（特征比对）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| frames | list | 是 | 候选帧引用 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| selected | str | 选中帧 |
| rework | list | 重绘建议 |

## 依赖
待实现：M4 任务

## 降级模式
M4 排期

## 验收锚点
G4 门禁
