---
skill: audit-log
domain: 00-公共基座
owner_agent: 智云·守护
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：02-智云守护/zhiyun_shouhu_agent.py 的 write_audit_log
---

# audit-log

## 触发条件
九步闭环每步执行后；拦截/阻断/降级事件必写

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| trace_id | str | 是 | 全链追踪 ID |
| action | str | 是 | 动作名 |
| detail | dict | 是 | 结构化详情 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| None | - | 写入 stream:audit:log / 本地降级打印 |

## 依赖
components：02-智云守护/zhiyun_shouhu_agent.py 的 write_audit_log

## 降级模式
Redis/NAS 不可达，本地打印降级（留证不缺）

## 验收锚点
总纲 §3.2 审计流
