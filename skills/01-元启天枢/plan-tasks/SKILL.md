---
skill: plan-tasks
domain: 01-元启天枢
owner_agent: 元启·天枢
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：01-元启天枢/yuanqi_tianshu_agent.py 的 plan_tasks
---

# plan-tasks

## 触发条件
综合任务分解为子任务工单

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| user_input | str | 是 | 综合请求 |
| available_agents | list | 否 | 在线 Agent 能力标签 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| tasks | list | 子任务列表（含执行者/依赖） |

## 依赖
components：01-元启天枢/yuanqi_tianshu_agent.py 的 plan_tasks

## 降级模式
LLM 不可达，规则拆解

## 验收锚点
TC-G2-001 综合场景
