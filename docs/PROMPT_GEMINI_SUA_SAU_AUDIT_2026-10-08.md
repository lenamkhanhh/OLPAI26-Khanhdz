# Prompt giao Gemini sửa bộ ôn OLP AI HCMUS 2026 sau audit

> Sao chép từ phần “Bắt đầu prompt” tới hết file và gửi cho Gemini đang làm dự án.
> Đây là yêu cầu sửa, chưa phải xác nhận các lỗi đã được sửa. Ưu tiên phục vụ ôn ngày 9–10/10, thi ngày 11/10/2026.

---

## Bắt đầu prompt

Bạn đang tiếp tục dự án `D:\Code\Code\AIO\Code\olp-ai-hcmus26`. Hãy sửa bộ tài liệu và web ôn thi theo audit dưới đây. Làm trực tiếp, kiểm tra kết quả và báo cáo đầy đủ; không chỉ trả lời kế hoạch hoặc viết lại tài liệu dài hơn.

### 1. Mục tiêu và phạm vi

- Người học thi vòng trường HCMUS trưa Chủ nhật 11/10/2026; chỉ còn ngày 9 và 10/10 để ôn.
- Thông báo HCMUS xác nhận **thi cá nhân: trắc nghiệm + tự luận giải pháp AI**. Chưa có số câu, thời gian và tỷ trọng điểm chính thức cho vòng trường. Không biến cấu trúc đề luyện thành quy chế thật.
- Các anh năm trước nói phần trắc nghiệm giống VOAI 2025. Dùng đề thật đã tìm được làm nguồn đối chiếu, không tiếp tục lấy đề thi thử 2026 làm bằng chứng cho độ sát năm 2025.
- Giữ phần mở rộng hữu ích nhưng phân biệt rõ: **ôn cốt lõi vòng trường / bài tập mở rộng / chuyên đề thực hành vòng miền**.
- Chỉ sửa có mục đích. Không redesign giao diện, đổi framework, thêm backend, thêm chatbot hoặc mở rộng thêm hàng trăm câu.
- Sửa trong dự án này. Giữ nguyên PDF, notebook, video và tài liệu nguồn ngoài dự án. Không chạy training, không upload/deploy ra ngoài nếu chưa được yêu cầu.
- Đọc AGENTS.md áp dụng, inspect luồng thực thi thật và các script sinh dữ liệu trước khi sửa. Không ghi đè thay đổi của người khác. Không chỉ vá đầu ra nếu generator sẽ sinh lại lỗi cũ.

### 2. Nguồn đúng phải sử dụng

**Thông báo vòng trường HCMUS 2026:**
https://www.fit.hcmus.edu.vn/tin-tuc/d/dang-ky-doi-thi-olympic-ai-hcmus-2026

**Trang BTC chứa đề VOAI 2025:**
https://www.olp.vn/olympic-ai-cho-h%E1%BB%8Dc-sinh/m%C3%B4i-tr%C6%B0%E1%BB%9Dng-%C4%91%E1%BB%81-thi

**PDF đề trắc nghiệm VOAI 2025 thật, mã đề 006:**
https://drive.google.com/file/d/1p7-Nnxxbuwvz0mjj2SnR23WdDTkr_o5h/view

- Tên trên trang BTC: `De-thi-trac-nghiem-soloai-public.pdf`.
- PDF 16 trang, 100 câu, 180 phút; mỗi câu chọn một đáp án, chọn sai không trừ điểm.
- Nếu cần lấy PDF công khai: `https://drive.google.com/uc?id=1p7-Nnxxbuwvz0mjj2SnR23WdDTkr_o5h&export=download`.
- Có code, công thức, ma trận và hình được nhúng dưới dạng ảnh. **Không coi text extraction là đầy đủ**; phải render và đọc những vùng này khi soạn lời giải.
- Chỉ số thời gian 180 phút thuộc đề VOAI 2025, không tự áp dụng thành thời gian thi HCMUS 2026.

