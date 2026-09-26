---
skill: storyboard-schema-check
domain: 03-格物宗师
owner_agent: 格物·宗师
priority: P0
version: v0.1.0
status: degraded-ok
backing: components 背书：manju-studio script_engine/storyboard_schema.py（校验+草稿生成）
---

# storyboard-schema-check

## 触发条件
分镜 JSON 过 storyboard.v1.json 12 字段 Schema

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| storyboard | dict | 是 | 分镜 JSON |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| valid | bool | 0 errors 才 True |
| errors | list | 字段级错误 |

## 依赖
待实现：schema 文件待填充（适配点 A7，manju-studio P1-3）

## 降级模式
M2 排期

## 验收锚点
TC-G2-007
