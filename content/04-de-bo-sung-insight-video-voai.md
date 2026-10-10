# ĐỀ THI 04: BỔ SUNG CHUYÊN SÂU INSIGHT VIDEO VOAI 2026
## 20 Câu Trắc Nghiệm Kỹ Thuật Chuyên Sâu (Module A) & 4 Bài Tự Luận Thực Chiến (Module C)

> **Nguồn gốc học thuật:** Đề thi tổng hợp các tình huống bài toán Deep Learning nâng cao mô phỏng kinh nghiệm thực chiến từ chuyên đề VOAI.
> **Lưu ý khảo thí:** Các số liệu định lượng (Macro-F1 ~84% lên 97.1%, 41 lỗi giảm còn 8 lỗi) là tình huống nghiên cứu ca điển hình giả định (unvalidated case study) để luyện tư duy tối ưu.

---

### Câu 01 [OLP04-Q01] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-01] [UNVALIDATED CASE STUDY] Xét tình huống nghiên cứu mô phỏng về bài toán ' Kẻ mạo danh ' (phân biệt ảnh người thật vs ảnh do AI Diffusion/GAN sinh ra): Giả định một mô hình phân loại sử dụng kiến trúc EfficientNet-B2 đã được tiền huấn luyện trên ImageNet. Trong kịch bản nghiên cứu này, thí sinh đóng băng toàn bộ trọng số Backbone (Frozen Backbone) và chỉ huấn luyện tầng phân loại (Classification Head), thu được Macro-F1 ~84% (41 mẫu lỗi trên tập kiểm thử Fold 0). Khi chuyển sang mở toàn bộ trọng số để Fine-Tuning (Full Fine-Tuning), kết quả thực nghiệm mô phỏng tăng vọt lên 97.1% (chỉ còn 8 lỗi). Dưới góc độ khoa học máy tính và thị giác máy tính, đâu là nguyên nhân bản chất sâu xa nhất giải thích cho hiện tượng này?

- **A.** ImageNet backbone chỉ nhận diện đặc trưng ngữ nghĩa bậc cao, trong khi tín hiệu Real vs Fake nằm ở nhiễu vi mô tần số cao bị triệt tiêu trong pre-training
- **B.** ImageNet backbone có 1000 lớp gây phương sai cực lớn ở classifier head, kích hoạt hiện tượng bùng nổ gradient khi chỉ đóng băng backbone và train head
- **C.** Quá trình đóng băng backbone làm vô hiệu hóa running stats của Batch Normalization, dẫn tới tính sai độ lệch chuẩn đặc trưng trên toàn bộ ảnh đầu vào
- **D.** Depthwise Separable Convolution làm mất hoàn toàn không gian màu RGB, đòi hỏi mở toàn bộ các tầng để tái lập ma trận biểu diễn đặc trưng không gian HSV

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Tưởng tượng ImageNet như một họa sĩ chuyên vẽ tranh chân dung. Ông ấy chỉ để ý nhìn xem người trong ảnh có đủ 2 mắt, 1 mũi, 1 miệng cân đối hay không. Cả ảnh người thật lẫn ảnh do AI vẽ đều có đủ mắt, mũi, miệng đẹp lung linh, nên người họa sĩ đó (khi bị đóng băng) bảo: ' Hai ảnh này y hệt nhau, tôi chịu không phân biệt nổi!' Nhưng khi mở khóa cho họa sĩ học tiếp (Full Fine-Tuning), ông ấy cầm kính lúp lên soi vào từng hạt mực siêu nhỏ (nhiễu vi mô tần số cao). Lúc này ông ấy mới phát hiện ra: ' À, da của ảnh AI mịn bất thường và có những vân kẻ sọc li ti của thuật toán tạo ảnh!'. Nhờ vậy độ chính xác nhảy vọt từ 84% lên 97.1%!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Hàm trích xuất đặc trưng của ImageNet backbone: $\Phi(I; \Theta_{\text{ImageNet}})$. Mục tiêu của ImageNet là bất biến với nhiễu (noise-invariant) và nhạy với hình thái vật thể (shape-sensitive): $\frac{\partial \mathcal{L}_{\text{ImageNet}}}{\partial (\text{High-Freq Noise})} \approx 0$.
- Ngược lại, ảnh sinh bởi GAN hoặc Diffusion Models để lại vết hằn ở phần dư vi mô: $R(I) = I - \text{GaussianFilter}(I, \sigma = 1.2)$. Phần dư $R(I)$ mang thông tin về Artifacts của phép nội suy điểm ảnh (Transposed Conv / Checkerboard pattern) và bước nhảy khối nén JPEG ($8 \times 8$ grid jump).
- Khi đóng băng $\Theta_{\text{ImageNet}}$, mạng chỉ nhận các đặc trưng ngữ nghĩa bậc cao ở tầng cuối $f \in \mathbb{R}^{d}$, vốn đã bị gạt bỏ hoàn toàn $R(I)$. Chỉ khi mở toàn bộ $\Theta$, gradient $\frac{\partial \mathcal{L}_{\text{Fake}}}{\partial \Theta}$ mới cập nhật lại các bộ lọc tích chập ở các tầng nông ($Conv_1, Conv_2$) để giữ lại tần số cao.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy B: Sai. Số lượng lớp của ImageNet không gây nổ gradient ở Classification Head mới khởi tạo nếu dùng learning rate chuẩn.
- Bẫy C: Sai. Depthwise Separable Conv không làm mất thông tin màu sắc (nó tách phép tích chập theo chiều sâu không gian và tích chập điểm $1 \times 1$ theo kênh), và không liên quan đến không gian HSV.
- Bẫy D: Sai. Batch Normalization trong inference sử dụng running mean/var đã đóng băng từ trước, không phải là nguyên nhân làm mất tín hiệu Real/Fake.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên nhấn mạnh: Khi thi contest các bài toán liên quan đến Kiểm định chất lượng ảnh, Nhận diện can thiệp (Steganography / Tampering / DeepFake), TUYỆT ĐỐI KHÔNG DÙNG FROZEN BACKBONE. Phải dùng Full Fine-Tuning với learning rate nhỏ ($\eta = 10^{-4}$ cho Head, $10^{-5}$ cho Backbone) kết hợp kỹ thuật cắt tâm 60% khuôn mặt (center60) để giữ trọn vẹn độ phân giải cục bộ.

---

### Câu 02 [OLP04-Q02] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-02] Trong video phân tích bài toán Document Visual Question Answering (DocViVQA), xét câu hỏi trắc nghiệm sau trên ảnh một bảng tài liệu hành chính: ' Trong bảng 1, hãy chọn dòng in đậm nằm giữa Phòng ban ' Vận hành ' và Phòng ban ' Kế toán ' có Định biên là '30', sau đó đọc giá trị ở cột ' Hiện có '.' Một kỹ sư sử dụng pipeline OCR tiên tiến nhất (Tesseract + PhoBERT) nhưng mô hình NLP liên tục trả lời sai hoặc dự đoán ngẫu nhiên giữa 2 dòng ứng viên. Đâu là hạn chế cốt tử của pipeline NLP thuần túy dựa trên OCR mà giảng viên đã phân tích?

- **A.** PhoBERT giới hạn ngữ cảnh tối đa 256 tokens (Sequence Length), khiến các dòng ở nửa sau bảng tài liệu bị cắt cụt và mất quan hệ liên kết
- **B.** Khoảng cách Levenshtein trong khớp mờ (Fuzzy String Matching) không thể so sánh kiểu dáng phông chữ giữa các dòng văn bản có vị trí đối xứng
- **C.** Chỉ số ANLS quy định kết quả trắc nghiệm phải là số nguyên (Integer Form), trong khi đầu ra OCR trả về dạng chuỗi số thực dấu phẩy động
- **D.** OCR chỉ trích xuất văn bản và bounding box, bỏ sót thuộc tính thị giác (độ dày nét in đậm, độ nghiêng, màu mực) cần thiết để phân định thực thể

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Một người khiếm thị nhờ một người bạn đọc văn bản hộ. Người bạn đọc lên thành tiếng: ' Dòng một: Kế hoạch, định biên 30, hiện có 25. Dòng hai: Báo cáo, định biên 30, hiện có 18.' Sau đó người khiếm thị hỏi: ' Thế dòng nào được in chữ đậm bằng mực đậm?' Người bạn chịu chết không trả lời được, vì trong lời nói (text) chỉ có chữ, không có hình ảnh nét mực đậm hay nhạt! OCR truyền thống cũng như vậy, nó chỉ đọc ra chữ mà vứt mất hình ảnh kiểu chữ.

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Đầu ra của mô-đun OCR truyền thống: $\mathcal{O} = \{ (t_i, b_i) \}_{i=1}^{N}, t_i \in \Sigma^*, b_i = [x_1, y_1, x_2, y_2] \in \mathbb{R}^4$.
- Cả 2 dòng ứng viên đều thỏa mãn biểu thức logic văn bản: $\text{Cand}_1: (\text{text}='\text{Dự án A}', \text{định biên}=30)$ và $\text{Cand}_2: (\text{text}='\text{Dự án B}', \text{định biên}=30)$. Cả hai đều hợp lệ theo NLP thuần túy!
- Tín hiệu quyết định nằm ở phân bố mật độ pixel mực trên nét chữ (Stroke Pixel Density): $\rho_{\text{bold}} = \frac{1}{|b_i|} \sum_{(x, y) \in b_i} \mathbb{I}(I(x, y) < \tau_{\text{ink}})$. Dòng in đậm có $\rho_{\text{bold}} > 35\%$, trong khi dòng thường chỉ $< 18\%$. Một mô hình NLP thuần túy không tiếp cận được ma trận điểm ảnh $I(x, y)$ nên không thể giải quyết được bài toán.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Sai. Dù có dùng mô hình hỗ trợ 100k tokens (như Longformer hay Gemini), nếu đầu vào chỉ là text từ OCR thì vẫn thiếu hoàn toàn thông tin ' in đậm '.
- Bẫy B: Sai. Fuzzy string matching so khớp chuỗi ký tự, nó hoàn toàn không biết chữ đó có in đậm hay không.
- Bẫy C: Sai. ANLS đo độ tương đồng Levenshtein chuẩn hóa giữa 2 chuỗi bất kỳ, không phân biệt số nguyên hay chuỗi float.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên hướng dẫn giải pháp kết hợp SOTA trong phòng thi: Sau khi OCR định vị được $b_i$, cắt ô ảnh (crop patch) đó ra và đưa qua một Lightweight CNN Classifier hoặc tính nhanh độ dày nét (Stroke Width Transform / Pixel Density) để gán thuộc tính `is_bold = True/False` cho từng token trước khi đưa vào mô hình ngôn ngữ đa phương thức (như LayoutLMv3 hoặc Donut).

---

### Câu 03 [OLP04-Q03] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-03] Trong bài giảng về Trích xuất cấu trúc bảng (Table Structure Recognition - TSR), giảng viên trình bày thuật toán hình thái học (Morphological Operations) kết hợp phép chiếu tích lũy để phục hồi lưới logic. Khi phân tích các dải pixel liên thông theo chiều ngang/dọc, quy tắc phân loại kích thước nào sau đây được giảng viên sử dụng để phân biệt dải mỏng, dải dày và xử lý khe nứt scan?

- **A.** Dải mỏng (< 3px) coi là nhiễu hạt bị xóa bỏ; Dải trung bình (3-20px) lấy tâm đơn; Dải dày (> 20px) giữ cả 2 biên để biểu diễn ô gộp đa dòng
- **B.** Dải mỏng (< 5px) giữ cả 2 biên để biểu diễn viền đôi; Dải dày (≥ 5px) xóa bỏ vì coi là khối văn bản multiline gây nhiễu cấu trúc lưới
- **C.** Dải mỏng (< 9px) lấy toạ độ tâm làm cạnh đơn; Dải dày (≥ 9px) giữ cả 2 biên biểu diễn viền đôi; Khe hở nhỏ (≤ 3px) nối liền vá đứt đoạn scan
- **D.** Mọi dải pixel đều được chuyển thành đường thẳng đơn qua biến đổi Hough Transform bất kể độ dày và khoảng cách khe hở giữa các ô

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Khi scan một bảng tài liệu, mực in có thể bị nhòe thành vệt dày hoặc bị đứt đoạn gãy nét. Quy tắc của giảng viên giống như một thợ sửa lưới: Nếu vết kẻ mảnh (< 9px), lấy đúng đường tim giữa; nếu vết kẻ quá to bản (≥ 9px), giữ cả mép trên và mép dưới để không làm mất đường viền kép; còn nếu đường kẻ bị thủng một lỗ nhỏ li ti (≤ 3px), thợ liền tay vá liền lại để thành đường kẻ liên tục!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Mặt nạ đường kẻ ngang và dọc: $M_h = \text{Dilate}(\text{Erode}(I, K_h), K_h)$ với $K_h = 1 \times W_{line}$, $M_v = \text{Dilate}(\text{Erode}(I, K_v), K_v)$ với $K_v = H_{line} \times 1$.
- Phép chiếu tích lũy: $P_v(x) = \sum_{y} M_v(x, y); P_h(y) = \sum_{x} M_h(x, y)$.
- Phân đoạn liên thông (connected runs): Cho một đoạn liên tục $[x_{\text{start}}, x_{\text{end}}]$ có chiều rộng $w = x_{\text{end}} - x_{\text{start}} + 1$:
  + Nếu $w < 9$: tạo 1 cạnh tại $x_{\text{mid}} = \frac{x_{\text{start}} + x_{\text{end}}}{2}$.
  + Nếu $w \ge 9$: tạo 2 cạnh tại $x_{\text{start}}$ và $x_{\text{end}}$.
  + Giữa 2 đoạn nếu gap $g = x_{\text{start}}^{(k+1)} - x_{\text{end}}^{(k)} \le 3$: hợp nhất thành 1 đoạn duy nhất.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Sai ngưỡng (ngưỡng chuẩn trong bài giảng là 9px và 3px, không phải 20px).
- Bẫy B: Sai thuật toán. Hough Transform chỉ tìm đường thẳng vô hạn, không xử lý được cấu trúc bảng ô lưới đứt đoạn cục bộ và viền kép.
- Bẫy D: Đảo ngược vô lý nguyên tắc (dải mỏng giữ 2 biên là hoàn toàn sai hình học).

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên bổ sung thêm một ' edge case ' cứu mạng trong contest: Outer Border Fallback. Nếu cạnh ngoài cùng tìm được cách mép bounding box của bảng lớn hơn 10px, thuật toán phải tự động fallback lấy viền của bounding box làm đường bao bảng, nếu không điểm TEDS sẽ sụt giảm trên 30% do mất hàng/cột biên!

---

### Câu 04 [OLP04-Q04] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-04] Trong đề thi chính thức VOAI 2025 Tác vụ 2 (Nhận diện ngôn ngữ ký hiệu từ video clip), script nộp bài ' main.py ' bị giới hạn thời gian chạy nghiệm thu tối đa là 20 phút trên máy chấm ban tổ chức (khoảng 500-1000 video test). Tại sao phương pháp sử dụng Video 3D-CNN (như I3D, SlowFast, Video ResNet) hầu như chắc chắn bị dính lỗi Time Limit Exceeded (TLE), trong khi phương pháp trích xuất MediaPipe Keypoints + ST-GCN lại hoàn thành toàn bộ test set chỉ trong dưới 90 giây?

- **A.** Video tập test bị mã hóa theo chuẩn AV1 độc quyền khiến OpenCV không thể giải mã các frame hình ảnh thô trên môi trường chấm thi
- **B.** 3D-CNN đòi hỏi giấy phép phần mềm CUDA chuyên dụng của ban tổ chức mới có thể kích hoạt cơ chế tăng tốc tính toán trên phần cứng GPU
- **C.** 3D-CNN tính tích chập trên toàn bộ tensor điểm ảnh thô (B, C, T, H, W) tốn hàng tỷ FLOPs; MediaPipe nén frame thành đồ thị xương siêu nhẹ cho ST-GCN
- **D.** Mô hình ST-GCN là mô hình phi tham số (Non-parametric) hoàn toàn không cần thực hiện phép lan truyền tiến qua các ma trận trọng số

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
3D-CNN giống như một người muốn nhận biết cử chỉ chào bằng cách tải toàn bộ cuốn phim nặng hàng Gigabyte về, soi từng điểm ảnh màu trên áo, trên tường, trên rèm cửa. Máy tính xử lý không kịp trong 20 phút và bị ban tổ chức bấm chuông đuổi về (TLE)! Trong khi đó, ST-GCN chỉ cần ghi nhớ đúng toạ độ các khớp ngón tay (như hình người que que). Một bức tranh que chỉ nặng vài chục con số, máy tính lướt qua trong 1 giây là xong 10 video!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Độ phức tạp tensor 3D-CNN: Đầu vào $X \in \mathbb{R}^{B \times 3 \times T \times 224 \times 224}$. Một lớp Conv3D với $C_{\text{in}}=64, C_{\text{out}}=128, K=(3, 3, 3)$ cần: $\text{FLOPs} = 2 \times T \times 224 \times 224 \times 64 \times 128 \times 27 \approx 1.48 \times 10^{11}$ FLOPs (148 GFLOPs) cho CHỈ MỘT LAYER!
- Độ phức tạp ST-GCN: Đầu vào chỉ là ma trận toạ độ khớp xương $X_{\text{pose}} \in \mathbb{R}^{B \times 3 \times T \times V}$ với $V = 42$ khớp (2 bàn tay). Một lớp Spatio-Temporal Graph Conv chỉ tốn: $\text{FLOPs} = 2 \times T \times V \times C_{\text{in}} \times C_{\text{out}} \times K_{\text{spatial}} \approx 2 \times 60 \times 42 \times 64 \times 128 \times 3 \approx 1.23 \times 10^8$ FLOPs (0.12 GFLOPs) — nhẹ hơn gấp 1.200 LẦN!

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Vô lý. Các framework PyTorch/Torchvision 3D-CNN đều là mã nguồn mở chạy tự do trên GPU NVIDIA.
- Bẫy B: Sai kiến thức. ST-GCN có hàng triệu tham số (trọng số của Spatial Graph Conv và Temporal Conv).
- Bẫy D: Sai. Tập dữ liệu cuộc thi được chuẩn hóa dạng MP4 định dạng H.264 tiêu chuẩn.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên chia sẻ ' Bí kíp cứu mạng ': Ở vòng contest, bạn phải tính nhẩm ngay số lượng video test nhân với thời gian xử lý 1 video. Nếu 1 video tốn 2 giây $\rightarrow 600 \times 2 = 1.200$s = 20 phút (sát nút bờ vực TLE). Bất kỳ phương pháp nào tốn quá 0.5s/video đều phải loại bỏ ngay, chuyển sang trích xuất Pose/Keypoint để đảm bảo an toàn tuyệt đối.

---

### Câu 05 [OLP04-Q05] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-05] Trong đề thi OLP AI Vòng Sơ loại SOLOAI (Tác vụ 1: Dịch máy Trung - Việt), ban tổ chức quy định: ' Nghiêm cấm sử dụng bất kỳ mô hình ngôn ngữ hoặc trọng số đã được huấn luyện trước (pretrained weights) cho tác vụ dịch máy '. Một đội thi quyết định huấn luyện mô hình Transformer Encoder-Decoder from scratch trên tập train 40.000 cặp câu. Khi tạo bộ tách từ (Tokenizer) Byte-Pair Encoding (BPE), đội này chọn kích thước từ vựng Vocab Size V = 64.000 (giống như các mô hình mBART lớn). Kết quả mô hình bị Overfitting nặng và điểm SacreBLEU trên Validation rớt thảm hại về dưới 4.0. Đâu là phân tích chính xác của giảng viên?

- **A.** Tiếng Trung không thể phân tách bằng thuật toán BPE mà bắt buộc phải mã hóa từng Hán tự đơn lẻ theo bảng mã Unicode chuẩn
- **B.** Tập train chỉ 40.000 cặp câu khiến Vocab 64.000 làm ma trận Embedding chiếm quá nhiều tham số và overfit; quy mô này cần thu gọn Vocab về ~8.000
- **C.** Hàm mất mát Cross-Entropy không thể hội tụ ổn định trên phần cứng GPU khi số lượng lớp đầu ra của tầng phân loại vượt quá 10.000 nhãn
- **D.** Chỉ số SacreBLEU chỉ tính toán được khi câu dịch của mô hình có độ dài lớn hơn 64 từ và không chứa các ký tự đặc biệt ngoài từ điển

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Giống như bạn mở một cuốn từ điển dày 64.000 từ để dạy một đứa trẻ mới học 40 bài tập đọc ngắn. Trong cuốn từ điển đó, có hàng chục nghìn từ chỉ xuất hiện đúng một lần trong suốt cả năm học. Đứa trẻ sẽ cố học vẹt những từ hiếm đó thay vì nắm vững các từ ngữ thông dụng hàng ngày. Khi đi thi, nó gặp câu mới là ú ớ ngay lập tức! Nếu thu gọn từ điển lại còn 8.000 từ thông dụng nhất, từ nào cũng được lặp đi lặp lại nhiều lần, đứa trẻ sẽ học cực kỳ vững và nhớ lâu.

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Số tham số ma trận Embedding hai đầu: $\Theta_{\text{emb}} = (V_{\text{src}} + V_{\text{tgt}}) \times d_{\text{model}}$. Với $V = 64.000, d_{\text{model}} = 512$: $\Theta_{\text{emb}} = (64.000 + 64.000) \times 512 = 65.536.000$ tham số (~65.5 triệu weights chỉ riêng cho bảng từ vựng!).
- Tổng số tokens trong 40.000 cặp câu: $40.000 \times 25 \approx 1.000.000$ tokens.
- Tỷ lệ dữ liệu trên tham số: $\frac{1.000.000 \text{ tokens}}{65.500.000 \text{ params}} \approx 0.015$ tokens/param — thiếu dữ liệu nghiêm trọng, dẫn đến ma trận nhúng bị thưa thớt (sparse gradients) và Overfitting hoàn toàn!
- Với $V = 8.000$: $\Theta_{\text{emb}} = 16.000 \times 512 \approx 8.19$ triệu tham số $\rightarrow$ mô hình cân đối hoàn hảo và hội tụ xuất sắc.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Sai. BPE và SentencePiece hoạt động rất tốt trên tiếng Trung ở cấp độ ký tự/subword.
- Bẫy C: Sai. Cross-Entropy trong NLP xử lý từ vựng 100k-250k bình thường (như trong LLaMA, GPT-4).
- Bẫy D: Sai. SacreBLEU đo trên độ dài bất kỳ, có cơ chế Brevity Penalty cho câu ngắn.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên lưu ý: Trong bài toán dịch máy không cho dùng pretrained weights, công thức vàng cho kích thước từ vựng BPE/SentencePiece là: $V \in [4.000, 10.000]$ cho data nhỏ (< 100k câu). Đi kèm đó là kiến trúc nhẹ: 4-6 layers, $d_{\text{model}}=256$ hoặc $512$, $d_{ff}=1024$ hoặc $2048$, Dropout $0.2-0.3$ và Label Smoothing $0.1$.

---

### Câu 06 [OLP04-Q06] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-06] Trong các cuộc thi Machine Learning dạng bảng (Tabular Contest), khi so sánh giữa LightGBM, XGBoost và CatBoost trên các bộ dữ liệu có nhiều biến phân loại (Categorical) và kích thước mẫu vừa/nhỏ, giảng viên đặc biệt đánh giá cao cơ chế ' Ordered Boosting ' của CatBoost. Cơ chế này giải quyết triệt để vấn đề gì mà các thuật toán GBDT truyền thống thường mắc phải?

- **A.** Triệt tiêu Prediction Shift và Target Leakage khi tính thống kê mục tiêu qua hoán vị ngẫu nhiên độc lập chỉ dùng các mẫu đứng trước
- **B.** Ngăn chặn hiện tượng cây quyết định bị tràn bộ nhớ đệm RAM khi độ sâu phân nhánh vượt quá 10 tầng thông qua việc cắt tỉa tự động
- **C.** Tự động đảo ngược thứ tự các cột đặc trưng để tạo ra ma trận tương quan trực giao giữa các biến phân loại và biến liên tục
- **D.** Chuyển đổi bài toán phân loại đa lớp phức tạp thành tập hợp các bài toán hồi quy đơn biến độc lập giải bằng Gradient Descent

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Hãy tưởng tượng bạn chấm điểm một học sinh dựa trên điểm số trung bình của các bạn trong lớp. Nếu bạn tính luôn cả điểm của chính học sinh đó vào con số trung bình, học sinh đó sẽ tự biết bài của mình, dẫn đến việc ' học vẹt ' và ảo tưởng về năng lực (Target Leakage)! CatBoost giải quyết việc này bằng cách xếp các học sinh thành một hàng ngẫu nhiên. Khi tính điểm cho học sinh thứ $i$, nó chỉ được phép nhìn điểm của những bạn đứng TRƯỚC học sinh đó trong hàng, tuyệt đối không được nhìn điểm của chính mình hay của bạn đứng sau!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Trong GBDT truyền thống, gradient của mẫu $i$ tại bước $t$ được tính bằng: $g^t(x_i, y_i) = \left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right]_{F = F^{t-1}}$. Mô hình $F^{t-1}$ được huấn luyện trên TẤT CẢ các mẫu bao gồm cả $(x_i, y_i)$, do đó $F^{t-1}(x_i)$ bị lệch (shifted) so với phân phối thực tế của mẫu chưa thấy $\rightarrow$ Hiện tượng Prediction Shift.
- Ordered Boosting: Sinh một hoán vị ngẫu nhiên $\sigma$ trên tập huấn luyện. Với mỗi mẫu $x_i$, mô hình duy trì mô hình hỗ trợ $M_i$ chỉ được huấn luyện trên các mẫu đứng trước nó: $\{ x_j : \sigma(j) < \sigma(i) \}$.
- Thống kê mục tiêu (Ordered Target Encoding): $\hat{x}_i^k = \frac{\sum_{j: \sigma(j) < \sigma(i)} \mathbb{I}(x_j^k = x_i^k) y_j + a \cdot p}{\sum_{j: \sigma(j) < \sigma(i)} \mathbb{I}(x_j^k = x_i^k) + a}$. Công thức này hoàn toàn không chứa $y_i$, triệt tiêu 100% rò rỉ mục tiêu!

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy B: Sai. Vấn đề bộ nhớ sâu giải quyết bằng max_depth hoặc histogram binning, không phải mục tiêu của Ordered Boosting.
- Bẫy C: Hoán vị là trên các HÀNG (mẫu quan sát), không phải đảo ngược các CỘT đặc trưng.
- Bẫy D: CatBoost hỗ trợ phân loại đa lớp nguyên bản qua MultiClass loss, không biến thành hồi quy đơn biến.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên chỉ ra quy tắc ngầm khi thi Tabular: Nếu dữ liệu có nhiều cột danh mục cardinality cao (như mã bưu điện, mã khách hàng, tên quận/huyện) và số dòng $< 50.000$, CatBoost với tham số mặc định gần như luôn đánh bại LightGBM được tinh chỉnh thủ công vì cơ chế Ordered Target Encoding và Oblivious Trees này.

---

### Câu 07 [OLP04-Q07] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-07] Trong mô hình Vision Transformer (ViT-B/16), ảnh đầu vào có kích thước (3, 224, 224) được chia thành các mảnh (patches) kích thước 16x16. Phép chiếu Patch Projection chiếu mỗi patch phẳng thành một vector đặc trưng có chiều d_model = 768. Về mặt hiện thực mã nguồn trong PyTorch, phép chiếu này tương đương chính xác với lớp tích chập nào sau đây?

- **A.** nn. Conv2d(in_channels=3, out_channels=768, kernel_size=1, stride=1)
- **B.** nn. Conv2d(in_channels=768, out_channels=3, kernel_size=16, stride=16)
- **C.** nn. Conv2d(in_channels=3, out_channels=768, kernel_size=16, stride=1, padding=8)
- **D.** nn. Conv2d(in_channels=3, out_channels=768, kernel_size=16, stride=16)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Thay vì phải dùng dao cắt tấm ảnh thành từng miếng vuông $16 \times 16$ rồi dùng hàm flatten duỗi thẳng ra rồi nhân với ma trận, các kỹ sư dùng một bộ lọc tích chập kích thước đúng bằng miếng vuông đó (kernel_size=16) và cho nó bước nhảy không chồng lấn (stride=16). Mỗi bước nhảy, bộ lọc chụp trọn một miếng vuông và ép nó thành 768 con số!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Số lượng patch: $N = \frac{H}{P} \times \frac{W}{P} = \frac{224}{16} \times \frac{224}{16} = 14 \times 14 = 196$ patches.
- Kích thước mỗi patch phẳng: $x_p \in \mathbb{R}^{3 \times 16 \times 16} = \mathbb{R}^{768}$.
- Phép chiếu tuyến tính: $z_0 = [x_{\text{class}}; x_p^1 E; x_p^2 E; \dots; x_p^N E] + E_{\text{pos}}$, với $E \in \mathbb{R}^{(P^2 C) \times D} = \mathbb{R}^{768 \times 768}$.
- Khi dùng `nn. Conv2d(in_channels=3, out_channels=768, kernel_size=16, stride=16)`:
  + Chiều không gian sau Conv: $H_{\text{out}} = \lfloor \frac{224 - 16}{16} \rfloor + 1 = 14$, $W_{\text{out}} = 14$.
  + Tensor đầu ra: $(B, 768, 14, 14)$. Sau khi gọi `.flatten(2).transpose(1, 2)`, tensor trở thành $(B, 196, 768)$ — đồng nhất 100% với định nghĩa toán học của ViT!

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: kernel=1, stride=1 cho ra tensor $(B, 768, 224, 224)$, số lượng token lên đến $50.176$ khiến Self-Attention bị OOM bộ nhớ ngay lập tức.
- Bẫy B: stride=1 tạo ra các patch chồng lấn (sliding window), không phải là phép phân rã rời rạc của ViT chuẩn.
- Bẫy C: Đảo ngược chiều kênh `in_channels` và `out_channels`.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên lưu ý: Việc sử dụng `nn. Conv2d(3, 768, 16, 16)` thay vì cắt thủ công bằng vòng lặp Python giúp tăng tốc độ nạp dữ liệu trên GPU lên hơn 15 lần nhờ các kernel tối ưu hóa CUDA cuDNN.

