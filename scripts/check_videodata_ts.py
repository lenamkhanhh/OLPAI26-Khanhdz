# -*- coding: utf-8 -*-
import re
import urllib.request
import urllib.error
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/videoData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Match entries like '§2.8': { ... youtubeId: 'tNIpEZLv_l8' ... }
entries = re.findall(r"'([§\d\.]+)':\s*\{[^}]+?youtubeId:\s*'([^']+)'", text)
print(f"Total video entries found in videoData.ts: {len(entries)}")

failed = []
for sec, ytid in entries:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={ytid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=4) as resp:
            pass
        print(f"✓ {sec}: {ytid}")
    except Exception as e:
        print(f"❌ {sec}: {ytid} -> {e}")
        failed.append((sec, ytid, str(e)))

print(f"\nTotal: {len(entries)} | Failed: {len(failed)}")
