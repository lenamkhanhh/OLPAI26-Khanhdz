# 01 — Cẩm nang Lý thuyết Toàn diện OLP AI HCMUS 2026 (Full LaTeX KaTeX)

> **Mục tiêu:** Cung cấp nền tảng toán học và kỹ thuật chuyên sâu cho vòng loại cấp trường Olympic AI HCMUS 2026 và Olympic Trí tuệ Nhân tạo Việt Nam (VOAI / IOAI).
> **Phạm vi:** 
> - §1. Machine Learning cổ điển
> - §2. Deep Learning cơ bản & PyTorch Framework
> - §3. Thị giác máy tính (Computer Vision)
> - §4. Xử lý ngôn ngữ tự nhiên (NLP)
> - §5. Xác suất & Thống kê cho AI
> - §6. Bảng 24 bẫy đề thi hay gặp (Lỗi hay mắc: SAI $\to$ ĐÚNG)
> - §7. Chuyên đề Tác vụ thực chiến OLP AI 2025 & 2026 (Khung giải pháp 5 bước)
>
> *Quy ước:* Mọi công thức toán học được chuẩn hóa KaTeX ($...$ cho inline và $$...$$ cho display block). Các câu hỏi trong đề luyện và đáp án trích dẫn trực tiếp theo mã mục (§x.y).

---

## §1. Machine Learning Cổ Điển

### §1.1 k-NN (k-Nearest Neighbors — Lazy Learner)
- **Định nghĩa:** Thuật toán phân loại/hồi quy phi tham số (non-parametric), thuộc nhóm **Lazy Learner** (người học lười). Thuật toán **không có pha huấn luyện tham số** (không học trọng số $w, b$), chỉ lưu toàn bộ tập huấn luyện vào bộ nhớ. Khi có điểm dữ liệu mới $x_q$, thuật toán mới tính khoảng cách đến tất cả các điểm trong tập dữ liệu, chọn ra $k$ điểm láng giềng gần nhất để vote đa số (Classification) hoặc lấy trung bình (Regression).
- **Hàm khoảng cách (Minkowski Metric):**
  $$D(x, y) = \left( \sum_{i=1}^d |x_i - y_i|^p \right)^{1/p}$$
  - $p = 1$: Khoảng cách Manhattan (L1 Norm): $D_1(x, y) = \sum_{i=1}^d |x_i - y_i|$
  - $p = 2$: Khoảng cách Euclid (L2 Norm): $D_2(x, y) = \sqrt{\sum_{i=1}^d (x_i - y_i)^2}$
- **Bầu chọn có trọng số (Distance-Weighted Voting):**
  $$w_i = \frac{1}{D(x_q, x_i) + \epsilon} \implies \hat{y} = \arg\max_c \sum_{i \in \mathcal{N}_k, y_i = c} w_i$$
- **Ảnh hưởng của siêu tham số $k$:**
  - $k$ nhỏ ($k=1$): Ranh giới phân chia rất phức tạp, nhạy cảm với nhiễu $\implies$ **Overfitting** (High Variance).
  - $k$ lớn ($k \to N$): Ranh giới phân chia phẳng mượt, dự đoán theo lớp đa số $\implies$ **Underfitting** (High Bias).
- **⭐ Hay ra thi:**
  1. k-NN **không có training phase** (độ phức tạp huấn luyện là $\mathcal{O}(1)$, độ phức tạp suy luận là $\mathcal{O}(N \cdot d)$).
  2. Bắt buộc phải **chuẩn hóa đặc trưng (Feature Scaling)** (MinMaxScaler hoặc StandardScaler) trước khi áp dụng k-NN vì khoảng cách Euclid bị chi phối bởi các chiều có biên độ lớn.
  3. Bị ảnh hưởng nặng nề bởi **Lời nguyền chiều dữ liệu (Curse of Dimensionality)** khi số chiều $d$ tăng cao.

---

### §1.2 Support Vector Machines (SVM & Kernel Trick)
- **Định nghĩa:** Tìm một siêu phẳng (hyperplane) phân tách hai lớp sao cho **Khoảng cách lề (Margin)** giữa siêu phẳng và các điểm dữ liệu gần nhất (gọi là **Support Vectors**) đạt giá trị cực đại.
- **Phương trình siêu phẳng:** $\mathbf{w}^T \mathbf{x} + b = 0$.
  - Khoảng cách hình học từ điểm $\mathbf{x}$ đến siêu phẳng: $\gamma = \frac{|\mathbf{w}^T \mathbf{x} + b|}{\|\mathbf{w}\|_2}$.
  - Độ rộng Margin hình học giữa 2 lớp:
    $$\text{Margin} = \frac{2}{\|\mathbf{w}\|_2}$$
- **Bài toán tối ưu Soft-Margin (Primal Formulation):**
  Cho phép một số điểm vi phạm lề qua biến bù $\xi_i \ge 0$:
  $$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2} \|\mathbf{w}\|_2^2 + C \sum_{i=1}^N \xi_i \quad \text{s.t.} \quad y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$
  - Siêu tham số $C$:
    - $C$ lớn: Phạt lỗi vi phạm rất nặng $\implies$ Margin hẹp, ít chấp nhận lỗi $\implies$ Dễ **Overfitting**.
    - $C$ nhỏ: Chấp nhận nhiều điểm vi phạm lề hơn $\implies$ Margin rộng $\implies$ Dễ **Underfitting**.
- **Kernel Trick (Chiếu phi tuyến):**
  Thay vì chiếu trực tiếp $\Phi(\mathbf{x})$, SVM dùng hàm nhân $K(\mathbf{x}, \mathbf{z}) = \langle \Phi(\mathbf{x}), \Phi(\mathbf{z}) \rangle$:
  - **RBF (Radial Basis Function / Gaussian) Kernel:**
    $$K(\mathbf{x}, \mathbf{z}) = \exp\left( -\gamma \|\mathbf{x} - \mathbf{z}\|_2^2 \right) \quad (\gamma > 0)$$
  - Vai trò của $\gamma$: $\gamma = \frac{1}{2\sigma^2}$.
    - $\gamma$ lớn: Bán kính ảnh hưởng hẹp, biên quyết định uốn lượn ôm sát từng điểm dữ liệu $\implies$ **Overfitting**.
    - $\gamma$ nhỏ: Bán kính ảnh hưởng rộng, biên quyết định phẳng mượt $\implies$ **Underfitting**.
- **⭐ Hay ra thi:**
  1. Độ rộng margin tỉ lệ nghịch với $\|\mathbf{w}\|$ ($\text{Margin} = \frac{2}{\|\mathbf{w}\|}$).
  2. Các điểm quyết định vị trí siêu phẳng chỉ là **Support Vectors**; dịch chuyển các điểm khác ngoài lề không làm đổi siêu phẳng.
  3. Cả $C$ lớn và $\gamma$ lớn đều làm mô hình có xu hướng **Overfitting**.

---

### §1.3 Cây quyết định (Decision Tree), Entropy & Information Gain
- **Định nghĩa:** Mô hình phân cấp dạng cây (Tree). Tại mỗi nút nội bộ (Internal Node), một đặc trưng được chọn để phân nhánh sao cho độ hỗn loạn (tạp chất - Impurity) của các nút con là thấp nhất.
- **Độ đo hỗn loạn:**
  - **Entropy (Shannon Entropy):**
    $$H(S) = -\sum_{i=1}^C p_i \log_2(p_i)$$
    Trong đó $p_i$ là tỉ lệ mẫu thuộc lớp $i$ trong tập $S$. Quy ước: nếu $p_i = 0$ thì $0 \log_2(0) = 0$.
    - Đơn vị: **bit** (vì dùng $\log$ cơ số 2).
    - Node thuần khiết (100% cùng 1 nhãn): $H(S) = 0$.
    - Node cân bằng đồng đều nhất: $H(S)$ đạt cực đại $= \log_2(C)$.
  - **Gini Impurity (Dùng trong thuật toán CART):**
    $$Gini(S) = 1 - \sum_{i=1}^C p_i^2$$
- **Độ lợi thông tin (Information Gain — ID3):**
  $$IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
  Tiêu chuẩn chọn nhánh: Chọn đặc trưng $A$ có **$IG(S, A)$ lớn nhất**.
- **⭐ Hay ra thi:**
  1. Công thức Entropy trong lý thuyết thông tin dùng **$\log_2$** (đơn vị bit).
  2. Information Gain thiên vị các thuộc tính có quá nhiều giá trị riêng biệt (như ID); thuật toán C4.5 khắc phục bằng **Gain Ratio**: $GR(S, A) = \frac{IG(S, A)}{SplitInfo(S, A)}$.
  3. Một cây quyết định phát triển không kiểm soát có thể nhớ toàn bộ tập huấn luyện $\implies$ Huấn luyện đạt 100% Accuracy nhưng bị Overfit nặng $\implies$ Phải cắt tỉa (Pruning: Pre-pruning hoặc Post-pruning).

---

### §1.4 Random Forest & Phương pháp Ensemble
- **Định nghĩa:** Thuật toán Bagging (Bootstrap Aggregating) kết hợp nhiều cây quyết định độc lập để giảm phương sai (Variance Reduction):
  1. **Bootstrap Sampling:** Tạo $B$ tập dữ liệu con bằng cách rút mẫu ngẫu nhiên **có hoàn lại** từ tập dữ liệu gốc ($N$ mẫu).
  2. **Random Subspace:** Tại mỗi lần chia nút của từng cây, chỉ chọn ngẫu nhiên một tập con gồm $m \approx \sqrt{p}$ đặc trưng (với phân loại) hoặc $m \approx p/3$ (với hồi quy) từ tổng số $p$ đặc trưng.
  3. **Aggregation:** Dự đoán bằng cách lấy biểu quyết đa số (Majority Voting) hoặc trung bình cộng (Averaging).
- **Out-of-Bag (OOB) Error:** Khoảng $36.8\%$ mẫu không được chọn trong mỗi lần rút mẫu bootstrap ($e^{-1} \approx 0.368$ khi $N \to \infty$). Tập OOB được sử dụng làm tập kiểm định tự nhiên mà không cần chia tập Validation riêng.
- **So sánh Bagging vs Boosting:**
  - **Bagging (Random Forest):** Huấn luyện các cây **song song độc lập**, mục tiêu chính là **giảm Variance** (chống overfit).
  - **Boosting (AdaBoost, GBDT, XGBoost, LightGBM, CatBoost):** Huấn luyện các cây **tuần tự**, cây sau sửa lỗi sai của cây trước (thông qua gán trọng số mẫu hoặc học phần dư Gradient), mục tiêu chính là **giảm Bias**.
- **⭐ Hay ra thi:**
  1. Random Forest giảm hiện tượng Overfitting nhờ kết hợp Bagging và ngẫu nhiên hóa không gian đặc trưng.
  2. Random Forest vẫn có thể bị Overfit nếu độ sâu từng cây quá lớn và dữ liệu có quá nhiều nhiễu.
  3. Đối với dữ liệu dạng bảng (Tabular Data), các mô hình GBDT (XGBoost, LightGBM) thường là lựa chọn số 1 về hiệu năng.

