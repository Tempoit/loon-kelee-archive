#!/usr/bin/env python3
"""生成 README.md / index.json，并做结构校验"""
import json, os, re, collections, hashlib, datetime

OUT = "/var/minis/workspace/kelee-lpx"
RAW, PLG, RES = f"{OUT}/raw", f"{OUT}/plugins", f"{OUT}/resources"
REPO = "Yjwj205/loon-kelee-archive"
BASE = f"https://raw.githubusercontent.com/{REPO}/main/"

hub = json.load(open(f"{OUT}/hub.json") if os.path.exists(f"{OUT}/hub.json") else "/tmp/hub.json")
meta = {re.search(r"plugin=(.*)$", it["url"]).group(1).rsplit("/", 1)[-1]: it for it in hub["lists"]}
res_manifest = json.load(open(f"{OUT}/resources.json"))["resources"]

rows, bad, tags = [], [], collections.Counter()
for f in sorted(os.listdir(PLG)):
    txt = open(f"{PLG}/{f}", encoding="utf-8").read()
    hdr = {}
    for ln in txt.split("\n")[:20]:
        m = re.match(r"#!(\w+)=(.*)", ln)
        if m:
            hdr[m.group(1)] = m.group(2)
    if "name" not in hdr:
        bad.append((f, "缺少 #!name"))
    it = meta.get(f, {})
    sections = [m for m in re.findall(r"^\[([^\]]+)\]", txt, re.M)]
    if not sections:
        bad.append((f, "没有任何配置段"))
    script_refs = len(re.findall(r"script\(", txt))
    jq_refs = len(re.findall(r"jq_file\(", txt))
    mock_refs = len(re.findall(r"body\.mock\(", txt))
    for t in it.get("tag", []) or []:
        tags[t] += 1
    rows.append({
        "file": f,
        "name": hdr.get("name", ""),
        "desc": hdr.get("desc", "").replace("\\n", " "),
        "version": hdr.get("loon_version", ""),
        "date": hdr.get("date", ""),
        "author": hdr.get("author", ""),
        "tags": it.get("tag", []),
        "sections": sections,
        "rules": len(re.findall(r",\s*REJECT\s*$", txt, re.M)),
        "scripts": script_refs, "jq": jq_refs, "mock": mock_refs,
        "lines": txt.count("\n"), "bytes": len(txt.encode()),
        "sha256": hashlib.sha256(txt.encode()).hexdigest(),
    })

json.dump({"repo": REPO, "source": "https://hub.kelee.one",
           "archived_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
           "plugin_count": len(rows), "resource_count": len(res_manifest),
           "plugins": rows,
           "resources": res_manifest}, open(f"{OUT}/index.json", "w"), ensure_ascii=False, indent=1)

# README
by_tag = collections.defaultdict(list)
for r in rows:
    key = (r["tags"] or ["未分类"])[0]
    by_tag[key].append(r)

L = []
L.append("# 可莉 Loon 插件中心 · 全量源码归档\n")
L.append(f"**来源**：[hub.kelee.one](https://hub.kelee.one)（作者 可莉🅥）  ")
L.append(f"**归档时间**：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
L.append(f"**规模**：{len(rows)} 个插件 · {len(res_manifest)} 个远程脚本/资源\n")
L.append("""## 这是什么

把 `hub.kelee.one` 插件中心里的**全部插件原文**抓下来归档，并做了两件事：

1. **规范化重写**：去 BOM、CRLF→LF、去行尾空白、压缩多余空行、统一以换行结尾 —— 文本等于重新写了一遍，原站以后加密/混淆也不影响这里的可读源码。
2. **依赖本地化**：插件里原本指向 `https://kelee.one/Resource/...` 的 198 处脚本/JQ/mock 资源全部改写为本仓库地址，**断网到上游也能离线安装使用**。

> 只改链接和空白，规则语义零改动（已用逐行 diff 校验 275 个文件全部一致）。

## 目录结构

```
plugins/     275 个 .lpx 插件（已规范化 + 链接本地化）
resources/   102 个被插件引用的 JS / jq / zip 资源
index.json   全量索引（名称、描述、标签、段落、规则数、sha256）
tools/       抓取与重写脚本（可自行刷新）
```

## 安装方式

Loon → 配置 → 插件 → 右上角 `+` → 添加外部插件，填入：

```
https://raw.githubusercontent.com/Yjwj205/loon-kelee-archive/main/plugins/<文件名>.lpx
```

只给原始 raw 链接（不用任何镜像 CDN）。

## 插件索引
""")
for tag in sorted(by_tag, key=lambda k: -len(by_tag[k])):
    L.append(f"\n### {tag}（{len(by_tag[tag])}）\n")
    L.append("| 插件 | 说明 | 规则 | 脚本 | 文件 |")
    L.append("|---|---|---|---|---|")
    for r in sorted(by_tag[tag], key=lambda x: x["file"].lower()):
        desc = (r["desc"] or "").replace("|", "\\|")
        desc = (desc[:52] + "…") if len(desc) > 52 else desc
        L.append(f"| {r['name'] or r['file']} | {desc} | {r['rules']} | {r['scripts']+r['jq']+r['mock']} | [{r['file']}](plugins/{r['file']}) |")
L.append("\n## 统计\n")
L.append(f"- 插件总数：**{len(rows)}**")
L.append(f"- 规则总数（REJECT）：**{sum(r['rules'] for r in rows):,}**")
L.append(f"- 引用脚本的插件：**{sum(1 for r in rows if r['scripts']+r['jq']+r['mock'])}**")
L.append(f"- 归档资源：**{len(res_manifest)}** 个，{sum(v['bytes'] for v in res_manifest.values())/1048576:.1f} MB")
L.append("\n## 刷新\n\n```bash\ncd tools && python3 fetch.py && python3 fetch_res.py && python3 rewrite.py && python3 build_index.py\n```\n")
L.append("""## 说明

- 插件版权归原作者 **可莉🅥**（[luestr/ProxyResource](https://github.com/luestr/ProxyResource)）所有，本仓库仅为个人备份/学习用途，未做商业化。
- 若原作者认为不妥，提 issue 或联系本人，会立即删除。
- 上游若更新规则，本仓库不会自动同步；需要时跑 `tools/` 下的脚本重新抓。
""")
open(f"{OUT}/README.md", "w", encoding="utf-8").write("\n".join(L))

print("插件:", len(rows), "资源:", len(res_manifest), "结构异常:", len(bad), bad[:5])
print("标签:", tags.most_common(8))
print("规则总数:", sum(r["rules"] for r in rows))
