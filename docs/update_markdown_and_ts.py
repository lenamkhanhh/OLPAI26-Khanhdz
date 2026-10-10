# -*- coding: utf-8 -*-
import os
import sys
import json

root = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26"
sys.path.insert(0, os.path.join(root, "docs"))
from voai_50_questions_data import VOAI_QUESTIONS

md_path = os.path.join(root, "content", "01-ly-thuyet-olp-ai.md")
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

voai_md_parts = [
    "\n\n---\n\n## §8. Bộ Đề Luyện Thi Thực Chiến Chuẩn VOAI 2026 (50 Câu) — Kèm Đáp Án & Giải Thích Chi Tiết\n\n",
    "> **Nguồn gốc:** Trích từ Đề thi thử Vòng loại Olympic Trí tuệ Nhân tạo Việt Nam (VOAI 2026) của Thầy Đỗ Đình Luật.\n",
    "> Toàn bộ 50 câu đều được phân tích cặn kẽ bản chất toán học, công thức tính tay, đối chiếu mã mục § trong Sổ tay và chỉ rõ các bẫy cần tránh.\n\n"
]

for q in VOAI_QUESTIONS:
    qid = q["id"]
    qtext = q["question"]
    opts = q["options"]
    ans = q["correct"]
    expl = q["explanation"]
    sec = q["section_ref"]
    trap = q["trap"]

    voai_md_parts.append(f"### Câu {qid} (VOAI 2026)\n**Đề bài:** {qtext}\n\n")
    for opt in opts:
        voai_md_parts.append(f"- {opt}\n")
    voai_md_parts.append(f"\n> **Đáp án đúng: {ans}**  \n")
    voai_md_parts.append(f"> **Giải thích chi tiết:** {expl}  \n")
    voai_md_parts.append(f"> **Căn cứ lý thuyết:** Tham chiếu mục **{sec}**.  \n")
    voai_md_parts.append(f"> **Bẫy đề thi:** *{trap}*\n\n")

matrix_md = """
---

## §9. Ma Trận Đối Chiếu Tra Cứu Web App & Lộ Trình Ôn Luyện Nước Rút

### §9.1 Phương pháp kết hợp Web App & Sổ tay PDF
1. **Luyện tập có phản hồi (Practice Mode):** Làm từng câu trên web, đọc giải thích inline và ghi nhớ mã mục lý thuyết (§x.y).
2. **Đọc sâu bản chất trong Sổ tay PDF:** Mở tài liệu PDF tại đúng mục § để nắm chắc đạo hàm, chứng minh và các tham số.
3. **Thi thử tính giờ (Exam Mode):** Làm đề 60 câu trắc nghiệm/code trong 90 phút, đạt $\\ge 70\\%$ điểm (ĐẠT).

### §9.2 Rubric tự chấm 4 bài tự luận (Thang 10 điểm/câu)
1. **Phân tích bài toán & Mục tiêu (2.0đ):** Xác định bài toán, đặc thù dữ liệu, ràng buộc tài nguyên.
2. **Xử lý dữ liệu & Validation Strategy (2.0đ):** Tiền xử lý, chia tập Stratified K-Fold / Time-Series Split chống Data Leakage.
3. **Lựa chọn mô hình & Kiến trúc (2.5đ):** Baseline -> Kiến trúc chính tối ưu (YOLO, ResNet, U-Net, BERT, LightGBM/CatBoost).
4. **Chiến lược Huấn luyện & Tối ưu (2.0đ):** Loss function, Optimizer (AdamW + Cosine Warmup), chống Overfitting.
5. **Đánh giá, Phân tích Lỗi & Triển khai (1.5đ):** Metric chuẩn (mAP, F1, BLEU), Error Analysis, Quantization/ONNX Runtime.
"""

voai_full_md = "".join(voai_md_parts) + matrix_md

if "## §8. Bộ Đề Luyện Thi Thực Chiến Chuẩn VOAI 2026" not in md_content:
    full_md = md_content.strip() + "\n" + voai_full_md
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"Da cap nhat {md_path} ({len(full_md)} ky tu)")
else:
    print("01-ly-thuyet-olp-ai.md da ton tai Section 8.")

# Cap nhat theoryData.ts
ts_path = os.path.join(root, "src", "data", "theoryData.ts")
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

with open(md_path, "r", encoding="utf-8") as f:
    latest_full_md = f.read()

ts_content = f"""// Du lieu So tay Ly thuyet OLP AI HCMUS 2026 (Full LaTeX KaTeX)
export interface TheoryChapter {{
  id: string;
  title: string;
  desc: string;
  sectionStart: string;
}}

export const THEORY_CHAPTERS: TheoryChapter[] = {json.dumps(chapters, ensure_ascii=False, indent=2)};

export const FULL_THEORY_MARKDOWN = {json.dumps(latest_full_md, ensure_ascii=False)};
"""

with open(ts_path, "w", encoding="utf-8") as f:
    f.write(ts_content)
print(f"Da cap nhat {ts_path} ({len(ts_content)} ky tu)")
