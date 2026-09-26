# ==============================================================
# YYC³ AIFamilyOrchestrator 步骤事件埋点 v1.0（M2 收尾 · TC-G2-009）
# 职责：九步闭环每步向 A2A 事件流埋点（trace_id 透传可检索）
# 后端自动选择：Redis Stream（stream:audit:log）→ 不可达/未装降级
#               JSONL 文件 events/<trace_id|untraced>.jsonl（降级留证不缺）
# 对齐：a2a_protocol 消息规范（91-A2A）；YYC3-60 TC-G2-009
# 依赖：redis 可选；文件后端仅标准库
# ==============================================================
import json
import os
import time
from pathlib import Path

EVENTS_DIR = Path(__file__).resolve().parents[1] / "events"


class StepEventEmitter:
    """步骤事件发射器：redis 可用走 Stream，否则 JSONL 文件降级（正向验收）"""

    def __init__(self, events_dir: Path = None):
        self.events_dir = Path(events_dir) if events_dir else EVENTS_DIR
        self.backend = "file"
        self._producer = None
        try:
            from a2a_protocol import MessageProducer  # 组件库 91-A2A
            import redis  # noqa: F401
            self._producer = MessageProducer
            self.backend = "redis"
        except Exception:  # noqa: BLE001  redis 未安装/模块缺失 → 文件降级
            self.backend = "file"
        self.events_dir.mkdir(parents=True, exist_ok=True)

    def emit(self, step: str, trace_id, payload: dict = None,
             status: str = "ok") -> dict:
        """埋点单条步骤事件；trace_id 可为 None（Step1 拦截场景）"""
        event = {
            "ts": int(time.time() * 1000),
            "trace_id": trace_id,
            "step": step,
            "status": status,
            "payload": payload or {},
        }
        if self.backend == "redis" and self._producer is not None:
            try:
                self._producer.send_task(
                    "stream:audit:log",
                    {"trace_id": trace_id or "", "step": step, "event": event})
                return event
            except Exception:  # noqa: BLE001  redis 运行期故障 → 文件兜底
                self.backend = "file"
        key = trace_id or "untraced"
        with open(self.events_dir / f"{key}.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
        return event

    @staticmethod
    def replay(trace_id) -> list:
        """按 trace_id 检索事件流（TC-G2-009 的取证入口）"""
        key = trace_id or "untraced"
        path = EVENTS_DIR / f"{key}.jsonl"
        if not path.exists():
            return []
        return [json.loads(line) for line in
                path.read_text(encoding="utf-8").splitlines() if line.strip()]


__all__ = ["StepEventEmitter", "EVENTS_DIR"]
