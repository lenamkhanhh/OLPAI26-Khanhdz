# PROMPT SỬA BẢN 600 CÂU SAU KIỂM ĐỊNH ĐỘC LẬP

Làm tại D:\Code\Code\AIO\Code\olp-ai-hcmus26. Đọc trước docs/VERIFY_NANG_CAP_600_CAU_2026-10-10.md và bằng chứng tmp/audit_600_2026-10-09/. Bản 600 câu đủ số lượng và 10 suite đều pass, nhưng chưa đạt nội dung. Mục tiêu là sửa lỗi và khóa bản ôn thi; không mở rộng tiếp hoặc viết lại hàng loạt chỉ để đẹp thống kê.

## 1. Sửa P0: 27 câu Đề04 lệch bộ lựa chọn

Các ID:
OLP04-Q22, Q23, Q30, Q51, Q52, Q53, Q54, Q55, Q56, Q57, Q59, Q60, Q61, Q62, Q76, Q77, Q78, Q79, Q80, Q81, Q82, Q83, Q84, Q85, Q86, Q87, Q88.
Tất cả tiền tố là OLP04-.

Đọc bảng trong audit để biết chủ đề/đáp án đúng cần diễn đạt. Hiện Q22 ArcFace nhưng options về bitrate; Q51 ViT nhưng options về giải mã văn bản; Q60 GCN nhưng options về các thành phần RAG; Q76 HNSW không có phương án graph. Không đổi một chữ cái để chữa: phải viết lại đủ 4 phương án phù hợp đề bài, đúng duy nhất một phương án, giải thích vì sao từng distractor sai. Đối chiếu nguồn sơ cấp khi có khái niệm/paper cụ thể.

Quét toàn bộ 100 câu Đề04 để tìm lỗi cùng dạng; 27 là danh sách đã chứng minh, không phải giới hạn phạm vi sửa. Không tái sử dụng options theo vị trí array của câu khác. Trước/sau phải có bảng ID + lỗi + khóa/text đúng + nguồn đối chiếu.

## 2. Sửa các lỗi kiến thức và code cụ thể

- OLP01-C10: khóa hiện B sai; sửa về A. Lời giải và A đã nói Ridge. Diễn đạt Lasso “có xu hướng chọn một vài biến tương quan”, không định luật chọn ngẫu nhiên luôn đúng một biến. Nhắc lambda>0 để X^T X+lambda I xác định dương.
- OLP01-M65: đổi câu hỏi từ điều kiện “cần và đủ” sang “đủ”; sửa giải thích. Phản ví dụ f(w)=w^4 có minimum duy nhất nhưng Hessian tại0 bằng0.
- VOAI25-079: B phải là model.to('cuda'), không phải model.to(' cuda '). Không sửa string literal hoặc code bằng quy tắc khoảng trắng văn xuôi. Quét code toàn bộ ngân hàng sau mọi bước OCR.
- VOAI02-M80: bỏ “FPR luôn nhỏ / ROC-AUC cao giả tạo”. TN lớn không tự suy ra AUC; giải thích FPR nhỏ vẫn có thể có nhiều FP so với TP và precision thấp. Bỏ số AUC0.98 nếu không có đủ dữ liệu tính.
- VOAI02-M92: một lớp có effective kernel 1+(K−1)d, tuyến tính theo d. Bỏ “theo cấp số” nếu không nêu lịch dilation nhiều tầng.
- OLP04-Q92: quadratic form là bình phương Mahalanobis distance; ghi d_M^2 hoặc squared-distance score. Các phương pháp OOD khác không phải sai nói chung, chỉ không đúng cơ chế đề hỏi.
- Sửa reference sai: §1.1 thực tế là k-NN, không phải Gradient Descent/KKT. Không dẫn một section chỉ vì ID tồn tại.

## 3. Giữ bản VOAI 2025 nguyên bản

Bản đang gắn nhãn chính thức có 29 câu sửa options, 10 câu sửa prompt, 8 câu thay cả text correct option (006,021,024,029,042,057,079,088). Report “chỉ sửa 3 distractor và bảo toàn correct text100%” sai.

