# ĐỀ THI CHÍNH THỨC OLYMPIC TRÍ TUỆ NHÂN TẠO 2025 (VOAI 2025)
## Vòng Sơ Loại — Mã Đề 006 (100 Câu — 180 Phút)

> **Nguồn gốc học thuật:** Đề thi chính thức do Ban Tổ Chức Olympic Tin Học Sinh Viên & Olympic Trí Tuệ Nhân Tạo Quốc Gia (VOAI) ban hành năm 2025.
> **Lời giải đối chiếu chi tiết:** Biên soạn và phân tích chuyên sâu đối chiếu với nguồn lời giải tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 01 [VOAI25-001] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong mạng nơ-ron, chuẩn hóa lô (Batch Normalization) thường được đặt ở đâu?

- **A.** Trước hàm kích hoạt ReLU và sau lớp tuyến tính (Linear)
- **B.** Sau hàm kích hoạt ReLU và trước lớp tuyến tính tiếp theo
- **C.** Sau lớp bỏ ngẫu nhiên (Dropout) và trước lớp đầu ra mạng
- **D.** Trước lớp đầu vào (Input Layer) của toàn bộ đồ thị mạng

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Theo bài báo gốc của Ioffe và Szegedy (2015), Batch Normalization (BN) được thiết kế. đểáp dụng trước hàm kích hoạt phi tuyến tính (như ReLU) và sau phép biến đổi tuyến.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Theo bài báo gốc của Ioffe và Szegedy (2015), Batch Normalization (BN) được thiết kế
đểáp dụng trước hàm kích hoạt phi tuyến tính (như ReLU) và sau phép biến đổi tuyến
tính (Convolution hoặc Linear/Fully Connected). Mặc dù trong thực tếđôi khi người ta
đặt sau ReLU, nhưng về mặt lý thuyết chuẩn mực và các đáp án được đưa ra, đáp án A
là chính xác nhất.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.8** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 1). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 02 [VOAI25-002] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thành phần nào sau đây là một tham số có thể học trong một lớp tích chập ?

- **A.** Kích thước của dữ liệu đầu vào
- **B.** Các giá trị trong bộ lọc
- **C.** Kích thước bước nhảy
- **D.** Kích thước padding

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong mạng tích chập (CNN), các tham số " học được "(learnable parameters) chính là các. trọng số (weights) nằm trong các bộ lọc (filters/kernels) và bias (nếu có).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Trong mạng tích chập (CNN), các tham số " học được "(learnable parameters) chính là các
trọng số (weights) nằm trong các bộ lọc (filters/kernels) và bias (nếu có). Kích thước bước
nhảy (stride), padding hay kích thước đầu vào là các siêu tham số (hyperparameters)
được thiết lập trước và không thay đổi qua quá trình backpropagation.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 2). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 03 [VOAI25-003] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Nếu mất mát (loss) không giảm sau 5 vòng lặp (epoch) đầu tiên dù tỷ lệ học là 0.001, bạn nên làm gì
đầu tiên?

- **A.** Dừng lại và chuyển sang một kiến trúc mô hình khác hoàn toàn (Alternative Architecture)
- **B.** Kiểm tra lại quy trình dữ liệu (data pipeline), tăng cường dữ liệu (augmentation) và bộ tối ưu
- **C.** Tăng tỷ lệ học lên mức 0.1 và tắt bỏ cơ chế suy giảm trọng số (Disable Weight Decay)
- **D.** Tăng gấp đôi số lượng tầng ẩn của mô hình (Increase Model Depth) để mở rộng dung lượng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi loss không giảm ngay từ đầu với một learning rate tiêu chuẩn (0. 001), khả năng cao.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Khi loss không giảm ngay từ đầu với một learning rate tiêu chuẩn (0.001), khả năng cao
là có lỗi trong quy trình xử lý dữ liệu (data pipeline), nhãn bị sai, hoặc bộ tối ưu chưa
được thiết lập đúng. Việc tăng LR lên 0.1 (quá lớn) hoặc thay đổi kiến trúc ngay lập tức
không phải là bước debug hợp lý đầu tiên.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 3). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 04 [VOAI25-004] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hạn chế lớn nhất khi tinh chỉnh (fine-tune) toàn bộ mô hình GPT là gì?

- **A.** Không dùng được tiếng Việt
- **B.** Cần tài nguyên tính toán rất lớn
- **C.** Không dùng được API
- **D.** Không sinh được ảnh

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Các mô hình GPT (đặc biệt là các phiên bản lớn như GPT-3, GPT-4) có hàng tỷ tham. Việc fine-tune toàn bộ (full fine-tuning) yêu cầu lưu trữtrạng thái của bộ tối ưu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Các mô hình GPT (đặc biệt là các phiên bản lớn như GPT-3, GPT-4) có hàng tỷ tham
số. Việc fine-tune toàn bộ (full fine-tuning) yêu cầu lưu trữtrạng thái của bộ tối ưu
(optimizer states) và gradient cho tất cả tham số, đòi hỏi dung lượng VRAM GPU và
khả năng tính toán khổng lồ.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 4). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 05 [VOAI25-005] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi muốn trích xuất đặc trưng (features) từ ResNet50, bạn nên làm gì?

- **A.** Sử dụng bộ tối ưu Adam
- **B.** Sử dụng đầu ra từ lớp gần cuối (ví dụ: avgpool, penultimate, …)
- **C.** Thêm nhiều lớp bỏ ngẫu nhiên (dropout)
- **D.** Thêm lớp kết nối đầy đủ siêu tốc (fully connected) mới

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đểtrích xuất đặc trưng (Feature Extraction), ta thường lấy vector đầu ra ở các lớp gần. cuối (như lớp Global Average Pooling) trước khi đi vào lớp phân loại (Fully Connected).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đểtrích xuất đặc trưng (Feature Extraction), ta thường lấy vector đầu ra ở các lớp gần
cuối (như lớp Global Average Pooling) trước khi đi vào lớp phân loại (Fully Connected)
cuối cùng. Vector này chứa các thông tin đặc trưng ngữnghĩa cao cấp của bức ảnh.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 5). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 06 [VOAI25-006] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Giả sử bạn đang xây dựng một mô hình phân loại cảm xúc văn bản (positive/negative) bằng cách sử
dụng biểu diễn Bag-of-Words (BoW) và PyTorch (phiên bản ≥ 1.6). Dưới đây là đoạn mã tiền xử lý đã được
thực hiện:

Phương án nào sau đây là phần mã đúng để huấn luyện mô hình phân loại nhị phân đơn giản với biểu diễn
BoW, một tầng tuyến tính và hàm loss phù hợp.

- **A.** model = nn. Linear(..., 1); loss_fn = nn. BCEWithLogitsLoss()
- **B.** model = nn. Sequential(..., nn. ReLU(), ...); loss_fn = nn. NLLLoss()
- **C.** model = nn. Linear(..., 2); loss_fn = nn. CrossEntropyLoss()
- **D.** model = nn. Linear(..., 1); loss_fn = nn. MSELoss()

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đối với phân loại nhịphân (Binary Classification) trong PyTorch:. • Đầu ra của mô hình thường là 1 logit (kích thước output layer là 1).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đối với phân loại nhịphân (Binary Classification) trong PyTorch:
• Đầu ra của mô hình thường là 1 logit (kích thước output layer là 1).
• Hàm mất mát phù hợp nhất là BCEWithLogitsLoss (kết hợp Sigmoid + BCELoss)
đểđảm bảo tính ổn định số học (numerical stability).

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.4** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 6). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 07 [VOAI25-007] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Điều nào sau đây là ĐÚNG khi so sánh SVM (support vector machine) với k-NN?

- **A.** Cả hai phương pháp chỉ được sử dụng cho các bài toán phân loại (không phải hồi quy)
- **B.** Huấn luyện SVM có thể tốn kém về mặt tính toán, đặc biệt đối với các bộ dữ liệu lớn, trong khi huấn luyện k-NN không liên quan đến quy trình huấn luyện rõ ràng
- **C.** SVM luôn tốt hơn k-NN trên mọi tập dữ liệu
- **D.** Dự đoán của cả hai phương pháp đều chậm vì cả hai đều cần xử lý tất cả các mẫu dữ liệu huấn luyện để dự đoán mẫu dữ liệu mới

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
k-NN là thuật toán " lười "(lazy learning), không có giai đoạn huấn luyện thực sự (chỉ lưu. dữ liệu), do đó chi phí huấn luyện bằng 0 (nhưng chi phí dự đoán cao).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
k-NN là thuật toán " lười "(lazy learning), không có giai đoạn huấn luyện thực sự (chỉ lưu
dữ liệu), do đó chi phí huấn luyện bằng 0 (nhưng chi phí dự đoán cao). SVM yêu cầu giải
bài toán tối ưu lồi (Quadratic Programming) đểtìm siêu phẳng, nên chi phí huấn luyện
tốn kém, đặc biệt với dữ liệu lớn O(N 2) hoặc O(N 3).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.2** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 7). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 08 [VOAI25-008] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Đối với SVM (support vector machine) phi tuyến, để dự đoán, đáp án nào đúng.

- **A.** Cần sử dụng cùng hàm chuyển đổi tương tự với giai đoạn huấn luyện
- **B.** Sử dụng một hàm chuyển đổi khác với giai đoạn huấn luyện
- **C.** SVM phi tuyến luôn tốt hơn SVM tuyến tính trong mọi tập dữ liệu
- **D.** Không cần hàm chuyển đổi

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
SVM phi tuyến sử dụng kỹ thuật " Kernel Trick " đểánh xạdữ liệu sang không gian nhiều. chiều hơn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
SVM phi tuyến sử dụng kỹ thuật " Kernel Trick " đểánh xạdữ liệu sang không gian nhiều
chiều hơn. Đểdự đoán chính xác một điểm dữ liệu mới, điểm đó cũng phải được ánh
xạ (hoặc tính kernel) bằng đúng hàm chuyển đổi/kernel đã dùng trong quá trình huấn
luyện.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.2** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 8). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 09 [VOAI25-009] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi sử dụng torchvision.models.resnet18(pretrained=True) trong PyTorch, mục đích chính là gì?

- **A.** Khởi tạo trọng số ngẫu nhiên để huấn luyện mô hình từ đầu (Train from Scratch) trên dữ liệu mới
- **B.** Mở rộng kích thước lô dữ liệu (Batch Size Expansion) để tối ưu hóa khả năng song song trên GPU
- **C.** Thử nghiệm cấu trúc liên kết mới của mạng mà không kế thừa bất kỳ tham số tiền huấn luyện nào
- **D.** Sử dụng trọng số huấn luyện trước (pre-trained weights) trên ImageNet để trích xuất đặc trưng

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tham sốpretrained=True (hoặc weights=’DEFAULT’ ở các bản mới) sẽtải các trọng. số đã được học trên tập dữ liệu ImageNet.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Tham sốpretrained=True (hoặc weights=’DEFAULT’ ở các bản mới) sẽtải các trọng
số đã được học trên tập dữ liệu ImageNet. Điều này cho phép áp dụng Transfer Learning
hoặc dùng mô hình làm bộ trích xuất đặc trưng (Feature Extractor) ngay lập tức mà
không cần train từ đầu.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 9). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 10 [VOAI25-010] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi các mô hình phát hiện vật thể hoạt động, chúng thường đề xuất nhiều hộp bao (bounding box) cho cùng một đối tượng trong ảnh. Nhiều hộp bao này có thể chồng lấn lên nhau, dẫn đến thông tin dư thừa vì mục tiêu của chúng ta là chỉ xác định một hộp bao duy nhất và chính xác nhất cho mỗi đối tượng. Thuật toán Non-Maximum Suppression (NMS) được thiết kế để giải quyết vấn đề này. Nó giúp lọc và loại bỏ các hộp bao dư thừa, chỉ giữ lại những hộp bao đại diện tốt nhất cho mỗi đối tượng.

Thuật toán NMS gồm các bước như sau:
- **Sắp xếp:** Sắp xếp tất cả các hộp bao trong tập $P$ theo thứ tự giảm dần của điểm tin cậy (confidence score).
- **Chọn hộp tốt nhất:** Chọn hộp bao $H$ có điểm tin cậy cao nhất từ tập $P$. Hộp bao này được xem là đại diện tốt nhất hiện tại.
- **Giữ lại và loại bỏ:** Chuyển hộp bao $H$ vào danh sách kết quả cuối cùng (gọi là $K$) và loại bỏ nó khỏi tập $P$.
- **So sánh và loại bỏ chồng lấn:**
  + Tính toán chỉ số Intersection over Union (IoU) giữa hộp $H$ (vừa chọn) và tất cả các hộp bao còn lại trong tập $P$.
  + Đối với mỗi hộp bao còn lại trong $P$, nếu giá trị IoU của nó với hộp $H$ lớn hơn một ngưỡng xác định trước (IoU_threshold), thì loại bỏ hộp bao đó khỏi $P$. Lý do là vì nó chồng lấn quá nhiều với hộp $H$ (vốn có điểm tin cậy cao hơn) và được coi là dư thừa cho cùng một đối tượng.
- **Lặp lại:** Quay lại bước chọn hộp có điểm tin cậy cao nhất tiếp theo từ $P$, thêm vào $K$, loại bỏ các hộp chồng lấn khỏi $P$ cho đến khi tập $P$ không còn hộp bao nào.
- **Kết quả:** Danh sách $K$ sẽ chứa các hộp bao cuối cùng được giữ lại, mỗi hộp đại diện cho một đối tượng riêng biệt đã được phát hiện.

Áp dụng thuật toán NMS với ngưỡng $\text{IoU\_threshold} = 0.40$ và giả sử tất cả các hộp cùng một lớp và thông tin các hộp đã sắp thứ tự theo độ tin cậy (confidence score) như sau:

| Hộp bao | Tọa độ $(x_1, y_1, x_2, y_2)$ | Độ tin cậy (Score) |
|:---:|:---:|:---:|
| $B_1$ | $(0, 0, 100, 100)$ | $0.95$ |
| $B_2$ | $(10, 10, 90, 90)$ | $0.90$ |
| $B_3$ | $(105, 105, 200, 200)$ | $0.85$ |

Những hộp nào sẽ được giữ lại?

- **A.** $B_1$ và $B_2$
- **B.** Chỉ $B_1$
- **C.** $B_1$ và $B_3$
- **D.** $B_2$ và $B_3$

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Hộp $B_1$ có điểm tin cậy cao nhất (0.95), được giữ lại đầu tiên làm chuẩn.
- Hộp $B_2$ (0.90) nằm lọt thỏm ngay bên trong ruột của $B_1$ (trùng lấn quá nhiều, IoU = 0.64 > 0.40), nên bị coi là dư thừa và bị xóa bỏ.
- Hộp $B_3$ (0.85) nằm ở một vị trí hoàn toàn tách biệt ngoài xa, không dính líu gì đến $B_1$ (IoU = 0), nên được giữ lại như một đối tượng riêng biệt.
Kết quả cuối cùng giữ lại hai hộp $B_1$ và $B_3$!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Thực hiện từng bước thuật toán NMS với ngưỡng IoU = 0.40:
- **Bước 1:** Chọn hộp có độ tin cậy cao nhất: $B_1$ (score = 0.95). Thêm $B_1$ vào danh sách giữ lại $K = \{B_1\}$.
- **Bước 2:** Tính $\text{IoU}(B_1, B_2)$:
  + Diện tích $B_1 = (100 - 0) \times (100 - 0) = 10000$.
  + Diện tích $B_2 = (90 - 10) \times (90 - 10) = 6400$.
  + Do $10 > 0$ và $90 < 100$, hộp $B_2$ nằm hoàn toàn trong $B_1$.
  + Diện tích giao (Intersection): $\text{Area}(B_1 \cap B_2) = 6400$.
  + Diện tích hội (Union): $\text{Area}(B_1 \cup B_2) = 10000 + 6400 - 6400 = 10000$.
  + $\text{IoU}(B_1, B_2) = \frac{6400}{10000} = 0.64$.
  + Vì $\text{IoU} = 0.64 > 0.40$ (vượt ngưỡng), loại bỏ $B_2$.
- **Bước 3:** Xét hộp $B_3$ (tọa độ $105 \dots 200$, score = 0.85):
  + Tọa độ $x_1 = 105 > 100$ nên không giao với $B_1$ $\implies \text{IoU}(B_1, B_3) = 0 \le 0.40$.
  + Giữ lại $B_3$, thêm vào danh sách $K$.
- **Kết quả:** Các hộp được giữ lại là $B_1$ và $B_3$. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Nhầm lẫn giữa phép Intersection ($6400$) và Union: lấy mẫu số là diện tích $B_2$ ($6400/6400=1$).
- Nhầm rằng NMS chỉ giữ duy nhất một hộp cho toàn bộ bức ảnh (dẫn đến chọn B). NMS giữ lại một hộp tốt nhất cho *mỗi đối tượng tách biệt*.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.8 Non-Maximum Suppression (NMS) & Bounding Box Regression** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 10).

---

### Câu 11 [VOAI25-011] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong Pandas, phương thức nào dùng để lấy 5 dòng đầu tiên của DataFrame?

