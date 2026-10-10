// Nguon video bai giang duoc tuyen chon ky luong tu cac chuyen gia hang dau the gioi:
// 3Blue1Brown, StatQuest (Josh Starmer), DeepLearning.AI (Andrew Ng), Andrej Karpathy, Yannic Kilcher, Computerphile.
// Tat ca cac video deu duoc TUA SAN (timestamp start=...) dung den doan trong tam can hoc.

export interface VideoResource {
  sectionId: string;
  topic: string;
  channel: string;
  title: string;
  youtubeId: string;
  startSeconds: number;
  timestampLabel: string;
  highlightNote: string;
}

export const VIDEO_RESOURCES: Record<string, VideoResource> = {
  '§1.1': {
    sectionId: '§1.1',
    topic: 'k-NN: Khoảng cách, cách chọn k và ranh giới quyết định',
    channel: 'StatQuest with Josh Starmer',
    title: 'StatQuest: K-nearest neighbors, Clearly Explained',
    youtubeId: 'HVXime0nQeI',
    startSeconds: 135,
    timestampLabel: '02:15',
    highlightNote: 'Giải thích trực quan cách thuật toán k-NN vote láng giềng, chọn k để tránh Overfit vs Underfit, và vì sao k-NN là Lazy Learner không có phase train.'
  },
  '§1.2': {
    sectionId: '§1.2',
    topic: 'SVM: Margin, Support Vectors và Kernel RBF (Vai trò của Gamma)',
    channel: 'StatQuest with Josh Starmer',
    title: 'Support Vector Machines Part 2: The Polynomial and RBF Kernel',
    youtubeId: '_PwhiWxHK8o',
    startSeconds: 240,
    timestampLabel: '04:00',
    highlightNote: 'Hiểu bản chất hàm nhân RBF (Radial Basis Function) và vì sao Gamma lớn làm biên quyết định cong ôm sát dữ liệu gây Overfitting.'
  },
  '§1.3': {
    sectionId: '§1.3',
    topic: 'Cây quyết định: Entropy và Information Gain',
    channel: 'StatQuest with Josh Starmer',
    title: 'Decision Trees: Entropy and Information Gain',
    youtubeId: 'YtebGVx-Fxw',
    startSeconds: 180,
    timestampLabel: '03:00',
    highlightNote: 'Cách tính Entropy dùng log cơ số 2 từng bước và công thức tính Information Gain để chọn nhánh phân tách tối ưu.'
  },
  '§1.4': {
    sectionId: '§1.4',
    topic: 'Random Forest: Bagging và Chọn đặc trưng ngẫu nhiên',
    channel: 'StatQuest with Josh Starmer',
    title: 'StatQuest: Random Forests Part 1 - Building, Using and Evaluating',
    youtubeId: 'J4Wdy0Wc_xQ',
    startSeconds: 110,
    timestampLabel: '01:50',
    highlightNote: 'Cơ chế Bootstrap Sampling và chọn ngẫu nhiên tập con đặc trưng (Random Subspace) giúp Random Forest giảm Overfit so với 1 cây đơn lẻ.'
  },
  '§1.5': {
    sectionId: '§1.5',
    topic: 'Bias-Variance Tradeoff, Overfitting & Cross-Validation',
    channel: 'StatQuest with Josh Starmer',
    title: 'Machine Learning Fundamentals: Bias and Variance',
    youtubeId: 'EuBBz3bI-aA',
    startSeconds: 150,
    timestampLabel: '02:30',
    highlightNote: 'Bản chất của High Bias (Underfitting) vs High Variance (Overfitting) và cách Cross-Validation kiểm định hiệu năng mô hình.'
  },
  '§1.6': {
    sectionId: '§1.6',
    topic: 'Regularization: Ridge (L2) vs Lasso (L1) và Tính chất Sparsity',
    channel: 'StatQuest with Josh Starmer',
    title: 'Regularization Part 3: Ridge vs Lasso',
    youtubeId: 'NGf0voTMlcs',
    startSeconds: 120,
    timestampLabel: '02:00',
    highlightNote: 'Vì sao Lasso (L1) triệt tiêu trọng số về chính xác bằng 0 tạo tính thưa (Sparsity) để chọn đặc trưng, trong khi Ridge (L2) chỉ co nhỏ đều.'
  },
  '§1.7': {
    sectionId: '§1.7',
    topic: 'Đánh giá mô hình: Precision, Recall, F1, ROC và PR Curve',
    channel: 'StatQuest with Josh Starmer',
    title: 'ROC and AUC, Clearly Explained!',
    youtubeId: '4jRBRDbJemM',
    startSeconds: 205,
    timestampLabel: '03:25',
    highlightNote: 'Giải thích Confusion Matrix, độ nhạy (Recall), độ đặc hiệu và cách vẽ đường cong ROC-AUC so với PR-AUC trên dữ liệu lệch.'
  },
  '§1.8': {
    sectionId: '§1.8',
    topic: 'K-Means Clustering & Silhouette Score',
    channel: 'StatQuest with Josh Starmer',
    title: 'StatQuest: K-means clustering',
    youtubeId: '4b5d3muPQmA',
    startSeconds: 165,
    timestampLabel: '02:45',
    highlightNote: 'Các bước hội tụ của K-Means và cách dùng Silhouette Score để đánh giá chất lượng phân cụm.'
  },
  '§1.9': {
    sectionId: '§1.9',
    topic: 'Xử lý mất cân bằng lớp & Thuật toán SMOTE',
    channel: 'Data Science Dojo',
    title: 'SMOTE (Synthetic Minority Over-sampling Technique) Explained',
    youtubeId: 'U3X98xZ4_no',
    startSeconds: 115,
    timestampLabel: '01:55',
    highlightNote: 'Giải thích trực quan cơ chế nội suy sinh mẫu nhân tạo mới của SMOTE thay vì sao chép thô sơ.'
  },
  '§1.10': {
    sectionId: '§1.10',
    topic: 'Quy tắc NumPy Broadcasting và Xử lý chiều Ma trận',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Broadcasting in Python',
    youtubeId: 'sca5rQ9x1cA',
    startSeconds: 60,
    timestampLabel: '01:00',
    highlightNote: 'Giáo sư Andrew Ng giải thích quy tắc tương thích chiều và cơ chế Broadcasting trong NumPy / Deep Learning.'
  },
  '§2.1': {
    sectionId: '§2.1',
    topic: 'Mạng Nơ-ron Nhân tạo & Vì sao cần Tính Phi Tuyến',
    channel: '3Blue1Brown',
    title: 'But what is a neural network? | Chapter 1, Deep learning',
    youtubeId: 'aircAruvnKk',
    startSeconds: 330,
    timestampLabel: '05:30',
    highlightNote: 'Hình ảnh hóa trực quan tuyệt đẹp về cách các tầng neuron và hàm kích hoạt trích xuất biểu diễn phi tuyến.'
  },
  '§2.2': {
    sectionId: '§2.2',
    topic: 'Các hàm kích hoạt: ReLU, Sigmoid, Softmax, GELU',
    channel: 'StatQuest with Josh Starmer',
    title: 'The Essential Main Ideas of Neural Networks & Activations',
    youtubeId: 'CqOfi41LfDw',
    startSeconds: 180,
    timestampLabel: '03:00',
    highlightNote: 'So sánh ưu nhược điểm của ReLU, Sigmoid, Tanh và hiện tượng Dying ReLU / Vanishing Gradient.'
  },
  '§2.3': {
    sectionId: '§2.3',
    topic: 'Lan truyền ngược (Backprop) & PyTorch Training Loop',
    channel: 'Andrej Karpathy',
    title: 'The spelled-out intro to neural networks and backpropagation: micrograd',
    youtubeId: 'VMj-3S1tku0',
    startSeconds: 2700,
    timestampLabel: '45:00',
    highlightNote: 'Andrej Karpathy (cựu giám đốc Tesla AI) code trực tiếp forward, zero_grad, loss.backward và optimizer.step từ đầu.'
  },
  '§2.4': {
    sectionId: '§2.4',
    topic: 'Hàm Loss: Cross-Entropy & BCEWithLogits',
    channel: 'StatQuest with Josh Starmer',
    title: 'Neural Networks Part 7: Cross Entropy',
    youtubeId: '6ArSys5qHAU',
    startSeconds: 140,
    timestampLabel: '02:20',
    highlightNote: 'Bản chất của Cross-Entropy Loss và lý do PyTorch tích hợp sẵn Softmax vào CrossEntropyLoss.'
  },
  '§2.5': {
    sectionId: '§2.5',
    topic: 'Thuật toán Tối ưu hóa: SGD, Momentum và Adam',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Adam Optimization Algorithm',
    youtubeId: 'JXQT_vxqwIs',
    startSeconds: 105,
    timestampLabel: '01:45',
    highlightNote: 'Công thức toán học kết hợp Momentum và RMSProp với hiệu chỉnh độ chệch (Bias correction) trong Adam.'
  },
  '§2.6': {
    sectionId: '§2.6',
    topic: 'Learning Rate Scheduling & Warmup cho Transformer',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Learning Rate Decay',
    youtubeId: 'QzulmoOg2JE',
    startSeconds: 60,
    timestampLabel: '01:00',
    highlightNote: 'Các chiến lược giảm tốc độ học (Decay, Cosine Annealing) và vai trò của Warmup để tránh phân kỳ đầu train.'
  },
  '§2.7': {
    sectionId: '§2.7',
    topic: 'Khởi tạo Trọng số: He (Kaiming) vs Xavier vs Lỗi Zeros',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Weight Initialization for Deep Networks',
    youtubeId: 's2coXdufOzE',
    startSeconds: 120,
    timestampLabel: '02:00',
    highlightNote: 'Vì sao khởi tạo Zeros phá vỡ tính đối xứng và cách He init giữ phương sai ổn định cho ReLU.'
  },
  '§2.8': {
    sectionId: '§2.8',
    topic: 'Batch Normalization vs Layer Normalization',
    channel: 'StatQuest with Josh Starmer',
    title: 'Batch Normalization, Clearly Explained!!!',
    youtubeId: 'YFwyHcJ8je8',
    startSeconds: 190,
    timestampLabel: '03:10',
    highlightNote: 'Cách BatchNorm chuẩn hóa mini-batch, vị trí đặt trước ReLU, và tại sao Transformer chuyển sang LayerNorm.'
  },
  '§2.9': {
    sectionId: '§2.9',
    topic: 'Dropout: Cơ chế Inverted Dropout và Tắt khi Test',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Understanding Dropout',
    youtubeId: 'ARq74QuavAo',
    startSeconds: 80,
    timestampLabel: '01:20',
    highlightNote: 'Cách Dropout ngẫu nhiên tắt neuron để chống overfit và lưu ý tắt Dropout khi inference.'
  },
  '§2.10': {
    sectionId: '§2.10',
    topic: 'Vanishing Gradient, ResNet Solution & Early Stopping',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Vanishing / Exploding Gradients',
    youtubeId: 'qhXZsFVxGKo',
    startSeconds: 90,
    timestampLabel: '01:30',
    highlightNote: 'Nguyên nhân triệt tiêu gradient ở mạng sâu và các giải pháp cứu cánh trong kiến trúc hiện đại.'
  },
  '§3.1': {
    sectionId: '§3.1',
    topic: 'Convolution 2D: Công thức Tính Kích thước Output & Padding',
    channel: '3Blue1Brown',
    title: 'Convolutions | Chapter 3, Deep learning',
    youtubeId: 'KuXjwB4LzSA',
    startSeconds: 240,
    timestampLabel: '04:00',
    highlightNote: 'Mô phỏng phép trượt filter, các chế độ Padding (Same/Valid), Stride và công thức kích thước đầu ra chính xác.'
  },
  '§3.2': {
    sectionId: '§3.2',
    topic: 'Pooling Layers & Global Average Pooling',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Pooling Layers in CNNs',
    youtubeId: '8oOgPUO-TBY',
    startSeconds: 75,
    timestampLabel: '01:15',
    highlightNote: 'Max pooling, Average pooling và cách Global Average Pooling thay thế lớp FC để giảm hàng triệu tham số.'
  },
  '§3.3': {
    sectionId: '§3.3',
    topic: 'Các kiến trúc CNN kinh điển: VGG, ResNet, EfficientNet',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Why ResNets Work',
    youtubeId: 'GWt6Fu05voI',
    startSeconds: 110,
    timestampLabel: '01:50',
    highlightNote: 'Phân tích bản chất đường dẫn tắt Residual Connection F(x) + x giải quyết vấn đề thoái hóa mô hình.'
  },
  '§3.4': {
    sectionId: '§3.4',
    topic: 'Skip Connection: ResNet (ADD) vs U-Net (CONCAT)',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'U-Net Architecture for Image Segmentation',
    youtubeId: 'oLvmLJkmXuc',
    startSeconds: 130,
    timestampLabel: '02:10',
    highlightNote: 'So sánh cốt lõi: U-Net ghép nối kênh (CONCAT) giữ chi tiết không gian, ResNet cộng phần tử (ADD).'
  },
  '§3.5': {
    sectionId: '§3.5',
    topic: 'Vision Transformer (ViT): Patches, [CLS] Token & No-Conv',
    channel: 'Yannic Kilcher',
    title: 'An Image is Worth 16x16 Words: Transformers for Image Recognition',
    youtubeId: 'TrdevFK_am4',
    startSeconds: 320,
    timestampLabel: '05:20',
    highlightNote: 'Yannic Kilcher giải thích chi tiết bài báo ViT: cắt ảnh thành patches, token [CLS], positional embedding và không dùng Conv.'
  },
  '§3.6': {
    sectionId: '§3.6',
    topic: 'Object Detection: IoU, NMS, mAP, YOLO vs Faster R-CNN',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Intersection Over Union (IoU) & Non-Max Suppression',
    youtubeId: '9s_FpMpdYW8',
    startSeconds: 90,
    timestampLabel: '01:30',
    highlightNote: 'Công thức tính IoU = Giao / Hợp và thuật toán NMS loại bỏ các hộp bounding box trùng lặp.'
  },
  '§3.7': {
    sectionId: '§3.7',
    topic: 'Phân vùng ảnh: Semantic Segmentation vs Instance Segmentation',
    channel: 'Stanford University School of Engineering',
    title: 'CS231n: Lecture 11 | Detection and Segmentation',
    youtubeId: 'nDPWywWRIRo',
    startSeconds: 360,
    timestampLabel: '06:00',
    highlightNote: 'Phân biệt gán nhãn từng pixel (Semantic) với tách biệt từng cá thể riêng biệt (Instance).'
  },
  '§3.8': {
    sectionId: '§3.8',
    topic: 'Mô hình Sinh: Diffusion Models vs GANs',
    channel: 'Computerphile',
    title: 'Diffusion Models | How AI Image Generators Work',
    youtubeId: '1CIpzeNxIhU',
    startSeconds: 150,
    timestampLabel: '02:30',
    highlightNote: 'Nguyên lý khử nhiễu từng bước của Diffusion Models (Stable Diffusion) và vì sao nó vượt trội GAN.'
  },
  '§3.9': {
    sectionId: '§3.9',
    topic: 'Data Augmentation & Chiến lược Transfer Learning',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Transfer Learning in Deep Learning',
    youtubeId: 'yofjFQddwHE',
    startSeconds: 100,
    timestampLabel: '01:40',
    highlightNote: 'Quy tắc đóng băng backbone khi dữ liệu ít và chỉ tinh chỉnh (fine-tune) tầng phân loại cuối.'
  },
  '§4.1': {
    sectionId: '§4.1',
    topic: 'NLP Pipeline: Tokenization, Normalization, Stemming & Lemmatization',
    channel: 'Stanford Online (CS224N)',
    title: 'CS224N: Natural Language Processing with Deep Learning',
    youtubeId: 'rmVRLeJRkl4',
    startSeconds: 180,
    timestampLabel: '03:00',
    highlightNote: 'Trình tự chuẩn các bước tiền xử lý văn bản trong xử lý ngôn ngữ tự nhiên hiện đại.'
  },
  '§4.2': {
    sectionId: '§4.2',
    topic: 'Biểu diễn từ: Word2Vec, FastText (Subwords) và BERT',
    channel: '3Blue1Brown',
    title: 'Word embeddings | Chapter 2, Deep learning',
    youtubeId: 'gQddtTdmG_8',
    startSeconds: 360,
    timestampLabel: '06:00',
    highlightNote: 'Trực quan hóa không gian hình học vector ngữ nghĩa và cơ chế bắt quan hệ giữa các từ.'
  },
  '§4.3': {
    sectionId: '§4.3',
    topic: 'Cosine Similarity: Công thức và Ứng dụng So khớp Embedding',
    channel: 'StatQuest with Josh Starmer',
    title: 'Cosine Similarity, Clearly Explained!!!',
    youtubeId: 'e9U0QAFbfLI',
    startSeconds: 90,
    timestampLabel: '01:30',
    highlightNote: 'Vì sao Cosine Similarity là thước đo chuẩn để so sánh embedding thay vì khoảng cách Euclid.'
  },
  '§4.4': {
    sectionId: '§4.4',
    topic: 'Mạng hồi quy: RNN, LSTM (Cell State & 3 Cổng) và GRU',
    channel: 'StatQuest with Josh Starmer',
    title: 'Long Short-Term Memory (LSTM), Clearly Explained',
    youtubeId: 'YCzL96nL7j0',
    startSeconds: 240,
    timestampLabel: '04:00',
    highlightNote: 'Giải thích hoạt động của Cell State, Cổng Quên (Forget Gate), Cổng Nhập (Input Gate) và Cổng Xuất.'
  },
  '§4.5': {
    sectionId: '§4.5',
    topic: 'Kiến trúc Transformer: Attention (Q, K, V) & Positional Encoding',
    channel: '3Blue1Brown',
    title: 'Attention in transformers, visually explained | Chapter 6',
    youtubeId: 'eMlx5fFNoYc',
    startSeconds: 420,
    timestampLabel: '07:00',
    highlightNote: 'Trực quan hóa tuyệt đẹp cơ chế Scaled Dot-Product Attention, ma trận Q/K/V và vì sao phải chia cho sqrt(d_k).'
  },
  '§4.6': {
    sectionId: '§4.6',
    topic: 'So sánh toàn diện: BERT (Encoder 2 chiều) vs GPT (Decoder Autoregressive)',
    channel: 'Andrej Karpathy',
    title: 'State of GPT | Microsoft Build 2023',
    youtubeId: 'bZQun8Y4L2A',
    startSeconds: 300,
    timestampLabel: '05:00',
    highlightNote: 'Andrej Karpathy phân tích sự khác nhau giữa kiến trúc hiểu (BERT) và kiến trúc sinh tự hồi quy (GPT).'
  },
  '§4.7': {
    sectionId: '§4.7',
    topic: 'Độ đo NLP: BLEU (Dịch máy), ROUGE (Tóm tắt) & Perplexity',
    channel: 'DeepLearning.AI (Andrew Ng)',
    title: 'Bleu Score (C5W3L09)',
    youtubeId: 'DejHQYAGb7Q',
    startSeconds: 120,
    timestampLabel: '02:00',
    highlightNote: 'Công thức tính modified n-gram precision và hệ số phạt câu ngắn Brevity Penalty trong BLEU.'
  },
  '§5.1': {
    sectionId: '§5.1',
    topic: 'Định lý Bayes & Ngụy biện Tỉ lệ Cơ sở (Base-Rate Fallacy y tế)',
    channel: '3Blue1Brown',
    title: 'Bayes theorem, the geometry of changing beliefs',
    youtubeId: 'HZGCoVF3YvM',
    startSeconds: 180,
    timestampLabel: '03:00',
    highlightNote: 'Bài toán xét nghiệm bệnh hiếm: vì sao test 90% chính xác nhưng người dương tính vẫn chỉ có 15% xác suất mắc bệnh.'
  },
  '§5.2': {
    sectionId: '§5.2',
    topic: 'Các phân phối xác suất: Bernoulli, Poisson & Định lý Giới hạn Trung tâm (CLT)',
    channel: '3Blue1Brown',
    title: 'Central limit theorem | Chapter 4, Essence of probability',
    youtubeId: 'zeJD6dqJ5lo',
    startSeconds: 210,
    timestampLabel: '03:30',
    highlightNote: 'Vì sao tổng của các biến ngẫu nhiên độc lập luôn hội tụ về phân phối chuẩn Gaussian.'
  },
  '§5.3': {
    sectionId: '§5.3',
    topic: 'Kỳ vọng, Phương sai & Tính chất Var(aX + b) = a^2 Var(X)',
    channel: 'StatQuest with Josh Starmer',
    title: 'Variance and Standard Deviation, Clearly Explained',
    youtubeId: 'SzZ6GpcfoQY',
    startSeconds: 120,
    timestampLabel: '02:00',
    highlightNote: 'Bản chất phương sai và giải thích vì sao hằng số cộng vào không đổi phương sai nhưng nhân hằng số làm phương sai tăng gấp a^2.'
  },
  '§5.4': {
    sectionId: '§5.4',
    topic: 'Ước lượng Tham số: MLE vs MAP (Mối liên hệ với Regularization)',
    channel: 'StatQuest with Josh Starmer',
    title: 'Maximum Likelihood, clearly explained!!!',
    youtubeId: 'XepXtl9YKwc',
    startSeconds: 150,
    timestampLabel: '02:30',
    highlightNote: 'Cách MLE tìm tham số tối đa hóa dữ liệu và MAP tích hợp phân phối tiên nghiệm Prior.'
  },
  '§5.5': {
    sectionId: '§5.5',
    topic: 'Kiểm định Giả thuyết & Bản chất thực sự của p-value',
    channel: 'StatQuest with Josh Starmer',
    title: 'p-values: What they are and how to interpret them',
    youtubeId: 'vemZtEM63GY',
    startSeconds: 120,
    timestampLabel: '02:00',
    highlightNote: 'Ý nghĩa chính xác của p-value: P(dữ liệu cực đoan | H0 đúng), giải thích hiểu lầm phổ biến nhất.'
  },
  '§5.6': {
    sectionId: '§5.6',
    topic: 'Tương quan vs Nhân quả (Confounders) & Lấy mẫu Phân tầng',
    channel: 'Khan Academy',
    title: 'Correlation and Causality | Statistical Studies',
    youtubeId: 'ROpbdO-gRUo',
    startSeconds: 60,
    timestampLabel: '01:00',
    highlightNote: 'Yếu tố nhiễu ẩn (Confounding Variable) và kỹ thuật Stratified Sampling trên dữ liệu lệch.'
  },
  '§7.1': {
    sectionId: '§7.1',
    topic: 'Tác vụ OLP 2025: Nhận diện Ngôn ngữ Ký hiệu Video (Spatio-Temporal & CTC)',
    channel: 'AI Vietnam',
    title: 'Sign Language Recognition Tutorial: CNN + Transformer Sequence Modeling',
    youtubeId: 'vT1JzLTH4G4',
    startSeconds: 180,
    timestampLabel: '03:00',
    highlightNote: 'Khung giải pháp 5 bước xử lý chuỗi video, tách người (Person-independent split) và CTC / Temporal Attention.'
  },
  '§7.2': {
    sectionId: '§7.2',
    topic: 'Tác vụ OLP 2025: Dịch máy Thương mại điện tử Hoa-Việt & SacreBLEU',
    channel: 'AI Vietnam',
    title: 'Machine Translation with Transformers and Subword BPE',
    youtubeId: 'TQQlZhbC5ps',
    startSeconds: 240,
    timestampLabel: '04:00',
    highlightNote: 'Tiền xử lý BPE song ngữ, bảo vệ mã số/tiền tệ và tính toán điểm SacreBLEU.'
  },
  '§7.3': {
    sectionId: '§7.3',
    topic: 'Tác vụ OLP 2026: Object Detection Nông nghiệp trên Mobile (YOLOv8/v11 Nano)',
    channel: 'Roboflow',
    title: 'YOLOv8: How to Train for Object Detection on a Custom Dataset',
    youtubeId: 'wuZtUMEiKWY',
    startSeconds: 120,
    timestampLabel: '02:00',
    highlightNote: 'Triển khai mô hình 1-stage siêu nhẹ cho phát hiện vết bệnh và tối ưu hóa thời gian thực.'
  },
  '§7.4': {
    sectionId: '§7.4',
    topic: 'Tác vụ OLP 2026: Tabular Churn Prediction & XAI với SHAP Values',
    channel: 'StatQuest with Josh Starmer',
    title: 'SHAP Values (SHapley Additive exPlanations), Clearly Explained!!!',
    youtubeId: 'MQ6fFDwjuco',
    startSeconds: 180,
    timestampLabel: '03:00',
    highlightNote: 'Cách tính SHAP Values để giải thích quyết định của mô hình Gradient Boosting (LightGBM/XGBoost).'
  }
};

// Ham lay video theo Section ID (vd: "§3.1") hoac fallback
export function getVideoForSection(sectionId: string): VideoResource | undefined {
  return VIDEO_RESOURCES[sectionId];
}

// Ham trich xuat section ID tu chuoi explanation (vd: "→ Xem §3.1" -> "§3.1")
export function extractSectionRef(text: string): string | undefined {
  const match = text.match(/§\d+\.\d+/);
  return match ? match[0] : undefined;
}
