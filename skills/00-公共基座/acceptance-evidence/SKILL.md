---
skill: acceptance-evidence
domain: 00-公共基座
owner_agent: 格物·宗师/验收组
priority: P0
version: v0.1.0
status: degraded-ok
backing: none（待实现，见依赖）
---

# acceptance-evidence

## 触发条件
每条 TC 用例执行后归档证据

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| tc_id | str | 是 | 用例编号 |
| evidence | dict | 是 | 命令原文+输出JSON+trace_id |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| evidence_path | str | NAS 归档路径（降级为本仓 docs/） |

## 依赖
docs/G1-底座通电验收记录-20260926.md（模板先例）

## 降级模式
NAS 未挂载，证据暂存本仓 docs/，挂载后迁移

## 验收锚点
YYC3-60 §六 留证模板
