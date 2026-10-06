# PROMPT SOẠN TÀI LIỆU ÔN THI OLP AI (đưa cho agent khác)

Bạn là chuyên gia soạn tài liệu ôn thi. Hãy tạo MỘT file markdown duy nhất, toàn diện và chi tiết để ôn thi vòng loại cấp trường Olympic AI HCMUS 2026.

## Bối cảnh kỳ thi
- Thi cá nhân, hình thức: **trắc nghiệm lý thuyết + tự luận giải pháp AI**
- Phạm vi: Học máy (ML), Thị giác máy tính (CV), Xử lý ngôn ngữ tự nhiên (NLP), Xác suất – Thống kê
- Đối tượng: sinh viên đại học ngành CNTT, đã có nền tảng lập trình
- Mục tiêu: tài liệu đủ sâu để làm được mọi câu trắc nghiệm lý thuyết và viết được bài tự luận đề xuất giải pháp AI

## PHẦN 1 — LÝ THUYẾT CHI TIẾT (trọng tâm)

### 1. ML cổ điển
k-NN (lazy learner, khoảng cách Euclid, cách chọn k), SVM (margin, support vectors, kernel RBF và vai trò của gamma), cây quyết định & Entropy/Information Gain, Random Forest, overfitting vs underfitting, bias-variance tradeoff, cross-validation (k-fold, stratified), regularization L1/L2, các metric (accuracy, precision, recall, F1, AUC-ROC, PR curve, confusion matrix), K-Means & silhouette, xử lý mất cân bằng lớp (oversampling/undersampling/SMOTE/class weights), feature engineering & feature selection.

### 2. Deep Learning
Perceptron/MLP, tất cả hàm kích hoạt (ReLU, Sigmoid, Softmax, Tanh, GELU, Leaky ReLU) + công thức + khi nào dùng cái nào, forward/backward propagation, các hàm loss chi tiết (MSE, MAE, BCE vs BCEWithLogitsLoss, CrossEntropyLoss — nhấn mạnh cái nào đã tích hợp sẵn activation nên KHÔNG thêm tay), optimizer (SGD, Momentum, Adam + ý tưởng công thức update), learning rate schedule, khởi tạo trọng số (zeros SAI ở đâu, Xavier/Glorot, He/Kaiming), BatchNorm/LayerNorm (vị trí đúng trong block), Dropout, vanishing/exploding gradient, early stopping.

### 3. Thị giác máy tính
Convolution + công thức kích thước output ⌊(W−k+2p)/s⌋+1 kèm nhiều ví dụ tính tay các trường hợp (same/valid/stride), pooling (max/avg/global avg), receptive field, các kiến trúc kinh điển và điểm đặc trưng của từng cái (LeNet, AlexNet, VGG, ResNet, EfficientNet), skip connection (ResNet dùng ADD, U-Net dùng CONCAT), Vision Transformer chi tiết (patches, [CLS] token, không dùng convolution), object detection (IoU = Giao/Hợp, NMS, mAP, R-CNN vs YOLO), segmentation (semantic vs instance), GAN vs Diffusion vs Autoencoder, data augmentation, transfer learning & fine-tuning.

### 4. NLP
Pipeline tiền xử lý theo đúng thứ tự (tokenization → normalization → stemming/lemmatization → POS tagging → loại stopwords), các phương pháp biểu diễn từ (one-hot, TF-IDF, Word2Vec CBOW/Skip-gram + negative sampling, GloVe, FastText, BERT contextual) + ưu/nhược điểm + khi nào dùng, cosine similarity, RNN/LSTM/GRU (vì sao cần gating, giải quyết vấn đề gì của RNN thường), Transformer chi tiết (self-attention Q/K/V, multi-head attention, positional encoding), BERT vs GPT, các metric (BLEU, ROUGE, perplexity), các task NLP kinh điển (classification, NER, MT, QA, summarization).

### 5. Xác suất – Thống kê
Định lý Bayes + ví dụ tính tay, các phân phối thường gặp (Bernoulli, Binomial, Normal, Poisson) + khi nào dùng, kỳ vọng/phương sai, MLE vs MAP, kiểm định giả thuyết & p-value, correlation vs causation, các phương pháp sampling.

### 6. Bảng "Lỗi hay mắc"
Ít nhất 20 cặp SAI → ĐÚNG thường gặp trong đề thi trắc nghiệm AI (ví dụ: vị trí BatchNorm, CrossEntropyLoss có sẵn Softmax, k-NN không có training phase, IoU = Giao/Hợp, Entropy dùng log cơ số 2, Stable Diffusion là Diffusion không phải GAN, zero_grad đặt trước backward, U-Net skip = CONCAT...).

**Quy tắc cho mỗi mục lý thuyết:** định nghĩa ngắn gọn → công thức (viết dạng text/markdown đơn giản) → ví dụ minh họa cụ thể → dòng "⭐ Hay ra thi" nêu điểm mấu chốt. Đánh số mục dạng §x.y để phần đáp án trích dẫn được.

## PHẦN 2 — ĐỀ LUYỆN (KHÔNG ghi đáp án trong phần này)

- **100 câu trắc nghiệm**, mỗi câu 4 đáp án A/B/C/D, phân bố đều 5 chương lý thuyết. Độ khó: 60% nhận biết/thông hiểu, 30% vận dụng, 10% vận dụng cao (tính toán tay: Conv2D output, Entropy, IoU, F1, cosine similarity, Bayes...). Đáp án đúng phân bố ngẫu nhiên, không theo pattern đoán mò được.
- **6 câu tự luận giải pháp AI** (2 CV, 2 NLP, 2 ML tabular): mỗi câu mô tả một bài toán thực tế cụ thể (có bối cảnh, dữ liệu, ràng buộc) + yêu cầu đề xuất giải pháp + khung gợi ý 5 bước (phân tích dữ liệu → lựa chọn mô hình và lý do → pipeline xử lý → metric đánh giá → phương án cải tiến). Không yêu cầu code chi tiết.

## PHẦN 3 — ĐÁP ÁN & LỜI GIẢI CHI TIẾT

- 100 câu trắc nghiệm: đáp án đúng + giải thích **tại sao đúng** + giải thích **tại sao 3 đáp án còn lại sai** + trích dẫn mục lý thuyết Phần 1 (dạng "→ Xem §x.y").
- 6 câu tự luận: bài giải mẫu hoàn chỉnh theo khung 5 bước, có trích dẫn lý thuyết liên quan.

## Yêu cầu chung
- Tiếng Việt, giải thích sâu nhưng dễ hiểu, nhiều ví dụ thực tế
- Không copy nguyên văn từ bất kỳ nguồn nào, diễn đạt bằng lời của bạn
- Ưu tiên độ bao phủ và chiều sâu: càng đầy đủ chi tiết càng tốt
- Xuất ra thành MỘT file markdown duy nhất, có mục lục đầu file
