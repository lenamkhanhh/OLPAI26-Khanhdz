# BÁO CÁO NGHIỆM THU TOÀN DIỆN & BÀN GIAO HỆ THỐNG ÔN THI OLYMPIC AI HCMUS 2026 (CHỐT SỔ VÒNG 3)

- **Dự án:** Olympic AI HCMUS 2026 — Academic Arena & Study Hub
- **Thời điểm nghiệm thu chốt sổ:** 09/10/2026 21:00 (Local Time)
- **Mục tiêu:** Bàn giao toàn diện hệ thống ôn thi trước ngày thi chính thức 11/10/2026.
- **Căn cứ đối soát kỹ thuật:**
  1. Yêu cầu chốt nghiệm thu vòng 3: [`docs/PROMPT_GEMINI_CHOT_NGHIEM_THU_LAN_3_2026-10-09.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/PROMPT_GEMINI_CHOT_NGHIEM_THU_LAN_3_2026-10-09.md)
  2. Báo cáo audit độc lập vòng 3: [`docs/VERIFY_NGHIEM_THU_LAN_3_2026-10-09.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/VERIFY_NGHIEM_THU_LAN_3_2026-10-09.md)
  3. Đề thi gốc Ban Tổ Chức: `C:\Users\HP\Downloads\OLPAI\Quizzes\voai2025_original.pdf` (Mã đề 006, 100 câu, 180 phút)
  4. Lời giải đối chiếu bên thứ ba: `C:\Users\HP\Downloads\OLPAI\Quizzes\VOAI_2025_Solution.pdf` (Tác giả Nguyễn Khắc Trung Kiên)
  5. Thư mục video & tài liệu: `C:\Users\HP\Downloads\OLPAI\VOAI NÂNG CAO`

---

## I. TỔNG HỢP HIỆN TRẠNG 6 NGÂN HÀNG ĐỀ THI (448 CÂU HỎI)

Hệ thống lưu trữ **6 ngân hàng đề thi chuẩn hóa**, với cấu trúc tách bạch giữa điểm Tự động chấm (**Graded/MCQ/Code**) và điểm Tự luận theo Rubric (**Essay**):

| Mã đề thi | File dữ liệu JSON | Phân loại & Nguồn gốc | Số câu Graded | Số bài Essay | Mẫu số Graded | Mẫu số Tự luận | Phân bố đáp án Graded | Ticker hiển thị | Trạng thái |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **`olp-01`** | [`src/data/exams/olp-01.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-01.json) | Mock OLP 01 (Toàn diện) | 60 | 4 | 100.0đ | 40.0đ | A:16, B:14, C:14, D:14 | Graded: /100đ · Essay: /40đ | **PASS** |
| **`olp-02`** | [`src/data/exams/olp-02.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-02.json) | Mock OLP 02 (Đề 2 Thầy Luật) | 60 | 6 | 90.0đ | 60.0đ | A:20, B:8, C:13, D:19 | Graded: /90đ · Essay: /60đ | **PASS** |
| **`olp-03`** | [`src/data/exams/olp-03.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-03.json) | Tuyển tập Mock 03 (Gemini hỗ trợ biên soạn) | 100 | 4 | 100.0đ | 40.0đ | A:30, B:18, C:28, D:24 | Graded: /100đ · Essay: /40đ | **PASS** |
| **`olp-04`** | [`src/data/exams/olp-04.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-04.json) | Mock Insight Chuyên đề (24 câu) | 20 | 4 | 60.0đ | 40.0đ | A:5, B:5, C:5, D:5 | Graded: /60đ · Essay: /40đ | **PASS** |
| **`olp-05`** | [`src/data/exams/olp-05.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-05.json) | Chuyên đề CV & NLP SkillPixel | 90 | 0 | 90.0đ | 0.0đ | A:22, B:16, C:37, D:15 | Graded: /90đ (Ẩn Essay) | **PASS** |
| **`voai-2025`**| [`src/data/exams/voai-2025.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/voai-2025.json)| **Đề 006 · Gốc VOAI 2025 (Chính thức)** | 100 | 0 | 100.0đ | 0.0đ | A:19, B:32, C:21, D:28 | Graded: /100đ (Ẩn Essay) | **PASS** |
| **TỔNG CỘNG**| **6 Ngân hàng** | — | **430** | **18** | — | — | — | — | **PASS 100%** |

