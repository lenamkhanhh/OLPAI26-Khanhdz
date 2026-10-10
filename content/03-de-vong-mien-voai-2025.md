# ĐỀ THI 03: MÔ PHỎNG ĐỀ THI OLYMPIC TRÍ TUỆ NHÂN TẠO QUỐC GIA VOAI (104 CÂU)
## 100 Câu Trắc Nghiệm Chuẩn Hóa (100.0đ) & 4 Bài Tự Luận Giải Pháp AI Thực Chiến (40.0đ)

> **Nguồn gốc học thuật:** Ngân hàng đề thi mô phỏng chuẩn cấu trúc kỳ thi Olympic AI Quốc gia (VOAI).
> **Tuyên bố minh bạch:** Bộ câu hỏi được tái tạo và chuẩn hóa với sự trợ giúp của AI (Gemini) dựa trên các chuyên đề ôn thi vòng trường, không phải nguyên bản 100 câu chính thức từ Thầy Đỗ Đình Luật.

---

### Câu 01 [VOAI03-M01] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho ma trận vuông $A$ kích thước $n \times n$. Nếu $A$ là ma trận trực giao (orthogonal matrix), phát biểu nào sau đây là ĐÚNG?

- **A.** Các cột của $A$ phụ thuộc tuyến tính
- **B.** $A^T = A^{-1}$
- **C.** Định thức của $A$ luôn bằng 0 ($\det(A) = 0$)
- **D.** $A$ là ma trận suy biến (singular matrix)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Ma trận trực giao (Orthogonal Matrix):** Ma trận vuông $A$ thỏa mãn $A^T A = A A^T = I$. Các vector cột/hàng có độ dài bằng 1 và đôi một vuông góc nhau.
- **Ma trận nghịch đảo ($A^{-1}$):** Ma trận thỏa mãn $A A^{-1} = I$.
- **Ma trận chuyển vị ($A^T$):** Ma trận đổi hàng thành cột.

🍼 **Hình dung thực tế cho em bé:**
Ma trận trực giao giống hệt như một phép xoay khối rubik trong không gian 3 chiều: Nó chỉ xoay góc nhìn chứ hoàn toàn không bóp méo, không kéo dãn hay thu nhỏ vật thể. Vì thế, muốn quay ngược trở lại vị trí ban đầu ($A^{-1}$), bạn chỉ cần lật ngược phép xoay đó (chính là ma trận chuyển vị $A^T$).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Theo định nghĩa chuẩn: $A^T A = I$.
Nhân cả hai vế từ bên phải với $A^{-1}$:
$$(A^T A) A^{-1} = I A^{-1} \iff A^T (A A^{-1}) = A^{-1} \iff A^T I = A^{-1} \iff A^T = A^{-1}$$
Lấy định thức hai vế: $\det(A^T A) = \det(A^T) \det(A) = [\det(A)]^2 = \det(I) = 1 \implies \det(A) = \pm 1 \ne 0$.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Phụ thuộc tuyến tính):** Sai, các cột trực giao với nhau nên độc lập tuyến tính tuyệt đối.
- **Phương án C (Định thức bằng 0):** Sai, $\det(A) = \pm 1$, không thể bằng 0.
- **Phương án D (Ma trận suy biến):** Sai, do $\det(A) \ne 0$ nên $A$ luôn khả nghịch, không suy biến.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§5.3 Đại số tuyến tính trong AI**.
🔗 **Liên hệ bài cũ:** Trong Deep Learning, phép khởi tạo trọng số trực giao (Orthogonal Initialization) giúp ngăn chặn hiện tượng bùng nổ/triệt tiêu gradient (Vanishing/Exploding Gradient) ở các tầng sâu (xem thêm câu C15 Đề 01).

---

### Câu 02 [VOAI03-M02] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong tối ưu hóa đa biến, nếu ma trận Hessian $H = \nabla^2 f(x^*)$ của hàm số tại điểm dừng $\nabla f(x^*) = 0$ là xác định dương (positive definite), điểm $x^*$ đó là:

- **A.** Điểm cực đại địa phương (Local maximum)
- **B.** Điểm không xác định
- **C.** Điểm cực tiểu địa phương (Local minimum)
- **D.** Điểm yên ngựa (Saddle point)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Ma trận Hessian ($H = \nabla^2 f(x)$):** Ma trận vuông chứa toàn bộ đạo hàm riêng bậc hai của hàm nhiều biến, đo độ cong của hàm số theo mọi hướng.
- **Ma trận xác định dương (Positive Definite, $H \succ 0$):** Ma trận có mọi trị riêng $\lambda_i > 0$, tức $\Delta x^T H \Delta x > 0$ với mọi vector khác không $\Delta x \ne 0$.
- **Điểm dừng (Stationary Point):** Điểm mà đạo hàm bậc nhất bằng 0 ($\nabla f(x^*) = 0$).

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng bạn đang đứng ở đáy của một chiếc bát ăn cơm úp ngửa. Chiếc bát cong lên ở mọi hướng (độ cong đều dương). Bất kể bạn bước sang trái, phải, trước hay sau, độ cao của bạn đều tăng lên. Vì thế đáy bát chính là điểm cực tiểu địa phương (Local Minimum)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khai triển Taylor bậc 2 của hàm $f$ quanh điểm dừng $x^*$:
$$f(x^* + \Delta x) = f(x^*) + \nabla f(x^*)^T \Delta x + \frac{1}{2} \Delta x^T H \Delta x + o(\|\Delta x\|^2)$$
Do $\nabla f(x^*) = 0$, ta có:
$$f(x^* + \Delta x) - f(x^*) \approx \frac{1}{2} \Delta x^T H \Delta x$$
Vì $H$ xác định dương ($H \succ 0$), với mọi $\Delta x \ne 0$ thì $\Delta x^T H \Delta x > 0$.
Do đó $f(x^* + \Delta x) > f(x^*)$ trong mọi lân cận nhỏ $\implies x^*$ là cực tiểu địa phương. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Cực đại địa phương):** Sai, cực đại khi $H$ xác định âm ($H \prec 0$, chiếc bát úp ngược).
- **Phương án D (Điểm yên ngựa):** Sai, yên ngựa xảy ra khi $H$ không xác định (Indefinite, có cả trị riêng âm và dương).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§5.2 Tối ưu hóa lồi & Đạo hàm đa biến**.
🔗 **Liên hệ bài cũ:** Trong Deep Learning, các hàm mất mát phức tạp thường gặp rất nhiều điểm yên ngựa (Saddle Points) chứ không phải cực tiểu địa phương, đó là lý do các optimizer như Adam hay Momentum cần quán tính để vượt qua điểm yên ngựa.

---

### Câu 03 [VOAI03-M03] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Tính đạo hàm bậc nhất của hàm số $f(x) = \ln(1 + e^{-x})$. Kết quả nào sau đây là ĐÚNG (với $\sigma(x) = \frac{1}{1 + e^{-x}}$)?

- **A.** $f '(x) = \sigma(x) - 1$
- **B.** $f '(x) = 1 + \sigma(x)$
- **C.** $f '(x) = \sigma(x)$
- **D.** $f '(x) = e^{-x}$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Hàm Sigmoid ($\sigma(x)$):** $\sigma(x) = \frac{1}{1 + e^{-x}}$, đưa giá trị thực bất kỳ về khoảng $(0, 1)$.
- **Đạo hàm hàm hợp (Chain Rule):** $[\ln(u)]' = \frac{u '}{u}$.

🍼 **Hình dung thực tế cho em bé:**
Hàm số này chính là hàm Softplus biến thể: $f(x) = \ln(1 + e^{-x})$. Ta chỉ việc áp dụng quy tắc đạo hàm lớp 12: Đạo hàm của $\ln(u)$ là $u '/u$, rồi biến đổi khéo léo một chút để đưa về dạng quen thuộc của hàm kích hoạt Sigmoid mà mạng nơ-ron hay dùng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Đặt $u = 1 + e^{-x} \implies u ' = -e^{-x}$.
$$f '(x) = \frac{u '}{u} = \frac{-e^{-x}}{1 + e^{-x}}$$
Nhân cả tử và mẫu với $e^x$:
$$f '(x) = \frac{-e^{-x} \cdot e^x}{(1 + e^{-x}) \cdot e^x} = \frac{-1}{e^x + 1} = -\frac{1}{1 + e^x}$$
Nhớ rằng $\sigma(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{1 + e^x}$.
Do đó: $\sigma(x) - 1 = \frac{e^x}{1 + e^x} - 1 = \frac{e^x - (1 + e^x)}{1 + e^x} = -\frac{1}{1 + e^x} = f '(x)$.
Vậy $f '(x) = \sigma(x) - 1$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B ($f '(x) = \sigma(x)$):** Quên dấu trừ của đạo hàm $e^{-x}$.
- **Phương án C & D:** Biến đổi nhầm lẫn giữa logarit tự nhiên và hàm mũ.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.2 Các hàm kích hoạt & Đạo hàm trong Deep Learning**.
🔗 **Liên hệ bài cũ:** Hàm Softplus $\text{Softplus}(x) = \ln(1 + e^x)$ là phiên bản làm mịn (smooth approximation) của hàm ReLU. Đạo hàm của $\text{Softplus}(x)$ chính là hàm Sigmoid $\sigma(x)$!

---

### Câu 04 [VOAI03-M04] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Đại lượng nào trong lý thuyết thông tin đo lường mức độ ' bất ngờ ' trung bình hoặc độ hỗn loạn của một phân phối xác suất rời rạc?

- **A.** Kỳ vọng (Expectation)
- **B.** Độ lệch chuẩn (Standard Deviation)
- **C.** Entropy (Shannon Entropy)
- **D.** Phương sai (Variance)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Shannon Entropy ($H(X)$):** Thước đo mức độ hỗn loạn, bất định (uncertainty) hoặc lượng thông tin trung bình chứa trong một phân phối xác suất.
- **Đơn vị Entropy:** Dùng $\log_2$ đo bằng **bit** (shannon); dùng $\ln$ đo bằng **nat**; dùng $\log_{10}$ đo bằng **hartley**.
- **Kỳ vọng & Phương sai:** Đo độ lệch tâm và độ phân tán của giá trị số học, không đo mức độ hỗn loạn thông tin.

🍼 **Hình dung thực tế cho em bé:**
Entropy giống như việc đoán xem một đồng xu tung lên sẽ ra mặt ngửa hay sấp: Nếu đồng xu 2 mặt đều có cơ hội 50-50, bạn hoàn toàn không đoán trước được (độ bất định tối đa $\implies$ Entropy cao nhất = 1 bit). Nhưng nếu đồng xu bị làm giả cả 2 mặt đều ngửa, bạn biết chắc chắn kết quả $\implies$ không có gì bất ngờ cả (Entropy = 0 bit).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Shannon Entropy cho biến ngẫu nhiên rời rạc $X$ có $C$ trạng thái:
$$H(X) = -\sum_{i=1}^C p_i \log_2(p_i)$$
Quy ước $0 \log_2(0) = 0$. $H(X)$ đạt cực tiểu bằng $0$ khi một lớp có xác suất $p=1$ (thuần khiết), đạt cực đại $\log_2(C)$ khi phân phối đều $p_i = 1/C$. Chọn **C** (Entropy).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Kỳ vọng):** Kỳ vọng chỉ là giá trị trung bình cộng theo xác suất, không đo mức độ hỗn loạn hay lượng thông tin xác suất.
- **Phương án D (Phương sai):** Phương sai chỉ đo độ phân tán của giá trị số học quanh kỳ vọng, phụ thuộc vào thang đo (scale), không đo mức độ bất định thông tin.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.3 Cây quyết định, Entropy & Information Gain**.
🔗 **Liên hệ bài cũ:** Ở câu B04 Đề 01, ta đã tính tay Entropy cho tập 10 mẫu (4 Chó, 6 Mèo). Thuật toán ID3 dùng hiệu số Entropy (Information Gain) để chọn thuộc tính phân chia tốt nhất.

---

### Câu 05 [VOAI03-M05] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán k-Nearest Neighbors (k-NN), khi giá trị tham số $k$ quá nhỏ (ví dụ $k=1$), mô hình có xu hướng:

- **A.** Bị Overfitting (High Variance), ranh giới phân chia ôm sát từng điểm và cực kỳ nhạy cảm với nhiễu
- **B.** Bị Underfitting (High Bias), ranh giới phân chia phẳng mượt và thiên vị lớp đa số toàn cục
- **C.** Bảo toàn phương sai tối ưu, ranh giới phân chia có khoảng cách lề cực đại tương đương SVM
- **D.** Đạt khả năng tổng quát hóa lý tưởng nhất trên tập kiểm thử độc lập mà không cần điều chuẩn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Thuật toán k-NN (k-Nearest Neighbors):** Thuật toán học lười (Lazy Learner), phân loại điểm mới dựa trên đa số $k$ điểm láng giềng gần nhất trong không gian đặc trưng.
- **Overfitting (Quá khớp / High Variance):** Mô hình ghi nhớ quá chi tiết tập huấn luyện, nhạy cảm với từng điểm nhiễu ngoại lai.
- **Underfitting (Thiếu khớp / High Bias):** Mô hình quá đơn giản, bỏ qua các quy luật phức tạp.

🍼 **Hình dung thực tế cho em bé:**
Khi $k=1$, mô hình chỉ nghe lời 1 người bạn gần nhất. Nếu người bạn đó tình cờ là một điểm dữ liệu bị gán nhãn nhầm (nhiễu), mô hình sẽ tin ngay lập tức! Ranh giới phân chia sẽ bị ngoằn ngoèo, gập ghềnh để bao bọc từng điểm nhiễu đơn lẻ $\implies$ Overfitting.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 - Khi $k=1$: Ranh giới quyết định tạo thành biểu đồ Voronoi phân mảnh cực kỳ phức tạp. Training error = 0, nhưng Test error rất lớn $\implies$ Variance cao, Bias thấp (Overfitting). Chọn **A**.
- Khi $k \to N$: Ranh giới mượt mà, luôn dự đoán lớp chiếm đa số trong toàn bộ dữ liệu $\implies$ Variance thấp, Bias cao (Underfitting).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Underfitting):** Ngược lại, $k$ quá lớn mới bị Underfitting.
- **Phương án D (Luôn chính xác nhất):** Sai hoàn toàn, $k=1$ rất dễ đoán sai trên dữ liệu kiểm thử do nhiễu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)**.
🔗 **Liên hệ bài cũ:** Trong cẩm nang §1.1, nguyên tắc vàng khi chọn $k$ là chọn số lẻ (với bài toán 2 lớp) để tránh hòa vote, và dùng Cross-Validation để tìm $k$ tối ưu (thường từ 3 đến 15).

---

### Câu 06 [VOAI03-M06] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán nào sau đây KHÔNG thuộc nhóm học có giám sát (Supervised Learning)?

- **A.** Logistic Regression
- **B.** Support Vector Machine (SVM)
- **C.** Principal Component Analysis (PCA)
- **D.** Random Forest

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Học có giám sát (Supervised Learning):** Dữ liệu có cả đặc trưng đầu vào $X$ và nhãn mục tiêu $y$ (Labels). Mô hình học ánh xạ $f(X) \to y$.
- **Học không giám sát (Unsupervised Learning):** Dữ liệu chỉ có $X$, không có nhãn $y$. Mục tiêu là tìm cấu trúc ẩn, gom cụm (Clustering) hoặc giảm chiều (Dimensionality Reduction).
- **PCA (Principal Component Analysis):** Kỹ thuật giảm chiều tuyến tính không giám sát bằng cách chiếu dữ liệu lên các trục có phương sai cực đại.

🍼 **Hình dung thực tế cho em bé:**
Học có giám sát giống như làm bài tập có sẵn sách giải ở trang cuối (biết đáp án đúng để đối chiếu). Còn PCA giống như việc bạn tự nhìn vào một tủ sách lộn xộn để gom các cuốn sách lại gọn gàng hơn mà không có ai chỉ bảo trước cuốn nào thuộc thể loại gì.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 PCA tìm các vector riêng (Eigenvectors) của ma trận hiệp phương sai $\Sigma = \frac{1}{N} X^T X$ ứng với các trị riêng lớn nhất. Quá trình này hoàn toàn không dùng và không cần bất kỳ nhãn mục tiêu $y$ nào. Chọn **C** (PCA).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **SVM, Random Forest, Logistic Regression:** Đều là các thuật toán học có giám sát kinh điển cần nhãn $y$ để tối ưu hàm mất mát.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.7 Giảm chiều dữ liệu: PCA & t-SNE**.
🔗 **Liên hệ bài cũ:** Khác với PCA (không giám sát), kỹ thuật LDA (Linear Discriminant Analysis) cũng là giảm chiều tuyến tính nhưng là học CÓ GIÁM SÁT vì tìm trục chiếu tối đa hóa khoảng cách giữa các lớp.

---

### Câu 07 [VOAI03-M07] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Mục tiêu cốt lõi của kỹ thuật ' Pruning ' (tỉa cành) trong cây quyết định là gì?

- **A.** Tăng số lượng nút lá để mở rộng dung lượng biểu diễn của cây phân loại trên không gian nhiều chiều
- **B.** Tăng độ sâu tối đa để đảm bảo mọi mẫu trong tập huấn luyện đều được phân loại chính xác 100%
- **C.** Giảm hiện tượng Overfitting bằng cách loại bỏ các nhánh con học nhiễu và làm giảm phương sai
- **D.** Chuyển đổi cây quyết định đơn lẻ thành mô hình rừng ngẫu nhiên có trọng số thông qua bagging

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Pruning (Tỉa cành cây quyết định):** Kỹ thuật loại bỏ bớt các nhánh con hoặc nút lá không quan trọng trên cây quyết định.
- **Pre-pruning (Dừng sớm):** Giới hạn độ sâu tối đa (`max_depth`), số mẫu tối thiểu ở nút lá (`min_samples_leaf`).
- **Post-pruning (Tỉa sau):** Để cây mọc tự do rồi cắt tỉa dựa trên hàm chi phí độ phức tạp (Cost-Complexity Pruning).

🍼 **Hình dung thực tế cho em bé:**
Cây quyết định giống như một cái cây ngoài vườn. Nếu bạn để nó mọc um tùm không cắt tỉa, cành lá sẽ đâm vào từng ngóc ngách nhỏ (học thuộc lòng từng chi tiết vụn vặt và nhiễu trong dữ liệu). ' Tỉa cành ' là cắt bỏ những nhánh con rườm rà đó đi để cây gọn gàng, khỏe mạnh và khái quát hóa tốt hơn cho tương lai $\implies$ Giảm Overfitting!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Hàm mục tiêu của Cost-Complexity Pruning (tham số $\alpha$):
$$R_\alpha(T) = R(T) + \alpha |T|$$
Trong đó $R(T)$ là tổng sai số trên tập dữ liệu của cây $T$, $|T|$ là số lượng nút lá, $\alpha \ge 0$ là hệ số phạt độ phức tạp. Khi $\alpha$ tăng, cây buộc phải tỉa bớt các nút lá để giảm Overfitting. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A & D:** Tỉa cành làm GIẢM độ sâu và làm cây ĐƠN GIẢN HƠN, không phải làm phức tạp hơn.
- **Phương án C:** Tỉa cành làm GIẢM số nút lá, không phải tăng.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.3 Cây quyết định, Entropy & Information Gain**.
🔗 **Liên hệ bài cũ:** Cây quyết định không tỉa cành có thể đạt độ chính xác 100% trên tập train nhưng sẽ sụp đổ trên tập test. Đó là lý do trong Scikit-Learn luôn khuyến nghị đặt `max_depth` hoặc dùng `ccp_alpha`.

---

### Câu 08 [VOAI03-M08] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán Random Forest kết hợp nhiều cây quyết định bằng phương pháp Ensemble nào?

- **A.** Boosting (Huấn luyện tuần tự)
- **B.** Stacking (Meta-Learner xếp chồng)
- **C.** Bagging (Bootstrap Aggregating)
- **D.** Cascading (Phân cấp điều kiện)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Ensemble Learning (Học kết hợp):** Phương pháp kết hợp nhiều mô hình yếu (Weak Learners) để tạo thành mô hình mạnh (Strong Learner).
- **Bagging (Bootstrap Aggregating):** Lấy mẫu lặp lại (Bootstrap) để huấn luyện song song nhiều mô hình độc lập, sau đó lấy trung bình hoặc vote đa số. Giúp giảm phương sai (Variance).
- **Boosting:** Huấn luyện tuần tự các mô hình, mô hình sau tập trung sửa sai cho mô hình trước. Giúp giảm độ chệch (Bias).
- **Random Forest:** Thuật toán kết hợp Bagging của nhiều cây quyết định với cơ chế chọn ngẫu nhiên tập con đặc trưng (Feature Subsampling).

🍼 **Hình dung thực tế cho em bé:**
Random Forest giống như việc bạn muốn chẩn đoán một ca bệnh khó: Thay vì hỏi 1 bác sĩ duy nhất (có thể nhìn nhận chủ quan), bạn hỏi ý kiến của 100 bác sĩ độc lập (Bagging). Mỗi bác sĩ được xem một tập hồ sơ bệnh án khác nhau và một nhóm chỉ số xét nghiệm khác nhau. Sau đó cả 100 bác sĩ bỏ phiếu vote đa số. Quyết định tập thể này sẽ cực kỳ khách quan và khó bị sai lệch!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Với $B$ cây quyết định độc lập có phương sai $\sigma^2$ và hệ số tương quan $\rho$, phương sai của dự đoán kết hợp là:
$$\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$$
Khi $B \to \infty$, thành phần thứ hai tiến về 0. Random Forest giảm thêm $\rho$ nhờ ngẫu nhiên hóa đặc trưng tại mỗi điểm cắt ($m = \sqrt{p}$). Chọn **C** (Bagging).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Boosting):** Là cơ chế của AdaBoost, Gradient Boosting, XGBoost, LightGBM (huấn luyện tuần tự), không phải Random Forest.
- **Phương án C (Stacking):** Huấn luyện mô hình meta kết hợp dự đoán của các mô hình khác loại.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Ở câu C03 Đề 01, ta đã phân biệt rõ: Bagging chạy song song độc lập (giảm Variance), còn Boosting chạy tuần tự (giảm Bias).

---

### Câu 09 [VOAI03-M09] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Chỉ số $F_1$-Score là trung bình điều hòa của hai đại lượng nào?

- **A.** Specificity và Sensitivity
- **B.** Precision và Recall
- **C.** Precision và Accuracy
- **D.** Accuracy và Recall

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Precision (Độ chuẩn xác):** Trong số những mẫu mô hình đoán là Dương tính, có bao nhiêu mẫu thật sự Dương tính ($TP / (TP + FP)$).
- **Recall (Độ nhạy / Thu hồi):** Trong số những mẫu thật sự Dương tính ngoài đời, mô hình bắt được bao nhiêu mẫu ($TP / (TP + FN)$).
- **F1-Score:** Trung bình điều hòa (Harmonic Mean) giữa Precision và Recall.

🍼 **Hình dung thực tế cho em bé:**
Precision trả lời câu hỏi: ' Bắt nhầm hay không?' (bắn 10 phát trúng mấy phát). Recall trả lời câu hỏi: ' Bỏ sót hay không?' (trong 10 con mồi bắt được mấy con). $F_1$-Score là cây cầu hòa giải công bằng nhất giữa hai mục tiêu này. Nó dùng trung bình điều hòa để phạt nặng nếu mô hình chỉ giỏi 1 bên mà bỏ bê bên kia!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức trung bình điều hòa:
$$F_1 = \frac{2}{\frac{1}{\text{Precision}} + \frac{1}{\text{Recall}}} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$
Nếu một trong hai chỉ số bằng 0, $F_1$ sẽ lập tức sụp đổ về 0. Chọn **B** (Precision và Recall).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A & B:** Nhầm lẫn với Accuracy (Độ chính xác toàn thể: $(TP+TN)/Total$). Trên tập dữ liệu lệch lớp, Accuracy hoàn toàn vô dụng.
- **Phương án D:** Specificity là độ đặc hiệu ($TN / (TN + FP)$).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.6 Các chỉ số đánh giá mô hình (Metrics)**.
🔗 **Liên hệ bài cũ:** Trong đề thi OLP AI 2025 Vòng Sơ loại (Tác vụ 2 Nhận diện ngôn ngữ ký hiệu), BTC đã dùng chính xác chỉ số **Macro-F1** (trung bình F1 của 50 lớp cử chỉ) làm metric chấm điểm chính thức!

---

### Câu 10 [VOAI03-M10] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong Hồi quy tuyến tính, nếu các biến độc lập có tương quan tuyến tính rất mạnh với nhau, hiện tượng này gọi là:

- **A.** Nhiễu trắng (White Noise)
- **B.** Phương sai thay đổi (Heteroscedasticity)
- **C.** Đa cộng tuyến (Multicollinearity)
- **D.** Tự tương quan (Autocorrelation)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Đa cộng tuyến (Multicollinearity):** Hiện tượng hai hoặc nhiều biến độc lập trong mô hình hồi quy tuyến tính có tương quan tuyến tính rất mạnh với nhau.
- **Hậu quả:** Ma trận $X^T X$ gần như suy biến (định thức gần bằng 0), khiến nghịch đảo $(X^T X)^{-1}$ không ổn định, dẫn đến phương sai của trọng số ước lượng $\hat{\beta}$ tăng vọt.
- **Tự tương quan (Autocorrelation):** Tương quan giữa các giá trị của cùng một biến qua các mốc thời gian khác nhau (trong Time Series).

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng bạn làm mô hình dự đoán giá nhà. Bạn đưa vào hai cột: Cột 1 là ' Diện tích tính theo mét vuông ($m^2$)' và Cột 2 là ' Diện tích tính theo centimét vuông ($cm^2$)'. Hai cột này thực chất là một! Mô hình sẽ bị bối rối không biết nên chia trọng số cho cột nào, dẫn đến kết quả trọng số bị nhảy múa lung tung và không đáng tin cậy. Đó gọi là Đa cộng tuyến!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ước lượng OLS: $\hat{\beta} = (X^T X)^{-1} X^T y$.
Ma trận hiệp phương sai của trọng số: $\text{Var}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$.
Khi các cột của $X$ tương quan cao, $\det(X^T X) \approx 0$, các phần tử đường chéo của $(X^T X)^{-1}$ (chỉ số phóng đại phương sai VIF) tiến tới vô cùng. Chọn **C** (Đa cộng tuyến).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Tự tương quan):** Là sai số của các quan sát liên tiếp phụ thuộc nhau (kiểm định bằng Durbin-Watson).
- **Phương án C (Phương sai thay đổi / Heteroskedasticity):** Phương sai sai số không đồng đều tại các mức giá trị $X$ khác nhau.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.2 Hồi quy tuyến tính & Regularization L1/L2**.
🔗 **Liên hệ bài cũ:** Để chữa hiện tượng đa cộng tuyến, kỹ thuật Ridge Regression (Regularization L2) cộng thêm $\lambda I$ vào $X^T X$ để đảm bảo ma trận luôn khả nghịch ổn định: $\hat{\beta} = (X^T X + \lambda I)^{-1} X^T y$.

---

### Câu 11 [VOAI03-M11] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Hàm mất mát chuẩn mực được dùng cho bài toán Logistic Regression nhị phân là:

- **A.** Mean Squared Error (MSE)
- **B.** Hinge Loss
- **C.** Binary Cross-Entropy (Log Loss)
- **D.** Huber Loss

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Logistic Regression:** Mô hình phân loại tuyến tính dùng hàm Sigmoid để ánh xạ tổ hợp tuyến tính thành xác suất $p = \sigma(w^T x + b)$.
- **Binary Cross-Entropy Loss (BCE / Log Loss):** Hàm mất mát xuất phát từ nguyên lý Ước lượng hợp lý cực đại (MLE) cho phân phối Bernoulli.
- **Hinge Loss:** Hàm mất mát của Support Vector Machine (SVM) tối đa hóa lề (Margin).
- **Huber Loss:** Hàm mất mát kết hợp MSE và MAE cho bài toán Hồi quy, chống ngoại lai (Outliers).