- **A.** df.head()
- **B.** df.take(5)
- **C.** df.top()
- **D.** df.first(5)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cú pháp chuẩn trong thư viện Pandas đểxem n dòng đầu tiên là df. nếu không truyền tham số, nó sẽtrảvề5 dòng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Cú pháp chuẩn trong thư viện Pandas đểxem n dòng đầu tiên là df.head(n). Mặc định
nếu không truyền tham số, nó sẽtrảvề5 dòng.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 11). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 12 [VOAI25-012] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán học máy nào sau đây là phổ biến và hiệu quả, dựa trên ý tưởng bagging?

- **A.** XGBoost
- **B.** Hồi quy tuyến tính (Linear Regression)
- **C.** Cây quyết định (Decision Tree)
- **D.** Rừng ngẫu nhiên (Random Forest)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Bagging (Bootstrap Aggregating) là kỹ thuật nền tảng của Random Forest. Forest tạo ra nhiều cây quyết định (Decision Trees) độc lập trên các tập con dữ liệu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Bagging (Bootstrap Aggregating) là kỹ thuật nền tảng của Random Forest. Random
Forest tạo ra nhiều cây quyết định (Decision Trees) độc lập trên các tập con dữ liệu
khác nhau và lấy kết quảtrung bình (hoặc bầu chọn đa số). XGBoost dựa trên Boosting,
không phải Bagging.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 12). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 13 [VOAI25-013] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật nào sau đây được sử dụng để giảm ảnh hưởng của nhiễu và ngoại lệtrong tập dữ liệu (khi huấn luyện)?

- **A.** Phân tích thành phần chính (Principal Component Analysis - PCA)
- **B.** Chính quy hóa (Regularization)
- **C.** Xác thực chéo (Cross-validation)
- **D.** Trích xuất đặc trưng (Feature extraction)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong ngữ cảnh huấn luyện mô hình đểtránh bị ảnh hưởng bởi nhiễu (noise) dẫn đến. quá khớp (overfitting), Chính quy hóa (Regularization) như L1, L2 là phương pháp.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Trong ngữ cảnh huấn luyện mô hình đểtránh bị ảnh hưởng bởi nhiễu (noise) dẫn đến
quá khớp (overfitting), Chính quy hóa (Regularization) như L1, L2 là phương pháp
chính. Nó thêm một thành phần phạt vào hàm mất mát đểngăn trọng số trởnên quá lớn
hoặc quá phức tạp đểkhớp với nhiễu. (Lưu ý: PCA giảm chiều cũng có thểgiảm nhiễu
nhưng Regularization là câu trảlời trực tiếp hơn cho việc kiểm soát mô hình).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 13). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 14 [VOAI25-014] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong xử lý ngôn ngữ tự nhiên, đâu là thứ tự đúng của các bước xử lý cơ bản sau đây?
- 1. Tách từ (Tokenization)
- 2. Chuẩn hóa văn bản (Normalization)
- 3. Rút gọn từ (Stemming)
- 4. Gán nhãn từ loại (Part-of-speech tagging)

- **A.** 2 → 1 → 4 → 3
- **B.** 2 → 1 → 3 → 4
- **C.** 1 → 3 → 2 → 4
- **D.** 1 → 2 → 4 → 3

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Quy trình tiền xử lý văn bản chuẩn mực diễn ra tuần tự:
1. **Tách từ (Tokenization):** Cắt văn bản thô thành các từ/mảnh token riêng lẻ.
2. **Chuẩn hóa văn bản (Normalization):** Đưa về chữ thường, xử lý viết tắt/dấu câu thống nhất.
4. **Gán nhãn từ loại (POS Tagging):** Cần thực hiện khi câu còn giữ nguyên cấu trúc ngữ pháp để xác định danh từ/động từ/tính từ.
3. **Rút gọn từ (Stemming/Lemmatization):** Đưa từ về dạng gốc, thường thực hiện sau khi đã có thông tin POS hoặc làm bước cuối để gom cụm giảm chiều từ điển.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích pipeline xử lý:
- Bước 1 (Tokenization) cắt chuỗi $S \to [w_1, w_2, \dots, w_n]$.
- Bước 2 (Normalization) chuẩn hóa chữ hoa/thường, Unicode.
- Bước 4 (POS Tagging) mô hình hóa xác suất $P(t_i \mid w_i, t_{i-1})$ cần trật tự câu hoàn chỉnh.
- Bước 3 (Stemming) chặt đuôi từ (Porter Stemmer) làm mất dạng ngữ pháp nên phải làm sau POS tagging.
Thứ tự chuẩn xác là 1 → 2 → 4 → 3. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nếu làm Stemming (3) trước POS Tagging (4), các hậu tố chỉ thì/thể bị chặt bỏ khiến bộ gắn nhãn từ loại dự đoán sai hoàn toàn.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 14).

---

### Câu 15 [VOAI25-015] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Tại sao learning rate thích ứng (adaptive learning rate) lại hữu ích trong thực tế?

- **A.** Làm mô hình huấn luyện ngẫu nhiên hơn
- **B.** Tự động điều chỉnh tốc độ học theo tham số cụ thể
- **C.** Tránh tràn số
- **D.** Hạn chế overfitting

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Các thuật toán như Adam, RMSprop, Adagrad có khả năng điều chỉnh learning rate. riêng cho từng tham số (weight) dựa trên lịch sửgradient của chúng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Các thuật toán như Adam, RMSprop, Adagrad có khả năng điều chỉnh learning rate
riêng cho từng tham số (weight) dựa trên lịch sửgradient của chúng. Điều này giúp các
tham sốít được cập nhật sẽcó bước nhảy lớn hơn và ngược lại, giúp hội tụnhanh và ổn
định hơn.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 15). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 16 [VOAI25-016] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** An là một học sinh giỏi toán. Khi biết rằng các mô hình ngôn ngữ lớn (LLM) có thể giải được những
bài toán phức tạp, An đã thử nghiệm nhưng kết quả không như mong đợi. Tuy nhiên, sau khi tìm hiểu và áp
dụng kỹ thuật Chain-of-Thought, An nhận thấy mô hình bắt đầu giải đúng nhiều bài toán hơn. Vậy, kỹ thuật
Chain-of-Thought là gì?

- **A.** Yêu cầu mô hình trả lời càng ngắn gọn càng tốt để tiết kiệm tài nguyên
- **B.** Huấn luyện mô hình dự đoán từ tiếp theo bằng dữ liệu song ngữ
- **C.** Yêu cầu mô hình sinh câu hỏi thay vì câu trả lời
- **D.** Thúc đẩy mô hình giải bài toán bằng cách liệt kê từng bước suy luận trung gian

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Chain-of-Thought (CoT) prompting là kỹ thuật yêu cầu mô hình ngôn ngữlớn (LLM). sinh ra một chuỗi các bước suy luận logic trước khi đưa ra câu trảlời cuối cùng, giúp cải.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Chain-of-Thought (CoT) prompting là kỹ thuật yêu cầu mô hình ngôn ngữlớn (LLM)
sinh ra một chuỗi các bước suy luận logic trước khi đưa ra câu trảlời cuối cùng, giúp cải
thiện đáng kểkhả năng giải quyết các bài toán phức tạp (toán học, logic).

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 16). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 17 [VOAI25-017] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trọng số các thuộc tính trong k-NN được được thực hiện bằng:

- **A.** Cập nhật giá trị thuộc tính của mẫu dữ liệu theo các trọng số khác nhau
- **B.** Thuộc tính quan trọng hơn được thêm vào bởi trọng số lớn hơn
- **C.** Điều chỉnh phép tính khoảng cách bằng cách nhân từng thuộc tính với trọng số
- **D.** Một ma trận trọng số được sử dụng để tính toán các hàng xóm

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Weighted k-NN hoặc việc gán trọng số cho thuộc tính (Feature weighting) thực chất là. thay đổi không gian metric.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Weighted k-NN hoặc việc gán trọng số cho thuộc tính (Feature weighting) thực chất là
thay đổi không gian metric. Khi tính khoảng cách (ví dụ Euclidean), ta nhân sự khác
biệt của mỗi thuộc tính với một trọng số wi. Công thức tổng quát cho khoảng cách giữa
hai điểm x và y trở thành:
d(x, y) =
v
u
u
t
n
X
i=1
wi(xi −yi)2
Thuộc tính quan trọng hơn sẽcó wi lớn hơn, đóng góp nhiều hơn vào giá trịkhoảng cách.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 17). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 18 [VOAI25-018] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Chúng ta muốn phân 7 điểm dữ liệu vào trong 3 cụm sử dụng thuật toán K-means (với khoảng cách
Euclid). Giả sử rằng sau vòng lặp đầu tiên, các cụm C1, C2 và C3 chứa các điểm dữ liệu sau (trong không
gian 2 chiều): C1 chứa 2 điểm dữ liệu: (0,6), (6,0); C2 chứa 3 điểm dữ liệu: (2,2), (4,4), (6,6); C3 chứa 2 điểm
dữ liệu: (5,5), (7,7). Tâm của 3 cụm sẽ là?

- **A.** C1: (0,0), C2: (48,48), C3: (35,35)
- **B.** C1: (3,3), C2: (4,4), C3: (6,6)
- **C.** C1: (6,6), C2: (12,12), C3: (12,12)
- **D.** C1: (3,3), C2: (6,6), C3: (12,12)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tâm cụm mới là trung bình cộng (mean) các điểm trong cụm:. • C1: (0+6.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Tâm cụm mới là trung bình cộng (mean) các điểm trong cụm:
• C1: (0+6
2 , 6+0
2 ) = (3, 3).
• C2: (2+4+6
3
, 2+4+6
3
) = (4, 4).
• C3: (5+7
2 , 5+7
2 ) = (6, 6).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.8** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 18). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 19 [VOAI25-019] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** GloVe là một phương pháp nhúng từ (word embedding). Phát biểu nào sau đây mô tả đúng cách mà
nhúng từ GloVe được tạo ra?

- **A.** Được tạo ra trong quá trình dịch máy
- **B.** Sử dụng cơ chế chú ý (attention) để tạo vector
- **C.** Được huấn luyện từ ma trận đồng xuất hiện (co-occurrence matrix) toàn cục
- **D.** Một dạng vector gồm các số 0 và một số 1 (one-hot vector)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
GloVe (Global Vectors for Word Representation) là phương pháp tạo word embedding. bằng cách phân tích ma trận đồng xuất hiện (global co-occurrence matrix) của các từ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
GloVe (Global Vectors for Word Representation) là phương pháp tạo word embedding
bằng cách phân tích ma trận đồng xuất hiện (global co-occurrence matrix) của các từ
trong toàn bộ tập dữ liệu, thay vì chỉ dùng cửa sổtrượt cục bộ như Word2Vec.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 19). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 20 [VOAI25-020] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình BERT nhận đầu vào là gì?

- **A.** Vector ID, mặt nạ chú ý (attention mask), ID loại token
- **B.** Chuỗi văn bản thô (raw text) và ma trận nhúng vị trí
- **C.** Cặp câu văn bản cùng với nhãn phân loại ngữ nghĩa
- **D.** Các từ vựng rời rạc và bảng tra cứu tần suất n-gram

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đầu vào tiêu chuẩn của BERT (thư viện Hugging Face) bao gồm 3 thành phần chính:. • Input IDs: Chuỗi số đại diện cho các token.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đầu vào tiêu chuẩn của BERT (thư viện Hugging Face) bao gồm 3 thành phần chính:
• Input IDs: Chuỗi số đại diện cho các token.
• Attention Mask: Đểphân biệt token thật và token đệm (padding).
• Token Type IDs: Đểphân biệt câu A và câu B (trong bài toán cặp câu).

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 20). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 21 [VOAI25-021] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Nếu muốn sử dụng GPT để sinh câu trả lời dựa trên một đoạn văn, mô hình nào phù hợp nhất?

- **A.** Mô hình BERT tiền huấn luyện với cơ chế mặt nạ từ vựng hai chiều (Masked Language Modeling)
- **B.** Mô hình GPT-2 phiên bản cơ bản với cơ chế sinh văn bản từ trái sang phải tuần tự tự do
- **C.** Mô hình GPT-Neo mã nguồn mở với cơ chế Attention cục bộ thưa thớt theo cửa sổ trượt
- **D.** Mô hình GPT-3.5 hoặc GPT-4 kết hợp câu lệnh gợi ý phù hợp (Prompt Engineering Context)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
5 và GPT-4 là các mô hình SOTA (State-of-the-art) về khả năng Instruction. Following (tuân theo chỉ dẫn) và Reading Comprehension.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
GPT-3.5 và GPT-4 là các mô hình SOTA (State-of-the-art) về khả năng Instruction
Following (tuân theo chỉ dẫn) và Reading Comprehension. Với prompt phù hợp, chúng
vượt trội hơn hẳn các đời cũ như GPT-2 hay GPT-Neo.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 21). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 22 [VOAI25-022] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Nếu thêm bỏ ngẫu nhiên (dropout) vào mô hình nhưng độ chính xác kiểm tra (validation accuracy)
giảm mạnh, bạn nên thử gì đầu tiên?

- **A.** Dùng bộ tối ưu khác
- **B.** Giảm xác suất bỏ ngẫu nhiên xuống nhỏ hơn
- **C.** Tắt bỏ ngẫu nhiên
- **D.** Tăng xác suất bỏ ngẫu nhiên lên 0.8

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Dropout giúp chống overfitting, nhưng nếu validation accuracy giảm mạnh, có thểdo tỷ. lệdropout quá cao khiến mô hình mất quá nhiều thông tin (underfitting).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Dropout giúp chống overfitting, nhưng nếu validation accuracy giảm mạnh, có thểdo tỷ
lệdropout quá cao khiến mô hình mất quá nhiều thông tin (underfitting). Giải pháp hợp
lý là giảm tỷ lệdropout (ví dụtừ0.5 xuống 0.2) trước khi tắt hẳn.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.9** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 22). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 23 [VOAI25-023] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán phân loại văn bản, nếu mô hình học tốt các từ khóa rõ ràng nhưng không hiểu ngữ
cảnh, phương pháp nào giúp cải thiện khả năng hiểu ngữ cảnh?

- **A.** Giảm số chiều nhúng (embedding)
- **B.** Dùng mô hình dựa trên chú ý (attention-based) như BERT
- **C.** Chuyển sang dùng TF-IDF
- **D.** Bỏ nhúng (embedding), dùng vector gồm các số 0 và một số 1 (one-hot vector)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Các mô hình truyền thống (BoW, TF-IDF) hoặc mạng nơ-ron đơn giản thường chỉ dựa. vào sự xuất hiện của từ (keyword).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Các mô hình truyền thống (BoW, TF-IDF) hoặc mạng nơ-ron đơn giản thường chỉ dựa
vào sự xuất hiện của từ (keyword). Đểhiểu " ngữ cảnh "(context - từ này phụ thuộc vào
từ kia, thứtựtừ), cơ chế Self-Attention trong Transformer (như BERT) là giải pháp tốt
nhất.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 23). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 24 [VOAI25-024] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Giả sử rằng bạn sử dụng phương pháp 1-láng giềng gần nhất (1-NN) để dự đoán nhãn lớp cho dữ liệu $x$, dựa trên tập huấn luyện $D$ và thước đo khoảng cách $d$. 1-NN sẽ đưa ra dự đoán nào cho $x$?

- **A.** $y^*$ trong đó $(a^*, y^*) = \arg\min_{(a, y) \in D} d(x, y)$
- **B.** $y^*$ trong đó $(a^*, y^*) = \arg\min_{(a, y) \in D} d(x, a)$
- **C.** $a^*$ trong đó $(a^*, y^*) = \arg\min_{(a, y) \in D} d(x, a)$
- **D.** $y^*$ trong đó $(a^*, y^*) = \min_{(a, y) \in D} d(x, a)$

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
1-NN tìm điểm dữ liệu $a^*$ trong tập huấn luyện $D$ gần vector đầu vào $x$ nhất (khoảng cách $d(x, a)$ nhỏ nhất), sau đó gán nhãn $y^*$ của điểm dữ liệu đó cho $x$.
- Điểm cần đo khoảng cách với $x$ là đặc trưng $a$, không phải nhãn $y$!
- Giá trị cần trả về là nhãn $y^*$, không phải vector đặc trưng $a^*$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định nghĩa chuẩn mực của 1-NN:
Tập huấn luyện $D = \{(a_i, y_i)\}_{i=1}^N$ gồm các cặp đặc trưng - nhãn $(a, y)$.
Điểm láng giềng gần nhất:
$$(a^*, y^*) = \arg\min_{(a, y) \in D} d(x, a)$$
Dự đoán của mô hình là nhãn tương ứng:
$$\hat{y} = y^*$$
Theo thứ tự phương án của đề thi gốc PDF (Mã đề 006), biểu thức này nằm ở phương án **B**. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Phương án A sai vì viết $d(x, y)$ (đo khoảng cách với nhãn, hoàn toàn vô nghĩa toán học).
- Phương án C sai vì trả về $a^*$ (vector đặc trưng) thay vì nhãn $y^*$.
- Phương án D sai vì dùng toán tử $\min$ (trả về giá trị khoảng cách bé nhất) thay vì $\arg\min$ (tìm phần tử đạt cực tiểu).
*Ghi chú đính chính nguồn:* Bản giải thứ ba đã tự ý đảo vị trí phương án A và B so với bản in đề gốc mã 006. Đáp án đúng theo đúng trật tự đề thi gốc là B.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 24).

---

