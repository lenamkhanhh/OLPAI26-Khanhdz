# -*- coding: utf-8 -*-
import re
import glob
import json
import urllib.request
import urllib.error
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('docs/generate_full_hub.py', 'r', encoding='utf-8') as f:
    hub_content = f.read()

# Extract sections in videos_map in generate_full_hub.py
hub_vid_pattern = re.compile(r'\"(§[\d\.]+)\":\s*\{\s*\"sectionId\":\s*\"[^\"]+\",\s*\"title\":\s*\"([^\"]+)\",\s*\"channel\":\s*\"([^\"]+)\",\s*\"youtubeId\":\s*\"([^\"]+)\",\s*\"startSeconds\":\s*(\d+)', re.DOTALL)
hub_videos = {m[0]: {"title": m[1], "channel": m[2], "youtubeId": m[3], "startSeconds": int(m[4])} for m in hub_vid_pattern.findall(hub_content)}

print(f"Videos defined in generate_full_hub.py: {len(hub_videos)}")

# Extract all sections referenced in questions
q_sections = set(re.findall(r'§\d+\.\d+', hub_content))
print(f"Unique sections referenced in generate_full_hub.py questions/content: {len(q_sections)}")
print(f"Sections referenced: {sorted(list(q_sections))}")

# Check which referenced sections are missing in hub_videos
missing_in_hub = [s for s in q_sections if s not in hub_videos]
print(f"Referenced sections missing in hub_videos: {missing_in_hub}")
