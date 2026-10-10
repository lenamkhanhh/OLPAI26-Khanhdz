# VERIFY NGHIỆM THU LẦN 3 — 09/10/2026

Thời điểm kết thúc kiểm tra: 2026-10-09T19:14:18 (Asia/Saigon).

Đối tượng: bản nghiệm thu mới ghi 19:05, sáu JSON, các Markdown trong content/, HTML public/dist/live và tám suite được liệt kê ở mục VI. Audit độc lập sau vòng 2; không sửa ngân hàng câu hỏi, code hay sản phẩm học tập.

**Kết luận: web đủ dùng để tiếp tục ôn thi; các lỗi Focal Loss, BatchNorm, ảnh Q26 và cache vòng trước đã được sửa thật. Chưa xác nhận “toàn bộ tài liệu đồng bộ 100%” hoặc chấp nhận báo cáo nghiệm thu hiện tại làm chuẩn đáp án.** Báo cáo vẫn ghi sai bốn câu; đề 02 Markdown còn lỗi hai đáp án IoU tương đương. Đây là mức sẵn sàng của công cụ trong phạm vi đã kiểm tra, không phải chứng nhận toàn bộ 448 câu đúng khoa học hoặc dự đoán đề HCMUS ngày 11/10.

## 1. Kết quả 12 câu được yêu cầu

| ID | Nội dung và kết quả hiện tại trong JSON/web | Đánh giá |
|---|---|---|
| OLP01-C10 | Ridge/đa cộng tuyến; **A** | Đáp án phù hợp; phát biểu khả nghịch cần điều kiện lambda>0 |
| VOAI02-M43 | IoU=400/(1600+1600−400)=1/7; **A**; D=2/7 | Đã hết trùng đáp án ở JSON |
| VOAI25-024 | **1-NN**, chọn nhãn y* của mẫu a* gần x nhất; **B** | JSON và đề gốc đúng; báo cáo ghi K-Means/C là sai |
| VOAI25-026 | Feature map từ PDF, **C** | Có ảnh gốc, bỏ spoiler, web tải Base64 thành công |
| VOAI25-032 | Average Pool 3×3 stride2; trung bình cửa sổ đầu=60; **C** | JSON đúng; báo cáo ghi B là sai |
| VOAI25-037 | 4 Passed, 2 Failed; entropy=0.918295834 bit, gần0.92; **C** | JSON đúng; báo cáo ghi3/3, H=1, B là sai |
| SKILL-NLP-01 | FastText character subword n-grams; **A**, ref§4.2 | Đã sửa ref đúng phần biểu diễn từ |
| SKILL-CV-40 | Conv1→32, kernel3, bias:32×(9+1)=320; **B** | Đúng |
| VOAI03-M04 | Khái niệm Shannon Entropy; **C** | Đúng; đây là nhận diện khái niệm, không phải yêu cầu tính H từ dữ liệu cụ thể |
| VOAI02-M02 | Binomial n20,p0.4: E=8, Var=4.8; **D** | JSON đúng; báo cáo ghi công thức PMF/keyA là sai |
| OLP04-Q08 | Thống kê N,H,W; không còn khẳng định N1 luôn variance0 hay luôn>0; **A** | Đã sửa lỗi trọng yếu |
| OLP04-Q13 | Hỏi hệ số **loss**, alpha1, giảm10⁻⁴; **D**; gradient có giả định logit lớp đích | Đã sửa đúng đạo hàm và phân biệt loss/gradient |

**Không đổi JSON theo các key sai của báo cáo nghiệm thu.** Báo cáo cần sửa theo dữ liệu và PDF gốc.

## 2. BatchNorm và Focal Loss: kiểm tra độc lập

BatchNorm2d Q08 hiện tính mean/variance theo mỗi kênh trên N×H×W; công thức variance dùng mẫu số m là estimator dùng trong forward. Cách chuẩn hóa với sqrt(variance+epsilon) đúng. Lời giải nêu rõ feature map đồng nhất vẫn có variance0; gợi ý GroupNorm/LayerNorm/FrozenBN đã chuyển thành lựa chọn tùy bài toán. Phần công thức đang viết normalized x, nên chưa có gamma/beta không phải lỗi định nghĩa output.

Nguồn đối chiếu: [tài liệu chính thức PyTorch BatchNorm2d](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm2d.html). Không suy rộng kết luận này sang tình huống training chỉ có đúng một phần tử trên kênh (N×H×W=1); đó là điều kiện khác với ví dụ ảnh độ phân giải cao của câu hỏi.