### Câu 25 [VOAI25-025] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Xét tập huấn luyện gồm 8 mẫu dưới đây. Mỗi mẫu được mô tả bằng 3 đặc trưng số $(F_1, F_2, F_3)$ và thuộc về một trong ba lớp:

| ID | F1 | F2 | F3 | Lớp |
|:---:|:---:|:---:|:---:|:---:|
| S1 | 2 | 2 | 0 | Đỏ |
| S2 | 1 | 3 | 1 | Đỏ |
| S3 | 0 | 2 | 2 | Đỏ |
| S4 | 8 | 7 | 7 | Xanh dương |
| S5 | 9 | 6 | 6 | Xanh dương |
| S6 | 7 | 7 | 8 | Xanh dương |
| S7 | 5 | 2 | 5 | Xanh lá |
| S8 | 6 | 1 | 4 | Xanh lá |

Sử dụng thuật toán K-láng giềng gần nhất (k-NN) với khoảng cách Euclid và $k = 3$, lớp nào sẽ được dự đoán cho điểm truy vấn $Q = (6, 2, 6)$?

- **A.** Xanh dương
- **B.** Đỏ
- **C.** Xanh lá
- **D.** Hòa thuật toán không thể quyết định

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ta đo khoảng cách từ điểm cần dự đoán $Q = (6, 2, 6)$ đến cả 8 người bạn trong danh sách. Ba người bạn đứng gần $Q$ nhất sẽ bỏ phiếu để quyết định màu áo của $Q$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Khoảng cách bình phương Euclid $d^2(Q, S) = (6 - F_1)^2 + (2 - F_2)^2 + (6 - F_3)^2$:
- $S_1(2,2,0): (4)^2 + (0)^2 + (6)^2 = 16 + 0 + 36 = 52$
- $S_2(1,3,1): (5)^2 + (-1)^2 + (5)^2 = 25 + 1 + 25 = 51$
- $S_3(0,2,2): (6)^2 + (0)^2 + (4)^2 = 36 + 0 + 16 = 52$
- $S_4(8,7,7): (-2)^2 + (-5)^2 + (-1)^2 = 4 + 25 + 1 = 30$
- $S_5(9,6,6): (-3)^2 + (-4)^2 + (0)^2 = 9 + 16 + 0 = 25$
- $S_6(7,7,8): (-1)^2 + (-5)^2 + (-2)^2 = 1 + 25 + 4 = 30$
- $S_7(5,2,5): (1)^2 + (0)^2 + (1)^2 = 1 + 0 + 1 = \mathbf{2}$
- $S_8(6,1,4): (0)^2 + (1)^2 + (2)^2 = 0 + 1 + 4 = \mathbf{5}$

Ba láng giềng gần nhất với khoảng cách nhỏ nhất:
1. $S_7$ ($d^2 = 2$) — Lớp **Xanh lá**
2. $S_8$ ($d^2 = 5$) — Lớp **Xanh lá**
3. $S_5$ ($d^2 = 25$) — Lớp **Xanh dương**

Đa số phiếu (2/3) thuộc về lớp **Xanh lá**. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Tính nhầm khoảng cách trục $F_3$ hoặc quên bình phương các tọa độ âm.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1 k-NN (k-Nearest Neighbors — Lazy Learner)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 25).

---

### Câu 26 [VOAI25-026] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hình dưới đây biểu thị bản đồ đặc trưng (feature map) thu được sau khi áp dụng một bộ lọc Conv2D lên ảnh đầu vào kích thước $128 \times 128$.

Hãy cho biết bộ lọc này đang phát hiện đặc trưng gì nhất?

![Hình minh họa VOAI25-026](assets/voai2025_q26.png)

- **A.** Các mẫu hoa văn bề mặt lặp lại tuần hoàn (Periodic Texture Patterns)
- **B.** Các đốm màu sắc không gian có cường độ đồng nhất (Uniform Color Blobs)
- **C.** Các cạnh theo hướng kết hợp ngang và dọc (cross directional edges)
- **D.** Các đường biên cạnh đơn lẻ chỉ theo hướng ngang (Horizontal Edges Only)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Feature map hiển thị đồng thời cả các đường kẻ sáng song song phương ngang và các đường kẻ sáng phương đứng cắt chéo nhau. Đây là đặc trưng cạnh đa hướng kết hợp (cross directional edges / góc giao).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích bộ lọc tích chập Conv2D:
- Bộ lọc Sobel ngang $G_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]$ chỉ làm nổi bật cạnh ngang.
- Bộ lọc Sobel dọc $G_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]$ chỉ làm nổi bật cạnh dọc.
- Khi bộ lọc kết hợp cả hai thành phần gradient hoặc toán tử vi phân bậc hai Laplacian $\nabla^2 I = \frac{\partial^2 I}{\partial x^2} + \frac{\partial^2 I}{\partial y^2}$, phản ứng cực đại xuất hiện ở cả hai trục trực giao (cạnh ngang và cạnh dọc).
Do đó bộ lọc đang phát hiện các cạnh theo hướng kết hợp ngang và dọc (cross directional edges). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Chỉ nhìn thấy các đường ngang mà bỏ qua các vệt đứng rõ rệt (dẫn đến chọn nhầm D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 26).

---

### Câu 27 [VOAI25-027] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Cho đoạn mã dưới đây, kích thước của output_tensor là bao nhiêu? Input(1, 32, 32, 3), Conv2D(32 filters, kernel_size=(5, 5), strides=(2, 2), padding=’same’).

- **A.** (1, 16, 16, 32)
- **B.** (1, 16, 16, 3)
- **C.** (1, 14, 14, 32)
- **D.** (1, 32, 32, 32)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Công thức tính kích thước với padding=’same’: Wout = ⌈Win/stride⌉. • Hout = ⌈32/2⌉= 16.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Công thức tính kích thước với padding=’same’: Wout = ⌈Win/stride⌉.
• Hout = ⌈32/2⌉= 16.
• Wout = ⌈32/2⌉= 16.
• Số kênh (depth) = số filters = 32.
• Batch size giữ nguyên = 1.
Kết quả: (1, 16, 16, 32).

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 27). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 28 [VOAI25-028] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mục đích chính của lấy mẫu phủ định (Negative Sampling) trong huấn luyện mô hình vectơ từ là gì?

- **A.** Tăng số lượng tham số của mô hình.
- **B.** Giúp mô hình sinh ra văn bản dài hơn và tự nhiên hơn.
- **C.** Giúp cải thiện độ chính xác mô hình.
- **D.** Giảm chi phí tính toán khi huấn luyện trên tập từ vựng lớn.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Thay vì cập nhật trọng số cho tất cả hàng triệu từ trong từ điển (như Softmax tiêu. chuẩn), Negative Sampling chỉ cập nhật cho từ dương (positive word) và một sốít từâm.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Thay vì cập nhật trọng số cho tất cả hàng triệu từ trong từ điển (như Softmax tiêu
chuẩn), Negative Sampling chỉ cập nhật cho từ dương (positive word) và một sốít từâm
(negative words) được chọn ngẫu nhiên, giúp giảm khối lượng tính toán đáng kể.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 28). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 29 [VOAI25-029] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi sử dụng bộ tối ưu Adam, nếu mất mát huấn luyện (training loss) ngừng giảm sớm (plateau), bạn
nên thử gì tiếp theo?

- **A.** Đặt lại toàn bộ các tham số trọng số của mô hình về giá trị ngẫu nhiên ban đầu để train lại
- **B.** Tăng kích thước lô dữ liệu (batch size) lên gấp đôi để giảm phương sai của vector gradient
- **C.** Loại bỏ hoàn toàn các tầng chuẩn hóa lô (BatchNorm) khỏi toàn bộ đồ thị tính toán của mạng
- **D.** Giảm tỷ lệ học (learning rate) hoặc thử lại với thuật toán SGD kết hợp động lượng Momentum

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi loss đi ngang (plateau), thường do learning rate hiện tại quá lớn để mô hình đi xuống. đáy của cực tiểu cục bộ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Khi loss đi ngang (plateau), thường do learning rate hiện tại quá lớn để mô hình đi xuống
đáy của cực tiểu cục bộ. Việc giảm LR (Learning Rate Decay) là kỹ thuật tiêu chuẩn.
Đôi khi chuyển sang SGD cũng giúp thoát khỏi điểm cực tiểu kém.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 29). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 30 [VOAI25-030] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Học tự giám sát (self-supervised learning) thường sử dụng phương pháp nào?

- **A.** Đầu phân loại đa lớp (classification head) và hàm mất mát Cross-Entropy tiêu chuẩn có giám sát
- **B.** Thuật toán phân cụm không giám sát (K-Means Clustering) trên không gian dữ liệu điểm ảnh gốc
- **C.** Tăng cường dữ liệu (augmentation) và mất mát đối lập (contrastive loss)
- **D.** Gán nhãn thủ công (Manual Labeling) toàn bộ tập dữ liệu với sự hỗ trợ của các chuyên gia miền

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Các phương pháp Self-supervised Learning hiện đại (như SimCLR, MoCo) hoạt động dựa. trên Contrastive Learning: Tạo ra các phiên bản augmented (xoay, cắt, đổi màu) của.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Các phương pháp Self-supervised Learning hiện đại (như SimCLR, MoCo) hoạt động dựa
trên Contrastive Learning: Tạo ra các phiên bản augmented (xoay, cắt, đổi màu) của
cùng một ảnh và huấn luyện mô hình đểkéo vector đặc trưng của chúng lại gần nhau,
đồng thời đẩy xa các ảnh khác.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 30). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 31 [VOAI25-031] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Chuẩn hóa rất quan trọng đối với k-NN vì:

- **A.** Giúp tránh được vấn đề một thuộc tính có thể đóng vai trò quyết định, lấn át các thuộc tính khác.
- **B.** Nó biến đổi các giá trị thuộc tính thành phạm vi [0, 1] để dễ dàng tính toán.
- **C.** Nó cho phép so sánh và phân tích có ý nghĩa giữa các biến.
- **D.** Nó cần thiết để tính toán khoảng cách giữa các mẫu dữ liệu.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Thuật toán k-NN dựa trên khoảng cách (thường là Euclid). Nếu một đặc trưng có dải.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Thuật toán k-NN dựa trên khoảng cách (thường là Euclid). Nếu một đặc trưng có dải
giá trịrất lớn (ví dụ: lương hàng triệu) so với đặc trưng khác (ví dụ: tuổi từ1-100),
đặc trưng lớn sẽchi phối hoàn toàn khoảng cách, làm sai lệch kết quả. Chuẩn hóa
(Normalization/Standardization) đưa các đặc trưng về cùng một thang đo đểđóng góp
ngang nhau.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 31). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 32 [VOAI25-032] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho bản đồ đặc trưng sau đây dưới dạng ma trận $4 \times 4$:
```python
[[ 10,  20,  30,  40],
 [ 50,  60,  70,  80],
 [ 90, 100, 110, 120],
 [130, 140, 150, 160]]
```
Giá trị ở vị trí $(0, 0)$ của bản đồ đặc trưng đầu ra sau khi áp dụng lớp gộp trung bình (Average Pooling) với kích thước cửa sổ $3 \times 3$ và bước nhảy (stride) bằng 2 là:

- **A.** 55
- **B.** 70
- **C.** 60
- **D.** 50

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cửa sổ $3 \times 3$ đặt tại góc trên bên trái $(0, 0)$ sẽ bao trọn 9 số đầu tiên:
Hàng 1: 10, 20, 30
Hàng 2: 50, 60, 70
Hàng 3: 90, 100, 110
Lớp Average Pooling chỉ đơn giản là tính trung bình cộng của 9 số này!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ma trận cửa sổ tại vị trí $(0, 0)$ (từ hàng 0 đến 2, cột 0 đến 2):
$$\text{Window} = \begin{bmatrix} 10 & 20 & 30 \\ 50 & 60 & 70 \\ 90 & 100 & 110 \end{bmatrix}$$
Tổng giá trị của 9 phần tử:
$$\text{Sum} = (10 + 20 + 30) + (50 + 60 + 70) + (90 + 100 + 110) = 60 + 180 + 300 = 540$$
Giá trị gộp trung bình:
$$\text{Out}[0, 0] = \frac{540}{9} = \mathbf{60}$$
Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Nhầm Max Pooling: Phần tử lớn nhất là 110.
- Nhầm kích thước cửa sổ $2 \times 2$: $(10+20+50+60)/4 = 35$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 32).

---

### Câu 33 [VOAI25-033] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Chương trình sau thực hiện:
- Tải ResNet-50 pre-trained trên ImageNet.
- Đóng băng toàn bộ các layer convolution.
- Lấy output của lớp avgpool (shape (2048, 1, 1)) và flatten thành vector 2048:

```python
import torch, torchvision.models as models

model = models.resnet50(weights=' DEFAULT ')

for p in model.parameters():
    p.requires_grad_(False)

model.fc = torch.nn. Identity()

x = torch.randn(1, 3, 224, 224)
...  # <-- điền vào đây
print(features.shape)
```
Bạn thiếu dòng nào dưới đây để trả về vector đặc trưng (feature vector)?

- **A.** features = model(x)
- **B.** features = model.layer4(x)
- **C.** features = model.avgpool(x)
- **D.** features = x

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đoạn code đã thay thế tầng phân loại cuối cùng `model.fc` bằng tầng rỗng `torch.nn. Identity()`. Khi gọi toàn bộ mô hình qua `model(x)`, luồng dữ liệu chạy qua tất cả các tầng tích chập, qua tầng gom trung bình `avgpool`, và qua tầng Identity mà không bị chiếu thành 1000 lớp, trả về nguyên vẹn vector đặc trưng 2048 chiều!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Kiến trúc luồng forward của ResNet-50 trong TorchVision:
1. $x \to \text{conv1} \to \text{layer1} \to \text{layer2} \to \text{layer3} \to \text{layer4} \to (2048, 7, 7)$
2. $(2048, 7, 7) \to \text{avgpool} \to (2048, 1, 1) \to \text{flatten} \to 2048$
3. $2048 \to \text{fc}$.
Vì đã gán `model.fc = torch.nn. Identity()`, hàm `model(x)` sẽ tự động thực hiện trọn vẹn chuỗi trên và cho ra kết quả `features` có shape `(1, 2048)`.
Dòng code đúng và ngắn gọn nhất là `features = model(x)`. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- `model.avgpool(x)` sai vì `avgpool` đòi hỏi đầu vào là tensor đặc trưng của `layer4`, không thể nhận trực tiếp ảnh thô $x$.
- `model.layer4(x)` sai vì cũng không thể nhận trực tiếp ảnh thô mà thiếu các tầng nông phía trước.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3 Các Kiến trúc CNN Kinh Điển & §3.9 Transfer Learning** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 33).

---

### Câu 34 [VOAI25-034] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Bạn muốn sử dụng một mô hình Mạng Nơ-ron Tích chập (CNN) cho nhiệm vụ phân tích ảnh viễn
thám (ảnh chụp từ vệ tinh, máy bay). Bạn có hai lựa chọn:
- Huấn luyện từ đầu: Xây dựng và huấn luyện một mô hình CNN hoàn toàn mới chỉ sử dụng bộ dữ liệu ảnh
viễn thám (giả sử có kích thước trung bình).
- Tinh chỉnh (Fine-tuning): Lấy một mô hình CNN đã được huấn luyện trước trên một tập dữ liệu lớn gồm ảnh
tự nhiên (ví dụ: ImageNet - ảnh chó, mèo, ô tô, v.v.) và điều chỉnh (tinh chỉnh) nó cho phù hợp với bộ dữ liệu
ảnh viễn thám của bạn.
So với việc huấn luyện mô hình từ đầu, phương pháp tinh chỉnh mang lại nhiều lợi ích. Tuy nhiên, điều nào
dưới đây KHÔNG phải là một ưu điểm điển hình của việc tinh chỉnh trong tình huống này?

- **A.** Giảm nguy cơ quá khớp (overfitting) vì số lượng tham số cần cập nhật ít hơn đáng kể so với ban đầu
- **B.** Khắc phục được hoàn toàn được vấn đề về sự khác biệt giữa đặc điểm ảnh tự nhiên và ảnh viễn thám.
- **C.** Mô hình hội tụ nhanh hơn nhiều do kế thừa các trọng số biểu diễn đặc trưng cơ bản từ dữ liệu gốc
- **D.** Tận dụng hiệu quả các đặc trưng cấp thấp tổng quát đã được học sẵn trên kho dữ liệu quy mô lớn

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mặc dù fine-tuning giúp mô hình thích nghi tốt hơn, nhưng việc khẳng định nó " khắc. phục hoàn toàn " sự khác biệt miền dữ liệu (Domain Shift) giữa ảnh tự nhiên (ImageNet).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Mặc dù fine-tuning giúp mô hình thích nghi tốt hơn, nhưng việc khẳng định nó " khắc
phục hoàn toàn " sự khác biệt miền dữ liệu (Domain Shift) giữa ảnh tự nhiên (ImageNet)
và ảnh viễn thám là không chính xác. Sự khác biệt về góc chụp, quang phổ, tỷ lệvật thể
vẫn là thách thức lớn. Các ý A, C, D đều là ưu điểm thực tếcủa Transfer Learning.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 34). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 35 [VOAI25-035] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Một bộ lọc hình vuông, mỗi cạnh của nó dài 𝑘 ô vuông. Bộ lọc này được dùng để quét qua một bức
ảnh ban đầu có chiều ngang 𝑚 ô vuông và chiều dọc 𝑛 ô vuông (𝑚,𝑛 > 𝑘). Mỗi lần quét, bộ lọc sẽ dịch
chuyển đi 2 ô vuông theo cả chiều ngang lẫn chiều dọc. Quá trình quét này không thêm bất kỳ lớp đệm nào
vào xung quanh ảnh gốc. Hỏi sau khi quét xong, bức ảnh kết quả (bản đồ đặc trưng đầu ra) sẽ có kích thước
bao nhiêu ô vuông chiều ngang và bao nhiêu ô vuông chiều dọc?
, - ,./ -./ ,./ -./ ,./0! -./0!