---

### §1.5 Overfitting, Underfitting, Bias-Variance Tradeoff & Cross-Validation
- **Bias-Variance Decomposition:**
  Sai số kỳ vọng của mô hình phân rã thành 3 thành phần:
  $$\mathbb{E}[(y - \hat{f}(x))^2] = \text{Bias}[\hat{f}(x)]^2 + \text{Var}[\hat{f}(x)] + \sigma^2$$
  - **Bias (Độ chệch):** Sai lệch giữa kỳ vọng dự đoán của mô hình và giá trị chân thực. Bias cao $\implies$ **Underfitting** (mô hình quá đơn giản, không học được quy luật).
  - **Variance (Phương sai):** Độ dao động của mô hình khi huấn luyện trên các tập dữ liệu khác nhau. Variance cao $\implies$ **Overfitting** (mô hình học vẹt cả nhiễu của tập train, train acc cao nhưng test acc thấp).
  - **$\sigma^2$ (Irreducible Error):** Nhiễu nội tại không thể loại bỏ của dữ liệu.
- **Kỹ thuật Cross-Validation (K-Fold):**
  - **K-Fold:** Chia dữ liệu thành $K$ phần bằng nhau, lần lượt dùng 1 phần làm validation và $K-1$ phần để huấn luyện.
  - **Stratified K-Fold:** Bắt buộc áp dụng cho bài toán **dữ liệu mất cân bằng lớp**, đảm bảo tỉ lệ các lớp trong mỗi fold giống hệt tỉ lệ trong toàn bộ tập dữ liệu.
  - **GroupKFold:** Đảm bảo toàn bộ mẫu thuộc cùng một nhóm (vd: cùng 1 bệnh nhân, cùng 1 người quay video, cùng 1 thửa ruộng) chỉ nằm trọn trong tập Train hoặc tập Val $\implies$ **Chống rò rỉ dữ liệu (Data Leakage)**.
- **⭐ Hay ra thi:**
  - Triệu chứng Train Acc 99% nhưng Val Acc 70% là biểu hiện kinh điển của **Overfitting**. Khắc phục: tăng dữ liệu, thêm Regularization (L1/L2), giảm số lượng tham số, Early Stopping.

---

### §1.6 Regularization L1 (Lasso) vs L2 (Ridge) vs ElasticNet
- **Định nghĩa:** Kỹ thuật thêm số hạng phạt vào hàm mất mát để kiểm soát độ phức tạp của trọng số $\mathbf{w}$:
  $$\mathcal{L}_{\text{reg}}(\mathbf{w}) = \mathcal{L}_0(\mathbf{w}) + \lambda \cdot \Omega(\mathbf{w})$$
- **L2 Regularization (Ridge Regression):**
  $$\Omega(\mathbf{w}) = \frac{1}{2} \|\mathbf{w}\|_2^2 = \frac{1}{2} \sum_{j=1}^d w_j^2$$
  - Gradient update: $w_j \leftarrow w_j(1 - \eta \lambda) - \eta \frac{\partial \mathcal{L}_0}{\partial w_j}$ (Weight Decay: kéo các trọng số nhỏ đều về gần 0 nhưng **không triệt tiêu hoàn toàn về 0**).
  - Nghiệm giải tích của Ridge: $\mathbf{w} = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$ (luôn khả nghịch nhờ $\lambda \mathbf{I}$).
- **L1 Regularization (Lasso Regression):**
  $$\Omega(\mathbf{w}) = \|\mathbf{w}\|_1 = \sum_{j=1}^d |w_j|$$
  - Tính chất đặc biệt: Tại điểm tối ưu, đường đồng mức của hàm loss tiếp xúc với hình thoi góc cạnh của chuẩn $L_1$ tại các trục tọa độ $\implies$ Ép nhiều trọng số $w_j$ **về chính xác bằng 0**.
  - Tác dụng: **Tạo tính thưa (Sparsity)** và thực hiện **chọn lọc đặc trưng tự động (Feature Selection)**.
- **⭐ Hay ra thi:**
  1. $L_1$ sinh ra mô hình thưa (Sparse Model), dùng để loại bỏ các đặc trưng thừa.
  2. $L_2$ co đều trọng số, ổn định hơn khi các đặc trưng có hiện tượng đa cộng tuyến (Multicollinearity).
  3. Dưới góc nhìn Bayes (§5.4): $L_2$ tương đương chuẩn tiên nghiệm Gaussian Prior; $L_1$ tương đương chuẩn tiên nghiệm Laplace Prior.

---

### §1.7 Các độ đo đánh giá mô hình (Classification Metrics)
- **Confusion Matrix:**
  $$\begin{pmatrix} TN & FP \\ FN & TP \end{pmatrix}$$
  - $TP$ (True Positive): Dương thật, đoán đúng.
  - $FP$ (False Positive - Type I Error): Âm thật, đoán thành Dương (Báo động giả).
  - $FN$ (False Negative - Type II Error): Dương thật, bỏ sót thành Âm (Bỏ lọt tội phạm/bệnh nhân).
  - $TN$ (True Negative): Âm thật, đoán đúng.
- **Công thức các độ đo:**
  - $\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$ (Chỉ có ý nghĩa khi các lớp cân bằng).
  - $\text{Precision} = \frac{TP}{TP + FP}$ (Đoán dương thì trúng bao nhiêu).
  - $\text{Recall (Sensitivity / True Positive Rate)} = \frac{TP}{TP + FN}$ (Bắt trúng được bao nhiêu ca dương thật).
  - $\text{Specificity (True Negative Rate)} = \frac{TN}{TN + FP}$.
  - $\text{False Positive Rate (FPR)} = 1 - \text{Specificity} = \frac{FP}{TN + FP}$.
  - **F1-Score:** Trung bình điều hòa (Harmonic Mean) của Precision và Recall:
    $$F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}$$
- **ROC-AUC vs PR-AUC:**
  - **ROC Curve:** Vẽ đồ thị $TPR$ (Trục Y) theo $FPR$ (Trục X) tại các ngưỡng cắt xác suất khác nhau. $AUC = 0.5$ tương đương đoán mò ngẫu nhiên; $AUC = 1.0$ là mô hình hoàn hảo.
  - **PR Curve:** Vẽ Precision theo Recall.
  - **⭐ Hay ra thi:** Khi dữ liệu **mất cân bằng lớp nghiêm trọng (Imbalanced)**, đường cong ROC-AUC dễ đưa ra đánh giá "lạc quan giả tạo" vì số lượng $TN$ áp đảo làm $FPR$ luôn cực nhỏ $\implies$ **Bắt buộc dùng PR-AUC và F1-Score**.

---

### §1.8 K-Means Clustering & Silhouette Score
- **Thuật toán K-Means:**
  Tối ưu hàm mục tiêu Inertia (Within-Cluster Sum of Squares - WCSS):
  $$J = \sum_{k=1}^K \sum_{x_i \in C_k} \|x_i - \mu_k\|_2^2$$
  - Khởi tạo $K$ centroids (dùng **K-Means++** để chọn các tâm cách xa nhau nhất).
  - Lặp: Gán từng điểm vào centroid gần nhất $\to$ Cập nhật centroid $\mu_k = \frac{1}{|C_k|}\sum_{x \in C_k} x$.
- **Silhouette Score (Hệ số bóng):**
  Đo lường mức độ phù hợp của điểm $i$ trong cụm của nó so với các cụm khác:
  $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
  - $a(i)$: Khoảng cách trung bình từ $i$ đến mọi điểm khác trong **cùng cụm**.
  - $b(i)$: Khoảng cách trung bình từ $i$ đến mọi điểm trong **cụm gần nó nhất**.
  - Miền giá trị: $s(i) \in [-1, 1]$.
    - $s(i) \approx 1$: Điểm nằm sâu trong cụm, phân tách rất tốt.
    - $s(i) \approx 0$: Điểm nằm sát biên giới giữa hai cụm.
    - $s(i) < 0$: Điểm có thể đã bị gán nhầm cụm.
- **⭐ Hay ra thi:**
  1. K-Means nhạy cảm với khởi tạo tâm ban đầu và các điểm ngoại lai (Outliers).
  2. Phải chuẩn hóa dữ liệu trước khi chạy K-Means.

---

### §1.9 Xử lý Mất cân bằng lớp (Imbalanced Data)
- **Vấn đề:** Lớp thiểu số (Minority Class) chiếm tỉ lệ quá nhỏ (vd: $1\%$ gian lận thẻ tín dụng, bệnh hiếm). Mô hình tối ưu Accuracy sẽ dự đoán $100\%$ nhãn đa số.
- **Kỹ thuật xử lý:**
  1. **Resampling:**
     - **Random Undersampling:** Bỏ bớt mẫu lớp đa số $\implies$ Nguy cơ mất thông tin quan trọng.
     - **Random Oversampling:** Sao chép nguyên văn mẫu thiểu số $\implies$ Dễ gây Overfitting.
     - **SMOTE (Synthetic Minority Over-sampling Technique):** **Nội suy sinh mẫu mới** trong không gian đặc trưng giữa một điểm thiểu số $\mathbf{x}_i$ và láng giềng gần nhất $\mathbf{x}_{zi}$:
       $$\mathbf{x}_{\text{new}} = \mathbf{x}_i + \lambda (\mathbf{x}_{zi} - \mathbf{x}_i), \quad \lambda \sim U(0, 1)$$
  2. **Cost-Sensitive Learning (Class Weights):** Gán trọng số phạt hàm loss lớn hơn cho lớp thiểu số:
     $$w_{\text{minority}} = \frac{N_{\text{total}}}{2 \cdot N_{\text{minority}}}$$
  3. **Focal Loss:** Thêm hệ số điều biến $(1 - p_t)^\gamma$ để giảm ảnh hưởng của các mẫu dễ phân loại (§2.4).
- **⭐ Hay ra thi:**
  - SMOTE **không phải là nhân bản (copy) y nguyên**, mà là sinh điểm mới bằng nội suy vector.
  - Phải áp dụng SMOTE **bên trong từng fold huấn luyện** của Cross-Validation, không được SMOTE trên toàn bộ tập dữ liệu trước khi chia fold (tránh data leakage).

---

### §1.10 Tiền xử lý Đặc trưng & Thao tác NumPy
- **Mã hóa (Encoding):**
  - **One-Hot Encoding:** Cho các biến danh mục không có thứ bậc (vd: Đỏ, Xanh, Vàng).
  - **Ordinal Encoding:** Cho các biến có thứ tự logic (vd: Tiểu học, Trung học, Đại học). Tránh dùng cho biến vô thứ tự vì sinh ra khoảng cách giả.
