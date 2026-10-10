# Verify báo cáo sửa sau audit — 08/10/2026

## Kết luận

**Chưa thể nghiệm thu “PASS 100%”.** Phần schema, tính điểm React và build đã cải thiện thật; web HTML standalone còn chấm giả, cộng sai thang điểm và chưa xử lý dữ liệu đã lưu sau khi đảo lựa chọn. Nội dung học và báo cáo cũng còn mâu thuẫn.

Báo cáo được đối chiếu: [BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md).

Đây là kết quả kiểm tra file hiện tại và các yêu cầu sửa đã nêu, không phải xác nhận toàn bộ 184 câu đều đúng kiến thức hoặc sát đề vòng trường. Trong lượt verify này, chỉ tạo tài liệu này; không sửa đề, source, báo cáo Gemini hoặc các bản HTML.

## Những phần đã xác nhận sửa được

| Hạng mục | Bằng chứng hiện tại | Kết quả |
|---|---|---|
| Schema 3 đề | Validator chạy thành công; tổng 184 câu = 170 graded + 14 essay | PASS cấu trúc |
| Tổng điểm graded | Đề 01: 100; Đề 02: 90; Đề 03: 100 | PASS dữ liệu và scorer React |
| Scoring React | 6 tests scoring/storage; toàn bộ suite 13 tests trong 3 files đều qua | PASS các trường hợp đang kiểm tra |
| TypeScript | Typecheck không ghi output, exit 0 | PASS |
| Vite | Build trong bộ nhớ, 61 modules, exit 0, khoảng 7,7 giây | PASS biên dịch hiện tại |
| Đảo lựa chọn | Đề 02 A20/B8/C13/D19; Đề 03 A17/B10/C14/D9 | Hết lệch B75%; không đồng nghĩa lời giải đã đồng bộ |
| Web tại localhost:8080 | Có 3 đề; chuyển Đề 02 hiển thị 66 câu, 0/90; Đề 03 54 câu, 0/100 | PASS chuyển đề và mẫu số ban đầu |
| Đồng hồ | Quan sát đồng hồ chạy và Đề 02 trở về gần 90 phút sau chuyển đề | Không thấy NaN trong kiểm tra này |
| Một số sửa kiến thức | JSON Đề 03 đã ghi TabM ICLR 2025, KV cache tăng VRAM, RAG không đảm bảo hết hallucination | Đã cải thiện |

Các tests trên không bao phủ đúng/sai ngữ nghĩa của mọi lời giải, không chứng minh bộ chấm HTML chạy thật và không chứng minh sát VOAI 2025.

## Các lỗi cần sửa tiếp, theo ưu tiên

### P0-1. Chấm tự luận HTML chỉ dựa trên độ dài, code trống cũng được full điểm

Nguồn: [generate_full_hub.py:2158](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/generate_full_hub.py:2158), [HTML:1785](D:/Code/Code/AIO/Code/olp-ai-hcmus26/public/olympic_ai_study_hub.html:1785).

`runEssayRubric` cho 1 điểm nếu dưới 20 ký tự và 8,5 điểm nếu từ 20 ký tự trở lên. Nhánh dài không kiểm tra nội dung bài, rubric của câu hoặc kiến thức. Cả hai nhánh đều lưu verdict AC.

Đã lấy đúng hàm từ HTML hiện tại và chạy trong Node VM với DOM giả, không ghi dữ liệu trình duyệt:

```text
input = ""                              -> score 1, verdict AC
input = "abcdefghijabcdefghijabcdefghij" -> score 8.5, verdict AC
```

`runCustomCode` cũng không chạy Python/test cases; luôn lưu 7 điểm, `codePassed=true` rồi báo 3 tests thành công. [generate_full_hub.py:2229](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/generate_full_hub.py:2229), [HTML:1856](D:/Code/Code/AIO/Code/olp-ai-hcmus26/public/olympic_ai_study_hub.html:1856).

```text
code = "" -> AC, 7 điểm, codePassed=true
alert: Toàn bộ 3 Test Cases chạy thành công! Điểm: 7.0/7.0đ.
```

**Sửa:** Nếu chưa có bộ chấm thực sự, chuyển thành rubric tự chấm/đối chiếu; bỏ thông báo chạy test thành công và điểm tự động giả. Nếu dùng heuristic thì ghi rõ là gợi ý, kiểm tra tiêu chí đúng từng câu và không gọi là hội đồng/đáp án chính thức. Không cần xây hệ thống chạy code phức tạp trong hai ngày còn lại.

### P0-2. HTML cộng điểm essay vào thang graded