---

### Câu 08 [OLP04-Q08] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-08] Trong các bài toán Computer Vision độ phân giải cao (như High-Resolution Segmentation hoặc Object Detection), do giới hạn bộ nhớ VRAM của GPU trong phòng thi, thí sinh buộc phải thiết lập kích thước lô batch size cực nhỏ (ví dụ $N = 1$ hoặc $N = 2$). Hiện tượng nào sau đây phản ánh chính xác nhất hạn chế của lớp Batch Normalization (BatchNorm2d) trong tình huống này?

- **A.** Thống kê mini-batch (mean và variance) ước lượng từ 1-2 ảnh có phương sai biến thiên cực lớn, làm suy giảm tính ổn định khi tối ưu mạng nơ-ron
- **B.** Tầng chuẩn hóa Batch Normalization tự động chuyển sang cơ chế loại bỏ ngẫu nhiên (Dropout Mode) khi kích thước lô $N \le 2$ để hạn chế bùng nổ gradient
- **C.** Tốc độ huấn luyện tăng gấp đôi do mô hình kích hoạt cơ chế bỏ qua chuẩn hóa đặc trưng (Bypass Normalization) khi số mẫu trong lô nhỏ hơn ngưỡng
- **D.** Phương sai của mini-batch luôn nhận giá trị bằng 0 tuyệt đối (Zero Variance) do chỉ có một ảnh đầu vào được truyền qua đồ thị tính toán mỗi bước

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Lớp `nn. BatchNorm2d` trong PyTorch tính trung bình và phương sai trên cả 3 chiều $(N, H, W)$ theo từng kênh. Kích thước $N = 1$ không tự động làm cho phương sai bằng 0 nếu $H \times W > 1$, vì vẫn có $H \times W$ điểm ảnh tham gia tính toán. Tuy nhiên, nếu tất cả các điểm ảnh trong feature map có giá trị bằng nhau (ví dụ vùng phẳng hoàn toàn) thì phương sai vẫn bằng 0; khi đó hằng số $\epsilon$ trong công thức đóng vai trò bảo vệ mẫu số chống chia cho 0.
Vấn đề cốt lõi khi $N$ rất nhỏ (1 hoặc 2) là các thống kê chỉ đại diện cho 1–2 mẫu đơn lẻ nên độ biến thiên ước lượng rất cao, có thể làm giảm tính ổn định của quá trình tối ưu hóa.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích chuẩn mực theo đặc tả PyTorch `torch.nn. BatchNorm2d`:
- Cho đầu vào tensor $(N, C, H, W)$. Với mỗi kênh $c \in [1, C]$, thống kê được tính trên tập hợp các phần tử kích thước $m = N \times H \times W$:
  $$\mu_c = \frac{1}{N \times H \times W} \sum_{n=1}^N \sum_{h=1}^H \sum_{w=1}^W x_{n, c, h, w}$$
  $$\sigma_c^2 = \frac{1}{N \times H \times W} \sum_{n=1}^N \sum_{h=1}^H \sum_{w=1}^W (x_{n, c, h, w} - \mu_c)^2$$
- Công thức chuẩn hóa phần tử:
  $$\hat{x}_{n, c, h, w} = \frac{x_{n, c, h, w} - \mu_c}{\sqrt{\sigma_c^2 + \epsilon}}$$
- Nhận xét khoa học:
  1. $N = 1$ không đồng nghĩa với $\sigma_c^2 = 0$. Tuy nhiên, $N = 1$ cũng không bảo đảm $\sigma_c^2 > 0$ (nếu feature map đồng nhất thì $\sigma_c^2 = 0$). Hằng số $\epsilon$ (mặc định $10^{-5}$) giúp phép chia luôn ổn định số học.
  2. Khi $N$ nhỏ, độ biến thiên của ước lượng thống kê mẫu cao hơn nhiều so với khi dùng batch lớn, có thể ảnh hưởng đến sự ổn định hội tụ.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi:**
- **Phương án B sai:** BatchNorm không bao giờ tự động chuyển thành Dropout.
- **Phương án C sai:** BatchNorm không bỏ qua bước chuẩn hóa.
- **Phương án D sai:** Ngộ nhận tai hại rằng $N=1$ thì phương sai luôn bằng 0; thực tế BatchNorm2d tính trên cả kích thước không gian $H \times W$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 Căn cứ lý thuyết: Xem tài liệu PyTorch `torch.nn. BatchNorm2d` và bài báo *Group Normalization* (Wu & He, ECCV 2018).
💡 Trong thực tế: Với batch size nhỏ, các kiến trúc hiện đại thường cân nhắc GroupNorm, LayerNorm hoặc sử dụng Frozen BatchNorm tùy thuộc vào bài toán và dữ liệu.

---

### Câu 09 [OLP04-Q09] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-09] Trong quá trình sinh văn bản tự hồi quy (Autoregressive Generation) của các mô hình ngôn ngữ lớn (như DeepSeek, LLaMA), cơ chế Key-Value Cache (KV Cache) lưu lại tensor K và V của các token quá khứ, giúp giảm độ phức tạp tính toán FLOPs tại mỗi bước sinh token mới từ O(T^2) xuống O(T). Tuy nhiên, cơ chế này đánh đổi bằng sự gia tăng mạnh mẽ của yếu tố tài nguyên nào?

- **A.** Tăng gấp đôi số lượng tham số lưu trữ trên đĩa cứng của mô hình do phải lưu ma trận trọng số cho từng bước sinh độc lập
- **B.** Dung lượng bộ nhớ VRAM của GPU tăng tuyến tính theo độ dài chuỗi sinh ra và kích thước batch, dễ dẫn đến lỗi tràn bộ nhớ Out-Of-Memory
- **C.** Làm mất tính chất nhân quả (Causality) của ma trận mặt nạ tam giác dưới (Causal Mask) do các vector Key bị ghi đè ngẫu nhiên
- **D.** Làm suy giảm độ chính xác của hàm kích hoạt phi tuyến SwiGLU do các phép toán xấp xỉ số thực dấu phẩy động bị tích lũy sai số

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mỗi khi sinh ra một từ mới, mô hình cần chú ý (attend) tới toàn bộ các từ đã sinh ra trước đó. Nhờ có KV Cache, mô hình không cần phải tính toán lại vector Key và Value của các từ cũ. Tuy nhiên, vector $q_{\text{new}}$ vẫn phải nhân vô hướng với toàn bộ $T$ vector $k$ trong cache, do đó phép tính Attention tại bước này tốn $\mathcal{O}(T)$ phép tính (thay vì $\mathcal{O}(T^2)$ nếu phải tính lại toàn bộ).
Cái giá phải trả là cuốn sổ tay KV Cache phình to theo thời gian: càng nói nhiều, VRAM càng cạn kiệt!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích độ phức tạp tính toán và bộ nhớ:
- Không có KV Cache: Tại bước $T$, tính lại Attention cho cả $T$ tokens tốn $\mathcal{O}(T^2 \cdot d)$ FLOPs.
- Có KV Cache: Chỉ tính $q_{\text{new}}$ cho 1 token mới, sau đó nhân với $K_{\text{past}} \in \mathbb{R}^{T \times d}$ tốn $\mathcal{O}(T \cdot d)$ FLOPs.
- Dung lượng bộ nhớ lưu trữ KV Cache:
  $$\text{Memory}_{\text{KV}} = 2 \times b \times T \times n_{\text{layers}} \times n_{\text{heads}} \times d_{\text{head}} \times \text{bytes}$$
  Tăng tuyến tính trực tiếp theo độ dài chuỗi $T$ và batch size $b$, chiếm hàng chục GB VRAM trên các context length lớn (32k, 128k).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi:**
- **Phương án A:** Phương án gây nhiễu, không phản ánh đúng cơ chế toán học/kỹ thuật.
- **Phương án C:** Phương án gây nhiễu, không phản ánh đúng cơ chế toán học/kỹ thuật.
- **Phương án D:** Phương án gây nhiễu, không phản ánh đúng cơ chế toán học/kỹ thuật.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 Căn cứ lý thuyết: Xem HuggingFace *KV Cache Explanation* và các bài báo GQA (Ainslie et al., 2023), MLA (DeepSeek-V2, 2024).

---

### Câu 10 [OLP04-Q10] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-10] Một thí sinh thực hiện quy trình chuẩn bị dữ liệu cho bài toán Tabular Regression như sau: Bước 1: Nạp toàn bộ tập dữ liệu (10.000 dòng). Bước 2: Sử dụng ' StandardScaler().fit_transform(X)' trên toàn bộ 10.000 dòng. Bước 3: Sử dụng ' KFold(n_splits=5, shuffle=True)' để chia tập huấn luyện và kiểm thử chéo. Điểm Cross-Validation đạt R^2 = 0.92 rất cao, nhưng khi nộp bài trên Private Test của ban tổ chức thì điểm tụt thảm hại xuống R^2 = 0.58. Đâu là sai lầm chí mạng mà thí sinh này đã phạm phải?

- **A.** Huấn luyện trên miền Fourier (Frequency Domain) cô lập hoàn toàn các thành phần tần số cao, trong khi nhiễu đối kháng chỉ phát sinh ở tần số thấp
- **B.** Tối ưu hóa đối kháng (Adversarial Training) qua $L_\infty$-PGD tìm nhiễu tệ nhất trong lân cận $\epsilon$ và cập nhật trọng số để chống lại nhiễu đó
- **C.** Cơ chế chuẩn hóa nhóm (Group Normalization) triệt tiêu hoàn toàn gradient của các vector nhiễu có độ lệch chuẩn nhỏ hơn ngưỡng dung sai hội tụ
- **D.** Hàm kích hoạt Swish (Self-Gated Activation) làm bão hòa đạo hàm bậc nhất của các mẫu nhiễu ngoại lai, ngăn chặn lan truyền tín hiệu phá hoại

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Giống như trước khi làm bài kiểm tra học kỳ, thầy giáo vô tình cho học sinh biết điểm trung bình và độ lệch chuẩn của toàn bộ đề thi sắp tới. Học sinh dùng thông tin đó để đoán bài, làm bài thử ở nhà đạt điểm 10 tuyệt đối. Nhưng khi bước vào phòng thi thật với một đề thi hoàn toàn mới (Private Test), học sinh không còn biết trước thông tin thống kê đó nữa và trượt vỏ chuối!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Giả sử toàn bộ tập dữ liệu $D = D_{\text{train}} \cup D_{\text{val}}$. Khi gọi `fit` trên $D$:
  $\mu_{\text{global}} = \frac{1}{N}\sum_{i \in D} x_i = \frac{N_{\text{train}}\mu_{\text{train}} + N_{\text{val}}\mu_{\text{val}}}{N}$.
- Từng mẫu trong $D_{\text{train}}$ được chuẩn hóa bằng $\mu_{\text{global}}$ vốn đã chứa $\mu_{\text{val}}$ bên trong. Mô hình học được các ranh giới tối ưu hóa dựa trên thông tin ngầm từ $D_{\text{val}}$.
- Trên Private Test $D_{\text{test}}$, phân phối $\mu_{\text{test}}$ khác biệt, khiến các trọng số được tối ưu từ thông tin rò rỉ trở nên hoàn toàn sai lệch.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: `shuffle=True` xáo trộn thứ tự các HÀNG (samples), không bao giờ làm xáo trộn các CỘT đặc trưng.
- Bẫy B: StandardScaler thiết kế riêng cho biến số liên tục (continuous features).
- Bẫy C: `n_splits` có thể chọn 5, 10 hoặc bất kỳ giá trị hợp lý nào tuỳ ý.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Quy tắc bất di bất dịch của phòng thi AI: ' Fit trên Train, chỉ Transform trên Val và Test '. Cách viết chuẩn duy nhất là sử dụng `sklearn.pipeline. Pipeline` kết hợp KFold, hoặc viết vòng lặp gọi `scaler.fit(X_train)` rồi mới `scaler.transform(X_val)`.

---

### Câu 11 [OLP04-Q11] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-11] Khi huấn luyện một mạng đa tác vụ (Multi-task Learning) trong Document AI gồm định vị hộp bao ô bảng (Bounding Box Regression Loss - L_box) và phân loại ngữ nghĩa văn bản (Text Classification Loss - L_cls), việc cộng tổng trực tiếp L = L_box + L_cls thường khiến mô hình chỉ tối ưu task box mà bỏ quên task cls vì biên độ L_box lớn hơn nhiều lần. Phương pháp Homoscedastic Uncertainty Weighting (Kendall et al.) giải quyết bài toán này như thế nào?

- **A.** Triệt tiêu hiện tượng sụp đổ biểu diễn (Dimensional Collapse) bằng cách ép ma trận hiệp phương sai của các vector nhúng phải tiến gần ma trận đơn vị
- **B.** Tăng tốc độ lan truyền ngược qua việc xấp xỉ ma trận Jacobi bằng ma trận đường chéo (Diagonal Approximation) giúp tiết kiệm bộ nhớ đệm đồ thị tính toán
- **C.** Tự động phân nhóm các vector đặc trưng vào các cụm phân bố chuẩn đa chiều (Gaussian Mixture Modeling) nhằm đơn giản hóa hàm mất mát phân loại tuyến tính
- **D.** Bảo toàn khoảng cách Euclid giữa các mẫu cùng lớp đồng thời tối đa hóa khoảng cách Cosine (Cosine Distance Maximization) giữa các mẫu thuộc lớp khác biệt

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Giống như một học sinh vừa phải học Toán vừa phải học Văn để đi thi. Điểm bài tập Toán tính theo thang 100 điểm, còn Văn tính theo thang 10 điểm. Nếu cứ cộng cơ học điểm số, học sinh sẽ dồn 90% thời gian cày Toán vì làm đúng 1 câu Toán được nhiều điểm hơn hẳn Văn! Cơ chế Uncertainty Weighting giống như việc tự động gắn cho mỗi môn một chiếc ' cân tiểu ly '. Môn nào bài tập đang quá khó hoặc thang điểm quá to sẽ tự động được điều chỉnh độ nhạy để học sinh phân bổ công sức đồng đều cho cả hai môn.

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Xuất phát từ hàm hợp lý cực đại đa nhiệm (Multi-task Maximum Likelihood) với giả thiết phân phối chuẩn Gaussian cho hồi quy và Softmax cho phân loại:
  $p(y_1, y_2 | f(x)) = \mathcal{N}(y_1; f_1(x), \sigma_1^2) \times \text{Softmax}(y_2; f_2(x), \sigma_2^2)$.
- Lấy logarit tự nhiên đổi dấu:
  $\mathcal{L}(W, \sigma_1, \sigma_2) = \frac{1}{2\sigma_1^2}\mathcal{L}_{\text{box}}(W) + \frac{1}{\sigma_2^2}\mathcal{L}_{\text{cls}}(W) + \ln(\sigma_1) + \ln(\sigma_2)$.
- Đạo hàm theo $\sigma_1$:
  $\frac{\partial \mathcal{L}}{\partial \sigma_1} = -\frac{1}{\sigma_1^3}\mathcal{L}_{\text{box}} + \frac{1}{\sigma_1} = 0 \iff \sigma_1^2 = \mathcal{L}_{\text{box}}$.
- Tham số $\sigma$ tự động đóng vai trò là trọng số tương đối: Khi task nào có loss lớn, $\sigma$ tự tăng lên để dìm trọng số $\frac{1}{\sigma^2}$ xuống, đồng thời số hạng $\ln(\sigma)$ đóng vai trò là regularizer chống $\sigma \to \infty$!

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Cố định hệ số tĩnh (static weight) không thích nghi được với sự thay đổi của loss qua từng giai đoạn huấn luyện.
- Bẫy C: Không thể ép task phân loại văn bản đa lớp dùng hàm MSE mà không làm suy giảm hiệu năng xác suất.
- Bẫy D: Huấn luyện tuần tự (Alternating training) gây hiện tượng Catastrophic Forgetting (quên tác vụ trước).

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên chỉ ra mẹo cài đặt số học trong PyTorch: Để tránh $\sigma \le 0$ gây lỗi toán học, người ta đặt biến học là $s_i = \ln(\sigma_i^2)$, khi đó loss trở thành: $\mathcal{L} = \exp(-s_1)\mathcal{L}_1 + \exp(-s_2)\mathcal{L}_2 + \frac{1}{2}s_1 + \frac{1}{2}s_2$. Cực kỳ ổn định và không bao giờ bị NaN!

---

### Câu 12 [OLP04-Q12] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-12] Trong bài toán dịch máy SOLOAI được chấm bằng chỉ số chuẩn SacreBLEU, một thí sinh có độ chính xác n-gram rất tốt: p1 = 0.8, p2 = 0.7, p3 = 0.6, p4 = 0.5. Tuy nhiên, do mô hình sinh ra token kết thúc [EOS] quá sớm, tổng độ dài câu dịch của mô hình chỉ là c = 8 từ, trong khi độ dài câu tham chiếu chuẩn là r = 16 từ. Điểm SacreBLEU của thí sinh bị sụt giảm bao nhiêu % so với điểm trung bình nhân độ chính xác (geometric mean of precisions)?

- **A.** Chuyển toàn bộ các phép nhân ma trận trọng số sang miền tần số Fourier (Fast Fourier Transform) để giảm độ phức tạp tính toán từ bậc 2 về bậc tuyến tính
- **B.** Chiếu không gian biểu diễn đa chiều sang dạng nhị phân 1-bit (One-bit Quantization) thông qua hàm bước nhảy Heaviside trước khi tính tích vô hướng
- **C.** Tách một ma trận lớn $W \in \mathbb{R}^{d \times k}$ thành tích hai ma trận hạng thấp (Low-Rank Decomposition) $B \times A$ với hạng $r \ll \min(d, k)$
- **D.** Đóng băng ngẫu nhiên 90% số lượng nơ-ron trong các tầng ẩn (Stochastic Layer Freezing) và chỉ cập nhật trọng số của các nơ-ron có độ nhạy gradient cao

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Tưởng tượng bạn làm bài thi dịch văn bản. Đề bài yêu cầu dịch một đoạn văn dài 16 từ. Bạn chỉ dịch đúng được 8 từ đầu tiên rồi nộp bài luôn. Mặc dù 8 từ bạn dịch ra đều chuẩn xác từng chữ, giám khảo không thể cho bạn điểm giỏi được vì bạn bỏ dở nửa sau của câu! Hệ số phạt Brevity Penalty của BLEU giống như một công thức trừ điểm nặng tay cho bài làm cụt: Nó lấy hàm mũ $\exp(-1) \approx 0.368$, tức là bạn mất trắng hơn 63% tổng số điểm chỉ vì câu dịch quá ngắn!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Điểm trung bình nhân độ chính xác (Precision): $P_{\text{geom}} = \exp\left( \frac{1}{4} \sum_{n=1}^4 \ln p_n \right) = \exp\left( \frac{\ln 0.8 + \ln 0.7 + \ln 0.6 + \ln 0.5}{4} \right) = \sqrt[4]{0.8 \times 0.7 \times 0.6 \times 0.5} = \sqrt[4]{0.168} \approx 0.6402$ (tương đương 64.02 điểm BLEU thô).
- Công thức Brevity Penalty khi độ dài dự đoán $c < r$:
  $\text{BP} = \exp\left(1 - \frac{r}{c}\right) = \exp\left(1 - \frac{16}{8}\right) = \exp(-1) \approx 0.367879$.
- Điểm SacreBLEU cuối cùng:
  $\text{BLEU} = \text{BP} \times P_{\text{geom}} = 0.367879 \times 0.6402 \approx 0.2355$ (chỉ còn 23.55 điểm!).
- Mức độ sụt giảm tương đối: $1 - \text{BP} = 1 - 0.367879 \approx 63.21\%$.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy C: Sai hoàn toàn. Nếu không có BP, một mô hình chỉ cần sinh ra đúng 1 từ duy nhất ' The ' có trong câu là đạt precision 1.0 (100%)!
- Bẫy B: Sai công thức. Phạt theo hàm số mũ $\exp(1 - r/c)$, không phải phạt tỷ lệ tuyến tính $c/r$.
- Bẫy D: Quy chế máy chấm tự động tính công thức toán, không có luật trừ điểm thủ công.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên lưu ý chiến thuật Beam Search trong phòng thi: Khi giải mã câu dịch, luôn thiết lập Length Penalty (tham số $\alpha$ trong công thức điểm beam score: $\text{score} = \frac{\log P(Y|X)}{(\frac{5+|Y|}{6})^\alpha}$). Đặt $\alpha \approx 0.6 - 0.8$ sẽ ngăn cản mô hình sinh token EOS quá sớm, đảm bảo độ dài câu dịch $c \approx r$ để giữ trọn vẹn điểm BP = 1.0!

---

### Câu 13 [OLP04-Q13] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-13] Trong bài toán phát hiện khuyết tật sản phẩm hoặc định vị bảng biểu hiếm gặp, tỷ lệ giữa mẫu nền âm tính (negative / background) và mẫu dương tính (positive) là 1000 : 1. Hàm mất mát Focal Loss được sử dụng: $\text{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \ln(p_t)$. Khi thiết lập $\gamma = 2$ và xét $\alpha_t = 1$ (hoặc so sánh tương quan với $\alpha$-weighted Cross-Entropy), tác động toán học của thừa số điều chế (modulating factor) $(1 - p_t)^\gamma$ lên giá trị mất mát (loss) của một mẫu nền dễ phân loại có xác suất dự đoán đúng $p_t = 0.99$ là gì?

- **A.** Cơ chế chuẩn hóa LayerNorm (Pre-Layer Normalization) đặt trước khối Multi-Head Attention giúp ổn định phân phối gradient qua các tầng sâu hơn
- **B.** Mặt nạ nhân quả tam giác dưới (Causal Attention Mask) ngăn không cho vị trí token hiện tại nhìn thấy các thông tin của các token nằm ở tương lai
- **C.** Hàm kích hoạt phi tuyến tính GELU (Gaussian Error Linear Unit) triệt tiêu hoàn toàn hiện tượng chết nơ-ron thường gặp ở các hàm ReLU truyền thống
- **D.** Phép mã hóa vị trí tương đối RoPE (Rotary Position Embedding) xoay các vector Query và Key trong mặt phẳng phức để bảo toàn khoảng cách tương đối

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Với một mẫu nền quá dễ nhận biết ($p_t = 0.99$), thừa số điều chế $(1 - p_t)^2 = (1 - 0.99)^2 = 0.0001 = 10^{-4}$. Thừa số này nhân thẳng vào hàm mất mát Cross-Entropy, dìm giá trị mất mát của mẫu nền xuống đúng 10.000 lần, giúp mô hình dồn toàn bộ sự chú ý vào các mẫu khó phân loại!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích định lượng chính xác:
- Hàm Cross-Entropy chuẩn (với $\alpha_t = 1$): $\text{CE}(0.99) = -\ln(0.99) \approx 0.0100503$.
- Thừa số điều chế Focal: $(1 - 0.99)^2 = (0.01)^2 = 10^{-4} = \frac{1}{10.000}$.
- Giá trị mất mát Focal Loss: $\text{FL}(0.99) = 10^{-4} \times 0.0100503 \approx 1.00503 \times 10^{-6}$ (giảm chính xác $10.000$ lần so với Cross-Entropy). Do đó chọn **D**.

📐 Mở rộng: Đạo hàm Gradient theo logit $z$ (hướng về lớp đích, với $p = \sigma(z)$):
- Đạo hàm giải tích chuẩn xác của Focal Loss theo logit $z$ với $\alpha = 1$:
  $$\frac{\partial \text{FL}}{\partial z} = (1 - p)^\gamma \left[ (p - 1) + \gamma p \ln(p) \right]$$
- Với $p = 0.99, \gamma = 2$:
  * $(1 - p)^2 = 10^{-4}$.
  * $p - 1 = -0.01$.
  * $\gamma p \ln(p) = 2 \times 0.99 \times \ln(0.99) \approx -0.019899665$.
  * Tổng trong ngoặc vuông: $(-0.01) + (-0.019899665) = -0.029899665$.
  * Gradient Focal Loss: $\frac{\partial \text{FL}}{\partial z} = 10^{-4} \times (-0.029899665) \approx -2.9899665 \times 10^{-6}$.
  * Trong khi đó, Gradient của Cross-Entropy: $\frac{\partial \text{CE}}{\partial z} = p - 1 = -0.01$.
  * Tỉ lệ gradient giữa Focal Loss và Cross-Entropy: $\frac{-2.9899665 \times 10^{-6}}{-0.01} = 0.00029899665$ (giảm xấp xỉ 3.344 lần).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi:**
- **Phương án A sai:** Không liên quan đến hàm Dirac delta.
- **Phương án B sai:** Thừa số điều chế phụ thuộc vào $p_t$, không phải hằng số.
- **Phương án C sai:** Focal Loss làm giảm (dìm) mất mát của mẫu dễ, không làm tăng.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 Căn cứ lý thuyết: Lin et al., *Focal Loss for Dense Object Detection*, ICCV 2017.

---

### Câu 14 [OLP04-Q14] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-14] Khi tối ưu mô hình để chạy script nộp bài trong 20 phút, một thí sinh thực hiện lượng hóa sau huấn luyện INT8 (Post-Training Quantization - PTQ) để giảm 50% dung lượng bộ nhớ. Tuy nhiên, khi chạy thử nghiệm suy luận trên môi trường máy chấm của ban tổ chức (máy chủ CPU thông thường hoặc GPU không hỗ trợ tập lệnh INT8 Tensor Cores / DP4A), thí sinh ngạc nhiên thấy thời gian suy luận (latency) lại CHẬM HƠN so với bản gốc FP16/FP32. Đâu là nguyên nhân kỹ thuật mà giảng viên giải thích cho hiện tượng này?

- **A.** Lớp đệm phản xạ biên (Reflection Padding) mở rộng kích thước ảnh đầu vào bằng cách lấy đối xứng gương qua các cạnh để tránh viền đen nhân tạo
- **B.** Tích chập chuyển vị (Transposed Convolution) với kernel $4 \times 4$ và bước nhảy $s=2$ tạo ra lưới chồng chập không đều, gây hiệu ứng bàn cờ (Checkerboard Artifacts)
- **C.** Cơ chế cắt tỉa đặc trưng (Channel Pruning) vô tình loại bỏ các kênh có phương sai thấp khiến mô hình mất thông tin chi tiết tần số cao
- **D.** Hàm mất mát $L_1$ (Mean Absolute Error) không có đạo hàm tại điểm 0, dẫn đến dao động gradient mạnh quanh điểm cực tiểu cục bộ của bề mặt tối ưu

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Giống như bạn dịch một bức thư từ tiếng Việt sang chữ viết tắt tiếng Anh siêu ngắn để tiết kiệm chỗ trên một mảnh giấy nhỏ. Nhưng người nhận thư lại không biết đọc tiếng Anh viết tắt! Mỗi khi đọc một chữ, họ lại phải lật từ điển tra cứu dịch ngược từng chữ về tiếng Việt rồi mới hiểu được. Việc tra cứu qua lại liên tục đó làm tốc độ đọc chậm hơn rất nhiều so với việc bạn cứ để nguyên bức thư tiếng Việt bình thường ngay từ đầu!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Phép lượng hóa Affine: $q = \text{round}\left(\frac{x}{s}\right) + z$, với $s$ là scale factor và $z$ là zero-point.
- Để tính tích ma trận $Y = X \cdot W$ với $X, W$ dạng INT8:
  + Trên phần cứng có INT8 Tensor Cores (như RTX 3090, A100, T4 Turing): Lệnh DP4A / WMMA thực hiện trực tiếp phép nhân nguyên tích luỹ 32-bit: $Y_{\text{int32}} = \sum (q_x - z_x)(q_w - z_w)$ trong 1 chu kỳ xung nhịp $\rightarrow$ Tăng tốc độ $2\times - 4\times$.
  + Trên phần cứng CPU cũ hoặc GPU không có INT8 engine: Không có tập lệnh song song số nguyên. Mạng phải unpack từng byte, thực hiện phép float: $w_{\text{fp}} = s_w \times (q_w - z_w)$ rồi mới gọi BLAS GEMM thông thường. Chi phí ép kiểu bộ nhớ (Type casting & Memory Bandwidth overhead) khiến tổng thời gian thực thi tăng thêm $30\% - 80\%$.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Hoàn toàn phi lý về mặt cơ chế phần cứng máy tính.
- Bẫy B: Lượng hóa thu nhỏ kích thước dữ liệu, giúp chứa được nhiều hơn trong L1 cache chứ không làm tăng dung lượng vật lý của cache.
- Bẫy D: ReLU hoạt động trên số nguyên bình thường qua phép so sánh `max(0, q)`.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên chỉ ra bài học sống còn: Trước khi áp dụng INT8 Quantization trong bài thi có giới hạn thời gian, BẮT BUỘC phải kiểm tra cấu hình máy chấm ban tổ chức. Nếu máy chấm chỉ cấp CPU thuần hoặc GPU Pascal (GTX 1080Ti) không có Tensor Cores INT8, hãy giữ nguyên định dạng FP16 (nửa độ chính xác) hoặc FP32 bằng ONNX Runtime để đạt tốc độ tối đa.

