# VERIFY DANH MỤC ÔN THI — 09/10/2026

## Kết luận để quyết định ngay

**Web và cấu trúc đề qua các kiểm tra đã chạy; nội dung bản sửa rạng sáng 09/10 chưa đạt nghiệm thu.** Có lỗi mới, đáng sửa trước khi học: phần thuật ngữ và liên hệ trong Đề 02 bị gắn nhầm chủ đề hàng loạt. Markdown Đề 02 và PDF cẩm nang chưa đồng bộ với JSON/web. Không thể dùng kết quả test hiện tại để khẳng định “100% đúng nội dung” hoặc “đã sát đề chính thức VOAI 2025”.

Báo cáo Gemini được đọc là `docs/BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md`, nhưng chính file ghi cập nhật lần 3 lúc **02:00 ngày 09/10**. JSON Đề 02 sửa lúc **01:58:13 ngày 09/10**. Đây là snapshot mới hơn các biên bản nghiệm thu ngày 08/10; biên bản cũ không tự động chứng nhận các thay đổi mới.

Không sửa source, câu hỏi, đáp án, script sinh dữ liệu hay các bản web/PDF. Chỉ tạo báo cáo kiểm tra này và ảnh trang PDF làm bằng chứng.

## 1. Kết quả từng nhóm

| Nhóm | Kết quả thực tế | Ý nghĩa |
|---|---|---|
| File trong project | 26 đường dẫn tương đối trong danh mục đều tồn tại | Tồn tại không đồng nghĩa nội dung đúng |
| Nguồn Downloads | 6 file nguồn kiểm tra đều tồn tại với tên đúng | Đường dẫn SOLOAI trong danh mục bị lỗi ký tự |
| JSON | 3 đề, 184 câu; schema validator qua | Có 168 MCQ + 2 code + 14 essay |
| Chấm điểm | 18 unit tests và 5 nhóm HTML logic qua | Các tình huống được test hoạt động; không chứng minh đúng kiến thức |
| TypeScript | `tsc --noEmit -p tsconfig.json` qua | Không phát sinh lỗi kiểu trong phạm vi cấu hình hiện tại |
| KaTeX | Kiểm tra độc lập 2.554 đoạn: 0 lỗi cú pháp | Không chứng minh đúng công thức về mặt khoa học hoặc mọi màn hình đều hiển thị đẹp |
| HTML | Public và dist cùng SHA-256; dữ liệu ALL_EXAMS public bằng cả 3 JSON | Web đã mang cả phần giải thích bị gắn nhầm mới nhất |
| Web localhost | Mở được, chuyển Đề 02, mở M05 và lời giải | Trực tiếp thấy lỗi SVD/PCA trong câu Hessian; 20 nút KaTeX, 0 `.katex-error`, 0 console error ở màn hình này |
| Markdown Đề 02 | 60 block câu MCQ, 0/60 chứa nguyên văn explanation hiện tại | Chưa đồng bộ lời giải; 60 nhãn đáp án được đối chiếu không có chênh lệch |
| PDF cẩm nang | 3 bản giống nhau, vẫn là bản 07/10, còn lỗi cũ | Không dùng làm bản đã sửa sau audit |
| Độ sát VOAI chính thức 2025 | **UNVALIDATED** | Chưa có đối chiếu toàn văn 100 câu mã 006 |

Số đúng trong danh mục: Đề 01 là **58 MCQ + 2 code + 4 essay**, không phải 60 MCQ + 4 essay. Đề 02: 60 MCQ + 6 essay. Đề 03: 50 MCQ + 4 essay. Tổng 170 câu graded gồm cả 2 bài code.

## 2. Lỗi cần sửa trước khi tiếp tục dùng phần mở rộng Đề 02

### P0 — Bảng enrichment gắn nhầm nội dung với ID câu

File gây lỗi: `scripts/enrich_olp02_terms_and_links.py`. `TOPIC_ENRICHMENTS` dùng các ID M01…M60, nhưng từ M05 trở đi danh sách chủ đề không khớp câu hỏi thật. Script chèn thuật ngữ vào khối 1 và thay nội dung khối 4, rồi ghi đè JSON. Test đếm đủ bốn khối vẫn qua vì văn bản có đủ tiêu đề, dù nội dung thuộc câu khác.