**Các nguồn local đã có:**
- `C:\Users\HP\Downloads\DTTN_VOAI_Bien_soan_Practice_1.pdf`: đề **thi thử VOAI 2026**, Đỗ Đình Luật, 50 câu / 60 phút. Không phải đề chính thức VOAI 2025.
- `C:\Users\HP\Downloads\Đề thi Olp_AI_2025 Vòng SOLOAI.pdf`: đề thực hành **Olympic AI sinh viên 2025**, 8 trang, Tác vụ 1 dịch Hoa–Việt, Tác vụ 2 video ký hiệu. Đây là cuộc thi/định dạng khác với trắc nghiệm VOAI dành cho học sinh.
- `C:\Users\HP\Downloads\Advanced_VOAI_L1.ipynb`: notebook giảng dạy, không phải đề thi chính thức.
- `C:\Users\HP\Downloads\OLP_Sinh_Vien_data.json`: danh mục bài học và link tài nguyên, không phải bộ câu hỏi thi.
- Hai file tài liệu/prompt trong Downloads có bản sao tương ứng trong `docs/`.
- Bốn video trong `D:\Code\Code\AIO\AIO26 - OLPAI` là nguồn chuyên đề. Audit mới xác nhận metadata/thời lượng, chưa xác minh toàn bộ lời giảng. Các số F1/tốc độ gán cho video cần timestamp hoặc tài liệu thí nghiệm để xác nhận.

Không tiếp tục ghi “chính thức”, “chuẩn format” hay “bám sát VOAI 2025” nếu chỉ có căn cứ là bộ mock 2026. Không bịa tỷ lệ tương đồng hoặc đáp án BTC.

### 3. P0 — Sửa web và dữ liệu để có thể dùng ngay

#### 3.1 Chuẩn hóa schema có một nguồn sự thật

Các file cần inspect:
`src/types/exam.ts`, `src/data/exams/index.ts`, ba JSON trong `src/data/exams/`, `src/utils/scoring.ts`, `src/utils/storage.ts`, các component lấy metadata và các generator liên quan trong `docs/`.

Hiện tại:
- Web đọc `durationMinutes`, `totalPoints`, `disclaimer`; Đề 02–03 lại ghi `duration_minutes`, `total_points` và thiếu disclaimer.
- Web hỗ trợ module A/B/C. Đề 02 dùng MATH/ML/DL/CV/NLP/ESSAY; Đề 03 có CASE và gán toàn bộ 50 trắc nghiệm vào B.
- 10 bài essay của Đề 02–03 thiếu `modelAnswer` và `rubric`; lời giải/rubric đầy đủ có trong Markdown nhưng chưa được chuyển đúng sang JSON. Riêng bốn essay Đề 03 có explanation “Không có giải thích chi tiết.”

Ưu tiên phương án ít thay đổi nhất: chuẩn hóa JSON về schema web hiện tại A/B/C, dùng `chapter`/`tags` hoặc metadata chủ đề để giữ MATH/ML/DL/CV/NLP. Gán module theo nội dung, không gán tất cả câu thành Python. Đọc thêm schema/reference hiện có trước khi quyết định.

Nếu chọn module động thì phải cập nhật **tất cả** consumer: kiểu dữ liệu, chấm điểm, thống kê, nhãn, palette, selector, validator và tài liệu. Không chỉ thêm optional chaining để che dữ liệu sai.

#### 3.2 Sửa chấm điểm và thời gian

Audit đã tái hiện bằng chính hàm `summarizeExam`:
- Đề 02: làm đúng toàn bộ MCQ -> lỗi `Cannot read properties of undefined (reading 'earned')` do module không khớp.
- Đề 03: đúng 50/50, earned=100 nhưng percent=0 vì `totalPoints` không tồn tại.
- Đề 02–03: `durationMinutes * 60 * 1000` thành NaN.

Quy ước cần giữ:
- Trắc nghiệm + code chấm trong một tổng; tự luận tách riêng.
- Đề 01: 58 MCQ + 2 code = 100 điểm; 4 essay = 40 điểm riêng. Chỉ đúng 58 MCQ thì 86/100 là hợp lý, không phải bug.
- Đề 02 hiện có 60 MCQ × 1.5 = **90 điểm**, 6 essay × 10 = **60 điểm riêng**. Metadata 150 hiện đang cộng chung hai phần. Chuẩn hóa tổng phần graded thành 90; phần trăm đúng hết phải là 100%. Nếu muốn quy đổi sang thang 100, hiển thị phép quy đổi rõ ràng và đồng bộ tài liệu; không đổi trọng số ngầm.
- Đề 03: 50 MCQ × 2 = **100 điểm**, 4 essay = **40 điểm riêng**.
- Kiểm tra chấm điểm một phần cho code: nếu UI cho nhập điểm số thì tổng kết phải dùng số điểm đã chấm, không tự biến thành 0/toàn điểm chỉ vì vượt ngưỡng pass. Phân biệt số điểm với nhãn đúng/pass.
- Metadata thời gian luyện phải hợp lệ và đồng hồ hoạt động. Giữ 90 phút hiện có nếu không có lý do thay đổi; ghi là thời gian luyện gợi ý.

