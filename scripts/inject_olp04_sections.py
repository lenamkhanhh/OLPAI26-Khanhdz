# -*- coding: utf-8 -*-
import json
import os

SECTIONS_MAP = {
    "OLP04-Q01": "§3.8",
    "OLP04-Q02": "§4.1",
    "OLP04-Q03": "§3.1",
    "OLP04-Q04": "§7.1",
    "OLP04-Q05": "§7.2",
    "OLP04-Q06": "§7.4",
    "OLP04-Q07": "§3.5",
    "OLP04-Q08": "§2.8",
    "OLP04-Q09": "§4.6",
    "OLP04-Q10": "§1.5",
    "OLP04-Q11": "§2.4",
    "OLP04-Q12": "§4.7",
    "OLP04-Q13": "§3.6",
    "OLP04-Q14": "§7.3",
    "OLP04-Q15": "§4.4",
    "OLP04-Q16": "§4.6",
    "OLP04-Q17": "§2.4",
    "OLP04-Q18": "§3.6",
    "OLP04-Q19": "§7.3",
    "OLP04-Q20": "§7.4",
}

fpath = os.path.join("src", "data", "exams", "olp-04.json")
with open(fpath, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for q in data["questions"]:
    qid = q["id"]
    if qid in SECTIONS_MAP:
        sec = SECTIONS_MAP[qid]
        exp = q.get("explanation", "")
        if sec not in exp:
            # Thêm tham chiếu vào phần 4
            if "### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến" in exp:
                q["explanation"] = exp.replace(
                    "### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến\n",
                    f"### 4. Căn cứ từ Video bài giảng & Ứng dụng thực chiến (Tham chiếu: {sec})\n"
                )
                count += 1
            elif "### 4. Mắt xích kiến thức & Căn cứ khoa học" in exp:
                q["explanation"] = exp.replace(
                    "### 4. Mắt xích kiến thức & Căn cứ khoa học\n",
                    f"### 4. Mắt xích kiến thức & Căn cứ khoa học (Tham chiếu: {sec})\n"
                )
                count += 1

with open(fpath, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Đã bổ sung tham chiếu chuyên đề cho {count} câu hỏi tại olp-04.json")