---

### Câu 15 [OLP04-Q15] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-15] Trong bài toán dự báo chuỗi thời gian phụ tải tiêu thụ điện năng cho 24 giờ tiếp theo (Time Series Forecasting), một thí sinh sử dụng phương pháp 5-Fold Cross-Validation tiêu chuẩn với hàm train_test_split có shuffle=True ngẫu nhiên. Mô hình LightGBM đạt điểm CV cực kỳ ấn tượng với R^2 = 0.98. Tuy nhiên, khi dự báo trên tập kiểm tra thực tế (Private Test gồm 7 ngày tiếp theo), mô hình hoàn toàn thất bại với R^2 < 0.15. Đâu là giải thích chuẩn xác nhất từ video bài giảng?

- **A.** Thực hiện phép nội suy song tuyến tính (Bilinear Interpolation) để xấp xỉ liên tục giá trị đặc trưng tại 4 điểm lân cận mà không làm tròn số nguyên
- **B.** Làm tròn toạ độ hộp bao về số nguyên gần nhất (Nearest Integer Rounding) sau đó áp dụng phép lấy mẫu Max-Pooling cục bộ trên từng ô lưới $7 \times 7$
- **C.** Chiếu toàn bộ vùng RoI sang miền tần số không gian (Frequency Domain Projection) rồi chọn lọc các thành phần tần số thấp mang năng lượng lớn nhất
- **D.** Gán nhãn nhị phân cho từng điểm ảnh dựa trên ngưỡng khoảng cách Euclid (Euclidean Distance Thresholding) so với tâm trọng lực của bounding box

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Tưởng tượng bạn làm bài thi dự đoán giá vàng ngày thứ Tư. Nhưng đề cương ôn thi ở nhà lại cho bạn biết trước giá vàng ngày thứ Ba và ngày thứ Năm! Bạn chỉ việc lấy trung bình cộng điểm số của ngày thứ Ba và thứ Năm là đoán trúng phóc ngày thứ Tư với độ chính xác 99%. Nhưng khi đi thi thật, bạn chỉ đứng ở ngày thứ Bảy và phải đoán giá vàng của tuần sau — lúc này bạn không hề có dữ liệu của tương lai để ' kẹp giữa ' nữa, và bạn đoán sai hoàn toàn!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Dữ liệu chuỗi thời gian có tính phụ thuộc tự tương quan mạnh: $\text{Cov}(y_t, y_{t-1}) \ne 0$.
- Khi chia ngẫu nhiên (Random Shuffle): Điểm $y_t$ nằm ở tập Train trong khi $y_{t-1}$ và $y_{t+1}$ nằm ở tập Val. Các đặc trưng trễ (Lag features $x_t = y_{t-1}$) và biến mục tiêu liên kết trực tiếp giữa các fold, làm mất tính độc lập giữa Train và Val: $P(D_{\text{val}} | D_{\text{train}}) \ne P(D_{\text{val}})$.
- Kỹ thuật đúng chuẩn: TimeSeriesSplit (Expanding Window hoặc Rolling Window):
  + Fold 1: Train $[0, t_1]$, Val $[t_1, t_2]$.
  + Fold 2: Train $[0, t_2]$, Val $[t_2, t_3]$.
  + Đảm bảo nguyên tắc thời gian: Mọi mẫu trong tập Train luôn diễn ra TRƯỚC tập Validation!

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Sai. LightGBM hỗ trợ regression (MSE / L2) là objective mặc định của nó.
- Bẫy C: Sai. GBDT kết hợp đặc trưng trễ (lag features, rolling stats) là SOTA thống trị hầu hết các cuộc thi Tabular Time Series.
- Bẫy D: R^2 là công thức toán thuần túy tính trên tập mẫu bất kỳ có kích thước $N \ge 2$.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên nhắc nhở: Trong bài toán Time Series, nếu bạn thấy CV Score quá cao một cách bất thường ($R^2 > 0.95$), 99% bạn đã dính lỗi Look-ahead Bias do shuffle hoặc do tính các đặc trưng rolling/expanding vượt qua ranh giới thời gian của tập kiểm thử!

---

### Câu 16 [OLP04-Q16] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-16] Khi xây dựng mô hình NLP cho tiếng Việt và tiếng Trung trong các kỳ thi AI, việc lựa chọn thuật toán tách từ con (Subword Tokenization) quyết định trực tiếp đến hiệu quả biểu diễn chuỗi. Sự khác biệt bản chất trong tiêu chí lựa chọn cặp ký tự để sáp nhập (merge criteria) giữa thuật toán Byte-Pair Encoding (BPE - GPT/LLaMA) và thuật toán WordPiece (BERT) là gì?

- **A.** WordPiece bắt đầu từ toàn bộ từ điển lớn rồi tỉa dần, trong khi BPE bắt đầu từ ký tự đơn lẻ rồi ghép dần lên thành từ con
- **B.** BPE chỉ chạy được trên các chuỗi mã nhị phân 0 và 1, trong khi WordPiece chỉ chạy được trên bảng chữ cái hệ ký tự Latinh
- **C.** BPE tạo ra độ dài chuỗi token luôn bằng đúng một nửa so với WordPiece khi mã hóa cùng một đoạn văn bản ngôn ngữ tự nhiên
- **D.** BPE chọn cặp token có tần suất ghép cao nhất; WordPiece chọn cặp token tối đa hóa hàm hợp lý Likelihood của tập ngữ liệu

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Hãy tưởng tượng bạn ghép các khối lego chữ cái để tạo thành các khối từ lớn hơn: BPE giống như một người đếm số máy móc: Cặp chữ nào xuất hiện cạnh nhau nhiều lần nhất trong cuốn sách (ví dụ chữ ' t ' và ' h ' xuất hiện 1 triệu lần) thì cứ thế dán chúng lại với nhau thành ' th '. Còn WordPiece giống như một nhà ngôn ngữ học thông minh: Ông ấy không chỉ nhìn tần suất, mà còn tự hỏi: ' Việc ghép hai chữ này lại có làm cho cả cuốn sách trở nên dễ hiểu và ít bất ngờ nhất hay không?' Nhờ vậy WordPiece chọn được những cặp ghép có ý nghĩa cấu trúc ngữ nghĩa sâu sắc hơn.

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Tiêu chí sáp nhập của BPE:
  $\text{pair}^* = \arg\max_{(u, v)} \text{Count}(u, v)$. Thuần túy dựa trên tần suất đếm cục bộ.
- Tiêu chí sáp nhập của WordPiece:
  Cho ngữ liệu $C$. Chọn cặp $(u, v)$ sao cho khi sáp nhập thành $w = uv$, hàm $\log$-likelihood của mô hình unigram tăng nhiều nhất:
  $\Delta \mathcal{L} = \log P(uv) - (\log P(u) + \log P(v)) = \log \frac{P(uv)}{P(u) P(v)}$.
  Đây chính là đại lượng Thông tin Tương hỗ từng điểm (Pointwise Mutual Information - PMI)! Cặp $(u, v)$ có thể tần suất không phải cao nhất tuyệt đối, nhưng nếu chúng luôn đi cùng nhau và hiếm khi tách rời, WordPiece sẽ ưu tiên sáp nhập.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Sai. Cả hai đều hoạt động trên chuỗi ký tự unicode hoặc bytes.
- Bẫy B: Đó là cơ chế của Unigram LM (SentencePiece Unigram), bắt đầu từ vocab lớn và tỉa dần dựa trên loss. Cả BPE và WordPiece đều là thuật toán bottom-up (ghép từ dưới lên).
- Bẫy C: Độ dài token hóa phụ thuộc vào kích thước từ vựng và ngữ liệu, không có quy luật cố định bằng một nửa.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên lưu ý cạm bẫy tiếng Việt có dấu: Nếu dùng Tokenizer tiền huấn luyện của tiếng Anh (như GPT-2 gốc) cho tiếng Việt, các ký tự có dấu như ' ệ ', ' ở ', ' đ ' không có trong từ vựng cơ sở và bị phân rã thành 3-4 byte con riêng biệt. Điều này làm độ dài câu tiếng Việt phình to gấp 3 lần, làm tràn cửa sổ ngữ cảnh (Context Length Exceeded) và khiến mạng attention chạy chậm gấp 9 lần!

---

### Câu 17 [OLP04-Q17] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-17] Trong các thư viện Deep Learning (như PyTorch), lớp nn. CrossEntropyLoss luôn kết hợp đồng thời nn. LogSoftmax và nn. NLLLoss thay vì để người dùng tính toán rời rạc hai bước. Bên cạnh việc áp dụng Log-Sum-Exp trick để tránh tràn số học (numerical overflow/underflow), lợi ích toán học thanh lịch nhất của sự kết hợp này khi tính đạo hàm lan truyền ngược theo logit đầu vào z_i là gì?

- **A.** Đạo hàm theo logit biến đổi thành phép nhân ma trận đối xứng bảo toàn chuẩn Euclid L2 của vector gradient lan truyền ngược
- **B.** Đạo hàm theo logit luôn luôn bằng hằng số 1 giúp mạng nơ-ron sâu triệt tiêu hoàn toàn hiện tượng biến mất gradient ở các tầng nông
- **C.** Gradient theo logit rút gọn thành hiệu số cực kỳ đơn giản $\frac{\partial L}{\partial z_i} = p_i - y_i$, triệt tiêu Jacobian phức tạp của Softmax
- **D.** Loại bỏ hoàn toàn sự cần thiết của các thuật toán tối ưu hóa thích ứng như Adam trong quá trình cập nhật trọng số nơ-ron

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi kết hợp `LogSoftmax` và `NLLLoss`, các đạo hàm phức tạp của hàm mũ triệt tiêu hoàn toàn lẫn nhau, chỉ còn lại công thức tao nhã: ' Độ lệch gradient đúng bằng Xác suất mô hình dự đoán ($p_i$) trừ đi Nhãn thực tế ($y_i$)'!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Đạo hàm chi tiết với giả thiết nhãn one-hot ($y_k \in \{0, 1\}, \sum_k y_k = 1$):
- $\mathcal{L} = -\sum_k y_k \log p_k = -\sum_k y_k \left( z_k - \ln \sum_j e^{z_j} \right)$.
- Lấy đạo hàm riêng theo logit $z_i$:
  $$\frac{\partial \mathcal{L}}{\partial z_i} = -y_i + \left( \sum_k y_k \right) \frac{e^{z_i}}{\sum_j e^{z_j}} = -y_i + 1 \cdot p_i = p_i - y_i$$
- Không cần tính ma trận Jacobian của Softmax, loại bỏ hoàn toàn các phép chia gây lỗi NaN.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi:**
- **Phương án A:** Phương án gây nhiễu, không phản ánh đúng cơ chế toán học/kỹ thuật.
- **Phương án B:** Phương án gây nhiễu, không phản ánh đúng cơ chế toán học/kỹ thuật.
- **Phương án D:** Phương án gây nhiễu, không phản ánh đúng cơ chế toán học/kỹ thuật.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 Căn cứ lý thuyết: Xem tài liệu PyTorch `torch.nn. CrossEntropyLoss`.

---

### Câu 18 [OLP04-Q18] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-18] Trong bài toán định vị hộp bao đối tượng (Bounding Box Regression) của Computer Vision và Document AI, hàm mất mát Complete IoU (CIoU Loss) đã thay thế hoàn toàn các hàm mất mát L1/L2 truyền thống và khắc phục hạn chế của GIoU. Khi so sánh hai hộp bao b và b_gt, CIoU Loss tính toán đồng thời ba đại lượng hình học then chốt nào?

- **A.** Đặc trưng hình học biên cạnh (Sobel Gradient Orientation) không đổi khi cường độ sáng thay đổi, giúp định vị chính xác đường bao vật thể cần gán nhãn
- **B.** Phân phối góc hướng gradient (HOG - Histogram of Oriented Gradients) mô tả hình dáng và cạnh cục bộ bất biến với biến đổi độ sáng tuyến tính
- **C.** Vector màu cục bộ (Color Co-occurrence Matrix) lưu trữ tần suất xuất hiện đồng thời của các bộ ba RGB trong lân cận $5 \times 5$ điểm ảnh
- **D.** Biến đổi sóng con Gabor (Gabor Wavelet Decomposition) phân tách ảnh thành các kênh tần số không gian có định hướng cụ thể để đo độ tương phản

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Khi bạn xếp hai chiếc hộp chữ nhật đè lên nhau, muốn biết chúng khớp nhau đến mức nào, bạn cần kiểm tra 3 điều: Thứ nhất, diện tích phần dính nhau to hay nhỏ (IoU); Thứ hai, tâm của hai chiếc hộp có bị lệch xa nhau không (Distance); Thứ ba, dáng hộp có giống nhau không (chiếc hộp này vuông vắn còn chiếc kia lại dẹt dài - Aspect Ratio). CIoU là công thức toàn diện nhất vì nó gom trọn cả 3 tiêu chuẩn này vào một hàm toán duy nhất!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Hạn chế của IoU Loss $\mathcal{L}_{\text{IoU}} = 1 - \text{IoU}$: Khi hai hộp không giao nhau ($\text{IoU} = 0$), gradient triệt tiêu hoàn toàn $\nabla \mathcal{L} = 0$, mô hình không biết kéo hộp về hướng nào!
- Công thức đầy đủ của CIoU Loss:
  $$\mathcal{L}_{\text{CIoU}} = 1 - \text{IoU} + \frac{\rho^2(b, b^{gt})}{c^2} + \alpha v$$
  Trong đó:
  1. $\text{IoU} = \frac{|b \cap b^{gt}|}{|b \cup b^{gt}|}$ (Độ trùng lặp diện tích).
  2. $\frac{\rho^2(b, b^{gt})}{c^2}$: Khoảng cách Euclid giữa 2 tâm $\rho(b, b^{gt})$ chia cho đường chéo $c$ của hộp bao nhỏ nhất chứa cả hai (Distance consistency).
  3. $v = \frac{4}{\pi^2}\left(\arctan\frac{w^{gt}}{h^{gt}} - \arctan\frac{w}{h}\right)^2$: Đo độ lệch tỷ lệ khung hình cạnh/chiều cao.
  4. $\alpha = \frac{v}{(1 - \text{IoU}) + v}$: Hệ số cân bằng động ưu tiên fit IoU trước khi fit tỷ lệ khung hình.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Bounding box loss hình học thuần túy không quan tâm đến cường độ màu sắc pixel bên trong.
- Bẫy C: Hộp bao chuẩn (Axis-aligned bounding box) luôn có 4 góc vuông 90 độ, không có góc nhọn.
- Bẫy D: Sử dụng khoảng cách Euclid chuẩn hóa chia cho đường chéo $c^2$, không dùng khoảng cách Manhattan hay eigenvalue.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên phân tích: GIoU chỉ phạt diện tích bao ngoài $C \setminus (b \cup b^{gt})$. Khi một hộp nằm trọn bên trong một hộp khác, diện tích bao ngoài không đổi khiến gradient GIoU bị suy biến. CIoU giải quyết triệt để vấn đề này nhờ số hạng khoảng cách tâm $\rho^2 / c^2$, giúp tốc độ hội quy của YOLOv5/v8 tăng tốc gấp 3 lần.

---

### Câu 19 [OLP04-Q19] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-19] Trong 60 phút cuối cùng của kỳ thi Olympic AI, khi ban tổ chức phát mật khẩu mở tập dữ liệu Private Test gồm 2.500 ảnh tài liệu, một thành viên đề xuất bật cơ chế Test-Time Augmentation (TTA) 8-phép biến đổi cho mô hình Ensemble 3 backbone (biết baseline suy luận 1x thông thường mất ~5 phút). Giảng viên đã đưa ra lời cảnh báo chiến thuật nghiêm khắc nào?

- **A.** TTA 8 phép biến đổi kết hợp ensemble 3 mô hình tăng forward passes lên 24 lần, làm latency vọt lên ~120 phút gây lỗi Time Limit Exceeded
- **B.** Kỹ thuật TTA chỉ áp dụng được cho các mô hình mạng nơ-ron tích chập 1D chứ không dùng được cho ảnh tài liệu hai chiều
- **C.** TTA làm giảm vĩnh viễn độ chính xác phân loại trên tập kiểm tra do phá vỡ hoàn toàn cấu trúc không gian hình học của tài liệu
- **D.** Quy chế thi Olympic AI cấm tuyệt đối việc sử dụng TTA và sẽ trừ trực tiếp 50% tổng điểm số bài thi nếu phát hiện trong mã nguồn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Giống như trong 15 phút cuối giờ làm bài kiểm tra, bạn đã làm xong bài và chuẩn bị nộp bài. Một người bạn xúi bạn: ' Hãy chép lại bài làm này ra 8 thứ tiếng khác nhau rồi so sánh từng chữ xem có sai sót gì không để ăn thêm 0.25 điểm!' Bạn cặm cụi ngồi chép, chưa chép xong bản thứ hai thì tiếng trống hết giờ vang lên. Giám thị thu bài khi bài làm chính thức của bạn còn chưa kịp nộp vào giỏ, và bạn bị 0 điểm vì phạm quy nộp trễ!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Bảng tính toán Runtime thực tế:
  + Giả sử 1 ảnh inference qua 1 backbone tốn $0.05$ giây trên GPU.
  + Ensemble 3 backbones: $0.05 \times 3 = 0.15$s / ảnh.
  + Không dùng TTA (1x): $2.500 \times 0.15 = 375$ giây = 6.25 phút $\rightarrow$ NẰM TRONG VÙNG AN TOÀN (< 20 phút).
  + Bật TTA 8-biến đổi: Số forward passes $= 3 \times 8 = 24$ lần/ảnh.
  + Tổng thời gian inference: $2.500 \times 0.05 \times 24 = 3.000$ giây = 50 PHÚT!
  + Giới hạn máy chấm tự động: `timeout 1200 python main.py` (20 phút = 1.200 giây).
  + Kết quả: Quá trình bị ngắt bằng tín hiệu `SIGKILL` tại phút thứ 20, file `submission.csv` không được ghi hoàn tất hoặc trống $\rightarrow$ ĐIỂM 0 TRÒN TRĨNH!

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy B: Quy chế không cấm TTA, ban tổ chức chỉ chấm file `submission.csv` và kiểm tra thời gian thực thi của script.
- Bẫy C: TTA thực tế giúp tăng nhẹ độ chính xác nhờ triệt tiêu phương sai, nhưng cái giá phải trả về thời gian là quá đắt.
- Bẫy D: TTA dùng phổ biến nhất cho ảnh 2D và video 3D.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Chiến lược phòng thi được giảng viên đúc kết thành châm ngôn: ' Chạy xong an toàn có điểm còn hơn điểm cao trên giấy mà dính TLE '. Trong 1 giờ cuối, ưu tiên số 1 là: Tắt toàn bộ TTA nặng, chỉ giữ 1-2 mô hình suy luận nhanh nhất, chạy thử trên tập sample 50 ảnh đo đếm số giây, nhân tỷ lệ với toàn bộ test set. Nếu tổng thời gian dự kiến $> 12$ phút, lập tức cắt giảm mô hình!

---

### Câu 20 [OLP04-Q20] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** [VOAI-VID-20] Khi mã hóa một biến phân loại có số lượng nhóm lớn (high cardinality, ví dụ 1.000 mã tỉnh/huyện) bằng trung bình biến mục tiêu (Target Encoding), các nhóm chỉ có 1 hoặc 2 mẫu trong tập dữ liệu rất dễ khiến mô hình học thuộc lòng nhãn và Overfitting nặng. Công thức làm mịn màng (Smoothing / M-Estimate) nào sau đây được giảng viên chỉ định để kéo giá trị mã hóa của các nhóm hiếm về giá trị trung bình toàn cục?

- **A.** $x_c = y_{\text{mean\_group}} + \ln(1 + m \cdot n_c)$ điều chỉnh phi tuyến tính theo số lượng mẫu quan sát được
- **B.** $x_c = y_{\text{group}} \cdot \exp(-n_c)$ làm suy giảm trọng số nhóm theo hàm số mũ cơ số tự nhiên
- **C.** $x_c = \frac{n_c \cdot y_{\text{mean\_group}} + m \cdot y_{\text{global}}}{n_c + m}$ kéo giá trị nhóm hiếm về trung bình toàn cục $y_{\text{global}}$
- **D.** $x_c = \frac{y_{\text{mean\_group}} - y_{\text{global}}}{n_c^2 + 1}$ chuẩn hóa độ lệch chuẩn theo bình phương kích thước nhóm

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Tưởng tượng bạn muốn đánh giá tỷ lệ đỗ đại học của học sinh theo từng trường cấp ba. Nếu một trường có 1.000 học sinh đi thi và 900 bạn đỗ, tỷ lệ 90% là cực kỳ tin cậy. Nhưng nếu một trường vùng sâu vùng xa năm nay chỉ có đúng 1 học sinh đi thi và bạn đó may mắn đỗ thủ khoa, bạn có dám khẳng định trường đó có tỷ lệ đỗ 100% không? Chắc chắn không! Công thức Smoothing giống như việc bạn thêm vào một lượng ' học sinh giả định ' $m$ có tỷ lệ đỗ bằng mức trung bình của cả nước ($y_{\text{global}}$). Với trường có ít học sinh, con số đánh giá sẽ tự động được kéo về mức trung bình cả nước cho an toàn; còn với trường có hàng nghìn học sinh, số liệu thực tế của trường sẽ chiếm ưu thế hoàn toàn!

### 2. Đạo hàm & Luận chứng kỹ thuật từng bước
- Công thức M-Estimate / Bayesian Smoothing:
  $$\hat{x}_c = \frac{n_c \cdot \bar{y}_c + m \cdot y_{\text{global}}}{n_c + m} = \lambda(n_c) \cdot \bar{y}_c + (1 - \lambda(n_c)) \cdot y_{\text{global}}$$
  với hệ số trọng số: $\lambda(n_c) = \frac{n_c}{n_c + m} \in [0, 1)$.
- Phân tích giới hạn biên:
  + Khi nhóm cực hiếm ($n_c = 1, m = 10$): $\lambda(1) = \frac{1}{11} \approx 0.09$. Giá trị mã hóa nhận $91\%$ thông tin từ trung bình toàn cục $y_{\text{global}}$, triệt tiêu rủi ro học thuộc nhãn.
  + Khi nhóm rất phổ biến ($n_c = 1.000, m = 10$): $\lambda(1000) = \frac{1000}{1010} \approx 0.99$. Giá trị mã hóa nhận $99\%$ từ trung bình thực tế của nhóm $\bar{y}_c$.
- Kết hợp kỹ thuật Out-of-Fold (K-Fold Target Encoding): Tính $\bar{y}_c$ chỉ trên các fold huấn luyện khác, tuyệt đối không chứa mẫu hiện tại.

### 3. Phân tích bẫy đề thi & Các phương án sai
- Bẫy A: Hàm mũ $\exp(-n_c)$ làm giá trị tiến về 0 khi số mẫu lớn, hoàn toàn sai lệch logic.
- Bẫy B: Phép cộng logarit làm thay đổi thang đo của biến mục tiêu, không phải là phép bình quân gia quyền.
- Bẫy D: Hiệu số chia cho bình phương làm biến mất thông tin định lượng của nhãn.

### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến
Giảng viên chỉ ra kinh nghiệm thực chiến: Tham số làm mịn $m$ thường được chọn trong khoảng $m \in [5, 20]$ tùy thuộc vào độ biến thiên phương sai của nhãn. Trong thư viện `category_encoders. TargetEncoder`, tham số này tương ứng với `smoothing`.

---

### Câu 21 [OLP04-Q21] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [SCENARIO AUDIT - HISTORICAL DOCUMENT OCR] Trong bài toán xử lý ảnh tài liệu văn bản lịch sử bị ố vàng, nhòe mực và độ tương phản không đồng đều, thuật toán nhị phân hóa cục bộ thích nghi Sauvola (Sauvola Adaptive Binarization) với ngưỡng $T(x, y) = m(x, y) [1 + k (\frac{s(x, y)}{R} - 1)]$ vượt trội hơn ngưỡng toàn cục Otsu ở điểm kỹ thuật cốt lõi nào?

