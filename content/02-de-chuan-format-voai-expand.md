# ĐỀ THI 02: CHUẨN FORMAT VOAI MỞ RỘNG (MOCK EXAM FULL STANDARD)
## 60 Câu Trắc Nghiệm Chuyên Sâu (90.0đ) & 6 Bài Tự Luận Thiết Kế Giải Pháp AI (60.0đ)

> **Mô tả:** Đề thi mô phỏng toàn diện chuẩn cấu trúc VOAI & Olympic AI Sinh viên 2025-2026 (Đề 2 Thầy Đỗ Đình Luật).
> **Thời gian làm bài:** 90 phút | **Tổng số câu:** 66 câu (60 Trắc nghiệm + 6 Tự luận) | **Thang điểm:** 150.0 điểm

---

### Câu 01 [VOAI02-M01] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Một căn bệnh hiếm gặp có tỉ lệ mắc trong cộng đồng là $P(D) = 0.5\%$. Một bộ kit xét nghiệm y tế có độ nhạy (Sensitivity / True Positive Rate) là $98\%$ và độ đặc hiệu (Specificity / True Negative Rate) là $96\%$. Nếu một người được xét nghiệm ngẫu nhiên và nhận kết quả **Dương tính** ($+$), xác suất người đó thực sự mắc bệnh $P(D \mid +)$ gần nhất với giá trị nào sau đây?

- **A.** Khoảng 4.0%
- **B.** Khoảng 98.0%
- **C.** Khoảng 50.0%
- **D.** Khoảng 11.0%

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Base Rate (Tỉ lệ nền / Xác suất tiên nghiệm):** Tỉ lệ mắc bệnh tự nhiên trong cộng đồng $P(D)$.
- **Sensitivity (Độ nhạy / True Positive Rate):** $P(+|D)$ - Xác suất test dương tính khi thực sự có bệnh.
- **Specificity (Độ đặc hiệu / True Negative Rate):** $P(-|\bar{D})$ - Xác suất test âm tính khi người hoàn toàn khỏe mạnh.
- **Base Rate Fallacy:** Sai lầm phán đoán khi bỏ qua tỉ lệ nền quá nhỏ khiến số ca dương tính giả áp đảo số ca bệnh thật.

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng trong một ngôi làng 10,000 người, chỉ có 50 người thực sự bị ốm. Bộ kit phát hiện đúng 49 người ốm (độ nhạy 98%). Nhưng với 9,950 người khỏe mạnh, kit báo nhầm (dương tính giả 4%) cho tận 398 người! Tổng cộng có 49 + 398 = 447 người cầm kết quả dương tính. Nhưng trong số đó, chỉ có 49 người thực sự ốm! Xác suất thật chỉ là 49 / 447 ≈ 10.96% mà thôi. Đừng tưởng kit 98% là bạn có 98% nguy cơ mắc bệnh!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng định lý Bayes toàn phần:
$$P(D \mid +) = \frac{P(+ \mid D) P(D)}{P(+)} = \frac{P(+ \mid D) P(D)}{P(+ \mid D) P(D) + P(+ \mid \bar{D}) P(\bar{D})}$$
Trong đó:
- $P(D) = 0.005$, suy ra $P(\bar{D}) = 1 - 0.005 = 0.995$.
- Độ nhạy: $P(+ \mid D) = 0.98$.
- Độ đặc hiệu $P(- \mid \bar{D}) = 0.96$, suy ra tỉ lệ dương tính giả: $P(+ \mid \bar{D}) = 1 - 0.96 = 0.04$.

Thay số vào mẫu số:
$$P(+) = (0.98 \times 0.005) + (0.04 \times 0.995) = 0.0049 + 0.0398 = 0.0447$$
Thay vào công thức Bayes:
$$P(D \mid +) = \frac{0.0049}{0.0447} \approx 0.109619 \approx 10.96\% \approx 11.0\%$$
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy tâm lý kinh điển trong đề thi AI/Y tế: Thí sinh nhìn thấy độ nhạy 98% liền vội vàng chọn 98% (A), hoặc lấy trung bình 98% và 96% ra ~97%. Đây là lỗi ' Base Rate Fallacy ' (bỏ qua tỉ lệ nền quá nhỏ 0.5% khiến số lượng dương tính giả của nhóm người khỏe áp đảo số dương tính thật).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§5.1 Định Lý Bayes & Bài Toán Chẩn Đoán Y Tế (Base-Rate Fallacy)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-A01: Cùng kiểm tra nghịch lý tỉ lệ nền (Base-Rate Fallacy) trong xét nghiệm y tế: OLP01-A01 tính xác suất có bệnh khi test dương tính với $P(D)=2\%$, còn M01 kiểm tra với $P(D)=0.5\%$.

---

### Câu 02 [VOAI02-M02] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho biến ngẫu nhiên rời rạc $X \sim \text{Binomial}(n = 20, p = 0.4)$. Kỳ vọng $\mathbb{E}[X]$ và phương sai $\text{Var}(X)$ của $X$ lần lượt là bao nhiêu?

- **A.** E[X] = 8, Var(X) = 8
- **B.** E[X] = 12, Var(X) = 4.8
- **C.** E[X] = 4.8, Var(X) = 8
- **D.** E[X] = 8, Var(X) = 4.8

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Binomial Distribution (Phân phối nhị thức):** Phân phối của số lần thành công trong $n$ phép thử Bernoulli độc lập có cùng xác suất thành công $p$.
- **Kỳ vọng $\mathbb{E}[X] = n \cdot p$:** Số lần thành công trung bình khi lặp lại thí nghiệm.
- **Phương sai $\text{Var}(X) = n \cdot p \cdot (1 - p)$:** Độ phân tán của số lần thành công quanh giá trị trung bình.

🍼 **Hình dung thực tế cho em bé:**
Bạn bắn cung 20 lần, mỗi lần có 40% trúng đích. Trung bình (kỳ vọng) bạn trúng được 20 × 0.4 = 8 lần. Độ phân tán xung quanh con số 8 này được tính bằng n × p × (1 - p) = 20 × 0.4 × 0.6 = 4.8.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Với biến ngẫu nhiên nhị thức $X = \sum_{i=1}^n Y_i$ trong đó các $Y_i \sim \text{Bernoulli}(p)$ độc lập:
$$\mathbb{E}[X] = n \cdot p = 20 \times 0.4 = 8$$
$$\text{Var}(X) = n \cdot p \cdot (1 - p) = 20 \times 0.4 \times 0.6 = 4.8$$
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Nhầm phương sai của phân phối Poisson (Var = E = 8) dẫn đến chọn A (8, 8); hoặc nhầm lẫn đảo ngược giữa kỳ vọng và phương sai dẫn đến chọn C (4.8, 8). Đáp án đúng là D (8, 4.8).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§5.2 Các Phân Phối Xác Suất Quan Trọng**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-A03: Phân phối nhị thức $\text{Binomial}(n, p)$ trong M02 chính là tổng của $n$ biến ngẫu nhiên $\text{Bernoulli}(p)$ độc lập trong OLP01-A03, kế thừa công thức kỳ vọng $n p$ và phương sai $n p (1-p)$.

---

### Câu 03 [VOAI02-M03] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong một nghiên cứu A/B Testing đánh giá thuật toán gợi ý mới, giả thuyết không $H_0$ là ' Thuật toán mới không làm tăng tỉ lệ click (CTR)'. Sau khi thu thập 100,000 phiên truy cập, nhóm kỹ sư tính ra giá trị $p\text{-value} = 0.012$. Với mức ý nghĩa kiểm định chuẩn $\alpha = 0.05$, kết luận thống kê nào sau đây là **CHÍNH XÁC**?

- **A.** Thuật toán mới chắc chắn cải thiện CTR với độ tin cậy tuyệt đối 100%
- **B.** Chấp nhận H0 vì p-value nhỏ hơn 0.05
- **C.** Xác suất H0 đúng là chính xác 1.2%
- **D.** Bác bỏ H0, có bằng chứng thống kê cho thấy thuật toán mới cải thiện CTR có ý nghĩa

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Giả thuyết không ($H_0$):** Giả định mặc định rằng không có sự khác biệt hay không có hiệu ứng (thuật toán gợi ý mới không làm thay đổi hoặc không làm tăng CTR).
- **p-value:** Xác suất, dưới giả định rằng giả thuyết không $H_0$ và mô hình kiểm định là đúng, thu được một thống kê kiểm định có độ lớn bằng hoặc cực đoan hơn giá trị thực tế quan sát được ($P(T \ge t_{\text{obs}} \mid H_0)$ hoặc $P(|T| \ge |t_{\text{obs}}| \mid H_0)$). Tuyệt đối không nhầm lẫn với xác suất dữ liệu cụ thể $P(\text{Data} \mid H_0)$ hay xác suất $H_0$ đúng $P(H_0 \mid \text{Data})$.
- **Mức ý nghĩa ($\alpha$):** Ngưỡng sai lầm loại I được ấn định trước (thường là 0.05). Nếu $p \le \alpha$, ta có đủ bằng chứng thống kê để bác bỏ $H_0$.

🍼 **Hình dung thực tế cho em bé:**
P-value giống như thước đo độ ' kỳ lạ ' nếu giả thuyết H0 đúng. Giả sử thuật toán mới hoàn toàn vô dụng (H0 đúng), khả năng xảy ra kết quả kỳ diệu như ta thấy chỉ là 1.2%. Vì 1.2% bé hơn ngưỡng hoài nghi 5% (alpha = 0.05), ta tuyên bố: Bác bỏ H0! Thuật toán mới thực sự có hiệu quả!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Quy tắc quyết định trong kiểm định giả thuyết thống kê cổ điển:
- Nếu $p\text{-value} \le \alpha$: Bác bỏ giả thuyết không $H_0$ (Reject $H_0$) ở mức ý nghĩa $\alpha$.
- Nếu $p\text{-value} > \alpha$: Chưa đủ bằng chứng bác bỏ $H_0$ (Fail to reject $H_0$).
Ở đây $p = 0.012 < \alpha = 0.05$, do đó bác bỏ $H_0$.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Cực kỳ chú ý đáp án C: Đây là sai lầm phổ biến nhất trong thống kê và phòng thi! $p\text{-value}$ KHÔNG PHẢI là $P(H_0 \text{ đúng})$. $p\text{-value}$ là xác suất quan sát được dữ liệu cực đoan như vậy giả định rằng $H_0$ đã đúng: $P(\text{Data} \ge \text{observed} \mid H_0)$.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§5.5 Kiểm Định Giả Thuyết Thống Kê & Bản Chất của p-value**.
🔗 **Mắt xích & Liên hệ bài học:** Đây là câu hỏi độc lập chuyên sâu trong ngân hàng đề kiểm tra trực tiếp định nghĩa chuẩn tắc của $p$-value và quy tắc ra quyết định trong A/B testing: $p$-value là xác suất của thống kê kiểm định cực đoan bằng hoặc hơn quan sát được dưới $H_0$ (theo Tuyên bố chính thức của Hiệp hội Thống kê Hoa Kỳ ASA), không phải $P(\text{Data} \mid H_0)$ hay $P(H_0 \mid \text{Data})$.

---

### Câu 04 [VOAI02-M04] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho ma trận dữ liệu đã chuẩn hóa chuẩn (zero-mean) $X \in \mathbb{R}^{N \times D}$. Trong thuật toán Phân tích Thành phần Chính (PCA), các trục thành phần chính (Principal Components) được tìm thấy bằng cách nào?

- **A.** Tìm các vector hàng của ma trận tam giác dưới từ phân tích LU của ma trận tương quan $R = X^T X$
- **B.** Tìm các vector riêng tương ứng với các trị riêng lớn nhất của ma trận hiệp phương sai $C = \frac{1}{N} X^T X$
- **C.** Tối ưu hóa hàm phi tuyến bằng Gradient Descent để tìm ma trận chiếu trực giao bảo toàn độ phân tán
- **D.** Tính ma trận nghịch đảo Moore-Penrose của $X^T X$ và chọn các cột có chuẩn Euclid lớn nhất

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **PCA (Principal Component Analysis):** Phương pháp giảm chiều tuyến tính tìm các trục chiếu trực giao tối đa hóa phương sai của dữ liệu.
- **Ma trận hiệp phương sai ($C = \frac{1}{N} X^T X$):** Ma trận vuông đối xứng đo mức độ biến thiên đồng thời giữa các cặp đặc trưng sau khi đã chuẩn hóa zero-mean.
- **Vector riêng & Trị riêng:** Trục thành phần chính thứ nhất là vector riêng ứng với trị riêng lớn nhất của ma trận hiệp phương sai $C$.

🍼 **Hình dung thực tế cho em bé:**
PCA muốn tìm những hướng mà đám mây dữ liệu trải rộng nhất (giữ được nhiều thông tin nhất). Hướng trải rộng nhất chính là vector riêng (eigenvector) của ma trận hiệp phương sai, và độ trải rộng chính là trị riêng (eigenvalue) tương ứng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ma trận hiệp phương sai mẫu của dữ liệu đã chuẩn hóa tâm:
$$C = \frac{1}{N} X^T X \in \mathbb{R}^{D \times D}$$
Vì $C$ đối xứng và nửa xác định dương, nó có $D$ trị riêng thực $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_D \ge 0$ và hệ $D$ vector riêng trực chuẩn $u_1, u_2, \dots, u_D$ thỏa mãn:
$$C u_i = \lambda_i u_i$$
Trục thành phần chính thứ nhất $u_1$ tối đa hóa phương sai hình chiếu: $\max_{\|u\|=1} u^T C u = \lambda_1$.
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Nhầm phân tích SVD trên chính $X = U \Sigma V^T$ với phân tích trị riêng trên $C$. Vector riêng của $C$ chính là các cột của $V$ (Right singular vectors của $X$).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.10 Tiền xử lý Đặc trưng & Thao tác NumPy**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M32: Cùng thuộc chuyên đề giảm chiều dữ liệu: M04 phân tích cơ sở toán học tuyến tính của PCA (trục chiếu theo vector riêng của ma trận hiệp phương sai), còn VOAI03-M32 so sánh PCA với phương pháp giảm chiều phi tuyến t-SNE.

---

### Câu 05 [VOAI02-M05] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho hàm số hai biến $f(x, y) = x^2 - 4xy + y^3$. Điểm dừng $P_0(0, 0)$ có gradient $\nabla f(0, 0) = [0, 0]^T$. Tính chất của điểm $P_0$ là gì?

- **A.** Điểm yên ngựa (Saddle Point)
- **B.** Điểm cực tiểu địa phương (Local Minimum)
- **C.** Không thể kết luận vì ma trận Hessian có định thức bằng 0
- **D.** Điểm cực đại địa phương (Local Maximum)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Ma trận Hessian ($H = \nabla^2 f(x, y)$):** Ma trận vuông chứa tất cả các đạo hàm riêng bậc hai của hàm đa biến, biểu diễn độ cong của bề mặt hàm số.
- **Điểm dừng (Stationary Point):** Điểm mà vector gradient triệt tiêu $\nabla f(x, y) = [0, 0]^T$.
- **Điểm yên ngựa (Saddle Point):** Điểm dừng mà theo một hướng thì đạt cực tiểu nhưng theo hướng khác lại đạt cực đại (ma trận Hessian có định thức $\det(H) < 0$ hoặc có cả trị riêng dương và âm).

🍼 **Hình dung thực tế cho em bé:**
Điểm yên ngựa giống như chiếc yên đặt trên lưng ngựa: nhìn theo chiều trước-sau thì nó trũng xuống (cực tiểu), nhưng nhìn theo chiều hai bên chân thì nó lại gồ lên (cực đại). Hessian có cả trị riêng dương và âm nghĩa là điểm đó chính là điểm yên ngựa!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tính các đạo hàm riêng bậc một và bậc hai:
$$\frac{\partial f}{\partial x} = 2x - 4y, \quad \frac{\partial f}{\partial y} = -4x + 3y^2$$
Tại $(0, 0)$, $\nabla f(0, 0) = [0, 0]^T$ (điểm dừng).
Các đạo hàm riêng bậc hai:
$$\frac{\partial^2 f}{\partial x^2} = 2, \quad \frac{\partial^2 f}{\partial x \partial y} = -4, \quad \frac{\partial^2 f}{\partial y^2} = 6y$$
Tại $(0, 0)$:
$$H(0, 0) = \begin{bmatrix} 2 & -4 \\ -4 & 0 \end{bmatrix}$$
Tính định thức của Hessian:
$$\det(H) = (2)(0) - (-4)^2 = -16 < 0$$
Vì $\det(H) < 0$, ma trận Hessian không xác định dấu (indefinite, có một trị riêng dương và một trị riêng âm). Do đó, $(0, 0)$ là **điểm yên ngựa** (Saddle Point).
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Thấy $f_{xx} = 2 > 0$ vội vàng kết luận là cực tiểu địa phương. Phải luôn kiểm tra định thức $\det(H) = f_{xx}f_{yy} - (f_{xy})^2$. Nếu $\det(H) < 0$, chắc chắn là điểm yên ngựa bất chấp dấu của $f_{xx}$!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.3 Lan truyền xuôi, Lan truyền ngược & Vòng lặp Huấn luyện PyTorch**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M02: Cùng kiểm tra việc dùng ma trận Hessian để xác định tính chất điểm dừng trong tối ưu hóa: VOAI03-M02 kiểm tra trường hợp Hessian xác định dương ($\det > 0, f_{xx} > 0 \implies$ cực tiểu địa phương), còn M05 kiểm tra trường hợp Hessian bất định ($\det(H) < 0 \implies$ điểm yên ngựa).

---

### Câu 06 [VOAI02-M06] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho vector logit $z = [z_1, z_2, \dots, z_C]^T$, xác suất dự đoán $p_i = \text{Softmax}(z)_i = \frac{e^{z_i}}{\sum_{k=1}^C e^{z_k}}$, và nhãn One-hot $y = [y_1, y_2, \dots, y_C]^T$. Hàm mất mát Cross-Entropy là $L = -\sum_{i=1}^C y_i \ln(p_i)$. Đạo hàm của hàm mất mát $L$ theo logit $z_i$, $\frac{\partial L}{\partial z_i}$, có dạng tối giản là:

- **A.** $\frac{\partial L}{\partial z_i} = p_i - y_i$
- **B.** $\frac{\partial L}{\partial z_i} = y_i - p_i$
- **C.** $\frac{\partial L}{\partial z_i} = -\frac{y_i}{p_i}$
- **D.** $\frac{\partial L}{\partial z_i} = p_i(1 - p_i)$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Softmax Function:** Hàm chuyển đổi vector logit thô $z$ thành phân phối xác suất hợp lệ có tổng bằng 1: $p_i = \frac{e^{z_i}}{\sum_k e^{z_k}}$.
- **Cross-Entropy Loss:** Hàm mất mát đo khoảng cách giữa phân phối dự đoán $p$ và nhãn One-hot $y$: $L = -\sum y_i \ln(p_i)$.
- **Gradient Logits ($p_i - y_i$):** Đạo hàm của hàm lỗi theo logit đầu vào bằng hiệu số giữa xác suất dự đoán và nhãn thực tế, mang ý nghĩa sai số trực tiếp.

🍼 **Hình dung thực tế cho em bé:**
Đây là công thức đẹp nhất trong Deep Learning! Gradient của hàm lỗi Cross-Entropy theo đầu vào logit chính là: ' Dự đoán trừ đi Thực tế ' ($p_i - y_i$). Nếu bạn dự đoán 90% (p=0.9) mà nhãn đúng là 1 (y=1), sai số là -0.1. Mạng chỉ cần đẩy logit lên thêm chút nữa!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng Chain Rule:
$$\frac{\partial L}{\partial z_i} = \sum_{k=1}^C \frac{\partial L}{\partial p_k} \frac{\partial p_k}{\partial z_i}$$
Trong đó:
1. $\frac{\partial L}{\partial p_k} = -\frac{y_k}{p_k}$.
2. Đạo hàm của Softmax:
$$\frac{\partial p_k}{\partial z_i} = \begin{cases} p_i(1 - p_i) & \text{nếu } k = i \\ -p_k p_i & \text{nếu } k \ne i \end{cases}$$
Thay vào:
$$\frac{\partial L}{\partial z_i} = -\frac{y_i}{p_i} p_i(1 - p_i) - \sum_{k \ne i} \frac{y_k}{p_k} (-p_k p_i)$$
$$= -y_i(1 - p_i) + p_i \sum_{k \ne i} y_k = -y_i + y_i p_i + p_i (1 - y_i) = p_i - y_i$$
(Vì vector One-hot thỏa mãn $\sum_{k=1}^C y_k = 1$, suy ra $\sum_{k \ne i} y_k = 1 - y_i$).
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Chỉ lấy đạo hàm riêng $-\frac{y_i}{p_i}$ (C) mà quên rằng thay đổi $z_i$ làm thay đổi TẤT CẢ các xác suất $p_k$ trong mẫu số Softmax! Hoặc nhầm với đạo hàm của Sigmoid $p_i(1 - p_i)$ (B).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát (Loss Functions)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B11: M06 giải thích về mặt giải tích gradient $\frac{\partial L}{\partial z_i} = p_i - y_i$ của Softmax kết hợp Cross-Entropy, bổ trợ trực tiếp cho OLP01-B11 về lý do vì sao trong PyTorch ta đưa raw logits trực tiếp vào `nn. CrossEntropyLoss()`.

---

### Câu 07 [VOAI02-M07] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Khoảng cách Mahalanobis giữa hai điểm $u, v \in \mathbb{R}^D$ được định nghĩa là $d_M(u, v) = \sqrt{(u - v)^T \Sigma^{-1} (u - v)}$, trong đó $\Sigma$ là ma trận hiệp phương sai. Ưu điểm vượt trội của khoảng cách Mahalanobis so với khoảng cách Euclid thông thường là gì?

- **A.** Chuẩn hóa phương sai từng biến và loại bỏ ảnh hưởng của tương quan tuyến tính giữa các chiều qua ma trận $\Sigma^{-1}$
- **B.** Chặn trên khoảng cách Manhattan và đảm bảo tính bất biến dưới mọi phép biến đổi tọa độ phi tuyến tùy ý
- **C.** Tối ưu hóa tốc độ tính toán ma trận nhanh hơn khoảng cách Euclid nhờ triệt tiêu hoàn toàn phép nhân đối xứng
- **D.** Đo lường độ tương đồng ngữ nghĩa trực tiếp trên dữ liệu chuỗi rời rạc mà không cần qua bước vector hóa

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Khoảng cách Mahalanobis:** Độ đo khoảng cách giữa hai điểm có tính đến tương quan và phương sai của các chiều đặc trưng: $d_M(u, v) = \sqrt{(u-v)^T \Sigma^{-1} (u-v)}$.
- **Ma trận hiệp phương sai ($\Sigma$):** Ma trận đo độ co giãn và góc nghiêng của đám mây dữ liệu.
- **Nghịch đảo $\Sigma^{-1}$:** Biến đổi chuẩn hóa đám mây hình ellipsoid nghiêng về dạng hình cầu đẳng hướng trước khi đo khoảng cách Euclid.

🍼 **Hình dung thực tế cho em bé:**
Khoảng cách Euclid coi mọi chiều đều bình đẳng và hình cầu. Nhưng nếu chiều chiều cao đo bằng mét (giá trị 1.7) còn cân nặng đo bằng gam (giá trị 70,000), khoảng cách Euclid sẽ bị cân nặng nuốt chửng! Khoảng cách Mahalanobis dùng ma trận hiệp phương sai để co giãn từng trục theo độ biến động của nó và ' xoay ' hệ trục để triệt tiêu tương quan giữa chiều cao và cân nặng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi $\Sigma = I$ (các đặc trưng độc lập và cùng phương sai bằng 1), khoảng cách Mahalanobis suy biến thành khoảng cách Euclid:
$$d_M(u, v) = \sqrt{(u - v)^T I (u - v)} = \|u - v\|_2$$
Khi các đặc trưng có phương sai khác nhau $\sigma_i^2$ và có tương quan (covariance $\sigma_{ij} \ne 0$), nghịch đảo ma trận hiệp phương sai $\Sigma^{-1}$ thực hiện chuẩn hóa whitening (xoay trục theo eigenvectors và chia độ lệch chuẩn theo eigenvalues), giúp đo khoảng cách thống kê thực sự không phụ thuộc vào đơn vị đo.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy tính toán: Nghịch đảo ma trận $\Sigma^{-1}$ có độ phức tạp $O(D^3)$, do đó khoảng cách Mahalanobis tính CHẬM hơn khoảng cách Euclid rất nhiều, không phải nhanh hơn (A sai).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.8 K-Means Clustering & Silhouette Score**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi lý thuyết độc lập mở rộng về khoảng cách trong không gian đặc trưng đa biến có tương quan: khi ma trận hiệp phương sai là ma trận đơn vị ($\Sigma = I$), khoảng cách Mahalanobis trở về đúng khoảng cách Euclid dùng trong thuật toán K-Means (§1.8).

---

### Câu 08 [VOAI02-M08] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong học máy, việc tối đa hóa hàm hợp lý hậu nghiệm (Maximum A Posteriori - MAP) trên trọng số $w$ tương đương với việc thêm số hạng điều chuẩn (regularization) vào hàm mất mát cực đại hóa hợp lý (MLE). Cụ thể, điều chuẩn $L_1$ (Lasso: $\lambda \|w\|_1$) và điều chuẩn $L_2$ (Ridge: $\frac{\lambda}{2} \|w\|_2^2$) tương ứng với giả định phân phối tiền nghiệm $P(w)$ nào?

- **A.** L1 tương ứng với Prior Gauss, L2 tương ứng với Prior Laplace
- **B.** L1 tương ứng với Prior Laplace, L2 tương ứng với Prior Gauss
- **C.** L1 tương ứng với Prior Poisson, L2 tương ứng với Prior Bernoulli
- **D.** Cả L1 và L2 đều tương ứng với Prior đều (Uniform Prior)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **MLE (Maximum Likelihood Estimation):** Ước lượng tham số chỉ dựa vào dữ liệu quan sát $\max_w P(D|w)$.
- **MAP (Maximum A Posteriori):** Ước lượng tham số kết hợp niềm tin tiên nghiệm (Prior): $\max_w P(D|w) P(w)$.
- **Gaussian Prior & L2 Regularization:** Giả định tiên nghiệm Gauss $w \sim \mathcal{N}(0, \sigma^2)$ tương đương toán học với hàm phạt L2 (Ridge / Weight Decay $\lambda \|w\|_2^2$).
- **Laplace Prior & L1 Regularization:** Giả định tiên nghiệm Laplace tương đương toán học với hàm phạt L1 (Lasso $\lambda \|w\|_1$).

🍼 **Hình dung thực tế cho em bé:**
Khi lấy log của xác suất: Phân phối Gauss có đuôi exp(-w²), log của nó ra -w² chính là phạt L2 (Ridge). Phân phối Laplace có đuôi exp(-|w|), log của nó ra -|w| chính là phạt L1 (Lasso)! Vì đỉnh của phân phối Laplace nhọn hoắt tại 0, nó ép các trọng số về đúng bằng 0 (tạo sparsity).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ước lượng MAP:
$$\hat{w}_{MAP} = \arg\max_w \ln P(D \mid w) + \ln P(w)$$
1. Nếu $P(w) \sim \text{Laplace}(0, b) = \frac{1}{2b} \exp\left(-\frac{|w|}{b}\right)$:
$$\ln P(w) = -\text{const} - \frac{1}{b} \|w\|_1 \implies -\ln P(w) = \lambda \|w\|_1 \quad (L_1 \text{ regularization})$$
2. Nếu $P(w) \sim \mathcal{N}(0, \sigma^2) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{w^2}{2\sigma^2}\right)$:
$$\ln P(w) = -\text{const} - \frac{1}{2\sigma^2} \|w\|_2^2 \implies -\ln P(w) = \frac{\lambda}{2} \|w\|_2^2 \quad (L_2 \text{ regularization})$$
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy rất hay lộn ngược: Sinh viên thường nhầm Gauss với L1 vì nghĩ Gauss phổ biến nhất. Nhớ quy tắc: Bình phương $\to$ Gauss ($e^{-x^2}$), Trị tuyệt đối $\to$ Laplace ($e^{-|x|}$).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§5.4 Ước Lượng Tham Số: MLE vs MAP**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C09: OLP01-C09 phân tích L1 vs L2 dưới góc độ điều chuẩn hình học trong học máy, còn M08 giải thích nguồn gốc xác suất Bayes của chúng: L2 tương ứng với tiên nghiệm Gauss, L1 tương ứng với tiên nghiệm Laplace trong ước lượng MAP.

---

### Câu 09 [VOAI02-M09] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho hai phân phối xác suất rời rạc $P$ và $Q$ trên cùng không gian mẫu. Phân kỳ Kullback-Leibler được định nghĩa là $D_{KL}(P \parallel Q) = \sum_x P(x) \ln \frac{P(x)}{Q(x)}$. Tính chất nào sau đây là **ĐÚNG** về $D_{KL}(P \parallel Q)$?

- **A.** $D_{KL}(P \parallel Q)$ luôn đối xứng: $D_{KL}(P \parallel Q) = D_{KL}(Q \parallel P)$
- **B.** $D_{KL}(P \parallel Q)$ là một metric khoảng cách toán học thỏa mãn bất đẳng thức tam giác
- **C.** $D_{KL}(P \parallel Q)$ có thể nhận giá trị âm nếu $Q(x) > P(x)$ tại nhiều điểm
- **D.** $D_{KL}(P \parallel Q) \ge 0$ (luôn không âm) và bằng 0 khi và chỉ khi $P = Q$ hầu khắp nơi

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **KL Divergence ($D_{KL}(P \parallel Q)$):** Độ đo lượng thông tin mất mát khi dùng phân phối xác suất $Q$ để xấp xỉ phân phối thực tế $P$: $D_{KL}(P \parallel Q) = \sum P(x) \log \frac{P(x)}{Q(x)}$.
- **Tính bất đối xứng (Asymmetry):** $D_{KL}(P \parallel Q) \ne D_{KL}(Q \parallel P)$, do đó KL Divergence không phải là một hàm khoảng cách (metric) toán học thực thụ.
- **Bất đẳng thức Gibbs:** $D_{KL}(P \parallel Q) \ge 0$ với mọi phân phối, đẳng thức xảy ra khi và chỉ khi $P = Q$.

🍼 **Hình dung thực tế cho em bé:**
KL Divergence đo xem phân phối Q ' lệch ' khỏi phân phối thật P bao nhiêu. Độ lệch này không bao giờ âm (nhỏ nhất là bằng 0 khi hai phân phối giống hệt nhau). Tuy nhiên, nó KHÔNG PHẢI là khoảng cách hình học vì nó bất đối xứng: từ nhà bạn đến trường khác từ trường về nhà bạn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Chứng minh $D_{KL}(P \parallel Q) \ge 0$ bằng bất đẳng thức Jensen:
Vì hàm số $f(t) = -\ln(t)$ là hàm lồi nghiêm ngặt (convex):
$$D_{KL}(P \parallel Q) = \sum_x P(x) \left( -\ln \frac{Q(x)}{P(x)} \right) = \mathbb{E}_{x \sim P} \left[ -\ln \frac{Q(x)}{P(x)} \right]$$
Áp dụng Jensen $\mathbb{E}[f(t)] \ge f(\mathbb{E}[t])$:
$$D_{KL}(P \parallel Q) \ge -\ln \left( \mathbb{E}_{x \sim P} \left[ \frac{Q(x)}{P(x)} \right] \right) = -\ln \left( \sum_x P(x) \frac{Q(x)}{P(x)} \right) = -\ln \left( \sum_x Q(x) \right) = -\ln(1) = 0$$
Dấu bằng xảy ra khi và chỉ khi $\frac{Q(x)}{P(x)} = 1 \iff P(x) = Q(x)$ với mọi $x$.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy kinh điển: KL Divergence KHÔNG PHẢI là một metric (distance metric) vì nó không đối xứng ($D_{KL}(P \parallel Q) \ne D_{KL}(Q \parallel P)$) và không thỏa mãn bất đẳng thức tam giác. Chọn A hoặc D là sai hoàn toàn.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát (Loss Functions)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M04: Cùng thuộc lý thuyết thông tin: VOAI03-M04 đo độ hỗn loạn nội tại của phân phối qua Shannon Entropy $H(P)$, còn M09 đo độ lệch tương đối giữa hai phân phối qua Phân kỳ KL $D_{KL}(P \parallel Q) = H(P, Q) - H(P)$.

---

### Câu 10 [VOAI02-M10] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Hàm kích hoạt SiLU (Sigmoid Linear Unit / Swish) được định nghĩa là $f(x) = x \cdot \sigma(x)$, trong đó $\sigma(x) = \frac{1}{1 + e^{-x}}$. Đạo hàm của hàm SiLU theo $x$, $f '(x)$, bằng biểu thức nào sau đây?

- **A.** $f '(x) = \sigma(x) + x \cdot \sigma(x)(1 - \sigma(x))$
- **B.** $f '(x) = \sigma(x) - x \cdot \sigma(x)(1 - \sigma(x))$
- **C.** $f '(x) = x \cdot \sigma(x) + \sigma(x)(1 - \sigma(x))$
- **D.** $f '(x) = 1 + x \cdot \sigma(x)(1 - \sigma(x))$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **SiLU (Sigmoid Linear Unit / Swish):** Hàm kích hoạt phi tuyến định nghĩa là $f(x) = x \cdot \sigma(x) = \frac{x}{1 + e^{-x}}$.
- **Smooth & Non-monotonic:** Khác với ReLU bị gãy khúc tại $x=0$, SiLU khả vi liên tục mọi bậc và không đơn điệu (đạt cực tiểu nhẹ $\approx -0.278$ tại $x \approx -1.28$).
- **Tự điều tiết (Self-Gated):** Giá trị $x$ được điều tiết bằng xác suất đi qua chính nó, giúp gradient lan truyền tốt hơn qua các tầng mạng rất sâu.

🍼 **Hình dung thực tế cho em bé:**
Hàm SiLU giống như việc cho x nhân với một cánh cổng Sigmoid. Khi tính đạo hàm, ta áp dụng quy tắc đạo hàm của tích: (u · v)' = u '·v + u·v '. Vì đạo hàm của x là 1, đạo hàm của Sigmoid là σ(1 - σ), ta ghép lại ra ngay công thức!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng quy tắc đạo hàm của tích hai hàm số $f(x) = u(x) v(x)$ với $u(x) = x$ và $v(x) = \sigma(x)$:
$$f '(x) = u '(x) v(x) + u(x) v '(x)$$
Ta có:
- $u '(x) = \frac{d}{dx}[x] = 1$
- $v '(x) = \frac{d}{dx}[\sigma(x)] = \sigma(x)(1 - \sigma(x))$
Thay vào:
$$f '(x) = 1 \cdot \sigma(x) + x \cdot \sigma(x)(1 - \sigma(x)) = \sigma(x) [1 + x(1 - \sigma(x))]$$
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Chỉ đạo hàm phần Sigmoid mà bỏ qua phần $x$ (B), hoặc nhầm lẫn công thức đạo hàm tích.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.2 Các hàm kích hoạt (Activation Functions)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C20: Cùng kiểm tra các hàm kích hoạt hiện đại: OLP01-C20 khẳng định SiLU/GELU vượt trội hơn ReLU trong Transformer và mạng sâu, còn M10 đi sâu vào công thức giải tích $f(x) = x \cdot \sigma(x)$ và tính chất không đơn điệu của SiLU.

---

### Câu 11 [VOAI02-M11] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho $Q \in \mathbb{R}^{n \times n}$ là một ma trận trực giao (orthogonal matrix, thỏa mãn $Q^T Q = Q Q^T = I$). Với bất kỳ vector $x \in \mathbb{R}^n$, chuẩn Euclid của vector sau khi biến đổi $\|Qx\|_2$ có mối quan hệ như thế nào với $\|x\|_2$?

- **A.** $\|Qx\|_2 = \|x\|_2$
- **B.** $\|Qx\|_2 = |\det(Q)| \cdot \|x\|_2$
- **C.** $\|Qx\|_2 \le \|x\|_2$
- **D.** $\|Qx\|_2 \ge \|x\|_2$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Ma trận trực giao (Orthogonal Matrix):** Ma trận vuông $Q$ thỏa mãn $Q^T Q = Q Q^T = I$, nghĩa là các cột (và các hàng) tạo thành một hệ trực chuẩn.
- **Bảo toàn chuẩn Euclid:** Với mọi vector $x$, $\|Q x\|_2^2 = (Q x)^T (Q x) = x^T Q^T Q x = x^T I x = \|x\|_2^2$.
- **Ý nghĩa hình học:** Phép nhân với ma trận trực giao tương ứng với phép quay (Rotation) hoặc phép phản xạ (Reflection) không gian, bảo toàn nguyên vẹn độ dài và góc giữa các vector.

🍼 **Hình dung thực tế cho em bé:**
Ma trận trực giao giống như động tác xoay hoặc lật một món đồ trong không gian. Khi bạn xoay một cây bút chì, độ dài của nó hoàn toàn không đổi. Vì thế chuẩn Euclid của vector qua ma trận trực giao luôn được bảo toàn 100%!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Bình phương chuẩn Euclid của $Qx$:
$$\|Qx\|_2^2 = (Qx)^T (Qx) = x^T (Q^T Q) x$$
Vì $Q$ trực giao nên $Q^T Q = I$:
$$\|Qx\|_2^2 = x^T I x = x^T x = \|x\|_2^2$$
Lấy căn bậc hai hai vế suy ra:
$$\|Qx\|_2 = \|x\|_2$$
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy đề thi: Đáp án B đưa định thức $\det(Q)$ vào gây nhiễu. Mặc dù $\det(Q) = \pm 1$, chuẩn vector luôn không âm nên không thể nhân với $\det(Q)$ khi $\det(Q) = -1$ (phép phản xạ).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.10 Tiền xử lý Đặc trưng & Thao tác NumPy**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M01: Cùng kiểm tra định nghĩa và tính chất của ma trận trực giao: cả hai câu đều khẳng định ma trận trực giao bảo toàn tích vô hướng và độ dài vector Euclid ($A^T A = I \implies \|A x\| = \|x\|$).

