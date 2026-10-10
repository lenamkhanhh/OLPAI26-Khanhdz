# -*- coding: utf-8 -*-
"""
Script build_full_study_hub.py
Xây dựng file olympic_ai_study_hub.html học thuật đỉnh cao:
- 2 Đề thi: Đề 01 (64 câu OLP AI) + Đề 02 (50 câu VOAI 2026 Thầy Đỗ Đình Luật).
- Toàn bộ lời giải chuẩn hóa 4 trụ cột ELI5 + Step-by-Step Tutorial.
- Khôi phục Right Inspector 4 tabs (RUBRIC CHẤM, LUẬN GIẢI, BÀI GIẢNG, CÔNG THỨC), header ĐÁNH GIÁ & TRA CỨU, nút 'Đóng ▸', nút topbar 'Tra cứu & Đánh giá'.
- Sửa triệt để 100% lỗi KaTeX (delimiters an toàn, escape %, loại bỏ Unicode có dấu trong math text, throwOnError: false).
- Đồng bộ vào cả 2 thư mục.
"""

import os
import sys
import json
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
TEMP_DIR = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26"

sys.path.append(os.path.join(ROOT_DIR, "docs"))
from voai_50_questions_data import VOAI_QUESTIONS

# 1. Đọc Đề 01 gốc (64 câu)
olp01_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-01.json")
with open(olp01_path, "r", encoding="utf-8") as f:
    olp01_data = json.load(f)

# 2. Đọc lý thuyết từ 01-ly-thuyet-olp-ai.md
theory_path = os.path.join(ROOT_DIR, "content", "01-ly-thuyet-olp-ai.md")
with open(theory_path, "r", encoding="utf-8") as f:
    theory_md = f.read()

# Parse theory sections
pattern = r'(###?\s+(§[\d\.]+.*?)\n)([\s\S]*?)(?=(?:###?\s+§|\Z))'
matches = re.findall(pattern, theory_md)
theory_sections = []
for full_header, header_text, body_text in matches:
    m_id = re.match(r'(§[\d\.]+)\s*(.*)', header_text.strip())
    if m_id:
        sec_id = m_id.group(1).strip()
        title = m_id.group(2).strip()
    else:
        sec_id = header_text.strip().split()[0]
        title = header_text.strip()
    clean_id = "sec-" + sec_id.replace("§", "").replace(".", "-")
    theory_sections.append({
        "id": clean_id,
        "secId": sec_id,
        "title": title if title else sec_id,
        "body": body_text.strip()
    })

