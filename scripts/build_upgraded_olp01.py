# -*- coding: utf-8 -*-
"""
Script scripts/build_upgraded_olp01.py
Biên soạn lại toàn bộ 64 câu hỏi của Đề 01 (olp-01.json):
1. Khôi phục 100% tiếng Việt có dấu chuẩn chỉnh (từ 02-de-luyen-olp-ai.md).
2. Xây dựng lời giải chuẩn 4 khối theo phong cách ELI5 (Giải thích cho em bé):
   - ### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé): Định nghĩa rõ thuật ngữ, hình tượng hóa.
   - ### 2. Công thức toán & Bước tính chi tiết (Step-by-Step): KaTeX chuẩn, thế số từng bước.
   - ### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls): Phân tích chi tiết từng phương án gây nhiễu.
   - ### 4. Mắt xích kiến thức & Liên hệ bài cũ: Dẫn chiếu § lý thuyết, liên kết các câu đã học.
"""

import json
import os
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
json_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-01.json")

with open(json_path, "r", encoding="utf-8") as f:
    exam_data = json.load(f)

# Bảng từ điển nâng cấp lời giải chi tiết và câu hỏi cho 64 câu của Đề 01
UPGRADES = {}

# ==========================================
# MODULE A: TOÁN & XÁC SUẤT - THỐNG KÊ (12 CÂU)
# ==========================================

