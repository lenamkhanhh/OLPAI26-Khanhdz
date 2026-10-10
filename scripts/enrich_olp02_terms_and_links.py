# -*- coding: utf-8 -*-
"""
scripts/enrich_olp02_terms_and_links.py
Nâng cấp và chuẩn hóa 100% 60 câu trắc nghiệm Đề 02 (src/data/exams/olp-02.json)
và đồng bộ sang content/02-de-chuan-format-voai-expand.md.

Đặc tả chất lượng sau rà soát Lần 4 (09/10/2026):
1. Khớp chuẩn xác 1:1 giữa Prompt thật <-> Thuật ngữ <-> § Giáo trình <-> ID liên hệ thật (hoặc chỉ rõ câu độc lập).
2. Định nghĩa p-value (M03) chuẩn xác theo tuyên bố của Hiệp hội Thống kê Hoa Kỳ (ASA):
   Xác suất thống kê kiểm định cực đoan bằng hoặc hơn quan sát dưới H0, tuyệt đối không dùng P(Data|H0).
3. Đổi các ID liên hệ sai lệch sang câu đích liên quan thực tế:
   M05 -> VOAI03-M02 (Hessian cực tiểu vs điểm yên ngựa)
   M13 -> OLP01-C01 (k-NN lazy learner)
   M49 -> OLP01-C28 (NLP preprocessing pipeline)
   M51 -> OLP01-B09 (Cosine similarity)
   M59 -> VOAI03-M23 (RAG retrieval)
   M60 -> VOAI03-M30 (KV Cache)
4. Bảo toàn tính toán toán học, không đổi ID/prompt/options/answer.
5. Idempotent 100% (không chèn lặp).
"""

import json
import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
json_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-02.json")
md_path = os.path.join(ROOT_DIR, "content", "02-de-chuan-format-voai-expand.md")