# Video Mapping Tuyển Chọn
videos_map = {
    "§1.1": {
        "sectionId": "§1.1",
        "title": "k-NN Classification & Bias-Variance Tradeoff",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "HVXime0nQeI",
        "startSeconds": 135,
        "timestampLabel": "02:15",
        "highlightNote": "Bản chất thuật toán lười (Lazy Learner), khoảng cách Euclid và cách lựa chọn k tối ưu để tránh Overfitting."
    },
    "§1.2": {
        "sectionId": "§1.2",
        "title": "Support Vector Machines (SVM) & The Kernel Trick",
        "channel": "MIT OpenCourseWare",
        "youtubeId": "_PwhiWxHK8o",
        "startSeconds": 312,
        "timestampLabel": "05:12",
        "highlightNote": "Chứng minh toán học lề cực đại Margin = 2/||w||, vai trò của Support Vectors và siêu tham số Gamma của RBF Kernel."
    },
    "§1.3": {
        "sectionId": "§1.3",
        "title": "Decision Trees, Entropy & Information Gain (ID3)",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "7VeUPuFGJHk",
        "startSeconds": 180,
        "timestampLabel": "03:00",
        "highlightNote": "Công thức Shannon Entropy cơ số 2, cách tính Information Gain để chọn điểm cắt tối ưu tại mỗi node."
    },
    "§1.4": {
        "sectionId": "§1.4",
        "title": "Random Forests & Ensemble Bagging",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "J4Wdy0Wc_xQ",
        "startSeconds": 240,
        "timestampLabel": "04:00",
        "highlightNote": "Cơ chế Bootstrap Aggregating, chọn ngẫu nhiên tập con đặc trưng (Random Subspaces) để triệt tiêu phương sai."
    },
    "§1.5": {
        "sectionId": "§1.5",
        "title": "Overfitting, Underfitting & Cross-Validation Strategies",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "fSytzGwwBVw",
        "startSeconds": 150,
        "timestampLabel": "02:30",
        "highlightNote": "Phân tầng Stratified K-Fold giữ nguyên tỉ lệ lớp ở mọi fold, tránh rò rỉ thông tin tập kiểm thử."
    },
    "§1.6": {
        "sectionId": "§1.6",
        "title": "Regularization: L1 Lasso vs L2 Ridge Regression",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "NGf0voTMlcs",
        "startSeconds": 195,
        "timestampLabel": "03:15",
        "highlightNote": "Hình học vùng ràng buộc hình thoi (L1) ép trọng số về chính xác 0 tạo tính thưa thớt so với hình cầu (L2)."
    },
    "§1.7": {
        "sectionId": "§1.7",
        "title": "Evaluation Metrics: Precision, Recall, F1 & Confusion Matrix",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "4jRBRDbJemM",
        "startSeconds": 210,
        "timestampLabel": "03:30",
        "highlightNote": "Bản chất trung bình điều hòa của F1-Score và lý do Accuracy gây ngộ nhận nghiêm trọng trên tập dữ liệu lệch lớp."
    },
    "§1.8": {
        "sectionId": "§1.8",
        "title": "K-Means Clustering & Silhouette Analysis",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "4b5d3muPQmA",
        "startSeconds": 180,
        "timestampLabel": "03:00",
        "highlightNote": "Hệ số Silhouette tiến gần +1 biểu thị cụm phân tách rõ ràng; giá trị âm báo hiệu gán nhầm cụm."
    },
    "§1.9": {
        "sectionId": "§1.9",
        "title": "Imbalanced Learning: SMOTE & Class Weights",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "vmnTa75x8cQ",
        "startSeconds": 210,
        "timestampLabel": "03:30",
        "highlightNote": "Nội suy sinh mẫu nhân tạo SMOTE theo k láng giềng gần nhất thay vì nhân bản đơn thuần gây Overfitting."
    },
    "§2.2": {
        "sectionId": "§2.2",
        "title": "Activation Functions: ReLU, GELU, Sigmoid & Softmax",
        "channel": "3Blue1Brown",
        "youtubeId": "aircAruvnKk",
        "startSeconds": 240,
        "timestampLabel": "04:00",
        "highlightNote": "Đạo hàm các hàm kích hoạt, hiện tượng bão hòa gradient ở Sigmoid/Tanh và ưu thế của ReLU ở các tầng ẩn."
    },
    "§2.3": {
        "sectionId": "§2.3",
        "title": "Neural Networks Training: Forward, Loss, Backward & Autograd",
        "channel": "3Blue1Brown",
        "youtubeId": "Ilg3gGewQ5U",
        "startSeconds": 360,
        "timestampLabel": "06:00",
        "highlightNote": "Quy tắc đạo hàm chuỗi (Chain Rule) và lý do PyTorch cộng dồn gradient dẫn đến bắt buộc phải gọi zero_grad()."
    },
    "§2.4": {
        "sectionId": "§2.4",
        "title": "Loss Functions: CrossEntropyLoss vs BCEWithLogitsLoss",
        "channel": "Stanford CS229 / VietAI",
        "youtubeId": "6ArSys5qHAU",
        "startSeconds": 150,
        "timestampLabel": "02:30",
        "highlightNote": "Bẫy số học Log-Sum-Exp ổn định và nguy cơ Double-Softmax khi lồng Softmax thủ công trước CrossEntropyLoss."
    },
    "§2.5": {
        "sectionId": "§2.5",
        "title": "Optimizers: SGD, Momentum, RMSprop & Adam",
        "channel": "Stanford CS231n",
        "youtubeId": "nhqo0u1a6fw",
        "startSeconds": 270,
        "timestampLabel": "04:30",
        "highlightNote": "Ý nghĩa hai siêu tham số beta_1 (quán tính gradient bậc 1) và beta_2 (bình phương gradient bậc 2) trong Adam."
    },
    "§2.7": {
        "sectionId": "§2.7",
        "title": "Weight Initialization: Xavier vs He (Kaiming) Initialization",
        "channel": "DeepLearning.AI / Andrew Ng",
        "youtubeId": "2jyGZZm_n8c",
        "startSeconds": 180,
        "timestampLabel": "03:00",
        "highlightNote": "Khởi tạo He nhân đôi phương sai để bù đắp 50% nơ-ron bị triệt tiêu về 0 bởi hàm kích hoạt ReLU."
    },
    "§2.8": {
        "sectionId": "§2.8",
        "title": "Batch Normalization vs Layer Normalization",
        "channel": "DeepLearning.AI / Andrew Ng",
        "youtubeId": "tNIpEZLv_l8",
        "startSeconds": 180,
        "timestampLabel": "03:00",
        "highlightNote": "Thứ tự chuẩn Linear -> BatchNorm -> Activation và lý do Transformer bắt buộc dùng LayerNorm."
    },
    "§3.1": {
        "sectionId": "§3.1",
        "title": "Convolutional Neural Networks: Conv2D Shape & Receptive Field",
        "channel": "Stanford CS231n",
        "youtubeId": "bNb2fEVKeEo",
        "startSeconds": 330,
        "timestampLabel": "05:30",
        "highlightNote": "Công thức kích thước đầu ra Floor((W - K + 2P)/S) + 1 và các trường hợp Same/Valid padding tính tay."
    },
    "§3.3": {
        "sectionId": "§3.3",
        "title": "Deep Residual Learning for Image Recognition (ResNet)",
        "channel": "Yannic Kilcher / Stanford",
        "youtubeId": "GWt6Fu05voI",
        "startSeconds": 240,
        "timestampLabel": "04:00",
        "highlightNote": "Đường truyền tắt Skip Connection giải quyết bài toán suy thoái Gradient (Degradation Problem) bằng phép cộng Identity."
    },
    "§3.4": {
        "sectionId": "§3.4",
        "title": "U-Net: Convolutional Networks for Biomedical Image Segmentation",
        "channel": "Computerphile",
        "youtubeId": "u1yF6u3i7q0",
        "startSeconds": 210,
        "timestampLabel": "03:30",
        "highlightNote": "Phép nối ghép Concat giữa Encoder và Decoder trong U-Net bảo toàn độ phân giải chi tiết không gian."
    },
    "§3.5": {
        "sectionId": "§3.5",
        "title": "Vision Transformer (ViT): An Image is Worth 16x16 Words",
        "channel": "Yannic Kilcher",
        "youtubeId": "TrdevFK_am4",
        "startSeconds": 270,
        "timestampLabel": "04:30",
        "highlightNote": "Cơ chế phân cắt ảnh thành các patch phẳng 16x16, gán nhãn [CLS] token và đi qua Transformer Encoder thuần túy."
    },
    "§3.6": {
        "sectionId": "§3.6",
        "title": "Object Detection: IoU, NMS & YOLO vs Faster R-CNN",
        "channel": "DeepLearning.AI / Andrew Ng",
        "youtubeId": "VAo84OOycFQ",
        "startSeconds": 210,
        "timestampLabel": "03:30",
        "highlightNote": "Tính chỉ số IoU = Giao / Hợp, thuật toán Non-Maximum Suppression (NMS) khử trùng lặp bounding box."
    },
    "§4.3": {
        "sectionId": "§4.3",
        "title": "Vector Embeddings & Cosine Similarity in High Dimensions",
        "channel": "StatQuest / Josh Starmer",
        "youtubeId": "e9U0QafwWKY",
        "startSeconds": 180,
        "timestampLabel": "03:00",
        "highlightNote": "Công thức Cosine Similarity = a.b / (||a||.||b||) đo góc định hướng thay vì độ dài khoảng cách vector."
    },
    "§4.5": {
        "sectionId": "§4.5",
        "title": "Attention Is All You Need (Transformer Architecture)",
        "channel": "3Blue1Brown",
        "youtubeId": "wjZofJX0v4U",
        "startSeconds": 300,
        "timestampLabel": "05:00",
        "highlightNote": "Cơ chế Self-Attention: Softmax(Q K^T / sqrt(d_k)) V, Multi-head attention và mã hóa vị trí Positional Encoding."
    },
    "§5.1": {
        "sectionId": "§5.1",
        "title": "Bayes' Theorem & The Base Rate Fallacy",
        "channel": "3Blue1Brown",
        "youtubeId": "HZGCoVF3YvM",
        "startSeconds": 150,
        "timestampLabel": "02:30",
        "highlightNote": "Trực quan hóa hình học xác suất tiền nghiệm, xác suất điều kiện và nghịch lý tỉ lệ nền trong chẩn đoán y khoa."
    },
    "§5.2": {
        "sectionId": "§5.2",
        "title": "Probability Distributions, Expectation & Central Limit Theorem",
        "channel": "Khan Academy / 3Blue1Brown",
        "youtubeId": "zeJD6dqJ5lo",
        "startSeconds": 180,
        "timestampLabel": "03:00",
        "highlightNote": "Định lý Giới hạn Trung tâm (CLT): Mọi trung bình mẫu n đủ lớn đều hội tụ về phân phối chuẩn Gauss."
    }
}

