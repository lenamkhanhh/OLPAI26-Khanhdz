# ĐỀ THI 05: NGÂN HÀNG CHUYÊN ĐỀ THỰC CHIẾN CV & NLP (90 CÂU - SKILLPIXEL)
## 35 Câu NLP & Dịch Máy + 55 Câu Computer Vision & CNN Kiến Trúc SOTA (90.0đ)

> **Nguồn gốc học thuật:** Tuyển tập 90 câu hỏi trắc nghiệm chuyên sâu từ ngân hàng đề SkillPixel Quizzes kết hợp hệ thống slide bài giảng Buổi 1, 2, 5, 6, 9.
> **Mục tiêu:** Củng cố toàn diện kiến thức biểu diễn từ (Word Representations §4.2), Attention, Transformer, ResNet, ViT, YOLO và các kiến trúc Deep Learning cốt lõi.

---

### Câu 01 [SKILL-NLP-01] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** FastText cải thiện đáng kể biểu diễn nhúng từ (word embeddings) so với Word2Vec
cổ điển nhờ vào yếu tố bổ sung nào?

- **A.** Áp dụng thuật toán BPE dựa trên tần suất cặp byte ký tự để phân tách từ vựng thành các mảnh subword tokens
- **B.** Sử dụng từ điển từ đơn cố định kết hợp giải thuật tìm kiếm từ dài nhất cực đại (MaxMatch) từ trái sang phải
- **C.** Phân chia văn bản thuần túy theo dấu cách (whitespace) và các dấu chấm câu chuẩn mực bằng các biểu thức chính quy
- **D.** Huấn luyện mạng nơ-ron hồi quy hai chiều (Bi-LSTM) để dự đoán nhãn phân tách ranh giới từ vựng trên chuỗi văn bản

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Nhờ chia nhỏ từ thành các N-grams ký tự (ví dụ: ” apple” →” app”, ” ppl”, ” ple”), FastText học được cấu trúc hình thái của từ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Nhờ chia nhỏ từ thành các N-grams ký tự (ví dụ: ” apple” →” app”, ” ppl”, ” ple”), FastText học được cấu trúc hình thái của từ.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

---

### Câu 02 [SKILL-NLP-02] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mục tiêu huấn luyện tiền huấn luyện ” Masked Language Modeling” (MLM) trong
BERT được định nghĩa như thế nào?

- **A.** Mô hình RoBERTa loại bỏ tác vụ NSP và sử dụng cơ chế mặt nạ động (Dynamic Masking) với kích thước batch cực lớn
- **B.** Mô hình BERT truyền thống đã đạt đến giới hạn hội tụ toán học tối ưu tuyệt đối trên mọi bộ dữ liệu thử nghiệm
- **C.** Mô hình RoBERTa giảm bớt một nửa số lượng tham số để tăng tốc độ suy luận thời gian thực trên các thiết bị di động
- **D.** Mô hình BERT không thể huấn luyện song song trên phần cứng đa GPU do cấu trúc liên kết phân tán bị phân mảnh

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Cơ chế Bidirectional (2 chiều) này khác biệt hoàn toàn với mô hình sinh tự hồi quy của GPT (chỉ nhìn bên trái).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Cơ chế Bidirectional (2 chiều) này khác biệt hoàn toàn với mô hình sinh tự hồi quy của GPT (chỉ nhìn bên trái).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 03 [SKILL-NLP-03] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Độ đo Perplexity trong mô hình ngôn ngữ (Language Modeling) thểhiện điều gì?

- **A.** Cơ chế chú ý đa đầu (Multi-Head Attention) kết hợp với các tầng nơ-ron truyền thẳng (Feed-Forward Network)
- **B.** Cơ chế chuẩn hóa lớp (Layer Normalization) đặt trước và sau các kết nối tắt phần dư (Residual Connections)
- **C.** Phép mã hóa vị trí tuyệt đối dạng hàm sin-cos (Sinusoidal Positional Encoding) cộng trực tiếp vào vector nhúng
- **D.** Tầng tích chập không gian 1D (Temporal Convolution) kết hợp cơ chế lấy mẫu cực đại dọc theo chiều chuỗi

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Perplexity tỷ lệnghịch với xác suất gán cho chuỗi kiểm tra.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `B`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Perplexity tỷ lệnghịch với xác suất gán cho chuỗi kiểm tra. Mô hình ngôn ngữxịn sẽdự đoán từ tiếp theo cực kỳtự tin, do đó bối rối thấp.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 04 [SKILL-NLP-04] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật ” Teacher Forcing” được sử dụng trong huấn luyện kiến trúc Encoder-
Decoder (ví dụ Seq2Seq dịch máy) nghĩa là gì?

- **A.** Mô hình Word2Vec gán nhãn tĩnh cho từ vựng, không thể phân biệt được đa nghĩa ngữ cảnh (Polysemy) của từ
- **B.** Mô hình Word2Vec có kích thước ma trận trọng số quá lớn khiến bộ nhớ đệm RAM của máy chủ bị tràn bộ nhớ
- **C.** Mô hình Word2Vec chỉ áp dụng được cho ngữ liệu tiếng Anh và hoàn toàn không thể mở rộng sang các ngôn ngữ khác
- **D.** Mô hình Word2Vec đòi hỏi phần cứng GPU chuyên dụng để tính toán và không thể chạy được trên các CPU thông thường

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Teacher Forcing giúp quá trình huấn luyện hội tụcực nhanh và ổn định bằng cách ngăn lỗi dây chuyền từ các bước sinh văn bản đầu tiên bị sai.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `B`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Teacher Forcing giúp quá trình huấn luyện hội tụcực nhanh và ổn định bằng cách ngăn lỗi dây chuyền từ các bước sinh văn bản đầu tiên bị sai.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 05 [SKILL-NLP-05] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Tại sao dòng kiến trúc GPT (Generative Pre-trained Transformer) lại sử dụng ” Cơ
chếchú ý bị che lấp” (Masked Self-Attention) trong Decoder?

- **A.** Đóng băng toàn bộ trọng số gốc và chỉ cập nhật các ma trận hạng thấp bổ sung (Low-Rank Adaptation Matrices)
- **B.** Cắt tỉa vĩnh viễn 80% số tầng nơ-ron trong khối giải mã để giảm chi phí bộ nhớ VRAM trong quá trình huấn luyện
- **C.** Chuyển toàn bộ các phép toán nhân ma trận sang miền tần số Fourier để giảm độ phức tạp tính toán thuật toán
- **D.** Huấn luyện lại toàn bộ hàng tỷ tham số của mô hình từ đầu trên tập dữ liệu đặc thù của miền ứng dụng mới

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Trong quá trình sinh văn bản, mô hình chỉ được dùng quá khứđểdự đoán tương lai.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Trong quá trình sinh văn bản, mô hình chỉ được dùng quá khứđểdự đoán tương lai. Attention Mask sẽép trọng số chú ý với từ tương lai bằng 0 (vô cực âm trước softmax).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 06 [SKILL-NLP-06] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Cấu trúc Tokenizer phổ biến nhất được sử dụng bởi các mô hình như GPT và LLaMA,
chuyên xử lý việc cân bằng giữa ký tự đơn và từ nguyên vẹn là gì?

- **A.** BPE (Byte Pair Encoding) hoặc SentencePiece (Subword tokenization).
- **B.** Hashing Trick đểánh xạmọi cụm từ về một không gian vector cố định.
- **C.** Word-Level Tokenizer kết hợp với stemming tự động.
- **D.** POS-tagging Tokenizer (tách từ và gán nhãn từ loại đồng thời).

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Subword tokenizers thống kê các cụm ký tự xuất hiện thường xuyên nhất để ghép lại thành token.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Subword tokenizers thống kê các cụm ký tự xuất hiện thường xuyên nhất để ghép lại thành token. Nó giúp từ điển nhỏ gọn gọn nhưng vẫn biểu diễn được mọi từ hiếm (chia thành sub-word).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 07 [SKILL-NLP-07] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Độ đo BLEU (Bilingual Evaluation Understudy) được thiết kếvà sử dụng phổ biến
nhất đểđánh giá hiệu suất của tác vụ NLP nào?

- **A.** Rút trích quan hệ thực thể (Relation Extraction).
- **B.** Dịch máy (Machine Translation).
- **C.** Tóm tắt văn bản (Text Summarization) ở mức độdiễn giải (Abstractive).
- **D.** Sinh văn bản sáng tạo (Creative Text Generation) dựa trên tiền tố.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: BLEU đếm sự trùng khớp của các n-gram giữa câu dự đoán của máy và một (hoặc nhiều) câu tham chiếu do con người dịch, đồng thời áp dụng hình phạt (Brevity Penalty) nếu máy dịch quá ngắn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `B`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: BLEU đếm sự trùng khớp của các n-gram giữa câu dự đoán của máy và một (hoặc nhiều) câu tham chiếu do con người dịch, đồng thời áp dụng hình phạt (Brevity Penalty) nếu máy dịch quá ngắn.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 08 [SKILL-NLP-08] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật trích xuất đặc trưng TF-IDF (Term Frequency-Inverse Document Frequency)
đánh giá tầm quan trọng của một từ cụthểtrong một tài liệu dựa trên nguyên tắc
kép nào?

- **A.** Khả năng mở rộng kích thước cửa sổ ngữ cảnh lên hàng triệu token mà không làm suy giảm chất lượng biểu diễn
- **B.** Hiện tượng mô hình chú ý nhiều hơn vào thông tin ở đầu và cuối ngữ cảnh, bỏ sót thông tin ở giữa (Lost in the Middle)
- **C.** Hiện tượng bùng nổ gradient khi độ dài chuỗi đầu vào vượt quá ngưỡng dung sai phân bổ của phần cứng bộ nhớ
- **D.** Cơ chế phân tách ngẫu nhiên các câu văn bản dài thành các đoạn nhỏ độc lập làm mất liên kết ngữ nghĩa toàn cục

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Một từ quan trọng và mang ý nghĩa đặc trưng (ví dụ: ” AI”, ” Olympiad”) phải xuất hiện nhiều trong văn bản đó, nhưng không phải là các từ quá phổ biến (như ” và”, ” là”, ” thì” - sẽbịgiảm IDF về0).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Một từ quan trọng và mang ý nghĩa đặc trưng (ví dụ: ” AI”, ” Olympiad”) phải xuất hiện nhiều trong văn bản đó, nhưng không phải là các từ quá phổ biến (như ” và”, ” là”, ” thì” - sẽbịgiảm IDF về0).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 09 [SKILL-NLP-09] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Lý do kiến trúc của BERT không phù hợp đểtriển khai các hệ thống sinh văn bản tự
động từ trái sang phải (như ChatGPT) là gì?

- **A.** Giảm độ trễ suy luận thời gian thực bằng cách chỉ tính toán ma trận Attention trên các token có độ bất định cao
- **B.** Ổn định phân phối gradient và chống hiện tượng bùng nổ kích hoạt khi huấn luyện các mô hình cực sâu (Deep Networks)
- **C.** Loại bỏ hoàn toàn sự cần thiết của các vector nhúng vị trí tương đối thông qua cơ chế chuẩn hóa động thích nghi
- **D.** Tăng tốc độ đọc ghi dữ liệu từ bộ nhớ HBM sang bộ nhớ SRAM siêu tốc trên các thế hệ chip gia tốc đồ họa mới

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Vì BERT (Encoder-only) trong lúc huấn luyện luôn ” nhìn thấy” toàn bộ câu cùng lúc.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Vì BERT (Encoder-only) trong lúc huấn luyện luôn ” nhìn thấy” toàn bộ câu cùng lúc. Việc sinh tuần tự yêu cầu Decoder-only (GPT) đểche lấp phần tương lai chưa được sinh ra.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 10 [SKILL-NLP-10] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Đối với các mô hình ngữnghĩa văn bản (Text Encoders) như Sentence-BERT, kỹ
thuật nào được áp dụng lên danh sách các token embeddings đầu ra để thu được
một vector duy nhất đại diện cho ngữnghĩa của TOÀN BỘ câu?

- **A.** Mô hình T5 chuyển đổi mọi tác vụ học máy thành bài toán văn bản sang văn bản (Text-to-Text Framework) thống nhất
- **B.** Mô hình T5 sử dụng một đầu phân loại Softmax đa nhãn cố định (Fixed Multiclass Head) cho toàn bộ các bài toán
- **C.** Mô hình T5 chỉ áp dụng được riêng cho bài toán dịch máy tự động (Machine Translation Only) giữa các cặp ngôn ngữ
- **D.** Mô hình T5 thay thế toàn bộ khối Attention bằng các mạng tích chập 1D (Pure 1D-CNN Architecture) để tăng tốc độ

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Vì mỗi token xuất ra một vector riêng, phép toán Mean Pooling sẽtính trung bình các vector này thành một vector duy nhất có cùng số chiều, tạo thành ” Sentence Embedding”.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Vì mỗi token xuất ra một vector riêng, phép toán Mean Pooling sẽtính trung bình các vector này thành một vector duy nhất có cùng số chiều, tạo thành ” Sentence Embedding”.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.1 Pipeline Tiền Xử Lý Văn Bản Chuẩn**.

---

### Câu 11 [SKILL-NLP-11] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Byte-Pair Encoding (BPE), thuật toán mã hóa từ (Tokenization) mặc định của GPT,
xử lý các từ hiếm (Out-Of-Vocabulary) vô cùng khéo léo bằng cách nào?

- **A.** Chia từ hiếm đó ra thành các token nhỏ hơn (Subwords) hoặc từng ký tự gốc, đảm bảo mọi từ đều biểu diễn được từ các thành phần ghép lại
- **B.** Thay thế từ hiếm bằng vector trung bình của các từ lân cận trong ngữ cảnh câu (Contextual Mean Vector) nhằm bảo toàn tính trơn của không gian
- **C.** Sử dụng khoảng cách Levenshtein (Levenshtein Distance) để sửa lỗi và quy chuẩn từ hiếm về từ vựng phổ biến nhất có trong từ điển chuẩn
- **D.** Tạo một bảng băm ánh xạ ngẫu nhiên (Hash-Mapping Table) để phân bổ các từ nằm ngoài tập dữ liệu huấn luyện vào các vector nhúng mặc định

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Thay vì thất bại khi gặp từ lạ, BPE (và các thuật toán subword khác) đảm bảo ” zero OOV” bằng cách fallback dần xuống cấp độchữcái.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Thay vì thất bại khi gặp từ lạ, BPE (và các thuật toán subword khác) đảm bảo ” zero OOV” bằng cách fallback dần xuống cấp độchữcái.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 12 [SKILL-NLP-12] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi đánh giá chất lượng của hệ thống Tóm tắt văn bản (Text Summarization), độ
đo ROUGE chủ yếu đo lường khía cạnh nào so với độ đo BLEU của dịch máy?

- **A.** ROUGE đo lường sự tương đồng về vector nhúng ngữ nghĩa (Semantic Embedding Similarity) giữa các câu tóm tắt thay vì so khớp từ vựng
- **B.** ROUGE đo lường mức độ liền mạch và tính liên kết ngữ pháp (Grammatical Coherence Index) của văn bản tóm tắt dựa trên mô hình ngôn ngữ
- **C.** ROUGE chủ yếu đo lường độ phủ thông tin (Recall Metric) - tức là tỷ lệ các n-gram từ bản tóm tắt chuẩn xuất hiện trong câu mô hình sinh ra
- **D.** ROUGE áp dụng hệ số phạt độ dài nghiêm ngặt (Brevity Penalty Factor) nếu bản tóm tắt có quá nhiều từ thừa so với văn bản gốc ban đầu

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Trong tóm tắt, việc ” không bỏ sót thông tin quan trọng” (Recall) quan trọng hơn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Trong tóm tắt, việc ” không bỏ sót thông tin quan trọng” (Recall) quan trọng hơn. Nếu máy sinh ra một bản tóm tắt dài dòng nhưng chứa đủý chính, ROUGE vẫn đánh giá cao.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 13 [SKILL-NLP-13] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong Tokenization cho các Mô hình Ngôn ngữ Lớn, sự khác biệt căn bản trong
chiến lược GỘP (merging) các sub-word giữa thuật toán Byte-Pair Encoding (BPE -
dùng trong GPT) và WordPiece (dùng trong BERT) là gì?

