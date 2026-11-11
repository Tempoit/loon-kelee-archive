#!/usr/bin/env python3
"""抓取 hub.kelee.one 全部插件原文（Loon UA 过 CF WAF），落盘到 raw/"""
import json, os, re, urllib.request, urllib.parse, time, sys

UA = "Loon/338 CFNetwork/1498.700.2 Darwin/23.6.0"
OUT = "/var/minis/workspace/kelee-lpx"
RAW = os.path.join(OUT, "raw")

def get(url, ua=UA, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

meta = json.loads(get("https://hub.kelee.one/list.json", ua="Mozilla/5.0").decode())
os.makedirs(RAW, exist_ok=True)
items, ok, fail = [], 0, []
for idx, it in enumerate(meta["lists"]):
    m = re.search(r"plugin=(https?://[^\s&]+)", it["url"])
    if not m:
        fail.append((it["name"], "no url")); continue
    url = m.group(1)
    name = url.rsplit("/", 1)[-1]
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", urllib.parse.unquote(name))
    try:
        data = get(url)
    except Exception as e:
        fail.append((name, str(e))); continue
    open(os.path.join(RAW, slug), "wb").write(data)
    ok += 1
    items.append({"idx": idx, "name": it["name"], "desc": it["desc"], "tag": it["tag"],
                  "icon": it["icon"], "date": it["date"], "author": it["author"],
                  "source": url, "file": slug, "bytes": len(data)})
    print(f"{ok:3d} {len(data):7d} {slug}", flush=True)

json.dump({"items": items, "fail": fail}, open(os.path.join(OUT, "index.json"), "w"),
          ensure_ascii=False, indent=1)
print("OK", ok, "FAIL", len(fail))
for f in fail: print("  FAIL", f)
