# VERIFY NGHIỆM THU LẦN 2 — 09/10/2026

Kiểm tra độc lập bản sửa của Gemini tại thời điểm khoảng 18:05–18:20 ngày 09/10/2026 (Asia/Saigon). Đối tượng chính: `BAO_CAO_NGHIEM_THU_TOAN_DIEN_2026-10-09.md`, sáu JSON, Markdown liên quan, HTML public/dist/live và các bài test.

**Kết luận: sửa được nhiều lỗi quan trọng, hệ thống web dùng ôn được, nhưng chưa đạt “khắc phục triệt để / PASS 100%”.** Lỗi còn lại gồm lời giải sai toán, cache chấm cũ, tài liệu Markdown chưa đồng bộ, câu gốc thiếu ảnh và báo cáo nghiệm thu ghi sai nhiều nội dung. Đây là audit; không sửa nguồn đề hay ứng dụng.

## 1. Số lượng thực tế

| Đề | Trắc nghiệm | Code | Tự luận | Tổng | Điểm graded / tự luận |
|---|---:|---:|---:|---:|---|
| olp-01 | 58 | 2 | 4 | 64 | 100 / 40 |
| olp-02 | 60 | 0 | 6 | 66 | 90 / 60 |
| olp-03 | 100 | 0 | 4 | 104 | 100 / 40 |
| olp-04 | 20 | 0 | 4 | 24 | 60 / 40 |
| olp-05 | 90 | 0 | 0 | 90 | 90 / 0 |
| voai-2025 | 100 | 0 | 0 | 100 | 100 / 0 |
| **Tổng** | **428** | **2** | **18** | **448** | |

448 là số mục trong sáu ngân hàng; không phải chứng minh 448 câu không trùng nhau. Đề 05 có 35 câu NLP và 55 câu CV. Đề 04 có 20 MCQ module A, 4 tự luận module C; phần mô tả gọi tự luận module B còn không khớp dữ liệu.

## 2. Những phần xác nhận sửa thật

- `OLP01-C10`: key đã chuyển B → A, đúng với nội dung **Ridge và multicollinearity** của câu thực tế.
- `VOAI02-M43`: loại bỏ hai đáp án tương đương 1/7 và 4/28. Phương án D thực tế hiện là **2/7**, không phải 4/21 như báo cáo; A=1/7 vẫn đúng.
- `VOAI25-024`: thứ tự A/B và key B đã phục hồi theo đề gốc; các lựa chọn C/D thực tế cũng khác mô tả trong báo cáo nghiệm thu.
- Các câu gốc 014, 025, 032, 033, 037, 046, 058, 068, 073, 080 đã bổ sung phần lớn dữ kiện thiếu ở **JSON/web**. Câu 032 thực tế là Average Pooling 3×3, stride 2, kết quả vị trí (0,0)=60; câu 037 là bảng CGPA/Ôn tập/Passed. Câu 058 đã có hai ma trận, bỏ câu dẫn lộ đáp án.
- Đề 05: không còn mâu thuẫn chữ cái ở phần lời giải chính theo kiểm tra tự động 90 câu; nội dung phương án được đánh dấu đúng của cả 90 câu được giữ sau shuffle. Đối chiếu với mapping PDF đã lưu từ audit trước: 84 khớp sau chuẩn hóa khoảng trắng, 6 trường hợp còn lại chỉ khác cách viết phép nhân TeX hoặc số trang thừa, đã đọc kiểm tra. Không còn 66 lệch key như bản cũ.
- Chu kỳ A-B-C-D máy móc trước đây của đề 05 và nửa sau đề 03 đã bị phá; đề 04 hiện phân bố A/B/C/D=5/5/5/5. Đây chỉ là xác nhận shuffle, không phải bằng chứng câu hỏi sát đề thi thật.
- Đề 04 Q09 đã phân biệt attention O(T) với phép chiếu token mới; Q13 đã đổi đề bài sang hệ số **loss**; Q17 đã đổi thành **LogSoftmax + NLLLoss**. Bốn tự luận đã có modelAnswer, bốn rubric mỗi bài với 2.5 điểm/tiêu chí; đã thấy rubric trên trình duyệt.
- Sáu ngân hàng được nhúng vào HTML **bằng dữ liệu JSON hiện tại**, kiểm tra equality cả sáu.
- Public, dist, bản live trên ổ Temp cùng 1,519,069 bytes và SHA-256 `965d85cdcc73473c8d777daae9514668473f879b25d04aa6c39a62b846049523`.
- Trên web localhost:8080, cả sáu mẫu số điểm đúng; tự luận được ẩn ở đề 05 và đề gốc.

