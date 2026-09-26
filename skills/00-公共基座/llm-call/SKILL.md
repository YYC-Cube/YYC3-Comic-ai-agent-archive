---
skill: llm-call
domain: 00-公共基座
owner_agent: 全体（BaseAgent）
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：00-公共基座/base_agent.py 的 BaseAgent.run
---

# llm-call

## 触发条件
任何 Agent 需要调用 LLM 时；统一走网关 base_url 单入口

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| prompt | str | 是 | 任务提示词 |
| context | str | 否 | RAG 注入上下文，[来源：xxx] 格式 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| text | str | 模型输出；LLM 不可达时为 Mock 文本 |

## 依赖
components：00-公共基座/base_agent.py 的 BaseAgent.run

## 降级模式
openai 未安装或 LLM_BASE_URL 不可达，转 _mock_run 本地兜底

## 验收锚点
TC-G1-002