- **Quy tắc NumPy Broadcasting:**
  Hai chiều kích thước tương thích khi: chúng bằng nhau, hoặc một trong hai bằng 1.
  - Ví dụ: Mảng $A$ có shape $(4, 1)$ cộng mảng $B$ có shape $(4,)$ (được mở rộng thành $(1, 4)$):
    $$(4, 1) + (1, 4) \implies (4, 4)$$
  - Chuyển vị mảng: Nếu `a.shape == (3, 4)` thì `a.T.shape == (4, 3)`.

---

## §2. Deep Learning Cơ Bản & PyTorch Framework

### §2.1 Perceptron, MLP & Tính Phi Tuyến
- **Perceptron đơn:** $y = f(\mathbf{w}^T \mathbf{x} + b)$. Chỉ giải được các bài toán phân tách tuyến tính (không giải được hàm XOR - Minsky & Papert, 1969).
- **Multi-Layer Perceptron (MLP):** Chồng nhiều tầng biến đổi tuyến tính kết hợp hàm kích hoạt phi tuyến:
  $$\mathbf{h}^{(1)} = \sigma(\mathbf{W}_1 \mathbf{x} + \mathbf{b}_1), \quad \mathbf{y} = \mathbf{W}_2 \mathbf{h}^{(1)} + \mathbf{b}_2$$
- **⭐ Hay ra thi:** Nếu không có hàm kích hoạt phi tuyến $\sigma$, thì dù xếp chồng bao nhiêu tầng tuyến tính:
  $$\mathbf{W}_2(\mathbf{W}_1 \mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2 = (\mathbf{W}_2\mathbf{W}_1)\mathbf{x} + (\mathbf{W}_2\mathbf{b}_1 + \mathbf{b}_2) = \mathbf{W}'\mathbf{x} + \mathbf{b}'$$
  Mạng vẫn chỉ tương đương với một phép biến đổi tuyến tính đơn tầng.

---

### §2.2 Các hàm kích hoạt (Activation Functions)
| Hàm kích hoạt | Công thức toán học | Đạo hàm | Miền giá trị | Nhược điểm / Ứng dụng |
|---|---|---|---|---|
| **Sigmoid** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | $\sigma(z)(1 - \sigma(z))$ | $(0, 1)$ | Bão hòa khi $|z|$ lớn $\implies$ **Vanishing Gradient**. Không zero-centered. Dùng cho lớp **Output bài toán Binary Classification**. |
| **Softmax** | $\frac{e^{z_i}}{\sum_{j=1}^C e^{z_j}}$ | $\frac{\partial p_i}{\partial z_j} = p_i(\delta_{ij} - p_j)$ | $(0, 1), \sum p_i = 1$ | Biến vector logits thành phân phối xác suất. Dùng cho lớp **Output bài toán Multi-Class Classification**. |
| **Tanh** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $1 - \tanh^2(z)$ | $(-1, 1)$ | Zero-centered (tốt hơn Sigmoid), nhưng vẫn bị bão hòa hai đầu gây Vanishing Gradient. |
| **ReLU** | $\max(0, z)$ | $\begin{cases} 1 & z > 0 \\ 0 & z < 0 \end{cases}$ | $[0, +\infty)$ | Tính toán cực nhanh, dập tắt Vanishing Gradient ở miền $z > 0$. Nhược điểm: **Dying ReLU** (khi $z \le 0$, gradient triệt tiêu vĩnh viễn). Chuẩn cho **Hidden Layer CNN/MLP**. |
| **Leaky ReLU** | $\max(\alpha z, z) \quad (\alpha \approx 0.01)$ | $\begin{cases} 1 & z > 0 \\ \alpha & z < 0 \end{cases}$ | $(-\infty, +\infty)$ | Khắc phục hoàn toàn hiện tượng Dying ReLU nhờ giữ một độ dốc nhỏ khi $z < 0$. |
| **GELU** | $x \Phi(x) = x P(X \le x), X \sim \mathcal{N}(0, 1)$ | Liên tục, mượt | $(-0.17, +\infty)$ | Phi tuyến mượt mà, chuẩn công nghiệp cho các mô hình **Transformer, BERT, GPT, ViT**. |

---

### §2.3 Lan truyền xuôi, Lan truyền ngược & Vòng lặp Huấn luyện PyTorch
- **Thứ tự chuẩn của 1 Epoch huấn luyện trong PyTorch:**
  ```python
  model.train()  # 1. Bật chế độ train (bật Dropout, BatchNorm cập nhật running stats)
  for inputs, targets in dataloader:
      optimizer.zero_grad()       # 2. XÓA GRADIENT TÍCH LŨY CỦA BATCH TRƯỚC
      outputs = model(inputs)     # 3. Forward pass
      loss = criterion(outputs, targets) # 4. Tính hàm mất mát
      loss.backward()            # 5. Backward pass (tính dLoss/dw lưu vào w.grad)
      optimizer.step()           # 6. Cập nhật trọng số: w = w - lr * w.grad
  ```
- **⭐ Hay ra thi:**
  1. PyTorch mặc định **cộng dồn gradient** (`w.grad += ...`) để thuận tiện tính toán tích lũy gradient qua nhiều mini-batch. Do đó, **bắt buộc phải gọi `optimizer.zero_grad()` TRƯỚC `loss.backward()`**.
  2. `loss.backward()` chỉ làm nhiệm vụ tính toán đạo hàm; việc cập nhật trọng số do hàm `optimizer.step()` thực hiện.

---

### §2.4 Các hàm mất mát (Loss Functions)
- **Hồi quy (Regression):**
  - **Mean Squared Error (MSE):** $\mathcal{L}_{\text{MSE}} = \frac{1}{N}\sum (y_i - \hat{y}_i)^2$. Nhạy cảm và phạt rất nặng các điểm ngoại lai (Outliers).
  - **Mean Absolute Error (MAE / L1 Loss):** $\mathcal{L}_{\text{MAE}} = \frac{1}{N}\sum |y_i - \hat{y}_i|$. Bền vững (Robust) hơn với Outliers.
  - **Huber Loss / Smooth L1 Loss:** Kết hợp MSE ở lân cận 0 và MAE khi sai số lớn.
- **Phân loại (Classification):**
  - **Binary Cross-Entropy (BCE):**
    $$\mathcal{L}_{\text{BCE}} = -\frac{1}{N}\sum [y_i \log(\hat{y}_i) + (1 - y_i)\log(1 - \hat{y}_i)]$$
    - Đầu vào $\hat{y}_i$ phải là xác suất trong khoảng $(0, 1)$ (đã qua Sigmoid).
  - **`nn.BCEWithLogitsLoss` trong PyTorch:** Gộp hàm Sigmoid và BCE vào chung một công thức toán học thống nhất bằng kỹ thuật log-sum-exp:
    $$\mathcal{L} = \max(z, 0) - z y + \log(1 + e^{-|z|})$$
    $\implies$ **Đầu vào nhận Logit thô $z$ (chưa qua Sigmoid)**, giúp chống hiện tượng tràn số (Overflow/Underflow).
  - **`nn.CrossEntropyLoss` trong PyTorch (Đa lớp):**
    Gộp trực tiếp `nn.LogSoftmax()` và `nn.NLLLoss()` (Negative Log Likelihood):
    $$\mathcal{L}_{\text{CE}} = -\log\left( \frac{e^{z_y}}{\sum_{j=1}^C e^{z_j}} \right) = -z_y + \log\left( \sum_{j=1}^C e^{z_j} \right)$$
    $\implies$ **Đầu vào nhận Logit thô $z$ (CHƯA qua Softmax)**.
- **⭐ Hay ra thi:** Lỗi **"Double Softmax"** hoặc **"Double Sigmoid"**: Nếu mô hình đã khai báo tầng cuối là `nn.Softmax()` mà loss lại dùng `nn.CrossEntropyLoss()`, kết quả gradient sẽ bị sai lệch nghiêm trọng.

---

### §2.5 Thuật toán tối ưu hóa (Optimizers)
- **SGD (Stochastic Gradient Descent):** $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \mathbf{g}_t$. Dễ bị dao động mạnh ở các hẻm vực dốc (ravines).
- **SGD with Momentum:** Thêm quán tính $\mathbf{v}_t$ để duy trì hướng đi và vượt qua cực tiểu địa phương cạn:
  $$\mathbf{v}_{t+1} = \beta \mathbf{v}_t + \eta \mathbf{g}_t, \quad \mathbf{w}_{t+1} = \mathbf{w}_t - \mathbf{v}_{t+1}$$
- **Adam (Adaptive Moment Estimation):** Kết hợp Momentum (moment bậc 1) và RMSProp (moment bậc 2 - thích ứng tốc độ học theo từng tham số):
  $$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \mathbf{g}_t, \quad \mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) \mathbf{g}_t^2$$
  Hiệu chỉnh độ chệch ban đầu (Bias Correction):
  $$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1 - \beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t}$$
  Cập nhật trọng số:
  $$\mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \hat{\mathbf{m}}_t$$
  *(Tham số mặc định chuẩn: $\beta_1 = 0.9, \beta_2 = 0.999, \epsilon = 10^{-8}$)*.
- **⭐ Hay ra thi:** Adam hội tụ rất nhanh và ít nhạy cảm với việc chọn Learning Rate ban đầu, là lựa chọn số 1 làm baseline.

---

### §2.6 Learning Rate Scheduling & Warmup
- **Learning Rate quá lớn:** Hàm mất mát phân kỳ (Diverge) hoặc nhảy vọt qua cực tiểu, loss biến thành `NaN`.
- **Learning Rate quá nhỏ:** Hội tụ cực kỳ chậm hoặc mắc kẹt ở điểm yên ngựa (Saddle Points).
- **Chiến lược điều chỉnh (Schedules):**
  - **Step Decay:** Giảm $\eta$ đi hệ số $\gamma$ (vd: $0.1$) sau mỗi $K$ epochs.
  - **Cosine Annealing:** Giảm $\eta$ theo dạng nửa chu kỳ hàm cosin, giúp hội tụ mượt mà về cuối quá trình học.
  - **Learning Rate Warmup:** Tăng dần $\eta$ từ giá trị rất nhỏ lên giá trị mục tiêu trong vài epoch đầu tiên. **Đặc biệt quan trọng đối với mô hình Transformer** để tránh gradient cực lớn ở đầu quá trình học phá vỡ các trọng số khởi tạo ban đầu.

---

### §2.7 Khởi tạo Trọng số (Weight Initialization)
- **Khởi tạo Zeros (Tất cả bằng 0):** **HOÀN TOÀN SAI**. Mọi neuron trong cùng một lớp nhận tín hiệu giống nhau và có cùng đạo hàm $\implies$ Cập nhật y hệt nhau, không thể phá vỡ tính đối xứng (Symmetry Problem).
- **Xavier / Glorot Initialization:** Giữ cho phương sai của tín hiệu và gradient không đổi qua các tầng:
  $$\text{Var}(W) = \frac{2}{n_{\text{in}} + n_{\text{out}}}$$
  $\implies$ Tối ưu cho các hàm kích hoạt có dạng đối xứng quanh 0 như **Tanh** và **Sigmoid**.