- **A.** ( , )
- **B.** (⌊ ⌋+1,⌊ ⌋+1)
- **C.** ( +𝑘, +𝑘)
- **D.** ( , ) " " " " " " " "

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Công thức tổng quát tính kích thước đầu ra của phép tích chập (hoặc pooling):. W −K + 2P.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Công thức tổng quát tính kích thước đầu ra của phép tích chập (hoặc pooling):
Output =
W −K + 2P
S

+ 1
Trong đó:
• W: Kích thước đầu vào (m hoặc n).
• K: Kích thước bộ lọc (k).
• P: Lớp đệm (padding = 0).
• S: Bước nhảy (stride = 2).
Thay các giá trịvào, ta có kích thước đầu ra là: (⌊m−k
2 ⌋+ 1, ⌊n−k
2 ⌋+ 1).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 35). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 36 [VOAI25-036] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi dùng ViT để phân loại ảnh, lớp cuối cùng thường là gì?

- **A.** Khối chú ý đa đầu (multi-head attention block) và tầng chuẩn hóa lớp
- **B.** Tầng loại bỏ ngẫu nhiên (dropout layer) kết hợp với hàm kích hoạt GELU
- **C.** Lớp kết nối đầy đủ (fully connected) và hàm Softmax
- **D.** Mạng nơ-ron hồi quy tuần tự (LSTM layer) với các cổng nhớ thông tin

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Giống như CNN, Vision Transformer (ViT) sử dụng một đầu phân loại (Classification. Head) ở cuối cùng, thường là một lớp MLP (Multilayer Perceptron) hoặc Linear Layer.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Giống như CNN, Vision Transformer (ViT) sử dụng một đầu phân loại (Classification
Head) ở cuối cùng, thường là một lớp MLP (Multilayer Perceptron) hoặc Linear Layer
kết hợp với hàm Softmax đểđưa ra xác suất cho các lớp.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 36). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 37 [VOAI25-037] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Dựa trên tập dữ liệu trong Bảng 1 dưới đây để xây dựng cây quyết định, hãy tính xấp xỉ entropy $H(\text{Passed})$. Cây quyết định này dự đoán liệu sinh viên có qua môn hay không (T là có, F là không), dựa trên điểm CGPA (H: cao, M: trung bình, L: thấp) và việc có ôn tập hay không (T hoặc F).

| CGPA | Ôn tập | Qua môn (Passed) |
|:---:|:---:|:---:|
| H | F | T |
| H | T | T |
| M | F | F |
| M | T | T |
| L | F | F |
| L | T | T |

- **A.** 0.66
- **B.** 1.92
- **C.** 0.92
- **D.** 1.32

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đề bài chỉ hỏi tính độ hỗn loạn (Entropy) của cột mục tiêu `Qua môn` (Passed).
Tổng cộng có 6 sinh viên:
- 4 sinh viên Qua môn (T)
- 2 sinh viên Trượt môn (F)
Tỉ lệ là 4/6 (hay 2/3) và 2/6 (hay 1/3). Ta chỉ việc áp dụng công thức Shannon Entropy quen thuộc!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Shannon Entropy với xác suất $p(T) = \frac{4}{6} = \frac{2}{3}$ và $p(F) = \frac{2}{6} = \frac{1}{3}$:
$$H(\text{Passed}) = - p(T) \log_2(p(T)) - p(F) \log_2(p(F))$$
$$H(\text{Passed}) = - \frac{2}{3} \log_2\left(\frac{2}{3}\right) - \frac{1}{3} \log_2\left(\frac{1}{3}\right)$$
Tính chi tiết:
- $\log_2(2/3) = \log_2(2) - \log_2(3) = 1 - 1.58496 = -0.58496$
- $\log_2(1/3) = -\log_2(3) = -1.58496$
- Số hạng 1: $-\frac{2}{3} \times (-0.58496) = +0.38997$
- Số hạng 2: $-\frac{1}{3} \times (-1.58496) = +0.52832$
$$H(\text{Passed}) = 0.38997 + 0.52832 = \mathbf{0.91829} \approx \mathbf{0.92}$$
Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Entropy không thể vượt quá 1 đối với bài toán nhị phân (loại ngay B = 1.92 và D = 1.32).
- Nhầm $\ln$ (cơ số tự nhiên) ra $0.636$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định (Decision Tree), Entropy & Information Gain** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 37).

---

### Câu 38 [VOAI25-038] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Một bức ảnh thuộc vào một trong hai lớp: ' chó ' hoặc ' mèo '. Nhãn thực tế (ground truth label) của ảnh
này được biểu diễn dưới dạng one-hot encoding là [0, 1], trong đó vị trí thứ nhất tương ứng với lớp ' chó ' và vị
trí thứ hai tương ứng với lớp ' mèo '. Mô hình của chúng ta đã dự đoán xác suất cho ảnh này là [0.3, 0.7], nghĩa
là xác suất dự đoán là 0.3 cho lớp ' chó ' và 0.7 cho lớp ' mèo '. Hãy tính giá trị của hàm mất mát cross-entropy
cho dự đoán này, sử dụng logarit tự nhiên (ln). Công thức hàm mất mát như sau:

- **A.** 0.105
- **B.** 0.247
- **C.** 0.357
- **D.** 0.713

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Công thức Cross-Entropy cho một mẫu: L = −P. i yi ln(ˆyi).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Công thức Cross-Entropy cho một mẫu: L = −P
i yi ln(ˆyi). Với y = [0, 1] (lớp thứ2
đúng) và ˆy = [0.3, 0.7]:
L = −(0 · ln(0.3) + 1 · ln(0.7)) = −ln(0.7)
L ≈−(−0.35667) ≈0.357

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 38). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 39 [VOAI25-039] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi tinh chỉnh (fine-tune) ResNet34, nếu suy luận (inference) chậm, bạn nên thử gì để tăng tốc độ?

- **A.** Chuyển sang dùng mô hình nhỏ hơn như MobileNet
- **B.** Thêm lớp bỏ ngẫu nhiên (dropout) vào suy luận
- **C.** Tăng số vòng lặp (epoch)
- **D.** Giảm số lớp (class)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
ResNet34 có kiến trúc khá sâu. Đểtăng tốc độsuy luận (inference speed) trên thiết.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
ResNet34 có kiến trúc khá sâu. Đểtăng tốc độsuy luận (inference speed) trên thiết
bị, giải pháp trực tiếp nhất là thay thếkiến trúc (Backbone) bằng các mô hình nhẹ
(lightweight) được tối ưu cho tốc độnhư MobileNet, EfficientNet hoặc ShuffleNet.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 39). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 40 [VOAI25-040] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi huấn luyện mạng nơ-ron đa tầng (MLP) bằng phương pháp tối ưu hóa theo lô nhỏ (mini-batch
SGD), bạn cần làm gì sau mỗi vòng lặp (epoch) để đảm bảo mô hình học hiệu quả và tránh thiên lệch?

- **A.** Xáo trộn dữ liệu (shuffle) huấn luyện
- **B.** Sử dụng toàn bộ dữ liệu (full-batch) để cập nhật trọng số
- **C.** Đặt lại trọng số về giá trị ban đầu
- **D.** Chuyển sang sử dụng bộ tối ưu Adam

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Việc xáo trộn (shuffle) dữ liệu sau mỗi epoch đảm bảo rằng các lô (batch) dữ liệu trong. epoch tiếp theo sẽngẫu nhiên và khác biệt so với epoch trước.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Việc xáo trộn (shuffle) dữ liệu sau mỗi epoch đảm bảo rằng các lô (batch) dữ liệu trong
epoch tiếp theo sẽngẫu nhiên và khác biệt so với epoch trước. Điều này giúp gradient
ước lượng không bị lặp lại theo chu kỳ, giúp mô hình hội tụtốt hơn và tránh kẹt vào cực
tiểu cục bộ.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 40). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 41 [VOAI25-041] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Với Lấy mẫu phủ định (Negative Sampling) , các mẫu sẽ được chọn như thế nào?

- **A.** Là các từ có độ tương đồng ngữ nghĩa cao với từ mục tiêu.
- **B.** Là các từ gần nhất với từ ngữ cảnh trong văn bản.
- **C.** Là các từ có nhãn đúng trong tập huấn luyện.
- **D.** Được chọn ngẫu nhiên từ toàn bộ từ vựng, thường theo một phân phối cố định.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong Word2Vec, các mẫu âm (negative samples) là các từ không xuất hiện cùng ngữ. cảnh với từ đích.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Trong Word2Vec, các mẫu âm (negative samples) là các từ không xuất hiện cùng ngữ
cảnh với từ đích. Chúng được lấy ngẫu nhiên từ từ điển (vocab) dựa trên phân phối tần
suất của từ (thường là phân phối unigram mũ 0.75).

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 41). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 42 [VOAI25-042] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Cho trước tập dữ liệu không có nhãn gồm N điểm dữ liệu: {𝑥 ,𝑥 ,...,𝑥 }. Chúng ta chạy K-means
! " 1
với 50 lần khởi tạo ngẫu nhiên tâm cụm khác nhau (luôn với cùng số lượng tâm cụm K) và thu được 50 bộ
tâm cụm khác nhau. Đâu là cách được gợi ý cho việc chọn 1 kết quả từ 50 kết quả trên để sử dụng?
1

- **A.** Chọn kết quả mà tổng bình phương khoảng cách tới tâm cụm $\sum ||x_i - m_k||^2$ đạt giá trị nhỏ nhất trong 50 lần chạy
- **B.** Chọn ngẫu nhiên kết quả của một lần chạy bất kỳ vì K-Means luôn luôn hội tụ về cùng một điểm cực tiểu toàn cục duy nhất
- **C.** Luôn luôn chọn kết quả của lần chạy cuối cùng (thứ 50) vì thuật toán được giả định tích lũy nghiệm tối ưu qua các chu kỳ
- **D.** Chỉ có thể đánh giá và chọn nghiệm chính xác khi toàn bộ tập dữ liệu được cung cấp nhãn giám sát thực tế từ ban đầu

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Hàm mục tiêu của K-means là tối thiểu hóa tổng bình phương khoảng cách từ các điểm. đến tâm cụm của chúng (Inertia/Distortion).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Hàm mục tiêu của K-means là tối thiểu hóa tổng bình phương khoảng cách từ các điểm
đến tâm cụm của chúng (Inertia/Distortion). Do K-means nhạy cảm với khởi tạo, ta chạy
nhiều lần và chọn lần có giá trịhàm mục tiêu (Inertia) nhỏ nhất. Công thức ở đáp án A
chính là Mean Squared Error của phép phân cụm.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.8** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 42). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 43 [VOAI25-043] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Sử dụng mô hình ResNet-18, với khoảng 11.7 triệu tham số, đã được tiền huấn luyện trên tập dữ liệu
ImageNet làm điểm khởi đầu. Trong quá trình tinh chỉnh cho nhiệm vụ cụ thể, bạn áp dụng chiến lược đóng
băng trọng số cho toàn bộ phần thân (backbone) của mô hình. Tuy nhiên, có một ngoại lệ đáng chú ý: bạn chỉ
mở băng và cho phép cập nhật trọng số cho một khối duy nhất là BasicBlock thứ hai nằm trong lớp thứ tư
(layer4), được gọi tắt là " block 4-2". Khối " block 4-2" này, bao gồm hai lớp tích chập 3×3:
- Bỏ qua tham số và tính toán không cần thiết: Chúng ta sẽ không tính số lượng tham số bias và bỏ qua chi
phí tính toán (FLOPs) của các lớp Batch Normalization (BN), hàm kích hoạt ReLU, và các kết nối tắt (skip
connection/identity mapping).
- Định nghĩa FLOPs: Một phép toán dấu phẩy động (FLOP) được tính là một phép nhân và một phép cộng.
Đối với lớp tích chập, tổng FLOPs xấp xỉ bằng 2 lần số phép tính nhân-cộng (MACs). (𝐹𝐿𝑂𝑃𝑠 ≈ 2×𝑀𝐴𝐶𝑠).
- Kích thước đầu vào cho khối: Khi mô hình xử lý một ảnh đầu vào gốc có kích thước 224×224, tensor đặc
trưng đi vào khối " block 4-2" có kích thước là (Batch=1, Channels=512, Height=7, Width=7).
Dựa trên giả sử trên, câu trả lời nào sau đây là đúng khi tính tính tổng số tham số có thể huấn luyện (trainable
parameters) chỉ chứa trong khối " block 4-2" và tổng số FLOPs cần thiết để thực thi chỉ riêng khối " block 4-
2" khi xử lý tensor đầu vào có kích thước (1,512,7,7).

- **A.** 11.7M; 1.8GFLOPs
- **B.** 4.7M; 0.46GFLOPs
- **C.** 0.50M; 0.05GFLOPs
- **D.** 8.4M; 0.82GFLOPs

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tham số (Params): Khối có 2 lớp Conv2D (3 × 3, Cin = 512, Cout = 512). Param1 = 3 × 3 × 512 × 512 = 2, 359, 296.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Tham số (Params): Khối có 2 lớp Conv2D (3 × 3, Cin = 512, Cout = 512).
Param1 = 3 × 3 × 512 × 512 = 2, 359, 296
Tổng params = 2 × 2, 359, 296 ≈4.7 triệu.
FLOPs: Input 7 × 7.
MACs1 = H × W × Param1 = 7 × 7 × 2, 359, 296 ≈115.6 triệu
Tổng MACs = 2 × 115.6 = 231.2 triệu. Tổng FLOPs ≈2 × MACs = 462.4 triệu ≈0.46
GFLOPs.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 43). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 44 [VOAI25-044] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Tỷ lệ học thích ứng (adaptive learning rate) như AdaGrad, RMSProp, Adam giúp gì cho mô hình?

- **A.** Giảm kích thước mô hình
- **B.** Tăng kích thước lô (batch size)
- **C.** Giảm số vòng lặp (epoch) cần thiết
- **D.** Tự động điều chỉnh tốc độ học cho từng tham số

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đặc điểm cốt lõi của các thuật toán Adaptive Learning Rate là chúng duy trì learning. rate riêng biệt cho mỗi tham số (weight) trong mạng, dựa trên độlớn của gradient trong.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đặc điểm cốt lõi của các thuật toán Adaptive Learning Rate là chúng duy trì learning
rate riêng biệt cho mỗi tham số (weight) trong mạng, dựa trên độlớn của gradient trong
quá khứ, thay vì dùng một learning rate chung cho toàn bộ mạng.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 44). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 45 [VOAI25-045] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Trong tối ưu hóa theo lô nhỏ (mini-batch SGD), nếu kích thước lô (batch size) quá nhỏ, hệ quả thường
gặp là gì?

- **A.** Giảm thời gian huấn luyện
- **B.** Gradient quá nhiễu, gây dao động
- **C.** Độ chính xác tăng nhanh
- **D.** Không ảnh hưởng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Batch size nhỏ đồng nghĩa với việc gradient được ước lượng từít mẫu dữ liệu hơn, dẫn. đến phương sai cao (nhiễu).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Batch size nhỏ đồng nghĩa với việc gradient được ước lượng từít mẫu dữ liệu hơn, dẫn
đến phương sai cao (nhiễu). Điều này khiến đường đi của hàm mất mát dao động mạnh
(zig-zag) và có thểlàm quá trình hội tụkhông ổn định, dù đôi khi giúp thoát khỏi cực
tiểu cục bộ.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 45). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 46 [VOAI25-046] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Những chiến lược nào có thể giúp giảm vấn đề quá khớp (overfitting) trong cây quyết định?
- (i) Giới hạn độ sâu tối đa của cây (Max depth)
- (ii) Áp đặt số lượng mẫu tối thiểu tại các nút lá (Min samples per leaf)
- (iii) Cắt tỉa cây (Pruning)
- (iv) Đảm bảo mỗi nút lá chứa duy nhất một lớp (Pure leaf)

- **A.** Không có lựa chọn nào đúng
- **B.** Tất cả
- **C.** (i), (ii) và (iii)
- **D.** (i), (iii), (iv)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Cây càng mọc sâu và phân nhánh vô tận thì càng học thuộc lòng cả các mẫu nhiễu (Overfitting).
- Vì vậy: Chặn độ sâu cây (i), bắt buộc mỗi lá phải có nhiều học sinh cùng nhóm (ii), và chặt bớt cành thừa sau khi trồng (iii) đều giúp cây đơn giản và tổng quát hóa tốt hơn.
- Ngược lại, ép mỗi lá chỉ chứa 1 người duy nhất (iv) chính là nguyên nhân trực tiếp gây Overfitting!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích từng chiến lược:
- (i) `max_depth` giới hạn số lượng câu hỏi, kiểm soát độ phức tạp mô hình VC dimension $\implies$ Giảm Overfitting.
- (ii) `min_samples_leaf` ngăn không cho cây tạo nhánh riêng cho một vài điểm dữ liệu ngoại lai $\implies$ Giảm Overfitting.
- (iii) `cost_complexity_pruning` (ccp_alpha) tối ưu hàm mục tiêu $R_\alpha(T) = R(T) + \alpha |T|$ để cắt bớt nhánh $\implies$ Giảm Overfitting.
- (iv) Làm lá thuần khiết 100% thúc đẩy cây phát triển tối đa cho đến khi Training Error = 0 $\implies$ Gây Overfitting nghiêm trọng.
Do đó chỉ có (i), (ii) và (iii) là đúng. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nhầm tưởng lá thuần khiết là mục tiêu lý tưởng và chọn B (Tất cả).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định (Decision Tree), Entropy & Information Gain** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 46).