- **A.** Tính toán ngưỡng biến thiên theo từng cửa sổ lân cận cục bộ dựa trên độ lệch chuẩn, bảo toàn nét chữ mờ trên nền ố
- **B.** Tự động dịch chuỗi ký tự Hán Nôm sang chữ Quốc ngữ mà không cần bước nhận dạng ký tự quang học OCR
- **C.** Loại bỏ hoàn toàn các điểm ảnh nhiễu muối tiêu bằng phép biến đổi hình thái học đóng Closing
- **D.** Tăng độ phân giải không gian của ảnh lên 4 lần thông qua phép nội suy song bậc hai Bicubic

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ngưỡng Otsu dùng 1 con số duy nhất cho cả trang giấy. Nếu góc trên sáng góc dưới ố vàng tối thui, Otsu sẽ biến góc dưới thành một bãi đen xì! Sauvola tính trung bình $m$ và độ lệch chuẩn $s$ trong từng ô vuông nhỏ: chỗ sáng tự đặt ngưỡng cao, chỗ tối tự hạ ngưỡng thấp, giúp chữ mờ trên nền loang lổ hiện rõ mồn một.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $T(x, y) = m(x, y) [1 + k (\frac{s(x, y)}{R} - 1)]$. $R$ là độ lệch chuẩn cực đại (thường $R=128$), $k \in [0.2, 0.5]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Sauvola là thuật toán tiền xử lý ảnh nhị phân hóa pixel, không phải OCR dịch văn bản (loại B) hay siêu phân giải (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 22 [OLP04-Q22] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [SCENARIO AUDIT - FACE VERIFICATION] Khi huấn luyện mạng nơ-ron xác minh danh tính khuôn mặt (Face Verification) từ các cặp ảnh Pos/Neg với hàm mất mát ArcFace (Additive Angular Margin Loss), số hạng lề góc $m > 0$ được cộng vào đâu trong biểu thức toán học?

- **A.** Duy trì tỷ lệ nén cố định (Constant Bitrate Encoding) giúp tối ưu hóa dung lượng truyền tải mạng nhưng làm suy giảm chất lượng các khung hình chuyển động
- **B.** Phân bổ số lượng bit biến thiên theo độ phức tạp không gian và thời gian (VBR - Variable Bitrate) nhằm duy trì chất lượng thị giác đồng đều toàn video
- **C.** Loại bỏ hoàn toàn các khung hình nội suy B-frame (Bidirectional Predictive Frame) để giảm thiểu độ trễ giải mã trong các ứng dụng thời gian thực
- **D.** Tăng kích thước khối bù chuyển động (Macroblock Size Expansion) lên $64 \times 64$ nhằm triệt tiêu hiện tượng phân mảnh khối ở các vùng biên sắc nét

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
ArcFace đưa mọi khuôn mặt lên bề mặt quả cầu (chuẩn hóa độ dài vector bằng 1). Để ép mạng phải gom mặt cùng 1 người lại gần nhau hơn, ArcFace cộng thêm một ' góc phạt ' $m$ vào góc $\theta$: $\cos(\theta + m)$. Vì hàm $\cos$ nghịch biến, góc bị cộng thêm làm điểm số tụt xuống, buộc mạng phải kéo góc thực $\theta$ nhỏ hơn nữa để bù lại!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $L_{\text{ArcFace}} = -\log \frac{e^{s \cos(\theta_{y_i} + m)}}{e^{s \cos(\theta_{y_i} + m)} + \sum_{j \ne y_i} e^{s \cos(\theta_j)}}$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** CosFace cộng $m$ bên ngoài: $\cos(\theta) - m$, còn ArcFace cộng góc bên trong $\cos(\theta + m)$. Chọn B.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 23 [OLP04-Q23] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [SCENARIO AUDIT - SIGN LANGUAGE VIDEO GCN] Trong kiến trúc mạng đồ thị không gian - thời gian (ST-GCN) xử lý chuỗi cử chỉ tay từ video, ma trận kề mở rộng $\tilde{A}$ kết hợp thông tin liên kết giữa các khớp ngón tay theo hai chiều nào?

- **A.** Khoảng cách Cosine (Cosine Similarity Metric) chỉ đo góc định hướng giữa hai vector mà bỏ qua hoàn toàn độ lớn biên độ của các vector đặc trưng
- **B.** Khoảng cách Mahalanobis (Mahalanobis Distance) chuẩn hóa dữ liệu theo ma trận hiệp phương sai nhưng đòi hỏi ma trận này phải khả nghịch tuyệt đối
- **C.** Khoảng cách Wasserstein (Earth Mover ' s Distance) đo công tối thiểu để chuyển phân phối xác suất này thành phân phối khác, phản ánh hình học thực sự
- **D.** Độ phân kỳ Kullback-Leibler (KL Divergence) là hàm đo phi đối xứng, dễ bùng nổ vô cùng khi giá trị xác suất của phân phối mục tiêu tiến dần về 0

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
ST-GCN nhìn bàn tay cử động như một mạng lưới 3D:
1. Chiều không gian: Ngón trỏ nối với khớp bàn tay trong cùng một bức ảnh (frame).
2. Chiều thời gian: Đầu ngón trỏ ở giây thứ 1 nối thẳng với đầu ngón trỏ ở giây thứ 2. Nhờ đó, thông tin cử động lướt đi mượt mà qua cả không gian lẫn thời gian!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Đồ thị $G = (V, E)$ với $E$ gồm cạnh nội khung (Intra-skeleton edges) và cạnh liên khung thời gian (Inter-frame temporal edges). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** ST-GCN làm việc trên tọa độ khung xương (Keypoints), không dùng kênh RGB (loại A) hay góc camera 3D (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 24 [OLP04-Q24] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** [SCENARIO AUDIT - OFFLINE NMT EMBEDDING] Khi huấn luyện mô hình dịch máy nơ-ron Transformer từ số không (From Scratch) mà không dùng mô hình ngôn ngữ lớn có sẵn, kỹ thuật chia sẻ trọng số ma trận nhúng (Weight Tying: Press & Wolf 2017) giữa Encoder Embedding, Decoder Embedding và Tầng Linear Output giúp giảm bao nhiêu tham số?

- **A.** Giảm khoảng 10% tổng số lượng tham số mô hình và tăng tốc độ hội tụ của thuật toán Adam lên gấp 3 lần trong pha train
- **B.** Loại bỏ hoàn toàn sự cần thiết của hàm mất mát Cross-Entropy trong quá trình huấn luyện mô hình dịch máy từ số không
- **C.** Thu nhỏ kích thước từ điển BPE từ 32.000 token xuống còn 256 byte ký tự cơ sở mà không làm giảm năng lực biểu diễn ngữ nghĩa
- **D.** Tiết kiệm 2 trong 3 ma trận kích thước $V \times d_{\text{model}}$, giảm hàng chục triệu tham số và cải thiện tổng quát hóa từ vựng

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Bình thường ta cần 3 bảng từ điển khổng lồ cỡ $32.000 \times 512 \approx 16$ triệu số: bảng dịch tiếng vào, bảng dịch tiếng ra, và bảng chuyển từ vector thành chữ ở đầu ra. Weight Tying cho cả 3 chỗ này dùng chung 1 bảng duy nhất! Tiết kiệm hơn 30 triệu tham số, vừa nhẹ máy vừa giúp từ vựng học đồng bộ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $W_{\text{enc}} = W_{\text{dec}} = W_{\text{proj}}^T$. Ba ma trận $V \times d_{\text{model}}$ gộp thành 1. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Weight Tying chia sẻ trọng số ma trận, không loại bỏ hàm Cross-Entropy (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 25 [OLP04-Q25] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Bộ lọc Sobel theo trục ngang $G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$ thực chất là tích chập rời rạc của hai bộ lọc một chiều (Separable Filter) nào sau đây?

- **A.** Bộ lọc làm mịn Gauss $[1, 2, 1]^T$ theo chiều dọc và bộ lọc vi phân trung tâm $[-1, 0, 1]$ theo chiều ngang
- **B.** Bộ lọc thông cao Laplace $[1, -2, 1]^T$ theo chiều dọc và bộ lọc trung vị ba điểm theo chiều ngang
- **C.** Bộ lọc trung bình cộng $[1, 1, 1]^T$ theo chiều dọc và bộ lọc sóng con Haar $[1, -1]$ theo chiều ngang
- **D.** Bộ lọc vi phân bậc hai $[-1, 2, -1]^T$ theo chiều dọc và bộ lọc đối xứng chẵn theo chiều ngang

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tìm cạnh đứng trong ảnh nghĩa là: theo chiều ngang phải tính độ chênh lệch màu sắc (vi phân $[-1, 0, 1]$), đồng thời theo chiều dọc phải làm mờ đi một chút để không bị nhiễu hạt đánh lừa (bộ lọc Gauss $[1, 2, 1]^T$). Nhân 2 vector này lại ra đúng ma trận Sobel $3 \times 3$!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \begin{bmatrix} -1 & 0 & 1 \end{bmatrix} = G_x$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Sobel kết hợp làm mịn Gauss bậc nhất và vi phân bậc nhất, không dùng toán tử Laplace bậc hai (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 26 [OLP04-Q26] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán dò biên Canny (Canny Edge Detector), bước triệt tiêu các điểm không cực đại (Non-Maximum Suppression - NMS) trên độ lớn gradient $M(x, y)$ đóng vai trò gì?

- **A.** Làm mịn toàn bộ bức ảnh bằng bộ lọc Gauss hai chiều đối xứng để triệt tiêu các thành phần nhiễu hạt tần số cao
- **B.** Làm mỏng các đường biên dày thành các đường có độ dày đúng 1 pixel bằng cách so sánh cực đại cục bộ dọc hướng gradient
- **C.** Phân loại các đường biên thành hai tập hợp độc lập dựa trên hai ngưỡng hysteresis cao và thấp để nối liền nét đứt
- **D.** Tính toán góc định hướng của cạnh và lượng tử hóa góc vào bốn cung phần tư hình học phẳng trước khi trích xuất đặc trưng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Sau khi lọc Sobel, cạnh biên trông như một vệt sáng dày cộp 3-4 pixel. NMS đi dọc theo hướng vuông góc với cạnh: trong đám pixel sáng đó, chỉ giữ lại pixel nào sáng rực rỡ nhất (cực đại cục bộ) và dập tắt các pixel bên cạnh, biến vệt dày thành đường mảnh tinh tế dày đúng 1 pixel!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nếu $M(p) < M(q)$ hoặc $M(p) < M(r)$ dọc theo hướng gradient $\theta(p)$, gán $M(p) = 0$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Lọc hysteresis hai ngưỡng là bước kế tiếp sau NMS (loại C); làm mịn là bước đầu tiên (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 27 [OLP04-Q27] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Biến đổi Hough (Hough Transform) chuyển đổi bài toán phát hiện đường thẳng trong không gian ảnh $(x, y)$ sang bài toán tích lũy phiếu bầu (Voting) trong không gian tham số cực $(\rho, \theta)$ theo phương trình đường thẳng nào?

- **A.** $\rho = x^2 + y^2 - \theta^2$ theo phương trình đường tròn đồng tâm
- **B.** $\rho = y - mx - c$ theo dạng độ dốc tiệm cận không xác định khi đường thẳng thẳng đứng
- **C.** $\rho = x \cos(\theta) + y \sin(\theta)$, với $\rho$ là khoảng cách từ gốc tọa độ đến đường thẳng và $\theta$ là góc pháp tuyến
- **D.** $\rho = \frac{x}{\cos(\theta)} + \frac{y}{\sin(\theta)}$ theo phương trình đoạn chắn trên các trục

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Dùng phương trình $y = mx + b$ sẽ bị lỗi chia cho 0 khi gặp đường thẳng đứng ($m = \infty$). Không gian cực $(\rho, \theta)$ dùng phương trình $\rho = x \cos\theta + y \sin\theta$. Mỗi điểm ảnh biến thành một đường sóng hình sin trong không gian cực. Giao điểm của nhiều đường sóng sin chính là đường thẳng đi qua các điểm đó!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tọa độ cực: $\rho = x \cos\theta + y \sin\theta$. Các điểm thẳng hàng có các đường sin giao nhau tại cùng $(\rho^*, \theta^*)$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Dạng $y = mx + b$ (loại B) bị kỳ dị tại đường thẳng đứng.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 28 [OLP04-Q28] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán phát hiện góc Harris Corner Detector phân loại một điểm ảnh là góc (Corner) dựa trên hai trị riêng $\lambda_1, \lambda_2$ của ma trận cấu trúc tự tương quan $M = \sum w(x, y) \begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix}$ khi nào?

- **A.** Cả hai trị riêng $\lambda_1$ và $\lambda_2$ đều rất nhỏ xấp xỉ bằng 0 (vùng đồng nhất bằng phẳng)
- **B.** Một trị riêng rất lớn và một trị riêng xấp xỉ bằng 0 (vùng biên cạnh đơn hướng)
- **C.** Hai trị riêng có giá trị bằng nhau nhưng mang dấu âm đối xứng qua trục hoành
- **D.** Cả hai trị riêng $\lambda_1$ và $\lambda_2$ đều có giá trị dương lớn (gradient biến thiên mạnh theo cả hai hướng)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Vùng phẳng (Flat): Di chuyển cửa sổ theo hướng nào màu cũng không đổi $\implies \lambda_1, \lambda_2 \approx 0$.
- Cạnh (Edge): Chỉ đổi màu khi đi vuông góc với cạnh $\implies$ 1 trị riêng to, 1 trị riêng bé.
- Góc (Corner): Đi hướng nào màu cũng đổi mãnh liệt $\implies$ Cả $\lambda_1$ và $\lambda_2$ đều cực to!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Chỉ số phản hồi $R = \det(M) - k (\text{Tr}(M))^2 = \lambda_1 \lambda_2 - k(\lambda_1 + \lambda_2)^2$. Điểm góc khi $R > 0$ và $\lambda_1, \lambda_2$ lớn. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B là đặc trưng của Cạnh (Edge), Phương án A là vùng phẳng (Flat).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 29 [OLP04-Q29] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán SIFT (Scale-Invariant Feature Transform) đạt được tính bất biến với tỷ lệ kích thước ảnh (Scale Invariance) nhờ kỹ thuật trích xuất điểm đặc trưng trên cấu trúc không gian nào?

- **A.** Tìm cực trị cục bộ trên không gian sai phân các hàm Gauss (Difference of Gaussians - DoG) qua nhiều thang tỉ lệ Octave
- **B.** Phóng to ảnh đầu vào bằng mạng nơ-ron sinh đối kháng GAN siêu phân giải đa mức trước khi áp dụng bộ lọc đạo hàm
- **C.** Chuyển ảnh sang miền tần số Fourier 2D và lọc bỏ toàn bộ các tần số góc trên đường chéo phụ của phổ công suất
- **D.** Áp dụng biến đổi phối cảnh ngẫu nhiên (Random Perspective) 100 lần trên mỗi điểm ảnh để học biểu diễn bất biến tỷ lệ

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Một vật ở gần trông rất to, ở xa trông rất nhỏ. SIFT làm mờ ảnh ở nhiều cấp độ khác nhau bằng hàm Gauss rồi lấy hiệu giữa hai ảnh mờ kế tiếp (DoG: Difference of Gaussians). Điểm nào là đỉnh chóp (cực trị) trong cả không gian ảnh lẫn thang độ mờ thì điểm đó sẽ bất biến dù phóng to hay thu nhỏ ảnh!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $D(x, y, \sigma) = (G(x, y, k\sigma) - G(x, y, \sigma)) * I(x, y) \approx (k-1)\sigma^2 \nabla^2 G$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** SIFT dựa trên DoG xấp xỉ Laplacian of Gaussian (LoG), không dùng GAN (loại B) hay Fourier (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 30 [OLP04-Q30] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình Bag of Visual Words (BoVW) cho phân loại ảnh cổ điển, ma trận từ điển thị giác (Visual Vocabulary / Codebook) được tạo ra bằng thuật toán nào áp dụng trên các vector đặc trưng cục bộ (như SIFT)?

- **A.** Phân tích cú pháp cây ngữ pháp xác suất phi ngữ cảnh (PCFG Parsing) trên chuỗi các điểm ảnh lân cận trong không gian màu biểu diễn RGB
- **B.** Chiếu ngẫu nhiên các mẩu ảnh vào từ điển trực quan (Visual Bag-of-Words) rồi phân loại bằng mô hình máy vector hỗ trợ tuyến tính SVM
- **C.** Giải thuật phân rã giá trị kỳ dị (Singular Value Decomposition - SVD) rút gọn ma trận đặc trưng cục bộ về hạng 1 duy nhất trước khi lượng tử hóa
- **D.** Mạng nơ-ron hồi quy hai chiều (Bi-directional LSTM) kết hợp cơ chế chú ý liên tục để xâu chuỗi các điểm đặc trưng hình học qua các khung hình

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Rút trích hàng triệu vector SIFT từ các ảnh, thuật toán K-Means gom chúng thành $K$ cụm (ví dụ 1000 cụm). Tâm của mỗi cụm chính là một ' từ thị giác ' (visual word). Mỗi bức ảnh sau đó được tóm tắt thành biểu đồ tần suất xuất hiện các từ này!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Codebook $\mathcal{C} = \{c_1, \dots, c_K\}$ sinh ra từ K-Means trên tập SIFT descriptors. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** BoVW là phương pháp học máy truyền thống, dùng K-Means để lượng tử hóa đặc trưng vector.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Giảm Chiều Dữ Liệu (Dimensionality Reduction)**.

---

### Câu 31 [OLP04-Q31] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Khai phá Mẫu âm Khó (Hard Negative Mining) trong bài toán huấn luyện bộ phát hiện vật thể (như SVM với HOG) cải thiện độ chính xác bằng cơ chế nào?

- **A.** Tự động đảo ngược nhãn của các mẫu dương có độ tin cậy dự đoán thấp hơn ngưỡng 0.5 (False Negatives) để cân bằng phân phối dữ liệu huấn luyện
- **B.** Xóa bỏ toàn bộ các mẫu dữ liệu có khoảng cách Mahalanobis lớn hơn 3 độ lệch chuẩn (Outlier Pruning) so với trọng tâm phân phối toàn cục
- **C.** Lọc các vùng ảnh nền bị đoán nhầm thành vật thể (False Positives) nạp lại làm mẫu âm khó để huấn luyện lại mô hình phát hiện đối tượng
- **D.** Thêm nhiễu ngẫu nhiên vào tọa độ bounding box của các mẫu dương (Box Jittering) nhằm mở rộng kích thước hộp và tăng độ bao phủ vùng giao

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ảnh có hàng triệu vùng nền (mặt đường, tán cây), mô hình không thể học hết. Chạy mô hình trên ảnh: nếu nó nhìn nhầm bụi cây thành người (đoán sai, False Positive), ta ' bắt quả tang ' vùng bụi cây đó, dán nhãn lại là ' Âm tính ' và bắt mô hình học lại thật kỹ để lần sau không bị lừa nữa!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tập $\mathcal{H}_{\text{neg}} = \{x \in \mathcal{D}_{\text{bg}} \mid f(x) > 0\}$. Cập nhật tập train: $\mathcal{D} \leftarrow \mathcal{D} \cup \mathcal{H}_{\text{neg}}$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Hard Negative là mẫu âm bị đoán nhầm thành dương (False Positive), không phải đảo nhãn mẫu dương (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Support Vector Machines (SVM)**.

---

### Câu 32 [OLP04-Q32] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mạng AlexNet (Krizhevsky et al., ImageNet 2012) ghi dấu mốc lịch sử hồi sinh Deep Learning nhờ ứng dụng đột phá của thành phần nào sau đây?

- **A.** Cơ chế chú ý Transformer Self-Attention trên chuỗi điểm ảnh tuần tự thay thế hoàn toàn cho các tầng tích chập Conv2D
- **B.** Thuật toán giải mã Beam Search kết hợp với ma trận hiệp phương sai thưa để tìm kiếm ranh giới phân loại tối ưu
- **C.** Tầng tích chập giãn nở Dilated Convolution với hệ số dãn nở bậc bốn giúp mở rộng trường tiếp nhận mà không tăng tham số
- **D.** Hàm kích hoạt ReLU, kỹ thuật điều chuẩn Dropout và tăng tốc tính toán song song trên GPU mở ra kỷ nguyên Deep Learning

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trước AlexNet, mạng sâu dùng Sigmoid bị triệt tiêu gradient nên học rất chậm. AlexNet thay bằng ReLU (học nhanh gấp 6 lần), thêm Dropout (chống học vẹt), và tận dụng sức mạnh tính toán song song của 2 card đồ họa GPU Nvidia GTX 580, nghiền nát hoàn toàn các phương pháp thị giác truyền thống!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 ReLU $\max(0, x)$, Dropout $p=0.5$, 2x GPU CUDA. Giảm Top-5 error từ $26\%$ xuống $15.3\%$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** AlexNet năm 2012 chưa có Transformer (2017) hay Dilated Convolution (2015).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 33 [OLP04-Q33] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc GoogLeNet (Inception-v1), mục đích chính của việc đặt các tầng tích chập $1 \times 1$ ngay trước các tầng tích chập $3 \times 3$ và $5 \times 5$ là gì?

- **A.** Giảm số lượng kênh đặc trưng (Dimensionality Reduction / Bottleneck) để giảm mạnh chi phí tính toán FLOPs cho tầng tích chập không gian kế tiếp
- **B.** Tăng kích thước không gian chiều rộng và chiều cao (Spatial Upsampling) của feature map lên gấp đôi trước khi thực hiện phép tích chập $3 \times 3$
- **C.** Loại bỏ hoàn toàn các giá trị kích hoạt âm (Negative Feature Suppression) mà không cần thông qua hàm kích hoạt phi tuyến tính ReLU ở các tầng sau
- **D.** Đảm bảo tất cả các feature map đều đạt chuẩn tắc hóa (Zero-Mean Normalization) với trung bình bằng 0 và phương sai bằng 1 theo chuẩn phân phối Gauss

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tích chập $5 \times 5$ trực tiếp trên 192 kênh rất tốn kém (hàng triệu phép tính). GoogLeNet chèn một tầng $1 \times 1$ để nén 192 kênh xuống chỉ còn 32 kênh (nhẹ đi 6 lần!), sau đó tầng $5 \times 5$ chỉ cần tính trên 32 kênh này. Nhờ thủ thuật ' cổ chai ' này, mạng tính nhanh hơn rất nhiều!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Conv $1 \times 1$ chiếu từ $C_{\text{in}} \to C_{\text{mid}} \ll C_{\text{in}}$. FLOPs giảm từ $H W C_{\text{in}} K^2 C_{\text{out}}$ xuống $H W C_{\text{in}} C_{\text{mid}} + H W C_{\text{mid}} K^2 C_{\text{out}}$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Conv $1 \times 1$ giữ nguyên kích thước không gian $H \times W$, chỉ thay đổi số kênh $C$ (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 34 [OLP04-Q34] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc DenseNet (Huang et al., 2017) kết nối các tầng mạng theo cơ chế kết nối dày đặc (Dense Connectivity). Điểm khác biệt cơ bản giữa cách kết hợp đặc trưng của DenseNet so với ResNet là gì?

- **A.** DenseNet nhân từng phần tử các feature map với nhau (Element-wise Product) trong khi ResNet sử dụng phép chia ma trận chuẩn hóa kênh chéo
- **B.** ResNet thực hiện phép cộng phần tử ($x_l = H(x_{l-1}) + x_{l-1}$) trong khi DenseNet ghép nối kênh (Channel Concatenation: $[x_0, x_1, \dots, x_{l-1}]$)
- **C.** DenseNet chỉ sử dụng duy nhất một tầng tích chập (Single Conv Layer) trong toàn bộ mạng và dựa vào các tầng kết nối đầy đủ Dense phía sau
- **D.** ResNet không sử dụng bất kỳ hàm kích hoạt phi tuyến tính nào (Linear Path) giữa các khối phần dư để bảo toàn trọn vẹn đặc trưng tín hiệu

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- ResNet: Cộng dồn dòng nước ($x + F(x)$), các đặc trưng hòa tan vào nhau.
- DenseNet: Ghép thêm ghế vào toa tàu (Concatenate: $[x_0, x_1, \dots, x_l]$). Tầng sau nhìn thấy nguyên vẹn đặc trưng của TẤT CẢ các tầng trước đó xếp cạnh nhau, giúp tái sử dụng đặc trưng triệt để và gradient truyền thẳng tắp!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 ResNet: $x_l = H_l(x_{l-1}) + x_{l-1}$. DenseNet: $x_l = H_l([x_0, x_1, \dots, x_{l-1}])$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** DenseNet dùng `torch.cat` (nối kênh), ResNet dùng `+` (cộng từng phần tử).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 35 [OLP04-Q35] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp tỷ lệ hợp chất (Compound Scaling) trong kiến trúc EfficientNet (Tan & Le, 2019) tối ưu hóa việc mở rộng mạng nơ-ron bằng cách cân bằng đồng thời ba chiều nào với hệ số $\phi$?

- **A.** Tốc độ học (Learning Rate), Kích thước Batch size, và Số lượng Epoch huấn luyện theo lịch trình suy giảm Cosine
- **B.** Hệ số Momentum, Hệ số Weight Decay, và Ngưỡng Gradient Clipping theo các tỷ lệ lũy thừa cơ số tự nhiên
- **C.** Độ sâu (Depth $d$), Chiều rộng (Width $w$), và Độ phân giải (Resolution $r$) theo tỉ lệ $d = \alpha^\phi, w = \beta^\phi, r = \gamma^\phi$
- **D.** Kích thước Kernel, Bước trượt Stride, và Độ dày đệm Padding của tất cả các tầng tích chập trong mạng nơ-ron sâu

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trước đây, người ta thường chỉ phóng to 1 thứ: hoặc làm mạng thật sâu (nhiều tầng), hoặc thật rộng (nhiều kênh), hoặc nạp ảnh thật to (độ phân giải cao). EfficientNet chứng minh: mở rộng cả 3 thứ cùng một lúc theo một tỷ lệ vàng cân đối sẽ cho hiệu năng vượt trội với lượng tính toán tiết kiệm nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Độ sâu $d = \alpha^\phi$, chiều rộng $w = \beta^\phi$, độ phân giải $r = \gamma^\phi$ thỏa mãn $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Compound Scaling mở rộng kiến trúc mô hình (Depth, Width, Resolution), không phải siêu tham số huấn luyện (loại A, B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 36 [OLP04-Q36] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình phát hiện vật thể hai giai đoạn Faster R-CNN, mạng đề xuất vùng Region Proposal Network (RPN) thay thế phương pháp Selective Search truyền thống bằng cơ chế nào?

- **A.** Áp dụng thuật toán phân cụm quang học Mean-Shift trên các mảng điểm ảnh RGB thô để tìm kiếm các vùng liên thông
- **B.** Quét toàn bộ bức ảnh bằng một cửa sổ trượt kích thước cố định có bước nhảy 1 pixel trên không gian ảnh ban đầu
- **C.** Thuật toán tìm kiếm theo chiều sâu DFS trên đồ thị liên thông các pixel để gom nhóm các vùng có cường độ đồng nhất
- **D.** Dùng mạng FCN trượt trên feature map dự đoán điểm số vật thể và tọa độ vi chỉnh cho tập Anchor Box cố định

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Selective Search chạy trên CPU rất chậm (mất tận 2 giây mỗi ảnh chỉ để đoán xem vật thể nằm ở đâu). RPN cắm thẳng một mạng nơ-ron nhỏ chạy trên GPU ngay trên bản đồ đặc trưng có sẵn, đặt các khung neo (Anchor boxes) ở đủ kích thước và hình dạng, chỉ mất 10 mili-giây để chỉ ra vùng có vật thể!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 RPN đầu ra gồm 2 nhánh: nhánh phân loại vật thể ($2k$ điểm số) và nhánh hồi quy tọa độ ($4k$ tọa độ) cho $k$ anchor boxes. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** RPN chia sẻ feature map với mạng trích xuất đặc trưng chính, tính toán hoàn toàn bằng tích chập FCN trên GPU.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.

---

### Câu 37 [OLP04-Q37] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Sự khác biệt kỹ thuật then chốt giữa tầng RoIAlign (trong Mask R-CNN) và RoIPool (trong Fast R-CNN) khi lượng tử hóa vùng quan tâm là gì?

- **A.** RoIAlign tránh hoàn toàn việc làm tròn số nguyên (Misalignment) bằng cách nội suy song tuyến tính tại các điểm mẫu liên tục
- **B.** RoIPool sử dụng phép nội suy song tuyến tính trong khi RoIAlign làm tròn số nguyên thô tại các ranh giới bin lượng tử hóa
- **C.** RoIAlign loại bỏ hoàn toàn các kênh đặc trưng có giá trị âm trước khi gom cụm để đảm bảo tính xác định dương của tensor
- **D.** RoIPool có độ chính xác cao hơn RoIAlign trong bài toán phân đoạn thể hiện (Instance Segmentation) trên các vật thể nhỏ

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi thu nhỏ ảnh 16 lần, hộp tọa độ 25 pixel biến thành $25 / 16 = 1.5625$. RoIPool ' chém thẳng tay ' làm tròn thành 1 (mất $0.56$ ô, tức lệch tận 9 pixel trên ảnh thật!). Với Bounding Box thì lệch một chút không sao, nhưng vẽ viền mặt nạ chi tiết từng pixel (Mask R-CNN) thì hỏng bét. RoIAlign giữ nguyên số lẻ $1.5625$ và tính màu bằng phép nội suy song tuyến tính mượt mà!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 RoIAlign lấy 4 điểm mẫu đều nhau trong mỗi bin và tính giá trị bằng nội suy song tuyến tính từ 4 pixel lân cận: $f(x, y) \approx \sum w_i f(x_i, y_i)$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B nói ngược hoàn toàn (RoIAlign mới là bên dùng nội suy song tuyến tính).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.

---

### Câu 38 [OLP04-Q38] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hàm mất mát Focal Loss $\text{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \ln(p_t)$ trong RetinaNet giải quyết bài toán mất cân bằng nghiêm trọng giữa mẫu âm (nền hậu cảnh) và mẫu dương (vật thể) bằng cơ chế nào với siêu tham số tập trung $\gamma > 0$?

- **A.** Tăng gấp đôi trọng số phạt đối với các mẫu dự đoán có độ tin cậy rất cao $p_t \approx 1$ (Hard Easy Mining) để ép mô hình học thuộc lòng
- **B.** Làm suy giảm mạnh mẽ (Down-weight) mất mát của các mẫu dễ ($p_t > 0.5$) qua thừa số $(1 - p_t)^\gamma$, dồn gradient vào các mẫu khó
- **C.** Triệt tiêu hoàn toàn gradient của các mẫu khó (Hard Example Suppression) và chỉ tối ưu hóa các mẫu dễ phân loại để đảm bảo hội tụ ổn định
- **D.** Loại bỏ hàm logarit tự nhiên và thay bằng hàm khoảng cách tuyệt đối tuyến tính (L1 Distance Loss) nhằm tăng tốc độ tính toán phần cứng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong 100.000 hộp neo, có 99.900 hộp chỉ chứa bầu trời/mặt đường (mẫu dễ, $p_t \approx 0.99$). Dù mỗi hộp chỉ sinh ra tí xíu lỗi, cộng 99.900 cái lại sẽ tạo thành một cơn sóng thần lấn át hoàn toàn các vật thể thực sự. Focal Loss nhân thêm $(1 - 0.99)^2 = 0.0001$, dìm chết 99.99% đóng góp của các mẫu dễ, buộc mạng phải dồn toàn bộ sự chú ý vào các mẫu khó!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khi $p_t \to 1$, $(1 - p_t)^\gamma \to 0$, mất mát triệt tiêu. Khi $p_t \to 0$, $(1 - p_t)^\gamma \to 1$, giữ nguyên phạt nặng. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Focal Loss phạt nặng mẫu khó ($p_t$ nhỏ), dìm mẫu dễ ($p_t$ to). Phương án A và C phát biểu ngược.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.3 Hàm Mất Mát (Loss Functions)**.

---

### Câu 39 [OLP04-Q39] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình phát hiện vật thể DETR (DEtection TRansformer - Carion et al., ECCV 2020) loại bỏ hoàn toàn các kỹ thuật thủ công như Anchor Boxes và Non-Maximum Suppression (NMS) bằng cách sử dụng cơ chế nào để khớp dự đoán với nhãn thực tế?

- **A.** Phép chiếu hình học ngẫu nhiên trên mặt cầu đơn vị (Random Spherical Projection) kết hợp với thuật toán phân loại khoảng cách Euclid gần nhất
- **B.** Thuật toán tìm kiếm theo chiều sâu (Depth-First Search Graph Traversal) trên đồ thị liên thông các pixel để gom nhóm các điểm ảnh cùng đối tượng
- **C.** Ghép cặp lưỡng phân tối ưu (Bipartite Matching) qua giải thuật Hungary (Hungarian Algorithm) giữa tập dự đoán và tập nhãn thực tế
- **D.** Gán nhãn ngẫu nhiên dựa trên khoảng cách Cosine (Cosine Similarity Assignment) giữa các vector truy vấn mà không cần hàm mất mát giám sát

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
DETR coi phát hiện vật thể như một bài toán ' ghép đôi ': mạng luôn dự đoán ra đúng 100 hộp. Thuật toán Hungary (Hungarian matching) tìm cách ghép 1-1 tối ưu nhất giữa các hộp dự đoán với các vật thể thật (Ground Truth) sao cho tổng sai số nhỏ nhất. Vì mỗi vật thể thật chỉ được ghép với đúng 1 hộp dự đoán duy nhất, không bao giờ có hiện tượng nhiều hộp trùng nhau $\implies$ vứt bỏ hoàn toàn bước lọc NMS!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\hat{\sigma} = \arg\min_{\sigma \in \mathfrak{S}_N} \sum_{i}^N \mathcal{L}_{\text{match}}(y_i, \hat{y}_{\sigma(i)})$. Giải bằng thuật toán Hungary độ phức tạp $O(N^3)$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** DETR dùng Hungarian Bipartite Matching, không dùng anchor hay NMS.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.

---

### Câu 40 [OLP04-Q40] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc mạng U-Net (Ronneberger et al., MICCAI 2015) cho phân vùng ảnh y sinh đạt độ chính xác phân giải biên vượt trội nhờ vào thành phần cốt lõi nào?

- **A.** Loại bỏ hoàn toàn các tầng tích chập giải mã và chỉ sử dụng phép nội suy láng giềng gần nhất để phóng đại bản đồ đặc trưng
- **B.** Sử dụng hàm kích hoạt tuyến tính ở tất cả các tầng mạng để tăng tốc tính toán và tránh hiện tượng bão hòa gradient
- **C.** Thay thế ma trận điểm ảnh bằng một biểu đồ phân phối xác suất Markov ngẫu nhiên trước khi đưa vào các tầng tích chập
- **D.** Skip Connections sao chép trực tiếp feature map độ phân giải cao từ Encoder sang Decoder để khôi phục ranh giới chi tiết

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi mạng nén ảnh lại để hiểu nội dung (Encoder), chi tiết viền mép bị mất hết. Nhánh Decoder phóng to ảnh ra nhưng viền bị nhòe nhoẹt. U-Net bắc các ' cây cầu ' (Skip connections) bê nguyên xi bản đồ viền nét căng ban đầu từ Encoder dán thẳng sang Decoder, giúp viền khối u được vẽ lại sắc nét từng milimet!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tầng Decoder ghép nối (Concatenate) feature map từ nhánh đối xứng tương ứng ở Encoder trước khi đưa qua Conv $3 \times 3$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** U-Net ghép nối kênh (Concatenation) từ Encoder sang Decoder, không bỏ tầng giải mã (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 41 [OLP04-Q41] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình nhúng từ Word2Vec kiến trúc Skip-Gram với kỹ thuật Lấy mẫu Âm (Negative Sampling), hàm mục tiêu tối đa hóa log-likelihood cho mỗi cặp từ đích $w_t$ và từ ngữ cảnh $w_c$ cùng $K$ từ âm $w_{n_i}$ có dạng toán học nào?

- **A.** $\log \sigma(v_{w_c}'^T v_{w_t}) + \sum_{i=1}^K \log \sigma(-v_{w_{n_i}}'^T v_{w_t})$
- **B.** $\log \left( \frac{\exp(v_{w_c}'^T v_{w_t})}{\sum_{w \in V} \exp(v_w '^T v_{w_t})} \right)$ không sử dụng phép lấy mẫu xấp xỉ
- **C.** $\sum_{i=1}^K (v_{w_c} - v_{w_{n_i}})^2$ theo chuẩn khoảng cách Euclid thuần túy
- **D.** $\prod_{i=1}^K \sigma(v_{w_{n_i}}'^T v_{w_t})$ độc lập với từ ngữ cảnh thực tế

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Softmax trên toàn bộ từ điển 100.000 từ cực kỳ chậm chạp. Negative Sampling biến thành bài toán phân loại nhị phân đơn giản: kéo từ ngữ cảnh thật $w_c$ lại gần (tối đa $\sigma(v_{w_c}'^T v_{w_t})$) và đẩy $K$ từ ngẫu nhiên bốc trúng trong từ điển (mẫu âm) ra xa (tối đa $\sigma(-v_{w_n}'^T v_{w_t})$)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mathcal{L} = \log \sigma(u_c^T v_t) + \sum_{i=1}^K \mathbb{E}_{w_i \sim P_n(w)} [\log \sigma(-u_{w_i}^T v_t)]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B là Softmax toàn cục nguyên bản (rất tốn kém tính toán mẫu số $O(|V|)$).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 42 [OLP04-Q42] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong kỹ thuật Negative Sampling của Word2Vec, phân phối xác suất để chọn một từ $w$ làm mẫu âm thường được nâng lên lũy thừa bao nhiêu (Unigram Distribution $P_n(w)$)?

- **A.** $P_n(w) \propto U(w)^{1.0}$ giữ nguyên tỷ lệ tần suất xuất hiện tự nhiên của từ vựng trong kho ngữ liệu văn bản ban đầu
- **B.** $P_n(w) \propto U(w)^{0.75}$ (lũy thừa $3/4$) giúp tăng xác suất chọn từ hiếm và giảm bớt sự thống trị của các từ dừng
- **C.** $P_n(w) \propto U(w)^{2.0}$ bình phương tần suất xuất hiện để tập trung lấy mẫu độc quyền trên các từ cực kỳ phổ biến
- **D.** $P_n(w) \propto \ln(U(w))$ chỉ sử dụng logarit tự nhiên của tần số xuất hiện nhằm làm phẳng hoàn toàn phân phối xác suất

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu giữ nguyên tần số thực $U(w)^{1.0}$, các từ như ' the ', ' is ', ' a ' sẽ bị bốc làm mẫu âm suốt ngày, còn các từ hiếm như ' hạc ', ' vượn ' không bao giờ được chọn. Lũy thừa $3/4$ ($0.75$) là công thức kinh nghiệm thần kỳ của Mikolov: nó ' nâng đỡ ' các từ hiếm lên một chút và ' ghìm bớt ' các từ cực phổ biến xuống!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $P_n(w) = \frac{f(w)^{3/4}}{\sum_{w '} f(w ')^{3/4}}$. Ví dụ: từ có tần suất $10^{-6}$ tăng tương đối so với từ có tần suất $10^{-2}$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Số mũ kinh nghiệm chuẩn mực của Word2Vec là $0.75$ (hoặc $3/4$), không phải $1.0$ (loại A) hay $2.0$ (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 43 [OLP04-Q43] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình nhúng từ GloVe (Pennington et al., EMNLP 2014) tối ưu hóa hàm mục tiêu dựa trên ma trận đồng xuất hiện toàn cục $X_{ij}$ thông qua phương trình hồi quy có trọng số nào?

- **A.** $J = \sum_{i, j=1}^V \|w_i - \tilde{w}_j\|^2$ không sử dụng thông tin tần suất đồng xuất hiện
- **B.** $J = \sum_{i, j=1}^V \ln(1 + \exp(w_i^T \tilde{w}_j))$ theo dạng hồi quy logistic nhị phân
- **C.** $J = \sum_{i, j=1}^V f(X_{ij}) (w_i^T \tilde{w}_j + b_i + \tilde{b}_j - \ln X_{ij})^2$
- **D.** $J = \prod_{i, j=1}^V \frac{X_{ij}}{\sum_k X_{ik}}$ theo tích xác suất chuyển trạng thái Markov

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
GloVe lập bảng đếm xem hai từ $i$ và $j$ xuất hiện cùng nhau bao nhiêu lần ($X_{ij}$). Sau đó nó ép tích vô hướng của hai vector từ $w_i^T \tilde{w}_j$ (cộng thêm 2 hệ số chệch bias) phải khớp với $\ln(X_{ij})$. Hàm trọng số $f(X_{ij})$ giúp các cặp từ xuất hiện quá nhiều không lấn át mô hình!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $w_i^T \tilde{w}_j + b_i + \tilde{b}_j = \ln(X_{ij})$. Hàm mất mát bình phương có trọng số $f(X_{ij})$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Biểu thức mục tiêu của GloVe khớp với logarit của số lần đồng xuất hiện $\ln X_{ij}$, không phải $X_{ij}$ tuyến tính.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 44 [OLP04-Q44] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình FastText (Bojanowski et al., 2017) khắc phục nhược điểm từ ngoài từ điển (Out-Of-Vocabulary - OOV) của Word2Vec bằng cải tiến kiến trúc cốt lõi nào?

- **A.** Tăng kích thước vector nhúng từ 300 chiều lên 4096 chiều (Dimension Scaling) trên toàn bộ kho từ vựng tĩnh để mở rộng không gian biểu diễn ngữ nghĩa
- **B.** Áp dụng cơ chế mã hóa cặp byte (Byte-Pair Encoding - BPE) trên các văn bản đã dịch song ngữ trước khi chuyển thành vector nhúng biểu diễn từ
- **C.** Sử dụng mạng nơ-ron tích chập 2D (Visual Character CNN) quét qua ma trận điểm ảnh của từng ký tự font chữ để trích xuất đặc trưng hình thái
- **D.** Biểu diễn mỗi từ bằng tổng các vector n-gram ký tự con (Character n-grams) cấu thành nên từ đó cùng với các ký hiệu biên mở đầu kết thúc

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Word2Vec coi mỗi từ là một hòn đá nguyên khối: gặp từ lạ chưa thấy bao giờ (OOV) là chịu chết. FastText băm nhỏ từ thành các mẩu n-gram ký tự (ví dụ từ `<where>` gồm `<wh`, `whe`, `her`, `ere>`, v.v.). Khi gặp một từ mới toanh, FastText chỉ việc cộng vector của các mẩu ký tự con quen thuộc lại là đoán được nghĩa ngay!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $v_w = \sum_{g \in \mathcal{G}_w} z_g$, với $\mathcal{G}_w$ là tập hợp các subword n-grams của từ $w$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** FastText dùng character n-grams trên từ, không dùng font chữ pixel (loại C) hay tăng chiều vector lên 4096 (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 45 [OLP04-Q45] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong cơ chế chú ý cộng tính Bahdanau (Additive Attention - Bahdanau et al., 2014) cho mô hình dịch máy Seq2Seq, điểm số tương đồng căn chỉnh $e_{ij}$ giữa trạng thái ẩn decoder $s_{i-1}$ và trạng thái ẩn encoder $h_j$ được tính bằng công thức nào?

- **A.** $e_{ij} = v_a^T \tanh(W_a s_{i-1} + U_a h_j)$
- **B.** $e_{ij} = s_{i-1}^T h_j$ (tích vô hướng thuần túy Luong dot attention)
- **C.** $e_{ij} = s_{i-1}^T W_a h_j$ (Luong general attention)
- **D.** $e_{ij} = \frac{s_{i-1}^T h_j}{\sqrt{d}}$ (Scaled dot-product attention)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cơ chế Bahdanau dùng một mạng nơ-ron nhỏ gồm 1 tầng ẩn để đo độ ăn khớp: nạp cả trạng thái người hỏi $s_{i-1}$ và người trả lời $h_j$ qua hai ma trận $W_a$ và $U_a$, cộng lại đưa qua hàm phi tuyến $\tanh$, rồi nhân với vector $v_a$ để ra điểm số chú ý.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Bahdanau Additive: $e_{ij} = v_a^T \tanh(W_a s_{i-1} + U_a h_j)$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B, C là Luong Attention (nhân tính Multiplicative); Phương án D là Transformer Scaled Dot-Product.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 46 [OLP04-Q46] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Độ đo đánh giá chất lượng dịch máy tự động BLEU (Bilingual Evaluation Understudy) kết hợp độ chính xác n-gram biến đổi (Modified n-gram Precision) với thừa số phạt độ dài Brevity Penalty (BP). Công thức tính thừa số phạt BP khi độ dài câu dự đoán $c$ nhỏ hơn độ dài câu tham chiếu hiệu dụng $r$ là gì?

- **A.** $\text{BP} = 1.0$ (No Penalty Factor) giữ nguyên điểm số không phạt đối với bất kỳ câu dịch ngắn nào nếu toàn bộ n-gram dự đoán đều chính xác
- **B.** $\text{BP} = \exp(1 - r/c)$ khi $c \le r$ (Brevity Penalty Exponential) phạt hàm mũ kéo tụt điểm BLEU của các bản dịch có độ dài quá ngắn
- **C.** $\text{BP} = \frac{c}{r} - 1$ (Linear Length Deviation) tuyến tính theo hiệu số độ dài giữa câu dự đoán và câu tham chiếu có trong ngữ liệu chuẩn
- **D.** $\text{BP} = 0.0$ (Zero Score Assignment) gán điểm bằng 0 tuyệt đối cho mọi câu dịch ngắn hơn câu tham chiếu chuẩn bất kể độ chính xác n-gram

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu không phạt câu ngắn, mô hình sẽ ' khôn lỏi ': cả câu dài ngoằng nó chỉ dịch đúng 1 từ duy nhất (' the ') và đạt Precision 100%! Thừa số phạt Brevity Penalty (BP) sẽ can thiệp: nếu câu dịch $c$ ngắn hơn câu mẫu $r$, BP sẽ nhân thêm một số nhỏ hơn 1: $\exp(1 - r/c)$ để phạt thật nặng tính ' lười biếng ' này!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\text{BP} = \begin{cases} 1 & \text{nếu } c > r \\ e^{1 - r/c} & \text{nếu } c \le r \end{cases}$. $\text{BLEU} = \text{BP} \cdot \exp\left(\sum w_n \ln p_n\right)$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Khi $c \le r$, số mũ $1 - r/c \le 0 \implies e^{1 - r/c} \le 1$. Chọn B.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.1 Tổng Quan Xử Lý Ngôn Ngữ Tự Nhiên & RNN/LSTM/GRU**.

---

### Câu 47 [OLP04-Q47] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Độ đo ROUGE-L thường được sử dụng trong đánh giá tóm tắt văn bản tự động dựa trên khái niệm nào giữa chuỗi câu dự đoán và chuỗi câu tham chiếu?

- **A.** Khoảng cách chỉnh sửa tối thiểu (Levenshtein Edit Distance) theo từng ký tự đơn lẻ giữa câu dự đoán của mô hình và câu tham chiếu chuẩn mực
- **B.** Tích vô hướng Cosine (Cosine Semantic Similarity) giữa hai vector biểu diễn câu được mã hóa bằng mô hình ngôn ngữ tiền huấn luyện BERT hai chiều
- **C.** Chuỗi con chung dài nhất (Longest Common Subsequence - LCS), không đòi hỏi các từ phải xuất hiện liên tiếp liền kề nhau trong văn bản
- **D.** Tỷ lệ phần trăm từ vựng (Vocabulary Overlap Ratio) xuất hiện đồng thời trong cả hai văn bản dựa trên một từ điển bách khoa toàn thư định trước

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
ROUGE-L (chữ L viết tắt của Longest Common Subsequence) tìm chuỗi các từ xuất hiện chung dài nhất theo đúng thứ tự trước sau, nhưng KHÔNG bắt buộc các từ phải dính liền sát vách nhau. Nhờ đó, nó đánh giá cấu trúc ngữ pháp và luồng thông tin tóm tắt cực kỳ linh hoạt và tự nhiên!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $R_{\text{LCS}} = \frac{\text{LCS}(\text{Ref}, \text{Cand})}{m}$, $P_{\text{LCS}} = \frac{\text{LCS}(\text{Ref}, \text{Cand})}{n}$, $F_{\text{LCS}}$ là harmonic mean. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** ROUGE-N là đếm n-gram liên tiếp, ROUGE-L là chuỗi con chung dài nhất (LCS không cần liên tiếp).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.1 Tổng Quan Xử Lý Ngôn Ngữ Tự Nhiên & RNN/LSTM/GRU**.

---

### Câu 48 [OLP04-Q48] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình BERT (Devlin et al., 2018) được tiền huấn luyện đồng thời trên hai tác vụ học tự giám sát (Self-Supervised Learning) nào?

- **A.** Dự đoán từ tiếp theo tự hồi quy (Autoregressive Causal LM) và Phân loại sắc thái cảm xúc
- **B.** Phục hồi câu bị đảo từ và Phân đoạn ngữ nghĩa ảnh văn bản
- **C.** Tương phản đa phương thức giữa hình ảnh và chú thích văn bản thô
- **D.** Mô hình ngôn ngữ che mặt nạ (Masked Language Model - MLM) và Dự đoán câu kế tiếp (Next Sentence Prediction - NSP)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
BERT học bằng 2 bài tập:
1. MLM (Điền từ vào chỗ trống): giấu 15% số từ bằng thẻ `[MASK]` rồi bắt mạng nhìn ngữ cảnh 2 bên trái phải để đoán từ bị giấu.
2. NSP (Đoán câu tiếp theo): cho 2 câu A và B, bắt mạng trả lời xem câu B có phải câu nối tiếp tự nhiên sau câu A trong sách hay không.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mathcal{L}_{\text{BERT}} = \mathcal{L}_{\text{MLM}} + \mathcal{L}_{\text{NSP}}$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Causal LM (dự đoán từ tiếp theo) là cách học của GPT, không phải BERT.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 49 [OLP04-Q49] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình RoBERTa (Liu et al., 2019) cải tiến quy trình tiền huấn luyện của BERT nguyên bản bằng thay đổi then chốt nào sau đây?

- **A.** Loại bỏ tác vụ NSP, dùng mặt nạ động (Dynamic Masking) và huấn luyện trên tập dữ liệu lớn hơn nhiều với kích thước mini-batch cực lớn
- **B.** Giảm bớt một nửa số tầng Transformer (Layer Pruning) để tăng tốc độ suy luận trong các ứng dụng xử lý ngôn ngữ tự nhiên thời gian thực
- **C.** Thay thế cơ chế Self-Attention bằng mạng nơ-ron hồi quy hai chiều (Bi-LSTM Network) kết hợp với các cổng lọc thông tin có chọn lọc
- **D.** Bổ sung thêm tác vụ dự đoán cú pháp phụ thuộc (Dependency Parsing Task) nhằm tăng cường năng lực nắm bắt cấu trúc ngữ pháp sâu của câu

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nhóm nghiên cứu RoBERTa phát hiện BERT ban đầu bị ' huấn luyện non ' (chưa tới ngưỡng). Họ vứt bỏ bài tập NSP (vì vô dụng và làm giảm điểm), đổi mặt nạ tĩnh thành mặt nạ động đổi mới liên tục sau mỗi epoch, tăng batch size lên 8.000 câu và nhồi thêm dữ liệu đọc sách gấp 10 lần. Kết quả: RoBERTa vượt trội BERT trên mọi bảng xếp hạng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Bỏ $\mathcal{L}_{\text{NSP}}$, Dynamic Masking thay cho static masking, $B = 8192$, token tăng từ 16GB lên 160GB text. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** RoBERTa không giảm tầng mạng (vẫn giữ cấu trúc Transformer 12 hoặc 24 tầng) và không dùng LSTM.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 50 [OLP04-Q50] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc T5 (Text-to-Text Transfer Transformer - Raffel et al., 2020) thống nhất tất cả các tác vụ xử lý ngôn ngữ tự nhiên (dịch thuật, phân loại, tóm tắt, trả lời câu hỏi) vào cùng một định dạng khuôn mẫu nào?

- **A.** Khuôn mẫu phân loại nhãn số nguyên (Integer Classification Head) với một tầng Softmax cố định dùng chung cho toàn bộ các bài toán học máy
- **B.** Khuôn mẫu Văn bản sang Văn bản (Text-to-Text Framework): cả đầu vào và đầu ra của mọi tác vụ đều luôn luôn là các chuỗi văn bản tự nhiên
- **C.** Khuôn mẫu biểu diễn đồ thị không gian (Spatial Graph Representation) kết hợp với các toán tử tích chập trên ma trận kề liên thông đa tầng
- **D.** Khuôn mẫu nén phổ Mel sang vector tiềm ẩn (Acoustic Latent Embedding) phục vụ chuyển đổi đa phương thức giữa âm thanh và văn bản số hóa

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trước T5, bài phân loại cho ra số 0/1, bài dịch ra câu tiếng nước ngoài, bài tóm tắt ra đoạn văn. T5 biến tất cả thành cùng một dạng: Nhập chữ $\to$ Xuất chữ! Muốn phân loại cảm xúc? Nhập: ' sentiment: phim hay ', T5 xuất ra đúng chữ: ' positive '. Cực kỳ đơn giản, thống nhất toàn bộ thế giới NLP vào một mô hình Encoder-Decoder duy nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khung Text-to-Text: $y = \text{Decoder}(\text{Encoder}(x))$. Cùng một kiến trúc, cùng một hàm mất mát Cross-Entropy trên chuỗi token. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** T5 là kiến trúc Encoder-Decoder Text-to-Text, không dùng đầu phân loại nhị phân riêng biệt (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 51 [OLP04-Q51] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình Vision Transformer (ViT - Dosovitskiy et al., ICLR 2021) xử lý một bức ảnh 2D đầu vào kích thước $H \times W \times C$ để đưa vào kiến trúc Transformer Encoder tiêu chuẩn bằng cách nào?

- **A.** Mô hình chỉ dự đoán vector phân phối xác suất trên toàn bộ kho từ vựng và tự động giải nén thông tin tiềm ẩn của toàn câu văn
- **B.** Mô hình sinh tuần tự từng token từ trái sang phải, mỗi token sinh ra được đưa ngược lại làm đầu vào cho bước dự đoán tiếp theo (Autoregressive Generation)
- **C.** Mô hình giải mã đồng thời toàn bộ câu trong một lượt lan truyền tiến duy nhất qua tầng Softmax đa chiều (Non-autoregressive Parallel Decoding)
- **D.** Mô hình tự động đảo ngược thứ tự các từ trong câu nguồn để tối ưu hóa khoảng cách phụ thuộc cú pháp xa giữa các thành phần câu

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Transformer chỉ quen đọc ' từng từ ' (token). Một bức ảnh $224 \times 224$ có tận 50.000 pixel, đưa từng pixel vào sẽ bị nổ bộ nhớ. ViT chia ảnh thành các ô vuông nhỏ $16 \times 16$ (gọi là patch, tổng cộng $14 \times 14 = 196$ ô). Mỗi ô vuông được coi như một ' từ ' trong câu, giúp Transformer xử lý ảnh y hệt như đọc một đoạn văn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Số lượng patch: $N = \frac{HW}{P^2}$. Mỗi patch có kích thước $P^2 C$. Chiếu tuyến tính: $x_p E \in \mathbb{R}^{N \times D}$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** ViT không xử lý từng pixel (loại A) vì độ phức tạp $O((HW)^2)$ không thể tính nổi trên GPU.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 52 [OLP04-Q52] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình ViT, token đặc biệt `[CLS]` (Class Token) được bổ sung vào chuỗi các patch token đầu vào nhằm mục đích chính nào?

- **A.** Top-k giữ lại $k$ token có xác suất cao nhất rồi chuẩn hóa lại; Top-p chọn tập token nhỏ nhất có tổng xác suất tích lũy đạt ngưỡng $p$ (Nucleus Sampling)
- **B.** Top-k chọn ngẫu nhiên đồng đều $k$ token bất kỳ trong từ điển; Top-p chỉ chọn duy nhất token có giá trị xác suất lớn nhất vượt ngưỡng xác suất $p$
- **C.** Top-k áp dụng cho các mô hình Transformer phân loại; Top-p chỉ áp dụng riêng cho các kiến trúc mạng nơ-ron hồi quy tuần tự sinh văn bản
- **D.** Top-k làm tăng phương sai phân phối bằng hàm lũy thừa bậc cao; Top-p làm phẳng phân phối xác suất bằng cách nhân thêm hệ số phạt lặp lại

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
ViT mượn ý tưởng token `[CLS]` từ BERT: một token học được cắm vào đầu chuỗi patch. Trong quá trình tự chú ý (Self-Attention), token này sẽ ' lắng nghe và trò chuyện ' với tất cả các mảnh ảnh khác. Tại tầng cuối cùng, vector của riêng token `[CLS]` sẽ mang trọn vẹn ý nghĩa của cả bức ảnh, chỉ cần đưa nó qua 1 tầng Linear là phân loại được con Mèo hay Chó!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $z_0 = [x_{\text{class}}; x_p^1 E; \dots; x_p^N E] + E_{\text{pos}}$. Vector đầu ra $y = \text{LN}(z_L^0)$ đưa vào MLP Head. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** `[CLS]` là vector học đại diện toàn cục cho bài toán phân loại, không chứa tọa độ hình học (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 53 [OLP04-Q53] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình đa phương thức CLIP (Contrastive Language-Image Pre-training - Radford et al., OpenAI 2021) được huấn luyện trên 400 triệu cặp (Ảnh, Văn bản) bằng hàm mất mát nào?

- **A.** Tối ưu hóa tham số qua phép chiếu ngẫu nhiên trên ma trận trực giao (Random Orthogonal Matrix) nhằm bảo toàn khoảng cách biểu diễn hình học
- **B.** Huấn luyện lại toàn bộ các tầng Multi-Head Attention và MLP bằng thuật toán lan truyền ngược kết hợp cơ chế suy giảm trọng số (Weight Decay)
- **C.** Đóng băng toàn bộ trọng số gốc $W_0$, bổ sung nhánh song song gồm tích hai ma trận hạng thấp $B \times A$ ($r \ll d$) để cập nhật trọng số hiệu chỉnh
- **D.** Lượng tử hóa các ma trận trọng số về định dạng số nguyên nhị phân 1-bit (Binary Neural Networks) để tăng tốc độ suy luận thời gian thực

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
CLIP có 1 mô hình nhìn ảnh (Image Encoder) và 1 mô hình đọc chữ (Text Encoder). Trong một batch gồm $N$ ảnh và $N$ câu miêu tả tương ứng, CLIP tính bảng tương đồng $N \times N$. Mục tiêu: đường chéo chính (ảnh nào đi với câu miêu tả nấy) phải có điểm số cực cao, còn các ô nằm ngoài đường chéo (ảnh nọ cắm câu kia) phải có điểm số cực thấp!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Symmetric InfoNCE: $\mathcal{L} = \frac{1}{2} (\mathcal{L}_{I \to T} + \mathcal{L}_{T \to I})$ trên ma trận điểm tương đồng $I \cdot T^T / \tau$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** CLIP không dùng nhãn phân loại cố định (loại D) nên có khả năng Zero-Shot Transfer cực kỳ ấn tượng.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 54 [OLP04-Q54] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khả năng phân loại không cần mẫu huấn luyện (Zero-Shot Classification) của mô hình CLIP trên một tập dữ liệu mới (ví dụ phân loại Chó vs Mèo) được thực hiện như thế nào?

- **A.** Lượng tử hóa mô hình xuống 4-bit qua chuẩn NormalFloat4 (NF4), áp dụng Double Quantization và bộ nhớ đệm trang phân trang (Paged Optimizers) chống tràn VRAM
- **B.** Cắt tỉa vĩnh viễn 75% số lượng tầng Transformer trong khối giải mã (Structured Layer Pruning) để nén kích thước mô hình xuống mức tối thiểu
- **C.** Chuyển toàn bộ các phép nhân ma trận sang tính toán trên bộ vi xử lý CPU đa luồng thay vì tận dụng phần cứng đồ họa chuyên dụng GPU
- **D.** Phân tán các tầng mô hình trên cụm 8 GPU độc lập thông qua giao thức truyền thông liên mạng (Pipeline Parallelism) với độ trễ cực thấp

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Không cần huấn luyện lại bất kỳ trọng số nào! Muốn phân loại, chỉ cần viết mẫu câu: ' A photo of a dog ' và ' A photo of a cat '. Đưa 2 câu này qua Text Encoder ra 2 vector, đưa bức ảnh qua Image Encoder ra 1 vector. Vector ảnh nghiêng về vector câu nào hơn (Cosine similarity lớn hơn) thì đó chính là đáp án!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\hat{y} = \arg\max_k \cos(E_I(\text{image}), E_T(\text{" a photo of a "} + c_k))$. Hoàn toàn Zero-Shot. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Zero-Shot nghĩa là không huấn luyện lại bất kỳ gradient nào (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 55 [OLP04-Q55] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình Phân vùng vạn năng SAM (Segment Anything Model - Kirillov et al., Meta AI 2023) có thể nhận các loại điều kiện nhắc nhở (Promptable Segmentation) nào ở đầu vào?

- **A.** Mô hình thưởng (Reward Model) xếp hạng chất lượng các câu trả lời do mô hình sinh ra, làm tín hiệu mục tiêu định hướng thuật toán PPO tối ưu chính sách
- **B.** Mô hình thưởng đóng vai trò bộ lọc an toàn loại bỏ triệt để các câu hỏi vi phạm chính sách trước khi đưa vào khối Transformer Decoder
- **C.** Mô hình thưởng thực hiện việc gán nhãn ngữ pháp tự động cho các từ loại trong câu phản hồi nhằm tăng cường độ chính xác ngữ nghĩa
- **D.** Mô hình thưởng tính toán khoảng cách Levenshtein giữa câu phản hồi của mô hình và câu mẫu của chuyên gia để phạt lỗi chính tả trực tiếp

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
SAM cực kỳ đa tài: bạn chỉ cần click 1 điểm chuột vào vật thể, hoặc vẽ 1 chiếc hộp bao quanh, hoặc bôi một mảng màu sơ sài, hoặc nhập câu chữ miêu tả, SAM sẽ hiểu ngay bạn muốn cắt vật thể nào và vẽ đường viền mặt nạ chính xác đến từng sợi tóc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Kiến trúc SAM gồm Image Encoder nặng (ViT-H) + Prompt Encoder nhẹ (Points/Boxes/Masks) + Fast Mask Decoder chạy real-time trong browser (< 50ms). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** SAM là mô hình phân đoạn tương tác đa dạng prompt (Points, Boxes, Masks, Text), không bị giới hạn video hay âm thanh.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 56 [OLP04-Q56] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình khuếch tán xác suất DDPM (Denoising Diffusion Probabilistic Models - Ho et al., 2020), quá trình thêm nhiễu xuôi (Forward Process) biến đổi ảnh gốc $x_0$ thành nhiễu trắng thuần túy Gaussian $x_T \sim \mathcal{N}(0, I)$ thông qua chuỗi phân phối có điều kiện nào?

- **A.** Mô hình Actor-Critic trực tiếp tối ưu hóa chính sách chính qua hàm mất mát kẹp cắt PPO-Clip kết hợp với bộ đệm phát lại kinh nghiệm
- **B.** Mô hình DPO loại bỏ hoàn toàn việc huấn luyện Reward Model riêng biệt và vòng lặp PPO, giải trực tiếp bài toán qua hàm mất mát phân loại nhị phân trên cặp câu
- **C.** Mô hình DPO bắt buộc phải lưu trữ đồng thời 4 mô hình lớn trong bộ nhớ VRAM của GPU trong toàn bộ quá trình cập nhật trọng số tham số
- **D.** Mô hình DPO chỉ áp dụng được cho các bài toán phân loại sắc thái tình cảm nhị phân và không hỗ trợ các tác vụ sinh ngôn ngữ tự do

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Quá trình xuôi giống như nhỏ từng giọt mực vào cốc nước: mỗi bước $t$, ta co nhỏ ảnh cũ lại một chút (nhân $\sqrt{1-\beta_t}$) rồi cộng thêm một lượng nhiễu hạt nhỏ (phương sai $\beta_t$). Sau 1000 bước, bức ảnh tan biến hoàn toàn thành một bức tranh nhiễu trắng xì xào tuyệt đối!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $q(x_t \mid x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1 - \bar{\alpha}_t) I)$ với $\alpha_t = 1 - \beta_t$ và $\bar{\alpha}_t = \prod_{s=1}^t \alpha_s$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nhiễu khuếch tán trong DDPM tuân theo phân phối Gauss Markovian, không dùng phân phối đều (loại A) hay cộng hằng số (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 57 [OLP04-Q57] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mạng nơ-ron U-Net trong mô hình sinh ảnh khuếch tán (Diffusion Models) được huấn luyện để giải quyết bài toán dự đoán đại lượng nào tại mỗi bước thời gian $t$?

- **A.** Truy xuất tài liệu liên quan từ kho tri thức bên ngoài rồi ghép vào ngữ cảnh câu hỏi prompt trước khi đưa vào mô hình ngôn ngữ lớn để trả lời
- **B.** Huấn luyện lại toàn bộ các tham số của mô hình ngôn ngữ lớn trên toàn bộ kho tài liệu doanh nghiệp bằng thuật toán lan truyền ngược có giám sát
- **C.** Nén toàn bộ cơ sở dữ liệu văn bản thành các vector nhị phân rồi lưu trực tiếp vào các thanh ghi phần cứng của chip tăng tốc TPU
- **D.** Chuyển đổi câu hỏi của người dùng thành các câu truy vấn cơ sở dữ liệu quan hệ SQL tiêu chuẩn để trích xuất bảng biểu có cấu trúc

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Thay vì bảo mạng ' hãy vẽ bức ảnh mới từ đầu ' (rất khó), người ta bày trò thông minh hơn: Cầm ảnh $x_t$ và bước thời gian $t$ đưa cho mạng U-Net và hỏi: ' Đoán xem hạt nhiễu nào đã được thêm vào ảnh này?'. Mạng chỉ cần đoán đúng lượng nhiễu $\epsilon_\theta$, sau đó ta lấy ảnh trừ bớt lượng nhiễu đó đi là ảnh sẽ rõ nét dần lên!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Hàm mất mát huấn luyện đơn giản hóa: $\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, x_0, \epsilon} [\|\epsilon - \epsilon_\theta(x_t, t)\|^2]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Mạng U-Net dự đoán nhiễu $\epsilon$ (noise prediction), không phải dự đoán nhãn phân loại (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 58 [OLP04-Q58] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Hướng dẫn Không cần Bộ phân loại (Classifier-Free Guidance - CFG) trong mô hình khuếch tán điều khiển chất lượng sinh ảnh theo câu prompt $c$ bằng công thức ngoại suy gradient nào với hệ số hướng dẫn $w > 1$?

- **A.** $\tilde{\epsilon}_\theta(x_t, c) = \frac{\epsilon_\theta(x_t, c) + \epsilon_\theta(x_t, \emptyset)}{w}$ lấy trung bình chia nhỏ
- **B.** $\tilde{\epsilon}_\theta(x_t, c) = \epsilon_\theta(x_t, \emptyset) + w \cdot [\epsilon_\theta(x_t, c) - \epsilon_\theta(x_t, \emptyset)]$
- **C.** $\tilde{\epsilon}_\theta(x_t, c) = \epsilon_\theta(x_t, c) \cdot \epsilon_\theta(x_t, \emptyset)$ theo phép nhân chập ma trận
- **D.** $\tilde{\epsilon}_\theta(x_t, c) = w \cdot \nabla_x \log P(y \mid x)$ sử dụng bộ phân loại phụ trợ bên ngoài

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- $\epsilon(x_t, \emptyset)$: Đoán nhiễu khi KHÔNG CÓ lời nhắc (vẽ bừa bãi).
- $\epsilon(x_t, c)$: Đoán nhiễu khi CÓ lời nhắc $c$.
Hiệu số $[\epsilon(x_t, c) - \epsilon(x_t, \emptyset)]$ chính là hướng đi giúp ảnh khớp với lời nhắc nhất! CFG nhân hiệu số này với hệ số $w > 1$ (ví dụ $w=7.5$) để phóng đại lời nhắc lên cực mạnh, khiến ảnh sinh ra tuân thủ mệnh lệnh câu prompt răm rắp!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\tilde{\epsilon}_\theta = (1 - w)\epsilon_\theta(x_t, \emptyset) + w \epsilon_\theta(x_t, c) = \epsilon_\theta(x_t, \emptyset) + w (\epsilon_\theta(x_t, c) - \epsilon_\theta(x_t, \emptyset))$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án D là Classifier Guidance (cần bộ phân loại bên ngoài); CFG không cần bộ phân loại bên ngoài mà dùng prompt rỗng $\emptyset$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 59 [OLP04-Q59] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình Stable Diffusion (Latent Diffusion Models - Rombach et al., CVPR 2022) đạt hiệu quả tính toán vượt bậc so với DDPM trên không gian điểm ảnh gốc nhờ cải tiến cấu trúc then chốt nào?

- **A.** Mô hình HNSW gom cụm các vector thành các phân vùng Voronoi phẳng cố định và chỉ tìm kiếm trong cụm có tâm gần nhất với vector truy vấn
- **B.** Xây dựng đồ thị Small-World nhiều tầng phân cấp: các tầng trên thưa giúp nhảy nhanh qua không gian lớn, tầng đáy dày đặc giúp hội tụ chính xác lân cận
- **C.** Chuyển toàn bộ các vector sang biểu diễn nhị phân Hamming rồi quét tuần tự qua toàn bộ cơ sở dữ liệu bằng các toán tử logic bitwise XOR
- **D.** Chiếu các vector vào không gian tiềm ẩn một chiều thông qua hàm băm cảm nhận vị trí LSH rồi sắp xếp theo thứ tự độ lớn tăng dần

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Chạy khuếch tán trên ảnh $512 \times 512$ pixel rất nặng và lãng phí (vì nhiều pixel chỉ là màu nền vô nghĩa). Stable Diffusion dùng một bộ nén VQ-VAE/Autoencoder nén ảnh 8 lần xuống không gian tiềm ẩn $64 \times 64$ (nhẹ đi 64 lần!). Mạng khuếch tán chỉ cần vẽ trên mảng $64 \times 64$ tí hon này, vẽ xong mới phóng to ngược lại thành ảnh sắc nét $512 \times 512$, giúp chạy mượt mà ngay trên card đồ họa gia đình!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ảnh $x \in \mathbb{R}^{H \times W \times 3} \to z = \mathcal{E}(x) \in \mathbb{R}^{\frac{H}{f} \times \frac{W}{f} \times d}$ với $f=8$. Khuếch tán diễn ra trên không gian tiềm ẩn $z$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Stable Diffusion dùng Cross-Attention để nhận điều kiện văn bản từ CLIP Text Encoder, không hề loại bỏ (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 60 [OLP04-Q60] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Mạng Tích chập Đồ thị GCN (Graph Convolutional Networks - Kipf & Welling, ICLR 2017), công thức lan truyền đặc trưng qua tầng mạng bậc $l$ sử dụng ma trận kề chuẩn hóa đối xứng nào?

- **A.** Bộ lọc Bloom Filter và Thuật toán tìm đường ngắn nhất Dijkstra
- **B.** Mô hình ngôn ngữ lớn LLM (để đọc hiểu văn bản) và Mô hình phân rã giá trị kỳ dị SVD (để giảm chiều không gian từ vựng)
- **C.** Mô hình nhúng Embedding Model (để tạo vector đặc trưng ngữ nghĩa) và Cơ sở dữ liệu Vector Database (để lưu trữ và tìm kiếm tương đồng)
- **D.** Mạng tích chập không gian CNN (để xử lý ảnh) và Thuật toán phân cụm K-Means (để gán nhãn không giám sát)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
1. Ma trận kề chuẩn $A$ không có đường nối một nút với chính nó, khiến nút quên mất thông tin của bản thân $\implies$ cộng thêm ma trận đơn vị $\tilde{A} = A + I$ (thêm self-loop).
2. Nếu một nút có 1000 bạn bè, tổng thông tin sẽ phát nổ quá lớn; nếu chỉ có 1 bạn bè thì quá nhỏ $\implies$ chuẩn hóa 2 bên bằng $\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2}$ để giữ cho độ lớn tín hiệu luôn ổn định!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Renormalization Trick (Kipf & Welling 2017): $\tilde{D}_{ii} = \sum_j \tilde{A}_{ij}$. $H^{(l+1)} = \sigma(\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(l)} W^{(l)})$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nếu không thêm self-loop (loại A) nút sẽ mất đặc trưng gốc; chuẩn hóa 1 phía (loại B) là Random Walk, còn GCN chuẩn là đối xứng 2 phía.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 61 [OLP04-Q61] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Mạng Chú ý Đồ thị GAT (Graph Attention Networks - Veličković et al., ICLR 2018), hệ số chú ý $\alpha_{ij}$ đo lường mức độ quan trọng của nút lân cận $j$ đối với nút $i$ được tính bằng cơ chế nào?

- **A.** Reranker là mô hình Bi-Encoder tính toán tích vô hướng cực nhanh trên hàng triệu vector được lập chỉ mục trước trong cơ sở dữ liệu
- **B.** Reranker sử dụng mô hình Cross-Encoder ghép đôi [Query, Doc] để mô hình hóa tương tác chú ý đầy đủ, đánh giá chính xác độ liên quan dù tốn kém hơn
- **C.** Reranker là thuật toán sắp xếp nổi bọt sắp xếp lại các tài liệu dựa trên số lượng từ vựng xuất hiện trùng lặp giữa câu hỏi và câu trả lời
- **D.** Reranker tự động tóm tắt các tài liệu dài thành các đoạn văn ngắn 50 từ trước khi gửi vào prompt ngữ cảnh của mô hình ngôn ngữ lớn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
GCN coi mọi người bạn đều quan trọng như nhau (chỉ chia theo bậc). GAT thông minh hơn: nó dùng cơ chế Attention để tự học xem trong đám bạn bè lân cận, ai nói câu có giá trị hơn thì lắng nghe người đó nhiều hơn (hệ số $\alpha_{ij}$ to hơn). Tương tự như cách bạn lắng nghe chuyên gia hơn là người qua đường!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Điểm chú ý: $e_{ij} = \text{LeakyReLU}(a^T [Wh_i \parallel Wh_j])$. Chuẩn hóa Softmax trên lân cận $\mathcal{N}_i$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** GAT dùng LeakyReLU kết hợp ghép vector $[Wh_i \parallel Wh_j]$, không chia đều theo bậc (loại B là GCN).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 62 [OLP04-Q62] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khung làm việc Truyền thông điệp tổng quát trên đồ thị MPNN (Message Passing Neural Networks - Gilmer et al., 2017) mô tả quá trình cập nhật trạng thái của mỗi nút $v$ ở bước $t$ qua hai hàm cốt lõi nào?

- **A.** Độ tương tự ngữ nghĩa (Semantic Similarity - Dense Retrieval) và Khớp từ khóa chính xác (Keyword Matching - BM25 Sparse Retrieval)
- **B.** Hàm biến đổi Fourier 1D (Frequency Domain Analysis) và Hàm phân tích lọc thông dải sóng con Wavelet (Wavelet Packet Transform)
- **C.** Hàm phân rã ma trận kỳ dị (Singular Value Decomposition) và Hàm tối ưu hóa lồi có ràng buộc bất đẳng thức Karush-Kuhn-Tucker
- **D.** Hàm tích chập không gian 2D (Spatial Convolution) và Hàm nội suy song tuyến tính điểm ảnh (Bilinear Interpolation)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
MPNN tóm gọn mọi mạng đồ thị (GCN, GAT, GraphSAGE) vào 2 bước đơn giản:
1. Gom thư (Aggregate): gom tin nhắn từ tất cả bạn bè xung quanh gửi về.
2. Cập nhật (Update): đọc đống tin nhắn đó kết hợp với suy nghĩ cũ của mình để cập nhật suy nghĩ mới!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $m_v^{t+1} = \sum_{w} M_t(h_v^t, h_w^t, e_{vw})$, $h_v^{t+1} = U_t(h_v^t, m_v^{t+1})$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** MPNN là khung đại số trừu tượng gồm Aggregate (bất biến hoán vị) và Update.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 63 [OLP04-Q63] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong Học tăng cường (Reinforcement Learning), Quá trình Quyết định Markov (Markov Decision Process - MDP) được định nghĩa bởi bộ 5 thành phần $(S, A, P, R, \gamma)$. Tính chất Markov (Markov Property) phát biểu điều kiện cốt lõi nào về trạng thái hiện tại $S_t$?

- **A.** Tương lai độc lập với quá khứ khi đã biết hiện tại: $P(S_{t+1} \mid S_t, A_t, S_{t-1}, A_{t-1}, \dots) = P(S_{t+1} \mid S_t, A_t)$ (trạng thái hiện tại nắm giữ đầy đủ thông tin lịch sử)
- **B.** Không gian hành động $A$ bắt buộc phải là một tập hợp hữu hạn có ít hơn 10 phần tử (Finite Discrete Actions) để bảng $Q$ không bị tràn bộ nhớ
- **C.** Phần thưởng nhận được ở tương lai không bao giờ bị chiết khấu theo thời gian (Zero Discounting: $\gamma = 1.0$) trong mọi kịch bản mô phỏng
- **D.** Chính sách của tác tử luôn luôn là một hàm tất định không chứa yếu tố ngẫu nhiên (Deterministic Policy) trong suốt quá trình tương tác

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tính chất Markov là ' quá khứ không quan trọng, chỉ có hiện tại mới quyết định tương lai ': Muốn biết bước tiếp theo quả bóng bay đi đâu, bạn chỉ cần biết vị trí và vận tốc hiện tại của nó, không cần quan tâm 10 phút trước nó đã bay qua những đâu!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $P(S_{t+1}=s ', R_{t+1}=r \mid S_t=s_t, A_t=a_t, \dots, S_0=s_0) = P(S_{t+1}=s ', R_{t+1}=r \mid S_t=s_t, A_t=a_t)$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Tính chất Markov là tính ' không nhớ quá khứ ', không ép buộc phần thưởng hay không gian hành động hữu hạn.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.1 Khái Niệm Cốt Lõi: Agent, Environment, State, Action, Reward**.

---

### Câu 64 [OLP04-Q64] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Phương trình kỳ vọng Bellman (Bellman Expectation Equation) cho hàm giá trị trạng thái $V^\pi(s)$ dưới chính sách $\pi$ phân rã giá trị hiện tại thành phần thưởng tức thời và giá trị tương lai theo công thức nào?

- **A.** $V^\pi(s) = \sum_{a} \pi(a \mid s) \sum_{s ', r} P(s ', r \mid s, a) [r + \gamma V^\pi(s ')]$
- **B.** $V^\pi(s) = \max_a [R(s, a) + \gamma \max_{s '} V(s ')]$
- **C.** $V^\pi(s) = \frac{1}{|S|} \sum_{s '} P(s ' \mid s)$
- **D.** $V^\pi(s) = \sum_{a} \pi(a \mid s) \sum_{s ', r} P(s ', r \mid s, a) [r + \gamma^2]$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Giá trị của ô đất bạn đang đứng bằng: trung bình phần thưởng bạn nhặt được ngay lập tức ở bước tiếp theo ($r$), cộng với giá trị của ô đất mới mà bạn bước tới ($V(s ')$) được giảm giá một chút theo thời gian (nhân hệ số chiết khấu $\gamma$).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $V^\pi(s) = \mathbb{E}_\pi [R_{t+1} + \gamma V^\pi(S_{t+1}) \mid S_t = s] = \sum_a \pi(a|s) \sum_{s ', r} P(s ', r|s, a)[r + \gamma V^\pi(s ')]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B là phương trình tối ưu Bellman (Bellman Optimality), câu hỏi hỏi phương trình kỳ vọng dưới chính sách $\pi$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.1 Khái Niệm Cốt Lõi: Agent, Environment, State, Action, Reward**.

---

### Câu 65 [OLP04-Q65] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Phương trình tối ưu Bellman (Bellman Optimality Equation) cho hàm giá trị hành động tối ưu $Q^*(s, a)$ có dạng toán học nào?

- **A.** $Q^*(s, a) = \sum_{s ', r} P(s ', r \mid s, a) [r + \gamma \max_{a '} Q^*(s ', a ')]$
- **B.** $Q^*(s, a) = \sum_{s ', r} P(s ', r \mid s, a) [r + \gamma \sum_{a '} \pi(a ' \mid s ') Q^*(s ', a ')]$
- **C.** $Q^*(s, a) = \min_{a '} [r + \gamma Q^*(s ', a ')]$
- **D.** $Q^*(s, a) = r^2 + \gamma \max_{a '} Q^*(s ', a ')^2$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu bạn đã là một kỳ thủ hoàn hảo (tối ưu), giá trị của nước cờ $(s, a)$ bằng phần thưởng bạn ăn được ngay ($r$), cộng với giá trị của nước cờ TỐT NHẤT mà bạn có thể đi ở bàn cờ tiếp theo (toán tử $\max_{a '} Q^*(s ', a ')$ chiết khấu $\gamma$).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $Q^*(s, a) = \mathbb{E}[R_{t+1} + \gamma \max_{a '} Q^*(S_{t+1}, a ') \mid S_t=s, A_t=a]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B là phương trình kỳ vọng dưới chính sách $\pi$, không phải tối ưu $\max$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.1 Khái Niệm Cốt Lõi: Agent, Environment, State, Action, Reward**.

---

### Câu 66 [OLP04-Q66] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán Q-Learning được phân loại là thuật toán học ngoại chính sách (Off-policy TD Control) vì quy tắc cập nhật bảng $Q$ của nó sử dụng thành phần nào để ước lượng giá trị tương lai?

- **A.** Giá trị hành động cực đại $\max_{a '} Q(S_{t+1}, a ')$ tại trạng thái kế tiếp, độc lập với hành động thực tế tác tử sẽ chọn theo chính sách khám phá
- **B.** Hành động thực tế $a_{t+1}$ mà tác tử vừa bốc theo chiến lược khám phá $\epsilon$-greedy tại trạng thái kế tiếp trong quỹ đạo tương tác
- **C.** Trung bình cộng kỳ vọng của tất cả các giá trị $Q(S_{t+1}, a)$ khả dĩ trong toàn bộ không gian hành động rời rạc tại bước thời gian tiếp theo
- **D.** Đạo hàm bậc nhất của hàm chính sách theo tham số nơ-ron Actor nhằm cập nhật trọng số thông qua thuật toán lan truyền ngược Gradient Descent

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Q-Learning gọi là ' ngoại chính sách ' (Off-policy) vì: lúc đi thì đi lăng nhăng để khám phá (chính sách hành vi $\epsilon$-greedy), nhưng lúc ngồi chấm điểm ghi sổ thì luôn giả định là mình sẽ đi nước cờ hoàn hảo nhất (chính sách mục tiêu $\max_{a '} Q$). Người làm một đằng, người chấm một nẻo!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a) - Q(S_t, A_t)]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A là SARSA (On-policy: dùng hành động thực tế $A_{t+1}$). Q-Learning dùng $\max_a$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.2 Q-Learning & SARSA: On-policy vs Off-policy**.

---

### Câu 67 [OLP04-Q67] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán kinh điển Vách đá hiểm trở (Cliff Walking), tại sao thuật toán SARSA (On-policy) lại tìm ra con đường đi an toàn vòng lên phía trên xa vách đá, trong khi Q-Learning (Off-policy) lại chọn con đường tối ưu đi sát sạt mép vực?

- **A.** SARSA tính đến rủi ro của việc vô tình nhảy xuống vực do bước đi ngẫu nhiên $\epsilon$-greedy, trong khi Q-Learning giả định bước sau sẽ luôn chọn hành động tối ưu tuyệt đối
- **B.** Q-Learning không thể cập nhật được các giá trị hàm chất lượng khi môi trường trả về các tín hiệu phần thưởng mang giá trị âm liên tục
- **C.** SARSA có tốc độ hội tụ tham số nhanh hơn Q-Learning gấp 10 lần nhờ việc loại bỏ hoàn toàn toán tử lấy giá trị cực đại trong nhãn TD
- **D.** SARSA chỉ áp dụng được trên không gian trạng thái liên tục nhiều chiều trong khi Q-Learning chỉ giải quyết được các bài toán rời rạc hữu hạn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đi sát mép vực thì ngắn nhất nhưng thỉnh thoảng táy máy đi ẩu (xác suất $\epsilon$) là rơi xuống vực gãy chân. Q-Learning mơ mộng nghĩ rằng ' lần sau mình sẽ không bao giờ đi ẩu ' nên cứ bò sát mép vực. SARSA thực tế hơn: nó biết tính mình thỉnh thoảng ngứa tay đi bừa, nên nó chọn đi vòng xa mép vực cho lành!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 SARSA cập nhật bằng $Q(S_{t+1}, A_{t+1})$ với $A_{t+1} \sim \epsilon\text{-greedy}$, phạt nặng các trạng thái gần vực thẳm. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Q-Learning tìm đường tối ưu lý thuyết (ngắn nhất sát mép vực), SARSA tìm đường an toàn thực tế khi đang khám phá.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.2 Q-Learning & SARSA: On-policy vs Off-policy**.

---

### Câu 68 [OLP04-Q68] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong thuật toán Deep Q-Networks (DQN - Mnih et al., Nature 2015), hai kỹ thuật cốt lõi nào giúp ổn định quá trình huấn luyện mạng nơ-ron xấp xỉ hàm giá trị và ngăn chặn phân kỳ gradient?

- **A.** Bộ đệm phát lại kinh nghiệm (Experience Replay) để xóa bỏ tương quan giữa các mẫu liên tiếp, và Mạng mục tiêu (Target Network) đóng băng trọng số để ổn định nhãn mục tiêu TD
- **B.** Kỹ thuật giải mã chùm tia (Beam Search Decoding) để tìm kiếm quỹ đạo tối ưu, và Mã hóa vị trí hình sin (Sinusoidal Positional Encoding) để ghi nhớ thời gian
- **C.** Khởi tạo trọng số ngẫu nhiên chuẩn hóa (Xavier Normal Initialization) để ổn định phương sai, và Tích chập giãn nở (Dilated Convolution) để mở rộng trường tiếp nhận
- **D.** Chuẩn hóa theo lô nhỏ (Batch Normalization) để chống trôi dạt hiệp phương sai nội tại, và Hàm kích hoạt Sigmoid để nén giá trị kích hoạt về khoảng $(0, 1)$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi mạng nơ-ron học chơi game Atari, nó hay bị điên đảo vì 2 lý do:
1. Các bước đi kế tiếp nhau giống hệt nhau $\implies$ Experience Replay lưu 1 triệu bước vào kho rồi bốc ngẫu nhiên xào xáo lên để học.
2. Vừa bắn bia vừa di chuyển bia $\implies$ Target Network đóng băng cái bia lại, 1000 bước sau mới cập nhật bia một lần để mạng ngắm bắn chuẩn xác!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Target: $y = r + \gamma \max_{a '} Q(s ', a '; \theta^-)$ với $\theta^-$ cố định theo chu kỳ. Loss: $(y - Q(s, a; \theta))^2$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Experience Replay + Target Network là cặp bài trùng làm nên cuộc cách mạng Deep Q-Learning năm 2015.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.3 Deep Q-Networks (DQN): Experience Replay, Target Network**.

---

### Câu 69 [OLP04-Q69] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Theo Định lý Gradient Chính sách (Policy Gradient Theorem), gradient của hàm mục tiêu kỳ vọng phần thưởng $J(\theta)$ trong thuật toán REINFORCE được tính bằng công thức nào sử dụng thủ thuật đạo hàm logarit (Likelihood Ratio Trick)?

- **A.** $\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \ln \pi_\theta(a_t \mid s_t) G_t \right]$ với $G_t$ là tổng phần thưởng tích lũy có chiết khấu theo thời gian
- **B.** $\nabla_\theta J(\theta) = \sum_{t=0}^T (\pi_\theta(a_t \mid s_t) - G_t)^2$ tối thiểu hóa sai số toàn phương trung bình giữa chính sách và phần thưởng thực tế
- **C.** $\nabla_\theta J(\theta) = \frac{1}{T} \sum_{t=0}^T \nabla_\theta G_t$ tính đạo hàm giải tích trực tiếp của hàm phần thưởng môi trường theo trạng thái quan sát
- **D.** $\nabla_\theta J(\theta) = \max_a \nabla_\theta \pi_\theta(a \mid s)$ lấy gradient của xác suất hành động cực đại để cập nhật trọng số theo hướng tất định

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ta không thể đạo hàm môi trường game (vì nó là hộp đen). Thủ thuật Log-Derivative chuyển phép đạo hàm vào chính mạng của ta: $\nabla P = P \nabla \ln P$. Ý nghĩa cực kỳ trực quan: Nếu chuỗi hành động này đem lại phần thưởng lớn ($G_t > 0$), hãy đẩy xác suất chọn lại các hành động đó lên cao (tăng $\pi(a_t|s_t)$)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\nabla_\theta \mathbb{E}[R] = \int \nabla_\theta P(\tau) R(\tau) d\tau = \mathbb{E}[\nabla_\theta \ln P(\tau) R(\tau)]$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Môi trường không khả vi nên không thể tính $\nabla G_t$ (loại C); REINFORCE dùng $\nabla \ln \pi_\theta \cdot G_t$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.4 Policy Gradient, Actor-Critic, PPO**.

---

### Câu 70 [OLP04-Q70] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Actor-Critic, việc sử dụng hàm lợi thế Advantage $A(s, a) = Q(s, a) - V(s)$ làm tín hiệu phản hồi thay cho tổng phần thưởng thô $G_t$ mang lại lợi ích toán học cốt lõi nào?

- **A.** Giảm đáng kể phương sai (Variance Reduction) của ước lượng gradient mà không làm chệch kỳ vọng (Unbiased), giúp mô hình học ổn định hơn nhiều
- **B.** Tăng phương sai của gradient lên gấp đôi (Variance Amplification) để kích thích tác tử tăng cường khám phá các vùng không gian trạng thái mới
- **C.** Loại bỏ hoàn toàn sự cần thiết của hàm mất mát giá trị Critic (Value Function Loss) giúp mạng Actor có thể cập nhật trực tiếp từ phần thưởng
- **D.** Cho phép tác tử học chính sách tối ưu mà không cần nhận bất kỳ tín hiệu phần thưởng nào (Reward-Free Exploration) từ môi trường mô phỏng

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Phần thưởng thô $G_t$ nhảy nhót rất dữ dội (hôm nay được 100 điểm, mai xui xẻo được 10 điểm), khiến gradient rung lắc khủng khiếp. Hàm lợi thế $A(s, a)$ trừ đi đường cơ sở $V(s)$ (điểm trung bình): ' Hành động này mang lại kết quả tốt hơn hay tệ hơn so với mức trung bình bình thường?'. Trừ đi mức trung bình giúp triệt tiêu rung lắc phương sai mà không làm lệch hướng học!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mathbb{E}[\nabla_\theta \ln \pi(a|s) V(s)] = 0$. Trừ baseline $V(s)$ không làm chệch gradient nhưng giảm phương sai cực mạnh. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Baseline trong Actor-Critic nhằm mục đích GIẢM PHƯƠNG SAI (Variance Reduction), không phải tăng phương sai (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.4 Policy Gradient, Actor-Critic, PPO**.

---

### Câu 71 [OLP04-Q71] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hàm mục tiêu kẹp cắt Proximal Policy Optimization (PPO-Clip - Schulman et al., 2017) với tỷ số xác suất $r_t(\theta) = \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_{\text{old}}}(a_t \mid s_t)}$ ngăn chặn bước cập nhật chính sách quá lớn phá hủy mô hình bằng biểu thức nào?

- **A.** $L^{\text{CLIP}}(\theta) = \mathbb{E}_t [r_t(\theta) + \epsilon]$ tuyến tính hóa hàm mất mát bằng cách cộng trực tiếp biên độ dung sai $\epsilon$ vào tỷ lệ xác suất
- **B.** $L^{\text{CLIP}}(\theta) = \mathbb{E}_t [\min(r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t)]$ với ngưỡng biên độ cắt $\epsilon \approx 0.2$
- **C.** $L^{\text{CLIP}}(\theta) = \mathbb{E}_t [\max(r_t(\theta), 1+\epsilon) \hat{A}_t]$ chỉ tối ưu hóa các bước cập nhật chính sách có tỷ lệ xác suất vượt trần giới hạn
- **D.** $L^{\text{CLIP}}(\theta) = \mathbb{E}_t [(r_t(\theta) - 1)^2 \hat{A}_t]$ áp dụng hàm mất mát sai số bình phương đối với độ lệch tỷ lệ xác suất so với giá trị đơn vị

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu chính sách mới thay đổi quá xa so với chính sách cũ, mô hình có thể bị ' sốc ' và tụt dốc không phanh. PPO đặt một chiếc ' kẹp an toàn ' $[1-\epsilon, 1+\epsilon]$ (thường là $[0.8, 1.2]$): nếu chính sách mới muốn nhảy vọt quá 20%, PPO sẽ gọt cụt phần vượt rào đi, giữ cho từng bước tiến hóa luôn nằm trong vùng kiểm soát an toàn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $L^{\text{CLIP}} = \hat{\mathbb{E}}_t [\min(r_t \hat{A}_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon) \hat{A}_t)]$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** PPO lấy $\min$ giữa giá trị gốc và giá trị bị kẹp clip để tạo cận dưới bi quan (Pessimistic Lower Bound).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.4 Policy Gradient, Actor-Critic, PPO**.

---

### Câu 72 [OLP04-Q72] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong xử lý tín hiệu âm thanh và giọng nói, thang đo Mel (Mel Scale) trong phổ đồ Mel-Spectrogram mô phỏng đặc tính sinh học nào của thính giác tai người?

- **A.** Tai người có độ nhạy tuyến tính hoàn hảo đối với mọi tần số âm thanh từ 20 Hz đến 20.000 Hz (Linear Frequency Response), do đó thang Hertz phản ánh trực tiếp cảm nhận thính giác
- **B.** Tai người phân biệt cao độ nhạy bén hơn nhiều ở các tần số thấp (< 1000 Hz) và kém nhạy hơn ở các tần số cao, chuyển đổi thang Hz sang Mel phi tuyến tính theo công thức $m = 2595 \log_{10}(1 + f/700)$
- **C.** Tai người chỉ có thể nghe được các sóng âm có biên độ áp suất lớn hơn 100 dB (High Sound Pressure Threshold), dẫn đến việc phải nén cường độ qua hàm logarit cơ số tự nhiên
- **D.** Tai người đảo ngược pha của các sóng âm thanh có tần số vượt quá 5000 Hz (Phase Inversion Artifact), đòi hỏi bộ lọc thang đo Mel phải triệt tiêu thành phần pha phức tạp

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tai người phân biệt nốt trầm cực giỏi (100 Hz lên 200 Hz thấy khác hẳn), nhưng với nốt cao chót vót (10.000 Hz lên 10.100 Hz) thì nghe chói tai y như nhau. Thang Mel bóp méo trục tần số lại: dãn rộng các nốt trầm ra để quan sát kỹ, và nén cụm các nốt cao lại, mô phỏng đúng cấu tạo ốc tai người!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\text{Mel}(f) = 2595 \log_{10}(1 + f / 700)$. Áp dụng ngân hàng bộ lọc tam giác Mel Filterbank lên phổ STFT. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Thính giác con người phi tuyến tính với tần số (nhạy ở tần số thấp), không phải tuyến tính (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến Trúc CNN & Các Khái Niệm Cốt Lõi**.

---

### Câu 73 [OLP04-Q73] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hàm mất mát CTC (Connectionist Temporal Classification - Graves et al., ICML 2006) trong bài toán Nhận dạng Giọng nói (ASR) giải quyết vấn đề không đồng bộ độ dài giữa chuỗi âm thanh và văn bản bằng cơ chế nào?

- **A.** Ép chuỗi tín hiệu âm thanh phải có số lượng khung hình frame bằng đúng số lượng ký tự trong câu (Linear Frame Interpolation) qua phép nội suy thời gian tuyến tính
- **B.** Bổ sung token khoảng trắng trống (Blank token $\epsilon$) và quy tắc gộp các ký tự lặp liên tiếp: $\mathcal{B}(a-a-\epsilon-b) = ab$ để tính tổng xác suất qua thuật toán Forward-Backward
- **C.** Cắt bỏ toàn bộ các đoạn âm thanh im lặng trong tệp ghi âm trước khi phân tích (Silence Removal Preprocessing) để đảm bảo không có khoảng cách thời gian giữa các âm vị
- **D.** Sử dụng mạng nơ-ron sinh đối kháng (Adversarial Data Augmentation) để sinh thêm các khung hình giả lập sao cho độ dài chuỗi âm thanh khớp chính xác với độ dài chuỗi từ

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nói chữ ' Ba ' mất 100 khung hình âm thanh, nhưng chữ ' Ba ' chỉ có 2 chữ cái. CTC cho phép mạng xuất ra: `B-B-B-blank-a-a-a`. Sau đó có một hàm dọn dẹp: gộp các chữ cái trùng liên tiếp lại thành 1 chữ, xóa token blank đi $\implies$ thu về đúng chữ ' Ba '! Nhờ đó không cần phải ngồi căn chỉnh thủ công từng mili-giây cho từng chữ cái.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Toán tử gộp $\mathcal{B}$: loại bỏ trùng lặp kế tiếp và xóa blank. $P(Y \mid X) = \sum_{\pi \in \mathcal{B}^{-1}(Y)} P(\pi \mid X)$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Token blank $\epsilon$ trong CTC dùng để phân biệt hai chữ cái giống nhau đứng cạnh nhau (ví dụ ' hello ': `l-blank-l`).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.1 Tổng Quan Xử Lý Ngôn Ngữ Tự Nhiên & RNN/LSTM/GRU**.

---

### Câu 74 [OLP04-Q74] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình nhận dạng giọng nói đa ngôn ngữ OpenAI Whisper (Radford et al., 2022) sử dụng cơ chế token đặc biệt nào trong Decoder để thực hiện đồng thời nhiều tác vụ (ASR, Dịch thuật, Phát hiện ngôn ngữ)?

- **A.** Thay đổi ma trận trọng số của Encoder cho từng ngôn ngữ qua các nhánh chuyên biệt: `<|lang_adapter|>`, `<|expert_weights|>`, `<|cross_module|>`, và `<|vocab_proj|>`
- **B.** Các token tiền tố chuyên biệt được đưa vào đầu chuỗi: `<|startoftranscript|>`, `<|lang_id|>`, `<|transcribe|>` hoặc `<|translate|>`, và `<|notimestamps|>`
- **C.** Sử dụng 100 bộ phân loại Softmax riêng biệt ở tầng đầu ra của mạng: `<|head_en|>`, `<|head_vi|>`, `<|head_zh|>`, và `<|head_es|>` cho từng ngôn ngữ mục tiêu
- **D.** Chuyển toàn bộ chuỗi âm thanh đầu vào thành chuỗi ký hiệu trung gian: `<|morse_code|>`, `<|phoneme_seq|>`, `<|byte_stream|>`, và `<|token_end|>` trước khi dịch

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Whisper là một mô hình duy nhất làm được mọi việc nhờ các token ' gợi ý ' ở đầu câu: bạn muốn dịch hay chép chính tả? Chỉ cần ném token `<|vi|>` (tiếng Việt), `<|transcribe|>` (chép lời) hay `<|translate|>` (dịch sang tiếng Anh). Mô hình nhìn thấy các thẻ này sẽ tự động chuyển chế độ làm việc tương ứng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Chuỗi decoder prefix: `[SOT, LANG, TASK, TIMESTAMPS]`. Mô hình tự động multitask không cần kiến trúc riêng. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Whisper chia sẻ 100% trọng số Transformer Encoder-Decoder cho mọi tác vụ và mọi ngôn ngữ thông qua prompt tokens.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 75 [OLP04-Q75] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong các cơ sở dữ liệu vector (Vector Databases như Milvus, Pinecone, Qdrant), khi tất cả các vector nhúng embedding đã được chuẩn hóa về chuẩn $L_2$ bằng 1 ($\ \|u\ \| = \ \|v\ \| = 1$), mối liên hệ giữa khoảng cách bình phương Euclid $d_E^2(u, v)$ và độ tương đồng Cosine $\cos(u, v)$ là gì?

- **A.** $d_E^2(u, v) = 1 + \cos(u, v)$ theo định lý Pythagoras mở rộng trên không gian Hilbert, do đó khoảng cách Euclid tỷ lệ thuận trực tiếp với độ tương đồng Cosine
- **B.** $d_E^2(u, v) = 2 - 2 \cos(u, v) = 2(1 - \cos(u, v))$, do đó tối đa hóa Cosine Similarity tương đương hoàn toàn với tối thiểu hóa khoảng cách Euclid
- **C.** $d_E^2(u, v) = \frac{1}{\cos(u, v)}$ theo quy tắc nghịch đảo tỷ lệ biến thiên, dẫn đến việc cực đại hóa đại lượng này sẽ làm cực tiểu hóa đại lượng kia
- **D.** Hai đại lượng này hoàn toàn độc lập và không có bất kỳ mối liên hệ giải tích nào do khoảng cách Euclid phụ thuộc độ dài còn Cosine chỉ phụ thuộc hướng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi hai mũi tên đều có độ dài bằng 1: bình phương khoảng cách giữa hai đầu mũi tên là $\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2u^T v = 1 + 1 - 2\cos\theta = 2(1 - \cos\theta)$. Hai mũi tên càng chụm vào nhau (Cosine = 1) thì khoảng cách giữa hai đầu càng bằng 0! Vì vậy tìm điểm gần nhất theo khoảng cách Euclid hay theo góc Cosine đều cho cùng 1 kết quả.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\|u - v\|_2^2 = \|u\|^2 + \|v\|^2 - 2 u \cdot v = 2 - 2 \cos(u, v)$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Công thức liên hệ là $2(1 - \cos\theta)$, không phải $1 + \cos\theta$ (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 76 [OLP04-Q76] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán tìm kiếm láng giềng gần đúng HNSW (Hierarchical Navigable Small World) trong cơ sở dữ liệu vector đạt tốc độ truy vấn $O(\log N)$ nhờ vào cấu trúc dữ liệu nào?

- **A.** Áp dụng kỹ thuật nén lượng tử hóa tích phân (Product Quantization - PQ) phân chia vector thành các khối con rồi ánh xạ vào các tâm cụm centroid tương ứng
- **B.** Cắt tỉa ngẫu nhiên 90% số chiều của vector đặc trưng (Random Subspace Sampling) để giảm kích thước lưu trữ trên bộ nhớ đệm RAM của máy chủ
- **C.** Chuyển toàn bộ các giá trị thực của vector thành chuỗi ký tự ASCII (String Serialization) rồi sử dụng thuật toán tìm kiếm văn bản toàn văn ElasticSearch
- **D.** Sắp xếp toàn bộ các phần tử trong vector theo thứ tự giảm dần (Magnitude Sorting) rồi chỉ lưu trữ duy nhất 10 thành phần có giá trị biên độ lớn nhất

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
HNSW giống như hệ thống giao thông: ở tầng cao nhất là đường cao tốc xuyên quốc gia (các bước nhảy cực xa, lướt nhanh đến đúng thành phố). Xuống tầng giữa là đường quốc lộ, và xuống tầng đáy cùng là đường làng ngõ xóm đi bộ đến đúng từng số nhà. Nhờ phân tầng như Skip-List, tìm kiếm giữa 10 triệu vector chỉ mất vài mili-giây!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tầng đồ thị Voronoi: tầng $l$ có xác suất tồn tại $e^{-l / m_L}$. Độ phức tạp tìm kiếm $O(\log N)$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** HNSW là đồ thị thế giới nhỏ phân tầng (Hierarchical Navigable Small World), mượn triết lý Skip-List, không phải cây AVL (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 77 [OLP04-Q77] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong hệ thống RAG (Retrieval-Augmented Generation), sự đánh đổi (Trade-off) giữa việc chọn kích thước đoạn văn bản cắt nhỏ (Chunk Size) lớn hay nhỏ là gì?

- **A.** Gom cụm các vector thành các phân vùng không gian Voronoi (Voronoi Partitioning), trong giai đoạn truy vấn chỉ tìm kiếm trong $n_{\text{probe}}$ cụm gần nhất
- **B.** Xây dựng cây nhị phân không gian KD-Tree nhiều chiều để phân chia không gian thành các siêu phẳng trực giao có kích thước hình học bằng nhau
- **C.** Ánh xạ các vector vào bảng băm đa hướng thông qua các hàm băm nhạy cảm vị trí (Locality-Sensitive Hashing) với số lượng hàm băm cố định
- **D.** Sắp xếp toàn bộ tập dữ liệu vector theo thứ tự chuẩn bậc hai (L2 Norm Ordering) rồi áp dụng thuật toán tìm kiếm nhị phân chia đôi Binary Search

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Cắt đoạn nhỏ (100 chữ): Retriever tìm rất trúng trọng tâm câu hỏi, nhưng có thể mất ngữ cảnh đoạn trước đoạn sau (đọc xong không hiểu ai đang nói gì).
- Cắt đoạn lớn (1000 chữ): Đầy đủ ngữ cảnh, nhưng vector embedding bị ' pha loãng ' bởi quá nhiều thông tin râu ria, khiến công cụ tìm kiếm dễ bốc nhầm và tốn tiền gọi LLM!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Trade-off giữa Retrieval Precision (ưu tiên chunk nhỏ) và Context Comprehensiveness (ưu tiên chunk lớn). Thường kết hợp với Chunk Overlap $\approx 10-20\%$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Không có kích thước chunk nào hoàn hảo cho mọi bài toán, cần cân bằng giữa độ chính xác truy xuất và tính toàn vẹn ngữ cảnh.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 78 [OLP04-Q78] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Tại sao kiến trúc Reranker hai giai đoạn trong RAG thường sử dụng mô hình Bi-Encoder cho bước truy xuất sơ bộ (Retriever) và mô hình Cross-Encoder cho bước xếp hạng lại (Re-ranking)?

- **A.** Tỷ lệ các tài liệu truy xuất ra thực sự hữu ích và phù hợp (Precision at k) đối với nhu cầu thông tin tìm kiếm ban đầu của người dùng
- **B.** Thước đo chiết khấu tích lũy chuẩn hóa (Normalized Discounted Cumulative Gain - NDCG@k) đánh giá độ liên quan đa mức và vị trí xếp hạng của tài liệu
- **C.** Thời gian phản hồi truy vấn tính bằng mili-giây (Query Latency Measure) trên máy chủ dịch vụ tính từ khi nhận câu hỏi tới khi trả về kết quả
- **D.** Mức độ đa dạng thông tin giữa các tài liệu kết quả (Result Diversity Index) đo lường bằng khoảng cách Cosine trung bình giữa các vector được chọn

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Bi-Encoder (Retriever): Mã hóa câu hỏi và triệu tài liệu thành các vector riêng rẽ từ trước. Khi tìm kiếm chỉ cần nhân vô hướng siêu nhanh trong 5 mili-giây để bốc ra Top-50 tài liệu tiềm năng.
- Cross-Encoder (Reranker): Nạp từng cặp (Câu hỏi + Tài liệu) vào chung một mạng để các từ ' nhìn ngắm và so sánh chéo ' với nhau qua Self-Attention. Rất chậm nhưng cực kỳ chính xác, dùng để xếp hạng lại Top-50 ra Top-3 chuẩn xác nhất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Bi-Encoder: $s = E(q) \cdot E(d)$ (tính toán độc lập, lưu cache). Cross-Encoder: $s = M([q; d])$ (full cross-attention $O((L_q + L_d)^2)$). Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Cross-Encoder chính xác hơn Bi-Encoder nhưng quá chậm để quét hàng triệu tài liệu, do đó chỉ dùng làm Reranker trên tập nhỏ Top-K.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 79 [OLP04-Q79] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán Căn chỉnh Trực tiếp theo Sở thích DPO (Direct Preference Optimization - Rafailov et al., NeurIPS 2023) thay thế quy trình RLHF truyền thống bằng bước đột phá toán học nào?

- **A.** Làm mất tính chất liên tục của hàm mục tiêu (Loss Discontinuity) khiến thuật toán lan truyền ngược Gradient Descent không thể tính toán đạo hàm
- **B.** Mô hình sinh khuếch tán DDPM (Denoising Diffusion Probabilistic Models) đòi hỏi hàng trăm bước suy luận lặp tuần tự (Iterative Steps) để giải nhiễu ảnh
- **C.** Yêu cầu kích thước ma trận trọng số phải tăng theo hàm mũ (Exponential Parameter Growth) theo số lượng bước thời gian lấy mẫu trong quá trình suy luận
- **D.** Không thể huấn luyện song song trên phần cứng đa GPU (Multi-GPU Incompatibility) do các bước lấy mẫu bị ràng buộc điều kiện nhân quả chặt chẽ

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
RLHF cũ rất rườm rà và dễ sập: phải dạy 1 mạng chấm điểm (Reward Model), rồi dùng thuật toán PPO phức tạp để luyện LLM. DPO chứng minh bằng toán học: chính tỷ lệ xác suất giữa câu trả lời được thích ($y_w$) và câu bị chê ($y_l$) đã chứa trọn vẹn điểm thưởng! DPO vứt bỏ hoàn toàn mạng Reward và PPO, biến việc căn chỉnh thành bài toán phân loại nhị phân BCE siêu ổn định!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mathcal{L}_{\text{DPO}} = -\mathbb{E} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} \right) \right]$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** DPO vẫn dùng dữ liệu cặp so sánh của người $(x, y_w, y_l)$, nhưng KHÔNG cần huấn luyện mô hình thưởng riêng biệt.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§7.4 Policy Gradient, Actor-Critic, PPO**.

---

### Câu 80 [OLP04-Q80] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật lượng tử hóa sau huấn luyện AWQ (Activation-aware Weight Quantization - Lin et al., 2023) bảo vệ độ chính xác của LLM khi nén trọng số xuống INT4 nhờ vào nhận định cốt lõi nào?

- **A.** DDIM xem quá trình khuếch tán xuôi là phi Markov (Non-Markovian Forward Process) có cùng phân phối biên, cho phép nhảy cóc các bước thời gian khi lấy mẫu
- **B.** DDIM thay thế hoàn toàn mạng tích chập U-Net bằng mạng nơ-ron hồi quy tuần tự (Recurrent Neural Network) để giảm thiểu độ phức tạp tính toán thời gian
- **C.** DDIM lượng tử hóa toàn bộ trọng số của mô hình khuếch tán về định dạng số nguyên nhị phân 1-bit (One-bit Binary Weights) để tăng tốc độ suy luận
- **D.** DDIM sử dụng thuật toán tìm kiếm chùm tia (Beam Search Trajectory Exploration) để tìm kiếm trực tiếp đường đi ngắn nhất về không gian ảnh gốc

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
AWQ phát hiện: không phải nhìn vào trọng số to hay nhỏ để quyết định, mà phải nhìn vào ' dòng điện ' (kích hoạt Activation) chạy qua nó! Trọng số nào đón những xung kích hoạt khổng lồ thì đó là ' yết hầu ' (Salient weights, chiếm khoảng 1%). AWQ nhân phóng to các trọng số này lên để khi làm tròn số nguyên 4-bit không bị mất nét, giữ cho LLM thông minh y như bản gốc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tối ưu ma trận scale $S = \text{diag}(s)$: tìm $s$ tối thiểu hóa $\|W X - Q(W \cdot S^{-1})(S X)\|_F^2$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** AWQ dựa vào độ lớn của kích hoạt (Activation-aware), không phải độ lớn thô của trọng số (Weight-magnitude).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 81 [OLP04-Q81] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cơ chế chú ý nhóm truy vấn GQA (Grouped-Query Attention - Ainslie et al., 2023) được áp dụng trong LLaMA-2-70B và LLaMA-3 cân bằng hoàn hảo giữa Multi-Head Attention (MHA) và Multi-Query Attention (MQA) bằng cách nào?

- **A.** Đưa trực tiếp văn bản vào tầng đầu vào của mạng tích chập U-Net (Channel Concatenation) thông qua phép ghép nối ma trận với tensor ảnh bị nhiễu
- **B.** Sử dụng cơ chế chú ý chéo (Cross-Attention Mechanisms) giữa các vector đặc trưng văn bản từ CLIP Text Encoder và các feature map trong mạng U-Net
- **C.** Nhân toàn bộ các trọng số của mạng U-Net với tích vô hướng của vector nhúng văn bản (Scalar Dot-Product Modulation) trong từng khối tích chập
- **D.** Sử dụng bộ phân loại Softmax độc lập ở mỗi tầng của mạng U-Net (Layer-wise Softmax Head) để dự đoán ngôn ngữ tương ứng của chuỗi prompt

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- MHA: Mỗi đầu Query có 1 đầu KV riêng (chất lượng cao nhưng ngốn quá nhiều RAM cho KV cache).
- MQA: Tất cả các đầu Query dùng chung duy nhất 1 đầu KV (siêu nhẹ nhưng trí thông minh bị giảm sút).
- GQA (Giải pháp vàng): Gom các đầu Query thành từng nhóm (ví dụ 8 nhóm, mỗi nhóm 8 đầu Query dùng chung 1 đầu KV). Bộ nhớ KV cache nhẹ đi 8 lần mà chất lượng vẫn ngang ngửa MHA!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Số đầu Key/Value: $H_{KV} = H_Q / G$ với $1 < G < H_Q$. Giảm băng thông bộ nhớ suy luận $G$ lần. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** MQA dùng duy nhất 1 đầu KV cho toàn bộ Query; GQA chia thành các nhóm (Grouped). Chọn A.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 82 [OLP04-Q82] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Giải mã suy đoán (Speculative Decoding - Leviathan et al., 2023) giúp tăng tốc độ sinh văn bản của LLM lớn gấp 2-3 lần mà không làm thay đổi phân phối đầu ra nhờ vào nguyên lý nào?

- **A.** Tự động phân nhóm các điểm ảnh thành các cụm màu tương đồng (Color Quantization) để giảm độ biến thiên sắc độ của bức ảnh tổng hợp
- **B.** Khuếch đại độ lệch giữa dự đoán có điều kiện văn bản và không điều kiện (Classifier-Free Guidance - CFG): $\tilde{\epsilon} = \epsilon_u + s(\epsilon_c - \epsilon_u)$
- **C.** Lọc bỏ toàn bộ các tần số không gian cao trong miền Fourier (Low-Pass Fourier Filtering) để làm mịn các vùng chuyển tiếp giữa các chi tiết ảnh
- **D.** Thêm nhiễu ngẫu nhiên vào vector nhúng văn bản (Text Embedding Jittering) trong quá trình suy luận để kích thích tính đa dạng nghệ thuật của mô hình

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mô hình 70B sinh từng chữ rất chậm vì phải nạp 70 tỷ tham số qua RAM cho mỗi từ. Speculative Decoding cho một mô hình con 1B siêu nhanh viết nháp trước 5 chữ. Sau đó mô hình 70B chỉ cần liếc mắt 1 lần duy nhất để duyệt cả 5 chữ đó! Nếu duyệt đúng cả 5, ta được 5 chữ với thời gian của đúng 1 lần chạy, kết quả giống 100% bản gốc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thuật toán chấp nhận Speculative Rejection Sampling: chấp nhận $x$ với xác suất $\min(1, \frac{P(x)}{Q(x)})$, bảo toàn phân phối mục tiêu $P(x)$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Speculative Decoding đảm bảo tính toán ra đúng phân phối của mô hình lớn 100% (Lossless speedup), không làm suy giảm chất lượng.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 83 [OLP04-Q83] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình DINO (Self-distillation with no labels - Caron et al., ICCV 2021) khi áp dụng trên Vision Transformer khám phá ra hiện tượng kỳ diệu nào xuất hiện tự nhiên trong bản đồ tự chú ý (Self-Attention Maps) mà không hề có sự giám sát của con người?

- **A.** Chuyển ảnh thành vector tiềm ẩn qua bộ mã hóa VAE rồi tối ưu hàm mất mát đối kháng WGAN-GP (Wasserstein GAN Gradient Penalty) với mạng phân biệt Discriminator
- **B.** Đưa ảnh $x_0$ vào bộ mã hóa VAE (Variational Autoencoder) để nén thành biểu diễn $z_0$, sau đó thực hiện toàn bộ quá trình thêm và khử nhiễu trong không gian tiềm ẩn $z$
- **C.** Áp dụng thuật toán nén ảnh JPEG lượng tử hóa (Discrete Cosine Transform) trực tiếp trên các frame hình ảnh thô trước khi nạp vào mạng U-Net
- **D.** Phân tách ảnh thành các thành phần tần số độc lập qua biến đổi sóng con (2D Discrete Wavelet Transform) rồi khử nhiễu riêng biệt trên từng dải băng tần phụ

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Không cần bất kỳ ai dán nhãn hay vẽ viền, chỉ cho mạng tự học bằng phương pháp chưng cất tự thân (Student học từ Teacher qua phép biến đổi ảnh). Khi mở các tầng chú ý của ViT ra xem, các nhà khoa học ngỡ ngàng: mạng tự động vẽ ra đường viền phân vùng chuẩn xác từng milimet bao quanh con khủng long hay chú chim trong ảnh!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Chưng cất tự thân không nhãn: $H(P_t, P_s) = -\sum P_t(x) \log P_s(x)$ kết hợp Centering và Sharpening chống sụp đổ biểu diễn. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Điểm đột phá nổi tiếng nhất của bài báo DINO là ViT tự học được đặc trưng phân đoạn đối tượng (Unsupervised Object Segmentation).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 84 [OLP04-Q84] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình Masked Autoencoders (MAE - He et al., CVPR 2022) cho tiền huấn luyện thị giác tự giám sát che giấu bao nhiêu phần trăm mảnh ảnh (Patch Masking Ratio) và tại sao tỉ lệ này lại cao hơn nhiều so với tỷ lệ che trong BERT (15%)?

- **A.** Tự động đảo ngược thứ tự các tầng nơ-ron trong khối giải mã (Layer Reversal) để tái cấu trúc dòng chảy thông tin đặc trưng của toàn mạng
- **B.** Đóng băng toàn bộ trọng số gốc của mô hình U-Net, tạo một nhánh sao chép có thể huấn luyện kết nối với mô hình gốc qua các tầng tích chập Zero Convolution
- **C.** Thay thế toàn bộ các tầng tích chập không gian trong U-Net bằng các tầng biến đổi Fourier nhanh (Fast Fourier Transform Layers) để giữ cấu trúc biên
- **D.** Huấn luyện lại toàn bộ hàng tỷ tham số của mô hình Stable Diffusion từ đầu (Full Fine-Tuning) trên tập dữ liệu ảnh kèm bản đồ nét vẽ phác thảo

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ngôn ngữ rất cô đọng: giấu 1 chữ trong câu là mất nhiều nghĩa. Nhưng ảnh thì cực kỳ thừa thãi: nếu chỉ giấu 15%, máy chỉ cần nhìn các pixel xung quanh là đoán ngay được màu ô bị giấu mà chẳng cần hiểu bức tranh vẽ gì. MAE giấu sạch 75% bức ảnh (chỉ chừa lại 25% vụn vặt), ép mạng phải hiểu cấu trúc toàn cục mới vẽ lại được bức ảnh trọn vẹn!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tỉ lệ che tối ưu của MAE là $75\%$. Encoder chỉ xử lý $25\%$ patch không bị che, giúp tiết kiệm $3-4\times$ chi phí tính toán và bộ nhớ. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Tỉ lệ che của MAE là 75% (cao vượt bậc so với 15% của BERT).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 85 [OLP04-Q85] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc YOLOv8 (Ultralytics 2023) chuyển từ cơ chế dự đoán dựa trên hộp neo (Anchor-based) sang không dùng hộp neo (Anchor-free) mang lại lợi thế kỹ thuật nào?

- **A.** Triệt tiêu hiện tượng sụp đổ biểu diễn (Representation Collapse) bằng cách ép ma trận hiệp phương sai của các vector nhúng phải tiến gần ma trận đơn vị
- **B.** Cơ chế kéo gần biểu diễn của các ảnh cùng nguồn tăng cường (Positive Pairs) và đẩy xa biểu diễn của các ảnh khác biệt (Negative Pairs) qua InfoNCE Loss
- **C.** Tăng tốc độ lan truyền ngược qua việc xấp xỉ ma trận Jacobi bằng ma trận đường chéo (Diagonal Approximation) giúp tiết kiệm bộ nhớ đệm đồ thị tính toán
- **D.** Tự động phân nhóm các vector đặc trưng vào các cụm phân bố chuẩn đa chiều (Gaussian Mixture Modeling) nhằm đơn giản hóa hàm mất mát phân loại

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Anchor-based cũ đòi hỏi bạn phải ngồi phân cụm K-Means chọn kích thước hộp neo sẵn (nếu chọn sai hộp neo cho tập dữ liệu mới, mô hình bắt vật thể rất tệ). Anchor-free của YOLOv8 dự đoán thẳng khoảng cách từ điểm tâm ra 4 cạnh $[l, t, r, b]$, không cần hộp neo mẫu nào cả, giúp mô hình bắt vật thể to nhỏ méo mó tự nhiên và dễ dàng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Anchor-free Decoupled Head: tách riêng nhánh phân loại (BCE) và nhánh hồi quy tọa độ (CIoU + DFL). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** YOLOv8 là anchor-free, loại bỏ bước chọn anchor thủ công.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.

---

### Câu 86 [OLP04-Q86] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán Soft-NMS (Bodla et al., ICCV 2017) khắc phục nhược điểm xóa nhầm vật thể đứng chen chúc (Occlusion) của Standard Hard-NMS bằng cơ chế suy giảm điểm số nào?

- **A.** Mô hình dừng huấn luyện khi tỷ lệ các mẫu âm tính vượt quá ngưỡng 90% (Early Stopping Condition) nhằm tránh bão hòa hàm phân loại đa lớp
- **B.** Mô hình ánh xạ mọi ảnh đầu vào thành cùng một vector hằng số cố định duy nhất (Trivial Constant Output), dẫn đến độ mất mát bằng 0 nhưng vô giá trị
- **C.** Trọng số của mạng nơ-ron tích chập bị bùng nổ tiến tới vô cùng (Gradient Explosion Phenomenon) do mẫu số của hàm mất mát tiệm cận về giá trị 0
- **D.** Ma trận biểu diễn đặc trưng bị suy biến thành ma trận trực giao đường chéo (Diagonal Orthogonality) làm mất mát hoàn toàn thông tin tương quan kênh

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi hai người đứng chen chúc ôm nhau, 2 hộp bao của họ bị đè lên nhau (IoU cao). Hard-NMS thẳng tay xóa luôn hộp của người thứ hai (làm mất người!). Soft-NMS nhân từ hơn: nó không xóa, mà chỉ hạ nhẹ điểm tin cậy của hộp thứ hai xuống theo hàm Gauss. Nhờ đó, người thứ hai vẫn được phát hiện mà không bị nuốt mất!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $s_i = s_i e^{-\frac{\text{IoU}(M, b_i)^2}{\sigma}}$. Điểm số giảm tỷ lệ với độ chồng lấn thay vì bị gán 0 đột ngột. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Soft-NMS làm suy giảm điểm số (score decay), không phải xóa cứng (loại A) hay gộp hộp (loại D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.

---

### Câu 87 [OLP04-Q87] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong tập chuẩn đánh giá COCO Object Detection, độ đo mAP@[.50:.05:.95] được tính toán bằng cách nào?

- **A.** Duy trì một hàng đợi động lưu trữ các vector mẫu âm (Dynamic Queue of Negative Embeddings) và cập nhật mạng Encoder tạo khóa thông qua Moving Average
- **B.** Tăng kích thước lô huấn luyện mini-batch lên $65.536$ mẫu trên cụm 512 GPU đồng bộ (Massive Distributed Batching) để tích lũy đủ số mẫu âm
- **C.** Loại bỏ hoàn toàn các mẫu âm khỏi hàm mất mát và chỉ tối ưu hóa độ tương đồng Cosine giữa hai góc nhìn tăng cường của cùng một bức ảnh gốc
- **D.** Sử dụng một mạng phân biệt đối kháng riêng biệt (Adversarial Discriminator Network) để sinh ra các mẫu âm giả lập có độ khó cực đại theo thời gian

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ngưỡng IoU = 0.50 khá dễ tính (hộp hơi lệch một chút vẫn cho qua). Để đánh giá xem mô hình vẽ hộp có khít khao sắc nét hay không, COCO tính điểm mAP ở 10 mức khắt khe khác nhau: 0.50, 0.55, 0.60, ..., 0.95 (cực kỳ nghiêm ngặt) rồi lấy trung bình cộng của cả 10 con số này lại!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\text{mAP} = \frac{1}{10} \sum_{\text{IoU}=0.50, 0.55, \dots, 0.95} \text{mAP}_{\text{IoU}}$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A là PASCAL VOC metric (mAP@0.50), còn COCO chuẩn là trung bình 10 mức từ 0.50 đến 0.95.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.

---

### Câu 88 [OLP04-Q88] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình ControlNet (Zhang et al., ICCV 2023) bổ sung điều kiện kiểm soát không gian (như cạnh Canny, bản đồ độ sâu Depth, tư thế người Pose) vào mạng khuếch tán Diffusion mà không làm hỏng trọng số gốc nhờ kỹ thuật nào?

- **A.** Thực hiện phép phân rã ma trận kỳ dị (Online Singular Value Decomposition) trên các vector kích hoạt nơ-ron sau mỗi bước cập nhật trọng số
- **B.** Sử dụng kiến trúc bất đối xứng: nhánh Online có thêm khối dự đoán (Predictor MLP) và nhánh Target được cập nhật trọng số chậm qua Moving Average (EMA)
- **C.** Ép buộc ma trận hiệp phương sai giữa các chiều biểu diễn phải là ma trận đường chéo (Diagonal Covariance Constraint) để triệt tiêu tương quan chéo
- **D.** Áp dụng cơ chế chuẩn hóa theo lô nhỏ với kích thước batch bằng 1 (Instance Normalization Mode) để xóa bỏ hoàn toàn thông tin thống kê toàn cục

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
ControlNet khóa chặt mô hình vẽ tranh Stable Diffusion gốc (không cho sửa đổi để giữ nguyên tài năng vẽ đẹp). Nó tạo ra một bản sao song song và nối lại bằng các tầng ' Zero Convolution ' (ban đầu trọng số bằng 0 tuyệt đối). Khi mới bắt đầu, nhánh phụ không gây bất kỳ tác động nào; sau đó nó học dần dần cách điều khiển nét vẽ theo khung xương hay nét vẽ viền!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Zero Convolution: $W=0, B=0 \implies \mathcal{Z}(x; 0, 0) = 0$ tại bước khởi đầu, đảm bảo không có nhiễu gradient phá vỡ mô hình gốc. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Zero Convolution với $W=0, b=0$ là phát minh then chốt của ControlNet.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 89 [OLP04-Q89] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong học tự giám sát SimSiam (Chen & He, CVPR 2021), hiện tượng sụp đổ biểu diễn (Representation Collapse: tất cả các ảnh đều bị biến thành cùng một vector hằng số vô nghĩa) được ngăn chặn mà KHÔNG CẦN mẫu âm, batch size khổng lồ hay mạng momentum nhờ vào thao tác kỹ thuật nào?

- **A.** Thêm nhiễu trắng Gaussian có phương sai bằng 100 vào tầng đầu ra (`noise_injection`) để phá vỡ cấu trúc điểm cân bằng tầm thường của mạng
- **B.** Ép buộc ma trận trọng số phải có định thức âm ở tất cả các tầng (`negative_determinant`) nhằm ngăn chặn sự co cụm của các vector đặc trưng
- **C.** Toán tử dừng gradient (Stop-gradient: `stop_gradient` / `detach()`) áp dụng trên một trong hai nhánh kiến trúc Siamese đối xứng trong quá trình tối ưu
- **D.** Sử dụng hàm mất mát sai số toàn phương trung bình (`mean_squared_error`) thay cho độ tương đồng Cosine để duy trì biên độ khoảng cách vector

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu hai nhánh mạng sinh đôi cứ bắt chước nhau, cách lười biếng nhất để đạt điểm tối đa là cả hai cùng xuất ra vector [0, 0, ..., 0] cho mọi bức ảnh (sụp đổ biểu diễn). SimSiam giải quyết cực kỳ kỳ diệu: chỉ cần chặn không cho dòng gradient chảy qua một bên (`stop_gradient`), bên kia bị buộc phải tự vận động tìm đặc trưng thực sự để đuổi theo, triệt tiêu hoàn toàn nguy cơ sụp đổ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mathcal{L} = \frac{1}{2} \mathcal{D}(p_1, \text{stop\_gradient}(z_2)) + \frac{1}{2} \mathcal{D}(p_2, \text{stop\_gradient}(z_1))$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phát minh của SimSiam là chứng minh `stop-gradient` là thành phần tối quan trọng để chống collapse.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 90 [OLP04-Q90] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Chuỗi Suy luận Tự nhất quán (Self-Consistency CoT - Wang et al., ICLR 2023) cải thiện độ chính xác giải toán và lập luận logic của LLM bằng phương pháp nào?

- **A.** Huấn luyện lại toàn bộ mô hình bằng thuật toán lan truyền ngược trên tập dữ liệu GSM8K (Supervised Fine-Tuning) với lịch trình học giảm dần
- **B.** Ép buộc nhiệt độ giải mã bằng đúng 0 (Greedy Deterministic Decoding) trong mọi lượt suy luận để loại bỏ hoàn toàn tính bất định của chuỗi sinh
- **C.** Lấy mẫu giải mã nhiều đường suy luận CoT độc lập với nhiệt độ $T > 0$, sau đó chọn câu trả lời cuối cùng xuất hiện nhiều nhất thông qua biểu quyết đa số (Majority Voting)
- **D.** Cắt bớt 50% câu hỏi đầu vào để mô hình tập trung vào phần kết luận (Context Truncation Strategy) nhằm giảm độ phức tạp tính toán ngữ cảnh

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Một bài toán khó có nhiều cách giải. Self-Consistency cho LLM giải bài toán đó 10 lần bằng các đường suy nghĩ khác nhau (nhiệt độ $T > 0$). Trong 10 lần giải, nếu có 7 lần ra đáp số là '42' và 3 lần ra đáp số khác, hệ thống sẽ chọn đáp số '42' theo nguyên tắc số đông (Majority Vote). Cách này loại bỏ hầu hết các lỗi tính nhẩm ngớ ngẩn của LLM!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\hat{a} = \arg\max_a \sum_{i=1}^N \mathbb{I}(\text{extract\_ans}(r_i) = a)$ với $r_i \sim \text{LLM}(x)$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Self-Consistency bắt buộc phải lấy mẫu đa dạng ($T > 0$), không dùng Greedy $T=0$ (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 91 [OLP04-Q91] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Bộ tiêu chuẩn đánh giá HumanEval (Chen et al., OpenAI 2021) đo lường khả năng sinh mã nguồn Python của LLM bằng chỉ số pass@k được tính chính xác không chệch (Unbiased Estimator) theo công thức nào khi sinh $n$ mẫu lời giải ($n \ge k$)?

- **A.** $\text{pass}@k = \frac{c}{n}$ ước lượng tỷ lệ các mẫu bài toán đơn lẻ vượt qua kiểm thử đơn vị trong tổng số $n$ mẫu sinh ra độc lập
- **B.** $\text{pass}@k = \frac{k \cdot c}{n}$ nhân trực tiếp tỷ lệ mẫu thành công với số lượng lượt thử nghiệm phân bổ cho bài toán lập trình
- **C.** $\text{pass}@k = \left(\frac{c}{n}\right)^k$ lũy thừa xác suất thành công độc lập nhằm đo lường khả năng vượt qua đồng thời của toàn bộ $k$ lời giải
- **D.** $\text{pass}@k = 1 - \frac{\binom{n - c}{k}}{\binom{n}{k}}$ với $c$ là số lượng mẫu lời giải vượt qua toàn bộ các bộ unit test trong tổng số $n$ mẫu được sinh ra

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Để đo xem ' sinh $k$ lần thì có ít nhất 1 lần viết code đúng hay không ', nếu chạy trực tiếp $k$ lần thì phương sai rất lớn. OpenAI sinh $n$ đoạn code (ví dụ 100 đoạn), đếm xem có $c$ đoạn đúng. Sau đó dùng công thức tổ hợp xác suất bốc ngẫu nhiên $k$ đoạn từ $n$ đoạn để tính ra xác suất có ít nhất 1 đoạn đúng: $1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}$ cực kỳ chuẩn xác và không bị lệch!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Xác suất không có mẫu nào đúng trong $k$ lần rút: $\frac{\binom{n-c}{k}}{\binom{n}{k}}$. Do đó $\text{pass}@k = 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Công thức HumanEval chuẩn của OpenAI dùng ước lượng tổ hợp siêu bội không chệch (Unbiased estimator).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---

### Câu 92 [OLP04-Q92] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp phát hiện mẫu ngoài phân phối OOD (Out-of-Distribution Detection) dựa trên khoảng cách Mahalanobis trong không gian đặc trưng biểu diễn $z$ (Lee et al., NeurIPS 2018) vượt trội hơn phương pháp xác suất Softmax cực đại (MSP) nhờ yếu tố nào?

- **A.** Sử dụng ngưỡng xác suất Softmax cực đại (Maximum Softmax Probability - MSP) gán nhãn cho các mẫu OOD dựa trên độ tự tin cực đại của tầng phân loại
- **B.** Tính điểm số mức năng lượng tự do (Energy-based Out-of-Distribution Scoring) tích hợp trên toàn bộ các giá trị logit mà không cần ước lượng tham số phân phối
- **C.** Đo khoảng cách Euclid chuẩn hóa (Normalized Euclidean Distance Metric) từ mẫu kiểm tra tới tâm trọng lực gần nhất của các lớp trong tập huấn luyện
- **D.** Sử dụng ma trận hiệp phương sai chung $\Sigma$ để tính khoảng cách Mahalanobis $d_M(z, \mu_c) = (z - \mu_c)^T \Sigma^{-1} (z - \mu_c)$, khắc phục hiện tượng mạng nơ-ron tự tin thái quá

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mạng nơ-ron có tật xấu là ' tự tin mù quáng ': đưa một bức ảnh chiếc máy bay vào mạng phân loại Chó/Mèo, Softmax vẫn tự tin tuyên bố ' Chó 99%'! Khoảng cách Mahalanobis nhìn thẳng vào không gian đặc trưng ẩn: đo xem điểm đó cách các cụm dữ liệu quen thuộc bao xa theo hình học elip. Nếu điểm nằm xa tít mọi cụm, nó lập tức báo động là dữ liệu lạ (OOD)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Điểm bất thường: $M(x) = \max_c - (f(x) - \hat{\mu}_c)^T \hat{\Sigma}^{-1} (f(x) - \hat{\mu}_c)$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** MSP (Maximum Softmax Probability) bị lỗi overconfidence; Mahalanobis distance trong không gian embedding đo khoảng cách hình học chuẩn xác.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Đánh Giá Mô Hình & Cross-Validation**.

---

### Câu 93 [OLP04-Q93] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong giám sát hệ thống Machine Learning triển khai thực tế (Production ML Monitoring), chỉ số Ổn định Dân số PSI (Population Stability Index) được tính bằng công thức $\text{PSI} = \sum (P_i - B_i) \ln(P_i / B_i)$ giữa phân phối thực tế $P$ và phân phối chuẩn cơ sở $B$. Ngưỡng giá trị PSI nào cảnh báo mô hình bắt đầu bị trôi dạt dữ liệu (Data Drift) mức độ vừa phải?

- **A.** $\text{PSI} < 0.01$ (phân phối dữ liệu hoàn toàn ổn định tuyệt đối, không ghi nhận bất kỳ dấu hiệu biến động nào giữa hai giai đoạn quan sát)
- **B.** $\text{PSI} = 0.0$ (phân phối dữ liệu đã bị biến đổi hoàn toàn sang một miền giá trị mới, đòi hỏi phải dừng hoạt động hệ thống ngay lập tức)
- **C.** $\text{PSI} > 10.0$ (chỉ số bình thường của mọi hệ thống học máy triển khai thực tế trong ngành tài chính ngân hàng và thương mại điện tử)
- **D.** $0.1 \le \text{PSI} < 0.2$ (trôi dạt mức độ vừa phải, cần theo dõi sát sao hoặc chuẩn bị huấn luyện lại mô hình để đảm bảo độ chính xác)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Quy tắc kinh nghiệm chuẩn trong công nghiệp:
- $\text{PSI} < 0.1$: Dữ liệu ổn định, mô hình chạy phà phà.
- $0.1 \le \text{PSI} < 0.2$: Bắt đầu có sự thay đổi nhẹ trong hành vi người dùng, cần chuẩn bị tinh thần cập nhật mô hình.
- $\text{PSI} \ge 0.2$: Dữ liệu đã trôi dạt nghiêm trọng (Significant Drift), bắt buộc phải huấn luyện lại (Retrain) ngay lập tức!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\text{PSI} = \sum_{i=1}^k (\text{Actual}_i - \text{Expected}_i) \times \ln\left(\frac{\text{Actual}_i}{\text{Expected}_i}\right)$. Ngưỡng chuẩn: $0.1 \le \text{PSI} < 0.2$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** $\text{PSI} \ge 0.2$ là trôi dạt nghiêm trọng; $0.1 \le \text{PSI} < 0.2$ là mức độ vừa phải (Moderate shift).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Đánh Giá Mô Hình & Cross-Validation**.

---

### Câu 94 [OLP04-Q94] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Sự khác biệt cốt lõi giữa Trôi dạt Khái niệm (Concept Drift) và Trôi dạt Dữ liệu (Data Drift / Covariate Shift) trong bài toán Machine Learning thực tế là gì?

- **A.** Concept Drift là hiện tượng phương sai biến thiên dữ liệu đầu vào thay đổi đột ngột (Input Covariance Shift) có thể khắc phục hoàn toàn bằng cách áp dụng chuẩn hóa phân phối StandardScaler cho các thuộc tính
- **B.** Concept Drift chỉ phát sinh trong các bài toán xử lý ngôn ngữ tự nhiên còn Data Drift chỉ xảy ra đối với các bài toán thị giác máy tính và phân loại hình ảnh đa phương thức (Multimodal Domain Gap)
- **C.** Data Drift làm giảm số lượng đặc trưng đầu vào xuống mức tối thiểu (Feature Space Reduction) trong khi Concept Drift làm tăng đột biến số lượng nhãn phân loại của tầng Softmax đầu ra trên môi trường phục vụ
- **D.** Data Drift là khi phân phối đầu vào thay đổi $P(X) \ne P_{\text{old}}(X)$ nhưng mối quan hệ $P(Y \mid X)$ không đổi; Concept Drift là khi mối quan hệ bản chất giữa đầu vào và nhãn thay đổi $P(Y \mid X) \ne P_{\text{old}}(Y \mid X)$

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Data Drift (Covariate Shift): Người dùng đổi sang mua sắm vào ban đêm nhiều hơn ban ngày ($P(X)$ đổi), nhưng ai mua hàng thì vẫn là mua hàng ($P(Y|X)$ giữ nguyên).
- Concept Drift: Lạm phát kinh tế xảy ra, trước đây thu nhập 10 triệu là khách hàng giàu ($Y=1$), bây giờ 10 triệu là nghèo ($Y=0$). Định nghĩa của bài toán đã bị thay đổi tận gốc rễ ($P(Y|X)$ đổi)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Covariate Shift: $P_{\text{train}}(X) \ne P_{\text{test}}(X)$, $P(Y|X)$ bất biến. Concept Drift: $P_{\text{train}}(Y|X) \ne P_{\text{test}}(Y|X)$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Concept Drift làm thay đổi ánh xạ $P(Y|X)$, là dạng trôi dạt nguy hiểm nhất đòi hỏi phải gán nhãn mới và retrain mô hình.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Đánh Giá Mô Hình & Cross-Validation**.

---

### Câu 95 [OLP04-Q95] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình nén sinh ảnh nhất quán LCM (Latent Consistency Models - Luo et al., 2023) tăng tốc suy luận sinh ảnh từ 50 bước khuếch tán xuống chỉ còn 2 đến 4 bước nhờ giải bài toán gì?

- **A.** Sử dụng mô hình rừng ngẫu nhiên (Random Forest Regressor) để ngoại suy trực tiếp hình ảnh đích từ trạng thái nhiễu ban đầu mà không cần tính tích chập
- **B.** Loại bỏ hoàn toàn không gian tiềm ẩn và thực hiện tính toán vi phân trực tiếp trên miền tần số Fourier thông qua các toán tử biến đổi trực giao nhanh
- **C.** Chuyển toàn bộ các tầng mạng nơ-ron thành một bảng tra cứu tĩnh đa chiều (Multi-dimensional Look-up Table) để truy xuất nghiệm giải tích trong một chu kỳ
- **D.** Ép hàm ánh xạ dự đoán điểm xuất phát trên quỹ đạo phương trình vi phân xác suất (PF-ODE) ánh xạ trực tiếp bất kỳ trạng thái $x_t$ nào về nghiệm $x_0$ thông qua hàm nhất quán $f_\theta(x_t, t) = x_0$

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mô hình khuếch tán cũ phải ' bước từng bước nhỏ ' (50 bước khử nhiễu) dọc theo đường cong vi phân để về đến đích $x_0$. Consistency Model dạy mạng một nguyên lý nhất quán: Dù bạn đang đứng ở bất kỳ khúc cua nào trên con đường ($t=500$ hay $t=200$), một bước nhảy duy nhất của hàm $f_\theta$ phải chỉ thẳng về đúng ngôi nhà $x_0$! Nhờ đó chỉ cần 2 đến 4 bước là sinh xong bức ảnh tuyệt đẹp!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Consistency Function: $f_\theta(x_t, t) = f_\theta(x_{t '}, t ') = x_0$ với mọi cặp điểm $(x_t, t)$ và $(x_{t '}, t ')$ nằm trên cùng một quỹ đạo ODE. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** LCM giải Consistency Mapping trên PF-ODE, cho phép sinh ảnh siêu tốc 2-4 bước thời gian thực (Real-time).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 96 [OLP04-Q96] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình BLIP-2 (Li et al., ICML 2023) cho bài toán đa phương thức Thị giác - Ngôn ngữ (VLM), module kiến trúc Q-Former (Querying Transformer) đóng vai trò làm cầu nối như thế nào giữa Image Encoder và LLM?

- **A.** Thay thế hoàn toàn bộ giải mã văn bản của LLM bằng mạng tích chập 1D (Temporal 1D-CNN Sequence Encoder) để trích xuất các chuỗi đặc trưng thời gian từ tensor hình ảnh liên tục qua các khung hình video
- **B.** Huấn luyện lại toàn bộ hàng chục tỷ tham số của cả Image Encoder và LLM từ đầu (End-to-End Joint Training) bằng tập dữ liệu hàng tỷ cặp ảnh-chú thích chất lượng cao thu thập từ môi trường mạng web
- **C.** Chuyển đổi toàn bộ tensor điểm ảnh thành chuỗi mã hóa ký tự nhị phân ASCII rồi truyền trực tiếp vào cửa sổ ngữ cảnh đầu vào (Raw Text Context Prompt) của mô hình ngôn ngữ lớn để tự suy luận hình ảnh
- **D.** Sử dụng một tập hợp cố định các vector truy vấn học được (Learned Queries) để trích xuất một số lượng cố định các đặc trưng thị giác cô đọng từ Image Encoder bị đóng băng, sau đó chiếu vào không gian chiều của LLM bị đóng băng

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cả Image Encoder (như ViT) và LLM đều là các ' gã khổng lồ ' đắt đỏ. BLIP-2 khóa chặt cả 2 gã khổng lồ này (không tốn tiền huấn luyện lại). Ở giữa, nó đặt một module ' phiên dịch viên ' nhỏ nhắn gọi là Q-Former: dùng 32 câu hỏi mẫu (queries) để hỏi Image Encoder và rút ra 32 mẩu thông tin thị giác tinh túy nhất, rồi đưa cho LLM đọc và trả lời mượt mà!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Q-Former gồm 2 giai đoạn tiền huấn luyện: Representation Learning (với Image Encoder đóng băng) và Generative Learning (với LLM đóng băng). Rút gọn hàng ngàn visual tokens về 32 embedding tokens. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Điểm sáng giá nhất của BLIP-2 là Q-Former làm cầu nối giữa Frozen Image Encoder và Frozen LLM, tiết kiệm chi phí tính toán khổng lồ.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 97 [OLP04-Q97] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Mixture of Depths (MoD - Raposo et al., Google DeepMind 2024) tối ưu hóa việc phân bổ tài nguyên tính toán trong Transformer bằng cơ chế nào?

- **A.** Ép toàn bộ các token trong chuỗi văn bản phải đi qua tất cả các tầng mạng (Uniform Static Computation) với số lượng phép tính cố định không phụ thuộc vào độ phức tạp ngữ nghĩa thực tế của ngữ cảnh đầu vào
- **B.** Tự động xóa bỏ vĩnh viễn 50% số tầng Transformer sau khi kết thúc pha huấn luyện (Static Structured Pruning Strategy) để tối ưu hóa tài nguyên phần cứng suy luận trên các cụm máy chủ điện toán đám mây
- **C.** Nhân đôi độ sâu của các khối mạng nơ-ron đối với mọi câu văn bản có độ dài ngữ cảnh vượt quá 512 token (Length-Dependent Deepening Policy) nhằm tăng dung lượng biểu diễn thông tin ngữ nghĩa dài
- **D.** Định tuyến động (Dynamic Routing) cho phép mô hình quyết định token nào cần được tính toán qua khối Self-Attention / MLP của một tầng, trong khi các token đơn giản khác được nhảy cóc (Skip) qua tầng đó thông qua kết nối tắt

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong câu văn, có những từ rất dễ đoán (như dấu chấm, từ ' là ', ' của ') không cần tốn nơ-ron suy nghĩ. MoD đặt một bộ điều phối tại mỗi tầng: từ nào khó và quan trọng thì cho đi qua tầng sâu để suy nghĩ kỹ; từ nào dễ thì cho đi ' đường tắt ' nhảy cóc qua tầng luôn! Nhờ đó mô hình chạy nhanh hơn 50% mà độ thông minh không suy giảm!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Top-$K$ router chọn tối đa $K$ token tham gia tính toán block ($K < S$). Các token ngoài top-$K$ đi qua identity residual connection. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** MoD định tuyến động trên chiều sâu (Depth), token đơn giản được skip tầng.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 98 [OLP04-Q98] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình DINOv2 (Oquab et al., Meta AI 2023) đạt được khả năng tạo biểu diễn thị giác tổng quát vượt trội ở cấp độ cả bức ảnh lẫn cấp độ từng điểm ảnh (Patch-level) nhờ kết hợp hai hàm mất mát tự giám sát nào?

- **A.** Hàm mất mát sinh đối kháng WGAN-GP (học từ token `[GEN]`) kết hợp với hàm mục tiêu khử nhiễu mô hình khuếch tán xác suất DDPM (học khôi phục các trạng thái ảnh tiềm ẩn)
- **B.** Hàm mất mát phân loại Cross-Entropy có giám sát trên 1 tỷ nhãn thủ công (học từ token `[IMG]`) kết hợp với hàm tối ưu khoảng cách Cosine đa góc nhìn không gian biểu diễn
- **C.** Hàm mất mát hồi quy bounding box CIoU Loss (học từ token `[BOX]`) kết hợp với hàm phân loại Focal Loss trên toàn bộ tập dữ liệu chú thích phát hiện vật thể quy mô lớn
- **D.** Hàm mất mát cấp độ ảnh Image-level DINO Loss (học từ token `[CLS]`) kết hợp với hàm mất mát cấp độ mảnh Masked Image Modeling iBOT Loss (học khôi phục các patch bị che)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
DINOv2 kết hợp 2 sức mạnh:
1. DINO Loss (toàn cục): giúp token `[CLS]` hiểu ý nghĩa tổng quan của cả bức ảnh.
2. iBOT Loss (cục bộ): giấu các mảnh nhỏ trong ảnh và bắt mạng đoán lại đặc trưng của từng mảnh.
Nhờ kết hợp cả ' rừng ' (toàn cục) lẫn ' cây ' (từng mảnh), vector của DINOv2 dùng để phân loại ảnh hay phân vùng chi tiết từng vật thể đều đạt điểm số cao kỷ lục!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\mathcal{L}_{\text{DINOv2}} = \mathcal{L}_{\text{DINO}} + \mathcal{L}_{\text{iBOT}} + \mathcal{L}_{\text{KoLeo}}$ (thêm KoLeo regularizer để phân tán đều các vector). Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** DINOv2 là mô hình học tự giám sát thuần túy (Self-Supervised), không cần nhãn thủ công ImageNet (loại B).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 99 [OLP04-Q99] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán FlashAttention-2 (Dao, 2023) tăng tốc độ tính toán lên gấp 2 lần so với FlashAttention-1 ban đầu nhờ vào cải tiến thuật toán nào sau đây?

- **A.** Chuyển đổi toàn bộ các ma trận trọng số sang biểu diễn số nguyên nhị phân 1-bit (1-bit Integer Quantization) để thay thế phép nhân bằng phép XNOR
- **B.** Thay thế các nhân Tensor Cores bằng các lệnh tính toán số học ALUs truyền thống (Standard Arithmetic ALUs) để giảm độ phức tạp điều khiển vi kiến trúc
- **C.** Loại bỏ hoàn toàn cơ chế chia khối Tiling và đọc trực tiếp dữ liệu từ bộ nhớ băng thông cao HBM (Direct HBM Access) trong mỗi chu kỳ xung nhịp
- **D.** Song song hóa (Parallelization) trực tiếp trên chiều dài chuỗi token $N$ thay vì chỉ song song trên Batch và Heads, đồng thời tối ưu hóa việc phân chia công việc giữa các Warp trong luồng GPU

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong FlashAttention-1, khi batch size nhỏ (ví dụ chỉ có 1 câu dài 100.000 từ), nhiều nhân của card GPU bị ' ngồi chơi xơi nước ' vì chỉ chia việc theo batch. FlashAttention-2 chia nhỏ chính chuỗi 100.000 từ đó ra cho tất cả các nhân GPU cùng tính song song, đồng thời bớt các phép tính chia thừa thãi, giúp tăng tốc gấp đôi và đạt 73% hiệu suất tối đa của chip A100/H100!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Parallelize over sequence length dimension, giảm non-matmul FLOPs trong online softmax rescale. Đạt $\approx 225$ TFLOPs/s trên A100. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** FlashAttention-2 vẫn giữ nguyên tính chính xác 100% (Exact Attention) và cơ chế Tiling trên SRAM.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3 Cơ Chế Attention & Kiến Trúc Transformer**.

---

### Câu 100 [OLP04-Q100] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi đánh giá toàn diện mô hình ngôn ngữ lớn trên bộ tiêu chuẩn Massive Multitask Language Understanding (MMLU - Hendrycks et al., ICLR 2021), phương pháp đo lường 5-shot được thực hiện như thế nào?

- **A.** Chia đề thi trắc nghiệm thành 5 phần bằng nhau (5-Fold Test Partitioning) và lấy trung bình cộng điểm số của tất cả các phần để xếp hạng năng lực
- **B.** Cho mô hình làm bài thi 5 lần độc lập với các hạt ngẫu nhiên khác nhau (Multi-seed Repetition) rồi lấy kết quả điểm số cao nhất làm đại diện
- **C.** Huấn luyện tinh chỉnh mô hình trên 5 epoch (5-Epoch Fine-Tuning) bằng tập dữ liệu câu hỏi ôn tập trước khi bắt đầu bài kiểm tra đánh giá chính thức
- **D.** Cung cấp chính xác 5 ví dụ minh họa kèm câu hỏi và lời giải mẫu (5-shot In-context Learning) trong prompt ngữ cảnh trước khi đưa ra câu hỏi trắc nghiệm kiểm thử

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
'5-shot ' là dạy mẫu trong đề bài: Trước khi hỏi câu hỏi thật, bạn ghi sẵn 5 câu hỏi ví dụ kèm câu trả lời mẫu ngay trong đoạn văn bản gửi cho mô hình. Mô hình đọc 5 ví dụ đó để hiểu quy cách làm bài (định dạng A, B, C, D) rồi mới trả lời câu hỏi chính thức!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 In-context learning: Prompt gồm $5$ cặp $(x_i, y_i)$ mẫu và câu hỏi truy vấn $x_{\text{test}}$. Tính độ chính xác accuracy trên 57 môn học. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** K-shot trong LLM benchmark là số lượng ví dụ mẫu đưa vào prompt ngữ cảnh (In-context learning), không phải số epoch fine-tune (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.4 Các Mô Hình Ngôn Ngữ Lớn (LLMs)**.

---