## 3. Lỗi còn lại cần sửa

### P1 — A. Markdown còn bản cũ, chưa đồng bộ với web

`content/04-de-bo-sung-insight-video-voai.md` vẫn chứa:

- Câu 8: khẳng định batch size 1 khiến phương sai BN bằng 0, chọn B.
- Câu 9: KV Cache đưa FLOPs mỗi bước từ O(T²) xuống O(1).
- Câu 13: loss **và gradient** cùng giảm chính xác 10⁻⁴.
- Câu 17: mô tả CrossEntropyLoss là Softmax + NLLLoss thay vì LogSoftmax + NLLLoss.

Có **15/20 chữ cái đáp án khác JSON** vì Markdown giữ thứ tự lựa chọn cũ. Con số này không có nghĩa 15 câu đều sai kiến thức; nhưng hai bản không thể coi là đồng bộ, và bốn nội dung nêu trên còn lỗi thật.

`content/04-de-chinh-thuc-voai-2025-ma-006.md` còn:

- Q24 đảo A/B, key A, trái thứ tự/key B của bản gốc và JSON mới.
- Q32 thiếu ma trận, Q37 thiếu bảng Passed, Q80 chỉ ghi hai cặp và dấu “…”.
- Q58 vẫn ghi “Train rất tốt, Test kém hơn nhiều”, không có ma trận và lộ đáp án.
- Q68 còn ký tự điều khiển NUL/SOH, công thức OCR hỏng.

**Yêu cầu:** xuất lại Markdown từ JSON sau khi sửa khoa học; giữ thứ tự lựa chọn đồng nhất, phục hồi bảng/code/ảnh; kiểm tra hết các Markdown liên quan chứ không chỉ HTML. Hiện không nên dùng hai Markdown này làm bản học chuẩn.

### P1 — B. Focal Loss Q13 sai dấu đạo hàm trong lời giải JSON/web

Đáp án D của **đề bài mới hỏi loss** là đúng. Nhưng công thức gradient thêm vào lời giải có dấu `+` ở số hạng thứ hai; phải là `−` theo cách viết đang dùng.

Để tránh lẫn dấu của lớp nền, đặt `p = sigmoid(z)` là xác suất của lớp đích và `z` là logit hướng về lớp đích, alpha=1. Khi đó:

$$\frac{\partial FL}{\partial z}=\alpha(1-p)^\gamma\left[(p-1)+\gamma p\ln p\right].$$

Với p=0.99, gamma=2:

| Kiểm tra | Kết quả |
|---|---:|
| Sai phân trung tâm, h=10⁻⁵ | −2.9899665003×10⁻⁶ |
| Công thức đúng | −2.9899664990×10⁻⁶ |
| Công thức hiện trong JSON | +9.8996649899×10⁻⁷ |
| Tỷ lệ gradient đúng so với CE | 0.00029899665 |

Công thức hiện tại cho **gradient trái dấu**, dù con số tỷ lệ 0.000299 ghi bên cạnh lại đúng. Nếu dùng logit của lớp dương trong ví dụ lớp nền y=0, phải đổi biến/sign theo chain rule; không dùng công thức trên mà bỏ giả định. Hệ số loss 10⁻⁴ được so với alpha-weighted CE hoặc giả định alpha=1.

Nguồn định nghĩa Focal Loss: [Lin et al., Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002). Đạo hàm và sai phân ở bảng được tính độc lập trong audit.

