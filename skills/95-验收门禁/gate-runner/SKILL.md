---
skill: gate-runner
domain: 95-验收门禁
owner_agent: 格物·宗师/验收组
priority: P0
version: v0.1.0
status: degraded-ok
backing: 本库 skills/_matrix/p0_smoke_matrix.py（已实现）
---

# gate-runner

## 触发条件
TC 用例执行器：P0 冒烟矩阵批量跑 + PASS/STUB/FAIL 判定

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| scope | str | 否 | 默认 p0；可指定域 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| results | dict | 逐技能结果 + 汇总 |

## 依赖
本库 skills/_matrix/p0_smoke_matrix.py（已实现）

## 降级模式
降级模式为正向验收；STUB 需登记 M 任务

## 验收锚点
YYC3-60 全手册
