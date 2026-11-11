#!/usr/bin/env python3
"""把 raw/ 里的插件规范化重写 + 把 kelee.one 远程脚本地址改写为本仓库 raw 地址。

规范化（不改语义）：
  - 去 UTF-8 BOM
  - CRLF / CR 统一为 LF
  - 去行尾空白
  - 连续 3 行以上空行压成 1 行
  - 确保文件以单个换行结尾
改写：
  - https://kelee.one/Resource/...  ->  https://raw.githubusercontent.com/<REPO>/main/resources/Resource/...
"""
import json, os, re, sys

REPO = "Yjwj205/loon-kelee-archive"
BRANCH = "main"
BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"
OUT = "/var/minis/workspace/kelee-lpx"
SRC = os.path.join(OUT, "raw")
DST = os.path.join(OUT, "plugins")

RES_MAP = json.load(open(os.path.join(OUT, "resources.json")))["resources"]
# 以已归档的资源为白名单，避免把 404 的地址也改掉（保持原样，便于追溯上游缺失）
RES_BY_URL = {u.rstrip("\\"): v["path"] for u, v in RES_MAP.items()}


def normalize(text: str) -> str:
    text = text.lstrip("\ufeff")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip(" \t") for ln in text.split("\n")]
    out, blank = [], 0
    for ln in lines:
        if ln == "":
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    while out and out[0] == "":
        out.pop(0)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def rewrite(text: str):
    hits = [0]

    def sub(m):
        path = RES_BY_URL.get(m.group(0))
        if not path:
            return m.group(0)
        hits[0] += 1
        return BASE + path

    # 反斜杠不进入匹配，避免破坏 mock body 里的 \" 转义
    text = re.sub(r"https://kelee\.one/Resource/[^\s\",)\\]*", sub, text)
    return text, hits[0]


os.makedirs(DST, exist_ok=True)
rows, total_hits = [], 0
for f in sorted(os.listdir(SRC)):
    raw = open(os.path.join(SRC, f), encoding="utf-8", errors="replace").read()
    txt, hits = rewrite(normalize(raw))
    open(os.path.join(DST, f), "w", encoding="utf-8", newline="\n").write(txt)
    total_hits += hits
    rows.append({"file": f, "lines": txt.count("\n"), "bytes": len(txt.encode()),
                 "rewritten": hits})
print(f"插件 {len(rows)} 个，改写脚本链接 {total_hits} 处")
print(f"仍指向 kelee.one 的行：")
left = 0
for f in os.listdir(DST):
    t = open(os.path.join(DST, f), encoding="utf-8").read()
    for ln in t.split("\n"):
        if "kelee.one/Resource" in ln:
            left += 1
print("  残留", left)
json.dump(rows, open(os.path.join(OUT, "plugins_stats.json"), "w"), ensure_ascii=False, indent=1)
