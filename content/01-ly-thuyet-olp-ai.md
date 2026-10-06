# 01 — Lý thuyết OLP AI HCMUS 2026 (vòng loại cấp trường)

> Phạm vi: ML cổ điển (§1) · Deep Learning (§2) · Thị giác máy tính (§3) · NLP (§4) · Xác suất – Thống kê (§5).
> Mỗi mục: định nghĩa → công thức (text) → ví dụ → ⭐ Hay ra thi.
> Bảng lỗi hay mắc: §6. File này là nền để tra cứu từ đáp án (dạng "→ Xem §x.y").

---

## §1. ML cổ điển

### §1.1 k-NN (lazy learner)
- Định nghĩa: không học tham số ở phase train (chỉ lưu dữ liệu — "lazy"); khi predict mới tính khoảng cách tới k láng giềng gần nhất rồi vote (classification) / trung bình (regression).
- Công thức: Euclid d = sqrt(sum((xi-yi)^2)); Manhattan = sum|xi-yi|.
- Ví dụ: k=3, nhãn láng giềng [0,1,1] → predict 1.
- ⭐ Hay ra thi: k-NN KHÔNG có training phase; k nhỏ → overfit (nhạy nhiễu), k lớn → underfit; nhớ chuẩn hóa feature vì dùng khoảng cách.

### §1.2 SVM (margin, support vectors, kernel)
- Định nghĩa: tìm siêu phẳng phân tách với margin (lề) lớn nhất; support vectors là điểm nằm sát lề quyết định biên.
- Công thức: margin = 2/||w||; RBF kernel K(x,z) = exp(-gamma * ||x-z||^2).
- Ví dụ: gamma lớn → biên cong ôm sát từng điểm (overfit); gamma nhỏ → biên mượt (underfit).
- ⭐ Hay ra thi: gamma là "độ cong" của RBF; C lớn → phạt lỗi nặng → margin hẹp, dễ overfit.

### §1.3 Cây quyết định, Entropy, Information Gain
- Định nghĩa: chia dữ liệu bằng câu hỏi trên feature sao cho node con "sạch" nhất; Entropy đo độ hỗn loạn.
- Công thức: Entropy H = -sum(p_i * log2(p_i)); Information Gain = H(cha) - trung bình có trọng số H(con).
- Ví dụ: node [3 đỏ, 3 xanh] → H = 1 bit; node [4 đỏ, 0 xanh] → H = 0.
- ⭐ Hay ra thi: Entropy dùng log cơ số 2 (đơn vị bit); Gain cao → split tốt.

### §1.4 Random Forest
- Định nghĩa: ensemble nhiều cây, mỗi cây train trên bootstrap sample + chọn ngẫu nhiên tập feature ở mỗi split, rồi vote.
- Ví dụ: 100 cây vote, 70 cây đoán "mèo" → predict "mèo".
- ⭐ Hay ra thi: RF giảm overfit so với 1 cây nhờ bagging + random feature; vẫn overfit được nếu cây quá sâu.

### §1.5 Overfitting / Underfitting, bias-variance, cross-validation
- Định nghĩa: overfit = thuộc train, kém test (variance cao); underfit = kém cả hai (bias cao). Bias-variance tradeoff: giảm cái này thường tăng cái kia.
- Công thức: k-fold CV: chia k phần, lần lượt lấy 1 phần làm validation, báo cáo trung bình; stratified giữ nguyên tỉ lệ lớp ở mỗi fold.
- Ví dụ: train acc 99%, val acc 70% → overfit → thêm data/regularization/giảm độ phức tạp.
- ⭐ Hay ra thi: stratified k-fold BẮT BUỘC khi dữ liệu mất cân bằng; early stopping chống overfit.

### §1.6 Regularization L1 / L2
- Định nghĩa: cộng phạt vào loss để ép trọng số nhỏ lại. L1 (Lasso): lambda*sum|w| → sinh sparsity (nhiều w = 0, tự chọn feature). L2 (Ridge): lambda*sum(w^2) → w nhỏ đều, không về 0 hẳn.
- Ví dụ: feature thừa nhiều → L1 tự loại; multicollinearity → L2 ổn định hơn.
- ⭐ Hay ra thi: L1 → sparse/chọn feature; L2 → co đều trọng số.