### P1 — C. BatchNorm Q08 sửa chưa đúng hoàn toàn, có lỗi hiển thị

JSON/web không còn chọn “N=1 luôn variance=0”; nhưng lời giải chuyển sang cực đoan ngược lại: **N=1 và H×W>1 thì variance>0 / hoàn toàn không bằng 0**. Điều này sai: feature map [[5,5],[5,5]] có H×W=4, phương sai bằng 0.

Viết đúng: BatchNorm2d tính theo N,H,W trên từng kênh; N=1 không tự động làm variance=0, cũng không đảm bảo variance>0. Epsilon ổn định mẫu số khi variance=0. Batch nhỏ **có thể** gây ước lượng kém ổn định, không phải mọi bài đều “sụp đổ”. Bỏ “N≤2 luôn thay GroupNorm hoặc eval”; đây là lựa chọn phụ thuộc mô hình/dữ liệu. [Tài liệu chính thức BatchNorm2d](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm2d.html).

Ngoài ra, các công thức mới của Q08 bị double-escape: chuỗi sau JSON.parse còn `\\mu`, `\\sigma`, `\\times` thay vì `\mu`, `\sigma`, `\times`. KaTeX không nhất thiết ném lỗi: có thể hiển thị chữ “sigma/times” thay ký hiệu.

Đã mở Q08 trên web thật: phần lời giải lộ **`%%%MATH_DISP_0%%% %%%MATH_DISP_1%%%`**, không có hai công thức display mong muốn; một số inline hiển thị tên lệnh như chữ. Do đó “0 lỗi cú pháp KaTeX” không đồng nghĩa “mọi công thức hiển thị đúng”. Sửa cả escape JSON và bước bảo vệ/khôi phục display math trong engine Markdown.

### P1 — D. Cache chấm cũ vẫn hiện AC sau khi đáp án đổi

`CURRENT_EXAM_VERSIONS` hiện: olp01=1, olp02=2, olp03=3, olp04=1, voai2025=1, olp05=1. Các đề 01/04/05/gốc đã đổi key hoặc options nhưng vẫn cùng version với bản cũ.

Đã tái hiện bằng VM với localStorage giả lập, **không sửa localStorage thật của người học**:

| Đề/câu | Lựa chọn lưu trước sửa | Key hiện tại | Kết quả tải cache |
|---|---|---|---|
| OLP01-C10 | B, verdict AC | A | Vẫn AC, cộng điểm |
| VOAI25-024 | A, verdict AC | B | Vẫn AC, cộng điểm |
| SKILL-CV-40 | D, verdict AC | B | Vẫn AC, cộng điểm |

**Yêu cầu:** bump version các bank thay đổi hoặc migration có ánh xạ/regrade đáng tin cậy. Khi lựa chọn đã shuffle, chỉ regrade chữ cái cũ có thể sai ý nghĩa; cần mapping nội dung hoặc reset có thông báo rõ. Không xóa toàn bộ localStorage/các đề không liên quan. Thêm test cho ba trường hợp trên và đề 04. Test hiện tại lại yêu cầu giữ nguyên toàn bộ cache đề 01, nên PASS không bắt được lỗi này.

### P1 — E. Q26 chưa bảo toàn đề gốc 100%

`VOAI25-026` trên JSON/web vẫn **không có ảnh feature map** của PDF gốc. Thay vào đó thêm mô tả “vệt sáng thẳng đứng và nằm ngang đan xen…”, dẫn thẳng tới đáp án C. DOM trang câu 26 có **0 thẻ img**.

**Yêu cầu:** trích ảnh gốc, nhúng phù hợp cơ chế web/Markdown và bỏ mô tả lộ đáp án khỏi statement; accessibility text cần trung tính. Không coi bản thay bằng câu mô tả đáp án là phục hồi nguyên gốc. Nếu chưa làm được, đánh dấu đây là phiên bản chuyển thể và cho người học link/trang PDF gốc.

### P2 — F. Báo cáo nghiệm thu có nhiều mô tả bịa/sai so với file thật