# Bảng từ điển thuật ngữ, § giáo trình và câu liên hệ chuẩn hóa 1:1 cho 60 câu Đề 02
TOPIC_ENRICHMENTS = {
    "VOAI02-M01": (
        "- **Base Rate (Tỉ lệ nền / Xác suất tiên nghiệm):** Tỉ lệ mắc bệnh tự nhiên trong cộng đồng $P(D)$.\n- **Sensitivity (Độ nhạy / True Positive Rate):** $P(+|D)$ - Xác suất test dương tính khi thực sự có bệnh.\n- **Specificity (Độ đặc hiệu / True Negative Rate):** $P(-|\\bar{D})$ - Xác suất test âm tính khi người hoàn toàn khỏe mạnh.\n- **Base Rate Fallacy:** Sai lầm phán đoán khi bỏ qua tỉ lệ nền quá nhỏ khiến số ca dương tính giả áp đảo số ca bệnh thật.",
        "§5.1 Định Lý Bayes & Bài Toán Chẩn Đoán Y Tế (Base-Rate Fallacy)",
        "Liên hệ câu OLP01-A01: Cùng kiểm tra nghịch lý tỉ lệ nền (Base-Rate Fallacy) trong xét nghiệm y tế: OLP01-A01 tính xác suất có bệnh khi test dương tính với $P(D)=2\\%$, còn M01 kiểm tra với $P(D)=0.5\\%$."
    ),
    "VOAI02-M02": (
        "- **Binomial Distribution (Phân phối nhị thức):** Phân phối của số lần thành công trong $n$ phép thử Bernoulli độc lập có cùng xác suất thành công $p$.\n- **Kỳ vọng $\\mathbb{E}[X] = n \\cdot p$:** Số lần thành công trung bình khi lặp lại thí nghiệm.\n- **Phương sai $\\text{Var}(X) = n \\cdot p \\cdot (1 - p)$:** Độ phân tán của số lần thành công quanh giá trị trung bình.",
        "§5.2 Các Phân Phối Xác Suất Quan Trọng",
        "Liên hệ câu OLP01-A03: Phân phối nhị thức $\\text{Binomial}(n, p)$ trong M02 chính là tổng của $n$ biến ngẫu nhiên $\\text{Bernoulli}(p)$ độc lập trong OLP01-A03, kế thừa công thức kỳ vọng $n p$ và phương sai $n p (1-p)$."
    ),
    "VOAI02-M03": (
        "- **Giả thuyết không ($H_0$):** Giả định mặc định rằng không có sự khác biệt hay không có hiệu ứng (thuật toán gợi ý mới không làm thay đổi hoặc không làm tăng CTR).\n- **p-value:** Xác suất, dưới giả định rằng giả thuyết không $H_0$ và mô hình kiểm định là đúng, thu được một thống kê kiểm định có độ lớn bằng hoặc cực đoan hơn giá trị thực tế quan sát được ($P(T \\ge t_{\\text{obs}} \\mid H_0)$ hoặc $P(|T| \\ge |t_{\\text{obs}}| \\mid H_0)$). Tuyệt đối không nhầm lẫn với xác suất dữ liệu cụ thể $P(\\text{Data} \\mid H_0)$ hay xác suất $H_0$ đúng $P(H_0 \\mid \\text{Data})$.\n- **Mức ý nghĩa ($\\alpha$):** Ngưỡng sai lầm loại I được ấn định trước (thường là 0.05). Nếu $p \\le \\alpha$, ta có đủ bằng chứng thống kê để bác bỏ $H_0$.",
        "§5.5 Kiểm Định Giả Thuyết Thống Kê & Bản Chất của p-value",
        "Đây là câu hỏi độc lập chuyên sâu trong ngân hàng đề kiểm tra trực tiếp định nghĩa chuẩn tắc của $p$-value và quy tắc ra quyết định trong A/B testing: $p$-value là xác suất của thống kê kiểm định cực đoan bằng hoặc hơn quan sát được dưới $H_0$ (theo Tuyên bố chính thức của Hiệp hội Thống kê Hoa Kỳ ASA), không phải $P(\\text{Data} \\mid H_0)$ hay $P(H_0 \\mid \\text{Data})$."
    ),
    "VOAI02-M04": (
        "- **PCA (Principal Component Analysis):** Phương pháp giảm chiều tuyến tính tìm các trục chiếu trực giao tối đa hóa phương sai của dữ liệu.\n- **Ma trận hiệp phương sai ($C = \\frac{1}{N} X^T X$):** Ma trận vuông đối xứng đo mức độ biến thiên đồng thời giữa các cặp đặc trưng sau khi đã chuẩn hóa zero-mean.\n- **Vector riêng & Trị riêng:** Trục thành phần chính thứ nhất là vector riêng ứng với trị riêng lớn nhất của ma trận hiệp phương sai $C$.",
        "§1.10 Tiền xử lý Đặc trưng & Thao tác NumPy",
        "Liên hệ câu VOAI03-M32: Cùng thuộc chuyên đề giảm chiều dữ liệu: M04 phân tích cơ sở toán học tuyến tính của PCA (trục chiếu theo vector riêng của ma trận hiệp phương sai), còn VOAI03-M32 so sánh PCA với phương pháp giảm chiều phi tuyến t-SNE."
    ),
    "VOAI02-M05": (
        "- **Ma trận Hessian ($H = \\nabla^2 f(x, y)$):** Ma trận vuông chứa tất cả các đạo hàm riêng bậc hai của hàm đa biến, biểu diễn độ cong của bề mặt hàm số.\n- **Điểm dừng (Stationary Point):** Điểm mà vector gradient triệt tiêu $\\nabla f(x, y) = [0, 0]^T$.\n- **Điểm yên ngựa (Saddle Point):** Điểm dừng mà theo một hướng thì đạt cực tiểu nhưng theo hướng khác lại đạt cực đại (ma trận Hessian có định thức $\\det(H) < 0$ hoặc có cả trị riêng dương và âm).",
        "§2.3 Lan truyền xuôi, Lan truyền ngược & Vòng lặp Huấn luyện PyTorch",
        "Liên hệ câu VOAI03-M02: Cùng kiểm tra việc dùng ma trận Hessian để xác định tính chất điểm dừng trong tối ưu hóa: VOAI03-M02 kiểm tra trường hợp Hessian xác định dương ($\\det > 0, f_{xx} > 0 \\implies$ cực tiểu địa phương), còn M05 kiểm tra trường hợp Hessian bất định ($\\det(H) < 0 \\implies$ điểm yên ngựa)."
    ),
    "VOAI02-M06": (
        "- **Softmax Function:** Hàm chuyển đổi vector logit thô $z$ thành phân phối xác suất hợp lệ có tổng bằng 1: $p_i = \\frac{e^{z_i}}{\\sum_k e^{z_k}}$.\n- **Cross-Entropy Loss:** Hàm mất mát đo khoảng cách giữa phân phối dự đoán $p$ và nhãn One-hot $y$: $L = -\\sum y_i \\ln(p_i)$.\n- **Gradient Logits ($p_i - y_i$):** Đạo hàm của hàm lỗi theo logit đầu vào bằng hiệu số giữa xác suất dự đoán và nhãn thực tế, mang ý nghĩa sai số trực tiếp.",
        "§2.4 Các hàm mất mát (Loss Functions)",
        "Liên hệ câu OLP01-B11: M06 giải thích về mặt giải tích gradient $\\frac{\\partial L}{\\partial z_i} = p_i - y_i$ của Softmax kết hợp Cross-Entropy, bổ trợ trực tiếp cho OLP01-B11 về lý do vì sao trong PyTorch ta đưa raw logits trực tiếp vào `nn.CrossEntropyLoss()`."
    ),
    "VOAI02-M07": (
        "- **Khoảng cách Mahalanobis:** Độ đo khoảng cách giữa hai điểm có tính đến tương quan và phương sai của các chiều đặc trưng: $d_M(u, v) = \\sqrt{(u-v)^T \\Sigma^{-1} (u-v)}$.\n- **Ma trận hiệp phương sai ($\\Sigma$):** Ma trận đo độ co giãn và góc nghiêng của đám mây dữ liệu.\n- **Nghịch đảo $\\Sigma^{-1}$:** Biến đổi chuẩn hóa đám mây hình ellipsoid nghiêng về dạng hình cầu đẳng hướng trước khi đo khoảng cách Euclid.",
        "§1.8 K-Means Clustering & Silhouette Score",
        "Câu hỏi lý thuyết độc lập mở rộng về khoảng cách trong không gian đặc trưng đa biến có tương quan: khi ma trận hiệp phương sai là ma trận đơn vị ($\\Sigma = I$), khoảng cách Mahalanobis trở về đúng khoảng cách Euclid dùng trong thuật toán K-Means (§1.8)."
    ),
    "VOAI02-M08": (
        "- **MLE (Maximum Likelihood Estimation):** Ước lượng tham số chỉ dựa vào dữ liệu quan sát $\\max_w P(D|w)$.\n- **MAP (Maximum A Posteriori):** Ước lượng tham số kết hợp niềm tin tiên nghiệm (Prior): $\\max_w P(D|w) P(w)$.\n- **Gaussian Prior & L2 Regularization:** Giả định tiên nghiệm Gauss $w \\sim \\mathcal{N}(0, \\sigma^2)$ tương đương toán học với hàm phạt L2 (Ridge / Weight Decay $\\lambda \\|w\\|_2^2$).\n- **Laplace Prior & L1 Regularization:** Giả định tiên nghiệm Laplace tương đương toán học với hàm phạt L1 (Lasso $\\lambda \\|w\\|_1$).",
        "§5.4 Ước Lượng Tham Số: MLE vs MAP",
        "Liên hệ câu OLP01-C09: OLP01-C09 phân tích L1 vs L2 dưới góc độ điều chuẩn hình học trong học máy, còn M08 giải thích nguồn gốc xác suất Bayes của chúng: L2 tương ứng với tiên nghiệm Gauss, L1 tương ứng với tiên nghiệm Laplace trong ước lượng MAP."
    ),
    "VOAI02-M09": (
        "- **KL Divergence ($D_{KL}(P \\parallel Q)$):** Độ đo lượng thông tin mất mát khi dùng phân phối xác suất $Q$ để xấp xỉ phân phối thực tế $P$: $D_{KL}(P \\parallel Q) = \\sum P(x) \\log \\frac{P(x)}{Q(x)}$.\n- **Tính bất đối xứng (Asymmetry):** $D_{KL}(P \\parallel Q) \\ne D_{KL}(Q \\parallel P)$, do đó KL Divergence không phải là một hàm khoảng cách (metric) toán học thực thụ.\n- **Bất đẳng thức Gibbs:** $D_{KL}(P \\parallel Q) \\ge 0$ với mọi phân phối, đẳng thức xảy ra khi và chỉ khi $P = Q$.",
        "§2.4 Các hàm mất mát (Loss Functions)",
        "Liên hệ câu VOAI03-M04: Cùng thuộc lý thuyết thông tin: VOAI03-M04 đo độ hỗn loạn nội tại của phân phối qua Shannon Entropy $H(P)$, còn M09 đo độ lệch tương đối giữa hai phân phối qua Phân kỳ KL $D_{KL}(P \\parallel Q) = H(P, Q) - H(P)$."
    ),
    "VOAI02-M10": (
        "- **SiLU (Sigmoid Linear Unit / Swish):** Hàm kích hoạt phi tuyến định nghĩa là $f(x) = x \\cdot \\sigma(x) = \\frac{x}{1 + e^{-x}}$.\n- **Smooth & Non-monotonic:** Khác với ReLU bị gãy khúc tại $x=0$, SiLU khả vi liên tục mọi bậc và không đơn điệu (đạt cực tiểu nhẹ $\\approx -0.278$ tại $x \\approx -1.28$).\n- **Tự điều tiết (Self-Gated):** Giá trị $x$ được điều tiết bằng xác suất đi qua chính nó, giúp gradient lan truyền tốt hơn qua các tầng mạng rất sâu.",
        "§2.2 Các hàm kích hoạt (Activation Functions)",
        "Liên hệ câu OLP01-C20: Cùng kiểm tra các hàm kích hoạt hiện đại: OLP01-C20 khẳng định SiLU/GELU vượt trội hơn ReLU trong Transformer và mạng sâu, còn M10 đi sâu vào công thức giải tích $f(x) = x \\cdot \\sigma(x)$ và tính chất không đơn điệu của SiLU."
    ),
    "VOAI02-M11": (
        "- **Ma trận trực giao (Orthogonal Matrix):** Ma trận vuông $Q$ thỏa mãn $Q^T Q = Q Q^T = I$, nghĩa là các cột (và các hàng) tạo thành một hệ trực chuẩn.\n- **Bảo toàn chuẩn Euclid:** Với mọi vector $x$, $\\|Q x\\|_2^2 = (Q x)^T (Q x) = x^T Q^T Q x = x^T I x = \\|x\\|_2^2$.\n- **Ý nghĩa hình học:** Phép nhân với ma trận trực giao tương ứng với phép quay (Rotation) hoặc phép phản xạ (Reflection) không gian, bảo toàn nguyên vẹn độ dài và góc giữa các vector.",
        "§1.10 Tiền xử lý Đặc trưng & Thao tác NumPy",
        "Liên hệ câu VOAI03-M01: Cùng kiểm tra định nghĩa và tính chất của ma trận trực giao: cả hai câu đều khẳng định ma trận trực giao bảo toàn tích vô hướng và độ dài vector Euclid ($A^T A = I \\implies \\|A x\\| = \\|x\\|$)."
    ),
    "VOAI02-M12": (
        "- **Importance Sampling:** Kỹ thuật xấp xỉ kỳ vọng của hàm số theo phân phối $P$ bằng cách lấy mẫu từ một phân phối đề xuất $Q$ dễ lấy mẫu hơn.\n- **Likelihood Ratio / Importance Weight:** Trọng số $w(x) = \\frac{P(x)}{Q(x)}$ bù trừ sai lệch xác suất giữa hai phân phối.\n- **Công thức bất biến:** $\\mathbb{E}_{x \\sim P}[f(x)] = \\int f(x) P(x) dx = \\int f(x) \\frac{P(x)}{Q(x)} Q(x) dx = \\mathbb{E}_{x \\sim Q}\\left[f(x) \\frac{P(x)}{Q(x)}\\right]$.",
        "§5.6 Tương Quan vs Nhân Quả (Correlation vs Causation) & Kỹ Thuật Lấy Mẫu",
        "Câu hỏi độc lập nâng cao về kỹ thuật lấy mẫu Monte Carlo và xấp xỉ kỳ vọng toán học khi không thể lấy mẫu trực tiếp từ phân phối mục tiêu $P(x)$ (§5.6)."
    ),
    "VOAI02-M13": (
        "- **k-NN (k-Nearest Neighbors):** Thuật toán phân loại/hồi quy dựa trên khoảng cách tới $k$ điểm dữ liệu gần nhất trong tập huấn luyện.\n- **Lazy Learner (Người học lười biếng):** Thuật toán không có pha huấn luyện tham số trước ($O(1)$ khi fit), chỉ lưu toàn bộ tập dữ liệu vào bộ nhớ.\n- **Chi phí suy luận cao:** Khi dự đoán một điểm mới, phải tính khoảng cách tới toàn bộ $N$ mẫu trong không gian $D$ chiều, chi phí tính toán là $O(N \\cdot D)$.",
        "§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)",
        "Liên hệ câu OLP01-C01: Cùng kiểm tra bản chất Lazy Learner của k-NN: OLP01-C01 tập trung vào đặc điểm không học trọng số ở pha huấn luyện, còn M13 phân tích sâu thêm độ phức tạp tính toán suy luận $O(N \\cdot D)$ khi phải quét toàn bộ tập dữ liệu."
    ),
    "VOAI02-M14": (
        "- **Soft-Margin SVM:** Mô hình SVM cho phép một số điểm dữ liệu vi phạm lề hoặc bị phân loại sai để xử lý tập dữ liệu không phân tách tuyến tính hoàn hảo.\n- **Biến bù Slack ($\\xi_i \\ge 0$):** Khoảng cách mà điểm thứ $i$ vi phạm lề ($0 < \\xi_i \\le 1$: nằm trong lề nhưng đúng lớp; $\\xi_i > 1$: phân loại sai).\n- **Siêu tham số $C$:** Đánh đổi giữa độ rộng lề $\\frac{1}{2}\\|w\\|^2$ và tổng mức độ phạt vi phạm $C \\sum \\xi_i$. $C$ càng lớn thì phạt vi phạm càng nặng, ranh giới càng khắt khe $\\implies$ nguy cơ Overfitting.",
        "§1.2 Support Vector Machines (SVM & Kernel Trick)",
        "Liên hệ câu OLP01-C03: Cùng kiểm tra lý thuyết lề trong SVM: OLP01-C03 xem xét Hard-Margin nguyên bản, còn M14 phân tích mối liên hệ khi siêu tham số phạt $C \\to \\infty$ của Soft-Margin sẽ tiệm cận về đúng bài toán Hard-Margin."
    ),
    "VOAI02-M15": (
        "- **Kernel RBF (Radial Basis Function / Gaussian):** Hàm nhân đo độ tương đồng không gian phi tuyến: $K(x, z) = \\exp(-\\gamma \\|x - z\\|^2)$.\n- **Siêu tham số $\\gamma$ (Gamma):** Nghịch đảo phương sai của phân phối Gauss ($\\gamma = \\frac{1}{2\\sigma^2}$), quyết định bán kính ảnh hưởng của từng điểm hỗ trợ (Support Vector).\n- **Khi $\\gamma$ quá lớn:** Bán kính ảnh hưởng rất hẹp, mô hình chỉ ghi nhớ từng điểm huấn luyện riêng lẻ, tạo ra các đảo ranh giới cục bộ quanh từng điểm $\\implies$ Overfitting nặng.",
        "§1.2 Support Vector Machines (SVM & Kernel Trick)",
        "Liên hệ câu OLP01-C04: Cùng phân tích hành vi của siêu tham số $\\gamma$ trong RBF Kernel: giá trị $\\gamma$ quá lớn làm thu hẹp bán kính ảnh hưởng của từng Support Vector, tạo các ranh giới cục bộ gây Overfitting nghiêm trọng."
    ),
    "VOAI02-M16": (
        "- **Gini Impurity ($I_G$):** Độ đo mức độ không thuần khiết tại một nút cây quyết định: $I_G = 1 - \\sum_{k=1}^K p_k^2$.\n- **Ý nghĩa xác suất:** Xác suất một phần tử ngẫu nhiên bị phân loại sai nếu ta gán nhãn ngẫu nhiên cho nó theo phân phối xác suất của nút.\n- **Nút thuần khiết hoàn toàn:** $I_G = 0$ khi tất cả các mẫu đều thuộc về duy nhất một lớp ($p_1 = 1$).",
        "§1.3 Cây quyết định (Decision Tree), Entropy & Information Gain",
        "Liên hệ câu OLP01-B04: Cùng thuộc bài toán đo độ hỗn loạn của nút trong cây quyết định: OLP01-B04 tính độ đo Entropy Shannon ($-\\sum p_i \\log_2 p_i$), còn M16 tính độ đo Gini Impurity ($1 - \\sum p_i^2$) dùng trong thuật toán CART."
    ),
    "VOAI02-M17": (
        "- **Bootstrap Sampling:** Phương pháp lấy mẫu có hoàn lại kích thước $N$ từ tập $N$ mẫu gốc.\n- **Out-Of-Bag (OOB):** Tập hợp các mẫu không được chọn vào mẫu Bootstrap của một cây con.\n- **Xác suất một mẫu không được chọn:** $(1 - \\frac{1}{N})^N$. Khi $N \\to \\infty$, giới hạn này hội tụ về $\\frac{1}{e} \\approx 0.368$ (khoảng $36.8\\%$).",
        "§1.4 Random Forest & Phương pháp Ensemble",
        "Liên hệ câu OLP01-C17: OLP01-C17 giải thích khả năng giảm phương sai của Random Forest nhờ cơ chế Bagging, còn M17 chứng minh bằng toán học xác suất tỉ lệ $\\approx 36.8\\%$ dữ liệu OOB đóng vai trò như tập kiểm thử độc lập cho từng cây con."
    ),
    "VOAI02-M18": (
        "- **AdaBoost (Adaptive Boosting):** Thuật toán Ensemble tuần tự, tăng trọng số cho các mẫu bị phân loại sai để cây tiếp theo tập trung sửa sai.\n- **Trọng số bộ phân loại ($\\alpha_t$):** $\\alpha_t = \\frac{1}{2} \\ln\\left(\\frac{1-\\epsilon_t}{\\epsilon_t}\\right)$, mô hình nào có tỉ lệ lỗi $\\epsilon_t$ càng thấp thì tiếng nói $\\alpha_t$ càng lớn.\n- **Quy tắc cập nhật:** $w_{t+1, i} \\propto w_{t, i} \\exp(-\\alpha_t y_i h_t(x_i))$. Nếu đoán đúng ($y_i h_t = 1$), trọng số giảm; nếu đoán sai ($y_i h_t = -1$), trọng số nhân thêm $\\exp(\\alpha_t) > 1$.",
        "§1.4 Random Forest & Phương pháp Ensemble",
        "Liên hệ câu VOAI03-M41: VOAI03-M41 phân biệt Bagging (song song) và Boosting (tuần tự), còn M18 phân tích sâu công thức toán học cập nhật trọng số mẫu trong thuật toán nền tảng AdaBoost giúp các cây sau tập trung sửa sai cho các cây trước."
    ),
    "VOAI02-M19": (
        "- **Gradient Boosting truyền thống (GBM):** Sử dụng phép tính xấp xỉ đạo hàm bậc một (Negative Gradient / Pseudo-Residuals) để khớp cây quyết định mới.\n- **XGBoost (Extreme Gradient Boosting):** Sử dụng khai triển Taylor bậc hai của hàm mất mát, kết hợp cả đạo hàm bậc một ($g_i$) và đạo hàm bậc hai ($h_i$) tại mỗi bước tối ưu.\n- **Điều chuẩn hóa trong hàm mục tiêu:** XGBoost đưa trực tiếp số lượng lá ($T$) và trọng số lá ($w$) vào hàm mục tiêu với hệ số $\\gamma$ và $\\lambda$.",
        "§1.4 Random Forest & Phương pháp Ensemble",
        "Liên hệ câu VOAI03-M48: VOAI03-M48 kiểm tra nguyên lý Gradient Boosting truyền thống khớp cây con vào đạo hàm bậc 1, còn M19 phân tích bước tiến của XGBoost khi tối ưu hóa hàm mục tiêu bằng khai triển Taylor bậc hai ($g_i$ và $h_i$)."
    ),
    "VOAI02-M20": (
        "- **GOSS (Gradient-based One-Side Sampling):** Giữ lại toàn bộ các mẫu có gradient lớn (chưa học tốt) và chỉ lấy mẫu ngẫu nhiên một tỉ lệ nhỏ các mẫu có gradient bé.\n- **EFB (Exclusive Feature Bundling):** Gộp các đặc trưng loại trừ lẫn nhau (hiếm khi cùng nhận giá trị khác 0) thành một đặc trưng đơn lẻ để giảm chiều dữ liệu.\n- **Leaf-wise Tree Growth:** Mọc cây theo nhánh có độ giảm hàm mất mát lớn nhất thay vì mọc cân bằng theo tầng (Depth-wise).",
        "§1.4 Random Forest & Phương pháp Ensemble",
        "Liên hệ câu VOAI03-M43: Cùng tìm hiểu các cải tiến hiệu năng của thư viện LightGBM: VOAI03-M43 kiểm tra chiến lược mọc cây theo lá (Leaf-wise), còn M20 kiểm tra 2 kỹ thuật xử lý dữ liệu đột phá GOSS (lọc mẫu theo gradient) và EFB (gộp đặc trưng loại trừ)."
    ),
    "VOAI02-M21": (
        "- **Target Encoding:** Thay thế biến phân loại bằng giá trị trung bình của biến mục tiêu trên từng nhóm danh mục.\n- **Target Leakage:** Sử dụng nhãn của chính mẫu hiện tại để tính toán giá trị mã hóa khiến mô hình ghi nhớ nhãn và overfitting nặng.\n- **Ordered Target Encoding trong CatBoost:** Tính toán mã hóa cho mẫu thứ $i$ chỉ dựa trên các mẫu xuất hiện trước nó theo một thứ tự hoán vị ngẫu nhiên: $\\hat{x}_i = \\frac{\\sum_{j < i} y_j + a \\cdot P}{\\sum_{j < i} 1 + a}$.",
        "§1.10 Tiền xử lý Đặc trưng & Thao tác NumPy",
        "Liên hệ câu VOAI03-M49: Cùng kiểm tra cơ chế chống rò rỉ nhãn (Target Leakage) độc quyền của thuật toán CatBoost: nguyên lý Ordered Target Encoding / Ordered Boosting dựa trên việc bảo toàn thứ tự thời gian giả lập."
    ),
    "VOAI02-M22": (
        "- **SMOTE:** Kỹ thuật sinh mẫu nhân tạo cho lớp thiểu số bằng cách nội suy tuyến tính giữa các điểm dữ liệu láng giềng k-NN.\n- **Quy tắc vàng Cross-Validation:** Mọi thao tác tiền xử lý, chuẩn hóa, và sinh mẫu SMOTE BẮT BUỘC chỉ được áp dụng trên tập huấn luyện (Train Fold).\n- **Data Leakage nguy hiểm:** Nếu áp dụng SMOTE trên toàn bộ dữ liệu trước khi chia K-Fold, các mẫu nhân tạo được tạo ra từ thông tin của tập Validation sẽ rò rỉ vào Train Fold.",
        "§1.9 Xử lý Mất cân bằng lớp (Imbalanced Data)",
        "Liên hệ câu VOAI03-M35: VOAI03-M35 kiểm tra nguyên lý thuật toán SMOTE, còn M22 kiểm tra quy trình thực hành chuẩn để ngăn chặn thảm họa rò rỉ dữ liệu (Data Leakage) khi kết hợp SMOTE với Cross-Validation."
    ),
    "VOAI02-M23": (
        "- **K-Means:** Thuật toán phân cụm dựa trên khoảng cách tâm, giả định các cụm có dạng hình cầu lồi (spherical) và kích thước tương đương, rất nhạy cảm với nhiễu.\n- **HDBSCAN:** Thuật toán phân cụm dựa trên mật độ phân cấp (Hierarchical Density-Based), phát hiện được các cụm có hình dạng hình học phức tạp tùy ý.\n- **Tự động xử lý nhiễu:** HDBSCAN tự động đánh dấu các điểm nằm ở vùng mật độ thấp là Outliers/Noise (nhãn -1) mà không ép chúng vào bất kỳ cụm nào.",
        "§1.8 K-Means Clustering & Silhouette Score",
        "Liên hệ câu OLP01-C18: Cùng thuộc chủ đề học không giám sát phân cụm dữ liệu: OLP01-C18 đánh giá cụm K-Means bằng Silhouette Score, còn M23 so sánh hạn chế cụm hình cầu của K-Means với thuật toán phân cụm mật độ HDBSCAN."
    ),
    "VOAI02-M24": (
        "- **Dữ liệu chuỗi thời gian (Time Series):** Các điểm dữ liệu có tương quan tự phát (Autocorrelation) và phụ thuộc chặt chẽ vào trục thời gian xuôi.\n- **Sai lầm KFold(shuffle=True):** Việc xáo trộn ngẫu nhiên sẽ lấy dữ liệu tương lai để dự đoán quá khứ (Look-ahead bias), làm điểm số validation cao ảo nhưng mô hình sụp đổ khi deploy.\n- **TimeSeriesSplit (Walk-Forward Validation):** Chia dữ liệu theo thứ tự thời gian, tập Train luôn đi trước tập Validation: Train $[0 \\dots t]$, Validation $[t+1 \\dots t+k]$.",
        "§1.5 Overfitting, Underfitting, Bias-Variance Tradeoff & Cross-Validation",
        "Liên hệ câu VOAI03-M50: Cùng kiểm tra nguyên lý kiểm chuẩn mô hình chuỗi thời gian: cả hai câu đều khẳng định K-Fold xáo trộn ngẫu nhiên phá vỡ tính liên tục thời gian và gây Data Leakage nghiêm trọng; bắt buộc phải chia theo trục thời gian xuôi (Rolling-window / TimeSeriesSplit)."
    ),
    "VOAI02-M25": (
        "- **`optimizer.zero_grad()`:** Xóa sạch gradient tích lũy trong các tensor trọng số từ bước trước.\n- **`loss = criterion(model(inputs), targets)`:** Thực hiện lan truyền xuôi (Forward Pass) và tính giá trị hàm mất mát.\n- **`loss.backward()`:** Lan truyền ngược (Backpropagation) tính toán đạo hàm riêng của Loss theo từng tham số.\n- **`optimizer.step()`:** Cập nhật giá trị trọng số theo thuật toán tối ưu: $w \\leftarrow w - \\eta \\nabla_w L$.",
        "§2.3 Lan truyền xuôi, Lan truyền ngược & Vòng lặp Huấn luyện PyTorch",
        "Liên hệ câu OLP01-B13: Cùng kiểm tra thứ tự 4 thao tác cốt lõi trong vòng lặp huấn luyện PyTorch; giải thích bản chất vì sao phải xóa gradient tích lũy trước khi lan truyền ngược."
    ),
    "VOAI02-M26": (
        "- **Symmetry Problem (Vấn đề đối xứng):** Khi khởi tạo toàn bộ trọng số bằng 0, mọi nơ-ron trong cùng một tầng ẩn nhận đầu vào giống nhau và có gradient giống hệt nhau $\\implies$ không thể học các đặc trưng phân hóa.\n- **Khởi tạo He / Kaiming (He et al., 2015):** Khởi tạo trọng số từ phân phối $\\mathcal{N}(0, \\frac{2}{n_{in}})$, được chứng minh toán học là tối ưu để duy trì phương sai kích hoạt ổn định qua các tầng sử dụng ReLU.\n- **Khởi tạo Xavier / Glorot:** Phù hợp với các hàm kích hoạt đối xứng quanh 0 như Tanh và Sigmoid ($\\text{Var} = \\frac{2}{n_{in} + n_{out}}$).",
        "§2.7 Khởi tạo Trọng số (Weight Initialization)",
        "Liên hệ câu OLP01-B14: Cùng kiểm tra chiến lược khởi tạo trọng số mạng sâu: OLP01-B14 chọn phương pháp He Normal/Uniform cho ReLU, còn M26 giải thích thêm nguy cơ phá vỡ tính phân hóa của nơ-ron khi khởi tạo bằng 0."
    ),
    "VOAI02-M27": (
        "- **BatchNorm pha Train (`model.train()`):** Sử dụng giá trị trung bình $\\mu_B$ và phương sai $\\sigma_B^2$ được tính toán trực tiếp trên mini-batch hiện tại để chuẩn hóa.\n- **Running Statistics:** Trong lúc train, mô hình liên tục cập nhật trung bình trượt: $\\mu_{run} = (1-m)\\mu_{run} + m \\mu_B$.\n- **BatchNorm pha Eval (`model.eval()`):** Đóng băng hoàn toàn việc tính toán trên batch; sử dụng cố định các giá trị running_mean và running_var đã tích lũy trong quá trình train.",
        "§2.8 Chuẩn hóa Tầng (Batch Normalization vs Layer Normalization)",
        "Liên hệ câu OLP01-B10: Cùng kiểm tra cơ chế hoạt động của lớp Batch Normalization trong PyTorch: phân biệt sự khác nhau căn bản giữa thống kê batch tức thời lúc train và thống kê tích lũy running stats lúc eval."
    ),
    "VOAI02-M28": (
        "- **Batch Normalization (BN):** Chuẩn hóa theo chiều batch, phụ thuộc chặt chẽ vào kích thước batch và giả định các mẫu có chiều dài bằng nhau.\n- **Độ dài chuỗi biến thiên trong NLP:** Các câu văn trong batch có độ dài rất khác nhau, sử dụng padding token làm sai lệch nghiêm trọng thống kê trung bình và phương sai của batch.\n- **Layer Normalization (LN):** Chuẩn hóa độc lập trên từng mẫu dữ liệu qua toàn bộ các kênh đặc trưng ẩn: $\\mu_L = \\frac{1}{D} \\sum_{i=1}^D x_i$, hoàn toàn không phụ thuộc vào batch size hay các câu khác.",
        "§2.8 Chuẩn hóa Tầng (Batch Normalization vs Layer Normalization)",
        "Liên hệ câu OLP01-C21: Cùng phân tích nguyên nhân LayerNorm là chuẩn mực trong NLP: chuẩn hóa độc lập theo từng mẫu trên chiều đặc trưng (feature dimension), hoàn toàn không phụ thuộc vào kích thước batch hay độ dài chuỗi biến thiên."
    ),
    "VOAI02-M29": (
        "- **Exploding Gradient (Bùng nổ gradient):** Tích của các ma trận trọng số trong chuỗi đạo hàm lan truyền ngược quá lớn khiến gradient tăng theo cấp số nhân.\n- **Hậu quả:** Trọng số nhận giá trị cực đại vượt quá phạm vi dấu phẩy động 32-bit $\\implies$ xuất hiện `NaN` hoặc `Inf`.\n- **Gradient Clipping (`torch.nn.utils.clip_grad_norm_`):** Nếu chuẩn $L_2$ của gradient vượt quá ngưỡng $c$, ta co tỷ lệ toàn bộ vector gradient: $g \\leftarrow g \\cdot \\frac{c}{\\|g\\|_2}$.",
        "§2.10 Gradient Vanishing & Exploding, Early Stopping",
        "Liên hệ câu OLP01-C22: Cùng kiểm tra vấn đề bất ổn định gradient trong mạng sâu và RNN chuỗi dài: M29 tập trung vào giải pháp cắt tỉa gradient (Gradient Clipping) để chặn bùng nổ gradient, bổ trợ cho §2.10."
    ),
    "VOAI02-M30": (
        "- **`nn.CrossEntropyLoss()`:** Trong PyTorch, lớp này tích hợp bên trong cả hàm `nn.LogSoftmax()` và `nn.NLLLoss()` (Negative Log Likelihood).\n- **Đầu vào bắt buộc (Input):** Tensor logit thô chưa qua kích hoạt Softmax, kích thước $(N, C)$ với $C$ là số lớp.\n- **Ổn định số học (Log-Sum-Exp Trick):** Việc gộp Log và Softmax giúp triệt tiêu số mũ cực lớn $e^{z_i}$, ngăn chặn hoàn toàn hiện tượng tràn số (Overflow/Underflow).",
        "§2.4 Các hàm mất mát (Loss Functions)",
        "Liên hệ câu OLP01-B11: Cùng kiểm tra cơ chế kỹ thuật của `nn.CrossEntropyLoss()` trong PyTorch: tích hợp LogSoftmax và Log-Sum-Exp để tối ưu độ ổn định số học, yêu cầu thí sinh đưa trực tiếp raw logits chưa qua Softmax."
    ),
    "VOAI02-M31": (
        "- **`nn.BCELoss` thủ công:** Đòi hỏi đưa đầu vào qua `torch.sigmoid(x)`, sau đó tính $-y \\ln(p) - (1-y)\\ln(1-p)$. Khi $p \\to 0$ hoặc $p \\to 1$, hàm $\\ln(0)$ gây lỗi `NaN`.\n- **`nn.BCEWithLogitsLoss`:** Nhận logit thô $z$ và tính trực tiếp qua công thức toán học hợp nhất: $\\max(z, 0) - z \\cdot y + \\ln(1 + e^{-|z|})$.\n- **Log-Sum-Exp Trick:** Đảm bảo số mũ luôn âm ($-|z| \\le 0$), giá trị $e^{-|z|} \\in (0, 1]$, triệt tiêu hoàn toàn nguy cơ tràn số.",
        "§2.4 Các hàm mất mát (Loss Functions)",
        "Liên hệ câu OLP01-B12: Cùng làm rõ lý do ổn định số học (numerical stability) của `nn.BCEWithLogitsLoss()` thông qua thủ thuật Log-Sum-Exp trong tính toán dấu phẩy động."
    ),
    "VOAI02-M32": (
        "- **Weight Decay trong Adam thông thường:** Thêm $\\lambda w$ trực tiếp vào gradient trước khi tính moment bậc một và bậc hai: $g_t \\leftarrow g_t + \\lambda w$. Điều này khiến các trọng số có gradient lớn bị phạt nhẹ hơn và ngược lại.\n- **AdamW (Decoupled Weight Decay):** Tách hoàn toàn việc suy giảm trọng số ra khỏi cập nhật moment thích nghi: $w_{t+1} = w_t - \\eta_t \\frac{m_t}{\\sqrt{v_t}+\\epsilon} - \\eta_t \\lambda w_t$.\n- **Khôi phục bản chất L2 Regularization:** Giúp mô hình Transformer tổng quát hóa vượt trội trên tập dữ liệu kiểm thử.",
        "§2.5 Thuật toán tối ưu hóa (Optimizers)",
        "Liên hệ câu OLP01-C11: OLP01-C11 phân tích sức mạnh của Adam, còn M32 đi sâu vào công trình đột phá AdamW (Loshchilov & Hutter 2019) tách biệt cơ chế Weight Decay để khôi phục đúng bản chất điều chuẩn L2 cho các bộ tối ưu thích nghi."
    ),
    "VOAI02-M33": (
        "- **Learning Rate Warmup:** Tăng dần tốc độ học từ 0 lên giá trị tối đa trong $N_{warmup}$ bước đầu tiên.\n- **Bản chất vấn đề:** Ở các bước khởi đầu, moment bậc hai $v_t$ của Adam chưa tích lũy đủ thông tin thống kê chính xác, learning rate lớn sẽ làm mô hình cập nhật những bước nhảy hỗn loạn phá hủy trọng số ban đầu.\n- **Cosine Annealing:** Sau pha Warmup, learning rate giảm dần theo đường cong cosin về tiệm cận 0 để hội tụ mượt mà vào cực tiểu chất lượng cao.",
        "§2.6 Learning Rate Scheduling & Warmup",
        "Liên hệ câu OLP01-C12: Cùng phân tích chiến lược lập lịch tốc độ học hiện đại: OLP01-C12 kiểm tra dạng đường cong Cosine Annealing with Warmup, còn M33 giải thích lý do toán học vì sao giai đoạn Warmup ban đầu là tối quan trọng để giữ mô hình không bị chệch hướng khi gradient sơ khai còn nhiễu."
    ),
    "VOAI02-M34": (
        "- **Inverted Dropout:** Trong pha Train, mỗi nơ-ron bị tắt với xác suất $p$; các nơ-ron còn lại được nhân tỷ lệ với hệ số $\\frac{1}{1-p}$.\n- **Bảo toàn kỳ vọng năng lượng:** $\\mathbb{E}[\\tilde{x}] = (1-p) \\cdot \\frac{x}{1-p} + p \\cdot 0 = x$, kỳ vọng kích hoạt lúc train bằng đúng kỳ vọng lúc test.\n- **Lợi ích thực tế:** Trong pha suy luận (`model.eval()`), mô hình chỉ việc giữ nguyên trọng số và chạy thẳng mà không cần bất kỳ phép toán co tỷ lệ nào.",
        "§2.9 Dropout & Tránh Overfitting",
        "Liên hệ câu OLP01-B10: Làm rõ kỹ thuật Inverted Dropout trong PyTorch: nhân hệ số tỷ lệ $\\frac{1}{1-p}$ ngay lúc huấn luyện để giữ nguyên kỳ vọng kích hoạt, giúp pha suy luận (model.eval()) diễn ra hoàn toàn tự nhiên không cần scaling."
    ),
    "VOAI02-M35": (
        "- **L1 Regularization (Lasso):** Vùng ràng buộc có dạng hình khối thoi nhiều góc nhọn (cross-polytope / diamond shape) nằm chính xác trên các trục tọa độ.\n- **Nghiệm thưa (Sparsity):** Các đường đồng mức của hàm mất mát có xu hướng tiếp xúc với góc nhọn của hình thoi trước tiên, khiến nhiều tọa độ trọng số bị triệt tiêu về đúng bằng 0.\n- **L2 Regularization (Ridge):** Vùng ràng buộc là hình cầu trơn (hypersphere) không có góc nhọn $\\implies$ điểm tiếp xúc hiếm khi nằm trên trục tọa độ, trọng số chỉ bị co nhỏ về gần 0.",
        "§1.6 Regularization L1 (Lasso) vs L2 (Ridge) vs ElasticNet",
        "Liên hệ câu OLP01-C09: Cùng đối chiếu L1 vs L2: OLP01-C09 nêu kết luận ứng dụng lựa chọn đặc trưng của L1, còn M35 giải thích trực quan hình học dựa trên đường đồng mức (contour lines) và hình học lồi của siêu mặt cầu $L_1$ và $L_2$."
    ),
    "VOAI02-M36": (
        "- **Patience (Độ kiên nhẫn):** Số epoch liên tiếp mà độ đo theo dõi trên tập validation (thường là Validation Loss) không cải thiện trước khi quyết định dừng huấn luyện.\n- **Model Checkpointing:** Luôn lưu lại bộ trọng số tại epoch có Validation Loss thấp nhất (Best Checkpoint).\n- **Ngăn chặn Overfitting:** Tránh dừng quá sớm khi gặp biến động ngẫu nhiên cục bộ, đồng thời đảm bảo không lấy trọng số ở epoch cuối cùng khi mô hình đã bắt đầu thoái hóa.",
        "§2.10 Gradient Vanishing & Exploding, Early Stopping",
        "Liên hệ câu VOAI03-M40: Cùng kiểm tra cơ chế Early Stopping: VOAI03-M40 xác định tín hiệu dừng dựa trên Validation Loss, còn M36 chi tiết hóa vai trò của tham số `patience` và nguyên tắc Model Checkpointing lưu lại trọng số tối ưu nhất thay vì trọng số của epoch cuối cùng."
    ),
    "VOAI02-M37": (
        "- **Công thức kích thước đầu ra Conv2D:** $W_{out} = \\left\\lfloor \\frac{W_{in} - K + 2P}{S} \\right\\rfloor + 1$.\n- **Các tham số:** $W_{in}$ là kích thước đầu vào, $K$ là kích thước kernel, $P$ là padding, $S$ là stride.\n- **Tính toán thực tế:** Đầu vào $224 \\times 224$, $K=7, P=3, S=2$: $W_{out} = \\left\\lfloor \\frac{224 - 7 + 2(3)}{2} \\right\\rfloor + 1 = \\left\\lfloor \\frac{223}{2} \\right\\rfloor + 1 = 111 + 1 = 112$.",
        "§3.1 Lớp Convolution & Công thức Kích thước Đầu ra",
        "Liên hệ câu VOAI03-M16: VOAI03-M16 đưa ra công thức tổng quát $\\lfloor\\frac{W - K + 2P}{S}\\rfloor + 1$, còn M37 là bài toán áp dụng số thực tế cho tầng tích chập đầu tiên kinh điển của ResNet ($224 \\to 112$)."
    ),
    "VOAI02-M38": (
        "- **Receptive Field (Trường thụ cảm):** Hai lớp Conv $3 \\times 3$ xếp chồng có receptive field tương đương một lớp $5 \\times 5$: $RF = 3 + (3-1) = 5$.\n- **Tiết kiệm tham số:** Hai lớp $3 \\times 3$ tốn $2 \\times (3^2 \\cdot C^2) = 18 C^2$ tham số, trong khi một lớp $5 \\times 5$ tốn $5^2 \\cdot C^2 = 25 C^2$ tham số (giảm $\\approx 28\\%$).\n- **Tăng tính phi tuyến:** Giữa hai lớp $3 \\times 3$ có thêm một hàm kích hoạt phi tuyến (như ReLU), giúp mạng học được các hàm phức tạp hơn.",
        "§3.3 Các Kiến trúc CNN Kinh Điển",
        "Liên hệ câu OLP01-C13: Cùng kiểm tra nguyên lý thiết kế đột phá của VGGNet: xếp chồng các kernel nhỏ $3 \\times 3$ để mở rộng Receptive Field mà vẫn tiết kiệm tham số tính toán và tăng chiều sâu biểu diễn phi tuyến."
    ),
    "VOAI02-M39": (
        "- **Global Average Pooling (GAP):** Phép toán tính trung bình cộng toàn bộ các giá trị không gian trên từng feature map: $\\text{GAP}(F_c) = \\frac{1}{H \\cdot W} \\sum_{h, w} F_c(h, w)$.\n- **Thay thế Fully Connected Layers:** Biến đổi trực tiếp tensor $(N, C, H, W)$ thành vector $(N, C)$ đưa thẳng vào bộ phân loại.\n- **Chống Overfitting & Giảm tham số:** Loại bỏ hàng chục triệu trọng số dễ gây quá khớp của các tầng Dense truyền thống, đồng thời tăng tính bất biến đối với phép dịch chuyển.",
        "§3.3 Các Kiến trúc CNN Kinh Điển",
        "Câu hỏi lý thuyết độc lập về kỹ thuật GAP trong kiến trúc Network In Network và ResNet, loại bỏ hoàn toàn các tầng kết nối đầy đủ (Fully Connected) chiếm 80-90% tham số trong các mạng cổ điển (§3.3)."
    ),
    "VOAI02-M40": (
        "- **Residual Connection (Kết nối tắt):** Đầu ra khối mạng cộng thêm đầu vào trực tiếp: $y = \\mathcal{F}(x, \\{W_i\\}) + x$.\n- **Giải tích đạo hàm:** Khi lan truyền ngược, đạo hàm theo đầu vào là $\\frac{\\partial y}{\\partial x} = \\frac{\\partial \\mathcal{F}}{\\partial x} + 1$.\n- **Triệt tiêu tiêu biến gradient:** Dù đạo hàm $\\frac{\\partial \\mathcal{F}}{\\partial x}$ có suy giảm tiệm cận về 0 qua các tầng sâu, số hạng $+1$ vẫn đảm bảo gradient được truyền nguyên vẹn ngược về các tầng đầu tiên.",
        "§3.4 Skip Connection: ResNet (ADD) vs U-Net (CONCAT)",
        "Liên hệ câu OLP01-C22: OLP01-C22 nêu hiện tượng suy thoái hiệu năng khi mạng quá sâu, còn M40 giải thích về mặt giải tích số hạng đạo hàm $+1$ trong kết nối tắt (Skip Connection) của ResNet giải quyết triệt để vấn đề này."
    ),
    "VOAI02-M41": (
        "- **U-Net Architecture:** Mạng nơ-ron phân đoạn ảnh gồm nhánh co (Encoder) và nhánh mở rộng (Decoder) đối xứng.\n- **Skip Connection Concatenate:** Ghép nối trực tiếp các feature map độ phân giải cao từ Encoder sang Decoder theo chiều channel.\n- **Khôi phục chi tiết không gian:** Bù đắp lượng thông tin vị trí không gian tinh xảo bị mất đi qua các tầng Max Pooling, giúp vẽ chính xác ranh giới của các phân vùng ảnh.",
        "§3.4 Skip Connection: ResNet (ADD) vs U-Net (CONCAT)",
        "Liên hệ câu OLP01-C23: Cùng kiểm tra cơ chế Skip Connection trong mạng phân vùng ảnh U-Net: phép nối ghép kênh (Concatenation) dọc theo chiều channel giúp bảo toàn nguyên vẹn tọa độ pixel ranh giới vật thể."
    ),
    "VOAI02-M42": (
        "- **Vision Transformer (ViT):** Chia ảnh kích thước $H \\times W \\times C$ thành lưới $N$ patch vuông kích thước $P \\times P$.\n- **Số lượng patch:** $N = \\frac{H \\cdot W}{P^2} = \\frac{224 \\cdot 224}{16 \\cdot 16} = 14 \\times 14 = 196$ patch.\n- **[CLS] Token:** Bổ sung thêm 1 token đặc biệt có thể học ở đầu chuỗi để đại diện cho toàn bộ bức ảnh $\\implies$ Tổng cộng $196 + 1 = 197$ token.\n- **Kích thước tensor đầu vào:** $[197, D]$ với $D = 768$ (ViT-Base).",
        "§3.5 Vision Transformer (ViT — Dosovitskiy et al., 2020)",
        "Liên hệ câu OLP01-C24: OLP01-C24 mô tả nguyên lý chia ảnh thành chuỗi patch phẳng và chiếu tuyến tính trong ViT, còn M42 yêu cầu tính toán cụ thể số lượng token ($196 + 1 = 197$) và kích thước tensor biểu diễn."
    ),
    "VOAI02-M43": (
        "- **Tọa độ Bounding Box:** Định dạng $[x_1, y_1, x_2, y_2]$ với diện tích $\\text{Area} = (x_2 - x_1) \\cdot (y_2 - y_1)$.\n- **Diện tích từng hộp:** Box A: $(50-10)(50-10) = 1600$; Box B: $(70-30)(70-30) = 1600$.\n- **Phần giao nhau (Intersection):** $[\\max(10, 30), \\max(10, 30), \\min(50, 70), \\min(50, 70)] = [30, 30, 50, 50] \\implies \\text{Area}_I = 20 \\times 20 = 400$.\n- **Chỉ số IoU:** $\\text{IoU} = \\frac{\\text{Area}_I}{\\text{Area}_A + \\text{Area}_B - \\text{Area}_I} = \\frac{400}{1600 + 1600 - 400} = \\frac{400}{2800} = \\frac{1}{7} \\approx 0.143$.",
        "§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN",
        "Liên hệ câu OLP01-B06: Cùng kiểm tra công thức tính chỉ số IoU (Intersection over Union) giữa hai hộp giới hạn: OLP01-B06 cho sẵn diện tích giao và hợp, còn M43 yêu cầu tính trực tiếp từ tọa độ hộp $[x_1, y_1, x_2, y_2]$."
    ),
    "VOAI02-M44": (
        "- **NMS (Non-Maximum Suppression):** Thuật toán hậu xử lý loại bỏ các bounding box dự đoán dư thừa bọc quanh cùng một đối tượng.\n- **Bước 1:** Lọc bỏ các box có điểm tin cậy (Confidence Score) thấp hơn ngưỡng $\\theta_{conf}$.\n- **Bước 2:** Sắp xếp các box còn lại theo thứ tự điểm tin cậy giảm dần.\n- **Bước 3 & 4:** Chọn box có điểm cao nhất lưu vào tập kết quả; tính IoU giữa box này với tất cả các box còn lại và loại bỏ bất kỳ box nào có $\\text{IoU} \\ge \\theta_{NMS}$. Lặp lại cho đến hết.",
        "§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN",
        "Liên hệ câu OLP01-C15: OLP01-C15 nêu vai trò loại bỏ các bounding box dư thừa của NMS, còn M44 chi tiết hóa từng bước thực thi trong pipeline thuật toán."
    ),
    "VOAI02-M45": (
        "- **mAP (Mean Average Precision):** Chỉ số đánh giá tổng thể độ chính xác phát hiện vật thể trên toàn bộ các lớp đối tượng.\n- **Ngưỡng IoU đơn lẻ (mAP@0.50):** Chỉ yêu cầu hộp dự đoán có $\\text{IoU} \\ge 0.50$ với nhãn thực tế là được tính là True Positive.\n- **Chuẩn COCO mAP@[0.5:0.95]:** Trung bình cộng của 10 giá trị mAP tính tại 10 ngưỡng IoU cách đều nhau từ 0.50 đến 0.95 với bước nhảy 0.05 ($0.50, 0.55, \\dots, 0.95$), đòi hỏi mô hình phải bám viền cực kỳ chuẩn xác.",
        "§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN",
        "Làm rõ thước đo đánh giá độ chính xác tiêu chuẩn COCO mAP@[0.5:0.95] đòi hỏi mô hình vừa định danh đúng lớp vừa dự đoán hộp bám sát biên giới hạn ở nhiều mức độ khắt khe IoU (§3.6)."
    ),
    "VOAI02-M46": (
        "- **One-Stage Detector (YOLO, SSD, RetinaNet):** Dự đoán trực tiếp tọa độ bounding box và phân loại lớp từ feature map chỉ qua một lượt forward duy nhất, tốc độ cực cao ($> 30$ FPS), lý tưởng cho thiết bị nhúng.\n- **Two-Stage Detector (Faster R-CNN):** Gồm 2 giai đoạn: sinh vùng đề xuất (RPN) rồi mới trích xuất đặc trưng và phân loại, độ chính xác cao hơn trên vật thể nhỏ nhưng tốc độ chậm.\n- **Sự đánh đổi:** 1-stage ưu tiên tốc độ xử lý thời gian thực, chấp nhận đánh đổi một phần độ chính xác khi phát hiện các vật thể kích thước siêu nhỏ hoặc chen chúc dày đặc.",
        "§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN",
        "Liên hệ câu OLP01-C16: Cùng so sánh sự đánh đổi giữa 1-stage và 2-stage detector: tốc độ xử lý thời gian thực (FPS) đối lập với độ chính xác định vị và nhận diện vật thể nhỏ."
    ),
    "VOAI02-M47": (
        "- **DeepFake / AI-Generated Artifacts:** Ảnh do AI sinh ra thường có độ hoàn thiện thị giác bề mặt rất cao nhưng để lại các dấu vết bất thường ở miền tần số và kết cấu vi mô.\n- **32 đặc trưng vật lý kết cấu:** Bao gồm gradient Sobel, toán tử Laplacian bậc 2, Gaussian residual và tính chu kỳ của ma trận lượng hóa JPEG $8 \\times 8$.\n- **Bản chất ưu việt:** Các mô hình CNN thông thường dễ bị đánh lừa bởi ngữ nghĩa vĩ mô; việc trích xuất tường minh các đặc trưng thống kê tần số cao giúp bóc trần sự thiếu tự nhiên của ảnh giả mạo.",
        "§3.8 Mô hình Sinh ảnh: GAN vs Diffusion vs Autoencoder",
        "Liên hệ câu VOAI03-E03: M47 kiểm tra lý thuyết về 32 đặc trưng kết cấu vật lý và vi sai nén JPEG, là nền tảng trực tiếp để giải quyết bài toán tự luận thiết kế hệ thống phát hiện ảnh giả mạo trong VOAI03-E03."
    ),
    "VOAI02-M48": (
        "- **MixUp (Zhang et al., 2017):** Kỹ thuật điều chuẩn tăng cường dữ liệu dựa trên phép nội suy lồi giữa hai mẫu ngẫu nhiên.\n- **Công thức nội suy:** $\\tilde{x} = \\lambda x_i + (1-\\lambda) x_j$ và $\\tilde{y} = \\lambda y_i + (1-\\lambda) y_j$ với $\\lambda \\sim \\text{Beta}(\\alpha, \\alpha)$.\n- **Hiệu ứng học máy:** Khuyến khích mô hình có hành vi tuyến tính giữa các lớp dữ liệu, làm mượt ranh giới quyết định và tăng cường khả năng chống chịu nhiễu đối kháng (Adversarial Robustness).",
        "§3.9 Data Augmentation & Transfer Learning",
        "Câu hỏi độc lập về kỹ thuật tăng cường dữ liệu kết hợp tuyến tính MixUp (Zhang et al.), giúp làm trơn bề mặt quyết định và tăng cường tính ổn định của mô hình (§3.9)."
    ),
    "VOAI02-M49": (
        "- **Text Preprocessing Pipeline:** Quy trình tiền xử lý văn bản thô theo trình tự logic bất biến.\n- **Bước 1 & 2:** Làm sạch ký tự đặc biệt, chuyển chữ thường (Lowercasing) và chuẩn hóa bảng mã Unicode.\n- **Bước 3:** Tách từ (Tokenization) chia văn bản thành các token đơn lẻ.\n- **Bước 4 & 5:** Loại bỏ từ dừng (Stopwords), chuẩn hóa từ gốc (Stemming/Lemmatization), sau đó mới thực hiện Vector hóa (TF-IDF / Embedding).",
        "§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn",
        "Liên hệ câu OLP01-C28: Cùng kiểm tra thứ tự logic bất biến trong pipeline tiền xử lý văn bản kinh điển: làm sạch, tách từ, lọc stopwords, chuẩn hóa từ gốc rồi mới vector hóa đặc trưng."
    ),
    "VOAI02-M50": (
        "- **CBOW (Continuous Bag-of-Words):** Sử dụng các từ ngữ cảnh xung quanh để dự đoán từ trung tâm mục tiêu $w_t$; tốc độ huấn luyện nhanh, biểu diễn tốt các từ xuất hiện thường xuyên.\n- **Skip-gram:** Sử dụng từ trung tâm $w_t$ để dự đoán các từ ngữ cảnh xung quanh trong cửa sổ; hoạt động xuất sắc với các tập dữ liệu nhỏ và biểu diễn cực tốt các từ hiếm gặp.\n- **Negative Sampling:** Kỹ thuật xấp xỉ mẫu âm giúp giảm độ phức tạp tính toán mẫu số Softmax từ $|V|$ xuống $k$ từ ngẫu nhiên.",
        "§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)",
        "Liên hệ câu VOAI03-M21: VOAI03-M21 nêu nhược điểm mất ngữ cảnh của BoW, dẫn dắt tới sự ra đời của Word2Vec trong M50 với hai cơ chế đối ngẫu: CBOW (ngữ cảnh đoán từ) và Skip-gram (từ đoán ngữ cảnh)."
    ),
    "VOAI02-M51": (
        "- **Cosine Similarity:** Độ đo góc giữa hai vector không gian đặc trưng: $\\cos(u, v) = \\frac{u \\cdot v}{\\|u\\|_2 \\|v\\|_2}$.\n- **Tích vô hướng:** $u \\cdot v = (1)(2) + (2)(0) + (2)(1) = 2 + 0 + 2 = 4$.\n- **Độ dài vector:** $\\|u\\| = \\sqrt{1^2 + 2^2 + 2^2} = \\sqrt{9} = 3$; $\\|v\\| = \\sqrt{2^2 + 0^2 + 1^2} = \\sqrt{5}$.\n- **Kết quả:** $\\cos(u, v) = \\frac{4}{3 \\sqrt{5}} = \\frac{4}{3 \\times 2.236} \\approx 0.596$.",
        "§4.3 Cosine Similarity",
        "Liên hệ câu OLP01-B09: Cùng kiểm tra phép tính độ tương đồng Cosine $\\frac{u \\cdot v}{\\|u\\| \\|v\\|}$ giữa hai vector embedding: OLP01-B09 tính trong không gian 2D, còn M51 tính trong không gian 3D."
    ),
    "VOAI02-M52": (
        "- **LSTM Forget Gate ($f_t$):** $f_t = \\sigma(W_f [h_{t-1}, x_t] + b_f)$, quyết định tỷ lệ thông tin nào từ ô nhớ cũ $C_{t-1}$ sẽ bị xóa bỏ (0: xóa hoàn toàn, 1: giữ nguyên vẹn).\n- **Cấu trúc GRU (Gated Recurrent Unit):** Loại bỏ ô nhớ trạng thái $C_t$, gộp trạng thái ẩn và tinh giản còn duy nhất 2 cổng: Cổng cập nhật (Update Gate $z_t$) và Cổng đặt lại (Reset Gate $r_t$).\n- **Lợi thế của GRU:** Ít tham số hơn $\\approx 25\\%$, tốc độ huấn luyện nhanh hơn và ít bị quá khớp trên tập dữ liệu nhỏ.",
        "§4.4 Mạng Nơ-ron Hồi Quy: RNN, LSTM & GRU",
        "Liên hệ câu VOAI03-M15: Cùng kiểm tra vai trò của Cổng quên (Forget Gate) trong kiến trúc LSTM và sự tiến hóa tinh giản sang GRU (chỉ gồm Reset Gate và Update Gate)."
    ),
    "VOAI02-M53": (
        "- **Scaled Dot-Product Attention:** $\\text{Attention}(Q, K, V) = \\text{Softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V$.\n- **Vấn đề khi $d_k$ lớn:** Tích vô hướng $Q K^T = \\sum_{i=1}^{d_k} q_i k_i$. Nếu các thành phần có trung bình 0 và phương sai 1, phương sai của tích vô hướng sẽ bằng $d_k$.\n- **Bão hòa Softmax:** Với $d_k$ lớn (ví dụ 64 hoặc 128), các giá trị tích vô hướng trở nên cực lớn, đẩy hàm Softmax vào vùng có đạo hàm tiệm cận 0 $\\implies$ gradient tiêu biến hoàn toàn.",
        "§4.5 Kiến trúc Transformer (Vaswani et al., 2017)",
        "Câu hỏi độc lập đào sâu bản chất toán học của hệ số tỷ lệ $\\frac{1}{\\sqrt{d_k}}$ trong cơ chế Scaled Dot-Product Attention: duy trì phương sai bằng 1 để Softmax không bị đẩy vào vùng bão hòa gradient (§4.5)."
    ),
    "VOAI02-M54": (
        "- **Multi-Head Attention (MHA):** Chiếu tuyến tính $Q, K, V$ thành $h$ không gian biểu diễn con khác nhau với số chiều $d_k = d_{model} / h$.\n- **Đa dạng góc nhìn biểu diễn:** Một đầu chú ý có thể tập trung vào quan hệ cú pháp (động từ - tân ngữ), đầu khác tập trung vào quan hệ thực thể, đầu khác tập trung vào vị trí lân cận.\n- **Single-Head Attention hạn chế:** Chỉ tính toán trung bình một phân phối chú ý duy nhất, làm mất đi khả năng nắm bắt đồng thời nhiều loại tương quan phức tạp trong câu.",
        "§4.5 Kiến trúc Transformer (Vaswani et al., 2017)",
        "Câu hỏi độc lập về lý do kiến trúc Multi-Head Attention vượt trội hơn Single-Head Attention: mở rộng khả năng nắm bắt đa góc độ quan hệ ngữ nghĩa trong câu (§4.5)."
    ),
    "VOAI02-M55": (
        "- **Sinusoidal Positional Encoding:** $PE_{(pos, 2i)} = \\sin\\left(\\frac{pos}{10000^{2i/d}}\\right)$, $PE_{(pos, 2i+1)} = \\cos\\left(\\frac{pos}{10000^{2i/d}}\\right)$.\n- **Biến đổi tuyến tính vị trí tương đối:** Với mọi độ lệch khoảng cách cố định $k$, tồn tại một ma trận biến đổi tuyến tính $M_k$ sao cho $PE_{pos+k} = M_k \\cdot PE_{pos}$.\n- **Khả năng ngoại suy (Extrapolation):** Cho phép mô hình dễ dàng học cách chú ý đến khoảng cách tương đối giữa các token, và có thể suy luận trên các chuỗi dài hơn độ dài đã thấy lúc huấn luyện.",
        "§4.5 Kiến trúc Transformer (Vaswani et al., 2017)",
        "Câu hỏi độc lập về ưu điểm toán học tuyệt vời của mã hóa vị trí hàm sin/cos trong Transformer: cho phép mô hình dễ dàng học cách chú ý theo khoảng cách tương đối (§4.5)."
    ),
    "VOAI02-M56": (
        "- **BERT (Devlin et al., 2018):** Kiến trúc Encoder-only, sử dụng cơ chế chú ý hai chiều tự do (Bi-directional Self-Attention); mục tiêu tiền huấn luyện là Masked Language Modeling (MLM) và Next Sentence Prediction (NSP).\n- **GPT (Radford et al., 2018):** Kiến trúc Decoder-only, sử dụng cơ chế chú ý nhân quả một chiều (Causal Masked Self-Attention) chỉ nhìn về các token quá khứ; mục tiêu tiền huấn luyện là Causal Language Modeling (Autoregressive Next Token Prediction).\n- **Phạm vi ứng dụng:** BERT tối ưu cho hiểu văn bản (NLU: phân loại, trích xuất thực thể); GPT tối ưu cho sinh ngôn ngữ tự nhiên (NLG: viết tiếp, hội thoại, lập luận).",
        "§4.6 So sánh BERT vs GPT",
        "Liên hệ câu OLP01-C30: OLP01-C30 ứng dụng BERT (Encoder-only) cho phân loại và GPT (Decoder-only) cho sinh văn bản, còn M56 đi sâu vào bản chất kiến trúc chú ý 2 chiều vs 1 chiều và mục tiêu tiền huấn luyện của chúng."
    ),
    "VOAI02-M57": (
        "- **SacreBLEU:** Bản chuẩn hóa của độ đo BLEU với tokenization cố định, tránh sai lệch điểm số giữa các cách tiền xử lý khác nhau.\n- **Brevity Penalty (BP):** Hệ số phạt độ ngắn: $\\text{BP} = \\exp\\left(\\min\\left(0, 1 - \\frac{r}{c}\\right)\\right)$ với $c$ là độ dài bản dịch máy và $r$ là độ dài bản dịch tham chiếu.\n- **Tính toán:** Với $c = 2$ và $r = 10$: $1 - \\frac{r}{c} = 1 - 5 = -4 \\implies \\text{BP} = \\exp(-4) \\approx 0.0183$. Toàn bộ điểm số BLEU bị nhân với $0.0183$ (phạt gần như triệt tiêu về 0).",
        "§4.7 Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity",
        "Liên hệ câu OLP01-E02: M57 kiểm tra công thức tính hệ số phạt độ ngắn Brevity Penalty của độ đo SacreBLEU, là metric cốt lõi đánh giá chất lượng mô hình trong bài tự luận Dịch máy OLP01-E02."
    ),
    "VOAI02-M58": (
        "- **BLEU (Bilingual Evaluation Understudy):** Đo lường độ chuẩn xác (Precision-oriented), tính tỉ lệ các n-gram trong câu dịch máy xuất hiện trong câu tham chiếu.\n- **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** Đo lường độ bao phủ (Recall-oriented), tính tỉ lệ các n-gram trong câu tham chiếu được mô hình khôi phục lại trong bản tóm tắt.\n- **Ứng dụng chuẩn mực:** BLEU là thước đo mặc định cho bài toán Dịch máy (Machine Translation); ROUGE là thước đo mặc định cho bài toán Tóm tắt văn bản (Text Summarization).",
        "§4.7 Các Độ Đo trong NLP: BLEU, SacreBLEU, ROUGE & Perplexity",
        "Câu hỏi độc lập làm rõ sự khác biệt triết lý giữa BLEU (hướng tới Precision cho dịch máy) và ROUGE (hướng tới Recall cho tóm tắt văn bản) (§4.7)."
    ),
    "VOAI02-M59": (
        "- **RAG (Retrieval-Augmented Generation):** Kiến trúc kết hợp truy xuất tri thức bên ngoài để tăng cường ngữ cảnh cho mô hình ngôn ngữ lớn.\n- **Giai đoạn 1 (Fast Dense/Sparse Retrieval):** Sử dụng Bi-Encoder (như BGE, Contriever) hoặc Hybrid BM25 để truy xuất nhanh top 50-100 tài liệu ứng viên từ hàng triệu văn bản.\n- **Giai đoạn 2 (Cross-Encoder Re-ranking):** Sử dụng Cross-Encoder (như BGE-Reranker, Cohere Rerank) tính toán attention chéo giữa câu hỏi và từng đoạn văn để xếp hạng lại cực kỳ chính xác top 3-5 tài liệu đưa vào prompt LLM.",
        "§4.3 Cosine Similarity",
        "Liên hệ câu VOAI03-M23: VOAI03-M23 nêu vai trò cốt lõi của RAG trong việc giảm ảo giác và cập nhật tri thức cho LLM, còn M59 phân tích kiến trúc truy xuất 2 giai đoạn (Bi-Encoder kết hợp Cross-Encoder Re-ranker) trong hệ thống RAG doanh nghiệp thực tế."
    ),
    "VOAI02-M60": (
        "- **Autoregressive Generation:** Mỗi bước suy luận, mô hình LLM sinh ra đúng 1 token mới và nối vào chuỗi đầu vào để dự đoán token tiếp theo.\n- **Không có KV Cache:** Tại bước $T$, mô hình phải tính lại toàn bộ ma trận Key và Value cho tất cả $T$ token từ đầu $\\implies$ Độ phức tạp mỗi bước là $O(T)$ và toàn bộ quá trình sinh là $O(T^2)$.\n- **Có KV Cache:** Lưu trữ các tensor Key và Value đã tính ở các bước trước trong GPU VRAM; mỗi bước chỉ cần chiếu duy nhất token mới $\\implies$ Độ phức tạp mỗi bước giảm xuống $O(1)$ phép chiếu vector.",
        "§4.5 Kiến trúc Transformer (Vaswani et al., 2017)",
        "Liên hệ câu VOAI03-M30: Cùng kiểm tra cơ chế KV Cache trong phục vụ mô hình ngôn ngữ lớn: VOAI03-M30 nêu định nghĩa kỹ thuật, còn M60 phân tích mức độ tối ưu hóa độ phức tạp tính toán của từng bước sinh token tự hồi quy."
    ),
}