### §1.7 Metric: accuracy, precision, recall, F1, AUC-ROC, PR, confusion matrix
- Định nghĩa: confusion matrix = [[TN, FP],[FN, TP]]. Precision = TP/(TP+FP) (đoán dương thì đúng bao nhiêu). Recall = TP/(TP+FN) (bắt được bao nhiêu ca dương thật). F1 = 2PR/(P+R). Accuracy = (TP+TN)/all.
- Ví dụ: phát hiện bệnh hiếm: accuracy 99% vẫn vô nghĩa nếu toàn đoán âm → dùng recall/F1/PR curve.
- ⭐ Hay ra thi: dữ liệu lệch → bỏ accuracy, dùng F1/PR-AUC; ROC-AUC dễ "đẹp giả" khi lớp dương hiếm; ngưỡng quyết định đổi → precision/recall đổi ngược nhau.

### §1.8 K-Means & silhouette
- Định nghĩa: clustering: khởi tạo k centroid, lặp 2 bước gán cụm → cập nhật centroid tới hội tụ. Silhouette s = (b-a)/max(a,b), a = khoảng cách trung bình tới điểm cùng cụm, b = tới cụm gần nhất; s gần 1 → cụm tốt.
- Ví dụ: s trung bình 0.8 → cụm tách tốt; s âm → điểm gán nhầm cụm.
- ⭐ Hay ra thi: K-Means nhạy khởi tạo + phải chuẩn hóa + phải chọn k trước (dùng elbow/silhouette).

### §1.9 Mất cân bằng lớp
- Định nghĩa: lớp thiểu số bị model bỏ qua. Cách xử lý: oversampling/SMOTE (sinh mẫu thiểu số), undersampling (bớt đa số), class weights (phạt nặng lỗi ở lớp hiếm).
- Ví dụ: gian lận 1:99 → class_weight {gian lận: 99} hoặc SMOTE.
- ⭐ Hay ra thi: SMOTE sinh mẫu nội suy giữa các điểm thiểu số (không copy y nguyên); undersampling mất thông tin.

### §1.10 Feature engineering & selection
- Định nghĩa: tạo feature mới (one-hot, binning, tương tác) + loại feature thừa (filter/wrapper/L1).
- ⭐ Hay ra thi: one-hot cho categorical không thứ tự; label-encoding gây "thứ tự giả".

---

## §2. Deep Learning

### §2.1 Perceptron / MLP
- Định nghĩa: perceptron: y = f(w·x + b). MLP = chồng nhiều lớp tuyến tính + activation phi tuyến → xấp xỉ hàm phức tạp.
- ⭐ Hay ra thi: không có activation phi tuyến thì chồng bao nhiêu lớp cũng chỉ là tuyến tính.

### §2.2 Hàm kích hoạt
- Sigmoid σ = 1/(1+e^-x) → (0,1), dùng output binary (kèm BCE). Softmax → phân phối xác suất đa lớp. Tanh → (-1,1), zero-centered hơn sigmoid. ReLU = max(0,x): rẻ, trị vanishing ở miền dương. Leaky ReLU: x<0 giữ slope nhỏ (trị dying ReLU). GELU: mượt, chuẩn cho Transformer/BERT.
- ⭐ Hay ra thi: Softmax dùng cho OUTPUT đa lớp (kèm CrossEntropy); ReLU/GELU cho hidden; Sigmoid hidden dễ bão hòa → vanishing.

### §2.3 Forward / Backward / vòng lặp train
- Thứ tự đúng: forward → tính loss → zero_grad → backward → optimizer.step(). zero_grad TRƯỚC backward (PyTorch cộng dồn grad).
- ⭐ Hay ra thi: quên zero_grad → grad cộng dồn qua batch → train sai; backward không tự update, phải gọi step().

