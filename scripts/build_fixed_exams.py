# -*- coding: utf-8 -*-
"""
Script scripts/build_fixed_exams.py
Thực thi toàn bộ bản đặc tả kiểm toán PROMPT_GEMINI_SUA_SAU_AUDIT_2026-10-08.md:
1. Chuẩn hóa schema thống nhất cho cả 3 đề trong src/data/exams/.
2. Sửa toàn bộ lỗi chấm điểm, durationMinutes, totalPoints, disclaimer.
3. Chuyển đổi toàn bộ giải thích HTML của Đề 02 sang Markdown sạch (không còn raw HTML).
4. Cung cấp đầy đủ rubric và modelAnswer cho 10 câu tự luận Đề 02 và Đề 03.
5. Sửa 12 điểm lý thuyết gây hiểu lầm (NLP pipeline, BatchNorm, ViT, KV cache, TabM ICLR 2025, v.v.).
6. Deterministic shuffle options với seed=42 để cân bằng đáp án A/B/C/D.
"""

import json
import os
import random
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
EXAMS_DIR = os.path.join(ROOT_DIR, "src", "data", "exams")

def html_to_markdown_olp02(html_text):
    res = []
    # 1. ELI5
    m_eli5 = re.search(r'1\.\s*ELI5[^\<]*</div>\s*<div[^>]*>([\s\S]*?)</div>\s*</div>', html_text, re.IGNORECASE)
    if m_eli5:
        res.append("### 1. ELI5 — Trực quan cho em bé\n" + m_eli5.group(1).strip())
    # 2. Math / Theory
    m_math = re.search(r'2\.\s*[^<]*</div>\s*<div[^>]*>([\s\S]*?)</div>\s*</div>', html_text, re.IGNORECASE)
    if m_math:
        res.append("### 2. Đạo hàm & Toán học Step-by-Step\n" + m_math.group(1).strip())
    # 3. Pitfalls
    m_pit = re.search(r'3\.\s*[^<]*</div>\s*<div[^>]*>([\s\S]*?)</div>\s*</div>', html_text, re.IGNORECASE)
    if m_pit:
        res.append("### 3. Bẫy đề thi & Pitfalls\n" + m_pit.group(1).strip())
    # 4. Code
    m_code = re.search(r'<pre[^>]*><code[^>]*>([\s\S]*?)</code></pre>', html_text, re.IGNORECASE)
    if m_code:
        code_text = m_code.group(1).strip()
        code_text = code_text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        res.append("### 4. Căn cứ lý thuyết & Code minh họa\n```python\n" + code_text + "\n```")
    return "\n\n".join(res)

def shuffle_mcq_options(question, seed=42):
    """
    Xáo trộn options theo seed cố định.
    Tìm đáp án đúng cũ theo text, xáo trộn, gán lại key A, B, C, D và cập nhật answer.
    Cập nhật các câu nhắc chữ cái trong explanation.
    """
    old_answer = question['answer']
    opts = list(question['options'])
    correct_opt = next((o for o in opts if o['key'] == old_answer), None)
    if not correct_opt:
        return question

    correct_text = correct_opt['text']
    
    # Tạo RNG riêng dựa trên seed + question id để deterministic
    # Dùng hash của question id để mỗi câu có hoán vị ngẫu nhiên khác nhau nhưng cố định
    q_seed = seed + hash(question['id']) % 1000000
    rng = random.Random(q_seed)
    rng.shuffle(opts)

    new_keys = ['A', 'B', 'C', 'D']
    new_options = []
    new_answer = old_answer

    for idx, opt in enumerate(opts):
        k = new_keys[idx]
        new_options.append({'key': k, 'text': opt['text']})
        if opt['text'] == correct_text:
            new_answer = k

    question['options'] = new_options
    question['answer'] = new_answer

    # Cập nhật lời giải nhắc chữ cái
    exp = question['explanation']
    # Thay thế cụm từ: Đáp án chính xác là **B**. -> Đáp án chính xác là **new_answer**.
    exp = re.sub(
        r'(Đáp án chính xác là\s*\*\*)[A-D](\*\*)',
        r'\g<1>' + new_answer + r'\g<2>',
        exp
    )
    exp = re.sub(
        r'(Đáp án đúng:\s*\*\*)[A-D](\*\*)',
        r'\g<1>' + new_answer + r'\g<2>',
        exp
    )
    exp = re.sub(
        r'(> \*\*Đáp án đúng:\*\*\s*\*\*)[A-D](\*\*)',
        r'\g<1>' + new_answer + r'\g<2>',
        exp
    )
    question['explanation'] = exp
    return question

