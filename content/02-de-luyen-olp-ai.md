# 02 — Đề luyện OLP AI HCMUS 2026 (KHÔNG có đáp án)

> Mỗi đề: 60 câu trắc nghiệm/code (thang 100) + 4 tự luận (chấm riêng thang 10/câu theo rubric).
> Đáp án xem file `03-dap-an-olp-ai.md`. Làm web thi thử: `npm run dev`.

---

# ĐỀ 01 — Ôn tập toàn diện

## Phần A — Toán & Xác suất – Thống kê (12 câu × 2đ)

**A01.** Một bệnh có tỉ lệ mắc 2%. Xét nghiệm có độ nhạy 95% và tỉ lệ dương tính giả 4%. Một người có kết quả dương tính. Xác suất người đó thật sự mắc bệnh là bao nhiêu?
A. 95% · B. Khoảng 32.6% · C. 2% · D. Khoảng 68%

**A02.** Xét nghiệm có độ nhạy 99% và đặc hiệu 99% cho bệnh hiếm (tỉ lệ 0.1%). Vì sao hầu hết người dương tính vẫn không mắc bệnh?
A. Do đặc hiệu của test thấp · B. Do độ nhạy của test thấp · C. Tỉ lệ mắc (base rate) trong dân số rất thấp · D. Test cho kết quả ngẫu nhiên

**A03.** Biến X ~ Bernoulli(p=0.3). Kỳ vọng và phương sai của X là?
A. E=0.3, Var=0.21 · B. E=0.5, Var=0.25 · C. E=0.3, Var=0.09 · D. E=0.7, Var=0.21

**A04.** Tung đồng xu cân đối 10 lần. Xác suất cả 10 lần đều sấp là?
A. 0.5 · B. Khoảng 0.25 · C. Khoảng 0.05 · D. Khoảng 0.001

**A05.** Tổng đài nhận trung bình 3 cuộc gọi/phút (mô hình Poisson). Xác suất trong 1 phút không có cuộc gọi nào là?
A. 0 · B. Khoảng 0.05 · C. Khoảng 0.5 · D. Khoảng 0.95

**A06.** Theo định lý giới hạn trung tâm (CLT), trung bình của mẫu có kích thước lớn sẽ có phân phối xấp xỉ gì?
A. Poisson · B. Bernoulli · C. Xấp xỉ phân phối chuẩn (Normal) · D. Phân phối đều

**A07.** Cho E[X]=5, Var(X)=4. Đặt Y=2X+3. Tính E[Y] và Var(Y).
A. E=13, Var=16 · B. E=13, Var=8 · C. E=10, Var=16 · D. E=13, Var=11

**A08.** Điểm khác biệt cốt lõi giữa MLE và MAP là gì?
A. MLE có prior, MAP không có prior · B. Hai phương pháp cho kết quả giống nhau mọi lúc · C. MAP chỉ dùng cho học không giám sát · D. MAP kết hợp dữ liệu với prior, MLE chỉ dùng dữ liệu

**A09.** Kiểm định với alpha=0.05 cho p-value=0.03. Kết luận đúng là gì?
A. Chấp nhận H0 vì p nhỏ · B. Bác bỏ H0 ở mức 5% · C. Xác suất H0 đúng là 3% · D. Hiệu ứng là rất lớn

**A10.** Số liệu cho thấy doanh số kem và số vụ chết đuối tương quan mạnh. Giải thích hợp lý nhất?
A. Có yếu tố nhiễu chung (mùa hè) gây ra cả hai · B. Ăn kem gây chết đuối · C. Số liệu sai, hai đại lượng độc lập · D. Cần thêm dữ liệu mới kết luận được bất cứ điều gì

**A11.** Dữ liệu có nhóm thiểu số chỉ 5%. Cách lấy mẫu đánh giá đúng đắn nhất?
A. Lấy mẫu chỉ từ nhóm đa số · B. Lấy mẫu ngẫu nhiên đơn giản luôn tốt hơn · C. Lấy mẫu phân tầng (stratified) giữ tỉ lệ các nhóm · D. Tăng kích thước test gấp đôi