### §2.4 Hàm loss
- MSE = mean((y-pred)^2): regression, phạt nặng outlier. MAE = mean|y-pred|: bền với outlier. BCE (binary): -[y log p + (1-y) log(1-p)], input là xác suất (đi với Sigmoid). BCEWithLogitsLoss = Sigmoid + BCE gộp (ổn định số, input là logit). CrossEntropyLoss (đa lớp) = LogSoftmax + NLL gộp, input là logit CHƯA softmax.
- ⭐ Hay ra thi: CrossEntropyLoss/BCEWithLogitsLoss ĐÃ tích hợp activation → KHÔNG thêm Softmax/Sigmoid tay trước đó (lỗi double-softmax rất hay ra).

### §2.5 Optimizer
- SGD: w -= lr * grad. Momentum: giữ vận tốc, vượt local minima/dao động. Adam = Momentum + RMSProp (lr thích ứng từng tham số): hội tụ nhanh, mặc định tốt cho hầu hết bài.
- ⭐ Hay ra thi: Adam hội tụ nhanh nhưng đôi khi generalize kém hơn SGD+momentum đã tune kỹ.

### §2.6 Learning rate schedule
- Định nghĩa: giảm lr theo thời gian (step decay, cosine annealing), warmup: tăng lr từ nhỏ lên đầu train (chuẩn cho Transformer).
- ⭐ Hay ra thi: lr quá lớn → diverge; quá nhỏ → kẹt/chậm; warmup chống shock đầu train.

### §2.7 Khởi tạo trọng số
- Zeros init SAI: mọi neuron giống nhau → học y hệt nhau (symmetry). Xavier/Glorot: cho Tanh/Sigmoid. He/Kaiming: cho ReLU (phương sai lớn gấp đôi).
- ⭐ Hay ra thi: zeros init phá đối xứng thất bại; ReLU đi với He, Tanh/Sigmoid đi với Xavier.

### §2.8 BatchNorm / LayerNorm (vị trí)
- BatchNorm: chuẩn hóa theo batch (N,H,W trên conv), block chuẩn Linear/Conv → Norm → Activation; có running stats cho inference; batch nhỏ → noisy. LayerNorm: chuẩn hóa theo feature của từng mẫu, không phụ thuộc batch → chuẩn cho Transformer/RNN.
- ⭐ Hay ra thi: thứ tự Linear → Norm → ReLU; inference dùng running stats, KHÔNG dùng stats của batch test; Transformer dùng LayerNorm.

### §2.9 Dropout
- Định nghĩa: train randomly tắt neuron với p (thường 0.2–0.5), inference TẮT dropout + (inverted dropout đã tự scale ở train).
- ⭐ Hay ra thi: quên tắt dropout khi test → kết quả ngẫu nhiên; dropout là ensemble ngầm.

### §2.10 Vanishing / exploding gradient, early stopping
- Vanishing: grad teo dần qua nhiều lớp (Sigmoid/Tanh + mạng sâu) → lớp đầu không học; trị bằng ReLU/residual/norm/init tốt. Exploding: grad phình → loss NaN; trị bằng gradient clipping. Early stopping: dừng khi val loss ngừng cải thiện (patience).
- ⭐ Hay ra thi: ResNet sinh ra để trị vanishing/degradation; clip trị exploding.

---

## §3. Thị giác máy tính

### §3.1 Convolution + công thức output
- Công thức: out = floor((W - k + 2p)/s) + 1 (mỗi chiều). Same padding: p để out = ceil(W/s); stride 1 + same → giữ nguyên kích thước. Valid: p = 0.
- Ví dụ: W=32, k=3, s=1, p=1 → (32-3+2)/1+1 = 32. W=32, k=3, s=2, p=1 → (32-3+2)/2+1 = floor(15.5)+1 = 16.
- Ví dụ 2: W=28, k=5, s=1, p=0 → 24. W=224, k=7, s=2, p=3 → (224-7+6)/2+1 = 112.
- ⭐ Hay ra thi: 90% câu tính tay rơi vào công thức này; nhớ floor TRƯỚC khi +1.