*Ghi chú học thuật:*
- 430 câu Graded gồm: 428 câu trắc nghiệm khách quan (MCQ) và 2 câu Code (OLP01-BC1, OLP01-BC2) tự đánh giá theo rubric kiểm thử từng phần (Partial scoring: 0đ, 2đ, 4đ, 5đ, 7đ).
- Đề 03 là bộ câu hỏi tái tạo phục vụ luyện tập do AI (Gemini) hỗ trợ biên soạn dựa trên chuyên đề ôn thi vòng trường; không phải đề thi 100 câu nguyên bản từ Thầy Đỗ Đình Luật.

---

## II. ĐỐI SOÁT VÀ ĐÍNH CHÍNH 100% CHÍNH XÁC THEO FILE DỮ LIỆU THẬT

Báo cáo này điều chỉnh triệt để 4 điểm mô tả chưa chuẩn xác từ bản nghiệm thu trước, bảo đảm khớp 100% với dữ liệu JSON và đề gốc:

### 1. `VOAI25-024`: Thuật toán 1-NN (1-Nearest Neighbor)
- **Nội dung thực tế trong file JSON và PDF gốc:** Câu hỏi khảo sát bài toán phân lớp với thuật toán 1-NN (k-Nearest Neighbors với $k=1$). Với mỗi điểm dữ liệu kiểm thử $x$, thuật toán chọn nhãn $y^*$ của mẫu huấn luyện $a^*$ có khoảng cách gần nhất tới $x$:
  $$a^* = \arg\min_{a \in A} d(x, a)$$
- **Đáp án:** Key **B**. *(Đính chính: Là thuật toán 1-NN và chọn Key B; không phải bài toán K-Means hay Key C).*

### 2. `VOAI25-032`: Average Pooling $3 \times 3$, Stride 2
- **Nội dung thực tế trong file JSON và PDF gốc:** Áp dụng phép toán **Average Pooling** với kích thước kernel $3 \times 3$, bước trượt $\text{stride} = 2$ lên ma trận đầu vào $4 \times 4$.
- **Tính toán:** Cửa sổ đầu tiên gồm 9 phần tử có tổng giá trị bằng $540 \implies \text{Giá trị trung bình} = \frac{540}{9} = 60$.
- **Đáp án:** Key **C** ($60$). *(Đính chính: Giá trị là 60 và chọn Key C; không phải Key B).*

### 3. `VOAI25-037`: Bảng Dữ Liệu Phân Lớp Sinh Viên & Entropy
- **Nội dung thực tế trong file JSON và PDF gốc:** Bảng dữ liệu gồm 6 sinh viên với 3 thuộc tính: Điểm tích lũy (`CGPA`), Số giờ tự ôn tập (`Revision`), và Kết quả (`Passed`). Trong đó có **4 sinh viên Passed (Đậu)** và **2 sinh viên Failed (Rớt)**.
- **Tính toán Entropy:**
  $$H(\text{Passed}) = -\frac{4}{6}\log_2\left(\frac{4}{6}\right) - \frac{2}{6}\log_2\left(\frac{2}{6}\right) \approx 0.918295834 \text{ bit (xấp xỉ } 0.92 \text{ bit)}$$
- **Đáp án:** Key **C** ($0.92$). *(Đính chính: Tập nhãn có 4 Passed, 2 Failed với $H \approx 0.92$, Key C; không phải 3/3, H=1, Key B).*

### 4. `VOAI02-M02`: Phân Phối Nhị Thức (Binomial Distribution)
- **Nội dung thực tế trong file JSON:** Biến ngẫu nhiên $X \sim \text{Binomial}(n = 20, p = 0.4)$.
- **Tính toán:**
  - Kỳ vọng: $E[X] = n \cdot p = 20 \times 0.4 = 8$.
  - Phương sai: $\text{Var}(X) = n \cdot p \cdot (1 - p) = 20 \times 0.4 \times 0.6 = 4.8$.
- **Đáp án:** Key **D** ($E[X] = 8, \text{Var}(X) = 4.8$). *(Đính chính: Hỏi giá trị kỳ vọng & phương sai với Key D; không phải hỏi công thức hàm mật độ xác suất PMF hay Key A).*

