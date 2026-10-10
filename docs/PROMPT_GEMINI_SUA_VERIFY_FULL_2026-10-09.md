# PROMPT GEMINI — SỬA KẾT QUẢ VERIFY FULL 09/10/2026

Hãy đọc báo cáo `D:\Code\Code\AIO\Code\olp-ai-hcmus26\docs\VERIFY_FULL_NGUON_VOAI_2026-10-09.md` và evidence `D:\Code\Code\AIO\Code\olp-ai-hcmus26\tmp\audit_full_2026-10-09\` trước khi sửa. Mục tiêu là tài liệu ôn thi đúng, có thể làm bài độc lập, chấm và giải thích nhất quán trước ngày 11/10. Đừng mở rộng thêm nội dung trước khi xử lý hết lỗi dưới đây.

Hiện tại có 6 JSON, 448 bản ghi =428 MCQ+2 code+18 essay. Sáu ngân hàng đang đồng bộ ở HTML cuối, nhưng validate FAIL do olp-04 chưa được khai báo. Không dùng báo cáo 184 câu cũ làm căn cứ nghiệm thu.

## A. Sửa lỗi chấm và bảo toàn đề gốc trước

1. `src/data/exams/olp-01.json`, OLP01-C10: phương án A đúng; answer hiện B là sai. Đổi key A, kiểm tra explanation và UI. Không chọn key theo thống kê phân bố.
2. `olp-02.json`, VOAI02-M43: A=1/7 và D=4/28 tương đương; thay D bằng distractor khác và sửa lời giải bẫy. IoU đúng 400/2800=1/7.
3. Nhập lại `voai-2025.json` từ **C:\Users\HP\Downloads\OLPAI\Quizzes\voai2025_original.pdf**. Đây là đề gốc 100 câu/180 phút/mã 006. Không dùng Solution.pdf để thay prompt gốc. Solution chỉ dùng làm nguồn lời giải bên thứ ba, tác giả Nguyễn Khắc Trung Kiên.
4. Giữ chính xác toàn bộ câu hỏi, thứ tự A/B/C/D, biểu thức, bảng, hình và code. Hình/code dạng ảnh phải được cắt/trích hoặc gõ lại và đối chiếu bằng mắt; đừng chấp nhận extract_text làm mất dữ kiện. Nội dung hình phải tự chứa trong web nếu tiếp tục cam kết HTML độc lập, hoặc đóng gói assets đủ và kiểm tra live.
5. Bắt buộc sửa VOAI25-014,024,025,026,032,033,037,046,058,068,073,080 theo bảng báo cáo. Câu 24: original A=d(x,y), B=d(x,a); đúng là **B theo thứ tự PDF original**. JSON đang đảo A/B theo lời giải bên thứ ba; khi khôi phục gốc phải cập nhật key và ghi erratum, không chỉ đổi key mà bỏ qua options.
6. Q32 đầu vào 4×4, không phải 3×3; Q80 đủ 8 cặp, MSE=7.5. Q58 phục hồi confusion matrices, bỏ nhận xét làm lộ đáp án trong prompt. Q68 phục hồi bốn công thức TeX và loại NUL/SOH. Q37 có bảng sáu sinh viên, entropy khoảng 0.9183.
7. Đối chiếu cả 100 câu, kể cả distractors từng bị viết lại (84/93) và ngữ cảnh/công thức bị cắt. Không dùng fuzzy ratio thấp để tự kết luận key sai. Không đảo phương án đề chính thức để cân bằng đáp án.

## B. Đồng bộ lựa chọn–key–explanation–bẫy

8. Đề 05 có **66/90** explanation kết luận chữ cái cũ sau đảo options. Danh sách đầy đủ trong `olp05_source_compare.json` / `answer_explanation_conflicts.json`. Nội dung phương án đúng đang khớp L5/L9; cập nhật lời giải theo options hiện tại, không đổi key theo chữ cũ. Ví dụ NLP01=A (subwords), NLP15=C (quadratic attention), CV40=C (320 tham số).
9. Bỏ thuật toán đặt đáp án theo A,B,C,D lặp tuần tự: đề 05 cả 90 câu và đề 03 M51–M100 đang có chu kỳ. Với mock dùng seed xác định để đảo không có chu kỳ, giữ mapping để cập nhật toàn bộ kết luận và từng distractor trong lời giải, Markdown. Đề chính thức giữ nguyên nguồn.
10. Soát bẫy của tất cả ngân hàng: VOAI03-M04 hiện A=Kỳ vọng, D=Phương sai nhưng bẫy ghi ngược; VOAI02-M02 bẫy Var=E phải dẫn phương án có (8,8), hiện là A. Không chỉ kiểm tra heading đủ bốn khối.

## C. Sửa đề 04 vừa thêm

11. OLP04-Q08 sai kiến thức: BatchNorm2d lấy thống kê trên N,H,W mỗi kênh. N=1 không suy ra variance=0 khi H*W>1. Viết lại prompt/options/explanation, loại câu “chắc chắn” và key hiện không đúng. Nguồn: https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm2d.html
12. Q09 sửa KV cache O(1): full attention cho token mới vẫn O(T) theo context, fixed dimensions. Key B về bộ nhớ tuyến tính có thể giữ sau sửa tiền đề. Nguồn: https://huggingface.co/docs/transformers/cache_explanation
13. Q13 phân biệt hệ số nhân loss với gradient. Modulation 10^-4 không có nghĩa gradient đúng giảm 10.000 lần; phải đạo hàm cả hệ số. Với p=.99,gamma=2,alpha=1, tỷ lệ gradient focal/CE theo binary target logit ~.000299. Có thể sửa câu chỉ hỏi loss để ngắn và đúng.
14. Q17 dùng **LogSoftmax + NLLLoss**, không Softmax+NLLLoss; ghi rõ giả định để gradient=p-y. Nguồn: https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html
15. Q10=A, Q12=C đang đúng; Q12 giảm BLEU 63.2%. Đề 04 hiện B18/A1/C1/D0; cân bằng chỉ sau kiểm tra key và remap explanation đúng.
16. Bốn essay OLP04-ESSAY-01..04 đang thiếu modelAnswer/rubric/rubricPoints. Chuyển bài giải explanation vào trường phù hợp schema hệ thống, có rubric tổng 10 điểm mỗi bài. Trên live hiện bài mẫu và rubric trống; kiểm tra hiển thị sau sửa.
17. Đính chính “VOAI 2025 tác vụ 2” thành **OLP AI sinh viên 2025 SOLOAI** nếu dẫn PDF Hoa–Việt/ngôn ngữ ký hiệu. Giới hạn 20 phút có nguồn; các số <90 giây/97.1%/8k/9px/3px cần clip+timestamp+trích đoạn hoặc ghi giả định/UNVALIDATED. Không gọi 3D-CNN chắc chắn TLE hoặc vocab8k tối ưu phổ quát. Q19: 24 forward không đủ chứng minh vượt20phút nếu thiếu baseline. Q11 viết rõ 1/(2*sigma_1^2).

## D. Sửa tích hợp và nguồn tham chiếu

18. Tính mẫu số graded và essay bằng tổng points từng loại, không hardcode olp02 versus allothers. Kết quả phải là 01=100/40,02=90/60,03=100/40,04=60/40,05=90/0,VOAI25=100/0. Cập nhật header/footer và báo cáo submit; đề không có essay ẩn phần tự luận hoặc hiển thị0.
19. Update validator/spec olp04, essay contract và phân bố phù hợp; audit_quality và audit_katex quét động đủ **6 ngân hàng/448 câu**, phát hiện không có file bị bỏ qua. Bỏ thông báo “184” hardcode. Test phải phát hiện ít nhất C10 sai, hai options M43 tương đương, key–explanation lệch, chu kỳ đáp án mock, missing rubric/modelAnswer, missing input của câu nguồn. Test nội dung có dữ liệu nguồn thật, không chỉ test cùng implementation.
20. Remap § theo heading thật: §4.1=preprocess,4.2=word representations,4.3=cosine,4.5=Transformer,4.6=BERT/GPT,4.7=NLPmetrics. NLP15 không dẫn4.2 cho Attention; NLP30 không dẫn4.3 cho LLM. Nếu chưa có nội dung thì bổ sung đúng hoặc bỏ link; không đổi tên fake của heading đang tồn tại. Tương tự source VOAI25 và CV40.
21. Đề03 không phải bản nguyên vẹn De_TN_So_3: M04 hiện Entropy trong khi sourceQ4 Manhattan. Ghi tuyển tập/biên tập và tách phần Gemini mở rộng, hoặc nhập đúng100source. Source120phút, JSON90phút; ghi rõ luyện nhanh hoặc chỉnh thời lượng. Update moduleLabels/moduleOverview theo actual32/39/33 gồm4essayC.
22. Sửa metadata YouTube: web§1.9 kênh Bhavesh Bhatt,§2.4 StatQuest,§2.5 Siraj Raval,§2.8 namkuner. 24 hub/46 React IDs đều oEmbed200 trong audit nhưng 22/24 mapping khác nhau. Thống nhất mapping, kiểm tra timestamp/chủ đề đúng, đừng xem oEmbed200 là bằng chứng xem hết video.
23. 19 lesson dùng video URL signed đã quá hạn; dẫn lesson URL ổn định và cho người học đăng nhập/lấy link mới. Không đưa token vào báo cáo. Dữ liệu OLP chuẩn16,VOAIchuẩn13 là lọc sidebar/heading, không tự bịa thêm bài cho đủ rawcounts17/23.
24. Notebook nguồn có lỗi ở Image Captioning/ImageCaptioning.ipynb cellindex8: ký tự c riêng ở dòng54 gây unexpectedindent dòng55. Nếu cần bản chạy, tạo bản sửa trong dự án và giữ nguyên nguồn tải về; không chạy training hoặc thay seeds/hyperparameters lặng lẽ. Audit hiện chưa chứng minh notebook chạy end-to-end.

## E. Điều kiện bàn giao

- Không xóa câu, rút bớt đề hoặc làm mất lời giải để qua check; không mở rộng thêm trước khi sửa lỗi.
- Giữ đúng nguồn: officialVOAI2025, lời giải bên thứ ba, đề luyện2026, lessonSkillPixel, Gemini mở rộng. Không tuyên bố có đề chính thức2026/2024 khi không có tài liệu gốc.
- Tăng data/cache version của các đề bị đổi key/options và migrate có phạm vi; tránh lưu verdict cũ sai sau remap.
- Đồng bộ JSON–Markdown–public–dist–live temp; không chỉ sửa tệp nguồn rồi nghiệm thu HTML cũ.
- Chạy validate, quality, fullKaTeX, HTMLlogic,18Vitest,tsc; browser thực các câu25/32/37/68/73/80,05NLP01/15/CV40 và04essay01; kiểm tra điểm đủ90đề05/60gradedđề04 và essay0củaVOAI25.
- Báo cáo từng lỗi: trước/sau, ID, nguồn/trang/timestamp, key trước/sau, test thực chạy/exit, giới hạn còn chưa xác nhận. Ghi count và hash bản HTML cuối. Không viết “khắc phục triệt để/PASS100%” khi chưa có kiểm tra đủ.

Trước khi bắt đầu hãy lập checklist theo thứ tự A→B→C→D; tự thực hiện đến khi xong rồi báo cáo. Mục tiêu ưu tiên là bản ôn gọn, đúng và đáng tin trước ngày11/10, không phải tăng số lượng nội dung.