- **He / Kaiming Initialization:** Do ReLU dập tắt $50\%$ tín hiệu âm, phương sai cần được nhân đôi:
  $$\text{Var}(W) = \frac{2}{n_{\text{in}}}$$
  $\implies$ **Bắt buộc dùng cho ReLU và Leaky ReLU**.

---

### §2.8 Chuẩn hóa Tầng (Batch Normalization vs Layer Normalization)
- **Batch Normalization (BatchNorm — Ioffe & Szegedy, 2015):**
  Chuẩn hóa trên toàn bộ mini-batch dọc theo chiều mẫu:
  $$\mu_B = \frac{1}{m}\sum x_i, \quad \sigma_B^2 = \frac{1}{m}\sum (x_i - \mu_B)^2, \quad \hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$
  $$y_i = \gamma \hat{x}_i + \beta \quad (\gamma, \beta \text{ là các tham số học được})$$
  - Vị trí chuẩn: **Linear / Conv $\to$ BatchNorm $\to$ ReLU**.
  - Lúc suy luận (Inference): Dùng giá trị trung bình tích lũy `running_mean` và `running_var` được lưu từ quá trình train.
  - Nhược điểm: Kém hiệu quả khi kích thước batch size nhỏ ($m < 8$) hoặc dữ liệu có độ dài thay đổi như văn bản.
- **Layer Normalization (LayerNorm — Ba et al., 2016):**
  Chuẩn hóa độc lập trên từng mẫu dữ liệu đơn lẻ dọc theo chiều các đặc trưng (Features). **Không phụ thuộc vào kích thước mini-batch**.
  $\implies$ **Là chuẩn mực bắt buộc cho Transformer, RNN và NLP**.

---

### §2.9 Dropout & Tránh Overfitting
- **Cơ chế Inverted Dropout:** Trong pha Train, tại mỗi bước lặp ngẫu nhiên tắt một neuron với xác suất $p$ (giữ lại với $1-p$). Đồng thời chia tín hiệu cho $1-p$ để giữ nguyên kỳ vọng:
  $$h_{\text{train}} = \frac{1}{1 - p} (h \odot m), \quad m \sim \text{Bernoulli}(1 - p)$$
- Khi suy luận (Inference/Test): **TẮT HOÀN TOÀN Dropout** (`model.eval()`), giữ nguyên toàn bộ mạng neuron.
- **⭐ Hay ra thi:** Dropout đóng vai trò như việc kết hợp ẩn (Ensemble) của vô số mạng con ngẫu nhiên. Nếu quên gọi `model.eval()` khi inference, kết quả dự đoán sẽ bị ngẫu nhiên và suy giảm độ chính xác.

---

### §2.10 Gradient Vanishing & Exploding, Early Stopping
- **Vanishing Gradient:** Đạo hàm lan truyền ngược bị triệt tiêu dần qua các tầng sâu $\implies$ Tầng đầu gần như không học được. Nguyên nhân: dùng Sigmoid/Tanh và mạng sâu. Khắc phục: Dùng **ReLU**, kết nối tắt **Residual Connection (ResNet)**, **BatchNorm**, khởi tạo **He Init**.
- **Exploding Gradient:** Đạo hàm bị phóng đại lũy thừa qua nhiều tầng $\implies$ Loss biến thành `NaN`. Khắc phục: **Gradient Clipping** ($\mathbf{g} \leftarrow \min(1, \frac{c}{\|\mathbf{g}\|})\mathbf{g}$).
- **Early Stopping:** Theo dõi loss trên tập Validation. Nếu sau $P$ epochs (patience) mà Val Loss không cải thiện, dừng huấn luyện và khôi phục checkpoint tốt nhất.

---

## §3. Thị Giác Máy Tính (Computer Vision)

### §3.1 Lớp Convolution & Công thức Kích thước Đầu ra
- **Phép tích chập 2D:** Trượt kernel kích thước $K \times K$ trên ma trận ảnh để trích xuất bản đồ đặc trưng (Feature Map).
- **Công thức tính kích thước không gian đầu ra:**
  $$O = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$$
  Trong đó: $W$ là kích thước cạnh vào, $K$ là kích thước kernel, $P$ là padding, $S$ là stride (bước trượt).
  - **Valid Padding:** $P = 0 \implies O = \lfloor \frac{W - K}{S} \rfloor + 1$.
  - **Same Padding:** Chọn $P$ sao cho kích thước giữ nguyên khi $S = 1$: $P = \frac{K - 1}{2}$ (với $K$ lẻ).
- **Tính toán số lượng tham số của 1 tầng Conv2D:**
  $$\text{Params} = (K_H \times K_W \times C_{\text{in}} + 1) \times C_{\text{out}}$$
  *(Trong đó $+1$ là bias cho mỗi filter đầu ra)*.
- **⭐ Hay ra thi:** 90% câu trắc nghiệm tính toán trong phần CV rơi vào công thức này. Hãy nhớ lấy phần nguyên sàn (`floor`) trước khi cộng 1.

---

### §3.2 Pooling & Trường Thụ Cảm (Receptive Field)
- **Lớp Pooling:**
  - **Max Pooling:** Lấy giá trị lớn nhất trong cửa sổ, giữ lại đặc trưng kích hoạt mạnh nhất, đem lại tính bất biến với phép tịnh tiến nhỏ.
  - **Average Pooling:** Lấy trung bình cộng, làm mượt đặc trưng.
  - **Global Average Pooling (GAP):** Tính trung bình cộng của toàn bộ không gian $H \times W$ của mỗi channel thành 1 giá trị duy nhất ($H \times W \times C \to 1 \times 1 \times C$). **Thay thế hoàn toàn các lớp Fully Connected cồng kềnh**, giúp giảm hàng triệu tham số và chống Overfitting mạnh mẽ.
- **⭐ Hay ra thi:** Lớp Pooling **hoàn toàn không có tham số học được (0 learnable parameters)**.
- **Receptive Field (RF):** Vùng trên ảnh đầu vào ảnh hưởng trực tiếp đến một neuron ở tầng hiện tại. Việc xếp chồng nhiều lớp conv $3 \times 3$ giúp mở rộng Receptive Field: 2 lớp $3 \times 3$ có RF tương đương 1 lớp $5 \times 5$, nhưng số tham số ít hơn ($2 \times 3^2 = 18 < 5^2 = 25$) và có 2 lần phi tuyến hóa.

---

### §3.3 Các Kiến trúc CNN Kinh Điển
- **LeNet-5 (1998):** Mở đầu kỷ nguyên CNN cho nhận dạng chữ số viết tay.
- **AlexNet (2012):** Vô địch ImageNet, sử dụng GPU, ReLU, Dropout, Data Augmentation.
- **VGG (2014):** Sử dụng triết lý thiết kế đồng nhất: chỉ xếp chồng các lớp tích chập nhỏ **$3 \times 3$** liên tiếp với stride 1 và MaxPool $2 \times 2$.
- **ResNet (He et al., 2015):** Đột phá giải quyết vấn đề thoái hóa mô hình (Degradation Problem) ở các mạng cực sâu thông qua **Residual Block**:
  $$\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$$
  Nhờ đường dẫn tắt (Identity Shortcut), gradient có thể chảy thẳng ngược về các tầng đầu tiên mà không bị suy giảm:
  $$\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \left( \frac{\partial \mathcal{F}}{\partial \mathbf{x}} + 1 \right)$$
  Số hạng $+1$ đảm bảo gradient không bao giờ bị triệt tiêu hoàn toàn về 0.
- **EfficientNet (2019):** Sử dụng cơ chế **Compound Scaling**, mở rộng đồng thời cả 3 chiều: độ sâu (Depth), chiều rộng (Width) và độ phân giải ảnh (Resolution) theo tỉ lệ cố định bằng hệ số $\phi$.

---

### §3.4 Skip Connection: ResNet (ADD) vs U-Net (CONCAT)
- **ResNet Skip Connection:** Phép **CỘNG theo từng phần tử (Element-wise ADD)**:
  $$\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$$
  - Yêu cầu: Số lượng channel và kích thước không gian của $\mathcal{F}(\mathbf{x})$ và $\mathbf{x}$ phải giống hệt nhau.
  - Mục tiêu: Học phần dư (Residual), cho phép xây dựng mạng sâu hàng trăm tầng.
- **U-Net Skip Connection:** Phép **GHÉP NỐI theo chiều kênh (Channel-wise CONCAT)**:
  $$\mathbf{y} = [\mathbf{x}_{\text{decoder}}, \mathbf{x}_{\text{encoder}}]$$
  - Nối trực tiếp bản đồ đặc trưng có độ phân giải cao từ nhánh Encoder sang nhánh Decoder.
  - Mục tiêu: Giữ lại chi tiết không gian chính xác đến từng pixel để phục vụ bài toán **Phân vùng ảnh (Segmentation)**.
- **⭐ Hay ra thi:** Nhớ quy tắc: **ResNet = ADD**, **U-Net = CONCAT**.

---

### §3.5 Vision Transformer (ViT — Dosovitskiy et al., 2020)
- **Cơ chế hoạt động:**
  1. Cắt ảnh $H \times W \times C$ thành $N$ mảnh vuông nhỏ (Patches) kích thước $P \times P$: $N = \frac{HW}{P^2}$.
  2. Dùng phép chiếu tuyến tính (Linear Projection) làm phẳng mỗi patch thành vector embedding $D$ chiều.
  3. Thêm một token đặc biệt có thể học được là **`[CLS]` token** vào đầu chuỗi (đại diện cho nhãn phân loại toàn ảnh).
  4. Cộng **Positional Embedding 1D** vào từng vector token để lưu giữ vị trí không gian.
  5. Đưa toàn bộ chuỗi token qua kiến trúc chuẩn Transformer Encoder (chỉ gồm Multi-Head Attention và MLP).
- **⭐ Hay ra thi:**
  - ViT **hoàn toàn không sử dụng các phép tích chập (No Convolution)**.
  - Do thiếu tính chất tiền định về không gian (Inductive Bias của CNN như tính cục bộ và bất biến tịnh tiến), ViT cần tập dữ liệu cực lớn (như JFT-300M, ImageNet-21k) để tiền huấn luyện mới vượt qua được CNN.

---

### §3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN
- **Độ đo Intersection over Union (IoU):**
  $$\text{IoU} = \frac{\text{Diện tích vùng Giao}}{\text{Diện tích vùng Hợp}} = \frac{|A \cap B|}{|A \cup B|}$$
  Một dự đoán được tính là True Positive ($TP$) nếu $\text{IoU} \ge \text{ngưỡng}$ (thường là $0.5$).
