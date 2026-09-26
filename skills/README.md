# YYC³ Skills 技能库（yyc3-ai-agent-archive/skills/）

> 框架定义见仓库根 docs/YYC3-AI-Family-Comic-Drama-Agent/YYC3-AI-Family-Skills技能库框架目录.md
> 事实源分层：本目录为技能层实现事实源；组件背书落位同仓 components/ 目录；验收锚点对齐 docs/YYC3-60。

## 规范要点
1. 一技能一目录一 SKILL.md（契约模板见框架文档 §三）；status 三态：stub → degraded-ok → verified
2. 编号与组件库同构（00 基座 / 01-08 八成员 / 90 RAG / 91 A2A / 95 验收门禁 / 99 编排引擎）
3. 桩先行：每技能必须可在降级模式冒烟；硬件/模型不可达记 STUB/BLOCKED 并登记 M 任务，不算缺陷
4. 验收锚点：每技能声明 TC-G?-???；无锚点不得注册
5. P0 冒烟矩阵：python3 skills/_matrix/p0_smoke_matrix.py（或 skills/95-验收门禁/gate-runner/run_gates.py）

## 当前状态（2026-09-26 建库日）
- 13 域 / 44 技能（P0×27、P1×7、P2×9、P3×1）
- degraded-ok：组件背书技能（契约已按 components/ 真实签名填充）
- stub：待实现技能（已登记 M2-M5 任务与锚点）
