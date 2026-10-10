# -*- coding: utf-8 -*-
import urllib.request
import json
import re

with open('src/data/videoData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r"'([§\d\.]+)':\s*\{\s*sectionId:\s*'[^']+',\s*topic:\s*'([^']+)',\s*channel:\s*'([^']+)',\s*title:\s*'([^']+)',\s*youtubeId:\s*'([^']+)',\s*startSeconds:\s*(\d+)", re.DOTALL)
matches = pattern.findall(text)

print(f"Kiểm tra {len(matches)} video trong videoData.ts:")
passed = []
failed = []

for sec, topic, chan, tit, ytid, start in matches:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={ytid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=4) as r:
            d = json.loads(r.read().decode('utf-8'))
            print(f"✓ [{sec}] {ytid} | {d.get('title')[:50]}")
            passed.append((sec, ytid, d.get('title')))
    except Exception as e:
        print(f"❌ [{sec}] {ytid} -> {e}")
        failed.append((sec, ytid, topic, str(e)))

print(f"\nTổng: {len(matches)} | PASS: {len(passed)} | FAIL: {len(failed)}")
if failed:
    print("\nChi tiết các video FAIL:")
    for f in failed:
        print(f, f)