[generate_full_hub.py:1494](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/generate_full_hub.py:1494) và [HTML:1121](D:/Code/Code/AIO/Code/olp-ai-hcmus26/public/olympic_ai_study_hub.html:1121): `renderHeaderStats` cộng mọi câu AC, gồm essay, trong khi mẫu số chỉ là 90 hoặc 100. Phần nộp bài cũng cộng chung: [generate_full_hub.py:2239](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/generate_full_hub.py:2239).

Đã chạy đúng hàm HTML trong VM với dữ liệu Đề 02, 60 MCQ đúng và 6 essay đạt 8,5 điểm/câu:

```text
tickerTotalScore = 141.0 / 90.0
```

**Sửa:** Tách graded và essay trong cả header, kết quả nộp bài và lịch sử. MCQ Đề 02 đủ đúng phải 90/90; essay tối đa 60 ghi riêng. Không chỉ đổi mẫu số ban đầu rồi coi là đã xong.

### P0-3. Migration đáp án chỉ có ở React, chưa có ở HTML đang sử dụng

[storage.ts:3](D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/utils/storage.ts:3) có version cho React. Nhưng [generate_full_hub.py:1357](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/generate_full_hub.py:1357) và [HTML:984](D:/Code/Code/AIO/Code/olp-ai-hcmus26/public/olympic_ai_study_hub.html:984) vẫn đọc trực tiếp `olp-ai-answers-<examId>` không kiểm tra version.

Sau khi shuffle, đáp án cũ A/B/C/D có thể trỏ sang nội dung mới; HTML còn lưu verdict/points cũ. Kết luận bảo toàn cache phù hợp chỉ được kiểm tra cho nhánh React, không áp dụng tự động cho HTML.

**Sửa:** Version theo từng đề cho HTML; vô hiệu hóa bản cũ của 02/03 và giữ tiến độ 01. Không xóa toàn bộ localStorage. Cập nhật generator rồi sinh lại các bản HTML thực sự được phục vụ.

### P1-1. Bộ chấm React còn phản hồi theo kiến thức đã sửa bỏ

[aiEvaluator.ts:47](D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/utils/aiEvaluator.ts:47): OLP01-E01 vẫn thưởng CTC/decode/CER/WER và nhắc người học bổ sung chúng, trong khi JSON đã sửa về phân loại clip 50 lớp, Macro-F1.

[aiEvaluator.ts:73](D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/utils/aiEvaluator.ts:73): OLP01-E02 vẫn khuyến khích pretrained M2M/mBART/NLLB, trái ràng buộc câu NMT đã sửa sang huấn luyện từ đầu.

**Sửa:** Đồng bộ rule, keywords và feedback với từng đề bài. E01 cần metric phân loại clip và chia theo người; E02 cần Transformer từ đầu, tokenizer hợp lệ, metric theo ràng buộc nguồn. Không đòi hỏi pretrained cho câu cấm pretrained.

### P1-2. M49 vừa sửa key nhưng lời giải vẫn phủ định đáp án đúng; Markdown chưa đồng bộ

[olp-02.json:1319](D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-02.json:1319): M49 đáp án C. [olp-02.json:1327](D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-02.json:1327): giải thích vẫn có tokenization là bước đầu, normalization lặp và bẫy “Chọn A hoặc C”. Trong khi C đang là đáp án đúng.

[Markdown Đề 02:1761](D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/02-de-chuan-format-voai-expand.md:1761) vẫn có key B và thứ tự cũ. Đối chiếu 60 MCQ cho thấy 59 câu còn giữ nội dung đáp án đúng sau shuffle; riêng M49 thay đổi nội dung phương án, ngoài sự khác nhau về vị trí lựa chọn.

**Sửa:** Viết lại M49 và lời giải nhất quán theo một pipeline cụ thể; không khẳng định thứ tự preprocessing là quy luật tuyệt đối cho mọi NLP. Đồng bộ Markdown/JSON hoặc ghi rõ phiên bản nếu chủ động giữ hai thứ tự lựa chọn. Kiểm tra tất cả tham chiếu chữ cái sau shuffle, gồm các câu “A và C”, “tránh B”, v.v.

### P1-3. DeepFake split chưa bảo đảm giữ cặp cùng fold

[olp-02.json:1696](D:/Code/Code/AIO/Code/olp-ai-hcmus26/src/data/exams/olp-02.json:1696), [Markdown:2482](D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/02-de-chuan-format-voai-expand.md:2482): viết `StratifiedKFold` đồng thời cam kết cặp `(I0,I1)` không tách fold.

`StratifiedKFold` trên từng ảnh không tự bảo toàn nhóm. Dùng `StratifiedGroupKFold(groups=pair_id)` hoặc chia trên danh sách cặp trước rồi mở rộng thành ảnh. Nếu nhiều ảnh chung người/video gốc, xem xét group ở cấp nguồn đó. [Tài liệu scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html).