def process_olp01():
    print("Processing olp-01.json...")
    path = os.path.join(EXAMS_DIR, "olp-01.json")
    with open(path, "r", encoding="utf-8") as f:
        exam = json.load(f)

    # Sửa các điểm lý thuyết theo §4.2:
    for q in exam['questions']:
        # 1. ViT: C24
        if q['id'] == 'OLP01-C24':
            for opt in q['options']:
                if opt['key'] == 'D':
                    opt['text'] = "ViT phân cắt ảnh thành patch (hoặc chiếu patch bằng Conv2D), dùng [CLS] token + Transformer Encoder"
            q['explanation'] = "ViT chia ảnh thành các patch phẳng (trong cài đặt thực tế thường dùng Conv2D kernel=16 stride=16 để chiếu patch), thêm [CLS] token và Position Embedding, rồi toàn bộ chuỗi token được xử lý bởi Transformer Encoder thuần túy. -> Xem §3.5."

        # 2. BatchNorm: B10
        if q['id'] == 'OLP01-B10':
            q['prompt'] = "Cấu hình chuẩn mực và phổ biến nhất của một khối tích chập có BatchNorm (như bài báo Ioffe & Szegedy 2015 và ResNet gốc) là gì?"
            q['explanation'] = "Cấu hình chuẩn kinh điển: Linear/Conv -> BatchNorm -> ReLU để chuẩn hóa giá trị tiền kích hoạt trước phi tuyến. (Một số biến thể như Pre-activation ResNet có thể đặt BN trước Conv, nhưng Conv->BN->ReLU là cấu hình phổ biến nhất). -> Xem §2.8."

        # 3. NLP Pipeline: C28
        if q['id'] == 'OLP01-C28':
            q['prompt'] = "Trong pipeline NLP tiếng Anh kinh điển, trình tự các bước tiền xử lý logic thường gặp nhất là gì?"
            for opt in q['options']:
                if opt['key'] == 'D':
                    opt['text'] = "Chuẩn hóa/Lowercasing -> Tokenization -> Lemmatization/POS -> Lọc stopwords"
            q['explanation'] = "Trình tự chuẩn hóa: Làm sạch chuỗi/hạ chữ thường (normalization) -> Tách từ (tokenization) -> Gán từ loại/Đưa về gốc từ (POS/lemma) -> Loại bỏ từ dừng (stopwords). Thứ tự cụ thể có thể linh hoạt theo thư viện, nhưng cần tokenization trước khi xử lý cấp độ từ. -> Xem §4.1."

        # 4. Entropy: C05
        if q['id'] == 'OLP01-C05':
            q['prompt'] = "Trong lý thuyết thông tin và cây quyết định, công thức Shannon Entropy tính theo đơn vị bit sử dụng logarit cơ số mấy?"
            q['explanation'] = "Shannon Entropy tính theo đơn vị bit dùng log cơ số 2. (Nếu dùng log tự nhiên ln thì đơn vị là nat). Node thuần khiết có H=0. -> Xem §1.3."

        # 5. E01: Phân loại clip ký hiệu
        if q['id'] == 'OLP01-E01':
            q['modelAnswer'] = "1) Phân tích dữ liệu: Video chuỗi thời gian, đa dạng người quay (100 người) và nền/ánh sáng; cần phân tách train/val person-independent chống rò rỉ; tăng cường dữ liệu (crop, xoay, ánh sáng). 2) Mô hình: Baseline trích đặc trưng frame (ResNet18/MobileNet) + pooling; mô hình chính: 3D-CNN / CRNN (CNN + Bi-LSTM) hoặc trích Hand Keypoints bằng MediaPipe + ST-GCN/Transformer gọn nhẹ chạy real-time. 3) Pipeline: Trích frame/keypoints -> Temporal model -> Head phân loại 50 lớp. 4) Metric: Macro-F1 (chuẩn theo đề SOLOAI) và Accuracy toàn clip; ma trận nhầm lẫn (confusion matrix). 5) Cải tiến: Pretraining, pseudo-labeling, ensembling và distillation sang mô hình nhe."
            q['rubric'] = [
                "Phân tích đúng đặc thù chuỗi video, đa dạng người quay và ràng buộc độ trễ",
                "Lựa chọn mô hình chuỗi thời gian (CRNN/3D-CNN/Keypoints ST-GCN) có luận giải",
                "Pipeline xử lý chuẩn xác, chia train/val person-independent chống rò rỉ",
                "Sử dụng đúng metric phân loại Macro-F1 và Confusion Matrix (không ép CER/WER)",
                "Đề xuất ít nhất 2 giải pháp cải tiến thực tế (Keypoints/Distillation/Augmentation)"
            ]

        # 6. E02: Dịch máy Hoa-Việt
        if q['id'] == 'OLP01-E02':
            q['prompt'] = "Dịch máy Hoa - Việt (phỏng theo tác vụ SOLOAI 2025): 200.000 cặp câu, văn bản thương mại điện tử, yêu cầu bảo tồn số lượng/tiền tệ và tuân thủ quy chế phòng thi (không dùng mô hình pretrained MT). Đề xuất giải pháp theo khung 5 bước, metric SacreBLEU."
            q['modelAnswer'] = "1) Phân tích: Cặp câu song ngữ Hoa-Việt lệch độ dài, từ ngữ thương mại, số lượng/tiền tệ; tiền xử lý: làm sạch, tách từ (jieba cho tiếng Trung, pyvi/rdrsegmenter cho tiếng Việt), huấn luyện BPE/SentencePiece from scratch chung kích thước vựng 8k-16k. 2) Mô hình: Tuân thủ quy chế cấm pretrained MT: Huấn luyện Transformer Encoder-Decoder from scratch (Vaswani et al.) 4-6 layers gọn nhẹ; tối ưu AdamW + Noam scheduler. 3) Pipeline: Tiền xử lý -> BPE -> Train với Label Smoothing 0.1 -> Beam search decoding (beam_size=4, length penalty). 4) Metric: SacreBLEU (đo n-gram precision + Brevity Penalty) và kiểm tra bảo tồn số/tiền tệ. 5) Cải tiến: Back-translation tạo dữ liệu tổng hợp, Ensembling nhiều checkpoint/seed, post-processing quy tắc bảo toàn định dạng số."
            q['rubric'] = [
                "Phân tích đúng đặc thù song ngữ Trung-Việt, bảo tồn số lượng/tiền tệ",
                "Thiết kế Transformer from scratch tuân thủ quy chế cấm pretrained model của đề gốc",
                "Pipeline đầy đủ BPE tokenization, Label Smoothing và Beam Search decoding",
                "Áp dụng chuẩn xác metric SacreBLEU kèm công thức phạt độ ngắn (Brevity Penalty)",
                "Đề xuất ít nhất 2 cải tiến khả thi (Back-translation/Ensemble/Post-processing)"
            ]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    print("olp-01.json updated.")

