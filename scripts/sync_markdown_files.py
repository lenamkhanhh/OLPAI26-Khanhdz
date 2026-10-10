# -*- coding: utf-8 -*-
"""
Script đồng bộ tài liệu Markdown:
1. Cập nhật content/03-de-vong-mien-voai-2025.md với đủ 100 câu MCQ + 4 câu tự luận.
2. Tạo mới content/05-chuyen-de-thuc-chien-cv-nlp.md cho 90 câu SkillPixel Quizzes.
"""

import json
import os

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
OLP03_JSON = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")
OLP05_JSON = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-05.json")

MD03_PATH = os.path.join(ROOT_DIR, "content", "03-de-vong-mien-voai-2025.md")
MD05_PATH = os.path.join(ROOT_DIR, "content", "05-chuyen-de-thuc-chien-cv-nlp.md")

with open(OLP03_JSON, "r", encoding="utf-8") as f:
    d3 = json.load(f)

with open(OLP05_JSON, "r", encoding="utf-8") as f:
    d5 = json.load(f)

# 1. Sinh content/03-de-vong-mien-voai-2025.md
lines_03 = [
    "# ĐỀ THI 03: MÔ PHỎNG ĐỀ THI OLYMPIC TRÍ TUỆ NHÂN TẠO QUỐC GIA VOAI (104 CÂU)",
    "> **Nguồn gốc**: Đề thi mô phỏng chuẩn cấu trúc kỳ thi Olympic AI Quốc gia (VOAI) do thầy Đỗ Đình Luật biên soạn gồm trọn vẹn 100 câu trắc nghiệm chuyên sâu (Module A, B, C) và 4 bài toán tự luận thiết kế kiến trúc AI thực chiến.",
    "> **Mục tiêu**: Luyện thi toàn diện Toán tối ưu, Học máy nền tảng, Deep Learning, Thị giác máy tính (CV), Xử lý ngôn ngữ tự nhiên (NLP) và Vận hành mô hình (MLOps).",
    "",
    "---",
    "",
    "## PHẦN 1: 100 CÂU HỎI TRẮC NGHIỆM CHUẨN VOAI",
    ""
]

for q in d3["questions"]:
    if q["type"] == "mcq":
        lines_03.append(f"### Câu {q['id']}: {q['prompt']}")
        lines_03.append("")
        for opt in q["options"]:
            lines_03.append(f"- **{opt['key']}.** {opt['text']}")
        lines_03.append("")
        lines_03.append(f"**Đáp án đúng:** `{q['answer']}`")
        lines_03.append("")
        lines_03.append("#### Lời giải chi tiết:")
        lines_03.append(q["explanation"])
        lines_03.append("")
        lines_03.append("---")
        lines_03.append("")

lines_03.append("## PHẦN 2: 4 BÀI TOÁN THỰC CHIẾN KIẾN TRÚC GIẢI PHÁP VÒNG MIỀN & VOAI")
lines_03.append("")

for q in d3["questions"]:
    if q["type"] != "mcq":
        lines_03.append(f"### Bài {q['id']}: {q['prompt']}")
        lines_03.append("")
        lines_03.append("#### Hướng dẫn giải chi tiết:")
        lines_03.append(q.get("explanation", ""))
        lines_03.append("")
        lines_03.append("---")
        lines_03.append("")

with open(MD03_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines_03))

print(f"Updated {MD03_PATH} successfully! Total lines: {len(lines_03)}")

# 2. Sinh content/05-chuyen-de-thuc-chien-cv-nlp.md
lines_05 = [
    "# ĐỀ THI 05: NGÂN HÀNG CHUYÊN ĐỀ THỰC CHIẾN CV & NLP (90 CÂU - SKILLPIXEL)",
    "> **Nguồn gốc**: Tuyển tập 90 câu hỏi trắc nghiệm chuyên sâu từ ngân hàng đề SkillPixel Quizzes kết hợp hệ thống slide bài giảng Buổi 1, 2, 5, 6, 9.",
    "> **Cấu trúc**: Gồm 35 câu NLP & Dịch máy (Session 5) và 55 câu Computer Vision & CNN Kiến trúc SOTA (Session 9) kèm lời giải 4 khối KaTeX chuẩn mực.",
    "",
    "---",
    "",
    "## PHẦN 1: CHUYÊN ĐỀ NLP & MACHINE TRANSLATION (35 CÂU)",
    ""
]

for q in d5["questions"]:
    if q["id"].startswith("SKILL-NLP"):
        lines_05.append(f"### Câu {q['id']}: {q['prompt']}")
        lines_05.append("")
        for opt in q["options"]:
            lines_05.append(f"- **{opt['key']}.** {opt['text']}")
        lines_05.append("")
        lines_05.append(f"**Đáp án đúng:** `{q['answer']}`")
        lines_05.append("")
        lines_05.append("#### Lời giải chi tiết:")
        lines_05.append(q["explanation"])
        lines_05.append("")
        lines_05.append("---")
        lines_05.append("")

lines_05.append("## PHẦN 2: CHUYÊN ĐỀ COMPUTER VISION & CNN BASICS (55 CÂU)")
lines_05.append("")

for q in d5["questions"]:
    if q["id"].startswith("SKILL-CV"):
        lines_05.append(f"### Câu {q['id']}: {q['prompt']}")
        lines_05.append("")
        for opt in q["options"]:
            lines_05.append(f"- **{opt['key']}.** {opt['text']}")
        lines_05.append("")
        lines_05.append(f"**Đáp án đúng:** `{q['answer']}`")
        lines_05.append("")
        lines_05.append("#### Lời giải chi tiết:")
        lines_05.append(q["explanation"])
        lines_05.append("")
        lines_05.append("---")
        lines_05.append("")

with open(MD05_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines_05))

print(f"Created {MD05_PATH} successfully! Total lines: {len(lines_05)}")
