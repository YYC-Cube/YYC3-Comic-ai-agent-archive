---
skill: scene-branch
domain: 99-编排引擎
owner_agent: 编排引擎
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：99-编排引擎-全链路闭环/ai_family_orchestrator.py 的 execute
---

# scene-branch

## 触发条件
ReAct-C 场景分支 A-F 裁剪执行

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| user_input | str | 是 | 请求 |
| scene | str | 否 | A-F，None 自动路由 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| result | dict | 含 steps/agent_outputs/trace_id/status |

## 依赖
components：99-编排引擎-全链路闭环/ai_family_orchestrator.py 的 execute

## 降级模式
LLM/RAG 全降级仍可跑（冒烟基准）

## 验收锚点
TC-G2-002