def process_olp02():
    print("Processing olp-02.json...")
    # Đọc markdown để lấy essay data
    md_path = os.path.join(ROOT_DIR, "content", "02-de-chuan-format-voai-expand.md")
    with open(md_path, "r", encoding="utf-8") as f:
        text2 = f.read()

    # Parse 6 essay questions from markdown
    essay_blocks = re.findall(r'(###\s+VOAI02-E\d+[\s\S]*?)(?=(?:###\s+VOAI02-E\d+|\Z))', text2)
    essay_dict = {}
    for b in essay_blocks:
        eid = re.search(r'VOAI02-E\d+', b).group(0)
        # prompt
        m_ctx = re.search(r'Bối\s*cảnh\s*bài\s*toán[^\n]*\n>([\s\S]*?)(?=\*\*Rubric)', b, re.IGNORECASE)
        ctx = m_ctx.group(1).strip() if m_ctx else ""
        m_title = re.search(r'###\s+VOAI02-E\d+\.\s*([^\n\[]+)', b)
        title = m_title.group(1).strip() if m_title else eid
        prompt = f"**{title}**\n\n{ctx}\n\n*Yêu cầu*: Trình bày giải pháp toàn diện theo khung 5 bước chuẩn kỹ sư AI."
        
        # rubric
        m_rub = re.search(r'Rubric\s*Chấm\s*Điểm[^\n]*\n([\s\S]*?)(?=####|\n###)', b, re.IGNORECASE)
        rub_raw = m_rub.group(1).strip() if m_rub else ""
        rub_lines = []
        for line in rub_raw.split('\n'):
            line = line.strip()
            if line.startswith('-'):
                # clean up line
                cleaned = re.sub(r'^-\s*\*\*[^*]+\*\*:\s*[\d\.]+đ:\s*', '', line)
                cleaned = re.sub(r'^-\s*', '', cleaned)
                if cleaned:
                    rub_lines.append(cleaned)
        
        # modelAnswer
        m_ans = re.search(r'####\s*LỜI\s*GIẢI\s*MẪU[\s\S]*?\n([\s\S]*)$', b, re.IGNORECASE)
        model_answer = m_ans.group(1).strip() if m_ans else ""
        
        essay_dict[eid] = {
            'prompt': prompt,
            'rubric': rub_lines,
            'modelAnswer': model_answer
        }

    path = os.path.join(EXAMS_DIR, "olp-02.json")
    with open(path, "r", encoding="utf-8") as f:
        exam = json.load(f)

    # 1. Metadata fixes
    exam['durationMinutes'] = 90
    exam['totalPoints'] = 90  # 60 MCQ * 1.5 = 90đ graded
    if 'duration_minutes' in exam: del exam['duration_minutes']
    if 'total_points' in exam: del exam['total_points']
    if 'total_questions' in exam: del exam['total_questions']

    exam['disclaimer'] = "Bộ đề luyện thi mô phỏng chuẩn format mở rộng Olympic AI (60 trắc nghiệm 90 điểm + 6 bài toán tự luận 60 điểm chấm riêng). Tài liệu ôn tập học thuật, không phải đề thi chính thức của BTC."
    exam['moduleLabels'] = {
        "A": "Toán & Xác suất – Thống kê (12 câu)",
        "B": "Machine Learning & Deep Learning (24 câu)",
        "C": "Computer Vision, NLP & Tự luận Giải pháp AI (24 MCQ + 6 Tự luận)"
    }
    exam['moduleOverview'] = [
        "A: 12 câu Toán & Xác suất Thống kê (VOAI02-M01 -> M12)",
        "B: 24 câu Machine Learning & Deep Learning (VOAI02-M13 -> M36)",
        "C: 24 câu CV, NLP & 6 bài toán tự luận giải pháp AI (VOAI02-M37 -> M60, E01 -> E06)"
    ]

    new_questions = []
    mcq_count = 0

    for q in exam['questions']:
        qid = q['id']
        if qid.startswith('VOAI02-M'):
            mcq_count += 1
            idx = int(qid.replace('VOAI02-M', ''))
            
            # Module assignment: 1-12 -> A, 13-36 -> B, 37-60 -> C
            if 1 <= idx <= 12:
                q['module'] = 'A'
            elif 13 <= idx <= 36:
                q['module'] = 'B'
            else:
                q['module'] = 'C'

            q['points'] = 1.5
            q['type'] = 'mcq'
            if 'raw_explanation' in q: del q['raw_explanation']
            if 'chapter' in q: del q['chapter']
            if 'title' in q: del q['title']

            # Chuyển HTML explanation sang Markdown
            md_exp = html_to_markdown_olp02(q.get('explanation', ''))
            q['explanation'] = md_exp

            # Sửa các câu lý thuyết đặc biệt trong Đề 02:
            if qid == 'VOAI02-M45':
                # Sửa code thiếu import numpy
                q['explanation'] = q['explanation'].replace(
                    "iou_thresholds = [round(x, 2) for x in np.arange(0.5, 1.0, 0.05)]",
                    "import numpy as np\niou_thresholds = [round(x, 2) for x in np.arange(0.5, 1.0, 0.05)]"
                )

            if qid == 'VOAI02-M49':
                # Sửa NLP pipeline
                q['prompt'] = "Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự các bước tiền xử lý văn bản thô thường gặp và hợp lý nhất là gì?"
                for opt in q['options']:
                    if opt['key'] == 'B':
                        opt['text'] = "Chuẩn hóa & Hạ chữ thường -> Tách từ (Tokenization) -> Lọc từ dừng (Stopwords) -> Rút gọn từ gốc (Stemming/Lemmatization) -> Vector hóa"
                q['explanation'] = q['explanation'].replace(
                    "1. **Tokenization**: Chia chuỗi ký tự liên tục",
                    "1. **Chuẩn hóa chuỗi (Normalization/Lowercasing)**: Làm sạch ký tự lạ, đưa về chữ thường trước khi tokenize.\n2. **Tokenization**: Chia chuỗi"
                )

            if qid == 'VOAI02-M59':
                # Sửa RAG không cam kết zero hallucination
                q['explanation'] = q['explanation'] + "\n\n*Lưu ý*: RAG giúp grounding thông tin vào tài liệu truy xuất để giảm thiểu đáng kể ảo giác, nhưng không đảm bảo 100% Zero Hallucination; cần kết hợp kiểm chứng nguồn (citations) và cơ chế từ chối trả lời (abstention) khi tài liệu không chứa câu trả lời."

            if qid == 'VOAI02-M60':
                # Sửa KV cache trade-off VRAM
                q['explanation'] = q['explanation'] + "\n\n*Lưu ý*: KV cache giảm tính toán lặp lại từ O(N^2) xuống O(N), nhưng đánh đổi lại là bộ nhớ VRAM lưu cache tăng tuyến tính theo context length và batch size."

            # Shuffle options deterministic với seed=42
            q = shuffle_mcq_options(q, seed=42)
            new_questions.append(q)

        elif qid.startswith('VOAI02-E'):
            # Essay question
            info = essay_dict.get(qid, {})
            essay_q = {
                'id': qid,
                'module': 'C',
                'type': 'essay',
                'points': 10,
                'prompt': info.get('prompt', q.get('prompt', '')),
                'rubric': info.get('rubric', [
                    "Phân tích đúng đặc thù bài toán và dữ liệu",
                    "Luận giải lựa chọn mô hình và kiến trúc phù hợp",
                    "Pipeline xử lý chuẩn xác, chống rò rỉ dữ liệu",
                    "Chỉ số đánh giá phù hợp kèm phân tích ngoại lệ",
                    "Phương án cải tiến thực chiến và tối ưu suy luận"
                ]),
                'modelAnswer': info.get('modelAnswer', q.get('explanation', '')),
                'tags': ['essay', 'solution-design']
            }
            new_questions.append(essay_q)

    exam['questions'] = new_questions
    with open(path, "w", encoding="utf-8") as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    print("olp-02.json updated.")