---

### Câu 12 [VOAI02-M12] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Khi cần tính xấp xỉ kỳ vọng $\mathbb{E}_{x \sim P}[f(x)]$ nhưng việc lấy mẫu trực tiếp từ phân phối $P(x)$ quá khó khăn hoặc tốn kém, kỹ thuật Lấy mẫu tầm quan trọng (Importance Sampling) cho phép lấy mẫu từ một phân phối đề xuất $Q(x)$ dễ lấy mẫu hơn ($Q(x) > 0$ khi $P(x) > 0$). Công thức ước lượng không chệch là:

- **A.** $\mathbb{E}_{x \sim P}[f(x)] = \frac{1}{M} \sum_{i=1}^M f(x_i) \frac{P(x_i)}{Q(x_i)} \quad \text{với } x_i \sim Q$
- **B.** $\mathbb{E}_{x \sim P}[f(x)] = \frac{1}{M} \sum_{i=1}^M f(x_i) [P(x_i) - Q(x_i)] \quad \text{với } x_i \sim Q$
- **C.** $\mathbb{E}_{x \sim P}[f(x)] = \frac{1}{M} \sum_{i=1}^M f(x_i) \quad \text{với } x_i \sim Q$
- **D.** $\mathbb{E}_{x \sim P}[f(x)] = \frac{1}{M} \sum_{i=1}^M f(x_i) \frac{Q(x_i)}{P(x_i)} \quad \text{với } x_i \sim Q$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Importance Sampling:** Kỹ thuật xấp xỉ kỳ vọng của hàm số theo phân phối $P$ bằng cách lấy mẫu từ một phân phối đề xuất $Q$ dễ lấy mẫu hơn.
- **Likelihood Ratio / Importance Weight:** Trọng số $w(x) = \frac{P(x)}{Q(x)}$ bù trừ sai lệch xác suất giữa hai phân phối.
- **Công thức bất biến:** $\mathbb{E}_{x \sim P}[f(x)] = \int f(x) P(x) dx = \int f(x) \frac{P(x)}{Q(x)} Q(x) dx = \mathbb{E}_{x \sim Q}\left[f(x) \frac{P(x)}{Q(x)}\right]$.

🍼 **Hình dung thực tế cho em bé:**
Bạn muốn khảo sát chiều cao trung bình của học sinh (phân phối P), nhưng chỉ gặp được các vận động viên bóng rổ (phân phối Q). Để không bị lệch, mỗi khi phỏng vấn một người từ nhóm Q, bạn phải nhân với một ' trọng số điều chỉnh ' là P(x)/Q(x). Ai thuộc nhóm hiếm gặp trong P sẽ bị hạ trọng số, ai thuộc nhóm phổ biến sẽ được tăng trọng số!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Biến đổi tích phân kỳ vọng:
$$\mathbb{E}_{x \sim P}[f(x)] = \int f(x) P(x) dx = \int f(x) \frac{P(x)}{Q(x)} Q(x) dx = \mathbb{E}_{x \sim Q}\left[ f(x) \frac{P(x)}{Q(x)} \right]$$
Ước lượng Monte Carlo với $M$ mẫu $x_1, x_2, \dots, x_M \sim Q$:
$$\hat{\mu} = \frac{1}{M} \sum_{i=1}^M f(x_i) w(x_i), \quad \text{với trọng số quan trọng } w(x_i) = \frac{P(x_i)}{Q(x_i)}$$
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy phổ biến: Lộn ngược tỉ số trọng số thành $Q(x)/P(x)$ (C) hoặc quên nhân trọng số điều chỉnh (A - gây chệch nghiêm trọng).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§5.6 Tương Quan vs Nhân Quả (Correlation vs Causation) & Kỹ Thuật Lấy Mẫu**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi độc lập nâng cao về kỹ thuật lấy mẫu Monte Carlo và xấp xỉ kỳ vọng toán học khi không thể lấy mẫu trực tiếp từ phân phối mục tiêu $P(x)$ (§5.6).

---

### Câu 13 [VOAI02-M13] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Vì sao thuật toán k-Nearest Neighbors (k-NN) được xếp vào nhóm ' Lazy Learner ' (người học lười biếng), và độ phức tạp tính toán tại pha dự đoán (Inference Phase) cho một điểm dữ liệu mới trên tập huấn luyện kích thước $N$ mẫu, $D$ chiều là bao nhiêu?

- **A.** Lưu trữ cấu trúc cây nhị phân phân cấp; Độ phức tạp tại pha dự đoán là $O(D^2)$
- **B.** Không có pha huấn luyện tham số tường minh; Độ phức tạp tại pha dự đoán là $O(N \cdot D)$
- **C.** Tự động loại bỏ đặc trưng nhiễu không gian; Độ phức tạp tại pha dự đoán là $O(\log N)$
- **D.** Cập nhật trọng số qua lan truyền ngược; Độ phức tạp tại pha dự đoán là $O(1)$

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **k-NN (k-Nearest Neighbors):** Thuật toán phân loại/hồi quy dựa trên khoảng cách tới $k$ điểm dữ liệu gần nhất trong tập huấn luyện.
- **Lazy Learner (Người học lười biếng):** Thuật toán không có pha huấn luyện tham số trước ($O(1)$ khi fit), chỉ lưu toàn bộ tập dữ liệu vào bộ nhớ.
- **Chi phí suy luận cao:** Khi dự đoán một điểm mới, phải tính khoảng cách tới toàn bộ $N$ mẫu trong không gian $D$ chiều, chi phí tính toán là $O(N \cdot D)$.

🍼 **Hình dung thực tế cho em bé:**
k-NN giống như một học sinh không bao giờ chịu học bài trước kỳ thi (Lazy). Khi vào phòng thi gặp câu hỏi mới, bạn ấy mới mở toàn bộ kho đề (N mẫu) ra và so sánh từng câu (D chiều) với câu hỏi hiện tại để tìm k câu giống nhất. Do đó lúc thi (inference) rất chậm vì phải quét qua toàn bộ dữ liệu: O(N · D)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khác với Eager Learners (như Linear Regression, SVM, Deep Learning) tối ưu hóa một tập trọng số $\theta^*$ trong giai đoạn train để dự đoán trong $O(D)$, k-NN không học hàm ánh xạ tổng quát nào. Khi có điểm mới $x_{test}$, k-NN phải tính khoảng cách Euclid (hoặc Minkowski) tới tất cả $N$ điểm trong tập train:
$$d(x_{test}, x_i) = \sqrt{\sum_{j=1}^D (x_{test, j} - x_{i, j})^2}$$
Mỗi phép tính khoảng cách tốn $O(D)$, quét $N$ mẫu tốn $O(N \cdot D)$. Sau đó tìm top $k$ phần tử nhỏ nhất tốn $O(N + k \log N)$. Tổng thời gian là $O(N \cdot D)$.
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy thường gặp: Nhầm lẫn giữa pha train (k-NN train tốn $O(1)$) và pha test (k-NN test tốn $O(N \cdot D)$). Rất nhiều thí sinh nghĩ test luôn nhanh $O(1)$ như mô hình tuyến tính.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C01: Cùng kiểm tra bản chất Lazy Learner của k-NN: OLP01-C01 tập trung vào đặc điểm không học trọng số ở pha huấn luyện, còn M13 phân tích sâu thêm độ phức tạp tính toán suy luận $O(N \cdot D)$ khi phải quét toàn bộ tập dữ liệu.

---

### Câu 14 [VOAI02-M14] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán Soft-Margin SVM, hàm mục tiêu tối thiểu hóa là $\min_{w, b, \xi} \frac{1}{2} \|w\|_2^2 + C \sum_{i=1}^N \xi_i$. Khi ta thiết lập giá trị $C$ **RẤT LỚN** ($C \to \infty$), mô hình SVM sẽ có xu hướng nào?

- **A.** Thu hẹp độ dốc hàm mất mát, biến mô hình thành hồi quy bình phương tối thiểu Ordinary Least Squares
- **B.** Triệt tiêu toàn bộ vector trọng số w về 0 để tối đa hóa độ rộng của lề phân cách giữa hai lớp dữ liệu
- **C.** Ưu tiên lề rộng tối đa, chấp nhận nhiều điểm vi phạm lề nhằm tăng độ chệch (Bias) và giảm phương sai
- **D.** Phạt cực nặng điểm vi phạm lề, ép lề hẹp lại để phân loại đúng tập train nhằm giảm Bias và tăng nguy cơ Overfitting

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Soft-Margin SVM:** Mô hình SVM cho phép một số điểm dữ liệu vi phạm lề hoặc bị phân loại sai để xử lý tập dữ liệu không phân tách tuyến tính hoàn hảo.
- **Biến bù Slack ($\xi_i \ge 0$):** Khoảng cách mà điểm thứ $i$ vi phạm lề ($0 < \xi_i \le 1$: nằm trong lề nhưng đúng lớp; $\xi_i > 1$: phân loại sai).
- **Siêu tham số $C$:** Đánh đổi giữa độ rộng lề $\frac{1}{2}\|w\|^2$ và tổng mức độ phạt vi phạm $C \sum \xi_i$. $C$ càng lớn thì phạt vi phạm càng nặng, ranh giới càng khắt khe $\implies$ nguy cơ Overfitting.

🍼 **Hình dung thực tế cho em bé:**
Tham số C giống như mức độ nghiêm khắc của giám khảo với lỗi sai (ξ). Nếu C rất lớn (cực kỳ nghiêm khắc), giám khảo không tha thứ cho bất kỳ điểm nào đứng sai vị trí, chấp nhận thu hẹp hành lang an toàn (margin) lại sát mép để không có ai phạm quy -> Rất dễ học vẹt (Overfitting)! Ngược lại C nhỏ thì phóng khoáng hơn, chấp nhận vài điểm phạm quy để đổi lấy hành lang rộng rãi, tổng quát tốt hơn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Hàm mục tiêu Soft-Margin SVM cân bằng giữa hai mục tiêu đối nghịch:
1. $\frac{1}{2} \|w\|_2^2$: Tối đa hóa độ rộng margin $\frac{2}{\|w\|_2}$ (tăng tính tổng quát).
2. $C \sum_{i=1}^N \xi_i$: Phạt các điểm vi phạm ràng buộc $y_i (w^T x_i + b) \ge 1 - \xi_i$.
- Khi $C \to \infty$, số hạng phạt $\xi_i$ áp đảo. Mô hình buộc phải ép $\xi_i \to 0$, tiệm cận bài toán Hard-Margin SVM. Margin bị thu hẹp tối đa để loại bỏ lỗi train $\implies$ Mô hình nhạy cảm với outliers, Variance tăng cao, nguy cơ Overfitting rất lớn.
- Khi $C$ nhỏ, mô hình ưu tiên margin rộng, chấp nhận nhiều điểm rơi vào trong margin $\implies$ Bias tăng, Variance giảm (chống Overfitting).
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy phòng thi: Nhiều thí sinh nhầm lẫn tác động của $C$ trong SVM với hệ số phạt $\lambda$ trong Ridge Regression ($C \sim 1/\lambda$). $C$ lớn nghĩa là phạt sai số trên train nhiều $\implies$ Regularization YẾU $\implies$ Overfitting!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.2 Support Vector Machines (SVM & Kernel Trick)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C03: Cùng kiểm tra lý thuyết lề trong SVM: OLP01-C03 xem xét Hard-Margin nguyên bản, còn M14 phân tích mối liên hệ khi siêu tham số phạt $C \to \infty$ của Soft-Margin sẽ tiệm cận về đúng bài toán Hard-Margin.

---

### Câu 15 [VOAI02-M15] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kernel RBF (Radial Basis Function / Gaussian Kernel) trong SVM có dạng $K(x, z) = \exp(-\gamma \|x - z\|^2)$. Nếu ta chọn giá trị $\gamma$ **QUÁ LỚN**, ranh giới quyết định (Decision Boundary) của SVM sẽ biến đổi như thế nào?

- **A.** Biến ranh giới phân loại thành một siêu phẳng tuyến tính phẳng hoàn toàn, gây hiện tượng Underfitting
- **B.** Giữ nguyên ranh giới quyết định vì gamma chỉ kiểm soát tốc độ hội tụ của thuật toán tối ưu hóa lồi
- **C.** Tạo ra các ranh giới co cụm cực hẹp quanh từng điểm dữ liệu mẫu, dẫn đến Overfitting nghiêm trọng
- **D.** Làm mịn hóa ranh giới phân chia trên toàn bộ không gian đặc trưng, dẫn đến Underfitting nghiêm trọng

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Kernel RBF (Radial Basis Function / Gaussian):** Hàm nhân đo độ tương đồng không gian phi tuyến: $K(x, z) = \exp(-\gamma \|x - z\|^2)$.
- **Siêu tham số $\gamma$ (Gamma):** Nghịch đảo phương sai của phân phối Gauss ($\gamma = \frac{1}{2\sigma^2}$), quyết định bán kính ảnh hưởng của từng điểm hỗ trợ (Support Vector).
- **Khi $\gamma$ quá lớn:** Bán kính ảnh hưởng rất hẹp, mô hình chỉ ghi nhớ từng điểm huấn luyện riêng lẻ, tạo ra các đảo ranh giới cục bộ quanh từng điểm $\implies$ Overfitting nặng.

🍼 **Hình dung thực tế cho em bé:**
Gamma (γ) quyết định tầm ảnh hưởng của một điểm dữ liệu. Nếu gamma nhỏ, mỗi điểm phát ra vầng sáng rộng lan tỏa, hòa vào nhau tạo thành đường biên mượt mà. Nếu gamma quá lớn, mỗi điểm chỉ phát ra một đốm sáng nhỏ li ti cục bộ; ranh giới quyết định sẽ bị cắt xé thành từng ' hòn đảo ' bao quanh từng điểm huấn luyện riêng lẻ -> Học vẹt hoàn toàn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ta có $\gamma = \frac{1}{2\sigma^2}$ trong phân phối Gauss:
$$K(x, z) = \exp\left(-\frac{\|x - z\|^2}{2\sigma^2}\right)$$
- Khi $\gamma \to \infty$ (tương ứng $\sigma \to 0$), hàm kernel suy biến thành $K(x, z) \to 0$ khi $x \ne z$ và $K(x, x) = 1$. Mỗi support vector chỉ có tầm ảnh hưởng trong một bán kính cực kỳ nhỏ xung quanh chính nó. Ranh giới quyết định sẽ tạo thành các vùng cô lập quanh từng điểm huấn luyện cá biệt $\implies$ Variance cực lớn, Overfitting nghiêm trọng.
- Khi $\gamma$ nhỏ, bán kính ảnh hưởng lớn $\implies$ Ranh giới mượt mà, tiệm cận mô hình tuyến tính $\implies$ Bias cao, Variance thấp.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Nhầm chiều biến thiên của $\gamma$ với phương sai $\sigma^2$. Nhớ: $\gamma$ TỶ LỆ NGHỊCH với $\sigma^2$. $\gamma$ lớn = $\sigma$ bé = phạm vi ảnh hưởng hẹp = Overfitting!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.2 Support Vector Machines (SVM & Kernel Trick)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C04: Cùng phân tích hành vi của siêu tham số $\gamma$ trong RBF Kernel: giá trị $\gamma$ quá lớn làm thu hẹp bán kính ảnh hưởng của từng Support Vector, tạo các ranh giới cục bộ gây Overfitting nghiêm trọng.

---

### Câu 16 [VOAI02-M16] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Tại một nút lá của bài toán phân loại nhị phân ($K = 2$), tỉ lệ mẫu của hai lớp là $p_1 = 0.8$ và $p_2 = 0.2$. Giá trị của chỉ số độ tinh khiết Gini Impurity ($I_G$) tại nút này bằng bao nhiêu?

- **A.** 0.64
- **B.** 0.50
- **C.** 0.32
- **D.** 0.16

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Gini Impurity ($I_G$):** Độ đo mức độ không thuần khiết tại một nút cây quyết định: $I_G = 1 - \sum_{k=1}^K p_k^2$.
- **Ý nghĩa xác suất:** Xác suất một phần tử ngẫu nhiên bị phân loại sai nếu ta gán nhãn ngẫu nhiên cho nó theo phân phối xác suất của nút.
- **Nút thuần khiết hoàn toàn:** $I_G = 0$ khi tất cả các mẫu đều thuộc về duy nhất một lớp ($p_1 = 1$).

🍼 **Hình dung thực tế cho em bé:**
Gini Impurity đo mức độ ' lẫn lộn ' của một nhóm. Công thức tính là: 1 trừ đi tổng bình phương tỉ lệ từng lớp. Ở đây: 1 - (0.8² + 0.2²) = 1 - (0.64 + 0.04) = 1 - 0.68 = 0.32. Nếu nút hoàn toàn thuần khiết (100% lớp 1), Gini bằng 0.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Gini Impurity cho tập gồm $K$ lớp:
$$I_G = 1 - \sum_{i=1}^K p_i^2$$
Với $K = 2$, $p_1 = 0.8$, $p_2 = 0.2$:
$$I_G = 1 - (0.8^2 + 0.2^2) = 1 - (0.64 + 0.04) = 1 - 0.68 = 0.32$$
Hoặc dạng tương đương cho 2 lớp:
$$I_G = 2 p_1 p_2 = 2 \times 0.8 \times 0.2 = 0.32$$
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy tính toán: Thí sinh tính nhầm $0.8 \times 0.2 = 0.16$ mà quên nhân 2 (B); hoặc nhầm với Entropy $- (0.8 \log_2 0.8 + 0.2 \log_2 0.2) \approx 0.722$.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định (Decision Tree), Entropy & Information Gain**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B04: Cùng thuộc bài toán đo độ hỗn loạn của nút trong cây quyết định: OLP01-B04 tính độ đo Entropy Shannon ($-\sum p_i \log_2 p_i$), còn M16 tính độ đo Gini Impurity ($1 - \sum p_i^2$) dùng trong thuật toán CART.

---

### Câu 17 [VOAI02-M17] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán Random Forest, mỗi cây con được xây dựng trên một tập mẫu Bootstrap kích thước $N$ (lấy mẫu có hoàn lại từ tập dữ liệu gốc gồm $N$ mẫu). Về mặt lý thuyết khi $N \to \infty$, tỉ lệ xấp xỉ phần trăm mẫu trong tập dữ liệu gốc **KHÔNG ĐƯỢC CHỌN** vào tập Bootstrap (được gọi là tập Out-Of-Bag - OOB) là bao nhiêu?

- **A.** Khoảng 36.8%
- **B.** Khoảng 5.0%
- **C.** Khoảng 50.0%
- **D.** Khoảng 63.2%

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Bootstrap Sampling:** Phương pháp lấy mẫu có hoàn lại kích thước $N$ từ tập $N$ mẫu gốc.
- **Out-Of-Bag (OOB):** Tập hợp các mẫu không được chọn vào mẫu Bootstrap của một cây con.
- **Xác suất một mẫu không được chọn:** $(1 - \frac{1}{N})^N$. Khi $N \to \infty$, giới hạn này hội tụ về $\frac{1}{e} \approx 0.368$ (khoảng $36.8\%$).

🍼 **Hình dung thực tế cho em bé:**
Khi bốc thăm N lần có hoàn lại từ N lá phiếu, xác suất một lá phiếu xui xẻo không bao giờ được bốc trúng là (1 - 1/N)^N. Khi N lớn, con số này tiệm cận đúng 1/e ≈ 36.8%! Nghĩa là có khoảng 36.8% dữ liệu nằm ngoài tập huấn luyện của cây đó, ta có thể dùng luôn tập này để kiểm tra (test OOB) miễn phí mà không cần chia tập validation riêng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Xác suất một mẫu cụ thể KHÔNG được chọn trong 1 lần rút là $1 - \frac{1}{N}$.
Vì $N$ lần rút là độc lập có hoàn lại, xác suất mẫu đó KHÔNG được chọn trong toàn bộ $N$ lần rút là:
$$P(\text{không được chọn}) = \left(1 - \frac{1}{N}\right)^N$$
Lấy giới hạn khi kích thước dữ liệu $N \to \infty$:
$$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = \frac{1}{e} \approx \frac{1}{2.71828} \approx 0.367879 \approx 36.8\%$$
Số mẫu được chọn vào cây là $1 - 36.8\% \approx 63.2\%$.
Tập mẫu không được chọn gọi là Out-Of-Bag (OOB), chiếm khoảng **36.8%**.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy kinh điển: Thí sinh nhầm lẫn giữa tỉ lệ mẫu ĐƯỢC CHỌN (63.2% - C) và tỉ lệ mẫu KHÔNG ĐƯỢC CHỌN / OOB (36.8% - B). Đề bài hỏi rõ ' KHÔNG ĐƯỢC CHỌN '.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Random Forest & Phương pháp Ensemble**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C17: OLP01-C17 giải thích khả năng giảm phương sai của Random Forest nhờ cơ chế Bagging, còn M17 chứng minh bằng toán học xác suất tỉ lệ $\approx 36.8\%$ dữ liệu OOB đóng vai trò như tập kiểm thử độc lập cho từng cây con.

---

### Câu 18 [VOAI02-M18] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán AdaBoost phân loại nhị phân ($y_i \in \{-1, +1\}$), tại vòng lặp $t$, bộ phân loại yếu $h_t(x)$ có tỉ lệ lỗi có trọng số là $\epsilon_t$. Trọng số của bộ phân loại này được tính là $\alpha_t = \frac{1}{2} \ln\left(\frac{1 - \epsilon_t}{\epsilon_t}\right)$. Khi cập nhật trọng số cho mẫu thứ $i$ ở vòng tiếp theo $w_{t+1, i} \propto w_{t, i} \exp(-\alpha_t y_i h_t(x_i))$, điều gì sẽ xảy ra?

- **A.** Toàn bộ các mẫu dữ liệu đều được nhân đôi trọng số phân loại nhằm tăng tốc độ hội tụ của thuật toán
- **B.** Trọng số của tất cả các mẫu bị mô hình dự đoán sai sẽ bị gán về 0 để loại bỏ hoàn toàn khỏi tập huấn luyện
- **C.** Các mẫu bị mô hình $h_t$ đoán SAI sẽ được TĂNG trọng số, các mẫu đoán ĐÚNG sẽ bị GIẢM trọng số
- **D.** Các mẫu đoán đúng được tăng trọng số theo hàm số mũ để mô hình tập trung khai thác các vùng dữ liệu an toàn

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **AdaBoost (Adaptive Boosting):** Thuật toán Ensemble tuần tự, tăng trọng số cho các mẫu bị phân loại sai để cây tiếp theo tập trung sửa sai.
- **Trọng số bộ phân loại ($\alpha_t$):** $\alpha_t = \frac{1}{2} \ln\left(\frac{1-\epsilon_t}{\epsilon_t}\right)$, mô hình nào có tỉ lệ lỗi $\epsilon_t$ càng thấp thì tiếng nói $\alpha_t$ càng lớn.
- **Quy tắc cập nhật:** $w_{t+1, i} \propto w_{t, i} \exp(-\alpha_t y_i h_t(x_i))$. Nếu đoán đúng ($y_i h_t = 1$), trọng số giảm; nếu đoán sai ($y_i h_t = -1$), trọng số nhân thêm $\exp(\alpha_t) > 1$.

🍼 **Hình dung thực tế cho em bé:**
AdaBoost giống như một người thầy thông minh: sau mỗi bài kiểm tra, thầy xem học sinh làm sai câu nào thì gắn sao đỏ cảnh báo vào câu đó (tăng trọng số), còn câu nào cả lớp đã làm đúng rồi thì giảm chú ý (giảm trọng số). Cây tiếp theo bắt buộc phải tập trung giải những câu khó mà cây trước làm sai!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Giả sử $\epsilon_t < 0.5$ (bộ phân loại tốt hơn đoán mò ngẫu nhiên), khi đó $\frac{1 - \epsilon_t}{\epsilon_t} > 1 \implies \alpha_t > 0$.
Số hạng mũ $\exp(-\alpha_t y_i h_t(x_i))$ phụ thuộc vào tính đúng sai của dự đoán:
1. Nếu đoán SAI: $y_i \ne h_t(x_i) \implies y_i h_t(x_i) = -1$.
$$w_{t+1, i} \propto w_{t, i} \exp(\alpha_t) = w_{t, i} \sqrt{\frac{1 - \epsilon_t}{\epsilon_t}} > w_{t, i} \quad (\text{TĂNG trọng số})$$
2. Nếu đoán ĐÚNG: $y_i = h_t(x_i) \implies y_i h_t(x_i) = +1$.
$$w_{t+1, i} \propto w_{t, i} \exp(-\alpha_t) = w_{t, i} \sqrt{\frac{\epsilon_t}{1 - \epsilon_t}} < w_{t, i} \quad (\text{GIẢM trọng số})$$
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy dấu: Nhìn vào $-\alpha_t y_i h_t$ tưởng là luôn giảm. Chú ý rằng khi đoán sai, $y_i h_t(x_i) = -1$, hai dấu trừ nhân nhau thành dấu CỘNG $\exp(+\alpha_t)$ nên trọng số TĂNG!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Random Forest & Phương pháp Ensemble**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M41: VOAI03-M41 phân biệt Bagging (song song) và Boosting (tuần tự), còn M18 phân tích sâu công thức toán học cập nhật trọng số mẫu trong thuật toán nền tảng AdaBoost giúp các cây sau tập trung sửa sai cho các cây trước.

---

### Câu 19 [VOAI02-M19] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khác biệt cốt lõi trong thuật toán tối ưu hóa giữa Gradient Boosting truyền thống (GBM của Friedman) và XGBoost (Chen & Guestrin) là gì?

- **A.** XGBoost chỉ dùng khai triển Taylor bậc một (Gradient Only) kết hợp thuật toán tối ưu hóa ngẫu nhiên theo mini-batch
- **B.** GBM dùng khai triển Taylor bậc hai (Hessian Matrix) kết hợp L2, trong khi XGBoost chỉ tối ưu sai phân bậc một đơn giản
- **C.** GBM dùng phân tích ma trận Hessian (Second Order) đầy đủ, trong khi XGBoost bỏ qua hoàn toàn thông tin đạo hàm bậc hai
- **D.** XGBoost áp dụng xấp xỉ Taylor bậc hai (Gradient & Hessian) cho hàm mất mát và tích hợp điều chuẩn L1/L2

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Gradient Boosting truyền thống (GBM):** Sử dụng phép tính xấp xỉ đạo hàm bậc một (Negative Gradient / Pseudo-Residuals) để khớp cây quyết định mới.
- **XGBoost (Extreme Gradient Boosting):** Sử dụng khai triển Taylor bậc hai của hàm mất mát, kết hợp cả đạo hàm bậc một ($g_i$) và đạo hàm bậc hai ($h_i$) tại mỗi bước tối ưu.
- **Điều chuẩn hóa trong hàm mục tiêu:** XGBoost đưa trực tiếp số lượng lá ($T$) và trọng số lá ($w$) vào hàm mục tiêu với hệ số $\gamma$ và $\lambda$.

🍼 **Hình dung thực tế cho em bé:**
GBM truyền thống giống như bước đi xuống dốc chỉ bằng mắt nhìn độ dốc (gradient bậc 1). Còn XGBoost giống như dùng radar quét cả độ dốc lẫn độ cong của mặt đất (Hessian bậc 2), giúp bước những bước chuẩn xác như phương pháp Newton-Raphson và tự động phạt các nhánh cây quá rườm rà!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tại vòng lặp $t$, hàm mục tiêu tối ưu của cây mới $f_t(x)$:
$$\mathcal{L}^{(t)} = \sum_{i=1}^N l(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) + \Omega(f_t)$$
Khai triển Taylor bậc hai quanh $\hat{y}_i^{(t-1)}$:
$$\mathcal{L}^{(t)} \approx \sum_{i=1}^N \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t(x_i)^2 \right] + \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
Trong đó:
- Gradient bậc một: $g_i = \partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}_i^{(t-1)})$
- Hessian bậc hai: $h_i = \partial^2_{\hat{y}^{(t-1)}} l(y_i, \hat{y}_i^{(t-1)})$
Nhờ khai triển bậc 2, XGBoost tìm được trọng số lá tối ưu giải tích $w_j^* = -\frac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda}$ mà không cần xấp xỉ đường dốc đơn giản.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Nhầm lẫn ngược lại rằng GBM dùng bậc 2 còn XGBoost dùng bậc 1 (A). Luôn nhớ: XGBoost nổi tiếng chính nhờ bước nhảy Newton cấp 2 (Second-order Taylor expansion).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Random Forest & Phương pháp Ensemble**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M48: VOAI03-M48 kiểm tra nguyên lý Gradient Boosting truyền thống khớp cây con vào đạo hàm bậc 1, còn M19 phân tích bước tiến của XGBoost khi tối ưu hóa hàm mục tiêu bằng khai triển Taylor bậc hai ($g_i$ và $h_i$).

---

### Câu 20 [VOAI02-M20] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** LightGBM đạt tốc độ huấn luyện vượt trội trên các tập dữ liệu lớn so với XGBoost truyền thống chủ yếu nhờ vào hai kỹ thuật nào sau đây?

- **A.** Phát triển cây theo chiều sâu cân bằng (Level-wise depth-first) kết hợp thuật toán lọc nhiễu ngoại lai toàn cục
- **B.** Chuyển toàn bộ cấu trúc cây sang dạng bảng băm trực tiếp và chỉ sử dụng hàm mất mát bình phương tối thiểu MSE
- **C.** Phát triển cây theo độ đối xứng nhánh (Symmetric tree growth) kết hợp chuẩn hóa ma trận đặc trưng đầu vào
- **D.** Phát triển cây theo nút lá tối ưu (Leaf-wise best-first) kết hợp lấy mẫu GOSS và gộp đặc trưng độc quyền EFB

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **GOSS (Gradient-based One-Side Sampling):** Giữ lại toàn bộ các mẫu có gradient lớn (chưa học tốt) và chỉ lấy mẫu ngẫu nhiên một tỉ lệ nhỏ các mẫu có gradient bé.
- **EFB (Exclusive Feature Bundling):** Gộp các đặc trưng loại trừ lẫn nhau (hiếm khi cùng nhận giá trị khác 0) thành một đặc trưng đơn lẻ để giảm chiều dữ liệu.
- **Leaf-wise Tree Growth:** Mọc cây theo nhánh có độ giảm hàm mất mát lớn nhất thay vì mọc cân bằng theo tầng (Depth-wise).

🍼 **Hình dung thực tế cho em bé:**
Thay vì bắt tất cả các cành phải mọc đều chằn chặn cùng một tầng (Level-wise như XGBoost cũ), LightGBM chọn cành nào đang đem lại nhiều lợi ích giảm lỗi nhất thì ưu tiên cho mọc tiếp (Leaf-wise). Đồng thời, LightGBM dùng GOSS: giữ lại tất cả các mẫu có sai số lớn (gradient lớn) và chỉ lấy mẫu ngẫu nhiên một phần nhỏ các mẫu có sai số bé, giúp giảm 80% thời gian tính toán mà độ chính xác gần như không đổi!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **Leaf-wise tree growth**: Tìm nút lá tối đa hóa độ giảm hàm mất mát (loss reduction) trên toàn bộ cây để rẽ nhánh, giúp giảm sai số nhanh hơn nhiều so với Level-wise cùng số lượng lá.
2. **GOSS (Gradient-based One-Side Sampling)**: Các mẫu có gradient nhỏ là các mẫu đã được huấn luyện tốt. GOSS sắp xếp các mẫu theo $|g_i|$, giữ lại top $a \times 100\%$ mẫu có gradient lớn nhất, và lấy mẫu ngẫu nhiên $b \times 100\%$ từ tập còn lại, sau đó nhân trọng số $\frac{1-a}{b}$ cho các mẫu nhỏ để duy trì kỳ vọng không chệch.
3. **EFB (Exclusive Feature Bundling)**: Gộp các đặc trưng thưa hiếm khi cùng khác 0 vào chung một cột (histogram binning).
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Cạm bẫy thực tế: Chiến lược Leaf-wise phát triển cây không đối xứng sâu có thể dẫn đến Overfitting trên tập dữ liệu nhỏ! Do đó luôn cần khống chế `max_depth` và `num_leaves` khi dùng LightGBM.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Random Forest & Phương pháp Ensemble**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M43: Cùng tìm hiểu các cải tiến hiệu năng của thư viện LightGBM: VOAI03-M43 kiểm tra chiến lược mọc cây theo lá (Leaf-wise), còn M20 kiểm tra 2 kỹ thuật xử lý dữ liệu đột phá GOSS (lọc mẫu theo gradient) và EFB (gộp đặc trưng loại trừ).

---

### Câu 21 [VOAI02-M21] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi mã hóa biến phân loại (Categorical Features) bằng Target Encoding thông thường trên toàn bộ tập dữ liệu, mô hình thường bị hiện tượng Target Leakage (Rò rỉ nhãn) dẫn đến Overfitting. CatBoost giải quyết triệt để vấn đề này bằng cơ chế nào?

- **A.** Ordered Target Statistics (TS): Sinh hoán vị ngẫu nhiên và chỉ tính thống kê mục tiêu dựa trên các mẫu đứng TRƯỚC
- **B.** Global Mean Target Statistics (GS): Tính giá trị trung bình nhãn trên toàn bộ tập dữ liệu rồi cộng thêm nhiễu Gauss
- **C.** One-Hot Categorical Encoding (OHE): Chuyển đổi mọi biến phân loại thành vector nhị phân thưa bất kể số lượng category
- **D.** Feature Frequency Truncation (FFT): Bỏ qua hoàn toàn các biến phân loại có tần suất xuất hiện dưới ngưỡng trung bình

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Target Encoding:** Thay thế biến phân loại bằng giá trị trung bình của biến mục tiêu trên từng nhóm danh mục.
- **Target Leakage:** Sử dụng nhãn của chính mẫu hiện tại để tính toán giá trị mã hóa khiến mô hình ghi nhớ nhãn và overfitting nặng.
- **Ordered Target Encoding trong CatBoost:** Tính toán mã hóa cho mẫu thứ $i$ chỉ dựa trên các mẫu xuất hiện trước nó theo một thứ tự hoán vị ngẫu nhiên: $\hat{x}_i = \frac{\sum_{j < i} y_j + a \cdot P}{\sum_{j < i} 1 + a}$.

🍼 **Hình dung thực tế cho em bé:**
Nếu tính trung bình nhãn của cả lớp để gán cho từng học sinh, học sinh đó sẽ ' nhìn thấy trước ' đáp án của cả bài thi (Target Leakage). CatBoost giải quyết bằng cách xếp hàng ngẫu nhiên các học sinh: một bạn đứng ở vị trí thứ k chỉ được phép tính trung bình từ những bạn đứng trước nó (từ 1 đến k-1), tuyệt đối không được nhìn những bạn đứng sau. Nhờ vậy không bị lộ đáp án!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ordered Target Statistics trong CatBoost:
Cho một hoán vị ngẫu nhiên $\sigma$ của tập dữ liệu train. Giá trị mã hóa của danh mục $x_{i, k}$ cho mẫu $x_i$ được tính bằng:
$$\hat{x}_{i, k} = \frac{\sum_{j: \sigma(j) < \sigma(i)} \mathbb{I}(x_{j, k} = x_{i, k}) y_j + a \cdot P}{\sum_{j: \sigma(j) < \sigma(i)} \mathbb{I}(x_{j, k} = x_{i, k}) + a}$$
Trong đó $P$ là prior trung bình toàn cục, $a > 0$ là trọng số prior smoothing.
Vì chỉ sử dụng các mẫu $\sigma(j) < \sigma(i)$, mẫu $x_i$ hoàn toàn không nhìn thấy nhãn của chính nó hay các mẫu tương lai $\implies$ Triệt tiêu hoàn toàn Target Leakage.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy phòng thi: Nhiều thí sinh nhầm rằng CatBoost chỉ đơn thuần dùng One-Hot Encoding (B). CatBoost chỉ dùng One-Hot khi số giá trị phân loại nhỏ (mặc định $\le 2$ giá trị), còn với cardinality lớn nó dùng Ordered Target Statistics độc quyền.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.10 Tiền xử lý Đặc trưng & Thao tác NumPy**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M49: Cùng kiểm tra cơ chế chống rò rỉ nhãn (Target Leakage) độc quyền của thuật toán CatBoost: nguyên lý Ordered Target Encoding / Ordered Boosting dựa trên việc bảo toàn thứ tự thời gian giả lập.

---

### Câu 22 [VOAI02-M22] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi áp dụng kỹ thuật sinh mẫu nhân tạo SMOTE (Synthetic Minority Over-sampling Technique) để xử lý dữ liệu mất cân bằng lớp kết hợp với K-Fold Cross-Validation, quy trình nào sau đây là **ĐÚNG ĐẮN VỀ MẶT KỸ THUẬT** để tránh rò rỉ dữ liệu (Data Leakage)?