#### 3.3 Sửa essay và hiển thị lời giải

- Chuyển đầy đủ rubric và lời giải từ Markdown sang `rubric: string[]` và `modelAnswer: string`, giữ ý nghĩa và điểm.
- Mở gợi ý, đáp án mẫu, tự chấm ở cả 10 essay phải hoạt động, không gọi `.map` hoặc `.split` trên undefined.
- Đề 02 hiện chứa raw HTML trong explanation; `MathText` escape HTML nên người học nhìn thấy `<div ...>` thành chữ. Chuyển lời giải về Markdown/text + công thức theo renderer hiện có. **Không sửa bằng cách cho phép mọi raw HTML chạy trực tiếp.**
- Kiểm tra công thức, code block và xuống dòng sau khi chuyển đổi; không chỉ kiểm JSON parse được.

#### 3.4 Sửa validator và đồng bộ bản build

- `scripts/validate.mjs` hiện ép mọi đề phải có 60 graded, 2 code, 4–5 essay, module 12/18/30, graded 100 điểm. Đó là cấu trúc Đề 01, không phải điều kiện chung.
- Validator phải kiểm cấu trúc thực của từng đề và tổng điểm thật: ID, loại câu, option, answer key, lời giải, rubric, thời gian, module hợp lệ, tổng graded/essay riêng. Giữ kiểm tra chặt, không tắt hàng loạt assertion để có PASS.
- Câu trùng hợp lệ giữa đề nguồn và biến thể phải có provenance; không ép xóa câu chỉ vì cùng stem.
- Hai bundle hiện có trong `dist` không chứa ID câu Đề 02–03. Build lại đúng entry point sau khi sửa. Kiểm tra route/người học thực sự mở bản nào, tránh chỉ sửa React trong khi người học đang dùng một HTML hub cũ.
- Đồng bộ nội dung nguồn, generator, `theoryData.ts`, JSON và bản hiển thị liên quan. Chỉ rebuild PDF nếu thực sự được dùng trong ôn tập và cần cập nhật nội dung.

### 4. P1 — Sửa nguồn, đáp án và các diễn giải gây học sai

#### 4.1 Đổi nhãn nguồn cho đúng

- 50 câu Đề 03 đi theo 50 câu của mock Đỗ Đình Luật 2026. Đổi tên/mô tả thành đề luyện từ **thi thử VOAI 2026 + chuyên đề thực hành mở rộng**.
- Phân biệt đề chính thức, đề thi thử, bài phỏng theo và tình huống giả định. Các con số dữ liệu tự thêm như 10.000 clip/100 người/200.000 cặp câu phải ghi là giả định của bài luyện nếu không có nguồn.
- Nguồn SOLOAI đánh số task 1=NMT, task 2=video; sửa các chỗ đảo thứ tự nếu đang nói về đề gốc.
- `content/01-giao-trinh-ly-thuyet.md` không tồn tại ở thời điểm audit. Không tuyên bố đã cập nhật file đó. Xác định `01-ly-thuyet-olp-ai.md` là nguồn chính hoặc tổ chức lại có dẫn đường rõ ràng.
- Giáo trình hiện có §8 là 50 câu mock; `theoryData.ts` chưa có DocViVQA/Header-Anchor/GriTS/center60. Không tiếp tục mô tả rằng web đã có chương chuyên đề khi chưa đồng bộ.

#### 4.2 Hiệu chỉnh các ý sau trên mọi bản sao liên quan

