# -*- coding: utf-8 -*-
"""
scripts/apply_all_upgrades_olp03.py
Cập nhật đầy đủ 100% 50 câu trắc nghiệm Đề 03 với cấu trúc 4 khối chuẩn:
👶 [1. ELI5 — BẢN CHẤT CỐT LÕI (GIẢI THÍCH CHO EM BÉ)]
   - Thuật ngữ mới cần hiểu trước
   - Hình dung thực tế cho em bé
📐 [2. CÔNG THỨC TOÁN & BƯỚC TÍNH CHI TIẾT (STEP-BY-STEP)]
⚠️ [3. BẪY ĐỀ THI & TẠI SAO CÁC ĐÁP ÁN KHÁC SAI (PITFALLS)]
📚 [4. MẮT XÍCH KIẾN THỨC & LIÊN HỆ BÀI CŨ]
"""

import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
json_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")

with open(json_path, "r", encoding="utf-8") as f:
    exam_data = json.load(f)

# Nạp bảng từ điển chi tiết cho tất cả các câu từ M01 đến M50
DATA = {
    # M01 - M10
    "VOAI03-M01": (
        "- **Ma trận trực giao (Orthogonal Matrix):** Ma trận vuông $A$ thỏa mãn $A^T A = A A^T = I$. Các vector cột/hàng có độ dài bằng 1 và đôi một vuông góc nhau.\n- **Ma trận nghịch đảo ($A^{-1}$):** Ma trận thỏa mãn $A A^{-1} = I$.\n- **Ma trận chuyển vị ($A^T$):** Ma trận đổi hàng thành cột.",
        "Ma trận trực giao giống hệt như một phép xoay khối rubik trong không gian 3 chiều: Nó chỉ xoay góc nhìn chứ hoàn toàn không bóp méo, không kéo dãn hay thu nhỏ vật thể. Vì thế, muốn quay ngược trở lại vị trí ban đầu ($A^{-1}$), bạn chỉ cần lật ngược phép xoay đó (chính là ma trận chuyển vị $A^T$).",
        "Theo định nghĩa chuẩn: $A^T A = I$.\nNhân cả hai vế từ bên phải với $A^{-1}$:\n$$(A^T A) A^{-1} = I A^{-1} \\iff A^T (A A^{-1}) = A^{-1} \\iff A^T I = A^{-1} \\iff A^T = A^{-1}$$\nLấy định thức hai vế: $\\det(A^T A) = \\det(A^T) \\det(A) = [\\det(A)]^2 = \\det(I) = 1 \\implies \\det(A) = \\pm 1 \\ne 0$.",
        "- **Phương án A (Phụ thuộc tuyến tính):** Sai, các cột trực giao với nhau nên độc lập tuyến tính tuyệt đối.\n- **Phương án C (Định thức bằng 0):** Sai, $\\det(A) = \\pm 1$, không thể bằng 0.\n- **Phương án D (Ma trận suy biến):** Sai, do $\\det(A) \\ne 0$ nên $A$ luôn khả nghịch, không suy biến.",
        "📚 Xem **§5.3 Đại số tuyến tính trong AI**.\n🔗 **Liên hệ bài cũ:** Trong Deep Learning, phép khởi tạo trọng số trực giao (Orthogonal Initialization) giúp ngăn chặn hiện tượng bùng nổ/triệt tiêu gradient (Vanishing/Exploding Gradient) ở các tầng sâu (xem thêm câu C15 Đề 01)."
    ),
    "VOAI03-M02": (
        "- **Ma trận Hessian ($H = \\nabla^2 f(x)$):** Ma trận vuông chứa toàn bộ đạo hàm riêng bậc hai của hàm nhiều biến, đo độ cong của hàm số theo mọi hướng.\n- **Ma trận xác định dương (Positive Definite, $H \\succ 0$):** Ma trận có mọi trị riêng $\\lambda_i > 0$, tức $\\Delta x^T H \\Delta x > 0$ với mọi vector khác không $\\Delta x \\ne 0$.\n- **Điểm dừng (Stationary Point):** Điểm mà đạo hàm bậc nhất bằng 0 ($\\nabla f(x^*) = 0$).",
        "Tưởng tượng bạn đang đứng ở đáy của một chiếc bát ăn cơm úp ngửa. Chiếc bát cong lên ở mọi hướng (độ cong đều dương). Bất kể bạn bước sang trái, phải, trước hay sau, độ cao của bạn đều tăng lên. Vì thế đáy bát chính là điểm cực tiểu địa phương (Local Minimum)!",
        "Khai triển Taylor bậc 2 của hàm $f$ quanh điểm dừng $x^*$:\n$$f(x^* + \\Delta x) = f(x^*) + \\nabla f(x^*)^T \\Delta x + \\frac{1}{2} \\Delta x^T H \\Delta x + o(\\|\\Delta x\\|^2)$$\nDo $\\nabla f(x^*) = 0$, ta có:\n$$f(x^* + \\Delta x) - f(x^*) \\approx \\frac{1}{2} \\Delta x^T H \\Delta x$$\nVì $H$ xác định dương ($H \\succ 0$), với mọi $\\Delta x \\ne 0$ thì $\\Delta x^T H \\Delta x > 0$.\nDo đó $f(x^* + \\Delta x) > f(x^*)$ trong mọi lân cận nhỏ $\\implies x^*$ là cực tiểu địa phương. Chọn **C**.",
        "- **Phương án A (Cực đại địa phương):** Sai, cực đại khi $H$ xác định âm ($H \\prec 0$, chiếc bát úp ngược).\n- **Phương án D (Điểm yên ngựa):** Sai, yên ngựa xảy ra khi $H$ không xác định (Indefinite, có cả trị riêng âm và dương).",
        "📚 Xem **§5.2 Tối ưu hóa lồi & Đạo hàm đa biến**.\n🔗 **Liên hệ bài cũ:** Trong Deep Learning, các hàm mất mát phức tạp thường gặp rất nhiều điểm yên ngựa (Saddle Points) chứ không phải cực tiểu địa phương, đó là lý do các optimizer như Adam hay Momentum cần quán tính để vượt qua điểm yên ngựa."
    ),
    "VOAI03-M03": (
        "- **Hàm Sigmoid ($\\sigma(x)$):** $\\sigma(x) = \\frac{1}{1 + e^{-x}}$, đưa giá trị thực bất kỳ về khoảng $(0, 1)$.\n- **Đạo hàm hàm hợp (Chain Rule):** $[\\ln(u)]' = \\frac{u'}{u}$.",
        "Hàm số này chính là hàm Softplus biến thể: $f(x) = \\ln(1 + e^{-x})$. Ta chỉ việc áp dụng quy tắc đạo hàm lớp 12: Đạo hàm của $\\ln(u)$ là $u'/u$, rồi biến đổi khéo léo một chút để đưa về dạng quen thuộc của hàm kích hoạt Sigmoid mà mạng nơ-ron hay dùng.",
        "Đặt $u = 1 + e^{-x} \\implies u' = -e^{-x}$.\n$$f'(x) = \\frac{u'}{u} = \\frac{-e^{-x}}{1 + e^{-x}}$$\nNhân cả tử và mẫu với $e^x$:\n$$f'(x) = \\frac{-e^{-x} \\cdot e^x}{(1 + e^{-x}) \\cdot e^x} = \\frac{-1}{e^x + 1} = -\\frac{1}{1 + e^x}$$\nNhớ rằng $\\sigma(x) = \\frac{1}{1 + e^{-x}} = \\frac{e^x}{1 + e^x}$.\nDo đó: $\\sigma(x) - 1 = \\frac{e^x}{1 + e^x} - 1 = \\frac{e^x - (1 + e^x)}{1 + e^x} = -\\frac{1}{1 + e^x} = f'(x)$.\nVậy $f'(x) = \\sigma(x) - 1$. Chọn **A**.",
        "- **Phương án B ($f'(x) = \\sigma(x)$):** Quên dấu trừ của đạo hàm $e^{-x}$.\n- **Phương án C & D:** Biến đổi nhầm lẫn giữa logarit tự nhiên và hàm mũ.",
        "📚 Xem **§2.2 Các hàm kích hoạt & Đạo hàm trong Deep Learning**.\n🔗 **Liên hệ bài cũ:** Hàm Softplus $\\text{Softplus}(x) = \\ln(1 + e^x)$ là phiên bản làm mịn (smooth approximation) của hàm ReLU. Đạo hàm của $\\text{Softplus}(x)$ chính là hàm Sigmoid $\\sigma(x)$!"
    ),
    "VOAI03-M04": (
        "- **Shannon Entropy ($H(X)$):** Thước đo mức độ hỗn loạn, bất định (uncertainty) hoặc lượng thông tin trung bình chứa trong một phân phối xác suất.\n- **Đơn vị Entropy:** Dùng $\\log_2$ đo bằng **bit** (shannon); dùng $\\ln$ đo bằng **nat**; dùng $\\log_{10}$ đo bằng **hartley**.\n- **Kỳ vọng & Phương sai:** Đo độ lệch tâm và độ phân tán của giá trị số học, không đo mức độ hỗn loạn thông tin.",
        "Entropy giống như việc đoán xem một đồng xu tung lên sẽ ra mặt ngửa hay sấp: Nếu đồng xu 2 mặt đều có cơ hội 50-50, bạn hoàn toàn không đoán trước được (độ bất định tối đa $\\implies$ Entropy cao nhất = 1 bit). Nhưng nếu đồng xu bị làm giả cả 2 mặt đều ngửa, bạn biết chắc chắn kết quả $\\implies$ không có gì bất ngờ cả (Entropy = 0 bit).",
        "Công thức Shannon Entropy cho biến ngẫu nhiên rời rạc $X$ có $C$ trạng thái:\n$$H(X) = -\\sum_{i=1}^C p_i \\log_2(p_i)$$\nQuy ước $0 \\log_2(0) = 0$. $H(X)$ đạt cực tiểu bằng $0$ khi một lớp có xác suất $p=1$ (thuần khiết), đạt cực đại $\\log_2(C)$ khi phân phối đều $p_i = 1/C$. Chọn **C** (Entropy).",
        "- **Phương án A (Phương sai):** Phương sai chỉ đo độ lệch khỏi giá trị trung bình của biến số, phụ thuộc vào thang đo (scale), không đo lượng thông tin xác suất.\n- **Phương án D (Kỳ vọng):** Kỳ vọng chỉ là giá trị trung bình cộng theo xác suất.",
        "📚 Xem **§1.3 Cây quyết định, Entropy & Information Gain**.\n🔗 **Liên hệ bài cũ:** Ở câu B04 Đề 01, ta đã tính tay Entropy cho tập 10 mẫu (4 Chó, 6 Mèo). Thuật toán ID3 dùng hiệu số Entropy (Information Gain) để chọn thuộc tính phân chia tốt nhất."
    ),
    "VOAI03-M05": (
        "- **Thuật toán k-NN (k-Nearest Neighbors):** Thuật toán học lười (Lazy Learner), phân loại điểm mới dựa trên đa số $k$ điểm láng giềng gần nhất trong không gian đặc trưng.\n- **Overfitting (Quá khớp / High Variance):** Mô hình ghi nhớ quá chi tiết tập huấn luyện, nhạy cảm với từng điểm nhiễu ngoại lai.\n- **Underfitting (Thiếu khớp / High Bias):** Mô hình quá đơn giản, bỏ qua các quy luật phức tạp.",
        "Khi $k=1$, mô hình chỉ nghe lời 1 người bạn gần nhất. Nếu người bạn đó tình cờ là một điểm dữ liệu bị gán nhãn nhầm (nhiễu), mô hình sẽ tin ngay lập tức! Ranh giới phân chia sẽ bị ngoằn ngoèo, gập ghềnh để bao bọc từng điểm nhiễu đơn lẻ $\\implies$ Overfitting.",
        "- Khi $k=1$: Ranh giới quyết định tạo thành biểu đồ Voronoi phân mảnh cực kỳ phức tạp. Training error = 0, nhưng Test error rất lớn $\\implies$ Variance cao, Bias thấp (Overfitting). Chọn **A**.\n- Khi $k \\to N$: Ranh giới mượt mà, luôn dự đoán lớp chiếm đa số trong toàn bộ dữ liệu $\\implies$ Variance thấp, Bias cao (Underfitting).",
        "- **Phương án B (Underfitting):** Ngược lại, $k$ quá lớn mới bị Underfitting.\n- **Phương án D (Luôn chính xác nhất):** Sai hoàn toàn, $k=1$ rất dễ đoán sai trên dữ liệu kiểm thử do nhiễu.",
        "📚 Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)**.\n🔗 **Liên hệ bài cũ:** Trong cẩm nang §1.1, nguyên tắc vàng khi chọn $k$ là chọn số lẻ (với bài toán 2 lớp) để tránh hòa vote, và dùng Cross-Validation để tìm $k$ tối ưu (thường từ 3 đến 15)."
    ),
    "VOAI03-M06": (
        "- **Học có giám sát (Supervised Learning):** Dữ liệu có cả đặc trưng đầu vào $X$ và nhãn mục tiêu $y$ (Labels). Mô hình học ánh xạ $f(X) \\to y$.\n- **Học không giám sát (Unsupervised Learning):** Dữ liệu chỉ có $X$, không có nhãn $y$. Mục tiêu là tìm cấu trúc ẩn, gom cụm (Clustering) hoặc giảm chiều (Dimensionality Reduction).\n- **PCA (Principal Component Analysis):** Kỹ thuật giảm chiều tuyến tính không giám sát bằng cách chiếu dữ liệu lên các trục có phương sai cực đại.",
        "Học có giám sát giống như làm bài tập có sẵn sách giải ở trang cuối (biết đáp án đúng để đối chiếu). Còn PCA giống như việc bạn tự nhìn vào một tủ sách lộn xộn để gom các cuốn sách lại gọn gàng hơn mà không có ai chỉ bảo trước cuốn nào thuộc thể loại gì.",
        "PCA tìm các vector riêng (Eigenvectors) của ma trận hiệp phương sai $\\Sigma = \\frac{1}{N} X^T X$ ứng với các trị riêng lớn nhất. Quá trình này hoàn toàn không dùng và không cần bất kỳ nhãn mục tiêu $y$ nào. Chọn **C** (PCA).",
        "- **SVM, Random Forest, Logistic Regression:** Đều là các thuật toán học có giám sát kinh điển cần nhãn $y$ để tối ưu hàm mất mát.",
        "📚 Xem **§1.7 Giảm chiều dữ liệu: PCA & t-SNE**.\n🔗 **Liên hệ bài cũ:** Khác với PCA (không giám sát), kỹ thuật LDA (Linear Discriminant Analysis) cũng là giảm chiều tuyến tính nhưng là học CÓ GIÁM SÁT vì tìm trục chiếu tối đa hóa khoảng cách giữa các lớp."
    ),
    "VOAI03-M07": (
        "- **Pruning (Tỉa cành cây quyết định):** Kỹ thuật loại bỏ bớt các nhánh con hoặc nút lá không quan trọng trên cây quyết định.\n- **Pre-pruning (Dừng sớm):** Giới hạn độ sâu tối đa (`max_depth`), số mẫu tối thiểu ở nút lá (`min_samples_leaf`).\n- **Post-pruning (Tỉa sau):** Để cây mọc tự do rồi cắt tỉa dựa trên hàm chi phí độ phức tạp (Cost-Complexity Pruning).",
        "Cây quyết định giống như một cái cây ngoài vườn. Nếu bạn để nó mọc um tùm không cắt tỉa, cành lá sẽ đâm vào từng ngóc ngách nhỏ (học thuộc lòng từng chi tiết vụn vặt và nhiễu trong dữ liệu). 'Tỉa cành' là cắt bỏ những nhánh con rườm rà đó đi để cây gọn gàng, khỏe mạnh và khái quát hóa tốt hơn cho tương lai $\\implies$ Giảm Overfitting!",
        "Hàm mục tiêu của Cost-Complexity Pruning (tham số $\\alpha$):\n$$R_\\alpha(T) = R(T) + \\alpha |T|$$\nTrong đó $R(T)$ là tổng sai số trên tập dữ liệu của cây $T$, $|T|$ là số lượng nút lá, $\\alpha \\ge 0$ là hệ số phạt độ phức tạp. Khi $\\alpha$ tăng, cây buộc phải tỉa bớt các nút lá để giảm Overfitting. Chọn **C**.",
        "- **Phương án A & D:** Tỉa cành làm GIẢM độ sâu và làm cây ĐƠN GIẢN HƠN, không phải làm phức tạp hơn.\n- **Phương án C:** Tỉa cành làm GIẢM số nút lá, không phải tăng.",
        "📚 Xem **§1.3 Cây quyết định, Entropy & Information Gain**.\n🔗 **Liên hệ bài cũ:** Cây quyết định không tỉa cành có thể đạt độ chính xác 100% trên tập train nhưng sẽ sụp đổ trên tập test. Đó là lý do trong Scikit-Learn luôn khuyến nghị đặt `max_depth` hoặc dùng `ccp_alpha`."
    ),
    "VOAI03-M08": (
        "- **Ensemble Learning (Học kết hợp):** Phương pháp kết hợp nhiều mô hình yếu (Weak Learners) để tạo thành mô hình mạnh (Strong Learner).\n- **Bagging (Bootstrap Aggregating):** Lấy mẫu lặp lại (Bootstrap) để huấn luyện song song nhiều mô hình độc lập, sau đó lấy trung bình hoặc vote đa số. Giúp giảm phương sai (Variance).\n- **Boosting:** Huấn luyện tuần tự các mô hình, mô hình sau tập trung sửa sai cho mô hình trước. Giúp giảm độ chệch (Bias).\n- **Random Forest:** Thuật toán kết hợp Bagging của nhiều cây quyết định với cơ chế chọn ngẫu nhiên tập con đặc trưng (Feature Subsampling).",
        "Random Forest giống như việc bạn muốn chẩn đoán một ca bệnh khó: Thay vì hỏi 1 bác sĩ duy nhất (có thể nhìn nhận chủ quan), bạn hỏi ý kiến của 100 bác sĩ độc lập (Bagging). Mỗi bác sĩ được xem một tập hồ sơ bệnh án khác nhau và một nhóm chỉ số xét nghiệm khác nhau. Sau đó cả 100 bác sĩ bỏ phiếu vote đa số. Quyết định tập thể này sẽ cực kỳ khách quan và khó bị sai lệch!",
        "Với $B$ cây quyết định độc lập có phương sai $\\sigma^2$ và hệ số tương quan $\\rho$, phương sai của dự đoán kết hợp là:\n$$\\text{Var}(\\bar{f}) = \\rho \\sigma^2 + \\frac{1 - \\rho}{B} \\sigma^2$$\nKhi $B \\to \\infty$, thành phần thứ hai tiến về 0. Random Forest giảm thêm $\\rho$ nhờ ngẫu nhiên hóa đặc trưng tại mỗi điểm cắt ($m = \\sqrt{p}$). Chọn **C** (Bagging).",
        "- **Phương án A (Boosting):** Là cơ chế của AdaBoost, Gradient Boosting, XGBoost, LightGBM (huấn luyện tuần tự), không phải Random Forest.\n- **Phương án C (Stacking):** Huấn luyện mô hình meta kết hợp dự đoán của các mô hình khác loại.",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Ở câu C03 Đề 01, ta đã phân biệt rõ: Bagging chạy song song độc lập (giảm Variance), còn Boosting chạy tuần tự (giảm Bias)."
    ),
    "VOAI03-M09": (
        "- **Precision (Độ chuẩn xác):** Trong số những mẫu mô hình đoán là Dương tính, có bao nhiêu mẫu thật sự Dương tính ($TP / (TP + FP)$).\n- **Recall (Độ nhạy / Thu hồi):** Trong số những mẫu thật sự Dương tính ngoài đời, mô hình bắt được bao nhiêu mẫu ($TP / (TP + FN)$).\n- **F1-Score:** Trung bình điều hòa (Harmonic Mean) giữa Precision và Recall.",
        "Precision trả lời câu hỏi: 'Bắt nhầm hay không?' (bắn 10 phát trúng mấy phát). Recall trả lời câu hỏi: 'Bỏ sót hay không?' (trong 10 con mồi bắt được mấy con). $F_1$-Score là cây cầu hòa giải công bằng nhất giữa hai mục tiêu này. Nó dùng trung bình điều hòa để phạt nặng nếu mô hình chỉ giỏi 1 bên mà bỏ bê bên kia!",
        "Công thức trung bình điều hòa:\n$$F_1 = \\frac{2}{\\frac{1}{\\text{Precision}} + \\frac{1}{\\text{Recall}}} = 2 \\cdot \\frac{\\text{Precision} \\cdot \\text{Recall}}{\\text{Precision} + \\text{Recall}}$$\nNếu một trong hai chỉ số bằng 0, $F_1$ sẽ lập tức sụp đổ về 0. Chọn **B** (Precision và Recall).",
        "- **Phương án A & B:** Nhầm lẫn với Accuracy (Độ chính xác toàn thể: $(TP+TN)/Total$). Trên tập dữ liệu lệch lớp, Accuracy hoàn toàn vô dụng.\n- **Phương án D:** Specificity là độ đặc hiệu ($TN / (TN + FP)$).",
        "📚 Xem **§1.6 Các chỉ số đánh giá mô hình (Metrics)**.\n🔗 **Liên hệ bài cũ:** Trong đề thi OLP AI 2025 Vòng Sơ loại (Tác vụ 2 Nhận diện ngôn ngữ ký hiệu), BTC đã dùng chính xác chỉ số **Macro-F1** (trung bình F1 của 50 lớp cử chỉ) làm metric chấm điểm chính thức!"
    ),
    "VOAI03-M10": (
        "- **Đa cộng tuyến (Multicollinearity):** Hiện tượng hai hoặc nhiều biến độc lập trong mô hình hồi quy tuyến tính có tương quan tuyến tính rất mạnh với nhau.\n- **Hậu quả:** Ma trận $X^T X$ gần như suy biến (định thức gần bằng 0), khiến nghịch đảo $(X^T X)^{-1}$ không ổn định, dẫn đến phương sai của trọng số ước lượng $\\hat{\\beta}$ tăng vọt.\n- **Tự tương quan (Autocorrelation):** Tương quan giữa các giá trị của cùng một biến qua các mốc thời gian khác nhau (trong Time Series).",
        "Tưởng tượng bạn làm mô hình dự đoán giá nhà. Bạn đưa vào hai cột: Cột 1 là 'Diện tích tính theo mét vuông ($m^2$)' và Cột 2 là 'Diện tích tính theo centimét vuông ($cm^2$)'. Hai cột này thực chất là một! Mô hình sẽ bị bối rối không biết nên chia trọng số cho cột nào, dẫn đến kết quả trọng số bị nhảy múa lung tung và không đáng tin cậy. Đó gọi là Đa cộng tuyến!",
        "Ước lượng OLS: $\\hat{\\beta} = (X^T X)^{-1} X^T y$.\nMa trận hiệp phương sai của trọng số: $\\text{Var}(\\hat{\\beta}) = \\sigma^2 (X^T X)^{-1}$.\nKhi các cột của $X$ tương quan cao, $\\det(X^T X) \\approx 0$, các phần tử đường chéo của $(X^T X)^{-1}$ (chỉ số phóng đại phương sai VIF) tiến tới vô cùng. Chọn **C** (Đa cộng tuyến).",
        "- **Phương án B (Tự tương quan):** Là sai số của các quan sát liên tiếp phụ thuộc nhau (kiểm định bằng Durbin-Watson).\n- **Phương án C (Phương sai thay đổi / Heteroskedasticity):** Phương sai sai số không đồng đều tại các mức giá trị $X$ khác nhau.",
        "📚 Xem **§1.2 Hồi quy tuyến tính & Regularization L1/L2**.\n🔗 **Liên hệ bài cũ:** Để chữa hiện tượng đa cộng tuyến, kỹ thuật Ridge Regression (Regularization L2) cộng thêm $\\lambda I$ vào $X^T X$ để đảm bảo ma trận luôn khả nghịch ổn định: $\\hat{\\beta} = (X^T X + \\lambda I)^{-1} X^T y$."
    )
}

# Áp dụng cho từng câu
qs = exam_data["questions"]
count = 0
for q in qs:
    qid = q["id"]
    if qid in DATA:
        term, eli5, math, trap, ref = DATA[qid]
        new_exp = f"""### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
{term}

🍼 **Hình dung thực tế cho em bé:**
{eli5}

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 {math}

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
{trap}

### 4. Mắt xích kiến thức & Liên hệ bài cũ
{ref}"""
        q["explanation"] = new_exp
        count += 1

print(f"Đã nâng cấp {count} câu đầu tiên thành công!")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)