| ID | Câu hỏi đang hỏi | Thuật ngữ được chèn |
|---|---|---|
| M05 | Hessian, điểm yên ngựa | SVD, PCA |
| M06 | Gradient Softmax + cross-entropy | Hessian |
| M13 | k-NN, lazy learning | GMM, EM |
| M22 | SMOTE | He/Xavier initialization |
| M27 | BatchNorm train/eval | Learning rate scheduler |
| M30 | CrossEntropyLoss | Gradient clipping |
| M37 | Kích thước đầu ra Conv2D | Semantic segmentation |
| M44 | NMS | Cosine similarity |
| M49 | Thứ tự tiền xử lý NLP | Causal mask |
| M51 | Tính cosine của hai vector | SacreBLEU |
| M57 | BLEU brevity penalty | Temperature |
| M60 | Temperature | Instruction tuning, RLHF |

Đã đọc prompt và nhãn thuật ngữ của toàn bộ 60 MCQ. M05–M58 và M60 có nhãn chủ đề chính lệch câu; M59 gắn chunking trong khi câu hỏi trọng tâm là hybrid retrieval/reranking, cùng miền RAG nhưng chưa giải thích đúng trọng tâm. M01–M04 có chủ đề thuật ngữ phù hợp hơn, **vẫn phải kiểm tra lại tham chiếu**.

Tham chiếu § cũng sai độc lập với nhãn thuật ngữ. Ví dụ M05 ghi “§5.3 Đại số tuyến tính”, nhưng §5.3 thật của `content/01-ly-thuyet-olp-ai.md` là **Tính chất của kỳ vọng & phương sai**. M02 dẫn §5.1 cho phân phối nhị thức, trong khi các phân phối nằm ở §5.2. Không chỉ đổi tên thuật ngữ; phải sửa cả đường dẫn lý thuyết và liên hệ câu cũ.

Lỗi đã xuất hiện trực tiếp trên `http://localhost:8080/olympic_ai_study_hub.html`: M05 có prompt Hessian; mở lời giải thấy phần đầu định nghĩa SVD/PCA và phần cuối dẫn SVD. Phần tính Hessian ở giữa vẫn kết luận điểm yên ngựa với det(H) = -16 đúng cho ví dụ này. **Không có căn cứ kết luận mọi đáp án Đề 02 đều sai; lỗi xác nhận là phần enrichment lạc chủ đề.**

### P1 — JSON, Markdown, PDF khác phiên bản

`content/02-de-chuan-format-voai-expand.md` có đủ 60 block MCQ nhưng không block nào chứa nguyên văn explanation của JSON hiện tại. Nhãn đáp án trong 60 block vẫn bằng JSON; khác biệt kiểm tra được nằm ở lời giải. Không nên tự coi Markdown cũ và JSON mới là cùng một tài liệu đã nghiệm thu.

Cả ba PDF docs/public/dist có SHA-256:

`75c7299430c65152cb19bd114c3f104df4be48d6f31bd2547b99b44350f958e9`

Các bản đều 412.247 byte, sửa lần cuối **07/10/2026 12:13:45**, 45 trang. Đã trích văn bản và render/đọc trực quan trang 41:

