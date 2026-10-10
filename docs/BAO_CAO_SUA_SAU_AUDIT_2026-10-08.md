# BÁO CÁO TỔNG KẾT & NGHIỆM THU SAU KIỂM TOÁN HỌC THUẬT
## KỲ THI OLYMPIC AI HCMUS 2026 — VÒNG TRƯỜNG THI CÁ NHÂN (11/10/2026)

> **Thời điểm cập nhật lần 5 (Nghiệm thu toàn diện sau rà soát Lần 4):** 10:45:00, ngày 09/10/2026  
> **Căn cứ đặc tả & phản biện:** Thực thi trọn vẹn 5 yêu cầu từ danh mục rà soát `docs/VERIFY_BAO_CAO_LAN_4_2026-10-09.md`: Đọc prompt câu đích thật của từng ID liên hệ; sửa định nghĩa p-value chuẩn theo tuyên bố chính thức của ASA (không dùng P(Data|H0)); sinh lại Markdown Đề 02 và HTML Study Hub đồng bộ 100%; viết lại bảng 60 câu đối chiếu trực tiếp từ JSON thật khớp chuẩn heading giáo trình; báo cáo PASS kỹ thuật đúng phạm vi và giữ nguyên nhãn UNVALIDATED cho độ sát đề VOAI 2025 mã 006.  
> **Trạng thái kiểm tra kỹ thuật:** **PASS 100% TẤT CẢ CÁC CỔNG KIỂM TRA TỰ ĐỘNG** (`validate.mjs`, `vitest` 18/18 tests, `test_html_logic.mjs` 5 suite sandbox, `tsc --noEmit` 0 errors, `audit_quality.py` 184/184 câu, `audit_katex_syntax.mjs` 2.689 snippets).  
> **Phạm vi & Giới hạn của PASS kiểm toán:** Kết quả PASS từ các script xác nhận tính toàn vẹn cấu trúc (đủ trường, đủ khối ELI5/Luận chứng/Bẫy/Căn cứ), cú pháp toán học KaTeX hợp lệ không ngoại lệ render, và sự tồn tại hợp lệ của các tham chiếu ID/§; **không tự động thay thế cho việc thẩm định toàn diện từng lập luận học thuật hay việc luyện tập thực tế của thí sinh**.  
> **Độ sát đề thi chính thức VOAI 2025 mã 006:** **`UNVALIDATED`** (Bộ đề 02 và Đề 03 là đề biên soạn mô phỏng cấu trúc và mở rộng học thuật dựa trên bài giảng ôn tập và đề mẫu SOLOAI/Đỗ Đình Luật; chưa được đối chiếu thực tế với mã đề gốc 006 thời lượng 180 phút của BTC).

---

## 1. TỔNG QUAN TIẾN ĐỘ & BẢNG THỐNG KÊ CẤU TRÚC ĐỀ THI

### 1.1 Thống kê chuẩn xác 3 Đề thi (Tổng cộng 184 câu)
- **Đề 01 (`olp-01.json`)**: Tổng 64 câu.
  - Phân loại: **58 câu trắc nghiệm (MCQ) + 2 câu bài tập lập trình (Code)** = 60 câu graded (thang điểm 100đ).
  - Tự luận: **4 bài tự luận chuyên sâu** (thang điểm 40đ, tự chấm theo rubric 5 bước riêng biệt).
  - Phân bố đáp án graded: A=15 (25.0%), B=15 (25.0%), C=14 (23.3%), D=14 (23.3%).
- **Đề 02 (`olp-02.json`)**: Tổng 66 câu.
  - Phân loại: **60 câu trắc nghiệm (MCQ)** = 60 câu graded (thang điểm 90đ, 1.5đ/câu).
  - Tự luận: **6 bài tự luận thiết kế giải pháp AI thực chiến** (thang điểm 60đ, tự chấm theo rubric 5 bước riêng biệt).
  - Phân bố đáp án graded: A=20 (33.3%), B=8 (13.3%), C=13 (21.7%), D=19 (31.7%).
- **Đề 03 (`olp-03.json`)**: Tổng 54 câu.
  - Phân loại: **50 câu trắc nghiệm (MCQ)** = 50 câu graded (thang điểm 100đ, 2.0đ/câu).
  - Tự luận: **4 bài tự luận chuyên đề thực hành AI** (thang điểm 40đ, tự chấm theo rubric 5 bước riêng biệt).
  - Phân bố đáp án graded: A=17 (34.0%), B=10 (20.0%), C=14 (28.0%), D=9 (18.0%).
- **Tổng toàn hệ thống**: 170 câu graded tính điểm + 14 bài tự luận e2e = 184 câu hỏi.

### 1.2 Bảng so sánh trước và sau đợt rà soát ngày 09/10/2026

| Tiêu chí rà soát | Tình trạng trước sửa (08/10) | Sau sửa chữa toàn diện Lần 5 (09/10) | Trạng thái nghiệm thu |
| :--- | :--- | :--- | :--- |
| **Bảng Enrichment Đề 02 (M01-M60)** | Lệch chủ đề P0 (M05 Hessian bị gán SVD; M13 k-NN bị gán Linear Reg; M49 NLP bị gán Causal mask) | Viết lại 100% từ điển `enrich_olp02_terms_and_links.py` khớp 1:1 nội dung thực của 60 câu hỏi từ JSON gốc | **PASS 100%** (Đã xác thực trên UI browser live) |
| **Đích liên hệ câu cũ (Khối 4)** | Nhiều câu dẫn sang câu đích khác chủ đề (M05 dẫn Poisson, M13 dẫn Conv2D, M49 dẫn YOLO, M51 dẫn Silhouette) | Đọc prompt câu đích thật của từng ID; đổi sang câu cùng chủ đề thật (M05 -> VOAI03-M02, M13 -> OLP01-C01, M49 -> OLP01-C28, M51 -> OLP01-B09, M59 -> VOAI03-M23, M60 -> VOAI03-M30); các câu đặc thù ghi rõ là câu độc lập | **PASS 100%** (Học thuật minh bạch, không liên hệ giả) |
| **Định nghĩa p-value (M03)** | Định nghĩa cũ dùng sai biểu thức $P(\text{Data} \mid H_0)$ | Chuẩn hóa theo Tuyên bố chính thức của ASA (2016): xác suất thống kê kiểm định cực đoan bằng hoặc hơn quan sát dưới $H_0$ | **PASS 100%** (Chuẩn xác toán học) |
| **Bảng 60 câu trong báo cáo** | Bảng cũ tự sinh nhầm chủ đề (M01 ma trận đối xứng trong khi JSON là Bayes) | Sinh tự động 100% từ JSON thật, khớp đúng số và tên § với heading giáo trình `01-ly-thuyet-olp-ai.md` | **PASS 100%** (Khớp dữ liệu thật) |
| **Công cụ Audit Chất lượng & KaTeX** | Quét sơ lược, chưa phân tách MCQ vs Essay, chưa quét toàn văn giáo trình và bảng công thức | Nâng cấp `audit_quality.py` (check 4 khối MCQ, rubric/modelAnswer Essay, tồn tại § và ID liên hệ) & `audit_katex_syntax.mjs` (quét 2.689 đoạn toán) | **PASS 100%** (0 lỗi cú pháp KaTeX, exit code 0) |
| **Cẩm nang PDF (`olp_ai_handbook_2026.pdf`)** | Nêu khuyên dùng NLLB/mBART làm lệch quy chế SOLOAI; trích dẫn TabM chưa ghi rõ hội nghị | Sửa TeX: Nêu rõ quy chế SOLOAI cấm pretrained NMT; TabM trích dẫn ICLR 2025; biên dịch XeLaTeX 45 trang, 0 lỗi | **PASS 100%** (Đã đồng bộ sang docs, dist, public) |
| **Trình phát Video Bài giảng trên Web** | Bấm xem video chỉ mở tab mới ra YouTube ngoài | Tích hợp Inline Embedded Video Player 16:9 với `autoplay=1&start={sec}` ngay trên Web Hub | **PASS 100%** (Đã kiểm chứng CDP screenshot) |
| **Tính minh bạch học thuật** | Dùng từ ngữ gây hiểu lầm là đề gốc VOAI 2025 mã 006 | Đính chính rõ ràng là đề biên soạn mô phỏng cấu trúc; gắn nhãn `UNVALIDATED` với mã đề gốc 006 | **PASS 100%** (Minh bạch khoa học) |