---

### Câu 47 [VOAI25-047] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Một nơ-ron có 3 đầu vào với trọng số lần lượt là 1, 4 và 3, không có bias. Hàm truyền là hàm tuyến
tính với hằng số tỷ lệ bằng 3. Các đầu vào lần lượt là 4, 8 và 5. Đầu ra sẽ là bao nhiêu?

- **A.** 162
- **B.** 153
- **C.** 139
- **D.** 160

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Tổng trọng số (Weighted Sum): z = 4 × 1 + 8 × 4 + 5 × 3 = 4 + 32 + 15 = 51. Hàm truyền.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Tổng trọng số (Weighted Sum): z = 4 × 1 + 8 × 4 + 5 × 3 = 4 + 32 + 15 = 51. Hàm truyền
(Activation): f(z) = 3 × z = 3 × 51 = 153.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 47). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 48 [VOAI25-048] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Gradient của hàm số $f(x, y) = 2x^2 - 3y^2 + 4y - 10$ tại điểm $(0, 0)$ là:

- **A.** 1i + 10j
- **B.** 2i - 3j
- **C.** -3i + 4j
- **D.** 0i + 4j

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Gradient của hàm số nhiều biến $\nabla f(x, y)$ là vector chứa các đạo hàm riêng theo từng biến $\left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
- **Đạo hàm riêng theo $x$:**
  $$\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(2x^2 - 3y^2 + 4y - 10) = 4x$$
  Tại điểm $(0, 0)$: $\frac{\partial f}{\partial x}(0, 0) = 4(0) = 0$.

- **Đạo hàm riêng theo $y$:**
  $$\frac{\partial f}{\partial y} = \frac{\partial}{\partial y}(2x^2 - 3y^2 + 4y - 10) = -6y + 4$$
  Tại điểm $(0, 0)$: $\frac{\partial f}{\partial y}(0, 0) = -6(0) + 4 = 4$.

- **Vector Gradient:**
  $$\nabla f(0, 0) = (0, 4) = 0\mathbf{i} + 4\mathbf{j}$$

**Đáp án chính xác là D.**

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cẩn thận nhầm dấu của số hạng $-3y^2$ khi lấy đạo hàm, dẫn đến chọn sai phương án B hoặc C.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 48). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 49 [VOAI25-049] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi huấn luyện mô hình phân loại nhiều lớp với tập dữ liệu mất cân bằng về nhãn lớp, nếu lớp hiếm
(ít dữ liệu huấn luyện) gần như không được dự đoán, cách xử lý phù hợp là gì?

- **A.** Giảm số vòng lặp (epoch)
- **B.** Xóa lớp hiếm khỏi dữ liệu
- **C.** Tăng bỏ ngẫu nhiên (dropout)
- **D.** Sử dụng hàm mất mát có trọng số

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi dữ liệu mất cân bằng (Imbalanced Data), mô hình có xu hướng thiên vị lớp đa số. Sử dụng Weighted Loss (gán trọng số phạt lớn hơn cho lớp thiểu số) giúp mô hình " chú.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Khi dữ liệu mất cân bằng (Imbalanced Data), mô hình có xu hướng thiên vị lớp đa số.
Sử dụng Weighted Loss (gán trọng số phạt lớn hơn cho lớp thiểu số) giúp mô hình " chú
ý " hơn đến các lỗi sai trên lớp hiếm, từ đó cải thiện khả năng dự đoán lớp này.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.9** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 49). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 50 [VOAI25-050] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi tinh chỉnh (fine-tune) MobileNetV2 trên tập dữ liệu nhỏ, bước đầu tiên bạn nên làm là gì để tối
ưu hóa hiệu suất?

- **A.** Tăng số lớp
- **B.** Thay toàn bộ mô hình
- **C.** Đóng băng (freeze) các lớp đầu tiên
- **D.** Tăng tỷ lệ học (learning rate)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi tập dữ liệu mới nhỏ và tương tự tập gốc (thường là ImageNet), chiến lược tốt nhất. là đóng băng (freeze) phần lớn các lớp trích xuất đặc trưng (backbone) đểgiữ lại các.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Khi tập dữ liệu mới nhỏ và tương tự tập gốc (thường là ImageNet), chiến lược tốt nhất
là đóng băng (freeze) phần lớn các lớp trích xuất đặc trưng (backbone) đểgiữ lại các
đặc trưng đã học, và chỉ huấn luyện lớp phân loại cuối cùng (Classifier head) đểtránh
Overfitting.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 50). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 51 [VOAI25-051] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi huấn luyện bằng PyTorch, nếu GPU bị đầy bộ nhớ (Out-of-Memory - OOM), bạn nên thử gì đầu
tiên?

- **A.** Chuyển toàn bộ quá trình tính toán sang CPU để tận dụng dung lượng bộ nhớ RAM của hệ thống máy tính
- **B.** Tăng tỷ lệ loại bỏ ngẫu nhiên (dropout rate) nhằm giảm bớt số lượng các kết nối nơ-ron đang hoạt động
- **C.** Sử dụng kiến trúc mô hình có quy mô tham số lớn hơn để mở rộng dung lượng bộ đệm đồ thị tính toán
- **D.** Giảm kích thước lô (batch size) hoặc dùng tích lũy gradient (gradient accumulation)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Lỗi OOM xảy ra khi VRAM không đủchứa các tensor (tham số+ activation + gradient). Cách hiệu quảnhất để giảm bộ nhớtức thời là giảm Batch Size.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Lỗi OOM xảy ra khi VRAM không đủchứa các tensor (tham số+ activation + gradient).
Cách hiệu quảnhất để giảm bộ nhớtức thời là giảm Batch Size. Nếu Batch Size quá nhỏ
ảnh hưởng đến hội tụ, có thểdùng Gradient Accumulation để mô phỏng batch lớn hơn.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 51). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 52 [VOAI25-052] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp nào sau đây KHÔNG thuộc nhóm học có giám sát?

- **A.** Cây quyết định
- **B.** Hồi quy tuyến tính với Ridge
- **C.** Naive Bayes
- **D.** K-means

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
K-means là thuật toán Phân cụm (Clustering), thuộc nhóm Học không giám sát. (Unsupervised Learning) vì nó làm việc với dữ liệu không có nhãn (unlabeled data).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
K-means là thuật toán Phân cụm (Clustering), thuộc nhóm Học không giám sát
(Unsupervised Learning) vì nó làm việc với dữ liệu không có nhãn (unlabeled data).
Các phương pháp còn lại đều yêu cầu nhãn y.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.8** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 52). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 53 [VOAI25-053] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Phát biểu nào sau đây là đúng về giải thuật học láng giềng gần nhất?

- **A.** Chỉ được sử dụng cho bài toán hồi quy
- **B.** Thuộc lớp bài toán học tham số
- **C.** Chỉ được sử dụng cho bài toán phân loại
- **D.** Được sử dụng cho cả bài toán phân loại và bài toán hồi quy

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
k-NN có thểdùng cho cả Classification (k-NN Classifier - bầu chọn đa số) và Regression. (k-NN Regressor - lấy trung bình giá trịcác láng giềng).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
k-NN có thểdùng cho cả Classification (k-NN Classifier - bầu chọn đa số) và Regression
(k-NN Regressor - lấy trung bình giá trịcác láng giềng). Nó là thuật toán phi tham số
(non-parametric).

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 53). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 54 [VOAI25-054] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mục đích chính của việc tăng cường dữ liệu trong huấn luyện mô hình học máy/học sâu là gì?

- **A.** Tăng tốc độ huấn luyện mô hình
- **B.** Giảm số lượng tham số của mô hình
- **C.** Giảm kích thước vật lý của tập dữ liệu gốc
- **D.** Cải thiện khả năng tổng quát hóa của mô hình

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Data Augmentation tạo ra các biến thểmới của dữ liệu huấn luyện (xoay, lật, nhiễu. giúp mô hình học được các đặc trưng bất biến (invariant features), từ đó giảm Overfitting.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Data Augmentation tạo ra các biến thểmới của dữ liệu huấn luyện (xoay, lật, nhiễu...),
giúp mô hình học được các đặc trưng bất biến (invariant features), từ đó giảm Overfitting
và tăng khả năng tổng quát hóa (Generalization) trên dữ liệu kiểm thử.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 54). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 55 [VOAI25-055] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi sử dụng BertTokenizer từ Hugging Face, điều nào sau đây đúng?

- **A.** Bộ mã hóa không hỗ trợ lô (batch)
- **B.** tokenizer.encode_plus() trả về input_ids, attention_mask
- **C.** BERT chỉ dùng cho tiếng Anh
- **D.** Bộ mã hóa (tokenizer) không cần đệm (padding)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Hàm encode_plus (hoặc __call__ trong các bản mới) của Tokenizer trảvề một. dictionary chứa các thành phần thiết yếu đểđưa vào mô hình BERT: input_ids (danh.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Hàm encode_plus (hoặc __call__ trong các bản mới) của Tokenizer trảvề một
dictionary chứa các thành phần thiết yếu đểđưa vào mô hình BERT: input_ids (danh
sách ID của token), attention_mask (mặt nạđể mô hình bỏ qua các phần padding), và
token_type_ids (phân biệt các câu).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 55). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 56 [VOAI25-056] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Dưới đây là một số lựa chọn để có thể thực hiện khi huấn luyện mạng nơ-ron. Đâu là trường hợp sẽ
khiến mạng của bạn KHÓ đạt được độ chính xác cao trong tương lai?

- **A.** Đảo ngẫu nhiên lại dữ liệu khi bắt đầu mỗi epoch
- **B.** Khởi tạo tất cả bộ tham số bằng 0
- **C.** Sử dụng momentum
- **D.** Sử dụng Dropout

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Việc khởi tạo tất cả trọng số bằng 0 (Zero Initialization) làm mất tính bất đối xứng. (Symmetry breaking).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Việc khởi tạo tất cả trọng số bằng 0 (Zero Initialization) làm mất tính bất đối xứng
(Symmetry breaking). Tất cả các nơ-ron trong cùng một lớp sẽtính toán ra cùng một
đầu ra và có cùng gradient, khiến chúng cập nhật giống hệt nhau. Mạng sẽ không bao
giờhọc được các tính năng phức tạp (hoạt động như một nơ-ron đơn lẻ).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 56). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 57 [VOAI25-057] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình SSD, hộp neo (anchor boxes) có vai trò gì?

- **A.** Định nghĩa trước các tỷ lệ và kích thước hộp neo (Anchor Boxes)
- **B.** Làm nhẹ mô hình để triển khai trên các thiết bị nhúng (Model Pruning)
- **C.** Làm tăng số lượng các tầng tích chập sâu (Deep Feature Stacking)
- **D.** Tăng độ phân giải không gian của ảnh trước khi phát hiện (Upsampling)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong các mô hình One-stage object detection như SSD hay YOLO, Anchor Boxes (hoặc. Default Boxes) là các hộp có kích thước và tỷ lệkhung hình (aspect ratio) được định.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Trong các mô hình One-stage object detection như SSD hay YOLO, Anchor Boxes (hoặc
Default Boxes) là các hộp có kích thước và tỷ lệkhung hình (aspect ratio) được định
nghĩa trước tại mỗi vị trí trên feature map. Mô hình sẽdự đoán độlệch (offset) so với
các hộp neo này thay vì dự đoán tọa độtuyệt đối.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 57). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 58 [VOAI25-058] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Quan sát hai ma trận nhầm lẫn (Confusion Matrix) dưới đây thu được trên tập huấn luyện (Train Set) và tập kiểm thử (Test Set):

**Train Set Confusion Matrix:**
| True \ Pred | A | B | C | D |
|:---:|:---:|:---:|:---:|:---:|
| **A** | 450 | 5 | 3 | 2 |
| **B** | 6 | 430 | 8 | 6 |
| **C** | 3 | 7 | 460 | 4 |
| **D** | 2 | 5 | 3 | 470 |

**Test Set Confusion Matrix:**
| True \ Pred | A | B | C | D |
|:---:|:---:|:---:|:---:|:---:|
| **A** | 80 | 10 | 5 | 5 |
| **B** | 12 | 70 | 10 | 8 |
| **C** | 8 | 12 | 65 | 15 |
| **D** | 10 | 8 | 12 | 70 |

Nhận định nào sau đây là chính xác nhất trong số các lựa chọn được đưa ra?

- **A.** Mô hình có dấu hiệu quá khớp (Overfitting)
- **B.** Mô hình có dấu hiệu kém khớp (Underfitting)
- **C.** Độ chính xác trên tập kiểm thử và huấn luyện là gần như tương đương nhau
- **D.** Sai số chỉ do phân bố lớp khác nhau giữa hai tập

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
- Trên tập học (Train): Đường chéo chính sáng rực (450, 430, 460, 470), các ô đoán sai rất ít $\implies$ Mô hình đạt độ chính xác gần như tuyệt đối (~97%).
- Trên tập thi (Test): Các ô đoán sai xuất hiện dày đặc xung quanh đường chéo, độ chính xác sụt giảm mạnh (~71%).
Khi kết quả bài học quá hoàn hảo nhưng bài thi thực tế tụt dốc, đó là dấu hiệu kinh điển của **Quá khớp (Overfitting)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 1. Tính Accuracy trên Train Set:
- Tổng đúng (đường chéo): $450 + 430 + 460 + 470 = 1810$.
- Tổng mẫu: $1810 + (5+3+2) + (6+8+6) + (3+7+4) + (2+5+3) = 1810 + 60 = 1870$.
$$\text{Acc}_{\text{train}} = \frac{1810}{1870} \approx 96.79\%$$
2. Tính Accuracy trên Test Set:
- Tổng đúng: $80 + 70 + 65 + 70 = 285$.
- Tổng mẫu: $285 + (10+5+5) + (12+10+8) + (8+12+15) + (10+8+12) = 285 + 115 = 400$.
$$\text{Acc}_{\text{test}} = \frac{285}{400} = 71.25\%$$
Độ chênh lệch lớn giữa Train (96.8%) và Test (71.3%) chứng minh mô hình bị Overfitting. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Nhầm Underfitting: Khi Underfitting thì ngay cả tập Train cũng có độ chính xác rất thấp.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5 Overfitting, Underfitting, Bias-Variance Tradeoff & Cross-Validation** và **§1.7 Các độ đo đánh giá mô hình** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 58).

---

### Câu 59 [VOAI25-059] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Entropy cao có nghĩa là các phần phân chia trong thuật toán cây quyết định ID3 thì

- **A.** Thuần khiết (Pure): Các điểm dữ liệu ở mỗi nhánh của cây quyết định tập trung đa số vào một lớp
- **B.** Không có ý nghĩa gì
- **C.** Không thuần khiết (Not pure): Các điểm dữ liệu ở mỗi nhánh của cây quyết định phân bố tương đối đều vào các lớp
- **D.** Có thể suy ra độ đo F1-score cao

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong thuật toán ID3, Entropy là thước đo độhỗn loạn (impurity) của dữ liệu. • Entropy thấp (xấp xỉ0): Các phần tửtrong tập dữ liệu chủ yếu thuộc về một.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Trong thuật toán ID3, Entropy là thước đo độhỗn loạn (impurity) của dữ liệu.
• Entropy thấp (xấp xỉ0): Các phần tửtrong tập dữ liệu chủ yếu thuộc về một
lớp duy nhất (thuần khiết).
• Entropy cao: Các phần tửphân bố đều giữa các lớp khác nhau, dẫn đến độhỗn
loạn cao hay còn gọi là không thuần khiết (Not pure).
Giá trị Entropy cực đại khi xác suất của các lớp là bằng nhau (pi = 1/n).

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 59). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 60 [VOAI25-060] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mục đích của việc thêm nhiễu Gaussian vào dữ liệu đầu vào khi huấn luyện là gì?

- **A.** Giảm số lớp cần thiết
- **B.** Tăng tính ổn định và khả năng chống nhiễu
- **C.** Giảm thời gian huấn luyện
- **D.** Tăng độ chính xác

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Thêm nhiễu (Noise injection) vào dữ liệu đầu vào là một hình thức Regularization. buộc mô hình không được phụ thuộc quá mức vào các chi tiết nhỏ (có thểlà nhiễu) của.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Thêm nhiễu (Noise injection) vào dữ liệu đầu vào là một hình thức Regularization. Nó
buộc mô hình không được phụ thuộc quá mức vào các chi tiết nhỏ (có thểlà nhiễu) của
dữ liệu ban đầu, từ đó giúp mô hình bền vững hơn (Robust) và có khả năng tổng quát
hóa tốt hơn khi gặp các dữ liệu thực tếbiến thiên.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.6** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 60). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 61 [VOAI25-061] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi huấn luyện mạng GAN, nếu bộ tạo (generator) tạo ra ảnh toàn màu xám, nguyên nhân có thể là
gì?

