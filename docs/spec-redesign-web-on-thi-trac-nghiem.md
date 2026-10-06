# Spec Redesign — Web Ôn Thi Trắc Nghiệm OLP AI

> Hiện trạng: Vite + React + TS. Dữ liệu đề JSON (mcq / code / essay, module A/B/C).
> Chế độ: Practice (hiện đáp án ngay), Exam (làm xong mới chấm), timer, tự luận tự chấm rubric, thống kê điểm theo module.
> Vấn đề: UI bê từ khung open-source nên rối; công thức toán render text thô rất xấu.
> Ngày lập spec: 07/10/2026.

---

## 1. Phân tích UI/UX app thi thử lái xe VN

Nguồn tham khảo: app OTOMOTO 600 câu, các app "600 câu GPLX" trên App Store/Google Play, web thi thử (thithulaixe.vn, daotaolaixehd.com.vn — giao diện mô phỏng phần mềm thi thật của Bộ Công an).

### 1.1. Màn hình chọn đề

- **2 tap là vào bài**: chọn hạng bằng → chọn đề cố định / đề ngẫu nhiên. Không bắt nhập thông tin thí sinh rườm rà ở bản mobile (bản PC cũ của Bộ Công an còn bắt nhập SBD, đăng nhập — pattern này nên bỏ).
- Đề hiện dạng list/card kèm meta ngay trên card: số câu, thời gian, % hoàn thành.
- Câu hỏi phân loại theo chương/chủ đề rõ ràng (khái niệm, biển báo, sa hình...), có mục riêng "câu điểm liệt" và "câu đã làm sai" để ôn trọng tâm.
- **Điểm dở cần tránh**: nhồi banner quảng cáo, menu nhiều tầng.

### 1.2. Màn hình làm bài (được tối ưu kỹ nhất)

- **1 câu / 1 màn hình.** Đáp án là nút full-width → chạm 1 lần là chọn, không có nút "xác nhận" thừa.
- **Chuyển câu**: swipe trái/phải hoặc nút mũi tên ← →. Bản web hỗ trợ phím tắt: phím số 1–4 chọn đáp án, phím mũi tên chuyển câu, Enter/Esc nộp bài.
- Thanh tiến trình + timer luôn sticky trên cùng, không bao giờ bị cuộn mất.
- **Palette câu hỏi**: 1 nút mở bottom sheet/modal dạng lưới số. Màu trạng thái chuẩn toàn ngành:
  - Xám = chưa làm
  - Xanh = đã làm
  - Viền đậm = câu đang làm
  - Đỏ = câu điểm liệt (tương đương "câu quan trọng" trong app của ta)
  - Tap vào số là nhảy câu ngay, không cần vuốt qua từng câu.

### 1.3. Chấm ngay (Practice mode)

- Chọn đáp án → highlight xanh/đỏ **tức thì** + giải thích hiện ngay dưới câu hỏi + nút "Câu tiếp →" xuất hiện.
- Không tap thừa, vòng lặp học (làm → biết đúng sai → hiểu vì sao) khép kín trong 1 màn hình.
- Pattern chung các app: "xem đáp án và giải thích ngay sau khi trả lời để học hỏi tức thì".

### 1.4. Màn hình kết quả

- Chữ **ĐẠT / KHÔNG ĐẠT** cỡ lớn đập vào mắt đầu tiên, sau đó mới đến số câu đúng, điểm, thời gian.
- Lưới review màu: **xanh = đúng, đỏ = sai, vàng = chưa trả lời**. Tap vào ô đỏ để xem lại câu + giải thích.
- Nút "Làm đề khác" 1 tap; có mục "câu đã làm sai" để ôn lại.

### 1.5. Bốn nguyên tắc làm chúng nhanh/gọn

1. **Single-tap select** — đáp án là nút bấm trực tiếp, không radio + nút xác nhận.
2. **Palette số** — nhảy đến bất kỳ câu nào trong 1 tap thay vì vuốt tuần tự.
3. **Keyboard shortcut** (bản desktop) — 1-4, mũi tên, Enter.
4. **Feedback inline** — chấm và giải thích ngay tại chỗ, không chuyển trang.