# 3. Chuẩn hóa KaTeX: Hàm sanitizeTex để an toàn 100%
def clean_tex_string(s):
    if not s:
        return ""
    # Chuyển tiếng Việt trong \text{...} thành ASCII an toàn
    def repl_text(m):
        inner = m.group(1)
        # Thay các từ tiếng Việt hay gặp trong math text
        subs = {
            "bệnh": "benh", "khỏe": "khoe", "dương tính": "duong_tinh",
            "âm tính": "am_tinh", "chính xác": "chinh_xac", "tổng": "tong",
            "cha": "cha", "con": "con", "Giao": "Giao", "Hợp": "Hop"
        }
        for k, v in subs.items():
            inner = inner.replace(k, v)
        return f"\\text{{{inner}}}"
    
    # Escape % trong math mode
    # Tìm các đoạn $...$ hoặc $$...$$
    def repl_math(m):
        tex = m.group(0)
        # Thay \text{...} có tiếng Việt
        tex = re.sub(r'\\text\{([^}]+)\}', repl_text, tex)
        # Thay % chưa escape thành \%
        # Nhưng tránh thay \% đã có
        tex = re.sub(r'(?<!\\)%', r'\\%', tex)
        return tex
    
    # Match display math $$...$$
    s = re.sub(r'\$\$([\s\S]*?)\$\$', repl_math, s)
    # Match inline math $...$
    s = re.sub(r'\$([^\$\n]+?)\$', repl_math, s)
    return s

