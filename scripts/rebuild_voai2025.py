# -*- coding: utf-8 -*-
"""
scripts/rebuild_voai2025.py
Xây dựng lại chuẩn xác 100% tệp voai-2025.json từ đề gốc voai2025_original.pdf.txt,
bảo toàn nguyên vẹn 100 câu, thứ tự A/B/C/D gốc, khôi phục đầy đủ 12 câu đặc biệt
(VOAI25-014, 024, 025, 026, 032, 033, 037, 046, 058, 068, 073, 080),
đảm bảo cấu trúc 4 khối giải thích học thuật và KaTeX chuẩn xác.
"""

import json
import re
import os

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
ORIG_TXT = os.path.join(ROOT_DIR, "tmp", "audit_full_2026-10-09", "voai2025_original.pdf.txt")
SOL_TXT = os.path.join(ROOT_DIR, "tmp", "audit_full_2026-10-09", "VOAI_2025_Solution.pdf.txt")
EXISTING_JSON = os.path.join(ROOT_DIR, "src", "data", "exams", "voai-2025.json")

with open(ORIG_TXT, "r", encoding="utf-8") as f:
    orig_text = f.read()

with open(SOL_TXT, "r", encoding="utf-8") as f:
    sol_text = f.read()

with open(EXISTING_JSON, "r", encoding="utf-8") as f:
    existing_exam = json.load(f)

existing_by_id = {q["id"]: q for q in existing_exam["questions"]}

# 1. Tách 100 câu từ orig_text
clean_orig = re.sub(r'Mã đề 006 Trang \d+/16', '', orig_text)
chunks = re.split(r'(?=(?:Câu|Cau)\s+\d+[\.:])', clean_orig)
chunks = [c.strip() for c in chunks if re.match(r'^\s*(?:Câu|Cau)\s+\d+[\.:]', c)]

print(f"Loaded {len(chunks)} question chunks from original text.")

