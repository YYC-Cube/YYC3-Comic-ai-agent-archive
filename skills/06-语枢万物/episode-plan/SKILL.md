---
skill: episode-plan
domain: 06-语枢万物
owner_agent: 语枢·万物
priority: P0
version: v0.1.0
status: degraded-ok
backing: manju-studio script_engine/episode_planner.py + hook_detector.py（规则基线）
---

# episode-plan

## 触发条件
分集规划 + 流量钩子植入（hook_detector）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| episodes | list | 是 | 分集结构 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| plan | list | 含 hook_shots 与 hook_flag 的分镜计划 |

## 依赖
待实现：M2 任务 P1-2（manju-studio script_engine）

## 降级模式
M2 排期

## 验收锚点
TC-G2-007 前置
