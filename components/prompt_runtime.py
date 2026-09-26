# ==============================================================
# YYC³ AI FAmily Prompt 装载运行时 v1.0（M2 收尾 · TC-G2-008）
# 职责：agents/<slug>/prompt.md → system_prompt 装载 + Agent 实例构建
# 结构：frontmatter（agent/slug/roles）+「一、基础 system_prompt」
#       +「二、漫剧场景定制段」（```text 围栏，按序拼接）
# 对齐：YYC3-03 §四 第二步（prompt 定制）；TC-G2-008 复验前置
# 依赖：仅标准库 + components 同包扁平 import
# ==============================================================
import re
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parents[1] / "agents"

_SLUG_CLASS = {
    # slug: (模块名, 类名)——模块名为蛇形文件名，不能由类名小写推导
    "yuanqi-tianshu": ("yuanqi_tianshu_agent", "YuanQiTianShuAgent"),
    "zhiyun-shouhu": ("zhiyun_shouhu_agent", "ZhiYunShouHuAgent"),
    "gewu-zongshi": ("gewu_zongshi_agent", "GeWuZongShiAgent"),
    "chuangxiang-lingyun": ("chuangxiang_lingyun_agent", "ChuangXiangLingYunAgent"),
    "yanqi-qianhang": ("yanqi_qianhang_agent", "YanQiQianHangAgent"),
    "yushu-wanwu": ("yushu_wanwu_agent", "YuShuWanWuAgent"),
    "yujian-xianzhi": ("yujian_xianzhi_agent", "YuJianXianZhiAgent"),
    "zhiyu-bole": ("zhiyu_bole_agent", "ZhiYuBoLeAgent"),
}


class PromptRuntime:
    """prompt.md 装载器：frontmatter + 基础段 + 漫剧定制段 → system_prompt"""

    def __init__(self, agents_dir: Path = None):
        self.agents_dir = Path(agents_dir) if agents_dir else AGENTS_DIR

    def load(self, slug: str) -> dict:
        """装载单个 Agent 的 prompt.md。

        :return: {"slug", "frontmatter", "system_prompt"(基础+定制拼接),
                  "contract"(【输出契约】段落文本，无则空串), "source"}
        """
        path = self.agents_dir / slug / "prompt.md"
        if not path.exists():
            raise FileNotFoundError(f"prompt.md 不存在：{path}")
        text = path.read_text(encoding="utf-8")

        fm = {}
        fm_match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if fm_match:
            for line in fm_match.group(1).splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip()

        # ```text 围栏块：第一个为基础 system_prompt，其后为漫剧定制段
        blocks = re.findall(r"```text\n(.*?)```", text, re.DOTALL)
        system_prompt = "\n\n".join(b.strip() for b in blocks)

        contract = ""
        cm = re.search(r"【输出契约】(.*?)(?:\n```|\n## |\Z)", text, re.DOTALL)
        if cm:
            contract = cm.group(1).strip()

        if not system_prompt:
            raise ValueError(f"{slug}: prompt.md 未提取到 ```text 系统提示词段")
        return {"slug": slug, "frontmatter": fm, "system_prompt": system_prompt,
                "contract": contract, "source": str(path)}

    def load_all(self) -> dict:
        """装载全部 8 个 Agent（缺一即 KeyError 由调用方处理）"""
        return {slug: self.load(slug) for slug in _SLUG_CLASS}

    def build_agent(self, slug: str):
        """构建注入 prompt.md 系统提示词的 Agent 实例（prompt 运行时核心）"""
        loaded = self.load(slug)
        module_name, class_name = _SLUG_CLASS[slug]
        import importlib
        mod = importlib.import_module(module_name)
        agent = getattr(mod, class_name)()
        # 装载运行时语义：prompt.md（基础+漫剧定制）覆盖代码内默认提示词
        agent.system_prompt = loaded["system_prompt"]
        agent.prompt_source = loaded["source"]
        return agent


__all__ = ["PromptRuntime", "AGENTS_DIR"]
