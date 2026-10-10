# -*- coding: utf-8 -*-
import json
import re
import glob

theory = open('content/01-ly-thuyet-olp-ai.md', encoding='utf-8').read()
valid_secs = set(re.findall(r'§[\d\.]+', theory))
print(f"Valid sections in theory ({len(valid_secs)}): {sorted(valid_secs)}")

invalid_refs = []
for f in sorted(glob.glob('src/data/exams/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for q in d.get('questions', []):
        exp = q.get('explanation', '') + ' ' + q.get('modelAnswer', '')
        secs = re.findall(r'§[\d\.]+', exp)
        for s in secs:
            if s not in valid_secs:
                invalid_refs.append((f, q['id'], s))

print(f"Total invalid refs: {len(invalid_refs)}")
for r in invalid_refs:
    print(r)

import sys
if len(invalid_refs) > 0:
    print(f"FAILED: Found {len(invalid_refs)} invalid section references!")
    sys.exit(1)
else:
    print("ALL SECTION REFS VALID (EXIT: 0)")
    sys.exit(0)
