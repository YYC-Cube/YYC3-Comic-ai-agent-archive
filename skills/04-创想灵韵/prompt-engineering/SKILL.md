---
skill: prompt-engineering
domain: 04-创想灵韵
owner_agent: 创想·灵韵
priority: P1
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# prompt-engineering

## 触发条件
分镜文生图提示词工程 + 负面提示词

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| shot | dict | 是 | 单镜头参数 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| prompt | str | 正向提示词 |
| negative | str | 负面提示词 |

## 依赖
待实现：M3 任务，对接 storyboard_engine/prompt_engine

## 降级模式
M3 排期

## 验收锚点
YYC3-02 §2.2.3
