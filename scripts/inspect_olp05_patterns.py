# -*- coding: utf-8 -*-
import json
import re

with open('src/data/exams/olp-05.json', 'r', encoding='utf-8') as f:
    e5 = json.load(f)

with open('tmp/audit_full_2026-10-09/olp05_source_compare.json', 'r', encoding='utf-8') as f:
    s_comp = json.load(f)

contradictions = {item['id']: item for item in s_comp['contradictions']}

patterns = []
for q in e5['questions']:
    qid = q['id']
    exp = q['explanation']
    ans = q['answer']
    # Find all occurrences of letters A, B, C, D in backticks or quotes or "phương án X" or "Chọn X"
    matches = re.findall(r'(?:phương án|chọn|đáp án|đáp án đúng|phương án đúng)\s*[:\*`]*\s*([ABCD])\b', exp, re.IGNORECASE)
    patterns.append((qid, ans, matches, contradictions.get(qid)))

print(f"Total questions: {len(patterns)}")
print("Sample matches:")
for p in patterns[:15]:
    print(p[0], f"ans={p[1]}", f"found={p[2]}", f"in_contra={p[3] is not None}")
