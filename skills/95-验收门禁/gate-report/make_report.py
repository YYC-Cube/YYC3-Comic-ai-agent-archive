# ==============================================================
# gate-report：门禁报告生成器（YYC3-60 §六 留证模板对齐 · 技能 95-验收门禁/gate-report）
# 输入：gate-runner 的 JSON（stdin 或 --results 文件）；输出：Markdown 报告到 stdout
# 运行：python3 run_gates.py | python3 make_report.py
# ==============================================================
import json
import sys
from datetime import datetime

MARK = {"PASS": "PASS ", "STUB": "STUB ", "FAIL": "FAIL "}


def render(summary: dict) -> str:
    lines = [
        f"# 技能门禁报告（{summary.get('gate', 'P0-skills')}）",
        "",
        f"- 执行时间：{datetime.now().isoformat(timespec='seconds')}",
        f"- 验收基线：{summary.get('anchor', 'YYC3-60 §二 通用规则（降级正向验收）')}",
        f"- 汇总：PASS {summary['pass']} / STUB {summary['stub']} / FAIL {summary['fail']}"
        f"（共 {summary['total']}）",
        "",
        "| 用例（域/技能） | 结果 | 证据摘要 |",
        "| ---- | ---- | ---- |",
    ]
    stubs = []
    for r in summary["results"]:
        lines.append(f"| {r['domain']}/{r['skill']} | {MARK[r['status']]} | {r['detail']} |")
        if r["status"] == "STUB":
            stubs.append(f"{r['domain']}/{r['skill']}")
    lines += ["", "## STUB 登记清单（转 M 任务跟踪）", ""]
    lines += [f"- {s}" for s in stubs] if stubs else ["- （无）"]
    lines += ["", "## 结论", ""]
    if summary["fail"] > 0:
        lines.append(f"- ❌ 存在 {summary['fail']} 项 FAIL：按 YYC3-60 §二 开缺陷单（BUG-G?-??），"
                     "FAIL 未清零前不得进入对应 TC-G 用例执行。")
    else:
        lines.append("- ✅ 无 FAIL；STUB 项已登记 M 任务，降级模式技能面就绪。")
    return "\n".join(lines) + "\n"


def main():
    raw = sys.stdin.read() if not sys.stdin.isatty() else ""
    if "--results" in sys.argv:
        p = Path(sys.argv[sys.argv.index("--results") + 1])
        raw = p.read_text(encoding="utf-8")
    if not raw.strip():
        print("用法：run_gates.py | python3 make_report.py  或  make_report.py --results results.json",
              file=sys.stderr)
        return 2
    start = raw.find("{")
    summary = json.loads(raw[start:]) if start >= 0 else json.loads(raw)
    print(render(summary))
    return 0 if summary["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
