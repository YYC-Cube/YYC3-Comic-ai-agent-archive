---
skill: output-audit
domain: 02-智云守护
owner_agent: 智云·守护
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：02-智云守护/zhiyun_shouhu_agent.py 的 audit
---

# output-audit

## 触发条件
一切输出交付用户前（Step8）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| content | str | 是 | 待审计内容 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| safe | bool | 是否通过 |
| desensitized_content | str | 脱敏后内容 |
| findings | list | 审计发现 |

## 依赖
components：02-智云守护/zhiyun_shouhu_agent.py 的 audit

## 降级模式
合规模型不可达，PII 正则脱敏兜底

## 验收锚点
总纲 §五 Step8
