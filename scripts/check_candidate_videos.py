# -*- coding: utf-8 -*-
import urllib.request
import json

candidates = [
    ("§2.2", "68BZ5fQtRL8", "StatQuest Activation Functions"),
    ("§4.3", "e9U0QafnwWQ", "StatQuest Cosine Similarity"),
    ("§5.6", "ROpbdO-gRUo", "Khan Academy Correlation vs Causation"),
    ("§7.3", "m9fH9OWn820", "YOLOv8 Guide Ultralytics"),
    ("§3.7", "aqx1rPfqHl8", "Semantic vs Instance Segmentation"),
    ("§3.7_alt", "d14QxUdX4TU", "Image Segmentation Overview"),
    ("§3.7_alt2", "ARNGV6aTjO8", "Computerphile Segmentation"),
    ("§3.7_alt3", "Fz3r3N_g960", "Segmentation architectures"),
]

for sec, ytid, desc in candidates:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={ytid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"✓ {sec:10s} | {ytid:11s} | {data.get('title')[:60]}")
    except Exception as e:
        print(f"❌ {sec:10s} | {ytid:11s} | {desc} -> {e}")