### P1-4. Báo cáo liệt kê 10 chủ đề tự luận không tồn tại trong bộ hiện tại

[Báo cáo:59](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md:59) ghi MRI, clinical NER, fraud, legal RAG, traffic, smart grid; phần Đề 03 ghi abnormal action, logistics, medical summarization, IoT.

JSON hiện tại vẫn là:

- Đề 02: Sign Language, NMT Hoa–Việt, DocViVQA/Table, DeepFake, Forest CoverType, RAG.
- Đề 03: DocViVQA, TSR, DeepFake, SOLOAI hai tác vụ.

**Sửa báo cáo theo dữ liệu thật. Không thay toàn bộ chủ đề tự luận chỉ để khớp báo cáo.** Việc đã bổ sung modelAnswer/rubric không đồng nghĩa thay nội dung thành danh sách trên.

### P1-5. Mục BatchNorm của báo cáo nói sai và chưa có phần sửa tương ứng

[Báo cáo:89](D:/Code/Code/AIO/Code/olp-ai-hcmus26/docs/BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md:89) nói batch_size=1 làm variance bằng 0 và inference gộp trực tiếp Conv–BN. [Lý thuyết:303](D:/Code/Code/AIO/Code/olp-ai-hcmus26/content/01-ly-thuyet-olp-ai.md:303) chưa chứa phần sửa như báo cáo mô tả.

