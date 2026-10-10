# -*- coding: utf-8 -*-
"""
scripts/build_full_upgrades_olp03_data.py
Bổ sung đầy đủ dữ liệu nâng cấp cho M11 đến M50 của Đề 03.
"""

import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
json_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")

with open(json_path, "r", encoding="utf-8") as f:
    exam_data = json.load(f)

UPGRADES_REMAINING = {
    "VOAI03-M21": (
        "- **Bag of Words (BoW):** Phương pháp biểu diễn văn bản bằng cách đếm số lần xuất hiện của từng từ trong từ điển (Vocabulary), bỏ qua hoàn toàn thứ tự từ.\n- **Tính chất thưa (Sparsity):** Vector có hàng chục ngàn chiều nhưng hầu hết là số 0.\n- **Semantic Blindness (Mù ngữ nghĩa):** Không hiểu được hai từ đồng nghĩa (ví dụ: 'xe hơi' và 'ô tô' bị coi là hai chiều độc lập hoàn toàn khác nhau).",
        "BoW giống như bạn ném tất cả các từ trong một câu vào một chiếc túi rồi xóc đều lên: Câu 'Chó cắn người' và câu 'Người cắn chó' có đúng các từ ngữ như nhau, nên BoW biến chúng thành cùng một vector y hệt! Nó hoàn toàn làm mất trật tự ngữ pháp và ngữ cảnh câu.",
        "Vector BoW của văn bản $d$: $v_d = [c(w_1, d), c(w_2, d), \\dots, c(w_{|V|}, d)]^T$.\nKhông có ma trận quan hệ thứ tự $P(w_i | w_{i-1})$. Chọn **B** (Làm mất thứ tự từ trong câu).",
        "- **Phương án A & C:** BoW có chi phí tính toán rất thấp và dễ cài đặt, không phải nhược điểm.\n- **Phương án D:** BoW hoàn toàn đếm được tần suất từ (đó chính là bản chất của nó).",
        "📚 Xem **§4.2 Biểu diễn từ & Vector hóa văn bản**.\n🔗 **Liên hệ bài cũ:** Nhược điểm này được khắc phục đầu tiên bởi TF-IDF (đánh trọng số), sau đó là Word2Vec/FastText (nhúng ngữ nghĩa) và cuối cùng là Transformer/BERT (chú ý ngữ cảnh 2 chiều)."
    ),
    "VOAI03-M22": (
        "- **BERT (Bidirectional Encoder Representations from Transformers):** Mô hình ngôn ngữ do Google đề xuất (2018), sử dụng phần **Encoder** của Transformer.\n- **Cơ chế 2 chiều (Bidirectional Attention):** Mỗi từ được chú ý đồng thời tới cả các từ đứng trước nó và đứng sau nó trong câu.\n- **Masked Language Model (MLM):** Che ngẫu nhiên 15% từ trong câu rồi bắt mô hình đoán từ bị che.",
        "Khác với người đọc sách bình thường phải đọc từ trái sang phải từng chữ một (như GPT), BERT nhìn toàn bộ câu văn cùng lúc như một bức tranh hoàn chỉnh! Nó nhìn cả bên trái lẫn bên phải của từ bị khuyết để hiểu trọn vẹn ngữ cảnh của câu. Đó là lý do BERT chỉ dùng khối **Transformer Encoder**!",
        "Kiến trúc BERT-Base gồm 12 tầng Transformer Encoder, 12 attention heads, hidden size $d=768$, tổng cộng 110 triệu tham số. Không có khối Decoder hay Causal Masking. Chọn **D** (Transformer Encoder).",
        "- **Phương án A (Transformer Decoder):** Là cấu trúc của dòng mô hình GPT (Autoregressive, có Causal Mask chỉ nhìn về bên trái).\n- **Phương án B (Encoder-Decoder):** Là cấu trúc của T5, BART (dùng cho bài toán dịch máy và tóm tắt văn bản).\n- **Phương án C (RNN/LSTM):** BERT hoàn toàn không dùng RNN.",
        "📚 Xem **§4.4 Transformer, Self-Attention & Large Language Models**.\n🔗 **Liên hệ bài cũ:** Nhớ quy tắc phân loại 3 dòng họ Transformer: BERT = Encoder-only (hiểu/phân loại); GPT = Decoder-only (sinh từ tự hồi quy); T5/BART = Encoder-Decoder (dịch máy/seq2seq)."
    ),
    "VOAI03-M23": (
        "- **RAG (Retrieval-Augmented Generation):** Kỹ thuật kết hợp giữa bộ truy xuất dữ liệu ngoài (Retriever - BM25 / Vector DB) và mô hình ngôn ngữ lớn (Generator - LLM).\n- **Ảo giác (Hallucination):** Hiện tượng LLM tự bịa ra thông tin sai lệch nhưng diễn đạt với giọng điệu cực kỳ tự tin.\n- **Bộ nhớ ngoài (External Knowledge Base):** Tài liệu văn bản nội bộ được cắt chunk và nhúng vector.",
        "RAG biến kỳ thi của LLM từ một 'Kỳ thi đóng sách' (phải học vẹt thuộc lòng toàn bộ kiến thức vào trọng số) thành một 'Kỳ thi mở sách': Khi người dùng hỏi một câu hỏi khó, hệ thống mở ngăn kéo tài liệu ra, tìm đúng trang sách liên quan nhất rồi kẹp vào đề bài để LLM đọc và trả lời. Nhờ đó, LLM giảm thiểu tối đa tình trạng nói bừa (ảo giác)!",
        "Công thức xác suất của RAG với tài liệu truy xuất $z$:\n$$P(y \\mid x) = \\sum_{z \\in \\text{Top-k}} P(z \\mid x) P(y \\mid x, z)$$\nRAG giúp LLM neo câu trả lời vào bằng chứng xác thực (Grounding), giảm thiểu đáng kể ảo giác. Chọn **A** (Hiện tượng ảo giác - Hallucination).",
        "- **Phương án B (Overfitting):** Overfitting là vấn đề của quá trình huấn luyện, RAG không can thiệp trọng số.\n- **Phương án C & D:** RAG không làm tăng tốc độ suy luận (thậm chí tăng thêm độ trễ do bước truy xuất) và không làm giảm kích thước mô hình.",
        "📚 Xem **§4.6 Retrieval-Augmented Generation (RAG) & Vector Database**.\n🔗 **Liên hệ bài cũ:** Trong bài tự luận E06 Đề 02, ta thiết kế một hệ thống Enterprise RAG chuẩn mực kết hợp Hybrid Retrieval (BM25 + BGE-m3) và Cross-Encoder Re-ranker."
    ),
    "VOAI03-M24": (
        "- **Max Pooling:** Phép toán lấy giá trị lớn nhất trong từng cửa sổ trượt không gian (thường là $2 \\times 2$, stride 2).\n- **Tính bất biến với dịch chuyển nhỏ (Translation Invariance):** Nếu vật thể trong ảnh bị xê dịch nhẹ một vài pixel, giá trị cực đại trong cửa sổ $2 \\times 2$ vẫn không đổi.\n- **Giảm chiều không gian (Downsampling):** Giảm kích thước ảnh đi một nửa, mở rộng vùng cảm thụ (Receptive Field) cho các tầng sau.",
        "Max Pooling giống như việc bạn nhìn một bức tranh từ xa: Bạn chỉ cần ghi nhớ điểm sáng nhất, nổi bật nhất của bức tranh đó mà không cần bận tâm chi tiết nhỏ bị xê dịch một chút sang trái hay sang phải. Nó giúp mạng máy tính nhận ra con mèo dù con mèo nằm ở chính giữa hay hơi lệch sang mép ảnh!",
        "Công thức Max Pooling kích thước $K \\times K$, stride $S$:\n$$y_{i, j} = \\max_{0 \\le p, q < K} x_{i \\cdot S + p, j \\cdot S + q}$$\nĐặc tính quan trọng: Max Pooling KHÔNG CÓ THAM SỐ HỌC ĐƯỢC (Parameters = 0). Nó tạo ra tính bất biến với dịch chuyển nhỏ. Chọn **B** (Tạo tính bất biến với phép tịnh tiến nhỏ).",
        "- **Phương án A (Tăng số kênh):** Sai, Max Pooling giữ nguyên số kênh $C$, chỉ giảm $W$ và $H$.\n- **Phương án C (Tăng số tham số):** Sai, Max Pooling có 0 tham số.\n- **Phương án D:** Không có khả năng loại bỏ hoàn toàn nhiễu hạt.",
        "📚 Xem **§3.1 Convolution, Stride, Padding & Receptive Field**.\n🔗 **Liên hệ bài cũ:** Khác với Max Pooling (chọn đặc trưng nổi bật nhất), Average Pooling tính trung bình nên làm mịn ảnh, thường được dùng ở tầng cuối cùng (Global Average Pooling) để thay thế tầng Dense cồng kềnh."
    ),
    "VOAI03-M25": (
        "- **YOLO (You Only Look Once):** Mô hình phát hiện vật thể dạng một giai đoạn (Single-stage Object Detector) do Joseph Redmon đề xuất năm 2016.\n- **Single-stage Detector:** Dự đoán trực tiếp tọa độ hộp bao (Bounding Box) và nhãn lớp trong MỘT lượt truyền thẳng duy nhất qua mạng.\n- **Two-stage Detector:** Gồm 2 bước riêng biệt: Bước 1 sinh vùng đề xuất (Region Proposals qua RPN), Bước 2 phân loại và tinh chỉnh hộp (như Faster R-CNN).",
        "YOLO giống như một tay súng thiện xạ nhìn lướt qua một căn phòng: Trong chớp mắt (một cái nhìn duy nhất), tay súng nhìn thấy toàn bộ đồ vật và vị trí của chúng cùng một lúc. Trong khi đó, Faster R-CNN giống như một nhà thám tử: Trước tiên dùng kính lúp khoanh vùng 2,000 điểm đáng ngờ, rồi mới đi kiểm tra từng điểm một $\\implies$ YOLO chạy nhanh gấp nhiều lần, phù hợp thời gian thực (Real-time)!",
        "YOLO chia ảnh thành lưới $S \\times S$. Mỗi ô lưới dự đoán $B$ hộp bao và xác suất của $C$ lớp. Toàn bộ quá trình được giải quyết như một bài toán hồi quy đơn lẻ qua hàm mất mát đa thành phần. Chọn **B** (Single-stage Detector).",
        "- **Phương án A (Two-stage Detector):** Là đặc trưng của họ R-CNN (R-CNN, Fast R-CNN, Faster R-CNN).\n- **Phương án C (Anchor-free duy nhất):** YOLO nguyên bản (v1-v5) sử dụng Anchor Boxes, không phải anchor-free thuần túy.\n- **Phương án D:** YOLO là mạng nơ-ron học sâu hoàn chỉnh.",
        "📚 Xem **§3.3 Nhận diện & Định vị vật thể (Object Detection)**.\n🔗 **Liên hệ bài cũ:** Nhớ bảng so sánh: Two-stage (Faster R-CNN) chính xác hơn nhưng chậm (5-15 FPS); Single-stage (YOLO, SSD) cực nhanh (30-140 FPS), lý tưởng cho camera giám sát và xe tự hành."
    ),
    "VOAI03-M26": (
        "- **NMS (Non-Maximum Suppression):** Thuật toán hậu xử lý trong Object Detection nhằm loại bỏ các hộp bao dư thừa trùng lặp trên cùng một vật thể.\n- **IoU (Intersection over Union):** Tỉ lệ diện tích giao trên diện tích hợp giữa 2 hộp bao: $\\text{IoU} = \\frac{|A \\cap B|}{|A \\cup B|}$.\n- **Cơ chế NMS:** Sắp xếp các hộp theo điểm tin cậy (Confidence Score) giảm dần. Chọn hộp cao nhất, loại bỏ tất cả các hộp khác có $\\text{IoU} > \\text{threshold}$ với hộp đó.",
        "Khi mô hình nhìn thấy một con mèo, nó có thể vẽ ra 50 chiếc hộp bao quanh con mèo đó với điểm số chênh lệch nhau một chút. NMS hoạt động như một trọng tài nghiêm khắc: Giữ lại duy nhất chiếc hộp đẹp nhất (điểm cao nhất), và xóa sổ tất cả các chiếc hộp khác bị chồng lấn quá nhiều lên nó!",
        "Thuật toán NMS:\n1. Chọn hộp $B_{max} = \\arg\\max \\text{score}(B)$.\n2. Thêm $B_{max}$ vào danh sách giữ lại.\n3. Với mọi hộp $B_i$ còn lại, nếu $\\text{IoU}(B_{max}, B_i) > \\tau$ (thường là 0.45 hoặc 0.5), loại bỏ $B_i$.\n4. Lặp lại cho đến khi hết hộp. Chọn **A** (Loại bỏ các hộp bao trùng lặp trên cùng một vật thể).",
        "- **Phương án B:** Tăng số lượng hộp là sai (NMS làm giảm số lượng hộp).\n- **Phương án C:** NMS là thuật toán hậu xử lý heuristic, không dùng để huấn luyện bộ phân loại.\n- **Phương án D:** NMS không phải phép tăng cường dữ liệu.",
        "📚 Xem **§3.3 Nhận diện & Định vị vật thể (Object Detection)**.\n🔗 **Liên hệ bài cũ:** Biến thể Soft-NMS không xóa hẳn các hộp lân cận mà chỉ giảm điểm tin cậy của chúng theo hàm Gauss, giúp không bỏ sót hai vật thể đứng sát đè lên nhau."
    ),
    "VOAI03-M27": (
        "- **Model Quantization (Lượng hóa mô hình):** Kỹ thuật chuyển đổi trọng số và giá trị kích hoạt từ số thực độ chính xác cao (FP32 hoặc FP16) sang số nguyên ít bit hơn (như INT8 hoặc FP4/INT4).\n- **Post-Training Quantization (PTQ):** Lượng hóa sau khi đã huấn luyện xong.\n- **Quantization-Aware Training (QAT):** Mô phỏng làm tròn số ngay trong quá trình huấn luyện để giữ độ chính xác cao nhất.",
        "Lượng hóa giống như việc bạn ghi lại số đo chiều cao: Thay vì ghi chi tiết đến từng phần triệu milimét (1.7523948 mét - tốn 32 chữ số), bạn làm tròn thành 1.75 mét (chỉ tốn 8 chữ số). Kích thước file giảm đi 4 lần, tiết kiệm bộ nhớ RAM/VRAM và giúp truyền tải dữ liệu nhanh gấp 4 lần trên chip máy tính!",
        "Công thức lượng hóa tuyến tính đối xứng:\n$$q = \\text{clamp}\\left(\\left\\lfloor \\frac{x}{S} \\right\\rceil, -128, 127\\right)$$\nTrong đó $S$ là hệ số tỉ lệ (Scale factor). Lợi ích lớn nhất là giảm dung lượng bộ nhớ VRAM và băng thông bộ nhớ (Memory Bandwidth) tới 75%. Chọn **A** (Giảm dung lượng bộ nhớ và tăng tốc độ suy luận).",
        "- **Phương án B:** Lượng hóa có thể làm suy giảm nhẹ độ chính xác (Accuracy), không làm tăng.\n- **Phương án C:** Lượng hóa không làm tăng số lượng tham số.\n- **Phương án D:** Lượng hóa dùng cho suy luận (Inference), không làm tăng tốc độ huấn luyện.",
        "📚 Xem **§2.8 Tối ưu hóa mô hình & MLOps Deployment**.\n🔗 **Liên hệ bài cũ:** Lưu ý bẫy đề thi nâng cao: Nếu phần cứng không có nhân xử lý INT8 chuyên dụng (như Tensor Cores), CPU phải giải lượng hóa (Dequantize) ngược lại về FP32, có thể làm tăng độ trễ suy luận!"
    ),
    "VOAI03-M28": (
        "- **Data Drift (Trôi dạt dữ liệu / Covariate Shift):** Hiện tượng phân phối của dữ liệu đầu vào $P(X)$ thay đổi theo thời gian giữa tập huấn luyện và môi trường thực tế ($P_{\\text{train}}(X) \\ne P_{\\text{serve}}(X)$), trong khi quan hệ $P(y|X)$ vẫn giữ nguyên.\n- **Concept Drift:** Bản chất quan hệ mục tiêu thay đổi ($P_{\\text{train}}(y|X) \\ne P_{\\text{serve}}(y|X)$).\n- **Công cụ phát hiện:** Kiểm định Kolmogorov-Smirnov (KS-test), Population Stability Index (PSI).",
        "Tưởng tượng bạn dạy một mô hình nhận diện phong cách thời trang dựa trên ảnh chụp năm 2010. Đến năm 2026, giới trẻ chuyển sang mặc phong cách hoàn toàn mới (quần áo, kiểu tóc, phụ kiện thay đổi). Dữ liệu đầu vào thực tế đã 'trôi dạt' sang một vùng hoàn toàn xa lạ so với những gì mô hình từng được học trong quá khứ $\\implies$ Mô hình dự đoán sai liên tục!",
        "Khi xảy ra Data Drift, kiểm định thống kê khoảng cách Wasserstein hoặc PSI giữa hai phân phối sẽ vượt ngưỡng báo động (thường $\\text{PSI} > 0.2$), kích hoạt pipeline tự động thu thập dữ liệu mới và huấn luyện lại mô hình (Continuous Training - CT). Chọn **C** (Sự thay đổi phân phối của dữ liệu đầu vào theo thời gian).",
        "- **Phương án A:** Dữ liệu bị mất mát là lỗi thiếu giá trị (Missing Data), không phải Drift.\n- **Phương án B:** Mô hình bị lỗi code là Bug phần mềm.\n- **Phương án D:** Dữ liệu bị overfitting là lỗi mô hình, không phải đặc tính trôi dạt dữ liệu.",
        "📚 Xem **§2.8 Tối ưu hóa mô hình & MLOps Deployment**.\n🔗 **Liên hệ bài cũ:** Trong các hệ thống AI thực chiến, hệ thống giám sát (Monitoring) phải liên tục theo dõi Data Drift để tự động phát cảnh báo trước khi hiệu năng mô hình bị suy thoái nghiêm trọng."
    ),
    "VOAI03-M29": (
        "- **MLOps (Machine Learning Operations):** Bộ quy chuẩn, công cụ và quy trình kết hợp giữa Machine Learning, DevOps và Kỹ thuật dữ liệu (Data Engineering).\n- **Mục tiêu:** Tự động hóa và vận hành vòng đời của mô hình AI: Thu thập dữ liệu $\\to$ Huấn luyện (CI/CD/CT) $\\to$ Đóng gói $\\to$ Triển khai Serving $\\to$ Giám sát Drift & Tự động huấn luyện lại.",
        "MLOps giống như quy trình biến một công thức nấu ăn ngon của một đầu bếp trong gia đình (mô hình AI trong notebook) thành một dây chuyền nhà máy sản xuất thực phẩm tự động phục vụ hàng triệu người tiêu dùng mỗi ngày: Đảm bảo nguyên liệu luôn tươi sạch, dây chuyền không bao giờ ngừng hoạt động và chất lượng món ăn luôn đồng đều!",
        "MLOps = Machine Learning + Operations. Chọn **C** (Machine Learning Operations).",
        "- **Phương án A (Machine Learning Optimization):** Tối ưu hóa ML chỉ là một phần nhỏ trong thuật toán.\n- **Phương án B (Machine Learning Operators):** Các toán tử toán học.\n- **Phương án D:** Từ viết tắt giả định.",
        "📚 Xem **§2.8 Tối ưu hóa mô hình & MLOps Deployment**.\n🔗 **Liên hệ bài cũ:** Bộ công cụ MLOps tiêu chuẩn hiện nay gồm: MLflow (quản lý thí nghiệm), DVC (phiên bản dữ liệu), Kubeflow (pipeline container), Prometheus/EvidentlyAI (giám sát drift)."
    ),
    "VOAI03-M30": (
        "- **LLM Serving:** Việc triển khai mô hình ngôn ngữ lớn để phục vụ yêu cầu của người dùng thời gian thực.\n- **KV Cache (Key-Value Caching):** Lưu lại các vector Key và Value của các token trước đó trong quá trình sinh từ tự hồi quy (Autoregressive) để không phải tính lại từ đầu.\n- **PagedAttention (vLLM):** Thuật toán quản lý bộ nhớ KV Cache lấy cảm hứng từ kỹ thuật phân trang bộ nhớ ảo của hệ điều hành, giảm phân mảnh bộ nhớ từ 60-80% xuống dưới 4%.\n- **Continuous Batching:** Gom cụm động các request đến lệch thời điểm theo từng bước sinh token.",
        "Mỗi khi LLM sinh ra một từ mới, nó phải nhớ lại toàn bộ các từ đã nói trước đó. Nếu không có bộ nhớ tạm (KV Cache), mỗi từ mới sinh ra mô hình đều phải đọc lại cuốn sách từ trang đầu tiên! Kỹ thuật PagedAttention giống như việc chia cuốn sổ tay thành các trang giấy rời được đánh số: Cần viết thêm chữ thì cấp phát đúng 1 trang nhỏ, không để thừa trang giấy trắng lãng phí bộ nhớ VRAM đắt đỏ!",
        "Nhờ PagedAttention và Continuous Batching, hệ thống vLLM tăng thông lượng (Throughput) phục vụ LLM lên gấp 2-4 lần so với các hệ thống thông thường. Chọn **A** (PagedAttention và Continuous Batching trong vLLM).",
        "- **Phương án B (Chạy tuần tự từng request):** Làm lãng phí GPU và nghẽn mạng nghiêm trọng.\n- **Phương án C (Tắt hoàn toàn KV cache):** Khiến độ phức tạp tính toán tăng vọt thành $O(N^2)$ cho mỗi token, làm suy giảm tốc độ sinh từ.",
        "📚 Xem **§4.5 Large Language Models & Efficient Serving**.\n🔗 **Liên hệ bài cũ:** Nhớ bản chất: KV Cache đánh đổi bộ nhớ VRAM để tiết kiệm phép tính FLOPs (tăng tốc độ sinh token)."
    )
}

# Cập nhật vào exam_data
qs = exam_data["questions"]
count = 0
for q in qs:
    qid = q["id"]
    if qid in UPGRADES_REMAINING:
        term, eli5, math, trap, ref = UPGRADES_REMAINING[qid]
        new_exp = f"""### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
👶 **Thuật ngữ mới cần hiểu trước:**
{term}

🍼 **Hình dung thực tế cho em bé:**
{eli5}

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
📐 {math}

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
⚠️ **Phân tích bẫy đề thi & Phương án gây nhiễu:**
{trap}

### 4. Mắt xích kiến thức & Liên hệ bài cũ
{ref}"""
        q["explanation"] = new_exp
        count += 1

print(f"Đã nâng cấp thêm {count} câu (M21-M30) trong Đề 03!")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)