def clean_markdown_and_enrich(explanation_text, qid):
    """Chuẩn hóa khối 1 và khối 4 mà không làm mất nội dung toán khối 2 và 3."""
    if qid not in TOPIC_ENRICHMENTS:
        return explanation_text

    terms_text, section_str, link_str = TOPIC_ENRICHMENTS[qid]

    # 1. Chuẩn hóa Khối 1: ELI5
    # Tìm khối 1 hiện tại
    # Mẫu chung: ### 1. ELI5 ... đến trước ### 2.
    k1_match = re.search(r'(### 1\. ELI5[^\n]*\n)(.*?)(?=\n### 2\.|\Z)', explanation_text, re.DOTALL)
    if k1_match:
        k1_header = k1_match.group(1)
        k1_body = k1_match.group(2).strip()

        # Bóc tách phần hình dung em bé (nếu có)
        baby_visual = ""
        baby_match = re.search(r'(🍼 \*\*Hình dung thực tế cho em bé:\*\*.*)', k1_body, re.DOTALL)
        if baby_match:
            baby_visual = "\n\n" + baby_match.group(1).strip()
        else:
            # Fallback nếu dùng định dạng khác
            lines = [l for l in k1_body.split('\n') if not l.startswith('- **') and not 'Thuật ngữ mới' in l]
            remaining = "\n".join(lines).strip()
            if remaining:
                baby_visual = "\n\n🍼 **Hình dung thực tế cho em bé:**\n" + remaining

        new_k1 = f"### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)\n👶 **Thuật ngữ mới cần hiểu trước:**\n{terms_text}{baby_visual}\n"
        explanation_text = explanation_text[:k1_match.start()] + new_k1 + explanation_text[k1_match.end():]

    # 2. Chuẩn hóa Khối 4: Mắt xích kiến thức & Liên hệ bài cũ
    new_k4 = (
        f"\n### 4. Mắt xích kiến thức & Liên hệ bài học\n"
        f"📚 **Căn cứ lý thuyết:** Xem **{section_str}**.\n"
        f"🔗 **Mắt xích & Liên hệ bài học:** {link_str}"
    )

    k4_match = re.search(r'\n### 4\. (?:Mắt xích kiến thức|Căn cứ lý thuyết).*', explanation_text, re.DOTALL)
    if k4_match:
        explanation_text = explanation_text[:k4_match.start()] + new_k4
    else:
        explanation_text = explanation_text.rstrip() + "\n" + new_k4

    return explanation_text.strip()