- **A.** Áp dụng SMOTE lên toàn bộ tập dữ liệu trước khi phân chia K-Fold Cross-Validation để đảm bảo các fold đều cân bằng
- **B.** Áp dụng SMOTE độc lập hai lần: một lần trên tập train fold và một lần trên tập validation fold để làm giàu dữ liệu
- **C.** Chia K-Fold trước; trong mỗi fold, CHỈ áp dụng SMOTE trên tập Train Fold, tuyệt đối KHÔNG áp dụng trên Validation Fold
- **D.** Chỉ áp dụng SMOTE trên tập Validation Fold nhằm mô phỏng phân phối thử nghiệm cân bằng lý tưởng khi đánh giá

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **SMOTE:** Kỹ thuật sinh mẫu nhân tạo cho lớp thiểu số bằng cách nội suy tuyến tính giữa các điểm dữ liệu láng giềng k-NN.
- **Quy tắc vàng Cross-Validation:** Mọi thao tác tiền xử lý, chuẩn hóa, và sinh mẫu SMOTE BẮT BUỘC chỉ được áp dụng trên tập huấn luyện (Train Fold).
- **Data Leakage nguy hiểm:** Nếu áp dụng SMOTE trên toàn bộ dữ liệu trước khi chia K-Fold, các mẫu nhân tạo được tạo ra từ thông tin của tập Validation sẽ rò rỉ vào Train Fold.

🍼 **Hình dung thực tế cho em bé:**
Tập Validation là bài thi thử thực tế ngoài đời. Ngoài đời tỉ lệ bệnh thật vẫn hiếm, bạn không thể ' tự chế thêm bệnh nhân giả ' vào phòng thi được! Hơn nữa, nếu bạn sinh mẫu giả trước khi chia fold, các mẫu giả (được nội suy từ mẫu thật) sẽ rơi vào cả tập train lẫn test, giống như chép đề thi trước vào tài liệu ôn tập $\implies$ Điểm val cao ảo tưởng nhưng test thật thì rớt thảm hại!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nguyên lý bất khả xâm phạm của Cross-Validation:
Validation fold phải mô phỏng chính xác phân phối của Test set trong thực tế (không có mẫu nhân tạo).
Nếu thực hiện SMOTE trước khi chia fold:
$$\tilde{x} = x_i + \lambda (x_{zi} - x_i), \quad \lambda \in [0, 1]$$
Mẫu nhân tạo $\tilde{x}$ nằm trên đoạn thẳng nối giữa hai điểm $x_i$ và $x_{zi}$. Nếu $x_i$ rơi vào train fold còn $\tilde{x}$ rơi vào val fold, thông tin của tập train đã bị rò rỉ trực tiếp vào tập val (Data Leakage) $\implies$ Mô hình đạt F1 99% ảo trên validation nhưng sụp đổ trên test.
Do đó: Phải đưa SMOTE vào bên trong pipeline sau khi đã tách train/val: `imblearn.pipeline. Pipeline([(' smote ', SMOTE()), (' model ', clf)])`.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Lỗi cấm kỵ hàng đầu của dân làm AI: Làm SMOTE trên toàn bộ dataframe trước khi train_test_split. Đây là câu hỏi bẫy xuất hiện trong hầu hết các kỳ phỏng vấn AI và đề thi OLP AI.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.9 Xử lý Mất cân bằng lớp (Imbalanced Data)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M35: VOAI03-M35 kiểm tra nguyên lý thuật toán SMOTE, còn M22 kiểm tra quy trình thực hành chuẩn để ngăn chặn thảm họa rò rỉ dữ liệu (Data Leakage) khi kết hợp SMOTE với Cross-Validation.

---

### Câu 23 [VOAI02-M23] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán phân tích cụm không gian biểu diễn (Representation Space Clustering), nhận định nào sau đây là **CHÍNH XÁC** khi so sánh giữa K-Means và HDBSCAN?

- **A.** Cả hai thuật toán đều bắt buộc người dùng phải xác định trước số cụm K và giả định các cụm có hình cầu lồi đồng nhất
- **B.** HDBSCAN bắt buộc chỉ định trước số cụm K, trong khi K-Means tự động tìm số cụm dựa trên cấu trúc liên thông phân cấp
- **C.** K-Means xử lý tốt các cụm có mật độ biến thiên và hình dạng uốn lượn, trong khi HDBSCAN chỉ hiệu quả với các khối cầu
- **D.** K-Means bắt buộc chỉ định trước số cụm K và giả định cụm hình cầu; HDBSCAN tự tìm số cụm theo mật độ và lọc được điểm nhiễu

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **K-Means:** Thuật toán phân cụm dựa trên khoảng cách tâm, giả định các cụm có dạng hình cầu lồi (spherical) và kích thước tương đương, rất nhạy cảm với nhiễu.
- **HDBSCAN:** Thuật toán phân cụm dựa trên mật độ phân cấp (Hierarchical Density-Based), phát hiện được các cụm có hình dạng hình học phức tạp tùy ý.
- **Tự động xử lý nhiễu:** HDBSCAN tự động đánh dấu các điểm nằm ở vùng mật độ thấp là Outliers/Noise (nhãn -1) mà không ép chúng vào bất kỳ cụm nào.

🍼 **Hình dung thực tế cho em bé:**
K-Means giống như việc vẽ các hình tròn tĩnh: bạn phải đoán trước có bao nhiêu hình tròn (K), và nó chỉ gom được những đám mây tròn vo, nếu gặp hình trăng khuyết hay dải uốn lượn thì K-Means cắt nát bét! Còn HDBSCAN giống như dòng nước tràn theo mật độ: chỗ nào đông đúc thì gom thành một cụm bất kể uốn éo thế nào, chỗ nào vắng vẻ cô lập thì coi là rác/nhiễu (noise) chứ không ép phải thuộc về cụm nào.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **K-Means**: Tối thiểu hóa hàm phương sai nội cụm $W(C) = \sum_{k=1}^K \sum_{x \in C_k} \|x - \mu_k\|^2$. Không gian bị phân hoạch theo sơ đồ Voronoi lồi (convex polyhedra), do đó thất bại hoàn toàn khi các cụm có hình dạng xoắn ốc, trăng khuyết, hoặc mật độ không đều.
2. **HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)**: Dựa trên khoảng cách khả năng tiếp cận lẫn nhau (Mutual Reachability Distance):
$$d_{mreach-k}(a, b) = \max\{core_k(a), core_k(b), d(a, b)\}$$
Xây dựng cây phân cấp bao trùm nhỏ nhất (MST) và cô đọng cây dựa trên độ ổn định của cụm (cluster stability $\sum (\lambda_{death} - \lambda_{birth})$). Không cần chọn $K$, tự động nhận diện outliers có nhãn $-1$.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy thời gian: HDBSCAN tính toán khoảng cách mật độ nên chạy CHẬM hơn K-Means (độ phức tạp $O(N^2)$ hoặc $O(N \log N)$ so với $O(N K D)$ của K-Means). Đáp án C nói HDBSCAN nhanh hơn gấp 100 lần là sai hoàn toàn.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.8 K-Means Clustering & Silhouette Score**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C18: Cùng thuộc chủ đề học không giám sát phân cụm dữ liệu: OLP01-C18 đánh giá cụm K-Means bằng Silhouette Score, còn M23 so sánh hạn chế cụm hình cầu của K-Means với thuật toán phân cụm mật độ HDBSCAN.

---

### Câu 24 [VOAI02-M24] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi xây dựng mô hình dự báo chuỗi thời gian (ví dụ: dự báo giá cổ phiếu hoặc lưu lượng truy cập theo giờ), vì sao việc sử dụng `KFold(shuffle=True)` là **HOÀN TOÀN SAI LẦM**, và phương pháp phân chia nào là chuẩn xác?

- **A.** Shuffle làm thay đổi phân phối nhãn (Class Distribution); Chuẩn xác là nhân đôi các mẫu thuộc lớp thiểu số trước khi chia
- **B.** KFold không hỗ trợ các hàm mất mát (Metric Failure); Chuẩn xác là chuyển đổi bài toán sang học không giám sát
- **C.** Shuffle làm giảm số lượng mẫu trong các fold (Sample Reduction); Chuẩn xác là phân chia tập dữ liệu ngẫu nhiên theo tỷ lệ 80:20
- **D.** Shuffle làm xáo trộn thứ tự thời gian (Look-ahead Bias); Chuẩn xác là dùng TimeSeriesSplit theo cửa sổ cuốn

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Dữ liệu chuỗi thời gian (Time Series):** Các điểm dữ liệu có tương quan tự phát (Autocorrelation) và phụ thuộc chặt chẽ vào trục thời gian xuôi.
- **Sai lầm KFold(shuffle=True):** Việc xáo trộn ngẫu nhiên sẽ lấy dữ liệu tương lai để dự đoán quá khứ (Look-ahead bias), làm điểm số validation cao ảo nhưng mô hình sụp đổ khi deploy.
- **TimeSeriesSplit (Walk-Forward Validation):** Chia dữ liệu theo thứ tự thời gian, tập Train luôn đi trước tập Validation: Train $[0 \dots t]$, Validation $[t+1 \dots t+k]$.

🍼 **Hình dung thực tế cho em bé:**
Bạn không thể dùng tin tức thời sự của ngày mai để ' dự đoán ' xem hôm nay trời có mưa không! Nếu xáo trộn dữ liệu (shuffle=True), các điểm ngày tương lai sẽ rơi vào tập train, mô hình nhìn trước tương lai nên ' đoán ' quá khứ cực chuẩn. Khi đem ra đời thực thì sụp đổ hoàn toàn vì đời thực thời gian chỉ trôi một chiều từ quá khứ đến tương lai! Phải luôn dùng TimeSeriesSplit: train ở quá khứ, test ở tương lai.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Hiện tượng này gọi là **Look-ahead Bias** hoặc **Temporal Data Leakage**.
Nếu chỉ số thời gian $t_1 < t_2 < \dots < t_N$:
- Trong K-Fold xáo trộn: Một mẫu tại thời điểm $t_{100}$ có thể nằm trong train set, trong khi mẫu tại thời điểm $t_{50}$ nằm trong test set. Các đặc trưng trễ (lag features, rolling mean, moving average) tại $t_{50}$ sẽ bị rò rỉ trực tiếp hoặc gián tiếp thông qua trọng số mô hình.
- Giải pháp chuẩn: `TimeSeriesSplit` (Expanding Window hoặc Rolling Window):
$$\text{Fold } k: \quad \text{Train} = \{x_t \mid t \le T_k\}, \quad \text{Val} = \{x_t \mid T_k < t \le T_k + \Delta\}$$
Đảm bảo tại mọi fold: $\max(t_{\text{train}}) < \min(t_{\text{val}})$.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Lỗi cấm kỵ cực kỳ nghiêm trọng trong thi đấu AI và thực tế tài chính: Shuffle chuỗi thời gian. Dù điểm F1 hay R2 đạt 0.99 thì bài thi cũng bị coi là vi phạm nguyên tắc cơ bản của AI.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Overfitting, Underfitting, Bias-Variance Tradeoff & Cross-Validation**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M50: Cùng kiểm tra nguyên lý kiểm chuẩn mô hình chuỗi thời gian: cả hai câu đều khẳng định K-Fold xáo trộn ngẫu nhiên phá vỡ tính liên tục thời gian và gây Data Leakage nghiêm trọng; bắt buộc phải chia theo trục thời gian xuôi (Rolling-window / TimeSeriesSplit).

---

### Câu 25 [VOAI02-M25] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong PyTorch, đoạn mã nào sau đây biểu diễn **ĐÚNG VÀ ĐẦY ĐỦ** thứ tự các bước trong một vòng lặp huấn luyện (Training Step) chuẩn mực?

- **A.** outputs = model(inputs) -> optimizer.step() -> loss = criterion(...) -> optimizer.zero_grad()
- **B.** optimizer.zero_grad() -> outputs = model(inputs) -> loss = criterion(...) -> loss.backward() -> optimizer.step()
- **C.** optimizer.step() -> loss.backward() -> outputs = model(inputs) -> optimizer.zero_grad()
- **D.** loss.backward() -> optimizer.step() -> outputs = model(inputs) -> loss = criterion(...) -> optimizer.zero_grad()

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **`optimizer.zero_grad()`:** Xóa sạch gradient tích lũy trong các tensor trọng số từ bước trước.
- **`loss = criterion(model(inputs), targets)`:** Thực hiện lan truyền xuôi (Forward Pass) và tính giá trị hàm mất mát.
- **`loss.backward()`:** Lan truyền ngược (Backpropagation) tính toán đạo hàm riêng của Loss theo từng tham số.
- **`optimizer.step()`:** Cập nhật giá trị trọng số theo thuật toán tối ưu: $w \leftarrow w - \eta \nabla_w L$.

🍼 **Hình dung thực tế cho em bé:**
Vòng lặp huấn luyện giống như một lượt bắn cung: 1. Xóa bảng điểm cũ (zero_grad), 2. Bắn tên vào bia (forward / model(inputs)), 3. Đo khoảng cách lệch tâm (loss), 4. Phân tích nguyên nhân lệch do tay hay do gió (backward / tính đạo hàm), 5. Điều chỉnh tư thế đứng để lượt sau bắn chuẩn hơn (optimizer.step()). Bỏ quên bước 1 thì điểm tích lũy dồn cục sai bét!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nguyên lý cơ chế tính gradient trong PyTorch:
1. `optimizer.zero_grad()`: PyTorch mặc định **tích lũy gradient** (`param.grad += dL/dw`). Phải xóa sạch gradient của batch trước về 0 trước khi tính gradient mới.
2. `outputs = model(inputs)`: Lan truyền tiến (Forward pass) xây dựng đồ thị tính toán động (Dynamic Computation Graph).
3. `loss = criterion(outputs, targets)`: Tính toán giá trị vô hướng hàm mất mát.
4. `loss.backward()`: Lan truyền ngược (Backpropagation) áp dụng Chain Rule tính toán đạo hàm riêng lưu vào thuộc tính `.grad` của từng tensor có `requires_grad=True`.
5. `optimizer.step()`: Cập nhật trọng số theo thuật toán tối ưu: $w \leftarrow w - \eta \cdot g$.
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Lỗi chết người của người mới học PyTorch: Đặt `optimizer.step()` TRƯỚC `loss.backward()` (D) dẫn đến lỗi vì gradient chưa được tính; hoặc quên `optimizer.zero_grad()` khiến gradient bị cộng dồn vô hạn qua các batch.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.3 Lan truyền xuôi, Lan truyền ngược & Vòng lặp Huấn luyện PyTorch**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B13: Cùng kiểm tra thứ tự 4 thao tác cốt lõi trong vòng lặp huấn luyện PyTorch; giải thích bản chất vì sao phải xóa gradient tích lũy trước khi lan truyền ngược.

---

### Câu 26 [VOAI02-M26] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Nếu khởi tạo tất cả các trọng số $W$ của một mạng nơ-ron sâu bằng giá trị **0 (Zeros)**, hiện tượng gì sẽ xảy ra? Và đối với các mạng sử dụng hàm kích hoạt **ReLU**, phương pháp khởi tạo nào là chuẩn mực khoa học nhất?

- **A.** Các nơ-ron cùng lớp nhận gradient giống hệt nhau (Symmetry Problem); Chuẩn mực cho ReLU là khởi tạo He (Kaiming)
- **B.** Làm bùng nổ gradient ngay bước đầu tiên (Gradient Explosion); Chuẩn mực cho ReLU là khởi tạo ngẫu nhiên đều [-10, 10]
- **C.** Hàm kích hoạt tự động phá vỡ tính đối xứng (Symmetry Breaking); Chuẩn mực cho ReLU là khởi tạo ma trận đơn vị đường chéo
- **D.** Mạng hội tụ nhanh gấp đôi nhưng mất độ chính xác (Accuracy Loss); Chuẩn mực cho ReLU là khởi tạo phân phối Bernoulli

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Symmetry Problem (Vấn đề đối xứng):** Khi khởi tạo toàn bộ trọng số bằng 0, mọi nơ-ron trong cùng một tầng ẩn nhận đầu vào giống nhau và có gradient giống hệt nhau $\implies$ không thể học các đặc trưng phân hóa.
- **Khởi tạo He / Kaiming (He et al., 2015):** Khởi tạo trọng số từ phân phối $\mathcal{N}(0, \frac{2}{n_{in}})$, được chứng minh toán học là tối ưu để duy trì phương sai kích hoạt ổn định qua các tầng sử dụng ReLU.
- **Khởi tạo Xavier / Glorot:** Phù hợp với các hàm kích hoạt đối xứng quanh 0 như Tanh và Sigmoid ($\text{Var} = \frac{2}{n_{in} + n_{out}}$).

🍼 **Hình dung thực tế cho em bé:**
Nếu cho một đội thám tử 10 người xuất phát từ cùng một tọa độ 0 và nhận chung một lệnh, cả 10 người sẽ luôn đi chung một con đường và nhìn thấy những thứ giống hệt nhau (phí phạm 9 người còn lại)! Khởi tạo trọng số bằng 0 làm các nơ-ron bị ' dính chặt ' vào nhau không thể phân hóa. Với hàm ReLU (cắt bỏ một nửa giá trị âm), công thức khởi tạo He (Kaiming) nhân thêm căn bậc hai của 2 để bù đắp năng lượng bị mất mát!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **Vấn đề đối xứng (Symmetry Breaking)**:
Khi $W^{(l)} = 0$, tại lớp $l$: $z^{(l)} = W^{(l)} a^{(l-1)} + b = b$. Mọi nơ-ron trong cùng lớp đều có giá trị kích hoạt giống hệt nhau. Khi lan truyền ngược, gradient $\frac{\partial L}{\partial W_{ij}^{(l)}}$ cũng bằng nhau cho mọi $i, j$. Sau khi cập nhật, toàn bộ trọng số trong lớp vẫn bằng nhau $\implies$ Mạng sâu $N$ nơ-ron suy biến thành một nơ-ron đơn lẻ!
2. **Khởi tạo He (Kaiming)**:
Vì ReLU triệt tiêu một nửa miền giá trị ($x < 0 \implies f(x) = 0$), phương sai của tín hiệu bị giảm đi một nửa: $\text{Var}(f(x)) = \frac{1}{2} \text{Var}(x)$. Để giữ cho phương sai không đổi qua các lớp sâu, Kaiming He đề xuất:
$$\text{Var}(W) = \frac{2}{n_{in}} \implies W \sim \mathcal{N}\left(0, \sqrt{\frac{2}{n_{in}}}\right)$$
(Trong khi Xavier chỉ là $\frac{1}{n_{in}}$ hoặc $\frac{2}{n_{in} + n_{out}}$, chỉ thích hợp cho Tanh/Sigmoid đối xứng qua 0).
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy đề thi: Chọn Xavier cho mạng ReLU. Xavier được thiết kế cho các hàm đối xứng quanh gốc tọa độ (Tanh), dùng Xavier cho ReLU sẽ khiến phương sai tín hiệu giảm dần về 0 khi mạng sâu.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.7 Khởi tạo Trọng số (Weight Initialization)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B14: Cùng kiểm tra chiến lược khởi tạo trọng số mạng sâu: OLP01-B14 chọn phương pháp He Normal/Uniform cho ReLU, còn M26 giải thích thêm nguy cơ phá vỡ tính phân hóa của nơ-ron khi khởi tạo bằng 0.

---

### Câu 27 [VOAI02-M27] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong lớp Batch Normalization (`nn. BatchNorm2d`), sự khác biệt căn bản về mặt toán học giữa pha huấn luyện (`model.train()`) và pha suy luận (`model.eval()`) là gì?

- **A.** Pha train chuẩn hóa bằng mean và var của mini-batch hiện tại; Pha eval sử dụng running_mean và running_var đã tích lũy
- **B.** Pha train cố định các tham số gamma và beta; Pha eval mới cập nhật các tham số tỉ lệ và độ dịch chuyển này
- **C.** Pha train không tính độ lệch chuẩn mà chỉ trừ kỳ vọng; Pha eval nhân đôi toàn bộ trọng số để bù trừ biên độ tín hiệu
- **D.** Pha train chuẩn hóa trên từng mẫu độc lập; Pha eval gộp toàn bộ tập kiểm thử thành một lô duy nhất để tính phân phối

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **BatchNorm pha Train (`model.train()`):** Sử dụng giá trị trung bình $\mu_B$ và phương sai $\sigma_B^2$ được tính toán trực tiếp trên mini-batch hiện tại để chuẩn hóa.
- **Running Statistics:** Trong lúc train, mô hình liên tục cập nhật trung bình trượt: $\mu_{run} = (1-m)\mu_{run} + m \mu_B$.
- **BatchNorm pha Eval (`model.eval()`):** Đóng băng hoàn toàn việc tính toán trên batch; sử dụng cố định các giá trị running_mean và running_var đã tích lũy trong quá trình train.

🍼 **Hình dung thực tế cho em bé:**
Lúc tập luyện (train), thầy giáo đo chiều cao trung bình của riêng nhóm học sinh đang đứng trên sân (mini-batch) để xếp hàng. Nhưng lúc thi đấu thực tế (eval / test), có thể chỉ có đúng 1 học sinh bước vào phòng thi (batch_size=1)! Với 1 người thì làm sao tính được trung bình và độ lệch chuẩn? Do đó, lúc test, mô hình phải dùng ' chiều cao trung bình toàn trường ' (running_mean) đã ghi chép tích lũy từ trước!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **Pha Train**:
Với mini-batch $\mathcal{B} = \{x_1, \dots, x_m\}$:
$$\mu_\mathcal{B} = \frac{1}{m}\sum_{i=1}^m x_i, \quad \sigma_\mathcal{B}^2 = \frac{1}{m}\sum_{i=1}^m (x_i - \mu_\mathcal{B})^2$$
$$\hat{x}_i = \frac{x_i - \mu_\mathcal{B}}{\sqrt{\sigma_\mathcal{B}^2 + \epsilon}}, \quad y_i = \gamma \hat{x}_i + \beta$$
Đồng thời cập nhật trung bình động chạy (exponential moving average):
$$\mu_{running} \leftarrow (1 - m) \mu_{running} + m \cdot \mu_\mathcal{B}$$
$$\sigma^2_{running} \leftarrow (1 - m) \sigma^2_{running} + m \cdot \sigma^2_\mathcal{B}$$
2. **Pha Eval**:
$$\hat{x} = \frac{x - \mu_{running}}{\sqrt{\sigma^2_{running} + \epsilon}}, \quad y = \gamma \hat{x} + \beta$$
Không phụ thuộc vào kích thước của mini-batch kiểm tra.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Lỗi ngớ ngẩn khi deploy: Quên gọi `model.eval()` trước khi dự đoán trên tập test với batch_size = 1. Khi đó PyTorch báo lỗi `ValueError: Expected more than 1 value per channel when training` vì không thể tính variance của 1 mẫu duy nhất!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.8 Chuẩn hóa Tầng (Batch Normalization vs Layer Normalization)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B10: Cùng kiểm tra cơ chế hoạt động của lớp Batch Normalization trong PyTorch: phân biệt sự khác nhau căn bản giữa thống kê batch tức thời lúc train và thống kê tích lũy running stats lúc eval.

---

### Câu 28 [VOAI02-M28] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Vì sao các kiến trúc Transformer và mô hình xử lý chuỗi ngôn ngữ tự nhiên (NLP) hầu như luôn sử dụng **Layer Normalization** thay vì **Batch Normalization**?

- **A.** LayerNorm chuẩn hóa theo chiều đặc trưng từng mẫu độc lập, hoạt động hoàn hảo với câu có độ dài biến thiên và batch nhỏ
- **B.** BatchNorm không thể tính được gradient lan truyền ngược trong không gian rời rạc của các vector nhúng từ vựng
- **C.** LayerNorm loại bỏ hoàn toàn các phép toán nhân ma trận trên GPU, giúp tăng tốc độ suy luận mô hình lên gấp 10 lần
- **D.** LayerNorm tự động chuyển đổi chuỗi văn bản thành ma trận xác suất chuyển trạng thái mà không cần thông qua bộ giải mã

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Batch Normalization (BN):** Chuẩn hóa theo chiều batch, phụ thuộc chặt chẽ vào kích thước batch và giả định các mẫu có chiều dài bằng nhau.
- **Độ dài chuỗi biến thiên trong NLP:** Các câu văn trong batch có độ dài rất khác nhau, sử dụng padding token làm sai lệch nghiêm trọng thống kê trung bình và phương sai của batch.
- **Layer Normalization (LN):** Chuẩn hóa độc lập trên từng mẫu dữ liệu qua toàn bộ các kênh đặc trưng ẩn: $\mu_L = \frac{1}{D} \sum_{i=1}^D x_i$, hoàn toàn không phụ thuộc vào batch size hay các câu khác.

🍼 **Hình dung thực tế cho em bé:**
BatchNorm cắt ngang qua toàn bộ batch (nhìn sang các câu khác). Nhưng trong NLP, câu thì dài 5 chữ, câu thì dài 50 chữ; nếu cắt ngang, những từ cuối câu dài sẽ bị ' ghép đôi ' với các khoảng trống đệm (padding) của câu ngắn, làm thống kê bị hỏng hoàn toàn! LayerNorm giải quyết bằng cách: mỗi câu tự chuẩn hóa riêng cho chính nó theo chiều sâu của từ (hidden dimension), không quan tâm câu khác dài ngắn hay batch to nhỏ ra sao!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Cho tensor đầu vào kích thước $(B, T, D)$ (Batch, Sequence Length, Hidden Dimension):
- **Batch Normalization**: Chuẩn hóa dọc theo chiều Batch $B$ cho từng đặc trưng độc lập. Khi các câu có độ dài khác nhau cần padding, việc tính mean/variance qua batch bị nhiễu nghiêm trọng bởi token padding.
- **Layer Normalization**: Chuẩn hóa ngang qua toàn bộ chiều đặc trưng $D$ cho từng token riêng lẻ tại từng vị trí thời gian $t$ của từng mẫu $i$:
$$\mu_{i, t} = \frac{1}{D} \sum_{j=1}^D x_{i, t, j}, \quad \sigma^2_{i, t} = \frac{1}{D} \sum_{j=1}^D (x_{i, t, j} - \mu_{i, t})^2$$
$$\text{LN}(x_{i, t}) = \frac{x_{i, t} - \mu_{i, t}}{\sqrt{\sigma^2_{i, t} + \epsilon}} \odot \gamma + \beta$$
Phép tính này hoàn toàn độc lập giữa các mẫu và các vị trí $t$, không cần đồng bộ giữa các GPU trong Distributed Training.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy phỏng vấn: Người ta hỏi ' LayerNorm có hoạt động được khi batch_size = 1 không?'. Câu trả lời là CÓ và HOÀN TOÀN BÌNH THƯỜNG, vì LayerNorm chuẩn hóa theo chiều feature của 1 mẫu duy nhất!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.8 Chuẩn hóa Tầng (Batch Normalization vs Layer Normalization)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C21: Cùng phân tích nguyên nhân LayerNorm là chuẩn mực trong NLP: chuẩn hóa độc lập theo từng mẫu trên chiều đặc trưng (feature dimension), hoàn toàn không phụ thuộc vào kích thước batch hay độ dài chuỗi biến thiên.

---

### Câu 29 [VOAI02-M29] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi huấn luyện mạng học sâu nhiều lớp hoặc mô hình RNN chuỗi dài, hiện tượng bùng nổ gradient (Exploding Gradient) thường khiến giá trị hàm mất mát biến thành `NaN` hoặc `Inf`. Giải pháp kỹ thuật phổ biến và hiệu quả nhất để khắc phục trực tiếp hiện tượng này trong PyTorch là gì?

- **A.** Tăng tốc độ học (Learning Rate) lên gấp 10 lần để đẩy các tham số vượt qua vùng thế năng cực tiểu cục bộ
- **B.** Thay thế toàn bộ các hàm kích hoạt phi tuyến bằng hàm Sigmoid để thu hẹp dải giá trị đầu ra của nơ-ron
- **C.** Kẹp gradient (Gradient Clipping theo chuẩn L2: torch.nn.utils.clip_grad_norm_) để giới hạn độ lớn vector gradient
- **D.** Loại bỏ hoàn toàn các lớp kết nối tắt (Skip Connections) nhằm triệt tiêu các luồng gradient cộng dồn không mong muốn

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Exploding Gradient (Bùng nổ gradient):** Tích của các ma trận trọng số trong chuỗi đạo hàm lan truyền ngược quá lớn khiến gradient tăng theo cấp số nhân.
- **Hậu quả:** Trọng số nhận giá trị cực đại vượt quá phạm vi dấu phẩy động 32-bit $\implies$ xuất hiện `NaN` hoặc `Inf`.
- **Gradient Clipping (`torch.nn.utils.clip_grad_norm_`):** Nếu chuẩn $L_2$ của gradient vượt quá ngưỡng $c$, ta co tỷ lệ toàn bộ vector gradient: $g \leftarrow g \cdot \frac{c}{\|g\|_2}$.

🍼 **Hình dung thực tế cho em bé:**
Gradient bùng nổ giống như việc bạn bước một bước chân quá dài (do bước nhảy khổng lồ) khiến bạn văng ra khỏi vực thẳm và rơi vào vùng vô cực (NaN/Inf). Kỹ thuật Gradient Clipping giống như chiếc dây đai an toàn: nếu bước nhảy vượt quá độ dài tối đa cho phép (ví dụ max_norm = 1.0), nó sẽ co ngắn bước chân lại theo đúng hướng đó để bạn không bị ngã!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi đạo hàm của chuỗi các ma trận trọng số $\prod_{l=1}^L W_l$ có trị riêng lớn hơn 1, chuẩn gradient $\|g\|_2$ tăng theo hàm mũ và bùng nổ.
**Gradient Clipping theo chuẩn L2 (norm clipping)**:
Nếu $\|g\|_2 > \text{max\_norm}$, gradient được điều chỉnh lại theo tỉ lệ:
$$g \leftarrow g \cdot \frac{\text{max\_norm}}{\|g\|_2}$$
Phép biến đổi này bảo toàn chính xác **hướng di chuyển** của gradient trong không gian tham số (giữ nguyên vector đơn vị $\frac{g}{\|g\|}$), chỉ khống chế độ dài bước nhảy tối đa là $\text{max\_norm}$.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy thứ tự lệnh: Gọi `clip_grad_norm_` PHẢI ĐƯỢC THỰC HIỆN SAU `loss.backward()` (khi đã có gradient) và TRƯỚC `optimizer.step()` (trước khi cập nhật trọng số).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.10 Gradient Vanishing & Exploding, Early Stopping**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C22: Cùng kiểm tra vấn đề bất ổn định gradient trong mạng sâu và RNN chuỗi dài: M29 tập trung vào giải pháp cắt tỉa gradient (Gradient Clipping) để chặn bùng nổ gradient, bổ trợ cho §2.10

---

### Câu 30 [VOAI02-M30] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong PyTorch, lớp `nn. CrossEntropyLoss()` đã tự động tích hợp sẵn phép biến đổi toán học nào bên trong, và thí sinh cần đưa đầu vào là gì?

- **A.** Tích hợp sẵn hàm kích hoạt ReLU; Đầu vào của hàm mất mát bắt buộc phải là các số nguyên dương không âm
- **B.** Không tích hợp hàm kích hoạt nào; Thí sinh bắt buộc phải gọi torch.softmax() ở tầng cuối cùng trước khi tính loss
- **C.** Tích hợp sẵn LogSoftmax và NLLLoss; Đầu vào của mô hình phải là Logits thô chưa qua hàm kích hoạt Softmax
- **D.** Tích hợp sẵn hàm kích hoạt Sigmoid; Đầu vào của mô hình bắt buộc phải là xác suất phân phối trong khoảng [0, 1]

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **`nn. CrossEntropyLoss()`:** Trong PyTorch, lớp này tích hợp bên trong cả hàm `nn. LogSoftmax()` và `nn. NLLLoss()` (Negative Log Likelihood).
- **Đầu vào bắt buộc (Input):** Tensor logit thô chưa qua kích hoạt Softmax, kích thước $(N, C)$ với $C$ là số lớp.
- **Ổn định số học (Log-Sum-Exp Trick):** Việc gộp Log và Softmax giúp triệt tiêu số mũ cực lớn $e^{z_i}$, ngăn chặn hoàn toàn hiện tượng tràn số (Overflow/Underflow).

🍼 **Hình dung thực tế cho em bé:**
nn. CrossEntropyLoss của PyTorch giống như một combo trọn gói gồm: Bếp nấu LogSoftmax + Bàn ăn NLLLoss. Nếu ở lớp cuối cùng bạn lại tự ý cho đầu ra chạy qua hàm Softmax một lần nữa, nghĩa là bạn bắt nó ăn hai lần bánh! Điều này khiến gradient bị teo nhỏ và mô hình học cực kỳ chậm hoặc sai lệch. Hãy luôn để đầu ra là Logits thô tự do!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 `nn. CrossEntropyLoss` tính toán theo công thức Log-Sum-Exp ổn định số học:
$$\text{loss}(x, y) = -\ln\left(\frac{\exp(x_y)}{\sum_j \exp(x_j)}\right) = -x_y + \ln\left(\sum_j \exp(x_j)\right)$$
Nếu người lập trình đưa qua `Softmax` trước:
$$p = \text{Softmax}(x) \in (0, 1)$$
Sau đó truyền $p$ vào `CrossEntropyLoss`, hàm loss sẽ tiếp tục lấy Softmax lần thứ hai trên $p$:
$$\text{loss} = -\ln(\text{Softmax}(p)_y)$$
Vì $p$ nằm trong khoảng hẹp $(0, 1)$, $\exp(p_j) \approx 1 + p_j$, phân phối bị làm phẳng nhân tạo, gradient suy biến nghiêm trọng.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Đây là lỗi sai phổ biến nhất trong bài thi thực hành Deep Learning: Thêm `nn. Softmax(dim=1)` vào lớp cuối của mô hình PyTorch khi dùng `nn. CrossEntropyLoss()`. Hãy khắc cốt ghi tâm: CẤM DÙNG SOFTMAX TRƯỚC CROSSENTROPYLOSS TRONG PYTORCH!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát (Loss Functions)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B11: Cùng kiểm tra cơ chế kỹ thuật của `nn. CrossEntropyLoss()` trong PyTorch: tích hợp LogSoftmax và Log-Sum-Exp để tối ưu độ ổn định số học, yêu cầu thí sinh đưa trực tiếp raw logits chưa qua Softmax.

---

### Câu 31 [VOAI02-M31] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Vì sao trong bài toán phân loại nhị phân hoặc phân loại đa nhãn (Multi-label), PyTorch khuyến nghị mạnh mẽ sử dụng `nn. BCEWithLogitsLoss()` thay vì ghép nối thủ công `nn. Sigmoid()` với `nn. BCELoss()`?

- **A.** Vì BCELoss thuần túy không hỗ trợ tính toán lan truyền ngược tự động cho các tầng nơ-ron kết nối đầy đủ
- **B.** Vì BCEWithLogitsLoss áp dụng mẹo Log-Sum-Exp giúp ổn định số học, tránh hiện tượng tràn số float khi logit quá lớn
- **C.** Vì BCEWithLogitsLoss tính toán nhanh gấp 10 lần trên GPU nhờ loại bỏ hoàn toàn các phép tính hàm mũ tự nhiên
- **D.** Vì BCEWithLogitsLoss tự động cân bằng tỷ lệ mẫu giữa các lớp bằng cách tự sinh trọng số nghịch đảo tần suất

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **`nn. BCELoss` thủ công:** Đòi hỏi đưa đầu vào qua `torch.sigmoid(x)`, sau đó tính $-y \ln(p) - (1-y)\ln(1-p)$. Khi $p \to 0$ hoặc $p \to 1$, hàm $\ln(0)$ gây lỗi `NaN`.
- **`nn. BCEWithLogitsLoss`:** Nhận logit thô $z$ và tính trực tiếp qua công thức toán học hợp nhất: $\max(z, 0) - z \cdot y + \ln(1 + e^{-|z|})$.
- **Log-Sum-Exp Trick:** Đảm bảo số mũ luôn âm ($-|z| \le 0$), giá trị $e^{-|z|} \in (0, 1]$, triệt tiêu hoàn toàn nguy cơ tràn số.

🍼 **Hình dung thực tế cho em bé:**
Khi x = -100, máy tính tính Sigmoid(x) = 1 / (1 + exp(100)) = 0.0 (tràn số dưới). Sau đó đem số 0.0 đó nhét vào hàm log(p) thì log(0) = -Vô Cùng (NaN / sập chương trình)! BCEWithLogitsLoss khôn khéo biến đổi công thức toán học gộp cả hai bước lại, triệt tiêu phép chia nguy hiểm bằng Log-Sum-Exp, nên dù x = -100 hay x = +100 máy vẫn tính ra số cực kỳ êm ái!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Hàm Binary Cross-Entropy với $p = \sigma(x) = \frac{1}{1 + e^{-x}}$:
$$\mathcal{L} = -y \ln(\sigma(x)) - (1 - y) \ln(1 - \sigma(x))$$
Biến đổi đại số:
$$\ln(\sigma(x)) = \ln\left(\frac{1}{1 + e^{-x}}\right) = -\ln(1 + e^{-x})$$
$$\ln(1 - \sigma(x)) = \ln\left(\frac{e^{-x}}{1 + e^{-x}}\right) = -x - \ln(1 + e^{-x})$$
Thay vào $\mathcal{L}$:
$$\mathcal{L} = y \ln(1 + e^{-x}) + (1 - y) [x + \ln(1 + e^{-x})] = (1 - y) x + \ln(1 + e^{-x})$$
Để ổn định khi $x < 0$, viết lại dạng tổng quát:
$$\mathcal{L} = \max(x, 0) - x \cdot y + \ln(1 + e^{-|x|})$$
Nhờ số hạng $e^{-|x|}$ với $|x| \ge 0$, số mũ luôn $\le 0 \implies e^{-|x|} \in (0, 1]$, triệt tiêu hoàn toàn nguy cơ tràn số trên `overflow` $\exp(+\infty)$ và tràn số dưới `underflow` $\ln(0)$.
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy lặp lại: Không bao giờ dùng `nn. Sigmoid()` rồi truyền vào `nn. BCEWithLogitsLoss()`. Đầu vào của `nn. BCEWithLogitsLoss` phải là logit thô!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát (Loss Functions)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B12: Cùng làm rõ lý do ổn định số học (numerical stability) của `nn. BCEWithLogitsLoss()` thông qua thủ thuật Log-Sum-Exp trong tính toán dấu phẩy động.

