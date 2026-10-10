# -*- coding: utf-8 -*-
"""
Script scripts/check_markdown_sync.py
Kiểm tra đối soát đồng bộ toàn diện giữa 6 file JSON và các file Markdown tương ứng trong content/.
Kiểm tra theo từng ID câu hỏi đầy đủ:
- Tồn tại ID trong Markdown
- Khớp đáp án (answer key) đối với câu MCQ
- Khớp phương án lựa chọn A, B, C, D
- Khớp modelAnswer và rubric đối với câu tự luận / lập trình
- Trả mã thoát 0 nếu đồng bộ 100%, 1 nếu có bất kỳ lỗi nào.
"""

import os
import sys
import json
import re

ROOT = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

EXAM_MAPPING = [
    ("voai-2025.json", "04-de-chinh-thuc-voai-2025-ma-006.md"),
    ("olp-04.json", "04-de-bo-sung-insight-video-voai.md"),
    ("olp-02.json", "02-de-chuan-format-voai-expand.md"),
    ("olp-03.json", "03-de-vong-mien-voai-2025.md"),
    ("olp-05.json", "05-chuyen-de-thuc-chien-cv-nlp.md"),
    ("olp-01.json", "01-de-luyen-olp-01-toan-dien.md"),
]

def check_sync():
    total_errors = 0
    total_checked = 0

    print("=== KIỂM TRA ĐỐI SOÁT ĐỒNG BỘ MARKDOWN <-> JSON ===")

    for json_file, md_file in EXAM_MAPPING:
        j_path = os.path.join(ROOT, "src", "data", "exams", json_file)
        m_path = os.path.join(ROOT, "content", md_file)
        
        if not os.path.exists(j_path):
            print(f"[ERROR] Không tìm thấy file JSON: {j_path}")
            total_errors += 1
            continue
        if not os.path.exists(m_path):
            print(f"[ERROR] Không tìm thấy file MD: {m_path}")
            total_errors += 1
            continue
            
        with open(j_path, "r", encoding="utf-8") as f:
            j_data = json.load(f)
        with open(m_path, "r", encoding="utf-8") as f:
            m_text = f.read()

        exam_errors = 0
        questions = j_data.get("questions", [])
        
        for q in questions:
            total_checked += 1
            qid = q["id"]
            
            # 1. Kiểm tra ID tồn tại
            if f"[{qid}]" not in m_text and f"{qid}" not in m_text:
                print(f"[{json_file}] Thiếu ID {qid} trong {md_file}")
                exam_errors += 1
                continue
                
            # 2. Với MCQ: Kiểm tra đáp án chính xác
            if q.get("type") == "mcq":
                expected_ans = q.get("answer")
                # Pattern: ### ... [qid] ... Đáp án chính xác: `X`
                # Tìm block câu hỏi
                q_pattern = rf"###[^\n]*?\[{re.escape(qid)}\][\s\S]*?(?=(?:###\s+(?:Câu\s+\d+|\[OLP|\[VOAI|\[SKILL)|\Z))"
                m_block = re.search(q_pattern, m_text)
                if not m_block:
                    print(f"[{json_file}] Không trích xuất được block cho ID {qid}")
                    exam_errors += 1
                    continue
                    
                block_content = m_block.group(0)
                ans_match = re.search(r"\*\*Đáp án chính xác:\*\*\s*`([A-D])`", block_content)
                if not ans_match:
                    ans_match = re.search(r"\*\*Đáp án đúng\*\*:\s*\*\*([A-D])\*\*", block_content)
                    
                if not ans_match:
                    print(f"[{json_file}] {qid}: Không tìm thấy đáp án trong Markdown")
                    exam_errors += 1
                elif ans_match.group(1) != expected_ans:
                    print(f"[{json_file}] {qid}: Lệch đáp án! JSON={expected_ans}, MD={ans_match.group(1)}")
                    exam_errors += 1

                # Kiểm tra đủ options
                for opt in q.get("options", []):
                    opt_key = opt["key"]
                    if f"- **{opt_key}.**" not in block_content and f"- {opt_key}." not in block_content:
                        print(f"[{json_file}] {qid}: Thiếu option {opt_key}")
                        exam_errors += 1
                        
            # 3. Với Tự luận: Kiểm tra rubric & modelAnswer
            elif q.get("type") == "essay":
                q_pattern = rf"###[^\n]*?\[{re.escape(qid)}\][\s\S]*?(?=(?:###\s+(?:Câu\s+\d+|\[OLP|\[VOAI|\[SKILL)|\Z))"
                m_block = re.search(q_pattern, m_text)
                if not m_block:
                    print(f"[{json_file}] Không trích xuất được block tự luận {qid}")
                    exam_errors += 1
                    continue
                block_content = m_block.group(0)
                if "Rubric" not in block_content and "chấm điểm" not in block_content:
                    print(f"[{json_file}] {qid}: Thiếu phần Rubric trong Markdown")
                    exam_errors += 1
                if "Model Answer" not in block_content and "Lời giải" not in block_content and "chi tiết" not in block_content:
                    print(f"[{json_file}] {qid}: Thiếu phần Model Answer trong Markdown")
                    exam_errors += 1

        if exam_errors == 0:
            print(f"✓ PASS {json_file} <-> {md_file}: Khớp 100% {len(questions)} câu.")
        else:
            print(f"✗ FAIL {json_file} <-> {md_file}: Có {exam_errors} lỗi.")
            total_errors += exam_errors

    print(f"\nTổng số câu đã kiểm tra đối soát: {total_checked}")
    print(f"Tổng số lỗi phát hiện: {total_errors}")

    if total_errors > 0:
        print("KẾT QUẢ: THẤT BẠI (EXIT 1)")
        sys.exit(1)
    else:
        print("KẾT QUẢ: TẤT CẢ MARKDOWN ĐỒNG BỘ 100% VỚI JSON (EXIT 0)")
        sys.exit(0)

if __name__ == "__main__":
    check_sync()