🍼 **Hình dung thực tế cho em bé:**
Tại sao không dùng sai số bình phương MSE cho Logistic Regression? Vì khi lồng hàm cong Sigmoid vào bình phương MSE, đồ thị hàm mất mát sẽ bị mấp mô lồi lõm (Non-convex) có nhiều hố sâu cục bộ, khiến Gradient Descent bị kẹt lại. Log Loss (Binary Cross-Entropy) dùng logarit để ' nắn thẳng ' độ dốc, tạo thành một chiếc bát lồi hoàn hảo (Convex) giúp mô hình trượt một mạch xuống đáy tối ưu toàn cục!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Hàm Binary Cross-Entropy cho mẫu $(x, y)$ với $y \in \{0, 1\}$ và dự đoán $\hat{y} = \sigma(z)$:
$$\mathcal{L}(y, \hat{y}) = -\left[ y \ln(\hat{y}) + (1 - y) \ln(1 - \hat{y}) \right]$$
Đạo hàm theo đầu ra tuyến tính $z = w^T x + b$ cực kỳ thanh thoát:
$$\frac{\partial \mathcal{L}}{\partial z} = \hat{y} - y$$
Đây chính là độ chênh lệch giữa xác suất dự đoán và nhãn thực tế. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (MSE):** Chỉ dùng cho Hồi quy (Regression), dùng cho Logistic sẽ bị Non-convex.
- **Phương án C (Hinge Loss):** Dùng cho SVM: $\mathcal{L} = \max(0, 1 - y \cdot f(x))$ với $y \in \{-1, +1\}$.
- **Phương án D (Huber Loss):** Dùng cho hồi quy bền vững (Robust Regression).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.4 Hàm mất mát (Loss Functions)**.
🔗 **Liên hệ bài cũ:** Trong PyTorch, luôn ưu tiên dùng `nn. BCEWithLogitsLoss()` thay vì gọi `nn. Sigmoid()` rồi `nn. BCELoss()` để tận dụng thủ thuật Log-Sum-Exp ổn định số học (xem câu C06 Đề 01).

---

### Câu 12 [VOAI03-M12] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho ma trận nhầm lẫn: $\text{TP}=80, \text{FP}=10, \text{FN}=20, \text{TN}=90$. Precision của mô hình là:

- **A.** 0.89
- **B.** 0.80
- **C.** 0.90
- **D.** 0.75

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Confusion Matrix (Ma trận nhầm lẫn):** Bảng thống kê kết quả phân loại gồm 4 ô: TP (Đúng dương), FP (Báo nhầm dương), FN (Bỏ sót dương), TN (Đúng âm).
- **Precision (Độ chuẩn xác):** Tỉ lệ đoán đúng trong toàn bộ các ca bị mô hình dán nhãn Dương tính: $\text{Precision} = \frac{TP}{TP + FP}$.

🍼 **Hình dung thực tế cho em bé:**
Đề bài cho: Đội tuần tra bắt được 80 tên trộm thật ($TP=80$), nhưng bắt nhầm 10 người dân vô tội ($FP=10$). Hỏi: Trong tất cả những người bị còng tay ($80 + 10 = 90$ người), có bao nhiêu phần trăm là trộm thật? Lấy $80 / 90 \approx 88.89\% \approx 0.888$. Chọn **A** (0.88).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thay số trực tiếp từ đề bài:
$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} = \frac{80}{80 + 10} = \frac{80}{90} \approx 0.8889 \approx 0.88$$
Chọn đáp án **A**.
Để đối chiếu:
$$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} = \frac{80}{80 + 20} = \frac{80}{100} = 0.80$$
$$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total}} = \frac{80 + 90}{80 + 10 + 20 + 90} = \frac{170}{200} = 0.85$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (0.80):** Đây là giá trị của **Recall** ($80/100$), thí sinh đọc không kỹ đề sẽ bấm nhầm sang Recall.
- **Phương án C (0.75):** Số gây nhiễu.
- **Phương án D (0.90):** Mẫu số $TP + FP = 90$, thí sinh chia nhầm cho 100 ra 0.9.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.6 Các chỉ số đánh giá mô hình (Metrics)**.
🔗 **Liên hệ bài cũ:** Ở câu B07 Đề 01, ta đã thực hành tính đủ bộ tứ Precision, Recall, Specificity và F1 trên ma trận nhầm lẫn y tế.

---

### Câu 13 [VOAI03-M13] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Tại sao hàm kích hoạt phi tuyến là bắt buộc trong mạng nơ-ron nhiều tầng?

- **A.** Để tăng tốc độ tính toán lan truyền thuận bằng cách loại bỏ các phép nhân ma trận dày
- **B.** Để thay thế hoàn toàn kỹ thuật điều chuẩn Dropout trong quá trình huấn luyện mạng sâu
- **C.** Để giới hạn biên độ các vector trọng số nằm nghiêm ngặt trong quả cầu đơn vị đối xứng
- **D.** Để mạng có thể học và xấp xỉ các ranh giới quyết định phi tuyến tính phức tạp trong dữ liệu

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Hàm kích hoạt phi tuyến (Non-linear Activation Function):** Hàm số $f(z)$ phi tuyến tính (như ReLU, GELU, Sigmoid) đặt sau tầng tuyến tính $z = W x + b$.
- **Tính chất ánh xạ tuyến tính:** Hợp thành của hai hoặc nhiều phép biến đổi tuyến tính liên tiếp vẫn chỉ là MỘT phép biến đổi tuyến tính duy nhất: $W_2 (W_1 x) = (W_2 W_1) x = W_{new} x$.
- **Định lý Xấp xỉ Toàn năng (Universal Approximation Theorem):** Mạng nơ-ron chỉ cần 1 tầng ẩn với hàm kích hoạt phi tuyến là có thể xấp xỉ bất kỳ hàm liên tục nào.

🍼 **Hình dung thực tế cho em bé:**
Nếu bạn không dùng hàm kích hoạt phi tuyến, thì dù bạn xếp 1,000 tầng nơ-ron sâu đến đâu, toàn bộ mạng lưới đó cũng chỉ tương đương với đúng MỘT phép nhân ma trận đơn giản (như một bài toán hồi quy tuyến tính lớp 9)! Thế giới thực đầy những đường cong ranh giới phức tạp; không có hàm kích hoạt phi tuyến, mạng sẽ hoàn toàn bất lực không thể uốn cong ranh giới quyết định.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Giả sử mạng 2 tầng chỉ dùng hàm tuyến tính:
$$h = W_1 x + b_1$$
$$y = W_2 h + b_2 = W_2 (W_1 x + b_1) + b_2 = (W_2 W_1) x + (W_2 b_1 + b_2) = W ' x + b '$$
Toàn bộ kiến trúc sụp đổ về một phương trình tuyến tính bậc nhất duy nhất. Do đó, hàm kích hoạt phi tuyến là điều kiện TIÊN QUYẾT để mạng học các biểu diễn phi tuyến phức tạp. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Chạy nhanh hơn):** Sai, thêm hàm phi tuyến còn tốn thêm phép tính tính toán.
- **Phương án C (Giới hạn trọng số):** Đó là nhiệm vụ của Weight Decay / Regularization, không phải hàm kích hoạt.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.2 Các hàm kích hoạt: ReLU, GELU, Sigmoid & Softmax**.
🔗 **Liên hệ bài cũ:** Xem câu B11 Đề 01: Hàm kích hoạt ReLU $\max(0, x)$ dù có dạng hai đoạn thẳng nhưng là hàm phi tuyến toàn cục, giải quyết triệt để vấn đề sụp đổ tuyến tính.

---

### Câu 14 [VOAI03-M14] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Một lớp Convolution có filter $5 \times 5$, input channels là 3, số lượng filter là 16. Tổng số tham số (không tính bias) là:

- **A.** 384
- **B.** 240
- **C.** 400
- **D.** 1200

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Tầng Convolution (Conv2D):** Tầng tích chập không gian quét bộ lọc trượt trên ảnh.
- **Filter / Kernel:** Khối trọng số kích thước $K_h \times K_w \times C_{in}$.
- **Số tham số (Parameters) của tầng Conv2D:** Mỗi filter chứa $K_h \times K_w \times C_{in}$ trọng số (weights). Có $C_{out}$ filters, nên tổng trọng số là $C_{out} \times (K_h \times K_w \times C_{in})$. Nếu tính cả bias, cộng thêm $C_{out}$.

🍼 **Hình dung thực tế cho em bé:**
Mỗi chiếc ' kính lúp ' (filter) có kích thước $5 \times 5$ và phải soi qua cả 3 lớp màu (Đỏ, Xanh lá, Xanh dương $\implies C_{in}=3$). Như vậy một chiếc kính lúp chứa $5 \times 5 \times 3 = 75$ núm vặn trọng số. Bạn dùng 16 chiếc kính lúp độc lập như vậy $\implies$ Tổng cộng cần $16 \times 75 = 1,200$ tham số!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng công thức số tham số tầng Conv2D (không tính bias):
$$\text{Params} = K_h \times K_w \times C_{in} \times C_{out} = 5 \times 5 \times 3 \times 16 = 25 \times 48 = 1,200$$
Nếu đề bài yêu cầu tính cả bias: $\text{Params}_{\text{with bias}} = 1,200 + 16 = 1,216$.
Đề bài chỉ rõ ' không tính bias ' $\implies 1,200$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (400):** Lấy $5 \times 5 \times 16$ mà quên nhân số kênh đầu vào $C_{in} = 3$.
- **Phương án C (240):** Tính nhầm phép nhân.
- **Lưu ý:** Kích thước không gian ảnh đầu vào ($W, H$) HOÀN TOÀN KHÔNG ảnh hưởng đến số lượng tham số của tầng Conv2D (đặc tính chia sẻ trọng số - Weight Sharing).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§3.1 Convolution, Stride, Padding & Receptive Field**.
🔗 **Liên hệ bài cũ:** Đây là câu hỏi kinh điển luôn xuất hiện ở mọi đề thi VOAI, IOAI và OLP AI. So sánh với tầng Fully Connected (Dense), Conv2D giảm hàng triệu tham số nhờ tính chất chia sẻ trọng số này!

---

### Câu 15 [VOAI03-M15] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong LSTM, cổng (gate) nào quyết định thông tin nào từ trạng thái ô nhớ cũ ($C_{t-1}$) sẽ bị loại bỏ?

- **A.** Forget Gate
- **B.** Input Gate
- **C.** Update Gate
- **D.** Output Gate

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **LSTM (Long Short-Term Memory):** Kiến trúc mạng hồi quy có bộ nhớ dài hạn, giải quyết triệt để hiện tượng tiêu biến gradient (Vanishing Gradient) của RNN truyền thống.
- **Trạng thái ô (Cell State $C_t$):** ' Băng chuyền thông tin ' xuyên suốt chuỗi thời gian.
- **Forget Gate (Cổng quên $f_t$):** Dùng hàm Sigmoid quyết định thông tin nào từ $C_{t-1}$ sẽ được giữ lại (gần 1) hoặc vứt bỏ (gần 0).
- **Input Gate ($i_t$):** Quyết định thông tin mới nào sẽ được ghi vào Cell State.
- **Output Gate ($o_t$):** Quyết định thông tin nào từ Cell State được đưa ra Hidden State $h_t$.

🍼 **Hình dung thực tế cho em bé:**
Cell State giống như một cuốn sổ tay nhật ký ghi chép cuộc đời. Forget Gate đóng vai trò như chiếc ' cục tẩy ': Khi bạn bắt đầu một chương mới (ví dụ chủ ngữ đổi từ ' Anh ấy ' sang ' Cô ấy '), Forget Gate sẽ xóa đi các đại từ nhân xưng cũ không còn liên quan để giải phóng bộ nhớ cho cuốn sổ tay!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Forget Gate tại thời điểm $t$:
$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
Sau đó cập nhật trạng thái ô:
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
Nếu $f_t = 0$, toàn bộ thông tin cũ $C_{t-1}$ bị xóa sạch hoàn toàn; nếu $f_t = 1$, thông tin cũ truyền nguyên vẹn không suy giảm. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Input Gate):** Chọn thông tin MỚI cần nạp vào, không phải xóa thông tin cũ.
- **Phương án C (Output Gate):** Lọc thông tin từ $C_t$ để xuất ra $h_t$.
- **Phương án D (Update Gate):** Tên gọi cổng trong kiến trúc GRU (Gated Recurrent Unit), không phải LSTM chuẩn.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§4.3 RNN, LSTM & GRU**.
🔗 **Liên hệ bài cũ:** Trong GRU (biến thể tinh giản của LSTM), Forget Gate và Input Gate được gộp chung lại thành một cổng duy nhất gọi là **Update Gate** $z_t$ (xem câu C20 Đề 01).

---

### Câu 16 [VOAI03-M16] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Cho đầu vào $W \times H$, filter $K \times K$, padding $P$, stride $S$. Công thức tính kích thước đầu ra $W_{out}$ là:

- **A.** $\lfloor (W - K + 2P)/S \rfloor + 1$
- **B.** $\lfloor (W + K - P)/S \rfloor + 1$
- **C.** $\lfloor W/S \rfloor + 2P - K$
- **D.** $\lfloor (W - K + P)/S \rfloor + 1$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Output Spatial Dimension:** Chiều không gian đầu ra (rộng $W_{out}$ và cao $H_{out}$) sau phép toán tích chập.
- **Padding ($P$):** Thêm viền số 0 quanh biên ảnh.
- **Kernel size ($K$):** Kích thước cửa sổ trượt bộ lọc.
- **Stride ($S$):** Bước nhảy trượt của bộ lọc.

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng bạn bước đi trên một cây cầu dài $W$ mét. Bạn mở rộng cầu ra hai đầu thêm mỗi bên $P$ mét $\implies$ Chiều dài mới là $W + 2P$. Mỗi bước chân của bạn dài $K$ mét. Sau bước đầu tiên, bạn còn lại $(W + 2P - K)$ mét. Cứ mỗi lần nhảy tiếp theo bạn nhảy $S$ mét. Tổng số bước nhảy là lấy đoạn đường còn lại chia cho $S$ rồi cộng thêm bước chân đầu tiên (+1)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức kích thước đầu ra chuẩn mực (lấy hàm sàn $\lfloor \cdot \rfloor$):
$$W_{out} = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$$
Ví dụ thực tế: Ảnh $W=32$, filter $K=5$, padding $P=2$, stride $S=1$:
$$W_{out} = \frac{32 - 5 + 2(2)}{1} + 1 = 32 \quad (\text{Same padding})$$
Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B:** Dấu âm dương của $P$ và $K$ bị đảo ngược sai lệch.
- **Phương án C & D:** Quên cộng bước chân đầu tiên ($+1$) hoặc quên nhân $2P$ (ảnh có 2 mép viền trái và phải).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§3.1 Convolution, Stride, Padding & Receptive Field**.
🔗 **Liên hệ bài cũ:** Xem lại câu B01 Đề 01 và cẩm nang công thức §3.1 Nhớ nguyên tắc: Muốn giữ nguyên kích thước ảnh khi stride $S=1$ với filter lẻ $K$, ta luôn chọn $P = (K - 1) / 2$.

---

### Câu 17 [VOAI03-M17] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Hàm kích hoạt nào thường được dùng ở lớp cuối của bài toán phân loại đa lớp loại trừ nhau (Multi-class)?

- **A.** ReLU
- **B.** Sigmoid
- **C.** Softmax
- **D.** Tanh

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Phân loại nhị phân (Binary Classification):** 2 lớp đối lập (0 hoặc 1). Dùng hàm kích hoạt **Sigmoid** ở đầu ra để ra xác suất đơn lẻ $p \in (0, 1)$.
- **Phân loại đa lớp rời rạc (Multi-class Classification):** $C$ lớp độc lập loại trừ lẫn nhau (chỉ thuộc 1 lớp duy nhất). Dùng hàm **Softmax** để tạo phân phối xác suất có tổng bằng 1.
- **Phân loại đa nhãn (Multi-label Classification):** Một mẫu có thể thuộc nhiều lớp cùng lúc. Dùng hàm **Sigmoid độc lập** trên từng nơ-ron đầu ra.

🍼 **Hình dung thực tế cho em bé:**
Hàm Softmax giống như việc chia một chiếc bánh pizza 100% cho $C$ người bạn: Nó biến đổi các điểm số thô (Logits) sao cho mọi người đều nhận được một phần bánh có giá trị từ 0% đến 100%, và tổng số phần bánh của tất cả mọi người cộng lại luôn bằng đúng 100%!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Softmax cho lớp thứ $i$ ($i = 1, \dots, C$):
$$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^C e^{z_j}}$$
Đặc tính:
1. $0 < \text{Softmax}(z_i) < 1$ với mọi $i$.
2. $\sum_{i=1}^C \text{Softmax}(z_i) = 1$.
Chọn đáp án **C** (Softmax).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Sigmoid):** Dùng cho phân loại nhị phân hoặc phân loại đa nhãn (Multi-label), không đảm bảo tổng xác suất các lớp bằng 1.
- **Phương án B (Tanh):** Đưa đầu ra về khoảng $(-1, 1)$, không phải phân phối xác suất.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.2 Các hàm kích hoạt: ReLU, GELU, Sigmoid & Softmax**.
🔗 **Liên hệ bài cũ:** Trong PyTorch, hàm mất mát `nn. CrossEntropyLoss()` đã tự động tích hợp sẵn hàm Softmax bên trong, do đó ở tầng cuối của mô hình PyTorch, ta KHÔNG ĐƯỢC thêm tầng `nn. Softmax()` thủ công (tránh lỗi double-softmax làm xẹp gradient).

---

### Câu 18 [VOAI03-M18] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán tối ưu Adam, tham số $\beta_1$ và $\beta_2$ thường được dùng để:

- **A.** Tính trung bình động hàm mũ của gradient (Momentum) và bình phương gradient (RMSprop)
- **B.** Khởi tạo trọng số ngẫu nhiên theo phân phối Gauss (Normal Init) và kẹp gradient (Gradient Clip)
- **C.** Điều chỉnh động kích thước mini-batch (Dynamic Batch) và hệ số suy giảm trọng số (Weight Decay)
- **D.** Tắt ngẫu nhiên nơ-ron trong các tầng ẩn (Dropout Rate) và chuẩn hóa vector đầu vào (MinMax Scale)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Thuật toán Adam (Adaptive Moment Estimation):** Thuật toán tối ưu kết hợp Momentum (quán tính bậc 1) và RMSprop (bình phương gradient bậc 2).
- **Siêu tham số $\beta_1$:** Hệ số suy giảm mũ cho mô-men bậc 1 (ước lượng trung bình gradient, quán tính hướng đi). Mặc định là 0.9.
- **Siêu tham số $\beta_2$:** Hệ số suy giảm mũ cho mô-men bậc 2 (ước lượng phương sai không định tâm của gradient, độ dài bước đi). Mặc định là 0.999.

🍼 **Hình dung thực tế cho em bé:**
Adam giống như một chiếc xe lăn xuống dốc có hai bộ phận thông minh:
1. $\beta_1$ là ' bánh đà quán tính ': Xe nhớ vận tốc các giây trước để tiếp tục lao tới phía trước vượt qua các ổ gà nhỏ (tương đương $\approx 1/(1-0.9) = 10$ bước gần nhất).
2. $\beta_2$ là ' bộ phanh thích ứng ': Xe đo xem mặt đường gồ ghề ra sao trong một khoảng thời gian dài hơn (tương đương $\approx 1/(1-0.999) = 1000$ bước gần nhất) để tự động hãm tốc độ lại nếu đường dốc quá lớn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Các phương trình cập nhật của Adam:
$$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t \quad (\text{First Moment})$$
$$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2 \quad (\text{Second Moment})$$
Hiệu chỉnh chệch (Bias Correction):
$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$
Cập nhật tham số: $\theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$. Giá trị tiêu chuẩn của bài báo gốc Kingma & Ba (2014) là $\beta_1 = 0.9, \beta_2 = 0.999$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B, C, D:** Các cặp số đảo lộn hoặc sai lệch giá trị chuẩn.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.5 Các thuật toán tối ưu hóa (Optimizers)**.
🔗 **Liên hệ bài cũ:** Hệ số $\epsilon$ (thường là $10^{-8}$) được thêm vào mẫu số để tránh lỗi chia cho 0 khi gradient bằng 0.

---

### Câu 19 [VOAI03-M19] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Mạng Generative Adversarial Networks (GAN) bao gồm hai thành phần chính nào?

- **A.** Input và Output
- **B.** Encoder và Decoder
- **C.** Generator và Discriminator
- **D.** Actor và Critic

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **GAN (Generative Adversarial Networks):** Kiến trúc sinh đối kháng do Ian Goodfellow đề xuất năm 2014.
- **Bộ sinh (Generator - $G$):** Nhận vector nhiễu ngẫu nhiên $z \sim p_z(z)$, cố gắng tạo ra ảnh giả giống hệt ảnh thật để đánh lừa Bộ phân biệt.
- **Bộ phân biệt (Discriminator - $D$):** Nhận một bức ảnh (thật từ dataset hoặc giả từ Generator), đóng vai trò như cảnh sát phân loại xem ảnh đó là Thật (1) hay Giả (0).

🍼 **Hình dung thực tế cho em bé:**
GAN giống như một cuộc đấu trí không hồi kết giữa một ' Kẻ làm tiền giả ' (Generator) và một ' Cảnh sát thẩm định tiền ' (Discriminator). Ban đầu, kẻ làm tiền giả in ra những tờ giấy lộn rất vụng về, cảnh sát phát hiện ngay. Kẻ làm tiền giả rút kinh nghiệm từ lỗi sai, in tinh vi hơn. Cảnh sát cũng phải nâng cao nghiệp vụ soi kính lúp. Sau hàng ngàn vòng đấu, kẻ làm tiền giả đạt trình độ thượng thừa, in ra những tờ tiền y như thật!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Trò chơi Minimax tổng bằng không (Zero-Sum Game):
$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}}[\ln D(x)] + \mathbb{E}_{z \sim p_z}[\ln(1 - D(G(z)))]$$
Khi đạt cân bằng Nash hoàn hảo, $D(x) = 1/2$ ở mọi nơi (cảnh sát hoàn toàn bó tay không thể phân biệt nổi thật hay giả). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Encoder & Decoder):** Là cấu trúc của Autoencoder hoặc VAE (Variational Autoencoder), không phải GAN.
- **Phương án B (Actor & Critic):** Là kiến trúc của thuật toán Học tăng cường (Reinforcement Learning - Actor-Critic).
- **Phương án D (Policy & Value Network):** Dùng trong AlphaGo / RL.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§3.7 Mô hình sinh trong Thị giác máy tính: GAN, VAE & Diffusion**.
🔗 **Liên hệ bài cũ:** Trong cẩm nang §3.7, GAN rất dễ bị hiện tượng ' Mode Collapse ' (bộ sinh chỉ sinh duy nhất 1 mẫu lặp đi lặp lại vì đã đánh lừa được Discriminator). Mô hình Diffusion hiện đại (Stable Diffusion) đã khắc phục được nhược điểm này.

---

### Câu 20 [VOAI03-M20] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Một nơ-ron có 3 đầu vào $(1, 2, 3)$, trọng số tương ứng $(0.5, -1, 2)$ và bias là 0.5. Nếu dùng ReLU, đầu ra là:

- **A.** 0.0
- **B.** 4.5
- **C.** 5.0
- **D.** -4.5

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Artificial Neuron (Nơ-ron nhân tạo):** Thực hiện phép nhân vô hướng giữa vector đầu vào $x$ và vector trọng số $w$, cộng thêm bias $b$, sau đó qua hàm kích hoạt: $y = f(w^T x + b)$.

🍼 **Hình dung thực tế cho em bé:**
Tính toán của 1 nơ-ron đơn giản chỉ là phép tính đại số lớp 7:
Nhân từng đầu vào với trọng số tương ứng, cộng hết lại với nhau rồi cộng thêm số bias, sau đó cho kết quả đi qua cửa ải hàm kích hoạt (ở đây là hàm ReLU).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Đầu vào: $x = (1, 2, 3)$. Trọng số: $w = (0.5, -1, 2)$. Bias: $b = -2$.
1. Tính tổng tuyến tính (Pre-activation):
$$z = w^T x + b = (1 \times 0.5) + (2 \times -1) + (3 \times 2) + (-2)$$
$$z = 0.5 - 2 + 6 - 2 = 2.5$$
2. Áp dụng hàm kích hoạt ReLU:
$$y = \text{ReLU}(z) = \max(0, z) = \max(0, 2.5) = 2.5$$
Chọn đáp án **C** (2.5).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (4.5):** Quên cộng bias $b = -2$.
- **Phương án B (0):** Nhầm dấu khiến tổng ra âm rồi bị ReLU ép về 0.
- **Phương án D (3.5):** Tính nhầm phép cộng trừ.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.1 Perceptron & Mạng truyền thẳng (Feedforward Neural Networks)**.
🔗 **Liên hệ bài cũ:** Dạng bài tính tay giá trị feedforward nơ-ron xuất hiện liên tục trong đề thi OLP AI (xem thêm câu B06 Đề 01).

---

### Câu 21 [VOAI03-M21] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp ' Bag of Words ' (BoW) có nhược điểm lớn nhất là gì?

- **A.** Chỉ sử dụng được cho tiếng Anh
- **B.** Mất hoàn toàn thông tin về thứ tự từ và ngữ cảnh của câu
- **C.** Tính toán quá chậm trên tập dữ liệu lớn
- **D.** Không thể đếm được tần suất xuất hiện của từ

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Bag of Words (BoW):** Phương pháp biểu diễn văn bản bằng cách đếm số lần xuất hiện của từng từ trong từ điển (Vocabulary), bỏ qua hoàn toàn thứ tự từ.
- **Tính chất thưa (Sparsity):** Vector có hàng chục ngàn chiều nhưng hầu hết là số 0.
- **Semantic Blindness (Mù ngữ nghĩa):** Không hiểu được hai từ đồng nghĩa (ví dụ: ' xe hơi ' và ' ô tô ' bị coi là hai chiều độc lập hoàn toàn khác nhau).

🍼 **Hình dung thực tế cho em bé:**
BoW giống như bạn ném tất cả các từ trong một câu vào một chiếc túi rồi xóc đều lên: Câu ' Chó cắn người ' và câu ' Người cắn chó ' có đúng các từ ngữ như nhau, nên BoW biến chúng thành cùng một vector y hệt! Nó hoàn toàn làm mất trật tự ngữ pháp và ngữ cảnh câu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Vector BoW của văn bản $d$: $v_d = [c(w_1, d), c(w_2, d), \dots, c(w_{|V|}, d)]^T$.
Không có ma trận quan hệ thứ tự $P(w_i | w_{i-1})$. Chọn **B** (Làm mất thứ tự từ trong câu).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A & C:** BoW có chi phí tính toán rất thấp và dễ cài đặt, không phải nhược điểm.
- **Phương án D:** BoW hoàn toàn đếm được tần suất từ (đó chính là bản chất của nó).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§4.2 Biểu diễn từ & Vector hóa văn bản**.
🔗 **Liên hệ bài cũ:** Nhược điểm này được khắc phục đầu tiên bởi TF-IDF (đánh trọng số), sau đó là Word2Vec/FastText (nhúng ngữ nghĩa) và cuối cùng là Transformer/BERT (chú ý ngữ cảnh 2 chiều).

---

### Câu 22 [VOAI03-M22] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc ' BERT ' (Devlin et al.) được xây dựng dựa trên thành phần nào của Transformer?

- **A.** Cả Encoder và Decoder
- **B.** Không thành phần nào
- **C.** Transformer Decoder
- **D.** Transformer Encoder

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **BERT (Bidirectional Encoder Representations from Transformers):** Mô hình ngôn ngữ do Google đề xuất (2018), sử dụng phần **Encoder** của Transformer.
- **Cơ chế 2 chiều (Bidirectional Attention):** Mỗi từ được chú ý đồng thời tới cả các từ đứng trước nó và đứng sau nó trong câu.
- **Masked Language Model (MLM):** Che ngẫu nhiên 15% từ trong câu rồi bắt mô hình đoán từ bị che.

