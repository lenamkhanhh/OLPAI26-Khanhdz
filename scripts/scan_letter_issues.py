# -*- coding: utf-8 -*-
import json
import re

exams = ['olp-01.json', 'olp-02.json', 'olp-03.json']

for fname in exams:
    path = f'src/data/exams/{fname}'
    data = json.load(open(path, encoding='utf-8'))
    print(f'=== Checking {fname} ({len(data["questions"])} questions) ===')
    for q in data['questions']:
        if q.get('type') != 'mcq':
            continue
        qid = q['id']
        ans = q.get('answer', '')
        exp = q.get('explanation', '')
        opts = {opt['key']: opt['text'] for opt in q.get('options', [])}
        
        # 1. Check if explanation says "Đáp án chính xác là [X]" where X != ans
        m_ans = re.findall(r'Đáp án chính xác là\s*\**([A-D])\**', exp)
        for m in m_ans:
            if m != ans:
                print(f'  [ERROR ANSWER KEY MISMATCH] {qid}: ans={ans}, but exp says: Đáp án chính xác là {m}')

        # 2. Check if explanation has trap referring to options
        lines = exp.split('\n')
        for line in lines:
            if 'bẫy' in line.lower() or 'pitfall' in line.lower() or 'phương án' in line.lower():
                # Check if it mentions "Chọn X" where X == ans
                for let in ['A', 'B', 'C', 'D']:
                    if f'chọn {let.lower()}' in line.lower() and let == ans:
                        print(f'  [ERROR TRAP CONFUSION] {qid}: ans={ans}, but trap mentions: \"{line.strip()}\"')
                    if f'chọn {let}' in line and let == ans:
                        print(f'  [ERROR TRAP CONFUSION] {qid}: ans={ans}, but trap mentions: \"{line.strip()}\"')

        # 3. Check if options contain "Cả A và B", "Cả A và C", "Tất cả các phương án trên"
        for k, text in opts.items():
            if re.search(r'\b[A-D]\s+và\s+[A-D]\b', text):
                print(f'  [WARNING RELATIVE OPTION] {qid} opt {k}: \"{text}\"')
            if 'tất cả' in text.lower() and k != 'D':
                print(f'  [WARNING ALL OF ABOVE NOT D] {qid} opt {k}: \"{text}\"')