### 5. `VOAI02-M43`: Phục Hồi Distractor D trong Markdown Đề 02
- **Nội dung:** Tính toán chỉ số IoU giữa hai bounding box $[10, 10, 50, 50]$ và $[30, 30, 70, 70]$. $\text{Area}_A = 1600, \text{Area}_B = 1600, \text{Intersection} = 400 \implies \text{Union} = 2800 \implies \text{IoU} = \frac{400}{2800} = \frac{1}{7} \approx 0.143$ (Key **A**).
- **Sửa lỗi Markdown:** Trong `content/02-de-chuan-format-voai-expand.md`, phương án D cũ ghi $\frac{4}{28}$ (trùng giá trị $\frac{1}{7}$ với A) đã được sửa thành **$\frac{2}{7}$ (khoảng 0.286)** theo đúng file JSON. Lời giải phân tích bẫy làm rõ: lỗi chọn D là do nhân đôi diện tích phần giao trong tử số ($800 / 2800 = 2/7$).

### 6. `OLP01-C10`: Hồi Quy Ridge và Hiện Tượng Đa Cộng Tuyến
- **Nội dung:** Xử lý hiện tượng đa cộng tuyến (multicollinearity) bằng L2 Regularization (Ridge). Khi các đặc trưng tương quan mạnh, ma trận $X^T X$ gần suy biến; việc cộng thêm $\lambda I$ (với điều kiện $\lambda > 0$) bảo đảm ma trận $(X^T X + \lambda I)$ luôn khả nghịch và xác định dương.
- **Đáp án:** Key **A**. Bản Markdown `02-de-luyen-olp-ai.md`, `03-dap-an-olp-ai.md` và bản chuẩn `01-de-luyen-olp-01-toan-dien.md` đã được đồng bộ chuyển sang Key **A** khớp hoàn toàn với `olp-01.json`.

### 7. `VOAI25-026`: Ảnh Feature Map Gốc từ PDF
- **Nguồn:** Trích xuất từ `voai2025_original.pdf` (Trang 5, xref 42, kích thước $1045 \times 1041$ px, SHA-256 asset: `396b065dbfdfc0d4dfdb314a53e0621bd734a4828b1b23c62823e7f897d42db5`).
- **Tích hợp:** Đã nhúng Base64 vào HTML độc lập; đề bài sạch không chứa spoiler. Đáp án đúng **C** (các cạnh theo hướng kết hợp ngang và dọc).

### 8. `SKILL-NLP-01`: FastText Subword Character N-Grams
- **Nội dung:** FastText cải thiện nhúng từ nhờ túi các n-gram ký tự con (subword character n-grams) để xử lý từ OOV. Đáp án **A**. Tham chiếu lý thuyết trỏ chuẩn vào **§4.2 Các Phương Pháp Biểu Diễn Từ (Word Representations)**.

### 9. `SKILL-CV-40`: Số Lượng Tham Số Lớp Conv2D
- **Nội dung:** Lớp `nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3)`. Số tham số: $(3 \times 3 \times 1 + 1) \times 32 = 320$. Đáp án **B**.

### 10. `VOAI03-M04`: Nhận Diện Khái Niệm Shannon Entropy
- **Nội dung:** Nhận diện công thức và khái niệm Shannon Entropy $H(X) = -\sum p(x) \log_2 p(x)$ của biến ngẫu nhiên rời rạc. Đáp án **C**.

### 11. `OLP04-Q08`: BatchNorm2d Khi Kích Thước Batch Nhỏ ($N=1$)
- **Nội dung:** Thống kê mean và variance tính trên $(N, H, W)$ theo từng kênh. $N=1, H \times W > 1$ thì vẫn có $H \times W$ điểm ảnh; không tự động khiến variance bằng 0. Nếu feature map đồng nhất hoàn toàn (homogeneous), variance bằng 0 thì hằng số $\epsilon$ trong mẫu số $\sqrt{\sigma^2 + \epsilon}$ bảo vệ tránh chia cho 0. Không dùng khẳng định tuyệt đối luôn sụp đổ. Đáp án **A**. Cú pháp KaTeX hiển thị sắc nét 3 display formulas trên DOM.

