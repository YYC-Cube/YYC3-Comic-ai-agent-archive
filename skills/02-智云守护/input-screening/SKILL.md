---
skill: input-screening
domain: 02-智云守护
owner_agent: 智云·守护
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：02-智云守护/zhiyun_shouhu_agent.py 的 check_input
---

# input-screening

## 触发条件
一切输入进入链路前（Step1）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| user_input | str | 是 | 原始输入 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| safe | bool | 是否放行 |
| risk | str | 风险说明 |
| level | str | L1注入/L2 PII/L3合规 |

## 依赖
components：02-智云守护/zhiyun_shouhu_agent.py 的 check_input

## 降级模式
三级过滤模型不可达，规则引擎兜底（注入关键词/PII 正则）

## 验收锚点
TC-G2-003 场景D
