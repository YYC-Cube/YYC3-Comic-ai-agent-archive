---
skill: novel-split
domain: 06-语枢万物
owner_agent: 语枢·万物
priority: P0
version: v0.1.0
status: degraded-ok
backing: manju-studio script_engine/splitter.py（规则基线）
---

# novel-split

## 触发条件
小说清洗/章节拆分/剧情要素抽取

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| novel_path | str | 是 | NAS 小说路径 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| episodes | list | 分集结构 |
| entities | dict | 角色/场景/对话要素 |

## 依赖
待实现：M2 任务 P1-2（manju-studio script_engine）

## 降级模式
M2 排期

## 验收锚点
TC-G2-007 前置
