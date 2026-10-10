# -*- coding: utf-8 -*-
"""
Script sinh tài liệu content/06-khoa-hoc-olp-ai-va-voai-nang-cao.md
Tổng hợp toàn bộ 29 bài giảng video, slide, transcript và notebook code
từ khóa học Olympic AI Sinh Viên Chuyên Sâu 2026 & VOAI Nâng Cao.
"""

import json
import os

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
DATA_PATH = os.path.join(ROOT_DIR, "src", "data", "courses_data.json")
OUT_MD = os.path.join(ROOT_DIR, "content", "06-khoa-hoc-olp-ai-va-voai-nang-cao.md")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    courses = json.load(f)

lines = [
    "# TỔNG HỢP TOÀN DIỆN KHO BÀI GIẢNG & TÀI NGUYÊN THỰC CHIẾN OLP AI & VOAI 2026",
    "> **Nguồn gốc dữ liệu**: Dữ liệu thu thập chính thức từ hệ thống đào tạo Olympic AI Sinh Viên Chuyên Sâu 2026 và Khóa Luyện thi VOAI Nâng Cao (SkillPixel).",
    "> **Mục đích**: Cung cấp trọn bộ đường dẫn Video bài giảng phát trực tiếp, Slide lý thuyết Google Drive, Transcript ghi chép tóm tắt và Notebook code thực hành cho các thí sinh ôn luyện.",
    "",
    "---",
    "",
    "## PHẦN 1: KHÓA HỌC OLYMPIC AI SINH VIÊN CHUYÊN SÂU 2026 (16 BUỔI)",
    "",
    "| STT | Tên Buổi Học | Ngày Học | Video Trực Tiếp | Slide Drive | Tài Liệu Transcript | Lab / Notebook |",
    "|:---:|:---|:---:|:---:|:---:|:---:|:---:|"
]

for l in courses["olp_course"]["lessons"]:
    idx = l.get("index", "")
    title = l.get("title", "")
    date = l.get("date", "-")
    
    vid = f"[Xem Video ↗]({l['videoIframe']})" if l.get("videoIframe") else "-"
    slide = f"[Tải Slide ↗]({l['slide']})" if l.get("slide") else "-"
    trans = f"[Xem Docs ↗]({l['transcript']})" if l.get("transcript") else "-"
    lab = f"[Mở Lab ↗]({l['lab']})" if l.get("lab") else "-"
    
    lines.append(f"| **{idx}** | {title} | {date} | {vid} | {slide} | {trans} | {lab} |")

lines.extend([
    "",
    "---",
    "",
    "## PHẦN 2: KHÓA CHUYÊN ĐỀ VOAI NÂNG CAO & GIẢI ĐỀ (13 BÀI GIẢNG CHUYÊN SÂU)",
    "",
    "| STT | Chuyên Đề Bài Giảng | Video Trực Tiếp | Slide Lý Thuyết | Notebook Code / Thực Hành |",
    "|:---:|:---|:---:|:---:|:---:|"
])

for i, l in enumerate(courses["voai_course"]["lessons"], 1):
    title = l.get("title", "")
    vid = f"[Xem Video ↗]({l['videoIframe']})" if l.get("videoIframe") else "-"
    slide = f"[Tải Slide ↗]({l['slide']})" if l.get("slide") else "-"
    nb = f"[Mở Notebook ↗]({l['notebook']})" if l.get("notebook") else "-"
    
    lines.append(f"| **{i}** | {title} | {vid} | {slide} | {nb} |")

lines.extend([
    "",
    "---",
    "",
    "## HƯỚNG DẪN SỬ DỤNG TÀI NGUYÊN HIỆU QUẢ",
    "1. **Xem Video kết hợp Sổ tay Lý thuyết**: Khi làm đề trên Web Study Hub, đối với mỗi câu hỏi lý thuyết phức tạp, bạn có thể tra cứu mục tương ứng trong Sổ tay (§1.x - §7.x) và mở video clip tương ứng.",
    "2. **Thực hành với Notebook Code**: Tải các file Notebook trong cột *Notebook Code / Lab* về chạy trên Google Colab hoặc Kaggle GPU để nắm vững pipeline xử lý dữ liệu, tinh chỉnh mô hình và viết submission file.",
    "3. **Đọc Transcript tóm tắt**: Sử dụng tài liệu Google Docs tóm tắt của từng buổi để ôn nhanh các khái niệm trước khi bước vào phòng thi."
])

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Successfully generated {OUT_MD} with {len(lines)} lines!")
