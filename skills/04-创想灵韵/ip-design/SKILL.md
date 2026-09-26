---
skill: ip-design
domain: 04-创想灵韵
owner_agent: 创想·灵韵
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：04-创想灵韵/chuangxiang_lingyun_agent.py 的 brainstorm_ideas
---

# ip-design

## 触发条件
IP 人设/画风/世界观创意（Character DNA 字典锚点）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| topic | str | 是 | 创意主题 |
| direction_count | int | 否 | 路径数，默认3 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| ideas | str | 保守/创新/跨界三路径方案 |

## 依赖
components：04-创想灵韵/chuangxiang_lingyun_agent.py 的 brainstorm_ideas

## 降级模式
LLM 不可达，保守路径直出

## 验收锚点
总纲 §六 阶段1