def run():
    print("-> Đang nạp src/data/exams/olp-02.json...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    for q in data["questions"]:
        qid = q["id"]
        if qid in TOPIC_ENRICHMENTS:
            old_exp = q.get("explanation", "")
            new_exp = clean_markdown_and_enrich(old_exp, qid)
            q["explanation"] = new_exp
            updated_count += 1

    print(f"-> Đã chuẩn hóa nội dung cho {updated_count}/60 câu trắc nghiệm Đề 02.")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("-> Đã lưu đè thành công src/data/exams/olp-02.json.")

    # Đồng bộ sang Markdown: content/02-de-chuan-format-voai-expand.md
    if os.path.exists(md_path):
        print("-> Đang đồng bộ sang content/02-de-chuan-format-voai-expand.md...")
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        for q in data["questions"]:
            qid = q["id"]
            if qid in TOPIC_ENRICHMENTS:
                pattern = rf"(### Câu {re.escape(qid)}:.*?\*\*Lời giải chi tiết:\*\*\n)(.*?)(?=\n---\n|### Câu |\Z)"
                exp_text = q['explanation']
                md_content = re.sub(pattern, lambda m, exp=exp_text: f"{m.group(1)}\n{exp}\n", md_content, flags=re.DOTALL)

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print("-> Đã đồng bộ hoàn tất sang content/02-de-chuan-format-voai-expand.md.")


if __name__ == "__main__":
    run()