---

### Câu 32 [VOAI02-M32] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Nghiên cứu của Loshchilov & Hutter (ICLR 2019) đã chỉ ra rằng việc cài đặt Weight Decay thông thường (thêm $\lambda w$ vào gradient) trong thuật toán Adam truyền thống là sai lệch so với bản chất của $L_2$ Regularization. Thuật toán **AdamW** giải quyết vấn đề này bằng cách nào?

- **A.** Tách rời Weight Decay khỏi bước cập nhật theo moment bậc hai, áp dụng trực tiếp suy giảm trọng số $w = w - \eta \lambda w$
- **B.** Tăng hệ số suy giảm moment bậc hai $\beta_2$ lên đúng 1.0 nhằm triệt tiêu hoàn toàn sự biến động phương sai của gradient
- **C.** Loại bỏ hoàn toàn bước ước lượng moment bậc một và chỉ cập nhật trọng số dựa trên thông tin độ lớn ma trận Hessian
- **D.** Chuyển sang sử dụng chuẩn L1 cho toàn bộ vector tham số nhằm ép các trọng số không quan trọng về đúng bằng 0

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Weight Decay trong Adam thông thường:** Thêm $\lambda w$ trực tiếp vào gradient trước khi tính moment bậc một và bậc hai: $g_t \leftarrow g_t + \lambda w$. Điều này khiến các trọng số có gradient lớn bị phạt nhẹ hơn và ngược lại.
- **AdamW (Decoupled Weight Decay):** Tách hoàn toàn việc suy giảm trọng số ra khỏi cập nhật moment thích nghi: $w_{t+1} = w_t - \eta_t \frac{m_t}{\sqrt{v_t}+\epsilon} - \eta_t \lambda w_t$.
- **Khôi phục bản chất L2 Regularization:** Giúp mô hình Transformer tổng quát hóa vượt trội trên tập dữ liệu kiểm thử.

🍼 **Hình dung thực tế cho em bé:**
Trong Adam cũ, khi bạn phạt trọng số (weight decay), số hạng phạt bị chia cho căn bậc hai của moment bậc hai (tốc độ biến động). Trọng số nào biến động mạnh thì bị phạt nhẹ, trọng số nào ít biến động lại bị phạt nặng! Điều này làm hỏng ý nghĩa của việc phạt trọng số. AdamW sửa lại bằng cách: tách việc phạt trọng số ra riêng, trừ thẳng vào trọng số mỗi bước như học sinh bị trừ điểm cố định, không để moment can thiệp vào nữa!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **L2 Regularization trong Adam gốc** (Ghép cặp - Coupled):
Gradient được sửa thành: $\tilde{g}_t = g_t + \lambda w_t$.
Quy tắc cập nhật tham số:
$$w_{t+1} = w_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} (\hat{m}_t + \lambda w_t)$$
Số hạng suy giảm trọng số bị chia cho $\sqrt{\hat{v}_t}$. Các tham số có gradient lịch sử lớn ($\hat{v}_t$ lớn) sẽ chịu mức độ suy giảm trọng số NHỎ HƠN so với các tham số có gradient nhỏ!
2. **Decoupled Weight Decay trong AdamW**:
Số hạng suy giảm trọng số được áp dụng trực tiếp, độc lập với gradient update:
$$w_{t+1} = w_t - \eta \lambda w_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$
Điều này khôi phục đúng bản chất hình học của suy giảm trọng số trên mọi tham số.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy thực hành: Khi huấn luyện các mô hình Transformer hiện đại (như BERT, ViT, GPT, LLaMA), nếu dùng `torch.optim. Adam` với `weight_decay > 0`, mô hình học kém hơn rõ rệt so với `torch.optim. AdamW`. Mặc định của các framework SOTA luôn là AdamW.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.5 Thuật toán tối ưu hóa (Optimizers)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C11: OLP01-C11 phân tích sức mạnh của Adam, còn M32 đi sâu vào công trình đột phá AdamW (Loshchilov & Hutter 2019) tách biệt cơ chế Weight Decay để khôi phục đúng bản chất điều chuẩn L2 cho các bộ tối ưu thích nghi.

---

### Câu 33 [VOAI02-M33] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật **Learning Rate Warmup** (tăng dần tốc độ học từ 0 lên giá trị cực đại trong một số bước đầu tiên) trước khi áp dụng Cosine Annealing có vai trò cốt lõi là gì?

- **A.** Tăng dần kích thước mini-batch theo từng bước tối ưu để khai thác tối đa băng thông bộ nhớ của phần cứng GPU
- **B.** Tự động tải thêm các mẫu dữ liệu tăng cường từ bộ nhớ đệm nhằm mở rộng không gian khám phá tham số ban đầu
- **C.** Làm chậm tốc độ lan truyền thuận để giảm tải nhiệt độ hoạt động của các bộ vi xử lý đồ họa trong giai đoạn đầu
- **D.** Tránh việc các gradient ban đầu rất lớn và bất ổn định phá hỏng biểu diễn sơ khai và làm chệch hướng tối ưu hóa

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Learning Rate Warmup:** Tăng dần tốc độ học từ 0 lên giá trị tối đa trong $N_{warmup}$ bước đầu tiên.
- **Bản chất vấn đề:** Ở các bước khởi đầu, moment bậc hai $v_t$ của Adam chưa tích lũy đủ thông tin thống kê chính xác, learning rate lớn sẽ làm mô hình cập nhật những bước nhảy hỗn loạn phá hủy trọng số ban đầu.
- **Cosine Annealing:** Sau pha Warmup, learning rate giảm dần theo đường cong cosin về tiệm cận 0 để hội tụ mượt mà vào cực tiểu chất lượng cao.

🍼 **Hình dung thực tế cho em bé:**
Lúc mới bắt đầu tập luyện, các trọng số còn đang bỡ ngỡ và ngẫu nhiên hoàn toàn. Nếu lập tức đạp hết chân ga (learning rate cao), mô hình sẽ lao vút vào bụi rậm hoặc nổ tung gradient! Warmup giống như chạy khởi động xe: lăn bánh từ từ nhẹ nhàng cho các bộ phận ăn khớp ổn định, sau đó mới tăng tốc tối đa rồi hạ dần tốc độ (Cosine Annealing) về đích an toàn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tại các bước đầu tiên $t \le T_{warmup}$:
$$\eta_t = \eta_{max} \cdot \frac{t}{T_{warmup}}$$
Sau đó áp dụng lịch trình suy giảm Cosine (Cosine Annealing) từ $t = T_{warmup}$ đến $T_{total}$:
$$\eta_t = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min}) \left(1 + \cos\left(\pi \frac{t - T_{warmup}}{T_{total} - T_{warmup}}\right)\right)$$
Lợi ích toán học: Trong giai đoạn đầu, các ước lượng moment bậc 1 và bậc 2 trong Adam chưa ổn định (chưa đủ mẫu). Warmup giữ cho bước cập nhật nhỏ để các vector thống kê hội tụ về vùng kỳ vọng tin cậy.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy trực giác: Nghĩ rằng tốc độ học ban đầu phải lớn nhất để đi nhanh nhất. Thực tế trong các mô hình lớn (Transformer, ResNet), không có Warmup mô hình thường bị kẹt ngay ở các cực tiểu địa phương tồi hoặc phân kỳ (diverge).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.6 Learning Rate Scheduling & Warmup**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C12: Cùng phân tích chiến lược lập lịch tốc độ học hiện đại: OLP01-C12 kiểm tra dạng đường cong Cosine Annealing with Warmup, còn M33 giải thích lý do toán học vì sao giai đoạn Warmup ban đầu là tối quan trọng để giữ mô hình không bị chệch hướng khi gradient sơ khai còn nhiễu.

---

### Câu 34 [VOAI02-M34] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong hầu hết các thư viện Deep Learning hiện đại (bao gồm PyTorch), kỹ thuật **Inverted Dropout** (với tỉ lệ drop $p$) được thực hiện như thế nào để đảm bảo tính nhất quán giữa pha huấn luyện và pha suy luận?

- **A.** Trong cả pha train và eval đều ngẫu nhiên tắt nơ-ron với tỉ lệ p nhằm duy trì tính ngẫu nhiên nhất quán của mạng
- **B.** Tắt ngẫu nhiên một nửa số biến trạng thái của optimizer trong mỗi bước cập nhật để giảm phương sai ước lượng
- **C.** Pha train giữ nguyên nơ-ron còn lại; Pha eval nhân toàn bộ trọng số với p để thu hẹp kỳ vọng tổng kích hoạt
- **D.** Pha train nhân nơ-ron còn lại với $\frac{1}{1 - p}$; Pha eval giữ nguyên đầu ra mà không cần thêm phép co giãn nào

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Inverted Dropout:** Trong pha Train, mỗi nơ-ron bị tắt với xác suất $p$; các nơ-ron còn lại được nhân tỷ lệ với hệ số $\frac{1}{1-p}$.
- **Bảo toàn kỳ vọng năng lượng:** $\mathbb{E}[\tilde{x}] = (1-p) \cdot \frac{x}{1-p} + p \cdot 0 = x$, kỳ vọng kích hoạt lúc train bằng đúng kỳ vọng lúc test.
- **Lợi ích thực tế:** Trong pha suy luận (`model.eval()`), mô hình chỉ việc giữ nguyên trọng số và chạy thẳng mà không cần bất kỳ phép toán co tỷ lệ nào.

🍼 **Hình dung thực tế cho em bé:**
Dropout truyền thống: lúc tập luyện bạn cất đi 50% học sinh (p=0.5), lúc thi bạn gọi tất cả đi thi nhưng phải chia đôi điểm của cả đội để kỳ vọng bằng nhau. Inverted Dropout thông minh hơn: ngay lúc tập luyện, bạn nhân đôi sức mạnh cho những bạn còn lại (nhân với 1/(1-p) = 2), thế là lúc đi thi thật bạn chỉ việc để nguyên cả đội thi đấu mà không cần chỉnh sửa bất kỳ điểm số nào!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Kỳ vọng của đầu ra qua lớp Dropout với xác suất giữ lại $q = 1 - p$:
1. **Standard Dropout (Cổ điển)**:
- Train: $y = m \odot x$, trong đó $m \sim \text{Bernoulli}(1 - p)$. Kỳ vọng $\mathbb{E}[y] = (1 - p) x$.
- Test: $y = (1 - p) x$ (phải nhân thêm $1 - p$ tại thời điểm suy luận).
2. **Inverted Dropout (Hiện đại trong PyTorch)**:
- Train: $y = \frac{1}{1 - p} (m \odot x)$. Kỳ vọng:
$$\mathbb{E}[y] = \frac{1}{1 - p} \mathbb{E}[m] x = \frac{1}{1 - p} (1 - p) x = x$$
- Test: $y = x$ (Identity mapping, không cần bất kỳ phép tính nào lúc test, tăng tốc độ suy luận).
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy câu chữ: Nhiều thí sinh nhầm rằng hệ số co giãn lúc train là $\frac{1}{p}$. Công thức đúng phải là chia cho xác suất giữ lại: $\frac{1}{1 - p}$. Ví dụ $p = 0.2$ thì chia cho $0.8$ (nhân $1.25$).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.9 Dropout & Tránh Overfitting**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B10: Làm rõ kỹ thuật Inverted Dropout trong PyTorch: nhân hệ số tỷ lệ $\frac{1}{1-p}$ ngay lúc huấn luyện để giữ nguyên kỳ vọng kích hoạt, giúp pha suy luận (model.eval()) diễn ra hoàn toàn tự nhiên không cần scaling.

---

### Câu 35 [VOAI02-M35] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Xét bài toán tối ưu hóa có điều kiện: $\min_w L(w)$ với ràng buộc $\|w\|_1 \le C$ (L1) hoặc $\|w\|_2^2 \le C$ (L2). Về mặt hình học, vì sao điều chuẩn L1 (Lasso) có khả năng triệt tiêu chính xác nhiều trọng số về đúng bằng 0 (tạo ra nghiệm thưa - Sparsity / Feature Selection), trong khi L2 (Ridge) chỉ co nhỏ trọng số chứ không đưa về 0?

- **A.** Quả cầu chuẩn L1 có các đỉnh nhọn nằm ngay trên các trục tọa độ nên đường elip mất mát dễ tiếp xúc tại các đỉnh này; L2 là mặt cầu trơn
- **B.** Hàm chuẩn L1 sử dụng toán tử mũ phân rã nhanh trong khi chuẩn L2 sử dụng toán tử logarit có đạo hàm tiệm cận hằng số
- **C.** Chuẩn L2 chỉ áp dụng được cho dữ liệu một chiều còn chuẩn L1 có thể mở rộng tự do cho các tensor đa chiều bất kỳ
- **D.** Hàm mục tiêu với ràng buộc L1 luôn có nghiệm giải tích dạng đóng trong khi bài toán L2 bắt buộc phải giải bằng số trị

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **L1 Regularization (Lasso):** Vùng ràng buộc có dạng hình khối thoi nhiều góc nhọn (cross-polytope / diamond shape) nằm chính xác trên các trục tọa độ.
- **Nghiệm thưa (Sparsity):** Các đường đồng mức của hàm mất mát có xu hướng tiếp xúc với góc nhọn của hình thoi trước tiên, khiến nhiều tọa độ trọng số bị triệt tiêu về đúng bằng 0.
- **L2 Regularization (Ridge):** Vùng ràng buộc là hình cầu trơn (hypersphere) không có góc nhọn $\implies$ điểm tiếp xúc hiếm khi nằm trên trục tọa độ, trọng số chỉ bị co nhỏ về gần 0.

🍼 **Hình dung thực tế cho em bé:**
Hình dung hình bao L1 là một viên kim cương hình thoi sắc nhọn với các đỉnh nhọn đâm thẳng vào trục tung và trục hoành. Khi một quả bóng elip (hàm mất mát) lăn tới va chạm với viên kim cương, điểm chạm đầu tiên gần như luôn luôn là các mũi nhọn trên trục tọa độ! Tại đỉnh trục tọa độ, các tọa độ còn lại bằng đúng 0 (Feature Selection). Còn hình bao L2 là một quả cầu trơn láng, quả bóng elip chạm vào bất kỳ điểm nào trên mặt cầu nên các tọa độ chỉ nhỏ đi chứ hầu như không bao giờ bằng đúng 0!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. Vùng chấp nhận của chuẩn $L_1$: $\{w \in \mathbb{R}^D \mid \sum_{i=1}^D |w_i| \le C\}$ là một khối đa diện (Cross-polytope / Diamond). Các đỉnh của khối đa diện này nằm chính xác tại các trục tọa độ $(\pm C, 0, \dots, 0)$. Tại các đỉnh này, gradient của hàm chuẩn $L_1$ không khả vi (tồn tại subgradient trong khoảng $[-1, 1]$), tạo thành điểm neo cho điều kiện KKT (Karush-Kuhn-Tucker) khiến nghiệm tối ưu có nhiều thành phần $w_i^* = 0$.
2. Vùng chấp nhận của chuẩn $L_2$: $\{w \in \mathbb{R}^D \mid \sum_{i=1}^D w_i^2 \le C\}$ là một hình cầu mịn (Euclidean Ball). Pháp vector tại mọi điểm tiếp xúc là liên tục, do đó xác suất tiếp xúc chính xác tại điểm giao với trục tọa độ bằng 0 trong không gian liên tục.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy đề thi: Chọn các phương án giải thích sai về hàm mũ/log hoặc nhầm lẫn L1/L2 với tiên nghiệm xác suất Laplace/Gauss khi đề bài đang hỏi căn cứ hình học (geometry of norm balls). Nhớ từ khóa hình học: ' Góc nhọn trên trục tọa độ ' (Corners / Vertices on axes).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§1.6 Regularization L1 (Lasso) vs L2 (Ridge) vs ElasticNet**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C09: Cùng đối chiếu L1 vs L2: OLP01-C09 nêu kết luận ứng dụng lựa chọn đặc trưng của L1, còn M35 giải thích trực quan hình học dựa trên đường đồng mức (contour lines) và hình học lồi của siêu mặt cầu $L_1$ và $L_2$.

---

### Câu 36 [VOAI02-M36] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi triển khai cơ chế Dừng Sớm (Early Stopping) trong quá trình huấn luyện mạng nơ-ron sâu, nhận định nào sau đây là **CHÍNH XÁC NHẤT** về cách thức hoạt động của tham số `patience` và việc lưu mô hình (Model Checkpointing)?

- **A.** Dừng huấn luyện ngay tại epoch đầu tiên mà training loss tăng lên so với epoch trước đó để tránh lãng phí tài nguyên
- **B.** Lưu trọng số tại epoch cuối cùng khi vòng lặp kết thúc vì epoch này đã được học qua số lượng mẫu dữ liệu lớn nhất
- **C.** Dừng khi validation loss không cải thiện qua ' patience ' epoch; lưu checkpoint tại epoch có validation metric tốt nhất
- **D.** Early Stopping chỉ áp dụng được cho hàm mất mát MSE trong bài toán hồi quy chứ không áp dụng được cho Cross-Entropy

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Patience (Độ kiên nhẫn):** Số epoch liên tiếp mà độ đo theo dõi trên tập validation (thường là Validation Loss) không cải thiện trước khi quyết định dừng huấn luyện.
- **Model Checkpointing:** Luôn lưu lại bộ trọng số tại epoch có Validation Loss thấp nhất (Best Checkpoint).
- **Ngăn chặn Overfitting:** Tránh dừng quá sớm khi gặp biến động ngẫu nhiên cục bộ, đồng thời đảm bảo không lấy trọng số ở epoch cuối cùng khi mô hình đã bắt đầu thoái hóa.

🍼 **Hình dung thực tế cho em bé:**
Giống như đi câu cá: bạn kiên nhẫn đợi thêm 5 phút (patience = 5) xem có con cá nào to hơn không. Nếu sau 5 phút không có cá to hơn, bạn dừng câu. Khi đem cá về khoe (nộp bài), bạn phải mang con cá to nhất bạn câu được từ trước (Best Checkpoint), chứ ai lại mang con cá bé xíu câu được ở phút cuối cùng lúc bạn đã nản chí!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thuật toán Early Stopping:
- Khởi tạo `best_val_loss = +inf`, `patience_counter = 0`.
- Tại mỗi epoch $e$:
  - Nếu $val\_loss_e < best\_val\_loss - \delta$:
    - `best_val_loss = val_loss_e`
    - `patience_counter = 0`
    - Lưu trọng số tốt nhất: `torch.save(model.state_dict(), ' best_model.pt ')`
  - Ngược lại:
    - `patience_counter += 1`
    - Nếu `patience_counter >= patience`: Dừng vòng lặp huấn luyện (`break`).
- Kết thúc: Nạp lại trọng số tốt nhất: `model.load_state_dict(torch.load(' best_model.pt '))`.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Lỗi ngớ ngẩn trong thi đấu: Thí sinh bật Early Stopping dừng ở epoch 45 (do 10 epoch từ 35-45 không cải thiện). Nhưng sau đó thí sinh lại lấy luôn `model` hiện tại ở epoch 45 để nộp bài! Mô hình ở epoch 45 đã bị Overfit nặng nề so với epoch 35.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§2.10 Gradient Vanishing & Exploding, Early Stopping**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M40: Cùng kiểm tra cơ chế Early Stopping: VOAI03-M40 xác định tín hiệu dừng dựa trên Validation Loss, còn M36 chi tiết hóa vai trò của tham số `patience` và nguyên tắc Model Checkpointing lưu lại trọng số tối ưu nhất thay vì trọng số của epoch cuối cùng.

---

### Câu 37 [VOAI02-M37] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho ảnh đầu vào kích thước vuông $W_{in} = 224$. Áp dụng lớp tích chập Conv2D với kích thước kernel $K = 7$, padding $P = 3$, và stride $S = 2$. Kích thước cạnh đầu ra $W_{out}$ bằng bao nhiêu?

- **A.** 109
- **B.** 111
- **C.** 114
- **D.** 112

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Công thức kích thước đầu ra Conv2D:** $W_{out} = \left\lfloor \frac{W_{in} - K + 2P}{S} \right\rfloor + 1$.
- **Các tham số:** $W_{in}$ là kích thước đầu vào, $K$ là kích thước kernel, $P$ là padding, $S$ là stride.
- **Tính toán thực tế:** Đầu vào $224 \times 224$, $K=7, P=3, S=2$: $W_{out} = \left\lfloor \frac{224 - 7 + 2(3)}{2} \right\rfloor + 1 = \left\lfloor \frac{223}{2} \right\rfloor + 1 = 111 + 1 = 112$.

🍼 **Hình dung thực tế cho em bé:**
Công thức tính kích thước ảnh sau khi quét kính lúp tích chập là: lấy chiều rộng ảnh ban đầu, cộng thêm phần viền đệm ở hai bên (2 × padding), trừ đi bề rộng của kính lúp (kernel), rồi chia cho bước nhảy (stride), cuối cùng cộng thêm 1. Ở đây: (224 + 6 - 7) / 2 + 1 = 223 / 2 + 1 = 111.5 làm tròn xuống thành 111 + 1 = 112!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng công thức tính kích thước không gian chuẩn của lớp tích chập:
$$W_{out} = \left\lfloor \frac{W_{in} - K + 2P}{S} \right\rfloor + 1$$
Thay số cụ thể:
- $W_{in} = 224$
- $K = 7$
- $P = 3 \implies 2P = 6$
- $S = 2$

Tính toán từng bước:
$$W_{in} - K + 2P = 224 - 7 + 6 = 223$$
$$\frac{223}{2} = 111.5 \implies \lfloor 111.5 \rfloor = 111$$
$$W_{out} = 111 + 1 = 112$$
(Đây chính xác là kích thước của lớp Conv1 đầu tiên trong kiến trúc kinh điển ResNet-50 / ResNet-18).
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hay gặp: Quên nhân đôi padding $2P$ (chỉ cộng $P=3$ thay vì $2P=6$ dẫn đến tính ra 110); hoặc quên cộng 1 ở cuối công thức.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M16: VOAI03-M16 đưa ra công thức tổng quát $\lfloor\frac{W - K + 2P}{S}\rfloor + 1$, còn M37 là bài toán áp dụng số thực tế cho tầng tích chập đầu tiên kinh điển của ResNet ($224 \to 112$).

---

### Câu 38 [VOAI02-M38] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong thiết kế mạng VGG và ResNet, vì sao người ta luôn ưu tiên xếp chồng hai lớp tích chập kích thước $3 \times 3$ liên tiếp (stride = 1) thay vì sử dụng một lớp tích chập duy nhất kích thước $5 \times 5$?

- **A.** Hai lớp 3x3 có Receptive Field lớn gấp đôi (bằng 10x10) so với việc chỉ sử dụng một lớp tích chập duy nhất kích thước 5x5
- **B.** Lớp tích chập 5x5 không thể tính toán được trên phần cứng GPU do kích thước kernel không chia hết cho lũy thừa của 2
- **C.** Hai lớp 3x3 làm giảm độ phân giải không gian của ảnh nhanh hơn, giúp tiết kiệm bộ nhớ đệm ma trận ở các tầng sâu
- **D.** Cùng đạt Receptive Field 5x5 nhưng hai lớp 3x3 tiết kiệm ~28% tham số và tăng thêm lần kích hoạt phi tuyến tính ReLU

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Receptive Field (Trường thụ cảm):** Hai lớp Conv $3 \times 3$ xếp chồng có receptive field tương đương một lớp $5 \times 5$: $RF = 3 + (3-1) = 5$.
- **Tiết kiệm tham số:** Hai lớp $3 \times 3$ tốn $2 \times (3^2 \cdot C^2) = 18 C^2$ tham số, trong khi một lớp $5 \times 5$ tốn $5^2 \cdot C^2 = 25 C^2$ tham số (giảm $\approx 28\%$).
- **Tăng tính phi tuyến:** Giữa hai lớp $3 \times 3$ có thêm một hàm kích hoạt phi tuyến (như ReLU), giúp mạng học được các hàm phức tạp hơn.

🍼 **Hình dung thực tế cho em bé:**
Nhìn qua một ống nhòm to 5x5 tương đương với việc nhìn qua hai ống nhòm nhỏ 3x3 xếp chồng lên nhau. Cả hai cách đều nhìn thấy vùng ảnh rộng 5x5 như nhau. Nhưng hai ống 3x3 chỉ tốn 3² + 3² = 18 viên gạch (tham số), trong khi ống 5x5 tốn tận 5² = 25 viên gạch! Dùng hai lớp 3x3 vừa tiết kiệm 28% bộ nhớ, lại vừa có thêm 2 lần kích hoạt ReLU giúp não AI thông minh hơn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **Vùng đón nhận (Receptive Field - RF)**:
Công thức tích lũy RF qua các lớp với stride = 1: $RF_l = RF_{l-1} + (k_l - 1)$.
- Lớp 1 (kernel $3 \times 3$): $RF_1 = 3$.
- Lớp 2 (kernel $3 \times 3$): $RF_2 = RF_1 + (3 - 1) = 3 + 2 = 5$.
Như vậy, 2 lớp $3 \times 3$ bao quát chính xác vùng đón nhận $5 \times 5$.
2. **So sánh tham số (giả sử cùng $C$ kênh vào và $C$ kênh ra)**:
- Một lớp $5 \times 5$: $5 \times 5 \times C \times C = 25 C^2$ tham số.
- Hai lớp $3 \times 3$: $2 \times (3 \times 3 \times C \times C) = 18 C^2$ tham số.
- Tỉ lệ tiết kiệm tham số:
$$\frac{25 C^2 - 18 C^2}{25 C^2} = \frac{7}{25} = 28\%$$
Đồng thời, mạng có 2 lớp kích hoạt phi tuyến tính thay vì chỉ 1.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hiểu nhầm: Nghĩ rằng hai lớp $3 \times 3$ sẽ có Receptive field là $3+3=6$ hoặc $3 \times 3 = 9$. Hãy nhớ công thức: $RF = 1 + \sum (k_i - 1) = 1 + 2 + 2 = 5$.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C13: Cùng kiểm tra nguyên lý thiết kế đột phá của VGGNet: xếp chồng các kernel nhỏ $3 \times 3$ để mở rộng Receptive Field mà vẫn tiết kiệm tham số tính toán và tăng chiều sâu biểu diễn phi tuyến.

---

### Câu 39 [VOAI02-M39] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Global Average Pooling (GAP) được giới thiệu trong mạng Network In Network (Lin et al.) và chuẩn hóa trong ResNet nhằm mục đích cốt lõi nào?

- **A.** Thay thế các lớp Fully Connected cồng kềnh ở cuối mạng, lấy trung bình toàn bộ không gian HxW của từng kênh để giảm tham số
- **B.** Chuyển đổi ảnh màu RGB thành ảnh xám đơn sắc nhằm tăng tốc độ tính toán lan truyền thuận trên các thiết bị nhúng
- **C.** Loại bỏ hoàn toàn hàm kích hoạt Softmax ở tầng đầu ra để chuyển bài toán phân loại đa lớp thành bài toán hồi quy lồi
- **D.** Nhân đôi kích thước không gian của feature map thông qua phép nội suy song tuyến tính trước khi đưa vào bộ phân loại

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Global Average Pooling (GAP):** Phép toán tính trung bình cộng toàn bộ các giá trị không gian trên từng feature map: $\text{GAP}(F_c) = \frac{1}{H \cdot W} \sum_{h, w} F_c(h, w)$.
- **Thay thế Fully Connected Layers:** Biến đổi trực tiếp tensor $(N, C, H, W)$ thành vector $(N, C)$ đưa thẳng vào bộ phân loại.
- **Chống Overfitting & Giảm tham số:** Loại bỏ hàng chục triệu trọng số dễ gây quá khớp của các tầng Dense truyền thống, đồng thời tăng tính bất biến đối với phép dịch chuyển.

🍼 **Hình dung thực tế cho em bé:**
Trong mạng VGG cũ, sau khi trích xuất đặc trưng, người ta kéo phẳng toàn bộ ảnh (Flatten) rồi nối vào các lớp Dense khổng lồ, ngốn tới 120 triệu tham số (85% toàn mạng) và cực kỳ dễ học vẹt (overfit)! Global Average Pooling giải quyết bằng cách: mỗi kênh đặc trưng (ví dụ kênh phát hiện tai mèo) chỉ cần lấy trung bình một con số duy nhất đại diện cho toàn bộ kênh. Không cần thêm bất kỳ trọng số nào, triệt tiêu hoàn toàn nguy cơ học vẹt!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Cho feature map cuối cùng $F \in \mathbb{R}^{C \times H \times W}$:
- Cách cũ (Flatten + Dense): Duỗi thành vector độ dài $C \cdot H \cdot W$, kết nối với lớp Dense $D$ nơ-ron $\implies$ Tốn $(C \cdot H \cdot W) \times D$ tham số trọng số (ví dụ $512 \times 7 \times 7 \times 4096 \approx 102$ triệu tham số!).
- Cách GAP (`nn. AdaptiveAvgPool2d((1, 1))`):
$$y_c = \frac{1}{H \cdot W} \sum_{h=1}^H \sum_{w=1}^W F_{c, h, w}$$
Biến feature map $(C, H, W)$ thành vector $(C, 1, 1)$ mà **HOÀN TOÀN KHÔNG CẦN THAM SỐ HUẤN LUYỆN** ($0$ parameter). Sau đó chỉ cần một lớp Linear duy nhất $C \to K$ nơ-ron lớp phân loại.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy khái niệm: GAP không làm mất thông tin kênh; mỗi kênh biểu diễn một bản đồ phản hồi đặc trưng ngữ nghĩa (semantic category), GAP buộc mỗi kênh phải trở thành một ' bản đồ tin cậy ' của một khái niệm cụ thể.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi lý thuyết độc lập về kỹ thuật GAP trong kiến trúc Network In Network và ResNet, loại bỏ hoàn toàn các tầng kết nối đầy đủ (Fully Connected) chiếm 80-90% tham số trong các mạng cổ điển (§3.3).

---

### Câu 40 [VOAI02-M40] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong khối Residual Block của kiến trúc ResNet, đầu ra được tính bằng phép cộng $y = \mathcal{F}(x, \{W_i\}) + x$. Về mặt giải tích lan truyền ngược, vì sao cơ chế này giải quyết triệt để vấn đề suy thoái (Degradation Problem) và biến mất gradient trong các mạng cực sâu (100+ lớp)?

- **A.** Phép cộng làm tăng gấp đôi số lượng kênh đặc trưng, cung cấp thêm dung lượng biểu diễn cho các tầng sâu của mạng
- **B.** Cơ chế này loại bỏ hoàn toàn các lớp Batch Normalization, giúp quá trình huấn luyện không bị phụ thuộc vào kích thước lô
- **C.** Đạo hàm theo x chứa số hạng '+ 1' hoạt động như đường cao tốc gradient truyền ngược về lớp nông không bị suy giảm
- **D.** Cơ chế này biến đổi mọi ma trận trọng số thành ma trận trực giao đơn vị, triệt tiêu hoàn toàn sự thay đổi phương sai

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Residual Connection (Kết nối tắt):** Đầu ra khối mạng cộng thêm đầu vào trực tiếp: $y = \mathcal{F}(x, \{W_i\}) + x$.
- **Giải tích đạo hàm:** Khi lan truyền ngược, đạo hàm theo đầu vào là $\frac{\partial y}{\partial x} = \frac{\partial \mathcal{F}}{\partial x} + 1$.
- **Triệt tiêu tiêu biến gradient:** Dù đạo hàm $\frac{\partial \mathcal{F}}{\partial x}$ có suy giảm tiệm cận về 0 qua các tầng sâu, số hạng $+1$ vẫn đảm bảo gradient được truyền nguyên vẹn ngược về các tầng đầu tiên.

🍼 **Hình dung thực tế cho em bé:**
Trong mạng bình thường, gradient khi đi lùi qua 100 lớp giống như một dòng nước phải chảy qua 100 van khóa liên tiếp. Nếu mỗi van làm giảm 10%, sau 100 van nước cạn kiệt (gradient biến mất)! Phép cộng + x trong ResNet tạo ra một đường ống cao tốc riêng chạy song song: gradient luôn có số hạng '+ 1' chảy thẳng tuột từ lớp 100 về lớp 1 mà không bị bất kỳ van khóa nào cản trở!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Quy tắc đạo hàm lan truyền ngược cho khối $x_{l+1} = x_l + \mathcal{F}(x_l, W_l)$:
Áp dụng Chain Rule cho bất kỳ lớp nông $l$ từ lớp sâu $L$:
$$\frac{\partial \mathcal{E}}{\partial x_l} = \frac{\partial \mathcal{E}}{\partial x_L} \frac{\partial x_L}{\partial x_l} = \frac{\partial \mathcal{E}}{\partial x_L} \left( I + \frac{\partial}{\partial x_l} \sum_{i=l}^{L-1} \mathcal{F}(x_i, W_i) \right)$$
Số hạng $\frac{\partial \mathcal{E}}{\partial x_L} I$ đảm bảo gradient luôn được bảo toàn và truyền thẳng ngược về lớp $l$ ngay cả khi gradient của các lớp biến đổi phi tuyến $\frac{\partial \mathcal{F}}{\partial x_l}$ bị triệt tiêu tiệm cận 0.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy phân biệt: Phép toán kết nối trong ResNet là PHÉP CỘNG phần tử theo phần tử ($ADD$), KHÔNG PHẢI ghép nối kênh ($CONCAT$ như U-Net hay DenseNet).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.4 Skip Connection: ResNet (ADD) vs U-Net (CONCAT)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C22: OLP01-C22 nêu hiện tượng suy thoái hiệu năng khi mạng quá sâu, còn M40 giải thích về mặt giải tích số hạng đạo hàm $+1$ trong kết nối tắt (Skip Connection) của ResNet giải quyết triệt để vấn đề này.

---

### Câu 41 [VOAI02-M41] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán phân đoạn ảnh ngữ nghĩa (Semantic Segmentation), kiến trúc U-Net (Ronneberger et al.) sử dụng Skip Connections để kết nối các feature maps từ nhánh Encoder sang nhánh Decoder bằng phép toán nào, và nhằm mục đích gì?

- **A.** Phép cộng phần tử (Element-wise Addition); Nhằm giảm một nửa số lượng kênh đặc trưng của nhánh Decoder khi giải mã
- **B.** Phép ghép nối kênh (Concatenation); Nhằm phục hồi thông tin không gian chi tiết và tọa độ đường biên bị mất ở Encoder
- **C.** Phép nhân từng phần tử (Hadamard Product); Nhằm làm mờ ảnh đầu ra để loại bỏ các nhiễu tần số cao của cảm biến scan
- **D.** Phép tích chập nhóm sâu (Depthwise Conv); Nhằm chuẩn hóa ma trận trọng số giữa hai nhánh độc lập mà không tăng kênh

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **U-Net Architecture:** Mạng nơ-ron phân đoạn ảnh gồm nhánh co (Encoder) và nhánh mở rộng (Decoder) đối xứng.
- **Skip Connection Concatenate:** Ghép nối trực tiếp các feature map độ phân giải cao từ Encoder sang Decoder theo chiều channel.
- **Khôi phục chi tiết không gian:** Bù đắp lượng thông tin vị trí không gian tinh xảo bị mất đi qua các tầng Max Pooling, giúp vẽ chính xác ranh giới của các phân vùng ảnh.

🍼 **Hình dung thực tế cho em bé:**
Khi ảnh đi qua phễu nén (Encoder), nó hiểu được ' đây là cái gì ' (ngữ nghĩa) nhưng lại bị mất nét tọa độ vị trí từng pixel do Max-Pooling làm mờ. U-Net giải quyết bằng cách lấy một bản sao ảnh nét ban đầu từ Encoder, đem bắc cầu ' dán nối ' (Concat) trực tiếp sang nhánh giải nén (Decoder). Nhờ thế Decoder vừa có ngữ nghĩa sâu, vừa có vị trí đường biên sắc nét để tô màu chính xác từng pixel!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tại mỗi tầng giải mã (Decoder level $l$):
1. Đầu vào từ tầng dưới được Upsample (Transposed Conv hoặc Bilinear Interpolation): $x_{up} \in \mathbb{R}^{C \times H \times W}$.
2. Feature map tương ứng từ Encoder được trích xuất: $x_{skip} \in \mathbb{R}^{C \times H \times W}$.
3. Thực hiện phép nối ghép kênh (Channel Concatenation):
$$x_{cat} = [x_{up}, \; x_{skip}] \in \mathbb{R}^{2C \times H \times W}$$
Khác với ResNet dùng phép cộng $ADD$ ($C + C \to C$) yêu cầu cùng số kênh, U-Net giữ nguyên song song hai luồng thông tin (ngữ nghĩa trừu tượng + tọa độ không gian cục bộ) cho lớp Conv tiếp theo tự do học cách dung hợp.
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy kinh điển: Nhầm giữa U-Net (dùng `torch.cat([x1, x2], dim=1)`) và ResNet (dùng `x1 + x2`). Câu hỏi này kiểm tra sự phân biệt rạch ròi giữa 2 kiến trúc trụ cột của CV.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.4 Skip Connection: ResNet (ADD) vs U-Net (CONCAT)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C23: Cùng kiểm tra cơ chế Skip Connection trong mạng phân vùng ảnh U-Net: phép nối ghép kênh (Concatenation) dọc theo chiều channel giúp bảo toàn nguyên vẹn tọa độ pixel ranh giới vật thể.

