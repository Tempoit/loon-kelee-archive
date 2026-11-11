#!/usr/bin/env python3
"""抓取所有插件引用的 kelee.one 远程资源（js/json/proto/图片等）"""
import json, os, re, time, urllib.request, hashlib

UA = "Loon/338 CFNetwork/1498.700.2 Darwin/23.6.0"
OUT = "/var/minis/workspace/kelee-lpx"
RAW = os.path.join(OUT, "raw")
RES = os.path.join(OUT, "resources")
os.makedirs(RES, exist_ok=True)

def get(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except Exception as e:
            last = e; time.sleep(1.5 * (i + 1))
    raise last

urls = set()
for f in os.listdir(RAW):
    txt = open(os.path.join(RAW, f), encoding="utf-8", errors="replace").read()
    for u in re.findall(r"https://kelee\.one/[^\s\",)]+", txt):
        urls.add(u.rstrip(";"))

manifest, fail = {}, []
for i, u in enumerate(sorted(urls), 1):
    rel = u.split("kelee.one/", 1)[1]
    # 去掉 illegal chars，保留目录结构
    rel = re.sub(r"[^\w./-]", "_", rel.replace("../", ""))
    dst = os.path.join(RES, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    try:
        data, ctype = get(u)
    except Exception as e:
        fail.append((u, str(e))); print("FAIL", u, e, flush=True); continue
    open(dst, "wb").write(data)
    manifest[u] = {"path": "resources/" + rel, "bytes": len(data), "type": ctype,
                   "sha256": hashlib.sha256(data).hexdigest()}
    print(f"{i:3d} {len(data):8d} {rel}", flush=True)

json.dump({"resources": manifest, "fail": fail}, open(os.path.join(OUT, "resources.json"), "w"),
          ensure_ascii=False, indent=1)
print("OK", len(manifest), "FAIL", len(fail))
