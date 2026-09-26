---
skill: env-config
domain: 00-公共基座
owner_agent: 全体（工程纪律）
priority: P0
version: v0.1.0
status: degraded-ok
backing: none（待实现，见依赖）
---

# env-config

## 触发条件
仓库初始化、CI 密钥扫描、新环境搭建

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| repo | str | 是 | 四仓库名 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| gitignore_has_env | bool | gitignore 含 .env 规则 |
| env_example_exists | bool | .env.example 模板在位 |

## 依赖
各仓 .gitignore / .env.example

## 降级模式
纯文件检查，无外部依赖

## 验收锚点
YYC3-06 §7.3 密钥零入库
