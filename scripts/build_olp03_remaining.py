# -*- coding: utf-8 -*-
"""
Script xây dựng 50 câu còn lại (Q51-Q100) cho Đề 03 của thầy Đỗ Đình Luật.
Đầy đủ công thức KaTeX, lời giải 4 khối học thuật, và liên kết mục lý thuyết §x.y tương ứng video YouTube.
"""

import json
import os
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
EXAM_PATH = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")
TEMP_DATA = os.path.join(ROOT_DIR, "temp_q51_q100.json")

with open(TEMP_DATA, "r", encoding="utf-8") as f:
    raw_qs = json.load(f)

# Metadata tri thức chuẩn mực cho 50 câu (51..100)
# Mỗi câu gồm:
# - category/topic
# - section_ref: mục lý thuyết tương ứng trong sổ tay để map video YouTube
# - math_katex: công thức toán chủ đạo
# - eli5: giải thích trực quan, bình dân
# - step_by_step: phân tích học thuật, các bước tính
# - pitfalls: cạm bẫy hay gặp
# - references: bài báo / tài liệu tham chiếu chuẩn

KNOWLEDGE_DB = {
    51: {
        "sec": "§3.1",
        "mod": "B",
        "eli5": "Thay vì duỗi thẳng (flatten) toàn bộ feature map thành một hàng dài tạo ra hàng triệu trọng số kết nối ở lớp Fully Connected, Global Average Pooling (GAP) chỉ đơn giản lấy trung bình cộng tất cả các điểm ảnh trên mỗi kênh (channel). Nếu có 512 kênh, GAP cho ra đúng một vector 512 phần tử, không tốn thêm bất kỳ tham số học nào!",
        "step": "Cho tensor đặc trưng đầu ra của lớp conv cuối $X \\in \\mathbb{R}^{H \\times W \\times C}$. Phép tính GAP trên từng kênh $c \\in [1, C]$ là:\n$$z_c = \\frac{1}{H \\cdot W} \\sum_{h=1}^H \\sum_{w=1}^W X_{h,w,c}$$\nVector kết quả $z = [z_1, z_2, \\dots, z_C]^T$ có số chiều đúng bằng $C$. Số tham số thêm vào là $0$, giúp giảm đột biến dung lượng mô hình và hạn chế tối đa Overfitting.",
        "pit": "Nhiều bạn nhầm GAP với Flatten hoặc Max Pooling. Flatten nối tất cả $H \\times W \\times C$ giá trị lại thành vector dài, dẫn tới ma trận trọng số ở lớp FC cực lớn ($H \\cdot W \\cdot C \\times K$). GAP không có tham số học và ép mỗi feature map tương ứng với một độ tin cậy của đặc trưng.",
        "ref": "Lin, M., Chen, Q., & Yan, S. (2013). Network In Network. ICLR 2014. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**."
    },
    52: {
        "sec": "§2.2",
        "mod": "B",
        "eli5": "Một Epoch giống như việc bạn đọc xong một lượt từ trang đầu đến trang cuối của một cuốn sách giáo khoa. Tức là toàn bộ các mẫu dữ liệu trong tập huấn luyện (training set) đều đã được mô hình 'nhìn thấy' và học qua đúng 1 lần.",
        "step": "Giả sử tập train có $N$ mẫu, kích thước mini-batch là $B$. Số bước lặp (iterations/steps) trong $1$ Epoch là:\n$$\\text{Steps per Epoch} = \\left\\lceil \\frac{N}{B} \\right\\rceil$$\nSau khi mô hình chạy hết số bước này, toàn bộ $N$ mẫu đã được duyệt qua đúng một chu kỳ trọn vẹn.",
        "pit": "Dễ nhầm giữa Epoch (toàn bộ dữ liệu) và Iteration/Step (chỉ một mini-batch gồm $B$ mẫu). Nếu $N = 10,000, B = 32$, một epoch cần 313 iterations.",
        "ref": "Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**."
    },
    53: {
        "sec": "§3.2",
        "mod": "C",
        "eli5": "Trong bài toán phát hiện đối tượng, các ô nền (background) quá nhiều và quá dễ nhận biết khiến mô hình bị áp đảo bởi các mẫu dễ, bỏ quên các vật thể nhỏ/hiếm. Focal Loss thêm một 'bộ điều tiết' $(1 - p_t)^\\gamma$: mẫu nào mô hình đã đoán đúng và tự tin ($p_t \\to 1$) thì phạt cực nhỏ, tập trung toàn bộ gradient vào các mẫu khó ($p_t$ thấp)!",
        "step": "Công thức Focal Loss cho bài toán phân loại nhị phân:\n$$\\text{FL}(p_t) = -\\alpha_t (1 - p_t)^\\gamma \\log(p_t)$$\nTrong đó:\n- $p_t$ là xác suất dự đoán cho lớp đúng.\n- $\\gamma \\ge 0$ là siêu tham số điều chế độ tập trung (focusing parameter). Khi $\\gamma = 2$, nếu mô hình dự đoán mẫu dễ với $p_t = 0.9$, hệ số phạt giảm đi $(1 - 0.9)^2 = 0.01$ (giảm 100 lần so với Cross-Entropy thông thường!).",
        "pit": "Focal Loss không dùng để tăng tốc độ tính toán hay làm sâu mạng, mà là vũ khí đặc trị mất cân bằng lớp cực đoan (Class Imbalance) giữa tiền cảnh và hậu cảnh (Foreground-Background).",
        "ref": "Lin, T. Y., et al. (2017). Focal Loss for Dense Object Detection (RetinaNet). ICCV 2017. Xem **§3.2 Định vị & Phát hiện đối tượng**."
    },
    54: {
        "sec": "§3.3",
        "mod": "C",
        "eli5": "Vision Transformer (ViT) không dùng phép tích chập (Convolution) để quét ảnh. Thay vào đó, nó cắt bức ảnh thành các ô vuông nhỏ giống như các mảnh ghép xếp hình (ví dụ $16 \\times 16$ pixel), duỗi thẳng từng mảnh thành vector rồi coi mỗi mảnh như một 'từ' (token) đưa vào mô hình Transformer tiêu chuẩn!",
        "step": "Cho ảnh đầu vào $X \\in \\mathbb{R}^{H \\times W \\times C}$ và kích thước mảnh $P \\times P$.\n1. Số lượng mảnh patch là:\n$$N = \\frac{H \\cdot W}{P^2}$$\n2. Mỗi mảnh được duỗi thẳng thành vector chiều dài $P^2 \\cdot C$, sau đó chiếu tuyến tính qua ma trận $E \\in \\mathbb{R}^{(P^2 C) \\times D}$ để tạo patch embeddings.\n3. Thêm token phân loại $[\\text{CLS}]$ và Position Embedding $E_{pos} \\in \\mathbb{R}^{(N+1) \\times D}$ trước khi đưa vào Transformer Encoder.",
        "pit": "ViT không giữ nguyên ma trận ảnh 2D khi đưa vào Encoder và cũng không dùng 50 lớp CNN. Điểm đột phá của ViT là chuyển đổi không gian ảnh 2D thành chuỗi 1D các patch tokens.",
        "ref": "Dosovitskiy, A., et al. (2020). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. ICLR 2021. Xem **§3.3 Kiến trúc CV SOTA**."
    },
    55: {
        "sec": "§1.6",
        "mod": "B",
        "eli5": "Weight Decay giống như một lực kéo vô hình luôn kéo độ lớn của các trọng số mạng về số 0 sau mỗi bước cập nhật. Nó tương đương toán học với kỹ thuật điều quy L2 (L2 Regularization), ngăn các trọng số tăng quá lớn dẫn tới ghi nhớ dữ liệu (Overfitting).",
        "step": "Hàm mục tiêu điều quy L2:\n$$J_{\\text{reg}}(\\theta) = J(\\theta) + \\frac{\\lambda}{2} \\|w\\|_2^2 = J(\\theta) + \\frac{\\lambda}{2} \\sum_i w_i^2$$\nQuy tắc cập nhật trọng số với đạo hàm:\n$$w \\leftarrow w - \\eta \\left( \\nabla J(w) + \\lambda w \\right) = (1 - \\eta \\lambda) w - \\eta \\nabla J(w)$$\nHệ số $(1 - \\eta \\lambda) < 1$ làm suy giảm (decay) trọng số $w$ tỷ lệ thuận với giá trị hiện tại của nó.",
        "pit": "L1 ép trọng số về chính xác $0$ (tạo thưa thớt - sparsity), còn L2 (Weight Decay) ép trọng số tiến gần về $0$ một cách mượt mà chứ không hoàn toàn triệt tiêu.",
        "ref": "Krogh, A., & Hertz, J. A. (1992). A Simple Weight Decay Can Improve Generalization. NeurIPS 1991. Xem **§1.6 Điều quy L1/L2 & Biến dạng dữ liệu**."
    },
    56: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Bag of Words (BoW) giống như việc bạn gom tất cả các từ trong một bài văn vứt vào một cái bao rồi xáo trộn lên: Bạn biết trong bao có từ 'không', có từ 'ngon', có từ 'rất', nhưng không thể biết là 'rất ngon, không dở' hay 'không ngon, rất dở'! Nó đánh mất hoàn toàn thứ tự từ và ngữ cảnh câu.",
        "step": "Mô hình BoW biểu diễn văn bản thành vector tần suất $v \\in \\mathbb{R}^{|V|}$:\n$$v_i = \\text{count}(\\text{word}_i, \\text{doc})$$\nDo chỉ đếm số lần xuất hiện rời rạc, hai câu có ý nghĩa trái ngược nhau hoàn toàn như 'Tôi yêu bạn không ghét' và 'Tôi ghét bạn không yêu' sẽ có cùng một vector biểu diễn BoW!",
        "pit": "BoW tính toán rất nhanh (đếm từ) và áp dụng được cho mọi ngôn ngữ, nhưng khuyết điểm cốt tử là hoàn toàn bỏ qua trật tự cú pháp và cấu trúc ngữ nghĩa.",
        "ref": "Jurafsky, D., & Martin, J. H. (2024). Speech and Language Processing (3rd ed.). Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    57: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Trong Word2Vec, nếu CBOW (Continuous Bag of Words) nhìn các từ xung quanh để đoán từ ở giữa, thì Skip-gram làm ngược lại hoàn toàn: Nó lấy từ ở giữa (từ trung tâm) và cố gắng 'phóng tầm nhìn' dự đoán xem những từ nào có khả năng cao xuất hiện xung quanh nó!",
        "step": "Hàm mục tiêu của Skip-gram là cực đại hóa log-likelihood trên toàn bộ chuỗi từ $w_1, w_2, \\dots, w_T$ với cửa sổ ngữ cảnh kích thước $c$:\n$$\\mathcal{L} = \\sum_{t=1}^T \\sum_{-c \\le j \\le c, j \\ne 0} \\log P(w_{t+j} \\mid w_t)$$\nTrong đó xác suất có điều kiện được tính bằng softmax:\n$$P(w_O \\mid w_I) = \\frac{\\exp(v_{w_O}'^T v_{w_I})}{\\sum_{w \\in V} \\exp(v_w'^T v_{w_I})}$$",
        "pit": "Nhiều bạn nhầm lẫn giữa CBOW và Skip-gram. Hãy nhớ mẹo: CBOW = Context predicts Target; Skip-gram = Single target predicts Context (Skip-gram học từ hiếm tốt hơn nhiều!).",
        "ref": "Mikolov, T., et al. (2013). Distributed Representations of Words and Phrases and their Compositionality. NeurIPS 2013. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    58: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Stemming giống như dùng một cây kéo cơ học cắt phéng đuôi từ (ví dụ 'studies', 'studying' bị cắt thành 'studi' - một từ không có nghĩa trong từ điển). Trong khi đó, Lemmatization dùng một cuốn từ điển chuẩn và ngữ pháp để đưa từ về nguyên thể chuẩn mực ('studies' -> 'study').",
        "step": "So sánh hai phương pháp tiền xử lý:\n- **Stemming (vd: Porter, Snowball):** Sử dụng tập luật heuristic dựa trên hậu tố string (cắt bỏ 'ing', 'ed', 'es'). Tốc độ rất nhanh nhưng hay tạo ra từ vô nghĩa hoặc over-stemming / under-stemming.\n- **Lemmatization (vd: WordNetLemmatizer):** Phân tích hình thái học (morphological analysis) kết hợp với nhãn từ loại (Part-of-Speech / POS tag) để tra cứu lemma gốc có nghĩa trong từ điển ngữ liệu.",
        "pit": "Không phải Stemming luôn tốt hơn. Lemmatization chính xác hơn về mặt ngữ nghĩa nhưng tốn tài nguyên và thời gian hơn vì phải phân tích từ loại.",
        "ref": "Manning, C. D., et al. (2008). Introduction to Information Retrieval. Cambridge University Press. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    59: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "TF-IDF viết tắt của Term Frequency - Inverse Document Frequency. Ý tưởng cốt lõi: Một từ xuất hiện nhiều lần trong văn bản hiện tại (TF cao) nhưng lại hiếm khi xuất hiện ở các văn bản khác trong thư viện (IDF cao) thì từ đó là từ khóa cực kỳ đặc trưng và quan trọng!",
        "step": "Công thức TF-IDF cho từ $t$ trong tài liệu $d$ thuộc tập tài liệu $D$ gồm $N = |D|$ văn bản:\n$$\\text{TF-IDF}(t, d, D) = \\text{TF}(t, d) \\times \\text{IDF}(t, D)$$\nTrong đó:\n$$\\text{TF}(t, d) = \\frac{f_{t,d}}{\\sum_{t' \\in d} f_{t',d}}, \\quad \\text{IDF}(t, D) = \\log \\left( \\frac{N}{|\\{d \\in D: t \\in d\\}| + 1} \\right)$$",
        "pit": "Các từ nối như 'và', 'thì', 'là' có TF rất cao nhưng xuất hiện trong hầu hết tài liệu nên IDF gần bằng 0, dẫn tới trọng số TF-IDF bị triệt tiêu thích đáng.",
        "ref": "Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval. Information Processing & Management. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    60: {
        "sec": "§4.2",
        "mod": "C",
        "eli5": "Mô hình Transformer gốc gồm 2 nửa: Encoder (hiểu câu) và Decoder (sinh câu tiếp theo). BERT (Bidirectional Encoder Representations from Transformers) chỉ sử dụng đúng phần Encoder. Nhờ vậy, nó có thể nhìn toàn bộ câu theo cả hai chiều (từ trái qua phải và từ phải qua trái đồng thời) để hiểu sâu sắc ngữ cảnh.",
        "step": "Kiến trúc BERT gồm một chuỗi các lớp Transformer Encoder xếp chồng lên nhau:\n$$\\text{Input} \\to [\\text{Patch / Token + Pos + Segment}] \\to \\text{Encoder}_1 \\to \\dots \\to \\text{Encoder}_L \\to \\text{Contextual Embeddings}$$\nTrong mỗi khối Encoder, cơ chế Self-Attention là không bị che (unmasked), cho phép token tại vị trí $i$ chú ý tới mọi token $j \\in [1, T]$ trong chuỗi.",
        "pit": "Nhầm BERT với GPT. GPT là kiến trúc Decoder-only (dùng Masked Self-Attention để tự hồi quy từ trái sang phải sinh từ). BERT là Encoder-only chuyên dùng để hiểu ngữ nghĩa (NLU - Natural Language Understanding).",
        "ref": "Devlin, J., et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL 2019. Xem **§4.2 Cơ chế Attention & Transformer**."
    },
    61: {
        "sec": "§4.2",
        "mod": "C",
        "eli5": "Masked Language Modeling (MLM) giống trò chơi điền từ vào chỗ trống: Người ta giấu đi một số từ trong câu bằng nhãn [MASK] (ví dụ: 'Hà Nội là [MASK] của Việt Nam') và bắt mô hình phải dựa vào cả từ đứng trước và từ đứng sau để đoán từ bị giấu đi là 'thủ đô'.",
        "step": "Chiến lược huấn luyện MLM của BERT:\n1. Chọn ngẫu nhiên $15\\%$ số token trong chuỗi đầu vào.\n2. Trong số $15\\%$ đó:\n   - $80\\%$ được thay bằng token đặc biệt `[MASK]`.\n   - $10\\%$ được thay bằng một token ngẫu nhiên bất kỳ.\n   - $10\\%$ được giữ nguyên không đổi.\n3. Hàm mất mát là Cross-Entropy chỉ tính trên các vị trí được chọn này:\n$$\\mathcal{L}_{\\text{MLM}} = -\\sum_{i \\in \\text{masked}} \\log P(x_i \\mid \\tilde{X})$$",
        "pit": "MLM không che toàn bộ các từ hay chỉ nhìn từ bên trái; ưu thế tuyệt đối của nó là khai thác ngữ cảnh hai chiều (bidirectional context) cùng lúc.",
        "ref": "Devlin, J., et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL 2019. Xem **§4.2 Cơ chế Attention & Transformer**."
    },
    62: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Nếu từ điển chỉ lưu các từ nguyên vẹn, gặp từ lạ mới toanh sẽ bị lỗi 'Out Of Vocabulary' (OOV). Kỹ thuật Subword Tokenization chia từ thành các mảnh nhỏ (như 'unbelievable' thành 'un', 'believ', 'able'). Nhờ đó, bất kỳ từ mới nào cũng có thể ghép lại từ các mảnh con đã biết!",
        "step": "Các thuật toán tách từ con (Subword Tokenization) tiêu biểu:\n- **BPE (Byte Pair Encoding):** Bắt đầu từ cấp độ ký tự, đếm và gộp lặp đi lặp lại cặp ký tự xuất hiện nhiều nhất (dùng trong GPT-2, RoBERTa).\n- **WordPiece:** Tương tự BPE nhưng chọn cặp ghép làm tăng likelihood của ngôn ngữ nhiều nhất (dùng trong BERT).\n- **SentencePiece / Unigram:** Coi khoảng trắng như một ký tự đặc biệt, tối ưu trên mô hình xác suất unigram.",
        "pit": "Subword không xóa bỏ từ hiếm mà phân rã từ hiếm thành các mảnh từ vựng con (subwords) có mặt trong kho từ điển cố định.",
        "ref": "Sennrich, R., et al. (2016). Neural Machine Translation of Rare Words with Subword Units. ACL 2016. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    63: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Perplexity (PPL) đo mức độ 'bối rối, lúng túng' của mô hình khi đoán từ tiếp theo. Nếu mô hình đoán từ nào cũng trúng phóc với xác suất cao, nó sẽ rất tự tin và ít bối rối, tức là PPL CÀNG THẤP THÌ MÔ HÌNH CÀNG GIỎI!",
        "step": "Công thức toán học của Perplexity trên chuỗi văn bản $W = (w_1, w_2, \\dots, w_N)$:\n$$\\text{PPL}(W) = \\exp \\left( -\\frac{1}{N} \\sum_{i=1}^N \\log P(w_i \\mid w_1, \\dots, w_{i-1}) \\right) = 2^{H(W)}$$\nTrong đó $H(W)$ là entropy chéo trung bình trên mỗi token. Khi mô hình dự đoán chính xác tuyệt đối ($P=1$), $\\log P = 0 \\implies \\text{PPL} = 1$ (mức lý tưởng nhỏ nhất).",
        "pit": "Bẫy đề thi: Thí sinh hay nhầm PPL giống như Accuracy (càng cao càng tốt). Ngược lại: Perplexity là hàm đo độ sai lệch/bối rối, PPL càng THẤP thì chất lượng mô hình ngôn ngữ càng CAO.",
        "ref": "Jurafsky, D., & Martin, J. H. (2024). Speech and Language Processing. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    64: {
        "sec": "§4.2",
        "mod": "C",
        "eli5": "Mạng RNN xử lý từng từ một theo thứ tự từ trái sang phải nên tự biết từ nào đứng trước. Nhưng Transformer xử lý tất cả các từ cùng một lúc (song song). Để mô hình biết được 'con mèo đuổi con chuột' khác với 'con chuột đuổi con mèo', người ta phải 'dán nhãn số thứ tự' (Positional Encoding) vào từng từ!",
        "step": "Hàm mã hóa vị trí sin-cosin kinh điển trong Vaswani et al. (2017) cho vị trí $pos$ và chiều vector $2i, 2i+1$:\n$$PE_{(pos, 2i)} = \\sin \\left( \\frac{pos}{10000^{2i/d_{\\text{model}}}} \\right)$$\n$$PE_{(pos, 2i+1)} = \\cos \\left( \\frac{pos}{10000^{2i/d_{\\text{model}}}} \\right)$$\nVector này được cộng trực tiếp vào token embedding: $X = X_{\\text{token}} + PE$.",
        "pit": "Positional Encoding không nhân vào vector mà được CỘNG trực tiếp vào token embedding, giúp mô hình học được mối quan hệ vị trí tương đối thông qua phép biến đổi tuyến tính.",
        "ref": "Vaswani, A., et al. (2017). Attention Is All You Need. NeurIPS 2017. Xem **§4.2 Cơ chế Attention & Transformer**."
    },
    65: {
        "sec": "§4.2",
        "mod": "C",
        "eli5": "GPT (Generative Pre-trained Transformer) là một 'nhà văn' tự động: nó đọc đoạn văn đã viết và nhiệm vụ duy nhất của nó là đoán xem từ tiếp theo nên là từ gì. Quá trình này lặp đi lặp lại từng từ một gọi là mô hình sinh tự hồi quy (Autoregressive Decoder-only).",
        "step": "Mục tiêu huấn luyện chuẩn của GPT là tối đa hóa log-likelihood nhân quả (Causal Language Modeling):\n$$\\mathcal{L}_{\\text{CLM}} = \\sum_{i=1}^T \\log P(x_i \\mid x_1, x_2, \\dots, x_{i-1})$$\nĐể thực hiện điều này, các lớp Self-Attention trong GPT áp dụng ma trận Mask tam giác trên (Causal Masking), gán $-\\infty$ cho tất cả các vị trí $j > i$ để ngăn mô hình 'nhìn trộm' từ tương lai.",
        "pit": "Khác với BERT (Encoder hai chiều), GPT là Decoder đơn hướng (chỉ nhìn từ quá khứ sang hiện tại để sinh từ tiếp theo).",
        "ref": "Radford, A., et al. (2018). Improving Language Understanding by Generative Pre-Training. OpenAI. Xem **§4.2 Cơ chế Attention & Transformer**."
    },
    66: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Named Entity Recognition (NER) giống như việc đọc một bài báo và lấy bút highlight tô màu các tên riêng: tên người (Nguyễn Văn A), tên địa điểm (Hà Nội), tên tổ chức (Đại học Quốc gia), mốc thời gian (2026).",
        "step": "Bài toán NER thường được mô hình hóa dưới dạng gán nhãn chuỗi (Sequence Tagging) dùng quy ước BIO (Begin, Inside, Outside):\n- `B-PER`: Bắt đầu tên người\n- `I-PER`: Phần tiếp theo tên người\n- `O`: Từ thông thường\nCác mô hình tiêu chuẩn giải quyết NER gồm BiLSTM-CRF hoặc BERT fine-tuning với phân loại token.",
        "pit": "NER không phải là phân loại cảm xúc câu (Sentiment Analysis) hay tóm tắt văn bản, mà là trích xuất và phân loại các thực thể định danh có tên trong văn bản.",
        "ref": "Lample, G., et al. (2016). Neural Architectures for Named Entity Recognition. NAACL 2016. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    67: {
        "sec": "§4.3",
        "mod": "C",
        "eli5": "RAG (Retrieval-Augmented Generation) giống như việc cho LLM làm bài thi có mở sách: Thay vì bắt mô hình phải ghi nhớ toàn bộ kiến thức vào bộ não (trọng số), khi người dùng hỏi, hệ thống sẽ chạy đi tìm các trang sách liên quan nhất trong thư viện rồi đưa cho LLM đọc và tổng hợp câu trả lời!",
        "step": "Quy trình 3 bước chuẩn của hệ thống RAG:\n1. **Index & Retrieve:** Mã hóa tài liệu bằng embedding model (Vector Database). Khi có câu hỏi $q$, truy vấn $k$ đoạn văn có độ tương đồng cosine cao nhất: $D = \\{d_1, \\dots, d_k\\}$.\n2. **Augment:** Ghép nối câu hỏi và ngữ liệu thành prompt: $P = [\\text{Context: } D; \\text{ Question: } q]$.\n3. **Generate:** Đưa prompt $P$ vào LLM sinh câu trả lời $y \\sim P_{\\text{LLM}}(y \\mid P)$.\nƯu điểm: Giảm triệt để ảo giác (Hallucination) và cập nhật kiến thức mới theo thời gian thực mà không cần retrain mô hình.",
        "pit": "RAG không đòi hỏi phải fine-tune lại các trọng số của LLM mỗi khi có dữ liệu mới. Toàn bộ thông tin mới được nạp động thông qua bối cảnh ngữ cảnh (In-context learning).",
        "ref": "Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS 2020. Xem **§4.3 Mô hình ngôn ngữ lớn (LLM)**."
    },
    68: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Khi dịch câu, nếu dùng thuật toán tham lam (Greedy Search), ở mỗi bước bạn chỉ chọn từ có xác suất cao nhất hiện tại, dễ dẫn tới ngõ cụt sai lầm sau đó. Beam Search thông minh hơn: Nó giữ lại một nhóm gồm $k$ câu dịch tốt nhất (gọi là beam width) cùng lúc, rồi mới chọn câu có điểm tích lũy cao nhất cuối cùng!",
        "step": "Thuật toán Beam Search với bề rộng chùm $B$:\nTại mỗi bước sinh $t$, với $B$ giả thuyết hiện tại, tính xác suất sinh từ tiếp theo cho toàn bộ từ điển $V$. Tính điểm log-probability tích lũy:\n$$\\text{Score}(y_1, \\dots, y_t) = \\sum_{i=1}^t \\log P(y_i \\mid y_{<i}, x)$$\nTrong số $B \\times |V|$ chuỗi ứng viên mở rộng, chỉ giữ lại đúng $B$ chuỗi có tổng điểm cao nhất để tiếp tục bước $t+1$.",
        "pit": "Beam Search với $B=1$ chính là Greedy Search. Khi $B \\to \\infty$, Beam Search tiến tới tìm kiếm vét cạn (Exhaustive Search). $B$ thường chọn từ 3 đến 5 trong dịch máy.",
        "ref": "Sutskever, I., et al. (2014). Sequence to Sequence Learning with Neural Networks. NeurIPS 2014. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    69: {
        "sec": "§4.1",
        "mod": "C",
        "eli5": "Stopwords (từ dừng) là những từ cực kỳ phổ biến trong ngôn ngữ (như 'và', 'thì', 'là', 'của', 'ở') xuất hiện ở khắp mọi nơi nhưng lại mang rất ít ý nghĩa đặc trưng để phân biệt nội dung các văn bản.",
        "step": "Trong các mô hình phân loại văn bản truyền thống (BoW, TF-IDF), việc loại bỏ stopwords giúp:\n1. Thu hẹp kích thước không gian từ điển $|V|$ đáng kể.\n2. Giảm độ thưa thớt của ma trận dữ liệu và tăng tốc độ tính toán.\n3. Ngăn các từ nối áp đảo tần suất của các từ khóa nội dung quan trọng.",
        "pit": "Trong các mô hình Transformer hiện đại (như BERT, GPT), người ta thường KHÔNG loại bỏ stopwords vì các từ nối đóng vai trò then chốt trong cấu trúc ngữ pháp và hiểu mối quan hệ nhân quả.",
        "ref": "Manning, C. D., et al. (2008). Introduction to Information Retrieval. Xem **§4.1 Xử lý ngôn ngữ tự nhiên & Mô hình chuỗi**."
    },
    70: {
        "sec": "§4.2",
        "mod": "C",
        "eli5": "Trong cơ chế Attention, hãy tưởng tượng bạn đi vào thư viện tìm sách:\n- **Query (Q):** Câu hỏi hoặc chủ đề bạn đang muốn tìm kiếm.\n- **Key (K):** Tên sách dán trên gáy ở các kệ để đối chiếu xem có khớp với câu hỏi của bạn không.\n- **Value (V):** Nội dung thực tế bên trong cuốn sách mà bạn sẽ rút ra đọc!",
        "step": "Công thức Scaled Dot-Product Attention:\n$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left( \\frac{Q K^T}{\\sqrt{d_k}} \\right) V$$\n1. $Q K^T$ tính mức độ tương đồng giữa Query và từng Key.\n2. Chia cho $\\sqrt{d_k}$ để giữ phương sai ổn định, chống bão hòa gradient ở Softmax.\n3. Softmax chuyển ma trận tương đồng thành các trọng số chú ý (tổng bằng 1).\n4. Nhân với $V$ để lấy tổ hợp tuyến tính các vector giá trị.",
        "pit": "Query là vector đi 'hỏi', Key là vector 'đối chiếu', và Value là vector 'chứa thông tin biểu diễn'. Đừng nhầm lẫn giữa vai trò của Query và Value.",
        "ref": "Vaswani, A., et al. (2017). Attention Is All You Need. NeurIPS 2017. Xem **§4.2 Cơ chế Attention & Transformer**."
    },
    71: {
        "sec": "§3.1",
        "mod": "B",
        "eli5": "Max Pooling giống như việc thu nhỏ bức ảnh: Nó chia feature map thành các ô nhỏ (ví dụ $2 \\times 2$) và chỉ chọn ra con số lớn nhất trong mỗi ô. Con số lớn nhất thể hiện đặc trưng mạnh nhất tại vùng đó, giúp giảm kích thước ảnh đi một nửa mà vẫn giữ nguyên thông tin cốt lõi.",
        "step": "Cho cửa sổ pooling kích thước $k \\times k$ trượt với bước nhảy $s$ trên feature map $X$:\n$$Y_{i,j} = \\max_{0 \\le m, n < k} X_{i \\cdot s + m, j \\cdot s + n}$$\nVới kernel $2 \\times 2, s=2$, chiều rộng và chiều cao giảm đi một nửa: $H_{\\text{out}} = \\lfloor H/2 \\rfloor, W_{\\text{out}} = \\lfloor W/2 \\rfloor$. Thao tác này không có tham số học (parameters = 0).",
        "pit": "Max Pooling không học thêm tham số trọng số nào, và nó giúp tăng tính bất biến tịnh tiến cục bộ (local translation invariance).",
        "ref": "LeCun, Y., et al. (1998). Gradient-based learning applied to document recognition. IEEE. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**."
    },
    72: {
        "sec": "§3.2",
        "mod": "C",
        "eli5": "Intersection over Union (IoU) đo độ trùng khớp giữa khung hình do AI vẽ và khung hình thật của con người: Bằng diện tích phần giao nhau chia cho diện tích phần hợp lại. Nếu $\\text{IoU} = 0.8$ (tức $80\\%$), hai khung gần như trùng khít lên nhau, chứng tỏ AI định vị cực kỳ chính xác!",
        "step": "Công thức tính IoU giữa bounding box dự đoán $B_p$ và nhãn thật $B_g$:\n$$\\text{IoU}(B_p, B_g) = \\frac{\\text{Area}(B_p \\cap B_g)}{\\text{Area}(B_p \\cup B_g)} = \\frac{\\text{Area}(B_p \\cap B_g)}{\\text{Area}(B_p) + \\text{Area}(B_g) - \\text{Area}(B_p \\cap B_g)}$$\nTrong chuẩn đánh giá Pascal VOC, ngưỡng chuẩn là $\\text{IoU} \\ge 0.5$. Trong MS COCO, ngưỡng tính từ $0.5$ đến $0.95$. Do đó $\\text{IoU} = 0.8$ là độ chuẩn xác định vị rất cao.",
        "pit": "IoU nằm trong đoạn $[0, 1]$. $\\text{IoU} = 0$ nghĩa là 2 khung không chạm nhau, $\\text{IoU} = 1$ nghĩa là 2 khung hoàn toàn trùng khít.",
        "ref": "Everingham, M., et al. (2010). The Pascal Visual Object Classes (VOC) Challenge. IJCV. Xem **§3.2 Định vị & Phát hiện đối tượng**."
    },
    73: {
        "sec": "§3.2",
        "mod": "C",
        "eli5": "YOLO viết tắt của 'You Only Look Once' (Bạn chỉ cần nhìn một lần): Khác với các mô hình 2 giai đoạn (như Faster R-CNN phải đề xuất vùng trước rồi mới phân loại), YOLO coi việc phát hiện vật thể như một bài toán hồi quy duy nhất: Đưa ảnh qua mạng một lần duy nhất là ra ngay cả vị trí tọa độ lẫn tên đồ vật, đạt tốc độ real-time siêu nhanh!",
        "step": "Nguyên lý YOLO chia ảnh thành lưới $S \\times S$. Mỗi ô lưới dự đoán đồng thời $B$ bounding boxes $(x, y, w, h, \\text{confidence})$ và xác suất các lớp $C$:\n$$\\text{Tensor đầu ra} \\in \\mathbb{R}^{S \\times S \\times (B \\times 5 + C)}$$\nToàn bộ quá trình tối ưu hóa bằng một hàm tổn thất đa nhiệm duy nhất (Multi-part Loss) gồm vị trí, kích thước, độ tin cậy và phân loại.",
        "pit": "YOLO thuộc họ 1-Stage Detector, ưu điểm số 1 là tốc độ cực nhanh (fps cao), phù hợp triển khai trên video thời gian thực hoặc thiết bị nhúng.",
        "ref": "Redmon, J., et al. (2016). You Only Look Once: Unified, Real-Time Object Detection. CVPR 2016. Xem **§3.2 Định vị & Phát hiện đối tượng**."
    },
    74: {
        "sec": "§3.2",
        "mod": "C",
        "eli5": "Anchor Boxes giống như việc người thợ may chuẩn bị sẵn các khung bìa mẫu với đủ kích cỡ (khung đứng cho người đi bộ, khung ngang cho xe hơi, khung vuông cho biển báo). Mạng AI không cần tự vẽ khung từ con số 0 mà chỉ cần học cách co giãn, tinh chỉnh các khung mẫu này để ôm khít đồ vật!",
        "step": "Các Anchor box $A = (w_a, h_a)$ đóng vai trò là khung tham chiếu ban đầu. Mạng nơ-ron học các độ lệch hồi quy (offsets):\n$$t_x = \\frac{x - x_a}{w_a}, \\quad t_y = \\frac{y - y_a}{h_a}, \\quad t_w = \\log\\left(\\frac{w}{w_a}\\right), \\quad t_h = \\log\\left(\\frac{h}{h_a}\\right)$$\nKhi suy luận, tọa độ thực tế được giải mã bằng hàm mũ: $w = w_a e^{t_w}, h = h_a e^{t_h}$.",
        "pit": "Anchor boxes được xác định trước (bằng thuật toán k-means clustering trên tập train hoặc cố định tỉ lệ), không phải là trọng số tự do được khởi tạo ngẫu nhiên.",
        "ref": "Ren, S., et al. (2015). Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. NeurIPS 2015. Xem **§3.2 Định vị & Phát hiện đối tượng**."
    },
    75: {
        "sec": "§3.2",
        "mod": "C",
        "eli5": "Semantic Segmentation (Phân đoạn ngữ nghĩa) giống như việc tô màu tranh theo mã số: Mỗi điểm ảnh (pixel) được gán đúng nhãn loại của nó (ví dụ tất cả các pixel thuộc về con chó được tô màu đỏ, cỏ tô màu xanh). Lưu ý rằng nếu có 2 con chó đứng cạnh nhau, chúng đều được tô chung màu đỏ mà không phân biệt con thứ nhất hay thứ hai!",
        "step": "Đầu ra của mô hình Semantic Segmentation là một bản đồ xác suất có kích thước bằng đúng ảnh gốc $Y \\in \\mathbb{R}^{H \\times W \\times C}$, trong đó tại mỗi tọa độ $(i, j)$:\n$$\\hat{y}_{i,j} = \\arg\\max_{c} P(\\text{class} = c \\mid X_{i,j})$$\nĐể phân biệt từng cá thể riêng biệt (con chó 1 vs con chó 2), người ta phải dùng Instance Segmentation (ví dụ Mask R-CNN).",
        "pit": "Phân biệt rõ: Semantic Segmentation gán nhãn pixel-level nhưng KHÔNG phân biệt các cá thể (instances) riêng lẻ trong cùng một lớp.",
        "ref": "Long, J., Shelhamer, E., & Darrell, T. (2015). Fully Convolutional Networks for Semantic Segmentation. CVPR 2015. Xem **§3.2 Định vị & Phát hiện đối tượng**."
    },
    76: {
        "sec": "§3.3",
        "mod": "C",
        "eli5": "U-Net có hình dáng chữ U đối xứng hoàn hảo: Nhánh bên trái co nhỏ ảnh lại để hiểu ngữ nghĩa tổng quát, nhánh bên phải phóng to ảnh trở lại kích thước gốc. Điều kỳ diệu là các đường 'cầu nối' (Skip Connections) dẫn thẳng thông tin chi tiết từng góc cạnh từ nhánh trái sang nhánh phải, giúp đường biên phân đoạn sắc nét tuyệt đối!",
        "step": "Kiến trúc U-Net gồm:\n1. **Contracting Path (Encoder):** Các lớp conv $3 \\times 3$ kèm Max Pooling $2 \\times 2$ trích xuất đặc trưng bậc cao và giảm độ phân giải.\n2. **Expansive Path (Decoder):** Các lớp Transposed Conv (Up-conv) $2 \\times 2$ khôi phục kích thước không gian.\n3. **Skip Connections:** Ghép nối tensor (concatenation) từ tầng encoder sang decoder cùng mức độ phân giải, bảo toàn nguyên vẹn tọa độ không gian chính xác.",
        "pit": "Trong U-Net, Skip Connection là phép nối kênh (Concatenation) dọc theo trục channel, khác với phép cộng phần tử (Addition) trong ResNet.",
        "ref": "Ronneberger, O., Fischer, P., & Brox, T. (2015). U-Net: Convolutional Networks for Biomedical Image Segmentation. MICCAI 2015. Xem **§3.3 Kiến trúc CV SOTA**."
    },
    77: {
        "sec": "§3.1",
        "mod": "B",
        "eli5": "Tính bất biến tịnh tiến (Translation Invariance) nghĩa là: Dù con mèo nằm ở góc trên bên trái hay chạy xuống góc dưới bên phải bức ảnh, mạng CNN vẫn nhận diện ra đó là con mèo! Đó là nhờ bộ lọc tích chập quét qua mọi vị trí trên ảnh với cùng một bộ trọng số chia sẻ (Weight Sharing).",
        "step": "Hai tính chất không gian nền tảng của mạng CNN:\n1. **Translation Equivariance (ở các tầng tích chập):** Nếu ảnh dịch chuyển $g(X)$, bản đồ đặc trưng cũng dịch chuyển tương ứng: $f(g(X)) = g(f(X))$.\n2. **Translation Invariance (sau khi qua Pooling / GAP):** Đầu ra phân loại không đổi khi vật thể dịch chuyển nhẹ: $f(g(X)) = f(X)$.",
        "pit": "MLP cổ điển không có tính chất này vì mỗi pixel nối với một trọng số riêng biệt, dịch chuyển ảnh 1 pixel là vector đầu vào thay đổi hoàn toàn.",
        "ref": "Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**."
    },
    78: {
        "sec": "§3.1",
        "mod": "B",
        "eli5": "Một bức ảnh xám 2 chiều có kích thước 28 hàng và 28 cột pixel. Tổng số điểm ảnh đơn giản là phép nhân diện tích hình chữ nhật: 28 nhân với 28 bằng đúng 784 điểm ảnh!",
        "step": "Kích thước ảnh xám (Grayscale): $H = 28, W = 28, C = 1$.\nTổng số pixel:\n$$N_{\\text{pixels}} = H \\times W \\times C = 28 \\times 28 \\times 1 = 784$$\nNếu ảnh màu RGB ($C=3$), số giá trị điểm ảnh sẽ là $28 \\times 28 \\times 3 = 2,352$.",
        "pit": "Đề bài nêu rõ là ảnh xám (grayscale) nên chỉ có 1 kênh màu duy nhất ($C=1$), không được nhân thêm 3 như ảnh màu RGB.",
        "ref": "LeCun, Y., et al. (1998). The MNIST Database of Handwritten Digits. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**."
    },
    79: {
        "sec": "§3.2",
        "mod": "C",
        "eli5": "Khi dò tìm một người, mô hình AI thường vẽ ra hàng chục khung bao chồng chéo lên nhau quanh người đó. Non-Maximum Suppression (NMS) đóng vai trò 'dọn dẹp': Nó chọn ra khung có điểm tự tin cao nhất, rồi xóa bỏ tất cả các khung khác có độ trùng lặp (IoU) quá cao với khung này, chỉ để lại duy nhất 1 khung đẹp nhất!",
        "step": "Thuật toán NMS chuẩn:\n1. Sắp xếp danh sách các khung $B$ theo điểm tự tin (confidence score) giảm dần.\n2. Chọn khung có điểm cao nhất $b_1$, đưa vào danh sách kết quả cuối cùng $D$ và xóa khỏi $B$.\n3. Tính IoU giữa $b_1$ và tất cả các khung $b_i \\in B$ còn lại.\n4. Nếu $\\text{IoU}(b_1, b_i) > \\text{threshold}$ (thường chọn $0.45 - 0.6$), xóa $b_i$ khỏi $B$.\n5. Lặp lại bước 2 đến khi danh sách $B$ trống.",
        "pit": "NMS là thuật toán hậu xử lý (Post-processing), không có đạo hàm huấn luyện trong các detector cổ điển, dùng để khử trùng lặp bounding box.",
        "ref": "Neubeck, A., & Van Gool, L. (2006). Efficient Non-Maximum Suppression. ICPR 2006. Xem **§3.2 Định vị & Phát hiện đối tượng**."
    },
    80: {
        "sec": "§3.1",
        "mod": "B",
        "eli5": "Dilated Convolution (tích chập giãn nở) giống như việc bạn kéo dãn chiếc kính lúp ra: Thay vì các điểm ảnh trong bộ lọc nằm dính sát nhau, nó tạo các khoảng trống giữa các điểm. Nhờ vậy, bộ lọc nhìn được một vùng ảnh rộng lớn hơn rất nhiều (Receptive Field to) mà không tốn thêm bất kỳ tham số hay phép nhân nào!",
        "step": "Với kernel kích thước $k \\times k$ và tỷ lệ giãn nở (dilation rate) $d$:\nKích thước kernel hiệu dụng (effective kernel size) là:\n$$k' = k + (k - 1)(d - 1)$$\nVí dụ với kernel $3 \\times 3$ và $d = 2$:\n$$k' = 3 + (3 - 1)(2 - 1) = 3 + 2 = 5$$\nTrường tiếp nhận mở rộng từ $3 \\times 3$ lên $5 \\times 5$ nhưng số tham số vẫn giữ nguyên $3 \\times 3 = 9$ trọng số.",
        "pit": "Dilated convolution không thêm tham số nào vào kernel; nó chỉ chèn các lỗ trống (holes / spaces) giữa các trọng số của kernel.",
        "ref": "Yu, F., & Koltun, V. (2015). Multi-Scale Context Aggregation by Dilated Convolutions. ICLR 2016. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**."
    },
    81: {
        "sec": "§3.2",
        "mod": "C",
        "eli5": "Trong bài toán phát hiện đồ vật, ta không thể dùng Accuracy đơn thuần. Thay vào đó, ta dùng mAP (mean Average Precision): Tính diện tích dưới đường cong đánh đổi giữa Precision (đoán trúng bao nhiêu) và Recall (bỏ sót bao nhiêu) cho từng loại đồ vật, rồi lấy trung bình cộng trên tất cả các lớp lại!",
        "step": "Quy trình tính mAP:\n1. Với mỗi lớp $c$, tính đường cong Precision-Recall bằng cách quét qua các ngưỡng confidence score.\n2. Tính Average Precision (AP) của lớp $c$ bằng tích phân hoặc nội suy 11 điểm:\n$$\\text{AP}_c = \\int_0^1 p(r) \\, dr$$\n3. Lấy trung bình cộng trên toàn bộ $C$ lớp đối tượng:\n$$\\text{mAP} = \\frac{1}{C} \\sum_{c=1}^C \\text{AP}_c$$",
        "pit": "mAP kết hợp cả khả năng phân loại lẫn độ chính xác định vị bounding box ở các ngưỡng IoU khác nhau (như mAP@0.5 hay mAP@[0.5:0.95]).",
        "ref": "Everingham, M., et al. (2010). The Pascal VOC Challenge. Xem **§3.2 Định vị & Phát hiện đối tượng**."
    },
    82: {
        "sec": "§3.1",
        "mod": "B",
        "eli5": "Tại đường biên của một đồ vật (cạnh cái bàn, mép cánh cửa), màu sắc và độ sáng đột ngột thay đổi từ tối sang sáng hoặc ngược lại. Bộ lọc Sobel tính đạo hàm xấp xỉ theo phương ngang và phương dọc để bắt trọn những vị trí có độ biến thiên ánh sáng mạnh nhất này!",
        "step": "Toán tử Sobel sử dụng hai ma trận kernel $3 \\times 3$ để tính xấp xỉ đạo hàm không gian:\n$$G_x = \\begin{bmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{bmatrix} * I, \\quad G_y = \\begin{bmatrix} -1 & -2 & -1 \\\\ 0 & 0 & 0 \\\\ 1 & 2 & 1 \\end{bmatrix} * I$$\nĐộ lớn gradient biên cạnh tổng hợp tại mỗi pixel:\n$$G = \\sqrt{G_x^2 + G_y^2}$$",
        "pit": "Toán tử Sobel là bộ lọc thủ công cổ điển (Handcrafted feature filter), giúp trực quan hóa cơ chế phát hiện biên cạnh mà các tầng đầu của CNN tự động học được.",
        "ref": "Sobel, I. (2014). An Isotropic 3x3 Image Gradient Operator. Xem **§3.1 Mạng nơ-ron tích chập (CNN)**."
    },
    83: {
        "sec": "§3.3",
        "mod": "C",
        "eli5": "Depthwise Separable Convolution là bí kíp giúp MobileNet chạy mượt mà trên điện thoại: Thay vì dùng một phép tích chập nặng nề vừa quét không gian vừa trộn kênh, nó tách làm 2 bước siêu nhẹ: Bước 1 lọc không gian từng kênh riêng lẻ (Depthwise), Bước 2 dùng kernel 1x1 để trộn các kênh lại (Pointwise)!",
        "step": "So sánh chi phí tính toán:\n- **Tích chập thông thường:** $D_K \\cdot D_K \\cdot M \\cdot N \\cdot D_F \\cdot D_F$\n- **Depthwise Separable Conv:**\n$$\\text{Cost} = D_K \\cdot D_K \\cdot M \\cdot D_F \\cdot D_F + M \\cdot N \\cdot D_F \\cdot D_F$$\nTỷ lệ tiết kiệm tính toán xấp xỉ:\n$$\\frac{\\text{Depthwise Separable}}{\\text{Standard Conv}} = \\frac{1}{N} + \\frac{1}{D_K^2}$$\nVới kernel $3 \\times 3$ ($D_K = 3$), lượng tính toán giảm từ 8 đến 9 lần mà độ chính xác gần như không suy giảm!",
        "pit": "Đây là nền tảng cốt lõi của họ kiến trúc MobileNet và Xception, giảm đột biến cả số tham số (parameters) lẫn số phép tính (FLOPs).",
        "ref": "Howard, A. G., et al. (2017). MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. arXiv:1704.04861. Xem **§3.3 Kiến trúc CV SOTA**."
    },
    84: {
        "sec": "§3.3",
        "mod": "C",
        "eli5": "Face Embedding nén toàn bộ đặc điểm khuôn mặt của một người thành một dãy số (ví dụ vector 512 chiều). Khuôn mặt của cùng một người ở các góc chụp khác nhau sẽ có vector nằm rất gần nhau trong không gian, còn khuôn mặt của người khác sẽ bị đẩy ra xa tít tắp!",
        "step": "Kỹ thuật Metric Learning (ArcFace / CosFace / Triplet Loss) tối ưu hóa khoảng cách không gian embedding:\n$$\\mathcal{L}_{\\text{triplet}} = \\max\\left(0, \\|f(x_a) - f(x_p)\\|_2^2 - \\|f(x_a) - f(x_n)\\|_2^2 + \\alpha\\right)$$\nTrong đó:\n- $x_a$: Ảnh neo (Anchor)\n- $x_p$: Ảnh cùng người (Positive)\n- $x_n$: Ảnh người khác (Negative)\n- $\\alpha$: Khoảng lề an toàn (margin).",
        "pit": "Trong nhận diện khuôn mặt thực tế, ta không huấn luyện Softmax phân loại từng người vì số người dùng luôn biến động; ta so sánh khoảng cách Cosine giữa các vector nhúng (Face Embeddings).",
        "ref": "Schroff, F., Kalenichenko, D., & Philbin, J. (2015). FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR 2015. Xem **§3.3 Kiến trúc CV SOTA**."
    },
    85: {
        "sec": "§2.2",
        "mod": "B",
        "eli5": "Trong bài toán đa nhãn (Multi-label - ví dụ một bức ảnh có thể vừa có 'chó', vừa có 'mèo', vừa có 'cây cỏ'), các nhãn này độc lập với nhau. Nếu dùng Softmax, tổng các xác suất bị ép bằng 1 (chó tăng thì mèo giảm). Do đó bắt buộc phải dùng Sigmoid riêng cho từng lớp để mỗi lớp tự do nhận giá trị xác suất từ 0 đến 1!",
        "step": "So sánh hàm kích hoạt ở lớp đầu ra:\n- **Multi-class (Độc quyền nhãn, 1 ảnh chỉ thuộc đúng 1 lớp):** Dùng Softmax:\n$$P(y = c \\mid x) = \\frac{e^{z_c}}{\\sum_{j=1}^C e^{z_j}}, \\quad \\sum_{c=1}^C P(y=c \\mid x) = 1$$\n- **Multi-label (Đa nhãn đồng thời, có thể chứa nhiều lớp cùng lúc):** Dùng Sigmoid độc lập (Binary Cross-Entropy trên từng lớp):\n$$P(y_c = 1 \\mid x) = \\sigma(z_c) = \\frac{1}{1 + e^{-z_c}}$$",
        "pit": "Lỗi kinh điển trong các đề thi OLP: Nhầm lẫn giữa Multi-class (chọn 1 trong nhiều, dùng Softmax) và Multi-label (chọn nhiều trong nhiều, dùng độc lập Sigmoid).",
        "ref": "Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**."
    },
    86: {
        "sec": "§1.5",
        "mod": "A",
        "eli5": "High Bias (độ chệch cao) chính là hiện tượng Underfitting (chưa học tới nơi tới chốn): Mô hình quá đơn giản (như dùng một đường thẳng để dự đoán một đám mây hình xoắn ốc), dẫn tới ngay cả trên tập luyện tập (Train set) nó cũng làm sai bét nhè!",
        "step": "Biểu hiện đặc trưng của High Bias (Underfitting):\n1. Training Error cao và Validation Error cũng cao xấp xỉ nhau.\n2. Tăng thêm dữ liệu huấn luyện hầu như không cải thiện được kết quả.\nBiện pháp khắc phục chuẩn:\n- Tăng độ phức tạp của mô hình (thêm tầng, thêm nơ-ron, tăng độ sâu cây).\n- Tạo thêm đặc trưng mới (Feature Engineering, tương tác bậc cao).\n- Giảm bớt ràng buộc điều quy (giảm hệ số $\\lambda$ của L1/L2, giảm Dropout).",
        "pit": "High Bias = Underfitting (mô hình quá cứng nhắc, học kém cả train lẫn val). High Variance = Overfitting (học vẹt, train điểm cực cao nhưng val điểm rất thấp).",
        "ref": "Hastie, T., et al. (2009). The Elements of Statistical Learning. Springer. Xem **§1.5 Đánh giá mô hình & Cross-Validation**."
    },
    87: {
        "sec": "§2.2",
        "mod": "B",
        "eli5": "SGD có Momentum giống như một hòn bi sắt lăn xuống dốc: Khi lăn xuống, nó tích lũy vận tốc và quán tính. Nhờ quán tính này, nó lăn vù qua những ổ gà gập ghềnh nhỏ (điểm cực tiểu cục bộ) và không bị lắc lư qua lại ở hai bên sườn núi hẹp, tiến nhanh về đáy vực!",
        "step": "Công thức cập nhật trọng số với Momentum:\n$$v_t = \\beta v_{t-1} + (1 - \\beta) g_t$$\n$$\\theta_t = \\theta_{t-1} - \\eta v_t$$\nTrong đó:\n- $g_t = \\nabla_\\theta J(\\theta)$ là gradient hiện tại.\n- $v_t$ là vector vận tốc tích lũy trung bình động mũ (EMA).\n- $\\beta \\in [0.9, 0.99]$ là hệ số quán tính (thường chọn $0.9$).",
        "pit": "Momentum không làm tăng learning rate ngẫu nhiên; nó khử dao động ở các hướng có độ cong cao và tăng tốc chuyển động theo hướng dốc nhất quán.",
        "ref": "Polyak, B. T. (1964). Some methods of speeding up the convergence of iteration methods. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**."
    },
    88: {
        "sec": "§1.5",
        "mod": "A",
        "eli5": "Grid Search giống như việc đi thử chìa khóa kiểu 'vét cạn': Bạn lập ra một cái bảng gồm tất cả các khả năng kết hợp của các siêu tham số (ví dụ learning rate = 0.01, 0.001; batch size = 16, 32, 64) và huấn luyện thử từng ô một trên lưới để tìm ra bộ thông số cho điểm cao nhất!",
        "step": "So sánh các chiến lược Hyperparameter Tuning:\n- **Grid Search:** Thử toàn bộ tích đề-các $\\mathcal{P} = P_1 \\times P_2 \\times \\dots \\times P_k$. Chi phí tính toán bùng nổ theo cấp số nhân số chiều $\\mathcal{O}(m^k)$.\n- **Random Search:** Lấy mẫu ngẫu nhiên trên phân phối siêu tham số, hiệu quả hơn Grid Search trong không gian nhiều chiều.\n- **Bayesian Optimization (Optuna, TPE):** Dựng mô hình xác suất học từ các lần thử trước để chọn điểm thử tiếp theo hứa hẹn nhất.",
        "pit": "Grid Search duyệt qua lưới tọa độ xác định trước một cách vét cạn thủ công, rất tốn thời gian tính toán khi không gian tìm kiếm lớn.",
        "ref": "Bergstra, J., & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. JMLR. Xem **§1.5 Đánh giá mô hình & Cross-Validation**."
    },
    89: {
        "sec": "§1.6",
        "mod": "A",
        "eli5": "Nếu dữ liệu có cột 'Tuổi' (từ 0 đến 100) và cột 'Thu nhập' (từ hàng triệu đến hàng trăm triệu), cột Thu nhập với những con số khổng lồ sẽ 'áp đảo' hoàn toàn gradient, làm mô hình học méo mó. Chuẩn hóa dữ liệu đưa mọi cột về cùng một thang đo (như từ 0 đến 1) để chúng công bằng bình đẳng!",
        "step": "Các phương pháp co giãn đặc trưng (Feature Scaling):\n1. **Standardization (Z-score):** Đưa về phân phối trung bình 0, phương sai 1:\n$$z = \\frac{x - \\mu}{\\sigma}$$\n2. **Min-Max Scaling:** Đưa về đoạn $[0, 1]$:\n$$x' = \\frac{x - x_{\\min}}{x_{\\max} - x_{\\min}}$$\nLợi ích cốt lõi: Làm đường đồng mức của hàm mất mát tròn đều hơn, giúp Gradient Descent hội tụ nhanh gấp nhiều lần và tránh tràn số.",
        "pit": "Không được fit scaler trên tập Test/Validation; chỉ được `fit` trên tập Train rồi dùng các giá trị $\\mu, \\sigma$ đó để `transform` cho tập Test nhằm tránh rò rỉ dữ liệu (Data Leakage).",
        "ref": "Hastie, T., et al. (2009). The Elements of Statistical Learning. Xem **§1.6 Điều quy L1/L2 & Biến dạng dữ liệu**."
    },
    90: {
        "sec": "§2.2",
        "mod": "B",
        "eli5": "Stochastic Gradient Descent (SGD thuần túy) là phiên bản 'vội vàng' nhất của tối ưu hóa: Cứ mỗi khi nhìn thấy đúng 1 mẫu dữ liệu duy nhất, nó tính ngay gradient và cập nhật trọng số luôn, không cần chờ đợi gom thành lô (batch)!",
        "step": "Quy tắc cập nhật của Pure SGD (Batch size = 1) tại mẫu $(x^{(i)}, y^{(i)})$:\n$$\\theta \\leftarrow \\theta - \\eta \\nabla_\\theta \\mathcal{L}(\\theta; x^{(i)}, y^{(i)})$$\nĐặc điểm: Cập nhật cực kỳ nhanh chóng nhưng gradient bị rung lắc rất mạnh (noisy) do từng mẫu đơn lẻ gây ra. Trong thực tế người ta dùng Mini-batch Gradient Descent (batch size $32, 64, 128$) để cân bằng giữa tính ổn định và khả năng tận dụng phần cứng GPU.",
        "pit": "Thuật ngữ SGD trong PyTorch thường được dùng chung cho Mini-batch Gradient Descent, nhưng theo định nghĩa giải thuật lý thuyết gốc, Pure SGD sử dụng đúng $1$ mẫu dữ liệu duy nhất cho mỗi lần cập nhật trọng số.",
        "ref": "Bottou, L. (2010). Large-scale machine learning with stochastic gradient descent. COMPSTAT 2010. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**."
    },
    91: {
        "sec": "§1.5",
        "mod": "A",
        "eli5": "Khi bạn làm bài ôn tập ở nhà được 10 điểm tuyệt đối, nhưng khi đi thi gặp đề mới thì chỉ được 3 điểm. Điều đó chứng tỏ bạn đã học vẹt (Overfitting): Mô hình ghi nhớ y nguyên tập dữ liệu luyện tập (Train) nhưng không hề có khả năng khái quát hóa trên dữ liệu thực tế (Validation/Test)!",
        "step": "Dấu hiệu chẩn đoán Overfitting trên đồ thị hàm mất mát theo Epoch:\n1. $\\mathcal{L}_{\\text{train}}$ tiếp tục giảm đều đặn tiến sát 0, $\\text{Acc}_{\\text{train}} \\to 100\\%$.\n2. $\\mathcal{L}_{\\text{val}}$ sau khi giảm tới một ngưỡng bắt đầu bật tăng trở lại, $\\text{Acc}_{\\text{val}}$ suy giảm hoặc chững lại.\nBiện pháp đặc trị:\n- Áp dụng Early Stopping (dừng huấn luyện khi val loss bắt đầu tăng).\n- Thêm điều quy L2 (Weight Decay) hoặc Dropout.\n- Tăng cường dữ liệu (Data Augmentation).",
        "pit": "Sự chênh lệch lớn giữa độ chính xác Train (rất cao) và Val (rất thấp) là chỉ dấu không thể nhầm lẫn của Overfitting (High Variance).",
        "ref": "Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§1.5 Đánh giá mô hình & Cross-Validation**."
    },
    92: {
        "sec": "§2.2",
        "mod": "B",
        "eli5": "Khi huấn luyện mô hình phân loại, ta thường ép xác suất của nhãn đúng phải là 1.0 (100%), khiến mô hình trở nên quá tự tin và kiêu ngạo. Kỹ thuật Label Smoothing hạ nhãn đúng xuống một chút (ví dụ 0.9) và chia đều 0.1 còn lại cho các lớp khác, giúp mô hình khiêm tốn hơn và chống Overfitting!",
        "step": "Công thức biến đổi phân phối nhãn với hệ số làm mịn $\\epsilon$ trên $K$ lớp:\n$$q_i = (1 - \\epsilon) y_i + \\frac{\\epsilon}{K}$$\nVới nhãn đúng ($y_i = 1$):\n$$q_{\\text{target}} = 1 - \\epsilon + \\frac{\\epsilon}{K}$$\nVới các nhãn sai ($y_i = 0$):\n$$q_{\\text{other}} = \\frac{\\epsilon}{K}$$\nVí dụ với $K = 10, \\epsilon = 0.1$: nhãn đúng chuyển từ $1.0$ thành $0.91$, các lớp khác nhận $0.01$. Điều này ngăn chặn logit $z_c \\to \\infty$, giúp gradient ổn định.",
        "pit": "Label Smoothing là kỹ thuật điều quy (Regularization) cho hàm loss, không làm thay đổi nhãn gốc của dữ liệu mà chỉ làm mềm phân phối đích (soft targets).",
        "ref": "Szegedy, C., et al. (2016). Rethinking the Inception Architecture for Computer Vision. CVPR 2016. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**."
    },
    93: {
        "sec": "§2.2",
        "mod": "B",
        "eli5": "Tốc độ học (Learning Rate) giống như bước chân khi bạn đi xuống đáy thung lũng trong sương mù: Nếu bước chân vừa phải, bạn sẽ từ từ chạm đáy an toàn. Nhưng nếu bước chân quá khổng lồ (learning rate quá lớn), một bước nhảy sẽ đưa bạn văng tít sang ngọn núi đối diện, thậm chí bay thẳng ra khỏi thung lũng (phân kỳ, loss biến thành NaN)!",
        "step": "Xét bài toán tối ưu bậc hai $f(x) = \\frac{1}{2} a x^2$ với $a > 0$.\nBước cập nhật: $x_{t+1} = x_t - \\eta (a x_t) = (1 - \\eta a) x_t$.\nĐiều kiện hội tụ là $|1 - \\eta a| < 1 \\iff 0 < \\eta < \\frac{2}{a}$.\nNếu chọn $\\eta > \\frac{2}{a}$, dãy số $|x_t| \\to \\infty$ bùng nổ theo cấp số nhân, hàm mất mát phân kỳ (Divergence) và xuất hiện lỗi tràn số `NaN` / `Inf`.",
        "pit": "Learning rate quá nhỏ làm hội tụ chậm; còn learning rate quá lớn KHÔNG BAO GIỜ giúp hội tụ nhanh hơn mà sẽ gây rung lắc dữ dội hoặc phân kỳ hoàn toàn.",
        "ref": "Goodfellow, I., et al. (2016). Deep Learning. MIT Press. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**."
    },
    94: {
        "sec": "§1.5",
        "mod": "A",
        "eli5": "Kiểm tra chéo K-Fold giống như việc chia lớp thành 5 nhóm học tập: Lần 1 nhóm 1 thi còn 4 nhóm kia làm bài ôn; lần 2 nhóm 2 thi; lần 3 nhóm 3 thi... Cứ như vậy, mọi học sinh đều có cơ hội vừa học vừa được kiểm tra công bằng, giúp điểm số đánh giá không bị may rủi!",
        "step": "Quy trình $K$-Fold Cross-Validation:\n1. Chia ngẫu nhiên tập dữ liệu $D$ thành $K$ phần con bằng nhau $F_1, F_2, \\dots, F_K$.\n2. Lặp qua $i = 1, \\dots, K$:\n   - Tập kiểm tra: $V_i = F_i$\n   - Tập huấn luyện: $T_i = D \\setminus F_i$\n   - Huấn luyện mô hình trên $T_i$ và đánh giá điểm $S_i$ trên $V_i$.\n3. Điểm đánh giá trung bình không thiên kiến:\n$$\\bar{S} = \\frac{1}{K} \\sum_{i=1}^K S_i$$",
        "pit": "Với bài toán dữ liệu chuỗi thời gian (Time-series), tuyệt đối không dùng K-Fold thông thường vì sẽ làm rò rỉ tương lai dự báo quá khứ (phải dùng TimeSeriesSplit).",
        "ref": "Kohavi, R. (1995). A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection. IJCAI. Xem **§1.5 Đánh giá mô hình & Cross-Validation**."
    },
    95: {
        "sec": "§2.2",
        "mod": "B",
        "eli5": "CPU giống như một vài vị giáo sư thông thái giải được các bài toán phức tạp tuần tự, còn GPU giống như hàng ngàn học sinh tiểu học cùng làm phép nhân ma trận đơn giản cùng một lúc. Do Deep Learning cốt lõi là hàng triệu phép nhân cộng ma trận, GPU và TPU chạy song song nhanh gấp hàng trăm lần CPU!",
        "step": "Bản chất tính toán mạng nơ-ron là các phép toán đại số tuyến tính cơ bản (BLAS):\n$$Y = W X + b$$\nGPU chứa hàng nghìn nhân CUDA (CUDA Cores) và nhân Tensor (Tensor Cores) được thiết kế tối ưu hóa cho phép tính nhân-cộng ma trận tích lũy song song (GEMM - General Matrix Multiply) với băng thông bộ nhớ (Memory Bandwidth) hàng trăm GB/s đến TB/s.",
        "pit": "GPU không tăng tốc cho các thuật toán đệ quy hoặc xử lý rẽ nhánh điều kiện logic phức tạp tuần tự (vốn là thế mạnh của CPU), mà chuyên trị tính toán ma trận song song ồ ạt.",
        "ref": "Kirk, D. B., & Hwu, W. W. (2016). Programming Massively Parallel Processors. Xem **§2.2 Lan truyền ngược & Tối ưu hóa**."
    },
    96: {
        "sec": "§7.1",
        "mod": "C",
        "eli5": "Lượng tử hóa (Quantization) giống như việc đổi từ dùng thước đo milimet chi tiết sang dùng thước đo centimet tròn số: Bình thường mỗi trọng số được lưu bằng số thực 32-bit (FP32). Nếu chuyển sang số nguyên 8-bit (INT8), mô hình sẽ nhẹ đi đúng 4 lần, tốn ít RAM hơn và chạy vèo vèo trên máy tính yếu!",
        "step": "Công thức lượng tử hóa tuyến tính từ số thực $x \\in [a, b]$ sang số nguyên $q \\in [0, 255]$ (INT8):\n$$q = \\text{round}\\left(\\frac{x}{S}\\right) + Z$$\nTrong đó:\n- $S = \\frac{b - a}{255}$ là hệ số tỉ lệ (Scale factor).\n- $Z$ là điểm không (Zero point).\nLợi ích: Giảm dung lượng bộ nhớ từ 4 byte (FP32) xuống 1 byte (INT8) cho mỗi tham số, tiết kiệm $75\\%$ dung lượng và tận dụng các tập lệnh SIMD INT8 tăng tốc tính toán.",
        "pit": "Quantization làm mô hình nhẹ đi và chạy nhanh hơn, nhưng nếu lượng tử hóa quá sâu (như 4-bit, 2-bit) mà không có kỹ thuật chuẩn (như QLoRA, AWQ) có thể làm sụt giảm nhẹ độ chính xác.",
        "ref": "Gholami, A., et al. (2022). A Survey of Quantization Methods for Efficient Neural Network Inference. Proceedings of the IEEE. Xem **§7.1 Kỹ thuật thi đấu & SOTA**."
    },
    97: {
        "sec": "§1.5",
        "mod": "A",
        "eli5": "A/B Testing giống như việc chia đôi khách vào quán: Một nửa khách hàng được phục vụ bằng thực đơn cũ (phiên bản A), một nửa được phục vụ bằng thực đơn mới (phiên bản B). Sau vài tuần, người chủ quán so sánh doanh thu thực tế giữa hai nhóm để quyết định có nên đổi toàn bộ sang thực đơn mới hay không!",
        "step": "Phương pháp A/B Testing trong triển khai hệ thống AI:\n1. Phân luồng lưu lượng người dùng ngẫu nhiên: $50\\%$ truy cập Model A (baseline hiện tại), $50\\%$ truy cập Model B (mô hình mới thử nghiệm).\n2. Thu thập các chỉ số nghiệp vụ thực tế (Business Metrics: tỷ lệ click CTR, thời gian lưu trang, doanh thu chuyển đổi).\n3. Kiểm định giả thuyết thống kê (t-test hoặc Z-test) để xác nhận sự cải thiện có ý nghĩa thống kê ($p < 0.05$) hay chỉ là ngẫu nhiên.",
        "pit": "A/B testing đo lường tác động thực tế trên người dùng thật (online evaluation), trong khi F1-score hay Accuracy trên tập test chỉ là đánh giá ngoại tuyến (offline evaluation).",
        "ref": "Kohavi, R., et al. (2020). Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing. Cambridge University Press. Xem **§1.5 Đánh giá mô hình & Cross-Validation**."
    },
    98: {
        "sec": "§1.5",
        "mod": "A",
        "eli5": "Data Drift (dữ liệu bị trôi) giống như việc một mô hình học nhận biết thời trang năm 2010 mang đi dự đoán cho giới trẻ năm 2026: Phong cách ăn mặc và thị hiếu của con người đã thay đổi hoàn toàn theo thời gian. Mẫu dữ liệu đầu vào trong thực tế không còn giống với những gì mô hình đã từng được học trong quá khứ!",
        "step": "Phân biệt hai loại hiện tượng trôi dạt trong hệ thống AI production:\n1. **Data Drift (Covariate Shift):** Phân phối đầu vào thay đổi $P_{\\text{test}}(X) \\ne P_{\\text{train}}(X)$ nhưng mối quan hệ $P(Y \\mid X)$ không đổi (vd: người dùng đổi sang dùng điện thoại mới chụp ảnh nét hơn).\n2. **Concept Drift:** Mối quan hệ giữa đặc trưng và nhãn thay đổi $P_{\\text{test}}(Y \\mid X) \\ne P_{\\text{train}}(Y \\mid X)$ (vd: sau đại dịch Covid, thói quen chi tiêu thay đổi khiến mô hình dự báo tài chính cũ bị sai hoàn toàn).\nPhương pháp phát hiện: Dùng kiểm định Kolmogorov-Smirnov (KS-test) hoặc độ phân kỳ Population Stability Index (PSI).",
        "pit": "Mô hình dù đạt độ chính xác 99% khi nghiệm thu vẫn sẽ dần bị thoái hóa hiệu năng trong thực tế (Model Decay) nếu không có hệ thống giám sát Data Drift liên tục.",
        "ref": "Gama, J., et al. (2014). A survey on concept drift adaptation. ACM Computing Surveys. Xem **§1.5 Đánh giá mô hình & Cross-Validation**."
    },
    99: {
        "sec": "§7.1",
        "mod": "C",
        "eli5": "MLOps là sự kết hợp giữa Machine Learning (Học máy) và DevOps (Vận hành phần mềm): Nó là toàn bộ quy trình tự động hóa từ thu thập dữ liệu, huấn luyện, kiểm thử, đóng gói mô hình cho đến đưa lên máy chủ phục vụ người dùng và giám sát lỗi 24/7 một cách bền bỉ và chuyên nghiệp.",
        "step": "Vòng đời chuẩn của hệ thống MLOps:\n1. **Data Engineering:** Ingestion, Validation, Feature Store.\n2. **Model Engineering:** Distributed Training, Hyperparameter Tuning, Experiment Tracking (MLflow, W&B).\n3. **Deployment & CI/CD:** Model Registry, Containerization (Docker), Model Serving (Triton, TorchServe).\n4. **Operations:** Monitoring latency, throughput, Data Drift & Automated Retraining.",
        "pit": "MLOps không chỉ là việc gọi hàm `model.fit()` và `model.predict()`, mà là quản lý toàn diện vòng đời của mã nguồn, dữ liệu và mô hình trong môi trường sản xuất thực tế.",
        "ref": "Kreuzberger, D., et al. (2023). Machine learning operations (mlops): Overview, definition, and architecture. IEEE Access. Xem **§7.1 Kỹ thuật thi đấu & SOTA**."
    },
    100: {
        "sec": "§4.3",
        "mod": "C",
        "eli5": "Khi sinh từng từ tiếp theo trong mô hình ngôn ngữ lớn (LLM), để sinh ra từ thứ 100, mô hình cần tính lại Attention với 99 từ trước. Kỹ thuật KV Caching lưu tạm các vector Key và Value của 99 từ trước vào bộ nhớ VRAM, giúp mô hình chỉ cần tính vector cho đúng 1 từ mới nhất, tăng tốc độ trả lời lên gấp hàng chục lần!",
        "step": "Trong quá trình sinh tự hồi quy (Autoregressive Generation):\nTại bước giải mã $t$, để tính toán Attention cho token mới $x_t$:\n- Thay vì tính lại toàn bộ ma trận $K_{1:t} = X_{1:t} W_K$ và $V_{1:t} = X_{1:t} W_V$ tốn chi phí $\\mathcal{O}(t^2)$,\n- KV Caching lưu trữ sẵn tensor $K_{1:t-1}$ và $V_{1:t-1}$ trong bộ nhớ đệm GPU VRAM.\n- Tại bước $t$, chỉ cần tính $k_t = x_t W_K, v_t = x_t W_V$ và ghép nối (concatenate):\n$$K_{1:t} = [K_{1:t-1}; k_t], \\quad V_{1:t} = [V_{1:t-1}; v_t]$$\nChi phí tính toán giảm từ $\\mathcal{O}(T^2)$ xuống $\\mathcal{O}(T)$ trên mỗi token sinh ra.",
        "pit": "KV Caching tiêu tốn một lượng VRAM rất lớn (tỉ lệ thuận với độ dài chuỗi $T$, kích thước batch $B$ và số lớp), dẫn tới sự ra đời của các kỹ thuật tối ưu như PagedAttention (vLLM) và FlashAttention.",
        "ref": "Dao, T., et al. (2022). FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. NeurIPS 2022. Xem **§4.3 Mô hình ngôn ngữ lớn (LLM)**."
    }
}

