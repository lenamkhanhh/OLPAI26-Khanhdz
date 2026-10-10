# -*- coding: utf-8 -*-
"""
scripts/apply_all_audit_fixes.py
Thực thi các sửa đổi nội dung và kiến thức theo VERIFY_SAU_SUA_2026-10-08.md:
1. Sửa VOAI02-M35, VOAI02-M49, VOAI02-M51 trong olp-02.json
2. Sửa DeepFake split thành StratifiedGroupKFold trong olp-02.json
3. Đồng bộ content/02-de-chuan-format-voai-expand.md cho M49 và E04
4. Cập nhật §2.8 BatchNorm trong content/01-ly-thuyet-olp-ai.md
"""

import json
import os
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

def update_exams():
    # 1. olp-02.json
    path_02 = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-02.json")
    with open(path_02, "r", encoding="utf-8") as f:
        data_02 = json.load(f)

    for q in data_02["questions"]:
        qid = q["id"]

        # VOAI02-M35
        if qid == "VOAI02-M35":
            q["explanation"] = q["explanation"].replace(
                "Bẫy đề thi: Chọn A (nhầm L1/L2 với prior Laplace/Gauss). Đề bài hỏi căn cứ hình học (geometry of norm balls). Nhớ từ khóa: 'Góc nhọn trên trục tọa độ' (Corners / Vertices on axes).",
                "Bẫy đề thi: Chọn các phương án giải thích sai về hàm mũ/log hoặc nhầm lẫn L1/L2 với tiên nghiệm xác suất Laplace/Gauss khi đề bài đang hỏi căn cứ hình học (geometry of norm balls). Nhớ từ khóa hình học: 'Góc nhọn trên trục tọa độ' (Corners / Vertices on axes)."
            )

        # VOAI02-M49
        if qid == "VOAI02-M49":
            q["prompt"] = "Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự chuẩn mực logic của các bước tiền xử lý văn bản thô (Text Preprocessing) nào sau đây là CHÍNH XÁC NHẤT?"
            q["options"] = [
                {
                    "key": "A",
                    "text": "Loại bỏ Stopwords -> Lemmatization -> Tách từ (Tokenization) -> Hạ chữ thường (Lowercasing)"
                },
                {
                    "key": "B",
                    "text": "Vector hóa -> Tách từ (Tokenization) -> Stemming -> Loại bỏ Stopwords"
                },
                {
                    "key": "C",
                    "text": "Tách từ (Tokenization) -> Chuẩn hóa & Hạ chữ thường (Normalization/Lowercasing) -> Loại bỏ từ dừng (Stopwords) -> Rút gọn từ gốc (Stemming/Lemmatization) -> Vector hóa (Vectorization)"
                },
                {
                    "key": "D",
                    "text": "Lemmatization -> Vector hóa -> Tách từ (Tokenization) -> POS Tagging"
                }
            ]
            q["answer"] = "C"
            q["explanation"] = """### 1. ELI5 — Trực quan cho em bé
Quy trình tiền xử lý văn bản cổ điển giống như sơ chế nguyên liệu nấu ăn:
- Bước 1: Đổ nguyên liệu ra thớt và thái thành từng miếng/từ độc lập (Tách từ - Tokenization).
- Bước 2: Rửa sạch bụi bẩn, đưa về cùng kích cỡ đồng nhất (Chuẩn hóa ký tự & Hạ chữ thường).
- Bước 3: Nhặt bỏ rác và cọng thừa không dùng được (Lọc từ dừng - Stopwords như 'và', 'thì', 'là').
- Bước 4: Gọt vỏ giữ lại phần lõi tinh túy (Rút gọn từ gốc - Stemming/Lemmatization).
- Bước 5: Cân đo định lượng thành các con số đưa vào mô hình (Vector hóa - BoW / TF-IDF)!

### 2. Đạo hàm & Toán học Step-by-Step
Trật tự phụ thuộc logic trong pipeline NLP cổ điển:
1. **Tokenization**: Chia chuỗi văn bản thô thành mảng các đơn vị từ vựng độc lập $\{w_1, w_2, \dots, w_T\}$. Đây là tiền đề bắt buộc trước khi có thể duyệt từ điển hoặc đếm tần suất.
2. **Normalization & Lowercasing**: Đưa các biến thể về dạng đồng nhất (ví dụ: 'Apple' và 'apple' về 'apple').
3. **Stopword Removal**: Loại bỏ các hư từ có tần suất xuất hiện quá cao nhưng mang ít giá trị ngữ nghĩa phân biệt.
4. **Stemming / Lemmatization**: Quy đổi các dạng ngữ pháp (chạy, đã chạy, đang chạy) về từ gốc (lemma).
5. **Vectorization**: Ánh xạ chuỗi từ đã sạch thành biểu diễn số học (TF-IDF, BoW).
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Pitfalls
Bẫy phi logic trong các phương án sai:
- Phương án A sai vì đòi lọc Stopwords và Lemmatize trước khi Tokenize (không thể so khớp từ dừng trong từ điển khi chuỗi chưa được cắt token).
- Phương án B sai vì đưa Vector hóa lên đầu tiên (không thể vector hóa khi chưa có token).
- Phương án D sai vì đặt Lemmatize và Vector hóa trước Tokenize.

### 4. Căn cứ lý thuyết & Code minh họa
```python
import nltk
text = 'The cats are running fast.'
tokens = nltk.word_tokenize(text.lower()) # 1. Tokenize + Lowercase
# 2. Filter stopwords & 3. Lemmatize
clean = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
# 4. Vectorize: BoW / TF-IDF
```"""

        # VOAI02-M51
        if qid == "VOAI02-M51":
            q["explanation"] = q["explanation"].replace(
                "nhầm mẫu số thành $3 \\times 3 = 9$ (chọn A).",
                "nhầm mẫu số thành $3 \\times 3 = 9$ (chọn B)."
            )

        # VOAI02-E04 (DeepFake)
        if qid == "VOAI02-E04":
            q["modelAnswer"] = q["modelAnswer"].replace(
                "5-Fold StratifiedKFold. Đảm bảo cặp ảnh $(I_0, I_1)$ luôn nằm trọn vẹn trong cùng một fold (tránh tách rời 2 ảnh của cùng một cặp vào train và val gây Data Leakage).",
                "5-Fold StratifiedGroupKFold với `groups = pair_id` (hoặc phân chia trên danh sách cặp $(I_0, I_1)$ trước rồi mới mở rộng thành từng ảnh). Nếu dữ liệu có nguồn video/người thực hiện gốc, group trực tiếp ở cấp nguồn video đó để triệt tiêu hoàn toàn Data Leakage giữa train và validation."
            )

    with open(path_02, "w", encoding="utf-8") as f:
        json.dump(data_02, f, ensure_ascii=False, indent=2)
    print("✓ Đã cập nhật xong src/data/exams/olp-02.json")

    # 2. Cập nhật content/02-de-chuan-format-voai-expand.md
    md_02_path = os.path.join(ROOT_DIR, "content", "02-de-chuan-format-voai-expand.md")
    with open(md_02_path, "r", encoding="utf-8") as f:
        md_02 = f.read()

    # Sửa M49 trong Markdown
    old_m49_md = """### VOAI02-M49. Trật Tự Chuẩn Của Pipeline Tiền Xử Lý Văn Bản Cổ Điển [1.5đ]
*Chương 4: NLP & LLMs*

**Câu hỏi**: Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự chuẩn mực logic của các bước tiền xử lý văn bản thô (Text Preprocessing) nào sau đây là **CHÍNH XÁC NHẤT**?

- A. Loại bỏ Stopwords -> Lemmatization -> Tokenization -> Hạ chữ thường (Lowercasing)
- B. Tokenization (Tách từ/token) -> Chuẩn hóa & Hạ chữ thường (Normalization/Lowercasing) -> Loại bỏ Stopwords -> Rút gọn từ gốc (Stemming / Lemmatization) -> Vector hóa (Vectorization)
- C. Vector hóa -> Tokenization -> Stemming -> Loại bỏ Stopwords
- D. Lemmatization -> Vector hóa -> Tokenization -> POS Tagging

**Đáp án đúng**: **B**"""

    new_m49_md = """### VOAI02-M49. Trật Tự Chuẩn Của Pipeline Tiền Xử Lý Văn Bản Cổ Điển [1.5đ]
*Chương 4: NLP & LLMs*

**Câu hỏi**: Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự chuẩn mực logic của các bước tiền xử lý văn bản thô (Text Preprocessing) nào sau đây là **CHÍNH XÁC NHẤT**?

- A. Loại bỏ Stopwords -> Lemmatization -> Tách từ (Tokenization) -> Hạ chữ thường (Lowercasing)
- B. Vector hóa -> Tách từ (Tokenization) -> Stemming -> Loại bỏ Stopwords
- C. Tách từ (Tokenization) -> Chuẩn hóa & Hạ chữ thường (Normalization/Lowercasing) -> Loại bỏ từ dừng (Stopwords) -> Rút gọn từ gốc (Stemming/Lemmatization) -> Vector hóa (Vectorization)
- D. Lemmatization -> Vector hóa -> Tách từ (Tokenization) -> POS Tagging

**Đáp án đúng**: **C**"""

    if old_m49_md in md_02:
        md_02 = md_02.replace(old_m49_md, new_m49_md)
        md_02 = md_02.replace("Đáp án chính xác là **B**.", "Đáp án chính xác là **C**.")

    # Sửa DeepFake split trong Markdown
    md_02 = md_02.replace(
        "5-Fold StratifiedKFold. Đảm bảo cặp ảnh $(I_0, I_1)$ luôn nằm trọn vẹn trong cùng một fold",
        "5-Fold StratifiedGroupKFold với `groups = pair_id` (hoặc phân chia trên danh sách cặp $(I_0, I_1)$ trước rồi mới mở rộng thành từng ảnh). Nếu dữ liệu có nguồn video/người thực hiện gốc, group trực tiếp ở cấp nguồn video đó để triệt tiêu hoàn toàn Data Leakage"
    )

    with open(md_02_path, "w", encoding="utf-8") as f:
        f.write(md_02)
    print("✓ Đã cập nhật xong content/02-de-chuan-format-voai-expand.md")

    # 3. Cập nhật §2.8 trong content/01-ly-thuyet-olp-ai.md
    theory_path = os.path.join(ROOT_DIR, "content", "01-ly-thuyet-olp-ai.md")
    with open(theory_path, "r", encoding="utf-8") as f:
        theory_md = f.read()

    old_bn = """- **Batch Normalization (BatchNorm — Ioffe & Szegedy, 2015):**
  Chuẩn hóa trên toàn bộ mini-batch dọc theo chiều mẫu:
  $$\\mu_B = \\frac{1}{m}\\sum x_i, \\quad \\sigma_B^2 = \\frac{1}{m}\\sum (x_i - \\mu_B)^2, \\quad \\hat{x}_i = \\frac{x_i - \\mu_B}{\\sqrt{\\sigma_B^2 + \\epsilon}}$$
  $$y_i = \\gamma \\hat{x}_i + \\beta \\quad (\\gamma, \\beta \\text{ là các tham số học được})$$
  - Vị trí chuẩn: **Linear / Conv $\\to$ BatchNorm $\\to$ ReLU**.
  - Lúc suy luận (Inference): Dùng giá trị trung bình tích lũy `running_mean` và `running_var` được lưu từ quá trình train.
  - Nhược điểm: Kém hiệu quả khi kích thước batch size nhỏ ($m < 8$) hoặc dữ liệu có độ dài thay đổi như văn bản."""

    new_bn = """- **Batch Normalization (BatchNorm — Ioffe & Szegedy, 2015):**
  Chuẩn hóa trên toàn bộ mini-batch dọc theo chiều mẫu:
  $$\\mu_B = \\frac{1}{m}\\sum x_i, \\quad \\sigma_B^2 = \\frac{1}{m}\\sum (x_i - \\mu_B)^2, \\quad \\hat{x}_i = \\frac{x_i - \\mu_B}{\\sqrt{\\sigma_B^2 + \\epsilon}}$$
  $$y_i = \\gamma \\hat{x}_i + \\beta \\quad (\\gamma, \\beta \\text{ là các tham số học được})$$
  - Vị trí chuẩn: **Linear / Conv $\\to$ BatchNorm $\\to$ ReLU**.
  - **Bản chất thống kê theo chiều dữ liệu**:
    - Với `BatchNorm1d` (dữ liệu bảng/vector), mẫu số thống kê là $m = N$ (batch size). Nếu $N=1$, mẫu số $N-1=0$, phương sai mẫu không xác định $\\implies$ không thể chuẩn hóa.
    - Với `BatchNorm2d` (ảnh), thống kê được tính trên toàn bộ $(N, H, W)$ với $m = N \\times H \\times W$ phần tử trên mỗi channel. Nếu $N=1$ nhưng $H > 1, W > 1$, số phần tử $H \\times W > 1$ nên phương sai mẫu vẫn xác định được (trừ khi feature map là hằng số). Tuy nhiên, mini-batch nhỏ vẫn làm ước lượng thống kê bị nhiễu cao.
  - **Lúc suy luận (Inference)**: `model.eval()` mặc định sử dụng `running_mean` và `running_var` tích lũy di động từ pha huấn luyện cùng các tham số affine $\\gamma, \\beta$.
  - **Tối ưu hóa Gộp Tầng (Conv + BN Fusion)**: Là kỹ thuật tối ưu hóa triển khai độc lập (thực hiện qua `torch.nn.utils.fusion.fuse_conv_bn_eval` hoặc TensorRT/ONNX) để gộp trọng số Conv và BatchNorm thành một phép tích chập đơn lẻ:
    $$W_{\\text{fused}} = W \\cdot \\frac{\\gamma}{\\sqrt{\\sigma_{\\text{running}}^2 + \\epsilon}}, \\quad b_{\\text{fused}} = \\beta + (b - \\mu_{\\text{running}}) \\cdot \\frac{\\gamma}{\\sqrt{\\sigma_{\\text{running}}^2 + \\epsilon}}$$
    giúp triệt tiêu hoàn toàn chi phí tính toán của lớp BatchNorm khi inference."""

    if old_bn in theory_md:
        theory_md = theory_md.replace(old_bn, new_bn)
        with open(theory_path, "w", encoding="utf-8") as f:
            f.write(theory_md)
        print("✓ Đã cập nhật xong §2.8 BatchNorm trong content/01-ly-thuyet-olp-ai.md")
    else:
        print("ℹ Không tìm thấy block cũ của BatchNorm, kiểm tra thủ công.")

if __name__ == "__main__":
    update_exams()