🍼 **Hình dung thực tế cho em bé:**
Khác với người đọc sách bình thường phải đọc từ trái sang phải từng chữ một (như GPT), BERT nhìn toàn bộ câu văn cùng lúc như một bức tranh hoàn chỉnh! Nó nhìn cả bên trái lẫn bên phải của từ bị khuyết để hiểu trọn vẹn ngữ cảnh của câu. Đó là lý do BERT chỉ dùng khối **Transformer Encoder**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Kiến trúc BERT-Base gồm 12 tầng Transformer Encoder, 12 attention heads, hidden size $d=768$, tổng cộng 110 triệu tham số. Không có khối Decoder hay Causal Masking. Chọn **D** (Transformer Encoder).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Transformer Decoder):** Là cấu trúc của dòng mô hình GPT (Autoregressive, có Causal Mask chỉ nhìn về bên trái).
- **Phương án B (Encoder-Decoder):** Là cấu trúc của T5, BART (dùng cho bài toán dịch máy và tóm tắt văn bản).
- **Phương án C (RNN/LSTM):** BERT hoàn toàn không dùng RNN.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§4.4 Transformer, Self-Attention & Large Language Models**.
🔗 **Liên hệ bài cũ:** Nhớ quy tắc phân loại 3 dòng họ Transformer: BERT = Encoder-only (hiểu/phân loại); GPT = Decoder-only (sinh từ tự hồi quy); T5/BART = Encoder-Decoder (dịch máy/seq2seq).

---

### Câu 23 [VOAI03-M23] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Hệ thống RAG (Retrieval-Augmented Generation) giúp mô hình LLM giải quyết vấn đề gì cốt lõi?

- **A.** Giảm thiểu hiện tượng ảo giác qua grounding dữ liệu ngoài và cập nhật tri thức mới không cần tái huấn luyện
- **B.** Tăng tốc độ suy luận mô hình lên gấp 10 lần nhờ nén ngữ cảnh đầu vào thành vector băm cố định
- **C.** Mở rộng kích thước từ điển tokenizer để bao trọn toàn bộ các thuật ngữ chuyên ngành hiếm gặp
- **D.** Loại bỏ hoàn toàn sự cần thiết của việc fine-tuning tham số cho mọi bài toán phân loại hạ nguồn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **RAG (Retrieval-Augmented Generation):** Kỹ thuật kết hợp giữa bộ truy xuất dữ liệu ngoài (Retriever - BM25 / Vector DB) và mô hình ngôn ngữ lớn (Generator - LLM).
- **Ảo giác (Hallucination):** Hiện tượng LLM tự bịa ra thông tin sai lệch nhưng diễn đạt với giọng điệu cực kỳ tự tin.
- **Bộ nhớ ngoài (External Knowledge Base):** Tài liệu văn bản nội bộ được cắt chunk và nhúng vector.

🍼 **Hình dung thực tế cho em bé:**
RAG biến kỳ thi của LLM từ một ' Kỳ thi đóng sách ' (phải học vẹt thuộc lòng toàn bộ kiến thức vào trọng số) thành một ' Kỳ thi mở sách ': Khi người dùng hỏi một câu hỏi khó, hệ thống mở ngăn kéo tài liệu ra, tìm đúng trang sách liên quan nhất rồi kẹp vào đề bài để LLM đọc và trả lời. Nhờ đó, LLM giảm thiểu tối đa tình trạng nói bừa (ảo giác)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức xác suất của RAG với tài liệu truy xuất $z$:
$$P(y \mid x) = \sum_{z \in \text{Top-k}} P(z \mid x) P(y \mid x, z)$$
RAG giúp LLM neo câu trả lời vào bằng chứng xác thực (Grounding), giảm thiểu đáng kể ảo giác. Chọn **A** (Hiện tượng ảo giác - Hallucination).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Overfitting):** Overfitting là vấn đề của quá trình huấn luyện, RAG không can thiệp trọng số.
- **Phương án C & D:** RAG không làm tăng tốc độ suy luận (thậm chí tăng thêm độ trễ do bước truy xuất) và không làm giảm kích thước mô hình.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§4.6 Retrieval-Augmented Generation (RAG) & Vector Database**.
🔗 **Liên hệ bài cũ:** Trong bài tự luận E06 Đề 02, ta thiết kế một hệ thống Enterprise RAG chuẩn mực kết hợp Hybrid Retrieval (BM25 + BGE-m3) và Cross-Encoder Re-ranker.

---

### Câu 24 [VOAI03-M24] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Phép toán ' Max Pooling ' trong mạng CNN có tác dụng cốt lõi là:

- **A.** Tăng độ phân giải không gian của ảnh nhằm khôi phục các chi tiết đường biên bị mờ
- **B.** Giảm kích thước không gian, giảm chi phí tính toán và giữ lại đặc trưng kích hoạt mạnh nhất
- **C.** Tăng số lượng kênh đặc trưng để mở rộng không gian biểu diễn cho các tầng tích chập sâu
- **D.** Tự động cân bằng độ sáng và độ tương phản của ảnh đầu vào trước khi trích xuất đặc trưng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Max Pooling:** Phép toán lấy giá trị lớn nhất trong từng cửa sổ trượt không gian (thường là $2 \times 2$, stride 2).
- **Tính bất biến với dịch chuyển nhỏ (Translation Invariance):** Nếu vật thể trong ảnh bị xê dịch nhẹ một vài pixel, giá trị cực đại trong cửa sổ $2 \times 2$ vẫn không đổi.
- **Giảm chiều không gian (Downsampling):** Giảm kích thước ảnh đi một nửa, mở rộng vùng cảm thụ (Receptive Field) cho các tầng sau.

🍼 **Hình dung thực tế cho em bé:**
Max Pooling giống như việc bạn nhìn một bức tranh từ xa: Bạn chỉ cần ghi nhớ điểm sáng nhất, nổi bật nhất của bức tranh đó mà không cần bận tâm chi tiết nhỏ bị xê dịch một chút sang trái hay sang phải. Nó giúp mạng máy tính nhận ra con mèo dù con mèo nằm ở chính giữa hay hơi lệch sang mép ảnh!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Max Pooling kích thước $K \times K$, stride $S$:
$$y_{i, j} = \max_{0 \le p, q < K} x_{i \cdot S + p, j \cdot S + q}$$
Đặc tính quan trọng: Max Pooling KHÔNG CÓ THAM SỐ HỌC ĐƯỢC (Parameters = 0). Nó tạo ra tính bất biến với dịch chuyển nhỏ. Chọn **B** (Tạo tính bất biến với phép tịnh tiến nhỏ).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Tăng số kênh):** Sai, Max Pooling giữ nguyên số kênh $C$, chỉ giảm $W$ và $H$.
- **Phương án C (Tăng số tham số):** Sai, Max Pooling có 0 tham số.
- **Phương án D:** Không có khả năng loại bỏ hoàn toàn nhiễu hạt.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§3.1 Convolution, Stride, Padding & Receptive Field**.
🔗 **Liên hệ bài cũ:** Khác với Max Pooling (chọn đặc trưng nổi bật nhất), Average Pooling tính trung bình nên làm mịn ảnh, thường được dùng ở tầng cuối cùng (Global Average Pooling) để thay thế tầng Dense cồng kềnh.

---

### Câu 25 [VOAI03-M25] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán phát hiện vật thể YOLO (You Only Look Once) thuộc nhóm kiến trúc nào?

- **A.** Instance Segmentation thuần túy
- **B.** Single-stage detector
- **C.** Unsupervised detector
- **D.** Two-stage detector

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **YOLO (You Only Look Once):** Mô hình phát hiện vật thể dạng một giai đoạn (Single-stage Object Detector) do Joseph Redmon đề xuất năm 2016.
- **Single-stage Detector:** Dự đoán trực tiếp tọa độ hộp bao (Bounding Box) và nhãn lớp trong MỘT lượt truyền thẳng duy nhất qua mạng.
- **Two-stage Detector:** Gồm 2 bước riêng biệt: Bước 1 sinh vùng đề xuất (Region Proposals qua RPN), Bước 2 phân loại và tinh chỉnh hộp (như Faster R-CNN).

🍼 **Hình dung thực tế cho em bé:**
YOLO giống như một tay súng thiện xạ nhìn lướt qua một căn phòng: Trong chớp mắt (một cái nhìn duy nhất), tay súng nhìn thấy toàn bộ đồ vật và vị trí của chúng cùng một lúc. Trong khi đó, Faster R-CNN giống như một nhà thám tử: Trước tiên dùng kính lúp khoanh vùng 2,000 điểm đáng ngờ, rồi mới đi kiểm tra từng điểm một $\implies$ YOLO chạy nhanh gấp nhiều lần, phù hợp thời gian thực (Real-time)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 YOLO chia ảnh thành lưới $S \times S$. Mỗi ô lưới dự đoán $B$ hộp bao và xác suất của $C$ lớp. Toàn bộ quá trình được giải quyết như một bài toán hồi quy đơn lẻ qua hàm mất mát đa thành phần. Chọn **B** (Single-stage Detector).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Two-stage Detector):** Là đặc trưng của họ R-CNN (R-CNN, Fast R-CNN, Faster R-CNN).
- **Phương án C (Anchor-free duy nhất):** YOLO nguyên bản (v1-v5) sử dụng Anchor Boxes, không phải anchor-free thuần túy.
- **Phương án D:** YOLO là mạng nơ-ron học sâu hoàn chỉnh.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§3.3 Nhận diện & Định vị vật thể (Object Detection)**.
🔗 **Liên hệ bài cũ:** Nhớ bảng so sánh: Two-stage (Faster R-CNN) chính xác hơn nhưng chậm (5-15 FPS); Single-stage (YOLO, SSD) cực nhanh (30-140 FPS), lý tưởng cho camera giám sát và xe tự hành.

---

### Câu 26 [VOAI03-M26] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán NMS (Non-Maximum Suppression) trong Object Detection dùng để làm gì?

- **A.** Loại bỏ các bounding box trùng lặp xung quanh cùng một đối tượng và giữ lại box có score cao nhất
- **B.** Mở rộng kích thước tất cả các bounding box để bao trọn vùng ngữ cảnh xung quanh đối tượng
- **C.** Làm mịn hóa ranh giới phân loại bằng cách tính trung bình tọa độ của toàn bộ anchor boxes
- **D.** Tính toán hàm mất mát hồi quy tọa độ kết hợp chuẩn hóa ma trận hiệp phương sai của nhãn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **NMS (Non-Maximum Suppression):** Thuật toán hậu xử lý trong Object Detection nhằm loại bỏ các hộp bao dư thừa trùng lặp trên cùng một vật thể.
- **IoU (Intersection over Union):** Tỉ lệ diện tích giao trên diện tích hợp giữa 2 hộp bao: $\text{IoU} = \frac{|A \cap B|}{|A \cup B|}$.
- **Cơ chế NMS:** Sắp xếp các hộp theo điểm tin cậy (Confidence Score) giảm dần. Chọn hộp cao nhất, loại bỏ tất cả các hộp khác có $\text{IoU} > \text{threshold}$ với hộp đó.

🍼 **Hình dung thực tế cho em bé:**
Khi mô hình nhìn thấy một con mèo, nó có thể vẽ ra 50 chiếc hộp bao quanh con mèo đó với điểm số chênh lệch nhau một chút. NMS hoạt động như một trọng tài nghiêm khắc: Giữ lại duy nhất chiếc hộp đẹp nhất (điểm cao nhất), và xóa sổ tất cả các chiếc hộp khác bị chồng lấn quá nhiều lên nó!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thuật toán NMS:
1. Chọn hộp $B_{max} = \arg\max \text{score}(B)$.
2. Thêm $B_{max}$ vào danh sách giữ lại.
3. Với mọi hộp $B_i$ còn lại, nếu $\text{IoU}(B_{max}, B_i) > \tau$ (thường là 0.45 hoặc 0.5), loại bỏ $B_i$.
4. Lặp lại cho đến khi hết hộp. Chọn **A** (Loại bỏ các hộp bao trùng lặp trên cùng một vật thể).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B:** Tăng số lượng hộp là sai (NMS làm giảm số lượng hộp).
- **Phương án C:** NMS là thuật toán hậu xử lý heuristic, không dùng để huấn luyện bộ phân loại.
- **Phương án D:** NMS không phải phép tăng cường dữ liệu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§3.3 Nhận diện & Định vị vật thể (Object Detection)**.
🔗 **Liên hệ bài cũ:** Biến thể Soft-NMS không xóa hẳn các hộp lân cận mà chỉ giảm điểm tin cậy của chúng theo hàm Gauss, giúp không bỏ sót hai vật thể đứng sát đè lên nhau.

---

### Câu 27 [VOAI03-M27] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật ' Model Quantization ' (Lượng hóa mô hình) mang lại lợi ích gì lớn nhất khi triển khai thực tế?

- **A.** Giảm dung lượng bộ nhớ VRAM và tăng tốc độ suy luận khi phần cứng có kernel hỗ trợ INT8/FP8
- **B.** Chuyển mã nguồn mô hình từ Python sang C++ để loại bỏ chi phí biên dịch trung gian
- **C.** Tăng độ chính xác phân loại của mô hình trên tập kiểm thử độc lập mà không cần huấn luyện
- **D.** Tự động loại bỏ các tầng tích chập dư thừa thông qua thuật toán phân rã ma trận kì dị SVD

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Model Quantization (Lượng hóa mô hình):** Kỹ thuật chuyển đổi trọng số và giá trị kích hoạt từ số thực độ chính xác cao (FP32 hoặc FP16) sang số nguyên ít bit hơn (như INT8 hoặc FP4/INT4).
- **Post-Training Quantization (PTQ):** Lượng hóa sau khi đã huấn luyện xong.
- **Quantization-Aware Training (QAT):** Mô phỏng làm tròn số ngay trong quá trình huấn luyện để giữ độ chính xác cao nhất.

🍼 **Hình dung thực tế cho em bé:**
Lượng hóa giống như việc bạn ghi lại số đo chiều cao: Thay vì ghi chi tiết đến từng phần triệu milimét (1.7523948 mét - tốn 32 chữ số), bạn làm tròn thành 1.75 mét (chỉ tốn 8 chữ số). Kích thước file giảm đi 4 lần, tiết kiệm bộ nhớ RAM/VRAM và giúp truyền tải dữ liệu nhanh gấp 4 lần trên chip máy tính!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức lượng hóa tuyến tính đối xứng:
$$q = \text{clamp}\left(\left\lfloor \frac{x}{S} \right\rceil, -128, 127\right)$$
Trong đó $S$ là hệ số tỉ lệ (Scale factor). Lợi ích lớn nhất là giảm dung lượng bộ nhớ VRAM và băng thông bộ nhớ (Memory Bandwidth) tới 75%. Chọn **A** (Giảm dung lượng bộ nhớ và tăng tốc độ suy luận).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B:** Lượng hóa có thể làm suy giảm nhẹ độ chính xác (Accuracy), không làm tăng.
- **Phương án C:** Lượng hóa không làm tăng số lượng tham số.
- **Phương án D:** Lượng hóa dùng cho suy luận (Inference), không làm tăng tốc độ huấn luyện.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.8 Tối ưu hóa mô hình & MLOps Deployment**.
🔗 **Liên hệ bài cũ:** Lưu ý bẫy đề thi nâng cao: Nếu phần cứng không có nhân xử lý INT8 chuyên dụng (như Tensor Cores), CPU phải giải lượng hóa (Dequantize) ngược lại về FP32, có thể làm tăng độ trễ suy luận!

---

### Câu 28 [VOAI03-M28] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hiện tượng ' Data Drift ' (Trôi dạt dữ liệu) trong vận hành mô hình máy học (MLOps) có nghĩa là:

- **A.** Tốc độ truyền dữ liệu qua băng thông mạng bị suy giảm do kích thước file ảnh quá lớn
- **B.** Dữ liệu bị sao chép trùng lặp nhiều lần trong cơ sở dữ liệu làm sai lệch kết quả thống kê
- **C.** Sự thay đổi phân phối xác suất của dữ liệu thực tế theo thời gian khiến mô hình suy giảm hiệu năng
- **D.** Dữ liệu bị mất mát một phần các trường thông tin quan trọng do lỗi trích xuất OCR đầu vào

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Data Drift (Trôi dạt dữ liệu / Covariate Shift):** Hiện tượng phân phối của dữ liệu đầu vào $P(X)$ thay đổi theo thời gian giữa tập huấn luyện và môi trường thực tế ($P_{\text{train}}(X) \ne P_{\text{serve}}(X)$), trong khi quan hệ $P(y|X)$ vẫn giữ nguyên.
- **Concept Drift:** Bản chất quan hệ mục tiêu thay đổi ($P_{\text{train}}(y|X) \ne P_{\text{serve}}(y|X)$).
- **Công cụ phát hiện:** Kiểm định Kolmogorov-Smirnov (KS-test), Population Stability Index (PSI).

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng bạn dạy một mô hình nhận diện phong cách thời trang dựa trên ảnh chụp năm 2010. Đến năm 2026, giới trẻ chuyển sang mặc phong cách hoàn toàn mới (quần áo, kiểu tóc, phụ kiện thay đổi). Dữ liệu đầu vào thực tế đã ' trôi dạt ' sang một vùng hoàn toàn xa lạ so với những gì mô hình từng được học trong quá khứ $\implies$ Mô hình dự đoán sai liên tục!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi xảy ra Data Drift, kiểm định thống kê khoảng cách Wasserstein hoặc PSI giữa hai phân phối sẽ vượt ngưỡng báo động (thường $\text{PSI} > 0.2$), kích hoạt pipeline tự động thu thập dữ liệu mới và huấn luyện lại mô hình (Continuous Training - CT). Chọn **C** (Sự thay đổi phân phối của dữ liệu đầu vào theo thời gian).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A:** Dữ liệu bị mất mát là lỗi thiếu giá trị (Missing Data), không phải Drift.
- **Phương án B:** Mô hình bị lỗi code là Bug phần mềm.
- **Phương án D:** Dữ liệu bị overfitting là lỗi mô hình, không phải đặc tính trôi dạt dữ liệu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.8 Tối ưu hóa mô hình & MLOps Deployment**.
🔗 **Liên hệ bài cũ:** Trong các hệ thống AI thực chiến, hệ thống giám sát (Monitoring) phải liên tục theo dõi Data Drift để tự động phát cảnh báo trước khi hiệu năng mô hình bị suy thoái nghiêm trọng.

---

### Câu 29 [VOAI03-M29] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật ngữ ' MLOps ' là viết tắt của:

- **A.** Mobile Learning Options
- **B.** Main Logic Operator
- **C.** Machine Learning Operations
- **D.** Multi-Layer Optimization

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **MLOps (Machine Learning Operations):** Bộ quy chuẩn, công cụ và quy trình kết hợp giữa Machine Learning, DevOps và Kỹ thuật dữ liệu (Data Engineering).
- **Mục tiêu:** Tự động hóa và vận hành vòng đời của mô hình AI: Thu thập dữ liệu $\to$ Huấn luyện (CI/CD/CT) $\to$ Đóng gói $\to$ Triển khai Serving $\to$ Giám sát Drift & Tự động huấn luyện lại.

🍼 **Hình dung thực tế cho em bé:**
MLOps giống như quy trình biến một công thức nấu ăn ngon của một đầu bếp trong gia đình (mô hình AI trong notebook) thành một dây chuyền nhà máy sản xuất thực phẩm tự động phục vụ hàng triệu người tiêu dùng mỗi ngày: Đảm bảo nguyên liệu luôn tươi sạch, dây chuyền không bao giờ ngừng hoạt động và chất lượng món ăn luôn đồng đều!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 MLOps = Machine Learning + Operations. Chọn **C** (Machine Learning Operations).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Machine Learning Optimization):** Tối ưu hóa ML chỉ là một phần nhỏ trong thuật toán.
- **Phương án B (Machine Learning Operators):** Các toán tử toán học.
- **Phương án D:** Từ viết tắt giả định.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.8 Tối ưu hóa mô hình & MLOps Deployment**.
🔗 **Liên hệ bài cũ:** Bộ công cụ MLOps tiêu chuẩn hiện nay gồm: MLflow (quản lý thí nghiệm), DVC (phiên bản dữ liệu), Kubeflow (pipeline container), Prometheus/EvidentlyAI (giám sát drift).

---

### Câu 30 [VOAI03-M30] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Để phục vụ (Serving) một mô hình LLM lớn, kỹ thuật nào thường được dùng để tránh tính toán lại dư thừa trạng thái Attention qua các bước sinh token (dù đánh đổi tiêu tốn VRAM làm bộ nhớ đệm)?

- **A.** KV Caching (Key-Value Caching)
- **B.** Weight Pruning (Cắt tỉa trọng số)
- **C.** Layer Normalization (Chuẩn hóa tầng)
- **D.** Gradient Accumulation (Tích lũy gradient)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **LLM Serving:** Việc triển khai mô hình ngôn ngữ lớn để phục vụ yêu cầu của người dùng thời gian thực.
- **KV Cache (Key-Value Caching):** Lưu lại các vector Key và Value của các token trước đó trong quá trình sinh từ tự hồi quy (Autoregressive) để không phải tính lại từ đầu.
- **PagedAttention (vLLM):** Thuật toán quản lý bộ nhớ KV Cache lấy cảm hứng từ kỹ thuật phân trang bộ nhớ ảo của hệ điều hành, giảm phân mảnh bộ nhớ từ 60-80% xuống dưới 4%.
- **Continuous Batching:** Gom cụm động các request đến lệch thời điểm theo từng bước sinh token.

🍼 **Hình dung thực tế cho em bé:**
Mỗi khi LLM sinh ra một từ mới, nó phải nhớ lại toàn bộ các từ đã nói trước đó. Nếu không có bộ nhớ tạm (KV Cache), mỗi từ mới sinh ra mô hình đều phải đọc lại cuốn sách từ trang đầu tiên! Kỹ thuật PagedAttention giống như việc chia cuốn sổ tay thành các trang giấy rời được đánh số: Cần viết thêm chữ thì cấp phát đúng 1 trang nhỏ, không để thừa trang giấy trắng lãng phí bộ nhớ VRAM đắt đỏ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nhờ PagedAttention và Continuous Batching, hệ thống vLLM tăng thông lượng (Throughput) phục vụ LLM lên gấp 2-4 lần so với các hệ thống thông thường. Chọn **A** (PagedAttention và Continuous Batching trong vLLM).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Chạy tuần tự từng request):** Làm lãng phí GPU và nghẽn mạng nghiêm trọng.
- **Phương án C (Tắt hoàn toàn KV cache):** Khiến độ phức tạp tính toán tăng vọt thành $O(N^2)$ cho mỗi token, làm suy giảm tốc độ sinh từ.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§4.5 Large Language Models & Efficient Serving**.
🔗 **Liên hệ bài cũ:** Nhớ bản chất: KV Cache đánh đổi bộ nhớ VRAM để tiết kiệm phép tính FLOPs (tăng tốc độ sinh token).

---

### Câu 31 [VOAI03-M31] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Học bán giám sát (Semi-supervised Learning) được áp dụng hiệu quả nhất trong kịch bản nào?

- **A.** Có một lượng nhỏ dữ liệu có nhãn và một lượng rất lớn dữ liệu chưa gán nhãn
- **B.** Không có bất kỳ dữ liệu nào được gán nhãn trong toàn bộ tập huấn luyện
- **C.** Số lượng nhãn lớp phân loại thay đổi liên tục theo từng chu kỳ kiểm tra
- **D.** Toàn bộ dữ liệu đều đã được các chuyên gia gán nhãn đầy đủ và chính xác

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Học bán giám sát (Semi-supervised Learning):** Phương pháp huấn luyện khi có một lượng nhỏ dữ liệu có nhãn (Labeled data) và một lượng rất lớn dữ liệu chưa có nhãn (Unlabeled data).
- **Pseudo-labeling:** Dùng mô hình huấn luyện trên tập có nhãn để dự đoán nhãn giả cho tập chưa có nhãn, sau đó chọn các mẫu có độ tin cậy cao để nạp lại vào tập huấn luyện.
- **Consistency Regularization:** Ép mô hình đưa ra dự đoán tương đồng khi ảnh đầu vào bị biến dạng nhẹ (Perturbation).

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng trong một lớp học, giáo viên chỉ có thời gian chấm điểm chi tiết cho 10 bài kiểm tra mẫu (dữ liệu có nhãn). Còn 1,000 bài tập khác chưa kịp chấm. Học bán giám sát giúp bạn học từ 10 bài mẫu đó trước, rồi tự làm thử 1,000 bài tập kia để nâng cao tay nghề thay vì bỏ phí 1,000 bài tập đó!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng khi chi phí dán nhãn (gán nhãn bởi chuyên gia/bác sĩ) rất đắt đỏ trong khi dữ liệu thô chưa dán nhãn lại cực kỳ phong phú và dễ thu thập. Chọn **A** (Dữ liệu có nhãn rất ít nhưng dữ liệu chưa có nhãn rất nhiều).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B & C:** Nếu dữ liệu đã có nhãn đầy đủ thì dùng Supervised Learning; nếu hoàn toàn không có nhãn thì dùng Unsupervised Learning.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.5 Các phương pháp học máy hiện đại**.
🔗 **Liên hệ bài cũ:** Trong các bài toán phát hiện bất thường ảnh công nghiệp (như đề thi OLP AI 2026 Tác vụ 2), việc tận dụng lượng lớn ảnh bình thường chưa gán nhãn là chìa khóa để xây dựng mô hình một lớp (One-class classification).

---

### Câu 32 [VOAI03-M32] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Điểm vượt trội của thuật toán t-SNE so với PCA khi giảm chiều dữ liệu để trực quan hóa là gì?

- **A.** t-SNE sử dụng phép chiếu trực giao (Linear Mapping) nên dễ dàng suy luận chiếu ngược lại
- **B.** t-SNE tính toán nhanh hơn PCA (GPU Speedup) gấp 10 lần trên tập dữ liệu hàng triệu chiều
- **C.** t-SNE bảo toàn tốt hơn cấu trúc phi tuyến và khoảng cách cục bộ (Local Manifold) giữa các cụm
- **D.** t-SNE luôn luôn bảo toàn 100% tổng phương sai (Variance Retention) của toàn bộ dữ liệu gốc

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **t-SNE (t-Distributed Stochastic Neighbor Embedding):** Thuật toán giảm chiều dữ liệu phi tuyến (Non-linear Dimensionality Reduction) chuyên dùng để trực quan hóa không gian nhiều chiều về 2D/3D.
- **PCA (Principal Component Analysis):** Kỹ thuật giảm chiều tuyến tính bằng phép chiếu trực giao.
- **Phân phối Student-t:** Có phần đuôi dày (Heavy-tailed), giải quyết triệt để vấn đề chen chúc (Crowding Problem) của các cụm trong không gian chiều thấp.

🍼 **Hình dung thực tế cho em bé:**
PCA giống như chiếu bóng của một chiếc ấm trà lên tường: Các chi tiết phía trước và phía sau bị đè bẹp lên nhau vì chỉ là bóng phẳng tuyến tính. Còn t-SNE giống như một người nghệ nhân khéo léo bóc tách từng cụm đất sét ra, trải chúng lên bàn sao cho các hạt gần nhau vẫn ở gần nhau, còn các cụm khác nhau được đẩy xa hẳn ra!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 t-SNE tối thiểu hóa phân kỳ Kullback-Leibler (KL Divergence) giữa phân phối xác suất láng giềng trong không gian gốc $p_{j|i}$ và không gian chiếu $q_{j|i}$:
$$KL(P \parallel Q) = \sum_i \sum_j p_{j|i} \log \frac{p_{j|i}}{q_{j|i}}$$
t-SNE bảo toàn cấu trúc lân cận phi tuyến cục bộ vượt trội so với PCA. Chọn **C** (Bảo toàn cấu trúc cục bộ và quan hệ phi tuyến tốt hơn nhiều).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Chạy nhanh hơn):** Sai, t-SNE có độ phức tạp tính toán $O(N^2)$ (hoặc $O(N \log N)$ với Barnes-Hut), chậm hơn PCA rất nhiều.
- **Phương án B (Dùng làm đặc trưng train):** Sai, t-SNE không học được hàm chiếu tổng quát để chiếu điểm dữ liệu mới (Out-of-sample mapping).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.7 Giảm chiều dữ liệu: PCA & t-SNE**.
🔗 **Liên hệ bài cũ:** Nhớ quy tắc thực tế: Dùng PCA để giảm chiều tiền xử lý trước khi đưa vào mô hình học máy; dùng t-SNE hoặc UMAP để vẽ biểu đồ trực quan hóa khám phá các cụm.

---

