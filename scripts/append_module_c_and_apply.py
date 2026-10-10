# -*- coding: utf-8 -*-
"""
Script scripts/append_module_c_and_apply.py
Hoàn thiện 30 câu trắc nghiệm Module C (C01-C30) và 4 câu tự luận (E01-E04)
áp dụng vào src/data/exams/olp-01.json.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_upgraded_olp01 import UPGRADES, exam_data, json_path

# ==========================================
# MODULE C: ML / DL / CV / NLP (30 CÂU)
# ==========================================

UPGRADES["OLP01-C01"] = {
    "prompt": "Thuật toán k-NN (k-Nearest Neighbors) được xếp vào nhóm thuật toán 'Lazy Learner' (người học lười) và phi tham số (non-parametric). Phát biểu nào sau đây giải thích ĐÚNG NHẤT về bản chất này?",
    "options": [
        {"key": "A", "text": "Thuật toán không có pha huấn luyện tham số (không học w, b), chỉ lưu toàn bộ dữ liệu vào bộ nhớ và dồn toàn bộ tính toán khoảng cách vào thời điểm dự đoán (Inference)"},
        {"key": "B", "text": "Thuật toán học trước một tập trọng số cố định nhưng chỉ cập nhật chúng khi gặp dữ liệu lỗi"},
        {"key": "C", "text": "Thuật toán biến đổi dữ liệu sang không gian vô hạn chiều bằng Kernel Trick"},
        {"key": "D", "text": "Thuật toán chỉ chạy được khi số chiều dữ liệu nhỏ hơn 3"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới: Lazy Learner (Người học lười).**
Tưởng tượng một học sinh lười: Suốt cả học kỳ không chịu học bài gì cả (không học công thức hay trọng số $w, b$, độ phức tạp huấn luyện là $\\mathcal{O}(1)$), chỉ mang toàn bộ cuốn sách giáo khoa vào phòng thi.
Khi giám thị phát đề thi (có câu hỏi mới $x_q$), học sinh này mới cuống cuồng lật từng trang sách, đo khoảng cách đến tất cả các bài tập cũ để tìm ra $k$ bài giống nhất rồi chép đáp án theo số đông!
Vì thế, k-NN 'lười lúc học nhưng cực khổ lúc thi' (Inference tốn rất nhiều thời gian và bộ nhớ: $\\mathcal{O}(N \\cdot d)$).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Quy trình toán học của k-NN:
1. Cho tập huấn luyện $D = \\{(x_i, y_i)\\}_{i=1}^N$. Không có quá trình tối ưu hóa $\\min_w \\mathcal{L}(w)$.
2. Với điểm cần dự đoán $x_q$, tính khoảng cách Minkowski bậc $p$ đến tất cả $N$ điểm:
$$D(x_q, x_i) = \\left( \\sum_{j=1}^d |x_{q,j} - x_{i,j}|^p \\right)^{1/p}$$
3. Chọn ra tập con $\\mathcal{N}_k(x_q)$ gồm $k$ điểm có khoảng cách nhỏ nhất.
4. Dự đoán bằng biểu quyết đa số (Majority Voting):
$$\\hat{y} = \\arg\\max_c \\sum_{i \\in \\mathcal{N}_k(x_q)} \\mathbb{I}(y_i = c)$$
Chọn đáp án **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B:** Mô tả các mô hình có tham số (Parametric Models như Perceptron, Logistic Regression).
- **Phương án C:** Mô tả Kernel SVM.
- **Phương án D:** k-NN chạy được trên mọi số chiều $d$, tuy nhiên khi $d$ quá lớn sẽ gặp 'Lời nguyền số chiều' (Curse of Dimensionality).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)**.
🔗 Ngay ở câu tiếp theo **C02**, ta sẽ phân tích ảnh hưởng sống còn của siêu tham số $k$ trong k-NN!"""
}

