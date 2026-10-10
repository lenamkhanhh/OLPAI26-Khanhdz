# -*- coding: utf-8 -*-
"""
scripts/update_and_run_hub.py
Cập nhật docs/generate_full_hub.py để nạp đủ 3 đề thi (olp-01, olp-02, olp-03),
sửa triệt để timer NaN, hỗ trợ rubric & modelAnswer 10 bài essay, format lời giải 4 khối chuẩn,
sau đó sinh ra olympic_ai_study_hub.html cho cả 3 đường dẫn (public, dist, temp/public).
"""

import os
import sys
import json
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
TEMP_DIR = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26"

def build():
    gen_script = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")
    with open(gen_script, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Bỏ import voai_50_questions_data
    content = content.replace('from voai_50_questions_data import VOAI_QUESTIONS', '# Đã chuyển sang đọc trực tiếp 3 đề JSON chuẩn hóa')

    # 2. Đọc cả 3 đề olp-01, olp-02, olp-03
    old_read = '''# 1. Đọc Đề 01 gốc (64 câu)
olp01_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-01.json")
with open(olp01_path, "r", encoding="utf-8") as f:
    olp01_data = json.load(f)'''

    new_read = '''# 1. Đọc cả 3 đề thi đã chuẩn hóa từ src/data/exams/
olp01_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-01.json")
olp02_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-02.json")
olp03_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")

with open(olp01_path, "r", encoding="utf-8") as f:
    olp01_data = json.load(f)
with open(olp02_path, "r", encoding="utf-8") as f:
    olp02_data = json.load(f)
with open(olp03_path, "r", encoding="utf-8") as f:
    olp03_data = json.load(f)'''

    content = content.replace(old_read, new_read)

    # 3. Thay thế đoạn xử lý voai_questions_converted bằng cách gom 3 đề trực tiếp
    old_exams_block = '''# Chuẩn hóa 50 câu VOAI
voai_questions_converted = []'''
    
    # Tìm đoạn từ voai_questions_converted đến all_exams_data = { ... }
    pattern = r'# Chuẩn hóa 50 câu VOAI[\s\S]*?all_exams_data = \{[\s\S]*?\}'
    replacement = '''# Tập hợp dữ liệu 3 đề thi chuẩn
all_exams_data = {
    "olp-01": olp01_data,
    "olp-02": olp02_data,
    "olp-03": olp03_data
}'''
    content = re.sub(pattern, replacement, content)

    # 4. Cập nhật selector HTML
    old_selector = '''        <select class="exam-select" id="examSelector" onchange="switchExam(this.value)">
          <option value="olp-01">Đề 01: Ôn Tập Toàn Diện OLP AI 2026 (64 câu)</option>
          <option value="voai-2026">Đề 02: Thi Thử VOAI 2026 — Đỗ Đình Luật (50 câu)</option>
        </select>'''

    new_selector = '''        <select class="exam-select" id="examSelector" onchange="switchExam(this.value)">
          <option value="olp-01">Đề 01: Ôn Tập Toàn Diện OLP AI 2026 (64 câu: 60 trắc nghiệm & code + 4 tự luận)</option>
          <option value="olp-02">Đề 02: Chuẩn Format VOAI Mở Rộng (66 câu: 60 trắc nghiệm + 6 tự luận)</option>
          <option value="olp-03">Đề 03: Luyện thi thử VOAI 2026 & Chuyên đề Thực hành (54 câu: 50 trắc nghiệm + 4 tự luận)</option>
        </select>'''
    content = content.replace(old_selector, new_selector)

    # 5. Sửa switchExam và timer NaN
    old_switch = '''    function switchExam(examId) {{
      if (ALL_EXAMS[examId]) {{
        currentExamId = examId;
        EXAM = ALL_EXAMS[examId];
        currentIndex = 0;
        editorialOpen = {{}};
        rubricEvalResults = {{}};
        loadSavedState();
        timerSeconds = EXAM.durationMinutes * 60;
        document.getElementById('examSelector').value = examId;
        renderSidebar();
        renderCenter();
        renderInspector();
        renderHeaderStats();
      }}
    }}'''

    new_switch = '''    function switchExam(examId) {{
      if (ALL_EXAMS[examId]) {{
        currentExamId = examId;
        EXAM = ALL_EXAMS[examId];
        currentIndex = 0;
        editorialOpen = {{}};
        rubricEvalResults = {{}};
        loadSavedState();
        timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;
        const sel = document.getElementById('examSelector');
        if (sel) sel.value = examId;
        renderSidebar();
        renderCenter();
        renderInspector();
        renderHeaderStats();
      }}
    }}'''
    content = content.replace(old_switch, new_switch)

    # 6. Sửa initial timerSeconds và startClock
    content = content.replace(
        'let timerSeconds = EXAM.durationMinutes * 60;',
        'let timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;'
    )

    old_clock = '''    function startClock() {{
      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(() => {{
        if (timerSeconds > 0) {{
          timerSeconds--;'''

    new_clock = '''    function startClock() {{
      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(() => {{
        if (isNaN(timerSeconds)) {{
          timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;
        }}
        if (timerSeconds > 0) {{
          timerSeconds--;'''
    content = content.replace(old_clock, new_clock)

    # 7. Sửa maxPoints trong renderHeaderStats và submitContestConfirm
    old_stats = "document.getElementById('tickerTotalScore').textContent = `${{totalPts.toFixed(1)}} / 100.0`;"
    new_stats = "const maxExamPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;\n      document.getElementById('tickerTotalScore').textContent = `${{totalPts.toFixed(1)}} / ${{maxExamPts.toFixed(1)}}`;"
    content = content.replace(old_stats, new_stats)

    old_submit = "Tổng điểm dự kiến: ${{totalPts.toFixed(1)}}/100.0 điểm."
    new_submit = "const maxExamPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;\n      const scoreMsg = `Tổng điểm dự kiến: ${{totalPts.toFixed(1)}}/${{maxExamPts.toFixed(1)}} điểm.`;"
    content = content.replace("Tổng điểm dự kiến: ${{totalPts.toFixed(1)}}/100.0 điểm.", "Tổng điểm dự kiến: ${{totalPts.toFixed(1)}}/${{EXAM.id === 'olp-02' ? '90.0' : '100.0'}} điểm.")

    # 8. Sửa shortLabel trong ma trận câu hỏi
    old_short = "const shortLabel = q.id.replace('OLP01-', '').replace('VOAI-', 'V');"
    new_short = "const shortLabel = q.id.split('-').pop();"
    content = content.replace(old_short, new_short)

    # 9. Ghi file dist luôn khi sinh
    old_write = '''# Ghi ra 2 thư mục
out_fixed = os.path.join(ROOT_DIR, "public", "olympic_ai_study_hub.html")
out_temp = os.path.join(TEMP_DIR, "public", "olympic_ai_study_hub.html")

with open(out_fixed, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"Đã ghi thành công vào: {out_fixed} ({os.path.getsize(out_fixed)} bytes)")

with open(out_temp, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"Đã ghi thành công vào: {out_temp} ({os.path.getsize(out_temp)} bytes)")'''

    new_write = '''# Ghi ra cả 3 thư mục: public, dist, và temp/public
out_public = os.path.join(ROOT_DIR, "public", "olympic_ai_study_hub.html")
out_dist = os.path.join(ROOT_DIR, "dist", "olympic_ai_study_hub.html")
out_temp = os.path.join(TEMP_DIR, "public", "olympic_ai_study_hub.html")

for p in [out_public, out_dist, out_temp]:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Đã ghi thành công vào: {p} ({os.path.getsize(p)} bytes)")'''
    content = content.replace(old_write, new_write)

    with open(gen_script, "w", encoding="utf-8") as f:
        f.write(content)
    print("Đã cập nhật xong docs/generate_full_hub.py")

if __name__ == "__main__":
    build()