### Câu 33 [VOAI03-M33] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Tại sao Stratified K-Fold lại là lựa chọn bắt buộc so với K-Fold thông thường trong bài toán phân loại có dữ liệu mất cân bằng?

- **A.** Tự động loại bỏ các điểm dị biệt ngoại lai khỏi tập dữ liệu huấn luyện ban đầu
- **B.** Giúp mô hình tăng tốc độ hội tụ bằng cách giảm bớt số lượng mẫu trong các fold
- **C.** Không cho phép bất kỳ mẫu dữ liệu nào bị trùng lặp giữa các lần chạy lặp lại
- **D.** Đảm bảo tỷ lệ phân bố giữa các lớp trong mỗi Fold đồng nhất với tỷ lệ trong toàn bộ tập dữ liệu gốc

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Stratified K-Fold:** Kỹ thuật chia tập dữ liệu thành $K$ phần (folds) sao cho tỉ lệ phân bố giữa các lớp (Class Ratio) trong mỗi fold giống hệt tỉ lệ của toàn bộ tập dữ liệu gốc.
- **K-Fold thông thường (Standard K-Fold):** Chia ngẫu nhiên không xét đến nhãn lớp.
- **Mất cân bằng lớp nghiêm trọng (Severe Imbalance):** Ví dụ lớp thiểu số chỉ chiếm 1% (như phát hiện gian lận thẻ tín dụng hoặc bệnh hiếm).

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng bạn làm một mâm cỗ có 100 chiếc bánh: Trong đó chỉ có đúng 5 chiếc bánh nhân sôcôla thượng hạng, còn lại 95 chiếc bánh nhân đậu xanh. Nếu chia ngẫu nhiên thành 5 đĩa (K-Fold thường), rất có thể đĩa thứ nhất không có chiếc bánh sôcôla nào, trong khi đĩa thứ hai lại ôm trọn cả 5 chiếc! Stratified K-Fold đảm bảo chia đều: Mỗi đĩa bắt buộc phải có đúng 1 chiếc bánh sôcôla và 19 chiếc bánh đậu xanh!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nếu dùng K-Fold thường trên tập dữ liệu lệch lớp, một fold kiểm thử có thể hoàn toàn không chứa mẫu nào của lớp thiểu số ($TP=0, FN=0$), khiến các chỉ số Precision, Recall và F1 bị vỡ hoặc không tính toán được. Stratified K-Fold bảo toàn $P(y=c)$ trên mọi fold. Chọn **D** (Đảm bảo tỉ lệ phân bố các lớp đồng đều trong mọi fold chia).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A & B:** Stratified K-Fold không làm tăng tốc độ chạy và không sinh thêm dữ liệu mới.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.5 Cross-Validation & Các phương pháp đánh giá mô hình**.
🔗 **Liên hệ bài cũ:** Trong bài tự luận E04 Đề 02 (Phát hiện ảnh Deepfake theo cặp), ta phải nâng cấp lên `StratifiedGroupKFold`: Vừa bảo đảm tỉ lệ nhãn đồng đều, vừa gom toàn bộ các ảnh cùng nhóm (`pair_id`) vào chung một fold để chống rò rỉ dữ liệu.

---

### Câu 34 [VOAI03-M34] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hiện tượng ' Data Leakage ' (Rò rỉ dữ liệu) nghiêm trọng nhất thường xảy ra khi:

- **A.** Sử dụng kỹ thuật Stratified K-Fold (Stratified Sampling) để chia tập dữ liệu mất cân bằng
- **B.** Chuẩn hóa dữ liệu (StandardScaler / MinMax) trên toàn bộ dataset trước khi chia Train / Val
- **C.** Áp dụng kỹ thuật dừng sớm (Early Stopping) dựa trên mất mát của tập Validation trong mỗi epoch
- **D.** Sử dụng độ đo cân bằng (F1-Score / PR-AUC) thay cho độ đo Accuracy khi đánh giá kiểm thử

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Data Leakage (Rò rỉ dữ liệu / Train-Test Contamination):** Hiện tượng thông tin từ tập kiểm tra (Test set) bị thẩm thấu (rò rỉ) vào quá trình huấn luyện mô hình.
- **Hậu quả:** Điểm số Validation/CV cao giả tạo nhưng mô hình sụp đổ hoàn toàn khi đưa vào môi trường Production thực tế.
- **Vị trí hay mắc lỗi nhất:** Gọi `StandardScaler.fit()` hoặc `Imputer.fit()` trên toàn bộ dữ liệu trước khi chia Train-Test.

🍼 **Hình dung thực tế cho em bé:**
Data Leakage giống như việc bạn đi thi nhưng đã vô tình đọc trộm đáp án và thang điểm của thầy giáo từ tối hôm trước! Bạn đạt 10 điểm tuyệt đối trong phòng thi thử, nhưng khi gặp một bài kiểm tra thực tế ngoài đời thì hoàn toàn không biết làm. Chuẩn hóa dữ liệu trên cả tập test khiến mô hình ' biết trước ' giá trị trung bình $\mu$ và độ lệch chuẩn $\sigma$ của tương lai!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Quy tắc vàng bất biến trong khoa học dữ liệu:
1. Chia tập dữ liệu thành Train và Test TRƯỚC TIÊN.
2. Chỉ gọi `scaler.fit_transform(X_train)` trên tập Train.
3. Chỉ gọi `scaler.transform(X_test)` trên tập Test (dùng nguyên $\mu_{\text{train}}$ và $\sigma_{\text{train}}$).
Chọn **B** (Chuẩn hóa toàn bộ dữ liệu trước khi chia Train/Test).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A, C, D:** Lấy mẫu ngẫu nhiên, chia dữ liệu trước và dùng cross-validation là các quy trình chuẩn mực chống rò rỉ.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.5 Cross-Validation & Pipeline chống leakage**.
🔗 **Liên hệ bài cũ:** Trong Scikit-Learn, cách tốt nhất để triệt tiêu Data Leakage là đóng gói toàn bộ các bước tiền xử lý và mô hình vào một `Pipeline(steps=[(' scaler ', StandardScaler()), (' clf ', Model())])`.

---

### Câu 35 [VOAI03-M35] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật SMOTE (Synthetic Minority Over-sampling Technique) giải quyết vấn đề mất cân bằng lớp bằng cách:

- **A.** Loại bỏ ngẫu nhiên các mẫu thuộc lớp đa số để đưa tỷ lệ phân phối về mức cân bằng 1:1
- **B.** Gán trọng số phạt lớn hơn cho các mẫu thuộc lớp đa số trong hàm mục tiêu huấn luyện
- **C.** Nhân bản lặp lại nguyên xi các mẫu có sẵn của lớp thiểu số mà không sinh thêm mẫu mới
- **D.** Tạo ra các mẫu tổng hợp mới cho lớp thiểu số bằng cách nội suy tuyến tính giữa các hàng xóm k-NN

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **SMOTE (Synthetic Minority Over-sampling Technique):** Thuật toán sinh mẫu nhân tạo cho lớp thiểu số bằng phép nội suy vector dựa trên $k$ láng giềng gần nhất (thường $k=5$).
- **Random Oversampling:** Nhân bản sao chép y nguyên các mẫu thiểu số cũ (dễ gây Overfitting).
- **Nhược điểm của SMOTE:** Có thể sinh mẫu rơi vào vùng ranh giới nhiễu giữa hai lớp (khắc phục bằng Borderline-SMOTE hoặc SVM-SMOTE).

🍼 **Hình dung thực tế cho em bé:**
Thay vì chỉ đơn giản là photocopy lại những bức ảnh cũ (làm mô hình học vẹt), SMOTE tìm hai điểm dữ liệu cùng thuộc lớp thiểu số đứng gần nhau, rồi vẽ một đoạn thẳng nối giữa hai điểm đó. Sau đó, nó chọn một vị trí ngẫu nhiên trên đoạn thẳng để ' nặn ' ra một điểm dữ liệu nhân tạo mới toanh! Giúp mở rộng ranh giới quyết định của lớp thiểu số một cách mượt mà.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức sinh mẫu của SMOTE:
$$x_{\text{new}} = x_i + \lambda (x_{zi} - x_i)$$
Trong đó $x_{zi}$ là một trong $k$ láng giềng gần nhất cùng lớp của $x_i$, và $\lambda \sim U(0, 1)$ là số ngẫu nhiên đều. Chọn **D** (Nội suy tuyến tính giữa các điểm láng giềng gần nhất của lớp thiểu số).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Nhân bản ngẫu nhiên):** Đó là Random Oversampling thô sơ.
- **Phương án B (Xóa bớt mẫu đa số):** Đó là kỹ thuật Undersampling (như Tomek Links, ENN).
- **Phương án C:** SMOTE không gán nhãn lại dữ liệu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.9 Xử lý dữ liệu mất cân bằng: SMOTE, Focal Loss & Class Weights**.
🔗 **Liên hệ bài cũ:** Cực kỳ lưu ý: CHỈ ĐƯỢC CHẠY SMOTE TRÊN TẬP HUẤN LUYỆN (Train Set). Nếu chạy SMOTE trước khi chia train/test, bạn sẽ làm rò rỉ dữ liệu nhân tạo sang tập test (Data Leakage nghiêm trọng)!

---

### Câu 36 [VOAI03-M36] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi đánh giá một mô hình phân loại trên tập dữ liệu cực kỳ mất cân bằng (ví dụ gian lận thẻ tín dụng chỉ chiếm 0.1%), độ đo nào sau đây bị coi là ' vô dụng ' và gây hiểu lầm nhất?

- **A.** Precision-Recall AUC (PR-AUC)
- **B.** Recall
- **C.** F1-Score
- **D.** Accuracy (Độ chính xác tổng thể)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **ROC-AUC (Area Under ROC Curve):** Diện tích dưới đường cong liên hệ giữa TPR ($TP/(TP+FN)$) và FPR ($FP/(FP+TN)$).
- **PR-AUC (Precision-Recall AUC / Average Precision):** Diện tích dưới đường cong liên hệ giữa Precision và Recall.
- **True Negative Inflation:** Khi số lượng mẫu âm tính ($TN$) quá khổng lồ, mẫu số của FPR ($FP + TN$) cực lớn khiến FPR luôn rất nhỏ, làm đường cong ROC bị thổi phồng giả tạo (Optimistic Bias).

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng trong một triệu giao dịch ngân hàng chỉ có đúng 10 vụ lừa đảo ($TN = 999,990$). Một mô hình tồi đoán nhầm 1,000 giao dịch bình thường thành lừa đảo ($FP=1,000$). Khi đó FPR chỉ là $1,000 / 1,000,000 = 0.1\%$ (trông như hoàn hảo!). Đường cong ROC-AUC sẽ đạt tới 0.99 đẹp như mơ! Nhưng thực tế Precision của nó cực tệ: Bắt 1,000 người thì chỉ có vài tên trộm. Chỉ có đường cong PR-AUC mới lột trần sự yếu kém này!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi bài toán có tỉ lệ lệch lớp cực đoan (như $1:100$ hoặc $1:1000$), chỉ số **PR-AUC** (Precision-Recall AUC) là tiêu chuẩn vàng duy nhất phản ánh chính xác hiệu năng mô hình trên lớp thiểu số quan trọng. Chọn **D** (PR-AUC / Precision-Recall Curve).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Accuracy):** Hoàn toàn vô dụng (đoán toàn bộ là Âm tính vẫn đạt Accuracy 99.9%).
- **Phương án B (ROC-AUC):** Bị thổi phồng bởi số lượng $TN$ khổng lồ.
- **Phương án C (MSE):** Chỉ dùng cho bài toán Hồi quy số thực.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.6 Các chỉ số đánh giá mô hình (Metrics)**.
🔗 **Liên hệ bài cũ:** Trong cẩm nang §1.6 và bài tự luận E05 Đề 02, luôn ưu tiên cặp chỉ số PR-AUC và Macro-F1 khi giải quyết các bài toán dữ liệu bảng mất cân bằng lớp.

---

### Câu 37 [VOAI03-M37] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Điểm khác biệt cơ bản về mặt hiệu ứng giữa Regularization L1 (Lasso) và L2 (Ridge) là gì?

- **A.** L1 có xu hướng ép các trọng số không quan trọng về đúng 0 (Sparsity), L2 chỉ thu nhỏ về gần 0
- **B.** L2 ép các trọng số về đúng 0 (Feature Selection), trong khi L1 chỉ thu nhỏ biên độ vector trọng số
- **C.** L1 luôn đảm bảo tìm được nghiệm toàn cục (Global Minimum), L2 dễ mắc kẹt tại cực tiểu địa phương
- **D.** L1 chỉ dùng cho bài toán hồi quy lồi (Convex Loss), L2 chỉ dùng cho mạng nơ-ron phân loại đa lớp

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Regularization (Chính quy hóa):** Kỹ thuật cộng thêm một số hạng phạt độ lớn trọng số vào hàm mất mát để chống Overfitting.
- **L1 Regularization (Lasso):** Phạt theo chuẩn $\ell_1$: $\Omega(w) = \lambda \sum |w_i|$. Dẫn đến nghiệm thưa (Sparsity - ép nhiều trọng số về đúng bằng 0), đóng vai trò như bộ chọn lọc đặc trưng tự động.
- **L2 Regularization (Ridge):** Phạt theo chuẩn $\ell_2$: $\Omega(w) = \lambda \sum w_i^2$. Ép các trọng số co nhỏ lại gần 0 nhưng không bao giờ bằng 0 tuyệt đối.

🍼 **Hình dung thực tế cho em bé:**
L1 giống như một chiếc kéo cắt cành tỉa lá: Nó thẳng tay cắt phăng những thuộc tính vô dụng và gán trọng số của chúng bằng đúng 0 (bỏ hẳn cột đó ra khỏi mô hình). Còn L2 giống như một chiếc dây cao su: Nó co kéo tất cả các trọng số lại thật nhỏ và đều đặn, nhưng vẫn giữ lại tất cả các cành lá chứ không cắt bỏ cành nào!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Về mặt hình học: Miền giới hạn của L1 là hình thoi (Diamond) có các góc nhọn nằm trên các trục tọa độ. Đường đồng mức sai số Elip có xác suất rất cao chạm vào các góc nhọn này đầu tiên $\implies$ Trọng số tại trục đó bằng 0. Miền của L2 là hình tròn trơn láng, không có góc nhọn. Chọn **A** (L1 tạo ra nghiệm thưa ép trọng số về 0, L2 co nhỏ trọng số nhưng không triệt tiêu về 0).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B & C:** Đảo lộn vai trò giữa L1 và L2.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.2 Hồi quy tuyến tính & Regularization L1/L2**.
🔗 **Liên hệ bài cũ:** Khi muốn kết hợp ưu điểm của cả L1 (chọn đặc trưng) và L2 (ổn định khi đa cộng tuyến), ta sử dụng **ElasticNet**: $\mathcal{L} + \lambda_1 \|w\|_1 + \lambda_2 \|w\|_2^2$.

---

### Câu 38 [VOAI03-M38] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong cây quyết định, việc thiết lập tham số `max_depth` quá lớn mà không có cơ chế cắt tỉa sẽ dẫn đến:

- **A.** Mô hình bị Overfitting do cây quá sâu, phân nhánh cục bộ và học thuộc cả các điểm nhiễu
- **B.** Mô hình bị Underfitting do ranh giới quyết định trở nên quá phẳng và thiên vị lớp đa số
- **C.** Độ chệch (Bias) của mô hình tăng cao khiến sai số trên cả tập Train và Validation đều lớn
- **D.** Thời gian huấn luyện giảm đi đáng kể do số lượng phép so sánh tại mỗi nút lá bị thu hẹp

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **`max_depth` (Độ sâu tối đa):** Số tầng quyết định tối đa từ nút gốc đến nút lá của cây quyết định.
- **Hiện tượng Overfitting ở cây:** Cây quyết định không bị ràng buộc sẽ tiếp tục phân chia cho đến khi mọi nút lá đều thuần khiết tuyệt đối (Pure Leaf - chứa đúng 1 mẫu), dẫn đến việc ghi nhớ từng điểm nhiễu.

🍼 **Hình dung thực tế cho em bé:**
Một cây quyết định có độ sâu 20 có thể chứa tới $2^{20} \approx 1,000,000$ nút lá! Nếu tập dữ liệu chỉ có 5,000 dòng, cây sẽ hỏi từng câu hỏi li ti để học thuộc lòng từng dòng dữ liệu một cách máy móc. Mô hình sẽ đạt 100% độ chính xác trên tập Train nhưng sẽ đoán sai bét nhè trên tập Test $\implies$ Overfitting nặng nề!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi `max_depth` tăng lên vô hạn, Bias của mô hình giảm về 0 nhưng Variance tăng vọt tới cực đại (Overfitting). Chọn **A** (Mô hình bị Overfitting do cây quá phức tạp học thuộc dữ liệu huấn luyện).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Underfitting):** Chỉ xảy ra khi `max_depth` quá nhỏ (ví dụ depth=1, gọi là Decision Stump).
- **Phương án C (Chạy nhanh hơn):** Cây càng sâu càng tốn thời gian tính toán và bộ nhớ RAM.
- **Phương án D:** Không có mô hình nào đạt độ chính xác tối ưu trên mọi tập dữ liệu nếu bị Overfitting.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.3 Cây quyết định, Entropy & Information Gain**.
🔗 **Liên hệ bài cũ:** Trong các thư viện LightGBM và XGBoost, giá trị `max_depth` tối ưu thường chỉ nằm trong khoảng từ 3 đến 8 để kiểm soát hiện tượng quá khớp.

---

### Câu 39 [VOAI03-M39] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong phân tích dữ liệu khám phá (EDA), biểu đồ Hộp (Boxplot) là công cụ cực kỳ hữu hiệu để nhanh chóng phát hiện:

- **A.** Tần suất xuất hiện từ vựng (Word Frequency) trong kho ngữ liệu văn bản theo phân phối Zipf
- **B.** Mối quan hệ tương quan tuyến tính (Pearson Correlation) và hệ số góc hồi quy giữa hai biến
- **C.** Ma trận hiệp phương sai (Covariance Matrix) và các vector riêng trực giao của không gian đặc trưng
- **D.** Các giá trị ngoại lai (Outliers) và các mốc tứ phân vị (Q1, Median, Q3, IQR) của phân phối

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Boxplot (Biểu đồ hộp - Tukey Boxplot):** Công cụ trực quan hóa phân phối dữ liệu dựa trên 5 con số thống kê: Min, $Q_1$ (Phân vị 25%), Median ($Q_2$ - Trung vị 50%), $Q_3$ (Phân vị 75%), Max.
- **IQR (Interquartile Range - Khoảng tứ phân vị):** $\text{IQR} = Q_3 - Q_1$.
- **Quy tắc Tukey phát hiện ngoại lai (Outliers):** Điểm nằm ngoài đoạn $[Q_1 - 1.5 \text{IQR}, Q_3 + 1.5 \text{IQR}]$.

🍼 **Hình dung thực tế cho em bé:**
Biểu đồ hộp giống như một chiếc vali đựng đồ: Chiếc vali chữ nhật chứa 50% số bạn học sinh ở khúc giữa của lớp. Hai chiếc quai (râu) kéo dài ra hai đầu để đón những bạn có điểm số bình thường. Nếu có bạn nào điểm số quá cao đột biến hoặc thấp bất thường vượt ra ngoài tầm với của chiếc râu, bạn đó sẽ bị đánh dấu thành một dấu chấm tròn cô đơn bên ngoài — đó chính là điểm ngoại lai (Outlier)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khoảng cách giữa hai râu của Boxplot:
- Râu dưới: $\max(\text{Min}, Q_1 - 1.5 \times \text{IQR})$.
- Râu trên: $\min(\text{Max}, Q_3 + 1.5 \times \text{IQR})$.
Mọi điểm nằm ngoài khoảng này đều được coi là Outliers. Chọn **D** (Phát hiện điểm dữ liệu ngoại lai - Outliers và phân bố tứ phân vị).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A:** Đo tương quan giữa 2 biến liên tục dùng biểu đồ phân tán (Scatter Plot) hoặc ma trận tương quan (Heatmap).
- **Phương án B:** Đánh giá phân loại dùng Confusion Matrix.
- **Phương án C:** Kiểm tra tương quan chuỗi thời gian dùng biểu đồ đường hoặc ACF.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§5.4 Thống kê mô tả & Phân tích khám phá EDA**.
🔗 **Liên hệ bài cũ:** Khác với giá trị trung bình (Mean) và độ lệch chuẩn (Std) rất dễ bị bóp méo bởi các giá trị ngoại lai cực đoan, Trung vị ($Q_2$) và IQR của Boxplot có tính bền vững (Robust Statistics) cực kỳ cao.

---

### Câu 40 [VOAI03-M40] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Early Stopping dừng quá trình huấn luyện mạng nơ-ron dựa trên tín hiệu nào chuẩn xác nhất?

- **A.** Khi Validation Loss không giảm hoặc tăng liên tục qua số epoch quy định (Patience Limit)
- **B.** Khi số lượng epoch đạt đúng giới hạn tối đa (Max Epochs) do người dùng thiết lập trong cấu hình
- **C.** Khi tốc độ tính toán phần cứng của GPU bị suy giảm (Thermal Throttling) do nhiệt độ vượt ngưỡng
- **D.** Khi Training Loss đạt giá trị bằng 0 tuyệt đối (Zero Loss) và độ chính xác train chạm ngưỡng 100%

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Early Stopping (Dừng sớm):** Kỹ thuật điều chuẩn (Regularization) trong huấn luyện mạng nơ-ron và mô hình Boosting.
- **Cơ chế hoạt động:** Giám sát hàm mất mát hoặc chỉ số đánh giá trên tập kiểm định (Validation Loss / Metric). Khi Validation Loss không còn giảm sau một số lượng epoch nhất định (tham số `patience`), quá trình huấn luyện sẽ dừng lại và khôi phục lại trọng số tại thời điểm tốt nhất.

🍼 **Hình dung thực tế cho em bé:**
Early Stopping giống như việc nướng một chiếc bánh trong lò vi sóng: Ban đầu chiếc bánh chín dần và thơm ngon (Validation Loss giảm). Nhưng nếu bạn cứ để lò bật quá lâu, chiếc bánh sẽ bị cháy khét (Train Loss vẫn giảm do học vẹt, nhưng Validation Loss bắt đầu tăng vọt do Overfitting). Early Stopping là chiếc cảm biến tự động ngắt điện đúng lúc chiếc bánh vừa chín tới hoàn hảo!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thuật toán Early Stopping:
$$\text{Nếu } \mathcal{L}_{\text{val}}^{(t)} > \min_{s < t} \mathcal{L}_{\text{val}}^{(s)} \quad \text{liên tục trong } P \text{ epochs (Patience)} \implies \text{Dừng và Khôi phục } \theta^*$$
Chọn **A** (Sai số trên tập kiểm định - Validation Loss bắt đầu tăng trở lại).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Train Loss bằng 0):** Khi Train loss = 0 mô hình đã bị Overfitting nghiêm trọng.
- **Phương án C (Hết số epoch tối đa):** Đó là dừng theo giới hạn vòng lặp, không phải dừng sớm.
- **Phương án D:** Gradient bằng 0 chỉ xảy ra khi chạm điểm dừng hoặc bị Vanishing Gradient.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§2.3 Vòng lặp huấn luyện mạng nơ-ron: Forward, Loss & Backward**.
🔗 **Liên hệ bài cũ:** Trong PyTorch Lightning hoặc Keras, callback `EarlyStopping(monitor=' val_loss ', patience=5, restore_best_weights=True)` là trang bị bắt buộc để tránh lãng phí GPU và chống quá khớp.

---

### Câu 41 [VOAI03-M41] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Điểm khác biệt cốt lõi nhất giữa phương pháp Bagging (như Random Forest) và Boosting (như XGBoost) là:

- **A.** Bagging chỉ áp dụng cho bài toán phân loại đa lớp; Boosting chỉ áp dụng cho bài toán hồi quy liên tục
- **B.** Boosting tập trung giảm phương sai (Variance); Bagging tập trung giảm độ chệch (Bias) của mô hình
- **C.** Bagging luôn luôn đạt độ chính xác cao hơn Boosting trên mọi tập dữ liệu bảng có cấu trúc thưa
- **D.** Bagging xây dựng các cây độc lập song song; Boosting xây dựng các cây tuần tự nối tiếp nhau học phần dư

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Bagging (Bootstrap Aggregating):** Huấn luyện SONG SONG các mô hình độc lập trên các tập con dữ liệu lấy mẫu có hoàn lại. Mục tiêu chính: Giảm phương sai (Reduce Variance), chống Overfitting.
- **Boosting:** Huấn luyện TUẦN TỰ các mô hình, mô hình sau tập trung tối ưu hàm mất mát để sửa chữa sai số của các mô hình trước. Mục tiêu chính: Giảm độ chệch (Reduce Bias).

🍼 **Hình dung thực tế cho em bé:**
Sự khác biệt cốt lõi:
- Bagging giống như một hội đồng 100 học sinh cùng làm bài thi độc lập rồi lấy trung bình điểm số (mỗi người giỏi một phần, tổng thể triệt tiêu sai số ngẫu nhiên $\implies$ Giảm Variance).
- Boosting giống như một người học sinh làm bài tập nhiều lần: Lần 1 làm sai câu nào thì lần 2 tập trung học kỹ câu đó; lần 2 vẫn sai thì lần 3 dồn toàn lực sửa tiếp $\implies$ Nâng cao trình độ từ dốt thành giỏi (Giảm Bias)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Bagging: $\mathbb{E}[\bar{f}] = \mathbb{E}[f_i]$ (Bias không đổi), $\text{Var}(\bar{f}) \approx \frac{\sigma^2}{B}$ (Variance giảm mạnh).
Boosting: $\text{Bias}$ giảm liên tục sau mỗi vòng lặp thông qua việc học phần dư (Residuals). Chọn **D** (Bagging chạy song song nhằm giảm Variance; Boosting chạy tuần tự nhằm giảm Bias).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A & B:** Đảo lộn bản chất giữa Bagging và Boosting.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Vì Boosting liên tục ép mô hình học các mẫu khó, nếu số lượng cây (Trees) quá lớn và learning rate không phù hợp, Boosting RẤT DỄ BỊ OVERFITTING (ngược lại với Random Forest hầu như không bị overfitting khi tăng số cây).

---

### Câu 42 [VOAI03-M42] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán CatBoost nổi tiếng nhờ khả năng xử lý tự động và tối ưu loại dữ liệu nào mà không cần qua bước One-Hot Encoding thủ công?

- **A.** Dữ liệu ảnh màu RGB
- **B.** Dữ liệu dạng âm thanh
- **C.** Dữ liệu dạng phân loại (Categorical features)
- **D.** Dữ liệu dạng chuỗi thời gian (Time-series)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **CatBoost (Categorical Boosting):** Thuật toán Gradient Boosting do Yandex phát triển (2017).
- **Đặc điểm nổi bật nhất:** Tên gọi CatBoost bắt nguồn từ **Cat**egorical + **Boost**ing. Nó nổi tiếng nhờ kỹ thuật mã hóa biến định danh tự động (Ordered Target Statistics) và cây đối xứng (Oblivious Trees) chạy cực nhanh trên GPU.

🍼 **Hình dung thực tế cho em bé:**
Hầu hết các thuật toán ML khi gặp cột chữ (như Tỉnh/Thành phố có 63 giá trị) đều bắt lập trình viên phải tự đổi thành dạng One-Hot Encoding (làm dữ liệu phình to 63 cột) hoặc Label Encoding. CatBoost thông minh hơn hẳn: Bạn chỉ cần chỉ định tên cột chữ (`cat_features`), CatBoost sẽ tự động biến đổi thành các con số xác suất tối ưu mà không bị rò rỉ dữ liệu!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 CatBoost tính toán Target Encoding dựa trên hoán vị ngẫu nhiên (Random Permutations) của tập dữ liệu để ngăn chặn hiện tượng Target Leakage. Chọn **C** (Dữ liệu dạng phân loại / danh mục - Categorical Features).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Ảnh chụp vệ tinh):** Dùng CNN hoặc Vision Transformer.
- **Phương án B (Âm thanh sóng):** Dùng 1D-CNN hoặc mô hình chuỗi / Spectrogram.
- **Phương án D (Đồ thị):** Dùng Graph Neural Networks (GNN).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Trong các cuộc thi dữ liệu bảng (Kaggle / OLP AI Tabular), CatBoost thường là lựa chọn số 1 khi bộ dữ liệu chứa nhiều cột phân loại có độ đo lớn (High-cardinality Categoricals).