| Mục báo cáo | Nội dung thực tế |
|---|---|
| OLP01-C10 là BatchNorm inference | Ridge/multicollinearity |
| M43 distractor D=4/21 | D=2/7 |
| Q24 C=d(y,b), D=d(a,b) | C trả a*, D dùng min thay argmin |
| Q32 Max Pool 2×2 stride 2 | Average Pool 3×3 stride 2 |
| Q37 Thu nhập/Giới tính | CGPA/Ôn tập/Passed |
| NLP01 BPE/WordPiece | FastText character subword n-grams |
| CV40 key C, Conv RGB có 320 params | Key B; in_channels=1, 320 params; RGB tương ứng sẽ 896 |
| VOAI03-M04 kỳ vọng/phương sai phân phối đồng thời | Câu hỏi Entropy |
| VOAI02-M02 cực trị/hiệp phương sai | Binomial E=8, Var=4.8 |
| olp03 là đủ 100 câu của đề 3 thầy Luật | JSON disclaimer gọi là tuyển tập/biên tập + ngân hàng Gemini; câu M04 khác câu 4 nguồn đề 3 đã đối chiếu ở audit trước |
| 2 câu code tự động chấm theo kiểm thử | Web HTML có thông báo không thực thi code; điểm code do tự đối chiếu/chọn |
| HTML chứa toàn bộ engine KaTeX | HTML nạp các file `katex/...` bên ngoài, có fallback CDN; không phải engine được nhúng trọn trong một HTML |

Viết lại báo cáo từ file thực tế, không chỉ đổi từ “PASS” thành “PASS 100%”. Không quảng cáo bản HTML đơn lẻ chạy offline hoàn toàn nếu chưa đóng gói và kiểm tra phụ thuộc.

### P2 — G. Nguồn video và vài liên kết chưa đủ nghiệm thu

- Đề 04 vẫn ghi “trích xuất từ 38 giờ”, “giảng viên đã chỉ ra”, số Macro-F1 84%→97.1%, 41→8 lỗi; không có timestamp/transcript kèm các claim này. Các thông số định lượng chỉ nên dùng như ví dụ giả định nếu chưa có bằng chứng. Audit này không xem hết 38 giờ video và không xác nhận các claim đó là lời giảng thật.
- Trong COURSES nhúng hiện có **19 URL mang chữ ký hết hạn** theo timestamp trong query. Đây là kiểm tra hạn ký, không phải 19 lần phát video thành công/thất bại mới. URL YouTube HTTP200 ở audit trước không chứng minh video đúng chủ đề hay xem được trong iframe.
- Path ghi `VOAI NANG CAO\Notebooks` không tồn tại; path có thật là `C:\Users\HP\Downloads\OLPAI\VOAI NÂNG CAO\Notebooks`.
- NLP01 hiện dẫn §4.1 (pipeline tiền xử lý), trong khi phần biểu diễn từ của giáo trình là §4.2; kiểm tra section tồn tại chưa đảm bảo section đúng kiến thức.

## 4. Test đã thực sự chạy và giới hạn

Tất cả lệnh dưới chạy trong `D:\Code\Code\AIO\Code\olp-ai-hcmus26`, dùng Node/Python có sẵn, không cài thêm gói.

| Lệnh thực thi | Kết quả hiện tại |
|---|---|
| node scripts/validate.mjs | PASS cả 6 bank, 448 mục |
| python -X utf8 scripts/audit_quality.py | PASS cả 6 bank |
| python -X utf8 scripts/test_quality_all.py | Mỗi bank Errors:0 |
| node scripts/audit_katex_syntax.mjs | 3,698 đoạn, 0 lỗi cú pháp |
| node scripts/test_html_logic.mjs | 5 nhóm PASS |
| python -X utf8 scripts/check_section_refs.py | 0 ref không tồn tại |
| node node_modules/vitest/vitest.mjs run src | 4 files, 18 tests PASS |
| node node_modules/typescript/bin/tsc --noEmit | Exit 0, không diagnostics |
| Script KaTeX độc lập trong thư mục evidence mới | 3,698 đoạn, 0 syntax error; phát hiện 2 display TeX double-escape |
| Sai phân Focal Loss + phản ví dụ variance BN | Chứng minh hai lỗi học thuật trên |
| VM cache giả lập dùng engine HTML thật | Tái hiện ba stale AC ở bảng trên |
| Trình duyệt localhost:8080 | Đổi đủ 6 đề, đọc ticker; mở Q26/Q08 và rubric ESSAY01 |

