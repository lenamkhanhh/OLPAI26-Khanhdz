# -*- coding: utf-8 -*-
"""
Chuẩn hóa công thức toán học LaTeX chuẩn cho các phương án trắc nghiệm (options)
trong các đề thi OLP AI (olp-01.json, olp-02.json).
Bảo toàn 100% answer key và cấu trúc đề thi.
"""
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Cập nhật olp-01.json
olp01_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-01.json")
with open(olp01_path, "r", encoding="utf-8") as f:
    olp01_data = json.load(f)

for q in olp01_data["questions"]:
    if q["id"] == "OLP01-A12":
        q["options"] = [
            {"key": "A", "text": "$\\frac{1}{6}$"},
            {"key": "B", "text": "$\\frac{5}{36}$"},
            {"key": "C", "text": "$\\frac{1}{12}$"},
            {"key": "D", "text": "$\\frac{1}{9}$"}
        ]
    elif q["id"] == "OLP01-C03":
        for opt in q["options"]:
            if opt["key"] == "B":
                opt["text"] = "$\\text{Margin} = \\frac{1}{\\|w\\|^2}$"
    elif q["id"] == "OLP01-C05":
        q["options"] = [
            {
                "key": "A",
                "text": "$H(S) = -\\sum_{i=1}^c p_i \\log_2(p_i)$, sử dụng logarit cơ số 2 với đơn vị đo là bit (hoặc shannon)"
            },
            {
                "key": "B",
                "text": "$H(S) = \\sum_{i=1}^c p_i \\ln(p_i)$, sử dụng logarit tự nhiên với đơn vị là nat"
            },
            {
                "key": "C",
                "text": "$H(S) = 1 - \\sum_{i=1}^c p_i^2$, sử dụng logarit cơ số 10"
            },
            {
                "key": "D",
                "text": "$H(S) = -\\sum_{i=1}^c p_i^2 \\log_2(p_i)$, sử dụng logarit cơ số 2"
            }
        ]
    elif q["id"] == "OLP01-C10":
        for opt in q["options"]:
            if opt["key"] == "A":
                opt["text"] = "Vì L1 sẽ chọn ngẫu nhiên 1 đặc trưng và loại bỏ các đặc trưng còn lại một cách không ổn định, trong khi L2 co đều các hệ số trọng số và luôn đảm bảo ma trận $(X^T X + \\lambda I)$ khả nghịch"

with open(olp01_path, "w", encoding="utf-8") as f:
    json.dump(olp01_data, f, ensure_ascii=False, indent=2)
print("Updated olp-01.json successfully.")

# 2. Cập nhật olp-02.json
olp02_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-02.json")
with open(olp02_path, "r", encoding="utf-8") as f:
    olp02_data = json.load(f)

