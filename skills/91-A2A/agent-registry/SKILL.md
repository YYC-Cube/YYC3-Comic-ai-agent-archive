---
skill: agent-registry
domain: 91-A2A
owner_agent: 全体（A2A）
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：91-A2A-通信协议/a2a_protocol.py 的 AgentRegistry
---

# agent-registry

## 触发条件
Agent Card 注册/心跳/离线剔除改派（30s/90s）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| agent_card | dict | 是 | 身份卡片 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| online | list | 在线 Agent 列表 |

## 依赖
components：91-A2A-通信协议/a2a_protocol.py 的 AgentRegistry

## 降级模式
Redis 不可达，注册 API 可调、存储降级（同步直调切换）

## 验收锚点
总纲 §3.2