- **A.** Hàm mất mát (loss function) giảm quá nhanh về 0 khiến gradient bị biến mất
- **B.** Tỷ lệ học (learning rate) quá nhỏ làm cho các trọng số hầu như không thay đổi
- **C.** Kích thước lô (batch size) quá lớn làm suy giảm tính ngẫu nhiên của bước nhảy
- **D.** Mất cân bằng giữa bộ phân biệt (discriminator) và bộ tạo (generator)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Hiện tượng ảnh sinh ra bị mờhoặc chỉ có màu xám trung tính thường xảy ra khi Bộ. phân biệt (Discriminator) quá mạnh so với Bộ tạo (Generator).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Hiện tượng ảnh sinh ra bị mờhoặc chỉ có màu xám trung tính thường xảy ra khi Bộ
phân biệt (Discriminator) quá mạnh so với Bộ tạo (Generator). Khi đó, gradient biến
mất hoặc không cung cấp đủthông tin hữu ích, khiến Generator chọn phương án " an
toàn " là sinh ra màu trung bình của tập dữ liệu (thường là màu xám) để giảm thiểu mất
mát cục bộ.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 61). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 62 [VOAI25-062] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán phân loại văn bản, nếu mô hình học tốt các từ khóa rõ ràng nhưng không hiểu ngữ
cảnh, phương pháp nào giúp cải thiện khả năng hiểu ngữ cảnh?

- **A.** Dùng mô hình dựa trên chú ý (attention-based) như BERT
- **B.** Bỏ nhúng (embedding), dùng vector gồm các số 0 và một số 1 (one-hot vector)
- **C.** Chuyển sang dùng TF-IDF
- **D.** Giảm số chiều nhúng (embedding)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Các phương pháp như TF-IDF hay One-hot chỉ quan tâm đến sự xuất hiện của từ (từ. khóa) mà bỏ qua thứtự.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Các phương pháp như TF-IDF hay One-hot chỉ quan tâm đến sự xuất hiện của từ (từ
khóa) mà bỏ qua thứtự. Đểnắm bắt " ngữ cảnh "(sự phụ thuộc giữa các từ trong câu),
cơ chế Self-Attention của BERT là giải pháp tối ưu nhất hiện nay.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 62). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 63 [VOAI25-063] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Nếu mô hình bị học quá mức (overfitting), phương pháp nào nên thử đầu tiên để giảm hiện tượng
này?

- **A.** Tăng số vòng lặp huấn luyện (epoch) để mô hình có thêm thời gian hội tụ sâu hơn
- **B.** Thêm bỏ ngẫu nhiên (dropout) hoặc tăng suy giảm trọng số (weight decay)
- **C.** Tăng tỷ lệ học (learning rate) lên gấp đôi để vượt qua các cực tiểu địa phương
- **D.** Giảm kích thước lô (batch size) và loại bỏ toàn bộ các bước tiền xử lý chuẩn hóa

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Dropout và Weight Decay (L2 Regularization) là hai kỹ thuật chính quy hóa. (Regularization) tiêu chuẩn và trực tiếp nhất để giảm Overfitting bằng cách ngăn mô.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Dropout và Weight Decay (L2 Regularization) là hai kỹ thuật chính quy hóa
(Regularization) tiêu chuẩn và trực tiếp nhất để giảm Overfitting bằng cách ngăn mô
hình phụ thuộc quá nhiều vào một sốnơ-ron hoặc trọng số cụthể.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.9** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 63). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 64 [VOAI25-064] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Khi huấn luyện, nếu độ chính xác huấn luyện (training accuracy) tăng đều nhưng độ chính xác kiểm
tra (validation accuracy) dao động mạnh và không cải thiện, nguyên nhân có thể là gì?

- **A.** Học quá mức (overfitting) hoặc dữ liệu kiểm tra chưa được xáo trộn kỹ
- **B.** Không kích hoạt cơ chế bỏ ngẫu nhiên (dropout) ở các tầng kết nối đầy đủ
- **C.** Kiến trúc mô hình quá nhỏ khiến dung lượng biểu diễn thông tin không đủ
- **D.** Số vòng lặp (epoch) quá ít khiến mô hình chưa kịp hội tụ trên tập huấn luyện

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đây là biểu hiện kinh điển của Overfitting: mô hình học thuộc lòng dữ liệu huấn luyện. (Training acc tăng) nhưng không tổng quát hóa được trên dữ liệu mới (Validation acc đi.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đây là biểu hiện kinh điển của Overfitting: mô hình học thuộc lòng dữ liệu huấn luyện
(Training acc tăng) nhưng không tổng quát hóa được trên dữ liệu mới (Validation acc đi
ngang hoặc giảm/dao động). Ngoài ra, nếu phân phối dữ liệu Validation khác biệt (do
chưa shuffle kỹ), hiện tượng này cũng xảy ra.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 64). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 65 [VOAI25-065] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mục tiêu chính khi tinh chỉnh (fine-tune) mô hình BERT cho bài toán phân loại văn bản là gì?

- **A.** Tạo nhúng (embedding)
- **B.** Thay lớp cuối bằng một lớp phân loại
- **C.** Dùng mô hình sinh
- **D.** Tạo một bộ mã hóa (tokenizer) mới

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Mô hình BERT gốc chỉ xuất ra các vector đặc trưng. Đểphân loại, ta cần thêm một lớp.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Mô hình BERT gốc chỉ xuất ra các vector đặc trưng. Đểphân loại, ta cần thêm một lớp
Linear (Classifier Head) vào vị trí đầu ra của token [CLS] và huấn luyện lớp này (cùng
với tinh chỉnh nhẹ BERT) đểdự đoán nhãn.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 65). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 66 [VOAI25-066] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Nếu tỷ lệ học (learning rate) quá cao, điều gì có thể xảy ra trong quá trình huấn luyện?

- **A.** Mô hình dao động và không hội tụ
- **B.** Tăng khả năng regularization
- **C.** Hàm mất mát giảm đều đặn
- **D.** Mô hình hội tụ nhanh hơn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Learning rate quá lớn khiến các bước cập nhật trọng số " nhảy " qua điểm cực tiểu. (overshoot), dẫn đến hàm mất mát dao động mạnh (oscillate) hoặc thậm chí phân kỳ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Learning rate quá lớn khiến các bước cập nhật trọng số " nhảy " qua điểm cực tiểu
(overshoot), dẫn đến hàm mất mát dao động mạnh (oscillate) hoặc thậm chí phân kỳ
(diverge - loss tăng dần đến vô cực).

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 66). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 67 [VOAI25-067] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Sự khác biệt chính giữa tập xác thực (validation set) và tập kiểm tra (test set) là gì?

- **A.** Tập xác thực là không cần thiết trong học máy.
- **B.** Tập xác thực dùng để điều chỉnh siêu tham số, còn tập kiểm tra dùng để đánh giá hiệu suất của mô hình.
- **C.** Tập xác thực và tập kiểm tra là một.
- **D.** Tập xác thực dùng để đánh giá hiệu suất mô hình trong quá trình huấn luyện, trong khi tập kiểm tra dùng để đánh giá sau khi huấn luyện.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
(D cũng khá đúng, nhưng B đúng hơn xíu). Validation Set: Dùng trong quá trình phát triển mô hình đểchọn ra kiến trúc tốt nhất,.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
(D cũng khá đúng, nhưng B đúng hơn xíu)
Validation Set: Dùng trong quá trình phát triển mô hình đểchọn ra kiến trúc tốt nhất,
tinh chỉnh siêu tham số (Hyperparameter tuning) và ngăn chặn hiện tượng quá khớp
(overfitting). Test Set: Chỉ được sử dụng một lần duy nhất sau khi quá trình huấn
luyện và tinh chỉnh đã hoàn tất đểđưa ra con số đánh giá thực tếnhất về khả năng tổng
quát hóa của mô hình trên dữ liệu mới.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 67). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 68 [VOAI25-068] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Xét một Random Forest gồm $K$ cây với nhiệm vụ hồi quy. Mỗi cây quyết định $i$ có thể biểu diễn một hàm $T_i(x)$ của đầu vào $x$. Random Forest này biểu diễn hàm nào sau đây?

- **A.** $y(x) = \sum_{i=1}^K T_i(x)$
- **B.** $y(x) = \max_{i \in \{1,\dots, K\}} T_i(x)$
- **C.** $y(x) = \sum_{i=1}^K T_i\left(\frac{x}{K}\right)$
- **D.** $y(x) = \frac{1}{K} \sum_{i=1}^K T_i(x)$

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong bài toán hồi quy (đoán số điểm, giá nhà), Random Forest sử dụng cơ chế trung bình cộng (Bagging Aggregation): Lấy kết quả dự đoán của từng cây $T_i(x)$ cộng lại rồi chia đều cho tổng số cây $K$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Mô hình Random Forest Hồi quy (Breiman, 2001):
Hàm dự đoán tổng hợp là trung bình cộng số học của $K$ cây quyết định độc lập:
$$y(x) = \frac{1}{K} \sum_{i=1}^K T_i(x)$$
Phép lấy trung bình này giúp giảm phương sai $\text{Var}(y(x)) \approx \rho \sigma^2 + \frac{1-\rho}{K} \sigma^2$ xuống đáng kể so với một cây đơn lẻ. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Phương án A thiếu hệ số chia $1/K$ (thành phép tính tổng thay vì trung bình).
- Phương án B là phép lấy max, chỉ dùng cho bài toán biên đặc thù.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.4 Random Forest & Phương pháp Ensemble** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 68).

---

### Câu 69 [VOAI25-069] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Để tải nhúng từ (embedding) Word2Vec đã được huấn luyện trước trong thư viện gensim, bạn sử
dụng lệnh nào?

- **A.** gensim.models.load(" word2vec ")
- **B.** import word2vec.load_model(path)
- **C.** KeyedVectors.load_word2vec_format(path)
- **D.** spacy.load_word2vec(path)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong thư viện Gensim (các phiên bản phổ biến gần đây), đểtải file vector Word2Vec. định dạng C (binary hoặc text), ta sử dụng lớp ‘KeyedVectors‘ và phương thức.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Trong thư viện Gensim (các phiên bản phổ biến gần đây), đểtải file vector Word2Vec
định dạng C (binary hoặc text), ta sử dụng lớp ‘KeyedVectors‘ và phương thức
‘load_word2vec_format‘.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 69). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 70 [VOAI25-070] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi sử dụng câu lệnh nn. CrossEntropyLoss trong PyTorch, bạn nên đưa gì vào đối số đầu tiên?

- **A.** Logits do lớp cuối cùng của mạng tạo ra
- **B.** Vector gồm các số 0 và một số 1 (one-hot vector) biểu diễn các lớp mục tiêu
- **C.** Xác suất thu được sau khi áp dụng softmax lên đầu ra của mạng
- **D.** Log-xác suất sau khi áp dụng log_softmax lên đầu ra của mạng

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đặc thù của ‘nn. CrossEntropyLoss‘ trong PyTorch là nó đã tích hợp sẵn hàm.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đặc thù của ‘nn. CrossEntropyLoss‘ trong PyTorch là nó đã tích hợp sẵn hàm
‘LogSoftmax‘ bên trong. Do đó, đầu vào của nó phải là Logits (giá trịthô chưa qua
activation), không phải xác suất hay one-hot.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 70). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 71 [VOAI25-071] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong huấn luyện, nếu mất mát huấn luyện (training loss) giảm nhưng mất mát kiểm tra (validation
loss) tăng, điều này cho thấy gì?

- **A.** Mô hình đang học quá mức (overfitting)
- **B.** Mô hình đang hội tụ
- **C.** Cần tăng tỷ lệ học (learning rate)
- **D.** Mô hình học chưa đủ (underfitting)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi Loss trên tập Train tiếp tục giảm trong khi Loss trên tập Validation bắt đầu tăng. ngược trởlại, đó là điểm gãy (inflection point) đánh dấu mô hình bắt đầu Overfitting.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Khi Loss trên tập Train tiếp tục giảm trong khi Loss trên tập Validation bắt đầu tăng
ngược trởlại, đó là điểm gãy (inflection point) đánh dấu mô hình bắt đầu Overfitting
(học nhiễu của tập train).

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 71). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 72 [VOAI25-072] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong các bài toán phân đoạn ảnh (image segmentation), một thách thức phổ biến là sự mất cân bằng
nghiêm trọng giữa các lớp. Ví dụ, diện tích của đối tượng cần phân đoạn (lớp tiền cảnh - foreground) có thể
rất nhỏ so với phần còn lại của ảnh (lớp hậu cảnh - background). Khi gặp tình huống mất cân bằng lớp như
vậy, hàm mất mát (loss function) nào trong số các lựa chọn dưới đây thường được xem là hiệu quả hơn và
được ưu tiên sử dụng thay cho hàm Cross-Entropy (CE) tiêu chuẩn?

- **A.** Mean Squared Error (MSE)
- **B.** Hinge Loss
- **C.** 𝐿 Loss
- **D.** Dice Loss hoặc Focal Loss !

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Dice Loss (dựa trên hệ số Dice/IoU) và Focal Loss được thiết kếđặc biệt đểxử lý vấn. đềmất cân bằng dữ liệu nghiêm trọng trong phân đoạn ảnh y tếhoặc vật thểnhỏ, bằng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Dice Loss (dựa trên hệ số Dice/IoU) và Focal Loss được thiết kếđặc biệt đểxử lý vấn
đềmất cân bằng dữ liệu nghiêm trọng trong phân đoạn ảnh y tếhoặc vật thểnhỏ, bằng
cách tập trung vào vùng giao thoa hoặc các mẫu khó phân loại.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 72). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 73 [VOAI25-073] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mạng nơ-ron ResNet sử dụng một kỹ thuật quan trọng gọi là kết nối tắt (skip connection) để giải quyết hiện tượng biến mất đạo hàm (Vanishing Gradient) trong quá trình huấn luyện. Dựa trên đoạn mã của khối identity_block dưới đây, hãy liệt kê các thành phần chính của khối theo đúng thứ tự xuất hiện và chỉ ra dòng mã thực hiện phép kết nối tắt:

```python
1  def identity_block(X, f, filters, stage, block):
2  
3      conv_name_base = ' res ' + str(stage) + block + '_branch '
4      bn_name_base = ' bn ' + str(stage) + block + '_branch '
5  
6      F1, F2, F3 = filters
7  
8      X_shortcut = X
9  
10     X = Conv2D(filters = F1, kernel_size = (1, 1), strides = (1, 1), padding = ' valid ', name = conv_name_base + '2a ', kernel_initializer = glorot_uniform(seed=0))(X)
11     X = BatchNormalization(axis = 3, name = bn_name_base + '2a ')(X)
12     X = Activation(' relu ')(X)
13  
14     X = Conv2D(filters = F2, kernel_size = (f, f), strides = (1, 1), padding = ' same ', name = conv_name_base + '2b ', kernel_initializer = glorot_uniform(seed=0))(X)
15     X = BatchNormalization(axis = 3, name = bn_name_base + '2b ')(X)
16     X = Activation(' relu ')(X)
17  
18     X = Conv2D(filters = F3, kernel_size = (1, 1), strides = (1, 1), padding = ' valid ', name = conv_name_base + '2c ', kernel_initializer = glorot_uniform(seed=0))(X)
19     X = BatchNormalization(axis = 3, name = bn_name_base + '2c ')(X)
20  
21     X = Add()([X_shortcut, X])
22     X = Activation(' relu ')(X)
23  
24     return X
```

- **A.** Ba cặp Conv2D–BatchNorm–ReLU; kết nối tắt ở dòng 8
- **B.** Hai cặp Conv2D–BatchNorm–ReLU; kết nối tắt nằm trong BatchNorm ở dòng 11, 15, 19
- **C.** Ba cặp Conv2D–BatchNorm–ReLU; Không có cơ chế kết nối tắt ở dòng 21
- **D.** Ba cặp Conv2D–BatchNorm–ReLU; kết nối tắt ở dòng 21

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đoạn code định nghĩa khối Bottleneck Residual Block của ResNet:
- Gồm 3 tầng tích chập: $1 \times 1$ nén kênh (dòng 10-12), $f \times f$ học không gian (dòng 14-16), $1 \times 1$ phục hồi kênh (dòng 18-20). Mỗi tầng Conv đều đi kèm BatchNorm và ReLU.
- Đường tắt $X_{\text{shortcut}}$ được lưu lại từ đầu ở dòng 8, sau đó được cộng trực tiếp vào đầu ra của nhánh chính bằng hàm `Add()([X_shortcut, X])` tại dòng 21!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phân tích từng dòng code:
1. Nhánh chính tính hàm $\mathcal{F}(X)$ qua 3 cụm Conv2D-BatchNorm-ReLU:
   - Dòng 10-12: Conv2D(F1) -> BN -> ReLU
   - Dòng 14-16: Conv2D(F2) -> BN -> ReLU
   - Dòng 18-20: Conv2D(F3) -> BN (chưa ReLU)
2. Phép kết nối tắt (Skip Connection Addition):
   - Dòng 21: `X = Add()([X_shortcut, X])` thực hiện phép toán $\mathcal{F}(X) + X$.
   - Dòng 22: Kích hoạt phi tuyến cuối cùng `Activation(' relu ')(X)`.
