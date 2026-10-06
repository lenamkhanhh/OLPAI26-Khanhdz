# Schema đề OLP AI HCMUS 2026 (module A/B/C)

Mỗi file `src/data/exams/olp-NN.json` là một đề đầy đủ.

## Metadata đề

```json
{
  "id": "olp-01",
  "title": "Đề 01 - Ôn tập toàn diện",
  "description": "...",
  "durationMinutes": 90,
  "totalPoints": 100,
  "disclaimer": "...",
  "moduleLabels": { "A": "...", "B": "...", "C": "..." },
  "moduleOverview": ["A: ...", "B: ...", "C: ..."],
  "questions": []
}
```

- `totalPoints = 100`: tổng điểm 60 câu chấm điểm (trắc nghiệm + code). Tự luận KHÔNG tính vào.
- `moduleOverview`: đúng 3 chuỗi (A/B/C). `moduleLabels`: đủ A/B/C, không có D.

## Câu hỏi (64–65 câu/đề)

| Loại | Module | Số lượng | Điểm | Yêu cầu |
|---|---|---|---|---|
| mcq | A | 12 | 2 | 4 options A/B/C/D khác nhau, `answer` hợp lệ, `explanation` + `→ Xem §x.y` |
| mcq | B | 16 | 2 | như trên, ưu tiên tính tay + NumPy |
| code | B | 2 | 7 | `modelAnswer` + `rubric` ≥ 3 ý |
| mcq | C | 30 | 1 | như trên, phủ ML/DL/CV/NLP |
| essay | C | 4–5 | 10 | `modelAnswer` theo khung 5 bước + `rubric` ≥ 3 ý, chấm riêng |

## Quy tắc toàn repo

- ID đề và ID câu hỏi duy nhất; prompt không trùng nhau giữa các đề.
- Đáp án MCQ phân bố đều: mỗi key A/B/C/D xuất hiện 6–24 lần/đề (mục tiêu ~14–15).
- ID câu hỏi dạng `OLP<NN>-<Module><số>` (vd `OLP01-C07`), tự luận `OLP<NN>-E<k>`.
