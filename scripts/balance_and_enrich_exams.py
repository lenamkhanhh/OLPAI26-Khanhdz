# -*- coding: utf-8 -*-
"""
Script cân bằng phân bố đáp án và chuẩn hóa metadata cho olp-03.json và olp-05.json:
- Đảm bảo mỗi đáp án A, B, C, D chiếm khoảng 20-30% (thỏa mãn min 8%, max 45%).
- Đảm bảo đầy đủ metadata: durationMinutes, disclaimer, totalPoints.
"""

import json
import os

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
OLP03_PATH = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")
OLP05_PATH = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-05.json")

def balance_exam_answers(questions, start_idx=0, end_idx=None, target_dist=None):
    """
    Xáo trộn có quy luật thứ tự phương án của các câu hỏi từ start_idx đến end_idx
    để phân bố đáp án đúng trải đều A, B, C, D.
    """
    if end_idx is None:
        end_idx = len(questions)
    
    # Mục tiêu phân phối luân phiên: A, B, C, D, A, B, C, D...
    targets = ['A', 'B', 'C', 'D']
    t_idx = 0
    
    for i in range(start_idx, end_idx):
        q = questions[i]
        if q.get('type') != 'mcq':
            continue
            
        cur_ans = q['answer']
        desired_ans = targets[t_idx % len(targets)]
        t_idx += 1
        
        if cur_ans == desired_ans:
            continue
            
        # Tìm vị trí của phương án đúng hiện tại và phương án mong muốn
        opts = q['options']
        cur_opt_idx = next(idx for idx, o in enumerate(opts) if o['key'] == cur_ans)
        desired_opt_idx = next(idx for idx, o in enumerate(opts) if o['key'] == desired_ans)
        
        # Hoán đổi text giữa 2 phương án này
        temp_text = opts[cur_opt_idx]['text']
        opts[cur_opt_idx]['text'] = opts[desired_opt_idx]['text']
        opts[desired_opt_idx]['text'] = temp_text
        
        # Cập nhật đáp án đúng mới
        q['answer'] = desired_ans

# 1. Cân bằng olp-03.json (cho các câu mới thêm từ 50 đến 100)
with open(OLP03_PATH, 'r', encoding='utf-8') as f:
    d3 = json.load(f)

d3['durationMinutes'] = 90
d3['totalPoints'] = 100.0
d3['disclaimer'] = "Bộ đề mô phỏng cấu trúc kỳ thi Olympic Trí tuệ Nhân tạo Quốc gia (VOAI) 2026 do thầy Đỗ Đình Luật biên soạn, tích hợp trọn vẹn 100 câu trắc nghiệm và 4 bài tự luận chuyên sâu."

# Xáo trộn cân bằng câu 50 đến 100 (index 50 đến 100)
balance_exam_answers(d3['questions'], start_idx=50, end_idx=100)

with open(OLP03_PATH, 'w', encoding='utf-8') as f:
    json.dump(d3, f, ensure_ascii=False, indent=2)

print("Updated and balanced olp-03.json!")

# 2. Cân bằng olp-05.json
with open(OLP05_PATH, 'r', encoding='utf-8') as f:
    d5 = json.load(f)

d5['durationMinutes'] = 90
d5['totalPoints'] = 90.0
d5['disclaimer'] = "Ngân hàng câu hỏi chuyên đề thực chiến Computer Vision & NLP từ SkillPixel Quizzes kết hợp hệ thống slide bài giảng, chuẩn hóa lời giải 4 khối KaTeX."

balance_exam_answers(d5['questions'], start_idx=0, end_idx=len(d5['questions']))

with open(OLP05_PATH, 'w', encoding='utf-8') as f:
    json.dump(d5, f, ensure_ascii=False, indent=2)

print("Updated and balanced olp-05.json!")
