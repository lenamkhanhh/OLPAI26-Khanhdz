# -*- coding: utf-8 -*-
import os
import sys
import re
import json

root = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
md_path = os.path.join(root, "content", "01-ly-thuyet-olp-ai.md")
ts_path = os.path.join(root, "src", "data", "theoryData.ts")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Pattern tim cac mục §x hoặc §x.y
pattern = r'(###?\s+(§[\d\.]+.*?)\n)([\s\S]*?)(?=(?:###?\s+§|\Z))'
matches = re.findall(pattern, text)

theory_sections = []
for full_header, header_text, body_text in matches:
    # Tach secId (vi du §1.1) va title
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

chapters = [
    {
        "id": "c1",
        "title": "Chương 1: Machine Learning Cổ Điển",
        "desc": "k-NN, SVM, Cây quyết định, Random Forest, Bias-Variance, L1/L2 Regularization, Metrics, K-Means, Imbalanced Data, NumPy.",
        "sectionStart": "§1",
    },
    {
        "id": "c2",
        "title": "Chương 2: Deep Learning & PyTorch",
        "desc": "Perceptron, MLP, Các hàm kích hoạt, PyTorch Training Loop, Loss Functions, Optimizers (Adam/SGD), BatchNorm/LayerNorm, Dropout.",
        "sectionStart": "§2",
    },
    {
        "id": "c3",
        "title": "Chương 3: Thị Giác Máy Tính (CV)",
        "desc": "Công thức kích thước Conv2D, Pooling, Kiến trúc VGG/ResNet/EfficientNet, Skip Connection (ADD vs CONCAT), ViT, Object Detection (IoU, NMS, mAP), GAN vs Diffusion.",
        "sectionStart": "§3",
    },
    {
        "id": "c4",
        "title": "Chương 4: Xử Lý Ngôn Ngữ Tự Nhiên (NLP)",
        "desc": "Pipeline tiền xử lý, Word Representations (TF-IDF, Word2Vec, FastText, BERT), Cosine Similarity, LSTM/GRU, Transformer Attention, BERT vs GPT, Metrics (BLEU, ROUGE).",
        "sectionStart": "§4",
    },
    {
        "id": "c5",
        "title": "Chương 5: Xác Suất & Thống Kê Cho AI",
        "desc": "Ma trận trực giao, Hessian, Định lý Bayes, Phân phối xác suất, Kỳ vọng/Phương sai, MLE vs MAP, p-value & Time-Series Split.",
        "sectionStart": "§5",
    },
    {
        "id": "c6",
        "title": "Chương 6: Bảng 24 Bẫy Đề Thi Kinh Điển",
        "desc": "Tổng hợp 24 lỗi hay mắc nhất (SAI -> ĐÚNG) thường xuyên gài bẫy trong đề thi trắc nghiệm OLP AI.",
        "sectionStart": "§6",
    },
    {
        "id": "c7",
        "title": "Chương 7: Chuyên Đề Tác Vụ Thực Chiến OLP AI 2025 & 2026",
        "desc": "Khung 5 bước giải pháp chuẩn cho: Nhận diện ngôn ngữ ký hiệu video, Dịch máy Hoa-Việt, Phát hiện bệnh lá cây di động, Dự đoán sinh viên bỏ học XAI.",
        "sectionStart": "§7",
    },
    {
        "id": "c8",
        "title": "Chương 8: Bộ Đề Luyện Thi Thực Chiến Chuẩn VOAI 2026 (50 Câu)",
        "desc": "50 câu hỏi trắc nghiệm thực chiến bám sát đề thi VOAI 2026 kèm đáp án chính thức và giải thích chi tiết toán học từng câu.",
        "sectionStart": "§8",
    },
    {
        "id": "c9",
        "title": "Chương 9: Ma Trận Đối Chiếu Tra Cứu Web App & Rubric Tự Luận",
        "desc": "Bảng ánh xạ câu hỏi trắc nghiệm giữa Web App và Handbook PDF, cùng Rubric tự chấm 4 bài tự luận thang điểm 10.",
        "sectionStart": "§9",
    }
]

ts_content = f"""// Du lieu So tay Ly thuyet OLP AI HCMUS 2026 (Full LaTeX KaTeX)
export interface TheorySection {{
  id: string;
  secId: string;
  title: string;
  body: string;
}}

export interface TheoryChapter {{
  id: string;
  title: string;
  desc: string;
  sectionStart: string;
}}

export const THEORY_SECTIONS: TheorySection[] = {json.dumps(theory_sections, ensure_ascii=False, indent=2)};

export const THEORY_CHAPTERS: TheoryChapter[] = {json.dumps(chapters, ensure_ascii=False, indent=2)};

export const FULL_THEORY_MARKDOWN = {json.dumps(text, ensure_ascii=False)};
"""

with open(ts_path, "w", encoding="utf-8") as f:
    f.write(ts_content)

print(f"Da tao thanh cong {ts_path} voi {len(theory_sections)} sections ({len(ts_content)} ky tu)")