**A12.** Gieo 2 xúc xắc cân đối. Xác suất tổng bằng 9 là?
A. 1/6 · B. 5/36 · C. 1/12 · D. 1/9

## Phần B — Python / NumPy / Tính tay (16 trắc nghiệm × 2đ + 2 code × 7đ)

**B01.** Ảnh 32x32 qua Conv2D kernel 3, stride 1, padding 1. Kích thước output?
A. 32x32 · B. 30x30 · C. 16x16 · D. 34x34

**B02.** Ảnh 28x28 qua Conv2D kernel 5, stride 1, không padding (valid). Kích thước output?
A. 28x28 · B. 24x24 · C. 14x14 · D. 23x23

**B03.** Ảnh 224x224 qua Conv2D kernel 7, stride 2, padding 3. Kích thước output?
A. 224x224 · B. 111x111 · C. 112x112 · D. 56x56

**B04.** Node cây quyết định có 4 mẫu đỏ, 4 mẫu xanh. Entropy của node là?
A. 0 bit · B. 0.5 bit · C. 2 bit · D. 1 bit

**B05.** Node cha [6 đỏ, 6 xanh], split tạo 2 node con sạch [6 đỏ, 0 xanh] và [0 đỏ, 6 xanh]. Information Gain là?
A. 1 · B. 0.5 · C. 0 · D. 2

**B06.** Box dự đoán và box thật có diện tích giao 30, hợp 120. IoU là bao nhiêu (ngưỡng 0.5)?
A. 0.5 · B. 0.25 · C. 0.2 · D. 4.0

**B07.** Mô hình chẩn đoán: TP=80, FP=20, FN=40. Precision và Recall là?
A. P=0.667, R=0.8 · B. P=0.8, R=0.8 · C. P=0.8, R~0.667 · D. P=0.5, R=0.667

**B08.** Precision=0.8, Recall=0.4. F1-score là?
A. 0.6 · B. 0.8 · C. 0.4 · D. Khoảng 0.533

**B09.** Cosine similarity giữa A=(1,0) và B=(1,1) là?
A. Khoảng 0.707 · B. 0 · C. 1 · D. 0.5

**B10.** Thứ tự đúng của một block có BatchNorm là gì?
A. ReLU -> BatchNorm -> Linear · B. Linear -> BatchNorm -> ReLU · C. Linear -> ReLU -> BatchNorm · D. BatchNorm -> Linear -> ReLU

**B11.** CrossEntropyLoss trong PyTorch nhận đầu vào dạng nào?
A. Xác suất sau Softmax · B. One-hot vector · C. Logit thô (chưa qua Softmax) · D. Nhãn đã Softmax + log

**B12.** Model nhị phân xuất logit (chưa Sigmoid). Cách dùng loss đúng và ổn định nhất?
A. Dùng BCE vì input là logit · B. Dùng MSE cho phân lớp nhị phân · C. Thêm Sigmoid rồi dùng BCEWithLogitsLoss · D. Dùng BCEWithLogitsLoss trực tiếp trên logit

**B13.** Thứ tự đúng trong vòng lặp train PyTorch là gì?
A. zero_grad -> backward -> step · B. backward -> zero_grad -> step · C. step -> backward -> zero_grad · D. backward -> step (không cần zero_grad)

**B14.** Mạng dùng ReLU ở hidden nên khởi tạo trọng số bằng phương pháp nào?
A. Zeros · B. He (Kaiming) · C. Hằng số 1 · D. Xavier là lựa chọn tốt nhất cho mọi activation

**B15.** Trong NumPy, a = np.zeros((3, 4)). Hình dạng của a.T là?
A. (3, 4) · B. (7,) · C. (4, 3) · D. (3, 3)

**B16.** Trong NumPy, np.zeros((4,1)) + np.zeros((4,)) cho kết quả hình dạng gì?
A. Báo lỗi không tương thích · B. (4, 1) · C. (4,) · D. (4, 4)