### §3.2 Pooling, receptive field
- Max pooling lấy đặc trưng mạnh nhất (bất biến dịch nhẹ), avg làm mượt, global avg pooling (GAP) ép mỗi channel thành 1 số (thay FC, giảm tham số). Receptive field: vùng ảnh gốc ảnh hưởng tới 1 neuron, tăng qua các lớp conv/stride.
- ⭐ Hay ra thi: GAP giảm overfit so với FC khủng; pooling giảm kích thước, KHÔNG học tham số.

### §3.3 Kiến trúc kinh điển
- LeNet: mở đường CNN. AlexNet: ReLU + Dropout + GPU. VGG: chồng conv 3x3 (sâu mà đơn giản). ResNet: residual (trị degradation). EfficientNet: scale đều sâu/rộng/phân giải (compound scaling).
- ⭐ Hay ra thi: VGG = 3x3 sâu; ResNet = residual; EfficientNet = compound scaling.

### §3.4 Skip connection: ResNet ADD vs U-Net CONCAT
- ResNet: cộng (ADD) input vào output block → học phần dư, giữ số channel. U-Net: nối (CONCAT) feature encoder vào decoder → giữ chi tiết không gian cho segmentation.
- ⭐ Hay ra thi: ADD = ResNet, CONCAT = U-Net; nhầm là mất điểm.

### §3.5 Vision Transformer (ViT)
- Ảnh cắt thành patches (vd 16x16), flatten + linear embed, thêm [CLS] token + positional embedding, cho qua Transformer encoder KHÔNG convolution.
- ⭐ Hay ra thi: ViT không có conv, không có inductive bias dịch chuyển → cần data lớn / pretrain; [CLS] để classification.

### §3.6 Detection: IoU, NMS, mAP, R-CNN vs YOLO
- IoU = Diện tích Giao / Diện tích Hợp, ngưỡng thường 0.5. NMS: giữ box điểm cao nhất, xóa box trùng IoU cao. mAP: trung bình AP các lớp. R-CNN dòng 2-stage (proposal rồi classify, chính xác, chậm). YOLO 1-stage (lưới predict trực tiếp, nhanh real-time).
- Ví dụ: Giao=20, Hợp=80 → IoU=0.25 < 0.5 → coi như sai.
- ⭐ Hay ra thi: IoU = Giao/HỢP (không phải giao/ảnh); NMS xóa trùng lặp; YOLO nhanh, R-CNN chính xác.

### §3.7 Segmentation: semantic vs instance
- Semantic: gán nhãn từng pixel (không phân biệt 2 xe khác nhau). Instance: tách từng vật thể riêng + nhãn.
- ⭐ Hay ra thi: U-Net là baseline semantic segmentation y tế.

### §3.8 GAN vs Diffusion vs Autoencoder
- GAN: Generator đấu Discriminator (nhanh, ảnh sắc, dễ mode collapse). Diffusion (Stable Diffusion): khử nhiễu dần (ảnh đẹp, đa dạng, sampling chậm). Autoencoder: nén → tái tạo (học biểu diễn, nén, denoise).
- ⭐ Hay ra thi: Stable Diffusion là Diffusion, KHÔNG phải GAN; mode collapse là bệnh của GAN.

### §3.9 Augmentation & transfer learning
- Augmentation: crop/flipxoay/màu/cutout-mixup (tăng data, chống overfit; test KHÔNG augment). Transfer: dùng backbone pretrain (ImageNet), fine-tune: đầu train lr nhỏ / đóng băng backbone khi data ít.
- ⭐ Hay ra thi: data ít → đóng băng backbone + fine-tune head; data nhiều/miền khác → unfreeze dần với lr nhỏ.

---

## §4. NLP

### §4.1 Pipeline tiền xử lý (đúng thứ tự)
- tokenization (cắt từ) → normalization (lowercase, bỏ dấu thừa) → stemming/lemmatization (về gốc từ) → POS tagging (gán từ loại) → loại stopwords.
- ⭐ Hay ra thi: thứ tự này hay hỏi; stemming cắt đuôi thô (running→runn), lemmatization về dạng từ điển (better→good).

