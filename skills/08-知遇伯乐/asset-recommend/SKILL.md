---
skill: asset-recommend
domain: 08-知遇伯乐
owner_agent: 知遇·伯乐
priority: P2
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# asset-recommend

## 触发条件
Seed/LoRA/模板复用推荐（match_score+理由链）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| scene | str | 是 | 生产场景 |
| knowledge_pool | list | 是 | 候选资产 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| recommendations | list | match_score+reason 结构化推荐 |

## 依赖
待实现：M4 任务（组件 recommend_content 可复用）

## 降级模式
M4 排期

## 验收锚点
YYC3-06 资产闭环