- **A.** BPE gộp dựa trên tần suất cặp ký tự xuất hiện liền kề cao nhất, còn WordPiece gộp dựa trên việc tối đa hóa hàm hợp lý Likelihood của ngữ liệu
- **B.** BPE bắt đầu bằng việc tách từng âm tiết ngữ âm (Syllable Segmentation), còn WordPiece dựa trên việc phân tích hình thái học của cấu trúc từ vựng
- **C.** BPE chỉ áp dụng riêng cho các ngôn ngữ sử dụng bảng chữ cái Latin, còn WordPiece được thiết kế chuyên biệt cho các ngôn ngữ có bộ chữ tượng hình
- **D.** BPE yêu cầu kích thước từ điển động thay đổi liên tục, còn WordPiece cố định số lượng token và chỉ tối ưu hóa các ma trận biểu diễn nhúng

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Dù kết quảkhá giống nhau, tiêu chí ưu tiên của BPE thiên về thống kê đếm số lần đụng độ (frequency) thuần túy, còn WordPiece đánh giá theo toán học mức độ đóng góp xác suất vào dữ liệu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Dù kết quảkhá giống nhau, tiêu chí ưu tiên của BPE thiên về thống kê đếm số lần đụng độ (frequency) thuần túy, còn WordPiece đánh giá theo toán học mức độ đóng góp xác suất vào dữ liệu.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 14 [SKILL-NLP-14] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khi đánh giá kết quảcủa các mô hình sinh ngôn ngữ, người ta dùng BLEU cho Dịch
máy và ROUGE cho Tóm tắt văn bản. Đâu là nhược điểm chí mạng CỦA CẢ HAI độ
đo tự động này khi so sánh với con người?

- **A.** Chúng không thể phạt được các mô hình lặp đi lặp lại cùng một từ vựng nhiều lần (Repetition Bias) trong quá trình giải mã tự hồi quy
- **B.** Chúng đòi hỏi phải sử dụng một mô hình ngôn ngữ lớn làm trọng tài đánh giá (LLM-as-a-Judge), gây tiêu tốn tài nguyên tính toán phần cứng
- **C.** Chúng chỉ đo lường sự trùng lặp từ vựng bề mặt (N-gram overlap), bỏ sót sự tương đồng về mặt ngữ nghĩa sâu khi sử dụng các cách diễn đạt tương đương
- **D.** Chúng chỉ đánh giá chính xác đối với các văn bản đã trải qua bước chuẩn hóa gốc từ hoàn chỉnh (Morphological Stemming) trước khi kiểm thử

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Ví dụviệc dịch ” The cat is happy” thành ” The feline is joyful” sẽbị BLEU và ROUGE chấm điểm 0 tuyệt đối vì không trùng lặp N-gram nào, mặc dù con người đánh giá là hoàn hảo vềý nghĩa.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Ví dụviệc dịch ” The cat is happy” thành ” The feline is joyful” sẽbị BLEU và ROUGE chấm điểm 0 tuyệt đối vì không trùng lặp N-gram nào, mặc dù con người đánh giá là hoàn hảo vềý nghĩa.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 15 [SKILL-NLP-15] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hạn chếcấu trúc nghiêm trọng nhất của kiến trúc Transformer tiêu chuẩn khi xử
lý các ngữ cảnh văn bản cực kỳdài (Long-Context Window, ví dụ: 1 triệu token) là
gì?

- **A.** Ma trận Embedding ban đầu gây ra hiện tượng triệt tiêu đạo hàm (vanishing gradient) khi chuỗi quá dài.
- **B.** Việc truyền ngữ cảnh dài làm giảm độ chính xác của hàm kích hoạt GELU tại các lớp cuối cùng.
- **C.** Cơ chếtựchú ý (Self-Attention) sẽquên đi các từ xuất hiện ở phần đầu của cuốn sách do giới hạn bộ nhớ LSTM.
- **D.** Chi phí tính toán và bộ nhớ VRAM của cơ chế Self-Attention tăng trưởng theo cấp số bình phương (quadratic O(N2)) so với độ dài chuỗi N.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Ma trận Attention có kích thước N × N.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `D`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Ma trận Attention có kích thước N × N. Với văn bản quá dài, ma trận này đòi hỏi một dung lượng bộ nhớkhổng lồvà số vòng lặp nhân ma trận khổng lồ, khiến các Transformer thông thường bị sập (OOM).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 16 [SKILL-NLP-16] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Giao thức Tokenization dựa trên mã hóa byte (Byte-Level BPE), được ứng dụng từ
thời GPT-2, nhằm mục đích giải quyết triệt đểvấn đềgì trong xử lý ngôn ngữtự
nhiên?

- **A.** Có thể mã hóa và xử lý hoàn hảo mọi loại ký tự Unicode hay emoji mà không bao giờ cần dựa vào ký hiệu Unknown token <UNK>
- **B.** Loại bỏ sự cần thiết của ma trận nhúng vị trí (Positional Embedding) bằng cách sử dụng các chỉ số byte tuần tự liên tiếp trong chuỗi
- **C.** Cho phép mô hình thực hiện nội suy tuyến tính trực tiếp trên các mảng bit tĩnh (Static Bit-Arrays) phân tán trong không gian bộ nhớ
- **D.** Giảm tải đáng kể hiện tượng bùng nổ gradient (Exploding Gradients) trong quá trình lan truyền ngược của kiến trúc Transformer Decoder

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: BBPE coi từ vựng gốc ban đầu là 256 byte cơ bản nhất, sau đó mới gộp chúng lên thành từ ngữ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: BBPE coi từ vựng gốc ban đầu là 256 byte cơ bản nhất, sau đó mới gộp chúng lên thành từ ngữ. Do mọi văn bản máy tính đều cấu tạo từ byte, mô hình không bao giờ gặp khái niệm ” từ nằm ngoài từ điển”.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 17 [SKILL-NLP-17] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Attention chéo (Cross-Attention) của các mô hình Encoder-Decoder
(ví dụ Machine Translation), bộ ba tham số Query (Q), Key (K), và Value (V) được trích
xuất từ đâu?

- **A.** Cả ba tham số Query, Key và Value đều được cập nhật độc lập thông qua một tầng Transformer trung gian đóng vai trò cầu nối
- **B.** Query và Key đến từ tầng Decoder để tìm điểm tương quan chú ý, còn Value được trích xuất từ tầng biểu diễn Encoder
- **C.** Query đến từ tầng ẩn Decoder ở bước hiện tại, còn Key và Value được cung cấp bởi toàn bộ chuỗi đầu ra từ Encoder
- **D.** Query và Value được trích xuất từ tầng biểu diễn cuối cùng của Encoder, còn Key được lấy từ tầng ẩn hiện tại của Decoder

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Đây là trái tim của giao tiếp dịch máy.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Đây là trái tim của giao tiếp dịch máy. Câu đang dịch (Decoder - Query) sẽ ” hỏi” xem nó nên chú ý vào từ nào trong câu gốc ngoại ngữ (Encoder - Keys/Values) để sinh từ tiếp theo chuẩn nhất.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 18 [SKILL-NLP-18] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Giải thuật Beam Search (Tìm kiếm theo chùm) khắc phục nhược điểm ” tầm nhìn
hạn hẹp” của giải thuật Greedy Search (Tìm kiếm tham lam) trong sinh ngôn ngữ
bằng cách nào?

- **A.** Kết hợp với mô hình Markov ẩn (Hidden Markov Models) để dự báo độ trôi chảy ngữ pháp cho toàn bộ câu văn bản phía sau
- **B.** Áp dụng hàm điều chỉnh nhiệt độ (Temperature Scaling) để làm phẳng phân phối xác suất dự đoán tại từng bước giải mã
- **C.** Sử dụng thuật toán quy hoạch động (Dynamic Programming Algorithm) để tìm kiếm chính xác chuỗi xác suất toàn cục cao nhất
- **D.** Tại mỗi bước, thay vì chỉ lấy 1 từ tốt nhất, giải thuật giữ lại $K$ chuỗi ứng viên (hypotheses) có xác suất tích lũy cao nhất

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Greedy Search chọn từ lớn nhất hiện tại có thểdẫn đến cả câu bị cụt nghĩa về sau.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `D`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Greedy Search chọn từ lớn nhất hiện tại có thểdẫn đến cả câu bị cụt nghĩa về sau. Beam Search giữ K kịch bản chạy song song, đảm bảo xác suất tổng hợp của toàn bộ đoạn văn được tối ưu tốt hơn.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 19 [SKILL-NLP-19] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình Skip-gram, một trong hai kiến trúc cốt lõi của thuật toán Word2Vec, được
thiết kếvới mục tiêu huấn luyện cụthểnào?

- **A.** Sử dụng một từ trung tâm (Center word) đểdự đoán xác suất xuất hiện của các từ nằm trong cửa sổngữ cảnh xung quanh nó.
- **B.** Phân cụm (Clustering) toàn bộ từ vựng thông qua thuật toán phân tích thành phần chính (PCA).
- **C.** Dự đoán nhãn từ loại (POS) của một từ trung tâm dựa vào sự kết hợp của các từ xung quanh.
- **D.** Tính trung bình các vector nhúng của ngữ cảnh đểtạo ra một vector câu đại diện duy nhất.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Skip-gram đi từ1 từ→dự đoán nhiều từ xung quanh, làm cho mô hình học biểu diễn rất tốt cho các từ hiếm.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Skip-gram đi từ1 từ→dự đoán nhiều từ xung quanh, làm cho mô hình học biểu diễn rất tốt cho các từ hiếm. Điều này ngược với cơ chế CBOW (Continuous Bag-of- Words).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 20 [SKILL-NLP-20] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khác với mô hình Masked Language Model (MLM), BERT còn được huấn luyện với
một mục tiêu thứhai (NSP - Next Sentence Prediction). Nhiệm vụthực sự của NSP
là gì?

- **A.** Tạo ra một biểu diễn không gian ẩn liên tục (continuous latent space) đểtóm tắt ý chính của câu A và sinh câu B.
- **B.** Đầu vào là cặp hai câu (A và B), mô hình phải dự đoán nhịphân xem câu B có phải là câu liền kềtiếp theo thực tếcủa câu A trong văn bản gốc hay không.
- **C.** Đo lường khoảng cách ngôn ngữgiữa hai câu thông qua thuật toán Earth Mover’s Distance (EMD).
- **D.** Huấn luyện một mạng Autoencoder đểkhôi phục cấu trúc ban đầu của cặp câu bị xáo trộn.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: NSP nhằm mục đích dạy mô hình hiểu được mối quan hệ logic, diễn ngôn giữa các câu, đặc biệt quan trọng cho các tác vụhỏi đáp (QA) hoặc suy luận ngôn ngữ tự nhiên (NLI).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `B`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: NSP nhằm mục đích dạy mô hình hiểu được mối quan hệ logic, diễn ngôn giữa các câu, đặc biệt quan trọng cho các tác vụhỏi đáp (QA) hoặc suy luận ngôn ngữ tự nhiên (NLI).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 21 [SKILL-NLP-21] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong một bài toán phát hiện giao dịch bất thường gồm 100 giao dịch. Thực tếcó 5
gian lận. Mô hình dự đoán có 10 gian lận, nhưng trong đó chỉ có 3 là gian lận thật.
Độchính xác (Precision) của mô hình là bao nhiêu?

- **A.** 95/100 = 0.95
- **B.** 3/5 = 0.6
- **C.** 3/10 = 0.3
- **D.** 7/10 = 0.7

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Precision (Độchính xác) = True Positive / (True Positive + False Positive).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Precision (Độchính xác) = True Positive / (True Positive + False Positive). Mô hình báo 10 trường hợp (Dự đoán Positive), đúng 3 (True Positive). Vậy Precision = 3/10 = 0.3.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 22 [SKILL-NLP-22] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong PyTorch, nếu một lớp nn. Linear(10, 5) được khởi tạo với độlệch (bias) được
bật mặc định, nó sẽchứa bao nhiêu tham số học được (trainable parameters)?

- **A.** 15
- **B.** 100
- **C.** 55
- **D.** 50

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Ma trận trọng số W có kích thước $5 \times 10$ = 50 tham số, cộng với vector bias kích thước 5, tổng cộng là 55 tham số.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Ma trận trọng số W có kích thước $5 \times 10$ = 50 tham số, cộng với vector bias kích thước 5, tổng cộng là 55 tham số.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 23 [SKILL-NLP-23] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Nếu một lớp Tích chập (Convolutional Layer) nhận đầu vào là ảnh kích thước $32 \times 32$,
sử dụng kích thước kernel (bộ lọc) là $3 \times 3$, stride (bước nhảy) là 1, và thiết lập
padding là ” same”. Kích thước không gian của bản đồđặc trưng (feature map) đầu
ra sẽlà bao nhiêu?

- **A.** $32 \times 32$
- **B.** $16 \times 16$
- **C.** $34 \times 34$
- **D.** $30 \times 30$

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Padding ” same” tự động chèn thêm một viền zero-padding vừa đủở các cạnh đểđảm bảo kích thước không gian (chiều rộng và chiều cao) không bị co ngót đi sau khi tích chập với stride=1.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Padding ” same” tự động chèn thêm một viền zero-padding vừa đủở các cạnh đểđảm bảo kích thước không gian (chiều rộng và chiều cao) không bị co ngót đi sau khi tích chập với stride=1.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 24 [SKILL-NLP-24] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hàm kích hoạt Swish (hoặc SiLU) do Google Brain đềxuất có công thức toán học là
gì?

- **A.** f(x) = ln(1 + ex)
- **B.** f(x) = max(0.01x, x)
- **C.** f(x) = x + max(0, x)
- **D.** f(x) = x · sigmoid(x)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Swish (x · σ(x)) không đơn điệu và có dạng cong trơn ở điểm âm, giúp luồng gradient mượt mà hơn ReLU và được dùng rộng rãi trong các mô hình như YOLOv5 hay EfficientNet.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `D`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Swish (x · σ(x)) không đơn điệu và có dạng cong trơn ở điểm âm, giúp luồng gradient mượt mà hơn ReLU và được dùng rộng rãi trong các mô hình như YOLOv5 hay EfficientNet.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 25 [SKILL-NLP-25] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong tính toán Self-Attention (Scaled Dot-Product Attention), tại sao ta phải chia
kết quảcủa phép nhân ma trận Query (Q) và Key (K) cho √dk?

- **A.** Đểgiữ cho phương sai của các giá trịlogits ổn định, ngăn chặn gradient của hàm Softmax rơi vào vùng bão hòa (bị triệt tiêu).
- **B.** Cân bằng sự chênh lệch độ dài giữa chuỗi query (đầu vào) và chuỗi key (ngữ cảnh).
- **C.** Đảm bảo khoảng cách Euclid giữa mọi vector nhúng luôn được giữ không đổi trong quá trình lặp.
- **D.** Đểtránh việc bộ nhớ GPU bị tràn khi khởi tạo ma trận Attention ở giới hạn phần cứng chuẩn.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Khi số chiều dk lớn, tích vô hướng của Q · KT trởnên rất lớn, đưa Softmax vào vùng gradient gần bằng 0, làm mô hình không học được.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Khi số chiều dk lớn, tích vô hướng của Q · KT trởnên rất lớn, đưa Softmax vào vùng gradient gần bằng 0, làm mô hình không học được.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.5 Kiến trúc Transformer (Vaswani et al., 2017)**.