### §4.2 Biểu diễn từ
- One-hot: sparse, khổng lồ, không ngữ nghĩa. TF-IDF: tần suất × nghịch đảo phủ văn bản, tốt cho retrieval/classification baseline. Word2Vec: CBOW (ngữ cảnh → từ, nhanh, từ phổ biến) / Skip-gram (từ → ngữ cảnh, tốt từ hiếm) + negative sampling. GloVe: dùng thống kê toàn cục. FastText: n-gram ký tự → trị OOV/từ hiếm/tiếng Việt dính lỗi. BERT: contextual (1 từ nhiều vector theo ngữ cảnh).
- ⭐ Hay ra thi: từ hiếm/OOV → FastText; cần ngữ cảnh → BERT; baseline nhanh → TF-IDF.

### §4.3 Cosine similarity
- cos = (A·B)/(||A||·||B||), miền [-1,1]; so hướng, bỏ qua độ dài → chuẩn cho embedding/search.
- Ví dụ: A=(1,0), B=(0,1) → cos=0 (trực giao, không liên quan).
- ⭐ Hay ra thi: embedding so bằng cosine, KHÔNG Euclid (Euclid nhạy độ dài vector).

### §4.4 RNN / LSTM / GRU
- RNN thường: vanishing qua chuỗi dài (trọng số lặp nhân nhiều lần). LSTM: cổng forget/input/output + cell state → giữ thông tin dài. GRU: gọn (reset/update), nhanh hơn, tương đương nhiều task.
- ⭐ Hay ra thi: gating sinh ra để trị vanishing trên chuỗi; GRU nhẹ hơn LSTM.

### §4.5 Transformer: self-attention Q/K/V, multi-head, positional encoding
- Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V; chia sqrt(d_k) để softmax không bão hòa. Multi-head: nhiều head học quan hệ khác nhau. Positional encoding (sin/cos hoặc học được): bù thứ tự từ vì attention vốn hoán vị bất biến.
- ⭐ Hay ra thi: thiếu positional encoding → mất thứ tự; chia sqrt(d_k) chống bão hòa softmax.

### §4.6 BERT vs GPT
- BERT: encoder 2 chiều + MLM (hiểu ngữ cảnh, NLU: classification/NER/QA trích xuất). GPT: decoder tự hồi quy left-to-right (sinh văn bản, few-shot).
- ⭐ Hay ra thi: hiểu/phân loại → BERT; sinh văn bản → GPT.

### §4.7 Metric: BLEU, ROUGE, perplexity
- BLEU: precision n-gram dịch máy vs reference (có brevity penalty phạt câu ngắn). ROUGE: recall-oriented cho tóm tắt. Perplexity = exp(loss): càng thấp model ngôn ngữ càng chắc.
- ⭐ Hay ra thi: BLEU ↔ dịch máy, ROUGE ↔ tóm tắt, perplexity thấp = tốt.

### §4.8 Task NLP kinh điển
- Classification (cảm xúc/spam), NER (tên người/địa danh), MT (dịch máy), QA (trích xuất/sinh câu trả lời), summarization (trích xuất/abstractive).
- ⭐ Hay ra thi: NER là token classification; QA trích xuất đo bằng F1/EM.

---

## §5. Xác suất – Thống kê

### §5.1 Định lý Bayes + ví dụ tính tay
- P(A|B) = P(B|A)P(A)/P(B). Khung bảng 1000 người cho bài test y tế.
- Ví dụ: bệnh 1%, test nhạy 90%, dương giả 5%. P(bệnh|+) = 0.9*0.01/(0.9*0.01+0.05*0.99) = 0.009/0.0585 ≈ 15.4%.
- ⭐ Hay ra thi: base rate thấp → hậu nghiệm vẫn thấp dù test tốt (base rate fallacy).

### §5.2 Phân phối thường gặp
- Bernoulli: 1 lần thử p (E=p, Var=p(1-p)). Binomial: n lần (đếm thành công). Normal: trung bình/đo lường + CLT. Poisson: đếm sự kiện hiếm trên đơn vị thời gian.
- ⭐ Hay ra thi: đếm sự kiện hiếm (cuộc gọi/phút) → Poisson; 0/1 → Bernoulli.

