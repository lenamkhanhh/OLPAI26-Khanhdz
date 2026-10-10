# -*- coding: utf-8 -*-
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

for name in ['olp-02.json', 'olp-03.json']:
    print(f"\n==================== {name} ====================")
    with open(f'src/data/exams/{name}', 'r', encoding='utf-8') as f:
        d = json.load(f)
    for idx, q in enumerate(d['questions'], 1):
        print(f"[{idx:02d}] {q['id']} ({q['module']}): {q['prompt'][:70]}... | Ans: {q.get('answer', 'N/A')}")
