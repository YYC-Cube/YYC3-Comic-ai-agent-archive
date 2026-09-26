---
skill: intent-routing
domain: 05-言启千行
owner_agent: 言启·千行
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：05-言启千行/yanqi_qianhang_agent.py 的 run（LLM+规则双路）
---

# intent-routing

## 触发条件
链路入口意图识别与路由（Step2，生成 trace_id）；漫剧意图扩展中

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| user_input | str | 是 | 用户请求 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| intent | str | 意图类型 |
| complexity | str | simple/complex/multi_agent |
| need_rag | bool | 是否需检索 |
| trace_id | str | trace-YYYYMMDD-xxxxxx |

## 依赖
components：05-言启千行/yanqi_qianhang_agent.py 的 run（LLM+规则双路）

## 降级模式
LLM 不可达，关键词规则兜底路由

## 验收锚点
TC-G2-001