for q in olp02_data["questions"]:
    if q["id"] == "VOAI02-M04":
        for opt in q["options"]:
            if opt["key"] == "B":
                opt["text"] = "Tìm các vector riêng tương ứng với các trị riêng lớn nhất của ma trận hiệp phương sai $C = \\frac{1}{N} X^T X$"
            elif opt["key"] == "D":
                opt["text"] = "Nghịch đảo ma trận tương quan $X^T X$"
    elif q["id"] == "VOAI02-M06":
        q["options"] = [
            {"key": "A", "text": "$\\frac{\\partial L}{\\partial z_i} = p_i - y_i$"},
            {"key": "B", "text": "$\\frac{\\partial L}{\\partial z_i} = y_i - p_i$"},
            {"key": "C", "text": "$\\frac{\\partial L}{\\partial z_i} = -\\frac{y_i}{p_i}$"},
            {"key": "D", "text": "$\\frac{\\partial L}{\\partial z_i} = p_i(1 - p_i)$"}
        ]
    elif q["id"] == "VOAI02-M09":
        q["options"] = [
            {"key": "A", "text": "$D_{KL}(P \\parallel Q)$ luôn đối xứng: $D_{KL}(P \\parallel Q) = D_{KL}(Q \\parallel P)$"},
            {"key": "B", "text": "$D_{KL}(P \\parallel Q)$ là một metric khoảng cách toán học thỏa mãn bất đẳng thức tam giác"},
            {"key": "C", "text": "$D_{KL}(P \\parallel Q)$ có thể nhận giá trị âm nếu $Q(x) > P(x)$ tại nhiều điểm"},
            {"key": "D", "text": "$D_{KL}(P \\parallel Q) \\ge 0$ (luôn không âm) và bằng 0 khi và chỉ khi $P = Q$ hầu khắp nơi"}
        ]
    elif q["id"] == "VOAI02-M10":
        q["options"] = [
            {"key": "A", "text": "$f'(x) = \\sigma(x) + x \\cdot \\sigma(x)(1 - \\sigma(x))$"},
            {"key": "B", "text": "$f'(x) = 1 + \\sigma(x)$"},
            {"key": "C", "text": "$f'(x) = x^2 \\cdot \\sigma(x)$"},
            {"key": "D", "text": "$f'(x) = \\sigma(x)(1 - \\sigma(x))$"}
        ]
    elif q["id"] == "VOAI02-M11":
        q["options"] = [
            {"key": "A", "text": "$\\|Qx\\|_2 = \\|x\\|_2$ (chuẩn luôn được bảo toàn nguyên vẹn)"},
            {"key": "B", "text": "$\\|Qx\\|_2 = \\det(Q) \\|x\\|_2$"},
            {"key": "C", "text": "$\\|Qx\\|_2 \\le \\|x\\|_2$"},
            {"key": "D", "text": "$\\|Qx\\|_2 \\ge \\|x\\|_2$"}
        ]
    elif q["id"] == "VOAI02-M12":
        q["options"] = [
            {"key": "A", "text": "$\\mathbb{E}_{x \\sim P}[f(x)] = \\frac{1}{M} \\sum_{i=1}^M f(x_i) \\frac{P(x_i)}{Q(x_i)} \\quad \\text{với } x_i \\sim Q$"},
            {"key": "B", "text": "$\\mathbb{E}_{x \\sim P}[f(x)] = \\frac{1}{M} \\sum_{i=1}^M f(x_i) [P(x_i) - Q(x_i)] \\quad \\text{với } x_i \\sim Q$"},
            {"key": "C", "text": "$\\mathbb{E}_{x \\sim P}[f(x)] = \\frac{1}{M} \\sum_{i=1}^M f(x_i) \\quad \\text{với } x_i \\sim Q$"},
            {"key": "D", "text": "$\\mathbb{E}_{x \\sim P}[f(x)] = \\frac{1}{M} \\sum_{i=1}^M f(x_i) \\frac{Q(x_i)}{P(x_i)} \\quad \\text{với } x_i \\sim Q$"}
        ]
    elif q["id"] == "VOAI02-M18":
        for opt in q["options"]:
            if opt["key"] == "C":
                opt["text"] = "Các mẫu bị mô hình $h_t$ đoán SAI sẽ được TĂNG trọng số, các mẫu đoán ĐÚNG sẽ bị GIẢM trọng số"
    elif q["id"] == "VOAI02-M19":
        for opt in q["options"]:
            if opt["key"] == "D":
                opt["text"] = "XGBoost áp dụng xấp xỉ Taylor bậc hai (sử dụng cả gradient bậc một $g_i$ và Hessian bậc hai $h_i$) cho hàm mất mát tùy ý và tích hợp sẵn số hạng phạt độ phức tạp cây L1/L2"
    elif q["id"] == "VOAI02-M32":
        for opt in q["options"]:
            if opt["key"] == "A":
                opt["text"] = "Tách rời (Decoupled) số hạng Weight Decay ra khỏi phép cập nhật gradient có tỷ lệ theo moment bậc hai, áp dụng trực tiếp suy giảm trọng số $w = w - \\eta \\lambda w$ vào tham số"
    elif q["id"] == "VOAI02-M34":
        for opt in q["options"]:
            if opt["key"] == "D":
                opt["text"] = "Trong pha train, các nơ-ron không bị tắt được nhân với hệ số co giãn $\\frac{1}{1 - p}$; Trong pha eval, không cần thực hiện bất kỳ phép tính co giãn nào (giữ nguyên đầu ra)"
    elif q["id"] == "VOAI02-M43":
        q["options"] = [
            {"key": "A", "text": "$\\frac{1}{7}$ (khoảng 0.143)"},
            {"key": "B", "text": "$\\frac{4}{32}$ (khoảng 0.125)"},
            {"key": "C", "text": "$\\frac{1}{4}$ (khoảng 0.250)"},
            {"key": "D", "text": "$\\frac{4}{28}$ (khoảng 0.143)"}
        ]
    elif q["id"] == "VOAI02-M48":
        q["options"] = [
            {"key": "A", "text": "$\\tilde{x} = x_i - x_j, \\quad \\tilde{y} = y_i - y_j$"},
            {"key": "B", "text": "$\\tilde{x} = x_i \\odot x_j, \\quad \\tilde{y} = y_i \\odot y_j$"},
            {"key": "C", "text": "$\\tilde{x} = \\max(x_i, x_j), \\quad \\tilde{y} = \\max(y_i, y_j)$"},
            {"key": "D", "text": "$\\tilde{x} = \\lambda x_i + (1 - \\lambda) x_j, \\quad \\tilde{y} = \\lambda y_i + (1 - \\lambda) y_j$"}
        ]
    elif q["id"] == "VOAI02-M51":
        q["options"] = [
            {"key": "A", "text": "$\\frac{4}{3\\sqrt{5}}$ (khoảng 0.596)"},
            {"key": "B", "text": "$\\frac{4}{9}$"},
            {"key": "C", "text": "$\\frac{4}{5}$"},
            {"key": "D", "text": "$\\frac{2}{\\sqrt{5}}$"}
        ]
    elif q["id"] == "VOAI02-M53":
        for opt in q["options"]:
            if opt["key"] == "D":
                opt["text"] = "Vì khi $d_k$ lớn, tích vô hướng $Q K^T$ có phương sai tăng tuyến tính bằng $d_k$, đẩy các giá trị đầu vào của Softmax ra các vùng có độ dốc cực kỳ bão hòa khiến gradient bị triệt tiêu tiệm cận 0 (Vanishing Gradient); chia cho $\\sqrt{d_k}$ đưa phương sai trở về 1"
    elif q["id"] == "VOAI02-M55":
        for opt in q["options"]:
            if opt["key"] == "B":
                opt["text"] = "Với bất kỳ khoảng cách dịch chuyển cố định $k$, $PE(\\text{pos} + k)$ có thể được biểu diễn như một hàm biến đổi tuyến tính của $PE(\\text{pos})$, cho phép mô hình dễ dàng học cách chú ý theo vị trí tương đối và có khả năng ngoại suy cho chuỗi dài hơn chuỗi lúc huấn luyện"
    elif q["id"] == "VOAI02-M57":
        for opt in q["options"]:
            if opt["key"] == "B":
                opt["text"] = "$BP = \\exp(1 - 10/2) = \\exp(-4) \\approx 0.0183$ (phạt cực nặng, giảm gần 98% điểm)"
            elif opt["key"] == "D":
                opt["text"] = "$BP = \\frac{10}{2} = 5.0$"
    elif q["id"] == "VOAI02-M60":
        for opt in q["options"]:
            if opt["key"] == "C":
                opt["text"] = "Từ $\\mathcal{O}(N)$ xuống $\\mathcal{O}(1)$ đối với phép chiếu Key và Value của các token quá khứ, biến độ phức tạp tính toán của bước sinh token mới thành $\\mathcal{O}(N)$ thay vì phải tính toán lại toàn bộ chuỗi tốn $\\mathcal{O}(N^2)$"
            elif opt["key"] == "D":
                opt["text"] = "Từ $\\mathcal{O}(N^2)$ xuống $\\mathcal{O}(1)$ (với $N$ là độ dài chuỗi hiện tại)"

with open(olp02_path, "w", encoding="utf-8") as f:
    json.dump(olp02_data, f, ensure_ascii=False, indent=2)
print("Updated olp-02.json successfully.")