---

### Câu 43 [VOAI03-M43] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán LightGBM sử dụng chiến lược phát triển cây nào giúp nó chạy nhanh hơn và tốn ít bộ nhớ hơn so với XGBoost truyền thống?

- **A.** Full-depth growth (Phát triển toàn bộ độ sâu cùng lúc)
- **B.** Leaf-wise growth (Phát triển theo chiều sâu của lá có mức giảm loss lớn nhất)
- **C.** Level-wise growth (Phát triển theo chiều ngang của cả tầng)
- **D.** Random growth (Phát triển ngẫu nhiên)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **LightGBM (Light Gradient Boosting Machine):** Thuật toán do Microsoft phát triển (2016).
- **Chiến lược Leaf-wise (Best-first):** Tại mỗi bước phân chia, thuật toán tìm nút lá có độ giảm tổn thất (Loss reduction) lớn nhất trên toàn bộ cây để tách tiếp, bất kể độ sâu của lá đó.
- **Chiến lược Level-wise (Depth-first):** Phân chia đều tất cả các nút trên cùng một tầng trước khi xuống tầng tiếp theo (như XGBoost truyền thống).

🍼 **Hình dung thực tế cho em bé:**
XGBoost truyền thống giống như một đội xây nhà làm việc tuần tự: Phải xây xong toàn bộ tầng 1 thì mới được phép xây lên tầng 2 (Level-wise). Còn LightGBM giống như một nhà thầu linh hoạt: Phòng nào xây nhanh nhất và mang lại nhiều lợi ích nhất thì tập trung xây cao vút lên trước (Leaf-wise). Cách làm này giảm sai số nhanh hơn rất nhiều nhưng cần giới hạn `max_depth` để không bị Overfitting!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Chiến lược Leaf-wise có thể giảm nhiều hàm mất mát hơn với cùng số lượng phép tách so với Level-wise. Đồng thời, LightGBM kết hợp thuật toán rời rạc hóa Histogram giúp tăng tốc độ huấn luyện gấp 10-20 lần. Chọn **B** (Chiến lược phát triển cây theo lá - Leaf-wise / Best-first).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Level-wise):** Là chiến lược mặc định của XGBoost truyền thống.
- **Phương án C (Oblivious Tree):** Là cấu trúc cây nhị phân đối xứng của CatBoost.
- **Phương án D (Random Split):** Là đặc trưng của Extra Trees.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Để kiểm soát Overfitting khi dùng Leaf-wise trong LightGBM, bạn luôn phải đặt tham số `num_leaves` nhỏ hơn $2^{\text{max\_depth}}$ (thường đặt `num_leaves = 31`).

---

### Câu 44 [VOAI03-M44] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp ' Stacking ' trong Ensemble Learning hoạt động theo cơ chế nào?

- **A.** Nhân kết quả dự báo của từng mô hình cơ sở với một trọng số tĩnh được xác định từ trước
- **B.** Dùng đầu ra dự báo của các mô hình cơ sở làm đặc trưng đầu vào cho một mô hình meta-learner cấp cao hơn
- **C.** Lấy trung bình cộng đơn giản xác suất dự báo của tất cả các mô hình cơ sở mà không huấn luyện thêm
- **D.** Loại bỏ hoàn toàn các mô hình có độ chính xác thấp hơn trung bình và chỉ giữ lại mô hình tốt nhất

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Stacking (Stacked Generalization):** Phương pháp Ensemble học kết hợp mô hình meta (Meta-learner).
- **Cơ chế:** Dùng dự đoán của nhiều mô hình nền tảng (Base Models - ví dụ XGBoost, CatBoost, Random Forest, Neural Net) làm các đặc trưng đầu vào mới ($X_{\text{meta}}$) để huấn luyện một mô hình cấp cao hơn (Meta-model - thường là Ridge hoặc Logistic Regression).
- **Out-of-Fold (OOF) Predictions:** Bắt buộc dùng dự đoán OOF từ K-Fold Cross-Validation để tạo $X_{\text{meta}}$ nhằm chống rò rỉ dữ liệu.

🍼 **Hình dung thực tế cho em bé:**
Stacking giống như một hội đồng thẩm phán: Các luật sư và chuyên gia khác nhau (Base Models) đưa ra các bản báo cáo nhận định độc lập. Một thẩm phán trưởng công tâm (Meta-Learner) sẽ ngồi lại, cân nhắc xem trong trường hợp nào thì nên tin chuyên gia nào, để đưa ra phán quyết cuối cùng chính xác nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Pipeline Stacking chuẩn mực:
1. Chia Train set thành $K$ folds.
2. Với mỗi Base Model, dự đoán OOF trên $K$ folds để ghép lại thành ma trận đặc trưng $X_{\text{meta}}$.
3. Huấn luyện Meta-Model trên $(X_{\text{meta}}, y_{\text{train}})$.
Chọn **B** (Dùng dự đoán của các mô hình cơ sở làm đầu vào để huấn luyện một mô hình Meta-Learner).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Tính trung bình trọng số):** Đó là kỹ thuật Weighted Blending thông thường.
- **Phương án C (Nhân bản cây):** Đó là Bagging.
- **Phương án D:** Không có liên quan đến Stacking.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Stacking là vũ khí tối thượng giúp các đội thi giật giải cao trong các kỳ thi học máy và AI Olympic khi kết hợp được thế mạnh của cả họ mô hình Cây (Trees) và mạng Học sâu (Deep Learning).

---

### Câu 45 [VOAI03-M45] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi xây dựng một cây quyết định đơn lẻ trong thuật toán Random Forest, tại mỗi nút chia, thuật toán sẽ:

- **A.** Luôn chọn đặc trưng có giá trị trung bình lớn nhất (Max Mean) để thực hiện phép phân nhánh nhị phân
- **B.** Chỉ chọn ngẫu nhiên một tập con các đặc trưng (thường là $\sqrt{p}$) để tìm điểm chia tốt nhất
- **C.** Tính ma trận tương quan (Linear Correlation) giữa các đặc trưng và chọn biến có phụ thuộc cao nhất
- **D.** Duyệt qua toàn bộ tất cả đặc trưng hiện có (Full Features) để tìm điểm chia có Information Gain cực đại

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Feature Subsampling (Lấy mẫu ngẫu nhiên đặc trưng):** Kỹ thuật chọn ngẫu nhiên một tập con đặc trưng tại mỗi nút phân chia của cây quyết định.
- **Mục tiêu cốt lõi:** Làm giảm sự tương quan (Decorrelate) giữa các cây trong rừng (Random Forest).
- **Số lượng đặc trưng chuẩn:** Cho bài toán Phân loại là $m = \lfloor \sqrt{p} \rfloor$; cho Hồi quy là $m = \lfloor p/3 \rfloor$ (với $p$ là tổng số cột đặc trưng).

🍼 **Hình dung thực tế cho em bé:**
Nếu trong dữ liệu có một cột quá mạnh (ví dụ cột ' Mức lương ' quyết định 80% khả năng mua nhà), thì nếu không lấy mẫu ngẫu nhiên, tất cả 100 cây trong rừng đều sẽ chọn cột ' Mức lương ' ở nút đầu tiên! Khi đó 100 cây sẽ trông giống hệt nhau, việc bỏ phiếu tập thể trở nên vô nghĩa. Bằng cách giấu bớt các cột mạnh ở một số cây, các cây buộc phải tìm tòi những cột tiềm năng khác $\implies$ Rừng đa dạng và mạnh mẽ hơn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức phương sai của Random Forest:
$$\text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$$
Khi lấy mẫu đặc trưng ngẫu nhiên $m = \sqrt{p}$, hệ số tương quan giữa các cây $\rho$ giảm xuống rõ rệt, kéo phương sai tổng thể của cả khu rừng giảm theo. Chọn **B** (Giảm độ tương quan giữa các cây trong rừng giúp tăng tính khái quát hóa).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A (Tăng độ tương quan):** Ngược lại, mục tiêu là GIẢM tương quan.
- **Phương án C & D:** Không phải mục đích chính.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Xem câu M08 Đề 03: Đây chính là điểm khác biệt sống còn giữa Random Forest và Bagging cây quyết định thông thường (Bagging thường dùng toàn bộ $p$ đặc trưng tại mỗi nút).

---

### Câu 46 [VOAI03-M46] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình FT-Transformer (Feature Tokenizer + Transformer, Gorishniy et al.) dành cho dữ liệu bảng áp dụng cơ chế Self-Attention vào đâu?

- **A.** Áp dụng tích chập 1D dọc theo trục hàng để trích xuất đặc trưng tuần tự thay cho Self-Attention
- **B.** Giữa các đặc trưng (các cột) khác nhau sau khi đã được Feature Tokenizer mã hóa thành các vector nhúng
- **C.** Giữa các cây quyết định trong một rừng ngẫu nhiên để tổng hợp trọng số biểu quyết thích ứng
- **D.** Giữa các mẫu dữ liệu khác nhau (các hàng) dọc theo chiều batch size để mô hình hóa tương quan mẫu

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **FT-Transformer (Feature Tokenizer + Transformer):** Kiến trúc Deep Learning cho dữ liệu bảng do Gorishniy et al. đề xuất năm 2021.
- **Feature Tokenizer:** Biến đổi từng giá trị số (Numerical feature) và biến danh mục (Categorical feature) thành một vector nhúng (Embedding vector) kích thước $d$.
- **Multi-Head Self-Attention:** Cho phép các cột trong cùng một dòng dữ liệu tương tác qua lại để học quan hệ phi tuyến phức tạp.

🍼 **Hình dung thực tế cho em bé:**
Trong xử lý ngôn ngữ tự nhiên, mỗi từ ngữ được biến thành một vector embedding. FT-Transformer áp dụng y nguyên ý tưởng đó cho bảng tính: Biến cột ' Tuổi tác = 25' và cột ' Huyết áp = 120' thành hai vector ngữ nghĩa độc lập, sau đó cho chúng ' nói chuyện ' với nhau qua cơ chế Self-Attention giống hệt mô hình ngôn ngữ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 FT-Transformer áp dụng phép chiếu tuyến tính có trọng số độc lập cho từng đặc trưng số: $e_j(x_j) = x_j \cdot W_j + b_j \in \mathbb{R}^d$. Sau đó đưa chuỗi các tokens đặc trưng qua nhiều tầng Transformer Encoder. Chọn **B** (Biến đổi từng đặc trưng số và danh mục thành vector nhúng Feature Token rồi qua Transformer).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A:** Chỉ là MLP thông thường.
- **Phương án C:** ResNet cho dữ liệu bảng dùng skip connection, không có tokenizer.
- **Phương án D:** XGBoost là cây, không phải mạng Transformer.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Deep Learning cho Dữ liệu bảng (Modern Tabular DL)**.
🔗 **Liên hệ bài cũ:** Mặc dù FT-Transformer rất mạnh mẽ và học được biểu diễn trừu tượng cao, nhưng trên dữ liệu bảng thông thường, các mô hình cây Boosting (XGBoost/LightGBM/CatBoost) vẫn chiếm ưu thế áp đảo về tốc độ huấn luyện và khả năng chống nhiễu.

---

### Câu 47 [VOAI03-M47] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình Neural Tabular nào gần đây (ICLR 2025) nổi tiếng với việc chia sẻ tham số (parameter sharing) hiệu quả để tạo ra một mini-ensemble gồm nhiều mạng nơ-ron bên trong một kiến trúc duy nhất?

- **A.** TabM (Tabular Model with Mini-Ensembles)
- **B.** SAINT
- **C.** NODE (Neural Oblivious Decision Ensembles)
- **D.** TabNet

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **TabM (Tabular Model with Parameter Batching):** Mô hình Deep Learning cho dữ liệu bảng tiên tiến nhất được chấp nhận tại hội nghị đỉnh cao **ICLR 2025**.
- **Điểm đột phá:** Sử dụng một thân mạng MLP đa tầng chia sẻ (Shared Backbone) kết hợp với các vector tham số mảng hóa (Batch of Parameter Vectors), cho phép dự báo ensemble gồm $k$ mô hình chỉ với chi phí tính toán và bộ nhớ xấp xỉ một mô hình đơn lẻ!

🍼 **Hình dung thực tế cho em bé:**
Trước đây, muốn ensemble 32 mô hình học sâu, bạn phải tốn gấp 32 lần thời gian và bộ nhớ GPU. TabM giống như một thân cây cổ thụ dùng chung một bộ rễ và thân chính vững chắc, nhưng trên ngọn tách ra 32 nhánh cành siêu nhẹ. Nhờ đó bạn có được sức mạnh của cả một đội quân 32 chuyên gia nhưng tốc độ chạy nhanh như một người đơn độc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 TabM biểu diễn các trọng số dưới dạng tensor 3 chiều: $W \in \mathbb{R}^{k \times d_{in} \times d_{out}}$ được tính toán song song qua phép nhân ma trận mảng hóa (Batch Matrix Multiplication). Chọn **A** (Mô hình TabM ICLR 2025 với cơ chế Parameter Batching chia sẻ backbone).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B, C, D:** Các mô hình thế hệ trước (TabNet 2019, NODE 2020, Saint 2021).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Deep Learning cho Dữ liệu bảng (Modern Tabular DL)**.
🔗 **Liên hệ bài cũ:** Đây là kiến thức đón đầu công nghệ mới nhất xuất hiện trong các đề thi tuyển chọn tài năng AI và Olympic AI 2025-2026.

---

### Câu 48 [VOAI03-M48] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán Gradient Boosting xây dựng các cây quyết định dựa trên nguyên lý chủ đạo nào?

- **A.** Mỗi cây sau cố gắng học cách dự báo phần dư âm (Negative Gradient) của các cây đứng trước nó
- **B.** Cây sau phải có độ sâu gấp đôi cây trước (Tree Doubling) để tăng dung lượng biểu diễn qua các vòng lặp
- **C.** Loại bỏ ngẫu nhiên 50% dữ liệu (Random Subsampling) trước khi xây dựng cây mới nhằm đa dạng hóa
- **D.** Các cây được huấn luyện độc lập hoàn toàn (Parallel Training) và kết quả tổng hợp bằng biểu quyết

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Gradient Boosting:** Thuật toán huấn luyện chuỗi các cây quyết định tuần tự bằng phương pháp giảm độ dốc (Gradient Descent) trong không gian hàm.
- **Phần dư giả (Pseudo-residuals):** Đạo hàm âm của hàm mất mát theo dự đoán hiện tại: $r_{im} = -\left[ \frac{\partial \mathcal{L}(y_i, F(x_i))}{\partial F(x_i)} \right]_{F=F_{m-1}}$.
- **Ý nghĩa:** Cây mới ở bước $m$ được huấn luyện để xấp xỉ các phần dư này.

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng bạn đang ném phi tiêu vào hồng tâm: Lần ném thứ nhất bị lệch sang trái 10 cm ($F_1$). Lần ném thứ hai, bạn không ném lại từ đầu, mà bạn bảo đồng đội của mình hãy nhắm bù sang phải đúng 10 cm ($h_2$). Tổng hợp hai lần ném ($F_1 + h_2$) phi tiêu sẽ găm trúng hồng tâm! Gradient Boosting liên tục huấn luyện cây sau để bù đắp đúng phần sai số còn lại của các cây trước.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thuật toán Gradient Boosting:
$$F_m(x) = F_{m-1}(x) + \eta \sum_{j=1}^J \gamma_{jm} \mathbb{I}(x \in R_{jm})$$
Trong đó cây thứ $m$ khớp trực tiếp vào giá trị âm của đạo hàm (Negative Gradient / Residuals). Chọn **A** (Học phần sai số dư - Residuals / Negative Gradient của các cây trước đó).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B (Tăng trọng số mẫu sai):** Đó là cơ chế riêng của AdaBoost (Adaptive Boosting), không phải tổng quát của Gradient Boosting.
- **Phương án C:** Cây sau không chạy độc lập mà phụ thuộc vào cây trước.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Đối với hàm mất mát MSE $\mathcal{L} = \frac{1}{2}(y - \hat{y})^2$, đạo hàm âm $-\partial \mathcal{L} / \partial \hat{y}$ chính bằng phần dư thực tế $y - \hat{y}$.

---

### Câu 49 [VOAI03-M49] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong CatBoost, kỹ thuật ' Ordered Boosting ' được thiết kế đặc biệt nhằm giải quyết triệt để vấn đề gì?

- **A.** Hiện tượng Target Leakage và Overfitting trong quá trình tính toán gradient trên tập dữ liệu nhỏ
- **B.** Hiện tượng bùng nổ gradient khi số lượng cây quyết định trong mô hình ensemble vượt quá 10.000 cây
- **C.** Sự phụ thuộc tuyến tính giữa các biến đặc trưng đầu vào thông qua phép chiếu trực giao ma trận
- **D.** Hiện tượng mô hình bị Underfitting nặng khi dữ liệu có nhiều biến phân loại có cardinality cực lớn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Target Leakage (Rò rỉ biến mục tiêu trong Target Encoding):** Khi tính giá trị trung bình mục tiêu của một danh mục, nếu dùng luôn giá trị $y_i$ của chính dòng đó, mô hình sẽ bị rò rỉ nhãn và Overfitting nghiêm trọng.
- **Ordered Target Statistics (CatBoost):** Hoán vị ngẫu nhiên toàn bộ tập dữ liệu, và khi tính thống kê cho dòng thứ $i$, chỉ sử dụng các dòng có cùng danh mục đứng TRƯỚC nó trong thứ tự hoán vị.
- **Ordered Boosting:** Áp dụng nguyên lý trật tự thời gian nhân tạo này vào cả quá trình tính toán gradient để loại bỏ hiện tượng lệch dự đoán (Prediction Shift).

🍼 **Hình dung thực tế cho em bé:**
Nếu bạn tính điểm trung bình của một học sinh bằng cách lấy cả bài thi của chính bạn đó vào mẫu số, bạn đó sẽ tự chấm điểm cho mình (rò rỉ mục tiêu!). Kỹ thuật Ordered Boosting giống như việc xếp hàng các học sinh theo một trật tự ngẫu nhiên: Bạn đứng ở vị trí số 10 chỉ được phép tham khảo kết quả của 9 bạn đứng trước mình trong hàng, tuyệt đối không được nhìn bài của chính mình hay của các bạn đứng sau!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Ordered Target Statistic của CatBoost cho mẫu $x_k$ tại hoán vị $\sigma$:
$$\hat{x}_{k}^j = \frac{\sum_{j=1}^{k-1} [x_{\sigma(j), k} = x_{\sigma(i), k}] \cdot y_{\sigma(j)} + a \cdot P}{\sum_{j=1}^{k-1} [x_{\sigma(j), k} = x_{\sigma(i), k}] + a}$$
Triệt tiêu hoàn toàn rò rỉ thông tin mục tiêu. Chọn **A** (Ngăn ngừa rò rỉ mục tiêu - Target Leakage và hiện tượng Prediction Shift).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án B:** Ordered Boosting tốn thêm thời gian tính toán hoán vị, không làm tăng tốc độ.
- **Phương án C & D:** Không phải mục đích của kỹ thuật này.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.
🔗 **Liên hệ bài cũ:** Nhờ Ordered Boosting, CatBoost là thư viện GBDT duy nhất có khả năng chạy mượt mà ngay trên các bộ dữ liệu nhỏ mà không bị hiện tượng quá khớp sớm.

---

### Câu 50 [VOAI03-M50] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Tại sao việc áp dụng K-Fold Cross-Validation thông thường trực tiếp lên dữ liệu chuỗi thời gian (Time-series) lại bị coi là sai lầm nghiêm trọng?

- **A.** Dữ liệu chuỗi thời gian có kích thước quá nhỏ (Small Sample) để có thể phân chia thành 5 fold độc lập
- **B.** Các thuật toán học máy chuỗi thời gian không có siêu tham số (No Tuning) cần tinh chỉnh qua validation
- **C.** Làm tăng gấp đôi số lượng mẫu (Data Duplication) do các phép nội suy chồng lấn giữa các fold liên tiếp
- **D.** Phá vỡ tính tuần tự thời gian và dẫn đến rò rỉ dữ liệu từ tương lai vào quá khứ (Look-ahead Bias)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Dữ liệu chuỗi thời gian (Time Series Data):** Dữ liệu có sự phụ thuộc nhân quả theo trật tự thời gian ($t_1 < t_2 < t_3 < \dots$).
- **Temporal Leakage (Rò rỉ thời gian / Look-ahead Bias):** Hiện tượng dùng thông tin từ tương lai để huấn luyện mô hình dự đoán quá khứ.
- **TimeSeriesSplit (Rolling / Expanding Window):** Kỹ thuật chia fold lũy tiến: Tập train luôn đứng trước tập validation theo trục thời gian.

🍼 **Hình dung thực tế cho em bé:**
Dự đoán tương lai (như giá cổ phiếu ngày mai) giống như việc sống trong đời thực: Bạn chỉ có ký ức của ngày hôm qua và hôm nay để quyết định cho ngày mai. Nếu dùng K-Fold ngẫu nhiên, bạn sẽ lấy dữ liệu của ngày thứ Sáu để dự đoán cho ngày thứ Ba! Mô hình sẽ ' nhìn thấy trước tương lai ' và đạt điểm kiểm tra cao giả tạo, nhưng khi đem ra giao dịch thực tế sẽ bị thua lỗ thảm hại!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi áp dụng Standard K-Fold lên Time Series, tính tự tương quan (Autocorrelation) giữa các mốc thời gian liền kề sẽ gây rò rỉ thông tin từ fold train sang fold test, vi phạm giả định độc lập và đồng phân phối (i.i.d). Bắt buộc phải dùng `TimeSeriesSplit`. Chọn **D** (Gây rò rỉ dữ liệu tương lai sang quá khứ - Look-ahead Bias / Temporal Leakage).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
- **Phương án A:** Chuỗi thời gian không nhất thiết phải tuân theo phân phối chuẩn.
- **Phương án B:** K-Fold không làm thay đổi số chiều dữ liệu.
- **Phương án C:** K-Fold vẫn tạo đủ số lượng fold.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Xem **§1.5 Cross-Validation & Chuỗi thời gian (Time Series)**.
🔗 **Liên hệ bài cũ:** Trong đề thi OLP AI, khi gặp bài toán dự báo phụ tải điện, giá thị trường hoặc chuỗi văn bản, luôn ghi nhớ nguyên tắc: KHÔNG BAO GIỜ SHUFFLE DỮ LIỆU CHUỖI THỜI GIAN!

---

### Câu 51 [VOAI03-M51] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** " Global Average Pooling " thường được dùng để:

- **A.** Thay thế các lớp Fully Connected cuối cùng để giảm thiểu số lượng tham số và chống Overfitting
- **B.** Làm mịn hóa ảnh đầu vào bằng bộ lọc trung bình không gian để triệt tiêu các nhiễu tần số cao
- **C.** Tính toán đạo hàm bậc hai của hàm mất mát theo từng vị trí pixel để điều chỉnh tốc độ học
- **D.** Tăng kích thước không gian của feature map lên gấp đôi trước khi chuyển sang nhánh giải mã

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Thay vì duỗi thẳng (flatten) toàn bộ feature map thành một hàng dài tạo ra hàng triệu trọng số kết nối ở lớp Fully Connected, Global Average Pooling (GAP) chỉ đơn giản lấy trung bình cộng tất cả các điểm ảnh trên mỗi kênh (channel). Nếu có 512 kênh, GAP cho ra đúng một vector 512 phần tử, không tốn thêm bất kỳ tham số học nào!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Cho tensor đặc trưng đầu ra của lớp conv cuối $X \in \mathbb{R}^{H \times W \times C}$. Phép tính GAP trên từng kênh $c \in [1, C]$ là:
$$z_c = \frac{1}{H \cdot W} \sum_{h=1}^H \sum_{w=1}^W X_{h, w, c}$$
Vector kết quả $z = [z_1, z_2, \dots, z_C]^T$ có số chiều đúng bằng $C$. Số tham số thêm vào là $0$, giúp giảm đột biến dung lượng mô hình và hạn chế tối đa Overfitting.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Nhiều bạn nhầm GAP với Flatten hoặc Max Pooling. Flatten nối tất cả $H \times W \times C$ giá trị lại thành vector dài, dẫn tới ma trận trọng số ở lớp FC cực lớn ($H \cdot W \cdot C \times K$). GAP không có tham số học và ép mỗi feature map tương ứng với một độ tin cậy của đặc trưng.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Lin, M., Chen, Q., & Yan, S. (2013). Network In Network. ICLR 2014. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**.

---

### Câu 52 [VOAI03-M52] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong ngữ cảnh của Deep Learning, " Epoch " là:

- **A.** Một lần duyệt qua toàn bộ tập dữ liệu huấn luyện.
- **B.** Thời gian huấn luyện tính bằng giây.
- **C.** Một lần duyệt qua một mini-batch.
- **D.** Số lượng nơ-ron trong mạng.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Một Epoch giống như việc bạn đọc xong một lượt từ trang đầu đến trang cuối của một cuốn sách giáo khoa. Tức là toàn bộ các mẫu dữ liệu trong tập huấn luyện (training set) đều đã được mô hình ' nhìn thấy ' và học qua đúng 1 lần.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Giả sử tập train có $N$ mẫu, kích thước mini-batch là $B$. Số bước lặp (iterations/steps) trong $1$ Epoch là:
$$\text{Steps per Epoch} = \left\lceil \frac{N}{B} \right\rceil$$
Sau khi mô hình chạy hết số bước này, toàn bộ $N$ mẫu đã được duyệt qua đúng một chu kỳ trọn vẹn.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Dễ nhầm giữa Epoch (toàn bộ dữ liệu) và Iteration/Step (chỉ một mini-batch gồm $B$ mẫu). Nếu $N = 10,000, B = 32$, một epoch cần 313 iterations.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**.

---

### Câu 53 [VOAI03-M53] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hàm loss " Focal Loss " thường được dùng để giải quyết vấn đề:

- **A.** Hiện tượng biến mất gradient trong các mạng nơ-ron có độ sâu vượt quá 100 tầng tích chập
- **B.** Tối ưu hóa tốc độ tính toán phần cứng GPU bằng cách loại bỏ các phép tính số thực dấu phẩy động
- **C.** Dữ liệu bị mất cân bằng lớp cực hạn bằng cách giảm trọng số của các mẫu dễ phân loại
- **D.** Thiếu hụt dữ liệu huấn luyện ban đầu thông qua cơ chế tự động sinh thêm các mẫu tăng cường

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Trong bài toán phát hiện đối tượng, các ô nền (background) quá nhiều và quá dễ nhận biết khiến mô hình bị áp đảo bởi các mẫu dễ, bỏ quên các vật thể nhỏ/hiếm. Focal Loss thêm một ' bộ điều tiết ' $(1 - p_t)^\gamma$: mẫu nào mô hình đã đoán đúng và tự tin ($p_t \to 1$) thì phạt cực nhỏ, tập trung toàn bộ gradient vào các mẫu khó ($p_t$ thấp)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức Focal Loss cho bài toán phân loại nhị phân:
$$\text{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)$$
Trong đó:
- $p_t$ là xác suất dự đoán cho lớp đúng.
- $\gamma \ge 0$ là siêu tham số điều chế độ tập trung (focusing parameter). Khi $\gamma = 2$, nếu mô hình dự đoán mẫu dễ với $p_t = 0.9$, hệ số phạt giảm đi $(1 - 0.9)^2 = 0.01$ (giảm 100 lần so với Cross-Entropy thông thường!).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Focal Loss không dùng để tăng tốc độ tính toán hay làm sâu mạng, mà là vũ khí đặc trị mất cân bằng lớp cực đoan (Class Imbalance) giữa tiền cảnh và hậu cảnh (Foreground-Background).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Lin, T. Y., et al. (2017). Focal Loss for Dense Object Detection (RetinaNet). ICCV 2017. Xem **§3.2 Định vị & Phát hiện đối tượng**.

---

### Câu 54 [VOAI03-M54] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Vision Transformer (ViT), ảnh đầu vào được xử lý như thế nào trước khi đưa vào
Transformer?

