# -*- coding: utf-8 -*-
"""
scripts/fix_section_refs.py
Sửa các tham chiếu § trong các đề thi khớp với heading thực tế trong content/01-ly-thuyet-olp-ai.md:
- §4.1: Pipeline Tiền Xử Lý Văn Bản Chuẩn
- §4.2: Các Phương Pháp Biểu Diễn Từ (Word Representations)
- §4.3: Cosine Similarity
- §4.5: Kiến trúc Transformer (Vaswani et al., 2017)
- §4.6: So sánh BERT vs GPT
- §4.7: Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity
- §3.1: Lớp Convolution & Công thức Kích thước Đầu ra
- §3.2: Pooling & Trường Thụ Cảm (Receptive Field)
- §3.3: Các Kiến trúc CNN Kinh Điển
- Sửa dấu chấm thừa ở VOAI02-M29 (§2.10.) và VOAI03-M16 (§3.1.).
"""

import json
import re

# 1. Sửa olp-02.json
with open('src/data/exams/olp-02.json', 'r', encoding='utf-8') as f:
    e2 = json.load(f)

for q in e2['questions']:
    if q['id'] == 'VOAI02-M29':
        q['explanation'] = q['explanation'].replace('§2.10.', '§2.10')

with open('src/data/exams/olp-02.json', 'w', encoding='utf-8') as f:
    json.dump(e2, f, ensure_ascii=False, indent=2)

# 2. Sửa olp-03.json
with open('src/data/exams/olp-03.json', 'r', encoding='utf-8') as f:
    e3 = json.load(f)

for q in e3['questions']:
    if q['id'] == 'VOAI03-M16':
        q['explanation'] = q['explanation'].replace('§3.1.', '§3.1')

with open('src/data/exams/olp-03.json', 'w', encoding='utf-8') as f:
    json.dump(e3, f, ensure_ascii=False, indent=2)

# 3. Sửa olp-05.json
with open('src/data/exams/olp-05.json', 'r', encoding='utf-8') as f:
    e5 = json.load(f)

for q in e5['questions']:
    exp = q['explanation']
    # NLP-01..10
    exp = exp.replace('§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi', '§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn')
    # NLP-11..25
    exp = exp.replace('§4.2 Cơ chế Attention & Transformer', '§4.5 Kiến trúc Transformer (Vaswani et al., 2017)')
    # NLP-26..35
    exp = exp.replace('§4.3 Mô hình ngôn ngữ lớn (LLM) & Ứng dụng SOTA', '§4.6 So sánh BERT vs GPT')
    # CV-01..15
    exp = exp.replace('§3.1 Mạng nơ-ron tích chập (CNN) & Thao tác không gian', '§3.1 Lớp Convolution & Công thức Kích thước Đầu ra')
    # CV-16..35
    exp = exp.replace('§3.1 Công thức chiều đặc trưng, Pooling & Receptive Field', '§3.2 Pooling & Trường Thụ Cảm (Receptive Field)')
    # CV-36..55
    exp = exp.replace('§3.3 Kiến trúc CV SOTA: ResNet, Inception, MobileNet', '§3.3 Các Kiến trúc CNN Kinh Điển')
    
    # Riêng CV-40: câu tính số tham số lớp tích chập
    if q['id'] == 'SKILL-CV-40':
        exp = exp.replace('§3.3 Các Kiến trúc CNN Kinh Điển', '§3.1 Lớp Convolution & Công thức Kích thước Đầu ra')
        
    q['explanation'] = exp

with open('src/data/exams/olp-05.json', 'w', encoding='utf-8') as f:
    json.dump(e5, f, ensure_ascii=False, indent=2)

print("Đã hoàn tất chuẩn hóa các tham chiếu § theo heading thực tế!")