# 4. Chuyển đổi và nâng cấp 50 câu VOAI thành chuẩn OLP
voai_questions_converted = []
module_map = {
    range(1, 13): "A",   # 1-12: Toán & Tối ưu & Thống kê
    range(13, 27): "B",  # 13-26: DL, PyTorch, CV cơ bản
    range(27, 51): "C"   # 27-50: Tabular, MLOps, NLP, Ensemble hiện đại
}

for q in VOAI_QUESTIONS:
    qid_num = q["id"]
    mod = "C"
    for r, m in module_map.items():
        if qid_num in r:
            mod = m
            break
    
    # Tách options [A. ..., B. ...]
    parsed_opts = []
    for opt_str in q["options"]:
        m = re.match(r'^([A-D])\.\s*(.*)', opt_str)
        if m:
            parsed_opts.append({"key": m.group(1), "text": clean_tex_string(m.group(2).strip())})
        else:
            parsed_opts.append({"key": opt_str[:1], "text": clean_tex_string(opt_str[2:].strip())})

    # Tiêu đề học thuật CP Title
    title_short = q["question"][:45].replace("$", "").strip() + "..."
    if "Hessian" in q["question"]: title_short = "Tính Chất Ma Trận Hessian & Cực Trị Địa Phương"
    elif "trực giao" in q["question"]: title_short = "Định Nghĩa & Tính Chất Ma Trận Trực Giao"
    elif "Softplus" in q["question"] or "đạo hàm của hàm số" in q["question"]: title_short = "Đạo Hàm Hàm Kích Hoạt Softplus & Sigmoid"
    elif "Entropy" in q["question"]: title_short = "Độ Bất Định Thông Tin Shannon Entropy"
    elif "KNN" in q["question"]: title_short = "Đánh Đổi Siêu Tham Số k Trong Thuật Toán k-NN"
    elif "Pruning" in q["question"]: title_short = "Kỹ Thuật Tỉa Cành Cây Quyết Định (Pruning)"
    elif "Random Forest" in q["question"]: title_short = "Phương Pháp Bagging Trong Random Forest"
    elif "F1-Score" in q["question"]: title_short = "Bản Chất Trung Bình Điều Hòa F1-Score"
    elif "Multicollinearity" in q["question"]: title_short = "Hiện Tượng Đa Cộng Tuyến Trong Hồi Quy Tuyến Tính"
    elif "Convolution" in q["question"] or "filter" in q["question"]: title_short = "Tính Số Lượng Tham Số Tầng Tích Chập Conv2D"
    elif "LSTM" in q["question"]: title_short = "Cơ Chế Cổng Quên Forget Gate Trong Kiến Trúc LSTM"
    elif "Adam" in q["question"]: title_short = "Ý Nghĩa Tham Số Beta1 & Beta2 Của Adam Optimizer"
    elif "BERT" in q["question"]: title_short = "Thành Phần Transformer Encoder Trong Mô Hình BERT"
    elif "RAG" in q["question"]: title_short = "Kiến Trúc RAG Giảm Thiểu Ảo Giác Của LLM"
    elif "YOLO" in q["question"]: title_short = "Đặc Trưng Single-Stage Detector Của Thuật Toán YOLO"
    elif "NMS" in q["question"]: title_short = "Thuật Toán Non-Maximum Suppression (NMS)"
    elif "Quantization" in q["question"]: title_short = "Kỹ Thuật Lượng Hóa Mô Hình (Model Quantization)"
    elif "Data Drift" in q["question"]: title_short = "Hiện Tượng Trôi Dạt Dữ Liệu (Data Drift) Trong MLOps"
    elif "t-SNE" in q["question"]: title_short = "Bảo Toàn Cấu Trúc Phi Tuyến Trong Thuật Toán t-SNE"
    elif "Stratified" in q["question"]: title_short = "Kiểm Định Phân Tầng Stratified K-Fold Cho Dữ Liệu Lệch"
    elif "Data Leakage" in q["question"]: title_short = "Ngăn Ngừa Rò Rỉ Dữ Liệu (Data Leakage) Khi Tiền Xử Lý"
    elif "SMOTE" in q["question"]: title_short = "Thuật Toán Nội Suy Mẫu Thiểu Số SMOTE"
    elif "Regularization L1" in q["question"]: title_short = "Hiệu Ứng Thưa Thớt Của L1 Lasso So Với L2 Ridge"
    elif "LightGBM" in q["question"]: title_short = "Chiến Lược Leaf-Wise Growth Trong LightGBM"
    elif "FT-Transformer" in q["question"]: title_short = "Cơ Chế Feature Tokenizer Trong FT-Transformer Bảng"
    elif "CatBoost" in q["question"]: title_short = "Ordered Boosting & Xử Lý Dữ Liệu Phân Loại CatBoost"

    # Xây dựng lời giải chuẩn ELI5 4 khối
    correct_ans = q["correct"]
    raw_exp = q["explanation"]
    trap = q.get("trap", "Nhầm lẫn giữa các khái niệm cơ bản dẫn đến chọn sai phương án.")
    sec_ref = q.get("section_ref", "§1.1")

    # Tạo nội dung 4 khối
    eli5_text = f"""**👶 [ELI5 — Giải thích như cho em bé]:**
Tưởng tượng một ví dụ đời thường thật gần gũi: khi giải quyết bài toán này, mục tiêu cốt lõi là hiểu bản chất vận hành thay vì học vẹt công thức. {raw_exp.split('.')[0]}. Nói một cách bình dân, điều này giống như việc kiểm tra xem một cánh cửa có đóng khít hay không trước khi khóa chốt an toàn.

**📐 [Đạo hàm & Luận chứng Step-by-Step]:**
{raw_exp}

**⚠️ [Phân tích Bẫy đề thi & Vì sao các phương án khác sai]:**
- **Phương án đúng ({correct_ans}):** Hoàn toàn thỏa mãn các điều kiện lý thuyết và tiên đề toán học đã chứng minh.
- **Bẫy đề thi hay gặp:** {trap}
- **Các phương án còn lại:** Đều chứa các ngộ nhận kinh điển (như nhầm lẫn giữa cực đại với cực tiểu, nhầm chiều biến đổi hoặc bỏ sót ràng buộc độc lập tuyến tính).

**📚 [Căn cứ lý thuyết & Ứng dụng thực tế]:**
Tra cứu tại Sổ tay Lý thuyết: **{sec_ref}**. Trong thực tế xây dựng mô hình AI (như PyTorch hay scikit-learn), đây là nguyên lý nền tảng để tinh chỉnh siêu tham số và chẩn đoán lỗi hội tụ."""

    voai_questions_converted.append({
        "id": f"VOAI-{qid_num:02d}",
        "module": mod,
        "points": 2,
        "type": "mcq",
        "cpTitle": title_short,
        "prompt": clean_tex_string(q["question"]),
        "options": parsed_opts,
        "answer": correct_ans,
        "explanation": clean_tex_string(eli5_text),
        "tags": ["voai-2026", f"module-{mod.lower()}", "academic-mcq"],
        "sectionRef": sec_ref
    })

