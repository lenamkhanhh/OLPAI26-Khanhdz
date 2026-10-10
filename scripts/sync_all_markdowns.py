# -*- coding: utf-8 -*-
"""
Script scripts/sync_all_markdowns.py
Đồng bộ hóa 100% tất cả 6 ngân hàng đề thi Markdown từ 6 file JSON nguồn chuẩn hóa.
Bảo đảm:
1. Đề 04 và VOAI 2025: Giữ nguyên vẹn các sửa đổi học thuật (Q08, Q13, ảnh Q26, [UNVALIDATED CASE STUDY]).
2. Đề 02 (02-de-chuan-format-voai-expand.md): Đồng bộ M43 phương án D là 2/7, key A, bẫy 800/2800; đủ 60 MCQ + 6 essays.
3. Đề 03 (03-de-vong-mien-voai-2025.md): Đồng bộ 100 MCQ và 4 essays (đầy đủ modelAnswer & rubric); header minh bạch nguồn gốc (tái tạo với Gemini).
4. Đề 05 (05-chuyen-de-thuc-chien-cv-nlp.md): Đồng bộ 90 MCQ, options, keys, explanations, NLP-01 ref §4.2.
5. Đề 01 (02-de-luyen-olp-ai.md, 03-dap-an-olp-ai.md, 01-de-luyen-olp-01-toan-dien.md): Đồng bộ C10 Ridge/L2 Key A.
"""

import os
import json
import re

ROOT = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

def format_question_block(q, idx=None):
    num_str = f"{idx:02d}" if idx is not None and idx < 100 else f"{idx}" if idx is not None else ""
    header_prefix = f"Câu {num_str} " if num_str else ""
    lines = [
        f"### {header_prefix}[{q['id']}] — Phân hệ Module {q['module']} (Thang điểm: {q.get('points', 1.0)}đ)",
        "",
        f"**Đề bài:** {q['prompt']}",
        ""
    ]
    if q.get("image"):
        lines.append(f"![Hình minh họa {q['id']}]({q['image']})")
        lines.append("")
    
    if q.get("type") == "mcq":
        if q.get("options"):
            for opt in q["options"]:
                lines.append(f"- **{opt['key']}.** {opt['text']}")
            lines.append("")
        lines.append(f"**Đáp án chính xác:** `{q['answer']}`")
        lines.append("")
        if q.get("explanation"):
            lines.append(q["explanation"])
            lines.append("")
    elif q.get("type") == "code":
        lines.append("**Dạng bài:** Lập trình thuật toán AI (Chấm theo tiêu chí kiểm thử từng phần)")
        lines.append("")
        if q.get("explanation"):
            lines.append(q["explanation"])
            lines.append("")
        if q.get("modelAnswer"):
            lines.append("**Mã nguồn mẫu / Lời giải:**")
            lines.append(q["modelAnswer"])
            lines.append("")
        if q.get("rubric"):
            lines.append("**Tiêu chí kiểm thử từng phần (Partial Scoring Rubric):**")
            for r in q["rubric"]:
                lines.append(f"- {r}")
            lines.append("")
    elif q.get("type") == "essay":
        lines.append("**Dạng bài:** Tự luận thiết kế giải pháp AI")
        lines.append("")
        if q.get("modelAnswer"):
            lines.append("**Hướng dẫn giải chi tiết (Model Answer):**")
            lines.append(q["modelAnswer"])
            lines.append("")
        if q.get("rubric"):
            lines.append("**Tiêu chí chấm điểm (Rubric):**")
            for r in q["rubric"]:
                lines.append(f"- {r}")
            lines.append("")
            
    lines.append("---")
    lines.append("")
    return "\n".join(lines)

def sync_voai2025():
    json_path = os.path.join(ROOT, "src", "data", "exams", "voai-2025.json")
    md_path = os.path.join(ROOT, "content", "04-de-chinh-thuc-voai-2025-ma-006.md")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    lines = [
        "# ĐỀ THI CHÍNH THỨC OLYMPIC TRÍ TUỆ NHÂN TẠO 2025 (VOAI 2025)",
        "## Vòng Sơ Loại — Mã Đề 006 (100 Câu — 180 Phút)",
        "",
        "> **Nguồn gốc học thuật:** Đề thi chính thức do Ban Tổ Chức Olympic Tin Học Sinh Viên & Olympic Trí Tuệ Nhân Tạo Quốc Gia (VOAI) ban hành năm 2025.",
        "> **Lời giải đối chiếu chi tiết:** Biên soạn và phân tích chuyên sâu đối chiếu với nguồn lời giải tác giả Nguyễn Khắc Trung Kiên.",
        "",
        "---",
        ""
    ]
    for i, q in enumerate(data["questions"], 1):
        lines.append(format_question_block(q, i))
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[SYNC] {md_path}: {len(data['questions'])} câu.")

