# -*- coding: utf-8 -*-
"""
scripts/upgrade_olp03_m31_m50.py
Bổ sung đầy đủ dữ liệu nâng cấp cho M31 đến M50 của Đề 03 (20 câu).
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

UPGRADES_31_50 = {
    "VOAI03-M31": (
        "- **Học bán giám sát (Semi-supervised Learning):** Phương pháp huấn luyện khi có một lượng nhỏ dữ liệu có nhãn (Labeled data) và một lượng rất lớn dữ liệu chưa có nhãn (Unlabeled data).\n- **Pseudo-labeling:** Dùng mô hình huấn luyện trên tập có nhãn để dự đoán nhãn giả cho tập chưa có nhãn, sau đó chọn các mẫu có độ tin cậy cao để nạp lại vào tập huấn luyện.\n- **Consistency Regularization:** Ép mô hình đưa ra dự đoán tương đồng khi ảnh đầu vào bị biến dạng nhẹ (Perturbation).",
        "Tưởng tượng trong một lớp học, giáo viên chỉ có thời gian chấm điểm chi tiết cho 10 bài kiểm tra mẫu (dữ liệu có nhãn). Còn 1,000 bài tập khác chưa kịp chấm. Học bán giám sát giúp bạn học từ 10 bài mẫu đó trước, rồi tự làm thử 1,000 bài tập kia để nâng cao tay nghề thay vì bỏ phí 1,000 bài tập đó!",
        "Áp dụng khi chi phí dán nhãn (gán nhãn bởi chuyên gia/bác sĩ) rất đắt đỏ trong khi dữ liệu thô chưa dán nhãn lại cực kỳ phong phú và dễ thu thập. Chọn **A** (Dữ liệu có nhãn rất ít nhưng dữ liệu chưa có nhãn rất nhiều).",
        "- **Phương án B & C:** Nếu dữ liệu đã có nhãn đầy đủ thì dùng Supervised Learning; nếu hoàn toàn không có nhãn thì dùng Unsupervised Learning.",
        "📚 Xem **§1.5 Các phương pháp học máy hiện đại**.\n🔗 **Liên hệ bài cũ:** Trong các bài toán phát hiện bất thường ảnh công nghiệp (như đề thi OLP AI 2026 Tác vụ 2), việc tận dụng lượng lớn ảnh bình thường chưa gán nhãn là chìa khóa để xây dựng mô hình một lớp (One-class classification)."
    ),
    "VOAI03-M32": (
        "- **t-SNE (t-Distributed Stochastic Neighbor Embedding):** Thuật toán giảm chiều dữ liệu phi tuyến (Non-linear Dimensionality Reduction) chuyên dùng để trực quan hóa không gian nhiều chiều về 2D/3D.\n- **PCA (Principal Component Analysis):** Kỹ thuật giảm chiều tuyến tính bằng phép chiếu trực giao.\n- **Phân phối Student-t:** Có phần đuôi dày (Heavy-tailed), giải quyết triệt để vấn đề chen chúc (Crowding Problem) của các cụm trong không gian chiều thấp.",
        "PCA giống như chiếu bóng của một chiếc ấm trà lên tường: Các chi tiết phía trước và phía sau bị đè bẹp lên nhau vì chỉ là bóng phẳng tuyến tính. Còn t-SNE giống như một người nghệ nhân khéo léo bóc tách từng cụm đất sét ra, trải chúng lên bàn sao cho các hạt gần nhau vẫn ở gần nhau, còn các cụm khác nhau được đẩy xa hẳn ra!",
        "t-SNE tối thiểu hóa phân kỳ Kullback-Leibler (KL Divergence) giữa phân phối xác suất láng giềng trong không gian gốc $p_{j|i}$ và không gian chiếu $q_{j|i}$:\n$$KL(P \\parallel Q) = \\sum_i \\sum_j p_{j|i} \\log \\frac{p_{j|i}}{q_{j|i}}$$\nt-SNE bảo toàn cấu trúc lân cận phi tuyến cục bộ vượt trội so với PCA. Chọn **C** (Bảo toàn cấu trúc cục bộ và quan hệ phi tuyến tốt hơn nhiều).",
        "- **Phương án A (Chạy nhanh hơn):** Sai, t-SNE có độ phức tạp tính toán $O(N^2)$ (hoặc $O(N \\log N)$ với Barnes-Hut), chậm hơn PCA rất nhiều.\n- **Phương án B (Dùng làm đặc trưng train):** Sai, t-SNE không học được hàm chiếu tổng quát để chiếu điểm dữ liệu mới (Out-of-sample mapping).",
        "📚 Xem **§1.7 Giảm chiều dữ liệu: PCA & t-SNE**.\n🔗 **Liên hệ bài cũ:** Nhớ quy tắc thực tế: Dùng PCA để giảm chiều tiền xử lý trước khi đưa vào mô hình học máy; dùng t-SNE hoặc UMAP để vẽ biểu đồ trực quan hóa khám phá các cụm."
    ),
    "VOAI03-M33": (
        "- **Stratified K-Fold:** Kỹ thuật chia tập dữ liệu thành $K$ phần (folds) sao cho tỉ lệ phân bố giữa các lớp (Class Ratio) trong mỗi fold giống hệt tỉ lệ của toàn bộ tập dữ liệu gốc.\n- **K-Fold thông thường (Standard K-Fold):** Chia ngẫu nhiên không xét đến nhãn lớp.\n- **Mất cân bằng lớp nghiêm trọng (Severe Imbalance):** Ví dụ lớp thiểu số chỉ chiếm 1% (như phát hiện gian lận thẻ tín dụng hoặc bệnh hiếm).",
        "Tưởng tượng bạn làm một mâm cỗ có 100 chiếc bánh: Trong đó chỉ có đúng 5 chiếc bánh nhân sôcôla thượng hạng, còn lại 95 chiếc bánh nhân đậu xanh. Nếu chia ngẫu nhiên thành 5 đĩa (K-Fold thường), rất có thể đĩa thứ nhất không có chiếc bánh sôcôla nào, trong khi đĩa thứ hai lại ôm trọn cả 5 chiếc! Stratified K-Fold đảm bảo chia đều: Mỗi đĩa bắt buộc phải có đúng 1 chiếc bánh sôcôla và 19 chiếc bánh đậu xanh!",
        "Nếu dùng K-Fold thường trên tập dữ liệu lệch lớp, một fold kiểm thử có thể hoàn toàn không chứa mẫu nào của lớp thiểu số ($TP=0, FN=0$), khiến các chỉ số Precision, Recall và F1 bị vỡ hoặc không tính toán được. Stratified K-Fold bảo toàn $P(y=c)$ trên mọi fold. Chọn **D** (Đảm bảo tỉ lệ phân bố các lớp đồng đều trong mọi fold chia).",
        "- **Phương án A & B:** Stratified K-Fold không làm tăng tốc độ chạy và không sinh thêm dữ liệu mới.",
        "📚 Xem **§1.5 Cross-Validation & Các phương pháp đánh giá mô hình**.\n🔗 **Liên hệ bài cũ:** Trong bài tự luận E04 Đề 02 (Phát hiện ảnh Deepfake theo cặp), ta phải nâng cấp lên `StratifiedGroupKFold`: Vừa bảo đảm tỉ lệ nhãn đồng đều, vừa gom toàn bộ các ảnh cùng nhóm (`pair_id`) vào chung một fold để chống rò rỉ dữ liệu."
    ),
    "VOAI03-M34": (
        "- **Data Leakage (Rò rỉ dữ liệu / Train-Test Contamination):** Hiện tượng thông tin từ tập kiểm tra (Test set) bị thẩm thấu (rò rỉ) vào quá trình huấn luyện mô hình.\n- **Hậu quả:** Điểm số Validation/CV cao giả tạo nhưng mô hình sụp đổ hoàn toàn khi đưa vào môi trường Production thực tế.\n- **Vị trí hay mắc lỗi nhất:** Gọi `StandardScaler.fit()` hoặc `Imputer.fit()` trên toàn bộ dữ liệu trước khi chia Train-Test.",
        "Data Leakage giống như việc bạn đi thi nhưng đã vô tình đọc trộm đáp án và thang điểm của thầy giáo từ tối hôm trước! Bạn đạt 10 điểm tuyệt đối trong phòng thi thử, nhưng khi gặp một bài kiểm tra thực tế ngoài đời thì hoàn toàn không biết làm. Chuẩn hóa dữ liệu trên cả tập test khiến mô hình 'biết trước' giá trị trung bình $\\mu$ và độ lệch chuẩn $\\sigma$ của tương lai!",
        "Quy tắc vàng bất biến trong khoa học dữ liệu:\n1. Chia tập dữ liệu thành Train và Test TRƯỚC TIÊN.\n2. Chỉ gọi `scaler.fit_transform(X_train)` trên tập Train.\n3. Chỉ gọi `scaler.transform(X_test)` trên tập Test (dùng nguyên $\\mu_{\\text{train}}$ và $\\sigma_{\\text{train}}$).\nChọn **B** (Chuẩn hóa toàn bộ dữ liệu trước khi chia Train/Test).",
        "- **Phương án A, C, D:** Lấy mẫu ngẫu nhiên, chia dữ liệu trước và dùng cross-validation là các quy trình chuẩn mực chống rò rỉ.",
        "📚 Xem **§1.5 Cross-Validation & Pipeline chống leakage**.\n🔗 **Liên hệ bài cũ:** Trong Scikit-Learn, cách tốt nhất để triệt tiêu Data Leakage là đóng gói toàn bộ các bước tiền xử lý và mô hình vào một `Pipeline(steps=[('scaler', StandardScaler()), ('clf', Model())])`."
    ),
    "VOAI03-M35": (
        "- **SMOTE (Synthetic Minority Over-sampling Technique):** Thuật toán sinh mẫu nhân tạo cho lớp thiểu số bằng phép nội suy vector dựa trên $k$ láng giềng gần nhất (thường $k=5$).\n- **Random Oversampling:** Nhân bản sao chép y nguyên các mẫu thiểu số cũ (dễ gây Overfitting).\n- **Nhược điểm của SMOTE:** Có thể sinh mẫu rơi vào vùng ranh giới nhiễu giữa hai lớp (khắc phục bằng Borderline-SMOTE hoặc SVM-SMOTE).",
        "Thay vì chỉ đơn giản là photocopy lại những bức ảnh cũ (làm mô hình học vẹt), SMOTE tìm hai điểm dữ liệu cùng thuộc lớp thiểu số đứng gần nhau, rồi vẽ một đoạn thẳng nối giữa hai điểm đó. Sau đó, nó chọn một vị trí ngẫu nhiên trên đoạn thẳng để 'nặn' ra một điểm dữ liệu nhân tạo mới toanh! Giúp mở rộng ranh giới quyết định của lớp thiểu số một cách mượt mà.",
        "Công thức sinh mẫu của SMOTE:\n$$x_{\\text{new}} = x_i + \\lambda (x_{zi} - x_i)$$\nTrong đó $x_{zi}$ là một trong $k$ láng giềng gần nhất cùng lớp của $x_i$, và $\\lambda \\sim U(0, 1)$ là số ngẫu nhiên đều. Chọn **D** (Nội suy tuyến tính giữa các điểm láng giềng gần nhất của lớp thiểu số).",
        "- **Phương án A (Nhân bản ngẫu nhiên):** Đó là Random Oversampling thô sơ.\n- **Phương án B (Xóa bớt mẫu đa số):** Đó là kỹ thuật Undersampling (như Tomek Links, ENN).\n- **Phương án C:** SMOTE không gán nhãn lại dữ liệu.",
        "📚 Xem **§1.9 Xử lý dữ liệu mất cân bằng: SMOTE, Focal Loss & Class Weights**.\n🔗 **Liên hệ bài cũ:** Cực kỳ lưu ý: CHỈ ĐƯỢC CHẠY SMOTE TRÊN TẬP HUẤN LUYỆN (Train Set). Nếu chạy SMOTE trước khi chia train/test, bạn sẽ làm rò rỉ dữ liệu nhân tạo sang tập test (Data Leakage nghiêm trọng)!"
    ),
    "VOAI03-M36": (
        "- **ROC-AUC (Area Under ROC Curve):** Diện tích dưới đường cong liên hệ giữa TPR ($TP/(TP+FN)$) và FPR ($FP/(FP+TN)$).\n- **PR-AUC (Precision-Recall AUC / Average Precision):** Diện tích dưới đường cong liên hệ giữa Precision và Recall.\n- **True Negative Inflation:** Khi số lượng mẫu âm tính ($TN$) quá khổng lồ, mẫu số của FPR ($FP + TN$) cực lớn khiến FPR luôn rất nhỏ, làm đường cong ROC bị thổi phồng giả tạo (Optimistic Bias).",
        "Tưởng tượng trong một triệu giao dịch ngân hàng chỉ có đúng 10 vụ lừa đảo ($TN = 999,990$). Một mô hình tồi đoán nhầm 1,000 giao dịch bình thường thành lừa đảo ($FP=1,000$). Khi đó FPR chỉ là $1,000 / 1,000,000 = 0.1\\%$ (trông như hoàn hảo!). Đường cong ROC-AUC sẽ đạt tới 0.99 đẹp như mơ! Nhưng thực tế Precision của nó cực tệ: Bắt 1,000 người thì chỉ có vài tên trộm. Chỉ có đường cong PR-AUC mới lột trần sự yếu kém này!",
        "Khi bài toán có tỉ lệ lệch lớp cực đoan (như $1:100$ hoặc $1:1000$), chỉ số **PR-AUC** (Precision-Recall AUC) là tiêu chuẩn vàng duy nhất phản ánh chính xác hiệu năng mô hình trên lớp thiểu số quan trọng. Chọn **D** (PR-AUC / Precision-Recall Curve).",
        "- **Phương án A (Accuracy):** Hoàn toàn vô dụng (đoán toàn bộ là Âm tính vẫn đạt Accuracy 99.9%).\n- **Phương án B (ROC-AUC):** Bị thổi phồng bởi số lượng $TN$ khổng lồ.\n- **Phương án C (MSE):** Chỉ dùng cho bài toán Hồi quy số thực.",
        "📚 Xem **§1.6 Các chỉ số đánh giá mô hình (Metrics)**.\n🔗 **Liên hệ bài cũ:** Trong cẩm nang §1.6 và bài tự luận E05 Đề 02, luôn ưu tiên cặp chỉ số PR-AUC và Macro-F1 khi giải quyết các bài toán dữ liệu bảng mất cân bằng lớp."
    ),
    "VOAI03-M37": (
        "- **Regularization (Chính quy hóa):** Kỹ thuật cộng thêm một số hạng phạt độ lớn trọng số vào hàm mất mát để chống Overfitting.\n- **L1 Regularization (Lasso):** Phạt theo chuẩn $\\ell_1$: $\\Omega(w) = \\lambda \\sum |w_i|$. Dẫn đến nghiệm thưa (Sparsity - ép nhiều trọng số về đúng bằng 0), đóng vai trò như bộ chọn lọc đặc trưng tự động.\n- **L2 Regularization (Ridge):** Phạt theo chuẩn $\\ell_2$: $\\Omega(w) = \\lambda \\sum w_i^2$. Ép các trọng số co nhỏ lại gần 0 nhưng không bao giờ bằng 0 tuyệt đối.",
        "L1 giống như một chiếc kéo cắt cành tỉa lá: Nó thẳng tay cắt phăng những thuộc tính vô dụng và gán trọng số của chúng bằng đúng 0 (bỏ hẳn cột đó ra khỏi mô hình). Còn L2 giống như một chiếc dây cao su: Nó co kéo tất cả các trọng số lại thật nhỏ và đều đặn, nhưng vẫn giữ lại tất cả các cành lá chứ không cắt bỏ cành nào!",
        "Về mặt hình học: Miền giới hạn của L1 là hình thoi (Diamond) có các góc nhọn nằm trên các trục tọa độ. Đường đồng mức sai số Elip có xác suất rất cao chạm vào các góc nhọn này đầu tiên $\\implies$ Trọng số tại trục đó bằng 0. Miền của L2 là hình tròn trơn láng, không có góc nhọn. Chọn **A** (L1 tạo ra nghiệm thưa ép trọng số về 0, L2 co nhỏ trọng số nhưng không triệt tiêu về 0).",
        "- **Phương án B & C:** Đảo lộn vai trò giữa L1 và L2.",
        "📚 Xem **§1.2 Hồi quy tuyến tính & Regularization L1/L2**.\n🔗 **Liên hệ bài cũ:** Khi muốn kết hợp ưu điểm của cả L1 (chọn đặc trưng) và L2 (ổn định khi đa cộng tuyến), ta sử dụng **ElasticNet**: $\\mathcal{L} + \\lambda_1 \\|w\\|_1 + \\lambda_2 \\|w\\|_2^2$."
    ),
    "VOAI03-M38": (
        "- **`max_depth` (Độ sâu tối đa):** Số tầng quyết định tối đa từ nút gốc đến nút lá của cây quyết định.\n- **Hiện tượng Overfitting ở cây:** Cây quyết định không bị ràng buộc sẽ tiếp tục phân chia cho đến khi mọi nút lá đều thuần khiết tuyệt đối (Pure Leaf - chứa đúng 1 mẫu), dẫn đến việc ghi nhớ từng điểm nhiễu.",
        "Một cây quyết định có độ sâu 20 có thể chứa tới $2^{20} \\approx 1,000,000$ nút lá! Nếu tập dữ liệu chỉ có 5,000 dòng, cây sẽ hỏi từng câu hỏi li ti để học thuộc lòng từng dòng dữ liệu một cách máy móc. Mô hình sẽ đạt 100% độ chính xác trên tập Train nhưng sẽ đoán sai bét nhè trên tập Test $\\implies$ Overfitting nặng nề!",
        "Khi `max_depth` tăng lên vô hạn, Bias của mô hình giảm về 0 nhưng Variance tăng vọt tới cực đại (Overfitting). Chọn **A** (Mô hình bị Overfitting do cây quá phức tạp học thuộc dữ liệu huấn luyện).",
        "- **Phương án B (Underfitting):** Chỉ xảy ra khi `max_depth` quá nhỏ (ví dụ depth=1, gọi là Decision Stump).\n- **Phương án C (Chạy nhanh hơn):** Cây càng sâu càng tốn thời gian tính toán và bộ nhớ RAM.\n- **Phương án D:** Không có mô hình nào đạt độ chính xác tối ưu trên mọi tập dữ liệu nếu bị Overfitting.",
        "📚 Xem **§1.3 Cây quyết định, Entropy & Information Gain**.\n🔗 **Liên hệ bài cũ:** Trong các thư viện LightGBM và XGBoost, giá trị `max_depth` tối ưu thường chỉ nằm trong khoảng từ 3 đến 8 để kiểm soát hiện tượng quá khớp."
    ),
    "VOAI03-M39": (
        "- **Boxplot (Biểu đồ hộp - Tukey Boxplot):** Công cụ trực quan hóa phân phối dữ liệu dựa trên 5 con số thống kê: Min, $Q_1$ (Phân vị 25%), Median ($Q_2$ - Trung vị 50%), $Q_3$ (Phân vị 75%), Max.\n- **IQR (Interquartile Range - Khoảng tứ phân vị):** $\\text{IQR} = Q_3 - Q_1$.\n- **Quy tắc Tukey phát hiện ngoại lai (Outliers):** Điểm nằm ngoài đoạn $[Q_1 - 1.5 \\text{IQR}, Q_3 + 1.5 \\text{IQR}]$.",
        "Biểu đồ hộp giống như một chiếc vali đựng đồ: Chiếc vali chữ nhật chứa 50% số bạn học sinh ở khúc giữa của lớp. Hai chiếc quai (râu) kéo dài ra hai đầu để đón những bạn có điểm số bình thường. Nếu có bạn nào điểm số quá cao đột biến hoặc thấp bất thường vượt ra ngoài tầm với của chiếc râu, bạn đó sẽ bị đánh dấu thành một dấu chấm tròn cô đơn bên ngoài — đó chính là điểm ngoại lai (Outlier)!",
        "Khoảng cách giữa hai râu của Boxplot:\n- Râu dưới: $\\max(\\text{Min}, Q_1 - 1.5 \\times \\text{IQR})$.\n- Râu trên: $\\min(\\text{Max}, Q_3 + 1.5 \\times \\text{IQR})$.\nMọi điểm nằm ngoài khoảng này đều được coi là Outliers. Chọn **D** (Phát hiện điểm dữ liệu ngoại lai - Outliers và phân bố tứ phân vị).",
        "- **Phương án A:** Đo tương quan giữa 2 biến liên tục dùng biểu đồ phân tán (Scatter Plot) hoặc ma trận tương quan (Heatmap).\n- **Phương án B:** Đánh giá phân loại dùng Confusion Matrix.\n- **Phương án C:** Kiểm tra tương quan chuỗi thời gian dùng biểu đồ đường hoặc ACF.",
        "📚 Xem **§5.4 Thống kê mô tả & Phân tích khám phá EDA**.\n🔗 **Liên hệ bài cũ:** Khác với giá trị trung bình (Mean) và độ lệch chuẩn (Std) rất dễ bị bóp méo bởi các giá trị ngoại lai cực đoan, Trung vị ($Q_2$) và IQR của Boxplot có tính bền vững (Robust Statistics) cực kỳ cao."
    ),
    "VOAI03-M40": (
        "- **Early Stopping (Dừng sớm):** Kỹ thuật điều chuẩn (Regularization) trong huấn luyện mạng nơ-ron và mô hình Boosting.\n- **Cơ chế hoạt động:** Giám sát hàm mất mát hoặc chỉ số đánh giá trên tập kiểm định (Validation Loss / Metric). Khi Validation Loss không còn giảm sau một số lượng epoch nhất định (tham số `patience`), quá trình huấn luyện sẽ dừng lại và khôi phục lại trọng số tại thời điểm tốt nhất.",
        "Early Stopping giống như việc nướng một chiếc bánh trong lò vi sóng: Ban đầu chiếc bánh chín dần và thơm ngon (Validation Loss giảm). Nhưng nếu bạn cứ để lò bật quá lâu, chiếc bánh sẽ bị cháy khét (Train Loss vẫn giảm do học vẹt, nhưng Validation Loss bắt đầu tăng vọt do Overfitting). Early Stopping là chiếc cảm biến tự động ngắt điện đúng lúc chiếc bánh vừa chín tới hoàn hảo!",
        "Thuật toán Early Stopping:\n$$\\text{Nếu } \\mathcal{L}_{\\text{val}}^{(t)} > \\min_{s < t} \\mathcal{L}_{\\text{val}}^{(s)} \\quad \\text{liên tục trong } P \\text{ epochs (Patience)} \\implies \\text{Stop & Restore } \\theta^*$$\nChọn **A** (Sai số trên tập kiểm định - Validation Loss bắt đầu tăng trở lại).",
        "- **Phương án B (Train Loss bằng 0):** Khi Train loss = 0 mô hình đã bị Overfitting nghiêm trọng.\n- **Phương án C (Hết số epoch tối đa):** Đó là dừng theo giới hạn vòng lặp, không phải dừng sớm.\n- **Phương án D:** Gradient bằng 0 chỉ xảy ra khi chạm điểm dừng hoặc bị Vanishing Gradient.",
        "📚 Xem **§2.3 Vòng lặp huấn luyện mạng nơ-ron: Forward, Loss & Backward**.\n🔗 **Liên hệ bài cũ:** Trong PyTorch Lightning hoặc Keras, callback `EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)` là trang bị bắt buộc để tránh lãng phí GPU và chống quá khớp."
    ),
    "VOAI03-M41": (
        "- **Bagging (Bootstrap Aggregating):** Huấn luyện SONG SONG các mô hình độc lập trên các tập con dữ liệu lấy mẫu có hoàn lại. Mục tiêu chính: Giảm phương sai (Reduce Variance), chống Overfitting.\n- **Boosting:** Huấn luyện TUẦN TỰ các mô hình, mô hình sau tập trung tối ưu hàm mất mát để sửa chữa sai số của các mô hình trước. Mục tiêu chính: Giảm độ chệch (Reduce Bias).",
        "Sự khác biệt cốt lõi:\n- Bagging giống như một hội đồng 100 học sinh cùng làm bài thi độc lập rồi lấy trung bình điểm số (mỗi người giỏi một phần, tổng thể triệt tiêu sai số ngẫu nhiên $\\implies$ Giảm Variance).\n- Boosting giống như một người học sinh làm bài tập nhiều lần: Lần 1 làm sai câu nào thì lần 2 tập trung học kỹ câu đó; lần 2 vẫn sai thì lần 3 dồn toàn lực sửa tiếp $\\implies$ Nâng cao trình độ từ dốt thành giỏi (Giảm Bias)!",
        "Bagging: $\\mathbb{E}[\\bar{f}] = \\mathbb{E}[f_i]$ (Bias không đổi), $\\text{Var}(\\bar{f}) \\approx \\frac{\\sigma^2}{B}$ (Variance giảm mạnh).\nBoosting: $\\text{Bias}$ giảm liên tục sau mỗi vòng lặp thông qua việc học phần dư (Residuals). Chọn **D** (Bagging chạy song song nhằm giảm Variance; Boosting chạy tuần tự nhằm giảm Bias).",
        "- **Phương án A & B:** Đảo lộn bản chất giữa Bagging và Boosting.",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Vì Boosting liên tục ép mô hình học các mẫu khó, nếu số lượng cây (Trees) quá lớn và learning rate không phù hợp, Boosting RẤT DỄ BỊ OVERFITTING (ngược lại với Random Forest hầu như không bị overfitting khi tăng số cây)."
    ),
    "VOAI03-M42": (
        "- **CatBoost (Categorical Boosting):** Thuật toán Gradient Boosting do Yandex phát triển (2017).\n- **Đặc điểm nổi bật nhất:** Tên gọi CatBoost bắt nguồn từ **Cat**egorical + **Boost**ing. Nó nổi tiếng nhờ kỹ thuật mã hóa biến định danh tự động (Ordered Target Statistics) và cây đối xứng (Oblivious Trees) chạy cực nhanh trên GPU.",
        "Hầu hết các thuật toán ML khi gặp cột chữ (như Tỉnh/Thành phố có 63 giá trị) đều bắt lập trình viên phải tự đổi thành dạng One-Hot Encoding (làm dữ liệu phình to 63 cột) hoặc Label Encoding. CatBoost thông minh hơn hẳn: Bạn chỉ cần chỉ định tên cột chữ (`cat_features`), CatBoost sẽ tự động biến đổi thành các con số xác suất tối ưu mà không bị rò rỉ dữ liệu!",
        "CatBoost tính toán Target Encoding dựa trên hoán vị ngẫu nhiên (Random Permutations) của tập dữ liệu để ngăn chặn hiện tượng Target Leakage. Chọn **C** (Dữ liệu dạng phân loại / danh mục - Categorical Features).",
        "- **Phương án A (Ảnh chụp vệ tinh):** Dùng CNN hoặc Vision Transformer.\n- **Phương án B (Âm thanh sóng):** Dùng 1D-CNN hoặc mô hình chuỗi / Spectrogram.\n- **Phương án D (Đồ thị):** Dùng Graph Neural Networks (GNN).",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Trong các cuộc thi dữ liệu bảng (Kaggle / OLP AI Tabular), CatBoost thường là lựa chọn số 1 khi bộ dữ liệu chứa nhiều cột phân loại có độ đo lớn (High-cardinality Categoricals)."
    ),
    "VOAI03-M43": (
        "- **LightGBM (Light Gradient Boosting Machine):** Thuật toán do Microsoft phát triển (2016).\n- **Chiến lược Leaf-wise (Best-first):** Tại mỗi bước phân chia, thuật toán tìm nút lá có độ giảm tổn thất (Loss reduction) lớn nhất trên toàn bộ cây để tách tiếp, bất kể độ sâu của lá đó.\n- **Chiến lược Level-wise (Depth-first):** Phân chia đều tất cả các nút trên cùng một tầng trước khi xuống tầng tiếp theo (như XGBoost truyền thống).",
        "XGBoost truyền thống giống như một đội xây nhà làm việc tuần tự: Phải xây xong toàn bộ tầng 1 thì mới được phép xây lên tầng 2 (Level-wise). Còn LightGBM giống như một nhà thầu linh hoạt: Phòng nào xây nhanh nhất và mang lại nhiều lợi ích nhất thì tập trung xây cao vút lên trước (Leaf-wise). Cách làm này giảm sai số nhanh hơn rất nhiều nhưng cần giới hạn `max_depth` để không bị Overfitting!",
        "Chiến lược Leaf-wise có thể giảm nhiều hàm mất mát hơn với cùng số lượng phép tách so với Level-wise. Đồng thời, LightGBM kết hợp thuật toán rời rạc hóa Histogram giúp tăng tốc độ huấn luyện gấp 10-20 lần. Chọn **B** (Chiến lược phát triển cây theo lá - Leaf-wise / Best-first).",
        "- **Phương án A (Level-wise):** Là chiến lược mặc định của XGBoost truyền thống.\n- **Phương án C (Oblivious Tree):** Là cấu trúc cây nhị phân đối xứng của CatBoost.\n- **Phương án D (Random Split):** Là đặc trưng của Extra Trees.",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Để kiểm soát Overfitting khi dùng Leaf-wise trong LightGBM, bạn luôn phải đặt tham số `num_leaves` nhỏ hơn $2^{\\text{max\\_depth}}$ (thường đặt `num_leaves = 31`)."
    ),
    "VOAI03-M44": (
        "- **Stacking (Stacked Generalization):** Phương pháp Ensemble học kết hợp mô hình meta (Meta-learner).\n- **Cơ chế:** Dùng dự đoán của nhiều mô hình nền tảng (Base Models - ví dụ XGBoost, CatBoost, Random Forest, Neural Net) làm các đặc trưng đầu vào mới ($X_{\\text{meta}}$) để huấn luyện một mô hình cấp cao hơn (Meta-model - thường là Ridge hoặc Logistic Regression).\n- **Out-of-Fold (OOF) Predictions:** Bắt buộc dùng dự đoán OOF từ K-Fold Cross-Validation để tạo $X_{\\text{meta}}$ nhằm chống rò rỉ dữ liệu.",
        "Stacking giống như một hội đồng thẩm phán: Các luật sư và chuyên gia khác nhau (Base Models) đưa ra các bản báo cáo nhận định độc lập. Một thẩm phán trưởng công tâm (Meta-Learner) sẽ ngồi lại, cân nhắc xem trong trường hợp nào thì nên tin chuyên gia nào, để đưa ra phán quyết cuối cùng chính xác nhất!",
        "Pipeline Stacking chuẩn mực:\n1. Chia Train set thành $K$ folds.\n2. Với mỗi Base Model, dự đoán OOF trên $K$ folds để ghép lại thành ma trận đặc trưng $X_{\\text{meta}}$.\n3. Huấn luyện Meta-Model trên $(X_{\\text{meta}}, y_{\\text{train}})$.\nChọn **B** (Dùng dự đoán của các mô hình cơ sở làm đầu vào để huấn luyện một mô hình Meta-Learner).",
        "- **Phương án A (Tính trung bình trọng số):** Đó là kỹ thuật Weighted Blending thông thường.\n- **Phương án C (Nhân bản cây):** Đó là Bagging.\n- **Phương án D:** Không có liên quan đến Stacking.",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Stacking là vũ khí tối thượng giúp các đội thi giật giải cao trong các kỳ thi học máy và AI Olympic khi kết hợp được thế mạnh của cả họ mô hình Cây (Trees) và mạng Học sâu (Deep Learning)."
    ),
    "VOAI03-M45": (
        "- **Feature Subsampling (Lấy mẫu ngẫu nhiên đặc trưng):** Kỹ thuật chọn ngẫu nhiên một tập con đặc trưng tại mỗi nút phân chia của cây quyết định.\n- **Mục tiêu cốt lõi:** Làm giảm sự tương quan (Decorrelate) giữa các cây trong rừng (Random Forest).\n- **Số lượng đặc trưng chuẩn:** Cho bài toán Phân loại là $m = \\lfloor \\sqrt{p} \\rfloor$; cho Hồi quy là $m = \\lfloor p/3 \\rfloor$ (với $p$ là tổng số cột đặc trưng).",
        "Nếu trong dữ liệu có một cột quá mạnh (ví dụ cột 'Mức lương' quyết định 80% khả năng mua nhà), thì nếu không lấy mẫu ngẫu nhiên, tất cả 100 cây trong rừng đều sẽ chọn cột 'Mức lương' ở nút đầu tiên! Khi đó 100 cây sẽ trông giống hệt nhau, việc bỏ phiếu tập thể trở nên vô nghĩa. Bằng cách giấu bớt các cột mạnh ở một số cây, các cây buộc phải tìm tòi những cột tiềm năng khác $\\implies$ Rừng đa dạng và mạnh mẽ hơn!",
        "Công thức phương sai của Random Forest:\n$$\\text{Var}(\\bar{f}) = \\rho \\sigma^2 + \\frac{1 - \\rho}{B} \\sigma^2$$\nKhi lấy mẫu đặc trưng ngẫu nhiên $m = \\sqrt{p}$, hệ số tương quan giữa các cây $\\rho$ giảm xuống rõ rệt, kéo phương sai tổng thể của cả khu rừng giảm theo. Chọn **B** (Giảm độ tương quan giữa các cây trong rừng giúp tăng tính khái quát hóa).",
        "- **Phương án A (Tăng độ tương quan):** Ngược lại, mục tiêu là GIẢM tương quan.\n- **Phương án C & D:** Không phải mục đích chính.",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Xem câu M08 Đề 03: Đây chính là điểm khác biệt sống còn giữa Random Forest và Bagging cây quyết định thông thường (Bagging thường dùng toàn bộ $p$ đặc trưng tại mỗi nút)."
    ),
    "VOAI03-M46": (
        "- **FT-Transformer (Feature Tokenizer + Transformer):** Kiến trúc Deep Learning cho dữ liệu bảng do Gorishniy et al. đề xuất năm 2021.\n- **Feature Tokenizer:** Biến đổi từng giá trị số (Numerical feature) và biến danh mục (Categorical feature) thành một vector nhúng (Embedding vector) kích thước $d$.\n- **Multi-Head Self-Attention:** Cho phép các cột trong cùng một dòng dữ liệu tương tác qua lại để học quan hệ phi tuyến phức tạp.",
        "Trong xử lý ngôn ngữ tự nhiên, mỗi từ ngữ được biến thành một vector embedding. FT-Transformer áp dụng y nguyên ý tưởng đó cho bảng tính: Biến cột 'Tuổi tác = 25' và cột 'Huyết áp = 120' thành hai vector ngữ nghĩa độc lập, sau đó cho chúng 'nói chuyện' với nhau qua cơ chế Self-Attention giống hệt mô hình ngôn ngữ!",
        "FT-Transformer áp dụng phép chiếu tuyến tính có trọng số độc lập cho từng đặc trưng số: $e_j(x_j) = x_j \\cdot W_j + b_j \\in \\mathbb{R}^d$. Sau đó đưa chuỗi các tokens đặc trưng qua nhiều tầng Transformer Encoder. Chọn **B** (Biến đổi từng đặc trưng số và danh mục thành vector nhúng Feature Token rồi qua Transformer).",
        "- **Phương án A:** Chỉ là MLP thông thường.\n- **Phương án C:** ResNet cho dữ liệu bảng dùng skip connection, không có tokenizer.\n- **Phương án D:** XGBoost là cây, không phải mạng Transformer.",
        "📚 Xem **§1.4 Deep Learning cho Dữ liệu bảng (Modern Tabular DL)**.\n🔗 **Liên hệ bài cũ:** Mặc dù FT-Transformer rất mạnh mẽ và học được biểu diễn trừu tượng cao, nhưng trên dữ liệu bảng thông thường, các mô hình cây Boosting (XGBoost/LightGBM/CatBoost) vẫn chiếm ưu thế áp đảo về tốc độ huấn luyện và khả năng chống nhiễu."
    ),
    "VOAI03-M47": (
        "- **TabM (Tabular Model with Parameter Batching):** Mô hình Deep Learning cho dữ liệu bảng tiên tiến nhất được chấp nhận tại hội nghị đỉnh cao **ICLR 2025**.\n- **Điểm đột phá:** Sử dụng một thân mạng MLP đa tầng chia sẻ (Shared Backbone) kết hợp với các vector tham số mảng hóa (Batch of Parameter Vectors), cho phép dự báo ensemble gồm $k$ mô hình chỉ với chi phí tính toán và bộ nhớ xấp xỉ một mô hình đơn lẻ!",
        "Trước đây, muốn ensemble 32 mô hình học sâu, bạn phải tốn gấp 32 lần thời gian và bộ nhớ GPU. TabM giống như một thân cây cổ thụ dùng chung một bộ rễ và thân chính vững chắc, nhưng trên ngọn tách ra 32 nhánh cành siêu nhẹ. Nhờ đó bạn có được sức mạnh của cả một đội quân 32 chuyên gia nhưng tốc độ chạy nhanh như một người đơn độc!",
        "TabM biểu diễn các trọng số dưới dạng tensor 3 chiều: $W \\in \\mathbb{R}^{k \\times d_{in} \\times d_{out}}$ được tính toán song song qua phép nhân ma trận mảng hóa (Batch Matrix Multiplication). Chọn **A** (Mô hình TabM ICLR 2025 với cơ chế Parameter Batching chia sẻ backbone).",
        "- **Phương án B, C, D:** Các mô hình thế hệ trước (TabNet 2019, NODE 2020, Saint 2021).",
        "📚 Xem **§1.4 Deep Learning cho Dữ liệu bảng (Modern Tabular DL)**.\n🔗 **Liên hệ bài cũ:** Đây là kiến thức đón đầu công nghệ mới nhất xuất hiện trong các đề thi tuyển chọn tài năng AI và Olympic AI 2025-2026."
    ),
    "VOAI03-M48": (
        "- **Gradient Boosting:** Thuật toán huấn luyện chuỗi các cây quyết định tuần tự bằng phương pháp giảm độ dốc (Gradient Descent) trong không gian hàm.\n- **Phần dư giả (Pseudo-residuals):** Đạo hàm âm của hàm mất mát theo dự đoán hiện tại: $r_{im} = -\\left[ \\frac{\\partial \\mathcal{L}(y_i, F(x_i))}{\\partial F(x_i)} \\right]_{F=F_{m-1}}$.\n- **Ý nghĩa:** Cây mới ở bước $m$ được huấn luyện để xấp xỉ các phần dư này.",
        "Tưởng tượng bạn đang ném phi tiêu vào hồng tâm: Lần ném thứ nhất bị lệch sang trái 10 cm ($F_1$). Lần ném thứ hai, bạn không ném lại từ đầu, mà bạn bảo đồng đội của mình hãy nhắm bù sang phải đúng 10 cm ($h_2$). Tổng hợp hai lần ném ($F_1 + h_2$) phi tiêu sẽ găm trúng hồng tâm! Gradient Boosting liên tục huấn luyện cây sau để bù đắp đúng phần sai số còn lại của các cây trước.",
        "Thuật toán Gradient Boosting:\n$$F_m(x) = F_{m-1}(x) + \\eta \\sum_{j=1}^J \\gamma_{jm} \\mathbb{I}(x \\in R_{jm})$$\nTrong đó cây thứ $m$ khớp trực tiếp vào giá trị âm của đạo hàm (Negative Gradient / Residuals). Chọn **A** (Học phần sai số dư - Residuals / Negative Gradient của các cây trước đó).",
        "- **Phương án B (Tăng trọng số mẫu sai):** Đó là cơ chế riêng của AdaBoost (Adaptive Boosting), không phải tổng quát của Gradient Boosting.\n- **Phương án C:** Cây sau không chạy độc lập mà phụ thuộc vào cây trước.",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Đối với hàm mất mát MSE $\\mathcal{L} = \\frac{1}{2}(y - \\hat{y})^2$, đạo hàm âm $-\\partial \\mathcal{L} / \\partial \\hat{y}$ chính bằng phần dư thực tế $y - \\hat{y}$."
    ),
    "VOAI03-M49": (
        "- **Target Leakage (Rò rỉ biến mục tiêu trong Target Encoding):** Khi tính giá trị trung bình mục tiêu của một danh mục, nếu dùng luôn giá trị $y_i$ của chính dòng đó, mô hình sẽ bị rò rỉ nhãn và Overfitting nghiêm trọng.\n- **Ordered Target Statistics (CatBoost):** Hoán vị ngẫu nhiên toàn bộ tập dữ liệu, và khi tính thống kê cho dòng thứ $i$, chỉ sử dụng các dòng có cùng danh mục đứng TRƯỚC nó trong thứ tự hoán vị.\n- **Ordered Boosting:** Áp dụng nguyên lý trật tự thời gian nhân tạo này vào cả quá trình tính toán gradient để loại bỏ hiện tượng lệch dự đoán (Prediction Shift).",
        "Nếu bạn tính điểm trung bình của một học sinh bằng cách lấy cả bài thi của chính bạn đó vào mẫu số, bạn đó sẽ tự chấm điểm cho mình (rò rỉ mục tiêu!). Kỹ thuật Ordered Boosting giống như việc xếp hàng các học sinh theo một trật tự ngẫu nhiên: Bạn đứng ở vị trí số 10 chỉ được phép tham khảo kết quả của 9 bạn đứng trước mình trong hàng, tuyệt đối không được nhìn bài của chính mình hay của các bạn đứng sau!",
        "Công thức Ordered Target Statistic của CatBoost cho mẫu $x_k$ tại hoán vị $\\sigma$:\n$$\\hat{x}_{k}^j = \\frac{\\sum_{j=1}^{k-1} [x_{\\sigma(j), k} = x_{\\sigma(i), k}] \\cdot y_{\\sigma(j)} + a \\cdot P}{\\sum_{j=1}^{k-1} [x_{\\sigma(j), k} = x_{\\sigma(i), k}] + a}$$\nTriệt tiêu hoàn toàn rò rỉ thông tin mục tiêu. Chọn **A** (Ngăn ngừa rò rỉ mục tiêu - Target Leakage và hiện tượng Prediction Shift).",
        "- **Phương án B:** Ordered Boosting tốn thêm thời gian tính toán hoán vị, không làm tăng tốc độ.\n- **Phương án C & D:** Không phải mục đích của kỹ thuật này.",
        "📚 Xem **§1.4 Ensemble: Bagging, Random Forest & Boosting**.\n🔗 **Liên hệ bài cũ:** Nhờ Ordered Boosting, CatBoost là thư viện GBDT duy nhất có khả năng chạy mượt mà ngay trên các bộ dữ liệu nhỏ mà không bị hiện tượng quá khớp sớm."
    ),
    "VOAI03-M50": (
        "- **Dữ liệu chuỗi thời gian (Time Series Data):** Dữ liệu có sự phụ thuộc nhân quả theo trật tự thời gian ($t_1 < t_2 < t_3 < \\dots$).\n- **Temporal Leakage (Rò rỉ thời gian / Look-ahead Bias):** Hiện tượng dùng thông tin từ tương lai để huấn luyện mô hình dự đoán quá khứ.\n- **TimeSeriesSplit (Rolling / Expanding Window):** Kỹ thuật chia fold lũy tiến: Tập train luôn đứng trước tập validation theo trục thời gian.",
        "Dự đoán tương lai (như giá cổ phiếu ngày mai) giống như việc sống trong đời thực: Bạn chỉ có ký ức của ngày hôm qua và hôm nay để quyết định cho ngày mai. Nếu dùng K-Fold ngẫu nhiên, bạn sẽ lấy dữ liệu của ngày thứ Sáu để dự đoán cho ngày thứ Ba! Mô hình sẽ 'nhìn thấy trước tương lai' và đạt điểm kiểm tra cao giả tạo, nhưng khi đem ra giao dịch thực tế sẽ bị thua lỗ thảm hại!",
        "Khi áp dụng Standard K-Fold lên Time Series, tính tự tương quan (Autocorrelation) giữa các mốc thời gian liền kề sẽ gây rò rỉ thông tin từ fold train sang fold test, vi phạm giả định độc lập và đồng phân phối (i.i.d). Bắt buộc phải dùng `TimeSeriesSplit`. Chọn **D** (Gây rò rỉ dữ liệu tương lai sang quá khứ - Look-ahead Bias / Temporal Leakage).",
        "- **Phương án A:** Chuỗi thời gian không nhất thiết phải tuân theo phân phối chuẩn.\n- **Phương án B:** K-Fold không làm thay đổi số chiều dữ liệu.\n- **Phương án C:** K-Fold vẫn tạo đủ số lượng fold.",
        "📚 Xem **§1.5 Cross-Validation & Chuỗi thời gian (Time Series)**.\n🔗 **Liên hệ bài cũ:** Trong đề thi OLP AI, khi gặp bài toán dự báo phụ tải điện, giá thị trường hoặc chuỗi văn bản, luôn ghi nhớ nguyên tắc: KHÔNG BAO GIỜ SHUFFLE DỮ LIỆU CHUỖI THỜI GIAN!"
    )
}

# Tiến hành cập nhật
qs = exam_data["questions"]
count = 0
for q in qs:
    qid = q["id"]
    if qid in UPGRADES_31_50:
        term, eli5, math, trap, ref = UPGRADES_31_50[qid]
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

print(f"Đã nâng cấp trọn vẹn {count} câu (M31-M50) trong Đề 03!")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Đã hoàn tất lưu file Đề 03!")
