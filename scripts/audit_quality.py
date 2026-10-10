# -*- coding: utf-8 -*-
"""
scripts/audit_quality.py
Bộ kiểm toán chất lượng học thuật và tính toàn vẹn của 6 ngân hàng đề thi OLP AI (448 câu hỏi):
- Quét động toàn bộ các tệp JSON trong src/data/exams.
- Phân biệt rõ loại câu: MCQ/Code (kiểm tra explanation 4 khối) vs Essay (kiểm tra modelAnswer, rubric, rubricPoints).
- Kiểm tra tính tồn tại của tham chiếu § giáo trình đối chiếu với content/01-ly-thuyet-olp-ai.md.
- Kiểm tra tính tồn tại của các ID câu hỏi liên hệ chéo.
- Kiểm tra chống lỗi chấm P0: OLP01-C10 phải là key A, VOAI02-M43 không trùng options, VOAI25-024 key B.
- Kiểm tra không tồn tại chu kỳ lặp đáp án tuần tự ABCD trong các đề mock.
- Trả về exit code 1 nếu phát hiện lỗi vi phạm; exit code 0 nếu pass toàn bộ.
"""

import json
import sys
import os
import re
import glob

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

# 1. Nạp danh mục mục § lý thuyết hợp lệ từ giáo trình
theory_path = os.path.join(ROOT_DIR, "content", "01-ly-thuyet-olp-ai.md")
with open(theory_path, "r", encoding="utf-8") as f:
    theory_text = f.read()

valid_sections = set(re.findall(r'§[\d\.]+', theory_text))
print(f"-> Đã nạp {len(valid_sections)} mục § lý thuyết từ giáo trình.")

# 2. Nạp toàn bộ câu hỏi từ tất cả các đề thi JSON trong src/data/exams
exams_dir = os.path.join(ROOT_DIR, "src", "data", "exams")
exam_files = sorted(glob.glob(os.path.join(exams_dir, "*.json")))

exams = {}
all_qids = set()
for path in exam_files:
    name = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        exams[name] = data
        for q in data.get("questions", []):
            all_qids.add(q["id"])

print(f"-> Đã quét động {len(exams)} ngân hàng đề thi: {', '.join(exams.keys())}")
print(f"-> Đã nạp tổng cộng {len(all_qids)} câu hỏi từ 6 đề thi.\n")

errors = []
stats = {}