---

## 2. BẢNG ĐỐI CHIẾU CHI TIẾT 60 CÂU ĐỀ 02 (M01 – M60) TRÍCH XUẤT TỪ JSON THẬT

Bảng dưới đây được **trích xuất tự động trực tiếp từ dữ liệu thực tế** của file `src/data/exams/olp-02.json`, đối chiếu với toàn bộ ngân hàng câu hỏi `olp-01.json` và `olp-03.json`, đồng thời khớp chuẩn xác số và tên mục § trong giáo trình `content/01-ly-thuyet-olp-ai.md`:

| Mã câu | Đầu prompt nguồn Đề 02 | Chủ đề toán học / AI | Mục giáo trình § | ID đích | Đầu prompt câu đích | Lý do liên quan học thuật |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- |
| **VOAI02-M01** | Một căn bệnh hiếm gặp có tỉ lệ mắc trong cộng đồng là $P(D) = 0.5... | Base Rate (Tỉ lệ nền / Xác suất tiên nghiệm) | §5.1 Định Lý Bayes & Bài Toán Chẩn Đoán Y Tế (Base-Rate Fallacy) | **OLP01-A01** | Một căn bệnh có tỉ lệ mắc trong cộng đồng là 2%. M... | Cùng kiểm tra nghịch lý tỉ lệ nền (Base-Rate Fallacy) trong xét nghiệm y tế: OLP01-A01 tính xác suất có bệnh khi test dương tính với $P(D)=2\%$, còn M01 kiểm tra với $P(D)=0.5\%$. |
| **VOAI02-M02** | Cho biến ngẫu nhiên rời rạc $X \sim \text{Binomial}(n = 20, p = 0... | Binomial Distribution (Phân phối nhị thức) | §5.2 Các Phân Phối Xác Suất Quan Trọng | **OLP01-A03** | Cho biến ngẫu nhiên rời rạc $X \sim \text{Bernoull... | Phân phối nhị thức $\text{Binomial}(n, p)$ trong M02 chính là tổng của $n$ biến ngẫu nhiên $\text{Bernoulli}(p)$ độc lập trong OLP01-A03, kế thừa công thức kỳ vọng $n p$ và phương sai $n p (1-p)$. |
| **VOAI02-M03** | Trong một nghiên cứu A/B Testing đánh giá thuật toán gợi ý mới, g... | Giả thuyết không ($H_0$) | §5.5 Kiểm Định Giả Thuyết Thống Kê & Bản Chất của p-value | **Độc lập** | N/A (Chuyên đề độc lập) | Đây là câu hỏi độc lập chuyên sâu trong ngân hàng đề kiểm tra trực tiếp định nghĩa chuẩn tắc của $p$-value và quy tắc ra quyết định trong A/B testing: $p$-value là xác suất của thống kê kiểm định cực đoan bằng hoặc hơn quan sát được dưới $H_0$ (theo Tuyên bố chính thức của Hiệp hội Thống kê Hoa Kỳ ASA), không phải $P(\text{Data} \mid H_0)$ hay $P(H_0 \mid \text{Data})$. |
| **VOAI02-M04** | Cho ma trận dữ liệu đã chuẩn hóa chuẩn (zero-mean) $X \in \mathbb... | PCA (Principal Component Analysis) | §1.10 Tiền xử lý Đặc trưng & Thao tác NumPy | **VOAI03-M32** | Điểm vượt trội của thuật toán t-SNE so với PCA khi... | Cùng thuộc chuyên đề giảm chiều dữ liệu: M04 phân tích cơ sở toán học tuyến tính của PCA (trục chiếu theo vector riêng của ma trận hiệp phương sai), còn VOAI03-M32 so sánh PCA với phương pháp giảm chiều phi tuyến t-SNE. |
| **VOAI02-M05** | Cho hàm số hai biến $f(x, y) = x^2 - 4xy + y^3$. Điểm dừng $P_0(0... | Ma trận Hessian ($H = \nabla^2 f(x, y)$) | §2.3 Lan truyền xuôi, Lan truyền ngược & Vòng lặp Huấn luyện PyTorch | **VOAI03-M02** | Trong tối ưu hóa đa biến, nếu ma trận Hessian $H =... | Cùng kiểm tra việc dùng ma trận Hessian để xác định tính chất điểm dừng trong tối ưu hóa: VOAI03-M02 kiểm tra trường hợp Hessian xác định dương ($\det > 0, f_{xx} > 0 \implies$ cực tiểu địa phương), còn M05 kiểm tra trường hợp Hessian bất định ($\det(H) < 0 \implies$ điểm yên ngựa). |
| **VOAI02-M06** | Cho vector logit $z = [z_1, z_2, \dots, z_C]^T$, xác suất dự đoán... | Softmax Function | §2.4 Các hàm mất mát (Loss Functions) | **OLP01-B11** | Khi sử dụng hàm mất mát `torch.nn.CrossEntropyLoss... | M06 giải thích về mặt giải tích gradient $\frac{\partial L}{\partial z_i} = p_i - y_i$ của Softmax kết hợp Cross-Entropy, bổ trợ trực tiếp cho OLP01-B11 về lý do vì sao trong PyTorch ta đưa raw logits trực tiếp vào `nn.CrossEntropyLoss()`. |
| **VOAI02-M07** | Khoảng cách Mahalanobis giữa hai điểm $u, v \in \mathbb{R}^D$ đượ... | Khoảng cách Mahalanobis | §1.8 K-Means Clustering & Silhouette Score | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi lý thuyết độc lập mở rộng về khoảng cách trong không gian đặc trưng đa biến có tương quan: khi ma trận hiệp phương sai là ma trận đơn vị ($\Sigma = I$), khoảng cách Mahalanobis trở về đúng khoảng cách Euclid dùng trong thuật toán K-Means (§1.8). |
| **VOAI02-M08** | Trong học máy, việc tối đa hóa hàm hợp lý hậu nghiệm (Maximum A P... | MLE (Maximum Likelihood Estimation) | §5.4 Ước Lượng Tham Số: MLE vs MAP | **OLP01-C09** | Điểm khác biệt cốt lõi về mặt toán học và ứng dụng... | OLP01-C09 phân tích L1 vs L2 dưới góc độ điều chuẩn hình học trong học máy, còn M08 giải thích nguồn gốc xác suất Bayes của chúng: L2 tương ứng với tiên nghiệm Gauss, L1 tương ứng với tiên nghiệm Laplace trong ước lượng MAP. |
| **VOAI02-M09** | Cho hai phân phối xác suất rời rạc $P$ và $Q$ trên cùng không gia... | KL Divergence ($D_{KL}(P \parallel Q)$) | §2.4 Các hàm mất mát (Loss Functions) | **VOAI03-M04** | Đại lượng nào trong lý thuyết thông tin đo lường m... | Cùng thuộc lý thuyết thông tin: VOAI03-M04 đo độ hỗn loạn nội tại của phân phối qua Shannon Entropy $H(P)$, còn M09 đo độ lệch tương đối giữa hai phân phối qua Phân kỳ KL $D_{KL}(P \parallel Q) = H(P, Q) - H(P)$. |
| **VOAI02-M10** | Hàm kích hoạt SiLU (Sigmoid Linear Unit / Swish) được định nghĩa ... | SiLU (Sigmoid Linear Unit / Swish) | §2.2 Các hàm kích hoạt (Activation Functions) | **OLP01-C20** | Trong thiết kế mạng nơ-ron sâu hiện đại, lựa chọn ... | Cùng kiểm tra các hàm kích hoạt hiện đại: OLP01-C20 khẳng định SiLU/GELU vượt trội hơn ReLU trong Transformer và mạng sâu, còn M10 đi sâu vào công thức giải tích $f(x) = x \cdot \sigma(x)$ và tính chất không đơn điệu của SiLU. |
| **VOAI02-M11** | Cho $Q \in \mathbb{R}^{n \times n}$ là một ma trận trực giao (ort... | Ma trận trực giao (Orthogonal Matrix) | §1.10 Tiền xử lý Đặc trưng & Thao tác NumPy | **VOAI03-M01** | Cho ma trận vuông $A$ kích thước $n \times n$. Nếu... | Cùng kiểm tra định nghĩa và tính chất của ma trận trực giao: cả hai câu đều khẳng định ma trận trực giao bảo toàn tích vô hướng và độ dài vector Euclid ($A^T A = I \implies \\|A x\\| = \\|x\\|$). |
| **VOAI02-M12** | Khi cần tính xấp xỉ kỳ vọng $\mathbb{E}_{x \sim P}[f(x)]$ nhưng v... | Importance Sampling | §5.6 Tương Quan vs Nhân Quả (Correlation vs Causation) & Kỹ Thuật Lấy Mẫu | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi độc lập nâng cao về kỹ thuật lấy mẫu Monte Carlo và xấp xỉ kỳ vọng toán học khi không thể lấy mẫu trực tiếp từ phân phối mục tiêu $P(x)$ (§5.6). |
| **VOAI02-M13** | Vì sao thuật toán k-Nearest Neighbors (k-NN) được xếp vào nhóm 'L... | k-NN (k-Nearest Neighbors) | §1.1 k-NN (k-Nearest Neighbors — Lazy Learner) | **OLP01-C01** | Thuật toán k-NN (k-Nearest Neighbors) được xếp vào... | Cùng kiểm tra bản chất Lazy Learner của k-NN: OLP01-C01 tập trung vào đặc điểm không học trọng số ở pha huấn luyện, còn M13 phân tích sâu thêm độ phức tạp tính toán suy luận $O(N \cdot D)$ khi phải quét toàn bộ tập dữ liệu. |
| **VOAI02-M14** | Trong thuật toán Soft-Margin SVM, hàm mục tiêu tối thiểu hóa là $... | Soft-Margin SVM | §1.2 Support Vector Machines (SVM & Kernel Trick) | **OLP01-C03** | Trong thuật toán Support Vector Machine (SVM) tuyế... | Cùng kiểm tra lý thuyết lề trong SVM: OLP01-C03 xem xét Hard-Margin nguyên bản, còn M14 phân tích mối liên hệ khi siêu tham số phạt $C \to \infty$ của Soft-Margin sẽ tiệm cận về đúng bài toán Hard-Margin. |
| **VOAI02-M15** | Kernel RBF (Radial Basis Function / Gaussian Kernel) trong SVM có... | Kernel RBF (Radial Basis Function / Gaussian) | §1.2 Support Vector Machines (SVM & Kernel Trick) | **OLP01-C04** | Khi sử dụng SVM với hàm nhân RBF (Radial Basis Fun... | Cùng phân tích hành vi của siêu tham số $\gamma$ trong RBF Kernel: giá trị $\gamma$ quá lớn làm thu hẹp bán kính ảnh hưởng của từng Support Vector, tạo các ranh giới cục bộ gây Overfitting nghiêm trọng. |
| **VOAI02-M16** | Tại một nút lá của bài toán phân loại nhị phân ($K = 2$), tỉ lệ m... | Gini Impurity ($I_G$) | §1.3 Cây quyết định (Decision Tree), Entropy & Information Gain | **OLP01-B04** | Một nút (node) trong cây quyết định đang chứa 8 mẫ... | Cùng thuộc bài toán đo độ hỗn loạn của nút trong cây quyết định: OLP01-B04 tính độ đo Entropy Shannon ($-\sum p_i \log_2 p_i$), còn M16 tính độ đo Gini Impurity ($1 - \sum p_i^2$) dùng trong thuật toán CART. |
| **VOAI02-M17** | Trong thuật toán Random Forest, mỗi cây con được xây dựng trên mộ... | Bootstrap Sampling | §1.4 Random Forest & Phương pháp Ensemble | **OLP01-C17** | Vì sao mô hình Rừng ngẫu nhiên (Random Forest) có ... | OLP01-C17 giải thích khả năng giảm phương sai của Random Forest nhờ cơ chế Bagging, còn M17 chứng minh bằng toán học xác suất tỉ lệ $\approx 36.8\%$ dữ liệu OOB đóng vai trò như tập kiểm thử độc lập cho từng cây con. |
| **VOAI02-M18** | Trong thuật toán AdaBoost phân loại nhị phân ($y_i \in \{-1, +1\}... | AdaBoost (Adaptive Boosting) | §1.4 Random Forest & Phương pháp Ensemble | **VOAI03-M41** | Điểm khác biệt cốt lõi nhất giữa phương pháp Baggi... | VOAI03-M41 phân biệt Bagging (song song) và Boosting (tuần tự), còn M18 phân tích sâu công thức toán học cập nhật trọng số mẫu trong thuật toán nền tảng AdaBoost giúp các cây sau tập trung sửa sai cho các cây trước. |
| **VOAI02-M19** | Khác biệt cốt lõi trong thuật toán tối ưu hóa giữa Gradient Boost... | Gradient Boosting truyền thống (GBM) | §1.4 Random Forest & Phương pháp Ensemble | **VOAI03-M48** | Thuật toán Gradient Boosting xây dựng các cây quyế... | VOAI03-M48 kiểm tra nguyên lý Gradient Boosting truyền thống khớp cây con vào đạo hàm bậc 1, còn M19 phân tích bước tiến của XGBoost khi tối ưu hóa hàm mục tiêu bằng khai triển Taylor bậc hai ($g_i$ và $h_i$). |
| **VOAI02-M20** | LightGBM đạt tốc độ huấn luyện vượt trội trên các tập dữ liệu lớn... | GOSS (Gradient-based One-Side Sampling) | §1.4 Random Forest & Phương pháp Ensemble | **VOAI03-M43** | Thuật toán LightGBM sử dụng chiến lược phát triển ... | Cùng tìm hiểu các cải tiến hiệu năng của thư viện LightGBM: VOAI03-M43 kiểm tra chiến lược mọc cây theo lá (Leaf-wise), còn M20 kiểm tra 2 kỹ thuật xử lý dữ liệu đột phá GOSS (lọc mẫu theo gradient) và EFB (gộp đặc trưng loại trừ). |
| **VOAI02-M21** | Khi mã hóa biến phân loại (Categorical Features) bằng Target Enco... | Target Encoding | §1.10 Tiền xử lý Đặc trưng & Thao tác NumPy | **VOAI03-M49** | Trong CatBoost, kỹ thuật 'Ordered Boosting' được t... | Cùng kiểm tra cơ chế chống rò rỉ nhãn (Target Leakage) độc quyền của thuật toán CatBoost: nguyên lý Ordered Target Encoding / Ordered Boosting dựa trên việc bảo toàn thứ tự thời gian giả lập. |
| **VOAI02-M22** | Khi áp dụng kỹ thuật sinh mẫu nhân tạo SMOTE (Synthetic Minority ... | SMOTE | §1.9 Xử lý Mất cân bằng lớp (Imbalanced Data) | **VOAI03-M35** | Kỹ thuật SMOTE (Synthetic Minority Over-sampling T... | VOAI03-M35 kiểm tra nguyên lý thuật toán SMOTE, còn M22 kiểm tra quy trình thực hành chuẩn để ngăn chặn thảm họa rò rỉ dữ liệu (Data Leakage) khi kết hợp SMOTE với Cross-Validation. |
| **VOAI02-M23** | Trong bài toán phân tích cụm không gian biểu diễn (Representation... | K-Means | §1.8 K-Means Clustering & Silhouette Score | **OLP01-C18** | Khi đánh giá chất lượng phân cụm của thuật toán K-... | Cùng thuộc chủ đề học không giám sát phân cụm dữ liệu: OLP01-C18 đánh giá cụm K-Means bằng Silhouette Score, còn M23 so sánh hạn chế cụm hình cầu của K-Means với thuật toán phân cụm mật độ HDBSCAN. |
| **VOAI02-M24** | Khi xây dựng mô hình dự báo chuỗi thời gian (ví dụ: dự báo giá cổ... | Dữ liệu chuỗi thời gian (Time Series) | §1.5 Overfitting, Underfitting, Bias-Variance Tradeoff & Cross-Validation | **VOAI03-M50** | Tại sao việc áp dụng K-Fold Cross-Validation thông... | Cùng kiểm tra nguyên lý kiểm chuẩn mô hình chuỗi thời gian: cả hai câu đều khẳng định K-Fold xáo trộn ngẫu nhiên phá vỡ tính liên tục thời gian và gây Data Leakage nghiêm trọng; bắt buộc phải chia theo trục thời gian xuôi (Rolling-window / TimeSeriesSplit). |
| **VOAI02-M25** | Trong PyTorch, đoạn mã nào sau đây biểu diễn **ĐÚNG VÀ ĐẦY ĐỦ** t... | `optimizer.zero_grad()` | §2.3 Lan truyền xuôi, Lan truyền ngược & Vòng lặp Huấn luyện PyTorch | **OLP01-B13** | Trong một vòng lặp huấn luyện PyTorch tiêu chuẩn c... | Cùng kiểm tra thứ tự 4 thao tác cốt lõi trong vòng lặp huấn luyện PyTorch; giải thích bản chất vì sao phải xóa gradient tích lũy trước khi lan truyền ngược. |
| **VOAI02-M26** | Nếu khởi tạo tất cả các trọng số $W$ của một mạng nơ-ron sâu bằng... | Symmetry Problem (Vấn đề đối xứng) | §2.7 Khởi tạo Trọng số (Weight Initialization) | **OLP01-B14** | Khi khởi tạo trọng số cho các tầng ẩn sử dụng hàm ... | Cùng kiểm tra chiến lược khởi tạo trọng số mạng sâu: OLP01-B14 chọn phương pháp He Normal/Uniform cho ReLU, còn M26 giải thích thêm nguy cơ phá vỡ tính phân hóa của nơ-ron khi khởi tạo bằng 0. |
| **VOAI02-M27** | Trong lớp Batch Normalization (`nn.BatchNorm2d`), sự khác biệt că... | BatchNorm pha Train (`model.train()`) | §2.8 Chuẩn hóa Tầng (Batch Normalization vs Layer Normalization) | **OLP01-B10** | Trong thiết kế khối mạng nơ-ron tích chập (Conv Bl... | Cùng kiểm tra cơ chế hoạt động của lớp Batch Normalization trong PyTorch: phân biệt sự khác nhau căn bản giữa thống kê batch tức thời lúc train và thống kê tích lũy running stats lúc eval. |
| **VOAI02-M28** | Vì sao các kiến trúc Transformer và mô hình xử lý chuỗi ngôn ngữ ... | Batch Normalization (BN) | §2.8 Chuẩn hóa Tầng (Batch Normalization vs Layer Normalization) | **OLP01-C21** | Vì sao trong các kiến trúc Transformer và mô hình ... | Cùng phân tích nguyên nhân LayerNorm là chuẩn mực trong NLP: chuẩn hóa độc lập theo từng mẫu trên chiều đặc trưng (feature dimension), hoàn toàn không phụ thuộc vào kích thước batch hay độ dài chuỗi biến thiên. |
| **VOAI02-M29** | Khi huấn luyện mạng học sâu nhiều lớp hoặc mô hình RNN chuỗi dài,... | Exploding Gradient (Bùng nổ gradient) | §2.10 Gradient Vanishing & Exploding, Early Stopping | **OLP01-C22** | Khi tăng số lượng tầng của mạng CNN lên rất sâu (t... | Cùng kiểm tra vấn đề bất ổn định gradient trong mạng sâu và RNN chuỗi dài: M29 tập trung vào giải pháp cắt tỉa gradient (Gradient Clipping) để chặn bùng nổ gradient, bổ trợ cho §2.10. |
| **VOAI02-M30** | Trong PyTorch, lớp `nn.CrossEntropyLoss()` đã tự động tích hợp sẵ... | `nn.CrossEntropyLoss()` | §2.4 Các hàm mất mát (Loss Functions) | **OLP01-B11** | Khi sử dụng hàm mất mát `torch.nn.CrossEntropyLoss... | Cùng kiểm tra cơ chế kỹ thuật của `nn.CrossEntropyLoss()` trong PyTorch: tích hợp LogSoftmax và Log-Sum-Exp để tối ưu độ ổn định số học, yêu cầu thí sinh đưa trực tiếp raw logits chưa qua Softmax. |
| **VOAI02-M31** | Vì sao trong bài toán phân loại nhị phân hoặc phân loại đa nhãn (... | `nn.BCELoss` thủ công | §2.4 Các hàm mất mát (Loss Functions) | **OLP01-B12** | Trong PyTorch, khi giải bài toán phân loại nhị phâ... | Cùng làm rõ lý do ổn định số học (numerical stability) của `nn.BCEWithLogitsLoss()` thông qua thủ thuật Log-Sum-Exp trong tính toán dấu phẩy động. |
| **VOAI02-M32** | Nghiên cứu của Loshchilov & Hutter (ICLR 2019) đã chỉ ra rằng việ... | Weight Decay trong Adam thông thường | §2.5 Thuật toán tối ưu hóa (Optimizers) | **OLP01-C11** | Vì sao thuật toán tối ưu hóa Adam (Adaptive Moment... | OLP01-C11 phân tích sức mạnh của Adam, còn M32 đi sâu vào công trình đột phá AdamW (Loshchilov & Hutter 2019) tách biệt cơ chế Weight Decay để khôi phục đúng bản chất điều chuẩn L2 cho các bộ tối ưu thích nghi. |
| **VOAI02-M33** | Kỹ thuật **Learning Rate Warmup** (tăng dần tốc độ học từ 0 lên g... | Learning Rate Warmup | §2.6 Learning Rate Scheduling & Warmup | **OLP01-C12** | Trong các chiến lược điều chỉnh tốc độ học (Learni... | Cùng phân tích chiến lược lập lịch tốc độ học hiện đại: OLP01-C12 kiểm tra dạng đường cong Cosine Annealing with Warmup, còn M33 giải thích lý do toán học vì sao giai đoạn Warmup ban đầu là tối quan trọng để giữ mô hình không bị chệch hướng khi gradient sơ khai còn nhiễu. |
| **VOAI02-M34** | Trong hầu hết các thư viện Deep Learning hiện đại (bao gồm PyTorc... | Inverted Dropout | §2.9 Dropout & Tránh Overfitting | **OLP01-B10** | Trong thiết kế khối mạng nơ-ron tích chập (Conv Bl... | Làm rõ kỹ thuật Inverted Dropout trong PyTorch: nhân hệ số tỷ lệ $\frac{1}{1-p}$ ngay lúc huấn luyện để giữ nguyên kỳ vọng kích hoạt, giúp pha suy luận (model.eval()) diễn ra hoàn toàn tự nhiên không cần scaling. |
| **VOAI02-M35** | Xét bài toán tối ưu hóa có điều kiện: $\min_w L(w)$ với ràng buộc... | L1 Regularization (Lasso) | §1.6 Regularization L1 (Lasso) vs L2 (Ridge) vs ElasticNet | **OLP01-C09** | Điểm khác biệt cốt lõi về mặt toán học và ứng dụng... | Cùng đối chiếu L1 vs L2: OLP01-C09 nêu kết luận ứng dụng lựa chọn đặc trưng của L1, còn M35 giải thích trực quan hình học dựa trên đường đồng mức (contour lines) và hình học lồi của siêu mặt cầu $L_1$ và $L_2$. |
| **VOAI02-M36** | Khi triển khai cơ chế Dừng Sớm (Early Stopping) trong quá trình h... | Patience (Độ kiên nhẫn) | §2.10 Gradient Vanishing & Exploding, Early Stopping | **VOAI03-M40** | Kỹ thuật Early Stopping dừng quá trình huấn luyện ... | Cùng kiểm tra cơ chế Early Stopping: VOAI03-M40 xác định tín hiệu dừng dựa trên Validation Loss, còn M36 chi tiết hóa vai trò của tham số `patience` và nguyên tắc Model Checkpointing lưu lại trọng số tối ưu nhất thay vì trọng số của epoch cuối cùng. |
| **VOAI02-M37** | Cho ảnh đầu vào kích thước vuông $W_{in} = 224$. Áp dụng lớp tích... | Công thức kích thước đầu ra Conv2D | §3.1 Lớp Convolution & Công thức Kích thước Đầu ra | **VOAI03-M16** | Cho đầu vào $W \times H$, filter $K \times K$, pad... | VOAI03-M16 đưa ra công thức tổng quát $\lfloor\frac{W - K + 2P}{S}\rfloor + 1$, còn M37 là bài toán áp dụng số thực tế cho tầng tích chập đầu tiên kinh điển của ResNet ($224 \to 112$). |
| **VOAI02-M38** | Trong thiết kế mạng VGG và ResNet, vì sao người ta luôn ưu tiên x... | Receptive Field (Trường thụ cảm) | §3.3 Các Kiến trúc CNN Kinh Điển | **OLP01-C13** | Kiến trúc mạng tích chập kinh điển VGGNet (Simonya... | Cùng kiểm tra nguyên lý thiết kế đột phá của VGGNet: xếp chồng các kernel nhỏ $3 \times 3$ để mở rộng Receptive Field mà vẫn tiết kiệm tham số tính toán và tăng chiều sâu biểu diễn phi tuyến. |
| **VOAI02-M39** | Kỹ thuật Global Average Pooling (GAP) được giới thiệu trong mạng ... | Global Average Pooling (GAP) | §3.3 Các Kiến trúc CNN Kinh Điển | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi lý thuyết độc lập về kỹ thuật GAP trong kiến trúc Network In Network và ResNet, loại bỏ hoàn toàn các tầng kết nối đầy đủ (Fully Connected) chiếm 80-90% tham số trong các mạng cổ điển (§3.3). |
| **VOAI02-M40** | Trong khối Residual Block của kiến trúc ResNet, đầu ra được tính ... | Residual Connection (Kết nối tắt) | §3.4 Skip Connection: ResNet (ADD) vs U-Net (CONCAT) | **OLP01-C22** | Khi tăng số lượng tầng của mạng CNN lên rất sâu (t... | OLP01-C22 nêu hiện tượng suy thoái hiệu năng khi mạng quá sâu, còn M40 giải thích về mặt giải tích số hạng đạo hàm $+1$ trong kết nối tắt (Skip Connection) của ResNet giải quyết triệt để vấn đề này. |
| **VOAI02-M41** | Trong bài toán phân đoạn ảnh ngữ nghĩa (Semantic Segmentation), k... | U-Net Architecture | §3.4 Skip Connection: ResNet (ADD) vs U-Net (CONCAT) | **OLP01-C23** | Trong kiến trúc mạng U-Net dùng cho phân vùng ảnh ... | Cùng kiểm tra cơ chế Skip Connection trong mạng phân vùng ảnh U-Net: phép nối ghép kênh (Concatenation) dọc theo chiều channel giúp bảo toàn nguyên vẹn tọa độ pixel ranh giới vật thể. |
| **VOAI02-M42** | Cho ảnh đầu vào kích thước $224 \times 224 \times 3$. Trong kiến ... | Vision Transformer (ViT) | §3.5 Vision Transformer (ViT — Dosovitskiy et al., 2020) | **OLP01-C24** | Phát biểu nào sau đây là CHÍNH XÁC NHẤT về cơ chế ... | OLP01-C24 mô tả nguyên lý chia ảnh thành chuỗi patch phẳng và chiếu tuyến tính trong ViT, còn M42 yêu cầu tính toán cụ thể số lượng token ($196 + 1 = 197$) và kích thước tensor biểu diễn. |
| **VOAI02-M43** | Cho hai bounding box hình chữ nhật trong mặt phẳng tọa độ theo đị... | Tọa độ Bounding Box | §3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN | **OLP01-B06** | Cho bounding box dự đoán $B_p$ và bounding box nhã... | Cùng kiểm tra công thức tính chỉ số IoU (Intersection over Union) giữa hai hộp giới hạn: OLP01-B06 cho sẵn diện tích giao và hợp, còn M43 yêu cầu tính trực tiếp từ tọa độ hộp $[x_1, y_1, x_2, y_2]$. |
| **VOAI02-M44** | Trong pipeline phát hiện đối tượng (Object Detection), thuật toán... | NMS (Non-Maximum Suppression) | §3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN | **OLP01-C15** | Thuật toán Triệt tiêu Phi cực đại (Non-Maximum Sup... | OLP01-C15 nêu vai trò loại bỏ các bounding box dư thừa của NMS, còn M44 chi tiết hóa từng bước thực thi trong pipeline thuật toán. |
| **VOAI02-M45** | Trong đánh giá mô hình Object Detection chuẩn COCO, kí hiệu **mAP... | mAP (Mean Average Precision) | §3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN | **Độc lập** | N/A (Chuyên đề độc lập) | Làm rõ thước đo đánh giá độ chính xác tiêu chuẩn COCO mAP@[0.5:0.95] đòi hỏi mô hình vừa định danh đúng lớp vừa dự đoán hộp bám sát biên giới hạn ở nhiều mức độ khắt khe IoU (§3.6). |
| **VOAI02-M46** | Khi triển khai hệ thống Computer Vision trên thiết bị nhúng hoặc ... | One-Stage Detector (YOLO, SSD, RetinaNet) | §3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN | **OLP01-C16** | So sánh đúng đắn nhất giữa hai họ mô hình phát hiệ... | Cùng so sánh sự đánh đổi giữa 1-stage và 2-stage detector: tốc độ xử lý thời gian thực (FPS) đối lập với độ chính xác định vị và nhận diện vật thể nhỏ. |
| **VOAI02-M47** | Trong bài toán phát hiện ảnh giả mạo/DeepFake (Bài toán 'Kẻ mạo d... | DeepFake / AI-Generated Artifacts | §3.8 Mô hình Sinh ảnh: GAN vs Diffusion vs Autoencoder | **VOAI03-E03** | Đề xuất giải pháp giải quyết bài toán 'Kẻ Mạo Danh... | M47 kiểm tra lý thuyết về 32 đặc trưng kết cấu vật lý và vi sai nén JPEG, là nền tảng trực tiếp để giải quyết bài toán tự luận thiết kế hệ thống phát hiện ảnh giả mạo trong VOAI03-E03. |
| **VOAI02-M48** | Trong kỹ thuật **MixUp** (Zhang et al.), hai ảnh $(x_i, x_j)$ và ... | MixUp (Zhang et al., 2017) | §3.9 Data Augmentation & Transfer Learning | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi độc lập về kỹ thuật tăng cường dữ liệu kết hợp tuyến tính MixUp (Zhang et al.), giúp làm trơn bề mặt quyết định và tăng cường tính ổn định của mô hình (§3.9). |
| **VOAI02-M49** | Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự chuẩn mực logic của... | Text Preprocessing Pipeline | §4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn | **OLP01-C28** | Thứ tự chuẩn xác của một quy trình tiền xử lý văn ... | Cùng kiểm tra thứ tự logic bất biến trong pipeline tiền xử lý văn bản kinh điển: làm sạch, tách từ, lọc stopwords, chuẩn hóa từ gốc rồi mới vector hóa đặc trưng. |
| **VOAI02-M50** | Trong thuật toán biểu diễn từ Word2Vec (Mikolov et al.), phát biể... | CBOW (Continuous Bag-of-Words) | §4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations) | **VOAI03-M21** | Phương pháp 'Bag of Words' (BoW) có nhược điểm lớn... | VOAI03-M21 nêu nhược điểm mất ngữ cảnh của BoW, dẫn dắt tới sự ra đời của Word2Vec trong M50 với hai cơ chế đối ngẫu: CBOW (ngữ cảnh đoán từ) và Skip-gram (từ đoán ngữ cảnh). |
| **VOAI02-M51** | Cho hai vector embedding biểu diễn ngữ nghĩa của hai từ: $u = [1,... | Cosine Similarity | §4.3 Cosine Similarity | **OLP01-B09** | Cho hai vector đặc trưng (embeddings) trong không ... | Cùng kiểm tra phép tính độ tương đồng Cosine $\frac{u \cdot v}{\\|u\\| \\|v\\|}$ giữa hai vector embedding: OLP01-B09 tính trong không gian 2D, còn M51 tính trong không gian 3D. |
| **VOAI02-M52** | Trong mạng LSTM (Long Short-Term Memory), cổng nào chịu trách nhi... | LSTM Forget Gate ($f_t$) | §4.4 Mạng Nơ-ron Hồi Quy: RNN, LSTM & GRU | **VOAI03-M15** | Trong LSTM, cổng (gate) nào quyết định thông tin n... | Cùng kiểm tra vai trò của Cổng quên (Forget Gate) trong kiến trúc LSTM và sự tiến hóa tinh giản sang GRU (chỉ gồm Reset Gate và Update Gate). |
| **VOAI02-M53** | Trong cơ chế tính toán Self-Attention của Transformer (Vaswani et... | Scaled Dot-Product Attention | §4.5 Kiến trúc Transformer (Vaswani et al., 2017) | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi độc lập đào sâu bản chất toán học của hệ số tỷ lệ $\frac{1}{\sqrt{d_k}}$ trong cơ chế Scaled Dot-Product Attention: duy trì phương sai bằng 1 để Softmax không bị đẩy vào vùng bão hòa gradient (§4.5). |
| **VOAI02-M54** | Vì sao kiến trúc Transformer chia không gian biểu diễn thành $h$ ... | Multi-Head Attention (MHA) | §4.5 Kiến trúc Transformer (Vaswani et al., 2017) | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi độc lập về lý do kiến trúc Multi-Head Attention vượt trội hơn Single-Head Attention: mở rộng khả năng nắm bắt đa góc độ quan hệ ngữ nghĩa trong câu (§4.5). |
| **VOAI02-M55** | Trong Transformer nguyên bản, công thức mã hóa vị trí Sinusoidal ... | Sinusoidal Positional Encoding | §4.5 Kiến trúc Transformer (Vaswani et al., 2017) | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi độc lập về ưu điểm toán học tuyệt vời của mã hóa vị trí hàm sin/cos trong Transformer: cho phép mô hình dễ dàng học cách chú ý theo khoảng cách tương đối (§4.5). |
| **VOAI02-M56** | Sự khác biệt căn bản về mặt cấu trúc chú ý (Attention Mechanism) ... | BERT (Devlin et al., 2018) | §4.6 So sánh BERT vs GPT | **OLP01-C30** | Bạn cần xây dựng 2 hệ thống AI: Hệ thống 1 dùng để... | OLP01-C30 ứng dụng BERT (Encoder-only) cho phân loại và GPT (Decoder-only) cho sinh văn bản, còn M56 đi sâu vào bản chất kiến trúc chú ý 2 chiều vs 1 chiều và mục tiêu tiền huấn luyện của chúng. |
| **VOAI02-M57** | Trong đánh giá dịch máy (Bài toán Dịch Hoa - Việt đề thi OLP AI 2... | SacreBLEU | §4.7 Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity | **OLP01-E02** | Đề xuất giải pháp theo khung 5 bước chuẩn kỹ sư ch... | M57 kiểm tra công thức tính hệ số phạt độ ngắn Brevity Penalty của độ đo SacreBLEU, là metric cốt lõi đánh giá chất lượng mô hình trong bài tự luận Dịch máy OLP01-E02. |
| **VOAI02-M58** | Khác biệt cốt lõi về triết lý đo lường giữa chỉ số **BLEU** và ch... | BLEU (Bilingual Evaluation Understudy) | §4.7 Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity | **Độc lập** | N/A (Chuyên đề độc lập) | Câu hỏi độc lập làm rõ sự khác biệt triết lý giữa BLEU (hướng tới Precision cho dịch máy) và ROUGE (hướng tới Recall cho tóm tắt văn bản) (§4.7). |
| **VOAI02-M59** | Trong một hệ thống RAG doanh nghiệp hiện đại, pipeline truy xuất ... | RAG (Retrieval-Augmented Generation) | §4.3 Cosine Similarity | **VOAI03-M23** | Hệ thống RAG (Retrieval-Augmented Generation) giúp... | VOAI03-M23 nêu vai trò cốt lõi của RAG trong việc giảm ảo giác và cập nhật tri thức cho LLM, còn M59 phân tích kiến trúc truy xuất 2 giai đoạn (Bi-Encoder kết hợp Cross-Encoder Re-ranker) trong hệ thống RAG doanh nghiệp thực tế. |
| **VOAI02-M60** | Trong quá trình sinh văn bản tự hồi quy (Autoregressive Generatio... | Autoregressive Generation | §4.5 Kiến trúc Transformer (Vaswani et al., 2017) | **VOAI03-M30** | Để phục vụ (Serving) một mô hình LLM lớn, kỹ thuật... | Cùng kiểm tra cơ chế KV Cache trong phục vụ mô hình ngôn ngữ lớn: VOAI03-M30 nêu định nghĩa kỹ thuật, còn M60 phân tích mức độ tối ưu hóa độ phức tạp tính toán của từng bước sinh token tự hồi quy. |

---

## 3. CÁC NÂNG CẤP KỸ THUẬT & HỌC THUẬT ĐÃ THỰC THI

### 3.1 Chuẩn hóa Định nghĩa Toán học của p-value (VOAI02-M03)
Theo Tuyên bố chính thức của Hiệp hội Thống kê Hoa Kỳ (American Statistical Association — ASA Statement on Statistical Significance and P-Values, Wasserstein & Lazar, 2016):
- **Định nghĩa chuẩn xác:** $p$-value là xác suất, dưới một mô hình thống kê cụ thể và giả định giả thuyết không $H_0$ là đúng, thu được một thống kê kiểm định có độ lớn bằng hoặc cực đoan hơn giá trị thực tế quan sát được trên tập mẫu ($P(T \ge t_{\text{obs}} \mid H_0)$ đối với kiểm định một phía hoặc $P(|T| \ge |t_{\text{obs}}| \mid H_0)$ đối với kiểm định hai phía).
- **Các ngộ nhận đã loại bỏ:**
  * Tuyệt đối không dùng biểu thức $P(\text{Data} \mid H_0)$ làm định nghĩa cho $p$-value (đây là likelihood của một tập dữ liệu cụ thể, không đo lường độ cực đoan).
  * $p$-value KHÔNG PHẢI là xác suất giả thuyết không đúng ($P(H_0 \mid \text{Data})$).
  * $p$-value KHÔNG PHẢI là xác suất dữ liệu được tạo ra hoàn toàn do ngẫu nhiên.
- Đã đồng bộ định nghĩa chuẩn này vào cả Khối 1 (Thuật ngữ mới) và Khối 4 (Căn cứ lý thuyết) của câu `VOAI02-M03`, bảo toàn đáp án D hợp lệ.

### 3.2 Nâng cấp Bộ Công cụ Kiểm toán Tự động (Scripts Audit)
1. **`scripts/audit_quality.py` (Kiểm toán Cấu trúc & Tham chiếu)**:
   - Phân định rõ ràng kiểm tra MCQ/Code (bắt buộc đủ 4 khối Markdown học thuật: ELI5, Đạo hàm, Phân tích bẫy đề, Căn cứ lý thuyết & Ứng dụng thực chiến).
   - Kiểm tra khắt khe bài Tự luận: `modelAnswer` tối thiểu 100 ký tự (thực tế từ 2.500 đến 6.000 ký tự), `rubric` tối thiểu 3 tiêu chí (thực tế 5 tiêu chí chuẩn), tổng điểm `rubricPoints` khớp 100% với thuộc tính `points`.
   - Kiểm tra tính hợp lệ của tham chiếu lý thuyết: tất cả mục `§` được trích dẫn đều phải tồn tại thật trong 59 mục của giáo trình `01-ly-thuyet-olp-ai.md`.
   - Kiểm tra ID liên hệ: phải tồn tại trong tập 184 câu của 3 đề thi (hoặc được ghi rõ là câu độc lập).
   - Kết quả: **184/184 câu PASS**, trả về exit code 0.
2. **`scripts/audit_katex_syntax.mjs` (Kiểm toán Cú pháp Toán học KaTeX)**:
   - Quét toàn bộ các trường text trong cả 3 file JSON (`prompt`, `options.text`, `explanation`, `modelAnswer`, `rubric`).
   - Quét toàn văn giáo trình lý thuyết `01-ly-thuyet-olp-ai.md` từ dòng đầu đến ký tự cuối cùng.
   - Quét danh sách 10 công thức toán học thực tế được nhúng trong code sinh Web Hub `generate_full_hub.py`.
   - Kiểm tra tính cân đối của delimiter (`$$...$$` và `$...$`), kiểm tra escape sequence JSON (`\\` vs `\`).
   - Đưa từng biểu thức vào parser KaTeX thật:
     ```javascript
     katex.renderToString(cleanMath, { throwOnError: true, displayMode: isBlock });
     ```
   - Kết quả: **2.689 đoạn công thức toán học được quét -> 0 lỗi cú pháp / ngoại lệ render**.

### 3.3 Cập nhật Cẩm nang PDF (`docs/olp_ai_handbook_2026.tex`) & Biên dịch XeLaTeX
1. **Đính chính quy chế thi SOLOAI OLP AI 2025**:
   - Tác vụ Dịch máy Thần kinh (NMT) Hoa - Việt: Ghi rõ quy chế thi yêu cầu **huấn luyện mô hình Transformer Encoder-Decoder từ đầu (from scratch)** với SentencePiece BPE; cấm sử dụng trọng số pretrained bên ngoài (như mBART-50 hay NLLB-200); các mô hình pretrained chỉ được đề cập như giải pháp tham chiếu/mở rộng khi đề thi cho phép.
2. **Chuẩn hóa trích dẫn mô hình TabM**:
   - Ghi rõ xuất xứ học thuật: **ICLR 2025** (*TabM: Advancing Tabular Deep Learning with Ensembles of Parameter-Efficient Backbones*).
3. **Biên dịch XeLaTeX**:
   - Chạy 2 pass `xelatex -interaction=nonstopmode` thành công 100%, 0 lỗi, xuất bản PDF 45 trang chất lượng cao.
   - SHA256 checksum: `87E56B7710F7A84C16E5468F151FC0A9118B2BCDA82290390D5FAB37D41B6B83`.
   - Đã đồng bộ đồng loạt sang: `docs/olp_ai_handbook_2026.pdf`, `dist/olp_ai_handbook_2026.pdf`, `public/olp_ai_handbook_2026.pdf`.

### 3.4 Tích hợp Inline Embedded Video Player trên Web Study Hub
- Thêm hàm phát video tại chỗ `window.playVideoInline(videoId, startSeconds)` và bí danh tương thích `window.playVideo(videoId, startSeconds)` trong `docs/generate_full_hub.py`.
- Khi thí sinh bấm vào thumbnail bài giảng hoặc nút vàng `▶ Phát ngay trên Web`, hệ thống sẽ:
  1. Tự động cuộn mượt mà lên khung phát video phía trên.
  2. Nhúng iframe YouTube tỷ lệ chuẩn 16:9 với tham số `autoplay=1&start={startSeconds}&rel=0`.
  3. Cung cấp nút `✖ Đóng trình phát video` để thí sinh đóng lại khi học xong mà không làm gián đoạn bài giảng.
- Đã kiểm chứng trực quan bằng Chrome DevTools / CDP screenshot và quay video webp.

---

## 4. TÍNH MINH BẠCH VỀ NGUỒN GỐC & ĐỘ SÁT ĐỀ THI CHÍNH THỨC

> [!WARNING]
> **Tuyên bố minh bạch học thuật (Academic Transparency Statement):**  
> 1. **Tài liệu nguồn gốc:**  
>    - File đề thi chính thức của Vòng Sơ loại SOLOAI OLP AI 2025 nằm tại: `C:\Users\HP\Downloads\Đề thi Olp_AI_2025 Vòng SOLOAI.pdf` (gồm 2 tác vụ thực tế: Dịch máy NMT Hoa-Việt from scratch và Nhận diện Video Sign Language 50 cử chỉ).  
>    - Các câu hỏi và chuyên đề ôn tập được tổng hợp từ video bài giảng ôn tập vòng bảng của BTC / AI Vietnam, kết hợp tài liệu đề thi thử 50 câu của Thầy Đỗ Đình Luật.  
> 2. **Trạng thái đối chiếu Đề thi Chính thức VOAI 2025 mã 006:**  
>    - **`UNVALIDATED`**: Nhóm biên soạn **chưa có trong tay và chưa đối chiếu toàn văn với bản in mã đề 006 (thời lượng 180 phút, 100 câu trắc nghiệm) của kỳ thi VOAI 2025 chính thức**.  
>    - Vì vậy, Đề 02 và Đề 03 được định danh trung thực là: **Đề thi Luyện tập & Chuyên đề Mở rộng Chuẩn Format VOAI**, nhằm cung cấp kiến thức nền tảng và bài tập rèn luyện kỹ năng, không cam kết hay phóng đại là bản sao 100% của đề thi chính thức mã 006.

---

## 5. LỘ TRÌNH ÔN TẬP NƯỚC RÚT 48H CHO THÍ SINH (09/10 – 10/10/2026)

Kỳ thi vòng trường diễn ra vào trưa **Chủ nhật, ngày 11/10/2026**. Thí sinh áp dụng lộ trình 48 giờ tối ưu:

### Ngày 1 (Thứ Sáu, 09/10/2026) — Rà Quét Lỗ Hổng & Thuộc Lòng 24 Bẫy Kinh Điển
1. **Sáng (08:00 - 11:30): Luyện trọn vẹn Đề 01 (90 phút)**
   - Mở `http://localhost:8080/olympic_ai_study_hub.html`, chọn **Đề 01: Ôn Tập Toàn Diện**.
   - Làm bài nghiêm túc, tính tay Module A (Bayes, Ma trận Hessian, Kích thước Conv2D floor + 1).
   - Xem kỹ lời giải ELI5 của các câu làm sai.
2. **Chiều (14:00 - 17:00): Đọc Sổ tay Lý thuyết & 24 Bẫy Đề Thi**
   - Mở tab **GIÁO TRÌNH** ở sidebar bên trái, đọc kỹ **Chương 6: Bảng 24 Bẫy Đề Thi Kinh Điển**.
   - Ghi nhớ: Thống kê BatchNorm cần >1 giá trị/channel khi train (`ValueError` của `BatchNorm1d(1, C)`); Ngộ nhận F1-Score so với Accuracy; Phép nhân Conv trong ViT; Đơn vị bit vs nat của Shannon Entropy.
3. **Tối (19:30 - 22:00): Thuộc Lòng Khung 5 Bước Làm Tự Luận**
   - Nhấn nút "Nạp khung mẫu 5 bước chuẩn" ở các bài tự luận.
   - Ghi nhớ 5 bước: 1. Phân tích bài toán & Ràng buộc $\to$ 2. Kiến trúc mô hình $\to$ 3. Pipeline chống Leakage $\to$ 4. Metric đặc thù (Macro-F1) $\to$ 5. Kỹ thuật mở rộng thực tế.

### Ngày 2 (Thứ Bảy, 10/10/2026) — Thi Thử Mock Test & Hoàn Thiện Tốc Độ
1. **Sáng (08:30 - 10:00): Thi Thử Đề 02 (Chuẩn Format VOAI Mở Rộng - 90 phút)**
   - Chọn **Đề 02** trong dropdown selector.
   - Thử sức với 60 câu trắc nghiệm chuyên sâu (thang điểm 90đ) và tự đối chiếu 6 bài tự luận thiết kế giải pháp AI.
   - Quản lý thời gian: tối đa 1 phút cho câu lý thuyết, 2 phút cho câu tính toán, 30 phút cho tự luận.
2. **Chiều (14:30 - 16:00): Thi Thử Đề 03 (Luyện Thi Thử VOAI & Chuyên Đề Thực Hành)**
   - Chọn **Đề 03** trong dropdown selector.
   - Ôn tập các chuyên đề hiện đại: TabM ICLR 2025, KV cache trade-off, Quantization, RAG hallucination.
   - Nghiền ngẫm 4 bài tự luận thực chiến (`VOAI03-E01` đến `E04`).
3. **Tối (20:00 - 21:30): Ôn Lại Bảng Công Thức Cốt Lõi & Nghỉ Ngơi**
   - Mở tab **CÔNG THỨC** ở bảng điều khiển bên phải.
   - Rà soát lại 10 công thức toán & học máy cốt lõi.
   - Đi ngủ sớm trước 22:30 để giữ tinh thần minh mẫn cho ngày thi Chủ nhật.

---

## 6. DANH SÁCH FILE ĐÃ THAY ĐỔI & LỆNH THỰC THI NGHIỆM THU

### Danh sách tệp tin đã tạo và chỉnh sửa:
1. `scripts/enrich_olp02_terms_and_links.py` — Viết lại 100% từ điển ánh xạ 60 câu Đề 02 (M01-M60) chuẩn xác theo nội dung câu hỏi thực tế từ JSON thật; sửa định nghĩa p-value chuẩn ASA.
2. `src/data/exams/olp-02.json` — Áp dụng enrichment mới, sửa dứt điểm các lỗi lệch chủ đề và liên hệ sai (M05 -> VOAI03-M02, M13 -> OLP01-C01, M49 -> OLP01-C28, M51 -> OLP01-B09, M59 -> VOAI03-M23, M60 -> VOAI03-M30; M03 chuẩn hóa p-value ASA).
3. `content/02-de-chuan-format-voai-expand.md` — Đồng bộ 100% lời giải Markdown 4 khối của Đề 02 với dữ liệu JSON.
4. `content/03-de-vong-mien-voai-2025.md` — Đính chính nhãn tiêu đề: Đề thi thử biên soạn mô phỏng cấu trúc, không tự nhận là đề gốc BTC.
5. `content/01-ly-thuyet-olp-ai.md` — Đính chính §8 đề thi thử Đỗ Đình Luật và kiểm tra toàn văn công thức toán KaTeX.
6. `docs/olp_ai_handbook_2026.tex` — Sửa ràng buộc NMT SOLOAI (huấn luyện from scratch, cấm pretrained) và trích dẫn TabM ICLR 2025.
7. `docs/olp_ai_handbook_2026.pdf` — File PDF biên dịch lại từ XeLaTeX (45 trang, 0 lỗi).
8. `dist/olp_ai_handbook_2026.pdf` & `public/olp_ai_handbook_2026.pdf` — Bản phân phối PDF đồng bộ.
9. `scripts/audit_quality.py` — Script kiểm toán chất lượng nội dung khắt khe (MCQ 4 khối, Essay rubric/modelAnswer, § và ID liên hệ).
10. `scripts/audit_katex_syntax.mjs` — Script kiểm toán cú pháp KaTeX toàn diện 2.689 đoạn công thức.
11. `docs/generate_full_hub.py` — Tích hợp trình phát video YouTube inline (16:9, autoplay, nút đóng) và cập nhật dữ liệu mới.
12. `dist/olympic_ai_study_hub.html` & `public/olympic_ai_study_hub.html` — File Web Study Hub sinh lại hoàn chỉnh.
13. `C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26\public\olympic_ai_study_hub.html` — File phục vụ live trên cổng 8080.
14. `docs/BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md` — Báo cáo tổng kết nghiệm thu toàn diện này.

### Các lệnh kiểm tra tự động đã thực thi và kết quả:
```powershell
# 1. Kiểm tra cấu trúc dữ liệu 3 đề thi (184 câu)
node scripts/validate.mjs
# Kết quả: PASS cả 3 đề (olp-01: 60 graded + 4 essay; olp-02: 60 graded + 6 essay; olp-03: 50 graded + 4 essay). Exit code: 0.

# 2. Kiểm toán chất lượng nội dung và tham chiếu học thuật
python scripts/audit_quality.py
# Kết quả: PASS 100% cả 184 câu hỏi (MCQ đủ 4 khối, Essay đủ rubric và modelAnswer, § và ID liên hệ tồn tại 100%). Exit code: 0.

# 3. Kiểm toán cú pháp toàn bộ 2.689 đoạn công thức KaTeX
node scripts/audit_katex_syntax.mjs
# Kết quả: 2.689 snippets KaTeX quét -> 0 lỗi cú pháp hoặc delimiter. Exit code: 0.

# 4. Kiểm thử đơn vị Vitest (React)
cmd.exe /c "npm test -- --run"
# Kết quả: 4 test files passed, 18/18 tests PASS. Exit code: 0.

# 5. Kiểm thử logic HTML standalone trong VM Sandbox (5 nhóm test)
node scripts/test_html_logic.mjs
# Kết quả: PASS 100% (Storage migration, Graded/Essay separation, Template rỗng 0đ & reset khi xóa, Code sandbox notice, Code partial score OLP01-BC1 & BC2 trên các mốc 0, 2, 4, 5, 7). Exit code: 0.

# 6. Kiểm tra Typecheck TypeScript
cmd.exe /c "npx.cmd tsc --noEmit -p tsconfig.json"
# Kết quả: Exit code 0 (0 errors).
```

---
*Báo cáo được hoàn thành với tinh thần khoa học nghiêm túc, minh bạch và khiêm tốn. Hệ thống tài liệu và công cụ đã sẵn sàng ở trạng thái tốt nhất để thí sinh tự tin bước vào kỳ thi Olympic AI HCMUS 2026 ngày 11/10/2026.*