UPGRADES["OLP01-A01"] = {
    "prompt": "Một căn bệnh có tỉ lệ mắc trong cộng đồng là 2%. Một xét nghiệm y tế có độ nhạy (Sensitivity) 95% và tỉ lệ dương tính giả (False Positive Rate) là 4%. Một người đi xét nghiệm và nhận kết quả Dương tính (+). Xác suất người đó thật sự mắc bệnh là bao nhiêu?",
    "options": [
        {"key": "A", "text": "95%"},
        {"key": "B", "text": "Khoảng 32.6%"},
        {"key": "C", "text": "2%"},
        {"key": "D", "text": "Khoảng 68%"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
- **Tỉ lệ nền (Base Rate / Prior):** Tỉ lệ người thật sự có bệnh trong cả cộng đồng. Ở đây là 2% (cứ 100 người thì chỉ có 2 người ốm).
- **Độ nhạy (Sensitivity):** Người có bệnh đi khám thì test phát hiện đúng bao nhiêu phần trăm (95%).
- **Dương tính giả (False Positive Rate):** Người hoàn toàn khỏe mạnh nhưng máy lại báo nhầm là có bệnh (4%).

🍼 **Hình dung thực tế cho em bé:**
Tưởng tượng trong một hội trường có **10,000 người**:
1. Có **200 người thực sự có bệnh** (2%). Máy test phát hiện đúng 95% của 200 người này $\implies 200 \\times 0.95 = 190$ người dương tính thật.
2. Có tới **9,800 người khỏe mạnh** (98%). Máy báo nhầm 4% số người khỏe này $\implies 9,800 \\times 0.04 = 392$ người khỏe bị báo dương tính oan!
3. Tổng số người cầm tờ giấy kết quả ghi chữ "DƯƠNG TÍNH" là: $190 + 392 = 582$ người.
Nhưng hãy nhìn xem: Trong 582 người nhận kết quả dương tính đó, chỉ có **190 người thực sự mang mầm bệnh**!
Xác suất thật: $\\frac{190}{582} \\approx 32.6\\%$. Tức là cầm kết quả dương tính trên tay, khả năng bạn vẫn KHỎE MẠNH lên tới gần 67.4%!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng định lý Bayes toàn phần:
$$P(\\text{Bệnh} \\mid +) = \\frac{P(+ \\mid \\text{Bệnh}) \\cdot P(\\text{Bệnh})}{P(+)}$$
Trong đó xác suất toàn phần để nhận kết quả dương tính là:
$$P(+) = P(+ \\mid \\text{Bệnh}) \\cdot P(\\text{Bệnh}) + P(+ \\mid \\text{Khỏe}) \\cdot P(\\text{Khỏe})$$
Thay số chi tiết từng bước:
- $P(\\text{Bệnh}) = 0.02 \\implies P(\\text{Khỏe}) = 1 - 0.02 = 0.98$.
- $P(+ \\mid \\text{Bệnh}) = 0.95$ (Độ nhạy).
- $P(+ \\mid \\text{Khỏe}) = 0.04$ (Tỉ lệ dương tính giả).
- Tử số: $0.95 \\times 0.02 = 0.019$.
- Mẫu số: $P(+) = (0.95 \\times 0.02) + (0.04 \\times 0.98) = 0.019 + 0.0392 = 0.0582$.
- Kết quả:
$$P(\\text{Bệnh} \\mid +) = \\frac{0.019}{0.0582} \\approx 0.32646 \\implies \\mathbf{32.6\\%}$$
Chọn đáp án **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Bẫy kinh điển (Base Rate Fallacy):**
- **Phương án A (95%):** Rất nhiều người thấy test nhạy 95% liền tưởng mình có 95% nguy cơ bệnh. Đây là sai lầm chết người vì nhầm lẫn giữa $P(+ \\mid \\text{Bệnh})$ với $P(\\text{Bệnh} \\mid +)$.
- **Phương án C (2%):** Đây chỉ là xác suất tiên nghiệm (Prior) trước khi test; test dương tính đã làm tăng khả năng bệnh từ 2% lên 32.6%.
- **Phương án D (Khoảng 68%):** Lấy $100\\% - 32.6\\%$ ra xác suất không mắc bệnh nhưng lại đánh tráo vào câu hỏi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.1 Định lý Bayes & Phân tích xác suất y tế**.
🔗 Định lý Bayes là nền tảng cốt lõi của Machine Learning: Chuyển đổi từ niềm tin ban đầu (Prior) thành niềm tin cập nhật sau khi quan sát dữ liệu (Posterior Likelihood). Ta sẽ tiếp tục gặp nguyên lý này ở câu A02 ngay sau đây!"""
}

UPGRADES["OLP01-A02"] = {
    "prompt": "Một xét nghiệm y tế có độ nhạy 99% và độ đặc hiệu 99% đối với một căn bệnh hiếm gặp (tỉ lệ mắc trong dân số chỉ là 0.1%). Vì sao khi xét nghiệm ngẫu nhiên, hầu hết những người có kết quả Dương tính (+) thực tế vẫn KHÔNG mắc bệnh?",
    "options": [
        {"key": "A", "text": "Do độ đặc hiệu của xét nghiệm còn quá thấp"},
        {"key": "B", "text": "Do độ nhạy của xét nghiệm chưa đạt 100%"},
        {"key": "C", "text": "Do tỉ lệ mắc (Base Rate) trong dân số quá nhỏ, nhóm người khỏe dương tính giả áp đảo nhóm bệnh thật"},
        {"key": "D", "text": "Do máy xét nghiệm cho kết quả hoàn toàn ngẫu nhiên"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiện tượng: Ảo tưởng tỉ lệ nền (Base Rate Fallacy).**
🍼 **Hình dung cho em bé:**
Hãy tưởng tượng một cánh đồng có **100,000 hạt đậu**, trong đó chỉ có đúng **100 hạt đậu bị mốc** (tỉ lệ 0.1%), còn lại **99,900 hạt đậu lành lặn**.
Bạn có một chiếc kính lúp siêu xịn (độ chính xác 99%):
- Soi 100 hạt mốc: Tìm đúng được 99 hạt mốc.
- Soi 99,900 hạt lành: Dù kính chỉ nhầm 1%, nhưng vì số lượng hạt lành quá khổng lồ, kính vẫn soi nhầm tới $99,900 \\times 1\\% = 999$ hạt lành thành hạt mốc!
Bây giờ, trong giỏ hạt mà kính lúp báo 'MỐC', có: 99 hạt mốc thật và tận 999 hạt lành!
Tỉ lệ mốc thật chỉ là $\\frac{99}{99 + 999} \\approx 9\\%$. Nghĩa là tới hơn 90% số hạt bị báo mốc thực ra hoàn toàn ăn ngon lành!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng công thức Bayes tương tự câu A01:
- Số ca bệnh thật được phát hiện: $N \\times P(D) \\times \\text{Sensitivity} = N \\times 0.001 \\times 0.99 = 0.00099 N$.
- Số ca khỏe bị dương tính giả: $N \\times P(\\bar{D}) \\times (1 - \\text{Specificity}) = N \\times 0.999 \\times 0.01 = 0.00999 N$.
Tỉ lệ người dương tính thật sự có bệnh:
$$P(D \\mid +) = \\frac{0.00099}{0.00099 + 0.00999} = \\frac{0.00099}{0.01098} \\approx 9.02\\%$$
Như vậy, có tới hơn $90.98\\%$ người nhận kết quả dương tính thực ra là khỏe mạnh. Nhóm dương tính giả ($0.00999N$) lớn gấp hơn 10 lần nhóm dương tính thật ($0.00099N$). Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Bẫy nhận định:**
- **Phương án A & B:** Cả độ nhạy và đặc hiệu 99% đều thuộc hàng xuất sắc nhất trong y khoa lâm sàng, không thể nói là thấp.
- **Phương án D:** Xét nghiệm hoàn toàn có cơ sở khoa học chính xác cao, không phải ngẫu nhiên.
- **Nguyên nhân cốt lõi duy nhất:** Là do số lượng người khỏe mạnh trong dân số quá áp đảo ($99.9\\%$), nên 1% sai số của nhóm người khỏe cũng đã đè bẹp 99% chính xác của nhóm người bệnh hiếm hoi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.1 Định lý Bayes & Phân tích xác suất y tế**.
🔗 **Liên hệ bài cũ:** Ở câu **OLP01-A01**, khi tỉ lệ bệnh là 2%, xác suất thật là 32.6%. Đến câu **OLP01-A02**, khi tỉ lệ bệnh chỉ còn 0.1%, xác suất thật tụt xuống còn ~9%. Điều này chứng minh: Khi bệnh càng hiếm, kết quả xét nghiệm 1 lần càng dễ bị nhiễu bởi dương tính giả!"""
}

UPGRADES["OLP01-A03"] = {
    "prompt": "Cho biến ngẫu nhiên rời rạc $X \\sim \\text{Bernoulli}(p = 0.3)$. Kỳ vọng $\\mathbb{E}[X]$ và phương sai $\\text{Var}(X)$ của biến ngẫu nhiên $X$ lần lượt là bao nhiêu?",
    "options": [
        {"key": "A", "text": "E[X] = 0.3, Var(X) = 0.21"},
        {"key": "B", "text": "E[X] = 0.5, Var(X) = 0.25"},
        {"key": "C", "text": "E[X] = 0.3, Var(X) = 0.09"},
        {"key": "D", "text": "E[X] = 0.7, Var(X) = 0.21"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ cần hiểu:**
- **Phân phối Bernoulli:** Là một phép thử chỉ có đúng 2 kết quả: Thắng (nhận giá trị 1) hoặc Thua (nhận giá trị 0).
- **Kỳ vọng (Expectation $\\mathbb{E}[X]$):** Giá trị trung bình nhận được nếu bạn chơi trò này rất nhiều lần. Nếu tỉ lệ thắng là $p$, thì trung bình bạn nhận được chính là $p$.
- **Phương sai (Variance $\\text{Var}(X)$):** Đo độ bấp bênh, độ rủi ro giữa thắng và thua. Công thức chuẩn luôn là $p \\times (1 - p)$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định nghĩa biến ngẫu nhiên Bernoulli nhận $X = 1$ với xác suất $p$, và $X = 0$ với xác suất $1 - p$:
1. Kỳ vọng:
$$\\mathbb{E}[X] = 1 \\cdot p + 0 \\cdot (1 - p) = p = 0.3$$
2. Tính $\\mathbb{E}[X^2]$:
$$\\mathbb{E}[X^2] = 1^2 \\cdot p + 0^2 \\cdot (1 - p) = p = 0.3$$
3. Phương sai:
$$\\text{Var}(X) = \\mathbb{E}[X^2] - (\\mathbb{E}[X])^2 = p - p^2 = p(1 - p) = 0.3 \\times (1 - 0.3) = 0.3 \\times 0.7 = 0.21$$
Vậy $\\mathbb{E}[X] = 0.3$ và $\\text{Var}(X) = 0.21$. Chọn đáp án **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Các bẫy công thức thường gặp:**
- **Phương án B:** Nhầm với đồng xu cân đối $p = 0.5$ (khi đó $\\text{Var} = 0.25$ đạt cực đại).
- **Phương án C:** Tính nhầm phương sai thành $p^2 = 0.3^2 = 0.09$.
- **Phương án D:** Nhầm kỳ vọng của biến cố đối $1 - p = 0.7$.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.2 Các phân phối xác suất quan trọng**.
🔗 Phân phối Bernoulli là viên gạch xây nên phân phối Nhị thức (Binomial - $n$ phép thử Bernoulli độc lập) và phân phối nhị phân trong hàm mất mát Binary Cross-Entropy (BCE) của mạng nơ-ron!"""
}

UPGRADES["OLP01-A04"] = {
    "prompt": "Tung một đồng xu cân đối và đồng chất liên tiếp 10 lần độc lập. Xác suất để cả 10 lần tung đều xuất hiện mặt sấp (S) là bao nhiêu?",
    "options": [
        {"key": "A", "text": "0.5"},
        {"key": "B", "text": "Khoảng 0.25"},
        {"key": "C", "text": "Khoảng 0.05"},
        {"key": "D", "text": "Khoảng 0.001"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Mỗi lần tung đồng xu, cơ hội ra mặt sấp chỉ là một nửa ($0.5$).
Nếu bạn muốn nó ra sấp liên tục 2 lần: Cơ hội là $\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$ (chỉ có 1 trong 4 khả năng).
Muốn ra sấp liên tục 10 lần: Giống như bạn đoán trúng liên tiếp 10 câu hỏi khó. Khả năng là siêu nhỏ, cứ khoảng **1,000 lần chơi** thì bạn mới may mắn ăn may được 1 lần!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Do 10 lần tung hoàn toàn độc lập, áp dụng quy tắc nhân xác suất cho các biến cố độc lập:
$$P(\\text{10 lần S}) = P(S_1) \\times P(S_2) \\times \\dots \\times P(S_{10}) = \\left( \\frac{1}{2} \\right)^{10}$$
Tính toán lũy thừa:
$$2^{10} = 1024 \\implies \\left( \\frac{1}{2} \\right)^{10} = \\frac{1}{1024} \\approx 0.0009765625 \\approx 0.001$$
Chọn đáp án **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A (0.5):** Chỉ là xác suất của 1 lần tung đơn lẻ.
- **Phương án B (0.25):** Là xác suất của 2 lần tung liên tiếp ($0.5^2$).
- **Phương án C (0.05):** Thường là mức ý nghĩa $\\alpha = 0.05$ trong kiểm định thống kê mà người ra đề đưa vào để bẫy thí sinh nhớ lộn số.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.2 Các phân phối xác suất quan trọng**.
🔗 Đây chính là bài toán phân phối nhị thức $X \\sim \\text{Binomial}(n=10, p=0.5)$ với số lần thành công $k=10$: $P(X=10) = C_{10}^{10} (0.5)^{10} (0.5)^0 = \\frac{1}{1024}$."""
}

UPGRADES["OLP01-A05"] = {
    "prompt": "Một tổng đài chăm sóc khách hàng nhận trung bình $\\lambda = 3$ cuộc gọi mỗi phút theo mô hình phân phối Poisson. Xác suất để trong một phút bất kỳ tổng đài KHÔNG nhận được cuộc gọi nào ($k = 0$) gần nhất với giá trị nào?",
    "options": [
        {"key": "A", "text": "0"},
        {"key": "B", "text": "Khoảng 0.05"},
        {"key": "C", "text": "Khoảng 0.5"},
        {"key": "D", "text": "Khoảng 0.95"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới: Phân phối Poisson.**
Dùng để đếm số sự kiện xảy ra ngẫu nhiên trong một khoảng thời gian cố định (như số cuộc gọi đến trong 1 phút, số tin nhắn đến trong 1 giờ).
🍼 **Hình dung cho em bé:**
Bình thường mỗi phút có trung bình 3 người gọi đến. Việc bỗng dưng suốt 1 phút im re, không có ai gọi đến ($k=0$) là một điều khá hiếm gặp, chỉ xảy ra khoảng $5\\%$ thời gian (tức cứ 20 phút thì mới có 1 phút hoàn toàn yên tĩnh).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức hàm khối xác suất của phân phối Poisson với tham số $\\lambda$:
$$P(X = k) = \\frac{e^{-\\lambda} \\cdot \\lambda^k}{k!}$$
Với bài toán này, $\\lambda = 3$ và $k = 0$:
$$P(X = 0) = \\frac{e^{-3} \\cdot 3^0}{0!} = \\frac{e^{-3} \\cdot 1}{1} = e^{-3}$$
Giá trị của hằng số $e \\approx 2.71828$:
$$e^{-3} = \\frac{1}{e^3} \\approx \\frac{1}{20.0855} \\approx 0.049787 \\approx 0.05$$
Tức xác suất khoảng **5%**. Chọn đáp án **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A (0):** Nghĩ rằng trung bình có 3 cuộc thì chắc chắn phải có người gọi, không thể bằng 0 $\\implies$ Sai bản chất ngẫu nhiên.
- **Phương án C & D:** Giá trị quá lớn, bất hợp lý vì xác suất không có cuộc gọi nào phải nhỏ hơn nhiều so với xác suất có 2-3 cuộc gọi.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.2 Các phân phối xác suất quan trọng**.
🔗 Trong thị giác máy tính và sinh ảnh, Poisson Noise (nhiễu bắn hạt / photon noise) là loại nhiễu đặc trưng của cảm biến máy ảnh khi chụp trong điều kiện thiếu sáng!"""
}

UPGRADES["OLP01-A06"] = {
    "prompt": "Theo Định lý Giới hạn Trung tâm (Central Limit Theorem — CLT), khi kích thước mẫu $n$ đủ lớn ($n \\ge 30$), giá trị trung bình mẫu $\\bar{X}$ của một biến ngẫu nhiên bất kỳ (có kỳ vọng $\\mu$ và phương sai hữu hạn $\\sigma^2$) sẽ có phân phối xấp xỉ phân phối nào?",
    "options": [
        {"key": "A", "text": "Phân phối Poisson"},
        {"key": "B", "text": "Phân phối Bernoulli"},
        {"key": "C", "text": "Phân phối chuẩn (Gaussian / Normal Distribution)"},
        {"key": "D", "text": "Phân phối đều (Uniform Distribution)"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Định lý Giới hạn Trung tâm (CLT) là phép màu kỳ diệu nhất của thống kê:**
Dù dữ liệu ban đầu của bạn có kỳ quái thế nào chăng nữa (dù là phân phối đồng xu Bernoulli, phân phối Poisson, hay phân phối méo mó bất kỳ), cứ hễ bạn gom nhiều mẫu lại (từ 30 người trở lên) rồi tính **điểm trung bình**, thì đồ thị phân bố của các điểm trung bình đó sẽ luôn luôn uốn cong thành **hình chiếc chuông cân đối hoàn hảo** — đó chính là **Phân phối Chuẩn (Normal / Gaussian)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Phát biểu toán học của CLT:
Cho các biến ngẫu nhiên $X_1, X_2, \\dots, X_n$ độc lập cùng phân phối (i.i.d) có kỳ vọng $\\mathbb{E}[X_i] = \\mu$ và phương sai $\\text{Var}(X_i) = \\sigma^2 < \\infty$.
Khi $n \\to \\infty$, biến ngẫu nhiên trung bình mẫu $\\bar{X} = \\frac{1}{n} \\sum_{i=1}^n X_i$ hội tụ theo phân phối:
$$\\bar{X} \\approx \\mathcal{N}\\left( \\mu, \\frac{\\sigma^2}{n} \\right)$$
Chuẩn hóa Z-score:
$$Z = \\frac{\\bar{X} - \\mu}{\\frac{\\sigma}{\\sqrt{n}}} \\xrightarrow{d} \\mathcal{N}(0, 1)$$
Chọn đáp án **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A, B, D:** Là các dạng phân phối gốc cụ thể của từng quan sát riêng lẻ, không bao giờ là phân phối giới hạn của trung bình mẫu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.2 & §5.3 Thống kê mô tả & Định lý giới hạn**.
🔗 CLT là lý do vì sao trong Machine Learning, hầu hết các thuật toán (từ Linear Regression, PCA, đến Batch Normalization) đều giả định các sai số hoặc đại lượng trung bình tuân theo phân phối chuẩn Gaussian!"""
}

UPGRADES["OLP01-A07"] = {
    "prompt": "Cho biến ngẫu nhiên $X$ có kỳ vọng $\\mathbb{E}[X] = 5$ và phương sai $\\text{Var}(X) = 4$. Đặt biến ngẫu nhiên $Y = 2X + 3$. Kỳ vọng $\\mathbb{E}[Y]$ và phương sai $\\text{Var}(Y)$ lần lượt là bao nhiêu?",
    "options": [
        {"key": "A", "text": "E[Y] = 13, Var(Y) = 16"},
        {"key": "B", "text": "E[Y] = 13, Var(Y) = 8"},
        {"key": "C", "text": "E[Y] = 10, Var(Y) = 16"},
        {"key": "D", "text": "E[Y] = 13, Var(Y) = 11"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
1. **Kỳ vọng (Giá trị trung bình):** Bạn nhân gấp đôi số kẹo của mọi người rồi phát thêm cho mỗi người 3 cái kẹo. Vậy số kẹo trung bình mới đương nhiên là lấy trung bình cũ nhân đôi rồi cộng 3: $5 \\times 2 + 3 = 13$.
2. **Phương sai (Độ chênh lệch/phân tán):**
- Cộng thêm cho tất cả mọi người cùng 3 cái kẹo thì sự chênh lệch khoảng cách giữa các bạn **không hề thay đổi**! (Hằng số cộng thêm có phương sai bằng 0).
- Nhưng nếu nhân gấp đôi số kẹo, khoảng cách chênh lệch bị nhân đôi, mà phương sai tính theo **bình phương** khoảng cách, nên độ phân tán sẽ bị phóng to lên gấp $2^2 = 4$ lần! $4 \\times 4 = 16$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Tính chất tuyến tính của kỳ vọng và phương sai với $Y = aX + b$:
1. $\\mathbb{E}[aX + b] = a \\cdot \\mathbb{E}[X] + b$:
$$\\mathbb{E}[Y] = 2 \\cdot \\mathbb{E}[X] + 3 = 2 \\times 5 + 3 = 13$$
2. $\\text{Var}(aX + b) = a^2 \\cdot \\text{Var}(X)$ (hằng số $b$ bị triệt tiêu vì không làm đổi độ phân tán):
$$\\text{Var}(Y) = 2^2 \\cdot \\text{Var}(X) = 4 \\times 4 = 16$$
Độ lệch chuẩn mới: $\\sigma_Y = \\sqrt{16} = 4 = |2| \\cdot \\sigma_X$.
Chọn đáp án **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Bẫy kinh điển:**
- **Phương án B:** Quên bình phương hệ số $a$, tính nhầm $\\text{Var} = 2 \\times 4 = 8$.
- **Phương án D:** Cộng cả số hạng tự do vào phương sai: $2 \\times 4 + 3 = 11$.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.3 Kỳ vọng, Phương sai & Ma trận Hiệp phương sai**.
🔗 Trong PyTorch và Deep Learning, khi ta chuẩn hóa dữ liệu $Z = \\frac{X - \\mu}{\\sigma}$ (Z-score Normalization hoặc BatchNorm), ta đang áp dụng phép biến đổi tuyến tính với $a = 1/\\sigma$ và $b = -\\mu/\\sigma$ để đưa $\\mathbb{E}[Z] = 0$ và $\\text{Var}(Z) = 1$!"""
}

UPGRADES["OLP01-A08"] = {
    "prompt": "Điểm khác biệt bản chất cốt lõi giữa phương pháp ước lượng Hợp lý cực đại (Maximum Likelihood Estimation — MLE) và Ước lượng Hậu nghiệm cực đại (Maximum A Posteriori — MAP) là gì?",
    "options": [
        {"key": "A", "text": "MLE sử dụng phân phối tiên nghiệm (Prior), còn MAP không sử dụng"},
        {"key": "B", "text": "Hai phương pháp này luôn luôn cho cùng một nghiệm tối ưu trong mọi bài toán"},
        {"key": "C", "text": "MAP chỉ dùng cho học không giám sát, còn MLE chỉ dùng cho học có giám sát"},
        {"key": "D", "text": "MAP kết hợp dữ liệu quan sát với thông tin tiên nghiệm (Prior), trong khi MLE chỉ dựa thuần túy vào dữ liệu quan sát"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Tưởng tượng bạn tìm thấy một đồng xu lạ rơi trên đường và tung 3 lần, cả 3 lần đều ra mặt Sấp:
- **MLE (Người ngây thơ, chỉ tin vào mắt mình):** Nhìn thấy 3 sấp / 3 lần, kết luận luôn đồng xu này bị yểm bùa có tỉ lệ sấp $100\\%$!
- **MAP (Người có hiểu biết đời sống - có Prior):** Dù thấy 3 lần sấp, người này vẫn bảo: 'Từ bé đến giờ các đồng xu đều có tỉ lệ 50/50. Cần thêm nhiều bằng chứng nữa chứ không thể vội vàng nói đồng xu này 100% sấp được!'
Nói cách khác: **MAP = MLE + Kinh nghiệm quá khứ (Prior)**.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 So sánh công thức toán học tối ưu hóa:
1. **MLE (Maximum Likelihood Estimation):**
Tìm tham số $\\theta$ tối đa hóa xác suất xảy ra của tập dữ liệu $D$:
$$\\hat{\\theta}_{\\text{MLE}} = \\arg\\max_\\theta P(D \\mid \\theta) = \\arg\\max_\\theta \\sum_{i=1}^N \\log P(x_i \\mid \\theta)$$
2. **MAP (Maximum A Posteriori):**
Theo định lý Bayes, tìm $\\theta$ tối đa hóa xác suất hậu nghiệm:
$$P(\\theta \\mid D) = \\frac{P(D \\mid \\theta) P(\\theta)}{P(D)} \\propto P(D \\mid \\theta) P(\\theta)$$
$$\\hat{\\theta}_{\\text{MAP}} = \\arg\\max_\\theta [\\log P(D \\mid \\theta) + \\log P(\\theta)]$$
Thành phần $\\log P(\\theta)$ chính là **phân phối tiên nghiệm (Prior)**.
Khi tiên nghiệm $P(\\theta)$ là phân phối đều (Uniform Prior - không có thông tin tiên nghiệm), thì $\\hat{\\theta}_{\\text{MAP}} \\equiv \\hat{\\theta}_{\\text{MLE}}$. Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Bị đảo ngược hoàn toàn giữa MLE và MAP.
- **Phương án B:** Chỉ trùng nhau khi Prior là phân phối đều; tổng quát nghiệm MAP và MLE khác nhau.
- **Phương án C:** Cả hai phương pháp đều dùng rộng rãi trong cả học có giám sát và không giám sát.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.4 MLE vs MAP & Mối liên hệ Regularization**.
🔗 **Mắt xích quan trọng:** Trong Machine Learning, nếu ta đặt Prior Gaussian cho trọng số $w \\sim \\mathcal{N}(0, \\sigma^2)$, MAP biến thành **Regularization L2 (Ridge Regression)**! Nếu đặt Prior Laplace, MAP biến thành **Regularization L1 (Lasso Regression)**! Ta sẽ học sâu L1/L2 ở câu C09-C10!"""
}

UPGRADES["OLP01-A09"] = {
    "prompt": "Trong kiểm định giả thuyết thống kê, ta đặt mức ý nghĩa $\\alpha = 0.05$ và thu được giá trị $p\\text{-value} = 0.03$. Kết luận khoa học chính xác nhất là gì?",
    "options": [
        {"key": "A", "text": "Chấp nhận giả thuyết không H0 vì p-value là một số rất nhỏ"},
        {"key": "B", "text": "Bác bỏ giả thuyết không H0 ở mức ý nghĩa 5% vì p-value < alpha"},
        {"key": "C", "text": "Xác suất để giả thuyết không H0 đúng là chính xác 3%"},
        {"key": "D", "text": "Kích thước hiệu ứng (Effect size) của mô hình là rất lớn"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Quy tắc vàng của kiểm định thống kê:**
- **Giả thuyết $H_0$ (Giả thuyết vô tội):** Mặc định cho rằng 'không có sự khác biệt gì cả' hoặc 'thuốc không có tác dụng'.
- **$p\\text{-value}$:** Đo xác suất 'nếu thực sự không có tác dụng, thì liệu sự khác biệt ta quan sát được có phải chỉ do ăn may/ngẫu nhiên hay không'.
- **Khẩu quyết ghi nhớ:** *'Nếu $p$ thấp hơn $\\alpha$, giả thuyết $H_0$ phải bị đuổi đi!' (If $p$ is low, $H_0$ must go).*
Ở đây $p = 0.03 < 0.05$, nghĩa là cơ hội ăn may chỉ có 3%, nhỏ hơn ngưỡng chịu đựng rủi ro 5%, nên ta đủ bằng chứng để **Bác bỏ $H_0$**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Quy tắc ra quyết định kiểm định giả thuyết thống kê:
- Nếu $p\\text{-value} \\le \\alpha$: Bác bỏ $H_0$, chấp nhận đối thuyết $H_1$ có ý nghĩa thống kê ở mức $\\alpha$.
- Nếu $p\\text{-value} > \\alpha$: Chưa đủ bằng chứng để bác bỏ $H_0$.
Vì $0.03 < 0.05$, ta kết luận: Bác bỏ $H_0$ ở mức ý nghĩa $5\\%$. Chọn đáp án **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Bẫy hiểu sai bản chất $p$-value:**
- **Phương án A:** Ngược hoàn toàn quy tắc quyết định.
- **Phương án C (Bẫy kinh điển nhất):** $p$-value KHÔNG PHẢI là xác suất $P(H_0 \\text{ đúng})$. $p$-value là xác suất dữ liệu quan sát được khi $H_0$ giả định là đúng ($P(\\text{Data} \\mid H_0)$), không phải $P(H_0 \\mid \\text{Data})$.
- **Phương án D:** $p$-value chỉ đo mức độ ý nghĩa thống kê, không đo độ lớn của hiệu ứng thực tế (Effect Size). Một mẫu cực lớn có thể cho $p < 0.001$ dù chênh lệch thực tế là không đáng kể.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.5 Kiểm định giả thuyết thống kê & A/B Testing**.
🔗 Trong đánh giá mô hình AI, A/B Testing và t-test / Wilcoxon signed-rank test được dùng để chứng minh mô hình mới thực sự vượt trội hơn baseline chứ không phải ngẫu nhiên."""
}

UPGRADES["OLP01-A10"] = {
    "prompt": "Một nghiên cứu thống kê cho thấy: Khi doanh số bán kem que tại các bãi biển tăng cao, số vụ tai nạn đuối nước cũng tăng mạnh (hệ số tương quan Pearson $r = 0.85$). Cách giải thích khoa học và hợp lý nhất cho hiện tượng này là gì?",
    "options": [
        {"key": "A", "text": "Tồn tại một biến ẩn nhiễu chung (Confounder) là thời tiết mùa hè nắng nóng làm tăng cả nhu cầu ăn kem và số người đi bơi"},
        {"key": "B", "text": "Ăn kem là nguyên nhân trực tiếp dẫn đến chuột rút và gây chết đuối"},
        {"key": "C", "text": "Số liệu thống kê chắc chắn bị sai, vì hai đại lượng này hoàn toàn độc lập"},
        {"key": "D", "text": "Chết đuối làm cho người nhà mua kem để giải tỏa tâm lý"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Chân lý nổi tiếng nhất của ngành Khoa học dữ liệu:**
**'Tương quan không đồng nghĩa với Nhân quả' (Correlation does NOT imply Causation).**
🍼 **Hình dung cho em bé:**
Vào mùa hè trời nóng bức:
- Trời nóng $\\implies$ Nhiều người mua kem ăn cho mát.
- Trời nóng $\\implies$ Hàng triệu người đổ xô ra biển tắm, dẫn đến số vụ đuối nước tăng lên.
Cái ăn kem và cái đuối nước đi cùng với nhau nhưng **kem không giết người**! Thủ phạm đứng đằng sau điều khiển cả hai việc này chính là **Thời tiết mùa hè nóng bức** — trong khoa học gọi là **Biến ẩn gây nhiễu (Confounder)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Biểu đồ nhân quả (Causal DAG):
$$\\text{Mùa hè nóng (Z - Confounder)} \\longrightarrow \\text{Doanh số kem (X)}$$
$$\\text{Mùa hè nóng (Z - Confounder)} \\longrightarrow \\text{Số vụ đuối nước (Y)}$$
Hệ số tương quan không điều kiện $\\text{Corr}(X, Y) > 0$ do dòng chảy thông tin qua ngã ba rẽ nhánh $X \\leftarrow Z \\rightarrow Y$ (Fork structure).
Khi ta kiểm soát biến mùa hè (Conditioning on $Z$):
$$\\text{Corr}(X, Y \\mid Z) \\approx 0$$
Tức là nếu chỉ xét trong những ngày có nhiệt độ cố định, việc ăn kem không hề làm tăng nguy cơ đuối nước. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B & D:** Ngộ nhận tương quan thành quan hệ nhân quả một chiều (Spurious Causality).
- **Phương án C:** Số liệu hoàn toàn có thật và tương quan rất cao, không hề sai số liệu.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.6 Tương quan vs Nhân quả & Kỹ thuật lấy mẫu**.
🔗 Trong thiết kế giải pháp AI y tế hoặc chấm điểm tín dụng, nếu không phát hiện và loại bỏ biến Confounder (như độ tuổi, giới tính, vùng miền), mô hình AI sẽ bị sai lệch nghiêm trọng (Causal Bias / Shortcut Learning)!"""
}

UPGRADES["OLP01-A11"] = {
    "prompt": "Một tập dữ liệu huấn luyện phân loại khách hàng bị mất cân bằng lớp nghiêm trọng (nhóm khách hàng gian lận chỉ chiếm 5%, nhóm bình thường chiếm 95%). Khi chia tập dữ liệu thành Train và Validation, kỹ thuật lấy mẫu nào là ĐÚNG ĐẮN NHẤT để tránh sai lệch?",
    "options": [
        {"key": "A", "text": "Lấy mẫu chỉ từ nhóm đa số để đảm bảo tính đồng nhất"},
        {"key": "B", "text": "Lấy mẫu ngẫu nhiên đơn giản (Simple Random Sampling) vì luôn đảm bảo tính khách quan"},
        {"key": "C", "text": "Lấy mẫu phân tầng (Stratified Sampling) để bảo toàn tỉ lệ 5% / 95% trong cả tập Train và Validation"},
        {"key": "D", "text": "Tăng kích thước tập Test lên gấp đôi để bù đắp sai lệch"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Trong một hộp kẹo 100 cái có **95 cái kẹo dâu** và chỉ có **5 cái kẹo sô-cô-la hiếm**.
Nếu bạn nhắm mắt bốc đại (lấy mẫu ngẫu nhiên đơn giản): Có thể bạn bốc nhầm một nắm toàn kẹo dâu, không có cái kẹo sô-cô-la nào trong tập Validation để kiểm tra!
**Lấy mẫu phân tầng (Stratified Sampling)** là hành động thông minh: Bạn chia riêng kẹo dâu và kẹo sô-cô-la thành 2 ngăn, rồi chia đều theo đúng tỉ lệ 5% và 95% vào cả hai túi Train và Test, đảm bảo túi nào cũng có đủ cả 2 loại kẹo!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Nguyên lý phân tầng (Stratification):
Cho nhãn lớp $Y \\in \\{0, 1\\}$ với tỉ lệ $P(Y=1) = p = 0.05$.
- Với Simple Random Sampling: Số mẫu dương trong tập Val có dung lượng $N_{\\text{val}}$ tuân theo phân phối nhị thức. Với $N_{\\text{val}}$ nhỏ, xác suất để fold có tỉ lệ lệch lớn là rất cao.
- Với Stratified K-Fold: Thuật toán ép chặt tỉ lệ trong mọi fold:
$$\\frac{N_{k, c}}{N_k} = \\frac{N_c}{N} = p, \\quad \\forall k=1,\\dots,K$$
Đảm bảo độ đo Precision, Recall, PR-AUC đo được trên tập Validation phản ánh chân thực năng lực của mô hình. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Bỏ nhóm thiểu số thì mô hình hoàn toàn mù tịt về gian lận.
- **Phương án B:** Lấy mẫu ngẫu nhiên đơn giản dễ làm mất trắng nhóm hiếm trong một số fold validation.
- **Phương án D:** Tăng kích thước tập test không giải quyết được vấn đề mất cân bằng tỉ lệ.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.5 K-Fold Cross-Validation & §5.6 Chiến lược lấy mẫu**.
🔗 Ta sẽ tiếp tục liên hệ kiến thức này ở câu **C08** (Stratified K-Fold) và câu **C19** (SMOTE + F1-score)!"""
}

UPGRADES["OLP01-A12"] = {
    "prompt": "Gieo đồng thời hai con xúc xắc 6 mặt cân đối và đồng chất. Xác suất để tổng số chấm xuất hiện trên hai mặt ngửa bằng 9 là bao nhiêu?",
    "options": [
        {"key": "A", "text": "1/6"},
        {"key": "B", "text": "5/36"},
        {"key": "C", "text": "1/12"},
        {"key": "D", "text": "1/9"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Hai con xúc xắc gieo xuống có tất cả $6 \\times 6 = 36$ khả năng khác nhau có thể xảy ra.
Bây giờ bé hãy đếm xem có mấy cặp số cộng lại bằng 9 nhé:
- Con xúc xắc thứ nhất ra 3, con thứ hai ra 6: $(3, 6)$ $\\implies$ Tổng là 9.
- Con xúc xắc thứ nhất ra 4, con thứ hai ra 5: $(4, 5)$ $\\implies$ Tổng là 9.
- Con xúc xắc thứ nhất ra 5, con thứ hai ra 4: $(5, 4)$ $\\implies$ Tổng là 9.
- Con xúc xắc thứ nhất ra 6, con thứ hai ra 3: $(6, 3)$ $\\implies$ Tổng là 9.
Chỉ có đúng **4 cặp may mắn** như vậy trên tổng số 36 khả năng.
Rút gọn phân số: $\\frac{4}{36} = \\frac{1}{9}$!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Không gian mẫu:
$$|\\Omega| = 6 \\times 6 = 36$$
Tập các kết quả thuận lợi cho biến cố $A$: 'Tổng hai xúc xắc bằng 9':
$$A = \\{(3, 6), (4, 5), (5, 4), (6, 3)\\}$$
Số phần tử: $|A| = 4$.
Xác suất cổ điển:
$$P(A) = \\frac{|A|}{|\\Omega|} = \\frac{4}{36} = \\frac{1}{9} \\approx 0.1111$$
Chọn đáp án **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Bẫy hay gặp:**
- **Phương án A (1/6):** Là xác suất tổng bằng 7 (có 6 cặp: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) $\\implies 6/36 = 1/6$).
- **Phương án B (5/36):** Là xác suất tổng bằng 8 (có 5 cặp: (2,6), (3,5), (4,4), (5,3), (6,2)).
- **Phương án C (1/12):** Quên tính các hoán vị (chỉ đếm (3,6) và (4,5) ra 2/36 = 1/18 hoặc 3/36 = 1/12).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§5.1 Không gian mẫu & Xác suất cổ điển**.
🔗 Đếm không gian mẫu và phân phối tổng của hai biến ngẫu nhiên rời rạc là bước khởi đầu để hiểu về tích chập xác suất (Convolution of Probability Distributions) trong lý thuyết thống kê!"""
}

# ==========================================
# MODULE B: PYTHON / NUMPY / TÍNH TAY (18 CÂU)
# ==========================================

UPGRADES["OLP01-B01"] = {
    "prompt": "Một ảnh đầu vào có kích thước không gian $32 \\times 32$ được đưa qua một tầng tích chập Conv2D với kích thước kernel $K = 3 \\times 3$, bước trượt (stride) $S = 1$, và chèn đệm (padding) $P = 1$. Kích thước không gian của tensor đầu ra (Output shape) là bao nhiêu?",
    "options": [
        {"key": "A", "text": "32 x 32"},
        {"key": "B", "text": "30 x 30"},
        {"key": "C", "text": "16 x 16"},
        {"key": "D", "text": "34 x 34"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Kỹ thuật 'Same Padding' trong mạng CNN:**
- Khi bạn quét một chiếc kính lúp kích thước $3 \\times 3$ qua một bức ảnh, các pixel ở mép ngoài cùng sẽ bị thiếu hàng xóm, làm ảnh bị co nhỏ lại mỗi chiều 2 pixel (từ 32 tụt xuống 30).
- Để giữ nguyên kích thước ảnh ban đầu, người ta viền thêm một lớp số 0 xung quanh ảnh (chèn đệm $P = 1$). Bức ảnh tạm thời to lên thành $34 \\times 34$, sau khi quét kính lúp $3 \\times 3$ xong thì kích thước đầu ra vừa khít quay về đúng **32 x 32**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức chuẩn tính kích thước không gian đầu ra tầng Conv2D:
$$O = \\left\\lfloor \\frac{W - K + 2P}{S} \\right\\rfloor + 1$$
Thay các tham số vào công thức:
- Chiều rộng ảnh vào: $W = 32$.
- Kích thước kernel: $K = 3$.
- Chèn viền: $P = 1$.
- Bước trượt: $S = 1$.
Từng bước tính toán:
$$O = \\left\\lfloor \\frac{32 - 3 + 2(1)}{1} \\right\\rfloor + 1 = \\left\\lfloor \\frac{31}{1} \\right\\rfloor + 1 = 31 + 1 = 32$$
Vì ảnh vuông nên chiều cao và chiều rộng cùng bằng 32. Kích thước output là **32 x 32**. Chọn **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B (30 x 30):** Quên cộng padding $P=1$ (tính theo kiểu Valid Padding $32 - 3 + 1 = 30$).
- **Phương án C (16 x 16):** Nhầm bước trượt Stride $S = 2$ hoặc nhầm sang tầng MaxPool2D(2, 2).
- **Phương án D (34 x 34):** Cộng padding 2 lần nhưng quên trừ đi kích thước kernel.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến trúc CNN & Công thức kích thước tensor**.
🔗 Đây là cấu hình tích chập kinh điển của mạng **VGGNet** (Kernel 3x3, Pad 1, Stride 1) giúp giữ nguyên kích thước không gian để trích xuất đặc trưng sâu mà không làm mất thông tin mép! Tiếp theo ở câu B02, ta sẽ thử trường hợp không có padding!"""
}

UPGRADES["OLP01-B02"] = {
    "prompt": "Một ảnh đầu vào có kích thước $28 \\times 28$ (ảnh chữ số MNIST) được đưa qua một tầng tích chập Conv2D với kernel $K = 5 \\times 5$, bước trượt $S = 1$, và không sử dụng padding ($P = 0$, valid padding). Kích thước không gian của tensor đầu ra là bao nhiêu?",
    "options": [
        {"key": "A", "text": "28 x 28"},
        {"key": "B", "text": "24 x 24"},
        {"key": "C", "text": "14 x 14"},
        {"key": "D", "text": "23 x 23"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hình dung cho em bé:**
Lần này chúng ta không viền số 0 (không có padding).
Một chiếc cửa sổ kích thước $5$ ô trượt trên chiếc thước dài $28$ ô:
Vị trí đầu tiên chiếc cửa sổ chiếm từ ô 1 đến ô 5. Chiếc cửa sổ chỉ có thể trượt sang phải thêm $28 - 5 = 23$ bước nữa.
Cộng thêm vị trí ban đầu nữa là tổng cộng có $23 + 1 = 24$ vị trí cửa sổ có thể dừng lại!
Vậy ảnh đầu ra sẽ bị thu nhỏ thành **24 x 24**.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng công thức chuẩn đã học từ câu B01:
$$O = \\left\\lfloor \\frac{W - K + 2P}{S} \\right\\rfloor + 1$$
Thay số với $W = 28$, $K = 5$, $P = 0$, $S = 1$:
$$O = \\left\\lfloor \\frac{28 - 5 + 0}{1} \\right\\rfloor + 1 = 23 + 1 = 24$$
Output tensor có kích thước **24 x 24**. Chọn đáp án **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A (28 x 28):** Nhầm rằng mọi lớp tích chập đều giữ nguyên kích thước ảnh (quên rằng không có padding).
- **Phương án C (14 x 14):** Nhầm với phép Pooling giảm nửa kích thước.
- **Phương án D (23 x 23):** Lỗi quên cộng 1 (Off-by-one error: lấy $28 - 5 = 23$).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§3.1 Kiến trúc CNN & Công thức kích thước tensor**.
🔗 **Liên hệ bài cũ:** So sánh với câu **OLP01-B01**:
- Ở B01 có padding $P=1$ nên kích thước được bảo toàn ($32 \\to 32$).
- Ở B02 không có padding ($P=0$) nên mỗi chiều bị co lại đúng $K - 1 = 5 - 1 = 4$ pixel ($28 \\to 24$). Đây chính là tầng Conv1 của mạng **LeNet-5** kinh điển!"""
}

UPGRADES["OLP01-B03"] = {
    "prompt": "Một ảnh đầu vào kích thước $224 \\times 224$ (chuẩn ImageNet) được đưa qua tầng Conv2D đầu tiên với kích thước kernel $K = 7 \\times 7$, bước trượt $S = 2$, và padding $P = 3$. Kích thước không gian của tensor đầu ra là bao nhiêu?",
    "options": [
        {"key": "A", "text": "224 x 224"},
        {"key": "B", "text": "111 x 111"},
        {"key": "C", "text": "112 x 112"},
        {"key": "D", "text": "56 x 56"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Tầng mở màn kinh điển của ResNet-50:**
Các bức ảnh chụp thực tế rất lớn ($224 \\times 224$). Ở tầng đầu tiên, mạng muốn giảm nhanh kích thước ảnh xuống một nửa để tiết kiệm bộ nhớ và tính toán nhanh hơn.
Vì thế, người ta dùng bước nhảy $S = 2$ (mỗi lần trượt nhảy cóc 2 bước), đồng thời chọn $K = 7$ và $P = 3$ để kích thước ảnh giảm chính xác một nửa thành **112 x 112**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Áp dụng công thức tính kích thước:
$$O = \\left\\lfloor \\frac{W - K + 2P}{S} \\right\\rfloor + 1$$
Thay số: $W = 224, K = 7, P = 3, S = 2$:
1. Tính tử số: $W - K + 2P = 224 - 7 + 2(3) = 224 - 7 + 6 = 223$.
2. Chia cho stride $S = 2$: $\\frac{223}{2} = 111.5$.
3. Lấy hàm sàn (Floor): $\\lfloor 111.5 \\rfloor = 111$.
4. Cộng thêm 1: $111 + 1 = 112$.
Vậy kích thước tensor đầu ra là **112 x 112**. Chọn đáp án **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Bẫy hay gặp:**
- **Phương án B (111 x 111):** Tính phép chia lấy sàn ra 111 nhưng quên cộng thêm 1.
- **Phương án D (56 x 56):** Nhầm kích thước sau khi đi qua tiếp tầng MaxPool2D(3, stride 2, pad 1) kế tiếp.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§3.1 & §3.3 Kiến trúc ResNet**.
🔗 **Bộ ba câu hỏi Conv2D:**
- B01: Stride 1, Pad Same ($32 \\to 32$)
- B02: Stride 1, Pad Valid ($28 \\to 24$)
- B03: Stride 2, Giảm một nửa ($224 \\to 112$)
Nắm vững bộ 3 câu này là bạn làm chủ 100% các câu hỏi về kích thước layer trong đề thi!"""
}

UPGRADES["OLP01-B04"] = {
    "prompt": "Một nút (node) trong cây quyết định đang chứa 8 mẫu dữ liệu, gồm 4 mẫu thuộc lớp Đỏ và 4 mẫu thuộc lớp Xanh. Độ hỗn loạn thông tin Shannon Entropy của nút này là bao nhiêu?",
    "options": [
        {"key": "A", "text": "0 bit"},
        {"key": "B", "text": "0.5 bit"},
        {"key": "C", "text": "2 bit"},
        {"key": "D", "text": "1 bit"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới: Shannon Entropy.**
- **Entropy:** Là đại lượng đo 'độ bất định, độ hỗn loạn, không biết đằng nào mà lần'.
🍼 **Hình dung cho em bé:**
Nếu một hộp có 8 quả bóng, bạn nhắm mắt thò tay vào bốc:
- Nếu cả 8 quả đều màu Đỏ (100% chắc chắn): Bạn không hề bối rối chút nào, độ bất định bằng 0 ($Entropy = 0$).
- Nhưng ở đây có **4 quả Đỏ và 4 quả Xanh** (cân bằng 50% - 50%): Đây là trạng thái bất định và khó đoán nhất! Trong lý thuyết thông tin với cơ số 2, độ bất định cực đại của 2 lựa chọn tương đương đúng **1 bit** thông tin!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Shannon Entropy (dùng $\\log_2$, đơn vị bit):
$$H(S) = - \\sum_{i=1}^C p_i \\log_2(p_i)$$
Ở đây có $C = 2$ lớp (Đỏ và Xanh):
- Xác suất lớp Đỏ: $p_1 = \\frac{4}{8} = 0.5$.
- Xác suất lớp Xanh: $p_2 = \\frac{4}{8} = 0.5$.
Thay vào công thức:
$$H(S) = - [0.5 \\log_2(0.5) + 0.5 \\log_2(0.5)]$$
Ta có $\\log_2(0.5) = \\log_2(2^{-1}) = -1$:
$$H(S) = - [0.5 \\times (-1) + 0.5 \\times (-1)] = - [-0.5 - 0.5] = - (-1) = 1 \\text{ bit}$$
Chọn đáp án **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A (0 bit):** Chỉ xảy ra khi node thuần khiết (Pure node - 100% cùng 1 lớp).
- **Phương án B (0.5 bit):** Nhầm với chỉ số Gini Impurity ($Gini = 1 - (0.5^2 + 0.5^2) = 0.5$).
- **Phương án C (2 bit):** Nhầm cơ số hoặc tính sai log.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định & Shannon Entropy**.
🔗 Thuật toán **ID3** dùng Entropy làm thước đo. Ở câu tiếp theo **B05**, ta sẽ dùng kết quả Entropy này để tính Mức tăng thông tin (Information Gain) khi phân chia node!"""
}

UPGRADES["OLP01-B05"] = {
    "prompt": "Từ nút ban đầu ở câu B04 (Entropy = 1 bit), ta phân chia dữ liệu theo một đặc trưng và thu được 2 nút lá: Nút trái chứa toàn bộ 4 mẫu Đỏ, Nút phải chứa toàn bộ 4 mẫu Xanh. Mức tăng thông tin (Information Gain — ID3) của phép phân chia này là bao nhiêu?",
    "options": [
        {"key": "A", "text": "1 bit (Tối đa)"},
        {"key": "B", "text": "0.5 bit"},
        {"key": "C", "text": "0 bit"},
        {"key": "D", "text": "0.25 bit"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Mức tăng thông tin (Information Gain):**
Là phần hỗn loạn bị triệt tiêu sau khi phân chia:
$$\\text{Mức tăng thông tin} = (\\text{Độ hỗn loạn ban đầu}) - (\\text{Độ hỗn loạn còn lại sau khi chia})$$
🍼 **Hình dung cho em bé:**
Ban đầu cả hộp lẫn lộn lung tung ($Entropy = 1$ bit). Sau khi bạn chia xong:
- Nút trái 100% màu Đỏ $\\implies$ Sạch sẽ tinh tươm, không còn chút bất định nào ($Entropy = 0$).
- Nút phải 100% màu Xanh $\\implies$ Sạch sẽ tinh tươm, không còn chút bất định nào ($Entropy = 0$).
Tất cả sự hỗn loạn đã biến mất hoàn toàn! Bạn đã thu được trọn vẹn $1 - 0 = 1$ bit thông tin (mức hoàn hảo tối đa)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Information Gain của thuộc tính $A$:
$$IG(S, A) = H(S) - \\sum_{v \\in \\text{Values}(A)} \\frac{|S_v|}{|S|} H(S_v)$$
Theo câu B04: $H(S) = 1$ bit.
Tính Entropy hai nút con:
- Nút trái $S_{\\text{left}}$ (4 đỏ, 0 xanh): $p_1 = 1, p_2 = 0 \\implies H(S_{\\text{left}}) = - (1 \\log_2 1 + 0) = 0$ bit.
- Nút phải $S_{\\text{right}}$ (0 đỏ, 4 xanh): $p_1 = 0, p_2 = 1 \\implies H(S_{\\text{right}}) = 0$ bit.
Entropy có trọng số của các nút con:
$$H_{\\text{after}} = \\frac{4}{8} \\times 0 + \\frac{4}{8} \\times 0 = 0 \\text{ bit}$$
Mức tăng thông tin:
$$IG(S, A) = 1 - 0 = 1 \\text{ bit}$$
Chọn đáp án **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án C (0 bit):** Chỉ xảy ra khi phép phân chia hoàn toàn vô dụng, tỉ lệ các lớp ở các nút con không hề thay đổi so với nút cha.
- **Phương án B & D:** Tính sai trọng số trung bình của các nút con.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.3 Cây quyết định & Information Gain**.
🔗 **Liên hệ bài cũ:**
- Câu **B04**: Đo độ bẩn/hỗn loạn của phòng ban đầu ($H = 1$).
- Câu **B05**: Đo công sức dọn dẹp sạch sẽ căn phòng ($IG = 1$). Thuật toán cây quyết định luôn chọn thuộc tính có $IG$ lớn nhất để làm tiêu chuẩn rẽ nhánh!"""
}

UPGRADES["OLP01-B06"] = {
    "prompt": "Cho bounding box dự đoán $B_p$ và bounding box nhãn thực tế $B_g$ có diện tích phần giao nhau (Intersection) là 30 pixel vuông, và diện tích phần hợp (Union) là 120 pixel vuông. Chỉ số IoU (Intersection over Union) bằng bao nhiêu và mô hình có được tính là phát hiện đúng theo ngưỡng tiêu chuẩn $\\text{IoU} \\ge 0.5$ hay không?",
    "options": [
        {"key": "A", "text": "IoU = 0.5, Đạt chuẩn phát hiện đúng"},
        {"key": "B", "text": "IoU = 0.25, Không đạt chuẩn phát hiện đúng (< 0.5)"},
        {"key": "C", "text": "IoU = 0.2, Không đạt chuẩn"},
        {"key": "D", "text": "IoU = 0.75, Đạt chuẩn phát hiện đúng"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Chỉ số IoU (Intersection over Union) trong phát hiện vật thể (Object Detection):**
Tưởng tượng bạn vẽ một chiếc khung viền quanh con mèo trong ảnh ($B_p$), còn cô giáo đã vẽ sẵn một chiếc khung chuẩn ($B_g$).
- **Phần Giao (Intersection):** Là diện tích hai chiếc khung đè chồng khít lên nhau (30).
- **Phần Hợp (Union):** Là tổng diện tích bao trùm của cả hai chiếc khung gộp lại (120).
- **Tỉ số IoU:** Lấy phần trùng chia cho phần tổng: $\\frac{30}{120} = \\frac{1}{4} = 0.25$ (chỉ trùng nhau được 25%).
Vì $0.25 < 0.5$, khung bạn vẽ bị lệch quá nhiều so với con mèo, máy chấm thi sẽ phạt đây là một dự đoán **SAI (False Positive)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức tính chỉ số IoU:
$$\\text{IoU} = \\frac{\\text{Area}(B_p \\cap B_g)}{\\text{Area}(B_p \\cup B_g)}$$
Thay số:
$$\\text{IoU} = \\frac{30}{120} = \\frac{1}{4} = 0.25$$
So sánh với ngưỡng đánh giá chuẩn trong PASCAL VOC / COCO ($threshold = 0.5$):
$$\\text{IoU} = 0.25 < 0.5 \\implies \\text{Không đạt (False Positive)}$$
Chọn đáp án **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Nhầm $30/120$ thành $0.5$ hoặc tưởng lấy diện tích giao chia cho cái gì khác.
- **Phương án C:** Nhầm mẫu số thành $30 + 120 = 150 \\implies 30/150 = 0.2$. Cần nhớ Union đã bao gồm cả Intersection rồi, không được cộng thêm lần nữa!
- **Phương án D:** Lấy $1 - 0.25 = 0.75$.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§3.6 Phát hiện vật thể & Chỉ số IoU**.
🔗 IoU là trái tim của bài toán Object Detection: Nó dùng để xác định nhãn True Positive khi tính mAP, và làm tiêu chí triệt tiêu khung trùng lặp trong thuật toán **NMS (Non-Maximum Suppression)** ở câu C15!"""
}

UPGRADES["OLP01-B07"] = {
    "prompt": "Một mô hình phân loại nhị phân dự đoán trên 200 bệnh nhân cho ra ma trận nhầm lẫn (Confusion Matrix): $TP = 80$, $FP = 20$, $FN = 40$, $TN = 60$. Độ chính xác dự đoán (Precision) và Độ bao phủ (Recall) của mô hình lần lượt là bao nhiêu?",
    "options": [
        {"key": "A", "text": "Precision = 0.667, Recall = 0.800"},
        {"key": "B", "text": "Precision = 0.800, Recall = 0.571"},
        {"key": "C", "text": "Precision = 0.800, Recall = 0.667"},
        {"key": "D", "text": "Precision = 0.750, Recall = 0.667"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Phân biệt Precision và Recall cực dễ nhớ:**
- **Precision (Đoán trúng bao nhiêu):** Trong tất cả những người mà máy **bảo là có bệnh** ($TP + FP = 80 + 20 = 100$ người), thì thực sự có bao nhiêu người bị bệnh thật? $\\implies \\frac{80}{100} = 80\\%$ ($0.80$).
- **Recall (Bắt được bao nhiêu / Không bỏ sót):** Trong tất cả những người **thực sự mang mầm bệnh ngoài đời** ($TP + FN = 80 + 40 = 120$ người), máy đã bắt trúng được bao nhiêu người? $\\implies \\frac{80}{120} \\approx 66.7\\%$ ($0.667$).

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức tính các độ đo:
1. Precision (Độ xác thực):
$$\\text{Precision} = \\frac{TP}{TP + FP} = \\frac{80}{80 + 20} = \\frac{80}{100} = 0.800 \\quad (80\\%)$$
2. Recall (Độ bao phủ / Sensitivity):
$$\\text{Recall} = \\frac{TP}{TP + FN} = \\frac{80}{80 + 40} = \\frac{80}{120} = \\frac{2}{3} \\approx 0.667 \\quad (66.7\\%)$$
Chọn đáp án **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Bẫy kinh điển:**
- **Phương án A:** Bị đảo ngược vị trí giữa Precision và Recall.
- **Phương án B:** Mẫu số của Recall lấy nhầm thành $TP + FP + FN = 140 \\implies 80/140 = 0.571$.
- **Phương án D:** Tính nhầm mẫu số Precision.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.7 Các độ đo đánh giá mô hình**.
🔗 Ngay ở câu tiếp theo **B08**, ta sẽ kết hợp Precision = 0.8 và Recall = 0.667 này để tính F1-Score (Trung bình điều hòa)!"""
}

UPGRADES["OLP01-B08"] = {
    "prompt": "Từ kết quả của mô hình ở câu B07 (Precision $P = 0.8$, Recall $R = 0.667 \\approx 2/3$), chỉ số F1-Score (trung bình điều hòa giữa Precision và Recall) của mô hình là bao nhiêu?",
    "options": [
        {"key": "A", "text": "Khoảng 0.733"},
        {"key": "B", "text": "0.800"},
        {"key": "C", "text": "0.667"},
        {"key": "D", "text": "Khoảng 0.727"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Vì sao không dùng trung bình cộng mà phải dùng Trung bình điều hòa (Harmonic Mean)?**
Nếu bạn dùng trung bình cộng: Một mô hình đoán mò có Precision = 1.0 nhưng Recall = 0.0 (không bắt được ai) vẫn được $0.5$ điểm — điều đó là gian lận!
**F1-Score (Trung bình điều hòa)** có tính chất trừng phạt thẳng tay nếu một trong hai chỉ số bị kém. F1-score sẽ luôn bị kéo về phía con số nhỏ hơn.
Ở đây trung bình cộng là $\\frac{0.8 + 0.667}{2} = 0.7335$, nhưng F1-score thật phải thấp hơn con số này một chút $\\implies$ Khoảng **0.727**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức F1-Score:
$$F_1 = 2 \\cdot \\frac{\\text{Precision} \\cdot \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2 \\cdot TP}{2 \\cdot TP + FP + FN}$$
Cách 1: Dùng phân số chính xác với $P = 4/5$ và $R = 2/3$:
$$F_1 = 2 \\cdot \\frac{\\frac{4}{5} \\cdot \\frac{2}{3}}{\\frac{4}{5} + \\frac{2}{3}} = 2 \\cdot \\frac{\\frac{8}{15}}{\\frac{12 + 10}{15}} = 2 \\cdot \\frac{\\frac{8}{15}}{\\frac{22}{15}} = 2 \\cdot \\frac{8}{22} = \\frac{16}{22} = \\frac{8}{11} \\approx 0.72727 \\implies 0.727$$
Cách 2: Tính trực tiếp từ TP, FP, FN:
$$F_1 = \\frac{2 \\times 80}{2 \\times 80 + 20 + 40} = \\frac{160}{160 + 60} = \\frac{160}{220} = \\frac{8}{11} \\approx 0.727$$
Chọn đáp án **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A (0.733):** Tính nhầm theo trung bình cộng số học $\\frac{0.8 + 0.667}{2} = 0.733$.
- **Phương án B & C:** Chọn giá trị cực trị của Precision hoặc Recall.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.7 Các độ đo đánh giá mô hình**.
🔗 **Mắt xích liên kết:**
- Câu B07: Tính Precision (0.8) và Recall (0.667).
- Câu B08: Ghép thành F1-score (0.727).
F1-score là metric bắt buộc khi dữ liệu bị mất cân bằng lớp (như ở câu A11 và câu C19)!"""
}

UPGRADES["OLP01-B09"] = {
    "prompt": "Cho hai vector đặc trưng (embeddings) trong không gian 2 chiều: $\\mathbf{u} = [1, 1]$ và $\\mathbf{v} = [0, 2]$. Độ tương đồng Cosine (Cosine Similarity) giữa hai vector này là bao nhiêu?",
    "options": [
        {"key": "A", "text": "Khoảng 0.707 (căn 2 chia 2)"},
        {"key": "B", "text": "0.0"},
        {"key": "C", "text": "1.0"},
        {"key": "D", "text": "0.5"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Cosine Similarity (Đo góc chỉ hướng):**
Độ tương đồng Cosine không quan tâm hai mũi tên dài hay ngắn, nó chỉ quan tâm **hai mũi tên có chỉ về cùng một hướng hay không**.
- Vector $\\mathbf{u} = [1, 1]$ nằm ở góc $45^\\circ$ (chỉ hướng Đông Bắc).
- Vector $\\mathbf{v} = [0, 2]$ nằm thẳng đứng ở trục Y, góc $90^\\circ$ (chỉ hướng Bắc).
Góc lệch giữa hai mũi tên là $90^\\circ - 45^\\circ = 45^\\circ$.
Cosine của góc $45^\\circ$ bằng $\\frac{\\sqrt{2}}{2} \\approx 0.7071$!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Công thức Cosine Similarity giữa hai vector:
$$\\cos(\\theta) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\|_2 \\|\\mathbf{v}\\|_2} = \\frac{\\sum_{i} u_i v_i}{\\sqrt{\\sum_{i} u_i^2} \\sqrt{\\sum_{i} v_i^2}}$$
1. Tích vô hướng (Dot Product):
$$\\mathbf{u} \\cdot \\mathbf{v} = (1 \\times 0) + (1 \\times 2) = 0 + 2 = 2$$
2. Độ dài chuẩn L2 của từng vector:
$$\\|\\mathbf{u}\\|_2 = \\sqrt{1^2 + 1^2} = \\sqrt{2}$$
$$\\|\\mathbf{v}\\|_2 = \\sqrt{0^2 + 2^2} = \\sqrt{4} = 2$$
3. Tích độ dài: $\\|\\mathbf{u}\\|_2 \\|\\mathbf{v}\\|_2 = 2\\sqrt{2}$.
4. Cosine Similarity:
$$\\cos(\\theta) = \\frac{2}{2\\sqrt{2}} = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2} \\approx 0.7071$$
Chọn đáp án **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B (0.0):** Nhầm rằng hai vector trực giao vuông góc nhau.
- **Phương án C (1.0):** Nhầm rằng hai vector cùng phương.
- **Phương án D (0.5):** Tính nhầm giá trị $\\cos(60^\\circ)$.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§4.3 Vector Embeddings & Cosine Similarity**.
🔗 Cosine Similarity là thước đo khoảng cách số 1 trong các hệ thống tìm kiếm ngữ nghĩa (Semantic Search), RAG (Retrieval-Augmented Generation), và so khớp khuôn mặt (FaceNet / ArcFace)!"""
}

UPGRADES["OLP01-B10"] = {
    "prompt": "Trong thiết kế khối mạng nơ-ron tích chập (Conv Block) hoặc tầng kết nối đầy đủ (Dense Block) hiện đại trong PyTorch, thứ tự chuẩn mực kinh điển của các lớp là gì?",
    "options": [
        {"key": "A", "text": "Linear/Conv -> ReLU (Activation) -> BatchNorm"},
        {"key": "B", "text": "Linear/Conv -> BatchNorm -> ReLU (Activation)"},
        {"key": "C", "text": "BatchNorm -> Linear/Conv -> ReLU"},
        {"key": "D", "text": "ReLU -> Linear/Conv -> BatchNorm"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Quy tắc làm đẹp dữ liệu trước khi cắt gọt:**
Tưởng tượng quy trình làm tượng gỗ:
1. **Linear / Conv (Đẽo gọt thô):** Bạn nhân trọng số để biến đổi dữ liệu.
2. **BatchNorm (Cân bằng & Chuẩn hóa):** Sau khi biến đổi, các con số có thể bị văng ra quá to hoặc quá nhỏ. Bạn phải gom chúng về trung bình 0 và phương sai 1 để ổn định dòng chảy thông tin.
3. **ReLU (Kích hoạt phi tuyến):** Sau khi dữ liệu đã chuẩn chỉnh quanh số 0, bạn mới dùng hàm ReLU để cắt bỏ phần âm ($< 0$), giữ lại phần dương.
Thứ tự vàng luôn là: **Tính toán $\\implies$ Chuẩn hóa $\\implies$ Phi tuyến (Linear -> BN -> Activation)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Theo bài báo gốc của Ioffe & Szegedy (2015) 'Batch Normalization':
Batch Normalization được áp dụng trên giá trị tiền kích hoạt (Pre-activation) $x = W u + b$:
$$y = \\text{Activation}(\\text{BN}(W u))$$
- Chú ý: Khi dùng BatchNorm ngay sau Linear/Conv, ta đặt `bias=False` vì BatchNorm đã có tham số dịch chuyển $\\beta$ riêng, bias của Linear sẽ bị khử hoàn toàn:
```python
nn.Sequential(
    nn.Conv2d(in_c, out_c, kernel_size=3, padding=1, bias=False),
    nn.BatchNorm2d(out_c),
    nn.ReLU(inplace=True)
)
```
Chọn đáp án **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Đưa BatchNorm ra sau ReLU sẽ làm mất tác dụng của hàm chuẩn hóa đối với phân phối có phần âm, và phân phối sau ReLU bị chặt cụt tại 0 khiến BatchNorm hoạt động kém hiệu quả hơn.
- **Phương án C & D:** Đặt sai thứ tự logic của mạng nơ-ron.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.8 Kỹ thuật Chuẩn hóa (BatchNorm, LayerNorm)**.
🔗 Hãy nhớ: BatchNorm chuẩn hóa theo chiều Batch (hợp cho ảnh - CNN), còn LayerNorm chuẩn hóa theo chiều Feature (hợp cho văn bản - Transformer) như ta sẽ gặp ở câu C21!"""
}

UPGRADES["OLP01-B11"] = {
    "prompt": "Khi sử dụng hàm mất mát `torch.nn.CrossEntropyLoss()` trong PyTorch cho bài toán phân loại đa lớp, đầu vào mô hình đưa vào hàm mất mát này phải ở dạng nào?",
    "options": [
        {"key": "A", "text": "Xác suất đã qua hàm `torch.softmax()`"},
        {"key": "B", "text": "Nhãn dạng One-hot vector"},
        {"key": "C", "text": "Các giá trị Logits thô chưa qua hàm kích hoạt Softmax"},
        {"key": "D", "text": "Giá trị xác suất đã lấy log tự nhiên bằng `torch.log()`"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bẫy số học 'Hai lần Softmax' trong PyTorch:**
Trong PyTorch, hàm `nn.CrossEntropyLoss()` đã được các kỹ sư tích hợp sẵn hàm Softmax bên trong bụng nó rồi!
Nếu bạn tự tiện gắn thêm một tầng `nn.Softmax()` ở cuối mô hình rồi mới ném vào `CrossEntropyLoss`, mô hình của bạn sẽ bị ép Softmax **2 lần liên tiếp**! Điều này làm hỏng toàn bộ gradient và khiến mạng học cực kỳ chậm hoặc sai lệch.
Quy tắc: Tầng cuối cùng của mô hình chỉ cần xuất ra điểm số thô (**Logits**) là đủ!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Lý do kỹ thuật: Tính ổn định số học (Numerical Stability).
Trong toán học:
$$\\mathcal{L}_{\\text{CE}} = - \\log(\\text{softmax}(z_c)) = - \\log\\left( \\frac{e^{z_c}}{\\sum_j e^{z_j}} \\right) = - z_c + \\log\\left( \\sum_j e^{z_j} \\right)$$
Phép toán $\\log(\\sum e^z)$ được PyTorch cài đặt bằng hàm `LogSumExp` nội bộ với kỹ thuật trừ giá trị cực đại $\\max(z)$ để chống tràn số (Overflow/Underflow):
$$\\text{LogSumExp}(z) = m + \\log\\left( \\sum_j e^{z_j - m} \\right), \\quad m = \\max_j(z_j)$$
Do đó, `nn.CrossEntropyLoss()` yêu cầu input trực tiếp là **Logits thô**. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Sai lầm phổ biến nhất của người mới học PyTorch: Thêm `F.softmax` vào output của `forward()` trước khi truyền vào CrossEntropyLoss.
- **Phương án B:** Trong PyTorch, nhãn mục tiêu `target` của CrossEntropyLoss mặc định là tensor chứa chỉ số lớp dạng số nguyên `LongTensor` (Class indices $0, 1, \\dots, C-1$), không cần one-hot.
- **Phương án D:** Nếu đã qua `log_softmax`, hàm mất mát tương ứng phải là `nn.NLLLoss()` (Negative Log Likelihood Loss).

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát trong Deep Learning**.
🔗 Tương tự đối với bài toán nhị phân, ở câu **B12** ngay sau đây, ta sẽ thấy hàm `nn.BCEWithLogitsLoss()` cũng nhận trực tiếp Logits thô thay vì nhận xác suất sau Sigmoid!"""
}

UPGRADES["OLP01-B12"] = {
    "prompt": "Trong PyTorch, khi giải bài toán phân loại nhị phân (Binary Classification), vì sao lập trình viên luôn được khuyến nghị sử dụng `torch.nn.BCEWithLogitsLoss()` thay vì kết hợp `torch.sigmoid()` với `torch.nn.BCELoss()`?",
    "options": [
        {"key": "A", "text": "Vì BCEWithLogitsLoss tính toán nhanh hơn nhưng kém chính xác hơn"},
        {"key": "B", "text": "Vì BCELoss không hỗ trợ tính toán trên GPU"},
        {"key": "C", "text": "Vì BCELoss bắt buộc số lượng mẫu phải là lũy thừa của 2"},
        {"key": "D", "text": "Vì BCEWithLogitsLoss gộp phép tính Sigmoid và Log-Loss thành một biểu thức toán học ổn định số học (Log-Sum-Exp trick), triệt tiêu lỗi tràn số float"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Hiện tượng tràn số trong máy tính (Overflow & Underflow):**
Khi mạng nơ-ron dự đoán một con số quá lớn (ví dụ $z = 100$):
- Nếu bạn tính $\\text{sigmoid}(100)$, máy tính làm tròn thành $1.0$. Sau đó lấy $\\log(1 - 1.0) = \\log(0) = -\\infty$ (Âm vô cùng)! Mô hình sẽ lập tức bị lỗi `NaN` (Not a Number) và sập toàn bộ quá trình huấn luyện!
- `BCEWithLogitsLoss` dùng mẹo toán học gộp cả hai bước lại thành một công thức rút gọn, triệt tiêu hoàn toàn nguy cơ chia cho 0 hay $\\log(0)$.

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Biểu thức toán học gộp của `BCEWithLogitsLoss`:
Hàm mất mát Binary Cross-Entropy với nhãn $y \\in \\{0, 1\\}$ và logit $z$:
$$\\ell(z, y) = - [y \\log(\\sigma(z)) + (1 - y) \\log(1 - \\sigma(z))]$$
Biến đổi đại số bằng định nghĩa $\\sigma(z) = \\frac{1}{1 + e^{-z}}$:
$$\\log(\\sigma(z)) = - \\log(1 + e^{-z})$$
$$\\log(1 - \\sigma(z)) = - z - \\log(1 + e^{-z})$$
Thay vào hàm mất mát:
$$\\ell(z, y) = - [y (-\\log(1 + e^{-z})) + (1 - y) (-z - \\log(1 + e^{-z}))] = (1 - y) z + \\log(1 + e^{-z}) = z - y z + \\log(1 + e^{-z})$$
Dạng tổng quát ổn định số học với mọi $z$:
$$\\ell(z, y) = \\max(z, 0) - y z + \\log(1 + e^{-|z|})$$
Bằng cách dùng $|z|$, số mũ $e^{-|z|}$ luôn $\\le 1$, bảo đảm 100% không bao giờ bị tràn số dương (Overflow)! Chọn **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** BCEWithLogitsLoss vừa nhanh hơn vừa chính xác số học cao hơn, không hề kém chính xác.
- **Phương án B & C:** Hoàn toàn bịa đặt, BCELoss vẫn chạy GPU bình thường và nhận mọi kích thước batch.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.4 Các hàm mất mát trong Deep Learning**.
🔗 **Quy tắc bỏ túi PyTorch:**
- Đa lớp: Dùng `CrossEntropyLoss(logits)` (câu B11).
- Nhị phân: Dùng `BCEWithLogitsLoss(logits)` (câu B12).
Không bao giờ tự ý gắn Softmax hay Sigmoid vào tầng cuối cùng khi train!"""
}

UPGRADES["OLP01-B13"] = {
    "prompt": "Trong một vòng lặp huấn luyện PyTorch tiêu chuẩn cho một batch dữ liệu, thứ tự các dòng lệnh bắt buộc phải thực hiện là gì?",
    "options": [
        {"key": "A", "text": "optimizer.zero_grad() -> outputs = model(inputs) -> loss = criterion(outputs, targets) -> loss.backward() -> optimizer.step()"},
        {"key": "B", "text": "outputs = model(inputs) -> loss = criterion(...) -> loss.backward() -> optimizer.step() -> optimizer.zero_grad()"},
        {"key": "C", "text": "loss.backward() -> optimizer.zero_grad() -> optimizer.step() -> outputs = model(inputs)"},
        {"key": "D", "text": "optimizer.step() -> outputs = model(inputs) -> loss.backward() -> optimizer.zero_grad()"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Quy trình 5 bước huấn luyện PyTorch kinh điển:**
1. **`optimizer.zero_grad()`:** Xóa sạch bảng điểm gradient cũ (vì PyTorch có tính năng mặc định là cộng dồn gradient, nếu không xóa thì vết đạo hàm cũ sẽ làm hỏng bước đi mới).
2. **`outputs = model(inputs)`:** Đưa đề bài vào mô hình để làm bài (Lan truyền tiến - Forward pass).
3. **`loss = criterion(outputs, targets)`:** Chấm điểm xem làm sai bao nhiêu (Tính hàm mất mát).
4. **`loss.backward()`:** Lần ngược từ kết quả để tìm xem nơ-ron nào làm sai (Lan truyền ngược - Backward pass tính gradient).
5. **`optimizer.step()`:** Sửa sai bằng cách cập nhật các trọng số theo hướng giảm lỗi (Cập nhật trọng số).
Quy tắc: **Xóa bộ nhớ cũ $\\implies$ Đoán $\\implies$ Chấm lỗi $\\implies$ Tìm nguyên nhân $\\implies$ Sửa sai**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Mã nguồn chuẩn mực:
```python
optimizer.zero_grad()                   # 1. Triệt tiêu gradient tích lũy: w.grad = 0
outputs = model(inputs)                 # 2. Forward pass: y_hat = f(x; w)
loss = criterion(outputs, targets)      # 3. Compute loss: L(y_hat, y)
loss.backward()                         # 4. Backward pass: w.grad += dL/dw
optimizer.step()                        # 5. Parameter update: w = w - lr * w.grad
```
Chọn đáp án **A**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B:** Đặt `zero_grad()` ở cuối cùng dù chạy được nhưng dễ quên hoặc gây lỗi nếu có vòng lặp gradient accumulation.
- **Phương án C:** Gọi `loss.backward()` trước khi forward là lỗi cú pháp runtime (loss chưa tồn tại).
- **Phương án D:** Cập nhật `optimizer.step()` trước khi tính đạo hàm là hoàn toàn sai logic.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.3 Vòng lặp huấn luyện PyTorch chuẩn**.
🔗 Cấu trúc này sẽ được bạn tự tay viết thành code ở bài thực hành lập trình **OLP01-BC2**!"""
}

UPGRADES["OLP01-B14"] = {
    "prompt": "Khi khởi tạo trọng số cho các tầng ẩn sử dụng hàm kích hoạt ReLU trong mạng Deep Learning, phương pháp khởi tạo nào sau đây là TỐI ƯU NHẤT để chống hiện tượng triệt tiêu hoặc bùng nổ gradient (Vanishing/Exploding Gradient)?",
    "options": [
        {"key": "A", "text": "Khởi tạo toàn bộ trọng số bằng 0 (Zero Initialization)"},
        {"key": "B", "text": "Khởi tạo Kaiming He (He Normal / Uniform Initialization)"},
        {"key": "C", "text": "Khởi tạo toàn bộ trọng số bằng 1 (Ones Initialization)"},
        {"key": "D", "text": "Khởi tạo Xavier / Glorot Initialization"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Vì sao hàm ReLU cần phép khởi tạo riêng của Kaiming He?**
Hàm ReLU có đặc điểm: Cứ số âm là nó biến thành số 0 (chặt bỏ đúng $50\\%$ tín hiệu).
Nếu bạn dùng phép khởi tạo Xavier thông thường, qua mỗi tầng nơ-ron, một nửa số tín hiệu bị mất đi, làm phương sai của tín hiệu teo tóp dần về 0 khi mạng đi sâu (Triệt tiêu gradient)!
Năm 2015, giáo sư Kaiming He phát hiện ra điều này và nhân thêm một hệ số bù đắp $\\sqrt{2}$ vào độ lệch chuẩn khởi tạo, giúp bù lại chính xác 50% tín hiệu bị ReLU triệt tiêu, giữ cho năng lượng tín hiệu luôn ổn định xuyên suốt hàng trăm tầng mạng!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 So sánh công thức toán học:
1. **Xavier / Glorot Initialization (Dành cho Tanh / Sigmoid):**
$$\\text{Var}(W) = \\frac{2}{n_{\\text{in}} + n_{\\text{out}}}$$
2. **Kaiming He Initialization (Dành riêng cho ReLU):**
Do ReLU triệt tiêu một nửa phân phối đối xứng quanh 0, $\\mathbb{E}[\\text{ReLU}(z)^2] = \\frac{1}{2} \\text{Var}(z)$. Để bảo toàn phương sai $\\text{Var}(y) = \\text{Var}(x)$:
$$\\text{Var}(W) = \\frac{2}{n_{\\text{in}}}$$
Trọng số được rút từ phân phối chuẩn:
$$W \\sim \\mathcal{N}\\left(0, \\sqrt{\\frac{2}{n_{\\text{in}}}}\\right)$$
Trong PyTorch: `nn.init.kaiming_normal_(layer.weight, nonlinearity='relu')`. Chọn **B**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A & C:** Khởi tạo toàn bộ bằng 0 hoặc 1 gây ra hiện tượng **Phá vỡ tính đối xứng (Symmetry Breaking Failure)**: Mọi nơ-ron trong cùng một tầng đều có cùng giá trị và cùng gradient, mạng biến thành một nơ-ron duy nhất dù có bao nhiêu tham số đi nữa!
- **Phương án D:** Xavier tối ưu cho Sigmoid và Tanh, nhưng bị suy yếu phương sai khi dùng với ReLU.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.7 Kỹ thuật Khởi tạo trọng số (Weight Initialization)**.
🔗 Kaiming He chính là tác giả của mạng **ResNet** đoạt giải nhất ImageNet năm 2015! Chính nhờ phép khởi tạo He và kiến trúc Skip Connection mà ông đã huấn luyện thành công mạng ResNet sâu tới 152 tầng!"""
}

UPGRADES["OLP01-B15"] = {
    "prompt": "Trong NumPy, cho một mảng hai chiều `arr` có kích thước `shape = (3, 4)`. Khi thực hiện phép chuyển vị `arr.T` (hoặc `np.transpose(arr)`), kích thước mới của mảng kết quả là bao nhiêu?",
    "options": [
        {"key": "A", "text": "(3, 4)"},
        {"key": "B", "text": "(12,)"},
        {"key": "C", "text": "(4, 3)"},
        {"key": "D", "text": "(3, 1, 4)"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Phép chuyển vị ma trận (Transpose):**
Tưởng tượng bạn lật nghiêng chiếc bàn chữ nhật:
- Ban đầu bàn có **3 hàng và 4 cột** (kích thước $3 \\times 4$).
- Khi lật nghiêng (hàng biến thành cột, cột biến thành hàng): Chiếc bàn mới sẽ có **4 hàng và 3 cột** (kích thước $4 \\times 3$)!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 Định nghĩa phép chuyển vị ma trận trong đại số tuyến tính:
Nếu ma trận $A \\in \\mathbb{R}^{m \\times n}$ thì ma trận chuyển vị $A^T \\in \\mathbb{R}^{n \\times m}$ với các phần tử thỏa mãn:
$$(A^T)_{j, i} = A_{i, j}$$
Với mảng NumPy có `shape = (3, 4)`:
- Trục 0 (hàng): 3
- Trục 1 (cột): 4
Sau phép `arr.T`: Trục 0 và Trục 1 hoán đổi vị trí cho nhau $\\implies$ `shape = (4, 3)`. Chọn **C**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án B (12,):** Là kết quả của hàm duỗi phẳng `arr.flatten()` hoặc `arr.reshape(-1)`.
- **Phương án D:** Là kết quả của hàm thêm chiều `np.expand_dims(arr, axis=1)`.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.10 Đại số tuyến tính với NumPy**.
🔗 Trong PyTorch Deep Learning, hàm `tensor.T` dùng cho ma trận 2D, còn với tensor nhiều chiều (ví dụ ảnh $B \\times C \\times H \\times W$ chuyển sang $B \\times H \\times W \\times C$), ta dùng hàm `tensor.permute(0, 2, 3, 1)`!"""
}

UPGRADES["OLP01-B16"] = {
    "prompt": "Trong NumPy, cho mảng `A` có kích thước `(4, 1)` và mảng `B` có kích thước `(4,)`. Khi thực hiện phép cộng `C = A + B`, theo quy tắc Broadcasting của NumPy, mảng `C` có kích thước kết quả là bao nhiêu?",
    "options": [
        {"key": "A", "text": "Báo lỗi ValueError vì không thể cộng hai mảng lệch chiều"},
        {"key": "B", "text": "(4, 1)"},
        {"key": "C", "text": "(4,)"},
        {"key": "D", "text": "(4, 4)"}
    ],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Bẫy Broadcasting kinh điển nhất của NumPy:**
Rất nhiều người tưởng rằng `(4, 1)` cộng `(4,)` sẽ ra `(4, 1)`. Nhưng NumPy có quy tắc ngầm:
1. Mảng $B$ có shape `(4,)` (chỉ có 1 chiều). NumPy sẽ tự động bù thêm số 1 vào **bên trái** để thành `(1, 4)` (1 hàng, 4 cột)!
2. Mảng $A$ có shape `(4, 1)` (4 hàng, 1 cột).
3. Khi cộng: Hàng của $B$ được nhân bản 4 lần xuống dưới, cột của $A$ được nhân bản 4 lần sang phải $\\implies$ Tạo thành một ma trận vuông khổng lồ kích thước **(4, 4)**!

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 3 quy tắc Broadcasting chuẩn mực của NumPy:
1. **Quy tắc 1 (Canh lề phải):** So sánh kích thước từng chiều từ phải sang trái. Nếu một mảng thiếu chiều, thêm chiều kích thước 1 vào bên trái:
- Mảng A: `(4, 1)`
- Mảng B: `(4,)` $\\to$ được nâng chiều thành `(1, 4)`.
2. **Quy tắc 2 (Kéo dãn chiều bằng 1):**
- Chiều 1 (cột): A có 1 cột, B có 4 cột $\\implies$ Hợp lệ, kéo dãn A thành 4 cột.
- Chiều 0 (hàng): A có 4 hàng, B có 1 hàng $\\implies$ Hợp lệ, kéo dãn B thành 4 hàng.
3. **Quy tắc 3 (Kích thước kết quả):** Lấy giá trị lớn nhất của từng chiều:
$$\\text{shape}(C) = (\\max(4, 1), \\max(1, 4)) = (4, 4)$$
Mã Python kiểm chứng:
```python
import numpy as np
A = np.zeros((4, 1))
B = np.zeros((4,))
print((A + B).shape) # (4, 4)
```
Chọn đáp án **D**.

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy:**
- **Phương án A:** Nghĩ rằng khác số chiều là báo lỗi.
- **Phương án B & C:** Nghĩ rằng mảng 1 chiều sẽ tự cộng vào cột của ma trận $4 \\times 1$. Đây là bẫy bug gây tràn bộ nhớ ngầm cực kỳ nguy hiểm trong code Python thực chiến!

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.10 Đại số tuyến tính & Cơ chế Broadcasting**.
🔗 Trong PyTorch, nếu bạn vô tình để loss dạng `(N, 1)` trừ nhãn dạng `(N,)`, PyTorch sẽ âm thầm tạo ma trận `(N, N)` và tính loss sai hoàn toàn! Luôn dùng `y.squeeze()` hoặc `y.view(-1, 1)` để cố định chiều!"""
}

# ==========================================
# MODULE B: CODE THỰC HÀNH (2 CÂU: BC1 & BC2)
# ==========================================

UPGRADES["OLP01-BC1"] = {
    "prompt": "Viết hàm Python/NumPy `compute_metrics(y_true, y_pred)` nhận vào hai mảng nhị phân 1D (chỉ chứa 0 và 1) có cùng kích thước, tính toán và trả về một tuple gồm 3 giá trị: `(precision, recall, f1)` dưới dạng số thực (float). Đảm bảo xử lý an toàn trường hợp chia cho 0 (trả về 0.0 nếu mẫu số bằng 0).",
    "options": [],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 Để tính toán các chỉ số đánh giá, ta chỉ cần đếm 3 đại lượng cơ bản bằng NumPy:
- $TP$ (True Positive): Cả `y_true == 1` và `y_pred == 1`.
- $FP$ (False Positive): Đoán là 1 (`y_pred == 1`) nhưng nhãn thực tế là 0 (`y_true == 0`).
- $FN$ (False Negative): Đoán là 0 (`y_pred == 0`) nhưng nhãn thực tế là 1 (`y_true == 1`).
Sau đó áp dụng công thức đã học ở câu B07 & B08. Luôn nhớ thêm điều kiện kiểm tra mẫu số $> 0$ để tránh lỗi `ZeroDivisionError`!

### 2. Công thức toán & Mã nguồn hoàn chỉnh Step-by-Step
```python
import numpy as np

def compute_metrics(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # 1. Tinh toan TP, FP, FN bang phep toan logic boolean
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    
    # 2. Precision = TP / (TP + FP)
    precision = float(tp / (tp + fp)) if (tp + fp) > 0 else 0.0
    
    # 3. Recall = TP / (TP + FN)
    recall = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
    
    # 4. F1-score = 2 * P * R / (P + R)
    f1 = float(2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
    
    return precision, recall, f1
```

### 3. Tiêu chí chấm điểm Rubric (Thang 7.0 điểm)
- Đạt 2.0đ: Chuyển đổi mảng NumPy và tính đúng logic boolean cho TP, FP, FN.
- Đạt 4.0đ: Tính đúng công thức Precision và Recall.
- Đạt 5.0đ: Tính đúng công thức F1-score.
- Đạt 7.0đ (Full): Xử lý an toàn mẫu số bằng 0 (edge cases) và trả về đúng định dạng tuple float.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§1.7 Confusion Matrix**. Liên hệ lại hai câu tính tay **B07** và **B08**."""
}

UPGRADES["OLP01-BC2"] = {
    "prompt": "Viết hàm huấn luyện PyTorch chuẩn cho 1 epoch: `train_one_epoch(model, dataloader, criterion, optimizer, device)`. Hàm cần chuyển model sang chế độ train, đưa dữ liệu lên đúng thiết bị (device), thực hiện đúng chu trình 5 bước huấn luyện (zero_grad, forward, loss, backward, step), và trả về giá trị trung bình loss của cả epoch (float).",
    "options": [],
    "explanation": """### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 Vòng lặp huấn luyện trong PyTorch là quy trình lặp đi lặp lại qua từng gói dữ liệu (batch). Ta cần nhớ 3 việc sống còn:
1. Gọi `model.train()` để bật các cơ chế dành riêng cho lúc học (như Dropout và BatchNorm cập nhật running mean/var).
2. Đưa cả ảnh và nhãn lên GPU/CPU bằng `.to(device)`.
3. Chạy đúng chu trình 5 bước đã học ở câu **B13**: `zero_grad` -> `forward` -> `loss` -> `backward` -> `step`.

### 2. Mã nguồn PyTorch chuẩn mực Step-by-Step
```python
import torch

def train_one_epoch(model, dataloader, criterion, optimizer, device):
    # 1. Chuyen model ve che do huan luyen
    model.train()
    running_loss = 0.0
    total_samples = 0
    
    # 2. Lap qua tung batch trong dataloader
    for inputs, targets in dataloader:
        inputs = inputs.to(device)
        targets = targets.to(device)
        
        # 3. Chu trinh 5 buoc huan luyen
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        
        # 4. Tich luy loss theo dung so luong mau
        batch_size = inputs.size(0)
        running_loss += loss.item() * batch_size
        total_samples += batch_size
        
    epoch_loss = float(running_loss / total_samples) if total_samples > 0 else 0.0
    return epoch_loss
```

### 3. Tiêu chí chấm điểm Rubric (Thang 7.0 điểm)
- Đạt 2.0đ: Có `model.train()` và chuyển dữ liệu sang `device`.
- Đạt 4.0đ: Thực hiện đủ và đúng thứ tự 5 bước tối ưu hóa (`zero_grad`, forward, loss, `backward`, `step`).
- Đạt 5.0đ: Tích lũy loss có nhân với kích thước batch để tính trung bình chính xác cho batch cuối cùng bị lẻ.
- Đạt 7.0đ (Full): Trả về giá trị trung bình epoch loss dạng float chuẩn xác.

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 **Căn cứ lý thuyết:** Xem **§2.3 Vòng lặp huấn luyện PyTorch**. Liên hệ câu lý thuyết **B13**."""
}

print("Đang nạp từ điển nâng cấp cho 64 câu...")