### 12. `OLP04-Q13`: Đạo Hàm Giải Tích và Kiểm Thử Số Trị Focal Loss
- **Công thức:** Với $p = \sigma(z), y = 1, \alpha = 1$:
  $$\frac{\partial \text{FL}}{\partial z} = (1 - p)^\gamma \left[ (p - 1) + \gamma p \ln(p) \right]$$
- **Kiểm thử số trị độc lập:** Tại $p = 0.99, \gamma = 2$, đạo hàm giải tích và sai phân trung tâm ($h = 10^{-5}$) đều bằng $-2.98996650 \times 10^{-6}$ (độ lệch tuyệt đối $1.33 \times 10^{-15}$). Tỉ lệ so với CE bằng $0.000299$ (triệt tiêu 3300 lần). Câu hỏi hỏi về hệ số mất mát loss $\alpha (1 - p)^\gamma = 10^{-4}$. Đáp án **D**.

---

## III. MINH BẠCH VỀ DỮ LIỆU ĐỀ 04 VÀ TÀI NGUYÊN KHÓA HỌC

1. **Gắn nhãn `[UNVALIDATED CASE STUDY]` trên Đề 04:**
   - Các con số thống kê trong Đề 04 (như Macro-F1 từ 84% lên 97.1%, 41 lỗi giảm còn 8 lỗi) đã được gắn nhãn trực tiếp trên đề bài, lời giải và Markdown: **`[UNVALIDATED CASE STUDY]`** (Tình huống nghiên cứu ca điển hình giả định để luyện tư duy tối ưu), không gán là lời giảng viên hay số liệu kiểm chứng từ transcript video.
   - Metadata đề thi Đề 04 đã sửa thành: 4 bài tự luận thuộc **Module C** (40 điểm).
2. **Minh bạch về 19 Link Video Bài Giảng trong `06-khoa-hoc-olp-ai-va-voai-nang-cao.md`:**
   - Danh mục gồm: 19 link nhúng video `iframe.mediadelivery.net` (có gắn chữ ký token tạm thời cần quyền truy cập/hạn dùng nội bộ), 28 link Google Drive, 6 link Google Docs, và **0 link Coursera**. Báo cáo này đính chính hoàn toàn thông tin nhầm lẫn về Coursera trước đây.
3. **Cơ chế Cache Migration trong Web App:**
   - Hàm `loadSavedState()` kiểm tra `CURRENT_EXAM_VERSIONS` (v2 cho `olp-01`, `olp-04`, `olp-05`, `voai-2025`; v3 cho `olp-03`). Khi phát hiện cache cũ, hệ thống ghi log `console.warn` dọn sạch dữ liệu cũ và kích hoạt thông báo Toast UI nhẹ nhàng trên màn hình cho thí sinh.

---

## IV. BẢO ĐẢM ĐỒNG BỘ 100% CẢ 6 NGÂN HÀNG MARKDOWN

Tất cả các tài liệu Markdown đã được tái tạo và đồng bộ 100% từ JSON thông qua công cụ chuyên dụng [`scripts/sync_all_markdowns.py`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/scripts/sync_all_markdowns.py) và kiểm chứng bởi [`scripts/check_markdown_sync.py`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/scripts/check_markdown_sync.py):

| Ngân hàng JSON | Tài liệu Markdown tương ứng | Số câu kiểm tra | Trạng thái đồng bộ |
| :--- | :--- | :---: | :---: |
| `voai-2025.json` | [`content/04-de-chinh-thuc-voai-2025-ma-006.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/04-de-chinh-thuc-voai-2025-ma-006.md) | 100 | **PASS 100%** (Khớp prompt, options, key, explanation, ảnh Q26, ma trận Q32, bảng Q37, TeX Q68, 8 cặp Q80) |
| `olp-04.json` | [`content/04-de-bo-sung-insight-video-voai.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/04-de-bo-sung-insight-video-voai.md) | 24 | **PASS 100%** (Khớp Q08, Q13, 4 essays Module C, nhãn `[UNVALIDATED CASE STUDY]`) |
| `olp-02.json` | [`content/02-de-chuan-format-voai-expand.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/02-de-chuan-format-voai-expand.md) | 66 | **PASS 100%** (Khớp M43 D: 2/7, key A, 6 essays đầy đủ modelAnswer & rubric) |
| `olp-03.json` | [`content/03-de-vong-mien-voai-2025.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/03-de-vong-mien-voai-2025.md) | 104 | **PASS 100%** (Khớp 100 MCQ, 4 essays modelAnswer & rubric, M04/M16, header minh bạch Gemini tuyển tập) |
| `olp-05.json` | [`content/05-chuyen-de-thuc-chien-cv-nlp.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/05-chuyen-de-thuc-chien-cv-nlp.md) | 90 | **PASS 100%** (Khớp 90 MCQ options/keys/explanations, NLP-01 trỏ §4.2) |
| `olp-01.json` | [`content/01-de-luyen-olp-01-toan-dien.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/01-de-luyen-olp-01-toan-dien.md) | 64 | **PASS 100%** (Khớp 58 MCQ + 2 Code + 4 Essays, C10 Ridge/L2 Key A) |