- **Non-Maximum Suppression (NMS):**
  Thuật toán loại bỏ các bounding box trùng lặp:
  1. Lọc bỏ các box có confidence score nhỏ hơn ngưỡng tin cậy.
  2. Chọn box $B_{\text{max}}$ có confidence cao nhất, đưa vào danh sách giữ lại.
  3. Tính IoU giữa $B_{\text{max}}$ và tất cả các box còn lại. Nếu $\text{IoU} \ge \text{ngưỡng NMS}$ (vd: $0.5$), xóa bỏ box đó.
  4. Lặp lại bước 2-3 cho đến khi hết box.
- **Mean Average Precision (mAP):**
  - $AP$ (Average Precision): Diện tích dưới đường cong Precision-Recall cho 1 lớp.
  - $mAP$: Trung bình $AP$ của tất cả các lớp vật thể.
  - $\text{mAP@0.5}$: Đo ở ngưỡng $\text{IoU} = 0.5$. $\text{mAP@[0.5:0.95]}$: Đo trung bình qua các ngưỡng từ $0.5$ đến $0.95$ với bước nhảy $0.05$.
- **So sánh YOLO (1-Stage) vs R-CNN (2-Stage):**
  - **1-Stage (YOLOv8, YOLOv11, SSD):** Chia ảnh thành lưới, dự đoán trực tiếp tọa độ box và xác suất lớp trên toàn bộ ảnh trong một lần forward duy nhất. **Tốc độ cực nhanh (Real-time 30-100+ FPS)**, thích hợp cho thiết bị di động/nhúng.
  - **2-Stage (Faster R-CNN):** Bước 1 dùng RPN (Region Proposal Network) đề xuất các vùng ứng viên; Bước 2 trích xuất đặc trưng và phân loại chi tiết. **Độ chính xác cao hơn cho vật thể nhỏ, nhưng chậm hơn**.

---

### §3.7 Phân vùng ảnh: Semantic vs Instance Segmentation
- **Semantic Segmentation:** Gán nhãn ngữ nghĩa cho **từng pixel** trên ảnh. Các vật thể thuộc cùng một lớp mang cùng một nhãn màu giống nhau (không phân biệt giữa hai chiếc xe đứng cạnh nhau). Mô hình tiêu biểu: **U-Net, DeepLabV3+**.
- **Instance Segmentation:** Vừa xác định lớp ngữ nghĩa cho từng pixel, vừa **tách biệt rõ ràng từng cá thể riêng biệt** trong cùng một lớp (gán ID riêng cho từng chiếc xe). Mô hình tiêu biểu: **Mask R-CNN**.

---

### §3.8 Mô hình Sinh ảnh: GAN vs Diffusion vs Autoencoder
- **GAN (Generative Adversarial Networks — Goodfellow, 2014):**
  Trò chơi đối kháng Minimax giữa hai mạng:
  $$\min_G \max_D V(D, G) = \mathbb{E}_{x}[\log D(x)] + \mathbb{E}_{z}[\log(1 - D(G(z)))]$$
  - $G$ (Generator): Tạo ảnh giả từ nhiễu $z$.
  - $D$ (Discriminator): Phân biệt ảnh thật từ dữ liệu và ảnh giả từ $G$.
  - Nhược điểm: Huấn luyện không ổn định, dễ mắc lỗi **Mode Collapse** (Generator chỉ tạo ra một số rất ít mẫu giống nhau lặp đi lặp lại).
- **Diffusion Models (DDPM, Stable Diffusion):**
  - Quá trình thuận (Forward Process): Thêm nhiễu Gaussian tăng dần qua $T$ bước thời gian vào ảnh thật biến thành nhiễu trắng thuần túy.
  - Quá trình nghịch (Reverse Process): Dùng mạng nơ-ron (kiến trúc U-Net) học cách **dự đoán nhiễu để khử nhiễu từng bước một** khôi phục lại ảnh rõ nét.
  - **⭐ Hay ra thi:** Stable Diffusion là **Diffusion Model**, **KHÔNG phải GAN**. Mô hình Diffusion tạo ảnh đa dạng, chất lượng cao và huấn luyện ổn định hơn GAN, nhưng tốc độ suy luận chậm hơn do phải lặp qua nhiều bước khử nhiễu.

---

### §3.9 Data Augmentation & Transfer Learning
- **Data Augmentation:** Tăng cường dữ liệu bằng các phép biến đổi hình học (Random Crop, Flip, Rotate), màu sắc (Color Jitter), hoặc nâng cao như **Mixup** (trộn tuyến tính 2 ảnh và 2 nhãn) và **CutMix** (cắt dán một phần ảnh này vào ảnh khác).
  - **⭐ Hay ra thi:** Data Augmentation **chỉ được áp dụng trong tập Train**, tập Validation và Test tuyệt đối giữ nguyên.
- **Transfer Learning (Học chuyển giao):**
  Sử dụng mô hình đã huấn luyện sẵn trên tập dữ liệu khổng lồ (ImageNet 1.4 triệu ảnh):
  - Dữ liệu mới rất ít: **Đóng băng toàn bộ Backbone**, chỉ huấn luyện phân loại ở lớp Head cuối cùng.
  - Dữ liệu mới dồi dào: Huấn luyện toàn bộ mạng với **Learning Rate rất nhỏ** để tinh chỉnh (Fine-tuning).

---

## §4. Xử Lý Ngôn Ngữ Tự Nhiên (NLP)

### §4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn
Quy trình tiền xử lý văn bản kinh điển theo **đúng thứ tự bắt buộc**:
1. **Tokenization (Tách từ/token):** Cắt văn bản thô thành các đơn vị nhỏ (từ, cụm từ, hoặc subword).
2. **Normalization (Chuẩn hóa):** Đưa về chữ thường (lowercase), loại bỏ dấu câu, chuẩn hóa bảng mã Unicode (NFC/NFD).
3. **Stemming / Lemmatization:**
   - **Stemming:** Cắt đuôi từ thô bạo theo quy tắc heuristic (vd: `running`, `runs` $\to$ `runn`).
   - **Lemmatization:** Đưa từ về dạng từ điển nguyên thể (Lemma) dựa trên ngữ cảnh và từ loại (vd: `better` $\to$ `good`, `was` $\to$ `be`).
4. **POS Tagging (Gán nhãn từ loại):** Gán nhãn Danh từ (NOUN), Động từ (VERB), Tính từ (ADJ).
5. **Stopwords Removal (Loại bỏ từ dừng):** Loại các từ phổ biến mang ít giá trị phân loại (vd: `và`, `là`, `the`, `is`).
- **⭐ Hay ra thi:** Thứ tự các bước trên rất hay được hỏi trong các câu trắc nghiệm.

---

### §4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)
- **One-Hot Encoding:** Biểu diễn từ bằng vector có số chiều bằng kích thước từ điển $|V|$. Rất thưa (sparse), tốn bộ nhớ và **không thể hiện được mối tương quan ngữ nghĩa** giữa các từ (tích vô hướng giữa hai từ bất kỳ luôn bằng 0).
- **TF-IDF (Term Frequency - Inverse Document Frequency):**
  $$\text{TF}(t, d) = \frac{f_{t,d}}{\sum_{t'} f_{t',d}}, \quad \text{IDF}(t, D) = \log\left( \frac{|D|}{|\{d \in D: t \in d\}|} \right)$$
  $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
  Từ xuất hiện thường xuyên trong một văn bản nhưng hiếm gặp trong toàn bộ kho tài liệu sẽ có trọng số TF-IDF rất cao. Rất hiệu quả cho các bài toán phân loại văn bản cơ bản và trích xuất thông tin (Information Retrieval).
- **Word2Vec (Mikolov et al., 2013):**
  Học vector dày đặc (Dense Vector) thông qua ngữ cảnh:
  - **CBOW (Continuous Bag of Words):** Dự đoán từ mục tiêu dựa vào các từ ngữ cảnh xung quanh. Huấn luyện nhanh hơn, tốt cho các từ xuất hiện thường xuyên.
  - **Skip-gram:** Dự đoán các từ ngữ cảnh xung quanh dựa vào từ mục tiêu ở giữa. Tốt hơn cho các từ hiếm gặp. Dùng kỹ thuật **Negative Sampling** để tăng tốc độ tính toán softmax.
- **FastText (Bojanowski et al., 2017):**
  Mở rộng Word2Vec bằng cách biểu diễn mỗi từ như một tập hợp các **ký tự n-gram** (Subwords).
  - Ví dụ: Từ `where` với 3-grams: `<wh`, `whe`, `her`, `ere`, `re>`.
  - **Ưu điểm vượt trội:** Xử lý triệt để bài toán **Từ ngoài từ điển (OOV — Out-of-Vocabulary)**, từ viết tắt và từ sai chính tả.
- **Contextual Embeddings (BERT / RoBERTa):**
  Mỗi từ có một vector biểu diễn **thay đổi linh hoạt tùy theo ngữ cảnh xuất hiện** trong câu (từ `ngân hàng` trong ngữ cảnh tài chính có vector khác hoàn toàn với `ngân hàng dữ liệu`).

---

### §4.3 Cosine Similarity
- **Công thức:**
  $$\cos(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2} = \frac{\sum u_i v_i}{\sqrt{\sum u_i^2} \sqrt{\sum v_i^2}}$$
- Miền giá trị: $[-1, 1]$.
  - $\cos = 1$: Hai vector cùng hướng hoàn toàn.
  - $\cos = 0$: Hai vector trực giao, không liên quan về ngữ nghĩa.
  - $\cos = -1$: Hai vector ngược hướng hoàn toàn.
- **⭐ Hay ra thi:** Khi so sánh độ tương đồng giữa các vector nhúng (Embeddings) trong NLP, **bắt buộc dùng Cosine Similarity** thay vì khoảng cách Euclid vì Cosine Similarity chuẩn hóa theo độ dài vector, không bị chi phối bởi độ dài câu hay tần suất xuất hiện.

---

### §4.4 Mạng Nơ-ron Hồi Quy: RNN, LSTM & GRU
- **Vanilla RNN:**
  $$h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b)$$
  Khi lan truyền ngược qua chuỗi thời gian dài (Backpropagation Through Time — BPTT), gradient bị nhân liên tiếp qua ma trận $W_{hh}^T$ $\implies$ **Vanishing Gradient nghiêm trọng**, làm RNN mất khả năng ghi nhớ thông tin phụ thuộc xa.
- **LSTM (Long Short-Term Memory — Hochreiter & Schmidhuber, 1997):**
  Giải quyết triệt để vấn đề mất nhớ dài hạn nhờ đường truyền **Cell State ($C_t$)** đóng vai trò như xa lộ thông tin được điều tiết bởi 3 cổng (Gates):
  1. **Cổng Quên (Forget Gate):** Quyết định bỏ thông tin cũ nào:
     $$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$$
  2. **Cổng Nhớ (Input Gate):** Quyết định nạp thông tin mới nào:
     $$i_t = \sigma(W_i [h_{t-1}, x_t] + b_i), \quad \tilde{C}_t = \tanh(W_c [h_{t-1}, x_t] + b_c)$$
  3. Cập nhật Cell State: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$.
  4. **Cổng Đầu ra (Output Gate):** Quyết định thông tin xuất ra hidden state:
     $$o_t = \sigma(W_o [h_{t-1}, x_t] + b_o), \quad h_t = o_t \odot \tanh(C_t)$$
