---
skill: script-dev
domain: 05-言启千行
owner_agent: 言启·千行
priority: P1
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# script-dev

## 触发条件
生产自动化脚本开发维护（nightly_run.sh/init_nas_path.sh）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| requirement | str | 是 | 脚本需求 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| script_path | str | 脚本落位路径 |

## 依赖
待实现：随 M2/M3 排期

## 降级模式
M2-M3 排期

## 验收锚点
YYC3-08 P2-6