**BC1 (code, 7đ).** Viết hàm NumPy/sklearn tính precision, recall, F1 từ hai mảng y_true, y_pred (nhị phân 0/1). Giải thích tại sao không chỉ báo cáo accuracy khi dữ liệu lệch lớp.

**BC2 (code, 7đ).** Viết vòng lặp train PyTorch đúng cho 1 epoch (model, loader, criterion, optimizer có sẵn). Giải thích vai trò của zero_grad, backward, step.

## Phần C — ML / DL / CV / NLP (30 câu × 1đ)

**C01.** Vì sao k-NN được gọi là lazy learner?
A. k-NN trì hoãn mọi tính toán đến lúc dự đoán · B. k-NN học trọng số w bằng gradient descent · C. k-NN cần chiếu dữ liệu qua kernel · D. k-NN luôn chọn k bằng cross-validation

**C02.** Dữ liệu nhiều nhiễu, nên chọn k cho k-NN như thế nào?
A. k=1 luôn tốt nhất vì nhớ hết dữ liệu · B. k quá nhỏ dễ overfit, k quá lớn dễ underfit · C. k càng lớn càng overfit · D. k không ảnh hưởng, chỉ khoảng cách quan trọng

**C03.** Trong SVM tuyến tính, điều gì quyết định độ rộng của margin?
A. Số lượng support vectors · B. Hằng số C · C. Độ lớn margin tỉ lệ nghịch với ||w|| · D. Số chiều của dữ liệu

**C04.** SVM kernel RBF với gamma rất lớn sẽ gây hiện tượng gì?
A. Biên càng mượt, underfit · B. Model trở thành tuyến tính · C. Margin càng rộng · D. Biên cong ôm sát dữ liệu, dễ overfit

**C05.** Công thức Entropy trong cây quyết định dùng log cơ số mấy?
A. Log cơ số 2, đơn vị bit · B. Log cơ số 10 · C. Log tự nhiên, đơn vị nat · D. Không dùng log, chỉ đếm tỉ lệ

**C06.** Tiêu chí chọn điểm split tốt trong cây quyết định là gì?
A. Split có nhiều nhánh con nhất · B. Split có Information Gain lớn nhất · C. Split cân bằng số mẫu nhất · D. Split dùng feature đầu tiên

**C07.** Model đạt train acc 99% nhưng val acc 70%. Chẩn đoán và hướng xử lý?
A. Underfitting, cần tăng độ phức tạp · B. Dữ liệu test bị nhiễu · C. Overfitting, cần regularization/thêm dữ liệu · D. Model hội tụ tốt, không vấn đề

**C08.** Dữ liệu 95% âm tính, 5% dương tính. Nên đánh giá bằng cách chia nào?
A. K-fold thường vì đơn giản · B. Leave-one-out vì chính xác nhất · C. Chia train/test một lần là đủ · D. Stratified k-fold để giữ tỉ lệ lớp mỗi fold

**C09.** Bài toán có hàng trăm feature thừa. Chọn regularization nào để tự động loại feature?
A. L1 (Lasso) vì tạo sparsity, tự loại feature thừa · B. L2 vì đẩy trọng số về 0 hẳn · C. Dropout vì là regularization duy nhất dùng được · D. Không cần regularization, thêm cây là đủ

**C10.** Trong trường hợp tập dữ liệu chứa nhiều đặc trưng có độ tương quan tuyến tính rất cao với nhau (hiện tượng Đa cộng tuyến — Multicollinearity), kỹ thuật L2 Regularization (Ridge) thường được ưu tiên hơn L1 (Lasso) vì lý do gì?
A. Vì L1 sẽ chọn ngẫu nhiên 1 đặc trưng và loại bỏ các đặc trưng còn lại một cách không ổn định, trong khi L2 co đều các hệ số trọng số và luôn đảm bảo ma trận $(X^T X + \lambda I)$ khả nghịch · B. Vì L2 tính toán không cần ma trận · C. Vì L2 luôn đưa toàn bộ trọng số về chính xác bằng 0 · D. Vì L2 không cần siêu tham số lambda