- **GRU (Gated Recurrent Unit — Cho et al., 2014):**
  Phiên bản tinh gọn của LSTM: Gộp Cell State và Hidden State, chỉ dùng **2 cổng: Cổng Reset ($r_t$) và Cổng Update ($z_t$)**. Số lượng tham số ít hơn LSTM, huấn luyện nhanh hơn mà hiệu quả tương đương trên nhiều tác vụ.

---

### §4.5 Kiến trúc Transformer (Vaswani et al., 2017)
- **Scaled Dot-Product Attention:**
  Cho 3 ma trận truy vấn (Query - $Q$), chìa khóa (Key - $K$), và giá trị (Value - $V$):
  $$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{QK^T}{\sqrt{d_k}} \right) V$$
  - **Vì sao phải chia cho $\sqrt{d_k}$?** Khi số chiều $d_k$ lớn, tích vô hướng $QK^T$ có phương sai tăng tỉ lệ thuận với $d_k$. Nếu không chia cho $\sqrt{d_k}$, các giá trị sẽ rất lớn, đẩy hàm Softmax vào vùng bão hòa có đạo hàm cực nhỏ $\implies$ **Vanishing Gradient**.
- **Multi-Head Attention (MHA):**
  Cho phép mô hình đồng thời chú ý đến thông tin từ các không gian biểu diễn khác nhau tại các vị trí khác nhau:
  $$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O$$
  $$\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$
- **Positional Encoding (Mã hóa Vị trí):**
  Do cơ chế Attention xử lý toàn bộ các từ song song và có tính chất bất biến hoán vị (Permutation Invariant), mô hình không tự nhận biết được thứ tự các từ trong câu. Do đó bắt buộc phải cộng vector vị trí vào vector nhúng từ:
  $$PE_{(pos, 2i)} = \sin\left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right), \quad PE_{(pos, 2i+1)} = \cos\left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right)$$

---

### §4.6 So sánh BERT vs GPT
| Tiêu chí | BERT (Devlin et al., 2018) | GPT (Radford et al., 2018) |
|---|---|---|
| **Kiến trúc** | **Encoder-only** của Transformer | **Decoder-only** của Transformer |
| **Cơ chế Attention** | **2 chiều (Bidirectional)**: Mỗi từ được nhìn cả từ phía trước và phía sau | **Tự hồi quy 1 chiều (Autoregressive, Causal Masked)**: Chỉ nhìn các từ phía trước (Left-to-Right) |
| **Nhiệm vụ Pre-training** | MLM (Masked Language Modeling — che ngẫu nhiên 15% từ) và NSP (Next Sentence Prediction) | Causal Language Modeling (Dự đoán từ tiếp theo: $\max \sum \log P(w_t \mid w_{<t})$) |
| **Ứng dụng sở trường** | **Hiểu ngôn ngữ (NLU)**: Phân loại câu, gán nhãn thực thể (NER), hỏi đáp trích xuất (Extractive QA) | **Sinh ngôn ngữ (NLG)**: Tạo văn bản, dịch máy, viết code, hội thoại tự do |

---

### §4.7 Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity
- **BLEU (Bilingual Evaluation Understudy):**
  Độ đo chuẩn cho bài toán **Dịch máy (Machine Translation)**, tính toán độ chính xác n-gram biến đổi (Modified n-gram Precision) giữa câu dịch của mô hình và các câu tham chiếu (References):
  $$\text{BLEU} = BP \times \exp\left( \sum_{n=1}^N w_n \log p_n \right)$$
  - Hệ số phạt câu dịch quá ngắn (Brevity Penalty — $BP$):
    $$BP = \begin{cases} 1 & \text{nếu } c > r \\ e^{1 - r/c} & \text{nếu } c \le r \end{cases}$$
    *(Trong đó $c$ là độ dài câu dự đoán, $r$ là độ dài câu tham chiếu)*.
- **SacreBLEU:** Bản nâng cấp chuẩn hóa quốc tế của BLEU, tự động thực hiện tokenization chuẩn để kết quả điểm số có thể tái lập và so sánh công bằng giữa các nghiên cứu.
- **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):**
  Độ đo định hướng độ phủ (Recall), chuẩn cho bài toán **Tóm tắt văn bản (Text Summarization)**:
  - **ROUGE-N:** Tỉ lệ bao phủ các n-gram tham chiếu có mặt trong bản tóm tắt mô hình tạo ra.
  - **ROUGE-L:** Dựa trên Chuỗi con chung dài nhất (Longest Common Subsequence — LCS).
- **Perplexity (PPL):**
  Độ bối rối của Mô hình ngôn ngữ (Language Model):
  $$\text{PPL} = \exp\left( -\frac{1}{N}\sum_{i=1}^N \log P(w_i \mid w_{<i}) \right) = 2^{\mathcal{L}_{\text{CE}}}$$
  $\implies$ **Điểm Perplexity càng THẤP thì mô hình càng TỐT** (càng ít bối rối khi dự đoán từ tiếp theo).

---

## §5. Xác Suất & Thống Kê Cho Trí Tuệ Nhân Tạo

### §5.1 Định Lý Bayes & Bài Toán Chẩn Đoán Y Tế (Base-Rate Fallacy)
- **Công thức xác suất có điều kiện & Định lý Bayes:**
  $$P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)} = \frac{P(B \mid A) P(A)}{P(B \mid A)P(A) + P(B \mid \neg A)P(\neg A)}$$
  - $P(A)$: Xác suất tiên nghiệm (Prior).
  - $P(B \mid A)$: Khả năng xảy ra (Likelihood).
  - $P(A \mid B)$: Xác suất hậu nghiệm (Posterior).
  - $P(B)$: Xác suất biên duyên (Marginal probability).
- **Ví dụ tính tay kinh điển (Bài toán xét nghiệm bệnh hiếm):**
  - Tỉ lệ mắc bệnh trong dân số: $P(\text{Bệnh}) = 1\% = 0.01 \implies P(\text{Khỏe}) = 0.99$.
  - Độ nhạy của test (Sensitivity): $P(+ \mid \text{Bệnh}) = 90\% = 0.90$.
  - Tỉ lệ dương tính giả (False Positive): $P(+ \mid \text{Khỏe}) = 5\% = 0.05$.
  - Xác suất một người có kết quả test Dương tính thực sự mắc bệnh:
    $$P(\text{Bệnh} \mid +) = \frac{0.90 \times 0.01}{0.90 \times 0.01 + 0.05 \times 0.99} = \frac{0.009}{0.009 + 0.0495} = \frac{0.009}{0.0585} \approx 15.38\%$$
- **⭐ Hay ra thi:** Do tỉ lệ bệnh trong dân số quá nhỏ ($1\%$), số lượng người khỏe bị dương tính giả ($4.95\%$) áp đảo số lượng người thực sự có bệnh ($0.9\%$). Vì vậy, dù test có độ nhạy $90\%$, xác suất thực sự có bệnh khi test dương tính **chỉ khoảng $15.4\%$**. Hiện tượng này gọi là **Ngụy biện tỷ lệ cơ sở (Base-Rate Fallacy)**.

---

### §5.2 Các Phân Phối Xác Suất Quan Trọng
1. **Phân phối Bernoulli:** Biến ngẫu nhiên nhị phân $X \in \{0, 1\}$ với xác suất thành công $p$:
   $$\mathbb{E}[X] = p, \quad \text{Var}(X) = p(1 - p)$$
2. **Phân phối Nhị thức (Binomial Distribution):** Số lần thành công trong $n$ phép thử Bernoulli độc lập:
   $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}, \quad \mathbb{E}[X] = np, \quad \text{Var}(X) = np(1 - p)$$
3. **Phân phối Poisson:** Mô hình hóa số lượng sự kiện hiếm xảy ra trong một khoảng thời gian/không gian cố định với tốc độ trung bình $\lambda$:
   $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad \mathbb{E}[X] = \lambda, \quad \text{Var}(X) = \lambda$$
   - Ví dụ: Số cuộc gọi đến tổng đài trung bình 3 cuộc/phút ($\lambda = 3$). Xác suất trong 1 phút không có cuộc gọi nào ($k=0$):
     $$P(X = 0) = \frac{3^0 e^{-3}}{0!} = e^{-3} \approx 0.0498 \approx 5\%$$
4. **Phân phối Chuẩn (Gaussian / Normal):** $X \sim \mathcal{N}(\mu, \sigma^2)$:
   $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)$$
   - **Định lý Giới hạn Trung tâm (CLT — Central Limit Theorem):** Tổng (hoặc trung bình cộng) của một số lượng lớn các biến ngẫu nhiên độc lập có cùng phân phối (bất kể phân phối gốc là gì) sẽ có xu hướng hội tụ về **Phân phối Chuẩn** khi kích thước mẫu $n \to \infty$.

---

### §5.3 Tính Chất của Kỳ Vọng & Phương Sai
- **Tính chất Kỳ vọng (Tuyến tính):**
  $$\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$$
  $$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y] \quad (\text{ngay cả khi } X, Y \text{ không độc lập})$$
- **Tính chất Phương sai:**
  $$\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$
  $$\text{Var}(aX + b) = a^2 \text{Var}(X) \quad (\text{hằng số } b \text{ không làm thay đổi phương sai!})$$
  - Nếu $X$ và $Y$ **độc lập**:
    $$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y), \quad \text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y)$$
- **Ví dụ tính tay:** Cho $\mathbb{E}[X] = 5, \text{Var}(X) = 4$. Đặt $Y = 2X + 3$:
  $$\mathbb{E}[Y] = 2(5) + 3 = 13$$
  $$\text{Var}(Y) = 2^2 \text{Var}(X) = 4 \times 4 = 16$$

---

### §5.4 Ước Lượng Tham Số: MLE vs MAP
- **Maximum Likelihood Estimation (MLE):** Tìm tham số $\theta$ tối đa hóa hàm hợp lý của dữ liệu:
  $$\hat{\theta}_{\text{MLE}} = \arg\max_\theta P(\mathcal{D} \mid \theta) = \arg\max_\theta \sum_{i=1}^N \log P(x_i \mid \theta)$$
  $\implies$ Chỉ dựa hoàn toàn vào dữ liệu quan sát được, không sử dụng kiến thức tiên nghiệm.
- **Maximum A Posteriori (MAP):** Tìm tham số $\theta$ tối đa hóa xác suất hậu nghiệm kết hợp với phân phối tiên nghiệm (Prior) $P(\theta)$:
  $$\hat{\theta}_{\text{MAP}} = \arg\max_\theta P(\theta \mid \mathcal{D}) = \arg\max_\theta \left[ \log P(\mathcal{D} \mid \theta) + \log P(\theta) \right]$$
