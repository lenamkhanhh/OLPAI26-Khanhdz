# -*- coding: utf-8 -*-
import json
import os
import glob
import re

ROOT = os.path.join("src", "data", "exams")
exams = sorted(glob.glob(os.path.join(ROOT, "*.json")))

print("=== KIỂM TRA TRƯỜNG THAM CHIẾU LÝ THUYẾT / VIDEO TRONG 6 ĐỀ ===")
for fpath in exams:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    qs = data.get("questions", [])
    has_sec = sum(1 for q in qs if re.search(r'§\s*\d+\.\d+', q.get("explanation", "")))
    has_tag = sum(1 for q in qs if q.get("tags"))
    print(f"{os.path.basename(fpath)}: {len(qs)} câu | {has_sec} câu có §x.y trong explanation | {has_tag} câu có tags")

print("\n=== KIỂM TRA FILE src/data/videoData.ts ===")
with open(os.path.join("src", "data", "videoData.ts"), "r", encoding="utf-8") as f:
    vts = f.read()

entries = re.findall(r"'([§\w\.\-]+)':\s*\{([^}]+youtubeId:[^}]+)\}", vts)
print(f"Tổng số mục trong videoData.ts: {len(entries)}")
yt_map = {}
for sec_id, body in entries:
    yt_m = re.search(r"youtubeId:\s*'([^']+)'", body)
    title_m = re.search(r"title:\s*'([^']+)'", body)
    topic_m = re.search(r"topic:\s*'([^']+)'", body)
    yt = yt_m.group(1) if yt_m else ""
    title = title_m.group(1) if title_m else ""
    topic = topic_m.group(1) if topic_m else ""
    if yt not in yt_map:
        yt_map[yt] = []
    yt_map[yt].append((sec_id, topic, title))

print(f"Số lượng YouTube ID duy nhất: {len(yt_map)}")
for yt, lst in yt_map.items():
    if len(lst) > 1:
        print(f"TRÙNG YOUTUBE ID ({yt}):")
        for s, top, tit in lst:
            print(f"   - {s}: {top} ({tit})")