Do đó, khối gồm ba cụm Conv2D–BatchNorm–ReLU và phép kết nối tắt thực sự được thực hiện tại dòng 21. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nhầm dòng 8 (`X_shortcut = X`) là nơi thực hiện kết nối tắt. Dòng 8 chỉ lưu con trỏ tensor ban đầu, phép cộng thực hiện ở dòng 21.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3 Các Kiến trúc CNN Kinh Điển & §3.4 Skip Connection: ResNet vs U-Net** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 73).

---

### Câu 74 [VOAI25-074] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình Transformer, cơ chếchú ý (attention) giúp ích gì cho quá trình xử lý?

- **A.** Tự động sinh từ tiếp theo một cách tất định mà không cần tầng Softmax
- **B.** Tập trung vào phần quan trọng của câu khi tính toán
- **C.** Xác định thứ tự vị trí tương đối của từng từ trong câu văn bản
- **D.** Chuẩn hóa các vector đặc trưng đầu vào về phân phối có phương sai 1

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cơ chế Attention cho phép mô hình gán trọng số (độquan trọng) khác nhau cho các từ. khác nhau trong câu đầu vào khi xử lý một từ cụthể, giúp nắm bắt mối quan hệ ngữ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Cơ chế Attention cho phép mô hình gán trọng số (độquan trọng) khác nhau cho các từ
khác nhau trong câu đầu vào khi xử lý một từ cụthể, giúp nắm bắt mối quan hệ ngữ
nghĩa bất kểkhoảng cách giữa chúng trong văn bản.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 74). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 75 [VOAI25-075] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong các kiến trúc mạng phân đoạn ảnh dạng bộ mã hóa - bộ giải mã (encoder-decoder), ví dụ như
U-Net, các " kết nối tắt " (skip connections) đóng vai trò quan trọng. Chúng kết hợp thông tin đặc trưng từ các
lớp ở bộ mã hóa (encoder path) với thông tin tương ứng ở bộ giải mã (decoder path) sau khi được phóng đại
(upsampling). Điều này giúp mô hình giữ lại các chi tiết không gian có độ phân giải cao bị mất trong quá trình
mã hóa.
Giả sử bạn đang xây dựng một lớp trong phần bộ giải mã của mạng U-Net bằng Python, sử dụng một
framework học sâu như TensorFlow/Keras hoặc PyTorch. Bạn có hai tensor:
- 𝑒𝑛𝑐𝑜𝑑𝑒𝑟_𝑜𝑢𝑡𝑝𝑢𝑡: Tensor chứa các đặc trưng từ một lớp tương ứng ở bộ mã hóa.

- 𝑑𝑒𝑐𝑜𝑑𝑒𝑟_𝑖𝑛𝑝𝑢𝑡: Tensor đầu vào cho lớp hiện tại ở bộ giải mã, đã được upsample để có cùng kích thước
chiều cao (H) và chiều rộng (W) với 𝑒𝑛𝑐𝑜𝑑𝑒𝑟_𝑜𝑢𝑡𝑝𝑢𝑡.
Thao tác 𝑠𝑜𝑚𝑒_𝑐𝑜𝑛𝑐𝑎𝑡𝑒𝑛𝑎𝑡𝑖𝑜𝑛_𝑜𝑝𝑒𝑟𝑎𝑡𝑖𝑜𝑛 và tham số 𝑎𝑥𝑖𝑠 phù hợp nhất để thực hiện kết nối tắt (skip
connection) kiểu U-Net là gì?

- **A.** Phép nối (Concatenation) và axis dọc theo chiều batch
- **B.** Phép nối (Concatenation) và axis dọc theo chiều kênh (channel dimension)
- **C.** Phép cộng element-wise và axis không quan trọng
- **D.** Phép nhân element-wise và axis không quan trọng

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khác với ResNet (dùng phép cộng - Add), U-Net sử dụng phép nối (Concatenation) để. ghép các đặc trưng từ Encoder sang Decoder nhằm giữ lại thông tin không gian chi tiết.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Khác với ResNet (dùng phép cộng - Add), U-Net sử dụng phép nối (Concatenation) để
ghép các đặc trưng từ Encoder sang Decoder nhằm giữ lại thông tin không gian chi tiết.
Việc nối thường thực hiện trên trục kênh (Channel dimension/Axis 1 trong PyTorch hoặc
Axis 3 trong Keras).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 75). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 76 [VOAI25-076] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình ngôn ngữ lớn (Large Language Model - LLM) là gì?

- **A.** Một hệ thống tìm kiếm thông tin dựa trên tập luật ngữ pháp cố định và cây cú pháp phân cấp
- **B.** Một mô hình học sâu được huấn luyện trên lượng lớn dữ liệu văn bản để dự đoán từ tiếp theo trong một chuỗi
- **C.** Một hệ thống học tăng cường chuyên sâu tối ưu hóa việc phân loại sắc thái tình cảm của các đoạn văn
- **D.** Một cơ sở dữ liệu đồ thị tri thức lưu trữ tường minh các mối quan hệ ngữ nghĩa giữa các thực thể từ

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Định nghĩa cơ bản của LLM (như GPT) là các mô hình xác suất (Probabilistic. Models) dựa trên kiến trúc Transformer, được huấn luyện với mục tiêu " Next Token.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Định nghĩa cơ bản của LLM (như GPT) là các mô hình xác suất (Probabilistic
Models) dựa trên kiến trúc Transformer, được huấn luyện với mục tiêu " Next Token
Prediction "(dự đoán từ tiếp theo) trên tập dữ liệu khổng lồđểhiểu và tạo ra văn bản tự
nhiên.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 76). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 77 [VOAI25-077] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Stable Diffusion thuộc loại mô hình nào trong các lựa chọn sau?

- **A.** Bộ chuyển đổi (Transformer)
- **B.** Mô hình khuếch tán (Diffusion Model)
- **C.** GAN
- **D.** Bộ mã hóa tự động (autoencoder)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Stable Diffusion là một Latent Diffusion Model (LDM). Nó hoạt động bằng cách thêm.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Stable Diffusion là một Latent Diffusion Model (LDM). Nó hoạt động bằng cách thêm
nhiễu dần dần vào ảnh và học cách khôi phục ảnh gốc từ nhiễu (quá trình khuếch tán
ngược).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 77). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 78 [VOAI25-078] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Để áp dụng kỹ thuật dừng sớm (Early Stopping) trong huấn luyện, bạn cần theo dõi chỉ số nào để
quyết định dừng huấn luyện?

- **A.** Mất mát kiểm tra (validation loss) hoặc độ chính xác kiểm tra (validation accuracy)
- **B.** Tốc độ biến thiên của tỷ lệ học (learning rate) theo lịch trình điều chỉnh giảm dần
- **C.** Tổng số lượng chu kỳ huấn luyện (epoch count) đã hoàn thành trên tập dữ liệu mẫu
- **D.** Hàm mất mát huấn luyện (training loss) và độ lớn vector gradient của các tầng ẩn

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Early Stopping theo dõi hiệu suất trên tập Validation (Loss hoặc Accuracy). Nếu chỉ số.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Early Stopping theo dõi hiệu suất trên tập Validation (Loss hoặc Accuracy). Nếu chỉ số
này không cải thiện sau một sốepoch nhất định (patience), quá trình huấn luyện sẽdừng
lại đểtránh Overfitting.

Đáp án chính xác là **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 78). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 79 [VOAI25-079] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Lệnh nào chuyển mô hình sang GPU trong PyTorch?

- **A.** model.gpu()
- **B.** model.to(' cuda ')
- **C.** model.cuda.enable()
- **D.** model.device(' GPU ')

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cú pháp chuẩn trong PyTorch là ‘model. to(device)‘ với device thường là ‘’cuda’‘ hoặc.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Cú pháp chuẩn trong PyTorch là ‘model.to(device)‘ với device thường là ‘’cuda’‘ hoặc
‘’cuda:0’‘. Ngoài ra ‘model.cuda()‘ cũng dùng được nhưng ‘model.to(’cuda’)‘ là cách viết
tổng quát và được khuyên dùng hơn.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 79). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 80 [VOAI25-080] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Hàm chi phí sử dụng MSE (Mean Squared Error) từ dữ liệu sau là bao nhiêu?
- Giá trị kỳ vọng ($y$): $[15, 17, 10, 26, 14, 12, 11, 13]$
- Giá trị thực tế ($\hat{y}$): $[12, 19, 15, 24, 13, 14, 8, 11]$

- **A.** 8.5
- **B.** 6.5
- **C.** 5.5
- **D.** 7.5

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Lấy từng cặp số trừ cho nhau, bình phương hiệu số đó lên, rồi tính trung bình cộng của cả 8 bình phương sai số đó.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Mean Squared Error cho $N = 8$ mẫu:
$$\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$$
Tính từng sai số bình phương $(y_i - \hat{y}_i)^2$:
1. $(15 - 12)^2 = 3^2 = 9$
2. $(17 - 19)^2 = (-2)^2 = 4$
3. $(10 - 15)^2 = (-5)^2 = 25$
4. $(26 - 24)^2 = 2^2 = 4$
5. $(14 - 13)^2 = 1^2 = 1$
6. $(12 - 14)^2 = (-2)^2 = 4$
7. $(11 - 8)^2 = 3^2 = 9$
8. $(13 - 11)^2 = 2^2 = 4$

Tổng các sai số bình phương:
$$\text{SSE} = 9 + 4 + 25 + 4 + 1 + 4 + 9 + 4 = 60$$
Giá trị MSE:
$$\text{MSE} = \frac{60}{8} = \mathbf{7.5}$$
Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Nhầm lẫn chia cho $N-1 = 7$ ($60/7 \approx 8.57$) hoặc tính sai bình phương $(-5)^2 = 25$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát (Loss Functions)** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 80).

---

### Câu 81 [VOAI25-081] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thư viện LangChain được sử dụng để làm gì?

- **A.** Phân tích và biến đổi tín hiệu âm thanh thành đặc trưng phổ Mel (Audio Pipeline Framework)
- **B.** Thực hiện việc dịch thuật tự động chất lượng cao giữa các cặp ngôn ngữ (Machine Translation)
- **C.** Sinh chuỗi văn bản ngẫu nhiên dựa trên các mô hình xác suất Markov (Text Generation Engine)
- **D.** Kết nối và xây dựng quy trình cho tác nhân ngôn ngữ lớn (LLM agent pipeline)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
LangChain là framework phổ biến giúp ghép nối LLM với các nguồn dữ liệu bên ngoài,. bộ nhớ, và các công cụkhác đểxây dựng các ứng dụng phức tạp (Chains/Agents).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
LangChain là framework phổ biến giúp ghép nối LLM với các nguồn dữ liệu bên ngoài,
bộ nhớ, và các công cụkhác đểxây dựng các ứng dụng phức tạp (Chains/Agents).

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 81). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 82 [VOAI25-082] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình hồi quy logistic sử dụng scikit-learn, thuộc tính nào chứa trọng số
đã học của mô hình?

- **A.** model.weights
- **B.** model.intercept
- **C.** model.coefficients
- **D.** model.coef

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Theo quy ước của Scikit-learn, các thuộc tính được học sau khi gọi hàm ‘. fit()‘ sẽcó dấu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Theo quy ước của Scikit-learn, các thuộc tính được học sau khi gọi hàm ‘.fit()‘ sẽcó dấu
gạch dưới ở cuối. Trọng số (hệ số góc) được lưu trong ‘model.coef_‘, còn hệ số chặn là
‘model.intercept_‘.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 82). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 83 [VOAI25-083] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Bạn đang phát triển một hệ thống phân tích ảnh vệ tinh để xác định các loại cây trồng khác nhau trong
một khu vực nông nghiệp rộng lớn. Sau khi tiền xử lý và trích xuất đặc trưng từ ảnh đa phổ, bạn áp dụng một

mô hình phân cụm (clustering) dựa trên thuật toán K-means để phân đoạn các vùng có khả năng chứa cùng
một loại cây trồng.
Giả sử sau khi chạy thuật toán K-means với K=3, bạn thu được ba cụm 𝐶 , 𝐶 , 𝐶 đại diện cho ba loại cây
! " #
trồng tiềm năng. Để đánh giá chất lượng phân cụm, bạn quyết định sử dụng một biến thể của Silhouette
Coefficient.
8(2).&(2)
Silhouette Coefficient cho một điểm dữ liệu 𝑖 được định nghĩa là: 𝑠(𝑖) = , trong đó 𝑎(𝑖) là khoảng
,&7(&(2),8(2))
cách trung bình từ điểm 𝑖 đến tất cả các điểm khác trong cùng cụm. 𝑏(𝑖) là khoảng cách trung bình từ điểm 𝑖
đến tất cả các điểm trong cụm lân cận gần nhất (khác với cụm của 𝑖).
Trong trường hợp đang xét, mỗi pixel trong ảnh sau khi trích xuất đặc trưng có thể được coi là một điểm dữ
liệu trong không gian đặc trưng nhiều chiều. Giả sử bạn chọn ngẫu nhiên một pixel p thuộc cụm 𝐶 . Sau khi
!
tính toán, bạn có các giá trị sau:
- Khoảng cách trung bình từ pixel p đến tất cả các pixel khác trong cụm 𝐶 là 𝑎(𝑝) = 0.35.
!
- Khoảng cách trung bình từ pixel p đến tất cả các pixel trong cụm 𝐶 là 𝑑(𝑝,𝐶 ) = 0.60.
" "
- Khoảng cách trung bình từ pixel p đến tất cả các pixel trong cụm 𝐶 là 𝑑(𝑝,𝐶 ) = 0.45.
# #
Biết rằng 𝑏(𝑝) là khoảng cách trung bình nhỏ nhất từ pixel 𝑝 đến các điểm trong một cụm khác với cụm chứa
𝑝. Hãy tính Silhouette Coefficient 𝑠(𝑝) cho pixel 𝑝.

- **A.** 0.0
- **B.** 0.222
- **C.** 0.125.
- **D.** 0.308

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
b(p) là khoảng cách trung bình nhỏ nhất đến cụm khác →b(p) = min(0. Công thức: s(p) =.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
b(p) là khoảng cách trung bình nhỏ nhất đến cụm khác →b(p) = min(0.60, 0.45) = 0.45.
Công thức: s(p) =
b(p)−a(p)
max(a(p), b(p)). s(p) =
0.45−0.35
max(0.35,0.45) = 0.10
0.45 = 2
9 ≈0.2222...

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.8** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 83). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 84 [VOAI25-084] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Nếu khởi tạo trọng số (weight initialization) không phù hợp, hiện tượng nào có thể xảy ra trong quá
trình huấn luyện?

- **A.** Mô hình học nhanh hơn
- **B.** Không ảnh hưởng vì bộ tối ưu sẽ điều chỉnh
- **C.** Học quá mức nhẹ (overfitting)
- **D.** Gradient biến mất (vanishing) hoặc nổ (exploding)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu trọng số khởi tạo quá nhỏ, tín hiệu qua nhiều lớp sẽgiảm dần về0 (Vanishing. Gradient).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Nếu trọng số khởi tạo quá nhỏ, tín hiệu qua nhiều lớp sẽgiảm dần về0 (Vanishing
Gradient). Nếu quá lớn, tín hiệu sẽtăng theo cấp số nhân (Exploding Gradient), làm
trọng số thay đổi quá mạnh và khiến mô hình không thểhội tụ. Các kỹ thuật như Xavier
(Glorot) hay Kaiming Initialization được thiết kếđểgiữ cho phương sai của tín hiệu ổn
định qua các lớp.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§5.2** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 84). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 85 [VOAI25-085] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Để đánh giá mô hình phân loại ảnh với các lớp không cân bằng, chỉ số nào nên dùng thay vì chỉ độ
chính xác (accuracy)?

- **A.** AUC (Area Under the Curve)
- **B.** Điểm F1 trung bình (Macro F1-score)
- **C.** RMSE (Root mean square error)
- **D.** Độ chính xác cao nhất (Top-1 accuracy)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Accuracy dễgây hiểu lầm với dữ liệu mất cân bằng (ví dụ99% mẫu thuộc lớp A thì. model luôn đoán A cũng được 99% acc).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Accuracy dễgây hiểu lầm với dữ liệu mất cân bằng (ví dụ99% mẫu thuộc lớp A thì
model luôn đoán A cũng được 99% acc). Macro F1-score tính F1 cho từng lớp rồi lấy
trung bình, do đó nó coi trọng các lớp thiểu số ngang hàng với lớp đa số, phản ánh đúng
hiệu suất hơn.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.7** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 85). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 86 [VOAI25-086] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Sau khi huấn luyện mô hình phân loại với độ chính xác 90%, khách hàng muốn triển khai thực tế.
Việc cần làm tiếp theo là gì?

- **A.** Nén ảnh đầu vào
- **B.** Chuyển mô hình sang TensorRT/ONNX để triển khai (deploy)
- **C.** Tăng thêm số vòng lặp (epoch) để đạt 95%
- **D.** Thay mô hình sang BERT

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đểtối ưu hóa tốc độvà khả năng tương thích khi triển khai (Deployment), bước tiêu. chuẩn là convert mô hình sang các định dạng trung gian tối ưu như ONNX hoặc dùng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đểtối ưu hóa tốc độvà khả năng tương thích khi triển khai (Deployment), bước tiêu
chuẩn là convert mô hình sang các định dạng trung gian tối ưu như ONNX hoặc dùng
engine chuyên dụng như TensorRT (cho NVIDIA GPU) đểtăng tốc suy luận (inference).

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 86). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 87 [VOAI25-087] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi xử lý dữ liệu ảnh, nếu một số ảnh bị hỏng (không mở được), cách tốt nhất để xử lý khi huấn luyện
là gì?