---

### Câu 42 [VOAI02-M42] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho ảnh đầu vào kích thước $224 \times 224 \times 3$. Trong kiến trúc Vision Transformer (ViT-Base, Dosovitskiy et al.) với kích thước patch $P = 16 \times 16$ và số chiều ẩn $D = 768$, chuỗi biểu diễn đầu vào trước khi đưa vào các khối Transformer Encoder bao gồm bao nhiêu token và có kích thước tensor bằng bao nhiêu?

- **A.** 197 tokens (gồm 196 patch tokens + 1 token học được [CLS]), kích thước (197, 768)
- **B.** 224 tokens (gồm 224 patch tokens dọc theo trục đường chéo), kích thước (224, 768)
- **C.** 196 tokens (chỉ gồm các patch tokens thuần túy không có CLS), kích thước (196, 768)
- **D.** 14 tokens (tương ứng với 14 lát cắt không gian theo chiều dọc), kích thước (14, 768)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Vision Transformer (ViT):** Chia ảnh kích thước $H \times W \times C$ thành lưới $N$ patch vuông kích thước $P \times P$.
- **Số lượng patch:** $N = \frac{H \cdot W}{P^2} = \frac{224 \cdot 224}{16 \cdot 16} = 14 \times 14 = 196$ patch.
- **[CLS] Token:** Bổ sung thêm 1 token đặc biệt có thể học ở đầu chuỗi để đại diện cho toàn bộ bức ảnh $\implies$ Tổng cộng $196 + 1 = 197$ token.
- **Kích thước tensor đầu vào:** $[197, D]$ với $D = 768$ (ViT-Base).

🍼 **Hình dung thực tế cho em bé:**
Ảnh 224x224 được cắt thành các mảnh ghép vuông 16x16 như chơi xếp hình. Số mảnh ghép là (224/16) × (224/16) = 14 × 14 = 196 mảnh. Mỗi mảnh được biến thành một vector 768 chiều. Để phân loại toàn bộ bức ảnh, ViT gắn thêm một ' học sinh trưởng ' đặc biệt đứng ở đầu hàng gọi là token [CLS]. Tổng cộng có 196 + 1 = 197 token!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. Số lượng patch không gian $N$:
$$N = \frac{H \cdot W}{P^2} = \frac{224 \times 224}{16 \times 16} = 14 \times 14 = 196$$
2. Mỗi patch có kích thước $(P^2 \cdot C) = 16 \times 16 \times 3 = 768$, được chiếu tuyến tính qua ma trận $E \in \mathbb{R}^{768 \times D}$ thành vector $D = 768$.
3. Chuỗi token bổ sung thêm token học được $[CLS] \in \mathbb{R}^{1 \times D}$ ở vị trí đầu tiên (prefix):
$$z_0 = [x_{class}; \; x_p^1 E; \; x_p^2 E; \dots; x_p^N E] + E_{pos} \in \mathbb{R}^{(196 + 1) \times 768} = \mathbb{R}^{197 \times 768}$$
Sau đó cộng thêm Positional Embedding $E_{pos} \in \mathbb{R}^{197 \times 768}$.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy bỏ quên token [CLS]: Nhiều thí sinh tính $14 \times 14 = 196$ rồi vội chọn đáp án A. Trong ViT (chuẩn theo BERT), token `[CLS]` luôn được gắn thêm vào đầu chuỗi để làm đại diện cho dự đoán phân loại nhãn.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.5 Vision Transformer (ViT — Dosovitskiy et al., 2020)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C24: OLP01-C24 mô tả nguyên lý chia ảnh thành chuỗi patch phẳng và chiếu tuyến tính trong ViT, còn M42 yêu cầu tính toán cụ thể số lượng token ($196 + 1 = 197$) và kích thước tensor biểu diễn.

---

### Câu 43 [VOAI02-M43] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho hai bounding box hình chữ nhật trong mặt phẳng tọa độ theo định dạng $[x_1, y_1, x_2, y_2]$ (tọa độ góc trên-trái và góc dưới-phải):
- Box A: $[10, 10, 50, 50]$
- Box B: $[30, 30, 70, 70]$
Chỉ số IoU (Intersection over Union) giữa hai hộp này bằng bao nhiêu?

- **A.** $\frac{1}{7}$ (khoảng 0.143)
- **B.** $\frac{4}{32}$ (khoảng 0.125)
- **C.** $\frac{1}{4}$ (khoảng 0.250)
- **D.** $\frac{2}{7}$ (khoảng 0.286)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Tọa độ Bounding Box:** Định dạng $[x_1, y_1, x_2, y_2]$ với diện tích $\text{Area} = (x_2 - x_1) \cdot (y_2 - y_1)$.
- **Diện tích từng hộp:** Box A: $(50-10)(50-10) = 1600$; Box B: $(70-30)(70-30) = 1600$.
- **Phần giao nhau (Intersection):** $[\max(10, 30), \max(10, 30), \min(50, 70), \min(50, 70)] = [30, 30, 50, 50] \implies \text{Area}_I = 20 \times 20 = 400$.
- **Chỉ số IoU:** $\text{IoU} = \frac{\text{Area}_I}{\text{Area}_A + \text{Area}_B - \text{Area}_I} = \frac{400}{1600 + 1600 - 400} = \frac{400}{2800} = \frac{1}{7} \approx 0.143$.

🍼 **Hình dung thực tế cho em bé:**
Hộp A rộng 40, cao 40 -> diện tích 1600. Hộp B rộng 40, cao 40 -> diện tích 1600. Phần giao nhau giữa chúng nằm từ x=30 đến 50 (rộng 20) và y=30 đến 50 (cao 20) -> diện tích phần giao là 20 × 20 = 400. Diện tích phần hợp (Union) là 1600 + 1600 - 400 = 2800. Chỉ số IoU = Giao / Hợp = 400 / 2800 = 1/7 ≈ 0.1428!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. Diện tích từng hộp:
- $\text{Area}(A) = (x_2^A - x_1^A) \times (y_2^A - y_1^A) = (50 - 10) \times (50 - 10) = 40 \times 40 = 1600$.
- $\text{Area}(B) = (x_2^B - x_1^B) \times (y_2^B - y_1^B) = (70 - 30) \times (70 - 30) = 40 \times 40 = 1600$.
2. Phần giao nhau (Intersection):
- $x_1^{\cap} = \max(x_1^A, x_1^B) = \max(10, 30) = 30$.
- $y_1^{\cap} = \max(y_1^A, y_1^B) = \max(10, 30) = 30$.
- $x_2^{\cap} = \min(x_2^A, x_2^B) = \min(50, 70) = 50$.
- $y_2^{\cap} = \min(y_2^A, y_2^B) = \min(50, 70) = 50$.
- $\text{Area}(\cap) = (50 - 30) \times (50 - 30) = 20 \times 20 = 400$.
3. Phần hợp (Union):
$$\text{Area}(\cup) = \text{Area}(A) + \text{Area}(B) - \text{Area}(\cap) = 1600 + 1600 - 400 = 2800$$
4. Chỉ số IoU:
$$\text{IoU} = \frac{\text{Area}(\cap)}{\text{Area}(\cup)} = \frac{400}{2800} = \frac{1}{7} \approx 0.142857$$
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (4/32 = 0.125):** Thí sinh tính mẫu số bằng cách lấy $1600 + 1600 = 3200$ mà quên trừ đi phần giao 400. Luôn nhớ: $\text{Union} = A + B - \text{Giao}$!
- **Phương án C (1/4 = 0.250):** Lỗi chia phần giao cho diện tích của một hộp duy nhất ($400 / 1600 = 0.25$).
- **Phương án D (2/7 $\approx$ 0.286):** Lỗi nhân đôi diện tích phần giao trong tử số ($800 / 2800 = 2/7$).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B06: Cùng kiểm tra công thức tính chỉ số IoU (Intersection over Union) giữa hai hộp giới hạn: OLP01-B06 cho sẵn diện tích giao và hợp, còn M43 yêu cầu tính trực tiếp từ tọa độ hộp $[x_1, y_1, x_2, y_2]$.

---

### Câu 44 [VOAI02-M44] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong pipeline phát hiện đối tượng (Object Detection), thuật toán NMS chuẩn mực hoạt động tuần tự theo các bước nào sau đây để loại bỏ các bounding box trùng lặp?

- **A.** Lọc box có score < thresh -> Sắp xếp giảm dần -> Chọn box cao nhất -> Tính IoU với box còn lại -> Xóa box có IoU > thresh
- **B.** Tính trung bình tọa độ của toàn bộ các anchor box trong ảnh rồi vẽ lại một bounding box duy nhất bao trọn toàn bộ
- **C.** Chọn ngẫu nhiên một bounding box cho mỗi nhãn lớp đối tượng xuất hiện trong ảnh mà không cần xem xét điểm tin cậy
- **D.** Chỉ giữ lại bounding box có diện tích không gian lớn nhất và xóa toàn bộ các bounding box nhỏ hơn bất kể điểm số

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **NMS (Non-Maximum Suppression):** Thuật toán hậu xử lý loại bỏ các bounding box dự đoán dư thừa bọc quanh cùng một đối tượng.
- **Bước 1:** Lọc bỏ các box có điểm tin cậy (Confidence Score) thấp hơn ngưỡng $\theta_{conf}$.
- **Bước 2:** Sắp xếp các box còn lại theo thứ tự điểm tin cậy giảm dần.
- **Bước 3 & 4:** Chọn box có điểm cao nhất lưu vào tập kết quả; tính IoU giữa box này với tất cả các box còn lại và loại bỏ bất kỳ box nào có $\text{IoU} \ge \theta_{NMS}$. Lặp lại cho đến hết.

🍼 **Hình dung thực tế cho em bé:**
Khi mô hình phát hiện một con mèo, nó vẽ ra hàng chục khung bao quanh con mèo đó. NMS giải quyết như sau: Chọn khung có điểm tin cậy cao nhất (khung đẹp nhất), giữ lại. Sau đó đo xem các khung khác có bị ' đè ' lên khung này quá nhiều không (IoU lớn hơn ngưỡng, ví dụ 0.5). Nếu đè lên quá nhiều nghĩa là cùng vẽ một con mèo -> Xóa bỏ các khung phụ đó đi! Lặp lại với các con vật khác.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thuật toán NMS chuẩn:
- Đầu vào: Tập các hộp $\mathcal{B} = \{b_1, \dots, b_M\}$, điểm tin cậy tương ứng $\mathcal{S} = \{s_1, \dots, s_M\}$, ngưỡng $N_t$.
- Khởi tạo tập kết quả $\mathcal{D} = \emptyset$.
- Vòng lặp:
  1. Chọn $m = \arg\max_i \mathcal{S}$.
  2. Đưa $b_m$ vào $\mathcal{D}$ và loại bỏ $b_m$ khỏi $\mathcal{B}$.
  3. Với mọi $b_i \in \mathcal{B}$ còn lại:
     - Nếu $\text{IoU}(b_m, b_i) \ge N_t$: Loại bỏ $b_i$ khỏi $\mathcal{B}$ (suppress).
  4. Dừng khi $\mathcal{B} = \emptyset$.
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy ngưỡng: Nếu đặt `IoU_thresh` quá thấp (ví dụ 0.1), hai con ngựa đứng sát cạnh nhau sẽ bị NMS xóa mất một con (bỏ sót đối tượng). Nếu đặt quá cao (ví dụ 0.9), sẽ bị sót nhiều box rác trùng lặp.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C15: OLP01-C15 nêu vai trò loại bỏ các bounding box dư thừa của NMS, còn M44 chi tiết hóa từng bước thực thi trong pipeline thuật toán.

---

### Câu 45 [VOAI02-M45] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong đánh giá mô hình Object Detection chuẩn COCO, kí hiệu **mAP@[0.5:0.95]** (hay mAP@[.5:.95]) biểu thị điều gì?

- **A.** Tỉ lệ khung hình (Aspect Ratio) của các bounding box hợp lệ phải nằm nghiêm ngặt trong khoảng từ 0.5 đến 0.95
- **B.** Chỉ số mAP chỉ được tính toán riêng biệt tại một ngưỡng IoU cố định duy nhất bằng 0.50 theo tiêu chuẩn PASCAL VOC
- **C.** Độ chính xác trung bình của mô hình được đảm bảo nằm trong khoảng tin cậy thống kê từ 50% đến 95% trên tập kiểm thử
- **D.** Giá trị trung bình của mAP tính qua 10 ngưỡng IoU từ 0.50 đến 0.95 với bước nhảy 0.05 trên toàn bộ các lớp đối tượng

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **mAP (Mean Average Precision):** Chỉ số đánh giá tổng thể độ chính xác phát hiện vật thể trên toàn bộ các lớp đối tượng.
- **Ngưỡng IoU đơn lẻ (mAP@0.50):** Chỉ yêu cầu hộp dự đoán có $\text{IoU} \ge 0.50$ với nhãn thực tế là được tính là True Positive.
- **Chuẩn COCO mAP@[0.5:0.95]:** Trung bình cộng của 10 giá trị mAP tính tại 10 ngưỡng IoU cách đều nhau từ 0.50 đến 0.95 với bước nhảy 0.05 ($0.50, 0.55, \dots, 0.95$), đòi hỏi mô hình phải bám viền cực kỳ chuẩn xác.

🍼 **Hình dung thực tế cho em bé:**
Nếu chỉ chấm điểm ở mức IoU = 0.5 (như chuẩn PASCAL VOC cũ), mô hình chỉ cần vẽ hộp bao trúng một nửa là được điểm tối đa (rất dễ dãi). Chuẩn COCO mAP@[0.5:0.95] nghiêm khắc hơn nhiều: chấm điểm ở 10 mức khắt khe khác nhau (0.50, 0.55, 0.60,... cho đến 0.95 - vẽ chuẩn từng milimet), rồi lấy trung bình cộng của cả 10 mức đó lại để tìm ra mô hình định vị chính xác nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định nghĩa COCO Average Precision:
$$\text{mAP}@[0.5:0.95] = \frac{1}{10} \sum_{k=0}^9 \text{mAP}_{\text{IoU} = 0.50 + 0.05 \times k}$$
Trong đó tại mỗi ngưỡng IoU, $AP$ của từng lớp được tính bằng diện tích dưới đường cong Precision-Recall đã được nội suy làm mượt (All-point interpolated PR curve):
$$AP = \sum_{r \in R} (r_{n+1} - r_n) p_{interp}(r_{n+1}), \quad p_{interp}(r) = \max_{\tilde{r} \ge r} p(\tilde{r})$$
Sau đó lấy trung bình $AP$ trên tất cả các lớp phân loại.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy nhầm lẫn: Nhầm mAP@0.5 (chuẩn VOC) với mAP@[0.5:0.95] (chuẩn COCO). Điểm mAP@[0.5:0.95] thường thấp hơn mAP@0.5 từ 15% đến 25% vì các ngưỡng IoU $\ge 0.85$ đòi hỏi hộp bao cực kỳ khắt khe.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.
🔗 **Mắt xích & Liên hệ bài học:** Làm rõ thước đo đánh giá độ chính xác tiêu chuẩn COCO mAP@[0.5:0.95] đòi hỏi mô hình vừa định danh đúng lớp vừa dự đoán hộp bám sát biên giới hạn ở nhiều mức độ khắt khe IoU (§3.6).

---

### Câu 46 [VOAI02-M46] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi triển khai hệ thống Computer Vision trên thiết bị nhúng hoặc yêu cầu thời gian thực (Real-time $\ge 30$ FPS), mô hình phát hiện đối tượng thuộc họ nào là lựa chọn ưu tiên hàng đầu, và sự đánh đổi (trade-off) so với mô hình 2-stage là gì?

- **A.** Họ 1-stage (YOLO, SSD) xử lý ảnh trong 1 lần quét không cần RPN riêng, tốc độ rất cao (real-time), dù có thể kém hơn chút ở vật thể nhỏ
- **B.** Họ 2-stage (Faster R-CNN) đề xuất vùng trước nên tốc độ suy luận nhanh gấp đôi mô hình 1-stage trên các thiết bị phần cứng di động
- **C.** Họ Transformer (DETR) loại bỏ hoàn toàn các thành phần CNN, đạt tốc độ xử lý thời gian thực vượt trội trên các chip CPU đơn nhân
- **D.** Cả hai họ mô hình đều có cùng cấu trúc và tốc độ suy luận tương đương, chỉ khác biệt ở định dạng nhãn bounding box đầu ra

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **One-Stage Detector (YOLO, SSD, RetinaNet):** Dự đoán trực tiếp tọa độ bounding box và phân loại lớp từ feature map chỉ qua một lượt forward duy nhất, tốc độ cực cao ($> 30$ FPS), lý tưởng cho thiết bị nhúng.
- **Two-Stage Detector (Faster R-CNN):** Gồm 2 giai đoạn: sinh vùng đề xuất (RPN) rồi mới trích xuất đặc trưng và phân loại, độ chính xác cao hơn trên vật thể nhỏ nhưng tốc độ chậm.
- **Sự đánh đổi:** 1-stage ưu tiên tốc độ xử lý thời gian thực, chấp nhận đánh đổi một phần độ chính xác khi phát hiện các vật thể kích thước siêu nhỏ hoặc chen chúc dày đặc.

🍼 **Hình dung thực tế cho em bé:**
2-stage (như Faster R-CNN) giống như một công ty có hai phòng ban: phòng 1 tìm kiếm các vùng nghi ngờ có đồ vật (RPN), phòng 2 soi kính lúp phân loại chi tiết -> Rất kỹ tính và chính xác nhưng chậm chạp (chỉ 5-10 FPS). 1-stage (như YOLO - You Only Look Once) giống như một siêu xạ thủ: chỉ liếc nhìn bức ảnh đúng một lần duy nhất là vẽ hộp và đọc tên đồ vật ngay lập tức -> Cực nhanh (60-140 FPS), lý tưởng cho camera thời gian thực!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **2-stage (Faster R-CNN)**: Tách làm 2 pha tuần tự:
- Stage 1: Region Proposal Network (RPN) sinh ra ~2000 RoI (Region of Interest).
- Stage 2: RoI Pooling / RoI Align + Fully Connected heads phân loại và tinh chỉnh bounding box cho từng RoI $\implies$ Tốn nhiều tài nguyên tính toán và độ trễ cao (Latency ~100-200ms).
2. **1-stage (YOLO v8/v11)**: Mô hình hóa bài toán detection thành bài toán hồi quy trực tiếp từ lưới ô ảnh (Grid cell / Anchor-free dense prediction) sang tọa độ và xác suất lớp trong một forward pass $\implies$ Tốc độ vượt trội (Latency ~5-15ms, $\ge 60$ FPS).
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy đề thi: Hỏi về kịch bản thời gian thực trên camera giám sát/robot tự hành mà chọn Faster R-CNN là sai. Đáp án chuẩn phải là 1-stage detector.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C16: Cùng so sánh sự đánh đổi giữa 1-stage và 2-stage detector: tốc độ xử lý thời gian thực (FPS) đối lập với độ chính xác định vị và nhận diện vật thể nhỏ.

---

### Câu 47 [VOAI02-M47] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán phát hiện ảnh giả mạo/DeepFake (Bài toán ' Kẻ mạo danh ' trong video AI Vietnam và IOAI 2026), vì sao việc kết hợp **32 đặc trưng vật lý kết cấu** (dung lượng file, gradient Sobel, Laplacian bậc 2, Gaussian residual, chu kỳ lưới nén JPEG $8 \times 8$) lại đem lại sự cải thiện vượt bậc so với việc chỉ dùng mạng CNN phân loại ảnh thông thường?

- **A.** Ảnh chụp thực tế không bao giờ có dung lượng tệp nhỏ hơn 100KB do cảm biến quang học luôn lưu giữ đầy đủ dải màu động
- **B.** Ảnh do AI sinh ra luôn có kích thước chiều rộng gấp đôi chiều cao do cơ chế nội suy song tuyến tính của bộ giải mã
- **C.** Các đặc trưng vật lý giúp giảm độ phân giải không gian của ảnh về 0, chuyển toàn bộ thông tin sang biểu diễn vector thưa
- **D.** Mô hình sinh ảnh để lại vết tích nhân tạo ở miền tần số cao và sai lệch thống kê nén JPEG mà CNN nhận diện ngữ nghĩa bỏ qua

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **DeepFake / AI-Generated Artifacts:** Ảnh do AI sinh ra thường có độ hoàn thiện thị giác bề mặt rất cao nhưng để lại các dấu vết bất thường ở miền tần số và kết cấu vi mô.
- **32 đặc trưng vật lý kết cấu:** Bao gồm gradient Sobel, toán tử Laplacian bậc 2, Gaussian residual và tính chu kỳ của ma trận lượng hóa JPEG $8 \times 8$.
- **Bản chất ưu việt:** Các mô hình CNN thông thường dễ bị đánh lừa bởi ngữ nghĩa vĩ mô; việc trích xuất tường minh các đặc trưng thống kê tần số cao giúp bóc trần sự thiếu tự nhiên của ảnh giả mạo.

🍼 **Hình dung thực tế cho em bé:**
Mạng CNN thông thường được huấn luyện để nhìn thấy ' con chó ' hay ' con mèo ' (ngữ nghĩa nội dung). Khi kẻ giả mạo tạo ra một bức ảnh con mèo giả bằng AI, nội dung con mèo trông vẫn rất đẹp mắt nên CNN bị đánh lừa! Nhưng 32 đặc trưng vật lý giống như máy soi kính hiển vi pháp y: nó không nhìn con mèo, nó soi các hạt nhiễu tần số cao, các vết cắt ghép lưới JPEG 8x8 và độ mờ của viền gradient. Nhờ thế phát hiện ngay đâu là ảnh do AI sinh ra!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Các đặc trưng vật lý miền tần số và cấu trúc vi mô:
1. **Phân tích nén JPEG**: Thuật toán nén JPEG chia ảnh thành các block $8 \times 8$ và áp dụng biến đổi DCT (Discrete Cosine Transform). Ảnh chụp từ camera thật có ma trận lượng tử hóa nhất quán. Ảnh AI sinh hoặc đã qua hậu kỳ chỉnh sửa có sự không đồng nhất trong lưới $8 \times 8$ (Periodic JPEG Grid Artifacts).
2. **Tàn dư tần số cao (High-frequency Residuals)**: Áp dụng lọc thông thấp Gauss $G_\sigma$ (với $\sigma = 1.2$), lấy hiệu $R = I - G_\sigma * I$. Ảnh do mô hình khuếch tán (Diffusion) thường có phân phối gradient Laplacian $\nabla^2 I$ và phổ năng lượng FFT lệch chuẩn so với cảm biến CMOS máy ảnh quang học thật.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy đóng băng backbone (Frozen Backbone Trap): Nếu freeze backbone ResNet/DenseNet pretrain trên ImageNet, mạng chỉ trích xuất semantic features (chó/mèo/nhà) và bỏ qua nhiễu tần số cao, dẫn đến điểm F1 bị kẹt ở mức thấp (~84%). Cần full fine-tuning hoặc bổ sung nhánh đặc trưng vật lý.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.8 Mô hình Sinh ảnh: GAN vs Diffusion vs Autoencoder**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-E03: M47 kiểm tra lý thuyết về 32 đặc trưng kết cấu vật lý và vi sai nén JPEG, là nền tảng trực tiếp để giải quyết bài toán tự luận thiết kế hệ thống phát hiện ảnh giả mạo trong VOAI03-E03.

---

### Câu 48 [VOAI02-M48] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kỹ thuật **MixUp** (Zhang et al.), hai ảnh $(x_i, x_j)$ và nhãn One-hot $(y_i, y_j)$ được kết hợp theo công thức nào với $\lambda \sim \text{Beta}(\alpha, \alpha)$?

- **A.** $\tilde{x} = (1 - \lambda) x_i + (1 - \lambda) x_j, \quad \tilde{y} = (1 - \lambda) y_i + (1 - \lambda) y_j$
- **B.** $\tilde{x} = \lambda x_i \odot (1 - \lambda) x_j, \quad \tilde{y} = \lambda y_i \odot (1 - \lambda) y_j$
- **C.** $\tilde{x} = \max(\lambda x_i, (1 - \lambda) x_j), \quad \tilde{y} = \max(\lambda y_i, (1 - \lambda) y_j)$
- **D.** $\tilde{x} = \lambda x_i + (1 - \lambda) x_j, \quad \tilde{y} = \lambda y_i + (1 - \lambda) y_j$

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **MixUp (Zhang et al., 2017):** Kỹ thuật điều chuẩn tăng cường dữ liệu dựa trên phép nội suy lồi giữa hai mẫu ngẫu nhiên.
- **Công thức nội suy:** $\tilde{x} = \lambda x_i + (1-\lambda) x_j$ và $\tilde{y} = \lambda y_i + (1-\lambda) y_j$ với $\lambda \sim \text{Beta}(\alpha, \alpha)$.
- **Hiệu ứng học máy:** Khuyến khích mô hình có hành vi tuyến tính giữa các lớp dữ liệu, làm mượt ranh giới quyết định và tăng cường khả năng chống chịu nhiễu đối kháng (Adversarial Robustness).

🍼 **Hình dung thực tế cho em bé:**
MixUp giống như việc hòa tan hai bức ảnh vào nhau như hiệu ứng bóng ma: lấy 70% màu của ảnh con mèo trộn với 30% màu của ảnh con chó. Đồng thời nhãn cũng được trộn theo đúng tỉ lệ đó: 0.7 nhãn Mèo + 0.3 nhãn Chó. Kỹ thuật này dạy cho mạng AI không được quá tự tin thái quá vào một nhãn duy nhất và làm cho không gian quyết định trở nên phẳng mịn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức toán học của MixUp:
Cho cặp mẫu $(x_i, y_i)$ và $(x_j, y_j)$ được lấy ngẫu nhiên từ tập huấn luyện:
$$\lambda \sim \text{Beta}(\alpha, \alpha) \in [0, 1]$$
Ảnh tổng hợp:
$$\tilde{x} = \lambda x_i + (1 - \lambda) x_j$$
Nhãn tổng hợp (xác suất mềm / soft labels):
$$\tilde{y} = \lambda y_i + (1 - \lambda) y_j$$
Hàm mất mát huấn luyện trở thành:
$$\mathcal{L} = \lambda \mathcal{L}(\text{model}(\tilde{x}), y_i) + (1 - \lambda) \mathcal{L}(\text{model}(\tilde{x}), y_j)$$
Khác với CutMix (cắt dán hình chữ nhật của ảnh $j$ đè lên ảnh $i$), MixUp thực hiện phép nội suy tuyến tính lồi (convex linear interpolation) trên toàn bộ không gian pixel.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy cài đặt: Khi áp dụng MixUp, nhãn mục tiêu không còn là số nguyên (class index) mà trở thành vector phân phối mềm, do đó không thể dùng trực tiếp `nn. CrossEntropyLoss()` với target dạng class index mà phải dùng target dạng xác suất (hỗ trợ từ PyTorch 1.10+).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§3.9 Data Augmentation & Transfer Learning**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi độc lập về kỹ thuật tăng cường dữ liệu kết hợp tuyến tính MixUp (Zhang et al.), giúp làm trơn bề mặt quyết định và tăng cường tính ổn định của mô hình (§3.9).

---

### Câu 49 [VOAI02-M49] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự chuẩn mực logic của các bước tiền xử lý văn bản thô (Text Preprocessing) nào sau đây là CHÍNH XÁC NHẤT?

- **A.** Loại bỏ từ dừng (Stopwords) -> Đưa về từ điển (Lemmatization) -> Tách từ (Tokenization) -> Hạ chữ thường (Lowercasing)
- **B.** Vector hóa (Vectorization) -> Tách từ (Tokenization) -> Rút gọn gốc từ (Stemming) -> Loại bỏ từ dừng (Stopwords)
- **C.** Tách từ (Tokenization) -> Chuẩn hóa & Hạ thường -> Loại bỏ từ dừng (Stopwords) -> Rút gốc từ (Stem/Lemma) -> Vector hóa
- **D.** Đưa về từ điển (Lemmatization) -> Vector hóa -> Tách từ (Tokenization) -> Gán nhãn từ loại (POS Tagging)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Text Preprocessing Pipeline:** Quy trình tiền xử lý văn bản thô theo trình tự logic bất biến.
- **Bước 1 & 2:** Làm sạch ký tự đặc biệt, chuyển chữ thường (Lowercasing) và chuẩn hóa bảng mã Unicode.
- **Bước 3:** Tách từ (Tokenization) chia văn bản thành các token đơn lẻ.
- **Bước 4 & 5:** Loại bỏ từ dừng (Stopwords), chuẩn hóa từ gốc (Stemming/Lemmatization), sau đó mới thực hiện Vector hóa (TF-IDF / Embedding).

🍼 **Hình dung thực tế cho em bé:**
Quy trình tiền xử lý văn bản cổ điển giống như sơ chế nguyên liệu nấu ăn:
- Bước 1: Đổ nguyên liệu ra thớt và thái thành từng miếng/từ độc lập (Tách từ - Tokenization).
- Bước 2: Rửa sạch bụi bẩn, đưa về cùng kích cỡ đồng nhất (Chuẩn hóa ký tự & Hạ chữ thường).
- Bước 3: Nhặt bỏ rác và cọng thừa không dùng được (Lọc từ dừng - Stopwords như ' và ', ' thì ', ' là ').
- Bước 4: Gọt vỏ giữ lại phần lõi tinh túy (Rút gọn từ gốc - Stemming/Lemmatization).
- Bước 5: Cân đo định lượng thành các con số đưa vào mô hình (Vector hóa - BoW / TF-IDF)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Trật tự phụ thuộc logic trong pipeline NLP cổ điển:
1. **Tokenization**: Chia chuỗi văn bản thô thành mảng các đơn vị từ vựng độc lập $\{w_1, w_2, \dots, w_T\}$. Đây là tiền đề bắt buộc trước khi có thể duyệt từ điển hoặc đếm tần suất.
2. **Normalization & Lowercasing**: Đưa các biến thể về dạng đồng nhất (ví dụ: ' Apple ' và ' apple ' về ' apple ').
3. **Stopword Removal**: Loại bỏ các hư từ có tần suất xuất hiện quá cao nhưng mang ít giá trị ngữ nghĩa phân biệt.
4. **Stemming / Lemmatization**: Quy đổi các dạng ngữ pháp (chạy, đã chạy, đang chạy) về từ gốc (lemma).
5. **Vectorization**: Ánh xạ chuỗi từ đã sạch thành biểu diễn số học (TF-IDF, BoW).
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy phi logic trong các phương án sai:
- Phương án A sai vì đòi lọc Stopwords và Lemmatize trước khi Tokenize (không thể so khớp từ dừng trong từ điển khi chuỗi chưa được cắt token).
- Phương án B sai vì đưa Vector hóa lên đầu tiên (không thể vector hóa khi chưa có token).
- Phương án D sai vì đặt Lemmatize và Vector hóa trước Tokenize.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C28: Cùng kiểm tra thứ tự logic bất biến trong pipeline tiền xử lý văn bản kinh điển: làm sạch, tách từ, lọc stopwords, chuẩn hóa từ gốc rồi mới vector hóa đặc trưng.

---

### Câu 50 [VOAI02-M50] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán biểu diễn từ Word2Vec (Mikolov et al.), phát biểu nào sau đây phân biệt **CHÍNH XÁC** giữa hai kiến trúc CBOW (Continuous Bag-of-Words) và Skip-gram?

- **A.** CBOW chạy chậm hơn Skip-gram gấp 10 lần trên mọi tập dữ liệu do phải tính toán ma trận hiệp phương sai đầy đủ
- **B.** Cả hai kiến trúc đều sử dụng mạng Transformer 12 tầng với cơ chế Multi-Head Attention hai chiều tự do
- **C.** CBOW dùng từ trung tâm dự đoán từ ngữ cảnh; Skip-gram dùng các từ ngữ cảnh xung quanh để dự đoán từ trung tâm
- **D.** CBOW dùng ngữ cảnh xung quanh dự đoán từ trung tâm; Skip-gram dùng từ trung tâm dự đoán ngữ cảnh, tốt hơn cho từ hiếm

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **CBOW (Continuous Bag-of-Words):** Sử dụng các từ ngữ cảnh xung quanh để dự đoán từ trung tâm mục tiêu $w_t$; tốc độ huấn luyện nhanh, biểu diễn tốt các từ xuất hiện thường xuyên.
- **Skip-gram:** Sử dụng từ trung tâm $w_t$ để dự đoán các từ ngữ cảnh xung quanh trong cửa sổ; hoạt động xuất sắc với các tập dữ liệu nhỏ và biểu diễn cực tốt các từ hiếm gặp.
- **Negative Sampling:** Kỹ thuật xấp xỉ mẫu âm giúp giảm độ phức tạp tính toán mẫu số Softmax từ $|V|$ xuống $k$ từ ngẫu nhiên.

🍼 **Hình dung thực tế cho em bé:**
CBOW giống như một câu đố điền từ vào chỗ trống: cho bạn 4 từ xung quanh (ngữ cảnh) và bắt bạn đoán từ bị khuyết ở giữa (từ đích). Vì nó cộng gộp các từ xung quanh lại nên chạy rất nhanh. Ngược lại, Skip-gram làm việc khó hơn: chỉ đưa cho bạn 1 từ ở giữa và bắt bạn đoán ra các từ xung quanh. Vì làm bài khó hơn và lặp lại nhiều lần cho từng cặp, Skip-gram học cực kỳ sâu sắc và nhớ rất kỹ cả những từ hiếm gặp!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **CBOW**:
Tối đa hóa xác suất có điều kiện của từ trung tâm $w_t$ khi biết cửa sổ ngữ cảnh $C = \{w_{t-c}, \dots, w_{t+c}\} \setminus \{w_t\}$:
$$\mathcal{L}_{CBOW} = \sum_{t=1}^T \ln P(w_t \mid w_{t-c}, \dots, w_{t+c})$$
Vector ngữ cảnh được lấy trung bình: $v_C = \frac{1}{2c} \sum_{-c \le j \le c, j \ne 0} v_{w_{t+j}}$. Huấn luyện nhanh hơn, làm mượt ngữ cảnh tốt.
2. **Skip-gram**:
Tối đa hóa xác suất các từ ngữ cảnh khi biết từ trung tâm $w_t$:
$$\mathcal{L}_{Skip-gram} = \sum_{t=1}^T \sum_{-c \le j \le c, j \ne 0} \ln P(w_{t+j} \mid w_t)$$
Mỗi lần xuất hiện của từ hiếm được ghép cặp riêng lẻ với từng từ ngữ cảnh $\implies$ Nhận được nhiều lượt cập nhật gradient hơn $\implies$ Biểu diễn từ hiếm tốt hơn rõ rệt.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy đảo ngược: Đảo vai trò của CBOW và Skip-gram (A). Hãy nhớ: CBOW = Bag-of-Words đoán 1 từ giữa; Skip-gram = 1 từ nhảy cóc (skip) đoán cả bầy ngữ cảnh.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M21: VOAI03-M21 nêu nhược điểm mất ngữ cảnh của BoW, dẫn dắt tới sự ra đời của Word2Vec trong M50 với hai cơ chế đối ngẫu: CBOW (ngữ cảnh đoán từ) và Skip-gram (từ đoán ngữ cảnh).

---

### Câu 51 [VOAI02-M51] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho hai vector embedding biểu diễn ngữ nghĩa của hai từ: $u = [1, 2, 2]$ và $v = [2, 0, 1]$. Độ tương đồng Cosine (Cosine Similarity) giữa hai vector này bằng bao nhiêu?

- **A.** $\frac{4}{3\sqrt{5}}$ (khoảng 0.596)
- **B.** $\frac{4}{9\sqrt{5}}$ (khoảng 0.198)
- **C.** $\frac{4}{5\sqrt{3}}$ (khoảng 0.462)
- **D.** $\frac{2}{3\sqrt{5}}$ (khoảng 0.298)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Cosine Similarity:** Độ đo góc giữa hai vector không gian đặc trưng: $\cos(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2}$.
- **Tích vô hướng:** $u \cdot v = (1)(2) + (2)(0) + (2)(1) = 2 + 0 + 2 = 4$.
- **Độ dài vector:** $\|u\| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{9} = 3$; $\|v\| = \sqrt{2^2 + 0^2 + 1^2} = \sqrt{5}$.
- **Kết quả:** $\cos(u, v) = \frac{4}{3 \sqrt{5}} = \frac{4}{3 \times 2.236} \approx 0.596$.

