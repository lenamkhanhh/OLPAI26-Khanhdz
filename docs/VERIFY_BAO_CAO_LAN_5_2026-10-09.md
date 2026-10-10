# Kiểm tra báo cáo Gemini lần 5 — 09/10/2026

**Kết luận:** các lỗi liên hệ rõ ràng và định nghĩa p-value của lần trước đã được sửa trong JSON/web. Bảng nghiệm thu đã khớp ID đích và heading giáo trình thực tế. Còn lỗi đồng bộ Markdown cần sửa; không nên công nhận tuyên bố “đã đồng bộ 100%” hiện tại.

Bản báo cáo được đọc ghi cập nhật lần 5 lúc **10:45 ngày 09/10/2026**. Chỉ kiểm tra, không sửa source hay sản phẩm học tập.

## Đã xác nhận

- M05 → VOAI03-M02 (Hessian); M13 → OLP01-C01 (k-NN); M49 → OLP01-C28 (NLP pipeline); M51 → OLP01-B09 (cosine); M59 → VOAI03-M23 (RAG). Các lỗi trỏ Poisson/Conv2D/YOLO/Silhouette đã được sửa trong JSON.
- M60 hiện hỏi KV Cache và liên hệ VOAI03-M30 cũng hỏi KV Cache; liên hệ này phù hợp câu hỏi hiện tại.
- M03 đã thay định nghĩa p-value trong JSON bằng xác suất thống kê kiểm định cực đoan bằng hoặc hơn quan sát dưới H0; đáp án D được giữ.
- Bảng báo cáo có 60 dòng; đối chiếu các ID liên hệ trong từng dòng với khối 4 của JSON: không có chênh lệch. Các số/tên § trích dẫn trong JSON khớp heading giáo trình.
- Prompt, 4 options và answer của 60 MCQ trong Markdown khớp JSON. **Lời giải chưa khớp**, xem mục dưới.
- Hai HTML public/dist bằng nhau, chứa Đề 02 đúng JSON mới. SHA-256: `bb4b174b9992ae6848fbd69db2b413e9b8918455ef4490512e0ea512f05bb4f7`.
- Ba PDF docs/dist/public vẫn đúng bản đã sửa ở lượt trước, cùng SHA-256 `87e56b7710f7a84c16e5468f151fc0a9118b2bcda82290390d5fab37d41b6b83`. Không cần biên dịch lại chỉ để xử lý lỗi đồng bộ Markdown này.
- Độ sát VOAI 2025 mã 006 vẫn ghi **UNVALIDATED**, phù hợp giới hạn bằng chứng hiện tại.

## 1. P1 — Script đồng bộ Markdown không thay được lời giải

Nguồn lỗi: `scripts/enrich_olp02_terms_and_links.py:414`.

Regex hiện tại tìm:

```text
### Câu VOAI02-Mxx: ... **Lời giải chi tiết:**
```

File Markdown thật dùng:

```text
### VOAI02-Mxx. ...
#### Lời giải chi tiết:
```

Kết quả: **0 heading** khớp mẫu script, trong khi file có **60 heading MCQ** dạng thật. Script vẫn ghi “Đã đồng bộ hoàn tất” dù không thay được block nào.

Đã tách 60 block và so sánh sau chuẩn hóa khoảng trắng: **60/60 explanation trong Markdown khác JSON**. Đây là khác biệt nội dung, không chỉ khác xuống dòng:

| Câu | JSON/web mới | Markdown vẫn còn |
|---|---|---|
| M03 | p-value theo thống kê kiểm định cực đoan; câu độc lập | `P(Data \mid H0)`; dẫn OLP01-A04 |
| M05 | Dẫn VOAI03-M02, Hessian | Dẫn OLP01-A05, Poisson |
| M13 | Dẫn OLP01-C01, k-NN | Dẫn OLP01-B01, Conv2D |
| M49 | Dẫn OLP01-C28, NLP pipeline | Dẫn OLP01-C16, object detection |
| M51 | Dẫn OLP01-B09, cosine | Dẫn OLP01-C18, Silhouette |

