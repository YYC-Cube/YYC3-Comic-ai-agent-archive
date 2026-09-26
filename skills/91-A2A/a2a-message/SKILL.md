---
skill: a2a-message
domain: 91-A2A
owner_agent: 全体（A2A）
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：91-A2A-通信协议/a2a_protocol.py 的 build_message/parse_message
---

# a2a-message

## 触发条件
Agent 间消息封套构建与解析（10 字段）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| trace_id | str | 是 | 全链追踪 |
| msg_type | str | 是 | task_request/task_result/heartbeat/error |
| sender | str | 是 | 发送方 |
| receiver | str | 是 | 接收方 |
| task_type | str | 是 | 能力标签 |
| payload | dict | 是 | 载荷 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| message | dict | 含 msg_id(雪花)/timestamp/ttl 的标准封套 |

## 依赖
components：91-A2A-通信协议/a2a_protocol.py 的 build_message/parse_message

## 降级模式
Redis 未装，封套构建/解析纯函数可用（收发降级）

## 验收锚点
TC-G2-009