1. **NLP pipeline:** bỏ “thứ tự bắt buộc duy nhất”. Normalization/tokenization/POS/lemmatization phụ thuộc pipeline. Đề 01 C28, Đề 02 M49 và §4.1 cần sửa stem/options để có một đáp án hợp lý trong bối cảnh xác định. Code M49 đang `word_tokenize(text.lower())`, tức lowercase trước tokenization, trái với lời giải hiện tại. Không học thuộc sai để đối chiếu câu 14 đề thật.
2. **BatchNorm:** Linear/Conv -> BN -> ReLU là block thông dụng, không phải mọi thứ tự khác đều sai. Giữ câu hỏi nếu hỏi cấu hình phổ biến, bỏ khẳng định độc tôn.
3. **ViT:** bỏ “hoàn toàn không dùng convolution”. Giải thích patch projection có thể dùng Conv2D tương đương phép chiếu patch; backbone xử lý token bằng Transformer. Sửa Đề 01 C24 và bảng bẫy §6.
4. **KV cache:** giảm tính toán lại, nhưng chiếm VRAM tăng theo độ dài context/batch. PagedAttention quản lý cache hiệu quả hơn. Đề 03 M30 đang gộp tiết kiệm bộ nhớ với tránh tính toán lại; sửa để không có xung đột giữa stem và lời giải.
5. **TabM:** sửa ICLR 2024 -> **ICLR 2025**; diễn giải ensemble chia sẻ tham số, không khẳng định chỉ phân nhánh ở tầng cuối. Không coi nó luôn nhanh hơn/thắng mọi GBDT. Repo tác giả: https://github.com/yandex-research/tabm .
6. **Entropy:** log2 cho đơn vị bit; log tự nhiên cho nat cũng hợp lệ. Nếu hỏi cơ số, phải nêu đơn vị/quy ước. Không ghi mọi entropy bắt buộc log2.
7. **Cosine:** thường dùng cho embedding, không bắt buộc thay mọi khoảng cách khác.
8. **ResNet:** tạo đường truyền gradient thuận lợi hơn; không bảo đảm mọi gradient luôn khác 0 hoặc giải quyết triệt để mọi vấn đề tối ưu.
9. **Quantization:** thường giảm bộ nhớ, có thể tăng tốc khi backend phù hợp; accuracy có thể thay đổi. Bỏ “không bao giờ tăng accuracy” và “luôn tăng tốc trên mọi thiết bị”.
10. **Validation:** stratification là lựa chọn tốt cho nhiều bài phân loại IID mất cân bằng, không thay thế chia theo thời gian/người/tài liệu/nhóm. E04 nếu một sample là một cặp ảnh thì StratifiedKFold trên cặp có thể hợp lệ; nếu flatten thành ảnh thì cần split pair_id hoặc Group/StratifiedGroupKFold. Nêu granularity, không gọi đó là lỗi chắc chắn khi chưa inspect cách tạo sample.
11. **GBDT:** baseline mạnh cho tabular, không “luôn vượt trội deep learning”.
12. **RAG:** không bảo đảm Zero Hallucination. Đề xuất retrieval tốt, grounding, kiểm chứng nguồn và abstention khi thiếu chứng cứ; trình bày latency như mục tiêu cần đo.

#### 4.3 Sửa rubric/chấm tự luận để không thưởng câu trả lời sai

Kiểm tra cả `src/utils/aiEvaluator.ts`, không chỉ sửa lời giải hiển thị:
- OLP01-E01 hiện là **phân loại clip vào 50 ký hiệu**, nhưng rubric và evaluator lại ưu tiên CER/WER/CTC. Với bài phân loại clip kiểu SOLOAI, metric nguồn là **Macro-F1**; có thể bổ sung accuracy, confusion matrix. CTC/CER/WER dành cho bài nhận dạng chuỗi ký hiệu liên tục phù hợp, không bắt người học viết chúng cho mọi video task.
- OLP01-E02 và §7.2 đang khuyến nghị pretrained NLLB/mBART trong một bài gắn với SOLOAI. PDF gốc cấm mô hình dịch Hoa–Việt pretrained. Hoặc bám ràng buộc đề gốc và sửa rubric/evaluator tương ứng, hoặc đổi nhãn thành tình huống giả định cho phép pretrained. Không vừa gắn “giống đề gốc” vừa thưởng vi phạm ràng buộc.
- Trợ lý hiện có logic theo keyword: ghi rõ đây là hỗ trợ tự đánh giá theo rubric, không phải chấm thi chính thức. Kiểm tra câu viết đúng mà dùng từ khác, hoặc liệt kê keyword nhưng lập luận sai. Không mở rộng thành dự án chatbot mới.