# 3. Tiến hành kiểm toán từng đề
for name, data in exams.items():
    qs = data.get('questions', [])
    stats[name] = {"mcq_pass": 0, "essay_pass": 0, "total": len(qs), "mcq_total": 0, "essay_total": 0}
    
    # Kiểm tra chu kỳ tuần tự ABCD trên các đề mock
    if name in ['olp-03.json', 'olp-05.json']:
        mcq_answers = [q['answer'] for q in qs if q.get('type') == 'mcq']
        if len(mcq_answers) >= 12:
            is_strict_cycle = all(mcq_answers[i] == ['A', 'B', 'C', 'D'][i % 4] for i in range(len(mcq_answers)))
            if is_strict_cycle:
                errors.append(f"[{name}]: Toàn bộ {len(mcq_answers)} câu MCQ đang dính chu kỳ lặp đáp án tuần tự ABCD thô sơ!")
    
    for q in qs:
        qid = q["id"]
        qtype = q.get("type", "mcq")
        
        # 3.1. Kiểm tra các câu P0 then chốt
        if qid == "OLP01-C10" and q.get("answer") != "A":
            errors.append(f"[{name}] OLP01-C10: Phải có đáp án là 'A' (xác suất Hồi âm=0), hiện là '{q.get('answer')}'.")
            
        if qid == "VOAI02-M43":
            opt_texts = [o.get("text", "").strip() for o in q.get("options", [])]
            if len(set(opt_texts)) != len(opt_texts):
                errors.append(f"[{name}] VOAI02-M43: Tồn tại phương án trùng lặp trong options.")
                
        if qid == "VOAI25-024" and q.get("answer") != "B":
            errors.append(f"[{name}] VOAI25-024: Đáp án chuẩn theo đề gốc PDF mã 006 phải là 'B', hiện là '{q.get('answer')}'.")

        if qtype in ['mcq', 'code']:
            stats[name]["mcq_total"] += 1
            exp = q.get("explanation", "")
            
            # Kiểm tra 4 khối chuẩn
            has_b1 = ("### 1." in exp) or ("ELI5" in exp)
            has_b2 = ("### 2." in exp) or ("Toán" in exp) or ("Công thức" in exp) or ("Đạo hàm" in exp)
            has_b3 = ("### 3." in exp) or ("Bẫy" in exp) or ("Pitfalls" in exp)
            has_b4 = ("### 4." in exp) or ("Mắt xích" in exp) or ("Căn cứ" in exp)
            
            if not (has_b1 and has_b2 and has_b3 and has_b4):
                errors.append(f"[{name}] {qid} ({qtype}): Thiếu cấu trúc 4 khối chuẩn trong explanation.")
                continue
                
            # Kiểm tra định nghĩa thuật ngữ trong Khối 1
            has_term = ("Thuật ngữ" in exp) or ("Định nghĩa" in exp) or ("Bản chất" in exp) or ("Hiểu nhanh" in exp) or ("👶" in exp) or ("Giống như" in exp) or ("Tưởng tượng" in exp) or ("Hãy tưởng tượng" in exp)
            if not has_term:
                errors.append(f"[{name}] {qid} ({qtype}): Thiếu định nghĩa thuật ngữ trong Khối 1.")
                
            # Kiểm tra tham chiếu mục § lý thuyết trong Khối 4
            sec_refs = [s.rstrip('.,;:!?)') for s in re.findall(r'§[\d\.]+', exp)]
            for s in sec_refs:
                if s not in valid_sections:
                    errors.append(f"[{name}] {qid} ({qtype}): Tham chiếu mục {s} không tồn tại trong giáo trình.")
                        
            # Kiểm tra ID câu hỏi liên hệ
            ref_qids = re.findall(r'(OLP01-[A-Z0-9]+|VOAI02-[A-Z0-9]+|VOAI03-[A-Z0-9]+)', exp)
            for rq in ref_qids:
                if rq != qid and rq not in all_qids:
                    errors.append(f"[{name}] {qid} ({qtype}): Tham chiếu câu liên hệ {rq} không tồn tại trong bộ đề.")
                    
            stats[name]["mcq_pass"] += 1
            
        elif qtype == 'essay':
            stats[name]["essay_total"] += 1
            model_ans = q.get("modelAnswer", "")
            rubric = q.get("rubric", [])
            rubric_pts = q.get("rubricPoints", [])
            
            if not model_ans or len(model_ans.strip()) < 100:
                errors.append(f"[{name}] {qid} (essay): modelAnswer trống hoặc quá ngắn (<100 ký tự).")
                continue
                
            if not rubric or len(rubric) < 3:
                errors.append(f"[{name}] {qid} (essay): rubric trống hoặc có ít hơn 3 tiêu chí.")
                continue
                
            if rubric_pts and sum(rubric_pts) != q.get("points", 0):
                errors.append(f"[{name}] {qid} (essay): Tổng rubricPoints ({sum(rubric_pts)}) không khớp điểm câu hỏi ({q.get('points')}).")
                continue
                
            stats[name]["essay_pass"] += 1

print("=== KẾT QUẢ AUDIT CHẤT LƯỢNG NỘI DUNG ===")
for name, s in stats.items():
    print(f"[{name}] Tổng {s['total']} câu | MCQ/Code: {s['mcq_pass']}/{s['mcq_total']} đạt chuẩn | Essay: {s['essay_pass']}/{s['essay_total']} đạt chuẩn")

if errors:
    print(f"\n[FAIL] Phát hiện {len(errors)} lỗi chất lượng cần khắc phục:")
    for err in errors[:20]:
        print("  - " + err)
    if len(errors) > 20:
        print(f"  ... và {len(errors) - 20} lỗi khác.")
    sys.exit(1)
else:
    print(f"\n[PASS] Tất cả {len(all_qids)} câu hỏi đều thỏa mãn 100% quy chuẩn cấu trúc, rubric, § giáo trình và ID liên hệ.")
    print("Ghi chú giới hạn: Kiểm toán tự động đảm bảo tính toàn vẹn cấu trúc và tham chiếu logic; không thay thế việc đọc hiểu và luyện tập thực tế của thí sinh.")
    sys.exit(0)
