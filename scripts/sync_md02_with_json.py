# -*- coding: utf-8 -*-
"""
scripts/sync_md02_with_json.py
Đồng bộ hóa 60 câu trắc nghiệm trong content/02-de-chuan-format-voai-expand.md
với src/data/exams/olp-02.json (các lựa chọn sau khi shuffle, đáp án đúng và lời giải).
"""

import json
import os
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
MD_PATH = os.path.join(ROOT_DIR, "content", "02-de-chuan-format-voai-expand.md")
JSON_PATH = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-02.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    exam_data = json.load(f)

json_mcqs = {q["id"]: q for q in exam_data["questions"] if q.get("type") == "mcq"}

with open(MD_PATH, "r", encoding="utf-8") as f:
    md_content = f.read()

essay_split = re.search(r'(## PHẦN II:\s*6 BÀI TOÁN TỰ LUẬN[\s\S]*)', md_content)
if not essay_split:
    print("Không tìm thấy phần tự luận trong markdown!")
    exit(1)

essay_part = essay_split.group(1)
mcq_part = md_content[:essay_split.start()]

updated_count = 0

def replace_mcq(m):
    global updated_count
    title_line = m.group(1)
    qid = m.group(2)
    chapter_line = m.group(3)
    if qid not in json_mcqs:
        return m.group(0)
    
    q = json_mcqs[qid]
    options_str = "\n".join([f"- {opt['key']}. {opt['text']}" for opt in q["options"]])
    
    new_block = f"""### {title_line}
{chapter_line}

**Câu hỏi**: {q['prompt']}

{options_str}

**Đáp án đúng**: **{q['answer']}**

#### Lời giải chi tiết:
{q['explanation']}

"""
    updated_count += 1
    return new_block

pattern = r'###\s+((VOAI02-M\d{2})\.[^\n]+)\n(\*[^\n]+\*)\n\n\*\*Câu hỏi\*\*:[\s\S]*?(?=(?:---\s*\n+###\s+VOAI02-M\d{2}|---\s*\n+## PHẦN II|\Z))'

new_mcq_part = re.sub(pattern, replace_mcq, mcq_part)

print(f"Đã cập nhật {updated_count}/60 câu trắc nghiệm trong markdown.")

new_full_md = new_mcq_part + essay_part
with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(new_full_md)

print("Hoàn tất ghi file markdown Đề 02!")
