# VERIFY FULL NGUỒN, NGÂN HÀNG ĐỀ VÀ WEB — 09/10/2026

**Kết luận: CHƯA ĐẠT để nghiệm thu “đúng toàn bộ / sát đề gốc”.** Bản mới có nguồn gốc tốt hơn và web đã nạp đủ sáu đề, nhưng vẫn còn lỗi đáp án, mất dữ kiện của đề chính thức, lời giải lệch sau đảo phương án và nội dung lý thuyết sai trong đề 04. Ưu tiên sửa các lỗi P0/P1 dưới đây trước khi tiếp tục mở rộng.

Thời điểm kiểm tra cuối: khoảng 15:03 ngày 09/10/2026, Asia/Saigon. Gemini tạo thêm `olp-04.json` và cập nhật HTML ngay trong lúc kiểm tra. Báo cáo lấy trạng thái cuối; số 184 hoặc 424 không còn là tổng hiện tại. Đính chính ghi nhận sơ bộ: đề 04 có **18/20 đáp án B**, không phải 20/20.

Đây là audit, không sửa ngân hàng, generator, notebook hoặc web. Các tệp mới do lần kiểm tra này tạo nằm trong `docs/VERIFY_FULL_NGUON_VOAI_2026-10-09.md`, `docs/PROMPT_GEMINI_SUA_VERIFY_FULL_2026-10-09.md` và `tmp/audit_full_2026-10-09/`.

## 1. Có bao nhiêu câu, ở những phần nào?

| Đề | MCQ | Code | Tự luận | Tổng | Điểm graded / tự luận | Thời gian JSON |
|---|---:|---:|---:|---:|---|---:|
| olp-01 | 58 | 2 | 4 | 64 | 100 / 40 | 90 phút |
| olp-02 | 60 | 0 | 6 | 66 | 90 / 60 | 90 phút |
| olp-03 | 100 | 0 | 4 | 104 | 100 / 40 | 90 phút |
| olp-04, vừa thêm | 20 | 0 | 4 | 24 | 60 / 40 | 90 phút |
| olp-05 | 90 | 0 | 0 | 90 | 90 / 0 | 90 phút |
| voai-2025 | 100 | 0 | 0 | 100 | 100 / 0 | 180 phút |
| **Tổng** | **428** | **2** | **18** | **448** | **430 câu graded + 18 tự luận** | |

Phân bố module thực tế, tính cả tự luận:

| Đề | A | B | C | Ý nghĩa cần lưu ý |
|---|---:|---:|---:|---|
| 01 | 12 | 18 | 34 | B có 2 code; C có 4 tự luận |
| 02 | 12 | 24 | 30 | C có 6 tự luận |
| 03 | 32 | 39 | 33 | C có 29 MCQ + 4 tự luận; nhãn module hiện vẫn ghi 25/25/4 |
| 04 | 20 | 4 | 0 | A là MCQ insight, B là tự luận; khác cách chia A/B/C ở các đề khác |
| 05 | 0 | 35 | 55 | 35 NLP Session 5; 55 CV Session 9 |
| VOAI 2025 | 12 | 48 | 40 | Phân nhóm tự tạo khi nhập, không phải cấu trúc A/B/C được xác nhận từ BTC |

Đây là số **bản ghi**, không phải 448 kiến thức độc lập. Các ngân hàng có chủ đề/câu tương tự nhau; không dùng tổng này để suy ra độ phủ syllabus.

## 2. Nguồn nào là đề chính thức?

