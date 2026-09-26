---
skill: rag-retrieve
domain: 90-公共RAG
owner_agent: 全体（Step3）
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：90-公共RAG-知识库/milvus_retriever.py 的 search + 编排引擎 _get_knowledge
---

# rag-retrieve

## 触发条件
知识检索与上下文注入（[来源：] 强制标识）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| query | str | 是 | 检索词 |
| top_k | int | 否 | 默认5 |
| category | str | 否 | 分类过滤 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| docs | list | source/content 结构化结果 |
| degraded | bool | Milvus 不可达标记 |

## 依赖
components：90-公共RAG-知识库/milvus_retriever.py 的 search + 编排引擎 _get_knowledge

## 降级模式
Milvus 不可达，返回空列表并标记 degraded（YYC3-AGT-5001，正向验收）

## 验收锚点
TC-G2-004
