---
skill: stage-adapter
domain: 99-编排引擎
owner_agent: 编排引擎
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：99-编排引擎-全链路闭环/drama_stage_adapter.py 的 DramaStageAdapter
---

# stage-adapter

## 触发条件
漫剧六阶段状态机 run_stage/run_pipeline/rewind/snapshot

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| project_id | str | 是 | 项目 ID |
| stage | str | 是 | 六阶段枚举 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| stage_result | dict | status/trace_id 三键 |
| snapshot | dict | 全阶段状态 |

## 依赖
components：99-编排引擎-全链路闭环/drama_stage_adapter.py 的 DramaStageAdapter

## 降级模式
全降级可跑；工具经 DramaToolGateway 桩

## 验收锚点
TC-G2-006