Focal Loss với alpha=1, p=sigmoid(z) và z hướng về lớp đích:

$$FL=-(1-p)^\gamma\ln p,$$
$$\frac{\partial FL}{\partial z}=(1-p)^\gamma[(p-1)+\gamma p\ln p].$$

Công thức này đã có đúng trong JSON, Markdown đề04 và DOM KaTeX. Khi p0.99,gamma2:

- Giải tích: −2.9899664989932935×10⁻⁶.
- Sai phân trung tâm h10⁻⁵: −2.9899665003275762×10⁻⁶.
- Độ lệch tuyệt đối khoảng1.33×10⁻¹⁵; tỷ lệ so với CE khoảng0.00029899665.

Không còn sai dấu ở số hạng đạo hàm. Lời giải ghi đúng giả định logit lớp đích, alpha1/alpha-weightedCE. Nguồn định nghĩa: [Lin et al., Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002); đạo hàm và sai phân được tính độc lập trong audit.

Trình duyệt thật: Q08 hiện **3 display formulas**, Q13 có display derivative; không thấy placeholder toán học hoặc katex-error ở hai câu. Đây là kiểm tra DOM thực, bổ sung cho parser test.

## 3. Ảnh Q26 và tính toàn vẹn HTML

- Đọc ảnh ở trang5 PDF gốc bằng pypdf, ảnh1045×1041. So sánh **pixel RGB bằng nhau** với asset hiện tại; đã nhìn ảnh để xác nhận đó là feature map.
- public/assets, dist/assets, content/assets/voai2025_q26.png cùng754,987 bytes, SHA256 `396b065dbfdfc0d4dfdb314a53e0621bd734a4828b1b23c62823e7f897d42db5`.
- Image trong JSON là đường dẫn assets; generator đổi thành data:image/png;base64 trong ALL_EXAMS. Decode Base64 cho byte bằng asset public.
- Browserlocalhost8080: img.complete=true, naturalWidth1045, naturalHeight1041; statement không chứa “vệt sáng”.
- Sáu ALL_EXAMS khớp JSON sau **chuẩn hóa duy nhất field image từ Base64 về đường dẫn nguồn**; không coi phép chuyển dạng hợp lệ này là sai đồng bộ.
- Public, dist và bản server trong Temp cùng **2,526,622 bytes**, SHA256 `5700eb35eaf870146c4fee74ef596b6e825008cdf64d5459acc74ea91aaeb4c6`; đúng số trong báo cáo mới.
- Số lượng giữ nguyên **448 mục =428MCQ+2code+18essay**, không chứng minh448câu khác nhau.

## 4. Cache migration

Bốn bank olp01/04/05/voai2025 đã tăng v1→v2. Code thực tế là loadSavedState, không phải hàm migrateLegacyStorage như tên gọi trong báo cáo.

Tái hiện độc lập bằng localStorage giả lập trong VM, với các AC cũ ở OLP01-C10(B), OLP04-Q13(B), VOAI25-024(A), SKILL-CV-40(D): cả bốn được reset đúng, version2, marker cài đặt ngoài bank vẫn giữ. Không sửa localStorage thật để tạo fixture.

TestHTML hiện kiểm tra01/gốc/05 và giữ tiến độ02v2. Audit bổ sung04 vì test hiện chưa có trường hợp này. **Lỗi stale AC vòng2 đã xử lý.** Báo cáo nói có Toast thông báo, nhưng HTML/generator không có toast hay migrateLegacyStorage; runtime chỉ console.warn rồi reset. Đây là mô tả UI chưa thực hiện, không làm mất hiệu quả reset.

## 5. Markdown: chưa đồng bộ đủ sáu ngân hàng

Đối chiếu theo ID câu và các trường prompt/options/answer/explanation/modelAnswer; loại bỏ khoảng trắng khi so sánh, không đòi hỏi định dạng file byte-identical. Kiểm tra riêng ý nghĩa phương án đúng để tránh nhầm “đổi chữ cái” với “sai kiến thức”.

