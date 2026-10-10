# -*- coding: utf-8 -*-
"""
scripts/shuffle_mock_exams.py
Khử chu kỳ ABCD nhân tạo trong Đề 05 (90 câu) và Đề 03 (M51-M100) bằng deterministic PRNG shuffle,
đồng thời đồng bộ 100% lời giải (66 câu NLP/CV lệch chữ cái),
sửa lỗi bẫy đảo ngược ở VOAI03-M04, và cập nhật metadata Đề 03.
"""

import json
import random
import re
import os

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
E5_PATH = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-05.json")
E3_PATH = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")

# ==========================================
# 1. XỬ LÝ ĐỀ 05
# ==========================================
with open(E5_PATH, "r", encoding="utf-8") as f:
    e5 = json.load(f)

# Ta dùng PRNG với seed xác định để có thể tái lập 100%
rng_e5 = random.Random(20261011)

e5_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
e5_shuffled_keys = []

for idx, q in enumerate(e5["questions"]):
    curr_ans = q["answer"]
    correct_opt = next(o for o in q["options"] if o["key"] == curr_ans)
    correct_text = correct_opt["text"]
    
    # 4 options hiện tại
    texts = [o["text"] for o in q["options"]]
    # Shuffle options
    rng_e5.shuffle(texts)
    
    # Gán lại key A, B, C, D
    new_options = [{"key": k, "text": t} for k, t in zip(["A", "B", "C", "D"], texts)]
    new_ans = next(o["key"] for o in new_options if o["text"] == correct_text)
    
    q["options"] = new_options
    q["answer"] = new_ans
    e5_dist[new_ans] += 1
    e5_shuffled_keys.append(new_ans)
    
    # Cập nhật lời giải
    exp = q["explanation"]
    # Với NLP: "Kiểm tra phương án `X`:" -> "Kiểm tra phương án `new_ans`:"
    exp = re.sub(r'Kiểm tra phương án `[ABCD]`:', f'Kiểm tra phương án `{new_ans}`:', exp)
    # Với CV: "Phương án `X` khớp" -> "Phương án `new_ans` khớp"
    exp = re.sub(r'Phương án `[ABCD]` khớp', f'Phương án `{new_ans}` khớp', exp)
    q["explanation"] = exp

print("Đề 05 Answer Distribution sau khi shuffle:", e5_dist)

# Kiểm tra xem có chu kỳ ABCD tuần tự lặp lại không
is_cycle_e5 = all(e5_shuffled_keys[i] == ["A", "B", "C", "D"][i % 4] for i in range(len(e5_shuffled_keys)))
print("Đề 05 còn chu kỳ tuần tự ABCD không?", is_cycle_e5)

with open(E5_PATH, "w", encoding="utf-8") as f:
    json.dump(e5, f, ensure_ascii=False, indent=2)

print("Đã cập nhật xong Đề 05.")

# ==========================================
# 2. XỬ LÝ ĐỀ 03
# ==========================================
with open(E3_PATH, "r", encoding="utf-8") as f:
    e3 = json.load(f)

# 2.1. Sửa lỗi bẫy VOAI03-M04
q_m04 = next(q for q in e3["questions"] if q["id"] == "VOAI03-M04")
# Sửa bẫy A (Kỳ vọng) và D (Phương sai)
q_m04["explanation"] = q_m04["explanation"].replace(
    "- **Phương án A (Phương sai):** Phương sai chỉ đo độ lệch khỏi giá trị trung bình của biến số, phụ thuộc vào thang đo (scale), không đo lượng thông tin xác suất.\n- **Phương án D (Kỳ vọng):** Kỳ vọng chỉ là giá trị trung bình cộng theo xác suất.",
    "- **Phương án A (Kỳ vọng):** Kỳ vọng chỉ là giá trị trung bình cộng theo xác suất, không đo mức độ hỗn loạn hay lượng thông tin xác suất.\n- **Phương án D (Phương sai):** Phương sai chỉ đo độ phân tán của giá trị số học quanh kỳ vọng, phụ thuộc vào thang đo (scale), không đo mức độ bất định thông tin."
)
print("Đã sửa bẫy VOAI03-M04.")

# 2.2. Khử chu kỳ ABCD ở M51-M100 (từ index 50 đến 99)
rng_e3 = random.Random(20260303)

for idx in range(50, 100):
    q = e3["questions"][idx]
    curr_ans = q["answer"]
    correct_opt = next(o for o in q["options"] if o["key"] == curr_ans)
    correct_text = correct_opt["text"]
    
    texts = [o["text"] for o in q["options"]]
    rng_e3.shuffle(texts)
    
    new_options = [{"key": k, "text": t} for k, t in zip(["A", "B", "C", "D"], texts)]
    new_ans = next(o["key"] for o in new_options if o["text"] == correct_text)
    
    q["options"] = new_options
    q["answer"] = new_ans

# 2.3. Cập nhật metadata Đề 03
e3["disclaimer"] = "Bộ đề tuyển tập và biên tập mô phỏng kỳ thi Olympic Tin học & Trí tuệ Nhân tạo OLP AI (dựa trên Đề TN Số 3 và ngân hàng mở rộng Gemini), gồm 100 câu trắc nghiệm (32 module A, 39 module B, 29 module C) và 4 bài tự luận chuyên sâu."
e3["durationMinutes"] = 120
e3["moduleLabels"] = {
    "A": "Lý thuyết Nền tảng, Tối ưu & Dữ liệu Bảng (32 câu)",
    "B": "Deep Learning, Computer Vision & NLP Nâng Cao (39 câu)",
    "C": "Học sâu Chuyên sâu & Tự luận Giải pháp Thực chiến (29 câu TN + 4 bài tự luận)"
}
e3["moduleOverview"] = [
    "A: 32 câu Lý thuyết nền tảng, Toán, Xác suất & Dữ liệu bảng (VOAI03-M01 -> M32)",
    "B: 39 câu Deep Learning, Tích chập CNN & Xử lý ngôn ngữ tự nhiên NLP",
    "C: 29 câu Trắc nghiệm chuyên sâu kết hợp 4 bài tự luận thiết kế hệ thống AI thực chiến"
]

e3_dist = {"A": 0, "B": 0, "C": 0, "D": 0}
for q in e3["questions"]:
    if q["type"] == "mcq":
        e3_dist[q["answer"]] += 1

print("Đề 03 Answer Distribution sau khi shuffle:", e3_dist)

with open(E3_PATH, "w", encoding="utf-8") as f:
    json.dump(e3, f, ensure_ascii=False, indent=2)

print("Đã cập nhật xong Đề 03.")