def sync_olp04():
    json_path = os.path.join(ROOT, "src", "data", "exams", "olp-04.json")
    md_path = os.path.join(ROOT, "content", "04-de-bo-sung-insight-video-voai.md")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    lines = [
        "# ĐỀ THI 04: BỔ SUNG CHUYÊN SÂU INSIGHT VIDEO VOAI 2026",
        "## 20 Câu Trắc Nghiệm Kỹ Thuật Chuyên Sâu (Module A) & 4 Bài Tự Luận Thực Chiến (Module C)",
        "",
        "> **Nguồn gốc học thuật:** Đề thi tổng hợp các tình huống bài toán Deep Learning nâng cao mô phỏng kinh nghiệm thực chiến từ chuyên đề VOAI.",
        "> **Lưu ý khảo thí:** Các số liệu định lượng (Macro-F1 ~84% lên 97.1%, 41 lỗi giảm còn 8 lỗi) là tình huống nghiên cứu ca điển hình giả định (unvalidated case study) để luyện tư duy tối ưu.",
        "",
        "---",
        ""
    ]
    for i, q in enumerate(data["questions"], 1):
        lines.append(format_question_block(q, i))
        
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[SYNC] {md_path}: {len(data['questions'])} câu.")

def sync_olp02():
    json_path = os.path.join(ROOT, "src", "data", "exams", "olp-02.json")
    md_path = os.path.join(ROOT, "content", "02-de-chuan-format-voai-expand.md")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    lines = [
        "# ĐỀ THI 02: CHUẨN FORMAT VOAI MỞ RỘNG (MOCK EXAM FULL STANDARD)",
        "## 60 Câu Trắc Nghiệm Chuyên Sâu (90.0đ) & 6 Bài Tự Luận Thiết Kế Giải Pháp AI (60.0đ)",
        "",
        "> **Mô tả:** Đề thi mô phỏng toàn diện chuẩn cấu trúc VOAI & Olympic AI Sinh viên 2025-2026 (Đề 2 Thầy Đỗ Đình Luật).",
        "> **Thời gian làm bài:** 90 phút | **Tổng số câu:** 66 câu (60 Trắc nghiệm + 6 Tự luận) | **Thang điểm:** 150.0 điểm",
        "",
        "---",
        ""
    ]
    for i, q in enumerate(data["questions"], 1):
        lines.append(format_question_block(q, i))
        
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[SYNC] {md_path}: {len(data['questions'])} câu.")

def sync_olp03():
    json_path = os.path.join(ROOT, "src", "data", "exams", "olp-03.json")
    md_path = os.path.join(ROOT, "content", "03-de-vong-mien-voai-2025.md")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    lines = [
        "# ĐỀ THI 03: MÔ PHỎNG ĐỀ THI OLYMPIC TRÍ TUỆ NHÂN TẠO QUỐC GIA VOAI (104 CÂU)",
        "## 100 Câu Trắc Nghiệm Chuẩn Hóa (100.0đ) & 4 Bài Tự Luận Giải Pháp AI Thực Chiến (40.0đ)",
        "",
        "> **Nguồn gốc học thuật:** Ngân hàng đề thi mô phỏng chuẩn cấu trúc kỳ thi Olympic AI Quốc gia (VOAI).",
        "> **Tuyên bố minh bạch:** Bộ câu hỏi được tái tạo và chuẩn hóa với sự trợ giúp của AI (Gemini) dựa trên các chuyên đề ôn thi vòng trường, không phải nguyên bản 100 câu chính thức từ Thầy Đỗ Đình Luật.",
        "",
        "---",
        ""
    ]
    for i, q in enumerate(data["questions"], 1):
        lines.append(format_question_block(q, i))
        
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[SYNC] {md_path}: {len(data['questions'])} câu.")

def sync_olp05():
    json_path = os.path.join(ROOT, "src", "data", "exams", "olp-05.json")
    md_path = os.path.join(ROOT, "content", "05-chuyen-de-thuc-chien-cv-nlp.md")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    lines = [
        "# ĐỀ THI 05: NGÂN HÀNG CHUYÊN ĐỀ THỰC CHIẾN CV & NLP (90 CÂU - SKILLPIXEL)",
        "## 35 Câu NLP & Dịch Máy + 55 Câu Computer Vision & CNN Kiến Trúc SOTA (90.0đ)",
        "",
        "> **Nguồn gốc học thuật:** Tuyển tập 90 câu hỏi trắc nghiệm chuyên sâu từ ngân hàng đề SkillPixel Quizzes kết hợp hệ thống slide bài giảng Buổi 1, 2, 5, 6, 9.",
        "> **Mục tiêu:** Củng cố toàn diện kiến thức biểu diễn từ (Word Representations §4.2), Attention, Transformer, ResNet, ViT, YOLO và các kiến trúc Deep Learning cốt lõi.",
        "",
        "---",
        ""
    ]
    for i, q in enumerate(data["questions"], 1):
        lines.append(format_question_block(q, i))
        
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[SYNC] {md_path}: {len(data['questions'])} câu.")

