# -*- coding: utf-8 -*-
import json
import re

with open('src/data/exams/olp-05.json', 'r', encoding='utf-8') as f:
    e5 = json.load(f)

with open('tmp/audit_full_2026-10-09/olp05_source_compare.json', 'r', encoding='utf-8') as f:
    s_comp = json.load(f)

contradictions = {item['id']: item for item in s_comp['contradictions']}

cv_matches = 0
cv_unmatched = []

for q in e5['questions'][35:]: # CV questions
    exp = q['explanation']
    m = re.search(r'Phương án `([ABCD])` khớp', exp)
    if m:
        cv_matches += 1
    else:
        cv_unmatched.append((q['id'], [line for line in exp.split('\n') if 'phương án' in line.lower()]))

print(f"CV questions matched with 'Phương án `[ABCD]` khớp': {cv_matches} / 55")
if cv_unmatched:
    print("Unmatched CV:", cv_unmatched)