---

### Câu 26 [SKILL-NLP-26] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong các độ đo đánh giá mô hình phân loại, F1-Score là trung bình điều hòa (Harmonic
Mean) của Precision và Recall. Tại sao lại sử dụng trung bình điều hòa thay vì trung
bình cộng thông thường?

- **A.** Vì phương pháp trung bình cộng số học (Arithmetic Mean) dễ gây ra hiện tượng phân kỳ gradient trong quá trình lan truyền ngược
- **B.** Vì đạo hàm của trung bình điều hòa ưu tiên các trọng số nhỏ, giúp hạn chế hiện tượng quá khớp (Overfitting) cho mô hình
- **C.** Vì trung bình điều hòa giúp chuẩn hóa kết quả cuối cùng theo phân phối Gauss chuẩn tắc (Standard Normal Distribution)
- **D.** Vì trung bình điều hòa phạt rất nặng khi một trong hai chỉ số (Precision hoặc Recall) quá thấp, ép mô hình phải cân bằng cả hai

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Nếu Precision = 1.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `D`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Nếu Precision = 1.0 và Recall = 0.0, trung bình cộng = 0.5, nhưng F1-Score = 0. Điều này đảm bảo mô hình không thể” ăn gian” bằng cách chỉ tối ưu một chỉ số.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 27 [SKILL-NLP-27] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Khởi tạo trọng số Xavier/Glorot (thường được dùng kết hợp với hàm Tanh hoặc
Sigmoid) có công thức dựa trên mục tiêu tối ưu toán học nào?

- **A.** Ngăn chặn tín hiệu mạng nơ-ron cộng dồn chồng chéo dẫn đến tràn bộ đệm biểu diễn dấu phẩy động 16-bit (Half Precision FP16)
- **B.** Chuẩn hóa mọi tín hiệu đầu vào thành phân phối xác suất có giá trị cực đại tại mốc 0 và cực tiểu tại mốc 1 một cách đồng đều
- **C.** Giữ cho phương sai của các tín hiệu đầu vào và phương sai của các đạo hàm gradient xấp xỉ không đổi qua tất cả các tầng mạng
- **D.** Cố định các trọng số về phân phối Laplace thưa thớt để kích hoạt cơ chế chuẩn hóa điều hòa L1 tự động trong toàn bộ mạng

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Bằng cách khởi tạo phương sai bằng 2/(n_in+n_out), tín hiệu không bị bùng nổhay triệt tiêu khi đi qua một mạng rất sâu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Bằng cách khởi tạo phương sai bằng 2/(n_in+n_out), tín hiệu không bị bùng nổhay triệt tiêu khi đi qua một mạng rất sâu.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 28 [SKILL-NLP-28] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Mô hình Whisper (của OpenAI) có năng lực siêu việt về nhận dạng giọng nói đa
ngôn ngữ (Multilingual ASR) chủ yếu là nhờ yếu tốnào?

- **A.** Sự ra đời của bộ tách từ chuyên biệt (Acoustic Tokenizer) cho tín hiệu âm thanh dựa trên các dải băng tần số Mel phi tuyến tính
- **B.** Thuật toán tích chập sóng phức (Complex Wave CNN) giải quyết triệt để hiện tượng biến dạng tín hiệu do nhiễu môi trường phòng thu
- **C.** Được huấn luyện bán giám sát trên tập dữ liệu khổng lồ 680.000 giờ âm thanh kèm văn bản đa dạng thu thập trực tiếp từ internet
- **D.** Kết hợp với mô hình ngôn ngữ lớn LLM để tự động sửa chữa toàn bộ lỗi chính tả và ngữ pháp sau giai đoạn giải mã âm vị học

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Whisper chứng minh sức mạnh của kiến trúc Transformer Encoder-Decoder cơ bản kết hợp với lượng dữ liệu tỷ lệlớn và yếu (weakly supervised).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Whisper chứng minh sức mạnh của kiến trúc Transformer Encoder-Decoder cơ bản kết hợp với lượng dữ liệu tỷ lệlớn và yếu (weakly supervised).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 29 [SKILL-NLP-29] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong các công cụxây dựng Agent LLM (như LangChain), khái niệm ” RAG” (Retrieval-
Augmented Generation) giải quyết vấn đềlớn nhất nào của mô hình ngôn ngữlớn?

- **A.** RAG loại bỏ giới hạn kích thước chuỗi ngữ cảnh đầu vào (Context Length Limit) của mô hình ngôn ngữ thông qua thuật toán cửa sổ trượt động
- **B.** RAG cho phép chuyển đổi ngôn ngữ đa quốc gia linh hoạt (Cross-Lingual Adaptation) trong thời gian thực thông qua hệ thống giao diện lập trình
- **C.** RAG tối ưu hóa ma trận Attention phân tán trên các cụm máy chủ (Distributed Attention), giúp mô hình tiết kiệm tối đa dung lượng bộ nhớ VRAM
- **D.** RAG giải quyết hiện tượng ảo giác (Hallucination) do thiếu thông tin mới cập nhật hoặc thiếu tri thức đặc thù trong dữ liệu nội bộ doanh nghiệp

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: RAG kết nối LLM với một cơ sởdữ liệu Vector; khi có câu hỏi, hệ thống truy xuất các đoạn văn bản tài liệu thực tếnhồi vào prompt cho LLM đểđảm bảo câu trảlời có bằng chứng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `D`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: RAG kết nối LLM với một cơ sởdữ liệu Vector; khi có câu hỏi, hệ thống truy xuất các đoạn văn bản tài liệu thực tếnhồi vào prompt cho LLM đểđảm bảo câu trảlời có bằng chứng.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 30 [SKILL-NLP-30] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Prompting ” Few-Shot” trong tương tác với Mô hình ngôn ngữ Lớn là phương
pháp cung cấp thông tin như thế nào?

- **A.** Phân tích cú pháp của các từ trong mệnh lệnh đểtrích xuất các quy luật biểu thức chính quy (Regex rules).
- **B.** Điều chỉnh hàm mất mát đểtrừng phạt lỗi lặp từ bằng một mạng sinh đối nghịch (GAN) cấu trúc đơn giản.
- **C.** Tiêm vào dấu nhắc (prompt) một vài (few) ví dụcụthểvềcâu hỏi và câu trảlời mẫu theo đúng định dạng, trước khi đưa ra câu hỏi thực sự cho mô hình giải quyết.
- **D.** Huấn luyện tinh chỉnh lại mô hình Large Language Model bằng phương pháp Low- Rank Adaptation (LoRA) chỉ với một vài mẫu nhỏ.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Việc đưa ví dụtrong ngữ cảnh (In-context learning) kích hoạt khả năng nhận dạng mẫu của LLM, giúp định hình phong cách phản hồi và cấu trúc dữ liệu đầu ra chính xác mà không tốn một chút chi phí cập nhật trọng số nào.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `C`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Việc đưa ví dụtrong ngữ cảnh (In-context learning) kích hoạt khả năng nhận dạng mẫu của LLM, giúp định hình phong cách phản hồi và cấu trúc dữ liệu đầu ra chính xác mà không tốn một chút chi phí cập nhật trọng số nào.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 31 [SKILL-NLP-31] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hệ thống Xử lý âm thanh, đặc trưng MFCC (Mel-Frequency Cepstral Coefficients)
yêu cầu áp dụng phép biến đổi toán học nào ở bước cuối cùng đểtách các thành
phần tần số tương quan?

- **A.** Phép biến đổi Fourier Nhanh (FFT - Fast Fourier Transform).
- **B.** Quá trình lọc Ngân hàng Mel với phổthông dải (Mel-Filter Bank Band-pass).
- **C.** Phép biến đổi Wavelet Liên tục (Continuous Wavelet Transform).
- **D.** Phép biến đổi Cosine rời rạc (DCT - Discrete Cosine Transform).

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: DCT giải tương quan (decorrelate) các bộ lọc ngân hàng Mel (Mel filter banks), nén thông tin vào một vài hệ số đầu tiên, cung cấp biểu diễn âm thanh cực kỳphù hợp cho học máy cổ điển và mạng nơ-ron nhỏ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `D`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: DCT giải tương quan (decorrelate) các bộ lọc ngân hàng Mel (Mel filter banks), nén thông tin vào một vài hệ số đầu tiên, cung cấp biểu diễn âm thanh cực kỳphù hợp cho học máy cổ điển và mạng nơ-ron nhỏ.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 32 [SKILL-NLP-32] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Hiện tượng ” Nút thắt KV-Cache” (KV-Cache Bottleneck) trong giai đoạn suy luận
(Inference) của các Mô hình Ngôn ngữ Lớn (LLM) đềcập đến vấn đềtiêu thụtài
nguyên gì?

- **A.** Sự tắc nghẽn dòng chảy thông tin tại tầng thắt nút (Bottleneck Layer) của khối giải mã tự hồi quy khi sinh các chuỗi văn bản dài
- **B.** Sự phình to của bộ nhớ VRAM dùng để lưu trữ các tensor Key và Value của các token cũ ở mọi tầng, tránh phải tính toán lại mỗi bước
- **C.** Hiện tượng sụt giảm độ chính xác giải tích của các ma trận Key và Value khi áp dụng lượng tử hóa xuống định dạng số nguyên 4-bit
- **D.** Băng thông mạng bị giới hạn khi các nút máy chủ trao đổi vector tham số trong các kịch bản huấn luyện phân tán quy mô lớn

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Việc sinh (generate) văn bản cực kỳtốn RAM không phải do bản thân mô hình lớn, mà là do bộ nhớđệm KV-Cache tỷ lệthuận với độ dài ngữ cảnh văn bản (context length).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `B`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Việc sinh (generate) văn bản cực kỳtốn RAM không phải do bản thân mô hình lớn, mà là do bộ nhớđệm KV-Cache tỷ lệthuận với độ dài ngữ cảnh văn bản (context length).

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 33 [SKILL-NLP-33] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Trong xử lý tín hiệu âm thanh (Audio Processing), đặc trưng Mel-Spectrogram thường
được trích xuất để mô phỏng khả năng gì trong thực tế?

- **A.** Mô phỏng thính giác tai người nhạy bén hơn nhiều ở các tần số thấp và kém nhạy hơn ở các tần số cao qua thang đo tần số Mel
- **B.** Mã hóa tiếng ồn nền của môi trường thành các tín hiệu số học rời rạc có thể triệt tiêu hoàn toàn bằng các bộ lọc tần số số học
- **C.** Mô phỏng khả năng cộng hưởng sóng âm trong không gian ba chiều của cấu trúc tai để bảo toàn định hướng không gian âm học
- **D.** Bù trừ độ trễ giao thoa của các dải sóng âm liên tục khi phát âm qua thanh quản nhằm đồng bộ hóa thời gian pha tín hiệu

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Thang đo Mel nén phổtần số tuyến tính gốc lại.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Thang đo Mel nén phổtần số tuyến tính gốc lại. Khoảng cách toán học giữa các tần số trên phổ Mel khớp với sự khác biệt cao độmà tai con người thực sự nghe được.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 34 [SKILL-NLP-34] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán FlashAttention tạo ra sự đột phá trong việc tính toán của Transformer
bằng cách tối ưu hóa yếu tốphần cứng nào?

