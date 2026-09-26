---
skill: a2a-v1-mapping
domain: 91-A2A
owner_agent: 言启·千行
priority: P1
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# a2a-v1-mapping

## 触发条件
自研 Redis Stream 协议向 A2A v1.0 标准 Agent Card 映射

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| card | dict | 是 | 自研卡片 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| v1_card | dict | A2A v1.0 标准格式 |

## 依赖
待实现：P2 穿插任务（升级不替换）

## 降级模式
P2 穿插

## 验收锚点
总纲 §9.3 遗留②