#### 4.4 Các số liệu và snippet

- Các claim như CPU <5ms, pipeline 120ms/trang, private test <1 phút, train chỉ 10 phút, F1 84.2% -> 97.1%, beam search chắc tăng 2–3 BLEU, 30–50 người dùng đồng thời cần nguồn và điều kiện đo. Nếu chưa xác minh, bỏ số hoặc ghi là ví dụ/kết quả cụ thể cần kiểm chứng; không gọi là quy luật hay độ ổn định tuyệt đối trên private test.
- Threshold 42%, thin/thick 9px, gap 3px, center crop 60% là hyperparameter minh họa, cần tune/scale theo dữ liệu; không biến thành rubric bắt buộc cho mọi bài.
- Các snippet hiện parse được sau khi bỏ thụt lề trình bày, nhưng phần lớn là minh họa. Đánh dấu placeholder và điều kiện chạy rõ ràng. M45 Đề 02 dùng `np.arange` thiếu import NumPy.
- Không sửa notebook nguồn ngoài dự án. Nếu dùng nó trong tài liệu, ghi rõ lỗi `os.path.existsb`, sampling thiếu random_state và việc chọn model bằng test score; đưa cách làm đúng là validation/CV để chọn, test để đánh giá cuối.

### 5. P1 — Khắc phục thiên lệch vị trí đáp án

Phân bố hiện tại:

| Đề | A | B | C | D |
|---|---:|---:|---:|---:|
| 01 — 58 MCQ | 15 | 15 | 14 | 14 |
| 02 — 60 MCQ | 12 | 45 | 3 | 0 |
| 03 — 50 MCQ | 25 | 20 | 4 | 1 |

- Đề 02 chọn toàn B đúng 75%; Đề 01 có nhiều đoạn A/B/C/D lặp theo chu kỳ. Sửa đề luyện để không thưởng việc học vị trí đáp án.
- Đảo **vị trí option**, không đổi nội dung đúng chỉ để cân bằng. Với đề tự soạn 60 câu, khoảng 15 câu mỗi chữ là mục tiêu hợp lý nhưng không ép bằng cách sửa kiến thức.
- Dùng seed cố định và ghi seed cho việc sinh thứ tự. Kiểm tra theo option text đúng trước/sau; cập nhật key, lời giải nhắc chữ cái, Markdown, JSON, generator cùng lúc.
- Với câu “cả A và C” hoặc đáp án tham chiếu option khác, không shuffle mù. Chuyển thành phát biểu tự đủ nghĩa hoặc cập nhật mọi tham chiếu và kiểm tra lại.
- Đề gốc chính thức phải được giữ nguyên thứ tự/nhãn để tra cứu; nếu muốn luyện xáo trộn thì tạo chế độ/biến thể có mapping nguồn rõ ràng.
- Việc đổi A/B/C/D làm tiến độ cũ không còn tương thích. Version dữ liệu và invalidate/migrate tiến độ, kết quả **chỉ của đề bị đổi**; không `localStorage.clear()` toàn bộ hoặc phá dữ liệu người dùng không liên quan.

### 6. P2 — Làm bộ ôn nước rút đúng trọng tâm

Sau khi P0/P1 hoạt động, bổ sung nguồn trắc nghiệm VOAI 2025 thật vào tài liệu/web theo cách có thể kiểm tra nguồn:
- Nếu nhập đủ 100 câu, giữ số câu nguồn, trang PDF và provenance; đọc cả hình/code, không bịa phần không trích xuất được.
- Khi chưa kiểm hết đáp án, đặt câu đó ở trạng thái “chưa xác minh/không chấm tự động” hoặc chỉ cung cấp bản PDF để luyện. Không phát hành answer key đoán như đã xác minh. Không để renderer/scorer nhận trạng thái chưa hỗ trợ.
- Với câu gốc có diễn đạt mơ hồ hoặc nhiều phương án có vẻ hợp lệ, ghi chú và lập luận; không tuyên bố một key là của BTC nếu không có key chính thức.
- Nếu thời gian sửa hạn chế, hoàn thành P0/P1 rồi đặt link đề thật và chỉ bổ sung các dạng còn thiếu đã kiểm được. Không chặn bộ ôn dùng ngay vì một lần nhập 100 câu chưa xong.