- **A.** Tối ưu hóa nhận thức I/O (IO-aware) bằng kỹ thuật chia khối (Tiling) và tính toán trên SRAM của GPU, giảm đọc ghi từ VRAM
- **B.** Xóa bỏ hoàn toàn khối mạng MLP trung gian và kích hoạt giao tiếp truyền dữ liệu trực tiếp qua đường truyền mạng băng thông cao
- **C.** Áp dụng kỹ thuật lượng tử hóa vector (Vector Quantization) để nén các ma trận trọng số dấu phẩy động xuống định dạng số nguyên INT8
- **D.** Ép xung xung nhịp phần cứng đồ họa tự động thông qua một mô hình học máy tăng cường thích nghi theo khối lượng tính toán

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Attention cổ điển tốn thời gian không phải vì phép toán nhân, mà vì quá trình di chuyển ma trận trung gian khổng lồ (N x N) qua lại giữa các cấp bộ nhớ.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `A`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Attention cổ điển tốn thời gian không phải vì phép toán nhân, mà vì quá trình di chuyển ma trận trung gian khổng lồ (N x N) qua lại giữa các cấp bộ nhớ. FlashAttention giải quyết triệt đểvấn đềbăng thông này.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 35 [SKILL-NLP-35] — Phân hệ Module B (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc Transformer phân tích tín hiệu âm thanh thô thường đối mặt với vấn đề
quá tải bộ nhớvì số lượng mẫu (samples) trong một giây âm thanh (ví dụ: 16.000
Hz) là cực lớn. Các mô hình hiện đại khắc phục bằng cách nào?

- **A.** Tự động loại bỏ hoàn toàn các dải tần số thấp nhạy cảm (dưới 500 Hz) bằng bộ lọc thông cao trước khi chuyển đổi sang miền số học
- **B.** Sử dụng các tầng CNN 1D đầu tiên làm bộ trích xuất đặc trưng để nén độ dài tín hiệu thô hàng chục ngàn mẫu xuống vài trăm vector
- **C.** Chia tệp âm thanh thành hàng ngàn phân đoạn siêu ngắn và huấn luyện một cách bất đồng bộ độc lập trên các luồng xử lý riêng rẽ
- **D.** Mã hóa tín hiệu âm thanh theo các khung thời gian 10 mili-giây qua phương thức nén dữ liệu trung gian chuẩn mực để giảm tải

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất cốt lõi: Chuỗi đầu vào quá dài là kẻthù của self-attention O(N2).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Phân tích bối cảnh bài toán và các khái niệm kỹ thuật trong câu hỏi.
2. Kiểm tra phương án `B`: Phù hợp hoàn toàn với lý thuyết nền tảng và thực nghiệm chuẩn. Chi tiết: Chuỗi đầu vào quá dài là kẻthù của self-attention O(N2). Kết hợp sức mạnh trích xuất biểu diễn đặc trưng cục bộ của CNN để” làm ngắn” sequence là tiêu chuẩn vàng của mọi mô hình audio-transformer hiện nay.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Tránh nhầm lẫn giữa các kỹ thuật xử lý chuỗi cổ điển và cơ chế tự chú ý (Self-Attention) hiện đại; chú ý các từ khóa điều kiện biên trong câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Sách giáo trình *Speech and Language Processing* (Jurafsky & Martin, 3rd ed.) và tài liệu *SkillPixel Session 5*. Xem **§4.6 So sánh BERT vs GPT**.

---

### Câu 36 [SKILL-CV-01] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong bài toán phân loại hình ảnh (Image Classification), máy tính nhìn nhận một
bức ảnh đầu vào dưới định dạng nào?

- **A.** Chuỗi các vector đặc trưng 1D (1D feature vectors)
- **B.** Đồthịcác đỉnh và cạnh biểu diễn hình học
- **C.** Ma trận các giá trịtần số không gian (Spatial frequency matrices)
- **D.** Lưới các giá trịđiểm ảnh (pixel values)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Máy tính xử lý hình ảnh số dưới dạng một ma trận (hoặc tensor) các giá trịđiểm ảnh (pixels), ví dụảnh màu được biểu diễn bởi tensor 3 chiều: Chiều cao × Chiều rộng × Số kênh màu (RGB).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Máy tính xử lý hình ảnh số dưới dạng một ma trận (hoặc tensor) các giá trịđiểm ảnh (pixels), ví dụảnh màu được biểu diễn bởi tensor 3 chiều: Chiều cao × Chiều rộng × Số kênh màu (RGB).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 37 [SKILL-CV-02] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mục tiêu chính của nhiệm vụphân loại hình ảnh (Image Classification) là gì?

- **A.** Phân đoạn và gán nhãn chi tiết cho từng điểm ảnh (Pixel-wise segmentation).
- **B.** Biến đổi ảnh đầu vào thành một biểu diễn nhúng (embedding) không gian nhỏ hơn.
- **C.** Gán một nhãn (label) hoặc lớp (class) tổng quát cho toàn bộ bức ảnh.
- **D.** Xác định vị trí (tọa độ) của một hoặc nhiều đối tượng trong ảnh.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Nhiệm vụphân loại hình ảnh (Image classification) là bài toán dự đoán nhãn tổng quát cho toàn bộ một hình ảnh đầu vào (ví dụ: gán nhãn ” con mèo” cho bức ảnh), khác với Object Detection hay Segmentation.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Nhiệm vụphân loại hình ảnh (Image classification) là bài toán dự đoán nhãn tổng quát cho toàn bộ một hình ảnh đầu vào (ví dụ: gán nhãn ” con mèo” cho bức ảnh), khác với Object Detection hay Segmentation.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 38 [SKILL-CV-03] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Lý do chính khiến Mạng nơ-ron Tích chập (CNN) trở thành kiến trúc tiêu chuẩn cho
xử lý ảnh thay vì Mạng Nơ-ron Đa tầng (MLP) truyền thống là gì?

- **A.** CNN đòi hỏi ít dữ liệu huấn luyện hơn nhờ việc sử dụng các thuật toán tối ưu hóa thích nghi (Adaptive Optimizers)
- **B.** CNN có khả năng học các mẫu phân cấp không gian (Hierarchical Patterns) trực tiếp từ dữ liệu tensor điểm ảnh thô
- **C.** CNN có tốc độ huấn luyện nhanh hơn nhờ việc loại bỏ hoàn toàn các tầng kết nối đầy đủ (Fully-Connected Layers)
- **D.** CNN không sử dụng đạo hàm để cập nhật trọng số, giúp mô hình tránh bị rơi vào các điểm cực tiểu cục bộ không mong muốn

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: CNN được thiết kếvới các lớp tích chập giúp trích xuất các đặc trưng không gian (như cạnh, vân, hình dạng) theo cấu trúc phân cấp, điều mà MLP (Fully Connected) rất kém hiệu quảdo phá vỡcấu trúc không gian dạng lưới của ảnh.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: CNN được thiết kếvới các lớp tích chập giúp trích xuất các đặc trưng không gian (như cạnh, vân, hình dạng) theo cấu trúc phân cấp, điều mà MLP (Fully Connected) rất kém hiệu quảdo phá vỡcấu trúc không gian dạng lưới của ảnh.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 39 [SKILL-CV-04] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc mạng CNN tiêu chuẩn, luồng xử lý thông tin đi qua các lớp (layers)
thường tuân theo thứtựnào dưới đây?

- **A.** Kết nối đầy đủ (FC) →Tích chập (Conv) →Gộp (Pooling) →Hàm kích hoạt
- **B.** Hàm kích hoạt →Kết nối đầy đủ (FC) →Tích chập (Conv) →Gộp (Pooling)
- **C.** Tích chập (Conv) →Hàm kích hoạt →Gộp (Pooling) →Kết nối đầy đủ (FC)
- **D.** Gộp (Pooling) →Tích chập (Conv) →Hàm kích hoạt →Đầu ra

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Một luồng CNN tiêu chuẩn bắt đầu bằng việc trích xuất đặc trưng qua lớp Tích chập, kích hoạt phi tuyến (như ReLU), giảm chiều bằng Pooling, lặp lại nhiều lần, và cuối cùng dùng lớp FC đểphân loại.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Một luồng CNN tiêu chuẩn bắt đầu bằng việc trích xuất đặc trưng qua lớp Tích chập, kích hoạt phi tuyến (như ReLU), giảm chiều bằng Pooling, lặp lại nhiều lần, và cuối cùng dùng lớp FC đểphân loại.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 40 [SKILL-CV-05] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mục đích chính của các lớp Tích chập (Convolutional Layers) trong mạng CNN là gì?

- **A.** Chuẩn hóa phương sai của dữ liệu đầu vào về1 đểtăng tốc độhội tụ.
- **B.** Giảm thiểu hiện tượng học quá mức (overfitting) bằng cách bỏ ngẫu nhiên các kết nối.
- **C.** Học các cấu trúc phân cấp đặc trưng không gian như cạnh, vân bề mặt, hình dạng.
- **D.** Ánh xạcác đặc trưng từ không gian nhiều chiều xuống không gian 1 chiều.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Lớp Tích chập sử dụng các bộ lọc (kernels/filters) quét qua ảnh đểdò tìm và trích xuất các đặc trưng không gian, từ mức độcơ bản (cạnh, góc) đến mức độphức tạp (hình dạng).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Lớp Tích chập sử dụng các bộ lọc (kernels/filters) quét qua ảnh đểdò tìm và trích xuất các đặc trưng không gian, từ mức độcơ bản (cạnh, góc) đến mức độphức tạp (hình dạng).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 41 [SKILL-CV-06] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Lớp Gộp (Pooling Layer) trong CNN có tác dụng chính nào sau đây?

- **A.** Tăng cường độphân giải của bản đồđặc trưng bằng phép nội suy song tuyến tính (bilinear interpolation).
- **B.** Chuyển đổi dữ liệu từ dạng hàm phi tuyến về dạng tuyến tính hoàn toàn.
- **C.** Giảm kích thước mẫu (downsample) của bản đồđặc trưng, giảm khối lượng tính toán và tạo tính bất biến tịnh tiến.
- **D.** Trích xuất các đặc trưng ngữnghĩa (semantic features) mức độcao từ ảnh thô.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Lớp Gộp (như Max Pooling) làm giảm kích thước không gian của tensor, giúp giảm số lượng tham số tính toán ở các lớp sau và giúp mạng chống chịu tốt hơn với sự dịch chuyển nhẹcủa vật thể (bất biến tịnh tiến cục bộ).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Lớp Gộp (như Max Pooling) làm giảm kích thước không gian của tensor, giúp giảm số lượng tham số tính toán ở các lớp sau và giúp mạng chống chịu tốt hơn với sự dịch chuyển nhẹcủa vật thể (bất biến tịnh tiến cục bộ).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 42 [SKILL-CV-07] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật ngữ “Đệm (Padding)” trong lớp Tích chập có nghĩa là gì?

- **A.** Khoảng cách dịch chuyển tối thiểu của bộ lọc trên hình ảnh trong mỗi lần quét.
- **B.** Tăng cường số lượng bộ lọc (kernel) đểmở rộng khả năng trích xuất đặc trưng.
- **C.** Thêm các điểm ảnh (thường là giá trị0) vào xung quanh biên của hình ảnh/bản đồ đặc trưng đầu vào.
- **D.** Kỹ thuật nội suy các điểm ảnh bị khuyết trong dữ liệu đầu vào.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Padding là kỹ thuật thêm các viền pixel (thường là 0) xung quanh ảnh gốc trước khi tích chập, giúp bảo toàn kích thước không gian và xử lý hiệu quảthông tin ở mép ảnh, không làm giảm kích thước tensor quá nhanh.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Padding là kỹ thuật thêm các viền pixel (thường là 0) xung quanh ảnh gốc trước khi tích chập, giúp bảo toàn kích thước không gian và xử lý hiệu quảthông tin ở mép ảnh, không làm giảm kích thước tensor quá nhanh.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 43 [SKILL-CV-08] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi tham số Padding được đặt là ' valid ', điều gì sẽxảy ra với kích thước của bản đồ
đặc trưng (feature map) đầu ra?

- **A.** Kích thước đầu ra sẽbằng chính kích thước của bộ lọc (kernel size).
- **B.** Kích thước đầu ra luôn luôn được bảo toàn bằng với kích thước đầu vào.
- **C.** Kích thước đầu ra sẽnhỏ hơn kích thước đầu vào do không có đệm.
- **D.** Kích thước đầu ra sẽđược nhân đôi so với kích thước đầu vào.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Padding ' valid ' có nghĩa là mạng sẽ không thêm bất cứlớp đệm nào.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Padding ' valid ' có nghĩa là mạng sẽ không thêm bất cứlớp đệm nào. Khi bộ lọc quét qua, nó không thểđi ra ngoài ranh giới ảnh, dẫn đến ảnh kết quảluôn bị thu nhỏ lại theo kích thước của kernel.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 44 [SKILL-CV-09] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật ngữ “Bước nhảy (Stride)” trong cấu hình mạng CNN ám chỉ điều gì?

- **A.** Số lượng điểm ảnh mà bộ lọc (kernel) dịch chuyển trên đầu vào sau mỗi lần quét.
- **B.** Kích thước không gian thực tếcủa lớp Pooling (ví dụ: $2 \times 2$).
- **C.** Số lượng lớp tích chập liên tiếp nằm trong cùng một khối phần dư (residual block).
- **D.** Hệ số điều chỉnh mức độcập nhật gradient của bộ tối ưu hóa (optimizer).

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Stride xác định bước dịch chuyển của bộ lọc (kernel).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Stride xác định bước dịch chuyển của bộ lọc (kernel). Stride bằng 1 nghĩa là dịch từng pixel một, Stride bằng 2 nghĩa là bỏ qua 1 pixel mỗi lần dịch, làm giảm một nửa kích thước không gian đầu ra.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 45 [SKILL-CV-10] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong mạng CNN, khái niệm “Vùng tiếp nhận (Receptive Field)” được hiểu như thế
nào?

- **A.** Là vùng của hình ảnh đầu vào mà một đặc trưng (hoặc một nơ-ron cụthể) ở các lớp sâu đang tác động tới.
- **B.** Là toàn bộ phạm vi bộ nhớ GPU mà mô hình được phép sử dụng trong lúc huấn luyện.
- **C.** Là vùng chứa các nhãn phân loại (classes) đã được mã hóa one-hot của tập dữ liệu.
- **D.** Là kích thước ma trận trọng số của lớp Fully Connected cuối cùng trước hàm Softmax.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Receptive Field là phạm vi khu vực trên bức ảnh gốc đầu vào tác động trực tiếp đến giá trịcủa một điểm nơ-ron cụthểở các lớp bản đồđặc trưng (feature maps) sâu hơn trong mạng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Receptive Field là phạm vi khu vực trên bức ảnh gốc đầu vào tác động trực tiếp đến giá trịcủa một điểm nơ-ron cụthểở các lớp bản đồđặc trưng (feature maps) sâu hơn trong mạng.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 46 [SKILL-CV-11] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Tăng cường dữ liệu (Data Augmentation) được sử dụng nhằm mục đích
chính nào trong học sâu?

- **A.** Mở rộng tập dữ liệu huấn luyện nhân tạo bằng cách sửa đổi ảnh gốc, giúp mô hình tổng quát hóa tốt hơn.
- **B.** Giảm chiều dữ liệu đầu vào thông qua các phép biến đổi PCA đểtăng tốc độhuấn luyện.
- **C.** Xóa bỏ nhiễu (denoise) trong các hình ảnh có chất lượng thấp của tập kiểm tra.
- **D.** Tự động gắn nhãn (pseudo-labeling) cho các dữ liệu hình ảnh chưa có nhãn trong tập huấn luyện.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Bằng cách thực hiện các phép biến đổi (xoay, lật, cắt, đổi độsáng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Bằng cách thực hiện các phép biến đổi (xoay, lật, cắt, đổi độsáng...) trên ảnh gốc, Data Augmentation tạo ra nhiều mẫu đa dạng giúp mô hình học được các đặc trưng bất biến, giảm Overfitting.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 47 [SKILL-CV-12] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Đâu KHÔNG PHẢI là một kỹ thuật Tăng cường dữ liệu (Data Augmentation) phổ biến
đối với dữ liệu hình ảnh?

- **A.** Lật ngang / lật dọc (Horizontal / Vertical Flip)
- **B.** Xoay ngẫu nhiên (Random Rotation)
- **C.** Sử dụng thuật toán phân cụm K-Means để giảm số lượng màu sắc
- **D.** Nhiễu độsáng / độtương phản (Brightness / Contrast Jitter)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Cắt, Xoay, Lật, và Thêm nhiễu màu/độsáng là các phép biến đổi ảnh (Data Augmentation) cơ bản.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Cắt, Xoay, Lật, và Thêm nhiễu màu/độsáng là các phép biến đổi ảnh (Data Augmentation) cơ bản. K-Means clustering là một thuật toán học máy không giám sát, không phải là kỹ thuật tăng cường mẫu huấn luyện.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 48 [SKILL-CV-13] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kỹ thuật Chuẩn hóa theo lô (Batch Normalization) mang lại lợi ích gì cho việc huấn
luyện mạng CNN?

- **A.** Ép các trọng số của mạng về mức 0 để giảm thiểu độphức tạp của mô hình.
- **B.** Ổn định và tăng tốc quá trình huấn luyện, cho phép sử dụng tỷ lệhọc (learning rates) cao hơn.
- **C.** Kết hợp thông tin từ nhiều độphân giải khác nhau đểthay thếlớp Gộp (Pooling).
- **D.** Loại bỏ hoàn toàn yêu cầu phải tính toán hàm mất mát (loss function) ở cuối mạng.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Batch Normalization chuẩn hóa phân phối dữ liệu đầu ra của lớp trước đó ở mỗi mini-batch, giảm hiện tượng internal covariate shift, giúp gradients ổn định và mô hình hội tụnhanh hơn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Batch Normalization chuẩn hóa phân phối dữ liệu đầu ra của lớp trước đó ở mỗi mini-batch, giảm hiện tượng internal covariate shift, giúp gradients ổn định và mô hình hội tụnhanh hơn.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 49 [SKILL-CV-14] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp Điều chuẩn Bỏ học (Dropout) giúp giảm hiện tượng quá khớp (overfitting)
dựa trên cơ chếnào?

- **A.** Trong quá trình huấn luyện, đặt ngẫu nhiên một tỷ lệcác nơ-ron về giá trị0, buộc mạng học các đặc trưng mạnh mẽhơn.
- **B.** Tự động loại bỏ các ảnh mà mô hình dự đoán sai nhiều lần khỏi tập dữ liệu huấn luyện.
- **C.** Giảm đồng loạt tất cả các trọng số (weights) của mạng xuống một tỷ lệnhất định sau mỗi vòng lặp (epoch).
- **D.** Thêm nhiễu ngẫu nhiên vào nhãn của dữ liệu đầu vào (label smoothing).

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Dropout ” tắt” ngẫu nhiên các nơ-ron, ngăn chặn mạng phụ thuộc quá nhiều vào một tập hợp đặc trưng hẹp, buộc mạng lưới phải phân tán trọng số và học các đặc trưng (robust features) tổng quát hơn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Dropout ” tắt” ngẫu nhiên các nơ-ron, ngăn chặn mạng phụ thuộc quá nhiều vào một tập hợp đặc trưng hẹp, buộc mạng lưới phải phân tán trọng số và học các đặc trưng (robust features) tổng quát hơn.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 50 [SKILL-CV-15] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Điều chuẩn L2 (Weight Decay) hoạt động như thế nào đểngăn chặn hiện tượng quá
khớp?

- **A.** Tăng cường giá trịcủa các nơ-ron quan trọng nhất lên cấp số nhân.
- **B.** Làm phẳng (flatten) dữ liệu đầu vào sớm hơn ở các lớp đầu tiên để giảm lượng tham số.
- **C.** Thêm một hình phạt (penalty) vào hàm mất mát dựa trên tổng bình phương độlớn của các trọng số mạng.
- **D.** Dừng quá trình huấn luyện ngay lập tức nếu độ chính xác trên tập kiểm định bắt đầu giảm.

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Weight Decay (Điều chuẩn L2) thêm tổng bình phương của các trọng số vào hàm mất mát, khuyến khích trình tối ưu hóa giữ cho các trọng số mô hình có giá trịnhỏ, phân tán đều đặn, từ đó giảm độphức tạp và ít bị quá khớp.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Weight Decay (Điều chuẩn L2) thêm tổng bình phương của các trọng số vào hàm mất mát, khuyến khích trình tối ưu hóa giữ cho các trọng số mô hình có giá trịnhỏ, phân tán đều đặn, từ đó giảm độphức tạp và ít bị quá khớp.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 51 [SKILL-CV-16] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Chiến lược ” Dừng sớm” (Early Stopping) ra quyết định dừng quá trình huấn luyện
dựa trên tiêu chí nào?

- **A.** Khi mất mát trên tập huấn luyện (training loss) giảm xuống và đạt đúng giá trị0.
- **B.** Khi thời gian huấn luyện vượt quá giới hạn tài nguyên của hệ thống (GPU timeout).
- **C.** Khi thuật toán tối ưu hóa tự động phát hiện ra cực tiểu toàn cục của hàm mất mát.
- **D.** Khi hiệu suất trên tập kiểm định (validation set) ngừng cải thiện trong nhiều vòng lặp liên tiếp.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Dừng sớm theo dõi Validation Loss/Accuracy.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Dừng sớm theo dõi Validation Loss/Accuracy. Khi các chỉ số này không còn cải thiện (hoặc bắt đầu tệđi), điều đó chứng tỏmô hình bắt đầu ” học vẹt” (overfit) tập huấn luyện, nên ta dừng huấn luyện lại.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 52 [SKILL-CV-17] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mạng ResNet (Residual Network) ra đời để giải quyết vấn đềcốt lõi nào thường gặp
ở các mạng CNN rất sâu?

- **A.** Tình trạng bùng nổkhông gian bộ nhớ (Memory Explosion) khi tăng số lớp.
- **B.** Sự thiếu hụt các đặc trưng cục bộ (Local Features) ở các lớp cuối cùng.
- **C.** Tốc độsuy luận (Inference Speed) quá chậm đểtriển khai trên các thiết bị di động.
- **D.** Hiện tượng triệt tiêu đạo hàm (Vanishing Gradients) trong quá trình lan truyền ngược.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Khi mạng nơ-ron quá sâu, quá trình lan truyền ngược làm các giá trịgradient nhân với nhau nhiều lần và tiến dần về0 (vanishing gradients), khiến các lớp đầu không học được.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Khi mạng nơ-ron quá sâu, quá trình lan truyền ngược làm các giá trịgradient nhân với nhau nhiều lần và tiến dần về0 (vanishing gradients), khiến các lớp đầu không học được. ResNet giải quyết vấn đềnày qua khối Residual Blocks.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 53 [SKILL-CV-18] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cơ chếkiến trúc nào là ” trái tim” tạo nên sự khác biệt của mạng ResNet?

- **A.** Cơ chếchú ý tự thân (Self-Attention Mechanism)
- **B.** Sử dụng hàm kích hoạt Sigmoid ở mọi lớp thay vì ReLU
- **C.** Kết nối tắt (Skip Connections / Shortcut)
- **D.** Lớp tích chập tách rời theo chiều sâu (Depthwise Separable Convolution)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Kết nối tắt (Skip Connections) trong khối thặng dư (Residual Block) cho phép dòng gradient truyền trực tiếp qua ” đường tắt”, vượt qua các lớp ẩn đểđến thẳng các lớp sâu hơn mà không bị triệt tiêu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Kết nối tắt (Skip Connections) trong khối thặng dư (Residual Block) cho phép dòng gradient truyền trực tiếp qua ” đường tắt”, vượt qua các lớp ẩn đểđến thẳng các lớp sâu hơn mà không bị triệt tiêu.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 54 [SKILL-CV-19] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Ý tưởng ” Mở rộng hỗn hợp” (Compound Scaling) của kiến trúc EfficientNet có nghĩa
là gì?

- **A.** Đồng thời mở rộng ba chiều: chiều sâu, chiều rộng và độphân giải ảnh theo một tỷ lệcân bằng có nguyên tắc.
- **B.** Sử dụng nhiều GPU kết hợp lại đểhuấn luyện các bản đồđặc trưng có kích thước khác nhau.
- **C.** Chỉ tăng độsâu của mạng (thêm lớp) bằng cách lặp lại các khối mạng huấn luyện sẵn nhiều lần.
- **D.** Kết hợp (mix) đầu ra của nhiều mô hình CNN khác nhau lại thành một mô hình Ensemble duy nhất.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: EfficientNet phát hiện ra rằng việc mở rộng mạng chỉ theo 1 hướng (rất sâu, hoặc rất rộng, hoặc ảnh rất to) mang lại hiệu quảgiảm dần.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: EfficientNet phát hiện ra rằng việc mở rộng mạng chỉ theo 1 hướng (rất sâu, hoặc rất rộng, hoặc ảnh rất to) mang lại hiệu quảgiảm dần. Thay vào đó, tăng đều cả3 yếu tốtheo một hệ số nhất định sẽtối ưu hiệu suất.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 55 [SKILL-CV-20] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc MobileNet được thiết kếvà tối ưu hóa đặc biệt cho mục đích gì?

- **A.** Huấn luyện các mô hình tạo sinh hình ảnh (Generative Adversarial Networks) độphân giải cao.
- **B.** Triển khai trên các thiết bị có tài nguyên hạn chếnhư điện thoại di động và thiết bị IoT.
- **C.** Trích xuất đặc trưng cho các mô hình ngôn ngữlớn (LLMs) đa phương thức.
- **D.** Xử lý trực tiếp các video thời gian thực với định dạng dữ liệu 3D-CNN.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: MobileNet được thiết kếđánh đổi một phần nhỏ độ chính xác đểđổi lấy dung lượng mô hình cực nhỏ gọn và tốc độsuy luận (inference) cực nhanh, lý tưởng cho mobile và edge computing.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: MobileNet được thiết kếđánh đổi một phần nhỏ độ chính xác đểđổi lấy dung lượng mô hình cực nhỏ gọn và tốc độsuy luận (inference) cực nhanh, lý tưởng cho mobile và edge computing.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 56 [SKILL-CV-21] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thành phần cốt lõi tạo nên sự tối ưu về tham số và tốc độcủa kiến trúc MobileNet là
gì?

- **A.** Kết hợp các lớp Gộp cực đại liên tiếp (Consecutive Max Pooling)
- **B.** Tích chập Tách rời theo Độsâu (Depthwise Separable Convolutions)
- **C.** Loại bỏ ngẫu nhiên các kênh đặc trưng (Channel Dropout)
- **D.** Chỉ sử dụng lớp tích chập với bộ lọc kích thước $1 \times 1$

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Depthwise Separable Convolution chia 1 phép tích chập chuẩn tốn kém thành 2 bước nhẹnhàng hơn: Depthwise (quét không gian từng kênh riêng biệt) và Pointwise (trộn thông tin giữa các kênh bằng tích chập $1 \times 1$).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Depthwise Separable Convolution chia 1 phép tích chập chuẩn tốn kém thành 2 bước nhẹnhàng hơn: Depthwise (quét không gian từng kênh riêng biệt) và Pointwise (trộn thông tin giữa các kênh bằng tích chập $1 \times 1$).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 57 [SKILL-CV-22] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Tích chập Tách rời theo Độsâu (Depthwise Separable Convolutions) bao gồm hai phép
toán cụthểnào?

- **A.** Tích chập $3 \times 3$ tiêu chuẩn theo sau là một lớp Max Pooling $2 \times 2$.
- **B.** Tích chập Depthwise (theo chiều sâu từng kênh) và Tích chập Pointwise (tích chập $1 \times 1$).
- **C.** Làm phẳng (Flatten) theo sau là kích hoạt Softmax trên toàn bộ kênh.
- **D.** Tích chập không gian $2 \times 2$ và một lớp Kết nối đầy đủ (Fully Connected).

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Bước 1: Depthwise áp dụng 1 filter cho 1 channel đầu vào đểtrích xuất không gian.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Bước 1: Depthwise áp dụng 1 filter cho 1 channel đầu vào đểtrích xuất không gian. Bước 2: Pointwise dùng filter $1 \times 1$ đểtuyến tính hóa và kết hợp thông tin giữa các channel lại với nhau.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 58 [SKILL-CV-23] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong quá trình tinh chỉnh (Fine-tuning) sử dụng mô hình huấn luyện sẵn (Pretrained
Model), mục đích chính của việc thay thếlớp phân loại cuối cùng (Custom Head) là
gì?

- **A.** Đểtái khởi tạo trọng số và bắt mô hình học lại từ đầu toàn bộ các đặc trưng cấp thấp.
- **B.** Đểsố lượng nút ở đầu ra tương thích với số lượng nhãn (classes) mới của bài toán hiện tại.
- **C.** Đểgiảm số lượng kênh (channels) của ảnh đầu vào từ RGB sang thang độxám (Grayscale).
- **D.** Đểđóng băng (freeze) vĩnh viễn các trọng số của phần thân (backbone) mà không cần cập nhật.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Các mô hình huấn luyện sẵn (như trên ImageNet) thường có lớp phân loại dự đoán 1000 classes.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Các mô hình huấn luyện sẵn (như trên ImageNet) thường có lớp phân loại dự đoán 1000 classes. Khi giải quyết bài toán mới (ví dụphân loại chó/mèo chỉ có 2 classes), ta bắt buộc phải thay thếlớp cuối cùng này (Head).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 59 [SKILL-CV-24] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong thư viện torchvision của PyTorch, đối với kiến trúc ResNet, lớp phân loại cuối
cùng thường được thiết kếdưới tên thuộc tính nào?

- **A.** Tầng phân loại `classification_layer` (tầng phân loại đa lớp chuẩn)
- **B.** Tầng phân loại `classifier` (khối trích xuất và phân loại đầu ra)
- **C.** Tầng phân loại `fc` (tầng kết nối đầy đủ fully connected)
- **D.** Tầng phân loại `head` (đầu ra tuyến tính cuối cùng của mạng)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Trong mã nguồn PyTorch, mô hình ResNet định nghĩa lớp fully connected cuối cùng là self.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Trong mã nguồn PyTorch, mô hình ResNet định nghĩa lớp fully connected cuối cùng là self.fc. Đểthay đổi lớp phân loại, ta gán model.fc = nn. Linear(...).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 60 [SKILL-CV-25] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong thư viện torchvision của PyTorch, đối với các kiến trúc như EfficientNet hoặc
MobileNet, mô-đun thực hiện phân loại ở cuối mạng thường được nhóm dưới tên
thuộc tính nào?

- **A.** classifier
- **B.** fc
- **C.** linear_head
- **D.** output_module

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Khác với ResNet dùng fc, các mạng kiến trúc mới hơn như EfficientNet, VGG hay MobileNet thường nhóm các lớp phân loại cuối cùng (như Dropout và Linear) thành một khối module tên là classifier (thường là một nn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Khác với ResNet dùng fc, các mạng kiến trúc mới hơn như EfficientNet, VGG hay MobileNet thường nhóm các lớp phân loại cuối cùng (như Dropout và Linear) thành một khối module tên là classifier (thường là một nn. Sequential).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 61 [SKILL-CV-26] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hàm kích hoạt (Activation function) đặc biệt nào được sử dụng trong mạng MobileNetV3
nhằm cải thiện độ chính xác nhưng vẫn tối ưu hóa được chi phí tính toán trên phần
cứng di động?

- **A.** GELU
- **B.** Leaky ReLU
- **C.** Hardswish
- **D.** Swish

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: MobileNetV3 giới thiệu hàm Hardswish (một xấp xỉtính toán của hàm Swish) giúp mô hình đạt độ chính xác cao hơn ReLU nhưng sử dụng các phép toán cơ bản dễtính toán hơn Swish gốc trên phần cứng di động.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: MobileNetV3 giới thiệu hàm Hardswish (một xấp xỉtính toán của hàm Swish) giúp mô hình đạt độ chính xác cao hơn ReLU nhưng sử dụng các phép toán cơ bản dễtính toán hơn Swish gốc trên phần cứng di động.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 62 [SKILL-CV-27] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khối nn. Sequential trong PyTorch có vai trò gì khi xây dựng các mô-đun hoặc ” Custom
Head” cho mô hình CNN?

- **A.** Gói gộp nhiều lớp mạng (như Linear, ReLU, Dropout) lại thành một luồng thực thi tuần tự duy nhất.
- **B.** Kiểm soát quy trình lan truyền ngược (Backpropagation) mà không cần gọi hàm backward().
- **C.** Xác định và tính toán hàm mất mát (Loss Function) tự động ở cuối luồng.
- **D.** Quản lý và nạp dữ liệu huấn luyện dạng lô (Data Batching).

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: nn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: nn. Sequential là một container. Các tensor đi qua nn. Sequential sẽlần lượt đi qua các lớp (layers) được định nghĩa bên trong nó theo đúng thứtự (ví dụ: Linear →ReLU →Dropout →Linear).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 63 [SKILL-CV-28] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Một lớp Kết nối đầy đủ (nn. Linear trong PyTorch) yêu cầu tensor đầu vào phải có cấu
trúc như thế nào?

- **A.** Một chuỗi các token (Tokenized Sequence) tương tự như mô hình Transformer.
- **B.** Một tensor 4 chiều dạng (Batch, Channels, Height, Width) giữ nguyên từ ảnh thô.
- **C.** Một ma trận vuông 2 chiều dạng (Height, Width) đại diện cho cường độpixel.
- **D.** Một tensor 1 chiều (hoặc 2 chiều với Batch là chiều thứnhất) chứa dữ liệu đã được làm phẳng (Flattened).

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Lớp Linear/Dense thực hiện phép nhân ma trận chuẩn y = xAT + b, nên nó không nhận tensor biểu diễn không gian 3D (C, H, W) của ảnh, mà yêu cầu dữ liệu phải được bẻ phẳng thành một vector 1D (thường kèm chiều batch thành 2D: [Batch, Features]).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Lớp Linear/Dense thực hiện phép nhân ma trận chuẩn y = xAT + b, nên nó không nhận tensor biểu diễn không gian 3D (C, H, W) của ảnh, mà yêu cầu dữ liệu phải được bẻ phẳng thành một vector 1D (thường kèm chiều batch thành 2D: [Batch, Features]).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 64 [SKILL-CV-29] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi nhắc đến kiến trúc phân loại ảnh CNN tiêu chuẩn, phần ” Trích xuất đặc trưng”
(Feature Extractor / Backbone) bao gồm các loại lớp mạng nào?

- **A.** Các lớp Tích chập (Conv2d), Hàm kích hoạt (ReLU/Hardswish) và Gộp (Pooling).
- **B.** Lớp Softmax ở cuối cùng kết hợp với hàm mất mát Cross-Entropy.
- **C.** Khối mã hóa vị trí (Positional Encoding) và Cơ chếchú ý (Attention).
- **D.** Chỉ bao gồm các lớp Linear (Kết nối đầy đủ) và Dropout.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Trong CNN, phần đầu của mạng (Backbone) làm nhiệm vụ Trích xuất đặc trưng không gian thông qua các phép toán tích chập, kích hoạt phi tuyến và gộp ảnh, trước khi chuyển giao tensor cho bộ phân loại (classifier).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Trong CNN, phần đầu của mạng (Backbone) làm nhiệm vụ Trích xuất đặc trưng không gian thông qua các phép toán tích chập, kích hoạt phi tuyến và gộp ảnh, trước khi chuyển giao tensor cho bộ phân loại (classifier).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 65 [SKILL-CV-30] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Dưới góc nhìn toán học trong Học sâu, một ” Hình ảnh” đầu vào mạng nơ-ron có thể
coi là một cấu trúc dữ liệu nào?

- **A.** Tensor (Mảng số học đa chiều) chứa các giá trịthực.
- **B.** Ma trận thưa (Sparse matrix) với hầu hết giá trịbằng không.
- **C.** Hàm mật độxác suất liên tục.
- **D.** Phương trình vi phân bậc hai có hướng.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Hình ảnh là một lưới rời rạc các điểm ảnh.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Hình ảnh là một lưới rời rạc các điểm ảnh. Trong PyTorch hoặc TensorFlow, lưới này được biểu diễn chính xác bằng một Tensor (mảng n chiều) chứa các số thực (thường chuẩn hóa về khoảng [0, 1] hoặc [−1, 1]).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 66 [SKILL-CV-31] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khả năng ” Bất biến tịnh tiến cục bộ” (Local Translation Invariance) của CNN (ví dụ:
nhận diện được con mèo dù nó nằm lệch sang trái một chút) chủ yếu đến từ cơ chế
nào?

- **A.** Nhờ lớp Dropout tự động loại bỏ các điểm ảnh ở biên.
- **B.** Nhờ việc chia sẻtrọng số của bộ lọc Tích chập và cơ chếchọn lọc giá trịcủa lớp Gộp (Pooling).
- **C.** Nhờ quá trình Chuẩn hóa theo lô (Batch Normalization) cân bằng dữ liệu.
- **D.** Nhờ hàm mất mát Cross Entropy có khả năng bỏ qua các nhãn sai.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Filter tích chập quét qua toàn bộ bức ảnh (chia sẻtrọng số), do đó có thểphát hiện đặc trưng dù nó ở đâu.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Filter tích chập quét qua toàn bộ bức ảnh (chia sẻtrọng số), do đó có thểphát hiện đặc trưng dù nó ở đâu. Kết hợp với Pooling (lấy giá trịnổi bật nhất trong vùng lân cận), mạng trởnên bất biến với các phép tịnh tiến nhỏ.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 67 [SKILL-CV-32] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi áp dụng phương pháp Dropout vào mạng nơ-ron đểchống quá khớp, ta thường
nên thiết lập tham số xác suất p (xác suất đặt nơ-ron về0) ở khoảng nào là phổ biến
và hợp lý nhất?

- **A.** Bắt buộc cố định tại 1.0
- **B.** Luôn luôn đặt trên 0.8
- **C.** Từ0.2 đến 0.5
- **D.** Từ0.001 đến 0.01

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Thông thường, xác suất p trong Dropout được thiết lập trong khoảng 0.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Thông thường, xác suất p trong Dropout được thiết lập trong khoảng 0.2 −0.5. Nếu thấp quá thì không có tác dụng điều chuẩn, nếu cao quá (ví dụ0.9) mạng sẽbị mất quá nhiều thông tin và khó hội tụ (underfitting).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 68 [SKILL-CV-33] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Các bản đồđặc trưng (Feature maps) học được ở các lớp Tích chập đầu tiên (gần với
ảnh đầu vào nhất) thường phản ánh những thông tin hình ảnh nào?

- **A.** Là các bộ phận hoàn chỉnh của đối tượng như mắt, mũi, bánh xe hay đường viền phức tạp của cơ thể (High-level semantics)
- **B.** Là các đặc trưng ngữ cảnh bao quát toàn cục của bức ảnh (Global Contextual Features) phản ánh nội dung ngữ nghĩa tổng thể
- **C.** Là các đặc trưng cấp thấp (Low-level features) như đường thẳng, mép cạnh, góc giao điểm và các mảng màu sắc cục bộ
- **D.** Là các phân bố xác suất ngữ nghĩa trừu tượng được ánh xạ trực tiếp vào không gian tiềm ẩn đa chiều (Latent Space)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Do Receptive Field ở các lớp đầu còn rất nhỏ, các filter chỉ nhìn thấy các mảng pixel cục bộ hẹp.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Do Receptive Field ở các lớp đầu còn rất nhỏ, các filter chỉ nhìn thấy các mảng pixel cục bộ hẹp. Chúng học cách phát hiện sự thay đổi độdốc pixel (edges/gradients) hoặc các mảng màu, tần số không gian cơ bản.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 69 [SKILL-CV-34] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong PyTorch, nn. Module đóng vai trò nền tảng gì?

- **A.** Là lớp cơ sở (Base class) bắt buộc kếthừa cho mọi mô hình và thành phần mạng nơ-ron.
- **B.** Là hàm hỗ trợchuyển đổi dữ liệu tensor từ định dạng CPU sang GPU.
- **C.** Là hàm kích hoạt mặc định tự động được gọi trong mọi mạng tích chập.
- **D.** Là đối tượng lưu trữthuật toán tối ưu hóa (optimizer) dùng đểcập nhật gradient.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: nn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: nn. Module là lớp cha cốt lõi trong PyTorch. Bất kỳkiến trúc CNN (như ResNet) hay module do người dùng tự định nghĩa (như SimpleCNN) đều phải kếthừa nn. Module và triển khai hàm forward().
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 70 [SKILL-CV-35] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Các phương pháp như Dropout, Data Augmentation, L2 Weight Decay và Early Stopping
được xếp chung vào nhóm kỹ thuật nào trong lĩnh vực Học máy?

- **A.** Điều chuẩn (Regularization)
- **B.** Tối ưu hóa siêu tham số (Hyperparameter Optimization)
- **C.** Khai phá dữ liệu (Data Mining)
- **D.** Lựa chọn đặc trưng (Feature Selection)

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Điều chuẩn (Regularization) là tập hợp các kỹ thuật được thiết kếnhằm đưa thêm các ràng buộc vào quá trình huấn luyện, làm giảm độphức tạp của hàm giả thuyết, từ đó giúp mô hình tránh việc ghi nhớcục bộ (Overfitting) và tổng quát hóa tốt hơn trên dữ liệu mới.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Điều chuẩn (Regularization) là tập hợp các kỹ thuật được thiết kếnhằm đưa thêm các ràng buộc vào quá trình huấn luyện, làm giảm độphức tạp của hàm giả thuyết, từ đó giúp mô hình tránh việc ghi nhớcục bộ (Overfitting) và tổng quát hóa tốt hơn trên dữ liệu mới.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.2 Pooling & Trường Thụ Cảm (Receptive Field)**.

---

### Câu 71 [SKILL-CV-36] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho một ảnh đầu vào đen trắng (1 kênh) có kích thước không gian $28 \times 28$ (giống tập
MNIST). Bạn áp dụng một lớp nn. Conv2d với kernel_size=3, stride=1, và KHÔNG dùng
padding (padding=0). Kích thước không gian (chiều cao × chiều rộng) của bản đồđặc
trưng (Feature map) đầu ra là bao nhiêu?

- **A.** $28 \times 28$
- **B.** $14 \times 14$
- **C.** $30 \times 30$
- **D.** $26 \times 26$

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Công thức tính kích thước không gian đầu ra của Tích chập vuông: Wout = ⌊Win−K+2P S ⌋+ 1.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Công thức tính kích thước không gian đầu ra của Tích chập vuông: Wout = ⌊Win−K+2P S ⌋+ 1. Thay số: Wout = ⌊28−3+0 ⌋+ 1 = 25 + 1 = 26. Output có shape $26 \times 26$.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 72 [SKILL-CV-37] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Bạn có một bản đồđặc trưng (Feature map) kích thước không gian là $32 \times 32$. Bạn
đưa nó qua một lớp Gộp cực đại nn. MaxPool2d(kernel_size=2, stride=2). Kích thước
không gian của tensor đầu ra sẽlà:

- **A.** $64 \times 64$
- **B.** $31 \times 31$
- **C.** $16 \times 16$
- **D.** $30 \times 30$

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Lớp MaxPool với kernel=2 và stride=2 sẽlàm giảm kích thước của bản đồđặc trưng đi một nửa ởcả2 trục không gian.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Lớp MaxPool với kernel=2 và stride=2 sẽlàm giảm kích thước của bản đồđặc trưng đi một nửa ởcả2 trục không gian. Áp dụng công thức: Wout = ⌊32−2 2 ⌋+1 = 15+1 = 16. Kích thước output là $16 \times 16$.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 73 [SKILL-CV-38] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Giả sử bạn có một tensor x có kích thước (shape) là (Batch=16, Channels=64, Height=5,
Width=5). Trong PyTorch, khi bạn gọi lệnh làm phẳng x = torch.flatten(x, 1), tensor
đầu ra sẽcó kích thước (shape) là bao nhiêu?

- **A.** (1, 25600)
- **B.** (16, 64, 25)
- **C.** (16, 1600)
- **D.** (1600)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Hàm torch.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Hàm torch.flatten(x, start_dim=1) làm phẳng tensor bắt đầu từ chiều số1 (Channels) trởđi, giữ nguyên chiều số0 (Batch size). Số đặc trưng của mỗi ảnh sẽlà tích các chiều từ1: $64 \times 5$ × 5 = 1600. Tensor mới có shape (16, 1600).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 74 [SKILL-CV-39] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hàm nn. Linear(in_features=128, out_features=10) (với tham số bias mặc định) sẽtạo
ra tổng cộng bao nhiêu tham số (parameters) có thểhọc được?

- **A.** 138
- **B.** 128
- **C.** 1290
- **D.** 1280

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Số tham số trong một lớp Linear (hay Fully Connected) bao gồm cả ma trận trọng số và vector bias.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Số tham số trong một lớp Linear (hay Fully Connected) bao gồm cả ma trận trọng số và vector bias. Công thức là: (in_features × out_features) + out_features. Tính toán: ($128 \times 10$) + 10 = 1280 + 10 = 1290 tham số.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 75 [SKILL-CV-40] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho một lớp Tích chập PyTorch: nn. Conv2d(in_channels=1, out_channels=32, kernel_size=3).
Giả sử lớp này sử dụng bias mặc định. Tổng số tham số (parameters) cần huấn luyện
của lớp này là bao nhiêu?

- **A.** 96
- **B.** 320
- **C.** 288
- **D.** 1024

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Tham số lớp Tích chập: (K × K × Cin × Cout) + Cout(nếu có bias).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Tham số lớp Tích chập: (K × K × Cin × Cout) + Cout(nếu có bias). Tính: ($3 \times 3$ × $1 \times 32$) + 32 = $9 \times 32$ + 32 = 288 + 32 = 320 tham số có thểhọc được.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.1 Lớp Convolution & Công thức Kích thước Đầu ra**.

---

### Câu 76 [SKILL-CV-41] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Xem xét dòng mã x = self.pool(F.relu(self.conv1(x))) trong phương thức forward.
Trình tự toán học áp dụng lên tensor x từ trong ra ngoài là gì?

- **A.** Pool →ReLU →Conv1
- **B.** Conv1 →ReLU →Pool
- **C.** ReLU →Conv1 →Pool
- **D.** Tất cả các hàm này được tính toán đồng thời đểtiết kiệm thời gian.

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Theo quy tắc thực thi hàm lồng nhau của Python, biểu thức trong cùng được tính trước.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Theo quy tắc thực thi hàm lồng nhau của Python, biểu thức trong cùng được tính trước. Tensor x đầu tiên đi qua lớp tích chập (self.conv1(x)), sau đó kết quảbịđưa qua hàm kích hoạt (F.relu(...)), và cuối cùng được đưa qua lớp gộp (self.pool(...)).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 77 [SKILL-CV-42] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong khối Thặng dư (Residual block) của mạng ResNet, phép toán kết nối tắt y =
F(x)+x được thực hiện. Giả sử tensor đầu vào x có kích thước là (Batch=1, Channels=256,
H=56, W=56). Đểphép cộng này hợp lệ, tensor F(x) trảvềtừ nhánh chính (nhánh Tích
chập) bắt buộc phải có kích thước bao nhiêu?

- **A.** (1, 256, 28, 28)
- **B.** (1, 128, 112, 112)
- **C.** (1, 512, 28, 28)
- **D.** (1, 256, 56, 56)

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Trong toán học Tensor, phép cộng từng phần tử (element-wise addition) như F(x) + x yêu cầu hai tensor F(x) và x phải có cùng chính xác mọi chiều không gian và kênh.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Trong toán học Tensor, phép cộng từng phần tử (element-wise addition) như F(x) + x yêu cầu hai tensor F(x) và x phải có cùng chính xác mọi chiều không gian và kênh. Do đó shape của F(x) phải khớp với x là (1, 256, 56, 56).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 78 [SKILL-CV-43] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Bạn muốn tăng cường dữ liệu bằng cách Cắt ngẫu nhiên (Random Crop) một hình
ảnh. Ảnh gốc có kích thước $256 \times 256$ pixel. Bạn muốn lấy các vùng crop kích thước
$224 \times 224$ pixel. Về mặt lý thuyết, có tối đa bao nhiêu vị trí crop (cửa sổtrượt hợp lệ)
khác nhau có thểđược tạo ra từ ảnh gốc này?

- **A.** 1024
- **B.** 33
- **C.** 224
- **D.** 1089

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Số vị trí hợp lệcho tọa độpixel X của góc trên cùng bên trái của vùng crop là (256 −224 + 1) = 33 vị trí.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Số vị trí hợp lệcho tọa độpixel X của góc trên cùng bên trái của vùng crop là (256 −224 + 1) = 33 vị trí. Tương tự đối với trục Y cũng có 33 vị trí hợp lệ. Tổng số vị trí crop khác nhau là $33 \times 33$ = 1089 tổhợp không gian.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 79 [SKILL-CV-44] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Bạn đang thay thếlớp phân loại của một mô hình resnet18 được tải từtorchvision.models.
Dựa vào mã nguồn của ResNet, dòng mã nào sau đây trích xuất ĐÚNG số đặc trưng
đầu vào (in_features) của lớp classifier nguyên bản?

- **A.** in_features = self.backbone.classifier.in_features
- **B.** in_features = self.backbone.head.in_features
- **C.** in_features = self.backbone.fc.in_features
- **D.** in_features = self.backbone[-1].in_features

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Theo kiến trúc thiết kếchuẩn của mạng ResNet trong PyTorch, lớp Linear cuối cùng đảm nhiệm phân loại được gán cứng vào thuộc tính có tên là fc.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Theo kiến trúc thiết kếchuẩn của mạng ResNet trong PyTorch, lớp Linear cuối cùng đảm nhiệm phân loại được gán cứng vào thuộc tính có tên là fc. Do đó, đểlấy số lượng node đầu vào của lớp này, ta phải truy xuất self.backbone.fc.in_features.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 80 [SKILL-CV-45] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi bạn tùy chỉnh một mô hình efficientnet_b0, phần phân loại của nó sử dụng một
nn. Sequential chứa nhiều lớp. Dòng mã nào ĐÚNG đểlấy in_features từ nhánh linear
nguyên bản?

- **A.** in_features = self.backbone.classifier[0].in_features
- **B.** in_features = self.backbone.fc.in_features
- **C.** in_features = self.backbone.classifier[1].in_features
- **D.** in_features = self.backbone.features.in_features

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Trong cấu trúc thuộc tính classifier của EfficientNet, lớp thứ0 thường là một lớp Dropout, và lớp thứ1 mới là nn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Trong cấu trúc thuộc tính classifier của EfficientNet, lớp thứ0 thường là một lớp Dropout, và lớp thứ1 mới là nn. Linear. Do đó, thuộc tính in_features phải được truy xuất từ lớp thứ1 qua cú pháp list: self.backbone.classifier[1].in_features.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 81 [SKILL-CV-46] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Đối với mobilenet_v3_small, thuộc tính classifier cũng bao gồm nhiều khối lớp. Theo
thiết kếmặc định, lớp Linear đầu tiên (nhận dữ liệu từ backbone) nằm ở vị trí chỉ mục
(index) nào trong nn. Sequential của classifier?

- **A.** Chỉ mục 3: classifier[3].in_features
- **B.** Chỉ mục 0: classifier[0].in_features
- **C.** mobilenet_v3_small sử dụng thuộc tính fc tương tự như ResNet.
- **D.** Chỉ mục 1: classifier[1].in_features

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Đối với MobileNetV3, sau lớp gộp thích ứng (Adaptive Pooling), tensor lập tức được đưa vào một lớp Linear để giảm chiều, lớp này nằm ngay ở vị trí đầu tiên của module classifier, nên ta lấy bằng self.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Đối với MobileNetV3, sau lớp gộp thích ứng (Adaptive Pooling), tensor lập tức được đưa vào một lớp Linear để giảm chiều, lớp này nằm ngay ở vị trí đầu tiên của module classifier, nên ta lấy bằng self.backbone.classifier[0].in_features.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `B` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 82 [SKILL-CV-47] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Giả sử một phép tích chập chuẩn có Cin = 32, Cout = 64, kernel_size=$3 \times 3$. Tổng số tham
số (không tính bias) là $3 \times 3$ × $32 \times 64$ = 18, 432. Nếu thay thếbằng cơ trúc Tích chập
Tách rời theo độsâu (Depthwise Separable) của MobileNet, tổng số tham số (không
bias) sẽxấp xỉlà bao nhiêu?

- **A.** 9,216
- **B.** 18,432
- **C.** 288
- **D.** 2,336

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Với Depthwise Separable, bước 1 (Depthwise - mỗi kênh 1 bộ lọc riêng) tốn $3 \times 3$×$32 \times 1$ = 288 tham số.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Với Depthwise Separable, bước 1 (Depthwise - mỗi kênh 1 bộ lọc riêng) tốn $3 \times 3$×$32 \times 1$ = 288 tham số. Bước 2 (Pointwise - kết hợp bằng $1 \times 1$) tốn $1 \times 1$×$32 \times 64$ = 2048 tham số. Tổng = 288 + 2048 = 2336 tham số. Lượng tham số giảm được gần 8 lần!
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 83 [SKILL-CV-48] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Phân tích Vùng tiếp nhận (Receptive Field): Giả sử hình ảnh gốc đi qua liên tiếp hai
lớp Conv2d(kernel_size=3, stride=1, padding=0). Kích thước Vùng tiếp nhận của một
điểm ảnh (pixel) tại đầu ra lớp thứ2, chiếu ngược về mặt không gian của ảnh gốc là
bao nhiêu?

- **A.** $9 \times 9$
- **B.** $6 \times 6$
- **C.** $5 \times 5$
- **D.** $3 \times 3$

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Qua lớp 1, một pixel nhìn thấy một vùng $3 \times 3$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Qua lớp 1, một pixel nhìn thấy một vùng $3 \times 3$. Lớp 2 dùng một filter $3 \times 3$ quét qua các ” pixel” đầu ra của lớp 1. Nó sẽnhìn thấy tâm $3 \times 3$ cộng thêm 1 pixel lan rộng ở mỗi lề (trái, phải, trên, dưới). Vùng nhìn thực tếlà 3 + (3 −1) = $5 \times 5$.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 84 [SKILL-CV-49] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kích thước (shape) của Tensor đầu ra sẽlà gì nếu cho một Tensor đầu vào có shape
(Batch=8, C=3, H=32, W=32) đi qua lớp nn. Conv2d(in_channels=3, out_channels=16, kernel_size=
padding=' same ', stride=1)?

- **A.** (16, 3, 32, 32)
- **B.** (8, 16, 30, 30)
- **C.** (8, 16, 32, 32)
- **D.** (8, 3, 30, 30)

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Vì padding=' same ' và stride=1, kích thước không gian H và W được bảo toàn là $32 \times 32$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Vì padding=' same ' và stride=1, kích thước không gian H và W được bảo toàn là $32 \times 32$. Số kênh đặc trưng (Channels) được ánh xạtừ Cin = 3 sang Cout = 16. Chiều Batch=8 giữ nguyên. Do đó, shape mới là (8, 16, 32, 32).
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 85 [SKILL-CV-50] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong PyTorch, khi khởi tạo lớp Gộp cực đại bằng mã nguồn nn. MaxPool2d(2, 2), hai
số2 được truyền vào tương ứng với các đối số (arguments) mặc định nào?

- **A.** stride=2 và padding=2
- **B.** in_channels=2 và out_channels=2
- **C.** kernel_size=2 và stride=2
- **D.** kernel_size=2 và padding=2

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Trong API định nghĩa torch.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Trong API định nghĩa torch.nn. MaxPool2d, tham số truyền vào đầu tiên và thứ hai theo thứtựsẽthiết lập kích thước bộ lọc (kernel_size) và bước nhảy (stride). Lớp mạng này sẽdùng một khung $2 \times 2$ và di chuyển với bước nhảy 2.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 86 [SKILL-CV-51] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong thiết kế Tích chập tách rời theo chiều sâu (Depthwise Separable Convolution)
của MobileNet, mục đích cụthểcủa lớp tích chập điểm (Pointwise Convolution, hay
tích chập $1 \times 1$) là gì?

- **A.** Tuyến tính hóa và kết hợp thông tin đặc trưng chéo giữa các kênh với nhau.
- **B.** Thu nhỏ kích thước hình ảnh (giảm Height và Width).
- **C.** Học các đặc trưng không gian trên từng kênh màu độc lập.
- **D.** Thêm lớp đệm (padding) tự động cho ảnh.

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Sau khi Depthwise trích xuất đặc trưng không gian độc lập trên từng kênh, Pointwise (dùng kernel $1 \times 1$) sẽtính tổng có trọng số xuyên suốt chiều sâu của các kênh này đểkết hợp tạo ra bộ đặc trưng mới.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Sau khi Depthwise trích xuất đặc trưng không gian độc lập trên từng kênh, Pointwise (dùng kernel $1 \times 1$) sẽtính tổng có trọng số xuyên suốt chiều sâu của các kênh này đểkết hợp tạo ra bộ đặc trưng mới.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `A` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 87 [SKILL-CV-52] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Hành vi của lớp Dropout trong PyTorch thay đổi như thế nào khi chuyển mô hình sang
chếđộđánh giá (model.eval())?

- **A.** Tập hợp nơ-ron bị tắt sẽđược cố định và không thay đổi giữa các hình ảnh đầu vào khác nhau.
- **B.** Hàm mất mát sẽbỏ qua các nơ-ron có giá trị0 do Dropout gây ra.
- **C.** Tỷ lệ Dropout tự động được nhân đôi đểtăng tính ổn định của kết quảdự đoán.
- **D.** Lớp Dropout bị vô hiệu hóa, tất cả các nơ-ron đều được kích hoạt với trọng số giữ nguyên tỉlệ.

**Đáp án chính xác:** `D`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Trong lúc suy luận (Inference/Evaluation), mô hình không cần điều chuẩn (không cần chống overfit nữa), nên Dropout được tắt hoàn toàn đểtận dụng năng lực của tất cả các nơ-ron nhằm cho ra kết quảdự đoán chính xác nhất.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Trong lúc suy luận (Inference/Evaluation), mô hình không cần điều chuẩn (không cần chống overfit nữa), nên Dropout được tắt hoàn toàn đểtận dụng năng lực của tất cả các nơ-ron nhằm cho ra kết quảdự đoán chính xác nhất.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `D` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 88 [SKILL-CV-53] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cho một bản đồđặc trưng có kích thước $32 \times 32$. Nếu cho bản đồnày đi qua một lớp
tích chập có kernel_size=3, stride=2, padding=1, thì kích thước của bản đồđặc trưng
đầu ra sẽlà bao nhiêu?

- **A.** $15 \times 15$
- **B.** $17 \times 17$
- **C.** $16 \times 16$
- **D.** $32 \times 32$

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Áp dụng công thức Wout = ⌊Win+2P−K S ⌋+ 1.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Áp dụng công thức Wout = ⌊Win+2P−K S ⌋+ 1. Thay số: Wout = ⌊32+2(1)−3 ⌋+ 1 = ⌊31 2 ⌋+ 1 = 15 + 1 = 16. Kích thước thu được là $16 \times 16$.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 89 [SKILL-CV-54] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong quá trình Fine-tuning một mô hình Custom Head cho bài toán phân loại ảnh
với tập dữ liệu rất nhỏ, điều gì có thểxảy ra nếu bạn bỏ quên việc đóng băng (freeze)
các trọng số của backbone?

- **A.** Các trọng số của backbone sẽ tự động suy biến về giá trị 0 sau một epoch (Weight Collapse) do không nhận được tín hiệu gradient phản hồi
- **B.** Mô hình sẽ huấn luyện nhanh hơn và tiêu tốn ít dung lượng bộ nhớ VRAM của GPU hơn (Memory Reduction) do kích thước đồ thị tính toán co lại
- **C.** Backbone có nguy cơ bị phá vỡ các đặc trưng tổng quát đã học (Catastrophic Forgetting) và dẫn đến tình trạng quá khớp nghiêm trọng
- **D.** Mô hình sẽ không thể tính toán được hàm mất mát phân loại (Gradient Synchronization Failure) do xảy ra hiện tượng mất đồng bộ giữa các tầng

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Khi dữ liệu mới quá nhỏ, việc mở băng (unfreeze) toàn bộ mạng sâu sẽkhiến các trọng số bị cập nhật mạnh bởi tín hiệu nhiễu từ bộ phân loại chưa khởi tạo, dẫn đến phá hủy các đặc trưng tổng quát (Catastrophic Forgetting) và dễquá khớp.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Khi dữ liệu mới quá nhỏ, việc mở băng (unfreeze) toàn bộ mạng sâu sẽkhiến các trọng số bị cập nhật mạnh bởi tín hiệu nhiễu từ bộ phân loại chưa khởi tạo, dẫn đến phá hủy các đặc trưng tổng quát (Catastrophic Forgetting) và dễquá khớp.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 90 [SKILL-CV-55] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Giả sử bạn có tensor đầu vào với số kênh (channels) là 128. Bạn áp dụng một lớp tích
chập Pointwise ($1 \times 1$) với out_channels=256 và bias=False. Số lượng tham số cần thiết
cho lớp mạng này là bao nhiêu?

- **A.** 1,152
- **B.** 33,024
- **C.** 32,768
- **D.** 256

**Đáp án chính xác:** `C`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
Bản chất thị giác máy tính: Một lớp tích chập Pointwise có kernel $1 \times 1$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
1. Nhận diện các tham số không gian: Chiều ảnh, kích thước bộ lọc (kernel), bước trượt (stride), phần đệm (padding) hoặc số kênh (channels).
2. Áp dụng công thức và tính toán: Một lớp tích chập Pointwise có kernel $1 \times 1$. Công thức tính tham số (khi không bias) là K × K × Cin × Cout. Thay số: $1 \times 1$ × $128 \times 256$ = 32, 768 tham số.
3. Đối chiếu kết quả với các phương án lựa chọn: Phương án `C` khớp chính xác với đáp án giải tích.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
Cẩn thận bẫy tính số tham số: Phân biệt rõ có bias hay không có bias ($+1$ cho mỗi filter), và phân biệt giữa tích chập thông thường với tích chập tách biệt theo chiều sâu (Depthwise Separable).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 Giáo trình *Deep Learning for Computer Vision* (Stanford CS231n) và *SkillPixel Session 9*. Xem **§3.3 Các Kiến trúc CNN Kinh Điển**.

---

### Câu 91 [SKILL-CV-56] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Vision Transformer (ViT-Base) áp dụng cho ảnh đầu vào kích thước $224 \times 224 \times 3$ với kích thước mảnh patch $P = 16$, số lượng token đầu vào cung cấp cho khối Transformer Encoder (sau khi thêm token đặc biệt [CLS]) bằng bao nhiêu?

- **A.** 196 token biểu diễn không gian ảnh kèm theo 1 token [CLS], tổng cộng là 197 token
- **B.** 256 token biểu diễn không gian ảnh kèm theo 1 token [CLS], tổng cộng là 257 token
- **C.** 144 token biểu diễn không gian ảnh kèm theo 1 token [CLS], tổng cộng là 145 token
- **D.** 224 token biểu diễn không gian ảnh kèm theo 1 token [CLS], tổng cộng là 225 token

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Cắt bức ảnh $224 \times 224$ thành các ô vuông nhỏ $16 \times 16$. Số ô theo chiều ngang là $224 / 16 = 14$, số ô theo chiều dọc là $224 / 16 = 14$. Tổng số ô (patches) là $14 \times 14 = 196$. Thêm 1 thẻ đặc biệt [CLS] ở đầu để đại diện cho toàn bộ bức ảnh $\implies$ Tổng cộng có $196 + 1 = 197$ token.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Số lượng patch: $N = (H / P) \times (W / P) = (224 / 16) \times (224 / 16) = 14 \times 14 = 196$.
Sau khi cộng thêm token phân loại [CLS]: $N_{\text{total}} = 196 + 1 = 197$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:**
- Phương án B (257): Nhầm tưởng chia ảnh theo lũy thừa 2 là $16 \times 16 = 256$.
- Phương án C (145): Nhầm kích thước patch là $P = 18$ hoặc tính sai $12 \times 12 = 144$.
- Phương án D (225): Nhầm $15 \times 15 = 225$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.8 Vision Transformer (ViT)**.

---

### Câu 92 [SKILL-CV-57] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Khi áp dụng kỹ thuật tinh chỉnh tham số hiệu quả LoRA (Low-Rank Adaptation) lên một ma trận trọng số tuyến tính $W_0 \in \mathbb{R}^{4096 \times 4096}$ với hạng phân rã $r = 16$, số lượng tham số có thể huấn luyện được (trainable parameters) của cặp ma trận thích ứng $A$ và $B$ bằng bao nhiêu?

- **A.** 65.536 tham số học (giảm 99.6% so với 16.777.216 tham số ban đầu của lớp)
- **B.** 131.072 tham số học (giảm 99.2% so với 16.777.216 tham số ban đầu của lớp)
- **C.** 262.144 tham số học (giảm 98.4% so với 16.777.216 tham số ban đầu của lớp)
- **D.** 524.288 tham số học (giảm 96.8% so với 16.777.216 tham số ban đầu của lớp)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Thay vì học lại cả ma trận khổng lồ $4096 \times 4096$ (gần 16.8 triệu số), LoRA tách thay đổi $\Delta W$ thành tích hai ma trận hẹp: $B \in \mathbb{R}^{4096 \times 16}$ và $A \in \mathbb{R}^{16 \times 4096}$.
Số lượng số cần học chỉ là: $4096 \times 16 + 16 \times 4096 = 131.072$ tham số!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Ma trận $W_0 \in \mathbb{R}^{d \times k}$ với $d = 4096, k = 4096, r = 16$.
- Ma trận $A \in \mathbb{R}^{r \times k} \implies |A| = 16 \times 4096 = 65.536$.
- Ma trận $B \in \mathbb{R}^{d \times r} \implies |B| = 4096 \times 16 = 65.536$.
Tổng tham số: $|A| + |B| = 65.536 + 65.536 = 131.072$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A chỉ tính 1 ma trận duy nhất ($65.536$) mà quên mất LoRA cần tích của 2 ma trận $B \times A$.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.6 Kiến Trúc Transformer: Self-Attention & Multi-Head**.

---

### Câu 93 [SKILL-CV-58] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Thuật toán FlashAttention giúp tăng tốc đáng kể cơ chế Self-Attention trên GPU hiện đại chủ yếu nhờ vào cải tiến kiến trúc phần cứng nào sau đây?

- **A.** Giảm thiểu số lượng phép tính FLOPs bằng cách lượng tử hóa trọng số ma trận sang số nguyên INT4 (Weight Quantization Mode)
- **B.** Phân chia ma trận thành các khối nhỏ (Tiling) để tối ưu hóa truy cập đọc ghi dữ liệu trên bộ nhớ đệm nhanh SRAM của GPU
- **C.** Loại bỏ hoàn toàn bước tính toán hàm Softmax để chuyển thành tích vô hướng tuyến tính (Linear Attention Approximation)
- **D.** Thực hiện song song hóa hoàn toàn dọc theo chiều không gian bằng mạng tích chập cục bộ (Spatial Convolution Parallelism)

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nút thắt cổ chai của Attention không phải do tính toán chậm, mà do tốc độ truyền dữ liệu từ bộ nhớ lớn (HBM) vào bộ nhớ siêu nhanh của chip (SRAM). FlashAttention chia nhỏ ma trận thành từng khối vừa khít SRAM (Tiling) và tính Softmax online trực tiếp trong SRAM, tránh ghi ma trận trung gian $N \times N$ ra HBM.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Độ phức tạp bộ nhớ HBM giảm từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$ nhờ thuật toán Online Softmax và Tiling. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** FlashAttention là thuật toán chính xác tuyệt đối (exact attention), không hề xấp xỉ FLOPs hay bỏ Softmax (tránh nhầm với Linear Attention hay Quantization).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.6 Kiến Trúc Transformer: Self-Attention & Multi-Head**.

---

### Câu 94 [SKILL-CV-59] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Cơ chế mã hóa vị trí quay RoPE (Rotary Position Embedding) được sử dụng phổ biến trong các mô hình LLaMA và Transformer hiện đại sở hữu đặc tính toán học ưu việt nào sau đây?

- **A.** Cộng trực tiếp vector vị trí tuyệt đối vào vector nhúng từ ban đầu ở lớp tiền xử lý
- **B.** Nhúng vị trí tương đối thông qua phép quay ma trận trực giao lên các cặp tọa độ vector
- **C.** Học vector vị trí động bằng một mạng hồi quy LSTM phụ trợ chạy song song với Attention
- **D.** Gán trọng số suy giảm hàm mũ cố định cho khoảng cách token mà không cần phép biến đổi

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Thay vì cộng thêm số (như Positional Encoding gốc của Transformer), RoPE xoay vector truy vấn $Q$ và vector khóa $K$ theo một góc tỉ lệ với vị trí của từ. Khi tính tích vô hướng $Q^T K$, tích số chỉ phụ thuộc vào góc xoay tương đối giữa hai từ $(m - n)$, giúp mô hình nắm bắt vị trí tương đối cực kỳ tự nhiên.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 RoPE áp dụng ma trận trực giao $R_{\Theta, m}^d$ lên vector $x_m$: $\langle R_{\Theta, m} q, R_{\Theta, n} k \rangle = g(q, k, m - n)$. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án A là Absolute Positional Encoding truyền thống. Phương án D là cơ chế ALiBi (Attention with Linear Biases).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.6 Kiến Trúc Transformer: Self-Attention & Multi-Head**.

---

### Câu 95 [SKILL-CV-60] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong các mô hình khuếch tán tạo ảnh (Diffusion Models như Stable Diffusion), cơ chế Classifier-Free Guidance (CFG) với hệ số hướng dẫn $w > 1$ hoạt động theo công thức dự đoán nhiễu nào sau đây?

- **A.** $\hat{\epsilon}_t = \epsilon_\theta(x_t, \emptyset) + w \cdot (\epsilon_\theta(x_t, c) - \epsilon_\theta(x_t, \emptyset))$ giúp tăng độ bám sát văn bản mô tả
- **B.** $\hat{\epsilon}_t = \epsilon_\theta(x_t, c) + w \cdot (\epsilon_\theta(x_t, \emptyset) - \epsilon_\theta(x_t, c))$ giúp tăng tính đa dạng ngẫu nhiên
- **C.** $\hat{\epsilon}_t = w \cdot \epsilon_\theta(x_t, c) \cdot \epsilon_\theta(x_t, \emptyset)$ kết hợp phi tuyến theo tích ma trận xác suất
- **D.** $\hat{\epsilon}_t = \frac{1}{w} \cdot \epsilon_\theta(x_t, c) + \frac{w-1}{w} \cdot \epsilon_\theta(x_t, \emptyset)$ chuẩn hóa tuyến tính convex combination

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
CFG lấy hướng đi từ ' vẽ tự do không điều kiện ' $\epsilon(x_t, \emptyset)$ sang ' vẽ có điều kiện văn bản ' $\epsilon(x_t, c)$, rồi phóng đại hướng đi đó lên $w$ lần. Nhờ đó, bức ảnh tạo ra bám cực sát vào câu lệnh prompt của người dùng.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 $\hat{\epsilon}_t = \epsilon_\theta(x_t, \emptyset) + w (\epsilon_\theta(x_t, c) - \epsilon_\theta(x_t, \emptyset)) = (1 - w)\epsilon_\theta(x_t, \emptyset) + w\epsilon_\theta(x_t, c)$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Phương án B bị đảo ngược dấu vector sai lệch, dẫn đến việc triệt tiêu điều kiện thay vì khuếch đại.

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 96 [SKILL-CV-61] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Mô hình phân đoạn ảnh vạn năng Segment Anything (SAM của Meta AI) sử dụng thành phần kiến trúc nào để sinh ra các mặt nạ phân đoạn chất lượng cao trong thời gian thực chỉ khoảng 50ms?

- **A.** Image Encoder cấu trúc ViT khổng lồ chạy lại liên tục cho mỗi điểm nhấp chuột tương tác
- **B.** Lightweight Mask Decoder dùng cơ chế Two-Way Cross-Attention giữa Prompt và Image Embedding
- **C.** Mạng đối kháng GAN phân biệt mặt nạ thật giả thông qua tầng Discriminator nhiều lớp
- **D.** Thuật toán quy hoạch động Dijkstra tìm đường bao cắt ngắn nhất trên ma trận gradient ảnh

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
SAM tính toán trước đặc trưng bức ảnh bằng mạng ViT nặng 1 lần duy nhất (lưu trong bộ nhớ). Khi người dùng nhấp chuột hoặc kéo hộp prompt, chỉ có tầng giải mã siêu nhẹ (Lightweight Mask Decoder) chạy qua cơ chế Two-Way Attention trong 50ms để xuất mặt nạ ngay lập tức.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Kiến trúc SAM gồm: Heavy Image Encoder (ViT-H tính 1 lần), Prompt Encoder (sparse/dense prompts), và Lightweight Mask Decoder chạy tương tác thời gian thực. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Image Encoder của SAM rất nặng (chạy mất vài giây), không thể chạy lại mỗi lần tương tác (loại A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 97 [SKILL-CV-62] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong mô hình học biểu diễn đa phương thức CLIP (Contrastive Language-Image Pretraining), hàm mất mát đối chiếu InfoNCE cho một mini-batch gồm $N$ cặp (ảnh, văn bản) được tối ưu hóa như thế nào?

- **A.** Cực đại hóa độ tương đồng Cosine của $N$ cặp đúng và cực tiểu hóa $N^2 - N$ cặp sai trên cả 2 chiều
- **B.** Tối ưu hóa hàm hồi quy Mean Squared Error (MSE) trực tiếp giữa pixel ảnh và token từ ngữ
- **C.** Huấn luyện bộ sinh văn bản Decoder tự hồi quy sinh lại chuỗi mô tả từ vector nhúng của ảnh
- **D.** Sử dụng phân loại nhị phân độc lập từng cặp ảnh văn bản mà không xét ma trận tương quan batch

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Trong lô $N$ ảnh và $N$ câu văn bản, ma trận tương đồng có kích thước $N \times N$. CLIP kéo $N$ cặp ảnh-chữ tương ứng trên đường chéo chính lại gần nhau (Cosine cao) và đẩy $N^2 - N$ cặp lệch nhau ra xa (Cosine thấp) bằng Cross-Entropy đối xứng theo cả chiều ngang và dọc.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Hàm mất mát đối xứng: $\mathcal{L} = \frac{1}{2} (\mathcal{L}_{\text{image-to-text}} + \mathcal{L}_{\text{text-to-image}})$, trong đó mỗi chiều dùng Cross-Entropy trên phân phối Softmax nhiệt độ $\tau$: $p_{i, j} = \frac{\exp(s_{i, j} / \tau)}{\sum_k \exp(s_{i, k} / \tau)}$. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** CLIP không tái tạo ảnh hay sinh văn bản (không dùng MSE hay Autoregressive Decoder).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---

### Câu 98 [SKILL-CV-63] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Trong kiến trúc Mixture of Experts (MoE) áp dụng cho các mô hình ngôn ngữ lớn (như Mixtral 8x7B), hàm mất mát phụ trợ Load Balancing Loss được đưa vào nhằm mục đích cốt lõi nào?

- **A.** Ép buộc tất cả các chuyên gia (experts) phải có trọng số ma trận hoàn toàn giống hệt nhau
- **B.** Ngăn chặn hiện tượng định tuyến mất cân bằng khi router chỉ liên tục dồn token vào một vài expert
- **C.** Triệt tiêu hoàn toàn thành phần gradient ngược của các chuyên gia không được kích hoạt
- **D.** Tăng số lượng chuyên gia được kích hoạt đồng thời cho mỗi token lên tối đa để cải thiện F1

**Đáp án chính xác:** `B`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Nếu không kiểm soát, mạng sẽ sinh ra hiện tượng ' chuyên gia ngôi sao ': bộ định tuyến Router chỉ thích gửi bài cho 1-2 chuyên gia quen thuộc, khiến các chuyên gia khác bị bỏ xó và lãng phí tài nguyên. Load Balancing Loss phạt Router nếu phân phối token giữa các chuyên gia không đồng đều.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Load Balancing Loss: $\mathcal{L}_{\text{aux}} = \alpha \cdot N \sum_{i=1}^N f_i \cdot P_i$, trong đó $f_i$ là tỉ lệ token gửi đến expert $i$, $P_i$ là xác suất trung bình của router dành cho expert $i$. Giá trị cực tiểu đạt được khi token phân bố đều khắp các experts. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** MoE cần các chuyên gia chuyên môn hóa khác nhau (không được giống nhau như phương án A).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§4.6 Kiến Trúc Transformer: Self-Attention & Multi-Head**.

---

### Câu 99 [SKILL-CV-64] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Kiến trúc mạng phát hiện vật thể YOLOv8 chuyển đổi từ thiết kế dựa trên Anchor (Anchor-Based) sang không dùng Anchor (Anchor-Free Decoupled Head) mang lại ưu điểm vượt trội nào?

- **A.** Loại bỏ hoàn toàn các siêu tham số kích thước hộp neo thủ công và tách biệt nhánh phân loại với tọa độ
- **B.** Tăng kích thước ma trận đầu vào lên gấp đôi mà không làm tiêu tốn thêm bộ nhớ đệm đồ họa VRAM
- **C.** Cho phép thay thế toàn bộ thuật toán Non-Maximum Suppression (NMS) bằng một tầng tích chập 1x1
- **D.** Tự động phát hiện các vật thể bị che khuất hoàn toàn mà không cần dữ liệu nhãn giám sát hộp bao

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
YOLOv8 không cần người lập trình phải dùng thuật toán K-Means chọn trước các hộp neo giả định (Anchor boxes) cứng nhắc. Đồng thời, nó tách riêng 2 nhánh: một nhánh chuyên phân loại đồ vật, một nhánh chuyên đo khoảng cách tọa độ (Decoupled Head), giúp mô hình hội tụ nhanh và chính xác hơn.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Anchor-Free dự đoán trực tiếp khoảng cách từ điểm neo tâm đến 4 cạnh của vật thể (Distribution Focal Loss). Decoupled Head giải quyết xung đột đặc trưng giữa nhiệm vụ phân loại (cần bất biến không gian) và định vị (cần nhạy cảm không gian). Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** YOLOv8 vẫn cần NMS ở bước hậu xử lý để lọc trùng (loại C).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện Vật thể (Object Detection): IoU, NMS, mAP, YOLO vs R-CNN**.

---

### Câu 100 [SKILL-CV-65] — Phân hệ Module C (Thang điểm: 1.0đ)

**Đề bài:** Phương pháp tự học biểu diễn thị giác tự giám sát DINO (Self-distillation with no labels) ngăn chặn hiện tượng sụp đổ biểu diễn (Representation Collapse) nhờ kết hợp hai kỹ thuật nào sau đây?

- **A.** Toán tử làm nhọn phân phối xác suất (Sharpening) kết hợp phép dịch tâm (Centering) trên đầu ra của mạng Teacher để cân bằng
- **B.** Kỹ thuật Dropout ngẫu nhiên 90% kết hợp phép chuẩn hóa Batch Normalization trên cả hai mạng Student và Teacher đồng thời
- **C.** Hàm mất mát phân loại có giám sát với nhãn giả ImageNet kết hợp ma trận xoay góc ngẫu nhiên (Rotational Invariance Loss)
- **D.** Cố định vĩnh viễn toàn bộ trọng số của mạng Student và chỉ cập nhật trọng số cho mạng Teacher qua lan truyền ngược chuẩn tắc

**Đáp án chính xác:** `A`

### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiểu nhanh bản chất:**
Khi học không có nhãn, mạng rất dễ bị khôn lỏi: sinh ra cùng một vector giống hệt nhau cho mọi bức ảnh (sụp đổ hoàn toàn). DINO dùng phép ' Centering ' (kéo lùi về tâm để tránh 1 chiều chiếm ưu thế) đối kháng với phép ' Sharpening ' (làm nhọn phân phối để tránh biến thành phân phối đều), tạo thế cân bằng hoàn hảo giúp biểu diễn tự nhiên xuất hiện.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Đầu ra Teacher: $P_t(x) = \text{softmax}((g_t(x) - c) / \tau_t)$. Trong đó $c$ là vector tâm cập nhật bằng Exponential Moving Average ($c \leftarrow m c + (1-m) \frac{1}{B} \sum g_t(x)$) chống sụp đổ về 1 chiều; và nhiệt độ $\tau_t$ nhỏ làm nhọn phân phối chống sụp đổ về phân phối đều. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Cạm bẫy:** Mạng Student được cập nhật bằng SGD/AdamW, mạng Teacher được cập nhật bằng Momentum EMA từ Student (không phải cố định vĩnh viễn như phương án D).

### 4. Mắt xích kiến thức & Căn cứ khoa học
📚 **Căn cứ lý thuyết:** Xem **§3.7 Các Kiến Trúc Deep Learning Tiêu Biểu & SOTA**.

---
