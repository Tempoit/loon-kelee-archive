#!/usr/bin/env python3
"""在归档插件上应用本地定制（不污染 plugins/ 纯净归档）→ custom/

patches.json 结构：
{
  "Block_HTTPDNS.lpx": {
     "note": "放行微信 HTTPDNS",
     "remove": ["DOMAIN, dns.weixin.qq.com, REJECT", ...]
  }
}
"""
import json, os

OUT = "/var/minis/workspace/kelee-lpx"
SRC = f"{OUT}/plugins"
DST = f"{OUT}/custom"
PATCHES = f"{OUT}/patches.json"

os.makedirs(DST, exist_ok=True)
spec = json.load(open(PATCHES, encoding="utf-8"))
report = []

for fname, ops in spec.items():
    src = os.path.join(SRC, fname)
    if not os.path.exists(src):
        report.append((fname, "源文件不存在")); continue
    lines = open(src, encoding="utf-8").read().split("\n")
    removed, missing = [], []
    for rule in ops.get("remove", []):
        hit = [i for i, ln in enumerate(lines) if ln.strip() == rule]
        if not hit:
            missing.append(rule); continue
        for i in reversed(hit):
            lines.pop(i)
        removed.append(rule)
    out = "\n".join(lines)
    os.makedirs(os.path.dirname(os.path.join(DST, fname)) or DST, exist_ok=True)
    open(os.path.join(DST, fname), "w", encoding="utf-8", newline="\n").write(out)
    report.append((fname, f"删除 {len(removed)} 条，缺失 {len(missing)} 条 {missing}"))

for r in report:
    print(*r)
