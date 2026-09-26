---
skill: kb-import-nas
domain: 90-公共RAG
owner_agent: 语枢·万物
priority: P1
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# kb-import-nas

## 触发条件
NAS 文档批量入库（OCR→embed→Milvus）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| nas_dir | str | 是 | NAS 文档目录 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| imported | int | 入库条数 |

## 依赖
待实现：M2-M3（batch_import_from_nas 组件已在位，缺 OCR/embed 服务）

## 降级模式
M2-M3 排期

## 验收锚点
YYC3-05 §2.3 入库链路