- **A.** Tăng kích thước lô (batch size) để bù lại
- **B.** Bỏ qua toàn bộ thư mục chứa ảnh đó
- **C.** Bắt lỗi khi tải ảnh và bỏ qua ảnh bị hỏng
- **D.** Dừng toàn bộ huấn luyện

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Dừng huấn luyện hay bỏ qua cả thư mục là lãng phí tài nguyên và dữ liệu. Cách xử lý.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Dừng huấn luyện hay bỏ qua cả thư mục là lãng phí tài nguyên và dữ liệu. Cách xử lý
tối ưu trong Data Loader (ví dụphương thức __getitem__ trong PyTorch) là sử dụng
cấu trúc try-except đểbắt lỗi khi đọc file. Nếu phát hiện ảnh lỗi, chương trình sẽbỏ
qua và lấy ảnh tiếp theo hoặc trảvề giá trị None đểhàm collate_fn xử lý, giúp quá
trình huấn luyện diễn ra liên tục.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 87). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 88 [VOAI25-088] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong PyTorch, để thêm lớp bỏ ngẫu nhiên (dropout) với xác suất 0.5 vào mạng nơ-ron, bạn sử dụng
lệnh nào?

- **A.** F.dropout(0.5)
- **B.** nn.dropout(0.5)
- **C.** nn. Dropout(p=0.5)
- **D.** nn. Dropout2d(0.5)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Đểthêm một lớp (Layer) vào mô hình (ví dụtrong ‘nn. Sequential‘), ta dùng class.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Đểthêm một lớp (Layer) vào mô hình (ví dụtrong ‘nn. Sequential‘), ta dùng class
‘nn. Dropout‘ (viết hoa chữ D) và tham số‘p=0.5‘. ‘F.dropout‘ là dạng hàm (functional),
‘nn. Dropout2d‘ dùng cho đặc trưng không gian (như sau Conv2D), ‘nn.dropout‘ (viết
thường) thường không phải tên class chuẩn.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.9** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 88). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 89 [VOAI25-089] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Hãy xem xét một công cụ phát hiện các gói tin chứa mối đe dọa trong trường hợp chỉ có một số lượng
nhỏ gói là mối đe dọa. Yêu cầu là công cụ cần phát hiện các gói đe dọa mà không bỏ sót gói nào. Đâu là độ
đo quan trọng nhất để đánh giá công cụ?

- **A.** Accuracy
- **B.** F1
- **C.** Recall
- **D.** Precision

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
" Không bỏ sót " nghĩa là muốn tối thiểu hóa False Negative (báo sót). Chỉ số đo lường.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
" Không bỏ sót " nghĩa là muốn tối thiểu hóa False Negative (báo sót). Chỉ số đo lường
khả năng tìm ra tất cả các mẫu dương tính là Recall (Độphủ). Chấp nhận nhầm (False
Positive) còn hơn bỏ sót.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.7** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 89). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 90 [VOAI25-090] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp nào dưới đây mà việc chuẩn hóa các thuộc tính dữ liệu đầu vào không ảnh hưởng đến
kết quả dự đoán?

- **A.** Mạng nơ-ron (Neural Networks)
- **B.** Cây quyết định
- **C.** Soft-margin SVM
- **D.** k-NN

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cây quyết định hoạt động dựa trên các luật ‘if feature > threshold‘. Việc nhân đặc trưng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Cây quyết định hoạt động dựa trên các luật ‘if feature > threshold‘. Việc nhân đặc trưng
với một hằng số (scaling) chỉ làm thay đổi giá trịthreshold tương ứng, chứkhông thay
đổi cấu trúc cây hay kết quảphân loại. Các thuật toán còn lại đều dựa trên khoảng cách
hoặc tích vô hướng nên rất nhạy cảm với chuẩn hóa.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 90). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 91 [VOAI25-091] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mục tiêu huấn luyện của mô hình CBOW (Continuous Bag-of-Words) là gì?

- **A.** Sử dụng toàn bộ văn bản để dự đoán một từ bất kỳ
- **B.** Sử dụng vị trí của từ trong câu để dự đoán nghĩa của câu
- **C.** Sử dụng các từ xung quanh để dự đoán từ trung tâm
- **D.** Sử dụng từ trung tâm để dự đoán các từ xung quanh

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
CBOW (Continuous Bag of Words): Input là ngữ cảnh (các từ xung quanh), Output là. từ ở giữa (Center word).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
CBOW (Continuous Bag of Words): Input là ngữ cảnh (các từ xung quanh), Output là
từ ở giữa (Center word). (Ngược lại, đáp án D là mô hình Skip-gram).

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 91). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 92 [VOAI25-092] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mục tiêu chính của phương pháp học tương phản (contrastive learning) trong lĩnh vực học tự giám
sát (self-supervised learning) là gì?

- **A.** Tối thiểu hóa khoảng cách Euclid giữa mọi cặp ảnh trong cùng một lô (mini-batch clustering) bất kể nguồn gốc nhằm gom cụm dữ liệu về tâm phân phối chung
- **B.** Khôi phục lại bức ảnh gốc ban đầu từ bức ảnh đã bị thêm nhiễu Gauss ngẫu nhiên (denoising autoencoder) thông qua hàm mất mát sai số toàn phương trung bình MSE
- **C.** Đưa các ảnh được biến đổi từ cùng một ảnh gốc thông qua các phép biến đổi cơ bản tới gần nhau, đẩy các mẫu lấy từ các ảnh khác nhau xa nhau trên không gian biểu diễn (embedding space)
- **D.** Tối ưu hóa hàm mất mát Cross-Entropy có giám sát đầy đủ (supervised multiclass loss) dựa trên tập nhãn phân loại thủ công nhằm phân định ranh giới quyết định

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nguyên lý của Contrastive Learning (ví dụ SimCLR): Kéo các view khác nhau. (augmented views) của cùng một mẫu (Positive pair) lại gần nhau trong không gian.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Nguyên lý của Contrastive Learning (ví dụ SimCLR): Kéo các view khác nhau
(augmented views) của cùng một mẫu (Positive pair) lại gần nhau trong không gian
embedding, đồng thời đẩy xa các view của các mẫu khác (Negative pairs).

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 92). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 93 [VOAI25-093] — Phân hệ Module A (Thang điểm: 1.0đ)

**Đề bài:** Điểm khác biệt chính giữa Stochastic Gradient Descent (SGD) và Mini-Batch Gradient Descent là
gì?

- **A.** SGD luôn hội tụ nhanh hơn
- **B.** Mini-Batch Gradient Descent là một thuật toán hoàn toàn khác
- **C.** SGD không dùng được trong mạng nơ-ron
- **D.** SGD cập nhật tham số sau mỗi mẫu dữ liệu, Mini-Batch thì sau một nhóm mẫu

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
SGD chuẩn: Cập nhật trọng số sau mỗi 1 mẫu dữ liệu (Batch size = 1). Mini-Batch GD:.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
SGD chuẩn: Cập nhật trọng số sau mỗi 1 mẫu dữ liệu (Batch size = 1). Mini-Batch GD:
Cập nhật sau khi tính toán trên một lô nhỏ (ví dụ32, 64 mẫu). Đây là phương pháp phổ
biến nhất hiện nay vì cân bằng được giữa tốc độtính toán và sựổn định của gradient.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 93). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 94 [VOAI25-094] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Giả sử các từ được biểu diễn bởi các vector 4 chiều như sau:
w1 = [0.8, 0.6, 0.0, 0.2]
w2 = [0.9, 0.5, 0.1, 0.3]
w3 = [1.0, 0.1, 0.0, 0.0]
w4 = [0.0, 0.1, 0.9, 0.3]
Hãy tính độ tương đồng cosine giữa w1 và các từ còn lại (w2, w3, w4), sau đó chọn từ gần nhất với w1.
Công thức tính cosine similarity giữa hai vector A và B là:
9⋅;
𝑐𝑜𝑠𝑖𝑛𝑒−𝑠𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦(𝐴,𝐵) = ( )
|9|×|;|
Với: 𝐴⋅𝐵 là tích vô hướng giữa hai vector, |𝐴| là độ dài của vector A, tính bằng căn bậc hai tổng bình phương
các thành phần

- **A.** Có nhiều hơn một từ gần nhất với w1
- **B.** w3
- **C.** w4
- **D.** w2

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
cosine-similarity(A, B) =. • Với w2: Vector w2 rất giống w1 về phân bổ trọng số ở các chiều (đều tập trung lớn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Để
tìm
từ
gần
nhất,
ta
tính
độ
tương
đồng
cosine
theo
công
thức:
cosine-similarity(A, B) =
A·B
∥A∥∥B∥.
• Với w2: Vector w2 rất giống w1 về phân bổ trọng số ở các chiều (đều tập trung lớn
ở chiều 1 và 2). Kết quảtính toán cho thấy cosine similarity ≈0.983, rất gần 1.
• Với w3: Chỉ tương đồng ở chiều thứnhất, các chiều còn lại lệch đáng kể. Cosine
similarity thấp hơn (≈0.839).
• Với w4: Hầu như khác biệt hoàn toàn vì w4 tập trung giá trịở chiều thứ3, trong
khi w1 bằng 0 ở chiều này. Cosine similarity rất thấp (≈0.123).
→Vậy w2 là vector gần nhất với w1.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.3** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 94). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 95 [VOAI25-095] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mạng GAN bao gồm hai mạng chính nào?

- **A.** Bộ phát hiện (Detector) và Bộ phân đoạn (Segmentor)
- **B.** Bộ chuyển đổi (Transformer) và Cơ chế chú ý (Attention)
- **C.** Bộ mã hóa (Encoder) và Bộ giải mã (Decoder)
- **D.** Bộ tạo (Generator) và Bộ phân biệt (Discriminator)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Kiến trúc Generative Adversarial Networks (GAN) gồm hai mạng đối nghịch: Generator. cố gắng sinh dữ liệu giả giống thật, và Discriminator cố gắng phân biệt đâu là thật, đâu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Kiến trúc Generative Adversarial Networks (GAN) gồm hai mạng đối nghịch: Generator
cố gắng sinh dữ liệu giả giống thật, và Discriminator cố gắng phân biệt đâu là thật, đâu
là giả.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 95). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 96 [VOAI25-096] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Quá khớp (Overfitting) có thểdo?

- **A.** Lựa chọn mô hình không phù hợp
- **B.** Độ phức tạp của bài toán học
- **C.** Một lỗi nào đó trong quá trình huấn luyện
- **D.** Nhiễu trong dữ liệu

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Ngoài lý do mô hình quá phức tạp, Nhiễu (Noise) trong dữ liệu là nguyên nhân lớn gây. Overfitting.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Ngoài lý do mô hình quá phức tạp, Nhiễu (Noise) trong dữ liệu là nguyên nhân lớn gây
Overfitting. Mô hình sẽcố gắng " học " cả những điểm nhiễu này (coi chúng là quy luật
đúng), dẫn đến khả năng tổng quát hóa kém trên dữ liệu sạch hoặc dữ liệu mới.

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 96). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 97 [VOAI25-097] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi huấn luyện bộ mã hóa tự động (Autoencoder), nếu ảnh đầu ra bị mờ (blurry), nguyên nhân chủ yếu có thểlà gì?

- **A.** Tỷ lệ bỏ ngẫu nhiên (dropout rate) được thiết lập ở mức quá thấp trong toàn bộ mạng
- **B.** Bộ tối ưu hóa được cấu hình sai thông số dẫn đến hiện tượng dao động gradient mạnh
- **C.** Lớp ẩn quá nhỏ hoặc chính quy hóa (regularization) quá mạnh
- **D.** Kích thước lô huấn luyện (batch size) quá lớn làm suy giảm tốc độ cập nhật trọng số

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu lớp ẩn (Latent space/Bottleneck) quá nhỏ, thông tin chi tiết về đặc trưng không. gian bị mất đi trong quá trình nén (compression).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Nếu lớp ẩn (Latent space/Bottleneck) quá nhỏ, thông tin chi tiết về đặc trưng không
gian bị mất đi trong quá trình nén (compression). Bên cạnh đó, việc sử dụng hàm loss
MSE (Mean Squared Error) có xu hướng cực tiểu hóa sai số bằng cách tính trung bình
các pixel khả thi, dẫn đến hiện tượng ảnh bị " mờ " hóa thay vì giữ được độsắc nét như
khi sử dụng các mô hình sinh đối kháng (GAN).

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§2.4** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 97). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 98 [VOAI25-098] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình DALL·E có khả năng đặc biệt nào?

- **A.** Phân đoạn vật thể
- **B.** Sinh ảnh từ mô tả văn bản
- **C.** Nén ảnh thành vector
- **D.** Sinh mô tả từ ảnh

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
DALL-E (của OpenAI) là mô hình Text-to-Image nổi tiếng, sử dụng kiến trúc Transformer. hoặc Diffusion (tùy phiên bản) đểtạo ra hình ảnh kỹ thuật số chất lượng cao từ các gợi.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
DALL-E (của OpenAI) là mô hình Text-to-Image nổi tiếng, sử dụng kiến trúc Transformer
hoặc Diffusion (tùy phiên bản) đểtạo ra hình ảnh kỹ thuật số chất lượng cao từ các gợi
ý văn bản (prompts) bằng ngôn ngữtự nhiên.

Đáp án chính xác là **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.5** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 98). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 99 [VOAI25-099] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong xử lý ngôn ngữ tự nhiên (NLP), mục đích chính của việc loại bỏ từ dừng (stopword) khỏi văn
bản là gì?

- **A.** Để giảm bớt số lượng mẫu dữ liệu câu văn bản cần xử lý trong toàn bộ tập huấn luyện
- **B.** Để tự động tái cấu trúc câu văn bản giúp các phát biểu trở nên hoàn chỉnh mạch lạc
- **C.** Để làm giảm độ phức tạp và tập trung vào các từ mang nội dung quan trọng
- **D.** Để giữ lại tất cả các từ vựng chức năng phục vụ cho các thuật toán so khớp chính xác

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Từ dừng (stopwords) như " thì ", " là ", " của ", " the ", " is ". xuất hiện rất nhiều nhưng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
Từ dừng (stopwords) như " thì ", " là ", " của ", " the ", " is "... xuất hiện rất nhiều nhưng
mang ít ý nghĩa ngữnghĩa đặc trưng. Loại bỏ chúng giúp giảm kích thước dữ liệu (vốn
từ vựng), giảm nhiễu và giúp các mô hình (như TF-IDF hoặc phân loại văn bản) tập
trung vào những từ thực sự mang giá trịnội dung.

Đáp án chính xác là **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Cần chú ý đọc kỹ các giả định đầu vào của bài toán (chuẩn hóa dữ liệu, chiều tensor, hàm mục tiêu). Các phương án gây nhiễu thường đưa ra khái niệm gần đúng nhưng sai phạm vi áp dụng thực tế.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.1** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 99). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---

### Câu 100 [VOAI25-100] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Cho các tham số của mô hình SVM (support vector machine) đã huấn luyện và bảng dữ liệu dưới
đây, dự đoán cho chỉ số 0 là gì?
Vector trọng số: 𝑤 = [2,−3] Độ lệch: 𝑏 = 1
Chỉ số X1 X2
0 1 2
1 -1 -1
2 -1 2
3 4 5

- **A.** không xác định được
- **B.** không phân loại
- **C.** +1
- **D.** -1 ----HẾT---

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Hàm quyết định của mô hình SVM tuyến tính phân lớp dựa trên dấu của biểu thức $f(x) = \mathbf{w} \cdot \mathbf{x} + b$. Nếu $f(x) \ge 0$ thì phân loại $+1$, nếu $f(x) < 0$ thì phân loại $-1$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 **Phân tích cơ sở lý thuyết & suy luận:**
- **Công thức hàm quyết định SVM:**
  $$f(\mathbf{x}) = \mathbf{w} \cdot \mathbf{x} + b$$

- **Thay số với $\mathbf{w} = [2, -3]$, $b = 1$, và điểm dữ liệu $\mathbf{x} = [1, 2]$:**
  $$f(\mathbf{x}) = (2 \times 1) + (-3 \times 2) + 1 = 2 - 6 + 1 = -3$$

- **Kết luận phân lớp:**
  Vì $f(\mathbf{x}) = -3 < 0$, theo quy tắc hàm dấu (sign function) của SVM, nhãn dự đoán là **$-1$**.

**Đáp án chính xác là D.**

Đáp án chính xác là **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy cần tránh:**
Tránh nhầm lẫn thứ tự tọa độ $X_1$ và $X_2$ hoặc quên cộng hằng số độ lệch bias $b = 1$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§1.2** trong Cẩm nang Giáo trình OLP AI 2026.
🔗 **Nguồn gốc câu hỏi:** Đề thi chính thức Olympic Trí tuệ nhân tạo Quốc gia VOAI 2025 (Mã đề 006, Câu 100). Lời giải đối chiếu học thuật từ tác giả Nguyễn Khắc Trung Kiên.

---
