# ==============================================================
# gate-runner：TC 用例执行器（YYC3-60 对齐 · 技能 95-验收门禁/gate-runner）
# 复用 P0 冒烟矩阵，输出结构化 JSON 结果（供 gate-report 消费）
# 运行：python3 skills/95-验收门禁/gate-runner/run_gates.py [--json > results.json]
# ==============================================================
import importlib.util
import json
import sys
from pathlib import Path

# 字面量路径：技能库根下固定位置（安全白名单）
MATRIX = Path(__file__).resolve().parents[2] / "_matrix" / "p0_smoke_matrix.py"


def load_matrix():
    spec = importlib.util.spec_from_file_location("p0_smoke_matrix", MATRIX)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    mod = load_matrix()
    summary = mod.run_matrix(verbose=True)
    summary["gate"] = "P0-skills"
    summary["anchor"] = "YYC3-60 §二 通用规则（降级正向验收）"
    print("\n--- JSON ---")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