- **A.** Giữ nguyên ma trận điểm ảnh thô (Raw Pixels) và đưa trực tiếp vào các tầng tích chập Conv2D 1x1 đa kênh
- **B.** Chuyển ảnh sang miền tần số (2D-FFT) và chỉ trích xuất các thành phần tần số thấp để làm token
- **C.** Đưa ảnh qua 50 tầng tích chập (ResNet-50) để lấy bản đồ đặc trưng trước khi tokenize thành vector
- **D.** Chia thành các mảnh vuông (Patches), chiếu tuyến tính thành vector token và thêm Positional Encoding

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Vision Transformer (ViT) không dùng phép tích chập (Convolution) để quét ảnh. Thay vào đó, nó cắt bức ảnh thành các ô vuông nhỏ giống như các mảnh ghép xếp hình (ví dụ $16 \times 16$ pixel), duỗi thẳng từng mảnh thành vector rồi coi mỗi mảnh như một ' từ ' (token) đưa vào mô hình Transformer tiêu chuẩn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Cho ảnh đầu vào $X \in \mathbb{R}^{H \times W \times C}$ và kích thước mảnh $P \times P$.
1. Số lượng mảnh patch là:
$$N = \frac{H \cdot W}{P^2}$$
2. Mỗi mảnh được duỗi thẳng thành vector chiều dài $P^2 \cdot C$, sau đó chiếu tuyến tính qua ma trận $E \in \mathbb{R}^{(P^2 C) \times D}$ để tạo patch embeddings.
3. Thêm token phân loại $[\text{CLS}]$ và Position Embedding $E_{pos} \in \mathbb{R}^{(N+1) \times D}$ trước khi đưa vào Transformer Encoder.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
ViT không giữ nguyên ma trận ảnh 2D khi đưa vào Encoder và cũng không dùng 50 lớp CNN. Điểm đột phá của ViT là chuyển đổi không gian ảnh 2D thành chuỗi 1D các patch tokens.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Dosovitskiy, A., et al. (2020). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. ICLR 2021. Xem **§3.3 Kiến trúc CV SOTA**.

---

### Câu 55 [VOAI03-M55] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** " Weight Decay " tương đương với kỹ thuật Regularization nào?

- **A.** Batch Normalization.
- **B.** L1 Regularization.
- **C.** L2 Regularization.
- **D.** Dropout.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Weight Decay giống như một lực kéo vô hình luôn kéo độ lớn của các trọng số mạng về số 0 sau mỗi bước cập nhật. Nó tương đương toán học với kỹ thuật điều quy L2 (L2 Regularization), ngăn các trọng số tăng quá lớn dẫn tới ghi nhớ dữ liệu (Overfitting).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Hàm mục tiêu điều quy L2:
$$J_{\text{reg}}(\theta) = J(\theta) + \frac{\lambda}{2} \|w\|_2^2 = J(\theta) + \frac{\lambda}{2} \sum_i w_i^2$$
Quy tắc cập nhật trọng số với đạo hàm:
$$w \leftarrow w - \eta \left( \nabla J(w) + \lambda w \right) = (1 - \eta \lambda) w - \eta \nabla J(w)$$
Hệ số $(1 - \eta \lambda) < 1$ làm suy giảm (decay) trọng số $w$ tỷ lệ thuận với giá trị hiện tại của nó.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
L1 ép trọng số về chính xác $0$ (tạo thưa thớt - sparsity), còn L2 (Weight Decay) ép trọng số tiến gần về $0$ một cách mượt mà chứ không hoàn toàn triệt tiêu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Krogh, A., & Hertz, J. A. (1992). A Simple Weight Decay Can Improve Generalization. NeurIPS 1991. Xem **§1.6 Điều quy L1/L2 & Biến dạng dữ liệu**.

---

### Câu 56 [VOAI03-M56] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp " Bag of Words "(BoW) có nhược điểm lớn nhất là gì?

- **A.** Mất hoàn toàn thông tin về thứ tự tuần tự và ngữ cảnh ngữ nghĩa giữa các từ trong câu văn
- **B.** Không thể biểu diễn được các văn bản có độ dài vượt quá 256 từ trong từ điển từ vựng tĩnh
- **C.** Đòi hỏi thời gian huấn luyện cực lớn do phải tối ưu hóa ma trận trọng số phi tuyến tính
- **D.** Chỉ áp dụng được cho dữ liệu ảnh xám chứ không thể vector hóa văn bản ngôn ngữ tự nhiên

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bag of Words (BoW) giống như việc bạn gom tất cả các từ trong một bài văn vứt vào một cái bao rồi xáo trộn lên: Bạn biết trong bao có từ ' không ', có từ ' ngon ', có từ ' rất ', nhưng không thể biết là ' rất ngon, không dở ' hay ' không ngon, rất dở '! Nó đánh mất hoàn toàn thứ tự từ và ngữ cảnh câu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Mô hình BoW biểu diễn văn bản thành vector tần suất $v \in \mathbb{R}^{|V|}$:
$$v_i = \text{count}(\text{word}_i, \text{doc})$$
Do chỉ đếm số lần xuất hiện rời rạc, hai câu có ý nghĩa trái ngược nhau hoàn toàn như ' Tôi yêu bạn không ghét ' và ' Tôi ghét bạn không yêu ' sẽ có cùng một vector biểu diễn BoW!

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
BoW tính toán rất nhanh (đếm từ) và áp dụng được cho mọi ngôn ngữ, nhưng khuyết điểm cốt tử là hoàn toàn bỏ qua trật tự cú pháp và cấu trúc ngữ nghĩa.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Jurafsky, D., & Martin, J. H. (2024). Speech and Language Processing (3rd ed.). Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 57 [VOAI03-M57] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Word2Vec phiên bản Skip-gram dùng để:

- **A.** Dự đoán các từ ngữ cảnh xung quanh từ một từ mục tiêu.
- **B.** Dự đoán từ mục tiêu từ các từ ngữ cảnh.
- **C.** Phân loại sắc thái câu.
- **D.** Dịch máy.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Trong Word2Vec, nếu CBOW (Continuous Bag of Words) nhìn các từ xung quanh để đoán từ ở giữa, thì Skip-gram làm ngược lại hoàn toàn: Nó lấy từ ở giữa (từ trung tâm) và cố gắng ' phóng tầm nhìn ' dự đoán xem những từ nào có khả năng cao xuất hiện xung quanh nó!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Hàm mục tiêu của Skip-gram là cực đại hóa log-likelihood trên toàn bộ chuỗi từ $w_1, w_2, \dots, w_T$ với cửa sổ ngữ cảnh kích thước $c$:
$$\mathcal{L} = \sum_{t=1}^T \sum_{-c \le j \le c, j \ne 0} \log P(w_{t+j} \mid w_t)$$
Trong đó xác suất có điều kiện được tính bằng softmax:
$$P(w_O \mid w_I) = \frac{\exp(v_{w_O}'^T v_{w_I})}{\sum_{w \in V} \exp(v_w '^T v_{w_I})}$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Nhiều bạn nhầm lẫn giữa CBOW và Skip-gram. Hãy nhớ mẹo: CBOW = Context predicts Target; Skip-gram = Single target predicts Context (Skip-gram học từ hiếm tốt hơn nhiều!).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Mikolov, T., et al. (2013). Distributed Representations of Words and Phrases and their Compositionality. NeurIPS 2013. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 58 [VOAI03-M58] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong NLP, " Stemming " và " Lemmatization " khác nhau ở điểm nào?

- **A.** Stemming dựa trên phân tích cú pháp cây; Lemmatization chỉ cắt bỏ các phụ tố tiền tố đơn giản
- **B.** Lemmatization chỉ áp dụng được cho động từ; Stemming áp dụng cho toàn bộ các từ loại trong câu
- **C.** Stemming cắt đuôi từ bằng quy tắc thô; Lemmatization dùng từ điển và ngữ pháp để đưa về dạng chuẩn
- **D.** Cả hai phương pháp đều hoàn toàn đồng nhất về mặt thuật toán và kết quả đầu ra trong mọi trường hợp

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Stemming giống như dùng một cây kéo cơ học cắt phéng đuôi từ (ví dụ ' studies ', ' studying ' bị cắt thành ' studi ' - một từ không có nghĩa trong từ điển). Trong khi đó, Lemmatization dùng một cuốn từ điển chuẩn và ngữ pháp để đưa từ về nguyên thể chuẩn mực (' studies ' -> ' study ').

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
So sánh hai phương pháp tiền xử lý:
- **Stemming (vd: Porter, Snowball):** Sử dụng tập luật heuristic dựa trên hậu tố string (cắt bỏ ' ing ', ' ed ', ' es '). Tốc độ rất nhanh nhưng hay tạo ra từ vô nghĩa hoặc over-stemming / under-stemming.
- **Lemmatization (vd: WordNetLemmatizer):** Phân tích hình thái học (morphological analysis) kết hợp với nhãn từ loại (Part-of-Speech / POS tag) để tra cứu lemma gốc có nghĩa trong từ điển ngữ liệu.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Không phải Stemming luôn tốt hơn. Lemmatization chính xác hơn về mặt ngữ nghĩa nhưng tốn tài nguyên và thời gian hơn vì phải phân tích từ loại.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Manning, C. D., et al. (2008). Introduction to Information Retrieval. Cambridge University Press. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 59 [VOAI03-M59] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** TF-IDF là viết tắt của:

- **A.** Term Frequency - Inverse Document Frequency.
- **B.** Task Flow - Information Distribution.
- **C.** Text Features - Internal Data Format.
- **D.** Tổng hợp - Phân phối - Thông tin.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
TF-IDF viết tắt của Term Frequency - Inverse Document Frequency. Ý tưởng cốt lõi: Một từ xuất hiện nhiều lần trong văn bản hiện tại (TF cao) nhưng lại hiếm khi xuất hiện ở các văn bản khác trong thư viện (IDF cao) thì từ đó là từ khóa cực kỳ đặc trưng và quan trọng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức TF-IDF cho từ $t$ trong tài liệu $d$ thuộc tập tài liệu $D$ gồm $N = |D|$ văn bản:
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
Trong đó:
$$\text{TF}(t, d) = \frac{f_{t, d}}{\sum_{t ' \in d} f_{t ', d}}, \quad \text{IDF}(t, D) = \log \left( \frac{N}{|\{d \in D: t \in d\}| + 1} \right)$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Các từ nối như ' và ', ' thì ', ' là ' có TF rất cao nhưng xuất hiện trong hầu hết tài liệu nên IDF gần bằng 0, dẫn tới trọng số TF-IDF bị triệt tiêu thích đáng.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval. Information Processing & Management. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 60 [VOAI03-M60] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " BERT " là mô hình dựa trên thành phần nào của Transformer?

- **A.** Decoder.
- **B.** Encoder.
- **C.** Không thành phần nào.
- **D.** Cả hai.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Mô hình Transformer gốc gồm 2 nửa: Encoder (hiểu câu) và Decoder (sinh câu tiếp theo). BERT (Bidirectional Encoder Representations from Transformers) chỉ sử dụng đúng phần Encoder. Nhờ vậy, nó có thể nhìn toàn bộ câu theo cả hai chiều (từ trái qua phải và từ phải qua trái đồng thời) để hiểu sâu sắc ngữ cảnh.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Kiến trúc BERT gồm một chuỗi các lớp Transformer Encoder xếp chồng lên nhau:
$$\text{Input} \to [\text{Patch / Token + Pos + Segment}] \to \text{Encoder}_1 \to \dots \to \text{Encoder}_L \to \text{Contextual Embeddings}$$
Trong mỗi khối Encoder, cơ chế Self-Attention là không bị che (unmasked), cho phép token tại vị trí $i$ chú ý tới mọi token $j \in [1, T]$ trong chuỗi.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Nhầm BERT với GPT. GPT là kiến trúc Decoder-only (dùng Masked Self-Attention để tự hồi quy từ trái sang phải sinh từ). BERT là Encoder-only chuyên dùng để hiểu ngữ nghĩa (NLU - Natural Language Understanding).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Devlin, J., et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL 2019. Xem **§4.2 Cơ chế Attention & Transformer**.

---

### Câu 61 [VOAI03-M61] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Nhiệm vụ " Masked Language Modeling "(MLM) trong BERT có mục đích gì?

- **A.** Học cách tóm tắt các đoạn văn bản dài (Text Summarization) thành các câu ngắn gọn chứa thực thể chính
- **B.** Tự động phát hiện và loại bỏ từ dừng (Stopwords Removal) không mang nhiều ý nghĩa ngữ nghĩa khỏi câu
- **C.** Dịch văn bản từ ngôn ngữ nguồn sang ngôn ngữ đích (Machine Translation) theo cơ chế Cross-Attention
- **D.** Học biểu diễn ngữ cảnh hai chiều (Bidirectional Context) sâu sắc bằng cách dự đoán token bị che khuất

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Masked Language Modeling (MLM) giống trò chơi điền từ vào chỗ trống: Người ta giấu đi một số từ trong câu bằng nhãn [MASK] (ví dụ: ' Hà Nội là [MASK] của Việt Nam ') và bắt mô hình phải dựa vào cả từ đứng trước và từ đứng sau để đoán từ bị giấu đi là ' thủ đô '.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Chiến lược huấn luyện MLM của BERT:
1. Chọn ngẫu nhiên $15\%$ số token trong chuỗi đầu vào.
2. Trong số $15\%$ đó:
   - $80\%$ được thay bằng token đặc biệt `[MASK]`.
   - $10\%$ được thay bằng một token ngẫu nhiên bất kỳ.
   - $10\%$ được giữ nguyên không đổi.
3. Hàm mất mát là Cross-Entropy chỉ tính trên các vị trí được chọn này:
$$\mathcal{L}_{\text{MLM}} = -\sum_{i \in \text{masked}} \log P(x_i \mid \tilde{X})$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
MLM không che toàn bộ các từ hay chỉ nhìn từ bên trái; ưu thế tuyệt đối của nó là khai thác ngữ cảnh hai chiều (bidirectional context) cùng lúc.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Devlin, J., et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL 2019. Xem **§4.2 Cơ chế Attention & Transformer**.

---

### Câu 62 [VOAI03-M62] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " Tokenizer " ở mức độ Sub-word (như BPE) giúp giải quyết vấn đề:

- **A.** Thiếu hụt bộ nhớ đệm VRAM (Memory Overflow) khi xử lý các batch dữ liệu văn bản có độ dài vượt quá 2048
- **B.** Hiện tượng từ ngoài từ điển (Out-of-Vocabulary) bằng cách phân rã từ hiếm thành các mảnh từ con
- **C.** Tự động sửa lỗi chính tả ngữ pháp (Grammar Correction) trong văn bản đầu vào trước khi qua embedding
- **D.** Rút ngắn độ dài câu văn (Token Pruning) bằng cách loại bỏ toàn bộ các dấu câu và ký tự đặc biệt

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Nếu từ điển chỉ lưu các từ nguyên vẹn, gặp từ lạ mới toanh sẽ bị lỗi ' Out Of Vocabulary ' (OOV). Kỹ thuật Subword Tokenization chia từ thành các mảnh nhỏ (như ' unbelievable ' thành ' un ', ' believ ', ' able '). Nhờ đó, bất kỳ từ mới nào cũng có thể ghép lại từ các mảnh con đã biết!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Các thuật toán tách từ con (Subword Tokenization) tiêu biểu:
- **BPE (Byte Pair Encoding):** Bắt đầu từ cấp độ ký tự, đếm và gộp lặp đi lặp lại cặp ký tự xuất hiện nhiều nhất (dùng trong GPT-2, RoBERTa).
- **WordPiece:** Tương tự BPE nhưng chọn cặp ghép làm tăng likelihood của ngôn ngữ nhiều nhất (dùng trong BERT).
- **SentencePiece / Unigram:** Coi khoảng trắng như một ký tự đặc biệt, tối ưu trên mô hình xác suất unigram.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Subword không xóa bỏ từ hiếm mà phân rã từ hiếm thành các mảnh từ vựng con (subwords) có mặt trong kho từ điển cố định.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sennrich, R., et al. (2016). Neural Machine Translation of Rare Words with Subword Units. ACL 2016. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 63 [VOAI03-M63] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Độ đo " Perplexity " thường dùng đểđánh giá:

- **A.** Hiệu năng phân cụm không giám sát (Clustering Performance) của thuật toán K-Means dựa trên tâm cụm
- **B.** Chất lượng của mô hình ngôn ngữ (Language Models) trong việc dự đoán phân phối xác suất từ tiếp theo
- **C.** Băng thông truyền dữ liệu (Network Bandwidth) giữa các cụm máy chủ trong quá trình huấn luyện song song
- **D.** Độ chính xác phân loại (Top-1 Accuracy) của mô hình thị giác máy tính trên các tập dữ liệu ảnh tự nhiên

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Perplexity (PPL) đo mức độ ' bối rối, lúng túng ' của mô hình khi đoán từ tiếp theo. Nếu mô hình đoán từ nào cũng trúng phóc với xác suất cao, nó sẽ rất tự tin và ít bối rối, tức là PPL CÀNG THẤP THÌ MÔ HÌNH CÀNG GIỎI!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức toán học của Perplexity trên chuỗi văn bản $W = (w_1, w_2, \dots, w_N)$:
$$\text{PPL}(W) = \exp \left( -\frac{1}{N} \sum_{i=1}^N \log P(w_i \mid w_1, \dots, w_{i-1}) \right) = 2^{H(W)}$$
Trong đó $H(W)$ là entropy chéo trung bình trên mỗi token. Khi mô hình dự đoán chính xác tuyệt đối ($P=1$), $\log P = 0 \implies \text{PPL} = 1$ (mức lý tưởng nhỏ nhất).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Bẫy đề thi: Thí sinh hay nhầm PPL giống như Accuracy (càng cao càng tốt). Ngược lại: Perplexity là hàm đo độ sai lệch/bối rối, PPL càng THẤP thì chất lượng mô hình ngôn ngữ càng CAO.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Jurafsky, D., & Martin, J. H. (2024). Speech and Language Processing. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 64 [VOAI03-M64] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Transformer, tại sao cần " Positional Encoding "?

- **A.** Để phân biệt danh từ, động từ và tính từ trong câu thông qua các nhãn gán từ loại ngữ pháp
- **B.** Để mô hình nhận biết thứ tự và vị trí tương đối của các từ vì Self-Attention không có tính tuần tự
- **C.** Để tăng số lượng tham số học được của mạng nơ-ron nhằm cải thiện năng lực biểu diễn ngữ nghĩa
- **D.** Để nén độ dài chuỗi văn bản đầu vào thành một vector có số chiều cố định trước khi đưa vào encoder

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Mạng RNN xử lý từng từ một theo thứ tự từ trái sang phải nên tự biết từ nào đứng trước. Nhưng Transformer xử lý tất cả các từ cùng một lúc (song song). Để mô hình biết được ' con mèo đuổi con chuột ' khác với ' con chuột đuổi con mèo ', người ta phải ' dán nhãn số thứ tự ' (Positional Encoding) vào từng từ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Hàm mã hóa vị trí sin-cosin kinh điển trong Vaswani et al. (2017) cho vị trí $pos$ và chiều vector $2i, 2i+1$:
$$PE_{(pos, 2i)} = \sin \left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right)$$
$$PE_{(pos, 2i+1)} = \cos \left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right)$$
Vector này được cộng trực tiếp vào token embedding: $X = X_{\text{token}} + PE$.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Positional Encoding không nhân vào vector mà được CỘNG trực tiếp vào token embedding, giúp mô hình học được mối quan hệ vị trí tương đối thông qua phép biến đổi tuyến tính.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Vaswani, A., et al. (2017). Attention Is All You Need. NeurIPS 2017. Xem **§4.2 Cơ chế Attention & Transformer**.

---

### Câu 65 [VOAI03-M65] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " GPT "(Generative Pre-trained Transformer) sử dụng kiến trúc:

- **A.** Encoder-only.
- **B.** LSTM.
- **C.** RNN kết hợp CNN.
- **D.** Decoder-only.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
GPT (Generative Pre-trained Transformer) là một ' nhà văn ' tự động: nó đọc đoạn văn đã viết và nhiệm vụ duy nhất của nó là đoán xem từ tiếp theo nên là từ gì. Quá trình này lặp đi lặp lại từng từ một gọi là mô hình sinh tự hồi quy (Autoregressive Decoder-only).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Mục tiêu huấn luyện chuẩn của GPT là tối đa hóa log-likelihood nhân quả (Causal Language Modeling):
$$\mathcal{L}_{\text{CLM}} = \sum_{i=1}^T \log P(x_i \mid x_1, x_2, \dots, x_{i-1})$$
Để thực hiện điều này, các lớp Self-Attention trong GPT áp dụng ma trận Mask tam giác trên (Causal Masking), gán $-\infty$ cho tất cả các vị trí $j > i$ để ngăn mô hình ' nhìn trộm ' từ tương lai.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Khác với BERT (Encoder hai chiều), GPT là Decoder đơn hướng (chỉ nhìn từ quá khứ sang hiện tại để sinh từ tiếp theo).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Radford, A., et al. (2018). Improving Language Understanding by Generative Pre-Training. OpenAI. Xem **§4.2 Cơ chế Attention & Transformer**.

---

### Câu 66 [VOAI03-M66] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán NER (Named Entity Recognition), mục tiêu là:

- **A.** Phân tích cảm xúc tích cực hoặc tiêu cực của người dùng từ các bài viết đánh giá sản phẩm
- **B.** Dịch tự động một đoạn văn bản từ ngôn ngữ nguồn sang ngôn ngữ đích mà vẫn bảo toàn ngữ nghĩa
- **C.** Trích xuất và phân loại các thực thể có tên như người, địa điểm, tổ chức trong chuỗi văn bản
- **D.** Kiểm tra và sửa lỗi ngữ pháp, chính tả tự động trong các tài liệu văn bản hành chính dài

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Named Entity Recognition (NER) giống như việc đọc một bài báo và lấy bút highlight tô màu các tên riêng: tên người (Nguyễn Văn A), tên địa điểm (Hà Nội), tên tổ chức (Đại học Quốc gia), mốc thời gian (2026).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Bài toán NER thường được mô hình hóa dưới dạng gán nhãn chuỗi (Sequence Tagging) dùng quy ước BIO (Begin, Inside, Outside):
- `B-PER`: Bắt đầu tên người
- `I-PER`: Phần tiếp theo tên người
- `O`: Từ thông thường
Các mô hình tiêu chuẩn giải quyết NER gồm BiLSTM-CRF hoặc BERT fine-tuning với phân loại token.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
NER không phải là phân loại cảm xúc câu (Sentiment Analysis) hay tóm tắt văn bản, mà là trích xuất và phân loại các thực thể định danh có tên trong văn bản.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Lample, G., et al. (2016). Neural Architectures for Named Entity Recognition. NAACL 2016. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 67 [VOAI03-M67] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hệ thống RAG (Retrieval-Augmented Generation) giúp mô hình LLM:

- **A.** Chạy nhanh hơn 10 lần.
- **B.** Giảm hiện tượng " ảo giác "(hallucination) bằng cách tham chiếu dữ liệu bên ngoài.
- **C.** Không cần huấn luyện lại.
- **D.** Cả A và C đều đúng.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
RAG (Retrieval-Augmented Generation) giống như việc cho LLM làm bài thi có mở sách: Thay vì bắt mô hình phải ghi nhớ toàn bộ kiến thức vào bộ não (trọng số), khi người dùng hỏi, hệ thống sẽ chạy đi tìm các trang sách liên quan nhất trong thư viện rồi đưa cho LLM đọc và tổng hợp câu trả lời!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Quy trình 3 bước chuẩn của hệ thống RAG:
1. **Index & Retrieve:** Mã hóa tài liệu bằng embedding model (Vector Database). Khi có câu hỏi $q$, truy vấn $k$ đoạn văn có độ tương đồng cosine cao nhất: $D = \{d_1, \dots, d_k\}$.
2. **Augment:** Ghép nối câu hỏi và ngữ liệu thành prompt: $P = [\text{Context: } D; \text{ Question: } q]$.
3. **Generate:** Đưa prompt $P$ vào LLM sinh câu trả lời $y \sim P_{\text{LLM}}(y \mid P)$.
Ưu điểm: Giảm triệt để ảo giác (Hallucination) và cập nhật kiến thức mới theo thời gian thực mà không cần retrain mô hình.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
RAG không đòi hỏi phải fine-tune lại các trọng số của LLM mỗi khi có dữ liệu mới. Toàn bộ thông tin mới được nạp động thông qua bối cảnh ngữ cảnh (In-context learning).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS 2020. Xem **§4.3 Mô hình ngôn ngữ lớn (LLM)**.

---

### Câu 68 [VOAI03-M68] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán " Beam Search " trong giải mã (decoding) văn bản giúp:

- **A.** Loại bỏ hoàn toàn các từ ngữ bị lặp lại nhiều lần trong quá trình sinh văn bản tự hồi quy
- **B.** Giảm dung lượng bộ nhớ lưu trữ các trạng thái ẩn trung gian của mô hình trong pha suy luận
- **C.** Tìm kiếm chuỗi giải mã có xác suất tích lũy cao hơn bằng cách duy trì k ứng viên tốt nhất ở mỗi bước
- **D.** Tăng tốc độ suy luận mô hình lên mức tối đa bằng cách luôn chọn token có xác suất cao nhất tại mỗi bước

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Khi dịch câu, nếu dùng thuật toán tham lam (Greedy Search), ở mỗi bước bạn chỉ chọn từ có xác suất cao nhất hiện tại, dễ dẫn tới ngõ cụt sai lầm sau đó. Beam Search thông minh hơn: Nó giữ lại một nhóm gồm $k$ câu dịch tốt nhất (gọi là beam width) cùng lúc, rồi mới chọn câu có điểm tích lũy cao nhất cuối cùng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Thuật toán Beam Search với bề rộng chùm $B$:
Tại mỗi bước sinh $t$, với $B$ giả thuyết hiện tại, tính xác suất sinh từ tiếp theo cho toàn bộ từ điển $V$. Tính điểm log-probability tích lũy:
$$\text{Score}(y_1, \dots, y_t) = \sum_{i=1}^t \log P(y_i \mid y_{<i}, x)$$
Trong số $B \times |V|$ chuỗi ứng viên mở rộng, chỉ giữ lại đúng $B$ chuỗi có tổng điểm cao nhất để tiếp tục bước $t+1$.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Beam Search với $B=1$ chính là Greedy Search. Khi $B \to \infty$, Beam Search tiến tới tìm kiếm vét cạn (Exhaustive Search). $B$ thường chọn từ 3 đến 5 trong dịch máy.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sutskever, I., et al. (2014). Sequence to Sequence Learning with Neural Networks. NeurIPS 2014. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 69 [VOAI03-M69] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Một " Stopword " điển hình trong tiếng Việt là:

- **A.** " Và "
- **B.** " Trí tuệnhân tạo "
- **C.** " Học máy "
- **D.** " Máy tính "

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Stopwords (từ dừng) là những từ cực kỳ phổ biến trong ngôn ngữ (như ' và ', ' thì ', ' là ', ' của ', ' ở ') xuất hiện ở khắp mọi nơi nhưng lại mang rất ít ý nghĩa đặc trưng để phân biệt nội dung các văn bản.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Trong các mô hình phân loại văn bản truyền thống (BoW, TF-IDF), việc loại bỏ stopwords giúp:
1. Thu hẹp kích thước không gian từ điển $|V|$ đáng kể.
2. Giảm độ thưa thớt của ma trận dữ liệu và tăng tốc độ tính toán.
3. Ngăn các từ nối áp đảo tần suất của các từ khóa nội dung quan trọng.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Trong các mô hình Transformer hiện đại (như BERT, GPT), người ta thường KHÔNG loại bỏ stopwords vì các từ nối đóng vai trò then chốt trong cấu trúc ngữ pháp và hiểu mối quan hệ nhân quả.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Manning, C. D., et al. (2008). Introduction to Information Retrieval. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**.

---

### Câu 70 [VOAI03-M70] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong Attention, vector " Query " dùng đểlàm gì?