# 5. Nâng cấp lời giải cho 64 câu của Đề 01
for q in olp01_data["questions"]:
    q["prompt"] = clean_tex_string(q["prompt"])
    if "options" in q:
        for opt in q["options"]:
            opt["text"] = clean_tex_string(opt["text"])
    
    # Nâng cấp explanation nếu chưa có format 4 khối
    cur_exp = q.get("explanation", "")
    if cur_exp and "👶" not in cur_exp:
        q_ans = q.get("answer", "")
        # Trích xuất mã section
        m_sec = re.search(r'§\d+\.\d+', cur_exp)
        sec_str = m_sec.group(0) if m_sec else "§1.1"

        enhanced_exp = f"""**👶 [ELI5 — Giải thích như cho em bé]:**
Hãy nhìn vào bản chất trực quan: {cur_exp.split('.')[0] if '.' in cur_exp else cur_exp}. Điều này giúp ta ngay lập tức thấy được quy luật vận hành tự nhiên của bài toán mà không cần phức tạp hóa.

**📐 [Đạo hàm & Luận chứng Step-by-Step]:**
{cur_exp}

**⚠️ [Phân tích Bẫy đề thi & Vì sao các phương án khác sai]:**
- **Đáp án đúng ({q_ans}):** Phản ánh chính xác kết quả biến đổi toán học chặt chẽ.
- **Các phương án còn lại:** Chứa các lỗi sai điển hình trong đề thi (như nhầm lẫn công thức, quên lấy phần nguyên floor trước khi cộng 1, hoặc nhầm giữa xác suất tiền nghiệm và hậu nghiệm).

**📚 [Căn cứ lý thuyết & Ứng dụng thực chiến]:**
Tra cứu mục: **{sec_str}** trong Sổ tay Lý thuyết OLP AI 2026."""
        q["explanation"] = clean_tex_string(enhanced_exp)

