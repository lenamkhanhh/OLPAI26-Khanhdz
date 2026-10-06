# OLP AI HCMUS 2026 — Ôn thi vòng loại cấp trường

Web thi thử + tài liệu ôn thi Olympic AI HCMUS 2026 (trắc nghiệm + tự luận giải pháp AI).
Khung web tái sử dụng từ [AI-TEST](https://github.com/HungBil/AI-TEST) (MIT), ruột đề soạn mới theo 5 chương OLP, chỉ giữ 3 module A/B/C (bỏ D vì OLP học thuật).

## Cấu trúc đề (mỗi đề)

| Module | Nội dung | Số câu | Điểm |
|---|---|---|---|
| A | Toán & Xác suất – Thống kê | 12 trắc nghiệm | 24 |
| B | Python / NumPy / Tính tay (gồm 2 code) | 16 trắc nghiệm + 2 code | 32 + 14 |
| C | ML / DL / CV / NLP | 30 trắc nghiệm | 30 |
| Tự luận (C) | 2 CV + 1 NLP + 1 tabular, khung 5 bước | 4 câu × 10đ | chấm riêng |

- Trắc nghiệm + code: thang 100 điểm. Tự luận: chấm riêng theo rubric (self-grade).
- Thời gian gợi ý: 90 phút trắc nghiệm + 60 phút tự luận.

## Tài liệu (`content/`)

- `01-ly-thuyet-olp-ai.md` — lý thuyết 5 chương + bảng lỗi hay mắc, đánh số §x.y.
- `02-de-luyen-olp-ai.md` — đề luyện (không đáp án).
- `03-dap-an-olp-ai.md` — đáp án + vì sao đúng/sai + trích dẫn §.

## UI/UX (kiểu app thi lái xe)

- Màn chọn đề: segmented Practice/Exam (nhớ lựa chọn), card từng đề kèm tiến độ + điểm gần nhất, CTA sticky.
- Màn làm bài: 1 câu/màn hình, đáp án full-width tap 1 lần (tap lại để bỏ), top bar sticky (Câu n/N + timer + palette ▦), bottom bar sticky (Trước/Sau/Nộp kèm số câu đã làm), palette lưới số, phím tắt desktop 1–4 + ←/→ + Enter.
- Practice: chấm + giải thích inline ngay tại chỗ + nút "Câu tiếp →". Exam: chỉ đánh dấu, hết giờ tự nộp.
- Kết quả: ĐẠT (≥70%) / CHƯA ĐẠT cỡ lớn, điểm module A/B/C, lưới review xanh/đỏ/vàng, ôn lại từ câu sai.
- Công thức render bằng KaTeX (`$...$`/`$$...$$` trong JSON, nhớ escape `\\`).

## Chạy web thi thử

```
npm install
npm run dev
```

## Kiểm tra đề

```
npm run validate
```

Validator (`scripts/validate.mjs`) kiểm tra: đủ 60 câu chấm điểm (A12/B18/C30, gồm 2 code ở B) + 4–5 tự luận ở C, tổng điểm trắc nghiệm = 100, tự luận 10đ/câu chấm riêng, MCQ đủ A/B/C/D với đáp án phân bố đều, essay/code có modelAnswer + rubric ≥ 3 ý, không trùng ID/prompt toàn repo.

## Build / deploy

```
npm run build
npm run preview
```

Bản build nằm ở `dist/`, host tĩnh được (GitHub Pages / Netlify / Vercel).

## Thêm đề mới

1. Copy `docs/exam-template.json` thành `src/data/exams/olp-NN.json` (NN = 02..20).
2. Điền 60 câu chấm điểm + 4 tự luận theo `docs/EXAM_SCHEMA_OLP.md`.
3. Thêm đề vào `content/02-de-luyen-olp-ai.md` (không đáp án) + `content/03-dap-an-olp-ai.md` (đáp án).
4. Chạy `npm run validate` rồi `npm run build`.

## Nguồn enrich

AI-TEST (600 câu) · VOAI 100 câu · Tutorial AI Vietnam CV/NLP · IOAI Guide (SOTA) · checklist 400+ bài SOTA · Đề IOAI 2026. Diễn đạt viết lại, không copy nguyên văn.