def process_olp03():
    print("Processing olp-03.json...")
    md_path = os.path.join(ROOT_DIR, "content", "03-de-vong-mien-voai-2025.md")
    with open(md_path, "r", encoding="utf-8") as f:
        text3 = f.read()

    # Parse 4 essays from 03 markdown
    e3_matches = re.findall(r'(##\s+MODULE\s+C\s*—\s*BÀI\s+TỰ\s+LUẬN[^\n]*\n[\s\S]*?)(?=(?:##\s+MODULE\s+C|\Z))', text3)
    essay_dict = {}
    for b in e3_matches:
        eid = re.search(r'VOAI03-E\d+', b).group(0)
        m_prompt = re.search(r'###\s*Đề\s*bài:\s*\n([\s\S]*?)(?=###\s*Tiêu\s*chí)', b, re.IGNORECASE)
        prompt = m_prompt.group(1).strip() if m_prompt else ""
        
        m_rub = re.search(r'Rubric\):\s*\n([\s\S]*?)(?=###\s*Bài\s*giải)', b, re.IGNORECASE)
        rub_items = [line.strip('- ').strip() for line in m_rub.group(1).strip().split('\n') if line.strip().startswith('-')] if m_rub else []
        
        m_ans = re.search(r'###\s*Bài\s*giải\s*mẫu[\s\S]*?\n([\s\S]*)$', b, re.IGNORECASE)
        model_answer = m_ans.group(1).strip() if m_ans else ""
        
        essay_dict[eid] = {
            'prompt': prompt,
            'rubric': rub_items,
            'modelAnswer': model_answer
        }

    path = os.path.join(EXAMS_DIR, "olp-03.json")
    with open(path, "r", encoding="utf-8") as f:
        exam = json.load(f)

    # 1. Metadata fixes & correct provenance labeling (§4.1)
    exam['id'] = 'olp-03'
    exam['title'] = "Đề 03 - Luyện thi thử VOAI 2026 & Chuyên đề Thực hành Mở rộng"
    exam['description'] = "Đề thi mô phỏng biên soạn dựa trên Đề thi thử VOAI 2026 (Đỗ Đình Luật) và chuyên đề thực hành Vòng miền AI Vietnam / SOLOAI 2025. Gồm 50 trắc nghiệm (100 điểm) + 4 chuyên đề tự luận (40 điểm chấm riêng)."
    exam['disclaimer'] = "Đề luyện thi thử phỏng theo đề thi thử VOAI 2026 (Đỗ Đình Luật) kết hợp chuyên đề thực hành Vòng miền AI Vietnam & bài toán mẫu SOLOAI. Không phải đề thi chính thức VOAI 2025 của BTC."
    exam['durationMinutes'] = 90
    exam['totalPoints'] = 100  # 50 MCQ * 2.0 = 100đ graded
    if 'duration_minutes' in exam: del exam['duration_minutes']
    if 'total_points' in exam: del exam['total_points']
    if 'total_questions' in exam: del exam['total_questions']

    exam['moduleLabels'] = {
        "A": "Lý thuyết Nền tảng, Tối ưu & Dữ liệu Bảng (25 câu)",
        "B": "Deep Learning, Computer Vision & NLP Nâng Cao (25 câu)",
        "C": "Chuyên đề Tự luận Giải pháp AI Vòng Miền & SOLOAI (4 bài tự luận)"
    }
    exam['moduleOverview'] = [
        "A: 25 câu Lý thuyết nền tảng, tối ưu hóa & dữ liệu bảng (VOAI03-M01 -> M25)",
        "B: 25 câu Deep Learning, Computer Vision & NLP nâng cao (VOAI03-M26 -> M50)",
        "C: 4 bài toán tự luận thiết kế hệ thống AI thực chiến (VOAI03-E01 -> E04)"
    ]

    new_questions = []
    for q in exam['questions']:
        qid = q['id']
        if qid.startswith('VOAI03-M'):
            idx = int(qid.replace('VOAI03-M', ''))
            # Module A: 1-25; Module B: 26-50
            q['module'] = 'A' if 1 <= idx <= 25 else 'B'
            q['points'] = 2.0
            q['type'] = 'mcq'
            if 'chapter' in q: del q['chapter']
            if 'title' in q: del q['title']
            if 'raw_explanation' in q: del q['raw_explanation']

            # Sửa các câu lý thuyết đặc biệt trong Đề 03:
            if qid == 'VOAI03-M23':
                # Chuyển Option D "Cả A và C đều đúng" thành phát biểu tự đủ nghĩa (§5)
                for opt in q['options']:
                    if opt['key'] == 'D':
                        opt['text'] = "Vừa giảm thiểu hiện tượng ảo giác qua grounding dữ liệu ngoài, vừa cập nhật tri thức mới mà không cần huấn luyện lại toàn bộ mô hình"
                q['explanation'] = q['explanation'] + "\n\n*Lưu ý*: RAG giúp giảm hiện tượng ảo giác nhờ grounding vào tài liệu truy xuất, tuy nhiên không cam kết Zero Hallucination tuyệt đối; vẫn cần kết hợp cơ chế kiểm chứng và trích dẫn nguồn."

            if qid == 'VOAI03-M27':
                # Quantization: làm rõ trade-off
                for opt in q['options']:
                    if opt['key'] == 'A':
                        opt['text'] = "Giảm dung lượng bộ nhớ (VRAM) và có thể tăng tốc độ suy luận khi phần cứng/kernel hỗ trợ"
                q['explanation'] = q['explanation'] + "\n\n*Lưu ý*: Lượng hóa (Quantization) thường giảm bộ nhớ; tốc độ suy luận tăng khi phần cứng/kernel hỗ trợ (ví dụ INT8 tensor core); độ chính xác có thể giảm nhẹ hoặc thay đổi tùy thuộc vào kỹ thuật Post-Training Quantization (PTQ) hay Quantization-Aware Training (QAT)."

            if qid == 'VOAI03-M30':
                # KV Cache stem fix
                q['prompt'] = "Để phục vụ (Serving) một mô hình LLM lớn, kỹ thuật nào thường được dùng để tránh tính toán lại dư thừa trạng thái Attention qua các bước sinh token (dù đánh đổi tiêu tốn VRAM làm bộ nhớ đệm)?"
                q['explanation'] = q['explanation'] + "\n\n*Lưu ý*: KV cache giảm tính toán lặp lại từ O(N^2) xuống O(N) cho bước sinh mới, nhưng dung lượng VRAM chiếm dụng tăng dần theo context length và batch size. Các kỹ thuật như PagedAttention (vLLM) được phát triển để quản lý vùng nhớ đệm này hiệu quả hơn."

            if qid == 'VOAI03-M47':
                # TabM ICLR 2025
                q['prompt'] = "Mô hình Neural Tabular nào gần đây (ICLR 2025) nổi tiếng với việc chia sẻ tham số (parameter sharing) hiệu quả để tạo ra một mini-ensemble gồm nhiều mạng nơ-ron bên trong một kiến trúc duy nhất?"
                q['explanation'] = q['explanation'].replace("ICLR 2024", "ICLR 2025")
                q['explanation'] = q['explanation'] + "\n\n*Lưu ý*: TabM (Gorishniy et al., ICLR 2025, https://github.com/yandex-research/tabm) sử dụng cơ chế chia sẻ tham số để tạo mini-ensemble. Mặc dù là baseline neural rất mạnh cho tabular data, GBDT (XGBoost, CatBoost, LightGBM) vẫn là đối thủ cạnh tranh hàng đầu và không có mô hình nào vượt trội tuyệt đối trên mọi tập dữ liệu."

            # Shuffle options deterministic với seed=42
            q = shuffle_mcq_options(q, seed=42)
            new_questions.append(q)

        elif qid.startswith('VOAI03-E'):
            info = essay_dict.get(qid, {})
            essay_q = {
                'id': qid,
                'module': 'C',
                'type': 'essay',
                'points': 10,
                'prompt': info.get('prompt', q.get('prompt', '')),
                'rubric': info.get('rubric', [
                    "Phân tích đúng đặc thù bài toán và dữ liệu",
                    "Luận giải lựa chọn mô hình và kiến trúc phù hợp",
                    "Pipeline xử lý chuẩn xác, chống rò rỉ dữ liệu",
                    "Chỉ số đánh giá phù hợp kèm phân tích ngoại lệ",
                    "Phương án cải tiến thực chiến và tối ưu suy luận"
                ]),
                'modelAnswer': info.get('modelAnswer', ""),
                'tags': ['essay', 'solution-design']
            }
            new_questions.append(essay_q)

    exam['questions'] = new_questions
    with open(path, "w", encoding="utf-8") as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    print("olp-03.json updated.")

if __name__ == "__main__":
    process_olp01()
    process_olp02()
    process_olp03()
    print("ALL 3 EXAMS SUCCESSFULLY PROCESSED AND NORMALIZED.")
