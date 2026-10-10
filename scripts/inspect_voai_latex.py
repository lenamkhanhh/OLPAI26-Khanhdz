# -*- coding: utf-8 -*-
import json
import re

with open('src/data/exams/voai-2025.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('Total questions:', len(d['questions']))
has_dollar = [q['id'] for q in d['questions'] if '$' in q['prompt'] or any('$' in o['text'] for o in q['options']) or '$' in q['explanation']]
print('Questions with dollar sign ($):', len(has_dollar))
print('List with dollar:', has_dollar)

# Check questions that have math characters or formulas like =, +, -, /, x, ^, IoU, alpha, beta, etc.
math_candidates = []
for q in d['questions']:
    full = q['prompt'] + " " + " ".join(o['text'] for o in q['options']) + " " + q['explanation']
    if any(k in full for k in ['\\', 'IoU', '×', '>=', '<=', '->', '∑', '∫', 'σ', 'μ', 'λ', 'θ', 'W^T', 'x_i', 'y_i', 'log', 'exp', 'W_1', 'B_1', 'B1', 'B2', 'B3']):
        math_candidates.append(q['id'])

print('Math candidates without proper LaTeX:', len(math_candidates))
print('Sample math candidates:', math_candidates[:15])
