# Handoff — Rebuild UI Web Ôn Thi OLP AI (cho Gemini)

## 1. Mục tiêu (làm gì)

Rebuild lại **UI/UX** web ôn thi trắc nghiệm OLP AI HCMUS 2026 cho đẹp + gọn kiểu app thi lái xe (OTOMOTO / 600 câu GPLX): chọn đề ≤2 tap, làm bài 1 câu/màn hình, đáp án full-width tap 1 lần, palette lưới số, top/bottom bar sticky, Practice chấm inline, Exam chấm sau, kết quả ĐẠT/CHƯA ĐẠT + lưới review xanh/đỏ/vàng. Công thức toán render đẹp bằng KaTeX.

**Phạm vi:** CHỈ làm lại UI + CSS + component hiển thị. **GIỮ NGUYÊN:** schema JSON đề, validator, logic chấm điểm, nội dung Đề 01, 3 file tài liệu `content/`.

## 2. Repo & link

- GitHub: https://github.com/lenamkhanhh/OLPAI26-Khanhdz (public, branch `main`)
- Web live: https://lenamkhanhh.github.io/OLPAI26-Khanhdz/
- Local: `C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26`
- Stack: Vite 5 + React 18 + TS + KaTeX (đã `npm i katex @types/katex`), deploy GitHub Pages bằng workflow có sẵn.
- Lệnh: `npm install` → `npm run dev` (port 5173) → `npm run validate` → `npm run build` → `npm test` (vitest).

## 3. Cấu trúc file (path → vai trò)

```
index.html                  title/desc OLP AI HCMUS 2026
vite.config.ts              base './' (cho Pages), react plugin
package.json                scripts: dev/build/preview/validate/test
.github/workflows/deploy.yml  validate → build → deploy Pages (đừng đụng)
scripts/validate.mjs        validator chuẩn (đừng đụng): mỗi đề 60 câu chấm điểm
                            A12×2đ / B16×2đ + 2 code×7đ / C30×1đ = 100đ
                            + 4–5 essay module C ×10đ chấm riêng; đáp án A/B/C/D
                            phân bố 6–24 lần/đề; ID/prompt duy nhất toàn repo
src/main.tsx                entry, import katex.min.css + App
src/App.tsx                 state mode (persist localStorage) + chọn đề/làm bài
src/types/exam.ts           ModuleId 'A'|'B'|'C'; Question mcq|code|essay;
                            AnswerState {selected?, text?, essayScore?, rubricChecks?}
src/data/exams/index.ts     auto-load mọi olp-*.json
src/data/exams/olp-01.json  Đề 01: 64 câu (60 chấm + 4 essay), công thức đã viết
                            LaTeX $...$/$$...$$ (nhớ escape \\ trong JSON)
src/utils/scoring.ts        summarizeExam: trắc nghiệm thang 100 + essay riêng
src/utils/storage.ts        localStorage: progress, results, mode
src/components/MathText.tsx       render text + KaTeX (đã đúng, có thể giữ)
src/components/AnswerOption.tsx   nút đáp án (làm lại style OK)
src/components/QuestionCard.tsx   card câu hỏi (memo theo id)
src/components/QuestionPalette.tsx bottom sheet lưới số
src/components/QuizTopBar.tsx     sticky top: ←, Câu n/N, timer rAF, ▦
src/components/QuizBottomBar.tsx  sticky bottom: Trước/Sau/Nộp (x/N)
src/components/QuizRunner.tsx     ghép màn làm bài + phím tắt 1-4/←/→/Enter + modal nộp
src/components/ExamSelector.tsx   màn chọn đề (segmented + card + CTA)
src/components/ResultSummary.tsx  hero ĐẠT≥70% + ModuleStats + lưới review
src/components/ModuleStats.tsx    thanh điểm A/B/C (giữ logic)
src/components/Disclaimer.tsx     disclaimer (giữ)
src/components/ScoreCatPopup.tsx  popup mèo (đang không dùng, xóa hoặc giữ)
src/styles/global.css             style cũ AI-TEST (đang rối → dọn/gộp lại)
src/styles/quiz.css               style UI mới (làm lại cho đẹp)
content/01-ly-thuyet-olp-ai.md    lý thuyết 5 chương + 24 lỗi hay mắc (đừng đụng)
content/02-de-luyen-olp-ai.md     đề luyện không đáp án (đừng đụng)
content/03-dap-an-olp-ai.md       đáp án full (đừng đụng)
docs/EXAM_SCHEMA_OLP.md           schema + quy ước LaTeX cho người soạn đề
docs/exam-template.json           template đề mới olp-NN.json
```

## 4. Spec redesign đã chốt (file gốc: `spec-redesign-web-on-thi-trac-nghiem.md`)

- 2 tap từ mở app đến làm bài; thao tác ≤2 chạm, target ≥48px; chuyển câu <1s.
- Practice: chọn → xanh/đỏ + giải thích inline + nút "Câu tiếp →". Exam: chỉ đánh dấu, không auto-advance, hết giờ tự nộp.
- Palette: xám chưa làm / xanh đã làm / viền đậm đang làm; tap số nhảy ngay.
- Nộp bài: modal "Còn N câu chưa làm. Nộp bài?" → Nộp / Tiếp tục.
- Essay: textarea + checklist rubric + slider điểm 0–10.
- KaTeX thắng MathJax (render đồng bộ, bundle ~230KB, `import 'katex/dist/katex.min.css'`, fonts tự vào dist, không config Vite thêm).
- Thứ tự ưu tiên: MathText → AnswerOption → QuestionCard → Palette/TopBar/BottomBar/Feedback → DeckPicker/ResultHero/ReviewGrid/EssayRubric.

## 5. Vấn đề hiện tại cần Gemini fix

1. Công thức một số chỗ còn hiện thô (text LaTeX lọt ra ngoài) — kiểm tra `MathText` split `$`/`$$`/code block + rà lại JSON đề.
2. UI tổng thể xấu, chưa gọn như app thi lái xe — làm lại layout + CSS mobile-first (giữ nguyên component interface để không vỡ logic).

## 6. Tiêu chí nghiệm thu

- `npm run validate` pass, `npm run build` pass, `npm test` pass (7 test).
- Chạy `npm run dev`: chọn đề → làm 1 câu Practice (đúng hiện xanh + KaTeX + Câu tiếp) → ▦ nhảy câu → Nộp (modal đếm đúng câu chưa làm) → hero + lưới 64 ô đúng màu → Ôn từ câu sai.
- Không sửa schema JSON, không đổi thang điểm, không động vào `content/` và `scripts/validate.mjs`.
