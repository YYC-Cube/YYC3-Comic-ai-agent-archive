---
skill: tool-gateway
domain: 05-言启千行
owner_agent: 言启·千行
priority: P0
version: v0.1.0
status: degraded-ok
backing: components：99-编排引擎/drama_stage_adapter.py 的 DramaToolGateway + H3VisionClient
---

# tool-gateway

## 触发条件
生产工具统一网关调用（ComfyUI/H3/SyncNet，桩到实推进中）

## 输入契约
| 参数 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| tool | str | 是 | text_to_image/image_to_video/tts/sync_score/compose |
| params | dict | 是 | 工具参数 |

## 输出契约
| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| result | dict | 含 status（stub_fallback/ok）与产物引用 |

## 依赖
components：99-编排引擎/drama_stage_adapter.py 的 DramaToolGateway + H3VisionClient

## 降级模式
上游不可达/未配置，stub_fallback（永不断流）；H3 走 HMAC claim

## 验收锚点
适配点 A8 / TC-G2-006