Khôi phục ngân hàng nguyên bản bằng đối chiếu C:\Users\HP\Downloads\OLPAI\Quizzes\voai2025_original.pdf; giữ thứ tự A–D và semantics gốc. Được sửa OCR/khôi phục công thức chính xác, phải lưu bảng khác biệt để review. Đừng khôi phục mù từ snapshot có OCR lỗi ở một vài công thức.

Nếu giữ bộ distractor nâng cấp thì đặt tên “VOAI 2025 chỉnh biên”; phân biệt rõ với original, không dùng nó để tuyên bố nguyên bản100%. Không gọi lời giải tác giả Nguyễn Khắc Trung Kiên là khóa BTC chính thức nếu chưa có nguồn xác nhận.

## 4. Sửa chống đoán, ưu tiên nội dung đúng

Đề04 Q21–60 lặp ABCD; Q61–70 toànA;71–80 toànB;81–90 toànC;91–100 toànD. Tổng25mỗi chữ không đủ. Đảo lựa chọn có seed cố định trên các đề luyện, cập nhật answer và mọi chữ cái trong explanation; không đảo bộ original.

Heuristic chọn option dài nhất (tie A→D) hiện đúng296/600=49,33%. Ba cue=0 không có nghĩa “triệt tiêu hoàn toàn”.
- Thêm thống kê longest-option và run/periodic pattern; định nghĩa rõ tiêu chí ±15%.
- Viết distractor hợp lý, cùng mức chi tiết; không nhồi câu thừa để tăng độ dài.
- Không đổi khóa khoa học để qua scanner.
- scratch/inspect_all_giveaways.py hiện chỉ print, exit0 kể cả có lỗi. Tạo fail gate cho tiêu chí thật sự bắt buộc; fixture có cue phải fail. Với original giữ nguyên lựa chọn dù có cue hình thức, phân biệt tiêu chí đề luyện/đề gốc.

## 5. Sửa cache và đồng bộ

Version vẫn01=2,02=2,03=3,04=2,05=2,VOAI=2 dù nâng cấp. Cache AC/WA cũ có thể khác chọn lại cùng option. Bump version hoặc fingerprint dữ liệu chấm, invalid/regrade cache từ:
- bản448 đã chốt;
- bản600 lỗi, đặc biệt C10 với B từng bị chấmAC;
- các câu đổi thứ tự lựa chọn.

Test phải chứng minh verdict/score sau load phù hợp dữ liệu đã sửa, và dữ liệu của đề không đổi vẫn được bảo toàn khi hợp lý.

Đồng bộ6JSON →6Markdowncanonical →public/dist/serverlive. Cập nhật header5Markdown còn ghi số câu/essay/điểm cũ. Kiểm full prompt/options/key/explanation từng block, không chỉ nhãn A–D. Giữ ảnh Q26 Base64 và không spoiler.

## 6. Nghiệm thu có bằng chứng

Chạy lại10suite, bổ sung kiểm:
1. C10 A đượcAC, B bịWA, explanation chọnA.
2. Q22/Q51/Q60/Q76 options khớp chủ đề, có đúng1 lựa chọn đúng.
3. M65 không còn claim cần-và-đủ PD; counterexample x^4 được giải thích.
4. CUDA literal không có space; nếu môi trường có torch, kiểm torch.device mà không cần GPU.
5. Migration cache phiên bản đã phát hành, không chỉv1→v2.
6. Báo cáo thống kê longest-option và pattern thật.
7. Đối chiếu bộ original với PDF, lập diff.
8. Full-content sync600 + header mới + HTML hashes đồng nhất.

Viết báo cáo sửa mới: ID thay đổi, nguồn, trước/sau, test đã chạy, SHA của JSON/HTML và những giới hạn chưa verify. Không tuyên bố “100% khoa học/hoàn hảo/production-ready” chỉ vì exit0. Đừng sửa các file VERIFY của GPT hay xóa snapshot audit để khiến bằng chứng cũ mất đi.