# Đọc olp-03.json hiện tại
with open(EXAM_PATH, "r", encoding="utf-8") as f:
    exam_data = json.load(f)

current_questions = exam_data.get("questions", [])
print(f"Current questions in olp-03.json: {len(current_questions)}")

# Tách 50 câu MCQ đầu và 4 câu tự luận
mcqs_01_50 = [q for q in current_questions if q.get("type") == "mcq" and int(q.get("id").replace("VOAI03-M", "")) <= 50]
essays = [q for q in current_questions if q.get("type") != "mcq"]

print(f"MCQs 1-50: {len(mcqs_01_50)}, Essays: {len(essays)}")

# Tạo 50 câu MCQ tiếp theo (VOAI03-M51 đến VOAI03-M100)
new_mcqs = []
for q_dict in raw_qs:
    q_num = q_dict["q_num"]
    qid = f"VOAI03-M{q_num:02d}"
    prompt = q_dict["prompt"]
    opts_raw = q_dict["opts"]
    ans = q_dict["ans"]
    
    meta = KNOWLEDGE_DB.get(q_num, {})
    mod = meta.get("mod", "C")
    sec = meta.get("sec", "§1.1")
    eli5 = meta.get("eli5", "")
    step = meta.get("step", "")
    pit = meta.get("pit", "")
    ref = meta.get("ref", "")
    
    # Chuẩn hóa options
    opt_keys = ["A", "B", "C", "D"]
    formatted_opts = []
    for idx, opt_text in enumerate(opts_raw):
        # Làm sạch khoảng trắng thừa
        opt_text = " ".join(opt_text.split())
        formatted_opts.append({
            "key": opt_keys[idx],
            "text": opt_text
        })
    
    # Soạn thảo explanation 4 khối chuẩn
    explanation_text = f"""### 1. ELI5 — Bản chất cốt lõi (Giải thích như cho em bé)
{eli5}

### 2. Công thức toán & Bước tính chi tiết (Step-by-Step)
{step}

### 3. Bẫy đề thi & Tại sao các đáp án khác sai (Pitfalls)
{pit}

### 4. Mắt xích kiến thức & Liên hệ bài cũ
📚 {ref}"""

    new_q = {
        "id": qid,
        "module": mod,
        "type": "mcq",
        "points": 1.0,  # Đưa về 1.0 điểm mỗi câu để 100 câu = 100 điểm trọn vẹn
        "prompt": prompt,
        "options": formatted_opts,
        "answer": ans,
        "explanation": explanation_text.strip(),
        "video": None
    }
    new_mcqs.append(new_q)

print(f"Generated {len(new_mcqs)} new MCQs (VOAI03-M51 to M100)")

# Đồng bộ điểm 50 câu đầu về 1.0 điểm để 100 câu trắc nghiệm = 100.0 điểm
for q in mcqs_01_50:
    q["points"] = 1.0

# Ghép toàn bộ: 100 câu MCQ + 4 bài tự luận
full_questions = mcqs_01_50 + new_mcqs + essays
exam_data["questions"] = full_questions
exam_data["title"] = "Đề 03: Mô Phỏng Đề Thi Quốc Gia VOAI 2026 (100 Câu Chuẩn)"
exam_data["description"] = "Đề thi mô phỏng cấu trúc kỳ thi Olympic AI Quốc gia (VOAI) gồm trọn vẹn 100 câu trắc nghiệm bao quát toàn diện ML, Deep Learning, CV, NLP & MLOps cùng 4 bài toán thiết kế kiến trúc thực chiến."

with open(EXAM_PATH, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"Successfully updated olp-03.json! Total questions now: {len(full_questions)}")
