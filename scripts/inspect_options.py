# -*- coding: utf-8 -*-
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

for fname in ['olp-01.json', 'olp-02.json', 'olp-03.json']:
    path = 'src/data/exams/' + fname
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    print(f"\n==================== {fname} ====================")
    print("title:", d.get('title'))
    print("durationMinutes:", d.get('durationMinutes'))
    print("totalPoints:", d.get('totalPoints'))
    print("disclaimer:", d.get('disclaimer')[:60] + "...")
    print("moduleLabels:", d.get('moduleLabels'))
    
    types = {}
    modules = {}
    ans_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    graded_pts = 0
    essay_pts = 0
    html_found = 0
    rubric_ok = 0
    
    for q in d['questions']:
        t = q['type']
        types[t] = types.get(t, 0) + 1
        m = q['module']
        modules[m] = modules.get(m, 0) + 1
        
        if t == 'mcq':
            graded_pts += q['points']
            ans_dist[q['answer']] += 1
            if '<div' in q['explanation'] or '<span' in q['explanation']:
                html_found += 1
        elif t == 'code':
            graded_pts += q['points']
            if len(q.get('rubric', [])) >= 3 and len(q.get('modelAnswer', '')) > 20:
                rubric_ok += 1
        elif t == 'essay':
            essay_pts += q['points']
            if len(q.get('rubric', [])) >= 3 and len(q.get('modelAnswer', '')) > 20:
                rubric_ok += 1
                
    print("question types:", types)
    print("question modules:", modules)
    print("answer distribution:", ans_dist)
    print(f"graded points: {graded_pts}, essay points: {essay_pts}")
    print(f"html tags in explanations: {html_found}")
    print(f"open questions with valid rubric & modelAnswer: {rubric_ok}")