**C11.** Cần train nhanh baseline ít tune hyperparameter. Chọn optimizer nào?
A. Chỉ dùng SGD vì Adam không bao giờ hội tụ · B. Dùng Adagrad cho mọi bài vision · C. Adam vì hội tụ nhanh, ít tune · D. Optimizer không ảnh hưởng kết quả

**C12.** Loss dao động mạnh rồi NaN ngay vài epoch đầu. Xử lý learning rate thế nào?
A. Tăng lr gấp 10 để train nhanh · B. Giữ lr cố định rất nhỏ suốt train · C. Dùng lr khác nhau mỗi layer là sai · D. Warmup lr từ nhỏ + giảm dần (cosine/step)

**C13.** Phát biểu đúng về kiến trúc kinh điển?
A. VGG: chồng nhiều lớp conv 3x3 · B. ResNet: dùng kernel 11x11 ở mọi lớp · C. AlexNet: dùng residual connection · D. LeNet: có attention

**C14.** Điểm đặc trưng của ResNet và EfficientNet?
A. ResNet dùng CONCAT như U-Net · B. ResNet dùng cộng dư (ADD), EfficientNet scale đều sâu/rộng/phân giải · C. EfficientNet chỉ tăng độ sâu · D. ResNet sâu hơn luôn tệ hơn VGG nông

**C15.** Vai trò của Non-Maximum Suppression (NMS) trong detection?
A. Giữ tất cả box để tăng recall · B. Chọn box nhỏ nhất · C. Giữ box điểm cao nhất, xóa box trùng lặp · D. Sắp xếp box theo diện tích

**C16.** So sánh đúng về YOLO và R-CNN?
A. YOLO chính xác hơn R-CNN mọi trường hợp · B. R-CNN nhanh hơn YOLO · C. Cả hai đều không dùng NMS · D. YOLO 1-stage nhanh real-time; R-CNN 2-stage chính xác, chậm

**C17.** Vì sao Random Forest đỡ overfit hơn một cây quyết định đơn?
A. Bagging + chọn feature ngẫu nhiên làm giảm overfit · B. Random Forest không bao giờ overfit · C. Càng ít cây càng tốt · D. Mỗi cây dùng toàn bộ dữ liệu và feature

**C18.** Đánh giá kết quả K-Means bằng silhouette như thế nào?
A. Silhouette âm là tốt · B. Silhouette trung bình gần 1 là cụm tốt · C. Silhouette chỉ dùng cho học giám sát · D. K-Means không cần chuẩn hóa dữ liệu

**C19.** Phát hiện gian lận tỉ lệ 1:99. Hướng xử lý đúng?
A. Chỉ dùng accuracy là đủ · B. Undersampling lớp thiểu số · C. SMOTE sinh mẫu thiểu số + đánh giá bằng F1 · D. Copy y nguyên mẫu thiểu số 100 lần

**C20.** Chọn hàm kích hoạt đúng cho hidden và output?
A. Sigmoid cho mọi hidden vì có đạo hàm đẹp · B. Softmax cho hidden để chuẩn hóa · C. Không cần activation nếu mạng đủ sâu · D. Hidden dùng ReLU/GELU, output dùng Softmax/Sigmoid tùy task

**C21.** Vì sao Transformer dùng LayerNorm thay vì BatchNorm?
A. LayerNorm vì không phụ thuộc batch · B. BatchNorm vì luôn tốt hơn mọi trường hợp · C. Bỏ hết norm để giảm tham số · D. InstanceNorm là chuẩn cho NLP

**C22.** CNN càng sâu càng tệ (degradation). Giải pháp kiến trúc đúng?
A. Tăng kernel lên 11x11 · B. Thêm residual connection như ResNet · C. Đổi hết sang Sigmoid · D. Giảm batch size xuống 1

**C23.** Skip connection trong U-Net dùng phép gì?
A. ADD như ResNet · B. Nhân (multiply) hai nhánh · C. CONCAT feature encoder vào decoder · D. Không có skip, U-Net là mạng thẳng

