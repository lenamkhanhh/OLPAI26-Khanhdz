# PROMPT GEMINI — SỬA NỐT SAU VERIFY LẦN 2, 09/10/2026

Đọc `D:\Code\Code\AIO\Code\olp-ai-hcmus26\docs\VERIFY_NGHIEM_THU_LAN_2_2026-10-09.md` trước khi sửa. Audit mới xác nhận nhiều lỗi đã sửa, nhưng chưa đạt 100%. Chỉ sửa các vấn đề đã chứng minh; không mở rộng thêm ngân hàng, không xáo trộn đề gốc, không thay câu bằng câu dễ hơn.

## 1. Đồng bộ Markdown thực sự

`content/04-de-bo-sung-insight-video-voai.md` vẫn giữ lỗi cũ ở Câu8 BN variance luôn0, Câu9 KVCache O(1), Câu13 gradient giảm chính xác10^-4, Câu17 Softmax+NLLLoss. 15/20 key khác JSON vì thứ tự options cũ.

`content/04-de-chinh-thuc-voai-2025-ma-006.md` vẫn Q24 keyA/thứ tự đảo, Q32 thiếu matrix, Q37 thiếu bảng, Q58 lộ đáp án/thiếu ma trận, Q68 OCR hỏng/NUL/SOH, Q80 thiếu8cặp.

Sau khi sửa JSON khoa học ở bước2, xuất lại các Markdown liên quan từ dữ liệu đã xác minh. Đối chiếu cả prompt/options/answer, không chỉ key. Giữ bảng, code, ảnh, công thức. Kiểm tra toàn bộ bộ đề Markdown được ghi “đồng bộ”; không khẳng định đã đồng bộ nếu chỉ build HTML.

## 2. Sửa kiến thức và render Q08/Q13 đề04

Q08: N=1, H*W>1 KHÔNG đảm bảo variance>0; feature map2x2 toàn5 có variance0. Viết “N=1 không tự động khiến phương sai0; statistics lấy N,H,W; batch nhỏ có thể kém ổn định; epsilon bảo vệ mẫu số”. Bỏ khẳng định luôn sụp đổ/luôn thayGN khiN<=2. KeyA hiện tại có thể giữ nếu sửa diễn đạt tránh kết luận tuyệt đối.

Q08 còn double-escape. Sau JSON.parse, TeX phải có `\mu`, `\sigma`, `\times` (một backslash); biểu diễn tương ứng trong fileJSON là `\\mu` chứ không `\\\\mu`. Sửa câu và renderer: trên web lời giải đang lộ `%%%MATH_DISP_0%%% %%%MATH_DISP_1%%%`, không có hai display formulas. Cần browser check actualDOM không còn placeholder, không còn chữ “sigma/times” thay ký hiệu. KaTeX parse không báo lỗi vẫn có thể render sai.

Q13: giữ câu hỏi LOSS, keyD. Nêu alpha=1 hoặc so với alpha-weightedCE. Công thức gradient hiện sai dấu số hạng2. Với p=sigmoid(z) là xác suất lớp đích và z hướng về lớp đích:
`dFL/dz = alpha*(1-p)^gamma*((p-1)+gamma*p*ln(p))`.
Nếu dùng logit positive cho background y=0, ghi rõ đổi biến/sign. p=.99,gamma2,alpha1 cho -2.989966499e-6, CEgrad=-.01, ratio=.00029899665; finiteDifference h1e-5 khớp. Công thức cũ cho +9.899664990e-7 trái dấu. Thêm test numerical differentiation có tolerance hợp lý, không test công thức sai bằng chính nó.

## 3. Sửa cache sau thay đổi key/options

CURRENT_EXAM_VERSIONS vẫn 01=1,04=1,05=1,official=1 dù dữ liệu đổi. Cache01C10 chọnB/AC, official024 chọnA/AC,05CV40 chọnD/AC vẫn hiệnAC/cộngđiểm trong bản mới.

Bump version bank thay đổi hoặc mapping/migration đúng nội dung và regrade. Shuffle options thì không được tự tái dùng selected letter cũ như cùng ý nghĩa. Chỉ reset bank liên quan, có thông báo; không clear toàn bộ localStorage. Cập nhật test_html_logic.mjs đang ép giữ nguyên cache01. Test bank04 và05/official; xác nhận stale verdict không còn sau load.

## 4. Phục hồi ảnh gốc VOAI25-026

PDF `C:\Users\HP\Downloads\OLPAI\Quizzes\voai2025_original.pdf` có hình feature map. Web hiện0img, thêm mô tả “vệt ngang/dọc đan xen…” lộ đáp án. Trích đúng ảnh, tích hợp schema/renderer/build và Markdown; bỏ lời mô tả đáp án khỏi statement. Không đổi thứ tựA/B/C/D, giữkey theo nguồn đã xác minh. Nếu chưa thể tích hợp, ghi rõ bản chuyển thể/không nguyên gốc100% và link/trangPDF.

## 5. Viết lại báo cáo nghiệm thu từ file thật

Các mô tả đang sai: C10 không phảiBN màRidge;M43D2/7 không4/21;Q24C/D khôngd(y,b)/d(a,b);Q32Average3x3 khôngMax2x2;Q37CGPA/Ôntập khôngThu nhập/Giới tính;NLP01FastTextngrams khôngBPE;CV40in_channels1,keyB,320params khôngRGB/keyC;03M04Entropy;02M02Binomial. OLP03 là tuyển tập+Gemini theo disclaimer, không gọi đầyđủ100câunguyêngốcĐề3thầyLuật.2code là tự đối chiếu/chọnđiểm, không engine chạy testcase. HTMLnạpKaTeXexternal+CDNfallback, khôngengineinlineđộc lập mộtfile. Module tựluận04 thực tếC.

Đề04 không có timestamp/transcript kiểm chứng số38h/84→97.1%/41→8lỗi và lời“giảng viênđã chỉra”. Cung cấp bằng chứng định danh video+timestamp/transcript hoặc đổi thành ví dụgiảđịnh/UNVALIDATED; không tự dựngtimestamp. Sửapath thưmục thành`VOAI NÂNG CAO`.19URLcourse chữký hết hạn: cậpnhật từ nguồn được phép nếu có; nếu không ghi hạn chế, khôngPASSlinkchỉvì tồn tại chuỗiURL. Ref NLP01đếnwordrepresentation§4.2, khôngtiềnxửlý§4.1.

## 6. Test và bàn giao

Chạy lại validate,audit_quality,test_quality_all,audit_katex_syntax,test_html_logic,check_section_refs,18Vitest,tsc --noEmit. Sửa haiPythonchecktest_quality_all/check_section_refs đểexitnonzero khi lỗi. Thêm kiểm tra nội dung/Markdownsynchronization,placeholder/doubleescape,cache vànumericalgradient trên trường hợp đã chứng minh; tránh tạo nhiều test chỉ phản chiếuimplementation.

Rebuildpublic/dist;đồngbộliveTemp đúngcheckout. Ghi hash,size,tổng448=428MCQ+2code+18essay. BrowsercheckQ08côngthức/Q26ảnh/rubric04/ticker6đề/cache. Lưu logthật,ghi test nào chạy/test nào chưa; khôngghiPASS100%kiếnthức chỉ vìschema vàparserpass. Khôngthay báo cáo auditGPT bằng tự nghiệmthu. Bàn giao báo cáo mới nêu cácID sửa và giới hạn còn lại.
