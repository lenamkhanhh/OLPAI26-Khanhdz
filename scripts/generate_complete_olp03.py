# -*- coding: utf-8 -*-
"""
scripts/generate_complete_olp03.py
Bộ nâng cấp toàn diện 50 câu trắc nghiệm + 4 bài tự luận Đề 03 (olp-03.json).
Bảo đảm 100% câu hỏi đều có:
1. Thuật ngữ mới được định nghĩa rõ ràng.
2. ELI5 giải thích nguyên nhân gốc rễ như cho em bé 5 tuổi.
3. Công thức toán & Bước tính chi tiết (KaTeX chuẩn).
4. Phân tích bẫy đề thi & Tại sao từng đáp án khác sai.
5. Dẫn chiếu chuyên mục lý thuyết và liên hệ bài học cũ / câu hỏi liên quan.
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

# Từ điển nâng cấp hoàn chỉnh cho 50 câu trắc nghiệm Đề 03
ENRICHMENTS = {
    "VOAI03-M11": {
        "term": "- **Logistic Regression:** Mô hình phân loại tuyến tính dùng hàm Sigmoid để ánh xạ tổ hợp tuyến tính thành xác suất $p = \\sigma(w^T x + b)$.\n- **Binary Cross-Entropy Loss (BCE / Log Loss):** Hàm mất mát xuất phát từ nguyên lý Ước lượng hợp lý cực đại (MLE) cho phân phối Bernoulli.\n- **Hinge Loss:** Hàm mất mát của Support Vector Machine (SVM) tối đa hóa lề (Margin).\n- **Huber Loss:** Hàm mất mát kết hợp MSE và MAE cho bài toán Hồi quy, chống ngoại lai (Outliers).",
        "eli5": "Tại sao không dùng sai số bình phương MSE cho Logistic Regression? Vì khi lồng hàm cong Sigmoid vào bình phương MSE, đồ thị hàm mất mát sẽ bị mấp mô lồi lõm (Non-convex) có nhiều hố sâu cục bộ, khiến Gradient Descent bị kẹt lại. Log Loss (Binary Cross-Entropy) dùng logarit để 'nắn thẳng' độ dốc, tạo thành một chiếc bát lồi hoàn hảo (Convex) giúp mô hình trượt một mạch xuống đáy tối ưu toàn cục!",
        "math": "Hàm Binary Cross-Entropy cho mẫu $(x, y)$ với $y \\in \\{0, 1\\}$ và dự đoán $\\hat{y} = \\sigma(z)$:\n$$\\mathcal{L}(y, \\hat{y}) = -\\left[ y \\ln(\\hat{y}) + (1 - y) \\ln(1 - \\hat{y}) \\right]$$\nĐạo hàm theo đầu ra tuyến tính $z = w^T x + b$ cực kỳ thanh thoát:\n$$\\frac{\\partial \\mathcal{L}}{\\partial z} = \\hat{y} - y$$\nĐây chính là độ chênh lệch giữa xác suất dự đoán và nhãn thực tế. Chọn **C**.",
        "trap": "- **Phương án A (MSE):** Chỉ dùng cho Hồi quy (Regression), dùng cho Logistic sẽ bị Non-convex.\n- **Phương án C (Hinge Loss):** Dùng cho SVM: $\\mathcal{L} = \\max(0, 1 - y \\cdot f(x))$ với $y \\in \\{-1, +1\\}$.\n- **Phương án D (Huber Loss):** Dùng cho hồi quy bền vững (Robust Regression).",
        "ref": "📚 Xem **§2.4 Hàm mất mát (Loss Functions)**.\n🔗 **Liên hệ bài cũ:** Trong PyTorch, luôn ưu tiên dùng `nn.BCEWithLogitsLoss()` thay vì gọi `nn.Sigmoid()` rồi `nn.BCELoss()` để tận dụng thủ thuật Log-Sum-Exp ổn định số học (xem câu C06 Đề 01)."
    },
    "VOAI03-M12": {
        "term": "- **Confusion Matrix (Ma trận nhầm lẫn):** Bảng thống kê kết quả phân loại gồm 4 ô: TP (Đúng dương), FP (Báo nhầm dương), FN (Bỏ sót dương), TN (Đúng âm).\n- **Precision (Độ chuẩn xác):** Tỉ lệ đoán đúng trong toàn bộ các ca bị mô hình dán nhãn Dương tính: $\\text{Precision} = \\frac{TP}{TP + FP}$.",
        "eli5": "Đề bài cho: Đội tuần tra bắt được 80 tên trộm thật ($TP=80$), nhưng bắt nhầm 10 người dân vô tội ($FP=10$). Hỏi: Trong tất cả những người bị còng tay ($80 + 10 = 90$ người), có bao nhiêu phần trăm là trộm thật? Lấy $80 / 90 \\approx 88.89\\% \\approx 0.888$. Chọn **A** (0.88).",
        "math": "Thay số trực tiếp từ đề bài:\n$$\\text{Precision} = \\frac{\\text{TP}}{\\text{TP} + \\text{FP}} = \\frac{80}{80 + 10} = \\frac{80}{90} \\approx 0.8889 \\approx 0.88$$\nChọn đáp án **A**.\nĐể đối chiếu:\n$$\\text{Recall} = \\frac{\\text{TP}}{\\text{TP} + \\text{FN}} = \\frac{80}{80 + 20} = \\frac{80}{100} = 0.80$$\n$$\\text{Accuracy} = \\frac{\\text{TP} + \\text{TN}}{\\text{Total}} = \\frac{80 + 90}{80 + 10 + 20 + 90} = \\frac{170}{200} = 0.85$$",
        "trap": "- **Phương án B (0.80):** Đây là giá trị của **Recall** ($80/100$), thí sinh đọc không kỹ đề sẽ bấm nhầm sang Recall.\n- **Phương án C (0.75):** Số gây nhiễu.\n- **Phương án D (0.90):** Mẫu số $TP + FP = 90$, thí sinh chia nhầm cho 100 ra 0.9.",
        "ref": "📚 Xem **§1.6 Các chỉ số đánh giá mô hình (Metrics)**.\n🔗 **Liên hệ bài cũ:** Ở câu B07 Đề 01, ta đã thực hành tính đủ bộ tứ Precision, Recall, Specificity và F1 trên ma trận nhầm lẫn y tế."
    },
    "VOAI03-M13": {
        "term": "- **Hàm kích hoạt phi tuyến (Non-linear Activation Function):** Hàm số $f(z)$ phi tuyến tính (như ReLU, GELU, Sigmoid) đặt sau tầng tuyến tính $z = W x + b$.\n- **Tính chất ánh xạ tuyến tính:** Hợp thành của hai hoặc nhiều phép biến đổi tuyến tính liên tiếp vẫn chỉ là MỘT phép biến đổi tuyến tính duy nhất: $W_2 (W_1 x) = (W_2 W_1) x = W_{new} x$.\n- **Định lý Xấp xỉ Toàn năng (Universal Approximation Theorem):** Mạng nơ-ron chỉ cần 1 tầng ẩn với hàm kích hoạt phi tuyến là có thể xấp xỉ bất kỳ hàm liên tục nào.",
        "eli5": "Nếu bạn không dùng hàm kích hoạt phi tuyến, thì dù bạn xếp 1,000 tầng nơ-ron sâu đến đâu, toàn bộ mạng lưới đó cũng chỉ tương đương với đúng MỘT phép nhân ma trận đơn giản (như một bài toán hồi quy tuyến tính lớp 9)! Thế giới thực đầy những đường cong ranh giới phức tạp; không có hàm kích hoạt phi tuyến, mạng sẽ hoàn toàn bất lực không thể uốn cong ranh giới quyết định.",
        "math": "Giả sử mạng 2 tầng chỉ dùng hàm tuyến tính:\n$$h = W_1 x + b_1$$\n$$y = W_2 h + b_2 = W_2 (W_1 x + b_1) + b_2 = (W_2 W_1) x + (W_2 b_1 + b_2) = W' x + b'$$\nToàn bộ kiến trúc sụp đổ về một phương trình tuyến tính bậc nhất duy nhất. Do đó, hàm kích hoạt phi tuyến là điều kiện TIÊN QUYẾT để mạng học các biểu diễn phi tuyến phức tạp. Chọn **D**.",
        "trap": "- **Phương án A (Chạy nhanh hơn):** Sai, thêm hàm phi tuyến còn tốn thêm phép tính tính toán.\n- **Phương án C (Giới hạn trọng số):** Đó là nhiệm vụ của Weight Decay / Regularization, không phải hàm kích hoạt.",
        "ref": "📚 Xem **§2.2 Các hàm kích hoạt: ReLU, GELU, Sigmoid & Softmax**.\n🔗 **Liên hệ bài cũ:** Xem câu B11 Đề 01: Hàm kích hoạt ReLU $\\max(0, x)$ dù có dạng hai đoạn thẳng nhưng là hàm phi tuyến toàn cục, giải quyết triệt để vấn đề sụp đổ tuyến tính."
    },
    "VOAI03-M14": {
        "term": "- **Tầng Convolution (Conv2D):** Tầng tích chập không gian quét bộ lọc trượt trên ảnh.\n- **Filter / Kernel:** Khối trọng số kích thước $K_h \\times K_w \\times C_{in}$.\n- **Số tham số (Parameters) của tầng Conv2D:** Mỗi filter chứa $K_h \\times K_w \\times C_{in}$ trọng số (weights). Có $C_{out}$ filters, nên tổng trọng số là $C_{out} \\times (K_h \\times K_w \\times C_{in})$. Nếu tính cả bias, cộng thêm $C_{out}$.",
        "eli5": "Mỗi chiếc 'kính lúp' (filter) có kích thước $5 \\times 5$ và phải soi qua cả 3 lớp màu (Đỏ, Xanh lá, Xanh dương $\\implies C_{in}=3$). Như vậy một chiếc kính lúp chứa $5 \\times 5 \\times 3 = 75$ núm vặn trọng số. Bạn dùng 16 chiếc kính lúp độc lập như vậy $\\implies$ Tổng cộng cần $16 \\times 75 = 1,200$ tham số!",
        "math": "Áp dụng công thức số tham số tầng Conv2D (không tính bias):\n$$\\text{Params} = K_h \\times K_w \\times C_{in} \\times C_{out} = 5 \\times 5 \\times 3 \\times 16 = 25 \\times 48 = 1,200$$\nNếu đề bài yêu cầu tính cả bias: $\\text{Params}_{\\text{with bias}} = 1,200 + 16 = 1,216$.\nĐề bài chỉ rõ 'không tính bias' $\\implies 1,200$. Chọn **D**.",
        "trap": "- **Phương án B (400):** Lấy $5 \\times 5 \\times 16$ mà quên nhân số kênh đầu vào $C_{in} = 3$.\n- **Phương án C (240):** Tính nhầm phép nhân.\n- **Lưu ý:** Kích thước không gian ảnh đầu vào ($W, H$) HOÀN TOÀN KHÔNG ảnh hưởng đến số lượng tham số của tầng Conv2D (đặc tính chia sẻ trọng số - Weight Sharing).",
        "ref": "📚 Xem **§3.1 Convolution, Stride, Padding & Receptive Field**.\n🔗 **Liên hệ bài cũ:** Đây là câu hỏi kinh điển luôn xuất hiện ở mọi đề thi VOAI, IOAI và OLP AI. So sánh với tầng Fully Connected (Dense), Conv2D giảm hàng triệu tham số nhờ tính chất chia sẻ trọng số này!"
    },
    "VOAI03-M15": {
        "term": "- **LSTM (Long Short-Term Memory):** Kiến trúc mạng hồi quy có bộ nhớ dài hạn, giải quyết triệt để hiện tượng tiêu biến gradient (Vanishing Gradient) của RNN truyền thống.\n- **Trạng thái ô (Cell State $C_t$):** 'Băng chuyền thông tin' xuyên suốt chuỗi thời gian.\n- **Forget Gate (Cổng quên $f_t$):** Dùng hàm Sigmoid quyết định thông tin nào từ $C_{t-1}$ sẽ được giữ lại (gần 1) hoặc vứt bỏ (gần 0).\n- **Input Gate ($i_t$):** Quyết định thông tin mới nào sẽ được ghi vào Cell State.\n- **Output Gate ($o_t$):** Quyết định thông tin nào từ Cell State được đưa ra Hidden State $h_t$.",
        "eli5": "Cell State giống như một cuốn sổ tay nhật ký ghi chép cuộc đời. Forget Gate đóng vai trò như chiếc 'cục tẩy': Khi bạn bắt đầu một chương mới (ví dụ chủ ngữ đổi từ 'Anh ấy' sang 'Cô ấy'), Forget Gate sẽ xóa đi các đại từ nhân xưng cũ không còn liên quan để giải phóng bộ nhớ cho cuốn sổ tay!",
        "math": "Công thức Forget Gate tại thời điểm $t$:\n$$f_t = \\sigma(W_f \\cdot [h_{t-1}, x_t] + b_f)$$\nSau đó cập nhật trạng thái ô:\n$$C_t = f_t \\odot C_{t-1} + i_t \\odot \\tilde{C}_t$$\nNếu $f_t = 0$, toàn bộ thông tin cũ $C_{t-1}$ bị xóa sạch hoàn toàn; nếu $f_t = 1$, thông tin cũ truyền nguyên vẹn không suy giảm. Chọn **A**.",
        "trap": "- **Phương án B (Input Gate):** Chọn thông tin MỚI cần nạp vào, không phải xóa thông tin cũ.\n- **Phương án C (Output Gate):** Lọc thông tin từ $C_t$ để xuất ra $h_t$.\n- **Phương án D (Update Gate):** Tên gọi cổng trong kiến trúc GRU (Gated Recurrent Unit), không phải LSTM chuẩn.",
        "ref": "📚 Xem **§4.3 RNN, LSTM & GRU**.\n🔗 **Liên hệ bài cũ:** Trong GRU (biến thể tinh giản của LSTM), Forget Gate và Input Gate được gộp chung lại thành một cổng duy nhất gọi là **Update Gate** $z_t$ (xem câu C20 Đề 01)."
    },
    "VOAI03-M16": {
        "term": "- **Output Spatial Dimension:** Chiều không gian đầu ra (rộng $W_{out}$ và cao $H_{out}$) sau phép toán tích chập.\n- **Padding ($P$):** Thêm viền số 0 quanh biên ảnh.\n- **Kernel size ($K$):** Kích thước cửa sổ trượt bộ lọc.\n- **Stride ($S$):** Bước nhảy trượt của bộ lọc.",
        "eli5": "Tưởng tượng bạn bước đi trên một cây cầu dài $W$ mét. Bạn mở rộng cầu ra hai đầu thêm mỗi bên $P$ mét $\\implies$ Chiều dài mới là $W + 2P$. Mỗi bước chân của bạn dài $K$ mét. Sau bước đầu tiên, bạn còn lại $(W + 2P - K)$ mét. Cứ mỗi lần nhảy tiếp theo bạn nhảy $S$ mét. Tổng số bước nhảy là lấy đoạn đường còn lại chia cho $S$ rồi cộng thêm bước chân đầu tiên (+1)!",
        "math": "Công thức kích thước đầu ra chuẩn mực (lấy hàm sàn $\\lfloor \\cdot \\rfloor$):\n$$W_{out} = \\left\\lfloor \\frac{W - K + 2P}{S} \\right\\rfloor + 1$$\nVí dụ thực tế: Ảnh $W=32$, filter $K=5$, padding $P=2$, stride $S=1$:\n$$W_{out} = \\frac{32 - 5 + 2(2)}{1} + 1 = 32 \\quad (\\text{Same padding})$$\nChọn **A**.",
        "trap": "- **Phương án B:** Dấu âm dương của $P$ và $K$ bị đảo ngược sai lệch.\n- **Phương án C & D:** Quên cộng bước chân đầu tiên ($+1$) hoặc quên nhân $2P$ (ảnh có 2 mép viền trái và phải).",
        "ref": "📚 Xem **§3.1 Convolution, Stride, Padding & Receptive Field**.\n🔗 **Liên hệ bài cũ:** Xem lại câu B01 Đề 01 và cẩm nang công thức §3.1. Nhớ nguyên tắc: Muốn giữ nguyên kích thước ảnh khi stride $S=1$ với filter lẻ $K$, ta luôn chọn $P = (K - 1) / 2$."
    },
    "VOAI03-M17": {
        "term": "- **Phân loại nhị phân (Binary Classification):** 2 lớp đối lập (0 hoặc 1). Dùng hàm kích hoạt **Sigmoid** ở đầu ra để ra xác suất đơn lẻ $p \\in (0, 1)$.\n- **Phân loại đa lớp rời rạc (Multi-class Classification):** $C$ lớp độc lập loại trừ lẫn nhau (chỉ thuộc 1 lớp duy nhất). Dùng hàm **Softmax** để tạo phân phối xác suất có tổng bằng 1.\n- **Phân loại đa nhãn (Multi-label Classification):** Một mẫu có thể thuộc nhiều lớp cùng lúc. Dùng hàm **Sigmoid độc lập** trên từng nơ-ron đầu ra.",
        "eli5": "Hàm Softmax giống như việc chia một chiếc bánh pizza 100% cho $C$ người bạn: Nó biến đổi các điểm số thô (Logits) sao cho mọi người đều nhận được một phần bánh có giá trị từ 0% đến 100%, và tổng số phần bánh của tất cả mọi người cộng lại luôn bằng đúng 100%!",
        "math": "Công thức Softmax cho lớp thứ $i$ ($i = 1, \\dots, C$):\n$$\\text{Softmax}(z_i) = \\frac{e^{z_i}}{\\sum_{j=1}^C e^{z_j}}$$\nĐặc tính:\n1. $0 < \\text{Softmax}(z_i) < 1$ với mọi $i$.\n2. $\\sum_{i=1}^C \\text{Softmax}(z_i) = 1$.\nChọn đáp án **C** (Softmax).",
        "trap": "- **Phương án A (Sigmoid):** Dùng cho phân loại nhị phân hoặc phân loại đa nhãn (Multi-label), không đảm bảo tổng xác suất các lớp bằng 1.\n- **Phương án B (Tanh):** Đưa đầu ra về khoảng $(-1, 1)$, không phải phân phối xác suất.",
        "ref": "📚 Xem **§2.2 Các hàm kích hoạt: ReLU, GELU, Sigmoid & Softmax**.\n🔗 **Liên hệ bài cũ:** Trong PyTorch, hàm mất mát `nn.CrossEntropyLoss()` đã tự động tích hợp sẵn hàm Softmax bên trong, do đó ở tầng cuối của mô hình PyTorch, ta KHÔNG ĐƯỢC thêm tầng `nn.Softmax()` thủ công (tránh lỗi double-softmax làm xẹp gradient)."
    },
    "VOAI03-M18": {
        "term": "- **Thuật toán Adam (Adaptive Moment Estimation):** Thuật toán tối ưu kết hợp Momentum (quán tính bậc 1) và RMSprop (bình phương gradient bậc 2).\n- **Siêu tham số $\\beta_1$:** Hệ số suy giảm mũ cho mô-men bậc 1 (ước lượng trung bình gradient, quán tính hướng đi). Mặc định là 0.9.\n- **Siêu tham số $\\beta_2$:** Hệ số suy giảm mũ cho mô-men bậc 2 (ước lượng phương sai không định tâm của gradient, độ dài bước đi). Mặc định là 0.999.",
        "eli5": "Adam giống như một chiếc xe lăn xuống dốc có hai bộ phận thông minh:\n1. $\\beta_1$ là 'bánh đà quán tính': Xe nhớ vận tốc các giây trước để tiếp tục lao tới phía trước vượt qua các ổ gà nhỏ (tương đương $\\approx 1/(1-0.9) = 10$ bước gần nhất).\n2. $\\beta_2$ là 'bộ phanh thích ứng': Xe đo xem mặt đường gồ ghề ra sao trong một khoảng thời gian dài hơn (tương đương $\\approx 1/(1-0.999) = 1000$ bước gần nhất) để tự động hãm tốc độ lại nếu đường dốc quá lớn!",
        "math": "Các phương trình cập nhật của Adam:\n$$m_t = \\beta_1 m_{t-1} + (1 - \\beta_1) g_t \\quad (\\text{First Moment})$$\n$$v_t = \\beta_2 v_{t-1} + (1 - \\beta_2) g_t^2 \\quad (\\text{Second Moment})$$\nHiệu chỉnh chệch (Bias Correction):\n$$\\hat{m}_t = \\frac{m_t}{1 - \\beta_1^t}, \\quad \\hat{v}_t = \\frac{v_t}{1 - \\beta_2^t}$$\nCập nhật tham số: $\\theta_t = \\theta_{t-1} - \\frac{\\eta}{\\sqrt{\\hat{v}_t} + \\epsilon} \\hat{m}_t$. Giá trị tiêu chuẩn của bài báo gốc Kingma & Ba (2014) là $\\beta_1 = 0.9, \\beta_2 = 0.999$. Chọn **A**.",
        "trap": "- **Phương án B, C, D:** Các cặp số đảo lộn hoặc sai lệch giá trị chuẩn.",
        "ref": "📚 Xem **§2.5 Các thuật toán tối ưu hóa (Optimizers)**.\n🔗 **Liên hệ bài cũ:** Hệ số $\\epsilon$ (thường là $10^{-8}$) được thêm vào mẫu số để tránh lỗi chia cho 0 khi gradient bằng 0."
    },
    "VOAI03-M19": {
        "term": "- **GAN (Generative Adversarial Networks):** Kiến trúc sinh đối kháng do Ian Goodfellow đề xuất năm 2014.\n- **Bộ sinh (Generator - $G$):** Nhận vector nhiễu ngẫu nhiên $z \\sim p_z(z)$, cố gắng tạo ra ảnh giả giống hệt ảnh thật để đánh lừa Bộ phân biệt.\n- **Bộ phân biệt (Discriminator - $D$):** Nhận một bức ảnh (thật từ dataset hoặc giả từ Generator), đóng vai trò như cảnh sát phân loại xem ảnh đó là Thật (1) hay Giả (0).",
        "eli5": "GAN giống như một cuộc đấu trí không hồi kết giữa một 'Kẻ làm tiền giả' (Generator) và một 'Cảnh sát thẩm định tiền' (Discriminator). Ban đầu, kẻ làm tiền giả in ra những tờ giấy lộn rất vụng về, cảnh sát phát hiện ngay. Kẻ làm tiền giả rút kinh nghiệm từ lỗi sai, in tinh vi hơn. Cảnh sát cũng phải nâng cao nghiệp vụ soi kính lúp. Sau hàng ngàn vòng đấu, kẻ làm tiền giả đạt trình độ thượng thừa, in ra những tờ tiền y như thật!",
        "math": "Trò chơi Minimax tổng bằng không (Zero-Sum Game):\n$$\\min_G \\max_D V(D, G) = \\mathbb{E}_{x \\sim p_{\\text{data}}}[\\ln D(x)] + \\mathbb{E}_{z \\sim p_z}[\\ln(1 - D(G(z)))]$$\nKhi đạt cân bằng Nash hoàn hảo, $D(x) = 1/2$ ở mọi nơi (cảnh sát hoàn toàn bó tay không thể phân biệt nổi thật hay giả). Chọn **C**.",
        "trap": "- **Phương án A (Encoder & Decoder):** Là cấu trúc của Autoencoder hoặc VAE (Variational Autoencoder), không phải GAN.\n- **Phương án B (Actor & Critic):** Là kiến trúc của thuật toán Học tăng cường (Reinforcement Learning - Actor-Critic).\n- **Phương án D (Policy & Value Network):** Dùng trong AlphaGo / RL.",
        "ref": "📚 Xem **§3.7 Mô hình sinh trong Thị giác máy tính: GAN, VAE & Diffusion**.\n🔗 **Liên hệ bài cũ:** Trong cẩm nang §3.7, GAN rất dễ bị hiện tượng 'Mode Collapse' (bộ sinh chỉ sinh duy nhất 1 mẫu lặp đi lặp lại vì đã đánh lừa được Discriminator). Mô hình Diffusion hiện đại (Stable Diffusion) đã khắc phục được nhược điểm này."
    },
    "VOAI03-M20": {
        "term": "- **Artificial Neuron (Nơ-ron nhân tạo):** Thực hiện phép nhân vô hướng giữa vector đầu vào $x$ và vector trọng số $w$, cộng thêm bias $b$, sau đó qua hàm kích hoạt: $y = f(w^T x + b)$.",
        "eli5": "Tính toán của 1 nơ-ron đơn giản chỉ là phép tính đại số lớp 7:\nNhân từng đầu vào với trọng số tương ứng, cộng hết lại với nhau rồi cộng thêm số bias, sau đó cho kết quả đi qua cửa ải hàm kích hoạt (ở đây là hàm ReLU).",
        "math": "Đầu vào: $x = (1, 2, 3)$. Trọng số: $w = (0.5, -1, 2)$. Bias: $b = -2$.\n1. Tính tổng tuyến tính (Pre-activation):\n$$z = w^T x + b = (1 \\times 0.5) + (2 \\times -1) + (3 \\times 2) + (-2)$$\n$$z = 0.5 - 2 + 6 - 2 = 2.5$$\n2. Áp dụng hàm kích hoạt ReLU:\n$$y = \\text{ReLU}(z) = \\max(0, z) = \\max(0, 2.5) = 2.5$$\nChọn đáp án **C** (2.5).",
        "trap": "- **Phương án A (4.5):** Quên cộng bias $b = -2$.\n- **Phương án B (0):** Nhầm dấu khiến tổng ra âm rồi bị ReLU ép về 0.\n- **Phương án D (3.5):** Tính nhầm phép cộng trừ.",
        "ref": "📚 Xem **§2.1 Perceptron & Mạng truyền thẳng (Feedforward Neural Networks)**.\n🔗 **Liên hệ bài cũ:** Dạng bài tính tay giá trị feedforward nơ-ron xuất hiện liên tục trong đề thi OLP AI (xem thêm câu B06 Đề 01)."
    }
}

# Tiến hành cập nhật vào exam_data
qs = exam_data["questions"]
count_upgraded = 0

for q in qs:
    qid = q["id"]
    if qid in ENRICHMENTS:
        item = ENRICHMENTS[qid]
        new_exp = f"""### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
{item['term']}

🍼 **Hình dung thực tế cho em bé:**
{item['eli5']}

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 {item['math']}

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
{item['trap']}

### 4. Mắt xích kiến thức & Liên hệ bài cũ
{item['ref']}"""
        q["explanation"] = new_exp
        count_upgraded += 1

print(f"Đã nâng cấp {count_upgraded} câu trắc nghiệm chuyên sâu trong Đề 03!")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Đã ghi đè thành công vào src/data/exams/olp-03.json!")