- **A.** Lưu trữ giá trị biểu diễn ngữ nghĩa nội dung thực tế của token được trích xuất từ các tầng trước
- **B.** Đóng vai trò là nhãn mục tiêu giám sát để tính toán hàm mất mát trong quá trình tiền huấn luyện
- **C.** Biểu diễn đầu ra phân loại cuối cùng của mô hình sau khi đã tổng hợp thông tin qua các khối chú ý
- **D.** Biểu diễn câu hỏi hoặc token hiện tại cần tìm kiếm thông tin tương quan từ các vector Key của từ khác

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Trong cơ chế Attention, hãy tưởng tượng bạn đi vào thư viện tìm sách:
- **Query (Q):** Câu hỏi hoặc chủ đề bạn đang muốn tìm kiếm.
- **Key (K):** Tên sách dán trên gáy ở các kệ để đối chiếu xem có khớp với câu hỏi của bạn không.
- **Value (V):** Nội dung thực tế bên trong cuốn sách mà bạn sẽ rút ra đọc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức Scaled Dot-Product Attention:
$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V$$
1. $Q K^T$ tính mức độ tương đồng giữa Query và từng Key.
2. Chia cho $\sqrt{d_k}$ để giữ phương sai ổn định, chống bão hòa gradient ở Softmax.
3. Softmax chuyển ma trận tương đồng thành các trọng số chú ý (tổng bằng 1).
4. Nhân với $V$ để lấy tổ hợp tuyến tính các vector giá trị.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Query là vector đi ' hỏi ', Key là vector ' đối chiếu ', và Value là vector ' chứa thông tin biểu diễn '. Đừng nhầm lẫn giữa vai trò của Query và Value.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Vaswani, A., et al. (2017). Attention Is All You Need. NeurIPS 2017. Xem **§4.2 Cơ chế Attention & Transformer**.

---

### Câu 71 [VOAI03-M71] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Phép toán " Max Pooling " có tác dụng:

- **A.** Tăng độ phân giải không gian của ảnh để hỗ trợ việc phân vùng chính xác các đường biên đối tượng
- **B.** Mở rộng số lượng kênh đặc trưng nhằm tăng cường khả năng nhận diện các họa tiết hoa văn phức tạp
- **C.** Giảm kích thước không gian, giảm chi phí tính toán và giữ lại đặc trưng kích hoạt mạnh nhất
- **D.** Chuẩn hóa không gian màu sắc của ảnh đầu vào về phân phối đều đối xứng qua trục tọa độ

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Max Pooling giống như việc thu nhỏ bức ảnh: Nó chia feature map thành các ô nhỏ (ví dụ $2 \times 2$) và chỉ chọn ra con số lớn nhất trong mỗi ô. Con số lớn nhất thể hiện đặc trưng mạnh nhất tại vùng đó, giúp giảm kích thước ảnh đi một nửa mà vẫn giữ nguyên thông tin cốt lõi.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Cho cửa sổ pooling kích thước $k \times k$ trượt với bước nhảy $s$ trên feature map $X$:
$$Y_{i, j} = \max_{0 \le m, n < k} X_{i \cdot s + m, j \cdot s + n}$$
Với kernel $2 \times 2, s=2$, chiều rộng và chiều cao giảm đi một nửa: $H_{\text{out}} = \lfloor H/2 \rfloor, W_{\text{out}} = \lfloor W/2 \rfloor$. Thao tác này không có tham số học (parameters = 0).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Max Pooling không học thêm tham số trọng số nào, và nó giúp tăng tính bất biến tịnh tiến cục bộ (local translation invariance).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 LeCun, Y., et al. (1998). Gradient-based learning applied to document recognition. IEEE. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**.

---

### Câu 72 [VOAI03-M72] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " IoU "(Intersection over Union) bằng 0.8 có nghĩa là:

- **A.** Mô hình dự đoán sai hoàn toàn.
- **B.** Có 80 đối tượng trong ảnh.
- **C.** Ảnh quá tối.
- **D.** Vùng dự đoán và thực tếtrùng khớp khá tốt.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Intersection over Union (IoU) đo độ trùng khớp giữa khung hình do AI vẽ và khung hình thật của con người: Bằng diện tích phần giao nhau chia cho diện tích phần hợp lại. Nếu $\text{IoU} = 0.8$ (tức $80\%$), hai khung gần như trùng khít lên nhau, chứng tỏ AI định vị cực kỳ chính xác!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức tính IoU giữa bounding box dự đoán $B_p$ và nhãn thật $B_g$:
$$\text{IoU}(B_p, B_g) = \frac{\text{Area}(B_p \cap B_g)}{\text{Area}(B_p \cup B_g)} = \frac{\text{Area}(B_p \cap B_g)}{\text{Area}(B_p) + \text{Area}(B_g) - \text{Area}(B_p \cap B_g)}$$
Trong chuẩn đánh giá Pascal VOC, ngưỡng chuẩn là $\text{IoU} \ge 0.5$. Trong MS COCO, ngưỡng tính từ $0.5$ đến $0.95$. Do đó $\text{IoU} = 0.8$ là độ chuẩn xác định vị rất cao.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
IoU nằm trong đoạn $[0, 1]$. $\text{IoU} = 0$ nghĩa là 2 khung không chạm nhau, $\text{IoU} = 1$ nghĩa là 2 khung hoàn toàn trùng khít.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Everingham, M., et al. (2010). The Pascal Visual Object Classes (VOC) Challenge. IJCV. Xem **§3.2 Định vị & Phát hiện đối tượng**.

---

### Câu 73 [VOAI03-M73] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán " YOLO " thuộc nhóm phát hiện đối tượng:

- **A.** Phân đoạn cá thể (Instance Segmentation).
- **B.** Single-stage detector.
- **C.** Unsupervised detector.
- **D.** Two-stage detector.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
YOLO viết tắt của ' You Only Look Once ' (Bạn chỉ cần nhìn một lần): Khác với các mô hình 2 giai đoạn (như Faster R-CNN phải đề xuất vùng trước rồi mới phân loại), YOLO coi việc phát hiện vật thể như một bài toán hồi quy duy nhất: Đưa ảnh qua mạng một lần duy nhất là ra ngay cả vị trí tọa độ lẫn tên đồ vật, đạt tốc độ real-time siêu nhanh!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Nguyên lý YOLO chia ảnh thành lưới $S \times S$. Mỗi ô lưới dự đoán đồng thời $B$ bounding boxes $(x, y, w, h, \text{confidence})$ và xác suất các lớp $C$:
$$\text{Tensor đầu ra} \in \mathbb{R}^{S \times S \times (B \times 5 + C)}$$
Toàn bộ quá trình tối ưu hóa bằng một hàm tổn thất đa nhiệm duy nhất (Multi-part Loss) gồm vị trí, kích thước, độ tin cậy và phân loại.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
YOLO thuộc họ 1-Stage Detector, ưu điểm số 1 là tốc độ cực nhanh (fps cao), phù hợp triển khai trên video thời gian thực hoặc thiết bị nhúng.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Redmon, J., et al. (2016). You Only Look Once: Unified, Real-Time Object Detection. CVPR 2016. Xem **§3.2 Định vị & Phát hiện đối tượng**.

---

### Câu 74 [VOAI03-M74] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong Object Detection, " Anchor boxes " dùng để:

- **A.** Làm khung tham chiếu kích thước và tỉ lệ cố định để dự đoán tọa độ và độ lệch của đối tượng
- **B.** Nén ảnh đầu vào xuống kích thước nhỏ hơn trước khi truyền qua các tầng tích chập của mạng
- **C.** Thay thế hoàn toàn các tầng tích chập trong backbone nhằm tăng tốc độ xử lý thời gian thực
- **D.** Lưu trữ nhãn phân loại của các đối tượng xuất hiện trong ảnh dưới dạng vector nhị phân thưa

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Anchor Boxes giống như việc người thợ may chuẩn bị sẵn các khung bìa mẫu với đủ kích cỡ (khung đứng cho người đi bộ, khung ngang cho xe hơi, khung vuông cho biển báo). Mạng AI không cần tự vẽ khung từ con số 0 mà chỉ cần học cách co giãn, tinh chỉnh các khung mẫu này để ôm khít đồ vật!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Các Anchor box $A = (w_a, h_a)$ đóng vai trò là khung tham chiếu ban đầu. Mạng nơ-ron học các độ lệch hồi quy (offsets):
$$t_x = \frac{x - x_a}{w_a}, \quad t_y = \frac{y - y_a}{h_a}, \quad t_w = \log\left(\frac{w}{w_a}\right), \quad t_h = \log\left(\frac{h}{h_a}\right)$$
Khi suy luận, tọa độ thực tế được giải mã bằng hàm mũ: $w = w_a e^{t_w}, h = h_a e^{t_h}$.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Anchor boxes được xác định trước (bằng thuật toán k-means clustering trên tập train hoặc cố định tỉ lệ), không phải là trọng số tự do được khởi tạo ngẫu nhiên.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Ren, S., et al. (2015). Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. NeurIPS 2015. Xem **§3.2 Định vị & Phát hiện đối tượng**.

---

### Câu 75 [VOAI03-M75] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " Semantic Segmentation " thực hiện việc gì?

- **A.** Chỉ phân loại toàn bộ ảnh.
- **B.** Phân biệt từng cá thểcủa cùng một lớp (ví dụ: người A, người B).
- **C.** Vẽ khung bao quanh đối tượng.
- **D.** Gán nhãn cho từng pixel của ảnh theo lớp đối tượng.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Semantic Segmentation (Phân đoạn ngữ nghĩa) giống như việc tô màu tranh theo mã số: Mỗi điểm ảnh (pixel) được gán đúng nhãn loại của nó (ví dụ tất cả các pixel thuộc về con chó được tô màu đỏ, cỏ tô màu xanh). Lưu ý rằng nếu có 2 con chó đứng cạnh nhau, chúng đều được tô chung màu đỏ mà không phân biệt con thứ nhất hay thứ hai!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Đầu ra của mô hình Semantic Segmentation là một bản đồ xác suất có kích thước bằng đúng ảnh gốc $Y \in \mathbb{R}^{H \times W \times C}$, trong đó tại mỗi tọa độ $(i, j)$:
$$\hat{y}_{i, j} = \arg\max_{c} P(\text{class} = c \mid X_{i, j})$$
Để phân biệt từng cá thể riêng biệt (con chó 1 vs con chó 2), người ta phải dùng Instance Segmentation (ví dụ Mask R-CNN).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Phân biệt rõ: Semantic Segmentation gán nhãn pixel-level nhưng KHÔNG phân biệt các cá thể (instances) riêng lẻ trong cùng một lớp.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Long, J., Shelhamer, E., & Darrell, T. (2015). Fully Convolutional Networks for Semantic Segmentation. CVPR 2015. Xem **§3.2 Định vị & Phát hiện đối tượng**.

---

### Câu 76 [VOAI03-M76] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc nào nổi tiếng cho bài toán Phân đoạn ảnh y tế?

- **A.** U-Net.
- **B.** AlexNet.
- **C.** VGG16.
- **D.** YOLOv8.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
U-Net có hình dáng chữ U đối xứng hoàn hảo: Nhánh bên trái co nhỏ ảnh lại để hiểu ngữ nghĩa tổng quát, nhánh bên phải phóng to ảnh trở lại kích thước gốc. Điều kỳ diệu là các đường ' cầu nối ' (Skip Connections) dẫn thẳng thông tin chi tiết từng góc cạnh từ nhánh trái sang nhánh phải, giúp đường biên phân đoạn sắc nét tuyệt đối!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Kiến trúc U-Net gồm:
1. **Contracting Path (Encoder):** Các lớp conv $3 \times 3$ kèm Max Pooling $2 \times 2$ trích xuất đặc trưng bậc cao và giảm độ phân giải.
2. **Expansive Path (Decoder):** Các lớp Transposed Conv (Up-conv) $2 \times 2$ khôi phục kích thước không gian.
3. **Skip Connections:** Ghép nối tensor (concatenation) từ tầng encoder sang decoder cùng mức độ phân giải, bảo toàn nguyên vẹn tọa độ không gian chính xác.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Trong U-Net, Skip Connection là phép nối kênh (Concatenation) dọc theo trục channel, khác với phép cộng phần tử (Addition) trong ResNet.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Ronneberger, O., Fischer, P., & Brox, T. (2015). U-Net: Convolutional Networks for Biomedical Image Segmentation. MICCAI 2015. Xem **§3.3 Kiến trúc CV SOTA**.

---

### Câu 77 [VOAI03-M77] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** " Invariance "(tính bất biến) trong CNN nghĩa là:

- **A.** Mô hình chỉ có khả năng xử lý các bức ảnh đầu vào là ảnh xám đơn sắc không có kênh màu RGB
- **B.** Trọng số của mô hình được đóng băng cố định và không bao giờ thay đổi trong suốt quá trình train
- **C.** Mô hình luôn luôn cho cùng một kết quả dự báo xác suất đồng nhất bất kể ảnh đầu vào là gì
- **D.** Khả năng nhận diện đối tượng ổn định ngay cả khi nó bị dịch chuyển vị trí, xoay nhẹ hoặc thay đổi tỉ lệ

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Tính bất biến tịnh tiến (Translation Invariance) nghĩa là: Dù con mèo nằm ở góc trên bên trái hay chạy xuống góc dưới bên phải bức ảnh, mạng CNN vẫn nhận diện ra đó là con mèo! Đó là nhờ bộ lọc tích chập quét qua mọi vị trí trên ảnh với cùng một bộ trọng số chia sẻ (Weight Sharing).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Hai tính chất không gian nền tảng của mạng CNN:
1. **Translation Equivariance (ở các tầng tích chập):** Nếu ảnh dịch chuyển $g(X)$, bản đồ đặc trưng cũng dịch chuyển tương ứng: $f(g(X)) = g(f(X))$.
2. **Translation Invariance (sau khi qua Pooling / GAP):** Đầu ra phân loại không đổi khi vật thể dịch chuyển nhẹ: $f(g(X)) = f(X)$.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
MLP cổ điển không có tính chất này vì mỗi pixel nối với một trọng số riêng biệt, dịch chuyển ảnh 1 pixel là vector đầu vào thay đổi hoàn toàn.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**.

---

### Câu 78 [VOAI03-M78] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Một ảnh xám kích thước 28 × 28 có bao nhiêu pixel?

- **A.** 2352
- **B.** 1000
- **C.** 784
- **D.** 56

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Một bức ảnh xám 2 chiều có kích thước 28 hàng và 28 cột pixel. Tổng số điểm ảnh đơn giản là phép nhân diện tích hình chữ nhật: 28 nhân với 28 bằng đúng 784 điểm ảnh!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Kích thước ảnh xám (Grayscale): $H = 28, W = 28, C = 1$.
Tổng số pixel:
$$N_{\text{pixels}} = H \times W \times C = 28 \times 28 \times 1 = 784$$
Nếu ảnh màu RGB ($C=3$), số giá trị điểm ảnh sẽ là $28 \times 28 \times 3 = 2,352$.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Đề bài nêu rõ là ảnh xám (grayscale) nên chỉ có 1 kênh màu duy nhất ($C=1$), không được nhân thêm 3 như ảnh màu RGB.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 LeCun, Y., et al. (1998). The MNIST Database of Handwritten Digits. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**.

---

### Câu 79 [VOAI03-M79] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán NMS (Non-Maximum Suppression) dùng để:

- **A.** Tính toán hàm mất mát phân loại và hồi quy tọa độ của các anchor boxes trong quá trình huấn luyện
- **B.** Loại bỏ các bounding box trùng lặp xung quanh cùng một đối tượng và giữ lại box có độ tin cậy cao nhất
- **C.** Tăng số lượng vùng đề xuất ứng viên bằng cách nội suy lưới tọa độ trong không gian đặc trưng
- **D.** Làm mịn hóa đường biên phân chia của đối tượng bằng bộ lọc trung bình Gaussian hai chiều

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Khi dò tìm một người, mô hình AI thường vẽ ra hàng chục khung bao chồng chéo lên nhau quanh người đó. Non-Maximum Suppression (NMS) đóng vai trò ' dọn dẹp ': Nó chọn ra khung có điểm tự tin cao nhất, rồi xóa bỏ tất cả các khung khác có độ trùng lặp (IoU) quá cao với khung này, chỉ để lại duy nhất 1 khung đẹp nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Thuật toán NMS chuẩn:
1. Sắp xếp danh sách các khung $B$ theo điểm tự tin (confidence score) giảm dần.
2. Chọn khung có điểm cao nhất $b_1$, đưa vào danh sách kết quả cuối cùng $D$ và xóa khỏi $B$.
3. Tính IoU giữa $b_1$ và tất cả các khung $b_i \in B$ còn lại.
4. Nếu $\text{IoU}(b_1, b_i) > \text{threshold}$ (thường chọn $0.45 - 0.6$), xóa $b_i$ khỏi $B$.
5. Lặp lại bước 2 đến khi danh sách $B$ trống.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
NMS là thuật toán hậu xử lý (Post-processing), không có đạo hàm huấn luyện trong các detector cổ điển, dùng để khử trùng lặp bounding box.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Neubeck, A., & Van Gool, L. (2006). Efficient Non-Maximum Suppression. ICPR 2006. Xem **§3.2 Định vị & Phát hiện đối tượng**.

---

### Câu 80 [VOAI03-M80] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** " Dilated Convolution "(Atrous convolution) giúp:

- **A.** Giảm độ phân giải không gian của bản đồ đặc trưng (Spatial Downsampling) để tiết kiệm bộ nhớ đệm
- **B.** Tăng tốc độ hội tụ của thuật toán tối ưu hóa (Faster Convergence) bằng cách giảm số lượng phép tính
- **C.** Mở rộng trường tiếp nhận (Receptive Field) của bộ lọc mà không làm tăng số tham số hay giảm độ phân giải
- **D.** Tự động biến đổi không gian màu sắc (Color Augmentation) nhằm chống chịu sự thay đổi chiếu sáng

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Dilated Convolution (tích chập giãn nở) giống như việc bạn kéo dãn chiếc kính lúp ra: Thay vì các điểm ảnh trong bộ lọc nằm dính sát nhau, nó tạo các khoảng trống giữa các điểm. Nhờ vậy, bộ lọc nhìn được một vùng ảnh rộng lớn hơn rất nhiều (Receptive Field to) mà không tốn thêm bất kỳ tham số hay phép nhân nào!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Với kernel kích thước $k \times k$ và tỷ lệ giãn nở (dilation rate) $d$:
Kích thước kernel hiệu dụng (effective kernel size) là:
$$k ' = k + (k - 1)(d - 1)$$
Ví dụ với kernel $3 \times 3$ và $d = 2$:
$$k ' = 3 + (3 - 1)(2 - 1) = 3 + 2 = 5$$
Trường tiếp nhận mở rộng từ $3 \times 3$ lên $5 \times 5$ nhưng số tham số vẫn giữ nguyên $3 \times 3 = 9$ trọng số.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Dilated convolution không thêm tham số nào vào kernel; nó chỉ chèn các lỗ trống (holes / spaces) giữa các trọng số của kernel.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Yu, F., & Koltun, V. (2015). Multi-Scale Context Aggregation by Dilated Convolutions. ICLR 2016. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**.

---

### Câu 81 [VOAI03-M81] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " Mean Average Precision "(mAP) là độ đo phổ biến cho bài toán:

- **A.** Phân loại ảnh toàn cục (Image Classification) xác định một nhãn duy nhất cho bức ảnh
- **B.** Phân cụm dữ liệu không giám sát (Unsupervised Clustering) gom nhóm các vector biểu diễn
- **C.** Phát hiện đối tượng (Object Detection) đánh giá đồng thời độ chính xác phân loại và định vị
- **D.** Hồi quy giá trị liên tục (Continuous Regression) dự báo các biến số thực từ dữ liệu bảng

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Trong bài toán phát hiện đồ vật, ta không thể dùng Accuracy đơn thuần. Thay vào đó, ta dùng mAP (mean Average Precision): Tính diện tích dưới đường cong đánh đổi giữa Precision (đoán trúng bao nhiêu) và Recall (bỏ sót bao nhiêu) cho từng loại đồ vật, rồi lấy trung bình cộng trên tất cả các lớp lại!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Quy trình tính mAP:
1. Với mỗi lớp $c$, tính đường cong Precision-Recall bằng cách quét qua các ngưỡng confidence score.
2. Tính Average Precision (AP) của lớp $c$ bằng tích phân hoặc nội suy 11 điểm:
$$\text{AP}_c = \int_0^1 p(r) \, dr$$
3. Lấy trung bình cộng trên toàn bộ $C$ lớp đối tượng:
$$\text{mAP} = \frac{1}{C} \sum_{c=1}^C \text{AP}_c$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
mAP kết hợp cả khả năng phân loại lẫn độ chính xác định vị bounding box ở các ngưỡng IoU khác nhau (như mAP@0.5 hay mAP@[0.5:0.95]).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Everingham, M., et al. (2010). The Pascal VOC Challenge. Xem **§3.2 Định vị & Phát hiện đối tượng**.

---

### Câu 82 [VOAI03-M82] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Đểtrích xuất các đặc trưng cạnh (edges), filter thường có đặc điểm:

- **A.** Toàn bộ các phần tử trong ma trận đều nhận giá trị bằng 0 tuyệt đối (Zero Kernel) để triệt tiêu nền
- **B.** Chứa các giá trị đạo hàm xấp xỉ biến thiên đột ngột qua các trục tọa độ (như Sobel filter)
- **C.** Khởi tạo bằng các giá trị ngẫu nhiên độc lập (Random Normal) tuân theo phân phối đều trên [-1, 1]
- **D.** Toàn bộ các phần tử trong kernel đều nhận giá trị bằng 1 (Box Blur) để thực hiện phép lọc trung bình

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Tại đường biên của một đồ vật (cạnh cái bàn, mép cánh cửa), màu sắc và độ sáng đột ngột thay đổi từ tối sang sáng hoặc ngược lại. Bộ lọc Sobel tính đạo hàm xấp xỉ theo phương ngang và phương dọc để bắt trọn những vị trí có độ biến thiên ánh sáng mạnh nhất này!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Toán tử Sobel sử dụng hai ma trận kernel $3 \times 3$ để tính xấp xỉ đạo hàm không gian:
$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix} * I, \quad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix} * I$$
Độ lớn gradient biên cạnh tổng hợp tại mỗi pixel:
$$G = \sqrt{G_x^2 + G_y^2}$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Toán tử Sobel là bộ lọc thủ công cổ điển (Handcrafted feature filter), giúp trực quan hóa cơ chế phát hiện biên cạnh mà các tầng đầu của CNN tự động học được.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sobel, I. (2014). An Isotropic 3x3 Image Gradient Operator. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**.

---

### Câu 83 [VOAI03-M83] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc " MobileNet " sử dụng loại tích chập nào đểtối ưu?

- **A.** 3D Convolution.
- **B.** Transposed Convolution.
- **C.** Deconvolution.
- **D.** Depthwise Separable Convolution.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Depthwise Separable Convolution là bí kíp giúp MobileNet chạy mượt mà trên điện thoại: Thay vì dùng một phép tích chập nặng nề vừa quét không gian vừa trộn kênh, nó tách làm 2 bước siêu nhẹ: Bước 1 lọc không gian từng kênh riêng lẻ (Depthwise), Bước 2 dùng kernel 1x1 để trộn các kênh lại (Pointwise)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
So sánh chi phí tính toán:
- **Tích chập thông thường:** $D_K \cdot D_K \cdot M \cdot N \cdot D_F \cdot D_F$
- **Depthwise Separable Conv:**
$$\text{Cost} = D_K \cdot D_K \cdot M \cdot D_F \cdot D_F + M \cdot N \cdot D_F \cdot D_F$$
Tỷ lệ tiết kiệm tính toán xấp xỉ:
$$\frac{\text{Depthwise Separable}}{\text{Standard Conv}} = \frac{1}{N} + \frac{1}{D_K^2}$$
Với kernel $3 \times 3$ ($D_K = 3$), lượng tính toán giảm từ 8 đến 9 lần mà độ chính xác gần như không suy giảm!

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Đây là nền tảng cốt lõi của họ kiến trúc MobileNet và Xception, giảm đột biến cả số tham số (parameters) lẫn số phép tính (FLOPs).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Howard, A. G., et al. (2017). MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. arXiv:1704.04861. Xem **§3.3 Kiến trúc CV SOTA**.

---

### Câu 84 [VOAI03-M84] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán nhận diện khuôn mặt, " Face Embedding " là:

- **A.** Vẽ khung chữ nhật bao quanh vị trí khuôn mặt xuất hiện trong khung hình để theo dõi chuyển động
- **B.** Gán nhãn danh tính của từng cá nhân vào cơ sở dữ liệu khuôn mặt phục vụ bài toán điểm danh
- **C.** Chuyển đổi ảnh khuôn mặt thành một vector số thực đặc trưng trong không gian nhúng có khoảng cách đo được
- **D.** Điều chỉnh độ sáng và cân bằng trắng tự động cho vùng khuôn mặt trước khi đưa vào bộ phân loại

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Face Embedding nén toàn bộ đặc điểm khuôn mặt của một người thành một dãy số (ví dụ vector 512 chiều). Khuôn mặt của cùng một người ở các góc chụp khác nhau sẽ có vector nằm rất gần nhau trong không gian, còn khuôn mặt của người khác sẽ bị đẩy ra xa tít tắp!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Kỹ thuật Metric Learning (ArcFace / CosFace / Triplet Loss) tối ưu hóa khoảng cách không gian embedding:
$$\mathcal{L}_{\text{triplet}} = \max\left(0, \|f(x_a) - f(x_p)\|_2^2 - \|f(x_a) - f(x_n)\|_2^2 + \alpha\right)$$
Trong đó:
- $x_a$: Ảnh neo (Anchor)
- $x_p$: Ảnh cùng người (Positive)
- $x_n$: Ảnh người khác (Negative)
- $\alpha$: Khoảng lề an toàn (margin).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Trong nhận diện khuôn mặt thực tế, ta không huấn luyện Softmax phân loại từng người vì số người dùng luôn biến động; ta so sánh khoảng cách Cosine giữa các vector nhúng (Face Embeddings).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Schroff, F., Kalenichenko, D., & Philbin, J. (2015). FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR 2015. Xem **§3.3 Kiến trúc CV SOTA**.

---

### Câu 85 [VOAI03-M85] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Tại sao hàm kích hoạt Softmax thường không dùng trong bài toán Multi-label Classification?

- **A.** Tốc độ tính toán của hàm Softmax quá chậm so với hàm kích hoạt ReLU trên phần cứng GPU
- **B.** Hàm Softmax chỉ có thể áp dụng được cho dữ liệu ảnh xám một kênh chứ không dùng được cho ảnh màu
- **C.** Đạo hàm bậc nhất của hàm Softmax luôn bị triệt tiêu về 0 khi có nhiều hơn 2 lớp phân loại
- **D.** Softmax ép tổng xác suất các lớp bằng 1 nên các lớp triệt tiêu lẫn nhau, không phù hợp cho đa nhãn độc lập

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Trong bài toán đa nhãn (Multi-label - ví dụ một bức ảnh có thể vừa có ' chó ', vừa có ' mèo ', vừa có ' cây cỏ '), các nhãn này độc lập với nhau. Nếu dùng Softmax, tổng các xác suất bị ép bằng 1 (chó tăng thì mèo giảm). Do đó bắt buộc phải dùng Sigmoid riêng cho từng lớp để mỗi lớp tự do nhận giá trị xác suất từ 0 đến 1!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
So sánh hàm kích hoạt ở lớp đầu ra:
- **Multi-class (Độc quyền nhãn, 1 ảnh chỉ thuộc đúng 1 lớp):** Dùng Softmax:
$$P(y = c \mid x) = \frac{e^{z_c}}{\sum_{j=1}^C e^{z_j}}, \quad \sum_{c=1}^C P(y=c \mid x) = 1$$
- **Multi-label (Đa nhãn đồng thời, có thể chứa nhiều lớp cùng lúc):** Dùng Sigmoid độc lập (Binary Cross-Entropy trên từng lớp):
$$P(y_c = 1 \mid x) = \sigma(z_c) = \frac{1}{1 + e^{-z_c}}$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Lỗi kinh điển trong các đề thi OLP: Nhầm lẫn giữa Multi-class (chọn 1 trong nhiều, dùng Softmax) và Multi-label (chọn nhiều trong nhiều, dùng độc lập Sigmoid).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**.

---

### Câu 86 [VOAI03-M86] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Khi mô hình có " High Bias ", ta nên làm gì?

