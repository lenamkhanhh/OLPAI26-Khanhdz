# -*- coding: utf-8 -*-
import json

with open('tmp/audit_full_2026-10-09/olp05_source_compare.json', 'r', encoding='utf-8') as f:
    s_comp = json.load(f)

with open('src/data/exams/olp-05.json', 'r', encoding='utf-8') as f:
    e5 = json.load(f)

mapping = {item['id']: item for item in s_comp['optionMapping']}
contradictions = {item['id']: item for item in s_comp['contradictions']}

print(f"Total mapped: {len(mapping)}, Total contradictions: {len(contradictions)}")

# Check first 5 contradictions
for q in e5['questions'][:10]:
    qid = q['id']
    if qid in contradictions:
        print(f"\n{qid}: answer={q['answer']}, explanationKeys={contradictions[qid]['explanationKeys']}")
        print(f"SourceKey={mapping[qid]['sourceKey']}, jsonKey={mapping[qid]['jsonKey']}")
        print("Last 200 chars of explanation:")
        print(q['explanation'][-250:])