*Ghi chú thêm:* Hai tài liệu tóm tắt [`content/02-de-luyen-olp-ai.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/02-de-luyen-olp-ai.md) và [`content/03-dap-an-olp-ai.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/03-dap-an-olp-ai.md) cũng đã được cập nhật đồng bộ câu C10 sang Key **A**.

---

## V. BẢNG TỔNG HỢP KIỂM THỬ KỸ THUẬT (9/9 SUITES PASS)

| STT | Bộ kiểm thử / Lệnh thực thi | Mục tiêu kiểm chứng | Kết quả | Mã thoát |
| :---: | :--- | :--- | :---: | :---: |
| 1 | `node scripts/validate.mjs` | Kiểm tra cấu trúc 6 file JSON đề thi, mẫu số điểm, phân bố đáp án | **PASS** | `0` |
| 2 | `python -X utf8 scripts/test_quality_all.py` | Kiểm tra tính toàn vẹn 448 câu hỏi, định dạng, bẫy đề thi | **PASS** | `0` |
| 3 | `python -X utf8 scripts/check_section_refs.py` | Kiểm tra 59 mục lý thuyết, 0 broken section references | **PASS** | `0` |
| 4 | `python -X utf8 scripts/check_markdown_sync.py` | Kiểm tra đối soát 100% Markdown <-> JSON cho cả 6 ngân hàng | **PASS (448/448 câu)** | `0` |
| 5 | `node scripts/audit_katex_syntax.mjs` | Quét cú pháp 3.724 công thức KaTeX, 0 lỗi delimiter/cú pháp | **PASS** | `0` |
| 6 | `node scripts/test_academic_rigor.mjs` | Kiểm thử sai phân số trị gradient, 0 double escape, 0 leaked placeholder | **PASS** | `0` |
| 7 | `node scripts/test_html_logic.mjs` | Kiểm thử di trú cache v2 (bao gồm Đề 04), ticker, rubric tự luận, partial code | **PASS** | `0` |
| 8 | `npm test` | 18 kiểm thử đơn vị React/TypeScript bằng Vitest | **PASS (18/18)** | `0` |
| 9 | `npx tsc --noEmit` | Kiểm tra kiểu dữ liệu toàn bộ dự án TypeScript | **PASS (0 lỗi)** | `0` |

---

## VI. DANH MỤC TẬP TIN BÀN GIAO & MÃ BĂM SHA-256