- **A.** Tăng độphức tạp của mô hình (thêm lớp, thêm nơ-ron).
- **B.** Giảm số lượng dữ liệu.
- **C.** Thêm Regularization (L2, Dropout).
- **D.** Thu thập thêm dữ liệu (thường không hiệu quảbằng tăng phức tạp).

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
High Bias (độ chệch cao) chính là hiện tượng Underfitting (chưa học tới nơi tới chốn): Mô hình quá đơn giản (như dùng một đường thẳng để dự đoán một đám mây hình xoắn ốc), dẫn tới ngay cả trên tập luyện tập (Train set) nó cũng làm sai bét nhè!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Biểu hiện đặc trưng của High Bias (Underfitting):
1. Training Error cao và Validation Error cũng cao xấp xỉ nhau.
2. Tăng thêm dữ liệu huấn luyện hầu như không cải thiện được kết quả.
Biện pháp khắc phục chuẩn:
- Tăng độ phức tạp của mô hình (thêm tầng, thêm nơ-ron, tăng độ sâu cây).
- Tạo thêm đặc trưng mới (Feature Engineering, tương tác bậc cao).
- Giảm bớt ràng buộc điều quy (giảm hệ số $\lambda$ của L1/L2, giảm Dropout).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
High Bias = Underfitting (mô hình quá cứng nhắc, học kém cả train lẫn val). High Variance = Overfitting (học vẹt, train điểm cực cao nhưng val điểm rất thấp).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Hastie, T., et al. (2009). The Elements of Statistical Learning. Springer. Xem **§1.5 Đánh giá mô hình & Cross-Validation**.

---

### Câu 87 [VOAI03-M87] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Giá trị " Momentum " trong tối ưu hóa giúp:

- **A.** Tự động gán nhãn cho các mẫu dữ liệu chưa có nhãn thông qua thuật toán giả nhãn Pseudo-Labeling
- **B.** Tự động điều chỉnh thu nhỏ kích thước mini-batch khi mô hình tiếp cận gần điểm hội tụ tối ưu
- **C.** Cố định tốc độ học learning rate ở một giá trị hằng số siêu nhỏ trong suốt quá trình huấn luyện
- **D.** Tích lũy vận tốc gradient giúp vượt qua các điểm cực tiểu địa phương nông và vùng yên ngựa nhanh hơn

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
SGD có Momentum giống như một hòn bi sắt lăn xuống dốc: Khi lăn xuống, nó tích lũy vận tốc và quán tính. Nhờ quán tính này, nó lăn vù qua những ổ gà gập ghềnh nhỏ (điểm cực tiểu cục bộ) và không bị lắc lư qua lại ở hai bên sườn núi hẹp, tiến nhanh về đáy vực!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức cập nhật trọng số với Momentum:
$$v_t = \beta v_{t-1} + (1 - \beta) g_t$$
$$\theta_t = \theta_{t-1} - \eta v_t$$
Trong đó:
- $g_t = \nabla_\theta J(\theta)$ là gradient hiện tại.
- $v_t$ là vector vận tốc tích lũy trung bình động mũ (EMA).
- $\beta \in [0.9, 0.99]$ là hệ số quán tính (thường chọn $0.9$).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Momentum không làm tăng learning rate ngẫu nhiên; nó khử dao động ở các hướng có độ cong cao và tăng tốc chuyển động theo hướng dốc nhất quán.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Polyak, B. T. (1964). Some methods of speeding up the convergence of iteration methods. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**.

---

### Câu 88 [VOAI03-M88] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** " Grid Search " dùng để:

- **A.** Thử nghiệm vét cạn toàn bộ các tổ hợp siêu tham số được định nghĩa trước trong không gian lưới
- **B.** Lấy mẫu ngẫu nhiên không gian siêu tham số theo phân phối đều để giảm chi phí tính toán
- **C.** Sử dụng quá trình Gauss (Gaussian Process) để ước lượng hàm mục tiêu theo tối ưu hóa Bayes
- **D.** Điều chỉnh động siêu tham số tại mỗi epoch dựa trên gradient bậc hai của validation loss

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Grid Search giống như việc đi thử chìa khóa kiểu ' vét cạn ': Bạn lập ra một cái bảng gồm tất cả các khả năng kết hợp của các siêu tham số (ví dụ learning rate = 0.01, 0.001; batch size = 16, 32, 64) và huấn luyện thử từng ô một trên lưới để tìm ra bộ thông số cho điểm cao nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
So sánh các chiến lược Hyperparameter Tuning:
- **Grid Search:** Thử toàn bộ tích đề-các $\mathcal{P} = P_1 \times P_2 \times \dots \times P_k$. Chi phí tính toán bùng nổ theo cấp số nhân số chiều $\mathcal{O}(m^k)$.
- **Random Search:** Lấy mẫu ngẫu nhiên trên phân phối siêu tham số, hiệu quả hơn Grid Search trong không gian nhiều chiều.
- **Bayesian Optimization (Optuna, TPE):** Dựng mô hình xác suất học từ các lần thử trước để chọn điểm thử tiếp theo hứa hẹn nhất.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Grid Search duyệt qua lưới tọa độ xác định trước một cách vét cạn thủ công, rất tốn thời gian tính toán khi không gian tìm kiếm lớn.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Bergstra, J., & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. JMLR. Xem **§1.5 Đánh giá mô hình & Cross-Validation**.

---

### Câu 89 [VOAI03-M89] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Tại sao chúng ta cần chuẩn hóa (normalize) dữ liệu đầu vào?

- **A.** Tạo ra các biểu đồ trực quan hóa dữ liệu có tính thẩm mỹ cao hơn phục vụ báo cáo khoa học
- **B.** Ngăn chặn các lỗi tính toán số học do phép chia cho 0 xảy ra trong các tầng lan truyền thuận
- **C.** Nén dung lượng bộ nhớ lưu trữ của tệp dữ liệu trên ổ đĩa cứng trước khi tải vào bộ nhớ RAM
- **D.** Đưa các đặc trưng về cùng thang đo, giúp mặt mức hàm mất mát tròn đều và Gradient Descent hội tụ nhanh hơn

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Nếu dữ liệu có cột ' Tuổi ' (từ 0 đến 100) và cột ' Thu nhập ' (từ hàng triệu đến hàng trăm triệu), cột Thu nhập với những con số khổng lồ sẽ ' áp đảo ' hoàn toàn gradient, làm mô hình học méo mó. Chuẩn hóa dữ liệu đưa mọi cột về cùng một thang đo (như từ 0 đến 1) để chúng công bằng bình đẳng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Các phương pháp co giãn đặc trưng (Feature Scaling):
1. **Standardization (Z-score):** Đưa về phân phối trung bình 0, phương sai 1:
$$z = \frac{x - \mu}{\sigma}$$
2. **Min-Max Scaling:** Đưa về đoạn $[0, 1]$:
$$x ' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
Lợi ích cốt lõi: Làm đường đồng mức của hàm mất mát tròn đều hơn, giúp Gradient Descent hội tụ nhanh gấp nhiều lần và tránh tràn số.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Không được fit scaler trên tập Test/Validation; chỉ được `fit` trên tập Train rồi dùng các giá trị $\mu, \sigma$ đó để `transform` cho tập Test nhằm tránh rò rỉ dữ liệu (Data Leakage).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Hastie, T., et al. (2009). The Elements of Statistical Learning. Xem **§1.6 Điều quy L1/L2 & Biến dạng dữ liệu**.

---

### Câu 90 [VOAI03-M90] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong huấn luyện, " Mini-batch size " bằng 1 tương đương với:

- **A.** Pure Stochastic Gradient Descent.
- **B.** Adam.
- **C.** RMSProp.
- **D.** Batch Gradient Descent.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Stochastic Gradient Descent (SGD thuần túy) là phiên bản ' vội vàng ' nhất của tối ưu hóa: Cứ mỗi khi nhìn thấy đúng 1 mẫu dữ liệu duy nhất, nó tính ngay gradient và cập nhật trọng số luôn, không cần chờ đợi gom thành lô (batch)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Quy tắc cập nhật của Pure SGD (Batch size = 1) tại mẫu $(x^{(i)}, y^{(i)})$:
$$\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}(\theta; x^{(i)}, y^{(i)})$$
Đặc điểm: Cập nhật cực kỳ nhanh chóng nhưng gradient bị rung lắc rất mạnh (noisy) do từng mẫu đơn lẻ gây ra. Trong thực tế người ta dùng Mini-batch Gradient Descent (batch size $32, 64, 128$) để cân bằng giữa tính ổn định và khả năng tận dụng phần cứng GPU.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Thuật ngữ SGD trong PyTorch thường được dùng chung cho Mini-batch Gradient Descent, nhưng theo định nghĩa giải thuật lý thuyết gốc, Pure SGD sử dụng đúng $1$ mẫu dữ liệu duy nhất cho mỗi lần cập nhật trọng số.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Bottou, L. (2010). Large-scale machine learning with stochastic gradient descent. COMPSTAT 2010. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**.

---

### Câu 91 [VOAI03-M91] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** " Overfitting " có thểđược nhận biết khi:

- **A.** Độ chính xác trên tập Train rất cao nhưng độ chính xác trên tập Validation lại rất thấp
- **B.** Mô hình hội tụ quá nhanh chỉ sau 1 epoch đầu tiên mà hàm mất mát đã chạm ngưỡng 0
- **C.** Độ chính xác trên cả tập Train và tập Validation đều thấp xấp xỉ mức đoán ngẫu nhiên
- **D.** Độ chính xác trên cả hai tập Train và Validation đều cao tương đương nhau và tăng ổn định

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Khi bạn làm bài ôn tập ở nhà được 10 điểm tuyệt đối, nhưng khi đi thi gặp đề mới thì chỉ được 3 điểm. Điều đó chứng tỏ bạn đã học vẹt (Overfitting): Mô hình ghi nhớ y nguyên tập dữ liệu luyện tập (Train) nhưng không hề có khả năng khái quát hóa trên dữ liệu thực tế (Validation/Test)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Dấu hiệu chẩn đoán Overfitting trên đồ thị hàm mất mát theo Epoch:
1. $\mathcal{L}_{\text{train}}$ tiếp tục giảm đều đặn tiến sát 0, $\text{Acc}_{\text{train}} \to 100\%$.
2. $\mathcal{L}_{\text{val}}$ sau khi giảm tới một ngưỡng bắt đầu bật tăng trở lại, $\text{Acc}_{\text{val}}$ suy giảm hoặc chững lại.
Biện pháp đặc trị:
- Áp dụng Early Stopping (dừng huấn luyện khi val loss bắt đầu tăng).
- Thêm điều quy L2 (Weight Decay) hoặc Dropout.
- Tăng cường dữ liệu (Data Augmentation).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Sự chênh lệch lớn giữa độ chính xác Train (rất cao) và Val (rất thấp) là chỉ dấu không thể nhầm lẫn của Overfitting (High Variance).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§1.5 Đánh giá mô hình & Cross-Validation**.

---

### Câu 92 [VOAI03-M92] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật " Label Smoothing " giúp:

- **A.** Tăng tốc độ đọc ghi dữ liệu (I/O Speedup) từ ổ đĩa cứng vào bộ nhớ đệm VRAM trong quá trình train
- **B.** Làm mịn hóa các đường biên phân loại (Boundary Smoothing) bằng cách áp dụng bộ lọc thông thấp Gauss
- **C.** Tự động phát hiện và loại bỏ các mẫu dữ liệu bị gán nhãn sai lệch (Noise Filtering) trong tập huấn luyện
- **D.** Phạt việc mô hình quá tự tin vào nhãn One-hot (Overconfidence Penalty), giúp tăng khả năng tổng quát

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Khi huấn luyện mô hình phân loại, ta thường ép xác suất của nhãn đúng phải là 1.0 (100%), khiến mô hình trở nên quá tự tin và kiêu ngạo. Kỹ thuật Label Smoothing hạ nhãn đúng xuống một chút (ví dụ 0.9) và chia đều 0.1 còn lại cho các lớp khác, giúp mô hình khiêm tốn hơn và chống Overfitting!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức biến đổi phân phối nhãn với hệ số làm mịn $\epsilon$ trên $K$ lớp:
$$q_i = (1 - \epsilon) y_i + \frac{\epsilon}{K}$$
Với nhãn đúng ($y_i = 1$):
$$q_{\text{target}} = 1 - \epsilon + \frac{\epsilon}{K}$$
Với các nhãn sai ($y_i = 0$):
$$q_{\text{other}} = \frac{\epsilon}{K}$$
Ví dụ với $K = 10, \epsilon = 0.1$: nhãn đúng chuyển từ $1.0$ thành $0.91$, các lớp khác nhận $0.01$. Điều này ngăn chặn logit $z_c \to \infty$, giúp gradient ổn định.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Label Smoothing là kỹ thuật điều quy (Regularization) cho hàm loss, không làm thay đổi nhãn gốc của dữ liệu mà chỉ làm mềm phân phối đích (soft targets).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Szegedy, C., et al. (2016). Rethinking the Inception Architecture for Computer Vision. CVPR 2016. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**.

---

### Câu 93 [VOAI03-M93] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Một " Learning Rate " quá lớn sẽdẫn đến:

- **A.** Thời gian huấn luyện tăng lên.
- **B.** Không ảnh hưởng gì.
- **C.** Hàm loss dao động mạnh và có thểkhông hội tụ.
- **D.** Mô hình học rất kỹ.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Tốc độ học (Learning Rate) giống như bước chân khi bạn đi xuống đáy thung lũng trong sương mù: Nếu bước chân vừa phải, bạn sẽ từ từ chạm đáy an toàn. Nhưng nếu bước chân quá khổng lồ (learning rate quá lớn), một bước nhảy sẽ đưa bạn văng tít sang ngọn núi đối diện, thậm chí bay thẳng ra khỏi thung lũng (phân kỳ, loss biến thành NaN)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Xét bài toán tối ưu bậc hai $f(x) = \frac{1}{2} a x^2$ với $a > 0$.
Bước cập nhật: $x_{t+1} = x_t - \eta (a x_t) = (1 - \eta a) x_t$.
Điều kiện hội tụ là $|1 - \eta a| < 1 \iff 0 < \eta < \frac{2}{a}$.
Nếu chọn $\eta > \frac{2}{a}$, dãy số $|x_t| \to \infty$ bùng nổ theo cấp số nhân, hàm mất mát phân kỳ (Divergence) và xuất hiện lỗi tràn số `NaN` / `Inf`.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Learning rate quá nhỏ làm hội tụ chậm; còn learning rate quá lớn KHÔNG BAO GIỜ giúp hội tụ nhanh hơn mà sẽ gây rung lắc dữ dội hoặc phân kỳ hoàn toàn.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**.

---

### Câu 94 [VOAI03-M94] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Tác dụng của " Cross-validation "(kiểm chéo) là:

- **A.** Thay thế hoàn toàn tập dữ liệu huấn luyện bằng một tập dữ liệu giả lập được sinh bởi mô hình AI
- **B.** Đánh giá mô hình khách quan trên nhiều phân vùng dữ liệu khác nhau để giảm thiểu sai số do cách chia tập
- **C.** Lưu trữ định kỳ các checkpoint trọng số có độ chính xác cao nhất trên tập kiểm thử độc lập
- **D.** Tăng số lượng tham số học được của mô hình bằng cách xếp chồng nhiều tầng nơ-ron liên tiếp

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Kiểm tra chéo K-Fold giống như việc chia lớp thành 5 nhóm học tập: Lần 1 nhóm 1 thi còn 4 nhóm kia làm bài ôn; lần 2 nhóm 2 thi; lần 3 nhóm 3 thi... Cứ như vậy, mọi học sinh đều có cơ hội vừa học vừa được kiểm tra công bằng, giúp điểm số đánh giá không bị may rủi!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Quy trình $K$-Fold Cross-Validation:
1. Chia ngẫu nhiên tập dữ liệu $D$ thành $K$ phần con bằng nhau $F_1, F_2, \dots, F_K$.
2. Lặp qua $i = 1, \dots, K$:
   - Tập kiểm tra: $V_i = F_i$
   - Tập huấn luyện: $T_i = D \setminus F_i$
   - Huấn luyện mô hình trên $T_i$ và đánh giá điểm $S_i$ trên $V_i$.
3. Điểm đánh giá trung bình không thiên kiến:
$$\bar{S} = \frac{1}{K} \sum_{i=1}^K S_i$$

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Với bài toán dữ liệu chuỗi thời gian (Time-series), tuyệt đối không dùng K-Fold thông thường vì sẽ làm rò rỉ tương lai dự báo quá khứ (phải dùng TimeSeriesSplit).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Kohavi, R. (1995). A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection. IJCAI. Xem **§1.5 Đánh giá mô hình & Cross-Validation**.

---

### Câu 95 [VOAI03-M95] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** " Hardware Acceleration " cho AI thường nhắc đến thiết bị nào?

- **A.** Chuột và bàn phím.
- **B.** Ổcứng HDD.
- **C.** GPU hoặc TPU.
- **D.** Màn hình 4K.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
CPU giống như một vài vị giáo sư thông thái giải được các bài toán phức tạp tuần tự, còn GPU giống như hàng ngàn học sinh tiểu học cùng làm phép nhân ma trận đơn giản cùng một lúc. Do Deep Learning cốt lõi là hàng triệu phép nhân cộng ma trận, GPU và TPU chạy song song nhanh gấp hàng trăm lần CPU!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Bản chất tính toán mạng nơ-ron là các phép toán đại số tuyến tính cơ bản (BLAS):
$$Y = W X + b$$
GPU chứa hàng nghìn nhân CUDA (CUDA Cores) và nhân Tensor (Tensor Cores) được thiết kế tối ưu hóa cho phép tính nhân-cộng ma trận tích lũy song song (GEMM - General Matrix Multiply) với băng thông bộ nhớ (Memory Bandwidth) hàng trăm GB/s đến TB/s.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
GPU không tăng tốc cho các thuật toán đệ quy hoặc xử lý rẽ nhánh điều kiện logic phức tạp tuần tự (vốn là thế mạnh của CPU), mà chuyên trị tính toán ma trận song song ồ ạt.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Kirk, D. B., & Hwu, W. W. (2016). Programming Massively Parallel Processors. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**.

---

### Câu 96 [VOAI03-M96] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " Model Quantization "(Lượng hóa mô hình) giúp:

- **A.** Chuyển đổi toàn bộ mã nguồn sang ngôn ngữ C++ (Code Porting) để triển khai trên các hệ thống nhúng
- **B.** Mở rộng kích thước các tầng ẩn (Layer Widening) bằng cách tăng gấp đôi số lượng nơ-ron trong các lớp
- **C.** Tăng cường độ chính xác phân loại của mô hình (Fine-tuning) bằng cách tinh chỉnh với learning rate nhỏ
- **D.** Chuyển đổi trọng số sang dạng số nguyên có số bit thấp (INT8/FP8) để giảm dung lượng và tăng tốc suy luận

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Lượng tử hóa (Quantization) giống như việc đổi từ dùng thước đo milimet chi tiết sang dùng thước đo centimet tròn số: Bình thường mỗi trọng số được lưu bằng số thực 32-bit (FP32). Nếu chuyển sang số nguyên 8-bit (INT8), mô hình sẽ nhẹ đi đúng 4 lần, tốn ít RAM hơn và chạy vèo vèo trên máy tính yếu!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Công thức lượng tử hóa tuyến tính từ số thực $x \in [a, b]$ sang số nguyên $q \in [0, 255]$ (INT8):
$$q = \text{round}\left(\frac{x}{S}\right) + Z$$
Trong đó:
- $S = \frac{b - a}{255}$ là hệ số tỉ lệ (Scale factor).
- $Z$ là điểm không (Zero point).
Lợi ích: Giảm dung lượng bộ nhớ từ 4 byte (FP32) xuống 1 byte (INT8) cho mỗi tham số, tiết kiệm $75\%$ dung lượng và tận dụng các tập lệnh SIMD INT8 tăng tốc tính toán.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Quantization làm mô hình nhẹ đi và chạy nhanh hơn, nhưng nếu lượng tử hóa quá sâu (như 4-bit, 2-bit) mà không có kỹ thuật chuẩn (như QLoRA, AWQ) có thể làm sụt giảm nhẹ độ chính xác.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Gholami, A., et al. (2022). A Survey of Quantization Methods for Efficient Neural Network Inference. Proceedings of the IEEE. Xem **§7.1 Kỹ thuật thi đấu & SOTA**.

---

### Câu 97 [VOAI03-M97] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** " A/B Testing " trong triển khai AI là:

- **A.** Phân chia tập dữ liệu huấn luyện thành hai nửa bằng nhau tương ứng với nhóm lớp A và nhóm lớp B
- **B.** Huấn luyện đồng thời mô hình trên hai máy chủ phần cứng khác nhau để so sánh thời gian hội tụ
- **C.** Thử nghiệm song song hai phiên bản mô hình trên các nhóm người dùng thực tế để so sánh định lượng hiệu quả
- **D.** Kiểm tra lỗi cú pháp và tính tương thích của mã nguồn trước khi đóng gói thành container Docker

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
A/B Testing giống như việc chia đôi khách vào quán: Một nửa khách hàng được phục vụ bằng thực đơn cũ (phiên bản A), một nửa được phục vụ bằng thực đơn mới (phiên bản B). Sau vài tuần, người chủ quán so sánh doanh thu thực tế giữa hai nhóm để quyết định có nên đổi toàn bộ sang thực đơn mới hay không!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Phương pháp A/B Testing trong triển khai hệ thống AI:
1. Phân luồng lưu lượng người dùng ngẫu nhiên: $50\%$ truy cập Model A (baseline hiện tại), $50\%$ truy cập Model B (mô hình mới thử nghiệm).
2. Thu thập các chỉ số nghiệp vụ thực tế (Business Metrics: tỷ lệ click CTR, thời gian lưu trang, doanh thu chuyển đổi).
3. Kiểm định giả thuyết thống kê (t-test hoặc Z-test) để xác nhận sự cải thiện có ý nghĩa thống kê ($p < 0.05$) hay chỉ là ngẫu nhiên.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
A/B testing đo lường tác động thực tế trên người dùng thật (online evaluation), trong khi F1-score hay Accuracy trên tập test chỉ là đánh giá ngoại tuyến (offline evaluation).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Kohavi, R., et al. (2020). Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing. Cambridge University Press. Xem **§1.5 Đánh giá mô hình & Cross-Validation**.

---

### Câu 98 [VOAI03-M98] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Khái niệm " Data Drift "(Trôi dạt dữ liệu) nghĩa là:

- **A.** Dữ liệu bị xóa mất khỏi cơ sở dữ liệu do sự cố phần cứng máy chủ lưu trữ trong quá trình vận hành
- **B.** Dữ liệu bị sao chép trùng lặp nhiều lần khiến kích thước tập kiểm thử bị thổi phồng nhân tạo
- **C.** Tốc độ truyền tải dữ liệu qua hệ thống mạng bị nghẽn cổ chai làm tăng độ trễ suy luận của API
- **D.** Sự thay đổi phân phối xác suất của dữ liệu thực tế theo thời gian khiến mô hình cũ suy giảm hiệu năng

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Data Drift (dữ liệu bị trôi) giống như việc một mô hình học nhận biết thời trang năm 2010 mang đi dự đoán cho giới trẻ năm 2026: Phong cách ăn mặc và thị hiếu của con người đã thay đổi hoàn toàn theo thời gian. Mẫu dữ liệu đầu vào trong thực tế không còn giống với những gì mô hình đã từng được học trong quá khứ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Phân biệt hai loại hiện tượng trôi dạt trong hệ thống AI production:
1. **Data Drift (Covariate Shift):** Phân phối đầu vào thay đổi $P_{\text{test}}(X) \ne P_{\text{train}}(X)$ nhưng mối quan hệ $P(Y \mid X)$ không đổi (vd: người dùng đổi sang dùng điện thoại mới chụp ảnh nét hơn).
2. **Concept Drift:** Mối quan hệ giữa đặc trưng và nhãn thay đổi $P_{\text{test}}(Y \mid X) \ne P_{\text{train}}(Y \mid X)$ (vd: sau đại dịch Covid, thói quen chi tiêu thay đổi khiến mô hình dự báo tài chính cũ bị sai hoàn toàn).
Phương pháp phát hiện: Dùng kiểm định Kolmogorov-Smirnov (KS-test) hoặc độ phân kỳ Population Stability Index (PSI).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Mô hình dù đạt độ chính xác 99% khi nghiệm thu vẫn sẽ dần bị thoái hóa hiệu năng trong thực tế (Model Decay) nếu không có hệ thống giám sát Data Drift liên tục.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Gama, J., et al. (2014). A survey on concept drift adaptation. ACM Computing Surveys. Xem **§1.5 Đánh giá mô hình & Cross-Validation**.

---

### Câu 99 [VOAI03-M99] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** " MLOps " là viết tắt của:

- **A.** Machine Learning Operations.
- **B.** Mobile Learning Options.
- **C.** Multi-Layer Optimization.
- **D.** Main Logic Operator.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
MLOps là sự kết hợp giữa Machine Learning (Học máy) và DevOps (Vận hành phần mềm): Nó là toàn bộ quy trình tự động hóa từ thu thập dữ liệu, huấn luyện, kiểm thử, đóng gói mô hình cho đến đưa lên máy chủ phục vụ người dùng và giám sát lỗi 24/7 một cách bền bỉ và chuyên nghiệp.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Vòng đời chuẩn của hệ thống MLOps:
1. **Data Engineering:** Ingestion, Validation, Feature Store.
2. **Model Engineering:** Distributed Training, Hyperparameter Tuning, Experiment Tracking (MLflow, W&B).
3. **Deployment & CI/CD:** Model Registry, Containerization (Docker), Model Serving (Triton, TorchServe).
4. **Operations:** Monitoring latency, throughput, Data Drift & Automated Retraining.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
MLOps không chỉ là việc gọi hàm `model.fit()` và `model.predict()`, mà là quản lý toàn diện vòng đời của mã nguồn, dữ liệu và mô hình trong môi trường sản xuất thực tế.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Kreuzberger, D., et al. (2023). Machine learning operations (mlops): Overview, definition, and architecture. IEEE Access. Xem **§7.1 Kỹ thuật thi đấu & SOTA**.

---

### Câu 100 [VOAI03-M100] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Đểphục vụ (serving) một mô hình LLM lớn, kỹ thuật nào thường được dùng đểtiết kiệm VRAM?

- **A.** Unzipping.
- **B.** Paging.
- **C.** KV Caching.
- **D.** Overclocking.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Khi sinh từng từ tiếp theo trong mô hình ngôn ngữ lớn (LLM), để sinh ra từ thứ 100, mô hình cần tính lại Attention với 99 từ trước. Kỹ thuật KV Caching lưu tạm các vector Key và Value của 99 từ trước vào bộ nhớ VRAM, giúp mô hình chỉ cần tính vector cho đúng 1 từ mới nhất, tăng tốc độ trả lời lên gấp hàng chục lần!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
Trong quá trình sinh tự hồi quy (Autoregressive Generation):
Tại bước giải mã $t$, để tính toán Attention cho token mới $x_t$:
- Thay vì tính lại toàn bộ ma trận $K_{1:t} = X_{1:t} W_K$ và $V_{1:t} = X_{1:t} W_V$ tốn chi phí $\mathcal{O}(t^2)$,
- KV Caching lưu trữ sẵn tensor $K_{1:t-1}$ và $V_{1:t-1}$ trong bộ nhớ đệm GPU VRAM.
- Tại bước $t$, chỉ cần tính $k_t = x_t W_K, v_t = x_t W_V$ và ghép nối (concatenate):
$$K_{1:t} = [K_{1:t-1}; k_t], \quad V_{1:t} = [V_{1:t-1}; v_t]$$
Chi phí tính toán giảm từ $\mathcal{O}(T^2)$ xuống $\mathcal{O}(T)$ trên mỗi token sinh ra.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
KV Caching tiêu tốn một lượng VRAM rất lớn (tỉ lệ thuận với độ dài chuỗi $T$, kích thước batch $B$ và số lớp), dẫn tới sự ra đời của các kỹ thuật tối ưu như PagedAttention (vLLM) và FlashAttention.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Dao, T., et al. (2022). FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. NeurIPS 2022. Xem **§4.3 Mô hình ngôn ngữ lớn (LLM)**.

---