---

## 2. Spec layout mới (mobile-first)

Nguyên tắc chung:

- Từ mở app đến làm bài: **tối đa 2 tap**.
- Mọi thao tác cốt lõi (chọn đáp án, chuyển câu, nộp bài) ≤ 2 chạm, target chạm ≥ 48px.
- Chuyển câu < 1s: preload câu kế trước, `QuestionCard` memoized theo question id (đổi câu chỉ re-render card, không re-render top/bottom bar), timer dùng ref + rAF thay vì setState mỗi giây, palette virtualize nếu > 100 câu.
- Exam mode: chọn đáp án chỉ đánh dấu, **không** auto-advance (tránh tap nhầm mất câu).

### 2.1. Màn 1 — Chọn đề (DeckPicker)

```
┌─────────────────────────┐
│ Ôn thi OLP AI      [🔥] │  ← header gọn, không menu rườm rà
│ ┌─────────┬─────────┐   │
│ │Practice │  Exam   │   │  ← segmented control, nhớ lựa chọn lần trước
│ └─────────┴─────────┘   │
│ ┌─ Module A ─────────┐  │
│ │ ML cơ bản · 40 câu │  │  ← 1 card = 1 dòng: tên, số câu,
│ │ ██████░░ 75% · TB 7.2│  │    progress bar, điểm TB. Tap = chọn
│ └────────────────────┘  │
│ ┌─ Module B ─────────┐  │
│ │ DL nâng cao · 32 câu  │
│ │ ████░░░░ 40% · TB 6.1 │
│ └────────────────────┘  │
│ ┌─ Module C ─────────┐  │
│ └────────────────────┘  │
│ Exam: [20c/15'] [40c/30']│ ← chip preset, chỉ hiện ở Exam mode
│ ┌─────────────────────┐ │
│ │     ▶ BẮT ĐẦU       │ │  ← CTA sticky bottom
│ └─────────────────────┘ │
└─────────────────────────┘
```

- Không form, không dropdown, không màn hình cấu hình riêng.
- Module nào cũng hiển thị tiến độ + điểm TB để user biết mình yếu đâu (kế thừa logic thống kê hiện có).

### 2.2. Màn 2 — Làm bài (Quiz)

```
┌─────────────────────────┐
│ ← │ Câu 7/40 │ ⏱ 12:34 │ ▦ │  ← sticky top bar (không cuộn mất)
├─────────────────────────┤
│ [Module B]              │  ← tag module của câu hiện tại
│                         │
│ Câu hỏi render đẹp...   │  ← QuestionCard:
│ ┌─────────────────────┐ │     text + MathText (KaTeX)
│ │ model.fit(X, y)     │ │  + code block scroll ngang
│ └─────────────────────┘ │
│                         │
│ ┌─ (A) đáp án 1 ──────┐ │
│ │ (B) đáp án 2        │ │  ← full-width, cao ≥48px
│ │ (C) đáp án 3        │ │    tap 1 lần chọn, tap lại để bỏ
│ └─ (D) đáp án 4 ──────┘ │
│                         │
│ ┌ Practice feedback ──┐ │  ← CHỈ Practice mode:
│ │ ✓ Đúng. Vì ...      │ │    xanh/đỏ + giải thích hiện
│ └─────────────────────┘ │    inline ngay tại chỗ
│                         │
├─────────────────────────┤
│ [← Trước]      [Sau →]  │  ← sticky bottom bar
│ ┌─────────────────────┐ │
│ │   NỘP BÀI (32/40)   │ │  ← hiện số câu đã làm
│ └─────────────────────┘ │
└─────────────────────────┘
```

Chi tiết tương tác:

- **Palette câu hỏi**: tap nút ▦ → bottom sheet lưới số 1..N, màu xám (chưa làm) / xanh (đã làm) / viền đậm (đang làm). Tap số → đóng sheet + nhảy câu.
- **Nộp bài**: tap → modal xác nhận liệt kê "Còn 8 câu chưa làm. Nộp bài?" → [Nộp] / [Tiếp tục làm].
- **Câu tự luận (essay)**: textarea + nút "Chấm theo rubric" mở panel rubric (slider điểm từng tiêu chí, xem §4 mục 11).
- **Câu code**: block `<pre>` scroll ngang, font mono, không render KaTeX bên trong.
- Hết giờ ở Exam mode: tự động nộp.