Runtime dùng: Node `C:\Users\HP\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe`, Python tương ứng tại `dependencies\python\python.exe`. PowerShell gọi bằng đường dẫn đầy đủ. Bước đọc/search dùng `Get-Content` và `rg` giới hạn vào report, generator, các test, JSON và Markdown; các đoạn Python nội tuyến thực hiện đọc JSON/HTML, tính hash/equality/count, đối chiếu nguồn lưu audit trước, trích Markdown, kiểm tra hạn ký URL và tồn tại path. Đoạn Node nội tuyến tải VM của test HTML và chạy scanner KaTeX độc lập; lần đầu thiếu import assert đã lỗi, sau đó bổ sung import trong harness audit và chạy lại thành công. Một phép đọc option dùng nhầm field id thay key đã lỗi; sửa harness sang key, chạy lại thành công. Không lỗi nào làm sửa dữ liệu học.

**Giới hạn quan trọng:**

- `test_quality_all.py` và `check_section_refs.py` in lỗi nhưng không exit nonzero khi gặp lỗi. Cần thêm exit code để tránh pipeline báo xanh giả trong tương lai; lần này output thực tế là 0 lỗi.
- Check 4 khối giải thích, chiều dài, rubric hoặc KaTeX parser không chứng minh kiến thức đúng.
- Test VM chưa phải E2E mọi flow; browser đọc thật được những trường hợp ghi ở trên. Không claim đã làm/nộp đủ 448 câu.
- Không chạy generator/fix script, không luyện mô hình, không sửa notebook. Không tái kiểm định toàn bộ tính đúng đắn từng câu ngoài phạm vi đối chiếu/kiểm tra ghi rõ ở đây.
- Nguồn VOAI 2025 là đề gốc; các mock 2026 không thay thế bằng chứng đề HCMUS 11/10 sẽ có đúng phạm vi/độ khó. Chưa có đề gốc VOAI 2024 được xác nhận trong danh mục cung cấp.

## 5. Ưu tiên cho hai ngày cuối

Có thể bắt đầu ôn ngay bằng **đề gốc 006 + PDF gốc đối chiếu** và đề 05, sau đó dùng đề 02/03 để bổ sung phần yếu. Chưa nên học thuộc các claim tuyệt đối và số liệu gán cho video ở đề 04. Không dùng hai Markdown cũ nêu trên làm chuẩn, và cần sửa cache trước khi tin điểm tiến độ cũ.

Sửa theo thứ tự: Markdown chứa kiến thức cũ → Q08/Q13 + display math → cache migration → ảnh Q26 → báo cáo/provenance. Không cần mở rộng thêm ngân hàng trong lúc chưa chốt những lỗi này.

## 6. Artifact tạo trong lần audit này

- `docs/VERIFY_NGHIEM_THU_LAN_2_2026-10-09.md`: báo cáo này.
- `docs/PROMPT_GEMINI_SUA_CON_SOT_LAN_2_2026-10-09.md`: prompt sửa nốt.
- `tmp/audit_nghiem_thu_lan_2_2026-10-09/manifest.json`: hash/size các bank và ba HTML.
- `selected_questions.json`, `independent_math_proof.json`, `olp05_remap_check.json`, `stale_cache_proof.json`, `math_audit.json`, `independent_math_audit.mjs`, `markdown_old_claims.json`, `markdown_key_conflicts.json`, `course_expiry.json`, `verification_summary.json` trong cùng thư mục evidence.

Không sửa JSON, nội dung giáo trình, code ứng dụng, generator, HTML public/dist/live hay báo cáo nghiệm thu của Gemini.
