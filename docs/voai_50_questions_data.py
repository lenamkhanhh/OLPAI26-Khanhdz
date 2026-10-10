# -*- coding: utf-8 -*-
"""
Dữ liệu chi tiết 50 câu trắc nghiệm đề thi thử VOAI 2026
Bao gồm:
- id: Số thứ tự câu (1-50)
- question: Nội dung câu hỏi
- options: Danh sách 4 phương án [A, B, C, D]
- correct_answer: Phương án đúng ('A', 'B', 'C', 'D')
- explanation: Phân tích bản chất, chứng minh toán học, công thức tính tay
- section_ref: Mã mục lý thuyết trong Handbook để tra cứu (§x.y)
- trap: Bẫy đề thi hay gặp ở câu này
"""

VOAI_QUESTIONS = [
    {
        "id": 1,
        "question": "Cho ma trận $A$ kích thước $n \\times n$. Nếu $A$ là ma trận trực giao (orthogonal matrix), phát biểu nào sau đây là ĐÚNG?",
        "options": [
            "A. $A^T = A^{-1}$",
            "B. Định thức của $A$ luôn bằng 0.",
            "C. $A$ là ma trận suy biến.",
            "D. Các hàng của $A$ phụ thuộc tuyến tính."
        ],
        "correct": "A",
        "explanation": r"Theo định nghĩa ma trận trực giao trong đại số tuyến tính: $A^T A = A A^T = I_n$. Điều này trực tiếp suy ra ma trận nghịch đảo $A^{-1} = A^T$. Hơn nữa, lấy định thức hai vế: $\det(A^T A) = \det(A)^2 = \det(I) = 1 \implies \det(A) = \pm 1 \neq 0$, do đó $A$ luôn khả nghịch (không bao giờ suy biến), và các hàng/cột của $A$ tạo thành một hệ trực chuẩn độc lập tuyến tính.",
        "section_ref": "§5.1 & §5.2",
        "trap": "Nhầm lẫn giữa trực giao (orthogonal, $\\det = \\pm 1$) với ma trận suy biến (singular, $\\det = 0$)."
    },
    {
        "id": 2,
        "question": "Trong tối ưu hóa, nếu ma trận Hessian của hàm số tại một điểm cực trị là xác định dương (positive definite), điểm đó là:",
        "options": [
            "A. Điểm cực đại địa phương.",
            "B. Điểm cực tiểu địa phương.",
            "C. Điểm yên ngựa.",
            "D. Điểm không xác định."
        ],
        "correct": "B",
        "explanation": r"Xét khai triển Taylor bậc 2 của hàm $f(\mathbf{x})$ quanh điểm dừng $\mathbf{x}^*$ (nơi $\nabla f(\mathbf{x}^*) = \mathbf{0}$): $f(\mathbf{x}) \approx f(\mathbf{x}^*) + \frac{1}{2}(\mathbf{x} - \mathbf{x}^*)^T H (\mathbf{x} - \mathbf{x}^*)$. Nếu ma trận Hessian $H = \nabla^2 f(\mathbf{x}^*)$ là xác định dương ($H \succ 0$, tức $\mathbf{u}^T H \mathbf{u} > 0, \; \forall \mathbf{u} \neq \mathbf{0}$, mọi trị riêng $\lambda_i > 0$), hàm số cong lồi lên trên tại mọi hướng $\implies \mathbf{x}^*$ là điểm cực tiểu địa phương (local minimum). (Ngược lại xác định âm $\implies$ cực đại; nửa xác định hoặc đổi dấu $\implies$ điểm yên ngựa).",
        "section_ref": "§5.2",
        "trap": "Nhầm lẫn chiều lồi: Đạo hàm bậc hai $> 0$ tương ứng cực tiểu (min), không phải cực đại (max)."
    },
    {
        "id": 3,
        "question": "(Khó) Tính đạo hàm của hàm số $f(x) = \\ln(1 + e^{-x})$. Kết quả nào sau đây đúng?",
        "options": [
            "A. $f'(x) = \\sigma(x) - 1$ (với $\\sigma$ là hàm sigmoid)",
            "B. $f'(x) = \\sigma(x)$",
            "C. $f'(x) = 1 + \\sigma(x)$",
            "D. $f'(x) = e^{-x}$"
        ],
        "correct": "A",
        "explanation": r"Áp dụng quy tắc đạo hàm hàm hợp $(\ln u)' = \frac{u'}{u}$: $f'(x) = \frac{(1 + e^{-x})'}{1 + e^{-x}} = \frac{-e^{-x}}{1 + e^{-x}} = -\frac{1}{e^x + 1}$. Mặt khác, hàm sigmoid là $\sigma(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1}$. Khi đó: $\sigma(x) - 1 = \frac{e^x}{e^x + 1} - 1 = \frac{e^x - (e^x + 1)}{e^x + 1} = -\frac{1}{e^x + 1} = f'(x)$. Đây là đạo hàm của hàm Softplus lật ngược, xuất hiện liên tục trong bài toán Logistic Regression và Binary Cross-Entropy.",
        "section_ref": "§2.2 & §5.2",
        "trap": "Quên dấu trừ khi đạo hàm $e^{-x}$ dẫn đến chọn nhầm B hoặc C."
    },
    {
        "id": 4,
        "question": "Đại lượng nào đo lường mức độ 'bất ngờ' hoặc thông tin trung bình của một phân phối xác suất?",
        "options": [
            "A. Phương sai.",
            "B. Entropy.",
            "C. Độ lệch chuẩn.",
            "D. Kỳ vọng."
        ],
        "correct": "B",
        "explanation": r"Trong lý thuyết thông tin của Claude Shannon, lượng tin cá biệt (surprisal) của biến cố $x$ có xác suất $p(x)$ là $I(x) = -\log_2 p(x)$. Kỳ vọng lượng tin trên toàn bộ phân phối chính là Shannon Entropy: $H(X) = \mathbb{E}[I(X)] = -\sum_{x} p(x) \log_2 p(x)$. Entropy đo lường độ bất định (uncertainty) và mức độ bất ngờ trung bình.",
        "section_ref": "§1.3",
        "trap": "Phương sai chỉ đo độ phân tán của biến ngẫu nhiên số thực quanh giá trị trung bình, không đo thông tin của phân phối xác suất."
    },
    {
        "id": 5,
        "question": "Trong thuật toán K-Nearest Neighbors (KNN), khi giá trị $k$ quá nhỏ, mô hình có xu hướng:",
        "options": [
            "A. Bị Underfitting.",
            "B. Bị Overfitting và nhạy cảm với nhiễu.",
            "C. Có độ chệch (Bias) cao.",
            "D. Luôn cho kết quả chính xác nhất."
        ],
        "correct": "B",
        "explanation": r"Khi $k$ nhỏ (ví dụ $k=1$), nhãn dự đoán hoàn toàn phụ thuộc vào điểm gần nhất. Ranh giới quyết định (Voronoi) sẽ uốn lượn ôm sát từng điểm dữ liệu, kể cả các điểm nhiễu ngoại lai (outliers) $\implies$ High Variance, Low Bias, dẫn đến hiện tượng Overfitting nghiêm trọng. Ngược lại khi $k \to N$, mô hình chỉ dự đoán theo lớp đa số $\implies$ Underfitting, High Bias.",
        "section_ref": "§1.1 & §1.5",
        "trap": "Nghĩ rằng $k=1$ khớp 100% tập train nghĩa là 'kết quả chính xác nhất'."
    },
    {
        "id": 6,
        "question": "Thuật toán nào sau đây KHÔNG thuộc nhóm học có giám sát (Supervised Learning)?",
        "options": [
            "A. Support Vector Machine.",
            "B. Random Forest.",
            "C. Principal Component Analysis (PCA).",
            "D. Logistic Regression."
        ],
        "correct": "C",
        "explanation": r"PCA (Principal Component Analysis - Phân tích thành phần chính) là thuật toán học không giám sát (Unsupervised Learning) dùng để giảm chiều dữ liệu. PCA tìm các trục trực giao cực đại hóa phương sai của tập dữ liệu mà hoàn toàn không sử dụng bất kỳ nhãn mục tiêu $y$ nào.",
        "section_ref": "§1.1 & §1.8",
        "trap": "Nhầm Logistic Regression là Unsupervised vì chữ 'Regression'."
    },
    {
        "id": 7,
        "question": "Mục tiêu chính của kỹ thuật 'Pruning' (tỉa cành) trong cây quyết định là gì?",
        "options": [
            "A. Tăng độ sâu của cây.",
            "B. Giảm hiện tượng Overfitting.",
            "C. Tăng số lượng nút lá.",
            "D. Làm cho cây phức tạp hơn."
        ],
        "correct": "B",
        "explanation": r"Cây quyết định nếu phát triển không giới hạn sẽ tiếp tục chia nhánh tới khi mọi nút lá đều thuần khiết, học cả nhiễu và overfit. Kỹ thuật tỉa cành (Pre-pruning: giới hạn max_depth, min_samples_split; hoặc Post-pruning: Cost-Complexity Pruning) loại bỏ các nhánh cây con không mang lại ý nghĩa thống kê trên tập validation, giúp giảm phương sai và kiểm soát Overfitting.",
        "section_ref": "§1.3",
        "trap": "Nhầm tỉa cành là làm tăng độ sâu để nâng cao accuracy trên tập train."
    },
    {
        "id": 8,
        "question": "Thuật toán Random Forest kết hợp nhiều cây quyết định bằng phương pháp:",
        "options": [
            "A. Boosting.",
            "B. Bagging.",
            "C. Stacking.",
            "D. Cascading."
        ],
        "correct": "B",
        "explanation": r"Random Forest là phương pháp Bagging (Bootstrap Aggregating) kết hợp Random Subspaces. Mô hình tạo ra $B$ tập con bằng cách lấy mẫu ngẫu nhiên có hoàn lại (bootstrap) từ tập train gốc, huấn luyện song song $B$ cây quyết định độc lập, và tổng hợp kết quả bằng biểu quyết đa số (classification) hoặc trung bình (regression) nhằm giảm phương sai.",
        "section_ref": "§1.4",
        "trap": "Nhầm giữa Bagging (song song, giảm variance) và Boosting (tuần tự, giảm bias)."
    },
    {
        "id": 9,
        "question": "Chỉ số F1-Score là trung bình điều hòa của hai đại lượng nào?",
        "options": [
            "A. Accuracy và Recall.",
            "B. Precision và Accuracy.",
            "C. Precision và Recall.",
            "D. Specificity và Sensitivity."
        ],
        "correct": "C",
        "explanation": r"Chỉ số $F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$. Trung bình điều hòa (Harmonic Mean) được sử dụng vì nó phạt rất nặng khi một trong hai đại lượng tiệm cận 0, đảm bảo mô hình cân bằng tốt giữa khả năng phân loại chính xác mẫu dương (Precision) và khả năng bắt trọn mẫu dương (Recall).",
        "section_ref": "§1.7",
        "trap": "Nhầm F1 là trung bình cộng (Arithmetic Mean) giữa Precision và Recall."
    },
    {
        "id": 10,
        "question": "Trong Linear Regression, nếu các biến độc lập có tương quan rất mạnh với nhau, hiện tượng này gọi là:",
        "options": [
            "A. Đa cộng tuyến (Multicollinearity).",
            "B. Tự tương quan.",
            "C. Phương sai thay đổi.",
            "D. Nhiễu trắng."
        ],
        "correct": "A",
        "explanation": r"Hiện tượng đa cộng tuyến (Multicollinearity) xuất hiện khi hai hoặc nhiều biến giải thích $X_i, X_j$ có tương quan tuyến tính cao. Khi đó ma trận hiệp phương sai $X^T X$ có định thức gần bằng 0 (gần suy biến), ma trận nghịch đảo $(X^T X)^{-1}$ không ổn định số học, khiến phương sai của các hệ số hồi quy $\hat{\beta}$ bùng nổ, làm dấu của trọng số bị đảo lộn bất thường.",
        "section_ref": "§1.6 & §5.3",
        "trap": "Tự tương quan (Autocorrelation) là tương quan của chính một biến với các bước trễ của nó trong dữ liệu chuỗi thời gian, không phải giữa các biến khác nhau."
    },
    {
        "id": 11,
        "question": "Hàm loss nào thường được dùng cho bài toán Logistic Regression?",
        "options": [
            "A. Mean Squared Error.",
            "B. Binary Cross-Entropy (Log Loss).",
            "C. Hinge Loss.",
            "D. Huber Loss."
        ],
        "correct": "B",
        "explanation": r"Logistic Regression mô hình hóa xác suất bằng hàm Sigmoid $p = \sigma(\mathbf{w}^T \mathbf{x})$. Tối ưu hóa ước lượng hợp lý cực đại (MLE) dẫn trực tiếp đến hàm mất mát Binary Cross-Entropy (Log Loss): $\mathcal{L} = -\frac{1}{N} \sum [y_i \ln p_i + (1 - y_i) \ln(1 - p_i)]$. MSE nếu dùng cho Logistic Regression sẽ tạo ra hàm mất mát không lồi (non-convex) có nhiều cực tiểu địa phương giả.",
        "section_ref": "§1.1 & §2.4",
        "trap": "Nghĩ rằng dùng MSE cho Logistic Regression vẫn được (thực tế MSE tạo loss surface không lồi)."
    },
    {
        "id": 12,
        "question": "(Khó) Cho ma trận nhầm lẫn: TP=80, FP=10, FN=20, TN=90. Precision của mô hình là:",
        "options": [
            "A. 0.8",
            "B. 0.88",
            "C. 0.75",
            "D. 0.9"
        ],
        "correct": "B",
        "explanation": r"Công thức Precision: $\text{Precision} = \frac{TP}{TP + FP} = \frac{80}{80 + 10} = \frac{80}{90} \approx 0.8888... \approx 0.88$ (hoặc 0.89). Trong khi đó $\text{Recall} = \frac{TP}{TP + FN} = \frac{80}{80 + 20} = 0.80$; $\text{Accuracy} = \frac{TP + TN}{\text{Total}} = \frac{80 + 90}{200} = 0.85$.",
        "section_ref": "§1.7",
        "trap": "Chia nhầm mẫu số thành $TP + FN$ (ra 0.80 là Recall) hoặc $TP + TN$."
    },
    {
        "id": 13,
        "question": "Tại sao hàm kích hoạt phi tuyến là cần thiết trong mạng nơ-ron?",
        "options": [
            "A. Để làm mạng chạy nhanh hơn.",
            "B. Để mạng có thể học được các ranh giới quyết định phức tạp (phi tuyến).",
            "C. Để giới hạn giá trị trọng số.",
            "D. Để thay thế lớp Dropout."
        ],
        "correct": "B",
        "explanation": r"Nếu các hàm kích hoạt đều là tuyến tính $f(z) = c z$, việc ghép nối nhiều lớp ẩn liên tiếp chỉ tương đương với một phép nhân ma trận đơn lẻ duy nhất: $\mathbf{W}_2(\mathbf{W}_1 \mathbf{x}) = (\mathbf{W}_2 \mathbf{W}_1)\mathbf{x} = \mathbf{W}_{net} \mathbf{x}$, biến toàn bộ mạng sâu thành một mô hình tuyến tính đơn giản (không thể học bài toán XOR). Hàm phi tuyến phá vỡ tính chất tuyến tính, cho phép mạng xấp xỉ bất kỳ hàm số liên tục nào theo Định lý Xấp xỉ Phổ quát (Universal Approximation Theorem).",
        "section_ref": "§2.1 & §2.2",
        "trap": "Nghĩ rằng phi tuyến giúp mạng chạy nhanh hơn (thực tế hàm phi tuyến tốn tài nguyên tính toán hơn)."
    },
    {
        "id": 14,
        "question": "(Khó) Một lớp Convolution có filter $5 \\times 5$, input channels là 3, số lượng filter là 16. Tổng số tham số (không tính bias) là:",
        "options": [
            "A. 1200",
            "B. 400",
            "C. 240",
            "D. 384"
        ],
        "correct": "A",
        "explanation": r"Mỗi bộ lọc (filter) phải quét qua toàn bộ các kênh của đầu vào ($C_{in} = 3$), do đó kích thước thực sự của một kernel 3D là $K_h \times K_w \times C_{in} = 5 \times 5 \times 3 = 75$ trọng số. Với 16 filter riêng biệt để sinh ra 16 kênh đầu ra ($C_{out} = 16$), tổng số tham số trọng số là: $75 \times 16 = 1200$. (Nếu tính cả hệ số bias thì cộng thêm 16 bias $\implies 1216$).",
        "section_ref": "§3.1",
        "trap": "Quên nhân với số kênh đầu vào ($C_{in} = 3$): $5 \times 5 \times 16 = 400$ (sai thiếu kênh)."
    },
    {
        "id": 15,
        "question": "Trong LSTM, cổng (gate) nào quyết định thông tin nào từ trạng thái ô (cell state) cũ sẽ bị loại bỏ?",
        "options": [
            "A. Input Gate.",
            "B. Forget Gate.",
            "C. Output Gate.",
            "D. Update Gate."
        ],
        "correct": "B",
        "explanation": r"Cổng quên (Forget Gate) trong LSTM tính toán: $\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f) \in (0, 1)$. Giá trị của $\mathbf{f}_t$ được nhân từng phần tử với trạng thái ô trước đó $\mathbf{C}_{t-1}$. Giá trị gần 0 đồng nghĩa 'quên hoàn toàn', giá trị gần 1 đồng nghĩa 'giữ nguyên hoàn toàn'.",
        "section_ref": "§4.4",
        "trap": "Nhầm Input Gate là cổng quyết định xóa thông tin (Input Gate quyết định nạp thông tin mới)."
    },
    {
        "id": 16,
        "question": "(Khó) Cho đầu vào $W \\times H$, filter $K \\times K$, padding $P$, stride $S$. Công thức tính kích thước đầu ra $W_{out}$ là:",
        "options": [
            "A. $(W - K + 2P)/S + 1$ (làm tròn xuống $\\lfloor \\cdot \\rfloor$)",
            "B. $(W + K - P)/S$",
            "C. $W/S + P$",
            "D. $(W - K + P)/S$"
        ],
        "correct": "A",
        "explanation": r"Công thức kinh điển xác định kích thước không gian đầu ra của tầng Conv2D: $W_{out} = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$. Padding $P$ được thêm vào cả hai phía (trái và phải) nên tổng độ rộng được bù là $2P$.",
        "section_ref": "§3.1",
        "trap": "Chỉ cộng $P$ thay vì $2P$ (quên padding ở cả hai đầu biên)."
    },
    {
        "id": 17,
        "question": "Hàm kích hoạt nào thường được dùng ở lớp cuối của bài toán phân loại đa lớp (Multi-class Classification)?",
        "options": [
            "A. Sigmoid.",
            "B. Softmax.",
            "C. Tanh.",
            "D. ReLU."
        ],
        "correct": "B",
        "explanation": r"Hàm Softmax biến đổi vector logit $\mathbf{z} \in \mathbb{R}^C$ thành phân phối xác suất hợp lệ: $\sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^C e^{z_j}}$, thỏa mãn $\sum_{i=1}^C \sigma(\mathbf{z})_i = 1$ và $\sigma(\mathbf{z})_i \in (0, 1)$, phù hợp với phân loại đa lớp loại trừ lẫn nhau (mutually exclusive). Sigmoid chỉ dùng cho phân loại nhị phân hoặc đa nhãn (multi-label).",
        "section_ref": "§2.2 & §2.4",
        "trap": "Dùng Sigmoid cho đa lớp (Sigmoid cho tổng xác suất $> 1$, chỉ đúng với bài toán Multi-label)."
    },
    {
        "id": 18,
        "question": "Trong thuật toán tối ưu Adam, tham số $\\beta_1$ và $\\beta_2$ thường được dùng để:",
        "options": [
            "A. Tính toán trung bình động của gradient và bình phương gradient.",
            "B. Thay đổi kích thước batch.",
            "C. Khởi tạo trọng số.",
            "D. Cắt (clip) gradient."
        ],
        "correct": "A",
        "explanation": r"Adam duy trì hai moment: $\beta_1$ (mặc định $0.9$) là hệ số suy giảm của trung bình động gradient (Moment bậc 1: $m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$), tương tự Momentum. $\beta_2$ (mặc định $0.999$) là hệ số của trung bình động bình phương gradient (Moment bậc 2: $v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$), tương tự RMSProp.",
        "section_ref": "§2.5",
        "trap": "Nhầm $\\beta_1, \\beta_2$ với hệ số clipping gradient hay learning rate."
    },
    {
        "id": 19,
        "question": "Mạng Generative Adversarial Networks (GAN) bao gồm hai thành phần chính nào?",
        "options": [
            "A. Encoder và Decoder.",
            "B. Generator và Discriminator.",
            "C. Actor và Critic.",
            "D. Input và Output."
        ],
        "correct": "B",
        "explanation": r"GAN (Goodfellow et al., 2014) gồm Mạng sinh (Generator $G$) cố gắng biến vector nhiễu ngẫu nhiên thành mẫu giả giống thật, và Mạng phân định (Discriminator $D$) cố gắng phân biệt mẫu thật từ dataset và mẫu giả từ $G$. Hai mạng được huấn luyện đối kháng qua trò chơi minimax hai người.",
        "section_ref": "§3.8",
        "trap": "Encoder và Decoder là kiến trúc của VAE (Variational Autoencoder) hoặc Transformer, không phải GAN."
    },
    {
        "id": 20,
        "question": "Một nơ-ron có 3 đầu vào $(1, 2, 3)$, trọng số tương ứng là $(0.5, -1, 2)$ và bias là $0.5$. Nếu dùng hàm ReLU, đầu ra là:",
        "options": [
            "A. 5",
            "B. 0",
            "C. -4.5",
            "D. 4.5"
        ],
        "correct": "A",
        "explanation": r"Tổng tuyến tính đầu vào: $z = \sum w_i x_i + b = (1 \times 0.5) + (2 \times -1) + (3 \times 2) + 0.5 = 0.5 - 2.0 + 6.0 + 0.5 = 5.0$. Áp dụng hàm kích hoạt ReLU: $\text{ReLU}(z) = \max(0, z) = \max(0, 5.0) = 5.0$.",
        "section_ref": "§2.1",
        "trap": "Quên cộng bias $0.5$ dẫn đến ra $4.5$ (chọn D)."
    },
    {
        "id": 21,
        "question": "Phương pháp 'Bag of Words' (BoW) có nhược điểm lớn nhất là gì?",
        "options": [
            "A. Mất hoàn toàn thông tin về thứ tự và ngữ cảnh của từ.",
            "B. Tính toán quá chậm.",
            "C. Không thể đếm được tần suất từ.",
            "D. Chỉ dùng được cho tiếng Anh."
        ],
        "correct": "A",
        "explanation": r"BoW chỉ biểu diễn văn bản dưới dạng vector đếm tần số từ độc lập, bỏ qua hoàn toàn trật tự từ (Word Order) và ngữ pháp cấu trúc câu. Ví dụ: 'Tôi không thích anh ta nhưng tôi thích bạn' và 'Tôi thích anh ta nhưng tôi không thích bạn' sẽ có biểu diễn BoW hoàn toàn giống nhau.",
        "section_ref": "§4.2",
        "trap": "Nghĩ rằng BoW tính toán chậm (thực tế BoW tính rất nhanh nhưng biểu diễn thô)."
    },
    {
        "id": 22,
        "question": "'BERT' là mô hình dựa trên thành phần nào của Transformer?",
        "options": [
            "A. Encoder.",
            "B. Decoder.",
            "C. Cả hai.",
            "D. Không thành phần nào."
        ],
        "correct": "A",
        "explanation": r"BERT (Bidirectional Encoder Representations from Transformers) được xây dựng hoàn toàn từ chồng các khối Transformer Encoder, sử dụng cơ chế Self-Attention hai chiều (Bidirectional) để hiểu sâu sắc ngữ cảnh hai phía. Dòng GPT sử dụng Transformer Decoder (Autoregressive), còn T5/BART sử dụng cả Encoder lẫn Decoder.",
        "section_ref": "§4.6",
        "trap": "Nhầm BERT với GPT (Decoder) hoặc mô hình dịch máy gốc (gồm cả hai)."
    },
    {
        "id": 23,
        "question": "Hệ thống RAG (Retrieval-Augmented Generation) giúp mô hình LLM:",
        "options": [
            "A. Giảm hiện tượng 'ảo giác' (hallucination) bằng cách tham chiếu dữ liệu bên ngoài.",
            "B. Chạy nhanh hơn 10 lần.",
            "C. Không cần huấn luyện lại.",
            "D. Cả A và C đều đúng."
        ],
        "correct": "D",
        "explanation": r"RAG kết hợp một hệ thống truy xuất (Retriever) và một mô hình sinh (Generator). Khi người dùng hỏi, tài liệu liên quan từ kho dữ liệu ngoài được truy xuất và đính kèm vào ngữ cảnh của LLM. Kỹ thuật này vừa giảm ảo giác (hallucination) do có bằng chứng thực tế, vừa cho phép cập nhật tri thức mới tức thì mà không cần tốn chi phí train lại mô hình.",
        "section_ref": "§4.6 & §4.8",
        "trap": "Chỉ chọn A mà quên mất C (hoặc ngược lại)."
    },
    {
        "id": 24,
        "question": "Phép toán 'Max Pooling' có tác dụng:",
        "options": [
            "A. Giảm kích thước không gian và giữ lại đặc trưng nổi bật nhất.",
            "B. Tăng số lượng kênh.",
            "C. Thay đổi màu sắc ảnh.",
            "D. Tăng độ phân giải."
        ],
        "correct": "A",
        "explanation": r"Max Pooling trượt một cửa sổ (ví dụ $2 \times 2$, stride 2) trên từng feature map và lấy giá trị lớn nhất trong cửa sổ. Nó làm giảm 1/2 kích thước không gian chiều rộng và chiều cao (giảm 75% số điểm ảnh), giảm số phép tính của các tầng sau, tạo tính bất biến dịch chuyển nhẹ (translation invariance), và giữ lại tín hiệu kích hoạt mạnh nhất.",
        "section_ref": "§3.2",
        "trap": "Nghĩ rằng Pooling tăng số lượng kênh (Pooling giữ nguyên số kênh $C$)."
    },
    {
        "id": 25,
        "question": "Thuật toán 'YOLO' thuộc nhóm phát hiện đối tượng:",
        "options": [
            "A. Single-stage detector.",
            "B. Two-stage detector.",
            "C. Unsupervised detector.",
            "D. Phân đoạn cá thể (Instance Segmentation)."
        ],
        "correct": "A",
        "explanation": r"YOLO (You Only Look Once) thuộc nhóm Single-stage Detector. Mô hình chia ảnh thành lưới và dự đoán đồng thời tọa độ bounding box cùng xác suất nhãn lớp trong một lần lan truyền tiến (single forward pass) duy nhất, đạt tốc độ thời gian thực (Real-time). Dòng R-CNN (Faster R-CNN) thuộc nhóm Two-stage Detector.",
        "section_ref": "§3.6",
        "trap": "Nhầm YOLO với Faster R-CNN (Two-stage detector có RPN)."
    },
    {
        "id": 26,
        "question": "Thuật toán NMS (Non-Maximum Suppression) dùng để:",
        "options": [
            "A. Loại bỏ các khung hình (bounding boxes) trùng lặp và chỉ giữ lại khung có xác suất cao nhất.",
            "B. Tăng số lượng dự đoán.",
            "C. Làm mượt ảnh.",
            "D. Tính toán hàm loss."
        ],
        "correct": "A",
        "explanation": r"Trong Object Detection, mạng thường tạo ra hàng chục box dự đoán chồng chéo lên cùng một đối tượng. NMS sắp xếp các box theo điểm tin cậy giảm dần, chọn box cao nhất, sau đó tính IoU với các box lân cận; nếu $\text{IoU} > \text{threshold}$ (thường $0.45 - 0.5$) thì loại bỏ các box trùng lặp đó.",
        "section_ref": "§3.6",
        "trap": "Nhầm NMS là thuật toán làm mượt ảnh hoặc hàm tối ưu."
    },
    {
        "id": 27,
        "question": "'Model Quantization' (Lượng hóa mô hình) giúp:",
        "options": [
            "A. Giảm dung lượng mô hình và tăng tốc độ suy luận (inference) trên thiết bị nhúng.",
            "B. Tăng độ chính xác của mô hình.",
            "C. Thêm nhiều nơ-ron hơn.",
            "D. Chuyển mô hình từ Python sang Java."
        ],
        "correct": "A",
        "explanation": r"Quantization chuyển đổi biểu diễn số học của trọng số và kích hoạt từ dấu phẩy động độ chính xác cao (FP32 hoặc FP16) sang định dạng bit thấp hơn (INT8, INT4, NF4). Điều này giúp giảm 50%–75% dung lượng RAM/VRAM, giảm băng thông bộ nhớ và tăng tốc độ suy luận lên đáng kể trên chip di động/edge.",
        "section_ref": "§2.7 & §7.3",
        "trap": "Nghĩ rằng lượng hóa làm tăng độ chính xác (thực tế lượng hóa có thể làm giảm nhẹ độ chính xác)."
    },
    {
        "id": 28,
        "question": "Khái niệm 'Data Drift' (Trôi dạt dữ liệu) nghĩa là:",
        "options": [
            "A. Sự thay đổi phân phối của dữ liệu thực tế theo thời gian khiến mô hình cũ không còn hiệu quả.",
            "B. Dữ liệu bị xóa mất.",
            "C. Dữ liệu bị sao chép.",
            "D. Tốc độ truyền dữ liệu chậm."
        ],
        "correct": "A",
        "explanation": r"Data Drift (Covariate Shift) xảy ra khi phân phối dữ liệu đầu vào trong môi trường thực tế thay đổi theo thời gian so với phân phối tập huấn luyện: $P_{production}(X) \neq P_{training}(X)$, ví dụ hành vi người dùng thay đổi theo mùa hoặc cảm biến bị lão hóa, dẫn đến hiệu năng của mô hình bị thoái hóa.",
        "section_ref": "§5.6 & §7.4",
        "trap": "Nhầm Data Drift với lỗi mất mát dữ liệu phần cứng."
    },
    {
        "id": 29,
        "question": "'MLOps' là viết tắt của:",
        "options": [
            "A. Machine Learning Operations.",
            "B. Multi-Layer Optimization.",
            "C. Mobile Learning Options.",
            "D. Main Logic Operator."
        ],
        "correct": "A",
        "explanation": r"MLOps (Machine Learning Operations) là sự giao thoa giữa Machine Learning, DevOps và Data Engineering nhằm chuẩn hóa toàn bộ vòng đời phát triển: CI/CD/CT (Continuous Training), tự động hóa triển khai, quản lý phiên bản dữ liệu/mô hình (DVC, MLflow) và giám sát drift trong production.",
        "section_ref": "§7",
        "trap": "Các lựa chọn viết tắt giả tạo như Multi-Layer Optimization."
    },
    {
        "id": 30,
        "question": "Để phục vụ (serving) một mô hình LLM lớn, kỹ thuật nào thường được dùng để tiết kiệm VRAM?",
        "options": [
            "A. Paging.",
            "B. KV Caching.",
            "C. Unzipping.",
            "D. Overclocking."
        ],
        "correct": "B",
        "explanation": r"Trong quá trình sinh văn bản tự hồi quy (Autoregressive), mỗi token mới sinh ra cần truy vấn lại toàn bộ ngữ cảnh trước đó. KV Caching lưu lại các tensor Key và Value của các token trước trên VRAM để tránh việc phải tính toán lại từ đầu. Kỹ thuật PagedAttention (vLLM) tổ chức KV Cache thành các trang bộ nhớ liên kết ảo để chống phân mảnh và tiết kiệm tối đa VRAM.",
        "section_ref": "§2.7 & §4.5",
        "trap": "Nhầm với các thuật ngữ ép xung phần cứng (Overclocking) hoặc giải nén."
    },
    {
        "id": 31,
        "question": "Học bán giám sát (Semi-supervised learning) thường được áp dụng hiệu quả nhất trong kịch bản nào?",
        "options": [
            "A. Toàn bộ dữ liệu đều đã được gán nhãn rất chuẩn xác.",
            "B. Không có bất kỳ dữ liệu nào được gán nhãn.",
            "C. Có một lượng nhỏ dữ liệu được gán nhãn và một lượng lớn dữ liệu chưa gán nhãn.",
            "D. Số lượng nhãn cần phân loại thay đổi liên tục theo thời gian."
        ],
        "correct": "C",
        "explanation": r"Trong thực tế, việc thu thập dữ liệu thô thường rất rẻ nhưng việc gán nhãn thủ công (bởi chuyên gia y tế, kỹ sư) lại cực kỳ đắt đỏ. Semi-supervised learning sử dụng tập nhỏ mẫu có nhãn để huấn luyện mô hình ban đầu, sau đó kết hợp cấu trúc phân phối của tập lớn dữ liệu không nhãn (qua Pseudo-labeling, Consistency Regularization) để cải thiện độ khái quát hóa.",
        "section_ref": "§1.1",
        "trap": "Nhầm với Unsupervised (hoàn toàn không có nhãn) hoặc Supervised (100% có nhãn)."
    },
    {
        "id": 32,
        "question": "Điểm vượt trội của thuật toán t-SNE so với PCA khi giảm chiều dữ liệu trực quan hóa là gì?",
        "options": [
            "A. t-SNE có tốc độ tính toán nhanh hơn rất nhiều trên tập dữ liệu lớn.",
            "B. t-SNE bảo toàn tốt hơn cấu trúc phi tuyến và khoảng cách cục bộ (local structure).",
            "C. t-SNE luôn giữ lại 100% phương sai của dữ liệu gốc.",
            "D. t-SNE sử dụng phép chiếu tuyến tính đơn giản nên dễ suy luận ngược."
        ],
        "correct": "B",
        "explanation": r"PCA là phép chiếu tuyến tính toàn cục, thường làm các cụm dữ liệu phi tuyến phức tạp đè bẹp lên nhau khi chiếu xuống 2D. t-SNE chuyển đổi khoảng cách Euclid giữa các điểm thành xác suất có điều kiện và sử dụng phân phối Student-t ở không gian thấp chiều, giúp bảo tồn xuất sắc các mối quan hệ láng giềng phi tuyến cục bộ (local manifold).",
        "section_ref": "§1.8",
        "trap": r"Nghĩ rằng t-SNE chạy nhanh hơn PCA (thực tế t-SNE chậm hơn PCA rất nhiều, độ phức tạp $\mathcal{O}(N^2)$)."
    },
    {
        "id": 33,
        "question": "Tại sao Stratified K-Fold lại được ưu tiên sử dụng hơn K-Fold thông thường trong các bài toán phân loại có dữ liệu mất cân bằng?",
        "options": [
            "A. Nó đảm bảo tỷ lệ giữa các lớp trong mỗi Fold giống với tỷ lệ trong toàn bộ tập dữ liệu.",
            "B. Nó giúp mô hình chạy nhanh hơn bằng cách giảm bớt số lượng mẫu.",
            "C. Nó tự động loại bỏ các dữ liệu ngoại lệ (outliers) gây nhiễu.",
            "D. Nó không cho phép các Fold có dữ liệu trùng lặp với nhau."
        ],
        "correct": "A",
        "explanation": r"Nếu một bài toán có lớp hiếm chỉ chiếm 1%, K-Fold ngẫu nhiên có thể tạo ra các fold hoàn toàn không có mẫu dương nào trong tập validation. Stratified K-Fold phân tầng dữ liệu sao cho tỷ lệ giữa các lớp trong mỗi fold con đại diện chính xác tỷ lệ phân bố của toàn bộ tập dữ liệu ban đầu, giúp đánh giá metric (F1, AUC) ổn định và khách quan.",
        "section_ref": "§1.5 & §1.9",
        "trap": "Nghĩ rằng Stratified K-Fold làm giảm số lượng mẫu hoặc loại bỏ outlier."
    },
    {
        "id": 34,
        "question": "Hiện tượng 'Data Leakage' (Rò rỉ dữ liệu) trong quá trình xử lý đặc trưng (Feature Engineering) thường xảy ra khi:",
        "options": [
            "A. Chúng ta chuẩn hóa dữ liệu (Scaling) trên toàn bộ dataset trước khi chia tập Train/Test.",
            "B. Tập dữ liệu Train có số lượng mẫu quá nhỏ so với tập Test.",
            "C. Dùng kỹ thuật K-Fold cross-validation để đánh giá mô hình.",
            "D. Mô hình có độ phức tạp quá thấp dẫn đến underfitting."
        ],
        "correct": "A",
        "explanation": r"Nếu gọi `scaler.fit_transform(full_data)` trước khi chia `train_test_split`, các thông tin thống kê của tập test (như mean $\mu$ và standard deviation $\sigma$) đã bị rò rỉ vào quá trình học của tập train. Khi đó kết quả kiểm thử trên test set sẽ bị lạc quan giả tạo. Quy trình chuẩn: Luôn chia tập trước, chỉ `fit` trên Train, sau đó áp dụng `transform` trên Test.",
        "section_ref": "§1.5 & §5.6",
        "trap": "Nhầm Data Leakage là một dạng Underfitting do mô hình đơn giản."
    },
    {
        "id": 35,
        "question": "Kỹ thuật SMOTE (Synthetic Minority Over-sampling Technique) giải quyết vấn đề Class Imbalance bằng cách:",
        "options": [
            "A. Loại bỏ ngẫu nhiên các mẫu thuộc lớp đa số (majority class).",
            "B. Tạo ra các mẫu tổng hợp mới cho lớp thiểu số dựa trên khoảng cách K-NN.",
            "C. Gán trọng số cao hơn cho các mẫu thuộc lớp đa số trong hàm loss.",
            "D. Nhân bản lặp đi lặp lại các mẫu có sẵn của lớp thiểu số."
        ],
        "correct": "B",
        "explanation": r"Khác với Random Over-sampling (nhân bản trùng lặp các điểm có sẵn dễ dẫn tới overfit), SMOTE chọn một điểm mẫu lớp thiểu số $x_i$, tìm $k$ láng giềng gần nhất cùng lớp của nó, chọn ngẫu nhiên một láng giềng $x_{zi}$, và sinh điểm mới bằng nội suy tuyến tính: $x_{new} = x_i + \lambda (x_{zi} - x_i)$ với $\lambda \in [0, 1]$.",
        "section_ref": "§1.9",
        "trap": "Chọn D (nhân bản lặp lại là Random Over-sampling, không phải SMOTE)."
    },
    {
        "id": 36,
        "question": "Khi đánh giá một mô hình phân loại trên tập dữ liệu cực kỳ mất cân bằng (như phát hiện gian lận thẻ tín dụng), độ đo nào sau đây thường bị coi là 'vô dụng' và gây hiểu lầm nhất?",
        "options": [
            "A. F1-score.",
            "B. Precision-Recall AUC.",
            "C. Accuracy (Độ chính xác tổng thể).",
            "D. Recall."
        ],
        "correct": "C",
        "explanation": r"Giả sử trong 10,000 giao dịch chỉ có 10 vụ gian lận (tỷ lệ 0.1%). Một mô hình hoàn toàn không học gì, luôn dự đoán mọi giao dịch là 'hợp lệ' (negative) thì Accuracy vẫn đạt $9990/10000 = 99.9\%$. Tuy nhiên mô hình này hoàn toàn vô dụng vì phát hiện được $0\%$ vụ gian lận. Do đó trên dữ liệu lệch, Accuracy là độ đo gây ngộ nhận nghiêm trọng nhất.",
        "section_ref": "§1.7 & §1.9",
        "trap": "Thói quen luôn dùng Accuracy cho mọi bài toán phân loại."
    },
    {
        "id": 37,
        "question": "Điểm khác biệt cơ bản về mặt hiệu ứng giữa Regularization L1 (Lasso) và L2 (Ridge) là gì?",
        "options": [
            "A. L1 có xu hướng triệt tiêu các trọng số về 0 (tạo tính thưa thớt), trong khi L2 chỉ thu nhỏ chúng.",
            "B. L2 triệt tiêu hoàn toàn các trọng số về 0, L1 thì không.",
            "C. L1 chạy nhanh hơn L2 trên mọi kiến trúc phần cứng.",
            "D. L1 chỉ dùng cho hồi quy tuyến tính, L2 dùng cho mạng nơ-ron."
        ],
        "correct": "A",
        "explanation": r"Do hình học của quả cầu chuẩn L1 có các góc nhọn nằm ngay trên các trục tọa độ (hình thoi trong 2D), các đường đồng mức của hàm loss thường tiếp xúc với biên ràng buộc L1 tại chính các đỉnh trục tọa độ $\implies$ một số trọng số bị ép chính xác về 0 (tạo tính thưa thớt - Sparsity, đóng vai trò chọn lọc đặc trưng Feature Selection). Chuẩn L2 (hình cầu trơn) chỉ kéo các trọng số co nhỏ dần về gần 0 nhưng không bao giờ bằng 0 tuyệt đối.",
        "section_ref": "§1.6",
        "trap": "Đảo ngược vai trò: nghĩ rằng L2 triệt tiêu về 0 còn L1 chỉ thu nhỏ."
    },
    {
        "id": 38,
        "question": "Trong cây quyết định (Decision Tree), việc thiết lập tham số max_depth quá lớn mà không có cơ chế cắt tỉa sẽ dẫn đến:",
        "options": [
            "A. Mô hình bị Underfitting nặng.",
            "B. Mô hình bị Overfitting do cây quá sâu và học cả nhiễu.",
            "C. Thời gian suy luận (Inference) giảm đi đáng kể.",
            "D. Độ chệch (Bias) của mô hình tăng cao."
        ],
        "correct": "B",
        "explanation": r"Độ sâu của cây quyết định kiểm soát độ phức tạp của mô hình. Khi `max_depth` quá lớn, cây sẽ tiếp tục phân nhánh đến tận từng mẫu riêng lẻ, tạo ra các lát cắt siêu nhỏ ghi nhớ cả ngoại lai và nhiễu ngẫu nhiên của tập train, khiến Training Error = 0 nhưng Test Error bùng nổ $\implies$ Overfitting (High Variance).",
        "section_ref": "§1.3",
        "trap": "Nhầm Overfitting với Underfitting."
    },
    {
        "id": 39,
        "question": "Trong phân tích dữ liệu khám phá (EDA), biểu đồ Boxplot (biểu đồ hộp) là công cụ cực kỳ hữu hiệu để nhanh chóng phát hiện:",
        "options": [
            "A. Các giá trị ngoại lệ (Outliers) và phân phối tứ phân vị của dữ liệu.",
            "B. Mối quan hệ tuyến tính giữa hai biến liên tục.",
            "C. Tần suất xuất hiện của các từ trong văn bản.",
            "D. Ma trận tương quan giữa tất cả các đặc trưng."
        ],
        "correct": "A",
        "explanation": r"Boxplot trực quan hóa 'Tóm tắt 5 số' của phân phối: Minimum, Tứ phân vị thứ nhất ($Q_1$), Trung vị ($Q_2$), Tứ phân vị thứ ba ($Q_3$) và Maximum. Khoảng trải giữa $IQR = Q_3 - Q_1$. Các điểm nằm ngoài khoảng râu $[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$ được biểu diễn bằng các chấm riêng biệt, giúp nhận diện Outliers ngay lập tức.",
        "section_ref": "§5.3 & §7",
        "trap": "Nhầm Boxplot với Scatter plot (dùng xem quan hệ tuyến tính giữa 2 biến)."
    },
    {
        "id": 40,
        "question": "Kỹ thuật Early Stopping dừng quá trình huấn luyện mạng nơ-ron dựa trên tín hiệu nào?",
        "options": [
            "A. Khi Train loss đạt giá trị bằng 0 tuyệt đối.",
            "B. Khi Validation loss không còn giảm hoặc bắt đầu tăng liên tục trong một số epoch.",
            "C. Khi số lượng epoch đạt đúng giới hạn do người dùng đặt ra từ đầu.",
            "D. Khi tốc độ tính toán của GPU bị sụt giảm."
        ],
        "correct": "B",
        "explanation": r"Khi mạng nơ-ron bắt đầu học vẹt (overfit), Train loss vẫn tiếp tục giảm nhưng Validation loss sẽ chạm đáy rồi bắt đầu tăng lên. Early Stopping theo dõi loss trên tập validation qua tham số `patience`; nếu sau số epoch này mà validation loss không cải thiện, quá trình train bị dừng lại và mô hình khôi phục bộ trọng số có validation loss thấp nhất.",
        "section_ref": "§2.3",
        "trap": "Chờ Train loss về 0 (đó là dấu hiệu của Overfitting cực nặng)."
    },
    {
        "id": 41,
        "question": "Điểm khác biệt cốt lõi giữa phương pháp Bagging (như Random Forest) và Boosting (như XGBoost) là:",
        "options": [
            "A. Bagging xây dựng các cây độc lập song song; Boosting xây dựng các cây tuần tự nối tiếp nhau.",
            "B. Bagging luôn cho độ chính xác cao hơn Boosting trên mọi tập dữ liệu.",
            "C. Boosting cố gắng giảm phương sai (Variance), Bagging cố gắng giảm độ chệch (Bias).",
            "D. Bagging chỉ dùng cho phân loại, Boosting chỉ dùng cho hồi quy."
        ],
        "correct": "A",
        "explanation": r"Bagging huấn luyện các cây độc lập song song trên các tập con bootstrap để giảm phương sai (Variance Reduction). Ngược lại, Boosting huấn luyện các cây tuần tự (Sequential): cây sau tập trung học để sửa sai số/phần dư (residuals) của các cây trước, nhằm giảm độ chệch (Bias Reduction).",
        "section_ref": "§1.4",
        "trap": "Đảo ngược mục tiêu: Bagging giảm Variance, Boosting giảm Bias."
    },
    {
        "id": 42,
        "question": "Thuật toán CatBoost nổi tiếng trong cộng đồng Kaggle nhờ khả năng xử lý tự động và tối ưu loại dữ liệu nào mà không cần qua bước One-Hot Encoding?",
        "options": [
            "A. Dữ liệu dạng chuỗi thời gian (Time-series).",
            "B. Dữ liệu dạng phân loại (Categorical features).",
            "C. Dữ liệu ảnh màu RGB.",
            "D. Dữ liệu dạng âm thanh."
        ],
        "correct": "B",
        "explanation": r"CatBoost (Categorical Boosting) do Yandex phát triển, nổi tiếng với khả năng tự động xử lý các đặc trưng phân loại (Categorical features) có số lượng giá trị phân biệt lớn (High-cardinality) bằng kỹ thuật Target Statistics theo thứ tự ngẫu nhiên (Ordered Target Encoding), giải quyết triệt để vấn đề bùng nổ chiều của One-Hot Encoding và chống Target Leakage.",
        "section_ref": "§1.4 & §7.4",
        "trap": "Nhầm CatBoost là chuyên về Time-series (chữ 'Cat' là viết tắt của Categorical)."
    },
    {
        "id": 43,
        "question": "Thuật toán LightGBM sử dụng chiến lược phát triển cây nào giúp nó thường chạy nhanh hơn và tốn ít bộ nhớ hơn so với XGBoost truyền thống?",
        "options": [
            "A. Leaf-wise growth (Phát triển theo chiều sâu của lá).",
            "B. Level-wise growth (Phát triển theo chiều ngang của tầng).",
            "C. Random growth (Phát triển ngẫu nhiên).",
            "D. Full-depth growth (Phát triển toàn bộ độ sâu cùng lúc)."
        ],
        "correct": "A",
        "explanation": r"Hầu hết các thuật toán GBDT truyền thống (như XGBoost ban đầu) dùng Level-wise (phát triển cây cân bằng theo từng tầng ngang). LightGBM sử dụng chiến lược Leaf-wise (Best-first): tại mỗi bước, nó chỉ tìm chiếc lá có độ giảm hàm tổn thất (loss reduction) lớn nhất để phân nhánh, kết hợp phân giỏ Histogram giúp tốc độ huấn luyện nhanh gấp nhiều lần và tiết kiệm RAM.",
        "section_ref": "§1.4",
        "trap": "Level-wise là của XGBoost truyền thống, Leaf-wise mới là của LightGBM."
    },
    {
        "id": 44,
        "question": "Phương pháp 'Stacking' trong Ensemble learning hoạt động theo cơ chế nào?",
        "options": [
            "A. Lấy trung bình cộng đơn giản kết quả dự báo của tất cả các mô hình cơ sở.",
            "B. Dùng đầu ra (dự báo) của các mô hình cơ sở làm đầu vào cho một mô hình meta-learner cấp cao hơn.",
            "C. Nhân kết quả dự báo của các mô hình với một trọng số cố định được gán từ trước.",
            "D. Loại bỏ các mô hình yếu và chỉ giữ lại mô hình mạnh nhất."
        ],
        "correct": "B",
        "explanation": r"Stacking (Stacked Generalization) huấn luyện nhiều mô hình cơ sở khác loại (Base learners: SVM, Random Forest, LightGBM...). Sau đó, các dự đoán Out-of-fold (OOF) của các mô hình này được ghép lại thành một ma trận đặc trưng mới để huấn luyện một mô hình cấp hai (Meta-learner, ví dụ Logistic Regression) nhằm học cách kết hợp tối ưu nhất.",
        "section_ref": "§1.4",
        "trap": "Nhầm Stacking với Voting/Averaging (lấy trung bình cộng đơn giản)."
    },
    {
        "id": 45,
        "question": "Khi xây dựng một cây quyết định đơn lẻ trong thuật toán Random Forest, tại mỗi nút chia, thuật toán sẽ:",
        "options": [
            "A. Duyệt qua toàn bộ tất cả các đặc trưng hiện có để tìm điểm chia tốt nhất.",
            "B. Chỉ chọn ngẫu nhiên một tập con các đặc trưng để tìm điểm chia tốt nhất.",
            "C. Luôn chọn đặc trưng có giá trị trung bình lớn nhất.",
            "D. Không sử dụng bất kỳ tiêu chí ngẫu nhiên nào."
        ],
        "correct": "B",
        "explanation": r"Để triệt tiêu tương quan giữa các cây (Decorrelation of trees), tại mỗi nút chia, Random Forest chỉ lấy ngẫu nhiên một tập con đặc trưng (kích thước $m \approx \sqrt{p}$ cho phân loại, $m \approx p/3$ cho hồi quy) trong tổng số $p$ đặc trưng để tìm điểm chia tối ưu. Nếu duyệt toàn bộ đặc trưng thì các cây sẽ có nhánh đầu giống hệt nhau (do đặc trưng mạnh nhất áp đảo), làm mất lợi thế giảm phương sai.",
        "section_ref": "§1.4",
        "trap": "Nghĩ rằng Random Forest duyệt qua toàn bộ $p$ đặc trưng tại mỗi nút."
    },
    {
        "id": 46,
        "question": "(Khó) Mô hình FT-Transformer (Feature Tokenizer + Transformer) dành cho dữ liệu bảng (Tabular data) áp dụng cơ chế Self-Attention vào đâu?",
        "options": [
            "A. Giữa các hàng (các mẫu dữ liệu) khác nhau để tìm sự tương đồng.",
            "B. Giữa các đặc trưng (các cột) khác nhau sau khi đã được 'mã hóa' thành các token.",
            "C. Giữa các cây quyết định trong một rừng ngẫu nhiên.",
            "D. Nó không sử dụng Self-Attention mà dùng tích chập 1D."
        ],
        "correct": "B",
        "explanation": r"FT-Transformer (Gorishniy et al., NeurIPS 2021) biến đổi từng đặc trưng (cả cột số và cột phân loại) thành một vector nhúng (Feature Tokenizer). Sau đó, nó áp dụng chồng các khối Self-Attention giữa các vector đặc trưng này (Attention across features/columns trong cùng một mẫu), cho phép mô hình học các tương tác phi tuyến bậc cao giữa các thuộc tính.",
        "section_ref": "§4.5 & §7.4",
        "trap": "Nhầm lẫn giữa Attention theo hàng (Row/Sample attention) và Attention theo cột (Feature attention)."
    },
    {
        "id": 47,
        "question": "Mô hình Neural Tabular nào gần đây nổi tiếng với việc chia sẻ tham số hiệu quả để tạo ra một 'ensemble' gồm nhiều mạng nơ-ron nhỏ bên trong một kiến trúc duy nhất?",
        "options": [
            "A. TabM.",
            "B. TabNet.",
            "C. NODE (Neural Oblivious Decision Ensembles).",
            "D. SAINT."
        ],
        "correct": "A",
        "explanation": r"TabM (Tabular Model with Mini-Ensembles, Gorishniy et al., ICLR 2024) giới thiệu kiến trúc mạng nơ-ron cho dữ liệu bảng chia sẻ phần lớn các tầng biểu diễn chung nhưng phân nhánh thành nhiều 'mini-ensembles' nhẹ bên trong, mang lại độ chính xác ngang ngửa hoặc vượt trội GBDT (XGBoost/CatBoost) mà tốc độ suy luận nhanh hơn nhiều so với việc ensemble nhiều model độc lập.",
        "section_ref": "§1.4 & §7.4",
        "trap": "Nhầm TabM với TabNet (TabNet dùng Sequential Attention Masking)."
    },
    {
        "id": 48,
        "question": "Thuật toán Gradient Boosting xây dựng các cây quyết định dựa trên nguyên lý chủ đạo nào?",
        "options": [
            "A. Mỗi cây sau cố gắng học cách dự báo phần dư (residuals/errors) của các cây đứng trước nó.",
            "B. Các cây hoàn toàn độc lập và kết quả cuối cùng được bầu chọn theo số đông.",
            "C. Cây sau phải có độ sâu gấp đôi cây trước.",
            "D. Loại bỏ ngẫu nhiên 50% dữ liệu trước khi xây dựng cây mới."
        ],
        "correct": "A",
        "explanation": r"Gradient Boosting xem việc huấn luyện là giải bài toán Gradient Descent trong không gian hàm. Mỗi cây mới $h_m(x)$ được khớp vào phần dư âm (negative gradient) của hàm loss tại dự đoán của mô hình hiện tại: $r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F=F_{m-1}}$. Với hàm loss MSE, giá trị này chính là sai số phần dư $y_i - F_{m-1}(x_i)$.",
        "section_ref": "§1.4",
        "trap": "Nhầm cơ chế học phần dư của Boosting với cơ chế độc lập của Bagging."
    },
    {
        "id": 49,
        "question": "Trong CatBoost, kỹ thuật 'Ordered Boosting' được thiết kế đặc biệt nhằm giải quyết triệt để vấn đề gì thường gặp ở các thuật toán Boosting khác?",
        "options": [
            "A. Hiện tượng Target leakage và Overfitting trong quá trình tính toán gradient trên tập dữ liệu nhỏ.",
            "B. Thời gian huấn luyện quá lâu trên CPU.",
            "C. Không thể chạy được trên GPU.",
            "D. Mô hình quá đơn giản dẫn đến Underfitting."
        ],
        "correct": "A",
        "explanation": r"Trong GBDT truyền thống, gradient của mẫu thứ $i$ được ước lượng bằng mô hình đã được xây dựng từ tập dữ liệu có chứa chính mẫu thứ $i$ đó, gây ra độ lệch dự đoán (Prediction Shift / Target Leakage). Ordered Boosting xáo trộn ngẫu nhiên thứ tự tập dữ liệu và chỉ tính gradient cho mẫu thứ $i$ dựa trên mô hình học từ các mẫu đứng trước nó theo thứ tự hoán vị, triệt tiêu rò rỉ thông tin.",
        "section_ref": "§1.4",
        "trap": "Nghĩ rằng Ordered Boosting chỉ là một kỹ thuật tối ưu tốc độ CPU/GPU."
    },
    {
        "id": 50,
        "question": "Tại sao việc áp dụng K-Fold cross-validation thông thường trực tiếp lên dữ liệu chuỗi thời gian (Time-series) để tuning mô hình lại bị coi là sai lầm nghiêm trọng?",
        "options": [
            "A. Vì nó phá vỡ tính tuần tự thời gian và dẫn đến rò rỉ dữ liệu từ tương lai vào quá khứ.",
            "B. Vì dữ liệu chuỗi thời gian không thể chia thành các Fold.",
            "C. Vì nó làm tăng gấp đôi kích thước của tập dữ liệu.",
            "D. Vì các mô hình chuỗi thời gian không có siêu tham số để tune."
        ],
        "correct": "A",
        "explanation": r"Dữ liệu chuỗi thời gian có mối phụ thuộc thời gian (Temporal Dependence). K-Fold ngẫu nhiên sẽ xáo trộn các mốc thời gian, khiến mô hình lấy dữ liệu của ngày hôm sau để dự đoán cho ngày hôm trước (Look-ahead bias / Data leakage). Bắt buộc phải dùng phương pháp Time-Series Split (Rolling/Expanding Window) trong đó tập Train luôn diễn ra trước tập Validation.",
        "section_ref": "§1.5 & §5.6",
        "trap": "Áp dụng rập khuôn K-Fold ngẫu nhiên cho bài toán chuỗi thời gian."
    }
]