| Bank / tài liệu | Kết quả |
|---|---|
| voai2025 / 04-de-chinh-thuc-voai-2025-ma-006.md | **PASS**100câu: prompt/options/key/explanation hiện khớp JSON; Q26 có ảnhMarkdown; bảng/ma trận/8cặp Q80 và TeX Q68 được phục hồi |
| olp04 / 04-de-bo-sung-insight-video-voai.md | **PASS**24câu: khớp prompt/options/key/explanation/modelAnswer; không còn bốn lỗi khoa học cũ trong bản này |
| olp02 / 02-de-chuan-format-voai-expand.md | **Chưa khớp**: các lời giải chưa giống JSON, một số khác biệt chỉ biên tập/TeX. **Lỗi chắc chắn còn:** M43D vẫn4/28, tương đương A1/7, trong khi JSOND2/7 |
| olp03 / 03-de-vong-mien-voai-2025.md | **Chưa đồng bộ**:37/100key khác do giữ thứ tựoptions cũ; nội dung phương án đúng vẫn khớp. M04/M16 lời giải khác;4tựluận thiếu bài modelAnswer đầy đủ so với JSON. Lời dẫn vẫn gán bộ100câu cho thầyLuật, trái disclaimer tuyển tập+Gemini của JSON/báo cáo |
| olp05 / 05-chuyen-de-thuc-chien-cv-nlp.md | **Chưa đồng bộ**:68/90key khác vì options bản khác; toàn bộ nội dung phương án đúng vẫn tương ứng JSON, không kết luận68câu sai. Lời giải90câu chưa khớp và NLP01ref cũ còn§4.1 trong khi JSON đã§4.2 |
| olp01 / 02-de-luyen-olp-ai.md + 03-dap-an-olp-ai.md | Là phiên bản biên tập cũ với options khác; C10B trongMarkdown làL2 phù hợp lựa chọn riêng của bản đó, trongJSONL2 ởA. Không gọi đây là bản đồng bộ key/options vớiJSON |

**Hành động tối thiểu:** sửa M43Markdown ngay; xuất các bản chuẩn03/05/01 và cập nhật02 từJSON, hoặc ghi rõ “phiên bản biến thể, khác thứ tựoptions” để người học không chuyển key giữa các bản. Không sửa keyMarkdown đơn lẻ mà quên chuyển options/lời giải.

Không dùng các số66/90/37 để diễn giải thành sốcâu sai khoa học: strict diff chỉ xác định nội dung không đồng bộ, cần đọc ngữ nghĩa như ví dụM43.

## 6. Tám suite đã chạy lại

Tất cả chạy từ root dự án, bằng Node/Python có sẵn. npm/npx được thay bằng gọi trực tiếp entrypoint local tương ứng; không cài gói, không rebuild/mutation code.

| STT | Lệnh thực thi | Kết quả |
|---|---|---|
|1|node scripts/validate.mjs|Exit0;6bank448mục|
|2|python -X utf8 scripts/test_quality_all.py|Exit0;Errors0 từngbank|
|3|python -X utf8 scripts/check_section_refs.py|Exit0;0invalidrefs|
|4|node scripts/audit_katex_syntax.mjs|Exit0;**3724**snippets,0syntax/delimitererrors|
|5|node scripts/test_academic_rigor.mjs|Exit0;finite difference khớp;0doubleescape theo phạm vi scanner|
|6|node scripts/test_html_logic.mjs|Exit0;5nhóm migration/ticker/essay/codePASS|
|7|node node_modules/vitest/vitest.mjs run src|Exit0;**4files,18testsPASS**|
|8|node node_modules/typescript/bin/tsc --noEmit|Exit0;khôngdiagnostics|

Hai Pythonchecks đã có exit1 khi lỗi; không còn tình trạng chỉ in lỗi rồi exit0 của bản trước. Không tiêm fixture lỗi vào thư mục dữ liệu thật.

Giới hạn của tests:

- Academicrigor so gradient từ công thức hardcode trong script, không tự xác minh biểu thức trong câuJSON; audit đã đọc JSON và DOM thật để bù phạm vi này.
- Placeholdertest quét HTML nguồn không đủ chứng minh mọi DOM render; audit chỉ mở trực tiếp Q08/Q13.
- Scanner doubleescape không duyệt mọi options và không phải chứng minh toàn bộ syntax/tri thức; dùng cùng suiteKaTeX và kiểm tra các trường hợp thực tế.
- Không suite nào hiện đối chiếu đầy đủ6bank với tất cả Markdown, nên8PASS không chứng minh “Markdownđồngbộ100%”.
-59sectionstrings bao gồm các tham chiếu root như§1., không có nghĩa59subsections riêng biệt đã thẩm định.