Sửa parser/regex theo heading thật, đếm số thay thế và fail nếu không đủ 60 câu; sau đó sinh lại Markdown. Thêm kiểm tra đối chiếu explanation theo ID để tránh “ghi file thành công” bị coi là “đồng bộ thành công”. Không đổi JSON đang đúng sang nội dung Markdown cũ.

## 2. P2 — Nhãn phương án trong giải thích M01 bị cũ

M01 có option **B = khoảng 98%**, option **A = khoảng 4%**, đáp án đúng D = khoảng 11%.

Khối bẫy vẫn viết “chọn 98% (A)” trong cả JSON và Markdown. Sửa `(A)` thành `(B)`, hoặc bỏ chữ cái và giữ nội dung “chọn 98%”. Không cần đổi option hay answer. Đây là chú thích sai phương án; phép tính Bayes và đáp án D vẫn đúng trong câu đang kiểm tra.

## Prompt sửa nốt

```text
Đọc docs/VERIFY_BAO_CAO_LAN_5_2026-10-09.md. Giữ JSON, các liên hệ mới, đáp án và PDF đã đúng.

1. Sửa đồng bộ Markdown trong scripts/enrich_olp02_terms_and_links.py: regex dòng 414 tìm “### Câu ID:” và “**Lời giải chi tiết:**”, nhưng file thật dùng “### ID.” và “#### Lời giải chi tiết:”. Hiện khớp 0 lần và cả 60 explanation Markdown vẫn cũ. Parse đúng block theo ID, dùng số thay thế/đối chiếu để fail nếu không đủ 60. Sinh lại Markdown từ explanation JSON hiện tại, bảo toàn prompt/options/answer/essay.
2. Sửa chú thích M01 “98% (A)” thành “98% (B)” hoặc bỏ nhãn chữ cái trong JSON và nguồn sinh liên quan. Không shuffle option, đổi answer hay điểm. Sinh lại Markdown và HTML để mang sửa đổi này sang các bản phân phối.
3. Xác nhận 60/60 prompt, options, answer và explanation của Markdown bằng JSON theo ID; public/dist HTML mang JSON mới. Chạy validator, audit quality và KaTeX. Ghi số block khớp thật trong báo cáo, không chỉ ghi script chạy thành công. Giữ UNVALIDATED cho độ sát VOAI2025.
Không mở rộng thêm đề hoặc thay các câu hiện tại để sửa liên hệ.
```

## Kiểm tra đã thực hiện và giới hạn

Chạy lại `node scripts/validate.mjs`, `node scripts/audit_katex_syntax.mjs`, `python -X utf8 scripts/audit_quality.py`: tất cả exit 0; 3 đề/184 câu đúng schema, KaTeX báo **2.689 đoạn, 0 lỗi** trong phạm vi script; audit quality qua tiêu chí cấu trúc/tồn tại tham chiếu.

Đọc báo cáo, nguồn enrichment và Markdown bằng `Get-Content`; dùng `rg` định vị regex đồng bộ và các liên hệ cũ; các đoạn Python chạy từ stdin để đối chiếu 60 dòng báo cáo với JSON, các câu đích, heading §, prompt/options/answer/explanation Markdown, dữ liệu nhúng HTML và SHA-256 HTML/PDF. Tìm memory liên quan không có hit phù hợp; không dùng memory làm căn cứ kết luận.

Không chạy lại unit tests/typecheck hoặc build vì lượt này tập trung vào thay đổi dữ liệu và đồng bộ, không có sửa code từ phía Codex. Kết quả 18 tests trong báo cáo là kết quả Gemini báo và đã được chạy lại ở lượt verify trước, không phải một lượt chạy mới ở đây. Không xác nhận phát video thực tế, không review lại toàn bộ 184 lập luận hoặc so toàn văn đề VOAI chính thức.

File tạo duy nhất trong lượt này: `docs/VERIFY_BAO_CAO_LAN_5_2026-10-09.md`.

**Ôn ngay:** dùng JSON/web mới để đọc lời giải và liên hệ đã sửa; tạm tránh lời giải Markdown Đề 02 cho đến khi đồng bộ lại. Không cần chờ các chi tiết này hoàn tất mới bắt đầu làm đề.