### 2.3. Màn 3 — Kết quả (Result)

```
┌─────────────────────────┐
│                         │
│        ✓  ĐẠT           │  ← hero cỡ lớn, xanh/đỏ
│         8.5 / 10        │
│    34/40 câu · 12'30"   │
│                         │
│ A ████████░░ 8.0        │  ← điểm theo module
│ B ██████████ 9.5        │    (giữ logic thống kê hiện có,
│ C ██████░░░░ 6.0        │     chỉ làm lại UI)
│                         │
│ ▦ ▦ ▦ ▦ ▦ ▦ ▦ ▦ …      │  ← lưới review xanh/đỏ/vàng,
│                         │    tap ô đỏ → chi tiết câu
│ ┌─────────────────────┐ │
│ │  ↻ Làm lại câu sai  │ │  ← CTA chính: chỉ ôn câu sai
│ └─────────────────────┘ │
│ [Đề mới]   [Trang chủ]  │
└─────────────────────────┘
```

- Practice mode: không cần hero to (feedback đã xong từng câu) — màn kết quả chỉ cần tổng điểm + lưới review + "làm lại câu sai".
- Chi tiết 1 câu khi review: hiện câu hỏi, đáp án user đã chọn (đỏ nếu sai), đáp án đúng (xanh), giải thích.

---

## 3. Giải pháp render công thức toán

### 3.1. KaTeX vs MathJax

| Tiêu chí | KaTeX | MathJax |
|---|---|---|
| Tốc độ | Render **đồng bộ**, không reflow trang; nhanh hơn MathJax ~2–3× trên cùng nội dung | v3 đã cải thiện nhiều nhưng vẫn chậm hơn rõ khi typeset lại nhiều công thức (đúng case chuyển câu nhanh) |
| Bundle | ~230KB JS + fonts woff2 (CSS chỉ tải font nào dùng đến, mỗi font vài chục KB) | v3 (tex-chtml) ~600KB–1MB; wrapper `better-react-mathjax` chỉ ~7KB nhưng MathJax vẫn phải tải từ CDN |
| Vite | `npm i katex` thuần túy: `import katex from 'katex'` + `import 'katex/dist/katex.min.css'`, fonts tự copy vào dist, **không cần config thêm**, không FOUC | Phải load script ngoài hoặc dynamic import nặng; dễ bị flash công thức thô khi chuyển câu |
| Cú pháp `$...$` | Hỗ trợ qua `katex/contrib/auto-render` hoặc tự split regex — đều dễ | Hỗ trợ native qua config |
| Hạn chế | Thiếu vài package LaTeX hiếm (`\require`, môi trường nâng cao) | Hỗ trợ gần như đầy đủ LaTeX |

**Chốt: KaTeX.**

Lý do quyết định: yêu cầu "chuyển câu < 1s" thì render công thức phải đồng bộ và rẻ. KaTeX render 1 công thức ở mức micro-giây; MathJax chạy async sẽ gây giật/nhấp nháy đúng lúc user vuốt nhanh qua các câu. Với công thức ML cơ bản (Conv, entropy, Bayes, IoU, F1, cosine...), KaTeX đáp ứng 100%.

### 3.2. Cách tích hợp trong React

- Viết **1 component duy nhất `MathText`**:
  - Input: string (có thể chứa text thường lẫn `$...$` inline và `$$...$$` display).
  - Xử lý: split string theo `$$...$$` và `$...$`, render từng đoạn công thức bằng `katex.renderToString`.
  - Bọc try/catch: công thức lỗi cú pháp → fallback hiển thị text thô, **không bao giờ crash cả câu hỏi**.
  - Dùng cho: stem câu hỏi, các option đáp án, phần giải thích.
- **Không render KaTeX trong block code** — câu code giữ nguyên `<pre>` + font mono.
- CSS: `import 'katex/dist/katex.min.css'` một lần ở entry; không cần config Vite đặc biệt.

