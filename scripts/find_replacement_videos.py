# -*- coding: utf-8 -*-
"""
Script tìm kiếm và kiểm tra các video YouTube còn sống 100% để thay thế 7 video lỗi.
"""

import urllib.request
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Đọc danh sách video trong src/data/videoData.ts để xem trước đây hệ thống dùng ID nào
with open('src/data/videoData.ts', 'r', encoding='utf-8') as f:
    ts_content = f.read()

import re
ts_matches = re.findall(r"'?(§[\d\.]+)'?:\s*\{\s*sectionId:\s*'[^']+',\s*topic:\s*'([^']+)',\s*channel:\s*'([^']+)',\s*title:\s*'([^']+)',\s*youtubeId:\s*'([^']+)',\s*startSeconds:\s*(\d+)", ts_content)

print(f"Tổng số video trong videoData.ts: {len(ts_matches)}")

tested_ids = {}
for sec, topic, chan, title, ytid, start_sec in ts_matches:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={ytid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    alive = False
    real_title = ""
    try:
        with urllib.request.urlopen(req, timeout=4) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode('utf-8'))
                alive = True
                real_title = data.get('title', '')
    except Exception:
        pass
    tested_ids[sec] = {
        "ytid": ytid,
        "alive": alive,
        "title": title,
        "real_title": real_title,
        "start": start_sec,
        "channel": chan
    }
    status = "OK" if alive else "DEAD"
    print(f"[{status:4s}] {sec}: {ytid} -> {real_title or title}")

with open('videoData_audit.json', 'w', encoding='utf-8') as f:
    json.dump(tested_ids, f, ensure_ascii=False, indent=2)