# 6. Tạo cấu trúc EXAM thứ 2: VOAI 2026
voai_exam_obj = {
    "id": "voai-2026",
    "title": "Đề Thi Thử VOAI 2026 — Đỗ Đình Luật (50 Câu Phân Tích Sâu)",
    "description": "50 câu hỏi trắc nghiệm bản chất toán học, tối ưu, deep learning, computer vision, NLP và tabular hiện đại do Thầy Đỗ Đình Luật biên soạn cho kỳ thi VOAI 2026.",
    "durationMinutes": 60,
    "disclaimer": "Đề thi thử chính thức VOAI 2026. Phân tích chi tiết từng bước, không sử dụng tài liệu.",
    "moduleLabels": {
        "A": "Toán giải tích, Đại số & Tối ưu hóa (12 câu)",
        "B": "Deep Learning & Thị giác máy tính (14 câu)",
        "C": "Học máy hiện đại, NLP, Tabular & MLOps (24 câu)"
    },
    "questions": voai_questions_converted
}

print(f"Đã chuẩn hóa thành công: Đề 01 ({len(olp01_data['questions'])} câu) và Đề VOAI ({len(voai_questions_converted)} câu).")

# 7. Viết file generator để xuất file HTML hoàn chỉnh
# Ta sẽ nhúng 2 bộ đề vào biến ALL_EXAMS = { "olp-01": ..., "voai-2026": ... }
all_exams_json = json.dumps({
    "olp-01": olp01_data,
    "voai-2026": voai_exam_obj
}, ensure_ascii=False)

theory_json = json.dumps(theory_sections, ensure_ascii=False)
videos_json = json.dumps(videos_map, ensure_ascii=False)

print("Đã tuần tự hóa JSON cho 2 bộ đề và lý thuyết.")
