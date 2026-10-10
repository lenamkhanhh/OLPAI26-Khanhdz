# -*- coding: utf-8 -*-
"""
Tạo file Markdown content/04-de-chinh-thuc-voai-2025-ma-006.md
từ src/data/exams/voai-2025.json
"""
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(ROOT_DIR, "src", "data", "exams", "voai-2025.json")

with open(json_path, "r", encoding="utf-8") as f:
    exam = json.load(f)

md_lines = [
    "# ĐỀ THI CHÍNH THỨC OLYMPIC TRÍ TUỆ NHÂN TẠO 2025 (VOAI 2025)",
    "## Vòng Sơ Loại — Mã Đề 006 (100 Câu — 180 Phút)",
    "",
    "> **Nguồn gốc học thuật:** Đề thi chính thức do Ban Tổ Chức Olympic Tin Học Sinh Viên & Olympic Trí Tuệ Nhân Tạo Quốc Gia (VOAI) ban hành năm 2025.",
    "> **Lời giải đối chiếu chi tiết:** Biên soạn và phân tích chuyên sâu bởi tác giả Nguyễn Khắc Trung Kiên.",
    "",
    "---",
    ""
]

for idx, q in enumerate(exam["questions"], 1):
    md_lines.append(f"### Câu {idx:02d} [{q['id']}] — Phân hệ Module {q['module']} (Thang điểm: {q['points']}đ)")
    md_lines.append("")
    md_lines.append(f"**Đề bài:** {q['prompt']}")
    md_lines.append("")
    for opt in q["options"]:
        md_lines.append(f"- **{opt['key']}.** {opt['text']}")
    md_lines.append("")
    md_lines.append(f"**Đáp án chính xác:** `{q['answer']}`")
    md_lines.append("")
    md_lines.append(q["explanation"])
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

out_md = os.path.join(ROOT_DIR, "content", "04-de-chinh-thuc-voai-2025-ma-006.md")
with open(out_md, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Đã tạo thành công file Markdown {out_md} với {len(exam['questions'])} câu hỏi.")
