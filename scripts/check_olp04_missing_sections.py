# -*- coding: utf-8 -*-
import json
import re

with open("src/data/exams/olp-04.json", "r", encoding="utf-8") as f:
    data = json.load(f)

missing = []
for q in data["questions"]:
    exp = q.get("explanation", "")
    if not re.search(r'§\s*\d+\.\d+', exp):
        missing.append((q["id"], q.get("prompt")[:70], q.get("tags", [])))

print(f"Số câu ở olp-04.json chưa có §: {len(missing)}")
for qid, p, tags in missing[:15]:
    print(f"[{qid}] tags={tags} | {p}...")
