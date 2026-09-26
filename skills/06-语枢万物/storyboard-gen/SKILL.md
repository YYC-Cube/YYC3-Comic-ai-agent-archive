---
skill: storyboard-gen
domain: 06-语枢万物
owner_agent: 语枢·万物
priority: P0
version: v0.1.0
status: degraded-ok
backing: manju-studio script_engine/storyboard_schema.py draft_storyboard（规则草稿，LLM 增强后续）
---

# storyboard-gen

## 触发条件
标准化分镜生成：12 字段 JSON（80-120 镜/集）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| plan | list | 是 | 分镜计划 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| storyboard | dict | 过 storyboard.v1.json Schema 的分镜 JSON |

## 依赖
待实现：M2 任务 P1-3/P1-4（依赖 schema 填充 + storyboard_engine）

## 降级模式
M2 排期

## 验收锚点
TC-G2-007
