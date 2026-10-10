# -*- coding: utf-8 -*-
"""
Script kiểm tra tính khả dụng của toàn bộ video YouTube trong hệ thống:
Sử dụng oEmbed API của YouTube để xác minh từng ID.
"""

import urllib.request
import urllib.error
import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('docs/generate_full_hub.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Trích xuất toàn bộ cấu hình video trong videos_map
vid_pattern = re.compile(r'\"(§[\d\.]+)\":\s*\{\s*\"sectionId\":\s*\"[^\"]+\",\s*\"title\":\s*\"([^\"]+)\",\s*\"channel\":\s*\"([^\"]+)\",\s*\"youtubeId\":\s*\"([^\"]+)\",\s*\"startSeconds\":\s*(\d+)', re.DOTALL)
matches = vid_pattern.findall(text)

print(f"Tổng số video tìm thấy trong generate_full_hub.py: {len(matches)}\n")

results = []
for sec_id, title, channel, ytid, start_sec in matches:
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={ytid}&format=json"
    status = "OK"
    error_msg = ""
    req = urllib.request.Request(
        oembed_url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                status = "OK"
    except urllib.error.HTTPError as e:
        status = f"ERROR_{e.code}"
        error_msg = str(e)
    except Exception as e:
        status = "EXCEPTION"
        error_msg = str(e)
    
    print(f"[{status:10s}] {sec_id}: ID={ytid} | {title[:40]}... (Kênh: {channel})")
    if status != "OK":
        print(f"            -> LỖI: {error_msg}")
    
    results.append({
        "sectionId": sec_id,
        "title": title,
        "channel": channel,
        "youtubeId": ytid,
        "startSeconds": int(start_sec),
        "status": status,
        "error": error_msg
    })

failed = [r for r in results if r["status"] != "OK"]
print(f"\n==========================================")
print(f"Tổng số video: {len(results)} | Hợp lệ: {len(results) - len(failed)} | LỖI: {len(failed)}")
print(f"==========================================")
for f in failed:
    print(f"  ❌ {f['sectionId']}: {f['youtubeId']} -> {f['status']} ({f['title']})")

with open('video_audit_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