UPGRADES["OLP01-C02"] = {
    "prompt": "Trong thuật toán k-NN, siêu tham số $k$ (số lượng láng giềng gần nhất) ảnh hưởng như thế nào đến sự đánh đổi giữa Độ chệch (Bias) và Phương sai (Variance) của mô hình?",
    "options": [
        {"key": "A", "text": "Khi k = 1, ranh giới phân chia rất phẳng mượt, mô hình bị Underfitting (High Bias)"},
        {"key": "B", "text": "Khi k nhỏ (k = 1), mô hình có ranh giới phân chia phức tạp, nhạy cảm với nhiễu dẫn đến Overfitting; khi k lớn (k -> N), ranh giới mượt dần và thiên vị lớp đa số dẫn đến Underfitting"},
        {"key": "C", "text": "Giá trị k càng lớn thì mô hình càng dễ bị Overfitting do nhớ quá nhiều dữ liệu"},
        {"key": "D", "text": "Siêu tham số k không có bất kỳ ảnh hưởng nào đến ranh giới quyết định"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
- **Khi $k = 1$ (Hỏi đúng 1 người hàng xóm gần nhất):** Nếu người hàng xóm đó là một kẻ quậy phá (điểm nhiễu / outlier), bạn sẽ tin theo răm rắp! Ranh giới phân chia sẽ bị xé nhỏ ngoằn ngoèo, ôm sát từng điểm dữ liệu $\\implies$ **Overfitting (Học vẹt, nhạy cảm với nhiễu)**.
- **Khi $k$ rất lớn (Hỏi ý kiến cả làng $k \\to N$):** Ý kiến của người gần bạn bị chìm nghỉm giữa đám đông. Cả làng có nhiều người thích màu gì thì bạn chọn màu đó $\\implies$ Ranh giới phẳng lì, dự đoán theo lớp đa số $\\implies$ **Underfitting (Quá đơn giản)**.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích Bias-Variance Tradeoff theo $k$:
- $k \\to 1$: Mô hình có độ phức tạp cao (High Model Complexity), sai số trên tập train bằng 0 ($Train\\_Acc = 100\\%$), nhưng phương sai rất lớn:
$$\\text{Var}[\\hat{f}(x)] \\text{ cao}, \\quad \\text{Bias}[\\hat{f}(x)] \\text{ thấp} \\implies \\text{Overfitting}$$
- $k \\to N$: Mô hình dự đoán nhãn cố định $\\hat{y} = \\arg\\max_c N_c$ cho mọi điểm đầu vào:
$$\\text{Bias}[\\hat{f}(x)] \\text{ cao}, \\quad \\text{Var}[\\hat{f}(x)] \\text{ thấp} \\implies \\text{Underfitting}$$
Do đó, ta luôn dùng Cross-Validation để tìm giá trị $k$ tối ưu ở vùng trũng của sai số kiểm định. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A & C:** Bị ngược hoàn toàn bản chất. Rất nhiều thí sinh nhầm tưởng $k$ lớn là nhớ nhiều nên overfit — thực tế $k$ lớn là lấy trung bình của nhiều người nên mô hình phẳng mượt và underfit!

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.1 k-NN & §1.5 Bias-Variance Tradeoff**.
🔗 **Liên hệ bài cũ:** Ở câu **C01**, ta đã biết k-NN lấy vote đa số của $k$ điểm láng giềng. Câu C02 khẳng định vai trò tối quan trọng của việc chọn $k$ phù hợp!"""
}

UPGRADES["OLP01-C03"] = {
    "prompt": "Trong thuật toán Support Vector Machine (SVM) tuyến tính dạng lề cứng (Hard-margin), khoảng cách lề (Margin) giữa hai siêu phẳng hỗ trợ phân tách hai lớp dữ liệu được tính bằng công thức nào?",
    "options": [
        {"key": "A", "text": "Margin = ||w|| / 2"},
        {"key": "B", "text": "Margin = 1 / ||w||^2"},
        {"key": "C", "text": "Margin = 2 / ||w||"},
        {"key": "D", "text": "Margin = 2 ||w||"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
SVM giống như một người mở đường: Cần xây một con đường cao tốc ngăn cách giữa hai ngôi làng.
Con đường cao tốc này phải có bề rộng lề (Margin) **càng rộng càng tốt** để xe cộ chạy an toàn không bị va chạm vào nhà dân hai bên.
Khoảng cách an toàn này tỉ lệ nghịch với độ dài của vector pháp tuyến $w$: Bề rộng lề chính là $\\frac{2}{\\|w\\|}$. Muốn lề to nhất, ta phải thu nhỏ $\\|w\\|$ lại!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Chứng minh toán học hình học:
Hai siêu phẳng hỗ trợ đi qua các điểm Support Vectors của hai lớp được định nghĩa bởi:
$$w^T x + b = +1 \\quad \\text{và} \\quad w^T x + b = -1$$
Vector pháp tuyến đơn vị vuông góc với hai siêu phẳng là $u = \\frac{w}{\\|w\\|}$.
Khoảng cách hình học giữa hai mặt phẳng song song này là hình chiếu của vector nối hai điểm trên hai mặt phẳng lên phương pháp tuyến:
$$\\text{Margin} = \\frac{(w^T x_1 + b) - (w^T x_2 + b)}{\\|w\\|} = \\frac{1 - (-1)}{\\|w\\|} = \\frac{2}{\\|w\\|}$$
Bài toán tối đa hóa lề $\\max_w \\frac{2}{\\|w\\|}$ tương đương với bài toán quy hoạch toàn phương lồi:
$$\\min_{w, b} \\frac{1}{2} \\|w\\|^2 \\quad \\text{s.t.} \\quad y_i(w^T x_i + b) \\ge 1, \\quad \\forall i=1,\\dots,N$$
Chọn đáp án **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A & D:** Đảo ngược vị trí của $\\|w\\|$ lên tử số. Nếu lề bằng $\\|w\\|/2$, khi tăng $\\|w\\|$ lên vô cùng lề sẽ to vô hạn $\\implies$ Vô lý hình học.
- **Phương án B:** Nhầm với hàm mục tiêu $\\frac{1}{2}\\|w\\|^2$ trong bài toán tối ưu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.2 Support Vector Machines (SVM)**.
🔗 Khái niệm độ rộng lề $\\frac{2}{\\|w\\|}$ là nền tảng để hiểu vì sao hàm mục tiêu SVM lại chứa số hạng $\\frac{1}{2}\\|w\\|^2$ — chính là số hạng L2 Regularization (Weight Decay) mà ta sẽ gặp lại ở câu C10!"""
}

UPGRADES["OLP01-C04"] = {
    "prompt": "Khi sử dụng SVM với hàm nhân RBF (Radial Basis Function Kernel), nếu siêu tham số $\\gamma$ (Gamma) được thiết lập ở giá trị quá lớn, mô hình sẽ có xu hướng:",
    "options": [
        {"key": "A", "text": "Trở thành một đường thẳng tuyến tính đơn giản và bị Underfitting"},
        {"key": "B", "text": "Không thể hội tụ trong quá trình tối ưu hóa"},
        {"key": "C", "text": "Khoảng cách lề tăng lên tối đa và bao trùm toàn bộ không gian"},
        {"key": "D", "text": "Ranh giới phân chia ôm sát cục bộ quanh từng điểm dữ liệu, dẫn đến Overfitting (High Variance)"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung siêu tham số Gamma như ngọn núi lửa:**
- Hàm RBF Kernel giống như việc bạn dựng một ngọn núi nhọn xung quanh mỗi điểm dữ liệu: $K(x, x') = \\exp(-\\gamma \\|x - x'\\|^2)$.
- **Khi Gamma rất nhỏ:** Chân núi thoai thoải và trải rộng khắp nơi, các ngọn núi hòa vào nhau thành một ngọn đồi mượt mà $\\implies$ Mô hình phẳng mượt.
- **Khi Gamma quá lớn:** Ngọn núi nhọn hoắt như cây kim và chỉ có bán kính ảnh hưởng cực kỳ hẹp. Mỗi điểm dữ liệu trở thành một chiếc gai nhọn riêng lẻ, mô hình chỉ chăm chăm nhớ từng điểm đơn lẻ $\\implies$ **Overfitting (Học vẹt, ranh giới phức tạp)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức RBF Kernel (Gaussian Kernel):
$$K(x, x') = \\exp(-\\gamma \\|x - x'\\|^2) = \\exp\\left(-\\frac{\\|x - x'\\|^2}{2\\sigma^2}\\right), \\quad \\gamma = \\frac{1}{2\\sigma^2}$$
- Khi $\\gamma \\to \\infty$ (tương đương $\\sigma \\to 0$):
$$K(x, x') \\to 0 \\quad \\text{với mọi } x \\ne x', \\quad K(x, x) = 1$$
Mỗi điểm dữ liệu huấn luyện chỉ tương tác với chính nó. Ma trận Kernel trở thành ma trận đơn vị $K \\approx I$.
Hàm quyết định $f(x) = \\text{sign}\\left(\\sum_{i} \\alpha_i y_i K(x_i, x) + b\\right)$ sẽ tạo ra các 'hòn đảo' cô lập quanh từng mẫu huấn luyện, gây ra hiện tượng **Overfitting trầm trọng**. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Bị ngược. Khi Gamma rất NHỎ ($\\gamma \\to 0$), RBF Kernel mới gần như tuyến tính và gây Underfitting.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.2 Support Vector Machines & RBF Kernel**.
🔗 **Mối liên hệ tương đồng:**
- Trong k-NN (câu C02): $k$ nhỏ $\\implies$ Overfitting.
- Trong SVM RBF (câu C04): $\\gamma$ lớn $\\implies$ Overfitting.
Cả hai đều cùng chung bản chất: Bán kính lân cận cục bộ bị thu hẹp quá mức!"""
}

UPGRADES["OLP01-C05"] = {
    "prompt": "Trong thuật toán cây quyết định ID3 và lý thuyết thông tin Shannon, độ hỗn loạn thông tin (Entropy) của phân phối xác suất rời rạc $p = (p_1, \\dots, p_C)$ được tính theo công thức nào và sử dụng logarit cơ số mấy?",
    "options": [
        {"key": "A", "text": "H(S) = - sum(p_i * log2(p_i)), sử dụng logarit cơ số 2 với đơn vị đo là bit (hoặc shannon)"},
        {"key": "B", "text": "H(S) = sum(p_i * ln(p_i)), sử dụng logarit tự nhiên với đơn vị là nat"},
        {"key": "C", "text": "H(S) = 1 - sum(p_i^2), sử dụng logarit cơ số 10"},
        {"key": "D", "text": "H(S) = - sum(p_i^2 * log2(p_i)), sử dụng logarit cơ số 2"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Vì sao lại là cơ số 2 và dấu trừ?**
- Vì trong máy tính, mọi thông tin đều được mã hóa bằng nhị phân (0 và 1). Cơ số 2 giúp mỗi bit thông tin đo lường tương đương với một câu hỏi Đúng/Sai (Yes/No).
- Do xác suất $p_i \\le 1$ nên $\\log_2(p_i)$ luôn là một số âm. Vì vậy Claude Shannon đã đặt thêm **dấu trừ ($-$)** ở phía trước để độ hỗn loạn Entropy luôn là một con số dương!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định nghĩa chuẩn của Shannon Entropy:
$$H(S) = - \\sum_{i=1}^C p_i \\log_2(p_i)$$
Quy ước: Nếu $p_i = 0$ thì $0 \\log_2(0) = \\lim_{p \\to 0^+} p \\log_2(p) = 0$.
- Đơn vị đo: **bit** (shannon) khi dùng $\\log_2$; nếu dùng $\\ln$ đơn vị là **nat**; nếu dùng $\\log_{10}$ đơn vị là **hartley**.
- Thuật toán cây quyết định ID3 và C4.5 chuẩn mực của Ross Quinlan sử dụng $\\log_2$ (bit). Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B:** Thiếu dấu trừ và dùng $\\ln$ (thường dùng trong hàm Cross-Entropy của Deep Learning, không phải chuẩn ID3).
- **Phương án C:** Đây là công thức của Gini Impurity trong thuật toán CART, không phải Entropy.
- **Phương án D:** Thừa số hạng $p_i^2$.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định & Shannon Entropy**.
🔗 Chúng ta đã trực tiếp áp dụng công thức này để tính tay ở câu **B04** ($H = 1$ bit) và câu **B05** ($IG = 1$ bit)!"""
}

UPGRADES["OLP01-C06"] = {
    "prompt": "Khi xây dựng cây quyết định (Decision Tree), tại mỗi nút phân chia, thuật toán ID3 lựa chọn thuộc tính nào để rẽ nhánh tiếp theo?",
    "options": [
        {"key": "A", "text": "Thuộc tính tạo ra nhiều nhánh con nhất có thể"},
        {"key": "B", "text": "Thuộc tính có Mức tăng thông tin (Information Gain — IG) lớn nhất"},
        {"key": "C", "text": "Thuộc tính có độ phức tạp tính toán nhỏ nhất"},
        {"key": "D", "text": "Thuộc tính có phương sai lớn nhất trong tập huấn luyện"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Nguyên lý chia để trị thông minh:**
Tưởng tượng bạn chơi trò đoán đồ vật bằng 20 câu hỏi Yes/No:
Bạn sẽ luôn muốn đặt câu hỏi nào mà sau khi nghe câu trả lời, bạn **loại bỏ được nhiều phương án nhất** (giảm độ hoang mang nhiều nhất).
Đó chính là câu hỏi có **Information Gain lớn nhất**! Thuật toán cây quyết định sẽ luôn ưu tiên thuộc tính này đặt lên đầu tiên để cây vừa ngắn vừa phân loại chuẩn nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tiêu chí lựa chọn thuộc tính tối ưu trong ID3:
$$A^* = \\arg\\max_{A} IG(S, A) = \\arg\\max_{A} \\left[ H(S) - \\sum_{v \\in \\text{Values}(A)} \\frac{|S_v|}{|S|} H(S_v) \\right]$$
Do $H(S)$ là hằng số đối với nút hiện tại, việc tối đa hóa $IG(S, A)$ tương đương với việc tối thiểu hóa Entropy còn lại của các nút con (Entropy sau phân chia càng gần 0 càng tốt). Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Đây chính là nhược điểm chí mạng của ID3 (thiên vị các thuộc tính có quá nhiều giá trị như ID khách hàng), làm cây bị overfit. Thuật toán C4.5 sau này đã sửa bằng cách dùng Gain Ratio.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định & Information Gain**.
🔗 Liên hệ trực tiếp với bài tập tính tay ở câu **B05**, nơi ta đã chứng minh thuộc tính có $IG = 1$ bit là sự lựa chọn tối ưu tuyệt đối!"""
}

UPGRADES["OLP01-C07"] = {
    "prompt": "Một kỹ sư AI huấn luyện mô hình phân loại ảnh và ghi nhận kết quả: Độ chính xác trên tập Train đạt 99.2%, nhưng độ chính xác trên tập Validation chỉ đạt 70.1% (chênh lệch tới gần 29%). Hiện tượng này là triệu chứng rõ rệt của vấn đề gì và giải pháp khắc phục là gì?",
    "options": [
        {"key": "A", "text": "Mô hình bị Underfitting; giải pháp là tăng số lượng tham số mô hình"},
        {"key": "B", "text": "Dữ liệu huấn luyện quá sạch; giải pháp là xóa bớt các nhãn chính xác"},
        {"key": "C", "text": "Mô hình bị Overfitting (High Variance); giải pháp là tăng cường dữ liệu (Data Augmentation), áp dụng Regularization (L1/L2, Dropout), và Early Stopping"},
        {"key": "D", "text": "Hiện tượng bình thường không cần xử lý"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bệnh 'Học vẹt' (Overfitting):**
- Học sinh làm bài tập ở nhà (tập Train) được 99 điểm vì chép thuộc lòng đáp án từng câu hỏi trong đề cương.
- Nhưng khi vào phòng thi gặp bài kiểm tra mới (tập Validation), học sinh này chỉ được 70 điểm vì không hiểu bản chất!
Khoảng cách chênh lệch khổng lồ giữa Train (99%) và Val (70%) chính là bằng chứng tố cáo mô hình đang **Học vẹt (Overfitting)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân rã sai số kỳ vọng:
$$\\text{Generalization Error} = \\text{Validation Loss} - \\text{Train Loss}$$
Khi Generalization Error lớn và $\\text{Train Loss} \\to 0$, mô hình có Phương sai cao (High Variance): Mô hình ghi nhớ cả các nhiễu ngẫu nhiên trong tập train.
Các giải pháp kỹ thuật đã được chứng minh hiệu quả:
1. **Thu hẹp không gian trọng số:** Thêm phạt $\\lambda \\|w\\|_2^2$ (L2 Regularization / Weight Decay) hoặc Dropout.
2. **Mở rộng dữ liệu:** Data Augmentation (xoay, lật, cắt ảnh), thu thập thêm dữ liệu thật.
3. **Cắt ngang quá trình học:** Early Stopping (dừng train khi Val Loss bắt đầu tăng). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Underfitting là khi cả Train Acc và Val Acc đều thấp (ví dụ Train 65%, Val 60%).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.5 Overfitting, Underfitting & Bias-Variance Tradeoff**.
🔗 Ở câu **C08**, **C09**, **C10** tiếp theo, ta sẽ đi sâu vào các công cụ mạnh mẽ nhất để triệt tiêu căn bệnh Overfitting này!"""
}

UPGRADES["OLP01-C08"] = {
    "prompt": "Khi đánh giá hiệu năng mô hình trên tập dữ liệu phân loại có mất cân bằng lớp nghiêm trọng (Imbalanced Data), kỹ thuật Cross-Validation nào là BẮT BUỘC phải áp dụng?",
    "options": [
        {"key": "A", "text": "K-Fold ngẫu nhiên thông thường (Standard K-Fold)"},
        {"key": "B", "text": "Leave-One-Out Cross-Validation (LOOCV)"},
        {"key": "C", "text": "Chỉ chia một lần Train/Val ngẫu nhiên không cần lặp"},
        {"key": "D", "text": "Stratified K-Fold Cross-Validation (K-Fold phân tầng)"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Vì sao K-Fold thường bị hỏng khi gặp dữ liệu lệch?**
Giả sử bài toán phát hiện gian lận chỉ có 1% mẫu gian lận.
Nếu dùng K-Fold ngẫu nhiên chia thành 10 phần: Rất có thể Fold số 1 không có một mẫu gian lận nào, trong khi Fold số 5 lại chứa hết cả đám! Kết quả chấm điểm sẽ nhảy lung tung và không đáng tin cậy.
**Stratified K-Fold (Phân tầng):** Bắt buộc mỗi Fold đều phải giữ nguyên tỉ lệ chính xác 1% gian lận và 99% bình thường, giúp bài thi thử phản ánh trung thực năng lực của mô hình!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nguyên lý chia mẫu phân tầng:
Cho tập dữ liệu $D$ với $C$ lớp, tỉ lệ mỗi lớp là $p_c = \\frac{N_c}{N}$.
Stratified K-Fold phân chia $D$ thành $K$ tập con không giao nhau $D_1, \\dots, D_K$ sao cho trong mỗi fold $D_k$:
$$\\frac{|D_k \\cap \\text{Class } c|}{|D_k|} = p_c \\pm \\epsilon, \\quad \\forall c \\in \\{1, \\dots, C\\}$$
Chọn đáp án **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Standard K-Fold không đảm bảo tỉ lệ lớp, rất dễ làm mất hoàn toàn lớp thiểu số trong tập kiểm định.
- **Phương án B:** LOOCV có chi phí tính toán cực kỳ đắt đỏ (huấn luyện $N$ lần) và phương sai kiểm định rất lớn.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.5 K-Fold Cross-Validation & §5.6 Chiến lược lấy mẫu**.
🔗 **Mối liên hệ mật thiết:** Ở câu **A11**, ta đã biết Stratified Sampling khi chia tập đơn. Đến câu **C08**, kỹ thuật này được nâng cấp thành quy trình kiểm định chéo $K$ lần hoàn chỉnh!"""
}

UPGRADES["OLP01-C09"] = {
    "prompt": "Điểm khác biệt cốt lõi về mặt toán học và ứng dụng của kỹ thuật điều chuẩn L1 Regularization (Lasso) so với L2 Regularization (Ridge) là gì?",
    "options": [
        {"key": "A", "text": "L1 có khả năng ép chính xác nhiều trọng số w về đúng bằng 0, tạo ra mô hình thưa (Sparsity) và thực hiện chọn lọc đặc trưng tự động (Feature Selection)"},
        {"key": "B", "text": "L1 luôn giữ lại tất cả các đặc trưng và chỉ giảm đều trọng số"},
        {"key": "C", "text": "L1 không có khả năng chống hiện tượng Overfitting"},
        {"key": "D", "text": "L1 chỉ dùng được cho bài toán phân loại nhị phân"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
- **L2 (Ridge - Người hòa giải):** Giống như bắt tất cả các nơ-ron phải cùng nhau giảm bớt cân nặng, các trọng số nhỏ đều về gần 0 nhưng **không bao giờ biến mất hoàn toàn**.
- **L1 (Lasso - Lưỡi gươm dứt khoát):** Giống như một cuộc thanh lọc: Trọng số nào không thực sự quan trọng sẽ bị chém đứt **về chính xác số 0**!
Nhờ vậy, L1 giúp ta tự động vứt bỏ các cột dữ liệu thừa thãi, chỉ giữ lại những đặc trưng tinh túy nhất (**Chọn lọc đặc trưng tự động**)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 So sánh toán học hàm mất mát:
$$\\mathcal{L}_{\\text{L1}}(w) = \\mathcal{L}_0(w) + \\lambda \\sum_{j=1}^d |w_j|$$
$$\\mathcal{L}_{\\text{L2}}(w) = \\mathcal{L}_0(w) + \\frac{\\lambda}{2} \\sum_{j=1}^d w_j^2$$
- Dưới góc nhìn hình học: Đường đẳng mức của chuẩn $L_1$ là hình thoi có các góc nhọn nằm ngay trên các trục tọa độ. Khi elip hàm loss $\\mathcal{L}_0$ tiếp xúc với hình thoi, điểm tiếp xúc tối ưu hầu như luôn rơi vào các góc nhọn trên trục tọa độ, nơi các tọa độ khác có $w_j = 0$ tuyệt đối.
- Dưới góc nhìn Bayes (câu A08): L1 tương đương tiên nghiệm Laplace Prior (phân phối có đỉnh nhọn tại 0). Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B:** Mô tả đặc tính của L2 Ridge, không phải L1.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.6 Regularization L1 vs L2**.
🔗 Ngay ở câu tiếp theo **C10**, ta sẽ đối chiếu với ưu thế vượt trội của L2 Ridge khi dữ liệu có hiện tượng đa cộng tuyến!"""
}

UPGRADES["OLP01-C10"] = {
    "prompt": "Trong trường hợp tập dữ liệu chứa nhiều đặc trưng có độ tương quan tuyến tính rất cao với nhau (hiện tượng Đa cộng tuyến — Multicollinearity), kỹ thuật L2 Regularization (Ridge) thường được ưu tiên hơn L1 (Lasso) vì lý do gì?",
    "options": [
        {"key": "A", "text": "Vì L1 sẽ chọn ngẫu nhiên 1 đặc trưng và loại bỏ các đặc trưng còn lại một cách không ổn định, trong khi L2 co đều các hệ số trọng số và luôn đảm bảo ma trận (X^T X + lambda I) khả nghịch"},
        {"key": "B", "text": "Vì L2 tính toán không cần ma trận"},
        {"key": "C", "text": "Vì L2 luôn đưa toàn bộ trọng số về chính xác bằng 0"},
        {"key": "D", "text": "Vì L2 không cần siêu tham số lambda"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Tưởng tượng có 3 người bạn làm việc nhóm hệt như nhau (3 đặc trưng tương quan mạnh):
- **L1 Lasso:** Sẽ bốc thăm ngẫu nhiên chọn 1 người và sa thải 2 người còn lại. Lần sau chạy lại có thể nó lại chọn người khác $\\implies$ Kết quả rất bất ổn định!
- **L2 Ridge:** Chia đều trách nhiệm cho cả 3 người, hạ bớt gánh nặng của mỗi người xuống một chút để cùng nhau gánh vác $\\implies$ Mô hình rất ổn định và bền vững!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nghiệm giải tích của Ridge Regression:
Khi có đa cộng tuyến, ma trận Gram $\\mathbf{X}^T \\mathbf{X}$ bị suy biến (Singular) hoặc gần suy biến, định thức $\\approx 0$ khiến nghịch đảo $(\\mathbf{X}^T \\mathbf{X})^{-1}$ phát nổ phương sai.
Với L2 Regularization:
$$\\hat{\\mathbf{w}}_{\\text{Ridge}} = (\\mathbf{X}^T \\mathbf{X} + \\lambda \\mathbf{I})^{-1} \\mathbf{X}^T \\mathbf{y}$$
Do $\\lambda > 0$, ma trận $\\mathbf{X}^T \\mathbf{X} + \\lambda \\mathbf{I}$ luôn luôn **xác định dương (Positive Definite)** và đảm bảo khả nghịch 100%, triệt tiêu hoàn toàn sự bấp bênh của đa cộng tuyến. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án C:** Ép trọng số về 0 là tính chất của L1 (câu C09).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.6 Regularization L1 vs L2**.
🔗 **Cặp bài trùng L1 vs L2:**
- Câu C09: Khi cần loại bỏ biến thừa $\\implies$ Dùng L1 Lasso (Sparse).
- Câu C10: Khi các biến dính líu tương quan $\\implies$ Dùng L2 Ridge (Weight Decay).
Khi muốn cả hai: Dùng **ElasticNet** (kết hợp cả L1 và L2)!"""
}

UPGRADES["OLP01-C11"] = {
    "prompt": "Vì sao thuật toán tối ưu hóa Adam (Adaptive Moment Estimation) thường được coi là thuật toán tối ưu mặc định đầu tiên khi huấn luyện các mô hình Deep Learning hiện đại?",
    "options": [
        {"key": "A", "text": "Vì Adam luôn đảm bảo tìm được nghiệm cực tiểu toàn cục (Global Minimum) trong mọi bài toán"},
        {"key": "B", "text": "Vì Adam không cần sử dụng gradient"},
        {"key": "C", "text": "Vì Adam kết hợp ưu điểm của Momentum (quán tính) và RMSprop (tốc độ học thích ứng theo từng tham số), hội tụ nhanh và ít phụ thuộc vào việc tinh chỉnh learning rate ban đầu"},
        {"key": "D", "text": "Vì Adam tiêu tốn ít bộ nhớ GPU hơn SGD thuần"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Adam = Hòn đá lăn có trớn (Momentum) + Chiếc phanh thông minh (RMSprop):**
- **Momentum (Moment bậc 1):** Giống như hòn đá lăn xuống dốc, có trớn đẩy nó vượt qua những ổ gà gập ghềnh (cực tiểu địa phương) mà không bị kẹt lại.
- **RMSprop (Moment bậc 2):** Đo độ dốc của từng bánh xe. Tham số nào có độ dốc quá lớn thì phanh chậm lại, tham số nào độ dốc phẳng lì thì nhấn ga chạy nhanh hơn (Learning rate thích ứng riêng cho từng nơ-ron).
Nhờ kết hợp cả hai, Adam leo đèo lội suối rất nhanh và bạn không cần phải tốn công vất vả dò tìm Learning rate!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Các bước cập nhật của Adam:
1. Moment bậc 1 (Trung bình động gradient có quán tính):
$$m_t = \\beta_1 m_{t-1} + (1 - \\beta_1) g_t$$
2. Moment bậc 2 (Trung bình động bình phương gradient):
$$v_t = \\beta_2 v_{t-1} + (1 - \\beta_2) g_t^2$$
3. Hiệu chỉnh độ lệch ban đầu (Bias correction):
$$\\hat{m}_t = \\frac{m_t}{1 - \\beta_1^t}, \\quad \\hat{v}_t = \\frac{v_t}{1 - \\beta_2^t}$$
4. Cập nhật tham số:
$$\\theta_t = \\theta_{t-1} - \\frac{\\eta}{\\sqrt{\\hat{v}_t} + \\epsilon} \\hat{m}_t$$
Giá trị mặc định chuẩn: $\\beta_1 = 0.9, \\beta_2 = 0.999, \\epsilon = 10^{-8}$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Mạng nơ-ron sâu là bài toán tối ưu phi lồi (Non-convex), không thuật toán nào cam kết tìm được cực tiểu toàn cục.
- **Phương án D:** Adam tốn bộ nhớ gấp 3 lần SGD thuần vì phải lưu thêm 2 tensor $m_t$ và $v_t$ cho từng tham số.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.5 Các thuật toán tối ưu hóa (Optimizers)**.
🔗 Trong huấn luyện Transformer hiện đại, biến thể **AdamW** (Adam kèm Weight Decay tách rời) là chuẩn mực số 1 thế giới!"""
}

UPGRADES["OLP01-C12"] = {
    "prompt": "Trong các chiến lược điều chỉnh tốc độ học (Learning Rate Scheduling) hiện đại cho Transformer và ResNet, chiến lược nào được coi là chuẩn mực tối ưu nhất?",
    "options": [
        {"key": "A", "text": "Khởi đầu bằng learning rate cực lớn và tiếp tục tăng dần theo từng epoch"},
        {"key": "B", "text": "Giữ learning rate cố định ở mức siêu nhỏ (1e-6) từ đầu đến cuối"},
        {"key": "C", "text": "Thay đổi learning rate ngẫu nhiên sau mỗi batch"},
        {"key": "D", "text": "Sử dụng giai đoạn khởi động làm ấm (Warmup: tăng tuyến tính từ 0 lên cực đại) kết hợp với suy giảm dần theo hàm Cosine (Cosine Annealing Decay)"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Chiến lược lái xe chuyên nghiệp:**
1. **Giai đoạn khởi động (Warmup):** Khi mô hình mới xuất phát, các trọng số còn hỗn loạn. Nếu đạp ga hết cỡ ngay lập tức, xe sẽ bị lật bánh (gradient phát nổ). Ta phải khởi động từ từ, tăng nhẹ ga từ 0 lên tốc độ tối đa trong vài vòng đầu.
2. **Giai đoạn hạ ga (Cosine Decay):** Khi xe đã gần đến đích (mô hình đã học được các nét cơ bản), ta từ từ nhả chân ga nhẹ nhàng theo hình sóng êm ái (Cosine) để xe đỗ vừa khít vào điểm đỗ tối ưu nhất mà không bị vọt lố qua đà!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Cosine Decay with Linear Warmup:
1. Khi $t \\le T_{\\text{warmup}}$:
$$\\eta_t = \\eta_{\\text{max}} \\cdot \\frac{t}{T_{\\text{warmup}}}$$
2. Khi $T_{\\text{warmup}} < t \\le T_{\\text{total}}$:
$$\\eta_t = \\eta_{\\text{min}} + \\frac{1}{2} (\\eta_{\\text{max}} - \\eta_{\\text{min}}) \\left(1 + \\cos\\left(\\pi \\frac{t - T_{\\text{warmup}}}{T_{\\text{total}} - T_{\\text{warmup}}}\\right)\\right)$$
Chiến lược này giúp mô hình ổn định tuyệt đối ở giai đoạn đầu và đạt độ hội tụ cực tiểu sâu nhất ở giai đoạn cuối. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Làm mô hình phát nổ gradient (Divergence / NaN).
- **Phương án B:** Học quá chậm, dễ bị mắc kẹt ở điểm yên ngựa (Saddle point).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.6 Kỹ thuật điều chỉnh Learning Rate**.
🔗 Chiến lược Linear Warmup + Cosine Annealing là cấu hình mặc định trong bài báo gốc của Vision Transformer (ViT), BERT, GPT-3, và LLaMA!"""
}

UPGRADES["OLP01-C13"] = {
    "prompt": "Kiến trúc mạng tích chập kinh điển VGGNet (Simonyan & Zisserman, 2014) nổi tiếng với nguyên lý thiết kế đột phá nào sau đây?",
    "options": [
        {"key": "A", "text": "Thay thế các kernel tích chập kích thước lớn (như 5x5, 7x7) bằng việc xếp chồng nhiều tầng tích chập nhỏ 3x3 liên tiếp"},
        {"key": "B", "text": "Chỉ sử dụng kernel kích thước 11x11 ở mọi tầng tích chập"},
        {"key": "C", "text": "Sử dụng đường tắt Residual Connection bỏ qua các tầng nơ-ron"},
        {"key": "D", "text": "Sử dụng cơ chế Self-Attention thay cho toàn bộ các lớp tích chập"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Phép thuật của việc ghép hai chiếc kính nhỏ 3x3:**
Thay vì dùng một chiếc kính lúp cồng kềnh $5 \\times 5$:
VGG xếp chồng **hai chiếc kính nhỏ $3 \\times 3$ liên tiếp**:
- Cả hai cách đều có cùng tầm nhìn (Vùng tiếp nhận Receptive Field) bằng đúng $5 \\times 5$!
- Nhưng hai chiếc kính $3 \\times 3$ chỉ tốn $2 \\times (3 \\times 3) = 18$ trọng số, trong khi chiếc kính $5 \\times 5$ tốn tận $25$ trọng số (tiết kiệm $28\\%$ phép tính).
- Hơn thế nữa, giữa 2 tầng $3 \\times 3$ ta được chèn thêm một hàm kích hoạt ReLU, giúp mô hình học được nhiều đường cong phi tuyến phức tạp hơn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Chứng minh toán học:
1. **Receptive Field (RF):**
$$\\text{RF}_2 = \\text{RF}_1 + (K_2 - 1) = 3 + (3 - 1) = 5$$
Hai lớp Conv $3 \\times 3$ tương đương một lớp Conv $5 \\times 5$. Ba lớp Conv $3 \\times 3$ tương đương một lớp Conv $7 \\times 7$.
2. **Số lượng tham số (với $C$ kênh):**
- Một lớp $7 \\times 7$: $7^2 \\cdot C^2 = 49 C^2$.
- Ba lớp $3 \\times 3$: $3 \\cdot (3^2 \\cdot C^2) = 27 C^2$ (giảm tới $45\\%$ tham số).
Chọn đáp án **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B:** Kernel $11 \\times 11$ là đặc trưng của AlexNet (tầng 1).
- **Phương án C:** Residual Connection là của ResNet (2015).
- **Phương án D:** Self-Attention là của Vision Transformer (ViT, 2020).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§3.3 Lịch sử các kiến trúc CNN kinh điển**.
🔗 Nhờ nguyên lý xếp chồng $3 \\times 3$ này, ta đã tính toán kích thước đầu ra $32 \\times 32$ rất dễ dàng ở câu **B01**!"""
}

UPGRADES["OLP01-C14"] = {
    "prompt": "Điểm khác biệt cốt lõi giữa kết nối tắt (Skip Connection) trong kiến trúc ResNet so với U-Net là gì?",
    "options": [
        {"key": "A", "text": "ResNet sử dụng phép nối chuỗi (Concatenation), còn U-Net sử dụng phép cộng phần tử (Element-wise Addition)"},
        {"key": "B", "text": "ResNet sử dụng phép cộng phần tử (Element-wise Addition: F(x) + x) để bảo toàn số kênh, trong khi U-Net sử dụng phép nối chuỗi (Concatenation) dọc theo trục kênh để ghép đặc trưng từ Encoder sang Decoder"},
        {"key": "C", "text": "Cả hai đều sử dụng phép nhân ma trận"},
        {"key": "D", "text": "ResNet không hề có kết nối tắt"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Phép Cộng (Add) vs Phép Ghép (Concat):**
- **ResNet (Phép Cộng):** Giống như bạn lấy 2 tờ giấy trong suốt vẽ cùng kích thước đặt đè lên nhau rồi cộng nét lại ($F(x) + x$). Kích thước và số lượng kênh không hề thay đổi, siêu nhẹ nhàng và giúp đạo hàm trôi tuột về các tầng trước mà không bị chặn lại!
- **U-Net (Phép Ghép):** Giống như bạn lấy cả chồng giấy bản đồ chi tiết của bên Encoder đem dán dính cạnh vào chồng giấy của Decoder ($torch.cat([x_1, x_2], dim=1)$). Số lượng kênh sẽ bị tăng gấp đôi!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 So sánh hai cơ chế:
1. **ResNet Residual Block (He et al., 2015):**
$$y = \\mathcal{F}(x, \\{W_i\\}) + x$$
Phép cộng phần tử `torch.add(F_x, x)` yêu cầu $\\mathcal{F}(x)$ và $x$ phải có cùng số kênh và cùng kích thước không gian.
Đạo hàm lan truyền ngược:
$$\\frac{\\partial \\mathcal{E}}{\\partial x} = \\frac{\\partial \\mathcal{E}}{\\partial y} \\left( \\frac{\\partial \\mathcal{F}}{\\partial x} + 1 \\right)$$
Số hạng $+1$ bảo đảm gradient không bao giờ bị triệt tiêu về 0!
2. **U-Net Skip Connection (Ronneberger et al., 2015):**
$$y = [\\mathcal{F}_{\\text{encoder}}, \\mathcal{F}_{\\text{decoder}}]$$
Phép nối kênh `torch.cat([feat_enc, feat_dec], dim=1)` giúp Decoder khôi phục lại các chi tiết không gian sắc nét của ảnh gốc. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Bị đảo ngược vị trí giữa ResNet và U-Net.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§3.3 ResNet & §3.4 U-Net Segmentation**.
🔗 Ta sẽ tiếp tục gặp lại câu hỏi chuyên sâu về U-Net ở câu **C23**!"""
}

UPGRADES["OLP01-C15"] = {
    "prompt": "Thuật toán Triệt tiêu Phi cực đại (Non-Maximum Suppression — NMS) đóng vai trò gì trong giai đoạn hậu xử lý (Post-processing) của các mô hình phát hiện vật thể (Object Detection như YOLO, Faster R-CNN)?",
    "options": [
        {"key": "A", "text": "Tăng kích thước tất cả các bounding box để bao trọn vật thể"},
        {"key": "B", "text": "Tính toán hàm mất mát hồi quy tọa độ (Bounding Box Loss)"},
        {"key": "C", "text": "Lọc bỏ các bounding box bị trùng lặp xung quanh cùng một vật thể, chỉ giữ lại chiếc hộp có điểm tin cậy (Confidence Score) cao nhất"},
        {"key": "D", "text": "Chuyển đổi ảnh màu RGB sang ảnh xám để tăng tốc độ xử lý"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Khi nhìn một chú chó trong ảnh, mô hình AI quá hăng hái nên đã vẽ ra **hàng chục chiếc khung chữ nhật** đè chằng chịt lên cùng chú chó đó!
Nếu để nguyên thì bức ảnh trông sẽ như một mớ mạng nhện.
**Thuật toán NMS** đóng vai trò như trọng tài:
1. Tìm chiếc khung đẹp nhất, có điểm tin cậy cao nhất của chú chó.
2. Quét tất cả các chiếc khung xung quanh: Khung nào đè trùng lên chiếc khung đẹp nhất này (có $IoU \\ge 0.5$, như câu B06) thì **xóa sổ ngay lập tức**!
Kết quả: Mỗi chú chó chỉ còn lại duy nhất một chiếc khung chuẩn nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Quy trình thuật toán NMS:
1. Đầu vào: Tập các hộp $\\mathcal{B} = \\{b_1, \\dots, b_m\\}$ kèm điểm số tương ứng $\\mathcal{S} = \\{s_1, \\dots, s_m\\}$, ngưỡng $\\text{IoU}_{\\text{thresh}}$ (thường là $0.45 - 0.5$).
2. Khởi tạo tập kết quả giữ lại $\\mathcal{D} = \\emptyset$.
3. Trong khi $\\mathcal{B} \\ne \\emptyset$:
   - Chọn hộp $m = \\arg\\max s_i$ trong $\\mathcal{B}$.
   - Đưa $m$ vào $\\mathcal{D}$, xóa $m$ khỏi $\\mathcal{B}$.
   - Với mọi hộp $b_i \\in \\mathcal{B}$: Nếu $\\text{IoU}(m, b_i) \\ge \\text{IoU}_{\\text{thresh}}$, xóa $b_i$ khỏi $\\mathcal{B}$.
4. Trả về tập các hộp tối ưu $\\mathcal{D}$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- NMS là bước hậu xử lý (Inference time post-processing), không tham gia vào quá trình tính Loss hay backprop.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện vật thể & Thuật toán NMS**.
🔗 NMS sử dụng trực tiếp công thức tính **IoU** mà ta đã thực hành tính tay ở câu **B06**!"""
}

# Nạp tiếp C16 đến C30 và E01 đến E04
# (Để đảm bảo code súc tích, nạp các câu còn lại chuẩn xác 100%)

C_REMAINING = {
    "OLP01-C16": {
        "prompt": "So sánh đúng đắn nhất giữa hai họ mô hình phát hiện vật thể: 1-stage detector (như YOLO, SSD) và 2-stage detector (như Faster R-CNN) là gì?",
        "options": [
            {"key": "A", "text": "YOLO luôn chính xác hơn Faster R-CNN trong mọi bài toán"},
            {"key": "B", "text": "Faster R-CNN chạy nhanh hơn YOLO và phù hợp cho thiết bị di động"},
            {"key": "C", "text": "Cả hai đều không cần sử dụng thuật toán NMS"},
            {"key": "D", "text": "Mô hình 1-stage (YOLO) dự đoán trực tiếp tọa độ và lớp trong 1 lần quét nên đạt tốc độ Real-time rất cao; trong khi 2-stage (Faster R-CNN) đề xuất vùng (RPN) trước rồi mới phân loại nên chính xác hơn ở vật thể nhỏ nhưng tốc độ chậm hơn"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **1-Stage (YOLO - Vận động viên chạy nước rút):**
Quét qua bức ảnh đúng một lần là chỉ ngay ra vị trí và tên các con vật. Tốc độ cực nhanh (trên 60 khung hình/giây), chạy mượt mà theo thời gian thực trên camera và điện thoại!
👶 **2-Stage (Faster R-CNN - Thám tử tỉ mỉ):**
- Bước 1: Dùng kính lúp khoanh tròn các vùng nghi ngờ có vật thể (Region Proposal Network).
- Bước 2: Soi kỹ từng vùng đó để kết luận. Rất chính xác (nhất là với các đồ vật tí hon), nhưng tốn nhiều thời gian hơn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
- 1-stage: Bài toán hồi quy trực tiếp từ tensor đặc trưng $S \\times S \\times (B \\cdot 5 + C)$.
- 2-stage: Gồm hai mạng nối tiếp RPN + RoI Pooling/RoIAlign + Classification Head.
Chọn đáp án **D**.

### 3. Bẫy đề thi & Pitfalls
Thường bẫy ở tốc độ và độ chính xác: YOLO thiên về tốc độ (Real-time), Faster R-CNN thiên về độ chính xác chi tiết.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§3.6 Phát hiện vật thể (1-Stage vs 2-Stage)**."""
    },
    "OLP01-C17": {
        "prompt": "Vì sao mô hình Rừng ngẫu nhiên (Random Forest) có khả năng chống hiện tượng Overfitting vượt trội hơn hẳn so với một Cây quyết định đơn lẻ (Decision Tree)?",
        "options": [
            {"key": "A", "text": "Nhờ kết hợp kỹ thuật lấy mẫu lặp lại (Bootstrap Aggregating) và ngẫu nhiên hóa không gian đặc trưng (Random Subspace) giúp giảm phương sai (Variance Reduction)"},
            {"key": "B", "text": "Vì Random Forest không bao giờ bị overfit trong bất kỳ tình huống nào"},
            {"key": "C", "text": "Vì mỗi cây trong rừng chỉ được huấn luyện trên 1 mẫu dữ liệu duy nhất"},
            {"key": "D", "text": "Vì Random Forest triệt tiêu hoàn toàn độ chệch (Bias)"}
        ],
        "answer": "A",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 Một cây quyết định đơn lẻ giống như một chuyên gia bảo thủ: Rất dễ bị học vẹt và phán đoán sai lầm.
Rừng ngẫu nhiên (Random Forest) tập hợp ý kiến của **100 người khác nhau**:
- Mỗi người được cho xem một góc nhìn khác nhau của cuốn sách (Bootstrap sample).
- Ở mỗi câu hỏi, mỗi người chỉ được nhìn vào một vài gợi ý ngẫu nhiên (Random features).
Khi gom 100 ý kiến độc lập đó lại để biểu quyết (Voting), các sai sót cá nhân sẽ tự triệt tiêu lẫn nhau, giúp kết quả chung vô cùng sáng suốt và ổn định!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Phương sai của trung bình $B$ biến ngẫu nhiên có tương quan $\\rho$ và phương sai $\\sigma^2$:
$$\\text{Var}(\\bar{X}) = \\rho \\sigma^2 + \\frac{1 - \\rho}{B} \\sigma^2$$
Nhờ ngẫu nhiên hóa đặc trưng tại mỗi node ($m \\approx \\sqrt{p}$), Random Forest giảm thiểu hệ số tương quan $\\rho$ giữa các cây, từ đó kéo tụt phương sai $\\text{Var}$ của toàn bộ mô hình xuống mức tối thiểu! Chọn **A**.

### 3. Bẫy đề thi & Pitfalls
Random Forest vẫn có thể bị overfit nếu dữ liệu quá nhiễu hoặc số lượng cây quá ít. Nó giảm Variance là chính, không phải giảm Bias.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§1.4 Random Forest & Phương pháp Ensemble**."""
    },
    "OLP01-C18": {
        "prompt": "Khi đánh giá chất lượng phân cụm của thuật toán K-Means mà không có nhãn thực tế, chỉ số Silhouette Score được sử dụng như thế nào?",
        "options": [
            {"key": "A", "text": "Silhouette Score âm càng sâu chứng tỏ các cụm càng tách bạch"},
            {"key": "B", "text": "Silhouette Score nằm trong khoảng [-1, 1]; giá trị trung bình càng gần 1 chứng tỏ các cụm dữ liệu phân tách rõ ràng và liên kết nội bộ chặt chẽ"},
            {"key": "C", "text": "Silhouette Score chỉ dùng cho bài toán học có giám sát"},
            {"key": "D", "text": "Silhouette Score đo lường tỉ lệ giữa Precision và Recall"}
        ],
        "answer": "B",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Chỉ số Silhouette (Đo độ hạnh phúc của từng điểm dữ liệu):**
- $a(i)$: Khoảng cách từ bạn đến các bạn cùng nhóm (Càng nhỏ càng tốt - nội bộ đoàn kết).
- $b(i)$: Khoảng cách từ bạn đến nhóm hàng xóm gần nhất (Càng lớn càng tốt - phân tách rõ ràng).
Nếu điểm số gần bằng **+1**: Bạn rất gần bạn cùng nhóm và ở rất xa người nhóm khác $\\implies$ Chia nhóm xuất sắc!
Nếu điểm số bị **âm (< 0)**: Bạn bị xếp nhầm nhóm rồi, bạn gần nhóm hàng xóm hơn nhóm của mình!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
$$s(i) = \\frac{b(i) - a(i)}{\\max(a(i), b(i))}, \\quad s(i) \\in [-1, 1]$$
Giá trị trung bình toàn bộ tập dữ liệu càng gần 1 thì cấu trúc phân cụm càng lý tưởng. Chọn **B**.

### 3. Bẫy đề thi & Pitfalls
Nhầm giá trị âm là tốt, hoặc nhầm sang bài toán học có giám sát.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§1.8 Phân cụm K-Means & Độ đo Silhouette**."""
    },
    "OLP01-C19": {
        "prompt": "Trong một bài toán phát hiện giao dịch gian lận với tỉ lệ mất cân bằng cực hạn (1 ca gian lận trên 99 ca bình thường), giải pháp kết hợp nào sau đây là CHUẨN MỰC NHẤT?",
        "options": [
            {"key": "A", "text": "Sử dụng độ đo Accuracy để đánh giá và dừng huấn luyện khi đạt 99%"},
            {"key": "B", "text": "Áp dụng kỹ thuật Undersampling xóa bớt nhóm gian lận"},
            {"key": "C", "text": "Sử dụng kỹ thuật SMOTE (hoặc Class Weights / Focal Loss) để xử lý mất cân bằng và bắt buộc đánh giá bằng F1-score / PR-AUC thay cho Accuracy"},
            {"key": "D", "text": "Nhân bản y nguyên các mẫu gian lận lên 100 lần (Oversampling thuần túy không sinh mới)"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Cái bẫy lừa người của Accuracy 99%:**
Một mô hình ngốc nghếch chỉ cần đoán 'TẤT CẢ ĐỀU BÌNH THƯỜNG' thì cũng đã đạt ngay độ chính xác **99%** mà không cần học hành gì cả! Nhưng nó hoàn toàn vô dụng vì để lọt 100% tội phạm gian lận.
Vì vậy, ta phải:
1. Dùng thuật toán **SMOTE** (sinh thêm các điểm gian lận nhân tạo nằm giữa các điểm cũ) hoặc phạt nặng khi đoán sai ca gian lận (**Class Weights / Focal Loss**).
2. Chấm điểm bằng **F1-Score / PR-AUC** (như đã học ở câu B08) để đo đúng năng lực bắt tội phạm!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
SMOTE (Synthetic Minority Over-sampling Technique):
$$x_{\\text{new}} = x_i + \\lambda (x_{zi} - x_i), \\quad \\lambda \\sim U(0, 1)$$
Chọn đáp án **C**.

### 3. Bẫy đề thi & Pitfalls
Tin vào Accuracy khi dữ liệu mất cân bằng là sai lầm sơ đẳng nhất trong AI.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§1.9 Xử lý dữ liệu mất cân bằng (Imbalanced Data)**. Liên hệ lại câu **A11** và câu **B08**."""
    },
    "OLP01-C20": {
        "prompt": "Trong thiết kế mạng nơ-ron sâu hiện đại, lựa chọn hàm kích hoạt (Activation Function) nào sau đây là CHUẨN XÁC NHẤT cho các tầng ẩn (Hidden layers) và tầng đầu ra (Output layer)?",
        "options": [
            {"key": "A", "text": "Tầng ẩn dùng Sigmoid vì đạo hàm mượt; tầng ra dùng Softmax cho mọi bài toán"},
            {"key": "B", "text": "Tầng ẩn dùng Softmax để chuẩn hóa; tầng ra dùng ReLU"},
            {"key": "C", "text": "Không cần dùng bất kỳ hàm kích hoạt nào nếu mạng đã đủ sâu"},
            {"key": "D", "text": "Tầng ẩn dùng ReLU hoặc GELU/SiLU để tránh triệt tiêu gradient; tầng ra dùng Sigmoid (cho nhị phân/đa nhãn) hoặc Softmax (cho đa lớp loại trừ nhau)"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Quy tắc chọn hàm kích hoạt:**
- **Tầng ẩn bên trong (Hidden):** Phải dùng **ReLU hoặc GELU/SiLU**. Vì hàm Sigmoid cũ kỹ có độ dốc quá phẳng ở hai đầu, khiến đạo hàm bị triệt tiêu (biến mất về 0) khi mạng đi sâu. ReLU có đạo hàm bằng 1 ở miền dương, giúp tín hiệu chảy băng băng qua hàng trăm tầng!
- **Tầng ra (Output):** Tùy thuộc bài thi:
  + Chọn 1 trong nhiều phương án (loại trừ nhau): Dùng **Softmax** (tổng xác suất = 100%).
  + Có/Không hoặc gán nhiều nhãn cùng lúc: Dùng **Sigmoid** (mỗi lớp độc lập từ 0 đến 1).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
- Nếu không có phi tuyến: Tích các ma trận $W_L \\dots W_2 W_1 x = W_{\\text{eff}} x$ suy biến thành một mô hình tuyến tính đơn giản!
- Đạo hàm Sigmoid: $\\sigma'(z) = \\sigma(z)(1 - \\sigma(z)) \\le 0.25$. Qua 10 tầng, gradient giảm $0.25^{10} \\approx 10^{-6}$ (Vanishing Gradient).
Chọn đáp án **D**.

### 3. Bẫy đề thi & Pitfalls
Dùng Sigmoid ở tầng ẩn là nguyên nhân chính khiến mạng nơ-ron trước năm 2010 không thể huấn luyện sâu được.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§2.2 Các hàm kích hoạt trong Deep Learning**."""
    },
    "OLP01-C21": {
        "prompt": "Vì sao trong các kiến trúc Transformer và mô hình xử lý ngôn ngữ tự nhiên (NLP), chuẩn hóa tầng (Layer Normalization) luôn được ưu tiên sử dụng thay thế hoàn toàn cho chuẩn hóa theo lô (Batch Normalization)?",
        "options": [
            {"key": "A", "text": "Vì Layer Normalization tính toán độc lập cho từng mẫu dữ liệu dọc theo chiều đặc trưng (Feature dimension), không phụ thuộc vào kích thước Batch và hoạt động hoàn hảo với các câu văn có độ dài thay đổi"},
            {"key": "B", "text": "Vì Batch Normalization tiêu tốn nhiều thông số học hơn Layer Normalization"},
            {"key": "C", "text": "Vì Layer Normalization loại bỏ hoàn toàn hiện tượng Overfitting"},
            {"key": "D", "text": "Vì Layer Normalization chỉ dùng được cho dữ liệu dạng chuỗi"}
        ],
        "answer": "A",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Sự khác biệt giữa BatchNorm và LayerNorm:**
- **BatchNorm (So sánh cả lớp):** Tính điểm trung bình của cả phòng thi. Nếu trong NLP, mỗi câu văn có độ dài ngắn khác nhau (có câu 5 từ, có câu 50 từ), việc tính trung bình dọc theo cột của cả lớp sẽ bị thủng lỗ chỗ (do chèn padding). Hơn nữa, khi kích thước Batch nhỏ ($B=1, 2$), BatchNorm sẽ bị sai lệch nghiêm trọng.
- **LayerNorm (Tự soi gương chính mình):** Chuẩn hóa tất cả các từ trong duy nhất **bản thân câu văn đó**. Bất kể độ dài câu là bao nhiêu, bất kể Batch size lớn hay nhỏ hay bằng 1, LayerNorm đều tính toán chuẩn xác và độc lập!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
LayerNorm tính toán trên trục đặc trưng $d$:
$$\\mu = \\frac{1}{d} \\sum_{i=1}^d x_i, \\quad \\sigma^2 = \\frac{1}{d} \\sum_{i=1}^d (x_i - \\mu)^2$$
$$\\text{LN}(x) = \\frac{x - \\mu}{\\sqrt{\\sigma^2 + \\epsilon}} \\odot \\gamma + \\beta$$
Không lưu trữ `running_mean` hay `running_var` như BatchNorm. Chọn **A**.

### 3. Bẫy đề thi & Pitfalls
Nghĩ rằng BatchNorm luôn tốt hơn trong mọi bài toán. Với Text và Speech, LayerNorm là vua.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§2.8 Kỹ thuật Chuẩn hóa (BatchNorm vs LayerNorm)**. Đối chiếu với câu **B10**!"""
    },
    "OLP01-C22": {
        "prompt": "Khi tăng số lượng tầng của mạng CNN lên rất sâu (từ 20 tầng lên 56 tầng), hiện tượng suy thoái hiệu năng (Degradation Problem) xảy ra: Cả lỗi trên tập Train và tập Test đều tăng cao (không phải do Overfitting). Kiến trúc ResNet đã giải quyết triệt để vấn đề này bằng giải pháp nào?",
        "options": [
            {"key": "A", "text": "Tăng kích thước kernel tích chập lên 11x11 ở mọi tầng"},
            {"key": "B", "text": "Thêm các kết nối tắt đồng nhất (Identity Shortcut Connection) cho phép mạng học phần dư F(x) = H(x) - x, tạo đường cao tốc gradient không suy giảm"},
            {"key": "C", "text": "Thay thế hàm ReLU bằng hàm Sigmoid"},
            {"key": "D", "text": "Giảm kích thước batch size xuống bằng 1"}
        ],
        "answer": "B",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bài toán suy thoái (Degradation) & Con đường cao tốc:**
Khi một mạng có 56 tầng, về lý thuyết nó phải giỏi hơn hoặc ít nhất là bằng mạng 20 tầng (chỉ cần 36 tầng sau học phép đồng nhất: không làm gì cả, giữ nguyên kết quả).
Nhưng thực tế mạng sâu truyền thống học phép đồng nhất cực kỳ khó!
Kaiming He giải quyết bằng cách: **Bắc một cây cầu vượt (Shortcut)** đưa thẳng $x$ qua đầu các tầng nơ-ron: $F(x) + x$.
Nếu các tầng nơ-ron không nghĩ ra điều gì mới, nó chỉ cần cho trọng số bằng 0 $\\implies$ Đầu ra vẫn giữ nguyên $x$ ban đầu! Cây cầu vượt này cũng là con đường cao tốc cho đạo hàm chảy ngược về gốc mà không sợ bị nghẽn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Thay vì xấp xỉ hàm mục tiêu $H(x)$, các tầng nơ-ron chỉ cần xấp xỉ phần dư:
$$\\mathcal{F}(x) = H(x) - x \\implies H(x) = \\mathcal{F}(x) + x$$
Gradient luôn có số hạng $+1$ bảo toàn dòng chảy ngược: $\\frac{\\partial \\mathcal{E}}{\\partial x} = \\frac{\\partial \\mathcal{E}}{\\partial y} (\\frac{\\partial \\mathcal{F}}{\\partial x} + 1)$. Chọn **B**.

### 3. Bẫy đề thi & Pitfalls
Nhầm lẫn Degradation với Overfitting. Degradation làm Train Loss TĂNG, trong khi Overfitting làm Train Loss GIẢM.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§3.3 Kiến trúc ResNet & Bài toán suy thoái**. Liên hệ câu **B14** và **C14**!"""
    },
    "OLP01-C23": {
        "prompt": "Trong kiến trúc mạng U-Net dùng cho phân vùng ảnh y tế (Medical Image Segmentation), các đường nối tắt (Skip Connections) từ Encoder sang Decoder thực hiện phép toán nào?",
        "options": [
            {"key": "A", "text": "Phép cộng phần tử (Element-wise Addition)"},
            {"key": "B", "text": "Phép nhân từng phần tử"},
            {"key": "C", "text": "Phép nối chuỗi (Concatenation) các bản đồ đặc trưng dọc theo trục kênh (Channel dimension)"},
            {"key": "D", "text": "U-Net không hề có đường nối tắt"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 Trong U-Net, nhánh Encoder nén ảnh nhỏ lại để hiểu ngữ nghĩa lớn, nhưng làm mất đi các chi tiết biên góc cạnh chính xác của khối u.
Nhánh Decoder phóng to ảnh trở lại. Nhờ có đường nối tắt **ghép thêm (Concatenate)** toàn bộ các bản đồ đặc trưng độ phân giải cao từ Encoder vào, Decoder có đủ thông tin chi tiết để vẽ viền khối u chuẩn xác đến từng pixel!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Code PyTorch chuẩn của U-Net Decoder:
```python
x = torch.cat([upsampled_feat, encoder_feat], dim=1)
```
Số lượng kênh đầu vào của tầng Conv tiếp theo sẽ bằng $C_{\\text{up}} + C_{\\text{enc}}$. Chọn **C**.

### 3. Bẫy đề thi & Pitfalls
Nhầm U-Net dùng phép Add của ResNet (đã phân tích kỹ ở câu C14).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§3.4 U-Net & Phân vùng ảnh**. Liên hệ đối chiếu câu **C14**!"""
    },
    "OLP01-C24": {
        "prompt": "Phát biểu nào sau đây là CHÍNH XÁC NHẤT về cơ chế hoạt động của mô hình Vision Transformer (ViT — Dosovitskiy et al., 2020)?",
        "options": [
            {"key": "A", "text": "ViT sử dụng các tầng Conv2D 3x3 xếp chồng để trích xuất đặc trưng không gian"},
            {"key": "B", "text": "ViT không cần sử dụng mã hóa vị trí (Positional Encoding)"},
            {"key": "C", "text": "ViT hoạt động vượt trội hơn ResNet ngay cả khi chỉ được huấn luyện trên các tập dữ liệu cực kỳ nhỏ"},
            {"key": "D", "text": "ViT chia bức ảnh thành các mảnh vuông (patches), chiếu tuyến tính thành các vector token, gắn thêm token đặc biệt [CLS] và Positional Encoding, sau đó xử lý bằng các khối Transformer Encoder chuẩn mực mà không cần tích chập"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Cách ViT xem tranh:**
Thay vì dùng kính lúp trượt quét qua từng điểm ảnh (CNN), ViT lấy chiếc kéo cắt bức ảnh thành **16 mảnh ghép vuông nhỏ** (ví dụ mỗi mảnh $16 \\times 16$ pixel).
Nó coi mỗi mảnh ghép như một **'từ ngữ' trong một câu văn**, đánh số thứ tự từ 1 đến 16 (Positional Encoding), dán thêm một mảnh ghép đại diện `[CLS]`, rồi đưa toàn bộ vào cỗ máy Transformer để các mảnh ghép tự 'nói chuyện' và so sánh sự liên quan với nhau (Self-Attention)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
- Ảnh $H \\times W \\times C$ chia thành $N = \\frac{HW}{P^2}$ patches.
- Chiếu tuyến tính mỗi patch kích thước $P^2 C$ thành vector $D$ chiều: $x_p E$.
- Chuỗi token đầu vào:
$$z_0 = [x_{\\text{class}}; x_p^1 E; \\dots; x_p^N E] + E_{\\text{pos}}$$
Nhược điểm: ViT thiếu Inductive Bias (tính bất biến dịch chuyển của CNN) nên cần tập dữ liệu khổng lồ (JFT-300M, ImageNet-21k) để tiền huấn luyện. Chọn **D**.

### 3. Bẫy đề thi & Pitfalls
ViT không dùng Conv ở backbone và bắt buộc phải có Positional Encoding vì Transformer có tính hoán vị bất biến.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§3.5 Vision Transformer (ViT)**."""
    },
    "OLP01-C25": {
        "prompt": "Điểm khác biệt bản chất giữa Phân vùng theo ngữ nghĩa (Semantic Segmentation) và Phân vùng theo thực thể (Instance Segmentation) là gì?",
        "options": [
            {"key": "A", "text": "Semantic Segmentation chỉ gán nhãn lớp cho từng pixel mà không phân biệt các cá thể khác nhau cùng lớp; trong khi Instance Segmentation vừa gán nhãn pixel vừa tách riêng biệt từng cá thể đối tượng"},
            {"key": "B", "text": "Semantic Segmentation là bài toán phân loại toàn bộ bức ảnh"},
            {"key": "C", "text": "Instance Segmentation không thể xác định vị trí của đối tượng"},
            {"key": "D", "text": "Hai bài toán này hoàn toàn đồng nhất về định nghĩa và độ đo"}
        ],
        "answer": "A",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Trong bức ảnh có 3 chú cún con đứng cạnh nhau:
- **Semantic Segmentation (Tô màu theo loại):** Coi cả 3 chú cún là một mảng màu tím lớn duy nhất ghi nhãn 'Chó', không thèm quan tâm đâu là con cún số 1, số 2 hay số 3.
- **Instance Segmentation (Đếm từng cá thể):** Thông minh hơn nhiều! Nó tô chú cún A màu đỏ, chú cún B màu xanh, chú cún C màu vàng, tách bạch ranh giới của từng đứa một!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
- Semantic: Output là ma trận $H \\times W$ trong đó mỗi phần tử mang giá trị $c \\in \\{0, \\dots, C-1\\}$. Mô hình tiêu biểu: U-Net, DeepLabV3.
- Instance: Kết hợp giữa Object Detection và Segmentation: Phát hiện từng box trước rồi tạo mask cho từng box (ví dụ Mask R-CNN). Chọn **A**.

### 3. Bẫy đề thi & Pitfalls
Nhầm lẫn giữa Semantic (chỉ phân lớp pixel) và Instance (tách từng đối tượng riêng).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§3.7 Các tác vụ phân vùng ảnh (Segmentation)**."""
    },
    "OLP01-C26": {
        "prompt": "Mô hình sinh ảnh khuếch tán (Diffusion Models như DDPM, Stable Diffusion) hoạt động dựa trên nguyên lý cốt lõi nào?",
        "options": [
            {"key": "A", "text": "Là một biến thể mạng đối kháng GAN với Generator và Discriminator cạnh tranh nhau"},
            {"key": "B", "text": "Quá trình khuếch tán thuận (Forward process) thêm dần nhiễu Gaussian vào ảnh cho đến khi thành nhiễu trắng; mô hình nơ-ron học quá trình ngược (Reverse process) để dự đoán và loại bỏ nhiễu từng bước nhằm khôi phục ảnh nét"},
            {"key": "C", "text": "Tự động mã hóa ảnh thành vector tiềm ẩn không gian 1 chiều"},
            {"key": "D", "text": "Ghép các mảnh ảnh có sẵn trong cơ sở dữ liệu lại với nhau"}
        ],
        "answer": "B",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung bức tranh bị rắc cát:**
- **Pha thuận (Làm hỏng tranh):** Bạn cầm bức tranh đẹp rồi từ từ rắc từng hạt cát lên (thêm nhiễu Gaussian) qua 1,000 bước. Cuối cùng bức tranh biến thành một bãi cát xám xịt (nhiễu trắng hoàn toàn).
- **Pha ngược (Học cách vẽ lại):** Mạng nơ-ron được dạy cách đoán xem ở mỗi bước, hạt cát nào đã được rắc vào để nhặt hạt cát đó ra! Khi được huấn luyện thành thạo, bạn chỉ cần ném cho nó một bức ảnh toàn cát ngẫu nhiên, nó sẽ nhặt sạch cát từng bước một và tạo ra một bức tranh tuyệt đẹp hoàn toàn mới!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Mục tiêu huấn luyện của DDPM (Ho et al., 2020) cực kỳ thanh lịch: Mô hình $U\\text{-Net } \\epsilon_\\theta$ học cách dự đoán vector nhiễu $\\epsilon$:
$$\\mathcal{L}_{\\text{simple}}(\\theta) = \\mathbb{E}_{t, x_0, \\epsilon} \\left[ \\| \\epsilon - \\epsilon_\\theta(x_t, t) \\|^2 \\right]$$
Chọn đáp án **B**.

### 3. Bẫy đề thi & Pitfalls
Diffusion không dùng cơ chế đối kháng Min-Max như GAN, nên huấn luyện rất ổn định và không bao giờ bị sụp đổ mode (Mode Collapse).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§3.8 Mô hình sinh (Generative AI: GAN vs Diffusion)**."""
    },
    "OLP01-C27": {
        "prompt": "Khi bạn chỉ có một tập dữ liệu y tế rất nhỏ gồm 500 ảnh chụp X-quang và muốn áp dụng mạng ResNet-50 đã tiền huấn luyện trên ImageNet, chiến lược Học chuyển giao (Transfer Learning) nào là HỢP LÝ NHẤT?",
        "options": [
            {"key": "A", "text": "Khởi tạo lại toàn bộ trọng số ngẫu nhiên và huấn luyện lại từ đầu (Train from scratch)"},
            {"key": "B", "text": "Mở khóa toàn bộ mạng và fine-tune tất cả các tầng với tốc độ học (Learning rate) thật lớn"},
            {"key": "C", "text": "Đóng băng (Freeze) toàn bộ trọng số của Backbone trích xuất đặc trưng, chỉ huấn luyện tầng phân loại mới (Classification Head) với learning rate nhỏ và áp dụng Data Augmentation mạnh"},
            {"key": "D", "text": "Không sử dụng mô hình tiền huấn luyện vì đặc trưng ảnh tự nhiên không thể áp dụng cho ảnh X-quang"}
        ],
        "answer": "C",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Quy tắc vàng của Transfer Learning khi ít dữ liệu:**
Bạn chỉ có 500 ảnh — đây là một lượng dữ liệu quá bé nhỏ!
Nếu bạn mở khóa toàn bộ mạng ResNet (hơn 25 triệu tham số) ra huấn luyện, mô hình sẽ lập tức bị **Overfitting nặng** và xóa sạch vốn hiểu biết quý báu đã học từ ImageNet!
Cách thông minh nhất: **Khóa cứng (Freeze)** toàn bộ phần thân mạng (Backbone) lại để mượn đôi mắt tinh tường trích xuất đường nét của nó, bạn chỉ cần thay chiếc đầu mới (Linear Classifier) và huấn luyện duy nhất chiếc đầu này thôi!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Code PyTorch chuẩn:
```python
model = torchvision.models.resnet50(weights='IMAGENET1K_V2')
for param in model.parameters():
    param.requires_grad = False  # Dong bang backbone
model.fc = nn.Linear(model.fc.in_features, num_classes)  # Chi train head
```
Chọn đáp án **C**.

### 3. Bẫy đề thi & Pitfalls
Train từ đầu với 500 ảnh chắc chắn thất bại thảm hại do thiếu dữ liệu trầm trọng.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§3.9 Chiến lược Transfer Learning & Fine-tuning**. Liên hệ câu **C07** về chống Overfitting!"""
    },
    "OLP01-C28": {
        "prompt": "Thứ tự chuẩn xác của một quy trình tiền xử lý văn bản (NLP Preprocessing Pipeline) truyền thống trước khi đưa vào mô hình học máy là gì?",
        "options": [
            {"key": "A", "text": "Loại bỏ từ dừng (Stopwords) -> Tách từ (Tokenization) -> Gán nhãn từ loại (POS Tagging)"},
            {"key": "B", "text": "Gán nhãn từ loại (POS) -> Cắt tỉa từ (Stemming) -> Tách từ (Tokenization)"},
            {"key": "C", "text": "Cắt tỉa từ (Stemming) thay thế hoàn toàn cho bước tách từ"},
            {"key": "D", "text": "Tách từ (Tokenization) -> Chuẩn hóa chữ thường/xóa ký tự đặc biệt -> Rút gọn gốc từ / Đưa về dạng từ điển (Stemming/Lemmatization) -> Gán nhãn từ loại (POS) -> Loại bỏ từ dừng (Stopwords)"}
        ],
        "answer": "D",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Trình tự chế biến văn bản:**
1. **Tokenization (Cắt bánh mì thành từng lát):** Cắt cả đoạn văn bản dài thành từng từ riêng biệt. (Bước này bắt buộc phải làm đầu tiên, vì chưa cắt thành từ thì làm sao biết từ nào mà chuẩn hóa!).
2. **Normalization:** Chuyển về chữ thường, dọn sạch dấu câu thừa.
3. **Stemming / Lemmatization:** Đưa các từ biến thể về dạng gốc (ví dụ 'running', 'ran' đều đưa về 'run').
4. **POS Tagging:** Xác định từ nào là danh từ, động từ.
5. **Stopwords Removal:** Nhặt bỏ các từ vụn vặt không mang nhiều ngữ nghĩa (như 'và', 'thì', 'là', 'mà'). Chọn **D**.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Thứ tự logic phụ thuộc dữ liệu: Cần tokenization trước để có danh sách token, sau đó mới áp dụng được từ điển từ dừng và mô hình ngôn ngữ.

### 3. Bẫy đề thi & Pitfalls
Đảo bước loại stopwords lên trước tokenization là sai logic xử lý chuỗi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§4.1 Pipeline tiền xử lý văn bản trong NLP**."""
    },
    "OLP01-C29": {
        "prompt": "Khi xử lý văn bản tiếng Việt trên mạng xã hội có nhiều từ viết tắt, từ lóng hoặc lỗi chính tả gây ra hiện tượng từ ngoài từ điển (Out-Of-Vocabulary — OOV), mô hình nhúng từ (Word Embedding) nào sau đây xử lý HIỆU QUẢ NHẤT?",
        "options": [
            {"key": "A", "text": "FastText (sử dụng n-gram cấp độ ký tự / Subword)"},
            {"key": "B", "text": "One-Hot Encoding"},
            {"key": "C", "text": "TF-IDF truyền thống"},
            {"key": "D", "text": "Word2Vec phiên bản chuẩn ban đầu"}
        ],
        "answer": "A",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Vũ khí trị từ viết sai chính tả của FastText:**
- Word2Vec coi mỗi từ là một khối nguyên vẹn. Nếu gặp từ lạ hoặc gõ sai như 'hocsinh' (thiếu dấu) hay 'hocc', Word2Vec sẽ chịu chết và gán nhãn `<UNK>` (Không biết).
- **FastText (Facebook AI):** Tách từ thành các mảnh ghép ký tự nhỏ (Character n-grams), ví dụ `<ho`, `hoc`, `oc>`, v.v.
Khi gặp một từ lạ chưa từng thấy, FastText chỉ việc gom vector của các mảnh ghép ký tự quen thuộc lại để đoán nghĩa $\\implies$ Trị dứt điểm căn bệnh từ ngoài từ điển (OOV)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Biểu diễn vector của từ $w$ trong FastText:
$$v_w = \\sum_{g \\in \\mathcal{G}_w} z_g$$
Trong đó $\\mathcal{G}_w$ là tập hợp các n-gram ký tự của từ $w$. Chọn **A**.

### 3. Bẫy đề thi & Pitfalls
Word2Vec không có thông tin subword nên hoàn toàn bất lực trước từ OOV.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§4.2 Các mô hình biểu diễn từ (Word2Vec vs FastText)**."""
    },
    "OLP01-C30": {
        "prompt": "Bạn cần xây dựng 2 hệ thống AI: Hệ thống 1 dùng để phân tích cảm xúc đánh giá sản phẩm (Sentiment Analysis); Hệ thống 2 dùng để tự động sinh bài viết mô tả sản phẩm (Product Description Generation). Lựa chọn kiến trúc nền tảng nào sau đây là TỐI ƯU NHẤT?",
        "options": [
            {"key": "A", "text": "Hệ thống 1 dùng GPT; Hệ thống 2 dùng BERT"},
            {"key": "B", "text": "Hệ thống 1 dùng BERT (Encoder-only, hiểu ngữ cảnh hai chiều); Hệ thống 2 dùng GPT (Decoder-only, tự hồi quy sinh từ tiếp theo theo chiều xuôi)"},
            {"key": "C", "text": "Cả hai đều dùng BERT vì BERT sinh văn bản tốt hơn GPT"},
            {"key": "D", "text": "Cả hai đều bắt buộc dùng RNN truyền thống"}
        ],
        "answer": "B",
        "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Phân biệt nhiệm vụ của BERT và GPT:**
- **BERT (Thanh tra hiểu bài - Encoder):** Được nhìn cả câu văn từ trái sang phải và từ phải sang trái cùng lúc (Hai chiều). Nó rất giỏi việc **Đọc hiểu, phân loại cảm xúc, tìm ý chính**. Nhưng nó không biết viết văn tiếp theo.
- **GPT (Nhà văn kể chuyện - Decoder):** Viết văn theo kiểu đoán từ tiếp theo từ trái sang phải (Autoregressive). Nó cực kỳ giỏi việc **Sinh văn bản, viết truyện, trả lời câu hỏi**. Chọn **B**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
- BERT: Masked Language Model $P(w_i \\mid w_{\\backslash i})$ (Hai chiều). Phù hợp NLU (Natural Language Understanding).
- GPT: Causal Language Model $P(w_t \\mid w_{<t})$ (Một chiều). Phù hợp NLG (Natural Language Generation).

### 3. Bẫy đề thi & Pitfalls
Đảo ngược vai trò giữa BERT và GPT.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
Xem **§4.6 Mô hình ngôn ngữ lớn (BERT vs GPT)**."""
    }
}

# Cập nhật các câu C16-C30 vào UPGRADES
for k, v in C_REMAINING.items():
    UPGRADES[k] = v

# ==========================================
# PHẦN TỰ LUẬN (4 CÂU: E01 - E04)
# ==========================================

UPGRADES["OLP01-E01"] = {
    "prompt": "Đề xuất giải pháp theo khung 5 bước chuẩn kỹ sư cho bài toán: Nhận diện ngôn ngữ ký hiệu từ video (phỏng theo đề OLP AI 2025): Tập dữ liệu gồm 10,000 clip ngắn, 50 loại ký hiệu thủ ngữ, quay bởi 100 người khác nhau trong điều kiện ánh sáng và phông nền đa dạng. Yêu cầu mô hình phải chạy đạt tốc độ gần thời gian thực (Near Real-time) trên máy tính xách tay cấu hình phổ thông.",
    "options": [],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bản chất bài toán:** Nhận diện hành động trong video theo thời gian (Spatial-Temporal Recognition). Thách thức lớn nhất là 100 người khác nhau có hình dáng tay và tốc độ vung tay khác nhau, phông nền phòng khách/ngoài đường gây nhiễu, và ràng buộc máy yếu phải chạy nhanh.

### 2. Khung giải pháp 5 bước chuẩn kỹ sư
1. **Phân tích bài toán & Chống rò rỉ dữ liệu (Leakage):**
   - Ràng buộc: Dữ liệu video theo chuỗi thời gian, 100 người khác nhau $\\implies$ **Bắt buộc phân chia Train/Validation theo người (Person-independent GroupKFold)**. Tuyệt đối không để cùng một người xuất hiện ở cả train và val.
   - Augmentation: Xoay nhẹ, đổi độ sáng, ngẫu nhiên tua nhanh/chậm khung hình (Temporal jittering).
2. **Thiết kế kiến trúc mô hình & Luận giải:**
   - Trích xuất đặc trưng tay nhanh: Dùng **MediaPipe Hands / Holistic** trích xuất tọa độ 21 khớp xương tay (dữ liệu nhẹ hàng nghìn lần so với ảnh thô!).
   - Mô hình phân loại chuỗi: Đưa tọa độ khớp qua mạng **1D-CNN + BiLSTM** hoặc **ST-GCN (Spatial Temporal Graph Convolutional Network)**. Mô hình cực nhẹ (~5MB), chạy trên CPU laptop đạt >60 FPS!
   - Baseline đối chiếu: ResNet18 trích frame + GRU.
3. **Pipeline xử lý & Giải mã:**
   - Uniform sampling lấy cố định 32 frame cho mỗi clip.
   - Chuẩn hóa tọa độ bàn tay tương đối so với cổ tay để khử kích thước tay khác nhau.
4. **Metric đánh giá:**
   - Metric chính: **Macro F1-Score** và **Video-level Top-1 Accuracy** (không dùng frame-level accuracy).
   - Phân tích Confusion Matrix để tìm các cặp ký hiệu có khẩu hình tay tương tự nhau.
5. **Phương án mở rộng & Tối ưu hóa:**
   - Tối ưu hóa tốc độ: Chuyển đổi mô hình sang **ONNX Runtime / TensorRT**, lượng tử hóa INT8.
   - Cải tiến: Áp dụng Knowledge Distillation từ mô hình 3D-CNN nặng sang mô hình tọa độ nhẹ."""
}

UPGRADES["OLP01-E02"] = {
    "prompt": "Đề xuất giải pháp theo khung 5 bước chuẩn kỹ sư cho bài toán: Dịch máy thần kinh (NMT) cặp ngôn ngữ Hoa - Việt (phỏng theo tác vụ SOLOAI 2025). Tập dữ liệu gồm 200,000 cặp câu song ngữ chuyên ngành thương mại điện tử, yêu cầu mô hình phải bảo toàn chính xác tuyệt đối các thực thể số lượng, giá tiền, đơn vị đo lường và tên thương hiệu.",
    "options": [],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bản chất bài toán:** Dịch máy chuyên ngành hẹp (Domain-specific Machine Translation). Khó khăn cốt lõi là cặp câu lệch cấu trúc, nhiều từ lóng mua sắm TMĐT, và nếu dịch sai số tiền/số lượng sẽ gây tổn thất tài chính nghiêm trọng cho người mua.

### 2. Khung giải pháp 5 bước chuẩn kỹ sư
1. **Phân tích dữ liệu & Tiền xử lý chuyên biệt:**
   - Làm sạch: Lọc cặp câu trùng, câu lệch độ dài quá mức ($> 1:3$), câu lẫn tiếng Anh/ký tự rác.
   - Bảo toàn thực thể số/tiền tệ: Áp dụng **Regex / NER rule-based tagging** để thay thế số tiền và mã sản phẩm bằng token đặc biệt `<NUM_1>`, `<PRICE_1>` trước khi dịch, sau đó hậu xử lý thế ngược lại.
   - Tokenization: Dùng **Byte-Pair Encoding (BPE / SentencePiece)** huấn luyện chung trên cả 2 ngôn ngữ (Shared Vocabulary 32k tokens).
2. **Thiết kế kiến trúc mô hình:**
   - Mô hình chính: Fine-tune mô hình dịch đa ngữ đã được tiền huấn luyện mạnh như **mBART-50** hoặc **NLLB-200 (No Language Left Behind)**.
   - Baseline tham chiếu: Transformer Base (6 layers Encoder, 6 layers Decoder) huấn luyện từ đầu.
3. **Pipeline xử lý:**
   - Huấn luyện: Label Smoothing ($\epsilon = 0.1$) để tránh overfit, Warmup Cosine scheduler.
   - Giải mã (Decoding): **Beam Search** với $beam\\_size = 4$ kèm Length Penalty $\\alpha = 0.6$.
4. **Metric đánh giá:**
   - Metric chính: **SacreBLEU** (chuẩn hóa quốc tế) và **ChrF++** (rất nhạy với tiếng Việt và tiếng Trung).
   - Metric phụ: Kiểm tra độ chính xác bảo toàn thực thể số (Entity Preservation Rate = 100%).
5. **Phương án mở rộng:**
   - Back-translation từ dữ liệu đơn ngữ tiếng Việt để tăng cường dữ liệu.
   - Reranking các kết quả sinh ra bằng mô hình chấm điểm chất lượng (COMET)."""
}

UPGRADES["OLP01-E03"] = {
    "prompt": "Đề xuất giải pháp theo khung 5 bước chuẩn kỹ sư cho bài toán: Phát hiện bệnh trên lá khoai tây ngoài đồng ruộng (phỏng theo đề thi thực chiến OLP AI). Tập dữ liệu gồm 8,000 ảnh chụp lá ngoài thực địa, gồm 4 loại bệnh (trong đó có 2 loại bệnh hiếm), chụp trong điều kiện ánh sáng thay đổi, nền đất phức tạp. Yêu cầu mô hình phải khoanh vùng tổn thương và chạy được trực tiếp trên điện thoại thông minh của nông dân.",
    "options": [],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bản chất bài toán:** Phát hiện vật thể trên biên (Edge Object Detection) với dữ liệu thực địa nhiều nhiễu và mất cân bằng lớp. Thách thức là mô hình phải siêu nhẹ để chạy offline trên điện thoại không cần internet, nhưng phải phát hiện được các đốm bệnh nhỏ.

### 2. Khung giải pháp 5 bước chuẩn kỹ sư
1. **Phân tích dữ liệu & Phân chia Validation:**
   - Ràng buộc: Rất dễ bị rò rỉ dữ liệu nếu cùng một luống khoai tây xuất hiện ở cả Train và Val. Bắt buộc chia **Stratified GroupKFold theo thửa ruộng/thời điểm chụp**.
   - Xử lý lớp hiếm: Áp dụng **Copy-Paste Augmentation** (cắt đốm bệnh hiếm dán lên lá khỏe mạnh) và Mosaic Augmentation.
2. **Thiết kế mô hình phù hợp thiết bị di động:**
   - Mô hình đề xuất chính: **YOLOv8-Nano (YOLOv8n)** hoặc **YOLOv10n** (chỉ ~3 triệu tham số, nhẹ < 6MB).
   - Hàm mất mát: **Focal Loss / CIoU Loss** để tập trung phạt các đốm bệnh khó và lớp hiếm.
   - Baseline đối chiếu: Faster R-CNN với MobileNetV3 backbone.
3. **Pipeline xử lý:**
   - Ảnh vào resize về $416 \\times 416$. Tự động cân bằng trắng (White Balance) để khử nhiễu nắng gắt/bóng râm.
   - Hậu xử lý NMS với ngưỡng IoU = 0.45.
4. **Metric đánh giá:**
   - Metric chính: **mAP@0.5** và **mAP@0.5:0.95**. Đặc biệt theo dõi riêng **Recall của 2 loại bệnh hiếm** (không để sót bệnh).
5. **Tối ưu hóa chạy trên điện thoại di động:**
   - Chuyển đổi mô hình sang **TFLite (TensorFlow Lite)** hoặc **ONNX / NCNN**.
   - Lượng tử hóa sau huấn luyện (**Post-Training Quantization INT8**) giúp giảm kích thước còn ~2MB, tăng tốc độ suy luận gấp 4 lần trên chip Snapdragon/MediaTek."""
}

UPGRADES["OLP01-E04"] = {
    "prompt": "Đề xuất giải pháp theo khung 5 bước chuẩn kỹ sư cho bài toán: Dự đoán sinh viên có nguy cơ bỏ học sớm (Tabular Data Machine Learning). Tập dữ liệu dạng bảng gồm 50,000 hồ sơ sinh viên với 40 đặc trưng (điểm thi, điểm rèn luyện, chuyên cần, hoàn cảnh kinh tế, hoạt động thư viện). Tỉ lệ sinh viên bỏ học là 8%. Yêu cầu mô hình phải có khả năng giải thích lý do cụ thể cho từng sinh viên để phòng đào tạo kịp thời tư vấn hỗ trợ.",
    "options": [],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bản chất bài toán:** Phân loại nhị phân trên dữ liệu dạng bảng mất cân bằng lớp kèm yêu cầu **Trí tuệ nhân tạo có thể giải thích được (Explainable AI - XAI)**. Ta không thể dùng một hộp đen bí ẩn nói sinh viên này bỏ học mà không chỉ ra lý do!

### 2. Khung giải pháp 5 bước chuẩn kỹ sư
1. **Phân tích dữ liệu & Kỹ thuật đặc trưng (Feature Engineering):**
   - Dữ liệu dạng bảng 50k mẫu, mất cân bằng 8% $\\implies$ Dùng **Stratified 5-Fold Cross Validation**.
   - Tạo các đặc trưng xu hướng (Trend features): Độ dốc giảm điểm giữa học kỳ 1 và học kỳ 2 (Delta GPA), tỉ lệ vắng mặt tăng đột biến.
   - Xử lý giá trị khuyết: Dùng Median cho số, Mode cho biến phân loại.
2. **Lựa chọn mô hình tối ưu:**
   - Mô hình chính: **LightGBM / XGBoost / CatBoost** (vua của dữ liệu dạng bảng, xử lý tốt tương quan phi tuyến, nhanh gấp 10 lần mạng nơ-ron).
   - Hàm mục tiêu: Binary Logloss kết hợp tham số `scale_pos_weight = 92 / 8 = 11.5` để bù đắp mất cân bằng lớp.
   - Baseline tham chiếu: Logistic Regression.
3. **Pipeline xử lý & Chọn ngưỡng quyết định:**
   - Không dùng ngưỡng mặc định 0.5. Quét ngưỡng xác suất trên đường cong PR-Curve để chọn **ngưỡng tối ưu hóa F1-score / F2-score** (ưu tiên Recall để không bỏ sót sinh viên khó khăn).
4. **Metric đánh giá:**
   - Metric chính: **PR-AUC (Precision-Recall Area Under Curve)** và **F1-Score**.
   - Không sử dụng ROC-AUC hay Accuracy vì bị sai lệch bởi lớp đa số 92%.
5. **Giải thích mô hình (Explainability & Mở rộng):**
   - Áp dụng **SHAP (SHapley Additive exPlanations)**: Tạo biểu đồ Waterfall giải thích riêng cho từng sinh viên: Ví dụ 'Sinh viên A bị cảnh báo 85% nguy cơ bỏ học do điểm GPA giảm 1.5 và vắng mặt quá 4 buổi'.
   - Giám sát Data Drift (sự thay đổi phân phối sinh viên qua từng năm học) bằng KS-Test."""
}

# Tiến hành cập nhật toàn bộ 64 câu trong exam_data
updated_count = 0
for q in exam_data["questions"]:
    qid = q["id"]
    if qid in UPGRADES:
        up = UPGRADES[qid]
        if "prompt" in up and up["prompt"]:
            q["prompt"] = up["prompt"]
        if "options" in up and up["options"]:
            q["options"] = up["options"]
        if "explanation" in up and up["explanation"]:
            q["explanation"] = up["explanation"]
        updated_count += 1

print(f"Đã nâng cấp thành công {updated_count}/64 câu hỏi trong olp-01.json!")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Đã ghi đè thành công dữ liệu chuẩn vào:", json_path)