🍼 **Hình dung thực tế cho em bé:**
Độ tương đồng Cosine đo góc kẹp giữa hai mũi tên: bằng tích vô hướng chia cho tích độ dài của hai mũi tên. Tích vô hướng: 1×2 + 2×0 + 2×1 = 2 + 0 + 2 = 4. Độ dài u = √(1² + 2² + 2²) = √9 = 3. Độ dài v = √(2² + 0² + 1²) = √5. Vậy kết quả là 4 / (3 × √5) ≈ 0.596!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức tính Cosine Similarity:
$$\text{CosineSim}(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2} = \frac{\sum_{i=1}^D u_i v_i}{\sqrt{\sum_{i=1}^D u_i^2} \sqrt{\sum_{i=1}^D v_i^2}}$$
Thay số từng thành phần:
1. Tích vô hướng (Dot product):
$$u \cdot v = (1 \times 2) + (2 \times 0) + (2 \times 1) = 2 + 0 + 2 = 4$$
2. Chuẩn Euclidean của $u$:
$$\|u\|_2 = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$
3. Chuẩn Euclidean của $v$:
$$\|v\|_2 = \sqrt{2^2 + 0^2 + 1^2} = \sqrt{4 + 0 + 1} = \sqrt{5}$$
4. Ghép lại mẫu số và phân số:
$$\text{CosineSim}(u, v) = \frac{4}{3 \sqrt{5}} = \frac{4 \sqrt{5}}{15} \approx \frac{4 \times 2.236}{15} \approx 0.59628$$
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy tính toán: Tính nhầm chuẩn của $v$ thành $\sqrt{4+0+1} = 3$ hoặc nhầm mẫu số thành $3 \times 3 = 9$ (chọn B). Luôn tính căn bậc hai cẩn thận từng vector.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cosine Similarity**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-B09: Cùng kiểm tra phép tính độ tương đồng Cosine $\frac{u \cdot v}{\|u\| \|v\|}$ giữa hai vector embedding: OLP01-B09 tính trong không gian 2D, còn M51 tính trong không gian 3D.

---

### Câu 52 [VOAI02-M52] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong mạng LSTM (Long Short-Term Memory), cổng nào chịu trách nhiệm quyết định tỉ lệ thông tin nào từ ô nhớ trạng thái cũ ($C_{t-1}$) sẽ bị xóa bỏ/lãng quên? Và GRU đã tinh giản cấu trúc của LSTM thành hai cổng nào?

- **A.** Forget Gate ($f_t$); GRU rút gọn thành 2 cổng là Reset Gate và Update Gate (loại bỏ ô nhớ Cell State riêng biệt)
- **B.** Input Gate ($i_t$); GRU giữ nguyên 3 cổng gồm Input Gate, Output Gate và cổng trạng thái Cell State trung gian
- **C.** Cell Gate ($C_t$); GRU loại bỏ hoàn toàn các cổng logic và chỉ sử dụng phép biến đổi tuyến tính đơn thuần
- **D.** Output Gate ($o_t$); GRU phân tách thành hai cổng độc lập gồm Forget Gate và Memory Projection Gate

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **LSTM Forget Gate ($f_t$):** $f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$, quyết định tỷ lệ thông tin nào từ ô nhớ cũ $C_{t-1}$ sẽ bị xóa bỏ (0: xóa hoàn toàn, 1: giữ nguyên vẹn).
- **Cấu trúc GRU (Gated Recurrent Unit):** Loại bỏ ô nhớ trạng thái $C_t$, gộp trạng thái ẩn và tinh giản còn duy nhất 2 cổng: Cổng cập nhật (Update Gate $z_t$) và Cổng đặt lại (Reset Gate $r_t$).
- **Lợi thế của GRU:** Ít tham số hơn $\approx 25\%$, tốc độ huấn luyện nhanh hơn và ít bị quá khớp trên tập dữ liệu nhỏ.

🍼 **Hình dung thực tế cho em bé:**
LSTM giống như một chiếc xe tải chở theo một thùng hàng dài hạn (Cell state C). Chiếc van quyết định xem cái gì cũ bị vứt bỏ gọi là Forget Gate (Cổng quên). Nếu cổng này phun ra số 0, thông tin cũ bị xóa sạch; nếu phun ra số 1, thông tin được giữ lại nguyên vẹn. Mạng GRU là phiên bản em út gọn nhẹ hơn: nó bỏ hẳn thùng hàng riêng C, gộp lại chỉ còn đúng 2 van là Reset Gate (van xóa tạm) và Update Gate (van cập nhật) giúp chạy nhanh hơn mà hiệu quả tương đương!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **LSTM (3 cổng + 1 trạng thái ô nhớ)**:
- Forget Gate: $f_t = \sigma(W_f [h_{t-1}, x_t] + b_f) \in [0, 1]$
- Input Gate: $i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$
- Candidate Cell: $\tilde{C}_t = \tanh(W_c [h_{t-1}, x_t] + b_c)$
- Cập nhật Cell State: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$ (Gradient highway truyền thẳng nhờ phép cộng)
- Output Gate: $o_t = \sigma(W_o [h_{t-1}, x_t] + b_o) \implies h_t = o_t \odot \tanh(C_t)$
2. **GRU (Gated Recurrent Unit - 2 cổng)**:
- Reset Gate: $r_t = \sigma(W_r [h_{t-1}, x_t])$
- Update Gate: $z_t = \sigma(W_z [h_{t-1}, x_t])$
- Cập nhật ẩn: $h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$
Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy số lượng cổng: Nhớ rõ: LSTM có 3 cổng (Forget, Input, Output). GRU chỉ có 2 cổng (Reset, Update).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Mạng Nơ-ron Hồi Quy: RNN, LSTM & GRU**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M15: Cùng kiểm tra vai trò của Cổng quên (Forget Gate) trong kiến trúc LSTM và sự tiến hóa tinh giản sang GRU (chỉ gồm Reset Gate và Update Gate).

---

### Câu 53 [VOAI02-M53] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong cơ chế tính toán Self-Attention của Transformer (Vaswani et al.): $\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$. Vì sao hệ số tỷ lệ $\frac{1}{\sqrt{d_k}}$ lại mang tính chất sống còn đối với sự hội tụ của mô hình khi số chiều $d_k$ lớn?

- **A.** Để giảm thiểu dung lượng bộ nhớ VRAM tiêu tốn khi lưu trữ các ma trận chú ý trung gian trong pha lan truyền thuận
- **B.** Để loại bỏ hoàn toàn các giá trị âm trong ma trận trọng số trước khi đưa qua hàm chuẩn hóa Softmax
- **C.** Để biến đổi ma trận chú ý thành ma trận trực giao có định thức bằng 1, giúp bảo toàn năng lượng vector tín hiệu
- **D.** Khi $d_k$ lớn, tích $Q K^T$ có phương sai tăng bằng $d_k$ đẩy Softmax vào vùng bão hòa triệt tiêu gradient; chia $\sqrt{d_k}$ đưa var về 1

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Scaled Dot-Product Attention:** $\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$.
- **Vấn đề khi $d_k$ lớn:** Tích vô hướng $Q K^T = \sum_{i=1}^{d_k} q_i k_i$. Nếu các thành phần có trung bình 0 và phương sai 1, phương sai của tích vô hướng sẽ bằng $d_k$.
- **Bão hòa Softmax:** Với $d_k$ lớn (ví dụ 64 hoặc 128), các giá trị tích vô hướng trở nên cực lớn, đẩy hàm Softmax vào vùng có đạo hàm tiệm cận 0 $\implies$ gradient tiêu biến hoàn toàn.

🍼 **Hình dung thực tế cho em bé:**
Nếu bạn tung 64 đồng xu rồi cộng điểm lại (d_k=64), tổng điểm sẽ dao động rất mạnh (phương sai bằng 64). Khi nạp những con số quá to (ví dụ +20 hoặc -20) vào hàm Softmax, hàm Softmax sẽ bị bão hòa: một số nhận 0.99999 còn các số khác nhận 0.00000. Tại vùng bằng phẳng bão hòa này, độ dốc (đạo hàm) gần như bằng 0, mô hình bị ' tê liệt ' không thể học được gì! Chia cho √64 = 8 giúp kéo các con số trở về mức vừa phải, giữ cho gradient luôn sống khỏe!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Giả sử các thành phần của $q$ và $k$ là các biến ngẫu nhiên độc lập có kỳ vọng bằng 0 và phương sai bằng 1:
$$\mathbb{E}[q_i] = 0, \quad \text{Var}(q_i) = 1; \quad \mathbb{E}[k_i] = 0, \quad \text{Var}(k_i) = 1$$
Tích vô hướng $q \cdot k = \sum_{i=1}^{d_k} q_i k_i$ có:
- Kỳ vọng: $\mathbb{E}[q \cdot k] = \sum_{i=1}^{d_k} \mathbb{E}[q_i] \mathbb{E}[k_i] = 0$
- Phương sai:
$$\text{Var}(q \cdot k) = \sum_{i=1}^{d_k} \text{Var}(q_i k_i) = \sum_{i=1}^{d_k} \text{Var}(q_i) \text{Var}(k_i) = d_k$$
Độ lệch chuẩn là $\sigma = \sqrt{d_k}$. Khi $d_k = 64$ hoặc $128$, giá trị tích vô hướng có thể lên tới $\pm 25$. Tại các giá trị này, đạo hàm của hàm Softmax $\frac{\partial p_i}{\partial z_j} = p_i(\delta_{ij} - p_j) \to 0$.
Khi chia cho $\sqrt{d_k}$:
$$\text{Var}\left(\frac{q \cdot k}{\sqrt{d_k}}\right) = \frac{1}{d_k} \text{Var}(q \cdot k) = \frac{d_k}{d_k} = 1$$
Đưa phương sai trở về 1 chuẩn tắc, gradient chảy mượt mà.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Câu hỏi lý thuyết kinh điển trong phỏng vấn AI SOTA: Nếu bỏ chia $\sqrt{d_k}$ thì điều gì xảy ra? Trả lời ngay: Softmax bị bão hòa, gradient biến mất (Softmax saturation / gradient vanishes).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi độc lập đào sâu bản chất toán học của hệ số tỷ lệ $\frac{1}{\sqrt{d_k}}$ trong cơ chế Scaled Dot-Product Attention: duy trì phương sai bằng 1 để Softmax không bị đẩy vào vùng bão hòa gradient (§4.5).

---

### Câu 54 [VOAI02-M54] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Vì sao kiến trúc Transformer chia không gian biểu diễn thành $h$ đầu chú ý song song (Multi-Head Attention với $d_v = d_{model} / h$) thay vì chỉ sử dụng một đầu chú ý duy nhất kích thước đầy đủ $d_{model}$?

- **A.** Để mô hình có thể huấn luyện hội tụ ổn định (Loss Free) mà hoàn toàn không cần sử dụng bất kỳ hàm mất mát giám sát nào
- **B.** Vì phần cứng GPU chỉ hỗ trợ nhân các ma trận nhỏ (Hardware Limit) kích thước dưới 64 chiều trên mỗi luồng tính toán
- **C.** Để giảm tổng số lượng phép tính dấu phẩy động (FLOPs Reduction) xuống 10 lần so với việc tính toán trên một ma trận duy nhất
- **D.** Cho phép mô hình đồng thời chú ý đến các không gian con biểu diễn khác nhau (cú pháp, ngữ nghĩa xa, đại từ tham chiếu)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Multi-Head Attention (MHA):** Chiếu tuyến tính $Q, K, V$ thành $h$ không gian biểu diễn con khác nhau với số chiều $d_k = d_{model} / h$.
- **Đa dạng góc nhìn biểu diễn:** Một đầu chú ý có thể tập trung vào quan hệ cú pháp (động từ - tân ngữ), đầu khác tập trung vào quan hệ thực thể, đầu khác tập trung vào vị trí lân cận.
- **Single-Head Attention hạn chế:** Chỉ tính toán trung bình một phân phối chú ý duy nhất, làm mất đi khả năng nắm bắt đồng thời nhiều loại tương quan phức tạp trong câu.

🍼 **Hình dung thực tế cho em bé:**
Nếu chỉ có một người quan sát duy nhất, người đó nhìn cả lớp và chỉ thấy một bức tranh chung chung bị mờ nhạt. Multi-Head Attention giống như cử một nhóm 8 chuyên gia cùng vào phòng quan sát: chuyên gia 1 chuyên để ý ai là chủ ngữ của câu, chuyên gia 2 chuyên theo dõi đại từ ' nó ' đang chỉ vào ai, chuyên gia 3 chuyên soi cảm xúc của từ,... Sau đó cả 8 chuyên gia ghép báo cáo lại với nhau thành một bức tranh toàn diện và sâu sắc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định nghĩa Multi-Head Attention:
$$\text{MHA}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O$$
$$\text{head}_i = \text{Attention}(Q W_i^Q, \; K W_i^K, \; V W_i^V)$$
Trong đó mỗi ma trận chiếu $W_i^Q, W_i^K \in \mathbb{R}^{d_{model} \times d_k}$ với $d_k = d_{model} / h$.
Tổng chi phí tính toán FLOPs của $h$ đầu chiếu kích thước $d_k$ tương đương chính xác với 1 đầu duy nhất kích thước $d_{model}$:
$$h \times (O(N^2 d_k)) = O(N^2 (h \cdot d_k)) = O(N^2 d_{model})$$
Nhưng việc phân tách thành $h$ không gian con chiếu độc lập ngăn chặn hiện tượng làm mờ (averaging out) của trọng số Softmax khi có nhiều mối liên kết ngữ nghĩa cạnh tranh nhau.
Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hiểu sai chi phí tính toán: Rất nhiều người tưởng Multi-Head Attention tốn tính toán hơn Single-Head gấp $h$ lần. Thực tế tổng FLOPs là BẰNG NHAU vì số chiều của mỗi đầu đã bị thu nhỏ lại thành $d_{model}/h$.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi độc lập về lý do kiến trúc Multi-Head Attention vượt trội hơn Single-Head Attention: mở rộng khả năng nắm bắt đa góc độ quan hệ ngữ nghĩa trong câu (§4.5).

---

### Câu 55 [VOAI02-M55] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong Transformer nguyên bản, công thức mã hóa vị trí Sinusoidal được định nghĩa là $PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right)$ và $PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$. Ưu điểm toán học xuất sắc của công thức này là gì?

- **A.** Nó đảm bảo toàn bộ các phần tử trong vector (Positive Values) đều nhận giá trị strictly dương lớn hơn 10000
- **B.** Với độ lệch $k$, $PE(\text{pos} + k)$ biểu diễn tuyến tính (Linear Transformation) qua $PE(\text{pos})$, giúp học vị trí tương đối
- **C.** Loại bỏ hoàn toàn sự cần thiết của hàm Softmax (Softmax Free) trong việc tính toán phân phối xác suất của cơ chế Self-Attention
- **D.** Tự động chuẩn hóa vector embedding của từ vựng (Unit Variance) về phân phối chuẩn tắc có kỳ vọng 0 và phương sai 1

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Sinusoidal Positional Encoding:** $PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right)$, $PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$.
- **Biến đổi tuyến tính vị trí tương đối:** Với mọi độ lệch khoảng cách cố định $k$, tồn tại một ma trận biến đổi tuyến tính $M_k$ sao cho $PE_{pos+k} = M_k \cdot PE_{pos}$.
- **Khả năng ngoại suy (Extrapolation):** Cho phép mô hình dễ dàng học cách chú ý đến khoảng cách tương đối giữa các token, và có thể suy luận trên các chuỗi dài hơn độ dài đã thấy lúc huấn luyện.

🍼 **Hình dung thực tế cho em bé:**
Các hàm sin và cos với nhiều tần số khác nhau giống như các kim của chiếc đồng hồ: kim giây quay nhanh, kim phút quay vừa, kim giờ quay chậm. Mỗi vị trí pos được đánh dấu bằng một góc chỉ giờ duy nhất. Nhờ công thức cộng góc lượng giác sin(a + b), một từ đứng cách từ khác k bước luôn có thể biến đổi tuyến tính qua một phép quay ma trận cố định, giúp mô hình hiểu được khoảng cách tương đối giữa các từ mà không cần học vẹt!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng công thức cộng lượng giác cho hệ tọa độ quay $(\sin(\omega_i pos), \cos(\omega_i pos))$ với $\omega_i = \frac{1}{10000^{2i/d}}$:
$$\begin{bmatrix} \sin(\omega_i (pos + k)) \\ \cos(\omega_i (pos + k)) \end{bmatrix} = \begin{bmatrix} \cos(\omega_i k) & \sin(\omega_i k) \\ -\sin(\omega_i k) & \cos(\omega_i k) \end{bmatrix} \begin{bmatrix} \sin(\omega_i pos) \\ \cos(\omega_i pos) \end{bmatrix}$$
Ma trận biến đổi $M_k$ là một ma trận trực giao phụ thuộc duy nhất vào độ lệch khoảng cách tương đối $k$, hoàn toàn không phụ thuộc vào vị trí tuyệt đối $pos$.
Điều này cho phép mô hình tuyến tính hóa quan hệ vị trí tương đối một cách tự nhiên.
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy phân biệt: Phân biệt Sinusoidal Positional Encoding (cố định bằng giải tích, có thể ngoại suy độ dài) với Learned Positional Embedding (như BERT, là ma trận trọng số học được, cố định độ dài tối đa 512 token, không ngoại suy được vượt quá 512).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi độc lập về ưu điểm toán học tuyệt vời của mã hóa vị trí hàm sin/cos trong Transformer: cho phép mô hình dễ dàng học cách chú ý theo khoảng cách tương đối (§4.5).

---

### Câu 56 [VOAI02-M56] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Sự khác biệt căn bản về mặt cấu trúc chú ý (Attention Mechanism) và bài toán huấn luyện trước (Pre-training Objective) giữa BERT và GPT là gì?

- **A.** BERT là Decoder-only (Causal Mask); GPT là Encoder-only (Masked LM hai chiều tự do trong pha tiền huấn luyện)
- **B.** BERT chỉ xử lý dữ liệu hình ảnh (Vision Only); GPT chỉ xử lý dữ liệu văn bản (Text Only) trong các bài toán sinh tự hồi quy
- **C.** BERT là Encoder-only (Self-Attention 2 chiều, học bằng MLM); GPT là Decoder-only (Causal Mask 1 chiều xuôi, học bằng Next-Token)
- **D.** Cả hai mô hình đều sử dụng chung cơ chế (Causal Attention), chỉ khác biệt ở kích thước bộ từ điển tokenizer

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **BERT (Devlin et al., 2018):** Kiến trúc Encoder-only, sử dụng cơ chế chú ý hai chiều tự do (Bi-directional Self-Attention); mục tiêu tiền huấn luyện là Masked Language Modeling (MLM) và Next Sentence Prediction (NSP).
- **GPT (Radford et al., 2018):** Kiến trúc Decoder-only, sử dụng cơ chế chú ý nhân quả một chiều (Causal Masked Self-Attention) chỉ nhìn về các token quá khứ; mục tiêu tiền huấn luyện là Causal Language Modeling (Autoregressive Next Token Prediction).
- **Phạm vi ứng dụng:** BERT tối ưu cho hiểu văn bản (NLU: phân loại, trích xuất thực thể); GPT tối ưu cho sinh ngôn ngữ tự nhiên (NLG: viết tiếp, hội thoại, lập luận).

🍼 **Hình dung thực tế cho em bé:**
BERT giống như một học sinh giải đề điền từ vào chỗ trống: bạn ấy được nhìn thấy toàn bộ câu (cả từ đằng trước lẫn từ đằng sau) để đoán từ bị che [MASK] ở giữa -> Rất giỏi phân tích, đọc hiểu câu văn! Còn GPT giống như một nhà văn viết truyện nối tiếp: tại mỗi chữ, bạn ấy bị bịt mắt không được nhìn tương lai (Causal Mask), chỉ được nhìn các chữ đã viết ra trước đó để sáng tác chữ tiếp theo -> Cực kỳ tài năng trong việc sinh văn bản tự do (Generative AI)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **BERT (Encoder-only)**:
- Mặt nạ chú ý: Ma trận đầy đủ $M_{ij} = 0$ cho mọi $i, j$ $\implies$ Token $i$ có thể nhìn thấy token $j$ với $j > i$ (nhìn cả quá khứ và tương lai 2 chiều).
- Mục tiêu huấn luyện: Che ngẫu nhiên $15\%$ token thành `[MASK]`, tối thiểu hóa Cross-Entropy dự đoán token bị che: $\mathcal{L}_{MLM} = -\sum_{m \in M} \ln P(x_m \mid x_{\setminus M})$.
2. **GPT (Decoder-only)**:
- Mặt nạ chú ý: Tam giác dưới (Autoregressive Causal Mask):
$$M_{ij} = \begin{cases} 0 & \text{khi } j \le i \\ -\infty & \text{khi } j > i \end{cases}$$
Đảm bảo $\text{Softmax}(QK^T + M)$ có xác suất chú ý về tương lai bằng 0 tuyệt đối.
- Mục tiêu huấn luyện: Dự đoán token kế tiếp: $\mathcal{L}_{CLM} = -\sum_{t=1}^T \ln P(x_t \mid x_{<t})$.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy lộn ngược tên: Hãy nhớ: BERT = Bidirectional Encoder Representations from Transformers (2 chiều). GPT = Generative Pre-trained Transformer (Tự hồi quy 1 chiều).

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.6 So sánh BERT vs GPT**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-C30: OLP01-C30 ứng dụng BERT (Encoder-only) cho phân loại và GPT (Decoder-only) cho sinh văn bản, còn M56 đi sâu vào bản chất kiến trúc chú ý 2 chiều vs 1 chiều và mục tiêu tiền huấn luyện của chúng.

---

### Câu 57 [VOAI02-M57] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong đánh giá dịch máy (Bài toán Dịch Hoa - Việt đề thi OLP AI 2025), công thức SacreBLEU kết hợp hệ số phạt độ ngắn: $\text{BP} = \exp\left(\min\left(0, 1 - \frac{r}{c}\right)\right)$, trong đó $c$ là tổng độ dài bản dịch máy và $r$ là tổng độ dài bản dịch tham chiếu. Nếu mô hình dịch máy dịch một câu rất ngắn chỉ gồm 2 từ đúng hoàn toàn nhưng câu tham chiếu dài 10 từ ($c = 2, r = 10$), hệ số BP sẽ phạt điểm số như thế nào?

- **A.** $BP = 1.0000$ (hoàn toàn không bị phạt do toàn bộ các từ được sinh ra đều khớp chính xác với bản dịch tham chiếu)
- **B.** $BP = \exp(1 - 10/2) = \exp(-4) \approx 0.0183$ (phạt cực nặng do câu dịch quá ngắn so với câu tham chiếu)
- **C.** $BP = 0.0000$ (bị loại bỏ hoàn toàn điểm số do độ dài câu dịch nhỏ hơn ngưỡng tối thiểu 3 từ theo chuẩn SacreBLEU)
- **D.** $BP = \frac{10}{2} = 5.0000$ (được nhân thưởng điểm số do câu dịch ngắn gọn và súc tích hơn bản dịch chuẩn)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **SacreBLEU:** Bản chuẩn hóa của độ đo BLEU với tokenization cố định, tránh sai lệch điểm số giữa các cách tiền xử lý khác nhau.
- **Brevity Penalty (BP):** Hệ số phạt độ ngắn: $\text{BP} = \exp\left(\min\left(0, 1 - \frac{r}{c}\right)\right)$ với $c$ là độ dài bản dịch máy và $r$ là độ dài bản dịch tham chiếu.
- **Tính toán:** Với $c = 2$ và $r = 10$: $1 - \frac{r}{c} = 1 - 5 = -4 \implies \text{BP} = \exp(-4) \approx 0.0183$. Toàn bộ điểm số BLEU bị nhân với $0.0183$ (phạt gần như triệt tiêu về 0).

🍼 **Hình dung thực tế cho em bé:**
Nếu không có Brevity Penalty, một mô hình lươn lẹo chỉ cần dịch đúng vỏn vẹn 1 từ ' Tôi ' thì độ chính xác n-gram vẫn là 100%! Để trừng phạt chiêu trò gian lận dịch cộc lốc này, hệ số BP sẽ hạ điểm theo cấp số nhân nếu câu dịch của bạn ngắn hơn câu chuẩn (c < r). Khi c = 2 mà chuẩn r = 10, BP = exp(1 - 5) = exp(-4) ≈ 0.018, biến điểm số từ 100 điểm tụt xuống chỉ còn chưa đầy 2 điểm!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích công thức Brevity Penalty (BP):
$$\text{BP} = \begin{cases} 1 & \text{nếu } c > r \\ \exp\left(1 - \frac{r}{c}\right) & \text{nếu } c \le r \end{cases}$$
Thay số: $c = 2$, $r = 10$. Vì $c \le r$:
$$\text{BP} = \exp\left(1 - \frac{10}{2}\right) = \exp(1 - 5) = \exp(-4) = \frac{1}{e^4} \approx \frac{1}{54.598} \approx 0.0183156$$
Điểm SacreBLEU bị nhân trực tiếp với $\text{BP}$:
$$\text{SacreBLEU} = \text{BP} \times \exp\left(\sum_{n=1}^4 w_n \ln p_n\right)$$
Do đó điểm số bị sụt giảm hơn $98\%$.
Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy chiến lược phòng thi NMT: Khi làm bài dịch máy OLP AI, nếu dùng Beam Search mà đặt chiều dài quá ngắn hoặc thiếu Length Penalty, mô hình sẽ có xu hướng sinh câu kết thúc sớm $\to c < r \to$ Điểm SacreBLEU bị sập thảm hại do BP. Luôn tinh chỉnh Length Penalty $\alpha \approx 0.6$ đến $0.8$ trong Beam Search để cân bằng độ dài $c \approx r$!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.7 Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu OLP01-E02: M57 kiểm tra công thức tính hệ số phạt độ ngắn Brevity Penalty của độ đo SacreBLEU, là metric cốt lõi đánh giá chất lượng mô hình trong bài tự luận Dịch máy OLP01-E02.

---

### Câu 58 [VOAI02-M58] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khác biệt cốt lõi về triết lý đo lường giữa chỉ số **BLEU** và chỉ số **ROUGE** trong xử lý ngôn ngữ tự nhiên là gì?

- **A.** BLEU chỉ dùng cho ngữ liệu tiếng Anh (English Only); ROUGE dùng cho các ngôn ngữ đơn lập như tiếng Việt (Vietnamese Only)
- **B.** BLEU dựa trên khoảng cách chỉnh sửa (Edit Distance); ROUGE dựa trên độ tương đồng góc Cosine (Cosine Similarity)
- **C.** BLEU thiên về Precision (đo độ chính xác n-gram sinh ra); ROUGE thiên về Recall (đo độ bao phủ n-gram của bản chuẩn)
- **D.** ROUGE không thể tính toán được cho n-gram lớn hơn 1 (Unigram Only) mà chỉ đếm số lượng từ đơn lẻ trùng lặp

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **BLEU (Bilingual Evaluation Understudy):** Đo lường độ chuẩn xác (Precision-oriented), tính tỉ lệ các n-gram trong câu dịch máy xuất hiện trong câu tham chiếu.
- **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** Đo lường độ bao phủ (Recall-oriented), tính tỉ lệ các n-gram trong câu tham chiếu được mô hình khôi phục lại trong bản tóm tắt.
- **Ứng dụng chuẩn mực:** BLEU là thước đo mặc định cho bài toán Dịch máy (Machine Translation); ROUGE là thước đo mặc định cho bài toán Tóm tắt văn bản (Text Summarization).

🍼 **Hình dung thực tế cho em bé:**
Dịch máy (BLEU) coi trọng Precision: bạn nói ra câu gì thì câu đó phải chuẩn xác từng chữ, không được bịa đặt. Tóm tắt văn bản (ROUGE) coi trọng Recall: bạn phải tóm tắt bao quát được hết các ý chính trong bài viết gốc, không được bỏ sót thông tin quan trọng của người ta!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **BLEU (Bilingual Evaluation Understudy)**:
$$p_n = \frac{\sum_{\text{ngram} \in \text{Hyp}} \text{Count}_{clip}(\text{ngram})}{\sum_{\text{ngram} \in \text{Hyp}} \text{Count}(\text{ngram})} \quad (\text{Precision: Mẫu số là độ dài bản sinh})$$
2. **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**:
$$\text{ROUGE-N} = \frac{\sum_{\text{ngram} \in \text{Ref}} \text{Count}_{match}(\text{ngram})}{\sum_{\text{ngram} \in \text{Ref}} \text{Count}(\text{ngram})} \quad (\text{Recall: Mẫu số là độ dài bản tham chiếu})$$
ROUGE-L sử dụng dãy con chung dài nhất (Longest Common Subsequence - LCS) để đánh giá độ trôi chảy cấu trúc cấp độ câu mà không đòi hỏi các từ phải đứng sát cạnh nhau liên tiếp.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy chữ cái đầu: Nhớ ngay tên viết tắt của ROUGE: ' Recall-Oriented Understudy...'. Chữ R đầu tiên là viết tắt của RECALL!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.7 Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity**.
🔗 **Mắt xích & Liên hệ bài học:** Câu hỏi độc lập làm rõ sự khác biệt triết lý giữa BLEU (hướng tới Precision cho dịch máy) và ROUGE (hướng tới Recall cho tóm tắt văn bản) (§4.7).

---

### Câu 59 [VOAI02-M59] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong một hệ thống RAG doanh nghiệp hiện đại, pipeline truy xuất kết hợp 2 giai đoạn (Two-Stage Retrieval) thường bao gồm:

- **A.** Giai đoạn 1 (Brute-force LLM): Dùng mô hình 70B đọc triệu văn bản; Giai đoạn 2 (Regex Filter): Lọc kết quả bằng biểu thức chính quy
- **B.** Giai đoạn 1 (Machine Translation): Dịch toàn bộ văn bản sang tiếng Anh; Giai đoạn 2 (Post-Editing): Dịch ngược lại tiếng Việt
- **C.** Giai đoạn 1 (Bi-Encoder / Dense & Sparse): tìm nhanh top 100 tài liệu; Giai đoạn 2 (Cross-Encoder): xếp hạng sâu chọn top 5 cho LLM
- **D.** Giai đoạn 1 (Hash Matching): Dùng hàm băm MD5 ánh xạ tài liệu; Giai đoạn 2 (Exact Lookup): Tra cứu bảng tĩnh cố định

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **RAG (Retrieval-Augmented Generation):** Kiến trúc kết hợp truy xuất tri thức bên ngoài để tăng cường ngữ cảnh cho mô hình ngôn ngữ lớn.
- **Giai đoạn 1 (Fast Dense/Sparse Retrieval):** Sử dụng Bi-Encoder (như BGE, Contriever) hoặc Hybrid BM25 để truy xuất nhanh top 50-100 tài liệu ứng viên từ hàng triệu văn bản.
- **Giai đoạn 2 (Cross-Encoder Re-ranking):** Sử dụng Cross-Encoder (như BGE-Reranker, Cohere Rerank) tính toán attention chéo giữa câu hỏi và từng đoạn văn để xếp hạng lại cực kỳ chính xác top 3-5 tài liệu đưa vào prompt LLM.

🍼 **Hình dung thực tế cho em bé:**
Tìm kiếm trong kho sách 1 triệu cuốn giống như tuyển sinh đại học: Vòng sơ tuyển (Giai đoạn 1 - Bi-Encoder + BM25) quét nhanh học bạ để lọc ra 100 hồ sơ sáng giá nhất trong 1 giây. Vòng phỏng vấn chuyên sâu (Giai đoạn 2 - Cross-Encoder Reranker) cho ban giám khảo ngồi đối thoại trực tiếp từng người một với câu hỏi để chọn ra đúng 5 thủ khoa xuất sắc nhất đem nộp cho sếp (LLM) trả lời!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **Stage 1: Bi-Encoder (Dense + Sparse Hybrid)**:
- Tính vector độc lập: $v_q = E(q)$, $v_d = E(d)$. Lưu trước vector của toàn bộ kho dữ liệu vào Vector DB.
- Lúc truy vấn: Tìm kiếm láng giềng gần nhất (HNSW / ScaNN / FAISS) với cosine similarity $v_q \cdot v_d$ kết hợp điểm BM25 (sparse keyword) trong $O(\log N)$. Tốc độ cực nhanh (Latency < 10ms cho hàng triệu tài liệu) nhưng biểu diễn tương tác từ chéo giữa $q$ và $d$ bị nén độc lập.
2. **Stage 2: Cross-Encoder Reranker**:
- Nạp đồng thời cặp câu vào chung một Transformer: $[CLS] \; q \; [SEP] \; d$.
- Cơ chế Full Self-Attention cho phép MỌI từ trong câu hỏi $q$ tương tác trực tiếp với MỌI từ trong đoạn văn $d$ tại tất cả các lớp $\implies$ Độ chính xác ngữ nghĩa vượt trội so với Bi-Encoder, lọc sạch tài liệu rác trước khi đưa vào context window của LLM.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Bẫy hiệu năng: Tại sao không dùng luôn Cross-Encoder cho 1 triệu tài liệu từ đầu? Vì Cross-Encoder không thể tính trước vector (pre-compute embeddings). Nếu có 1 triệu tài liệu, phải chạy mô hình Transformer 1 triệu lần cho MỖI câu hỏi $\implies$ Mất hàng giờ cho 1 lượt tìm kiếm!

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cosine Similarity**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M23: VOAI03-M23 nêu vai trò cốt lõi của RAG trong việc giảm ảo giác và cập nhật tri thức cho LLM, còn M59 phân tích kiến trúc truy xuất 2 giai đoạn (Bi-Encoder kết hợp Cross-Encoder Re-ranker) trong hệ thống RAG doanh nghiệp thực tế.

---

### Câu 60 [VOAI02-M60] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong quá trình sinh văn bản tự hồi quy (Autoregressive Generation) của các mô hình LLM (như GPT-4, LLaMA, DeepSeek), kỹ thuật **KV Caching** giúp giảm độ phức tạp tính toán của mỗi bước sinh token mới từ mức nào xuống mức nào?

- **A.** Tăng tốc độ đọc ghi dữ liệu tuần tự từ ổ cứng SSD NVMe vào bộ nhớ RAM của hệ thống máy chủ phục vụ mô hình
- **B.** Giảm dung lượng bộ nhớ VRAM tiêu tốn của toàn bộ mạng về 0 bằng cách xóa các vector trạng thái sau mỗi bước sinh
- **C.** Từ $O(N)$ xuống $O(1)$ cho bước chiếu Key/Value quá khứ, đưa độ phức tạp sinh 1 token mới về $O(N)$ thay vì $O(N^2)$
- **D.** Từ $O(N^2)$ xuống $O(1)$ đối với toàn bộ các phép nhân ma trận Feed-Forward Network trong các khối Transformer

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Autoregressive Generation:** Mỗi bước suy luận, mô hình LLM sinh ra đúng 1 token mới và nối vào chuỗi đầu vào để dự đoán token tiếp theo.
- **Không có KV Cache:** Tại bước $T$, mô hình phải tính lại toàn bộ ma trận Key và Value cho tất cả $T$ token từ đầu $\implies$ Độ phức tạp mỗi bước là $O(T)$ và toàn bộ quá trình sinh là $O(T^2)$.
- **Có KV Cache:** Lưu trữ các tensor Key và Value đã tính ở các bước trước trong GPU VRAM; mỗi bước chỉ cần chiếu duy nhất token mới $\implies$ Độ phức tạp mỗi bước giảm xuống $O(1)$ phép chiếu vector.

🍼 **Hình dung thực tế cho em bé:**
Mỗi khi bạn viết thêm một từ mới vào bài văn: nếu không có trí nhớ (không có KV Cache), bạn phải đọc lại từ đầu bài văn và tính toán lại toàn bộ cảm xúc của từng từ từ trước đến nay (tốn N bước tính mỗi lần, cả bài văn tốn N² bước tính). Có KV Cache giống như việc bạn ghi nhớ sẵn kết quả của các từ cũ vào một cuốn sổ tay; khi viết từ mới, bạn chỉ cần tính cho duy nhất từ mới đó và tra cứu sổ tay! Bạn không bao giờ phải tính lại từ cũ nữa!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. **Không có KV Cache**:
Tại bước sinh token thứ $t+1$, mô hình nhận toàn bộ chuỗi $x_{1:t+1}$.
Phải tính lại phép chiếu $Q, K, V = X W_Q, X W_K, X W_V$ cho TẤT CẢ $t+1$ token từ đầu $\implies$ Tốn $O((t+1) d^2)$. Để sinh $N$ token, tổng chi phí là:
$$\sum_{t=1}^N O(t) = O(N^2)$$
2. **Có KV Cache**:
Các tensor $K_{1:t}$ và $V_{1:t}$ của các token quá khứ được lưu sẵn trong VRAM.
Tại bước $t+1$, mô hình CHỈ CẦN tính cho token mới nhất:
$$q_{t+1} = x_{t+1} W_Q, \quad k_{t+1} = x_{t+1} W_K, \quad v_{t+1} = x_{t+1} W_V$$
Nối thêm vào cache: $K_{new} = [K_{past}, k_{t+1}]$, $V_{new} = [V_{past}, v_{t+1}]$.
Phép chú ý chỉ cần tính $q_{t+1} K_{new}^T$ tốn $O(t \cdot d)$ thay vì tính lại toàn bộ ma trận $(t+1) \times (t+1)$. Tổng độ phức tạp sinh $N$ token giảm từ $O(N^3)$ xuống $O(N^2)$, và chi phí mỗi bước sinh chuyển từ việc tính toán lại $O(N)$ sang tái sử dụng trong $O(1)$ phép chiếu.
Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
Sự đánh đổi của KV Cache (Trade-off): KV Cache đánh đổi BỘ NHỚ VRAM để lấy TỐC ĐỘ. Khi context length dài (32k hay 128k token), KV Cache chiếm hàng chục Gigabyte VRAM, dẫn đến sự ra đời của các kỹ thuật như PagedAttention (vLLM) và FlashAttention.