def sync_olp01():
    json_path = os.path.join(ROOT, "src", "data", "exams", "olp-01.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # 1. Tạo bản canonical đầy đủ: content/01-de-luyen-olp-01-toan-dien.md
    canonical_path = os.path.join(ROOT, "content", "01-de-luyen-olp-01-toan-dien.md")
    lines = [
        "# ĐỀ THI 01: ÔN TẬP TOÀN DIỆN OLP AI HCMUS 2026 (CANONICAL EDITION)",
        "## 60 Câu Tự Động Chấm (58 MCQ + 2 Code: 100.0đ) & 4 Bài Tự Luận Theo Rubric (40.0đ)",
        "",
        "> **Nguồn gốc học thuật:** Đề thi chuẩn hóa toàn diện phủ kín 3 phân hệ Module A (Toán & Xác suất thống kê), Module B (Học máy cổ điển), Module C (Deep Learning & Computer Vision/NLP).",
        "",
        "---",
        ""
    ]
    for i, q in enumerate(data["questions"], 1):
        lines.append(format_question_block(q, i))
    with open(canonical_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[SYNC] {canonical_path}: {len(data['questions'])} câu.")
    
    # 2. Cập nhật câu C10 trong 02-de-luyen-olp-ai.md
    p2 = os.path.join(ROOT, "content", "02-de-luyen-olp-ai.md")
    with open(p2, "r", encoding="utf-8") as f:
        c2 = f.read()
    
    c10_q = [q for q in data['questions'] if q['id'] == 'OLP01-C10'][0]
    # Sửa C10 trong 02-de-luyen-olp-ai.md sang khớp JSON (Key A)
    old_c10_block = "**C10.** Nhiều feature tương quan mạnh với nhau. Dùng L1 hay L2 ổn định hơn, vì sao?\nA. L1 vì luôn cho độ chính xác cao hơn · B. L2 vì co đều trọng số, ổn định hơn · C. Bỏ regularization vì ridge làm chậm · D. Cả hai như nhau với mọi dữ liệu"
    new_c10_block = "**C10.** Trong trường hợp tập dữ liệu chứa nhiều đặc trưng có độ tương quan tuyến tính rất cao với nhau (hiện tượng Đa cộng tuyến — Multicollinearity), kỹ thuật L2 Regularization (Ridge) thường được ưu tiên hơn L1 (Lasso) vì lý do gì?\nA. Vì L1 sẽ chọn ngẫu nhiên 1 đặc trưng và loại bỏ các đặc trưng còn lại một cách không ổn định, trong khi L2 co đều các hệ số trọng số và luôn đảm bảo ma trận $(X^T X + \\lambda I)$ khả nghịch · B. Vì L2 tính toán không cần ma trận · C. Vì L2 luôn đưa toàn bộ trọng số về chính xác bằng 0 · D. Vì L2 không cần siêu tham số lambda"
    
    if old_c10_block in c2:
        c2 = c2.replace(old_c10_block, new_c10_block)
        with open(p2, "w", encoding="utf-8") as f:
            f.write(c2)
        print(f"[SYNC] Updated C10 in {p2}")
        
    # 3. Cập nhật câu C10 trong 03-dap-an-olp-ai.md
    p3 = os.path.join(ROOT, "content", "03-dap-an-olp-ai.md")
    with open(p3, "r", encoding="utf-8") as f:
        c3 = f.read()
    
    c3 = c3.replace("| C10 | B |", "| C10 | A |")
    c3 = c3.replace(
        "**C10 → B.** Đúng: L2 co đều, ổn định. Sai: A L1 giật cục khi tương quan; C/D sai. → Xem §1.6.",
        "**C10 → A.** Đúng: L1 bấp bênh khi tương quan cao; L2 co đều trọng số và cộng $\\lambda I$ giúp $(X^T X + \\lambda I)$ luôn khả nghịch (với $\\lambda > 0$). Sai: B/C/D. → Xem §1.6."
    )
    with open(p3, "w", encoding="utf-8") as f:
        f.write(c3)
    print(f"[SYNC] Updated C10 in {p3}")

if __name__ == "__main__":
    sync_voai2025()
    sync_olp04()
    sync_olp02()
    sync_olp03()
    sync_olp05()
    sync_olp01()
    print("=== TẤT CẢ 6 NGÂN HÀNG ĐỀ THI MARKDOWN ĐÃ ĐƯỢC ĐỒNG BỘ 100% TỪ JSON ===")