### §5.3 Kỳ vọng / phương sai
- E[aX+b] = aE[X]+b; Var(aX+b) = a^2 Var(X); X,Y độc lập: Var(X+Y)=Var(X)+Var(Y).
- ⭐ Hay ra thi: hằng số cộng vào không đổi phương sai; nhân a → phương sai nhân a^2.

### §5.4 MLE vs MAP
- MLE: argmax P(data|θ) (chỉ dữ liệu). MAP: argmax P(data|θ)P(θ) (dữ liệu + prior) → MAP = MLE + regularization (prior Gaussian ↔ L2).
- ⭐ Hay ra thi: MAP có prior, MLE không; prior Gaussian tương đương L2.

### §5.5 Kiểm định giả thuyết & p-value
- p-value = P(thấy kết quả cực đoan ≥ quan sát | H0 đúng). p < alpha (0.05) → bác bỏ H0. p-value KHÔNG phải P(H0 đúng).
- ⭐ Hay ra thi: p nhỏ → bác bỏ H0; p-value không đo độ lớn hiệu ứng.

### §5.6 Correlation vs causation, sampling
- Tương quan ≠ nhân quả (confounder ẩn). Sampling: random/stratified (giữ tỉ lệ nhóm) / cluster.
- ⭐ Hay ra thi: stratified sampling cho dữ liệu lệch nhóm.

---

## §6. Bảng "Lỗi hay mắc" (SAI → ĐÚNG)

| # | SAI (bẫy) | ĐÚNG |
|---|---|---|
| 1 | BatchNorm đặt sau ReLU | Linear/Conv → Norm → Activation (§2.8) |
| 2 | Thêm Softmax trước CrossEntropyLoss | Loss đã gồm Softmax, đưa logit thô (§2.4) |
| 3 | Thêm Sigmoid trước BCEWithLogitsLoss | Đưa logit thô (§2.4) |
| 4 | k-NN có phase training | Lazy, chỉ lưu data (§1.1) |
| 5 | IoU = giao / diện tích ảnh | IoU = Giao / Hợp (§3.6) |
| 6 | Entropy log cơ số 10/e | Log cơ số 2, đơn vị bit (§1.3) |
| 7 | Stable Diffusion là GAN | Là Diffusion (§3.8) |
| 8 | zero_grad sau backward | Trước backward (§2.3) |
| 9 | U-Net skip là ADD | CONCAT; ADD là ResNet (§3.4) |
| 10 | Accuracy tốt cho dữ liệu lệch | Dùng F1/PR-AUC (§1.7) |
| 11 | Khởi tạo toàn 0 vẫn train được | Vỡ đối xứng, dùng He/Xavier (§2.7) |
| 12 | Dropout bật khi inference | Tắt khi test (§2.9) |
| 13 | So embedding bằng Euclid | Dùng cosine (§4.3) |
| 14 | p-value = P(H0 đúng) | P(data cực đoan \| H0 đúng) (§5.5) |
| 15 | ViT dùng convolution | Patches + Transformer, không conv (§3.5) |
| 16 | gamma RBF lớn → biên mượt | Gamma lớn → biên cong ôm sát, overfit (§1.2) |
| 17 | L1 chỉ co trọng số | L1 sinh sparse/chọn feature (§1.6) |
| 18 | BLEU cho tóm tắt | BLEU ↔ dịch máy; tóm tắt ↔ ROUGE (§4.7) |
| 19 | Test có augment như train | Test không augment (§3.9) |
| 20 | Attention không cần chia sqrt(d_k) | Phải chia để softmax khỏi bão hòa (§4.5) |
| 21 | BERT để sinh văn bản dài | Sinh → GPT; BERT để hiểu (§4.6) |
| 22 | Pooling có tham số học | Không tham số (§3.2) |
| 23 | SMOTE = copy mẫu thiểu số | Nội suy sinh mẫu mới (§1.9) |
| 24 | Var(aX+b) = a·Var(X) | = a²·Var(X) (§5.3) |