## 7. Báo cáo nghiệm thu còn sai; cần sửa trước khi dùng làm tài liệu học

**Bốn lỗi rõ ràng:** Q24phải1NN/B, khôngKMeans/C; Q32phải60/C, khôngB; Q37phải4T2F,H≈0.9183/C, không3/3,H1/B; M02phảiE8Var4.8/D, khôngkeyA củaPMF.

Các claim khác chưa được thực hiện như ghi:

- “Tất cảMarkdownđồngbộ100%”: chỉ xác nhận đầy đủ hai bản04/gốc; các bản khác còn nêu ở mục5.
- “CácsốvideođãđịnhdanhUNVALIDATED”: **không có UNVALIDATED trongHTML hiện tại**; JSON04metadata còn “trích xuất38giờ” vàQ01 vẫn gán84→97.1%,41→8lỗi cho giảng viên. Muốn gọi mô phỏng cần sửa nhãn ngay trên câu/web/Markdown, hoặc cung cấp transcript/timestamp. Không chỉ ghi một disclaimer trong báo cáo kỹ thuật.
- “19linkCoursera”: COURSES thực tế có19linkiframe.mediadelivery.net,21Drive,6GoogleDocs và **0linkCoursera**.19signediframeURL đều hết hạn theoexpiresquery hiện tại. Audit lần này kiểm tra hạnký, không thửphát19video/đăngnhập; không tự kết luận có thể khắc phục bằng Coursera.
- Mô tả đề04metadata còn gọi tựluậnmoduleB, dữ liệu thậtmoduleC.
- MigrationToast chưa có như nêu ởmục4.

Các lỗi mô tả không làm key đúng trên web biến thành sai; nhưng báo cáo không đáng dùng như tóm tắt kiến thức/đáp án chuẩn ở trạng thái hiện tại.

## 8. Mức sẵn sàng trước 11/10/2026

**Đủ sẵn sàng để ôn bằng web trong phạm vi đã kiểm tra:** schema,điểm,các câu trọng yếu,ảnh,công thứcQ08/Q13,cache và bảnHTMLđồngnhất đều ổn. Có thể dùng đề006+PDFgốc,đề05 vàcácmock để luyện kiến thức; không cần tiếp tục mở rộng đề trước khi hoàn thiện bản chuẩn.

**Chưa nghiệm thu toàn bộ bộ tài liệu:** sửa bốn lỗi báo cáo vàM43Markdown trước; chuẩn hóa các Markdown còn lại và nhãn dữ kiện mô phỏng.8suitePASS không chứng minh mọi câu trong448mục chính xác khoa học hoặc đúng nội dung kỳthiHCMUS. Không có bằng chứng mới nào ở lần kiểm tra này để bảo đảm mức độ trùng đề ngày11/10.

## 9. Phạm vi thao tác và artifact

Chỉ tạo file báo cáo,prompt và evidence mới; không sửa sourceJSON/Markdownhọc,HTML,generator,asset hay báo cáo củaGemini. Các lệnh đọc/search: rg scopedMemory/project, Get-Content(report,tests,generator,PDFskill); Pythonnội tuyến cho snapshot/hash,JSON/HTMLnormalize,soMarkdown,phép toán,signedexpiry,pypdfimagepixelcompare; Nodenội tuyến chạyVMcachefixture. Một harnessPythonsoMarkdown có lỗi dấu ngoặc đã sửa và chạy lại. Parser soMD ban đầu cắt ở headingslờigiải và khớpM10/M100 theo substring; đã chỉnh và lưu kết quả cuối theoIDđầyđủ; không dùng falsepositives này kết luận lỗi dữ liệu. Kiểm tra thư viện/tài liệu chính thức quaweb; browser đọcQ26,Q08,Q13,không làm/nộp448câu.

Evidence: `tmp/audit_nghiem_thu_lan_3_2026-10-09/` gồm manifest,source_snapshot6JSON,selected_questions,test_runs,math_proof,source_image_check,cache_proof,markdown_sync_check,markdown_semantic_compare,olp03_sync_final,course_expiry,verification_summary. So sánh bank03 dùng kết quả cuốiolp03_sync_final.

Báo cáo: `docs/VERIFY_NGHIEM_THU_LAN_3_2026-10-09.md`.
Prompt: `docs/PROMPT_GEMINI_CHOT_NGHIEM_THU_LAN_3_2026-10-09.md`.