| Tên tập tin | Kích thước (Bytes) | Mã băm SHA-256 |
| :--- | :---: | :--- |
| [`public/olympic_ai_study_hub.html`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/public/olympic_ai_study_hub.html) | 2,528,457 | `ef704297fabb8d832782b73522c1b6c35fabb09ff5f17447c60915fe4ddad734` |
| [`dist/olympic_ai_study_hub.html`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/dist/olympic_ai_study_hub.html) | 2,528,457 | `ef704297fabb8d832782b73522c1b6c35fabb09ff5f17447c60915fe4ddad734` |
| [`content/04-de-chinh-thuc-voai-2025-ma-006.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/04-de-chinh-thuc-voai-2025-ma-006.md) | 220,790 | `21e60045383907c761f7110987043920cd7d488335402a301b51a95c9cf157ad` |
| [`content/04-de-bo-sung-insight-video-voai.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/04-de-bo-sung-insight-video-voai.md) | 101,900 | `dc51d3206cb2794face65957344071a27d5fabe1f87d6321e8c7bc5e5498ea80` |
| [`content/02-de-chuan-format-voai-expand.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/02-de-chuan-format-voai-expand.md) | 265,953 | `e1fe6c32e0058898618a23d3a11dd79a55d8eba46bf465df98bd4aad3cfa45e3` |
| [`content/03-de-vong-mien-voai-2025.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/03-de-vong-mien-voai-2025.md) | 258,960 | `82c7fea42ceb6f7cda3a18f7a8bef817cf731a1aa312fac852574b6642b639ae` |
| [`content/05-chuyen-de-thuc-chien-cv-nlp.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/05-chuyen-de-thuc-chien-cv-nlp.md) | 191,977 | `ff1a093f2bc43d2a83833787889cd696d0bd1805339b4d904d64c3288e08c1c4` |
| [`content/01-de-luyen-olp-01-toan-dien.md`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/01-de-luyen-olp-01-toan-dien.md) | 170,178 | `1addf8e8dd8c00ab8a038435fd03189fad95ae8fd7d82c3fdceea63405dcf944` |
| [`src/data/exams/olp-01.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-01.json) | 200,899 | `0267f12cdb20b39e8091c3ef78ae02d2806c22b5e75b2a76f95b61ce15a88a45` |
| [`src/data/exams/olp-02.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-02.json) | 286,347 | `5376860acddc952d2844c11c12bdfe5a960f51306f32e5c264e479edd725beb9` |
| [`src/data/exams/olp-03.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-03.json) | 291,189 | `d88c486ecf71af5de61d13f2928bc9c7abb3c4fd3394f0cdfe24bd846f5ab252` |
| [`src/data/exams/olp-04.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-04.json) | 112,899 | `ce79ae59b39adfb7254508b0ace5cc2a5e93ba6b0c169df3515a5ea9c9e836ea` |
| [`src/data/exams/olp-05.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-05.json) | 220,330 | `36579d324adba8d65ecd9ac7adf25711e5b1919dcbe1077ad5582f92795cc68d` |
| [`src/data/exams/voai-2025.json`](file:///D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/voai-2025.json) | 257,790 | `b34fd34d1f63ede6e18413f59f1d76f0d52ebe374cec4a5549bb1e622da8b893` |

---

## VII. LỜI NHẮC REVIEW DÀNH CHO GPT AUDITOR

Dưới đây là prompt mẫu để người dùng gửi trực tiếp cho GPT kiểm chứng nghiệm thu vòng 3:

```text
Xin chào GPT,
Dưới đây là toàn bộ tài liệu nghiệm thu kỹ thuật và dữ liệu đã được cập nhật triệt để theo checklist audit vòng 3 của bạn (docs/VERIFY_NGHIEM_THU_LAN_3_2026-10-09.md).
Vui lòng đối soát các nội dung sau trên hệ thống tại D:\Code\Code\AIO\Code\olp-ai-hcmus26:
1. Đọc docs/BAO_CAO_NGHIEM_THU_TOAN_DIEN_2026-10-09.md:
   - Đã đính chính đúng 4 câu: VOAI25-024 (1-NN, Key B), VOAI25-032 (Average Pool 3x3 stride 2, mean=60, Key C), VOAI25-037 (4 Passed 2 Failed, H=0.9183, Key C), VOAI02-M02 (Binomial n=20 p=0.4: E=8, Var=4.8, Key D).
   - Đã sửa M43 trong content/02-de-chuan-format-voai-expand.md phương án D là 2/7.
2. Kiểm tra sự đồng bộ 100% giữa 6 file JSON và các file Markdown trong content/ (đã có script scripts/check_markdown_sync.py kiểm tra theo từng ID, exit 0).
3. Kiểm tra nhãn [UNVALIDATED CASE STUDY] đã hiển thị trên metadata Đề 04, Q01 prompt & explanation, và tự luận Module C.
4. Kiểm tra đính chính 19 link video iframe.mediadelivery.net (0 link Coursera).
5. Kiểm tra cơ chế loadSavedState() và Toast UI notification khi di trú cache.
6. Kiểm tra kết quả 9 suite test trong mục V của báo cáo nghiệm thu.
Cho nhận xét khách quan và xác nhận trạng thái sẵn sàng cho kỳ thi ngày 11/10/2026!
```
