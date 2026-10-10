# -*- coding: utf-8 -*-
"""
Script phân tích và trích xuất dữ liệu khóa học OLP Sinh Viên & VOAI Nâng Cao
để tích hợp vào Study Hub và tài liệu học tập.
"""

import json
import os

OLP_PATH = r"C:\Users\HP\Downloads\OLP_Sinh_Vien_data.json"
VOAI_PATH = r"C:\Users\HP\Downloads\VOAI_Nang_Cao_full_data (1).json"
OUT_PATH = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26\src\data\courses_data.json"

with open(OLP_PATH, "r", encoding="utf-8") as f:
    olp_data = json.load(f)

with open(VOAI_PATH, "r", encoding="utf-8") as f:
    voai_data = json.load(f)

# Xây dựng danh mục các buổi học hợp nhất chuẩn
# Gồm tiêu đề, chủ đề, ngày học, link video iframe (BunnyCDN), slide Drive, transcript, notebook lab
merged_lessons = []

# 1. Khóa OLP Sinh Viên Chuyên Sâu 2026 (17 Buổi)
for l in olp_data.get("lessons", []):
    title = l.get("title", "").strip()
    if not title or title.lower() == "sidebar":
        continue
    
    idx = l.get("index")
    date = l.get("date", "")
    res = l.get("resources", {}) or {}
    vids = l.get("videoSources", {}) or {}
    
    slide = res.get("slide")
    lab = res.get("lab")
    transcript = res.get("transcript")
    
    iframes = vids.get("iframes", [])
    video_url = iframes[0] if iframes else None
    
    merged_lessons.append({
        "course": "OLP Sinh Viên 2026",
        "index": idx,
        "title": title,
        "date": date,
        "slide": slide,
        "lab": lab,
        "transcript": transcript,
        "videoIframe": video_url
    })

# 2. Khóa VOAI Nâng Cao (13 Buổi bài giảng có video)
voai_lessons = []
for l in voai_data.get("lessons", []):
    title = l.get("title", "").strip()
    if not title or title.lower() == "sidebar":
        continue
    v = l.get("videoIframe")
    s = l.get("slide")
    nb = l.get("notebook")
    if v or s or nb:
        voai_lessons.append({
            "course": "VOAI Nâng Cao",
            "title": title,
            "slide": s,
            "notebook": nb,
            "videoIframe": v
        })

print(f"OLP Sinh Viên valid lessons: {len(merged_lessons)}")
print(f"VOAI Nâng Cao valid lessons: {len(voai_lessons)}")

out_payload = {
    "olp_course": {
        "title": "Olympic AI Sinh Viên Chuyên Sâu 2026 (17 Buổi)",
        "lessons": merged_lessons
    },
    "voai_course": {
        "title": "Chuyên Đề VOAI Nâng Cao & Giải Đề",
        "lessons": voai_lessons
    }
}

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(out_payload, f, ensure_ascii=False, indent=2)

print(f"Saved merged course data to: {OUT_PATH}")
