# Skills 总索引（13 域 44 技能）

| 域 | 技能 | P级 | 状态 | 验收锚点 | 依赖/落位 |
| -- | ---- | --- | ---- | -------- | --------- |
| 00-公共基座 | llm-call | P0 | degraded-ok | TC-G1-002 | components：00-公共基座/base_agent.py 的 BaseAgent.run |
| 00-公共基座 | nas-path | P0 | degraded-ok | TC-G1-003/004 | manju-studio/scripts/init_nas_path.sh + 0379-world path_normalize 中间件 |
| 00-公共基座 | audit-log | P0 | degraded-ok | 总纲 §3.2 审计流 | components：02-智云守护/zhiyun_shouhu_agent.py 的 write_audit_log |
| 00-公共基座 | env-config | P0 | degraded-ok | YYC3-06 §7.3 密钥零入库 | 各仓 .gitignore / .env.example |
| 00-公共基座 | acceptance-evidence | P0 | degraded-ok | YYC3-60 §六 留证模板 | docs/G1-底座通电验收记录-20260926.md（模板先例） |
| 01-元启天枢 | five-step-decision | P0 | degraded-ok | 总纲 §五 Step6 | components：01-元启天枢/yuanqi_tianshu_agent.py 的 decide |
| 01-元启天枢 | plan-tasks | P0 | degraded-ok | TC-G2-001 综合场景 | components：01-元启天枢/yuanqi_tianshu_agent.py 的 plan_tasks |
| 01-元启天枢 | capacity-schedule | P2 | stub | G3 门禁 | 待实现：M3 任务，对接算力监控数据 |
| 02-智云守护 | input-screening | P0 | degraded-ok | TC-G2-003 场景D | components：02-智云守护/zhiyun_shouhu_agent.py 的 check_input |
| 02-智云守护 | output-audit | P0 | degraded-ok | 总纲 §五 Step8 | components：02-智云守护/zhiyun_shouhu_agent.py 的 audit |
| 02-智云守护 | consistency-check | P1 | stub | G3 门禁（一致性≥80%） | 待实现：M3 任务，依赖 face_encoder 真实 512 维特征 |
| 02-智云守护 | content-compliance | P1 | stub | YYC3-09 风险#4 版权备案 | 待实现：M3-M4 任务 |
| 03-格物宗师 | four-dim-validate | P0 | degraded-ok | TC-G2-005 | components：03-格物宗师/gewu_zongshi_agent.py 的 validate |
| 03-格物宗师 | fact-trace | P0 | degraded-ok | 总纲 §3.4 红线3 | components：03-格物宗师/gewu_zongshi_agent.py 的 validate（溯源维度） |
| 03-格物宗师 | storyboard-schema-check | P0 | degraded-ok | TC-G2-007 | 待实现：schema 文件待填充（适配点 A7，manju-studio P1-3） |
| 04-创想灵韵 | ip-design | P0 | degraded-ok | 总纲 §六 阶段1 | components：04-创想灵韵/chuangxiang_lingyun_agent.py 的 brainstorm_ideas |
| 04-创想灵韵 | prompt-engineering | P1 | stub | YYC3-02 §2.2.3 | 待实现：M3 任务，对接 storyboard_engine/prompt_engine |
| 04-创想灵韵 | style-keeping | P1 | stub | G3 门禁 | 待实现：M3 任务，对接 style_keeper |
| 04-创想灵韵 | keyframe-review | P2 | stub | G4 门禁 | 待实现：M4 任务 |
| 05-言启千行 | intent-routing | P0 | degraded-ok | TC-G2-001 | components：05-言启千行/yanqi_qianhang_agent.py 的 run（LLM+规则双路） |
| 05-言启千行 | tool-gateway | P0 | degraded-ok | 适配点 A8 / TC-G2-006 | components：99-编排引擎/drama_stage_adapter.py 的 DramaToolGateway + H3VisionClient |
| 05-言启千行 | batch-submit | P2 | stub | YYC3-01 §5.4 异常分级 | 待实现：M3 任务 |
| 05-言启千行 | script-dev | P1 | stub | YYC3-08 P2-6 | 待实现：随 M2/M3 排期 |
| 06-语枢万物 | novel-split | P0 | degraded-ok | TC-G2-007 前置 | 待实现：M2 任务 P1-2（manju-studio script_engine） |
| 06-语枢万物 | episode-plan | P0 | degraded-ok | TC-G2-007 前置 | 待实现：M2 任务 P1-2（manju-studio script_engine） |
| 06-语枢万物 | storyboard-gen | P0 | degraded-ok | TC-G2-007 | 待实现：M2 任务 P1-3/P1-4（依赖 schema 填充 + storyboard_engine） |
| 07-预见先知 | hit-forecast | P2 | stub | G4/G5 门禁 | 待实现：M4 任务（组件 full_forecast 可复用，缺运营数据源） |
| 07-预见先知 | ops-data-collect | P2 | stub | YYC3-06 §4.4 | 待实现：M4 任务 |
| 07-预见先知 | pace-diagnosis | P3 | stub | G5 门禁 | 待实现：M5 任务 |
| 08-知遇伯乐 | capacity-profile | P2 | stub | YYC3-03 阶段6 | 待实现：M4 任务（组件 build_user_profile 可复用） |
| 08-知遇伯乐 | asset-recommend | P2 | stub | YYC3-06 资产闭环 | 待实现：M4 任务（组件 recommend_content 可复用） |
| 08-知遇伯乐 | asset-deposit | P2 | stub | YYC3-06 §5.3 | 待实现：M4 任务 |
| 90-公共RAG | rag-retrieve | P0 | degraded-ok | TC-G2-004 | components：90-公共RAG-知识库/milvus_retriever.py 的 search + 编排引擎 _get_knowledge |
| 90-公共RAG | kb-import-nas | P1 | stub | YYC3-05 §2.3 入库链路 | 待实现：M2-M3（batch_import_from_nas 组件已在位，缺 OCR/embed 服务） |
| 91-A2A | a2a-message | P0 | degraded-ok | TC-G2-009 | components：91-A2A-通信协议/a2a_protocol.py 的 build_message/parse_message |
| 91-A2A | agent-registry | P0 | degraded-ok | 总纲 §3.2 | components：91-A2A-通信协议/a2a_protocol.py 的 AgentRegistry |
| 91-A2A | a2a-v1-mapping | P1 | stub | 总纲 §9.3 遗留② | 待实现：P2 穿插任务（升级不替换） |
| 95-验收门禁 | gate-runner | P0 | degraded-ok | YYC3-60 全手册 | 本库 skills/_matrix/p0_smoke_matrix.py（已实现） |
| 95-验收门禁 | gate-report | P0 | degraded-ok | YYC3-60 §六 模板 | 本库 skills/95-验收门禁/gate-report/make_report.py（已实现） |
| 95-验收门禁 | regression-anchor | P0 | degraded-ok | TC-G2-003/004/005 | 本库 skills/95-验收门禁/regression-anchor/regression_anchor.py（已实现） |
| 99-编排引擎 | scene-branch | P0 | degraded-ok | TC-G2-002 | components：99-编排引擎-全链路闭环/ai_family_orchestrator.py 的 execute |
| 99-编排引擎 | stage-adapter | P0 | degraded-ok | TC-G2-006 | components：99-编排引擎-全链路闭环/drama_stage_adapter.py 的 DramaStageAdapter |
| 99-编排引擎 | qc-rework-loop | P0 | degraded-ok | TC-G2-005 | components：99-编排引擎-全链路闭环/ai_family_orchestrator.py 的 MAX_QC_ROUNDS |
| 99-编排引擎 | nightly-batch | P2 | stub | G3 门禁（夜间 DGX 利用率≥85%） | 待实现：M3 任务，依赖 DGX 就位 |