### 4. Mắt xích kiến thức & Liên hệ bài học
📚 **Căn cứ lý thuyết:** Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.
🔗 **Mắt xích & Liên hệ bài học:** Liên hệ câu VOAI03-M30: Cùng kiểm tra cơ chế KV Cache trong phục vụ mô hình ngôn ngữ lớn: VOAI03-M30 nêu định nghĩa kỹ thuật, còn M60 phân tích mức độ tối ưu hóa độ phức tạp tính toán của từng bước sinh token tự hồi quy.

---

### Câu 61 [VOAI02-E01] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [CASE STUDY 1 - SIGN LANGUAGE RECOGNITION] Trong bài toán nhận diện ngôn ngữ ký hiệu video tiếng Việt (chuỗi video liên tục chứa cử chỉ bàn tay và nét mặt), nhóm kỹ sư cần lựa chọn kiến trúc trích xuất đặc trưng không gian - thời gian tối ưu giữa Conv3D thuần túy, 2D-CNN + BiLSTM, và Pipeline kết hợp MediaPipe Keypoints + Graph Convolutional Network (GCN). Nhận định nào sau đây là chính xác nhất về sự đánh đổi (trade-off) giữa các giải pháp?

- **A.** Conv3D thuần túy có chi phí bộ nhớ VRAM nhẹ nhất và phù hợp nhất để triển khai trên các thiết bị di động biên
- **B.** MediaPipe Keypoints + GCN giảm mạnh chiều dữ liệu, loại bỏ nhiễu hậu cảnh nhưng phụ thuộc nặng vào độ chính xác trích khớp
- **C.** 2D-CNN + BiLSTM hoàn toàn miễn nhiễm với hiện tượng mất thông tin ngữ cảnh thời gian dài khi độ dài video vượt quá 1000 frame
- **D.** Mô hình dựa trên điểm ảnh thô (RGB frames) luôn tổng quát hóa tốt hơn mô hình dựa trên khung xương khi thay đổi trang phục người

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nhìn cả bức ảnh video (pixel) tốn rất nhiều RAM và dễ bị phân tâm bởi hình nền/áo quần. Rút trích khung xương (21 khớp ngón tay qua MediaPipe) rồi đưa vào GCN giúp mô hình siêu nhẹ và nhanh. Tuy nhiên, nếu tay bị che khuất làm MediaPipe bốc trúng khớp sai, GCN phía sau sẽ bị hỏng theo.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Spatial-Temporal GCN (ST-GCN) biểu diễn đồ thị khớp $G = (V, E)$. Chi phí tính toán giảm từ $O(T \cdot H \cdot W \cdot C)$ xuống $O(T \cdot |V| \cdot C_{\text{joint}})$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Conv3D cực kỳ nặng VRAM (loại A), BiLSTM vẫn bị nghẽn thông tin chuỗi rất dài (loại C), RGB thô dễ bị overfit vào nền và trang phục (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 62 [VOAI02-E02] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [CASE STUDY 2 - LOW-RESOURCE NMT] Bạn cần xây dựng hệ thống Dịch Máy Nơ-ron (NMT) cho cặp ngôn ngữ hiếm tài nguyên từ tập dữ liệu song ngữ nhỏ (ví dụ chỉ có 50.000 cặp câu). Kỹ thuật nào sau đây mang lại bước nhảy vọt lớn nhất về điểm BLEU bằng cách tận dụng hiệu quả kho ngữ liệu đơn ngữ (Monolingual Data) dồi dào?

- **A.** Tăng kích thước từ điển (Vocab Expansion) lên 250.000 token để chứa trọn vẹn mọi biến thể hình thái từ ghép trong văn bản
- **B.** Giảm độ sâu mô hình (Model Pruning) xuống còn 1 tầng Encoder và 1 tầng Decoder để triệt tiêu hoàn toàn hiện tượng quá khớp
- **C.** Dịch ngược (Back-Translation): dùng mô hình sơ khởi dịch đơn ngữ đích sang nguồn tạo dữ liệu song ngữ tổng hợp
- **D.** Khởi tạo trọng số ngẫu nhiên (Uniform Initialization) trên đoạn [-10, +10] nhằm mở rộng không gian tìm kiếm gradient

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ít dữ liệu song ngữ thì không thể dịch giỏi. Nhưng ta có hàng triệu câu tiếng Việt một mình (đơn ngữ đích). Lấy mô hình tạm thời dịch ngược tiếng Việt sang ngôn ngữ nguồn, ta tạo ra hàng triệu cặp câu nhân tạo (nguồn tổng hợp - đích chuẩn). Dạy mạng trên dữ liệu này giúp cải thiện BLEU cực kỳ ngoạn mục!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Back-Translation (Sennrich et al.): tạo tập dữ liệu song ngữ bổ sung $\mathcal{D}_{\text{pseudo}} = \{(\hat{x}, y) \mid \hat{x} = M_{Y \to X}(y), y \in \mathcal{D}_{Y}\}$, sau đó huấn luyện mô hình $M_{X \to Y}$ trên $\mathcal{D}_{\text{true}} \cup \mathcal{D}_{\text{pseudo}}$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Tăng BPE lên 250k với dữ liệu nhỏ làm ma trận embedding quá thưa thớt (overfitting trầm trọng, loại A); phân phối khởi tạo $[-10, 10]$ làm nổ gradient ngay lập tức (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 63 [VOAI02-E03] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [CASE STUDY 3 - DOCUMENT VQA & TABLE EXTRACTION] Khi xây dựng hệ thống hỏi đáp trên tài liệu biểu mẫu và trích xuất bảng biểu từ ảnh scan hóa đơn mờ nhòe, giải pháp kết hợp đa phương thức LayoutLM (kết hợp đồng thời văn bản OCR, tọa độ 2D Bounding Box và hình ảnh trực quan) vượt trội hơn phương pháp NLP thuần văn bản (như BERT thuần) ở điểm then chốt nào?

- **A.** LayoutLM hoàn toàn không cần module OCR (Optical Recognition) mà đọc trực tiếp chuỗi ký tự từ mảng điểm ảnh RGB thô
- **B.** Mã hóa không gian 2D (Spatial Coordinates) giúp hiểu quan hệ căn hàng, cột và cặp Khóa - Giá trị (Key-Value) theo hình học trang
- **C.** LayoutLM thay thế phép nhân ma trận tự chú ý (Attention Replacement) bằng phép lọc trung vị phi tuyến tính 2D trên trang
- **D.** Tốc độ xử lý của LayoutLM (Inference Speedup) nhanh hơn BERT 100 lần nhờ loại bỏ hoàn toàn ma trận vector nhúng từ vựng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong hóa đơn, ' Tổng tiền:' và con số '500.000đ ' nằm ở hai vị trí thẳng hàng nhau trên trang. BERT thường chỉ nhìn dòng chữ phẳng một chiều từ trái sang phải nên không hiểu bảng biểu. LayoutLM nạp thêm tọa độ $(x_0, y_0, x_1, y_1)$ của từng chữ, giúp mạng ' nhìn ' thấy ô nào nằm chung cột, ô nào là tiêu đề của ô nào.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 LayoutLM biểu diễn embedding vị trí 2D: $e_{\text{pos}} = [E_x(x_0), E_y(y_0), E_x(x_1), E_y(y_1)]$, kết hợp với text embedding và visual embedding qua cộng vector. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** LayoutLM vẫn cần OCR (loại A) và vẫn dùng Self-Attention chuẩn (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 64 [VOAI02-E04] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [CASE STUDY 4 - DEEPFAKE DETECTION] Trong bài toán phát hiện khuôn mặt giả mạo DeepFake (Face Swap / GAN-generated), các mô hình phân loại trên miền không gian pixel thường thất bại khi ảnh bị nén JPEG mạnh hoặc đưa qua mạng xã hội. Phương pháp phân tích trên miền tần số (Frequency Domain Analysis, ví dụ 2D-FFT hoặc DCT) mang lại căn cứ khoa học vững chắc nào để phát hiện vết tích giả mạo?

- **A.** Tần số cao của ảnh nén JPEG (High Frequencies) luôn bị triệt tiêu hoàn toàn về 0 trên toàn bộ phổ công suất biến đổi
- **B.** Thuật toán biến đổi Fourier (Fourier Transform) loại bỏ hoàn toàn nhu cầu dán nhãn dữ liệu khi huấn luyện mạng nơ-ron
- **C.** Phép nội suy upsampling của GAN/Diffusion để lại các đỉnh phổ chu kỳ bất thường (Spectral Artifacts) trên phổ Fourier
- **D.** Miền tần số làm giảm kích thước ma trận ảnh (Dimensionality Reduction) từ hàng triệu pixel xuống chỉ còn 4 hệ số cơ sở

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi mắt người nhìn ảnh DeepFake thấy da mặt rất mịn, nhưng thực chất thuật toán sinh ảnh (GAN/Diffusion) dùng các bước phóng to ảnh (Transposed Conv / Bilinear Upsampling) lặp đi lặp lại. Phép nhân ô lưới này để lại các hoa văn chu kỳ siêu nhỏ. Khi chiếu qua lăng kính Fourier (FFT), các hoa văn này lộ rõ thành các đốm sáng chu kỳ bất thường!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phép upsampling định kỳ tạo ra hiện tượng folding/aliasing trong miền tần số: $\mathcal{F}\{f(x/M)\} = M \mathcal{F}\{f\}(M \omega)$. Đỉnh phổ công suất chu kỳ xuất hiện rõ rệt tại các tần số con. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** JPEG nén giảm tần số cao chứ không triệt tiêu về 0 tuyệt đối (loại A), và Fourier bảo toàn kích thước phổ chứ không thu về 4 hệ số (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 65 [VOAI02-E05] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [CASE STUDY 5 - EXTREME IMBALANCED DATA] Trong quy trình thẩm định mô hình phát hiện bệnh hiểm nghèo với dữ liệu bảng cực kỳ mất cân bằng (chỉ 50 ca dương tính trên 100.000 bản ghi), nhóm nghiên cứu áp dụng kỹ thuật sinh mẫu tổng hợp SMOTE kết hợp Cross-Validation 5-Fold. Sai lầm phương pháp luận nghiêm trọng nào sẽ dẫn đến hiện tượng rò rỉ dữ liệu (Data Leakage) và điểm kiểm thử ảo?

- **A.** Thực hiện biến đổi Min-Max Scaling (Independent Scaling) độc lập trên từng fold kiểm thử của tập validation
- **B.** Áp dụng SMOTE trên toàn bộ tập dữ liệu (Global Oversampling) TRƯỚC KHI chia fold, gây rò rỉ dữ liệu (Data Leakage)
- **C.** Sử dụng độ đo PR-AUC (Precision-Recall Metric) thay cho ROC-AUC để đánh giá hiệu năng phân loại lớp thiểu số
- **D.** Cố định seed ngẫu nhiên (Random Seed Fixing) của thuật toán LightGBM để đảm bảo tính tái lập kết quả thí nghiệm

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu bạn chạy SMOTE trước khi chia tập, các điểm nhân tạo mới sẽ được sinh ra từ việc ' nối dây ' giữa điểm của tập Train và điểm của tập Val. Khi chia ra, tập Train chứa anh em sinh đôi của tập Val, khiến mô hình ' nhìn trộm bài kiểm tra '. Phải chia Fold trước, fold Train mới được dùng SMOTE!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Data Leakage xảy ra khi $x_{\text{syn}} = x_i + \lambda (x_j - x_i)$ với $x_i \in \mathcal{D}_{\text{train}}$ và $x_j \in \mathcal{D}_{\text{val}}$. SMOTE bắt buộc phải nằm bên trong `imblearn.pipeline. Pipeline` của từng fold huấn luyện. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án C là thực hành chuẩn xác (PR-AUC tốt hơn ROC-AUC khi mất cân bằng nặng); cố định seed (D) là nguyên tắc tái lập cơ bản.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.7 Xử Lý Dữ Liệu Mất Cân Bằng (Imbalanced Data)**.

---

### Câu 66 [VOAI02-E06] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [CASE STUDY 6 - ENTERPRISE RAG & LLM SERVING] Khi triển khai mô hình ngôn ngữ lớn (ví dụ Llama-3-70B) phục vụ hệ thống Enterprise RAG với hàng trăm yêu cầu đồng thời, hiện tượng nghẽn cổ chai bộ nhớ VRAM lớn nhất khi sinh token chuỗi dài (Long Context KV Cache) được giải quyết hiệu quả nhất bằng kỹ thuật quản lý bộ nhớ nào trong hệ thống vLLM?

- **A.** Ép toàn bộ trọng số mô hình về độ chính xác 1-bit (Model Binarization) bằng kỹ thuật lượng tử hóa cực hạn không dấu
- **B.** Loại bỏ hoàn toàn các vector Value (Value Dropping) và chỉ lưu trữ các vector Key trong bộ nhớ đệm chú ý của ngữ cảnh
- **C.** PagedAttention: quản lý bộ nhớ đệm KV Cache theo các trang (Pages) bộ nhớ phân mảnh linh hoạt như bộ nhớ ảo hệ điều hành
- **D.** Khởi động lại toàn bộ tiến trình suy luận (Inference Reset) từ đầu cho mỗi token mới được sinh ra để giải phóng bộ nhớ

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi phục vụ nhiều người dùng cùng lúc, độ dài câu trả lời thay đổi liên tục. Nếu cấp phát sẵn một vùng nhớ RAM liền tù tì khổng lồ cho mỗi người (như cách truyền thống), bộ nhớ VRAM sẽ bị phân mảnh và lãng phí 60-80%. PagedAttention cắt KV cache thành các ' trang nhỏ ' (pages) rời rạc như RAM máy tính, giúp nhồi thêm gấp 2-4 lần người dùng vào cùng 1 card đồ họa!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 PagedAttention (Kwon et al., SOSP 2023) quản lý bảng trang logic sang vật lý, giảm tỷ lệ lãng phí bộ nhớ KV Cache từ $\approx 60-80\%$ xuống dưới $4\%$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Không thể bỏ vector Value (loại B) vì cần tính tổng trọng số; chạy lại từ đầu (loại D) có độ phức tạp thời gian $O(N^2)$ cực kỳ chậm chạp.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 67 [VOAI02-M67] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho bài toán tối ưu hóa có ràng buộc bất đẳng thức $\min_{x} f(x)$ thỏa mãn $g_i(x) \le 0$ ($i = 1, \dots, m$). Điều kiện bù trùng (Complementary Slackness) trong hệ điều kiện Karush-Kuhn-Tucker (KKT) yêu cầu phát biểu toán học nào đối với nhân tử Lagrange $\lambda_i$?

- **A.** $\lambda_i + g_i(x) = 0$ với mọi chỉ số $i \in \{1, \dots, m\}$ nhằm cân bằng sai phân bậc nhất trong không gian đối ngẫu
- **B.** $\lambda_i g_i(x) = 0$ và $\lambda_i \ge 0$ với mọi $i$, tức nếu $g_i(x) < 0$ (ràng buộc không kích hoạt) thì bắt buộc $\lambda_i = 0$
- **C.** $\lambda_i / g_i(x) = 1$ trên toàn bộ miền nghiệm chấp nhận được của bài toán tối ưu hóa lồi có điều kiện biên
- **D.** $\sum_{i=1}^m \lambda_i = 1$ theo tính chất chuẩn hóa của phân phối xác suất tiên nghiệm của các nhân tử Lagrange

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Điều kiện bù trừ KKT nói rằng: Nếu điểm nghiệm nằm lọt thỏm bên trong ranh giới an toàn ($g_i(x) < 0$), bức tường ranh giới không tạo ra lực cản nào cả, nên nhân tử Lagrange $\lambda_i$ bằng đúng 0. Chỉ khi nào nghiệm chạm sát vào bức tường ($g_i(x) = 0$) thì $\lambda_i$ mới có thể lớn hơn 0!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 KKT Complementary Slackness: $\lambda_i g_i(x^*) = 0$ với $\lambda_i \ge 0, g_i(x^*) \le 0$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A nhầm phép nhân bằng 0 với phép cộng bằng 0.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 Cơ Sở Tối Ưu Hóa & Gradient Descent**.

---

### Câu 68 [VOAI02-M68] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong lý thuyết tối ưu hóa lồi, điều kiện đủ Slater (Slater ' s Condition) đảm bảo khoảng cách đối ngẫu bằng 0 (Strong Duality: giá trị tối ưu của bài toán gốc bằng bài toán đối ngẫu $p^* = d^*$) đòi hỏi điều kiện nào?

- **A.** Hàm mục tiêu phải có ma trận Hessian (Strict Convexity) là ma trận đường chéo với các phần tử strictly dương toàn cục
- **B.** Tồn tại ít nhất một điểm khả thi ngặt $x$ (Strict Feasibility) thỏa mãn nghiêm ngặt tất cả các ràng buộc $g_i(x) < 0$
- **C.** Tất cả các nhân tử Lagrange (Positive Multipliers) tương ứng với các ràng buộc bất đẳng thức đều lớn hơn 10
- **D.** Không gian biến số bài toán (Bounded Domain) phải bị chặn hoàn toàn trong một quả cầu Euclid đóng có bán kính hữu hạn

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Điều kiện Slater chỉ đơn giản là: Vùng hợp lệ của bài toán phải có ' ruột ' (nội hàm dày dặn), tức là tìm được ít nhất một điểm nằm sâu bên trong ranh giới mà không chạm mép ($g_i(x) < 0$). Khi đó, giải bài toán đối ngẫu (Dual) sẽ cho ra đáp số chính xác bằng bài toán gốc (Primal).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\exists x \in \text{relint}(\mathcal{D}): g_i(x) < 0, \forall i \implies p^* = d^*$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Slater là điều kiện tồn tại điểm trong khả thi ngặt, không ép buộc cấu trúc Hessian (loại A) hay nhân tử nguyên (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 Cơ Sở Tối Ưu Hóa & Gradient Descent**.

---

### Câu 69 [VOAI02-M69] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Khi so sánh tốc độ hội tụ gần điểm cực tiểu địa phương giữa phương pháp Newton-Raphson (bậc hai) và Gradient Descent (bậc một), phát biểu nào sau đây phản ánh chính xác nhất bản chất tiệm cận toán học?

- **A.** Gradient Descent hội tụ theo cấp số nhân bậc ba trong khi Newton-Raphson chỉ hội tụ dưới tuyến tính
- **B.** Newton-Raphson hội tụ bậc hai (Quadratic Convergence) với sai số $\|e_{k+1}\| \le M \|e_k\|^2$, nhanh hơn hẳn tốc độ tuyến tính của GD
- **C.** Cả hai phương pháp đều có cùng tốc độ hội tụ tiệm cận $O(1/\sqrt{k})$ bất kể độ cong của hàm mục tiêu
- **D.** Newton-Raphson có chi phí tính toán cho mỗi bước lặp thấp hơn Gradient Descent trên không gian nhiều chiều

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Gradient Descent chỉ biết hướng dốc nên mỗi bước giảm sai số theo tỉ lệ cố định (tuyến tính: 0.1, 0.01, 0.001...). Newton-Raphson dùng cả độ cong (ma trận Hessian) nên khi đã vào gần đáy, sai số bình phương lên: $10^{-2} \to 10^{-4} \to 10^{-8}$ (hội tụ bậc hai, siêu tốc)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Gần nghiệm tối ưu: $\|w_{k+1} - w^*\| \le C \|w_k - w^*\|^2$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án D sai vì Newton phải tính nghịch đảo ma trận Hessian $O(d^3)$, đắt hơn rất nhiều so với GD $O(d)$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 Cơ Sở Tối Ưu Hóa & Gradient Descent**.

---

### Câu 70 [VOAI02-M70] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Phép phân rã Cholesky phân tích một ma trận đối xứng xác định dương $\Sigma \in \mathbb{R}^{n \times n}$ thành dạng nào sau đây và thường được sử dụng trong tác vụ nào của Machine Learning?

- **A.** Thành tích hai ma trận trực giao $\Sigma = Q_1 Q_2$ nhằm nén kích thước lưu trữ tensor trên các thiết bị phần cứng di động
- **B.** Thành tích $\Sigma = L L^T$ với $L$ là ma trận tam giác dưới, ứng dụng hiệu quả để lấy mẫu từ phân phối chuẩn đa biến
- **C.** Thành tổng của ba ma trận phản đối xứng nhằm giải hệ phương trình vi phân đạo hàm riêng trong các mô hình vật lý
- **D.** Thành ma trận đường chéo thuần túy bằng cách gán toàn bộ các phần tử ngoài đường chéo chính bằng đúng số 0

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Phân rã Cholesky giống như ' rút căn bậc hai ' của một ma trận: $\Sigma = L L^T$ với $L$ là ma trận tam giác dưới. Khi muốn sinh điểm ngẫu nhiên từ phân phối chuẩn đa biến, chỉ cần bốc vector ngẫu nhiên độc lập $z \sim \mathcal{N}(0, I)$ rồi nhân $x = \mu + L z$ là xong ngay!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\text{Cov}(L z) = L \text{Cov}(z) L^T = L I L^T = L L^T = \Sigma$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Cholesky phân tích thành tam giác dưới nhân chuyển vị của nó ($L L^T$), không phải hai ma trận trực giao (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.2 Các Phân Phối Xác Suất Thông Dụng**.

---

### Câu 71 [VOAI02-M71] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho hai ma trận $A \in \mathbb{R}^{m \times n}$ và $B \in \mathbb{R}^{n \times m}$. Tính chất hoán vị vòng quanh của toán tử vết (Trace Cyclic Property) phát biểu đẳng thức nào sau đây?

- **A.** $\text{Tr}(AB) = \text{Tr}(A) \cdot \text{Tr}(B)$ bất kể kích thước và cấu trúc của hai ma trận trong không gian tuyến tính
- **B.** $\text{Tr}(AB) = \text{Tr}(BA)$ mặc dù ma trận $AB \in \mathbb{R}^{m \times m}$ và $BA \in \mathbb{R}^{n \times n}$ có thể khác kích thước
- **C.** $\text{Tr}(AB) = -\text{Tr}(BA)$ khi và chỉ khi một trong hai ma trận là ma trận phản đối xứng trên trường số thực
- **D.** $\text{Tr}(AB) = 0$ khi định thức của ma trận tích khác 0 và các giá trị riêng đều phân biệt trên trường số phức

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Một tính chất cực đẹp của Vết ma trận (tổng các số trên đường chéo): Dù $A$ cỡ $2 \times 100$ và $B$ cỡ $100 \times 2$, thì vết của ma trận $AB$ ($2 \times 2$) luôn luôn bằng đúng vết của ma trận $BA$ ($100 \times 100$)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\text{Tr}(AB) = \sum_{i=1}^m (AB)_{ii} = \sum_{i=1}^m \sum_{j=1}^n A_{ij} B_{ji} = \sum_{j=1}^n \sum_{i=1}^m B_{ji} A_{ij} = \text{Tr}(BA)$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A nhầm phép vết của tích với tích hai vết (sai hoàn toàn).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 Cơ Sở Tối Ưu Hóa & Gradient Descent**.

---

### Câu 72 [VOAI02-M72] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Số điều kiện (Condition Number) $\kappa(A) = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)}$ của ma trận hệ số trong bài toán giải hệ phương trình tuyến tính $Ax = b$ phản ánh điều gì về độ ổn định số trị (Numerical Stability)?

- **A.** Nếu $\kappa(A) \approx 1$, hệ phương trình là Ill-conditioned và rất dễ bị khuếch đại sai số làm tròn số thực
- **B.** Nếu $\kappa(A) \gg 1$ (rất lớn), ma trận gần suy biến (Ill-conditioned), một nhiễu cực nhỏ ở đầu vào $b$ có thể gây sai số khổng lồ ở nghiệm $x$
- **C.** Số điều kiện luôn luôn bằng định thức của ma trận chia cho bình phương vết của nó
- **D.** Số điều kiện không phụ thuộc vào các giá trị kỳ dị của ma trận mà chỉ phụ thuộc vào số chiều

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Số điều kiện đo mức độ ' nhạy cảm ' của ma trận. Nếu $\kappa(A)$ cực lớn (ví dụ $10^8$), ma trận giống như một chiếc bập bênh siêu chông chênh: chỉ cần một hạt bụi nhỏ (sai số làm tròn 0.00001) rơi vào vế phải $b$, nghiệm $x$ tính ra sẽ bị văng xa hàng triệu đơn vị!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\frac{\|\delta x\|}{\|x\|} \le \kappa(A) \frac{\|\delta b\|}{\|b\|}$. Khi $\kappa(A)$ lớn, sai số tương đối bị khuếch đại tối đa $\kappa(A)$ lần. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** $\kappa(A) \approx 1$ là Well-conditioned (cực kỳ ổn định), phương án A nói ngược.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 Cơ Sở Tối Ưu Hóa & Gradient Descent**.

---

### Câu 73 [VOAI02-M73] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong ước lượng tham số mô hình hồi quy tuyến tính, sự khác biệt toán học cốt lõi giữa Ước lượng Hợp lý Cực đại (MLE) và Ước lượng Hậu nghiệm Cực đại (MAP) khi giả định phân phối tiên nghiệm của trọng số là Gauss $\mathcal{N}(0, \sigma_w^2 I)$ là gì?

- **A.** MLE tương đương với hồi quy Lasso ($L_1$) trong khi MAP tương đương với hồi quy Elastic Net
- **B.** MAP tương đương với MLE cộng thêm số hạng điều hòa L2 Regularization (Ridge Regression), kéo trọng số về 0
- **C.** MLE hoàn toàn không sử dụng dữ liệu quan sát mà chỉ dựa vào kiến thức chuyên gia tiên nghiệm
- **D.** MAP luôn cho nghiệm trọng số thưa thớt tuyệt đối (nhiều hệ số bằng đúng 0) giống như hồi quy Lasso

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
MLE chỉ quan tâm dữ liệu nói gì (maximize likelihood). MAP kết hợp thêm niềm tin ban đầu (tiên nghiệm Prior). Nếu ta tin rằng trọng số tuân theo phân phối hình chuông Gauss quanh số 0, phép tính log-posterior sẽ tự nhiên sinh ra số hạng phạt $-\lambda \|w\|^2$. Đó chính là hồi quy Ridge (L2)! Còn nếu tin theo phân phối Laplace, nó sẽ sinh ra hồi quy Lasso (L1).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\ln P(w \mid X, y) = \ln P(y \mid X, w) + \ln P(w) - \text{const} = -\frac{1}{2\sigma^2}\|y - Xw\|^2 - \frac{1}{2\sigma_w^2}\|w\|^2$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Tiên nghiệm Gauss sinh ra Ridge ($L_2$), không sinh ra nghiệm thưa như Lasso (Lasso sinh ra từ tiên nghiệm Laplace, loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.1 Khái Niệm Xác Suất & Định Lý Bayes**.

---

### Câu 74 [VOAI02-M74] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Bất đẳng thức Jensen đối với một hàm lồi $f$ và một biến ngẫu nhiên $X$ phát biểu mối quan hệ nào sau đây, vốn là nền tảng để thiết lập chặn dưới bằng chứng (ELBO) trong mô hình VAE?

- **A.** $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$, tức giá trị hàm lồi tại kỳ vọng luôn nhỏ hơn hoặc bằng kỳ vọng của hàm lồi
- **B.** $f(\mathbb{E}[X]) \ge \mathbb{E}[f(X)]$ áp dụng cho mọi hàm số khả vi bất kể tính lồi lõm
- **C.** $\mathbb{E}[f(X)] = f(\mathbb{E}[X]) + \text{Var}(X)$ với mọi biến ngẫu nhiên có phương sai hữu hạn
- **D.** $\mathbb{E}[f(X)] \le 0$ khi và chỉ khi biến ngẫu nhiên $X$ tuân theo phân phối đều

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Với một hàm cong như cái bát (hàm lồi, ví dụ $f(x) = x^2$): Đáy bát tại điểm trung bình $f(\mathbb{E}[X])$ luôn thấp hơn hoặc bằng mức trung bình của các điểm trên vành bát $\mathbb{E}[f(X)]$. Vì hàm logarit là hàm lõm (úp ngược), bất đẳng thức đổi chiều: $\ln \mathbb{E}[X] \ge \mathbb{E}[\ln X]$, tạo nên cận dưới ELBO cho VAE!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Bất đẳng thức Jensen cho hàm lồi: $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B nhầm chiều bất đẳng thức của hàm lồi.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.1 Khái Niệm Xác Suất & Định Lý Bayes**.

---

### Câu 75 [VOAI02-M75] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Theo Định lý Giới hạn Trung tâm (Central Limit Theorem - CLT), nếu $X_1, X_2, \dots, X_n$ là các biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) có kỳ vọng $\mu$ và phương sai $\sigma^2 < \infty$, phân phối của trung bình mẫu $\bar{X}_n$ sẽ tiến tới phân phối nào khi $n \to \infty$?

- **A.** Phân phối đều liên tục (Uniform Distribution) trên đoạn $[\mu - \sigma, \mu + \sigma]$ với mật độ xác suất hằng số
- **B.** Phân phối Poisson rời rạc (Poisson Distribution) với tham số cường độ $\lambda = \mu / \sigma^2$ mô tả số lượng biến cố
- **C.** Phân phối chuẩn $\mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$, với độ lệch chuẩn thu hẹp theo tốc độ ($1/\sqrt{n}$)
- **D.** Phân phối Cauchy (Heavy-tailed Distribution) có đuôi cực nặng và không tồn tại kỳ vọng toán học cũng như phương sai

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Dù dữ liệu ban đầu có hình thù kỳ dị đến đâu (tung xúc xắc, nhị thức, xiên lệch), cứ lấy trung bình cộng của nhiều mẫu lại ($n \ge 30$), phân phối của số trung bình đó sẽ luôn luôn có dạng hình chuông chuẩn Gauss tuyệt đẹp! Càng lấy nhiều mẫu, quả chuông càng bóp hẹp lại (phương sai giảm dần theo $\sigma^2 / n$).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1) \implies \bar{X}_n \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Thí sinh hay quên chia phương sai cho $n$ (độ lệch chuẩn chia $\sqrt{n}$).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.2 Các Phân Phối Xác Suất Thông Dụng**.

---

### Câu 76 [VOAI02-M76] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong kiểm định giả thuyết thống kê (Hypothesis Testing), sai lầm loại I (Type I Error) và lực của kiểm định (Statistical Power) được định nghĩa bằng các xác suất nào sau đây?

- **A.** Sai lầm loại I là chấp nhận $H_0$ khi $H_0$ sai (False Negative); Lực kiểm định là xác suất bác bỏ $H_0$ khi giả thuyết đúng
- **B.** Sai lầm loại I là bác bỏ $H_0$ khi $H_0$ đúng (mức ý nghĩa $\alpha$); Lực kiểm định là $1 - \beta$ (bác bỏ $H_0$ khi $H_0$ sai)
- **C.** Sai lầm loại I luôn bằng 0 (Zero Error) khi kích thước mẫu quan sát $N$ vượt quá 1000 phần tử theo luật số lớn
- **D.** Lực kiểm định là xác suất sai số bình phương trung bình (MSE Minimization) đạt giá trị cực tiểu toàn cục

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Giả thuyết $H_0$: Bị cáo vô tội.
- Sai lầm loại I (False Positive / $\alpha$): Bị cáo vô tội nhưng tòa án lại tuyên có tội (bác bỏ nhầm $H_0$).
- Sai lầm loại II (False Negative / $\beta$): Bị cáo có tội thật nhưng tòa lại tha bổng (chấp nhận nhầm $H_0$).
- Lực kiểm định ($1 - \beta$): Xác suất bắt đúng kẻ có tội!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\alpha = P(\text{Reject } H_0 \mid H_0 \text{ is True})$, $\text{Power} = 1 - \beta = P(\text{Reject } H_0 \mid H_0 \text{ is False})$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A đảo ngược định nghĩa của hai loại sai lầm.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.3 Ước Lượng Tham Số & Kiểm Định Giả Thuyết**.

---

### Câu 77 [VOAI02-M77] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Hệ số tương quan Pearson $r_{XY}$ chuẩn hóa hiệp phương sai $\text{Cov}(X, Y)$ bằng cách chia cho đại lượng nào, và sở hữu miền giá trị bị chặn như thế nào?

- **A.** Chia cho tổng kỳ vọng $\mathbb{E}[X] + \mathbb{E}[Y]$ và bị chặn trong đoạn $[0, +\infty)$
- **B.** Chia cho tích hai độ lệch chuẩn $\sigma_X \sigma_Y$ và luôn bị chặn nghiêm ngặt trong đoạn $[-1, +1]$
- **C.** Chia cho hiệu hai phương sai $\sigma_X^2 - \sigma_Y^2$ và có thể nhận giá trị vô cùng lớn
- **D.** Chia cho trung bình nhân của kích thước tập dữ liệu và luôn luôn nhận giá trị dương

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Hiệp phương sai $\text{Cov}(X, Y)$ bị nhược điểm là phụ thuộc đơn vị đo (đổi từ mét sang milimet thì số phóng to cả triệu lần). Hệ số Pearson chia cho tích hai độ lệch chuẩn $\sigma_X \sigma_Y$ để ' triệt tiêu đơn vị ', ép giá trị luôn nằm ngoan ngoãn trong đoạn $[-1, 1]$. Bằng 1 là tương quan tuyến tính thuận tuyệt đối, bằng -1 là nghịch tuyệt đối.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $r_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \in [-1, 1]$ (theo bất đẳng thức Cauchy-Schwarz). Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A và C chia sai mẫu số và xác định sai miền chặn.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.1 Khái Niệm Xác Suất & Định Lý Bayes**.

---

### Câu 78 [VOAI02-M78] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Nếu số lượng cuộc gọi đến tổng đài trong 1 giờ tuân theo phân phối Poisson với cường độ $\lambda$, thì thời gian chờ đợi giữa hai cuộc gọi liên tiếp sẽ tuân theo phân phối xác suất nào và có tính chất đặc trưng gì?

- **A.** Phân phối chuẩn (Gaussian) với tính đối xứng qua điểm trung bình thời gian phục vụ
- **B.** Phân phối lũy thừa (Exponential) với tham số $\lambda$ và sở hữu tính chất không nhớ (Memoryless Property)
- **C.** Phân phối đều (Uniform) không phụ thuộc vào thời điểm bắt đầu theo dõi cuộc gọi
- **D.** Phân phối nhị thức âm với số lần thử nghiệm độc lập tiến tới vô cùng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Số sự kiện xảy ra trong một khoảng thời gian là Poisson, thì thời gian chờ giữa hai sự kiện là phân phối mũ (Exponential). Tính ' không nhớ ' nghĩa là: dù bạn đã chờ xe buýt suốt 30 phút mà chưa thấy đâu, thì xác suất phải chờ thêm 10 phút nữa vẫn y nguyên như lúc bạn vừa mới bước chân ra trạm!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $P(T > t+s \mid T > s) = P(T > t) = e^{-\lambda t}$. Đây là phân phối mũ Exponential($\lambda$). Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Các phân phối Normal, Uniform không có tính chất không nhớ (Memoryless).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.2 Các Phân Phối Xác Suất Thông Dụng**.

---

### Câu 79 [VOAI02-M79] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Xét góc độ hình học tối ưu hóa có ràng buộc, tại sao điều hòa $L_1$ (Lasso Regression: $\|w\|_1 \le t$) có khả năng triệt tiêu trọng số về đúng 0 (Feature Selection / Sparsity) trong khi điều hòa $L_2$ (Ridge Regression: $\|w\|_2^2 \le t$) thì không?

- **A.** Đường đẳng mức của hàm mất mát luôn là các hình tròn đồng tâm tiếp xúc với mặt cầu $L_2$ tại vô số điểm kỳ dị
- **B.** Khối cầu $L_1$ có các đỉnh nhọn trên trục tọa độ nên đường elip mất mát dễ tiếp xúc tại đỉnh nhọn làm các tọa độ khác bằng 0
- **C.** Hàm chuẩn $L_1$ có đạo hàm tại điểm 0 bằng vô cùng trong khi hàm $L_2$ có đạo hàm triệt tiêu đồng nhất tại mọi điểm
- **D.** Điều hòa $L_1$ tự động loại bỏ các biến phụ thuộc tuyến tính thông qua phân tích ma trận trực giao Gram-Schmidt

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Vùng an toàn của $L_2$ là hình tròn mượt mà: quả bóng elip sai số khi chạm vào hình tròn thường chạm ở một điểm lơ lửng trên đường cong (cả hai trọng số đều khác 0).
- Vùng an toàn của $L_1$ là hình thoi/kim cương có các ' mũi nhọn ' đâm thẳng vào các trục tọa độ ($w_1 = 0$ hoặc $w_2 = 0$). Quả bóng elip khi nở ra rất dễ va quẹt đầu tiên vào chính các mũi nhọn này, làm cho một trọng số bị triệt tiêu sạch về 0!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khối đa diện $L_1$-ball có các điểm góc (corners) tại $w_i = 0$. Điểm tiếp xúc của contour ellipsoid với $L_1$-ball có xác suất rất cao rơi vào các đỉnh này. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Đạo hàm của $|w|$ tại 0 là subgradient $[-1, 1]$, không phải bằng vô cùng (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.2 Hồi Quy Tuyến Tính & Logistic Regression**.

---

### Câu 80 [VOAI02-M80] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi đánh giá bài toán phân loại nhị phân trên tập dữ liệu có tỷ lệ mất cân bằng lớp cực lớn (ví dụ lớp dương chỉ chiếm 0.01%), tại sao đường cong PR (Precision-Recall Curve) phản ánh độ tin cậy thực tế tốt hơn nhiều so với đường cong ROC (Receiver Operating Characteristic)?

- **A.** Đường cong ROC không thể tính toán được khi số lượng mẫu thuộc lớp âm lớn hơn 10.000 mẫu trong tập kiểm thử
- **B.** Mẫu số của FPR chứa lượng khổng lồ TN khiến FPR luôn nhân tạo rất nhỏ và ROC-AUC cao giả tạo; PR không bị ảnh hưởng bởi TN
- **C.** Chỉ số Precision hoàn toàn không phụ thuộc vào việc điều chỉnh ngưỡng phân ngưỡng xác suất của bộ phân loại
- **D.** Đường cong PR luôn đi qua điểm tọa độ $(0, 0)$ và $(1, 1)$ trong mọi trường hợp phân phối xác suất của dữ liệu

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong trục hoành của ROC là $FPR = FP / (FP + TN)$. Vì lớp âm (TN) quá đông đảo (100.000 mẫu), dù mô hình đoán nhầm bừa bãi $FP = 500$ ca thì $FPR$ vẫn chỉ là $500 / 100.500 \approx 0.005$ (nhỏ xíu!). ROC nhìn rất đẹp (AUC 0.98), nhưng thực tế Precision chỉ có $50 / (50 + 500) \approx 9\%$ (vô dụng). Đường cong PR nhìn thẳng vào thảm họa này!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi $TN \gg FP$, $FPR \approx 0$ ngay cả khi $FP \gg TP$. Ngược lại, $\text{Precision} = \frac{TP}{TP + FP}$ phản ánh trực tiếp sự suy giảm hiệu năng do $FP$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** ROC luôn vẽ được (loại A); Precision thay đổi theo ngưỡng threshold (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.7 Xử Lý Dữ Liệu Mất Cân Bằng (Imbalanced Data)**.

---

### Câu 81 [VOAI02-M81] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Chỉ số $F_\beta$ Score được tính theo công thức $F_\beta = (1 + \beta^2) \frac{\text{Precision} \cdot \text{Recall}}{(\beta^2 \cdot \text{Precision}) + \text{Recall}}$. Trong bài toán chẩn đoán ung thư, nơi việc bỏ sót bệnh nhân (False Negative) nguy hiểm hơn nhiều so với việc chẩn đoán nhầm (False Positive), ta nên chọn giá trị $\beta$ như thế nào?

- **A.** $\beta = 0$ để triệt tiêu hoàn toàn thành phần Recall ra khỏi độ đo đánh giá
- **B.** $\beta > 1$ (ví dụ $F_2$ Score) để coi trọng chỉ số Recall gấp $\beta$ lần so với Precision
- **C.** $\beta < 1$ (ví dụ $F_{0.5}$ Score) để ưu tiên tối đa tính chuẩn xác Precision của các ca dương tính
- **D.** $\beta = -1$ để đảo ngược thứ tự xếp hạng của các mẫu kiểm định

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
$\beta$ là thước đo ' coi trọng ai hơn '. $\beta = 1$ là $F_1$ coi Recall và Precision ngang nhau. Nếu sợ bỏ sót bệnh nhân ung thư (cần Recall cực cao), ta đặt $\beta = 2$ ($F_2$-score). Nhìn vào công thức, $\beta^2 = 4$ đứng cạnh Precision ở mẫu số, buộc mô hình muốn điểm cao thì bắt buộc phải tăng Recall lên!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $F_\beta$ cân trọng số: $\beta$ đo số lần Recall quan trọng hơn Precision. $\beta = 2$ ưu tiên Recall. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** $\beta = 0.5$ ưu tiên Precision (thích hợp cho chống spam email, loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Đánh Giá Mô Hình & Cross-Validation**.

---

### Câu 82 [VOAI02-M82] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong quy trình xây dựng mô hình Machine Learning chuẩn mực, hành động nào sau đây là nguyên nhân trực tiếp dẫn đến hiện tượng Rò rỉ Thông tin (Data Leakage) khi tiền xử lý dữ liệu chuẩn hóa StandardScaler?

- **A.** Chỉ gọi `scaler.fit(X_train)` trên tập huấn luyện rồi dùng `scaler.transform()` cho cả Train và Test
- **B.** Gọi `scaler.fit_transform(X)` trên TOÀN BỘ tập dữ liệu trước khi chia tách thành Train và Test
- **C.** Lưu đối tượng scaler đã học vào tệp pickle để sử dụng lại trong pha Inference thực tế
- **D.** Kiểm tra giá trị trung bình của tập Train sau chuẩn hóa có xấp xỉ bằng 0 hay không

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
`fit` là bước tính trung bình $\mu$ và độ lệch chuẩn $\sigma$. Nếu bạn tính $\mu$ và $\sigma$ trên toàn bộ dữ liệu trước khi chia Train-Test, thông tin phân phối của tập Test đã lọt vào tập Train (nhìn trộm đề). Hậu quả: điểm test lúc thí nghiệm cao ngất ngưởng, nhưng khi triển khai thực tế gặp khách hàng mới thì sập tiệm!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mu_{\text{all}}$ chứa $\{x_i\}_{i \in \text{test}}$. Quy tắc vàng: chỉ `fit` trên `X_train`. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A là quy trình chuẩn xác 100%, câu hỏi hỏi hành vi gây ra rò rỉ dữ liệu.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Đánh Giá Mô Hình & Cross-Validation**.

---

### Câu 83 [VOAI02-M83] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hàm mất mát $\epsilon$-không nhạy ($\epsilon$-insensitive loss function) trong mô hình Hồi quy Vector Hỗ trợ (Support Vector Regression - SVR) được định nghĩa như thế nào đối với phần dư sai số $e = |y - f(x)|$?

- **A.** $L_\epsilon(e) = 0$ nếu $e \le \epsilon$, và bằng $e - \epsilon$ nếu $e > \epsilon$
- **B.** $L_\epsilon(e) = e^2$ nếu $e \le \epsilon$, và bằng $2\epsilon e - \epsilon^2$ nếu $e > \epsilon$
- **C.** $L_\epsilon(e) = 0$ nếu $e > \epsilon$, và bằng $\epsilon - e$ nếu $e \le \epsilon$
- **D.** $L_\epsilon(e) = e$ nếu $e \le \epsilon$, và bằng $0$ nếu $e > \epsilon$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
SVR dựng một ' đường ống ' có bán kính $\epsilon$ xung quanh đường hồi quy. Nếu điểm dữ liệu nằm lọt bên trong đường ống ($|y - f(x)| \le \epsilon$), sai số được coi là 0 (hoàn toàn miễn phạt). Chỉ những điểm nào nằm văng ra ngoài ống mới bị tính phạt tuyến tính $e - \epsilon$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $L_\epsilon(y, f(x)) = \max(0, |y - f(x)| - \epsilon)$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án C nói ngược điều kiện; Phương án B là Huber Loss chứ không phải SVR tube.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Support Vector Machines (SVM)**.

---

### Câu 84 [VOAI02-M84] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Theo Định lý Mercer, điều kiện cần và đủ để một hàm nhân $K(x, z)$ là một hàm nhân hợp lệ (Valid Mercer Kernel) biểu diễn tích vô hướng trong không gian Hilbert $\langle \phi(x), \phi(z) \rangle$ là gì?

- **A.** Hàm nhân phải có đạo hàm bậc hai liên tục và bằng 0 tại gốc tọa độ trên toàn bộ không gian số thực nhiều chiều
- **B.** Hàm nhân $K(x, z)$ đối xứng và ma trận Gram $G_{ij} = K(x_i, x_j)$ phải nửa xác định dương (PSD) với mọi tập dữ liệu
- **C.** Hàm nhân phải là một hàm tuần hoàn có chu kỳ cơ sở bằng $\pi$ và tích phân trên toàn miền xác định bằng đúng 1
- **D.** Giá trị của hàm nhân luôn bị chặn nghiêm ngặt trong khoảng hở $(0, 1)$ và đơn điệu giảm theo khoảng cách Euclid

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Để ' thủ thuật nhân ' (Kernel Trick) chạy được mà không bị lỗi toán học, ma trận khoảng cách/tương đồng giữa các điểm (ma trận Gram) phải luôn luôn là ma trận nửa xác định dương ($c^T G c \ge 0$). Điều này tương đương với việc nó thực sự là tích vô hướng trong một không gian hình học thực thụ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định lý Mercer: $K$ đối xứng và $\iint g(x) K(x, z) g(z) dx dz \ge 0, \forall g \in L_2 \iff G \succeq 0$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Kernel không bắt buộc tuần hoàn (RBF, Polynomial đều không tuần hoàn, loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Support Vector Machines (SVM)**.

---

### Câu 85 [VOAI02-M85] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong kỹ thuật tỉa cành Cây Quyết Định Cost-Complexity Pruning (tham số `ccp_alpha` trong scikit-learn), hàm mục tiêu tối thiểu hóa chi phí $R_\alpha(T) = R(T) + \alpha |T|$ cân bằng giữa hai đại lượng nào?

- **A.** Sai số phân loại $R(T)$ và số lượng lá $|T|$ của cây; khi $\alpha$ tăng lên, cây bị tỉa ngắn lại (Overfitting Reduction)
- **B.** Thời gian huấn luyện trên GPU và kích thước RAM (Memory Reduction); khi $\alpha$ tăng lên thì cây nở rộng ra để tăng tốc
- **C.** Độ sâu tối đa và số lượng đặc trưng đầu vào (Feature Pruning); khi $\alpha$ tăng lên thì độ sâu tăng theo hàm số mũ
- **D.** Chỉ số entropy và chỉ số Gini (Impurity Swapping); khi $\alpha$ tăng lên thì hai chỉ số này tự động hoán đổi vị trí

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cây càng nhiều lá ($|T|$ to) thì càng dễ học vẹt (overfitting). Công thức phạt thêm $\alpha |T|$ giống như tính ' tiền phạt ' cho mỗi chiếc lá mọc thêm. Nếu $\alpha = 0$, cây cứ mọc thoải mái. Khi tăng $\alpha$ lên, thuật toán sẽ chặt bớt những cành lá rườm rà không đóng góp nhiều cho độ chính xác, giúp cây gọn gàng và tổng quát hóa tốt hơn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $R_\alpha(T) = R(T) + \alpha |T|$. $\alpha \ge 0$ là hệ số phạt độ phức tạp. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** $\alpha$ tăng làm cây nhỏ lại (tỉa cành), không phải mọc to ra (loại B, C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.6 Cây Quyết Định (Decision Trees)**.

---

### Câu 86 [VOAI02-M86] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán XGBoost sử dụng khai triển Taylor bậc hai của hàm mục tiêu để tìm cấu trúc cây và trọng số tối ưu tại mỗi lá $w_j^*$. Công thức tính điểm tối ưu $w_j^*$ theo tổng gradient bậc một $G_j = \sum_{i \in I_j} g_i$ và tổng Hessian bậc hai $H_j = \sum_{i \in I_j} h_i$ với hệ số phạt L2 $\lambda$ là gì?

- **A.** $w_j^* = -\frac{H_j}{G_j + \lambda}$
- **B.** $w_j^* = -\frac{G_j}{H_j + \lambda}$
- **C.** $w_j^* = -\frac{G_j \cdot H_j}{\lambda}$
- **D.** $w_j^* = \sqrt{\frac{G_j^2}{H_j + \lambda}}$

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
XGBoost xấp xỉ hàm mất mát tại mỗi lá thành một parabol bậc 2: $f(w_j) = G_j w_j + \frac{1}{2}(H_j + \lambda) w_j^2$. Đáy parabol (đạo hàm bằng 0) nằm tại $G_j + (H_j + \lambda) w_j = 0 \implies w_j^* = -\frac{G_j}{H_j + \lambda}$. Cực kỳ đơn giản, đẹp mắt và tối ưu chính xác tuyệt đối!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\frac{\partial \tilde{\mathcal{L}}}{\partial w_j} = G_j + (H_j + \lambda) w_j = 0 \implies w_j^* = -\frac{G_j}{H_j + \lambda}$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A đảo ngược vị trí giữa Gradient ($G$) và Hessian ($H$).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.6 Cây Quyết Định (Decision Trees)**.

---

### Câu 87 [VOAI02-M87] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán LightGBM tăng tốc độ huấn luyện vượt bậc so với XGBoost truyền thống nhờ kết hợp hai kỹ thuật cốt lõi nào sau đây?

- **A.** Kỹ thuật Stochastic Gradient Descent đa luồng (Multi-thread SGD) và mạng nơ-ron tích chập 1D để học đặc trưng bảng
- **B.** GOSS (Lấy mẫu một phía dựa trên gradient) và EFB (Gộp các đặc trưng loại trừ lẫn nhau để giảm chiều dữ liệu)
- **C.** Loại bỏ hoàn toàn các biến định lượng (Numeric Removal) và chỉ giữ lại các biến phân loại one-hot để tìm ngưỡng
- **D.** Sử dụng biến đổi Wavelet (Wavelet Transform) để làm phẳng toàn bộ cây quyết định thành ma trận thưa trước khi chia

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
LightGBM có 2 ' vũ khí bí mật ':
1. GOSS: Giữ lại tất cả các mẫu có gradient lớn (học chưa tốt), còn các mẫu có gradient nhỏ (đã học tốt) thì bốc ngẫu nhiên một phần nhỏ $\implies$ giảm số lượng dòng dữ liệu.
2. EFB: Gom các cột dữ liệu ít khi cùng xuất hiện (thưa thớt) vào chung một cột duy nhất $\implies$ giảm số lượng cột dữ liệu. Nhờ đó tốc độ tăng gấp nhiều lần!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Gradient-based One-Side Sampling (GOSS) + Exclusive Feature Bundling (EFB). Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** LightGBM không dùng Wavelet (loại D) hay ép về one-hot (nó có xử lý categorical trực tiếp rất thông minh, loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.6 Cây Quyết Định (Decision Trees)**.

---

### Câu 88 [VOAI02-M88] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán CatBoost xử lý các biến phân loại (Categorical Features) bằng kỹ thuật Target Statistics có thứ tự (Ordered Target Statistics) nhằm ngăn ngừa hiện tượng tiêu cực nào?

- **A.** Ngăn chặn hiện tượng tràn bộ nhớ VRAM (Memory Overflow) khi số lượng category của các biến vượt quá ngưỡng 100
- **B.** Ngăn chặn hiện tượng rò rỉ nhãn mục tiêu (Target Leakage) dẫn đến Overfitting khi mã hóa bằng trung bình nhãn
- **C.** Triệt tiêu sự phụ thuộc tuyến tính (Collinearity Removal) giữa các biến đầu vào bằng ma trận nghịch đảo Moore-Penrose
- **D.** Đảm bảo tất cả các biến phân loại (Gaussian Normalization) đều tuân theo phân phối chuẩn tắc có kỳ vọng 0 và phương sai 1

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mã hóa category bằng trung bình nhãn (Target Encoding thường) rất nguy hiểm vì nó lấy nhãn của chính dòng đó tính vào trung bình $\implies$ rò rỉ nhãn mục tiêu và overfit nặng. CatBoost xáo trộn thứ tự dữ liệu, mỗi dòng chỉ được dùng nhãn của những dòng đứng TRƯỚC nó để tính trung bình, hoàn toàn không bị rò rỉ tương lai!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\hat{x}_{k} = \frac{\sum_{j < i, x_j = x_i} y_j + a \cdot P}{\sum_{j < i, x_j = x_i} 1 + a}$ trên hoán vị ngẫu nhiên $\sigma$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Ordered TS chống Target Leakage (loại B), không phải giải quyết VRAM (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.6 Cây Quyết Định (Decision Trees)**.

---

### Câu 89 [VOAI02-M89] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong phân cụm phân cấp tích tụ (Agglomerative Hierarchical Clustering), phương pháp liên kết đơn (Single Linkage: khoảng cách giữa hai cụm là khoảng cách ngắn nhất giữa hai điểm) thường gặp phải hạn chế cố hữu nào?

- **A.** Hiệu ứng dây xích (Chaining Effect): các cụm dễ bị nối dài do một vài điểm nhiễu nằm bắc cầu giữa các vùng dữ liệu
- **B.** Luôn ép các cụm phân tách phải có dạng hình cầu đối xứng hoàn hảo với bán kính bằng nhau trong không gian Euclid
- **C.** Không thể xử lý được không gian dữ liệu có số chiều lớn hơn 3 do hạn chế của ma trận khoảng cách hình học
- **D.** Độ phức tạp tính toán thời gian bị tăng lên bậc bốn $O(N^4)$ khiến thuật toán không thể hội tụ trên tập dữ liệu lớn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Single Linkage tính khoảng cách giữa 2 cụm bằng 2 điểm gần nhau nhất. Nếu có vài điểm nhiễu nằm rải rác làm ' cầu nối ' giữa 2 cụm lớn ở xa nhau, thuật toán sẽ cứ thế bò theo cây cầu này và gộp luôn 2 cụm thành một chuỗi dài loằng ngoằng (gọi là Chaining Effect)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $D(A, B) = \min_{x \in A, y \in B} d(x, y)$. Rất nhạy cảm với outliers và cầu nối nhiễu. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Ép cụm hình cầu là đặc tính của Ward Linkage hoặc K-Means, không phải Single Linkage (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Giảm Chiều Dữ Liệu (Dimensionality Reduction)**.

---

### Câu 90 [VOAI02-M90] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán phân cụm dựa trên mật độ DBSCAN phân loại một điểm dữ liệu $p$ là điểm lõi (Core Point) khi thỏa mãn điều kiện toán học nào với bán kính lân cận $\epsilon$ và ngưỡng số điểm tối thiểu $\text{MinPts}$?

- **A.** Khoảng cách từ điểm $p$ đến trọng tâm của tập dữ liệu (Centroid Distance) phải nhỏ hơn đúng $\epsilon / 2$ theo chuẩn Euclid
- **B.** Vùng lân cận $N_\epsilon(p) = \{q \mid d(p, q) \le \epsilon\}$ chứa ít nhất $\text{MinPts}$ điểm (bao gồm cả chính điểm $p$)
- **C.** Điểm $p$ phải có ít nhất $\text{MinPts}$ vector trực giao (Orthogonal Basis) với các vector cơ sở của không gian đặc trưng
- **D.** Mật độ xác suất Gaussian tại điểm $p$ (Density Threshold) phải lớn hơn ngưỡng kỳ vọng toàn cục ước lượng qua EM

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
DBSCAN coi điểm là ' lõi ' (Core Point) nếu vẽ một vòng tròn bán kính $\epsilon$ quanh nó mà chứa được từ $\text{MinPts}$ điểm trở lên (đủ đông đúc). Nếu ít hơn $\text{MinPts}$ nhưng vẫn nằm trong vòng tròn của một điểm lõi khác, nó là điểm biên (Border). Còn nếu cô độc một mình thì là điểm nhiễu (Noise)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $|N_\epsilon(p)| = |\{q \in D \mid \text{dist}(p, q) \le \epsilon\}| \ge \text{MinPts}$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** DBSCAN là mật độ phi tham số dựa trên khoảng cách, không dùng Gaussian kỳ vọng (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Giảm Chiều Dữ Liệu (Dimensionality Reduction)**.

---

### Câu 91 [VOAI02-M91] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán giảm chiều trực quan hóa t-SNE, tại sao phân phối xác suất trong không gian chiều thấp (2D/3D) lại sử dụng phân phối Student-t với 1 bậc tự do (Cauchy) thay vì dùng phân phối Gauss?

- **A.** Phân phối Cauchy giúp tính toán tích phân ma trận nhanh hơn phân phối Gauss gấp 10 lần trên phần cứng tăng tốc GPU
- **B.** Giải quyết vấn đề dồn cục (Crowding Problem): đuôi nặng của Student-t đẩy các cụm dữ liệu khác biệt ra xa nhau
- **C.** Đảm bảo ma trận khoảng cách pairwise trong không gian chiều thấp luôn có định thức khác 0 và khả nghịch tuyệt đối
- **D.** Loại bỏ hoàn toàn sự cần thiết của bước tối ưu hóa phân kỳ Kullback-Leibler (KL) bằng thuật toán Gradient Descent

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong không gian cao chiều, thể tích nở ra cực lớn nên các điểm có nhiều chỗ đứng. Khi ép xuống mặt phẳng 2D chật chội, các điểm ở xa nhau bị dồn cục lại thành một mớ hỗn độn (Crowding Problem). Phân phối Student-t có đuôi rất dày (Heavy-tailed), giúp ' đẩy bung ' các cụm khác nhau ra xa, làm bức tranh trực quan hóa rõ ràng và đẹp mắt!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_k \sum_{l \ne k} (1 + \|y_k - y_l\|^2)^{-1}}$. Đuôi giảm theo bậc $1/r^2$ thay vì $e^{-r^2}$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** t-SNE vẫn tối ưu hóa KL divergence bằng Gradient Descent (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Giảm Chiều Dữ Liệu (Dimensionality Reduction)**.

---

### Câu 92 [VOAI02-M92] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Tích chập giãn nở (Dilated Convolution / Atrous Convolution) với hệ số giãn nở $d > 1$ mang lại ưu điểm vượt trội nào trong các bài toán phân đoạn ngữ nghĩa (Semantic Segmentation như DeepLab)?

- **A.** Tự động đảo ngược thứ tự các kênh màu RGB để tạo ra đặc trưng bất biến với sự biến đổi cường độ ánh sáng môi trường
- **B.** Mở rộng Receptive Field theo cấp số mà không làm tăng số lượng tham số hay làm suy giảm độ phân giải không gian ảnh
- **C.** Giảm số lượng phép nhân tích chập về 0 nhờ chèn các phần tử số 0 ngẫu nhiên vào ma trận trọng số của bộ lọc
- **D.** Triệt tiêu hoàn toàn hiện tượng mất mát thông tin khi nén ảnh qua các tầng pooling bằng cách nội suy song tuyến tính

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Bình thường muốn nhìn rộng hơn, bạn phải dùng Max Pooling (thu nhỏ ảnh, làm mất chi tiết viền) hoặc dùng filter to hơn (tốn thêm rất nhiều tham số). Dilated Convolution ' chọc thủng các lỗ rỗng ' giữa các trọng số của filter (hệ số $d$), giúp filter $3 \times 3$ nhìn rộng như ô $5 \times 5$ hay $7 \times 7$ mà số lượng tham số vẫn chỉ đúng 9 số, và ảnh không bị thu nhỏ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Kernel hiệu dụng: $K ' = K + (K - 1)(d - 1)$. Với $K=3, d=2 \implies K '=5$, tham số vẫn là $3 \times 3$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Dilated conv không triệt tiêu phép nhân về 0 (loại C) và không can thiệp kênh màu (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 93 [VOAI02-M93] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc MobileNet, tầng tích chập Depthwise Separable Convolution phân tách một tầng tích chập chuẩn $K \times K$ với $C_{\text{in}}$ kênh vào và $C_{\text{out}}$ kênh ra thành hai bước nào?

- **A.** Bước tích chập 1D theo chiều ngang (Horizontal Conv) và bước tích chập 1D theo chiều dọc để bảo toàn tính đối xứng ảnh
- **B.** Bước Depthwise Conv (tích chập $K \times K$ độc lập từng kênh) và bước Pointwise Conv (tích chập $1 \times 1$ gộp kênh)
- **C.** Bước phân tích ma trận SVD rút gọn (Rank Truncation) và bước khử nhiễu tín hiệu bằng bộ lọc Gaussian hai chiều
- **D.** Bước lượng tử hóa trọng số INT8 (Weight Quantization) và bước giải mã số thực dấu phẩy động FP16 trước khi kích hoạt

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tích chập chuẩn vừa lo nhìn không gian ($K \times K$) vừa lo pha trộn các kênh màu ($C_{\text{in}} \times C_{\text{out}}$), cực kỳ nặng nề. MobileNet tách đôi nhiệm vụ:
1. Depthwise Conv: mỗi kênh tự lọc không gian bằng filter $K \times K$ của riêng mình.
2. Pointwise Conv: dùng filter $1 \times 1$ để trộn các kênh lại với nhau.
Nhờ tách đôi, lượng tính toán giảm khoảng 8 đến 9 lần!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tỉ số chi phí: $\frac{K^2 C_{\text{in}} + C_{\text{in}} C_{\text{out}}}{K^2 C_{\text{in}} C_{\text{out}}} = \frac{1}{C_{\text{out}}} + \frac{1}{K^2} \approx \frac{1}{9}$ khi $K=3$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A là Spatially Separable Convolution, không phải Depthwise Separable Convolution.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 94 [VOAI02-M94] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cơ chế kết nối tắt (Residual Skip Connection: $x_{l+1} = x_l + F(x_l)$) trong kiến trúc ResNet giải quyết bài toán biến mất gradient (Vanishing Gradient) trong mạng cực sâu nhờ tính chất toán học nào của đạo hàm lan truyền ngược?

- **A.** Đạo hàm theo đầu vào luôn chứa số hạng hằng số $+1$: $\frac{\partial \mathcal{E}}{\partial x_l} = \frac{\partial \mathcal{E}}{\partial x_L} \left(1 + \frac{\partial}{\partial x_l} \sum F\right)$, tạo đường cao tốc truyền gradient
- **B.** Đạo hàm theo đầu vào nhân đôi gradient sau mỗi tầng mạng: $\frac{\partial \mathcal{E}}{\partial x_l} = 2 \cdot \frac{\partial \mathcal{E}}{\partial x_{l+1}}$, bù đắp năng lượng tiêu hao khi lan truyền ngược
- **C.** Đạo hàm ép các ma trận trọng số về ma trận trực giao đơn vị: $\frac{\partial \mathcal{E}}{\partial x_l} = I \cdot \frac{\partial \mathcal{E}}{\partial x_L}$, bảo toàn chuẩn Euclid của vector tensor
- **D.** Đạo hàm biến phép toán cộng thành phép nhân ma trận đối xứng: $\frac{\partial \mathcal{E}}{\partial x_l} = F(x_l)^T \frac{\partial \mathcal{E}}{\partial x_{l+1}}$, tăng tốc độ tính toán phần cứng

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi mạng sâu hàng trăm tầng, nhân chuỗi đạo hàm gồm toàn các số nhỏ sẽ làm gradient teo tóp về 0. Đường tắt $x_{l+1} = x_l + F(x_l)$ có đạo hàm của $x_l$ bằng đúng số 1. Số 1 này đóng vai trò như một ' đường dây cao tốc ': gradient từ tầng cuối cùng có thể chạy thẳng tuột về tầng đầu tiên mà không bao giờ bị nhân nhỏ về 0!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\frac{\partial \mathcal{E}}{\partial x_l} = \frac{\partial \mathcal{E}}{\partial x_L} \frac{\partial x_L}{\partial x_l} = \frac{\partial \mathcal{E}}{\partial x_L} \left(1 + \frac{\partial}{\partial x_l}\sum_{i=l}^{L-1} F(x_i)\right)$. Số hạng $1$ bảo vệ gradient. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Skip connection không nhân đôi gradient bừa bãi (loại B) và không ép ma trận trực giao (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 95 [VOAI02-M95] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khối phần dư đảo ngược (Inverted Residual Block) trong kiến trúc MobileNetV2 khác biệt với khối phần dư cổ điển của ResNet ở đặc điểm cấu trúc nào?

- **A.** ResNet nén kênh ở giữa (Dày - Mỏng - Dày) trong khi MobileNetV2 mở rộng kênh ở giữa (Mỏng - Dày - Mỏng) và dùng Linear Bottleneck
- **B.** MobileNetV2 loại bỏ kết nối tắt skip connection (No Residuals) để tăng tốc độ tính toán lan truyền thuận trên thiết bị di động
- **C.** ResNet sử dụng hàm kích hoạt ReLU6 ở tất cả các tầng (Standard ReLU) trong khi MobileNetV2 chỉ sử dụng hàm phi tuyến Sigmoid
- **D.** MobileNetV2 thay thế các tầng tích chập bằng tầng kết nối đầy đủ (Dense Layers) kết hợp với cơ chế Dropout tỉ lệ cao

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- ResNet Bottleneck: Rộng $\to$ Bóp hẹp lại ở giữa $\to$ Nở rộng ra (Dày - Mỏng - Dày).
- MobileNetV2 Inverted: Mỏng $\to$ Phóng to số kênh ra để tích chập Depthwise học nhiều đặc trưng $\to$ Nén mỏng lại (Mỏng - Dày - Mỏng). Ở tầng cuối dùng kích hoạt tuyến tính (Linear Bottleneck) để tránh ReLU phá hủy thông tin trong không gian ít chiều!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Pointwise $1 \times 1$ expand ($t \times C$) $\to$ Depthwise $3 \times 3$ $\to$ Pointwise $1 \times 1$ projection (linear, no non-linearity). Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** MobileNetV2 vẫn dùng skip connection khi stride = 1 (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 96 [VOAI02-M96] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Độ phức tạp tính toán thời gian và bộ nhớ đệm ma trận của cơ chế Self-Attention chuẩn trong Transformer phụ thuộc vào độ dài chuỗi đầu vào $N$ theo hàm độ phức tạp nào, vốn là điểm nghẽn lớn khi mở rộng ngữ cảnh dài (Long Context)?

- **A.** $O(N \log N)$ theo thuật toán chia để trị tương tự như phép biến đổi Fourier nhanh 1D trên chuỗi thời gian
- **B.** $O(N)$ tuyến tính thuần túy theo chiều dài chuỗi token nhờ cơ chế nén trạng thái ẩn cục bộ theo từng cửa sổ
- **C.** $O(N^2)$ bậc hai đối với chiều dài chuỗi, do phải tính ma trận tích tương quan giữa mọi cặp token $(i, j)$
- **D.** $O(2^N)$ theo cấp số nhân bùng nổ tổ hợp do không gian trạng thái của từ vựng tăng theo hàm mũ đa biến

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mỗi từ trong câu phải nhìn ngắm và bắt tay với tất cả các từ khác trong câu. Nếu câu có $N$ từ, tổng số cái bắt tay là $N \times N = N^2$. Khi câu dài gấp 10 lần (từ 1k lên 10k token), ma trận chú ý phình to gấp 100 lần, làm cạn kiệt bộ nhớ VRAM của GPU!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ma trận điểm tương đồng $S = \frac{Q K^T}{\sqrt{d_k}} \in \mathbb{R}^{N \times N}$. Thời gian và bộ nhớ đều là $O(N^2 d)$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Attention chuẩn là $O(N^2)$, các biến thể Linear Attention mới đạt $O(N)$ nhưng bị giảm sút chất lượng biểu diễn.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 97 [VOAI02-M97] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cơ chế mã hóa vị trí tương đối RoPE (Rotary Position Embedding) được áp dụng phổ biến trong các mô hình LLM hiện đại (như LLaMA, Mistral) bằng phép toán đại số nào trên các cặp tọa độ 2D của vector truy vấn $q$ và khóa $k$?

- **A.** Cộng trực tiếp vector vị trí vào vector nhúng token ban đầu theo phép cộng affine trước khi qua các khối Transformer
- **B.** Nhân với ma trận quay trực giao 2D $R_{\Theta, m}$, biến tích vô hướng giữa $q_m$ và $k_n$ phụ thuộc vào khoảng cách tương đối $m - n$
- **C.** Chia tọa độ vector cho chỉ số vị trí để làm suy giảm biên độ tín hiệu theo hàm logarit tự nhiên của độ dài ngữ cảnh
- **D.** Ánh xạ vector qua một mạng nơ-ron nhiều tầng MLP phi tuyến tính độc lập để dự đoán ma trận tương quan vị trí không gian

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Thay vì cộng thêm số (như Positional Encoding cũ), RoPE xoay vector trong mặt phẳng 2D một góc tỉ lệ với vị trí $m$. Khi hai vector xoay một góc $\theta_m$ và $\theta_n$, tích vô hướng giữa chúng chỉ phụ thuộc vào góc chênh lệch $\theta_m - \theta_n = \theta(m - n)$. Máy tính biết ngay khoảng cách tương đối giữa hai từ mà không lo tràn vị trí tuyệt đối!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\langle R_{\Theta, m} q, R_{\Theta, n} k \rangle = q^T R_{\Theta, n-m} k = g(q, k, m-n)$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A là Absolute Positional Encoding truyền thống (như trong BERT / Transformer gốc).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 98 [VOAI02-M98] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán FlashAttention tăng tốc tính toán Self-Attention và giảm mạnh bộ nhớ VRAM bằng kỹ thuật tối ưu hóa phần cứng GPU cốt lõi nào?

- **A.** Chuyển toàn bộ dữ liệu từ bộ nhớ GPU sang ổ đĩa cứng NVMe (Host Offloading) để giải phóng băng thông truyền thông tin
- **B.** Chia nhỏ ma trận thành các khối (Tiling), tính trên SRAM nhanh và dùng Online Softmax để không ghi ma trận $N \times N$ ra HBM
- **C.** Bỏ qua hoàn toàn phép tính Softmax (Softmax Free) và thay bằng phép chuẩn hóa $L_2$ tuyến tính nhằm giảm thiểu độ phức tạp
- **D.** Giảm độ phân giải trọng số Query và Key xuống còn 1 bit nguyên (1-bit Quantization) bằng kỹ thuật nhị phân hóa ma trận

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
GPU tính toán cực nhanh nhưng việc đọc/ghi dữ liệu vào bộ nhớ chính (HBM) rất chậm. Attention truyền thống phải ghi cả ma trận khổng lồ $N \times N$ ra HBM rồi đọc lại để tính Softmax. FlashAttention chia nhỏ thành các miếng gạch (Tiling), bốc vào bộ nhớ con SRAM siêu tốc nằm ngay sát nhân tính toán, tính gộp luôn Softmax và nhân ma trận mà không bao giờ ghi ma trận $N \times N$ ra ngoài!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 IO-Aware Attention: giảm số lần truy xuất HBM từ $O(N^2)$ xuống $O(N^2 d / M)$ với $M$ là kích thước SRAM. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** FlashAttention tính toán chính xác 100% kết quả chuẩn (Exact Attention), không phải xấp xỉ hay bỏ Softmax (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 99 [VOAI02-M99] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kỹ thuật tinh chỉnh tham số hiệu quả LoRA (Low-Rank Adaptation), ma trận cập nhật trọng số $\Delta W \in \mathbb{R}^{d \times k}$ được phân rã thành tích của hai ma trận hạng thấp $\Delta W = B \cdot A$ với rank $r \ll \min(d, k)$. Khẳng định nào sau đây là chính xác về cách khởi tạo trọng số ban đầu của $A$ và $B$?

- **A.** Cả hai ma trận $A$ và $B$ đều được khởi tạo bằng ma trận đơn vị đối xứng nhằm bảo toàn giá trị kích hoạt ban đầu
- **B.** Ma trận $A$ khởi tạo ngẫu nhiên theo phân phối Gauss và ma trận $B$ khởi tạo bằng 0, đảm bảo $\Delta W = 0$ khi bắt đầu huấn luyện
- **C.** Cả hai ma trận $A$ và $B$ đều được khởi tạo bằng ma trận số 1 toàn phần để duy trì độ dốc gradient đồng đều
- **D.** Ma trận $A$ khởi tạo bằng 0 và ma trận $B$ khởi tạo bằng ma trận trực giao nghịch đảo để triệt tiêu phương sai ban đầu

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi mới cắm module LoRA vào mô hình gốc, mô hình phải hoạt động y nguyên như cũ, chưa bị biến đổi gì cả. Vì vậy, ta bắt buộc phải có $\Delta W = B \cdot A = 0$. Bằng cách đặt $B = 0$ và $A$ lấy ngẫu nhiên theo Gauss, tích $B \cdot A$ ban đầu bằng đúng 0 tuyệt đối, sau đó gradient sẽ giúp nó học dần dần!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $A \sim \mathcal{N}(0, \sigma^2), B = 0 \implies \Delta W = B A = 0$ tại $t=0$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nếu cả hai đều khởi tạo khác 0 (loại A, C), mô hình bị sốc ngay ở epoch đầu tiên vì $\Delta W \ne 0$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 100 [VOAI02-M100] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Mô hình Đa Chuyên gia Thưa (Sparse Mixture of Experts - MoE như Mixtral 8x7B), hàm mất mát phụ cân bằng tải (Auxiliary Load Balancing Loss) được bổ sung vào hàm mục tiêu huấn luyện nhằm giải quyết vấn đề kỹ thuật nào?

- **A.** Ép toàn bộ các chuyên gia phải có chung một ma trận trọng số Feed-Forward Network để giảm thiểu số lượng tham số lưu trữ
- **B.** Ngăn chặn hiện tượng Routing Collapse: mạng dồn token cho một vài chuyên gia ưa thích và bỏ đói các chuyên gia khác
- **C.** Tự động tắt nguồn các chip GPU không tham gia tính toán để tiết kiệm điện năng tiêu thụ trong quá trình huấn luyện cụm
- **D.** Chuyển đổi kiến trúc MoE từ thưa thớt (Sparse) thành mô hình đậm đặc (Dense) toàn phần nhằm tăng cường độ chính xác

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Bộ định tuyến Router bốc 2 chuyên gia giỏi nhất cho mỗi token. Nếu một chuyên gia ban đầu hơi nhỉnh hơn một chút, router sẽ liên tục gửi bài cho chuyên gia đó giải, khiến chuyên gia đó ngày càng giỏi hơn trong khi các chuyên gia còn lại không có bài để học và ' chết dần ' (Routing Collapse). Hàm Load Balancing Loss phạt nặng router nếu nó không chia đều việc cho tất cả chuyên gia!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mathcal{L}_{\text{aux}} = \alpha N \sum_{i=1}^E f_i P_i$, phạt khi tích giữa tỷ lệ token được gán $f_i$ và xác suất router $P_i$ bị lệch. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** MoE không gộp trọng số chuyên gia (loại A) và không liên quan đến tắt nguồn phần cứng (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---