Các PDF trong `C:\Users\HP\Downloads\OLPAI\Quizzes\` đã kiểm tra tồn tại và đọc được:

| Tệp | Nội dung / phạm vi xác nhận |
|---|---|
| voai2025_original.pdf | Đề chính thức VOAI 2025 vòng sơ loại, mã 006, 100 câu, 180 phút, 16 trang |
| VOAI_2025_Solution.pdf | Lời giải Nguyễn Khắc Trung Kiên, 38 trang, ghi ngày 29/01/2026; **nguồn lời giải bên thứ ba** |
| de_1_solution.pdf | Lời giải đề luyện 2026, 50 câu, Đỗ Đình Luật |
| De_TN_So_2.pdf + de_2_solution.pdf | Đề luyện số 2 năm 2026, 60 câu, 90 phút và lời giải |
| De_TN_So_3.pdf + de_3_solution.pdf | Đề mô phỏng 2026, 100 câu, **120 phút** và lời giải |
| L5_Answer.pdf | 35 câu SkillPixel Session 5: NLP, summarization, machine translation |
| L9_CV1_Answer.pdf | 55 câu SkillPixel Session 9: CNN/CV |

Đã đọc thêm `C:\Users\HP\Downloads\Đề thi Olp_AI_2025 Vòng SOLOAI.pdf`: đây là **Olympic AI sinh viên Việt Nam 2025**, gồm hai tác vụ thực hành Hoa–Việt và ngôn ngữ ký hiệu. Không gộp tài liệu này thành đề trắc nghiệm VOAI mã 006.

Danh sách được cung cấp lần này có **đề gốc VOAI 2025 và đề luyện 2026**. Chưa có bằng chứng trong các nguồn đã kiểm tra rằng có đề chính thức VOAI 2024 hoặc đề chính thức VOAI 2026. Các JSON khóa học SkillPixel là metadata đào tạo, không tự động trở thành đề cương chính thức BTC.

## 3. P0 — lỗi ảnh hưởng trực tiếp làm bài/chấm điểm

### 3.1 OLP01-C10: đáp án chấm sai

Trong `src/data/exams/olp-01.json`, câu đa cộng tuyến/Ridge:

- `answer = B`, nhưng B là “Vì L2 tính toán không cần ma trận”, sai.
- A diễn đạt lý do Ridge ổn định hơn trong đa cộng tuyến và tính khả nghịch của `X^T X + lambda I` với lambda > 0.
- Chính lời giải hiện kết luận “Chọn A”.

**Sửa đáp án thành A**, kiểm tra chấm trên UI và cập nhật phiên bản cache của đề 01 nếu đáp án cũ đã được lưu. Cách nói Lasso “bốc thăm ngẫu nhiên” chỉ là ví von về tính bất ổn định khi các biến tương quan, không phải mô tả bắt buộc của solver.

### 3.2 VOAI02-M43: có hai lựa chọn đúng

IoU hai hộp `[10,10,50,50]` và `[30,30,70,70]`: giao 400, hợp 2800, kết quả `1/7`.

- A = `1/7`.
- D = `4/28` = `1/7`.
- Key chỉ nhận A, nên chọn D đúng toán học vẫn bị chấm sai.

**Thay D bằng một distractor thật sự khác**, đồng bộ phần bẫy và Markdown. Không đổi công thức đúng để làm hợp key.

### 3.3 Đề VOAI 2025 trên web: mất dữ kiện và khác bản gốc

Đã tách đủ 100 câu của đề gốc và lời giải để so sánh với JSON. **100/100 key JSON khớp lời giải của tác giả**, nhưng điều đó không chứng minh khớp đáp án chính thức hoặc bảo toàn đề gốc. Script `scripts/rebuild_voai2025_with_latex.py` lấy PDF **Solution**, không nhập trực tiếp PDF đề gốc; nhiều câu được rút ngắn thủ công.

Các lỗi xác nhận:

| ID | Hiện trạng JSON / web | Cần phục hồi |
|---|---|---|
| VOAI25-014 | Chọn thứ tự 1–4 nhưng không còn định nghĩa bước 1–4 | Tokenization, Normalization, Stemming, POS tagging theo đúng số gốc |
| VOAI25-024 | Đảo A/B so với bản gốc; giữ key A của lời giải bên thứ ba | Đề gốc A dùng d(x,y), B dùng d(x,a); **đúng toán học là B theo thứ tự gốc**. Khôi phục thứ tự rồi key B; ghi chú đính chính nguồn lời giải |
| VOAI25-025 | “với tập dữ liệu cho trước” nhưng mất toàn bộ bảng kNN | Đủ 8 mẫu, tọa độ, nhãn; Q=(6,2,6), k=3 |
| VOAI25-026 | Hỏi feature map nhưng không có hình | Hình feature map trong đề gốc |
| VOAI25-032 | Không có giá trị ma trận; còn đổi đầu vào từ 4×4 thành 3×3 | Ma trận 4×4 gốc, cửa sổ 3×3, stride 2; ô đầu ra (0,0)=60 |
| VOAI25-033 | Hỏi dòng code thiếu nhưng bỏ đoạn ResNet50/Identity | Toàn bộ code và vị trí cần điền; feature extraction dựa trên model đã bỏ fc |
| VOAI25-037 | “Dựa trên tập dữ liệu...” nhưng không có bảng Passed | Bảng 6 dòng CGPA/ôn tập/qua môn; 4 T, 2 F, entropy khoảng 0.9183 |
| VOAI25-046 | Options còn i/ii/iii/iv nhưng không có danh sách chiến lược | Đầy đủ bốn chiến lược được đánh số |
| VOAI25-058 | Thay hai confusion matrix bằng câu “Train rất tốt, Test kém hơn nhiều” | Phục hồi hai ma trận; để người học tự suy luận, tránh lộ đáp án trong prompt |
| VOAI25-068 | Công thức bị thành “PK”, “1 K”; option C có ký tự điều khiển | Chuyển cả bốn lựa chọn sang TeX chính xác, đặc biệt trung bình `(1/K) sum T_i(x)` |
| VOAI25-073 | Hỏi skip connection ở dòng nào nhưng không có code đánh số | Code identity_block gốc; phép Add ở dòng 21 |
| VOAI25-080 | Chỉ có hai cặp số và dấu “...” | Đủ 8 cặp; MSE=60/8=7.5 |

Đã xác nhận trên **web live** câu 025 thiếu bảng và câu 068 hiển thị công thức hỏng. Không chỉ là lỗi trích xuất text của PDF.

Dữ liệu cần phục hồi nhanh:

- Câu 25: S1=(2,2,0), S2=(1,3,1), S3=(0,2,2) nhãn Đỏ; S4=(8,7,7), S5=(9,6,6), S6=(7,7,8) nhãn Xanh dương; S7=(5,2,5), S8=(6,1,4) nhãn Xanh lá. Giữ đúng thứ tự nguồn.
- Câu 32: `[[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]]`.
- Câu 80: expected `[15,17,10,26,14,12,11,13]`, actual `[12,19,15,24,13,14,8,11]`.

Ngoài các lỗi trên, nhiều distractor đã bị viết lại, ví dụ câu 84/93; câu 75 lược bỏ ngữ cảnh encoder/decoder. Tệp `official_option_difference_candidates.json` liệt kê 38 câu có khác biệt chuỗi ở các options trích được. **38 là danh sách ứng viên cần đối chiếu, không phải 38 đáp án sai**: một phần khác biệt do định dạng PDF hoặc cách viết. Các câu công thức/bảng cũng không được bao phủ hết bởi phép so chuỗi này.

**Khuyến nghị:** nhập lại từ PDF original, giữ nguyên câu, phương án, bảng, hình, code. Lời giải ELI5 đặt riêng. Không gắn “đề gốc chính thức” cho bản giản lược đang thiếu dữ kiện.

### 3.4 Đề 05: 66/90 lời giải nói sai chữ cái sau đảo phương án

So 90 phương án đúng với hai PDF L5/L9: nội dung lựa chọn đúng khớp nguồn sau chuẩn hóa khoảng trắng và cách viết kích thước TeX. Năm khác biệt chuỗi là cách viết `32×32`, `26×26`, `16×16`, `5×5` hoặc số trang lẫn trong PDF; đã xem lại.

Tuy nhiên, **66 câu có chữ cái kết luận trong lời giải khác `answer`**: 29 NLP và 37 CV.

Ví dụ:

- SKILL-NLP-01: key A là subword n-grams; lời giải bảo chọn C, hiện C là hierarchical softmax.
- SKILL-NLP-15: key C là quadratic attention; lời giải bảo chọn B, hiện B là lời giải thích sai về bộ nhớ LSTM.
- SKILL-CV-40: tính đúng 320 tham số, key C; lời giải bảo chọn A, hiện A=96.

Nguyên nhân đọc được: `balance_and_enrich_exams.py` chỉ đổi text options và `answer`, không cập nhật các chữ cái tham chiếu trong explanation.

Danh sách đủ 66 ID và mapping nguồn có trong `tmp/audit_full_2026-10-09/olp05_source_compare.json`; tổng hợp cả lỗi OLP01-C10 trong `answer_explanation_conflicts.json`. **Không thay key theo chữ cũ trong lời giải**; phải cập nhật lời giải theo nội dung options hiện tại hoặc tạo mapping đảo phương án đúng.

### 3.5 Đề 04: lỗi kiến thức cần viết lại

- **OLP04-Q08:** batch size 1 trong CNN không đồng nghĩa phương sai BN bằng 0. BatchNorm2d lấy thống kê trên các phần tử N,H,W của mỗi kênh. Khi N=1, H×W vẫn có thể lớn và biến thiên khác 0. Câu hiện dùng “chắc chắn” và cả bốn options đều không phù hợp; phải viết lại prompt/options/lời giải. [PyTorch BatchNorm2d](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm2d.html).
- **OLP04-Q09:** KV cache không làm full attention cho token mới thành O(1) theo chiều dài context. Query mới vẫn đọc K/V của các token cũ; phần attention mỗi bước là O(T) nếu giữ cố định số chiều/head/layer. Key B về VRAM tăng theo chuỗi hợp lý, nhưng tiền đề O(1) sai. [Hugging Face: How caching works](https://huggingface.co/docs/transformers/cache_explanation).
- **OLP04-Q13:** `(1-p)^gamma=10^-4` là hệ số nhân **loss**, không phải hệ số nhân gradient chính xác, vì hệ số đó phụ thuộc p. Với p=0.99, gamma=2, alpha=1, tỷ lệ độ lớn đạo hàm focal/CE theo binary target logit khoảng 0.000299, không phải 0.0001. Sửa câu chỉ hỏi hệ số loss hoặc tính đạo hàm đầy đủ.
- **OLP04-Q17:** thuật ngữ đúng của PyTorch là **LogSoftmax + NLLLoss** trên logits, không phải Softmax + NLLLoss. Công thức gradient `p-y` đúng với CE không weighted cho một mẫu; cần ghi điều kiện nếu nói về reduction/weights. [PyTorch CrossEntropyLoss](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html).

Q10 có key A; Q12 có key C và mức giảm BLEU 63.2%, phù hợp phép tính. Không sửa hai câu này thành B để cân bằng.

## 4. P1 — chất lượng đề, mapping, nguồn và rubric

### 4.1 Đáp án có quy luật dễ đoán

- Toàn bộ 90 MCQ của đề 05: A,B,C,D lặp tuần tự.
- 50 câu mới M51–M100 của đề 03: A,B,C,D lặp tuần tự từ M51.
- Đề 04: B=18/20 (90%), A=1, C=1, D=0.

Phân bố tổng A/B/C/D đều không bảo đảm chất lượng nếu chuỗi vị trí dễ đoán. Với đề mô phỏng, đảo phương án bằng seed xác định, đồng bộ explanation/distractors/Markdown. Với đề chính thức, **giữ thứ tự gốc**, không cân bằng lại để qua validator.

### 4.2 Đề 04 có bốn essay sai schema của hệ thống hiện tại

Cả bốn essay chỉ có `answer`, `explanation`, không có `modelAnswer`, `rubric`, `rubricPoints`. Nội dung bài giải có trong explanation nhưng giao diện đọc modelAnswer.

Đã mở OLP04-ESSAY-01 trên web: rubric trống; bấm mở “Bài giải mẫu” chỉ mở một vùng trống. Phải chuyển dữ liệu sang schema essay đúng, giữ bài giải, thêm tiêu chí/chấm điểm tổng 10đ mỗi bài. Không đổ essay vào trường answer của MCQ.

### 4.3 Tham chiếu lý thuyết tồn tại nhưng sai chủ đề

Đề 05 đang gán § theo khoảng số câu, không theo heading thật:

| Ví dụ | Lời giải ghi | Heading thật |
|---|---|---|
| NLP-01 | §4.1 về biểu diễn từ/chuỗi | §4.1 Pipeline tiền xử lý; FastText nên hướng tới §4.2 |
| NLP-15 | §4.2 Attention & Transformer | §4.2 Word Representations; Transformer nằm §4.5 |
| NLP-30 | §4.3 LLM & SOTA | §4.3 Cosine Similarity |
| CV-40 | §3.3 kiến trúc SOTA | Câu tính tham số Conv2d nên có liên hệ công thức Conv ở §3.1 |

Cần mapping từng câu sang chủ đề đúng; nếu giáo trình chưa có phần tương ứng thì bổ sung heading rõ ràng hoặc bỏ link, không đặt tên mới cho § đang tồn tại.

Đề chính thức cũng dùng fallback keyword/§1.1 và phân nhóm bằng danh sách/cap số lượng. Không gọi những nhãn này là phân bố module chính thức.

### 4.4 Đề 03 không phải bản nguyên vẹn De_TN_So_3

M01–M50 giữ bộ luyện cũ; M51–M100 thêm từ đề số 3. Ví dụ JSON M04 hỏi Entropy, trong **De_TN_So_3 câu 4 hỏi Manhattan giữa (1,2) và (4,6)**. Tự luận bốn bài là phần mở rộng của dự án. Vì vậy nhãn “trọn vẹn đề 100 câu do thầy Đỗ Đình Luật biên soạn” cần đổi thành tuyển tập/biên tập từ các nguồn, hoặc nhập đúng cả 100 câu đề số 3.

Nếu muốn mô phỏng đúng nguồn De_TN_So_3, thời gian là **120 phút**; JSON hiện 90 phút. Nếu cố ý luyện nhanh 90 phút thì ghi rõ chế độ luyện khác thời lượng nguồn. Sửa moduleLabels/moduleOverview 25/25/4 thành thống kê thật.

### 4.5 Một số phần bẫy của bộ cũ chưa được remap

Ví dụ VOAI03-M04 hiện A=Kỳ vọng, D=Phương sai, nhưng phần bẫy lại viết “A (Phương sai)” và “D (Kỳ vọng)”. VOAI02-M02 mô tả chọn B khi nhầm Var=E, trong khi A mới là `(8,8)`. Đây là lỗi nội dung sau đảo options, khác với lỗi key chấm.

Nhiều lời giải mới có đủ bốn heading nhưng dùng bẫy chung cho mọi câu; đạt cấu trúc không đồng nghĩa đạt giải thích từng distractor.

### 4.6 Số liệu và phát biểu được gán cho video chưa có evidence đủ

Đề 04 nói “trích xuất 38 giờ video”, 84% → 97.1%, 41 → 8 lỗi, ngưỡng pixel 9/3, vocab “tối ưu phải 8k”, keypoints “dưới 90 giây”. Chưa có mapping clip/timestamp/transcript để xác nhận các phát biểu cụ thể trong lần audit này.

Cần gắn nguồn và thời điểm thật, hoặc ghi **tình huống giả định / UNVALIDATED**. Không biến cấu hình một baseline thành quy tắc phổ quát.

OLP04-Q04 gọi tác vụ video là “VOAI 2025 tác vụ 2”, nhưng nguồn thực hành được cung cấp là **OLP AI sinh viên 2025 SOLOAI**. Giới hạn chạy lại 20 phút có trong PDF SOLOAI; thời gian 3D-CNN chắc chắn TLE hoặc skeleton dưới 90 giây còn phụ thuộc phần cứng, số frame và chi phí trích keypoints. Q19 cũng chỉ suy ra số forward tăng 24 lần; không suy ra chắc chắn TLE nếu không biết thời gian baseline. Q11 cần viết rõ `1/(2*sigma_1^2)` để tránh cách đọc thành `(1/2)*sigma_1^2`.

## 5. Web, video và notebook

### 5.1 Đồng bộ web cuối: PASS

Sáu JSON khớp nội dung `ALL_EXAMS` của bản HTML cuối. Ba tệp public/dist/live temp bằng nhau, 1,476,526 byte, SHA256:

`e21a67ba8eb172da1ae99aeb478c75e2b009ce3d7f35d264aa04017bef04a885`

Đã mở đủ 5 đề đầu trên browser và mở đề 04 sau reload; dropdown cuối có đủ 6 đề. Các lỗi mất dữ kiện và lời giải mâu thuẫn tái hiện trên live. Tab đang mở từ bản cũ cần reload để thấy bản cập nhật.

### 5.2 Điểm tối đa trên UI: FAIL với các đề mới

`generate_full_hub.py` hardcode mẫu số graded: đề 02=90, các đề khác=100; tự luận: đề 02=60, các đề khác=40.

- Đề 05 đúng phải graded 90, essay 0; UI hiện 100 và 40.
- Đề 04 graded phải 60, essay 40; UI hiện graded 100.
- VOAI 2025 không có essay; UI vẫn hiện essay 40.

Sửa cả header/footer và báo cáo nộp bài: tính tổng điểm theo loại câu, không hardcode theo tên đề.

### 5.3 YouTube: link tồn tại, metadata chưa hoàn toàn đúng

- 24 mapping trong generator/web: **24/24 oEmbed HTTP 200**.
- 46 mapping trong `src/data/videoData.ts`: **46/46 oEmbed HTTP 200**.
- 22/24 mapping trùng § giữa hai nguồn khác ID hoặc startSeconds. Có thể dùng video khác nhau, nhưng cần nguồn mapping thống nhất để bảo trì và xác nhận timestamp.

Sai tên kênh xác nhận ở web:

| § | Kênh đang ghi | Kênh oEmbed |
|---|---|---|
| 1.9 SMOTE | StatQuest / Josh Starmer | Bhavesh Bhatt |
| 2.4 Cross Entropy | Stanford CS229 / VietAI | StatQuest with Josh Starmer |
| 2.5 Optimizers | Stanford CS231n | Siraj Raval |
| 2.8 BatchNorm | DeepLearning.AI / Andrew Ng | namkuner, bản đăng/giảng lại |

§1.7 đặt tiêu đề Precision/Recall/F1/Confusion Matrix nhưng video thực tế là ROC/AUC; §2.2 đặt ReLU/GELU/Sigmoid/Softmax nhưng video là nhập môn neural network. Cần kiểm tra mục tiêu/timestamp, không chỉ HTTP 200.

Kiểm tra oEmbed **không chứng minh** mọi video nhúng phát được, timestamp đúng đoạn, hoặc bao phủ đầy đủ nội dung. Không đánh dấu “đã xem toàn bộ video”.

### 5.4 Khóa học: metadata có nhưng link video ký hạn đã hết hạn

- JSON OLP gốc: 17 mục, có một “Sidebar”; dữ liệu chuẩn hóa: 16 mục.
- JSON VOAI full: 23 mục, có mục sidebar/nhóm; dữ liệu chuẩn hóa: 13 bài. Không suy ra thiếu 10 bài chỉ từ chênh lệch này.
- 19 bài trong `courses_data.json` có URL video ký hạn. Trường expires của nhóm OLP nằm khoảng **19:43–19:46 ngày 08/10**, nhóm VOAI khoảng **14:22–14:23 ngày 09/10**, giờ Việt Nam. Đã quá hạn lúc audit.

Nên dẫn sang **trang lesson ổn định** để người học đăng nhập/lấy link mới, hoặc lưu video khi có quyền. Không dùng URL ký hạn như nguồn xem lâu dài. Không ghi lại token vào báo cáo.

### 5.5 Notebook: 10 tệp, có một lỗi cú pháp

Đường dẫn thật: `C:\Users\HP\Downloads\OLPAI\VOAI NÂNG CAO\Notebooks\` — có dấu **Â**, khác chuỗi “VOAI NANG CAO” được cung cấp.

Đọc được 10 ipynb, tổng 137 code cells. Kiểm tra AST 130 cell thành công, bỏ qua 6 cell chứa magic/shell; 1 cell lỗi:

`Image Captioning\ImageCaptioning.ipynb`, cell index 8, dòng 54 có ký tự `c` đứng riêng, khiến dòng 55 bị `unexpected indent`.

Không chạy huấn luyện, tải dữ liệu hay GPU. AST không chứng minh notebook chạy được, đủ data/dependencies hoặc tái lập kết quả. L13baseline và Lab3_2 không thấy seed explicit qua kiểm tra chuỗi; đây là ghi nhận cần xem khi dùng làm baseline, không phải kết luận mọi notebook còn lại reproducible.

## 6. Kiểm tra đã thực hiện và giới hạn

| Kiểm tra | Kết quả cuối | Phạm vi / ý nghĩa |
|---|---|---|
| `node scripts/validate.mjs` | **FAIL, exit 1** | Chưa khai báo olp-04; 5 đề còn lại qua schema. Không phát hiện key C10 sai hoặc hai options bằng nhau |
| `node scripts/test_html_logic.mjs` | PASS 5 nhóm | Migration, graded/essay, template rỗng, sandbox notice, partial code; chủ yếu fixture đề 01/02/03 |
| `node node_modules/vitest/vitest.mjs run src --no-cache` | PASS 18/18, 4 files | Chạy lại 15:03 sau khi có đề 04; không phải kiểm định nội dung 448 câu |
| `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json` | PASS, exit 0 | Kiểu mã ứng dụng; không bảo đảm dữ liệu essay đúng |
| `python -X utf8 scripts/audit_quality.py` | PASS trong phạm vi cũ | Chỉ đọc 3 đề =234 câu; thông báo hardcode “184”; bỏ 214 câu của 04/05/VOAI25 |
| `node scripts/audit_katex_syntax.mjs` | PASS 3,010 snippets | Chỉ 3 đề cũ + giáo trình/công thức; bỏ các ngân hàng mới |
| Audit toán độc lập `tmp/audit_full_2026-10-09/independent_math_audit.mjs` | PASS cú pháp 3,478 snippets | Quét 6 JSON + toàn văn lý thuyết + 10 công thức web; bỏ code/inline code |
| So nguồn VOAI 2025 | 100/100 key khớp lời giải bên thứ ba | Có lỗi nhập rõ ở bảng trên; chưa có answer key BTC độc lập |
| So SkillPixel | 90 phương án đúng khớp nguồn sau chuẩn hóa | 66 kết luận chữ cái sai trong explanation |
| Browser live | Mở đủ 6 đề, xác nhận lỗi nội dung/rubric/mẫu số | Không nộp bài hoặc xóa bài làm người dùng |
| Notebook | 130 AST PASS; 1 FAIL; 6 magic bỏ qua | Không thực thi notebook |
| Video metadata | 24/24 hub +46/46 React HTTP 200 | Không xác nhận nội dung/timestamp hoặc xem hết video |

**0 lỗi parser KaTeX không có nghĩa không mất công thức**: câu 68 là text hỏng không nằm trong delimiter toán nên parser không thể bắt. Câu 48 đã kiểm tra trực tiếp: backslash sau giải mã JSON hợp lệ, `mathbf` render được; không có lỗi double-escaping ở câu này.

Các lệnh đọc/search phục vụ audit: `Get-Content`, `Get-ChildItem`, scoped `rg/rg --files`; các đoạn Python/Node đọc JSON/HTML, trích PDF bằng pdfplumber, render trang PDF, tính số và gọi YouTube oEmbed. Không chạy generator/build/rebuild và không sửa source. Script check YouTube gốc không được chạy vì nó ghi `video_audit_results.json` ở root; dùng phép kiểm tra tương đương và lưu bằng chứng vào thư mục audit.

Một số lệnh khám phá ban đầu lỗi encoding alias, glob PowerShell hoặc cú pháp snippet đã được sửa rồi chạy lại; không dùng các lần lỗi làm evidence PASS. Danh sách artifact mới nằm trong thư mục audit, bao gồm bản chụp sáu JSON tại `source_snapshot/`, ảnh trang PDF 03/05/06/07/09/10/11/12/13, so sánh 100 câu, mapping 90 câu, kiểm tra toán, video, notebook và manifest/hash cuối.

Báo cáo cũ `BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md` vẫn nói 184 câu và trạng thái chưa đối chiếu đề gốc; không dùng làm nghiệm thu bản mới.

## 7. Có sát VOAI năm ngoái để ôn trong hai ngày không?

**Có nguồn đúng để ôn; bản web hiện chưa bảo toàn đủ đề đó.** PDF gốc mã 006 là điểm tựa đáng tin cho dạng hỏi, độ dài và phân bố chủ đề thực tế. Đề 01/02/03 là ngân hàng luyện mở rộng; tự luận DocViVQA/TSR/DeepFake/SOLOAI giúp luyện thực hành nhưng không có trong phần 100 MCQ của PDF mã 006.

Không thể suy ra đề vòng trường ngày 11/10 chắc chắn giống đề này chỉ từ lời kể các năm trước. Không có thông báo chính thức vòng trường để xác nhận tỷ lệ/chủ đề/thời gian.

Trong thời gian Gemini sửa: làm trực tiếp PDF gốc 100 câu, đánh dấu câu sai/chưa hiểu, ưu tiên ML nền tảng, metrics/confusion matrix, CNN shape/parameters/pooling, NLP/embeddings/attention, Python/API và các câu tính toán gặp thật trong nguồn. Đừng lấy chữ cái đáp án để học thuộc; dùng nội dung/công thức.

Chưa nên dồn thời gian đọc hết phần mở rộng mới, đặc biệt đề 04 có lỗi Q08/Q09/Q13/Q17 và các số liệu video chưa xác minh. Hai ngày còn lại nên ưu tiên luyện và chữa câu nguồn thực tế trước.

## 8. Thứ tự sửa và nghiệm thu

1. Sửa C10, distractor trùng M43; khôi phục dữ kiện/figure/code đề gốc, đặc biệt 12 ID nêu trên.
2. Sửa 66 lời giải đề 05 theo mapping phương án; sửa Q08/Q09/Q13/Q17 đề 04.
3. Bổ sung schema bốn essay đề 04; sửa mẫu số chấm điểm và validator cho đủ sáu đề.
4. Xóa chu kỳ đáp án mock; remap tất cả chữ cái trong bẫy, update cache version khi đổi options/key.
5. Sửa tên nguồn/năm/kỳ thi, moduleLabels, thời lượng mô phỏng, mục §, kênh video và link lesson.
6. Đồng bộ JSON–Markdown–public–dist–live; chạy kiểm tra mới bao phủ **448 câu hiện tại** và browser các câu lỗi. Nghiệm thu có ID/bằng chứng, không chỉ dòng “PASS 100%”.

Prompt giao Gemini nằm trong `docs/PROMPT_GEMINI_SUA_VERIFY_FULL_2026-10-09.md`.