- **Mối liên hệ sâu sắc giữa MAP và Regularization:**
  - Nếu ta đặt tiên nghiệm là phân phối Chuẩn (Gaussian Prior) $\theta \sim \mathcal{N}(0, \sigma_0^2)$, thì $\log P(\theta) \propto -\frac{1}{2\sigma_0^2} \|\theta\|_2^2 \implies$ **Chính là Regularization L2 (Ridge Regression)**.
  - Nếu ta đặt tiên nghiệm là phân phối Laplace, thì $\log P(\theta) \propto -\lambda \|\theta\|_1 \implies$ **Chính là Regularization L1 (Lasso Regression)**.
- **⭐ Hay ra thi:** MAP chính là MLE được bổ sung thêm thành phần phạt Regularization thông qua Prior.

---

### §5.5 Kiểm Định Giả Thuyết Thống Kê & Bản Chất của p-value
- **Khái niệm:**
  - Giả thuyết vô hiệu $H_0$ (Null Hypothesis): Thường giả định không có sự khác biệt, không có hiệu ứng.
  - Giả thuyết đối $H_1$ (Alternative Hypothesis).
  - Mức ý nghĩa $\alpha$ (thường chọn $\alpha = 0.05$).
- **Bản chất thực sự của p-value:**
  $$p\text{-value} = P(\text{Quan sát dữ liệu cực đoan như thế hoặc hơn thế} \mid H_0 \text{ đúng})$$
  - Quy tắc quyết định: Nếu $p\text{-value} < \alpha$ (vd: $0.03 < 0.05$), ta **bác bỏ giả thuyết $H_0$** và chấp nhận $H_1$ ở mức ý nghĩa $5\%$.
- **⭐ Hay ra thi:**
  1. $p$-value **KHÔNG PHẢI** là xác suất giả thuyết $H_0$ đúng ($P(H_0 \mid \mathcal{D})$).
  2. $p$-value nhỏ chỉ cho biết dữ liệu không phù hợp với $H_0$, chứ **không đo lường độ lớn của hiệu ứng thực tế** (Effect Size).

---

### §5.6 Tương Quan vs Nhân Quả (Correlation vs Causation) & Kỹ Thuật Lấy Mẫu
- **Tương quan $\ne$ Nhân quả:** Hai biến $X$ và $Y$ tương quan mạnh không đồng nghĩa $X$ gây ra $Y$. Thường có sự tồn tại của **Yếu tố nhiễu ẩn (Confounding Variable)**.
  - Ví dụ: Doanh số bán kem tương quan thuận với số vụ đuối nước $\implies$ Yếu tố nhiễu chung là *Thời tiết nắng nóng mùa hè*.
- **Phương pháp lấy mẫu:**
  - **Random Sampling:** Lấy ngẫu nhiên đơn giản, có nguy cơ bỏ sót nhóm thiểu số.
  - **Stratified Sampling (Lấy mẫu phân tầng):** Chia quần thể thành các tầng theo thuộc tính phân loại rồi lấy mẫu sao cho giữ nguyên tỉ lệ các nhóm. Bắt buộc dùng khi đánh giá mô hình trên dữ liệu mất cân bằng.

---

## §6. Bảng 24 Bẫy Đề Thi Kinh Điển (Lỗi Hay Mắc: SAI $\to$ ĐÚNG)

| # | QUAN NIỆM SAI (BẪY ĐỀ THI) | KIẾN THỨC ĐÚNG | Mục lý thuyết |
|---|---|---|---|
| 1 | `BatchNorm` đặt sau hàm kích hoạt `ReLU` | Thứ tự chuẩn mực là: **Linear / Conv $\to$ BatchNorm $\to$ ReLU** | §2.8 |
| 2 | Bọc thêm `Softmax` trước `nn.CrossEntropyLoss` trong PyTorch | `CrossEntropyLoss` đã tích hợp sẵn `LogSoftmax` và `NLLLoss`, đầu vào bắt buộc là **Logit thô** | §2.4 |
| 3 | Thêm `Sigmoid` ở tầng cuối khi dùng `nn.BCEWithLogitsLoss` | `BCEWithLogitsLoss` đã chứa sẵn phép biến đổi sigmoid toán học, đầu vào phải là **Logit thô** | §2.4 |
| 4 | Thuật toán k-NN có giai đoạn cập nhật trọng số huấn luyện | k-NN là **Lazy Learner**, chỉ lưu dữ liệu vào bộ nhớ, không có pha huấn luyện tham số | §1.1 |
| 5 | Chỉ số $\text{IoU} = \frac{\text{Diện tích Giao}}{\text{Diện tích toàn ảnh}}$ | $\text{IoU} = \frac{\mathbf{Diện\ tích\ Giao}}{\mathbf{Diện\ tích\ Hợp}}$ của hai bounding box | §3.6 |
| 6 | Entropy trong cây quyết định sử dụng $\log$ cơ số $10$ hoặc $\ln$ | Luôn dùng **$\log_2$** trong lý thuyết thông tin, đơn vị là **bit** | §1.3 |
| 7 | Stable Diffusion là một biến thể nâng cấp của GAN | Stable Diffusion thuộc họ **Mô hình Khử nhiễu từng bước (Diffusion Model)**, không phải GAN | §3.8 |
| 8 | Gọi `optimizer.zero_grad()` sau khi đã tính `loss.backward()` | Phải gọi `zero_grad()` **TRƯỚC `loss.backward()`** vì gradient mặc định bị cộng dồn | §2.3 |
| 9 | Skip connection trong mạng U-Net là phép cộng phần tử (`ADD`) | U-Net dùng phép **ghép nối kênh (`CONCAT`)**; phép cộng `ADD` là của ResNet | §3.4 |
| 10 | Báo cáo Accuracy cao để chứng minh mô hình tốt trên dữ liệu lệch | Accuracy bị đánh lừa bởi lớp đa số; bắt buộc dùng **F1-Score, Precision, Recall, PR-AUC** | §1.7 |
| 11 | Khởi tạo toàn bộ ma trận trọng số bằng $0$ vẫn huấn luyện được | Gây ra **hiện tượng đối xứng (Symmetry)** khiến mọi neuron học y hệt nhau; phải dùng He hoặc Xavier | §2.7 |
| 12 | Giữ Dropout bật trong giai đoạn đánh giá / kiểm thử (Inference) | Phải tắt Dropout khi kiểm thử (`model.eval()`) để giữ kết quả ổn định và chính xác | §2.9 |
| 13 | So sánh khoảng cách các vector nhúng (Embeddings) bằng khoảng cách Euclid | Chuẩn trong NLP/Search là dùng **Cosine Similarity** (bỏ qua độ dài norm vector) | §4.3 |
| 14 | $p$-value là xác suất giả thuyết vô hiệu $H_0$ là đúng ($P(H_0)$) | $p$-value là xác suất thấy dữ liệu cực đoan như vậy giả định $H_0$ đúng ($P(\mathcal{D} \mid H_0)$) | §5.5 |
| 15 | Vision Transformer (ViT) dùng các bộ lọc tích chập $3 \times 3$ xếp chồng | ViT **hoàn toàn không dùng Convolution**, cắt ảnh thành patches và xử lý bằng Transformer Encoder | §3.5 |
| 16 | Tham số $\gamma$ của SVM RBF kernel càng lớn thì biên phân chia càng mượt | $\gamma$ càng lớn thì biên quyết định **càng cong ôm sát từng điểm dữ liệu $\implies$ Overfitting** | §1.2 |
| 17 | Regularization L1 (Lasso) chỉ làm co nhỏ độ lớn các trọng số | L1 có khả năng triệt tiêu trọng số về chính xác bằng 0 $\implies$ **Tạo tính thưa và chọn đặc trưng** | §1.6 |
| 18 | Dùng metric BLEU để đánh giá bài toán Tóm tắt văn bản | **BLEU dùng cho Dịch máy**; Tóm tắt văn bản định hướng Recall dùng **ROUGE** | §4.7 |
| 19 | Áp dụng Data Augmentation trên toàn bộ tập Train, Val và Test | **Tuyệt đối KHÔNG áp dụng Augmentation trên tập Validation và Test** | §3.9 |
| 20 | Trong Self-Attention không cần chia cho căn bậc hai $\sqrt{d_k}$ | Phải chia $\sqrt{d_k}$ để tránh tích vô hướng quá lớn làm hàm Softmax bị bão hòa gradient | §4.5 |
| 21 | Sử dụng mô hình BERT để sinh câu trả lời hoặc văn bản dài tự do | BERT học biểu diễn 2 chiều dùng cho **Hiểu văn bản (NLU)**; sinh văn bản tự hồi quy phải dùng **GPT** | §4.6 |
| 22 | Lớp Pooling (Max Pooling, Average Pooling) chứa tham số cần học | Lớp Pooling **hoàn toàn không có tham số học được (0 learnable parameters)** | §3.2 |
| 23 | Thuật toán SMOTE nhân bản y nguyên các mẫu của lớp thiểu số | SMOTE **nội suy điểm mới** ngẫu nhiên trên đoạn thẳng nối điểm thiểu số với láng giềng | §1.9 |
| 24 | Tính chất phương sai: $\text{Var}(aX + b) = a \cdot \text{Var}(X)$ | Đúng là: **$\text{Var}(aX + b) = a^2 \cdot \text{Var}(X)$** (hằng số cộng vào không đổi phương sai) | §5.3 |

---

## §7. Chuyên Đề Tác Vụ Thực Chiến OLP AI 2025 & 2026 (Khung 5 Bước Chuẩn)

### Khung 5 Bước Giải Pháp AI Vạn Năng:
1. **Bước 1: Phân tích Dữ liệu & Đặc thù Bài toán** (Cấu trúc dữ liệu, độ lệch lớp, rủi ro Data Leakage, ràng buộc phần cứng/độ trễ).
2. **Bước 2: Lựa chọn Mô hình (Baseline $\to$ SOTA) & Lý do** (Mô hình cơ sở đơn giản $\to$ Kiến trúc chính tối ưu, phân tích ưu nhược điểm).
3. **Bước 3: Pipeline Xử lý & Chiến lược Validation** (Tiền xử lý, Data Augmentation, chia Fold chống rò rỉ, hậu xử lý).
4. **Bước 4: Metric Đánh giá** (Chọn metric phù hợp với bản chất dữ liệu, không dùng Accuracy đơn thuần).
5. **Bước 5: Phương án Cải tiến & Tối ưu Thực tế** (Kỹ thuật nâng cao: Pretraining, Ensemble, Distillation, Quantization).

---

