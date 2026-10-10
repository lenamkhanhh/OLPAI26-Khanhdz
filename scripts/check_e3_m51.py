# -*- coding: utf-8 -*-
import json
import re

with open('src/data/exams/olp-03.json', 'r', encoding='utf-8') as f:
    e3 = json.load(f)

for idx, q in enumerate(e3['questions'][50:100], start=51):
    exp = q['explanation']
    # check if letter is mentioned in markdown bold or backticks
    m = re.findall(r'(?:phương án|đáp án|chọn)\s*[*`]*([ABCD])[*`]*\b', exp, re.I)
    if m:
        print(f"Q{idx} ({q['id']}): {m}")
print("Done checking M51-M100 in olp-03.")
