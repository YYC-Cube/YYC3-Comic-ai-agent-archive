---
skill: style-keeping
domain: 04-创想灵韵
owner_agent: 创想·灵韵
priority: P1
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# style-keeping

## 触发条件
风格种子/LUT/色彩配置持久化，同角色跨镜头强制一致

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| project_id | str | 是 | 项目 ID |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| style_profile | dict | 种子+LUT+笔触参数 |

## 依赖
待实现：M3 任务，对接 style_keeper

## 降级模式
M3 排期

## 验收锚点
G3 门禁
