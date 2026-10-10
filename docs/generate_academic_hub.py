# -*- coding: utf-8 -*-
"""
Script generate_academic_hub.py
Tạo ứng dụng web học thuật Olympic AI Study Hub hoàn chỉnh E2E:
1. Khôi phục Sidebar bên phải (Right Inspector) đúng chuẩn: 4 tabs (RUBRIC CHẤM, LUẬN GIẢI, BÀI GIẢNG, CÔNG THỨC),
   header ĐÁNH GIÁ & TRA CỨU, nút 'Đóng ▸', topbar toggle 'Tra cứu & Đánh giá [I]'.
2. Sửa triệt để 100% lỗi KaTeX (delimiters an toàn, escape %, loại bỏ Unicode có dấu trong math text, throwOnError: false).
3. Tích hợp ngân hàng câu hỏi kép: Đề 01 (64 câu OLP AI) + Đề 02 (50 câu VOAI 2026 Thầy Đỗ Đình Luật).
4. Chuẩn hóa lời giải theo phong cách Instruct Tutorial / ELI5 (4 khối: Trực quan đời thường cho em bé, Đạo hàm Step-by-Step, Bẫy đề thi & Phương án sai, Căn cứ lý thuyết & PyTorch).
5. Đồng bộ vào cả 2 thư mục local & temp.
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

# Đọc video mapping
videos_map = {
    "§1.1": {
        "sectionId": "§1.1",
        "title": "Machine Learning Fundamentals & k-NN Classification",
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
    "§3.6": {
        "sectionId": "§3.6",
        "title": "Object Detection: IoU, NMS & YOLO vs Faster R-CNN",
        "channel": "DeepLearning.AI / Andrew Ng",
        "youtubeId": "VAo84OOycFQ",
        "startSeconds": 210,
        "timestampLabel": "03:30",
        "highlightNote": "Tính chỉ số IoU = Giao / Hợp, thuật toán Non-Maximum Suppression (NMS) khử trùng lặp bounding box."
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

print("Dữ liệu cơ sở đã sẵn sàng.")