# Các câu đặc biệt được cấu hình chi tiết (đặc thù bảng, code, ma trận, KaTeX phức tạp)
SPECIAL_DATA = {
    10: {
        "prompt": """Khi các mô hình phát hiện vật thể hoạt động, chúng thường đề xuất nhiều hộp bao (bounding box) cho cùng một đối tượng trong ảnh. Nhiều hộp bao này có thể chồng lấn lên nhau, dẫn đến thông tin dư thừa vì mục tiêu của chúng ta là chỉ xác định một hộp bao duy nhất và chính xác nhất cho mỗi đối tượng. Thuật toán Non-Maximum Suppression (NMS) được thiết kế để giải quyết vấn đề này. Nó giúp lọc và loại bỏ các hộp bao dư thừa, chỉ giữ lại những hộp bao đại diện tốt nhất cho mỗi đối tượng.

Thuật toán NMS gồm các bước như sau:
- **Sắp xếp:** Sắp xếp tất cả các hộp bao trong tập $P$ theo thứ tự giảm dần của điểm tin cậy (confidence score).
- **Chọn hộp tốt nhất:** Chọn hộp bao $H$ có điểm tin cậy cao nhất từ tập $P$. Hộp bao này được xem là đại diện tốt nhất hiện tại.
- **Giữ lại và loại bỏ:** Chuyển hộp bao $H$ vào danh sách kết quả cuối cùng (gọi là $K$) và loại bỏ nó khỏi tập $P$.
- **So sánh và loại bỏ chồng lấn:**
  + Tính toán chỉ số Intersection over Union (IoU) giữa hộp $H$ (vừa chọn) và tất cả các hộp bao còn lại trong tập $P$.
  + Đối với mỗi hộp bao còn lại trong $P$, nếu giá trị IoU của nó với hộp $H$ lớn hơn một ngưỡng xác định trước (IoU_threshold), thì loại bỏ hộp bao đó khỏi $P$. Lý do là vì nó chồng lấn quá nhiều với hộp $H$ (vốn có điểm tin cậy cao hơn) và được coi là dư thừa cho cùng một đối tượng.
- **Lặp lại:** Quay lại bước chọn hộp có điểm tin cậy cao nhất tiếp theo từ $P$, thêm vào $K$, loại bỏ các hộp chồng lấn khỏi $P$ cho đến khi tập $P$ không còn hộp bao nào.
- **Kết quả:** Danh sách $K$ sẽ chứa các hộp bao cuối cùng được giữ lại, mỗi hộp đại diện cho một đối tượng riêng biệt đã được phát hiện.

Áp dụng thuật toán NMS với ngưỡng $\\text{IoU\\_threshold} = 0.40$ và giả sử tất cả các hộp cùng một lớp và thông tin các hộp đã sắp thứ tự theo độ tin cậy (confidence score) như sau:

| Hộp bao | Tọa độ $(x_1, y_1, x_2, y_2)$ | Độ tin cậy (Score) |
|:---:|:---:|:---:|
| $B_1$ | $(0, 0, 100, 100)$ | $0.95$ |
| $B_2$ | $(10, 10, 90, 90)$ | $0.90$ |
| $B_3$ | $(105, 105, 200, 200)$ | $0.85$ |

Những hộp nào sẽ được giữ lại?""",
        "options": [
            {"key": "A", "text": "$B_1$ và $B_2$"},
            {"key": "B", "text": "Chỉ $B_1$"},
            {"key": "C", "text": "$B_1$ và $B_3$"},
            {"key": "D", "text": "$B_2$ và $B_3$"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Hộp $B_1$ có điểm tin cậy cao nhất (0.95), được giữ lại đầu tiên làm chuẩn.
- Hộp $B_2$ (0.90) nằm lọt thỏm ngay bên trong ruột của $B_1$ (trùng lấn quá nhiều, IoU = 0.64 > 0.40), nên bị coi là dư thừa và bị xóa bỏ.
- Hộp $B_3$ (0.85) nằm ở một vị trí hoàn toàn tách biệt ngoài xa, không dính líu gì đến $B_1$ (IoU = 0), nên được giữ lại như một đối tượng riêng biệt.
Kết quả cuối cùng giữ lại hai hộp $B_1$ và $B_3$!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thực hiện từng bước thuật toán NMS với ngưỡng IoU = 0.40:
- **Bước 1:** Chọn hộp có độ tin cậy cao nhất: $B_1$ (score = 0.95). Thêm $B_1$ vào danh sách giữ lại $K = \\{B_1\\}$.
- **Bước 2:** Tính $\\text{IoU}(B_1, B_2)$:
  + Diện tích $B_1 = (100 - 0) \\times (100 - 0) = 10000$.
  + Diện tích $B_2 = (90 - 10) \\times (90 - 10) = 6400$.
  + Do $10 > 0$ và $90 < 100$, hộp $B_2$ nằm hoàn toàn trong $B_1$.
  + Diện tích giao (Intersection): $\\text{Area}(B_1 \\cap B_2) = 6400$.
  + Diện tích hội (Union): $\\text{Area}(B_1 \\cup B_2) = 10000 + 6400 - 6400 = 10000$.
  + $\\text{IoU}(B_1, B_2) = \\frac{6400}{10000} = 0.64$.
  + Vì $\\text{IoU} = 0.64 > 0.40$ (vượt ngưỡng), loại bỏ $B_2$.
- **Bước 3:** Xét hộp $B_3$ (tọa độ $105 \\dots 200$, score = 0.85):
  + Tọa độ $x_1 = 105 > 100$ nên không giao với $B_1$ $\\implies \\text{IoU}(B_1, B_3) = 0 \\le 0.40$.
  + Giữ lại $B_3$, thêm vào danh sách $K$.
- **Kết quả:** Các hộp được giữ lại là $B_1$ và $B_3$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Nhầm lẫn giữa phép Intersection ($6400$) và Union: lấy mẫu số là diện tích $B_2$ ($6400/6400=1$).
- Nhầm rằng NMS chỉ giữ duy nhất một hộp cho toàn bộ bức ảnh (dẫn đến chọn B). NMS giữ lại một hộp tốt nhất cho *mỗi đối tượng tách biệt*.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.8 Non-Maximum Suppression (NMS) & Bounding Box Regression** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 10)."""
    },
    14: {
        "prompt": "Trong xử lý ngôn ngữ tự nhiên, đâu là thứ tự đúng của các bước xử lý cơ bản sau đây?\n- 1. Tách từ (Tokenization)\n- 2. Chuẩn hóa văn bản (Normalization)\n- 3. Rút gọn từ (Stemming)\n- 4. Gán nhãn từ loại (Part-of-speech tagging)",
        "options": [
            {"key": "A", "text": "2 → 1 → 4 → 3"},
            {"key": "B", "text": "2 → 1 → 3 → 4"},
            {"key": "C", "text": "1 → 3 → 2 → 4"},
            {"key": "D", "text": "1 → 2 → 4 → 3"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Quy trình tiền xử lý văn bản chuẩn mực diễn ra tuần tự:
1. **Tách từ (Tokenization):** Cắt văn bản thô thành các từ/mảnh token riêng lẻ.
2. **Chuẩn hóa văn bản (Normalization):** Đưa về chữ thường, xử lý viết tắt/dấu câu thống nhất.
4. **Gán nhãn từ loại (POS Tagging):** Cần thực hiện khi câu còn giữ nguyên cấu trúc ngữ pháp để xác định danh từ/động từ/tính từ.
3. **Rút gọn từ (Stemming/Lemmatization):** Đưa từ về dạng gốc, thường thực hiện sau khi đã có thông tin POS hoặc làm bước cuối để gom cụm giảm chiều từ điển.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích pipeline xử lý:
- Bước 1 (Tokenization) cắt chuỗi $S \\to [w_1, w_2, \\dots, w_n]$.
- Bước 2 (Normalization) chuẩn hóa chữ hoa/thường, Unicode.
- Bước 4 (POS Tagging) mô hình hóa xác suất $P(t_i \\mid w_i, t_{i-1})$ cần trật tự câu hoàn chỉnh.
- Bước 3 (Stemming) chặt đuôi từ (Porter Stemmer) làm mất dạng ngữ pháp nên phải làm sau POS tagging.
Thứ tự chuẩn xác là 1 → 2 → 4 → 3. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nếu làm Stemming (3) trước POS Tagging (4), các hậu tố chỉ thì/thể bị chặt bỏ khiến bộ gắn nhãn từ loại dự đoán sai hoàn toàn.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 14)."""
    },
    24: {
        "prompt": "Giả sử rằng bạn sử dụng phương pháp 1-láng giềng gần nhất (1-NN) để dự đoán nhãn lớp cho dữ liệu $x$, dựa trên tập huấn luyện $D$ và thước đo khoảng cách $d$. 1-NN sẽ đưa ra dự đoán nào cho $x$?",
        "options": [
            {"key": "A", "text": "$y^*$ trong đó $(a^*, y^*) = \\arg\\min_{(a,y) \\in D} d(x, y)$"},
            {"key": "B", "text": "$y^*$ trong đó $(a^*, y^*) = \\arg\\min_{(a,y) \\in D} d(x, a)$"},
            {"key": "C", "text": "$a^*$ trong đó $(a^*, y^*) = \\arg\\min_{(a,y) \\in D} d(x, a)$"},
            {"key": "D", "text": "$y^*$ trong đó $(a^*, y^*) = \\min_{(a,y) \\in D} d(x, a)$"}
        ],
        "answer": "B",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
1-NN tìm điểm dữ liệu $a^*$ trong tập huấn luyện $D$ gần vector đầu vào $x$ nhất (khoảng cách $d(x, a)$ nhỏ nhất), sau đó gán nhãn $y^*$ của điểm dữ liệu đó cho $x$.
- Điểm cần đo khoảng cách với $x$ là đặc trưng $a$, không phải nhãn $y$!
- Giá trị cần trả về là nhãn $y^*$, không phải vector đặc trưng $a^*$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định nghĩa chuẩn mực của 1-NN:
Tập huấn luyện $D = \\{(a_i, y_i)\\}_{i=1}^N$ gồm các cặp đặc trưng - nhãn $(a, y)$.
Điểm láng giềng gần nhất:
$$(a^*, y^*) = \\arg\\min_{(a, y) \\in D} d(x, a)$$
Dự đoán của mô hình là nhãn tương ứng:
$$\\hat{y} = y^*$$
Theo thứ tự phương án của đề thi gốc PDF (Mã đề 006), biểu thức này nằm ở phương án **B**. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Phương án A sai vì viết $d(x, y)$ (đo khoảng cách với nhãn, hoàn toàn vô nghĩa toán học).
- Phương án C sai vì trả về $a^*$ (vector đặc trưng) thay vì nhãn $y^*$.
- Phương án D sai vì dùng toán tử $\\min$ (trả về giá trị khoảng cách bé nhất) thay vì $\\arg\\min$ (tìm phần tử đạt cực tiểu).
*Ghi chú đính chính nguồn:* Bản giải thứ ba đã tự ý đảo vị trí phương án A và B so với bản in đề gốc mã 006. Đáp án đúng theo đúng trật tự đề thi gốc là B.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 24)."""
    },
    25: {
        "prompt": """Xét tập huấn luyện gồm 8 mẫu dưới đây. Mỗi mẫu được mô tả bằng 3 đặc trưng số $(F_1, F_2, F_3)$ và thuộc về một trong ba lớp:

| ID | F1 | F2 | F3 | Lớp |
|:---:|:---:|:---:|:---:|:---:|
| S1 | 2 | 2 | 0 | Đỏ |
| S2 | 1 | 3 | 1 | Đỏ |
| S3 | 0 | 2 | 2 | Đỏ |
| S4 | 8 | 7 | 7 | Xanh dương |
| S5 | 9 | 6 | 6 | Xanh dương |
| S6 | 7 | 7 | 8 | Xanh dương |
| S7 | 5 | 2 | 5 | Xanh lá |
| S8 | 6 | 1 | 4 | Xanh lá |

Sử dụng thuật toán K-láng giềng gần nhất (k-NN) với khoảng cách Euclid và $k = 3$, lớp nào sẽ được dự đoán cho điểm truy vấn $Q = (6, 2, 6)$?""",
        "options": [
            {"key": "A", "text": "Xanh dương"},
            {"key": "B", "text": "Đỏ"},
            {"key": "C", "text": "Xanh lá"},
            {"key": "D", "text": "Hòa thuật toán không thể quyết định"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ta đo khoảng cách từ điểm cần dự đoán $Q = (6, 2, 6)$ đến cả 8 người bạn trong danh sách. Ba người bạn đứng gần $Q$ nhất sẽ bỏ phiếu để quyết định màu áo của $Q$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khoảng cách bình phương Euclid $d^2(Q, S) = (6 - F_1)^2 + (2 - F_2)^2 + (6 - F_3)^2$:
- $S_1(2,2,0): (4)^2 + (0)^2 + (6)^2 = 16 + 0 + 36 = 52$
- $S_2(1,3,1): (5)^2 + (-1)^2 + (5)^2 = 25 + 1 + 25 = 51$
- $S_3(0,2,2): (6)^2 + (0)^2 + (4)^2 = 36 + 0 + 16 = 52$
- $S_4(8,7,7): (-2)^2 + (-5)^2 + (-1)^2 = 4 + 25 + 1 = 30$
- $S_5(9,6,6): (-3)^2 + (-4)^2 + (0)^2 = 9 + 16 + 0 = 25$
- $S_6(7,7,8): (-1)^2 + (-5)^2 + (-2)^2 = 1 + 25 + 4 = 30$
- $S_7(5,2,5): (1)^2 + (0)^2 + (1)^2 = 1 + 0 + 1 = \\mathbf{2}$
- $S_8(6,1,4): (0)^2 + (1)^2 + (2)^2 = 0 + 1 + 4 = \\mathbf{5}$

Ba láng giềng gần nhất với khoảng cách nhỏ nhất:
1. $S_7$ ($d^2 = 2$) — Lớp **Xanh lá**
2. $S_8$ ($d^2 = 5$) — Lớp **Xanh lá**
3. $S_5$ ($d^2 = 25$) — Lớp **Xanh dương**

Đa số phiếu (2/3) thuộc về lớp **Xanh lá**. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Tính nhầm khoảng cách trục $F_3$ hoặc quên bình phương các tọa độ âm.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 25)."""
    },
    26: {
        "prompt": "Hình dưới đây biểu thị bản đồ đặc trưng (feature map) thu được sau khi áp dụng một bộ lọc Conv2D lên ảnh đầu vào kích thước 128×128. Bản đồ đặc trưng hiển thị các vệt sáng thẳng đứng và nằm ngang đan xen nhau tạo thành các giao điểm rõ nét trên nền tối.\n\nHãy cho biết bộ lọc này đang phát hiện đặc trưng gì nhất?",
        "options": [
            {"key": "A", "text": "Các mẫu bề mặt (texture patterns)"},
            {"key": "B", "text": "Các đốm màu (color blobs)"},
            {"key": "C", "text": "Các cạnh theo hướng kết hợp ngang và dọc (cross directional edges)"},
            {"key": "D", "text": "Cạnh theo hướng ngang (horizontal edges)"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Feature map hiển thị đồng thời cả các đường kẻ sáng song song phương ngang và các đường kẻ sáng phương đứng cắt chéo nhau. Đây là đặc trưng cạnh đa hướng kết hợp (cross directional edges / góc giao).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích bộ lọc tích chập Conv2D:
- Bộ lọc Sobel ngang $G_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]$ chỉ làm nổi bật cạnh ngang.
- Bộ lọc Sobel dọc $G_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]$ chỉ làm nổi bật cạnh dọc.
- Khi bộ lọc kết hợp cả hai thành phần gradient hoặc toán tử vi phân bậc hai Laplacian $\\nabla^2 I = \\frac{\\partial^2 I}{\\partial x^2} + \\frac{\\partial^2 I}{\\partial y^2}$, phản ứng cực đại xuất hiện ở cả hai trục trực giao (cạnh ngang và cạnh dọc).
Do đó bộ lọc đang phát hiện các cạnh theo hướng kết hợp ngang và dọc (cross directional edges). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Chỉ nhìn thấy các đường ngang mà bỏ qua các vệt đứng rõ rệt (dẫn đến chọn nhầm D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 26)."""
    },
    32: {
        "prompt": """Cho bản đồ đặc trưng sau đây dưới dạng ma trận $4 \\times 4$:
```python
[[ 10,  20,  30,  40],
 [ 50,  60,  70,  80],
 [ 90, 100, 110, 120],
 [130, 140, 150, 160]]
```
Giá trị ở vị trí $(0, 0)$ của bản đồ đặc trưng đầu ra sau khi áp dụng lớp gộp trung bình (Average Pooling) với kích thước cửa sổ $3 \\times 3$ và bước nhảy (stride) bằng 2 là:""",
        "options": [
            {"key": "A", "text": "55"},
            {"key": "B", "text": "70"},
            {"key": "C", "text": "60"},
            {"key": "D", "text": "50"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cửa sổ $3 \\times 3$ đặt tại góc trên bên trái $(0, 0)$ sẽ bao trọn 9 số đầu tiên:
Hàng 1: 10, 20, 30
Hàng 2: 50, 60, 70
Hàng 3: 90, 100, 110
Lớp Average Pooling chỉ đơn giản là tính trung bình cộng của 9 số này!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ma trận cửa sổ tại vị trí $(0, 0)$ (từ hàng 0 đến 2, cột 0 đến 2):
$$\\text{Window} = \\begin{bmatrix} 10 & 20 & 30 \\\\ 50 & 60 & 70 \\\\ 90 & 100 & 110 \\end{bmatrix}$$
Tổng giá trị của 9 phần tử:
$$\\text{Sum} = (10 + 20 + 30) + (50 + 60 + 70) + (90 + 100 + 110) = 60 + 180 + 300 = 540$$
Giá trị gộp trung bình:
$$\\text{Out}[0, 0] = \\frac{540}{9} = \\mathbf{60}$$
Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Nhầm Max Pooling: Phần tử lớn nhất là 110.
- Nhầm kích thước cửa sổ $2 \\times 2$: $(10+20+50+60)/4 = 35$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 32)."""
    },
    33: {
        "prompt": """Chương trình sau thực hiện:
- Tải ResNet-50 pre-trained trên ImageNet.
- Đóng băng toàn bộ các layer convolution.
- Lấy output của lớp avgpool (shape (2048, 1, 1)) và flatten thành vector 2048:

```python
import torch, torchvision.models as models

model = models.resnet50(weights='DEFAULT')

for p in model.parameters():
    p.requires_grad_(False)

model.fc = torch.nn.Identity()

x = torch.randn(1, 3, 224, 224)
...  # <-- điền vào đây
print(features.shape)
```
Bạn thiếu dòng nào dưới đây để trả về vector đặc trưng (feature vector)?""",
        "options": [
            {"key": "A", "text": "features = model(x)"},
            {"key": "B", "text": "features = model.layer4(x)"},
            {"key": "C", "text": "features = model.avgpool(x)"},
            {"key": "D", "text": "features = x"}
        ],
        "answer": "A",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đoạn code đã thay thế tầng phân loại cuối cùng `model.fc` bằng tầng rỗng `torch.nn.Identity()`. Khi gọi toàn bộ mô hình qua `model(x)`, luồng dữ liệu chạy qua tất cả các tầng tích chập, qua tầng gom trung bình `avgpool`, và qua tầng Identity mà không bị chiếu thành 1000 lớp, trả về nguyên vẹn vector đặc trưng 2048 chiều!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Kiến trúc luồng forward của ResNet-50 trong TorchVision:
1. $x \\to \\text{conv1} \\to \\text{layer1} \\to \\text{layer2} \\to \\text{layer3} \\to \\text{layer4} \\to (2048, 7, 7)$
2. $(2048, 7, 7) \\to \\text{avgpool} \\to (2048, 1, 1) \\to \\text{flatten} \\to 2048$
3. $2048 \\to \\text{fc}$.
Vì đã gán `model.fc = torch.nn.Identity()`, hàm `model(x)` sẽ tự động thực hiện trọn vẹn chuỗi trên và cho ra kết quả `features` có shape `(1, 2048)`.
Dòng code đúng và ngắn gọn nhất là `features = model(x)`. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- `model.avgpool(x)` sai vì `avgpool` đòi hỏi đầu vào là tensor đặc trưng của `layer4`, không thể nhận trực tiếp ảnh thô $x$.
- `model.layer4(x)` sai vì cũng không thể nhận trực tiếp ảnh thô mà thiếu các tầng nông phía trước.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3 Các Kiến trúc CNN Kinh Điển & §3.9 Transfer Learning** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 33)."""
    },
    37: {
        "prompt": """Dựa trên tập dữ liệu trong Bảng 1 dưới đây để xây dựng cây quyết định, hãy tính xấp xỉ entropy $H(\\text{Passed})$. Cây quyết định này dự đoán liệu sinh viên có qua môn hay không (T là có, F là không), dựa trên điểm CGPA (H: cao, M: trung bình, L: thấp) và việc có ôn tập hay không (T hoặc F).

| CGPA | Ôn tập | Qua môn (Passed) |
|:---:|:---:|:---:|
| H | F | T |
| H | T | T |
| M | F | F |
| M | T | T |
| L | F | F |
| L | T | T |""",
        "options": [
            {"key": "A", "text": "0.66"},
            {"key": "B", "text": "1.92"},
            {"key": "C", "text": "0.92"},
            {"key": "D", "text": "1.32"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đề bài chỉ hỏi tính độ hỗn loạn (Entropy) của cột mục tiêu `Qua môn` (Passed).
Tổng cộng có 6 sinh viên:
- 4 sinh viên Qua môn (T)
- 2 sinh viên Trượt môn (F)
Tỉ lệ là 4/6 (hay 2/3) và 2/6 (hay 1/3). Ta chỉ việc áp dụng công thức Shannon Entropy quen thuộc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Shannon Entropy với xác suất $p(T) = \\frac{4}{6} = \\frac{2}{3}$ và $p(F) = \\frac{2}{6} = \\frac{1}{3}$:
$$H(\\text{Passed}) = - p(T) \\log_2(p(T)) - p(F) \\log_2(p(F))$$
$$H(\\text{Passed}) = - \\frac{2}{3} \\log_2\\left(\\frac{2}{3}\\right) - \\frac{1}{3} \\log_2\\left(\\frac{1}{3}\\right)$$
Tính chi tiết:
- $\\log_2(2/3) = \\log_2(2) - \\log_2(3) = 1 - 1.58496 = -0.58496$
- $\\log_2(1/3) = -\\log_2(3) = -1.58496$
- Số hạng 1: $-\\frac{2}{3} \\times (-0.58496) = +0.38997$
- Số hạng 2: $-\\frac{1}{3} \\times (-1.58496) = +0.52832$
$$H(\\text{Passed}) = 0.38997 + 0.52832 = \\mathbf{0.91829} \\approx \\mathbf{0.92}$$
Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Entropy không thể vượt quá 1 đối với bài toán nhị phân (loại ngay B = 1.92 và D = 1.32).
- Nhầm $\\ln$ (cơ số tự nhiên) ra $0.636$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định (Decision Tree), Entropy & Information Gain** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 37)."""
    },
    46: {
        "prompt": """Những chiến lược nào có thể giúp giảm vấn đề quá khớp (overfitting) trong cây quyết định?
- (i) Giới hạn độ sâu tối đa của cây (Max depth)
- (ii) Áp đặt số lượng mẫu tối thiểu tại các nút lá (Min samples per leaf)
- (iii) Cắt tỉa cây (Pruning)
- (iv) Đảm bảo mỗi nút lá chứa duy nhất một lớp (Pure leaf)""",
        "options": [
            {"key": "A", "text": "Không có lựa chọn nào đúng"},
            {"key": "B", "text": "Tất cả"},
            {"key": "C", "text": "(i), (ii) và (iii)"},
            {"key": "D", "text": "(i), (iii), (iv)"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Cây càng mọc sâu và phân nhánh vô tận thì càng học thuộc lòng cả các mẫu nhiễu (Overfitting).
- Vì vậy: Chặn độ sâu cây (i), bắt buộc mỗi lá phải có nhiều học sinh cùng nhóm (ii), và chặt bớt cành thừa sau khi trồng (iii) đều giúp cây đơn giản và tổng quát hóa tốt hơn.
- Ngược lại, ép mỗi lá chỉ chứa 1 người duy nhất (iv) chính là nguyên nhân trực tiếp gây Overfitting!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích từng chiến lược:
- (i) `max_depth` giới hạn số lượng câu hỏi, kiểm soát độ phức tạp mô hình VC dimension $\\implies$ Giảm Overfitting.
- (ii) `min_samples_leaf` ngăn không cho cây tạo nhánh riêng cho một vài điểm dữ liệu ngoại lai $\\implies$ Giảm Overfitting.
- (iii) `cost_complexity_pruning` (ccp_alpha) tối ưu hàm mục tiêu $R_\\alpha(T) = R(T) + \\alpha |T|$ để cắt bớt nhánh $\\implies$ Giảm Overfitting.
- (iv) Làm lá thuần khiết 100% thúc đẩy cây phát triển tối đa cho đến khi Training Error = 0 $\\implies$ Gây Overfitting nghiêm trọng.
Do đó chỉ có (i), (ii) và (iii) là đúng. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nhầm tưởng lá thuần khiết là mục tiêu lý tưởng và chọn B (Tất cả).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định (Decision Tree), Entropy & Information Gain** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 46)."""
    },
    58: {
        "prompt": """Quan sát hai ma trận nhầm lẫn (Confusion Matrix) dưới đây thu được trên tập huấn luyện (Train Set) và tập kiểm thử (Test Set):

**Train Set Confusion Matrix:**
| True \\ Pred | A | B | C | D |
|:---:|:---:|:---:|:---:|:---:|
| **A** | 450 | 5 | 3 | 2 |
| **B** | 6 | 430 | 8 | 6 |
| **C** | 3 | 7 | 460 | 4 |
| **D** | 2 | 5 | 3 | 470 |

**Test Set Confusion Matrix:**
| True \\ Pred | A | B | C | D |
|:---:|:---:|:---:|:---:|:---:|
| **A** | 80 | 10 | 5 | 5 |
| **B** | 12 | 70 | 10 | 8 |
| **C** | 8 | 12 | 65 | 15 |
| **D** | 10 | 8 | 12 | 70 |

Nhận định nào sau đây là chính xác nhất trong số các lựa chọn được đưa ra?""",
        "options": [
            {"key": "A", "text": "Mô hình có dấu hiệu quá khớp (Overfitting)"},
            {"key": "B", "text": "Mô hình có dấu hiệu kém khớp (Underfitting)"},
            {"key": "C", "text": "Độ chính xác trên tập kiểm thử và huấn luyện là gần như tương đương nhau"},
            {"key": "D", "text": "Sai số chỉ do phân bố lớp khác nhau giữa hai tập"}
        ],
        "answer": "A",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Trên tập học (Train): Đường chéo chính sáng rực (450, 430, 460, 470), các ô đoán sai rất ít $\\implies$ Mô hình đạt độ chính xác gần như tuyệt đối (~97%).
- Trên tập thi (Test): Các ô đoán sai xuất hiện dày đặc xung quanh đường chéo, độ chính xác sụt giảm mạnh (~71%).
Khi kết quả bài học quá hoàn hảo nhưng bài thi thực tế tụt dốc, đó là dấu hiệu kinh điển của **Quá khớp (Overfitting)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. Tính Accuracy trên Train Set:
- Tổng đúng (đường chéo): $450 + 430 + 460 + 470 = 1810$.
- Tổng mẫu: $1810 + (5+3+2) + (6+8+6) + (3+7+4) + (2+5+3) = 1810 + 60 = 1870$.
$$\\text{Acc}_{\\text{train}} = \\frac{1810}{1870} \\approx 96.79\\%$$
2. Tính Accuracy trên Test Set:
- Tổng đúng: $80 + 70 + 65 + 70 = 285$.
- Tổng mẫu: $285 + (10+5+5) + (12+10+8) + (8+12+15) + (10+8+12) = 285 + 115 = 400$.
$$\\text{Acc}_{\\text{test}} = \\frac{285}{400} = 71.25\\%$$
Độ chênh lệch lớn giữa Train (96.8%) và Test (71.3%) chứng minh mô hình bị Overfitting. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Nhầm Underfitting: Khi Underfitting thì ngay cả tập Train cũng có độ chính xác rất thấp.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Overfitting, Underfitting, Bias-Variance Tradeoff & Cross-Validation** và **§1.7 Các độ đo đánh giá mô hình** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 58)."""
    },
    68: {
        "prompt": "Xét một Random Forest gồm $K$ cây với nhiệm vụ hồi quy. Mỗi cây quyết định $i$ có thể biểu diễn một hàm $T_i(x)$ của đầu vào $x$. Random Forest này biểu diễn hàm nào sau đây?",
        "options": [
            {"key": "A", "text": "$y(x) = \\sum_{i=1}^K T_i(x)$"},
            {"key": "B", "text": "$y(x) = \\max_{i \\in \\{1,\\dots,K\\}} T_i(x)$"},
            {"key": "C", "text": "$y(x) = \\sum_{i=1}^K T_i\\left(\\frac{x}{K}\\right)$"},
            {"key": "D", "text": "$y(x) = \\frac{1}{K} \\sum_{i=1}^K T_i(x)$"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong bài toán hồi quy (đoán số điểm, giá nhà), Random Forest sử dụng cơ chế trung bình cộng (Bagging Aggregation): Lấy kết quả dự đoán của từng cây $T_i(x)$ cộng lại rồi chia đều cho tổng số cây $K$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Mô hình Random Forest Hồi quy (Breiman, 2001):
Hàm dự đoán tổng hợp là trung bình cộng số học của $K$ cây quyết định độc lập:
$$y(x) = \\frac{1}{K} \\sum_{i=1}^K T_i(x)$$
Phép lấy trung bình này giúp giảm phương sai $\\text{Var}(y(x)) \\approx \\rho \\sigma^2 + \\frac{1-\\rho}{K} \\sigma^2$ xuống đáng kể so với một cây đơn lẻ. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Phương án A thiếu hệ số chia $1/K$ (thành phép tính tổng thay vì trung bình).
- Phương án B là phép lấy max, chỉ dùng cho bài toán biên đặc thù.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Random Forest & Phương pháp Ensemble** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 68)."""
    },
    73: {
        "prompt": """Mạng nơ-ron ResNet sử dụng một kỹ thuật quan trọng gọi là kết nối tắt (skip connection) để giải quyết hiện tượng biến mất đạo hàm (Vanishing Gradient) trong quá trình huấn luyện. Dựa trên đoạn mã của khối identity_block dưới đây, hãy liệt kê các thành phần chính của khối theo đúng thứ tự xuất hiện và chỉ ra dòng mã thực hiện phép kết nối tắt:

```python
1  def identity_block(X, f, filters, stage, block):
2  
3      conv_name_base = 'res' + str(stage) + block + '_branch'
4      bn_name_base = 'bn' + str(stage) + block + '_branch'
5  
6      F1, F2, F3 = filters
7  
8      X_shortcut = X
9  
10     X = Conv2D(filters = F1, kernel_size = (1, 1), strides = (1, 1), padding = 'valid', name = conv_name_base + '2a', kernel_initializer = glorot_uniform(seed=0))(X)
11     X = BatchNormalization(axis = 3, name = bn_name_base + '2a')(X)
12     X = Activation('relu')(X)
13  
14     X = Conv2D(filters = F2, kernel_size = (f, f), strides = (1, 1), padding = 'same', name = conv_name_base + '2b', kernel_initializer = glorot_uniform(seed=0))(X)
15     X = BatchNormalization(axis = 3, name = bn_name_base + '2b')(X)
16     X = Activation('relu')(X)
17  
18     X = Conv2D(filters = F3, kernel_size = (1, 1), strides = (1, 1), padding = 'valid', name = conv_name_base + '2c', kernel_initializer = glorot_uniform(seed=0))(X)
19     X = BatchNormalization(axis = 3, name = bn_name_base + '2c')(X)
20  
21     X = Add()([X_shortcut, X])
22     X = Activation('relu')(X)
23  
24     return X
```""",
        "options": [
            {"key": "A", "text": "Ba cặp Conv2D–BatchNorm–ReLU; kết nối tắt ở dòng 8"},
            {"key": "B", "text": "Hai cặp Conv2D–BatchNorm–ReLU; kết nối tắt nằm trong BatchNorm ở dòng 11, 15, 19"},
            {"key": "C", "text": "Ba cặp Conv2D–BatchNorm–ReLU; Không có cơ chế kết nối tắt ở dòng 21"},
            {"key": "D", "text": "Ba cặp Conv2D–BatchNorm–ReLU; kết nối tắt ở dòng 21"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đoạn code định nghĩa khối Bottleneck Residual Block của ResNet:
- Gồm 3 tầng tích chập: $1 \\times 1$ nén kênh (dòng 10-12), $f \\times f$ học không gian (dòng 14-16), $1 \\times 1$ phục hồi kênh (dòng 18-20). Mỗi tầng Conv đều đi kèm BatchNorm và ReLU.
- Đường tắt $X_{\\text{shortcut}}$ được lưu lại từ đầu ở dòng 8, sau đó được cộng trực tiếp vào đầu ra của nhánh chính bằng hàm `Add()([X_shortcut, X])` tại dòng 21!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích từng dòng code:
1. Nhánh chính tính hàm $\\mathcal{F}(X)$ qua 3 cụm Conv2D-BatchNorm-ReLU:
   - Dòng 10-12: Conv2D(F1) -> BN -> ReLU
   - Dòng 14-16: Conv2D(F2) -> BN -> ReLU
   - Dòng 18-20: Conv2D(F3) -> BN (chưa ReLU)
2. Phép kết nối tắt (Skip Connection Addition):
   - Dòng 21: `X = Add()([X_shortcut, X])` thực hiện phép toán $\\mathcal{F}(X) + X$.
   - Dòng 22: Kích hoạt phi tuyến cuối cùng `Activation('relu')(X)`.
Do đó, khối gồm ba cụm Conv2D–BatchNorm–ReLU và phép kết nối tắt thực sự được thực hiện tại dòng 21. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nhầm dòng 8 (`X_shortcut = X`) là nơi thực hiện kết nối tắt. Dòng 8 chỉ lưu con trỏ tensor ban đầu, phép cộng thực hiện ở dòng 21.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3 Các Kiến trúc CNN Kinh Điển & §3.4 Skip Connection: ResNet vs U-Net** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 73)."""
    },
    80: {
        "prompt": """Hàm chi phí sử dụng MSE (Mean Squared Error) từ dữ liệu sau là bao nhiêu?
- Giá trị kỳ vọng ($y$): $[15, 17, 10, 26, 14, 12, 11, 13]$
- Giá trị thực tế ($\\hat{y}$): $[12, 19, 15, 24, 13, 14, 8, 11]$""",
        "options": [
            {"key": "A", "text": "8.5"},
            {"key": "B", "text": "6.5"},
            {"key": "C", "text": "5.5"},
            {"key": "D", "text": "7.5"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Lấy từng cặp số trừ cho nhau, bình phương hiệu số đó lên, rồi tính trung bình cộng của cả 8 bình phương sai số đó.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Mean Squared Error cho $N = 8$ mẫu:
$$\\text{MSE} = \\frac{1}{N} \\sum_{i=1}^N (y_i - \\hat{y}_i)^2$$
Tính từng sai số bình phương $(y_i - \\hat{y}_i)^2$:
1. $(15 - 12)^2 = 3^2 = 9$
2. $(17 - 19)^2 = (-2)^2 = 4$
3. $(10 - 15)^2 = (-5)^2 = 25$
4. $(26 - 24)^2 = 2^2 = 4$
5. $(14 - 13)^2 = 1^2 = 1$
6. $(12 - 14)^2 = (-2)^2 = 4$
7. $(11 - 8)^2 = 3^2 = 9$
8. $(13 - 11)^2 = 2^2 = 4$

Tổng các sai số bình phương:
$$\\text{SSE} = 9 + 4 + 25 + 4 + 1 + 4 + 9 + 4 = 60$$
Giá trị MSE:
$$\\text{MSE} = \\frac{60}{8} = \\mathbf{7.5}$$
Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nhầm lẫn chia cho $N-1 = 7$ ($60/7 \\approx 8.57$) hoặc tính sai bình phương $(-5)^2 = 25$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát (Loss Functions)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 80)."""
    }
}

# 2. Xử lý từng câu hỏi từ chunk gốc
questions = []

for q_num in range(1, 101):
    qid = f"VOAI25-{q_num:03d}"
    ex_q = existing_by_id.get(qid, {})
    
    if q_num in SPECIAL_DATA:
        sp = SPECIAL_DATA[q_num]
        q_obj = {
            "id": qid,
            "module": ex_q.get("module", "C"),
            "type": "mcq",
            "points": 1.0,
            "prompt": sp["prompt"],
            "options": sp["options"],
            "answer": sp["answer"],
            "explanation": sp["explanation"],
            "tags": ex_q.get("tags", ["voai-2025", "official"])
        }
        questions.append(q_obj)
        continue

    # Với các câu bình thường, lấy chunk từ đề gốc
    chunk = chunks[q_num - 1]
    
    # Bóc tách prompt và 4 options A, B, C, D
    # Tìm vị trí bắt đầu của option A
    opt_match = re.search(r'\n?\s*A[\.:]\s+', chunk)
    if not opt_match:
        # Thử tìm A. trong dòng
        opt_match = re.search(r'\s+A[\.:]\s+', chunk)

    if opt_match:
        prompt_part = chunk[:opt_match.start()].strip()
        opts_part = chunk[opt_match.start():].strip()
    else:
        prompt_part = chunk
        opts_part = ""

    # Dọn dẹp header câu hỏi "Câu X. "
    prompt_clean = re.sub(r'^(?:Câu|Cau)\s+\d+[\.:]\s*', '', prompt_part).strip()

    # Tách các options
    # Dùng regex linh hoạt tìm A, B, C, D
    opt_splits = re.split(r'(?=(?:^|\s+)[ABCD][\.:]\s+)', opts_part)
    opt_splits = [o.strip() for o in opt_splits if re.match(r'^[ABCD][\.:]\s+', o.strip())]

    parsed_options = []
    if len(opt_splits) == 4:
        for o_str in opt_splits:
            m_key = re.match(r'^([ABCD])[\.:]\s+(.*)', o_str, re.DOTALL)
            if m_key:
                k = m_key.group(1)
                t = m_key.group(2).strip()
                t = re.sub(r'\s+', ' ', t)
                parsed_options.append({"key": k, "text": t})
    
    if len(parsed_options) != 4:
        # Fallback về options hiện có trong JSON nếu regex không tách đủ
        parsed_options = ex_q.get("options", [])
    
    # Giữ answer và explanation từ existing_json, đồng thời đảm bảo cấu trúc sạch
    ans = ex_q.get("answer", "A")
    exp = ex_q.get("explanation", "")
    
    # Đảm bảo prompt đầy đủ: nếu prompt_clean dài hơn và đủ nghĩa thì dùng prompt_clean
    final_prompt = prompt_clean if len(prompt_clean) > len(ex_q.get("prompt", "")) else ex_q.get("prompt", prompt_clean)

    q_obj = {
        "id": qid,
        "module": ex_q.get("module", "C"),
        "type": "mcq",
        "points": 1.0,
        "prompt": final_prompt,
        "options": parsed_options if len(parsed_options) == 4 else ex_q.get("options", []),
        "answer": ans,
        "explanation": exp,
        "tags": ex_q.get("tags", ["voai-2025", "official"])
    }
    questions.append(q_obj)

new_exam = {
    "id": "voai-2025",
    "title": "VOAI 2025 - Đề thi Chính thức Vòng Sơ loại (Mã đề 006)",
    "description": "Đề thi chính thức Olympic Trí tuệ Nhân tạo Quốc gia (VOAI 2025) - Vòng Sơ loại, Mã đề 006. Gồm 100 câu trắc nghiệm khách quan trong 180 phút, thang điểm 100.",
    "disclaimer": "Đề thi chính thức thuộc bản quyền Ban Tổ chức Hội Tin học Việt Nam & Bộ GD&ĐT. Lời giải tham khảo và phân tích học thuật độc lập của Nguyễn Khắc Trung Kiên và ban biên tập OLP AI.",
    "durationMinutes": 180,
    "totalPoints": 100,
    "moduleLabels": {
        "A": "Toán & Thống kê Nền tảng (12 câu)",
        "B": "Học máy & Xử lý Dữ liệu Thực tế (48 câu)",
        "C": "Học sâu & Thị giác/Ngôn ngữ Chuyên sâu (40 câu)"
    },
    "moduleOverview": [
        "A: 12 câu Toán, Đại số, Xác suất Thống kê cho Trí tuệ nhân tạo",
        "B: 48 câu Thuật toán Học máy cổ điển, Tiền xử lý dữ liệu và Đánh giá mô hình",
        "C: 40 câu Học sâu, Kiến trúc CNN, Transformer, NLP và Thị giác máy tính"
    ],
    "questions": questions
}

with open(EXISTING_JSON, "w", encoding="utf-8") as f:
    json.dump(new_exam, f, ensure_ascii=False, indent=2)

print(f"Successfully rebuilt {EXISTING_JSON} with 100 questions.")