Ưu tiên ôn: đọc code và shape tensor; CNN/pooling/tham số/FLOPs; loss/logits/train loop; k-NN/SVM/cây/ensemble; preprocessing/validation/metrics; embeddings/Transformer; tình huống OOM, loss plateau, overfit và transfer learning.

Các câu đề thật đáng tập trung khi đối chiếu: **6, 10, 18, 25, 27, 32, 33, 37–38, 43, 73, 75, 80, 83, 94, 100**. Đây là danh sách luyện, không phải dự báo câu sẽ thi.

Giữ phần Hessian/Jensen/Mahalanobis/importance sampling và pipeline DocVQA/Table/DeepFake/enterprise RAG trong mục mở rộng. Đừng để chúng lấn át phần cốt lõi hoặc ép người học thuộc kiến trúc/số liệu của một lời giải duy nhất.

Tạo một trang/bảng ôn ngày 9–10/10 ngắn gọn: đề thật -> chữa câu sai -> luyện tính tay/code -> hai bài tự luận có bấm giờ. Phân bổ gợi ý 75% trắc nghiệm và 25% tự luận; ghi là lịch ôn đề xuất, không phải trọng số điểm thi.

### 7. Tiêu chí nghiệm thu bắt buộc

Thực hiện kiểm tra phù hợp, báo đúng lệnh và kết quả thực tế:

1. `npm run validate` phải qua validator đã sửa có ý nghĩa. Không PASS bằng cách tắt assertion hoặc bỏ các đề lỗi khỏi danh sách.
2. `npm run test` với test hồi quy cho các lỗi chấm điểm/schema, thiếu rubric, thời gian và lưu tiến độ sau đổi options. Bổ sung test thiết yếu, không viết test chỉ lặp lại implementation.
3. `npm run build` thành công; bản build chứa dữ liệu hiện hành.
4. Chấm đúng toàn bộ phần graded: Đề 01 = 100/100 khi cả code đã chấm đủ; Đề 02 = 90/90 = 100%; Đề 03 = 100/100 = 100%. Essay không làm đổi mẫu số này.
5. Không trả lời = 0%; sai một MCQ trừ đúng điểm câu đó; điểm essay/code nhập một phần được cộng đúng; không có NaN/undefined ở kết quả.
6. Mở cả ba đề trên browser thật: selector, timer chạy, đổi câu, trả lời, nộp, review và restart. Không crash, không lỗi console do dữ liệu đề.
7. Mở hint/model answer/self-score ở 10 essay Đề 02–03; đọc được rubric/lời giải đúng câu. Đề 02 không hiện raw HTML; công thức và code hiển thị đúng.
8. Markdown và JSON khớp nội dung, answer key, điểm, count và source. Hiện có 184 câu = 168 MCQ + 2 code + 14 essay; nếu thay số lượng phải báo lý do và count mới.
9. Test tiến độ/kết quả cũ: dữ liệu đã đổi option không bị chấm theo key mới một cách âm thầm; đề không đổi không bị mất tiến độ ngoài ý muốn.
10. Nếu có thêm câu gốc dùng ảnh/code, kiểm bằng render PDF và kiểm đáp án độc lập. Báo câu nào còn chưa xác minh.

Không gọi AST parse là đã chạy snippet; không gọi build thành công là đã kiểm browser; không gọi tự chấm keyword là xác nhận chất lượng tự luận.

### 8. Kết quả phải giao

- Code/dữ liệu/tài liệu đã sửa và dùng được trong dự án, không chỉ một bản đề xuất.
- Một báo cáo Markdown ngắn trong `docs/`: file đã sửa, thay đổi chính, lệnh đã chạy, test/build/browser thực tế, count/điểm/phân bố key trước–sau, nguồn được xác minh, hạn chế còn lại.
- Chỉ rõ cách mở **đúng bản web đã kiểm**, và thứ tự tài liệu người học nên ôn trong hai ngày.
- Nếu PDF chính thức chưa nhập hết hoặc video chưa kiểm timestamp, nói rõ; không tuyên bố đã hoàn thành phần đó.
- Hoàn thành sửa lỗi chặn việc ôn trước rồi mới bổ sung nội dung. Không triển khai thêm các ý tưởng ngoài phạm vi này.

## Hết prompt
