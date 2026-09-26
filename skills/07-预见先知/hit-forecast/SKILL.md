---
skill: hit-forecast
domain: 07-预见先知
owner_agent: 预见·先知
priority: P2
version: v0.1.0
status: stub
backing: none（待实现，见依赖）
---

# hit-forecast

## 触发条件
爆款潜质预测（定量 95%CI + LLM 定性）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| metric | str | 是 | 指标名 |
| history | list | 是 | 历史数据 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| forecast_values | list | 预测值 |
| confidence_upper | list | 95% 置信上界 |
| confidence_lower | list | 95% 置信下界 |

## 依赖
待实现：M4 任务（组件 full_forecast 可复用，缺运营数据源）

## 降级模式
M4 排期

## 验收锚点
G4/G5 门禁