### 3.3. Chuẩn viết công thức cho người soạn đề

Quy ước lưu trong JSON:

- Field text (stem / options / explanation) được phép chứa `$...$` (inline) và `$$...$$` (display, xuống dòng).
- Trong JSON nhớ **escape backslash nhân đôi** (`\\frac`, `\\sum`...).
- Biến số: `$x$`, `$y$` (KaTeX tự in nghiêng). Chữ thường trong công thức (tên hàm, chữ viết tắt) dùng `\text{}`: `$p_\text{data}$` — không viết `$p_data$` (xấu, sai chính tả toán).
- Phân số `\frac{}{}` tối đa lồng 2 tầng; sâu hơn thì viết dạng `$1 / (1 + e^{-z})$`.
- Ma trận / vector: `\begin{bmatrix} ... \end{bmatrix}`.
- Xuống dòng trong display: `$$ ... \\ ... $$`.

### 3.4. Mẫu công thức chuẩn (copy-paste cho người soạn đề)

- **Conv output size:** `$$O = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$$`
- **Entropy:** `$$H(p) = -\sum_{i=1}^{n} p_i \log p_i$$`
- **Bayes:** `$$P(A|B) = \frac{P(B|A)\,P(A)}{P(B)}$$`
- **IoU:** `$$\text{IoU} = \frac{|A \cap B|}{|A \cup B|}$$`
- **F1:** `$$F_1 = \frac{2PR}{P + R}$$`
- **Cosine similarity:** `$$\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}$$`
- Inline trong câu: `Hàm softmax $\sigma(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$ chuẩn hóa...`

---

## 4. Component cần build/sửa (theo thứ tự ưu tiên)

1. **MathText** — wrapper KaTeX render `$...$`/`$$...$$` trong stem/option/giải thích, có fallback text thô khi lỗi cú pháp.
2. **AnswerOption** — nút đáp án full-width ≥48px, badge A/B/C/D, 3 trạng thái (chưa chọn / đã chọn / đúng-sai), tap 1 lần chọn.
3. **QuestionCard** — card câu hỏi memoized theo question id (text + MathText + code block scroll ngang); chìa khóa cho chuyển câu <1s.
4. **QuestionPalette** — bottom sheet lưới số câu với màu trạng thái xám/xanh/viền, tap để nhảy câu.
5. **QuizTopBar** — sticky top: nút thoát, tiến trình "Câu n/N", timer (ref + rAF), nút mở palette.
6. **QuizBottomBar** — sticky bottom: Trước / Sau / Nộp bài; nút Nộp mở modal xác nhận liệt kê số câu chưa làm.
7. **PracticeFeedback** — panel xanh/đỏ + giải thích hiện inline ngay sau khi chọn đáp án ở Practice mode.
8. **ResultHero** — ĐẠT/KHÔNG ĐẠT cỡ lớn, điểm số, thời gian, thanh điểm theo module A/B/C.
9. **ReviewGrid** — lưới màu xanh/đỏ/vàng xem lại từng câu; tap ô đỏ mở chi tiết đáp án đúng/sai + giải thích.
10. **DeckPicker** — màn chọn đề: segmented Practice/Exam, card module A/B/C (tên, số câu, progress, điểm TB), chip preset số câu/giờ cho Exam, CTA sticky.
11. **EssayRubric** — form tự chấm tự luận gọn cho mobile: slider điểm từng tiêu chí thay vì input số.
12. **StatsDashboard** — giữ nguyên logic thống kê điểm theo module, chỉ làm lại UI theo style mới.

### Thứ tự triển khai gợi ý

- **Đợt 1 (giải quyết 2 pain point chính):** MathText → AnswerOption → QuestionCard. Xong đợt này là công thức đã đẹp và màn làm bài đã gọn.
- **Đợt 2 (tốc độ thao tác):** QuestionPalette → QuizTopBar → QuizBottomBar → PracticeFeedback.
- **Đợt 3 (hoàn thiện):** DeckPicker → ResultHero → ReviewGrid → EssayRubric → StatsDashboard.