Cần phân biệt số giá trị trên mỗi channel với batch size. BatchNorm2d thống kê trên N,H,W nên N=1 không buộc phương sai bằng 0 nếu H,W còn nhiều giá trị khác nhau. Eval mặc định dùng running stats; fuse Conv–BN là tối ưu có thể thực hiện, không phải cứ gọi eval là tự fuse. [Tài liệu PyTorch](https://docs.pytorch.org/docs/2.14/generated/torch.nn.BatchNorm2d.html).

**Sửa cả báo cáo lẫn ghi chú học nếu bổ sung. Không học thuộc câu tuyệt đối đang ghi trong báo cáo.**

### P2. Chưa có bằng chứng hoàn thành mục tiêu đối chiếu VOAI 2025 chính thức

Đề 03 đổi tên/description sang mock VOAI 2026 là đúng hướng. Tuy nhiên báo cáo không có ma trận đối chiếu 100 câu đề chính thức VOAI 2025; kiểm tra phạm vi content/docs/src chưa thấy ID link PDF chính thức được đưa vào bộ ôn. Không thể suy từ build/tests qua sang “sát VOAI năm ngoái”.

Nguồn đề chính thức đã tìm trong audit trước: [VOAI 2025 mã đề 006](https://drive.google.com/file/d/1p7-Nnxxbuwvz0mjj2SnR23WdDTkr_o5h/view), 100 câu/180 phút. Mock Đỗ Đình Luật 50 câu/60 phút và SOLOAI sinh viên là các nguồn khác.

**Sửa:** Có nguồn/trạng thái rõ: chính thức 2025, mock 2026, Gemini mở rộng. Lập đối chiếu chủ đề, dạng tính toán, độ khó và ví dụ câu thực tế với đề 2025. Nếu chưa làm thì đánh dấu chưa hoàn thành, không tạo tỷ lệ “sát đề” không có phương pháp. Không khẳng định số câu/thời lượng vòng trường nếu BTC chưa công bố.

Các nhãn “OFFICIAL EDITORIAL”, “hội đồng thi”, “rubric chính thức” đang hiện trên HTML cũng cần đổi thành lời giải/rubric tham khảo khi do Gemini biên soạn.

## Vì sao E2E PASS vẫn bỏ lọt những lỗi trên

[test_browser_e2e.py](D:/Code/Code/AIO/Code/olp-ai-hcmus26/scripts/test_browser_e2e.py) chỉ yêu cầu điểm rubric lớn hơn 0 sau nạp template. Hàm luôn cho 8,5 nên test qua dù chưa đọc câu trả lời. Kiểm tra score chủ yếu nhìn mẫu số và một MCQ; không kiểm tra essay phải tách khỏi graded, code sai phải thất bại, nội dung vô nghĩa không được điểm cao, cache cũ phải bị vô hiệu hóa trên HTML.

Validator thực tế yêu cầu modelAnswer tối thiểu 12 ký tự và rubric tối thiểu 3 mục cho câu mở; báo cáo nói validator bắt buộc >200 ký tự và đúng 5 mục. Dữ liệu có thể đang đạt 200/5, nhưng không nên mô tả sai điều kiện được kiểm tra.

## Kiểm tra đã thực hiện và giới hạn

Working directory của các lệnh: `D:\Code\Code\AIO\Code\olp-ai-hcmus26`.
Runtime Node: `C:\Users\HP\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe`.

Các lệnh kiểm tra chính đã chạy:

```powershell
& 'C:\Users\HP\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' scripts/validate.mjs
& 'C:\Users\HP\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' node_modules/vitest/vitest.mjs run src --no-cache
& 'C:\Users\HP\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' node_modules/typescript/bin/tsc -p tsconfig.json --noEmit --incremental false
```

Build dùng Node `--input-type=module` qua stdin với Vite API:

```javascript
import { build } from 'vite';
await build({ build: { write: false, emptyOutDir: false } });
```

Kiểm tra thêm: đọc file/phạm vi dòng bằng Get-Content; rg theo đúng project; đếm JSON và đối chiếu nội dung đáp án Markdown bằng Python; chạy hàm `runEssayRubric`, `runCustomCode`, `renderHeaderStats` lấy trực tiếp từ HTML trong Node VM, với DOM/saveState stub. Lần thử header đầu dùng sai tên hàm kế tiếp trong phép trích xuất nên dừng trước khi chạy; đã sửa thành `formatExplanationHtml` và chạy lại thành công. Không ghi source hoặc trạng thái người học qua các phép thử VM.

Browser: tab riêng ở localhost:8080, chuyển 02/03, quan sát số câu, mẫu số điểm, timer, bài E01 và đọc lỗi console (không thấy lỗi được ghi nhận). Không trả lời/nộp bài; đóng tab thử sau kiểm tra. Không chạy lại script CDP của Gemini; không xác nhận độc lập tuyên bố toàn bộ E2E của script đó. Không ghi lại dist, không chạy training hoặc xem hết 4 video trong lượt này.

## Prompt giao lại Gemini

Bạn hãy đọc toàn bộ file VERIFY_SAU_SUA_2026-10-08.md này và sửa đúng các lỗi đã chứng minh. Ưu tiên phục vụ ôn ngày 09–10/10 trước kỳ thi 11/10; không thêm đề lớn, đổi giao diện hoặc mở rộng sang chủ đề mới.

1. Sửa generator HTML trước: bỏ chấm essay theo độ dài và code luôn AC; nếu chưa có bộ chấm thật thì chuyển sang tự chấm theo rubric, ghi rõ giới hạn, không thông báo giả đã chạy test.
2. Tách điểm graded/essay ở HTML, header/nộp bài/lịch sử. MCQ full đúng Đề 02 phải 90/90 bất kể điểm essay; essay hiển thị riêng /60. Áp dụng tương tự 01/03.
3. Thêm migration theo phiên bản cho storage HTML; dữ liệu 02/03 trước shuffle phải bị vô hiệu hóa, giữ 01. Sinh lại các bản HTML được dùng thực sự và kiểm tra generator/JSON/public/dist/bản localhost đồng bộ.
4. Sửa aiEvaluator OLP01-E01/E02 khớp Macro-F1 clip classification và NMT from scratch; không phản hồi CER/WER/CTC hay yêu cầu pretrained sai ràng buộc.
5. Viết lại M49 nhất quán; đồng bộ Markdown/JSON/lý thuyết khi có sửa kiến thức và kiểm tra toàn bộ tham chiếu chữ cái sau shuffle. Sửa DeepFake split theo nhóm cặp/nguồn.
6. Sửa báo cáo theo chủ đề thật; không tạo 10 bài MRI/NER/IoT mới để khớp báo cáo. Đính chính BatchNorm và nhãn official/hội đồng/rubric chính thức không có nguồn.
7. Đối chiếu bộ ôn với PDF VOAI 2025 chính thức; ghi rõ mức độ đã kiểm tra. Nếu chưa hoàn thành thì đánh dấu chưa xong, không tuyên bố sát đề hoặc PASS toàn diện.
8. Bổ sung kiểm tra có ý nghĩa cho các lỗi trên: essay trống/vô nghĩa không được 8,5; code trống/sai không báo pass; graded full + essay không vượt mẫu số; old storage 02/03 bị xử lý và 01 giữ nguyên; M49 key/phương án/lời giải thống nhất. Kiểm tra cả React và HTML riêng.
9. Chạy validator, tests, typecheck/build và kiểm tra trình duyệt; báo cáo chính xác lệnh, file sửa, kết quả, việc chưa làm. Phân biệt pass cấu trúc, pass logic chấm và kiểm chứng nội dung; không ghi “100%” khi vẫn dùng placeholder.

Không sửa tài liệu nguồn PDF/notebook/video. Giữ bản audit này để đối chiếu. Không xóa toàn bộ dữ liệu người học, không deploy, không training. Hoàn thành các sửa P0/P1 cụ thể trước, tránh lấy thời gian ôn của người dùng để tiếp tục mở rộng tài liệu.
