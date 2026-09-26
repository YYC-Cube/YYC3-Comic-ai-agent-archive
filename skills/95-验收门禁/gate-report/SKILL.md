---
skill: gate-report
domain: 95-验收门禁
owner_agent: 验收组
priority: P0
version: v0.1.0
status: degraded-ok
backing: 本库 skills/95-验收门禁/gate-report/make_report.py（已实现）
---

# gate-report

## 触发条件
门禁报告生成（对齐留证模板格式）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| results | dict | 是 | gate-runner 输出 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| report_md | str | Markdown 报告 |

## 依赖
本库 skills/95-验收门禁/gate-report/make_report.py（已实现）

## 降级模式
纯格式化，无外部依赖

## 验收锚点
YYC3-60 §六 模板