### §7.1 Tác vụ 1 (Đề OLP AI 2025): Nhận diện Ngôn Ngữ Ký Hiệu từ Video
- **Bối cảnh:** $10.000$ clip ngắn ghi lại $50$ cử chỉ ký hiệu, thu thập từ $100$ tình nguyện viên khác nhau trong điều kiện ánh sáng, góc quay và phông nền đa dạng. Yêu cầu chạy near real-time trên máy tính xách tay phổ thông.
- **Giải pháp 5 bước:**
  1. **Phân tích dữ liệu:** 
     - Dữ liệu dạng video chuỗi thời gian spatio-temporal. Mỗi video có số lượng frame biến thiên.
     - Rủi ro lớn nhất là **Data Leakage**: Nếu các frame của cùng một người xuất hiện ở cả Train và Val, mô hình sẽ học nhận diện khuôn mặt người thay vì học ký hiệu bàn tay.
     - Phân bố cử chỉ có thể không đồng đều giữa các lớp.
  2. **Lựa chọn mô hình:**
     - *Baseline:* Trích xuất đặc trưng từng frame độc lập bằng MobileNetV3 + trung bình trượt thời gian (Temporal Rolling Average).
     - *Mô hình chính:* Kết hợp trích xuất đặc trưng không gian nhẹ (ConvNeXt-Femto hoặc MediaPipe Holistic trích xuất 3D Landmark bàn tay/khớp) với mô hình mô hình hóa chuỗi thời gian như **Bi-directional GRU hoặc Temporal Transformer Encoder + Attention Pooling**.
  3. **Pipeline xử lý:**
     - Lấy mẫu cố định $T = 32$ frames cho mỗi video bằng uniform sampling.
     - Augmentation không gian (Random crop, color jitter) và thời gian (Time masking, thay đổi tốc độ khung hình $\pm 20\%$).
     - Chiến lược Validation: **Person-independent K-Fold (GroupKFold theo ID người thực hiện)**.
     - Huấn luyện với hàm mất mát **CTC Loss (Connectionist Temporal Classification)** hoặc Cross-Entropy sau Temporal Pooling.
  4. **Metric đánh giá:**
     - **Sequence-level Accuracy** (đoán đúng toàn bộ ký hiệu), **Word Error Rate (WER)** và Top-5 Accuracy.
     - Tuyệt đối không tính Accuracy trung bình trên từng frame đơn lẻ.
  5. **Phương án cải tiến:**
     - Tận dụng tọa độ Landmark từ MediaPipe để giảm chiều không gian từ ảnh điểm ảnh về vector khớp xương $\implies$ Tăng tốc độ $10\times$.
     - Knowledge Distillation từ mô hình lớn sang mô hình nhỏ; Lượng tử hóa INT8 bằng ONNX Runtime để đạt 30+ FPS trên CPU.

---

### §7.2 Tác vụ 2 (Đề OLP AI 2025): Dịch Máy Thương Mại Điện Tử Hoa — Việt
- **Bối cảnh:** $200.000$ cặp câu song ngữ chuyên ngành thương mại điện tử (E-Commerce). Yêu cầu dịch chính xác tên thuộc tính sản phẩm và **tuyệt đối không làm sai lệch số lượng, đơn vị đo lường và mệnh giá tiền tệ**.
- **Giải pháp 5 bước:**
  1. **Phân tích dữ liệu:**
     - Cặp câu bất đối xứng: Tiếng Trung viết liền không dấu cách, mật độ thông tin cao; Tiếng Việt nhiều từ ghép đa âm tiết.
     - Chứa nhiều thuật ngữ viết tắt, mã hiệu model sản phẩm, giá tiền ($¥$, VND), số đo ($cm, kg$).
  2. **Lựa chọn mô hình:**
     - *Baseline:* Seq2Seq GRU 2 lớp với Luong Attention.
     - *Mô hình chính:* **Transformer tiêu chuẩn (6 Encoder layers, 6 Decoder layers)** hoặc Fine-tune từ mô hình dịch máy đa ngữ tiền huấn luyện nguồn mở mạnh như **NLLB-200 (No Language Left Behind) hoặc mBART-50**.
  3. **Pipeline xử lý:**
     - Tách từ chuyên biệt: Dùng Jieba/pkuseg cho tiếng Trung, VnCoreNLP cho tiếng Việt.
     - Huấn luyện bộ mã hóa Subword BPE (Byte-Pair Encoding) chung với kích thước từ điển $32.000$ tokens.
     - **Quy tắc bảo vệ số/tiền tệ:** Dùng Regular Expressions thay thế các giá trị số, mã model bằng placeholder (vd: `<NUM_1>`, `<CURR_VND>`) trước khi dịch, sau đó đối ánh xạ ngược lại vào câu dịch tiếng Việt.
     - Giải mã: **Beam Search (Beam Width = 5)** kết hợp **Label Smoothing = 0.1**.
  4. **Metric đánh giá:**
     - **SacreBLEU** (chuẩn hóa tokenization) và **chrF++** (độ đo dựa trên mức ký tự, rất nhạy với lỗi chính tả tiếng Việt).
     - Đánh giá thủ công (Human Evaluation) trên tập $200$ câu thử nghiệm đặc thù chứa nhiều thông số kỹ thuật và tiền tệ.
  5. **Phương án cải tiến:**
     - **Back-translation:** Dịch ngược dữ liệu đơn ngữ tiếng Việt sang tiếng Trung để nhân đôi tập dữ liệu huấn luyện.
     - Reranking kết quả Beam Search bằng mô hình ngôn ngữ tiếng Việt tiền huấn luyện (PhoBERT).

---

### §7.3 Tác vụ 3 (Đề xuất 2026): Phát Hiện Bệnh Lá Cây Trồng Trên Thiết Bị Di Động
- **Bối cảnh:** $8.000$ ảnh chụp lá cây ngoài ruộng thực tế, $4$ nhóm bệnh (trong đó $2$ nhóm bệnh hiếm). Yêu cầu phát hiện khoanh vùng chính xác vị trí vết bệnh và vận hành mượt mà trên ứng dụng di động của người nông dân.
- **Giải pháp 5 bước:**
  1. **Phân tích dữ liệu:**
     - Bài toán Object Detection ngoài thực địa: Phông nền đất ruộng và bóng râm rất phức tạp.
     - Mất cân bằng lớp nghiêm trọng giữa các bệnh phổ biến và bệnh hiếm.
     - Ràng buộc: Thiết bị di động giá rẻ, không có kết nối internet $\implies$ Dung lượng mô hình $< 20\text{ MB}$, độ trễ $< 50\text{ ms}$.
  2. **Lựa chọn mô hình:**
     - *Baseline:* EfficientNet-B0 làm bộ phân loại toàn ảnh (không khoanh vùng).
     - *Mô hình chính:* **YOLOv8n (Nano) hoặc YOLOv11n**. Kiến trúc 1-stage với số lượng tham số chỉ khoảng $3\text{ triệu}$, tối ưu hóa cao cho các bộ xử lý di động NPU/GPU.
  3. **Pipeline xử lý:**
     - Augmentation phong phú: Mosaic, Random HSV, Flip, Random Rotate.
     - Validation: **GroupKFold theo thửa ruộng và ngày chụp ảnh** để tránh trùng lặp điều kiện ánh sáng.
     - Xử lý mất cân bằng: Áp dụng **Focal Loss** để giảm ảnh hưởng của các vùng nền dễ phát hiện, tập trung vào các vết bệnh nhỏ và hiếm.
  4. **Metric đánh giá:**
     - $\text{mAP@0.5}$ và $\text{mAP@[0.5:0.95]}$.
     - Báo cáo riêng Precision và Recall cho $2$ lớp bệnh hiếm.
  5. **Phương án cải tiến:**
     - Test-Time Augmentation (TTA) khi người dùng chụp ảnh ở chế độ chất lượng cao.
     - Xuất mô hình sang định dạng **TFLite / ONNX và lượng tử hóa số nguyên Post-Training Quantization (INT8)** giúp giảm $4\times$ dung lượng và tăng tốc $3\times$ trên điện thoại.

---

### §7.4 Tác vụ 4 (Đề xuất 2026): Dự Đoán Sinh Viên Bỏ Học & Giải Thích Quyết Định (XAI)
- **Bối cảnh:** Dữ liệu dạng bảng gồm $50.000$ sinh viên với $40$ trường thông tin (điểm học phần, số tín chỉ trễ, tình trạng đóng học phí, điểm rèn luyện). Tỉ lệ sinh viên bỏ học là $8\%$. Phòng đào tạo cần mô hình dự đoán chính xác và **giải thích được nguyên nhân cụ thể cho từng sinh viên** để cố vấn học tập kịp thời can thiệp.
- **Giải pháp 5 bước:**
  1. **Phân tích dữ liệu:**
     - Dữ liệu dạng bảng (Tabular Data) với $8\%$ nhãn dương (Imbalanced Data).
     - Chứa cả biến định lượng liên tục (GPA, học phí) và biến phân loại danh mục (ngành học, khu vực).
     - Yêu cầu nghiệp vụ bắt buộc: Tính minh bạch và khả năng giải thích (Explainability / XAI).
  2. **Lựa chọn mô hình:**
     - *Baseline:* Logistic Regression (sau khi chuẩn hóa StandardScaler).
     - *Mô hình chính:* **LightGBM hoặc XGBoost**. Hiệu năng vượt trội trên dữ liệu dạng bảng, xử lý tự nhiên các tương tác phi tuyến và giá trị khuyết, không cần Deep Learning phức tạp.
  3. **Pipeline xử lý:**
     - Missing Value: Điền trung vị (Median) cho biến số, tạo nhãn `Missing` riêng cho biến phân loại.
     - Feature Engineering: Tạo các đặc trưng vi phân biểu thị xu hướng: $\Delta \text{GPA} = \text{GPA}_{\text{kỳ này}} - \text{GPA}_{\text{kỳ trước}}$, tỉ lệ tín chỉ rớt $/ \text{tín chỉ đăng ký}$.
     - Validation: **Stratified 5-Fold Cross Validation**.
     - Xử lý lệch lớp: Thiết lập tham số `scale_pos_weight = (50000 - 4000) / 4000 = 11.5`.
     - Tối ưu ngưỡng cắt xác suất (Threshold Tuning) dựa trên việc tối đa hóa chỉ số F1-Score hoặc hàm chi phí thực tế.
  4. **Metric đánh giá:**
     - **PR-AUC (Precision-Recall AUC)** và **F1-Score**.
     - Ma trận chi phí (Cost Matrix): Phạt nặng chi phí khi bỏ lọt sinh viên bỏ học ($FN$) so với báo động nhầm ($FP$).
  5. **Phương án cải tiến & Giải thích mô hình:**
     - Tích hợp **SHAP (SHapley Additive exPlanations)**:
       - Giải thích toàn cục (Global Importance): Xác định top các nguyên nhân hàng đầu dẫn đến nguy cơ bỏ học trên toàn trường.
       - Giải thích cục bộ (Local Waterfall Plot): Vẽ đồ thị đóng góp của từng chỉ số cho một sinh viên cụ thể gửi trực tiếp cho cố vấn học tập để lên kế hoạch hỗ trợ phù hợp.

---
*Bản quyền tài liệu ôn thi OLP AI HCMUS 2026. Chúc các bạn thi đạt giải cao!*