**C24.** Phát biểu đúng về Vision Transformer (ViT)?
A. ViT dùng conv 3x3 xếp chồng · B. ViT không cần positional encoding · C. ViT hiệu quả với dữ liệu cực nhỏ từ đầu · D. ViT cắt patch, dùng [CLS] + Transformer, không convolution

**C25.** Phân biệt semantic và instance segmentation?
A. Semantic gán nhãn pixel, không tách vật thể riêng · B. Instance là phân lớp ảnh · C. Semantic tách từng vật thể · D. Hai task giống nhau hoàn toàn

**C26.** Phát biểu đúng về mô hình sinh?
A. Stable Diffusion là một biến thể GAN · B. Stable Diffusion dùng diffusion khử nhiễu dần · C. GAN không bao giờ mode collapse · D. Autoencoder sinh ảnh đẹp hơn diffusion

**C27.** Chỉ có 500 ảnh X-quang, dùng ResNet pretrain ImageNet. Chiến lược đúng?
A. Train từ đầu với data nhỏ · B. Fine-tune toàn mạng với lr lớn · C. Đóng băng backbone, fine-tune head lr nhỏ · D. Bỏ pretrain vì gây overfit

**C28.** Thứ tự đúng của pipeline tiền xử lý văn bản?
A. Loại stopwords -> tokenization -> POS · B. POS -> stemming -> tokenization · C. Stemming thay thế tokenization · D. Tokenization -> normalization -> stemming/lemma -> POS -> loại stopwords

**C29.** Tiếng Việt nhiều từ viết tắt, sai chính tả (OOV). Biểu diễn từ nào phù hợp?
A. FastText (n-gram ký tự) trị OOV/từ hiếm · B. One-hot vì nhẹ và giữ ngữ nghĩa · C. TF-IDF vì hiểu ngữ cảnh sâu · D. Word2Vec có sẵn là đủ mọi trường hợp

**C30.** Task phân loại cảm xúc và task sinh mô tả sản phẩm. Chọn model đúng?
A. BERT để sinh truyện, GPT để phân loại · B. Hiểu/phân loại dùng BERT, sinh văn bản dùng GPT · C. Cả hai giống nhau, chọn ngẫu nhiên · D. GPT hiểu 2 chiều tốt hơn BERT

## Phần tự luận (chấm riêng, 10đ/câu)

**E01 (CV).** Nhận diện ngôn ngữ ký hiệu từ video (giống đề OLP AI 2025): 10.000 clip ngắn, 50 ký hiệu, quay bởi 100 người khác nhau, ánh sáng/nền đa dạng, cần chạy gần real-time trên laptop thường. Đề xuất giải pháp theo khung 5 bước: (1) phân tích dữ liệu, (2) lựa chọn mô hình và lý do, (3) pipeline xử lý, (4) metric đánh giá, (5) phương án cải tiến. Không cần code chi tiết.

**E02 (NLP).** Dịch máy Hoa–Việt (giống đề OLP AI 2025): 200.000 cặp câu, nhiều câu thương mại điện tử, yêu cầu bảo vệ nghĩa số lượng/tiền tệ. Đề xuất giải pháp theo khung 5 bước như trên, metric SacreBLEU. Không cần code chi tiết.

**E03 (CV).** Phát hiện bệnh trên lá khoai tây ngoài đồng: 8.000 ảnh, 4 loại bệnh (2 loại hiếm), cần khoanh vùng bệnh trên lá, chạy trên điện thoại của nông dân. Đề xuất giải pháp theo khung 5 bước. Không cần code chi tiết.

**E04 (ML tabular).** Dự đoán sinh viên bỏ học: 50.000 hồ sơ x 40 đặc trưng, tỉ lệ bỏ học 8%, phòng đào tạo cần biết lý do để can thiệp sớm. Đề xuất giải pháp theo khung 5 bước. Không cần code chi tiết.

---
*Còn tiếp Đề 02–20 (đang soạn). Mỗi đề mới 60 câu trắc nghiệm/code + 4 tự luận.*
