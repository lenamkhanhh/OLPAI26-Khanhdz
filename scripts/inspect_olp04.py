# -*- coding: utf-8 -*-
import json
import re

with open('src/data/exams/olp-04.json', 'r', encoding='utf-8') as f:
    e4 = json.load(f)

for q in e4['questions']:
    if q['type'] == 'mcq':
        exp = q['explanation']
        keys_found = re.findall(r'(?:Chọn|đáp án|phương án|Bẫy)\s+([ABCD])', exp, re.IGNORECASE)
        print(f"{q['id']}: answer={q['answer']}, found in exp: {keys_found}")