- **Trang 21:** tác vụ dịch Hoa–Việt vẫn đề xuất fine-tune NLLB-200/mBART-50. Đề SOLOAI gốc trang 4 ghi không được sử dụng mô hình dịch Hoa–Việt đã huấn luyện sẵn. Cần nêu đúng ràng buộc này và tách mở rộng thực tế khỏi phương án hợp lệ trong đề.
- **Trang 41:** TabM vẫn ghi **ICLR 2024**. Đúng là **ICLR 2025**, kiểm tra lại từ [repository chính thức của tác giả](https://github.com/yandex-research/tabm).

Bằng chứng trực quan: [trang 41 được render](D:/Code/Code/AIO/Code/olp-ai-hcmus26/tmp/pdfs/verify_2026-10-09/handbook_page41.png).

Hai HTML public/dist cùng SHA-256:

`f463936eafd5dda3568f544194bebb4998790d5bffa75d9cd1e0ef93de435bc9`

### P1 — Script audit chưa đủ để làm cổng nghiệm thu

`scripts/audit_quality.py` chỉ đếm chuỗi trong `explanation`, không đánh giá nội dung, không kiểm tra khớp prompt–thuật ngữ–tham chiếu và không đặt ngưỡng fail/exit code. Kết quả 60/66 ở Đề 02 hoặc 50/54 ở Đề 03 không tự chứng minh thiếu lời giải tự luận: essay dùng `modelAnswer`, nhưng script chưa đọc trường đó. Cần tách tiêu chuẩn MCQ/code và essay, thay vì tuyên bố cả 184 câu đều đủ cùng một kiểu bốn khối.

`scripts/audit_katex_syntax.mjs`:

- Bỏ qua `modelAnswer` và `rubric`.
- Bảng công thức thực tế ở HTML/generator, trong khi script tìm `src/data/formulas.ts`, file này không tồn tại và được bỏ qua im lặng.
- Regex giáo trình dùng `\\Z` trong JavaScript, không phải neo cuối văn bản; phần cuối có thể bị bỏ sót.
- Không kiểm tra `\\(...\\)` / `\\[...\\]` và delimiter chưa đóng.
- Khi phát hiện lỗi vẫn không đặt exit code khác 0.

Kiểm tra độc lập đã đọc mọi trường chuỗi của 184 câu, bỏ fenced/inline code trước khi trích math, quét toàn bộ giáo trình và 10 công thức trực tiếp trong HTML. Số đoạn kiểm tra: Đề 01 **603**, Đề 02 **852**, Đề 03 **485**, giáo trình **604**, bảng công thức **10**; tổng **2.554**, không lỗi parser KaTeX. Kết quả này bổ sung độ phủ, **không sửa được sai nội dung enrichment** và không phải xác nhận mọi công thức đúng toán học.

### P2 — Nguồn và mức độ sát đề chưa được chứng minh

Trong báo cáo Gemini, dòng 6 ghi PASS 100% các cổng P0/P1/P2, nhưng mục 4.4 dòng 145 ghi **chưa đối chiếu toàn văn đề chính thức VOAI 2025 mã 006, 100 câu, 180 phút**. Cần bỏ tuyên bố PASS toàn bộ nếu P2 ở đây bao gồm độ sát đề; nếu dùng P2 để chỉ đồng bộ web, phải định nghĩa rõ, tách hạng mục độ sát đề riêng.

Các nguồn phải phân biệt:

- `DTTN_VOAI_Bien_soan_Practice_1.pdf`: **đề thi thử biên soạn 2026 của Đỗ Đình Luật**, 50 câu/60 phút; không phải đề chính thức 2025.
- `Đề thi Olp_AI_2025 Vòng SOLOAI.pdf`: đề sinh viên, gồm dịch máy và phân loại video cử chỉ; trang 8 nêu Macro-F1. Không dùng cấu trúc đề thực hành này để suy ra cấu trúc MCQ VOAI.
- `DethichinhthucCV.pdf`: đề sinh viên 2026, 9 trang; tác vụ anomaly detection là nguồn thực hành CV, không xác nhận độ sát MCQ.
- `OLP_Sinh_Vien_data.json`: metadata **17 lessons** của khóa học; không tự chứng nhận 17 chủ đề syllabus chính thức.
- `VOAI_Nang_Cao_data.json`: metadata **2 lessons**, không phải bộ dữ liệu huấn luyện số học.
- Tên `content/03-de-vong-mien-voai-2025.md` và tiêu đề “VOAI 2025/2026” còn dễ gây hiểu nhầm; cần gắn nhãn ngay đầu là bộ đề biên soạn, ghi rõ nguồn từng phần như JSON đã làm.

Đường dẫn SOLOAI đúng: `C:\Users\HP\Downloads\Đề thi Olp_AI_2025 Vòng SOLOAI.pdf`; đường dẫn có `D? thi ... Vng` trong danh mục không phải tên thật.

Nguồn BTC để đối chiếu: [trang môi trường và đề thi Olympic AI học sinh](https://www.olp.vn/olympic-ai-cho-h%E1%BB%8Dc-sinh/m%C3%B4i-tr%C6%B0%E1%BB%9Dng-%C4%91%E1%BB%81-thi). Link đề chính thức đã được chỉ ra trong các vòng audit trước: [VOAI 2025 mã 006](https://drive.google.com/file/d/1p7-Nnxxbuwvz0mjj2SnR23WdDTkr_o5h/view). **Lần kiểm tra này không thực hiện lại đối chiếu từng câu của toàn bộ đề đó.**

## 3. Prompt đưa Gemini sửa

```text
Đọc docs/VERIFY_DANH_MUC_2026-10-09.md và sửa lỗi trên snapshot hiện tại. Không mở rộng thêm đề vì tôi thi ngày 11/10 và cần bộ ôn ổn định.

1. Ưu tiên scripts/enrich_olp02_terms_and_links.py và src/data/exams/olp-02.json. TOPIC_ENRICHMENTS đang gắn nhầm chủ đề với ID câu: M05 Hessian nhưng SVD, M13 k-NN nhưng GMM, M49 preprocessing nhưng causal mask, M51 cosine nhưng BLEU. Rà từng câu M01–M60 dựa trên prompt, options và answer thật; sửa khối thuật ngữ, hình dung, tham chiếu §, liên hệ câu cũ. Không đổi ID/prompt/answer/thứ tự option để hợp thức hóa bảng enrichment sai. Giữ phần tính toán đúng. Mỗi liên hệ phải có ID đích tồn tại và giải thích quan hệ thật; mỗi § phải đúng số và đúng tiêu đề của giáo trình hiện tại. Không chỉ đổi nhãn rồi giữ đoạn văn sai.

2. Sửa nguồn enrichment trước rồi kiểm tra chạy lại không tái tạo lỗi hoặc chèn lặp. Kiểm tra thủ công toàn bộ 60 câu, lập bảng ID | chủ đề câu | thuật ngữ | § thực tế | ID liên hệ. Test đủ 4 tiêu đề không thay thế kiểm tra này.

3. Đồng bộ Markdown Đề 02 với JSON sau khi nội dung đúng. Kiểm tra prompt, đáp án và toàn bộ lời giải, bảo toàn câu/tự luận hợp lệ. Kiểm tra Markdown Đề 03 và giáo trình để bỏ nhãn gây hiểu là đề chính thức khi đó là nguồn biên soạn.

4. Cập nhật LaTeX và biên dịch lại cẩm nang theo phạm vi nội dung sách đang có, rồi đồng bộ docs/public/dist. Sửa trang 21 phương án NMT theo đúng câu ràng buộc của SOLOAI; NLLB/mBART chỉ là mở rộng khi được phép. Sửa TabM thành ICLR 2025. Không chỉ copy PDF cũ sang ba nơi. Render lại các trang sửa để kiểm tra nội dung và bố cục.

5. Cải thiện audit_quality.py theo loại câu: MCQ/code dùng explanation; essay kiểm tra modelAnswer và rubric. Kiểm tra tham chiếu/ID tồn tại; fail có exit code khác 0; ghi rõ những phần phải review thủ công. Cải thiện audit_katex_syntax.mjs để kiểm tra tất cả trường math, cả phần cuối giáo trình, bảng công thức thật, delimiter thiếu; ghi số đoạn và fail thật. Không dùng tìm từ khóa để chứng nhận đúng khoa học.

6. Chạy schema validator, unit tests, HTML logic, typecheck; sinh lại web từ JSON đã sửa, xác nhận public/dist và ALL_EXAMS khớp JSON; kiểm tra UI tối thiểu M05/M13/M49/M51, essay, timer/chấm điểm. Không đổi seed/shuffle đáp án hay trọng số điểm ngoài yêu cầu sửa lỗi xác nhận.

7. Cập nhật báo cáo nghiệm thu: tách PASS kỹ thuật khỏi đúng nội dung và độ sát VOAI chính thức. Chừng nào chưa đối chiếu 100 câu mã 006, ghi UNVALIDATED cho độ sát đề; không ghi PASS 100% P0/P1/P2. Sửa danh mục Đề01 thành 58 MCQ + 2 code + 4 essay và sửa đường dẫn SOLOAI.

Trả lại danh sách file sửa, kiểm tra đã chạy, số liệu thực tế, bảng đối chiếu 60 câu và hạn chế còn lại. Không viết lời cam kết “triệt để/100%” nếu bằng chứng chưa đủ.
```

## 4. Cách dùng tài liệu trong lúc chờ sửa

- Dùng bộ đã có để luyện câu hỏi, nhưng **tạm bỏ qua khối thuật ngữ và liên hệ mới của Đề 02** cho tới khi sửa. Không suy ra rằng đủ bốn khối là lời giải đúng.
- PDF hiện tại là bản cũ; đọc giáo trình Markdown hiện tại cho các mục đã sửa như BatchNorm, NMT, NLP pipeline, TabM.
- Đừng mở rộng thêm nội dung trong hai ngày cuối. Ưu tiên làm đề và chữa những câu sai; dùng nguồn chính thức để xác định mức độ/format khi có thể, giữ nhãn “biên soạn” cho ba đề của project.
- Chưa thể khẳng định Đề 01/03 đúng toàn bộ học thuật chỉ từ lượt verify này; các tests qua xác nhận những hành vi đã test và không thay thế review từng lời giải.

## 5. Phạm vi kiểm tra và lệnh đã chạy

Trong thư mục project, dùng Node/Python runtime đi kèm Codex:

```text
node scripts/validate.mjs                         PASS 3 đề
node scripts/audit_katex_syntax.mjs               In 0 lỗi; đã đọc giới hạn script
python -X utf8 scripts/audit_quality.py           Báo số block; chưa phải cổng fail
node node_modules/vitest/vitest.mjs run src --no-cache
                                                PASS 18/18, 4 file test
node scripts/test_html_logic.mjs                 PASS 5 nhóm
node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json
                                                PASS
```

Một lần thử `tsc --noEmit -p tsconfig.app.json` thất bại vì project không có cấu hình đó; đã đọc cấu hình thật và chạy lại `tsconfig.json` thành công. Không chạy build/generator trong lượt này để tránh ghi đè các sản phẩm trước khi nội dung được sửa.

Các thao tác đọc bổ sung: `Get-Content` báo cáo Gemini, package.json, tsconfig.json và các script audit/enrichment; `rg` giới hạn file cho các mục P2, ID lỗi, section lý thuyết, timer, ALL_EXAMS/FORMULAS; `Get-Item` kiểm tra thời gian sửa; `rg --files docs tmp` kiểm kê artifact. Các đoạn Python/Node chạy từ stdin để kiểm tra tồn tại 26 file project + 6 Downloads, thống kê type, hash HTML/PDF, so JSON–HTML, tách 60 block Markdown, đọc/render PDF, trích prompt/thuật ngữ 60 câu, và parse độc lập KaTeX. Browser chỉ điều hướng và mở lời giải, không chọn đáp án, không nộp bài hay chỉnh điểm.

Đã mở nguồn chính thức TabM và trang đề BTC bằng web để xác minh nguồn. Không chạy toàn bộ notebook, huấn luyện mô hình, xem lại bốn video, hay thực hiện lại toàn bộ so sánh học thuật 184 câu với đề chính thức. Notebook có lỗi `os.path.existsb`; không nên hiểu “file tồn tại” là “notebook chạy được”.

File tạo trong lượt kiểm tra:

1. `docs/VERIFY_DANH_MUC_2026-10-09.md` — báo cáo này và prompt sửa.
2. `tmp/pdfs/verify_2026-10-09/handbook_page41.png` — ảnh trang PDF cũ làm bằng chứng.

## 6. Phụ lục đối chiếu prompt với thuật ngữ mới của 60 MCQ Đề 02

Bảng dưới trích tự động từ JSON hiện tại để Gemini định vị; cột thuật ngữ là nhãn đầu tiên của phần mới, không phải kết luận rằng toàn bộ lời giải câu đó sai.

| ID | Đầu prompt hiện tại | Thuật ngữ đầu tiên chèn vào |
|---|---|---|
| VOAI02-M01 | Một căn bệnh hiếm gặp có tỉ lệ mắc trong cộng đồng là $P(D) = 0.5\%$. Một bộ kit xét nghiệm y tế có độ nhạy (Sensitivity / Tr… | Base Rate (Tỉ lệ nền / Xác suất tiên nghiệm): |
| VOAI02-M02 | Cho biến ngẫu nhiên rời rạc $X \sim \text{Binomial}(n = 20, p = 0.4)$. Kỳ vọng $\mathbb{E}[X]$ và phương sai $\text{Var}(X)$ … | Binomial Distribution (Phân phối nhị thức): |
| VOAI02-M03 | Trong một nghiên cứu A/B Testing đánh giá thuật toán gợi ý mới, giả thuyết không $H_0$ là 'Thuật toán mới không làm tăng tỉ l… | Giả thuyết không ($H_0$): |
| VOAI02-M04 | Cho ma trận dữ liệu đã chuẩn hóa chuẩn (zero-mean) $X \in \mathbb{R}^{N \times D}$. Trong thuật toán Phân tích Thành phần Chí… | PCA (Principal Component Analysis): |
| VOAI02-M05 | Cho hàm số hai biến $f(x, y) = x^2 - 4xy + y^3$. Điểm dừng $P_0(0, 0)$ có gradient $\nabla f(0, 0) = [0, 0]^T$. Tính chất của… | SVD (Singular Value Decomposition): |
| VOAI02-M06 | Cho vector logit $z = [z_1, z_2, \dots, z_C]^T$, xác suất dự đoán $p_i = \text{Softmax}(z)_i = \frac{e^{z_i}}{\sum_{k=1}^C e^… | Hessian Matrix ($H = \nabla^2 f(x)$): |
| VOAI02-M07 | Khoảng cách Mahalanobis giữa hai điểm $u, v \in \mathbb{R}^D$ được định nghĩa là $d_M(u, v) = \sqrt{(u - v)^T \Sigma^{-1} (u … | K-Means Clustering: |
| VOAI02-M08 | Trong học máy, việc tối đa hóa hàm hợp lý hậu nghiệm (Maximum A Posteriori - MAP) trên trọng số $w$ tương đương với việc thêm… | SVM (Support Vector Machine): |
| VOAI02-M09 | Cho hai phân phối xác suất rời rạc $P$ và $Q$ trên cùng không gian mẫu. Phân kỳ Kullback-Leibler được định nghĩa là $D_{KL}(P… | Bias-Variance Tradeoff: |
| VOAI02-M10 | Hàm kích hoạt SiLU (Sigmoid Linear Unit / Swish) được định nghĩa là $f(x) = x \cdot \sigma(x)$, trong đó $\sigma(x) = \frac{1… | Regularization L1 (Lasso): |
| VOAI02-M11 | Cho $Q \in \mathbb{R}^{n \times n}$ là một ma trận trực giao (orthogonal matrix, thỏa mãn $Q^T Q = Q Q^T = I$). Với bất kỳ ve… | Cross-Validation: |
| VOAI02-M12 | Khi cần tính xấp xỉ kỳ vọng $\mathbb{E}_{x \sim P}[f(x)]$ nhưng việc lấy mẫu trực tiếp từ phân phối $P(x)$ quá khó khăn hoặc … | ROC Curve: |
| VOAI02-M13 | Vì sao thuật toán k-Nearest Neighbors (k-NN) được xếp vào nhóm 'Lazy Learner' (người học lười biếng), và độ phức tạp tính toá… | GMM (Gaussian Mixture Model): |
| VOAI02-M14 | Trong thuật toán Soft-Margin SVM, hàm mục tiêu tối thiểu hóa là $\min_{w, b, \xi} \frac{1}{2} \\|w\\|_2^2 + C \sum_{i=1}^N \xi_… | Imbalanced Learning: |
| VOAI02-M15 | Kernel RBF (Radial Basis Function / Gaussian Kernel) trong SVM có dạng $K(x, z) = \exp(-\gamma \\|x - z\\|^2)$. Nếu ta chọn giá… | Feature Importance: |
| VOAI02-M16 | Tại một nút lá của bài toán phân loại nhị phân ($K = 2$), tỉ lệ mẫu của hai lớp là $p_1 = 0.8$ và $p_2 = 0.2$. Giá trị của ch… | Perceptron: |
| VOAI02-M17 | Trong thuật toán Random Forest, mỗi cây con được xây dựng trên một tập mẫu Bootstrap kích thước $N$ (lấy mẫu có hoàn lại từ t… | Hàm kích hoạt ReLU (Rectified Linear Unit): |
| VOAI02-M18 | Trong thuật toán AdaBoost phân loại nhị phân ($y_i \in \{-1, +1\}$), tại vòng lặp $t$, bộ phân loại yếu $h_t(x)$ có tỉ lệ lỗi… | Hàm kích hoạt GELU (Gaussian Error Linear Unit): |
| VOAI02-M19 | Khác biệt cốt lõi trong thuật toán tối ưu hóa giữa Gradient Boosting truyền thống (GBM của Friedman) và XGBoost (Chen & Guest… | CrossEntropyLoss: |
| VOAI02-M20 | LightGBM đạt tốc độ huấn luyện vượt trội trên các tập dữ liệu lớn so với XGBoost truyền thống chủ yếu nhờ vào hai kỹ thuật nà… | BCEWithLogitsLoss: |
| VOAI02-M21 | Khi mã hóa biến phân loại (Categorical Features) bằng Target Encoding thông thường trên toàn bộ tập dữ liệu, mô hình thường b… | Backpropagation (Lan truyền ngược): |
| VOAI02-M22 | Khi áp dụng kỹ thuật sinh mẫu nhân tạo SMOTE (Synthetic Minority Over-sampling Technique) để xử lý dữ liệu mất cân bằng lớp k… | Khởi tạo trọng số He (Kaiming Initialization): |
| VOAI02-M23 | Trong bài toán phân tích cụm không gian biểu diễn (Representation Space Clustering), nhận định nào sau đây là **CHÍNH XÁC** k… | BatchNorm (Batch Normalization): |
| VOAI02-M24 | Khi xây dựng mô hình dự báo chuỗi thời gian (ví dụ: dự báo giá cổ phiếu hoặc lưu lượng truy cập theo giờ), vì sao việc sử dụn… | LayerNorm (Layer Normalization): |
| VOAI02-M25 | Trong PyTorch, đoạn mã nào sau đây biểu diễn **ĐÚNG VÀ ĐẦY ĐỦ** thứ tự các bước trong một vòng lặp huấn luyện (Training Step)… | Dropout: |
| VOAI02-M26 | Nếu khởi tạo tất cả các trọng số $W$ của một mạng nơ-ron sâu bằng giá trị **0 (Zeros)**, hiện tượng gì sẽ xảy ra? Và đối với … | Optimizer Adam: |
| VOAI02-M27 | Trong lớp Batch Normalization (`nn.BatchNorm2d`), sự khác biệt căn bản về mặt toán học giữa pha huấn luyện (`model.train()`) … | Learning Rate Scheduler: |
| VOAI02-M28 | Vì sao các kiến trúc Transformer và mô hình xử lý chuỗi ngôn ngữ tự nhiên (NLP) hầu như luôn sử dụng **Layer Normalization** … | Vanishing Gradient (Tiêu biến gradient): |
| VOAI02-M29 | Khi huấn luyện mạng học sâu nhiều lớp hoặc mô hình RNN chuỗi dài, hiện tượng bùng nổ gradient (Exploding Gradient) thường khi… | Weight Decay (Suy giảm trọng số): |
| VOAI02-M30 | Trong PyTorch, lớp `nn.CrossEntropyLoss()` đã tự động tích hợp sẵn phép biến đổi toán học nào bên trong, và thí sinh cần đưa … | Gradient Clipping: |
| VOAI02-M31 | Vì sao trong bài toán phân loại nhị phân hoặc phân loại đa nhãn (Multi-label), PyTorch khuyến nghị mạnh mẽ sử dụng `nn.BCEWit… | Same Padding trong Conv2D: |
| VOAI02-M32 | Nghiên cứu của Loshchilov & Hutter (ICLR 2019) đã chỉ ra rằng việc cài đặt Weight Decay thông thường (thêm $\lambda w$ vào gr… | Receptive Field (Vùng cảm thụ): |
| VOAI02-M33 | Kỹ thuật **Learning Rate Warmup** (tăng dần tốc độ học từ 0 lên giá trị cực đại trong một số bước đầu tiên) trước khi áp dụng… | Global Average Pooling (GAP): |
| VOAI02-M34 | Trong hầu hết các thư viện Deep Learning hiện đại (bao gồm PyTorch), kỹ thuật **Inverted Dropout** (với tỉ lệ drop $p$) được … | Skip Connection (Kết nối tắt): |
| VOAI02-M35 | Xét bài toán tối ưu hóa có điều kiện: $\min_w L(w)$ với ràng buộc $\\|w\\|_1 \le C$ (L1) hoặc $\\|w\\|_2^2 \le C$ (L2). Về mặt hì… | Vision Transformer (ViT - Dosovitskiy et al., 2020): |
| VOAI02-M36 | Khi triển khai cơ chế Dừng Sớm (Early Stopping) trong quá trình huấn luyện mạng nơ-ron sâu, nhận định nào sau đây là **CHÍNH … | Anchor Boxes: |
| VOAI02-M37 | Cho ảnh đầu vào kích thước vuông $W_{in} = 224$. Áp dụng lớp tích chập Conv2D với kích thước kernel $K = 7$, padding $P = 3$,… | Semantic Segmentation (Phân đoạn theo ngữ nghĩa): |
| VOAI02-M38 | Trong thiết kế mạng VGG và ResNet, vì sao người ta luôn ưu tiên xếp chồng hai lớp tích chập kích thước $3 \times 3$ liên tiếp… | Data Augmentation: |
| VOAI02-M39 | Kỹ thuật Global Average Pooling (GAP) được giới thiệu trong mạng Network In Network (Lin et al.) và chuẩn hóa trong ResNet nh… | Video Classification (Phân loại video): |
| VOAI02-M40 | Trong khối Residual Block của kiến trúc ResNet, đầu ra được tính bằng phép cộng $y = \mathcal{F}(x, \{W_i\}) + x$. Về mặt giả… | Unsupervised Anomaly Detection (Phát hiện bất thường không giám sát): |
| VOAI02-M41 | Trong bài toán phân đoạn ảnh ngữ nghĩa (Semantic Segmentation), kiến trúc U-Net (Ronneberger et al.) sử dụng Skip Connections… | Tokenization trong NLP: |
| VOAI02-M42 | Cho ảnh đầu vào kích thước $224 \times 224 \times 3$. Trong kiến trúc Vision Transformer (ViT-Base, Dosovitskiy et al.) với k… | TF-IDF (Term Frequency - Inverse Document Frequency): |
| VOAI02-M43 | Cho hai bounding box hình chữ nhật trong mặt phẳng tọa độ theo định dạng $[x_1, y_1, x_2, y_2]$ (tọa độ góc trên-trái và góc … | Word2Vec (Mikolov et al., 2013): |
| VOAI02-M44 | Trong pipeline phát hiện đối tượng (Object Detection), thuật toán NMS chuẩn mực hoạt động tuần tự theo các bước nào sau đây đ… | Cosine Similarity: |
| VOAI02-M45 | Trong đánh giá mô hình Object Detection chuẩn COCO, kí hiệu **mAP@[0.5:0.95]** (hay mAP@[.5:.95]) biểu thị điều gì?… | RNN (Recurrent Neural Network): |
| VOAI02-M46 | Khi triển khai hệ thống Computer Vision trên thiết bị nhúng hoặc yêu cầu thời gian thực (Real-time $\ge 30$ FPS), mô hình phá… | Self-Attention (Tự chú ý): |
| VOAI02-M47 | Trong bài toán phát hiện ảnh giả mạo/DeepFake (Bài toán 'Kẻ mạo danh' trong video AI Vietnam và IOAI 2026), vì sao việc kết h… | Multi-Head Attention (Chú ý đa đầu): |
| VOAI02-M48 | Trong kỹ thuật **MixUp** (Zhang et al.), hai ảnh $(x_i, x_j)$ và nhãn One-hot $(y_i, y_j)$ được kết hợp theo công thức nào vớ… | Positional Encoding (Mã hóa vị trí): |
| VOAI02-M49 | Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự chuẩn mực logic của các bước tiền xử lý văn bản thô (Text Preprocessing) nào sa… | Causal Mask (Mặt nạ nhân quả / Look-ahead Mask): |
| VOAI02-M50 | Trong thuật toán biểu diễn từ Word2Vec (Mikolov et al.), phát biểu nào sau đây phân biệt **CHÍNH XÁC** giữa hai kiến trúc CBO… | So sánh BERT vs GPT vs T5: |
| VOAI02-M51 | Cho hai vector embedding biểu diễn ngữ nghĩa của hai từ: $u = [1, 2, 2]$ và $v = [2, 0, 1]$. Độ tương đồng Cosine (Cosine Sim… | SacreBLEU: |
| VOAI02-M52 | Trong mạng LSTM (Long Short-Term Memory), cổng nào chịu trách nhiệm quyết định tỉ lệ thông tin nào từ ô nhớ trạng thái cũ ($C… | ROUGE (Recall-Oriented Understudy for Gisting Evaluation): |
| VOAI02-M53 | Trong cơ chế tính toán Self-Attention của Transformer (Vaswani et al.): $\text{Attention}(Q, K, V) = \text{Softmax}\left(\fra… | Perplexity (PPL - Độ bối rối): |
| VOAI02-M54 | Vì sao kiến trúc Transformer chia không gian biểu diễn thành $h$ đầu chú ý song song (Multi-Head Attention với $d_v = d_{mode… | LoRA (Low-Rank Adaptation - Huấn luyện thích ứng hạng thấp): |
| VOAI02-M55 | Trong Transformer nguyên bản, công thức mã hóa vị trí Sinusoidal được định nghĩa là $PE_{(pos, 2i)} = \sin\left(\frac{pos}{10… | Sparse Retrieval vs Dense Retrieval: |
| VOAI02-M56 | Sự khác biệt căn bản về mặt cấu trúc chú ý (Attention Mechanism) và bài toán huấn luyện trước (Pre-training Objective) giữa B… | Cross-Encoder Re-ranker: |
| VOAI02-M57 | Trong đánh giá dịch máy (Bài toán Dịch Hoa - Việt đề thi OLP AI 2025), công thức SacreBLEU kết hợp hệ số phạt độ ngắn: $\text… | Temperature trong sinh văn bản LLM: |
| VOAI02-M58 | Khác biệt cốt lõi về triết lý đo lường giữa chỉ số **BLEU** và chỉ số **ROUGE** trong xử lý ngôn ngữ tự nhiên là gì?… | Top-p Sampling (Nucleus Sampling): |
| VOAI02-M59 | Trong một hệ thống RAG doanh nghiệp hiện đại, pipeline truy xuất kết hợp 2 giai đoạn (Two-Stage Retrieval) thường bao gồm:… | Chunking trong RAG: |
| VOAI02-M60 | Trong quá trình sinh văn bản tự hồi quy (Autoregressive Generation) của các mô hình LLM (như GPT-4, LLaMA, DeepSeek), kỹ thuậ… | Instruction Tuning & RLHF: |
