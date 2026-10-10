# VERIFY BÁO CÁO GEMINI LẦN 4 — 09/10/2026

## Kết luận

**Đã sửa được các lỗi chính của lượt trước, nhưng chưa đạt tuyên bố khớp 1:1 toàn bộ nội dung.** Đề 02 hiện có nhãn thuật ngữ phù hợp chủ đề ở 60 MCQ; Markdown chứa đầy đủ 60 explanation của JSON mới. PDF đã biên dịch lại và sửa hai mục NMT/TabM. Tuy nhiên, phần liên hệ câu cũ vẫn trỏ sai chủ đề hàng loạt, và bảng 60 câu trong báo cáo không khớp dữ liệu thật.

Đây là kiểm tra bản `docs/BAO_CAO_SUA_SAU_AUDIT_2026-10-08.md` ghi cập nhật lần 4 lúc **09:15 ngày 09/10**, thời gian sửa file thực tế **09:07:43**; JSON Đề 02 sửa **08:54:54**. Không sửa source, câu hỏi, script hoặc sản phẩm phân phối trong lượt kiểm tra này.

## Những phần đã xác nhận sửa thật

- Đọc prompt và nhãn thuật ngữ đầu phần enrichment của cả 60 MCQ Đề 02: M05 đã là Hessian, M13 là k-NN, M49 là NLP preprocessing, M51 là cosine; các nhãn lạc chủ đề của snapshot 02:00 đã được thay.
- Markdown Đề 02 chứa nguyên văn **60/60 explanation** MCQ của JSON hiện tại.
- `ALL_EXAMS['olp-02']` trong HTML public bằng JSON Đề 02.
- HTML public/dist cùng SHA-256: `e4d335fdb591da5d01862e3e4c7c88fb28be6efdf96eb65ed1bd28dd3ee356e2`.
- PDF docs/public/dist cùng SHA-256, khớp checksum báo cáo: `87e56b7710f7a84c16e5468f151fc0a9118b2bcda82290390d5fab37d41b6b83`.
- PDF 45 trang. Đã trích text và render/đọc trực quan trang 21 và 41: NMT có phương án from scratch theo SOLOAI và tách NLLB/mBART thành mở rộng khi được phép; TabM đã ghi ICLR 2025.
- Báo cáo đã tách **UNVALIDATED** cho độ sát VOAI 2025 mã 006. Đây là nhãn hợp lý với giới hạn bằng chứng hiện tại; chưa có đối chiếu toàn văn mới trong lượt kiểm tra này.

## Các lỗi còn lại

### 1. P1 — Liên hệ có ID tồn tại nhưng sai nội dung

Lỗi nằm trong khối 4 của `src/data/exams/olp-02.json` và nguồn sinh `scripts/enrich_olp02_terms_and_links.py`. Đồng bộ Markdown/web thành công cũng mang các liên hệ sai này sang các bản đó.

| Câu Đề 02 | Chủ đề thật | ID được dẫn | Câu đích thật đang hỏi |
|---|---|---|---|
| M03 | p-value, A/B testing | OLP01-A04 | Xác suất 10 lần tung đồng xu đều mặt sấp |
| M05 | Hessian, điểm yên ngựa | OLP01-A05 | Poisson, số cuộc gọi tổng đài |
| M13 | k-NN, lazy learning | OLP01-B01 | Kích thước đầu ra Conv2D |
| M49 | NLP preprocessing | OLP01-C16 | One-stage và two-stage object detector |
| M51 | Cosine similarity | OLP01-C18 | Silhouette Score của K-Means |
| M57 | BLEU brevity penalty | OLP01-C24 | Kiến trúc ViT |
| M58 | BLEU và ROUGE | OLP01-C25 | Semantic và instance segmentation |
| M59 | Hybrid retrieval, RAG | VOAI03-M45 | Chọn ngẫu nhiên đặc trưng tại nút cây Random Forest |
| M60 | Temperature | VOAI03-M46 | FT-Transformer cho dữ liệu bảng |

Các mô tả liên hệ hiện tại không giải thích quan hệ gián tiếp với những chủ đề đích trên; chúng nói về chủ đề của câu nguồn như thể câu đích cùng chủ đề. Vì vậy đây là liên hệ sai nội dung, không chỉ là chọn bài ứng dụng ở miền khác.

Các đích thay thế đã kiểm tra được:

- M05 có thể liên hệ **VOAI03-M02**: Hessian xác định dương tại điểm dừng; giải thích sự khác biệt giữa cực tiểu và Hessian bất định của M05.
- M13 có thể liên hệ **OLP01-C01**: đúng bản chất k-NN lazy learner.
- M51 có thể liên hệ **OLP01-B09**: đúng bài tính cosine của hai vector.

Phải đọc lại đích của cả 60 câu, không thay ID theo số thứ tự. Nếu không có câu đích phù hợp, ghi rõ hoặc bỏ liên hệ giả; không cần tạo thêm câu.

### 2. P1 — Bảng nghiệm thu 60 câu không được lấy từ JSON thực tế

Trong báo cáo Gemini:

- Dòng 47: **M01** ghi “ma trận đối xứng, trị riêng”; JSON thực tế là **Bayes, base-rate fallacy**.
- Dòng 48: **M02** ghi “nhân ma trận”; JSON thực tế là **phân phối nhị thức, kỳ vọng và phương sai**.
- Dòng 49: **M03** ghi “hạng ma trận”; JSON thực tế là **p-value**.
- Dòng 50: **M04** ghi “chuẩn vector”; JSON thực tế là **PCA**.
- Các dòng này còn dẫn **§2.2 Vector hóa & Tối ưu NumPy**, trong khi §2.2 của giáo trình hiện tại là **Các hàm kích hoạt**. JSON M01 hiện dẫn đúng §5.1; lỗi bảng không được dùng làm căn cứ đổi JSON đang đúng sang bảng đang sai.

Viết lại bảng từ các ID, prompt, section và liên hệ thật sau khi sửa mục 1. Không thể dùng bảng hiện tại làm bằng chứng “khớp 1:1”.

### 3. P1 — Định nghĩa p-value M03 còn cần chỉnh chính xác

Phần thuật ngữ vẫn viết p-value là `P(Data | H0)`. Phải nêu xác suất của **thống kê kiểm định cực đoan bằng hoặc hơn giá trị quan sát**, dưới giả thuyết không và mô hình kiểm định đã chỉ định. Xác suất của toàn bộ dữ liệu cụ thể/likelihood không phải định nghĩa p-value. Khối liên hệ còn viết “xác suất dữ liệu xảy ra giả sử H0 đúng”, tiếp tục làm mất điều kiện độ cực đoan.

Nguồn xác minh: [tuyên bố chính thức của ASA về p-value](https://doi.org/10.1080/00031305.2016.1154108). Sửa lời giải cho đúng định nghĩa; không có căn cứ đổi đáp án D của câu M03 chỉ vì lỗi diễn đạt này.

### 4. Giới hạn của PASS từ script

`audit_quality.py` đã cải thiện thật: tách MCQ/code và essay, đọc modelAnswer/rubric, kiểm tra section/ID, trả exit 1 khi có lỗi. Nhưng nó chỉ xác nhận **ID câu đích tồn tại**, không biết câu đích có đúng chủ đề. Cổng này vẫn PASS khi M05 dẫn Poisson. Nó cũng lấy danh sách § từ mọi lần xuất hiện trong giáo trình, không kiểm chứng nội dung section hoặc đúng tên section.

Vì vậy giữ nhãn **PASS cấu trúc và tồn tại tham chiếu**, bổ sung review nội dung tham chiếu; không diễn giải PASS này thành “liên hệ đúng học thuật 100%”. Kiểm tra đủ bốn khối vẫn dựa vào chuỗi/tiêu đề, không xác nhận mọi lập luận đúng.

`audit_katex_syntax.mjs` cũng đã cải thiện phạm vi và exit code; chạy lại thực sự báo **2.655 đoạn, 0 lỗi cú pháp hoặc delimiter trong phạm vi kiểm tra của script**. Không suy ra mọi công thức đúng khoa học hoặc mọi delimiter khả dĩ đều được bắt từ con số này.

## Các kiểm tra đã chạy lại

Trong thư mục `D:\Code\Code\AIO\Code\olp-ai-hcmus26`, dùng runtime Node/Python đi kèm Codex:

| Lệnh | Kết quả |
|---|---|
| `node scripts/validate.mjs` | PASS 3 đề, 170 graded + 14 essay |
| `python -X utf8 scripts/audit_quality.py` | PASS 184 câu theo tiêu chí script |
| `node scripts/audit_katex_syntax.mjs` | 2.655 đoạn, 0 lỗi được script phát hiện |
| `node scripts/test_html_logic.mjs` | PASS 5 nhóm |
| `node node_modules/vitest/vitest.mjs run src --no-cache` | PASS 18/18, 4 file test |
| `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json` | Exit 0 |

Thao tác đọc bổ sung: `Get-Content` báo cáo và hai script audit; `rg` định vị các ID/lỗi và tìm memory liên quan (không có hit phù hợp); các đoạn Python chạy từ stdin để đọc prompt/thuật ngữ/khối 4, câu đích, heading giáo trình, hash/metadata PDF và HTML, so JSON–Markdown–HTML, trích và render PDF. Dùng `view_image` để kiểm tra trang 21/41. Tìm nguồn ASA cho định nghĩa p-value.

Không chạy lại generator/build, không huấn luyện mô hình, không xem video hoặc xác nhận video YouTube thực sự phát trên localhost trong lượt này; không đối chiếu lại toàn văn đề VOAI chính thức. Không sửa sản phẩm học tập để “làm test qua”.

## Prompt sửa nốt, giữ phạm vi hẹp

```text
Đọc docs/VERIFY_BAO_CAO_LAN_4_2026-10-09.md. Giữ các phần đã đúng: thuật ngữ M01–M60 theo chủ đề thật, câu hỏi/đáp án/options, scoring, PDF NMT/TabM, nhãn UNVALIDATED.

1. Sửa khối 4 trong scripts/enrich_olp02_terms_and_links.py và JSON Đề02: đọc prompt câu đích thật của TỪNG ID liên hệ. M05 hiện dẫn Poisson, M13 dẫn Conv2D, M49 dẫn YOLO, M51 dẫn Silhouette, M59 dẫn RandomForest, M60 dẫn FT-Transformer. Đổi sang câu liên quan thật và viết rõ quan hệ; nếu không có đích phù hợp thì bỏ liên hệ giả. Đích kiểm tra được: M05 -> VOAI03-M02; M13 -> OLP01-C01; M51 -> OLP01-B09. Không sửa prompt/answer hay hoán đổi ID để hợp thức hóa liên hệ sai.

2. Sửa định nghĩa p-value M03 thành xác suất của thống kê kiểm định cực đoan bằng hoặc hơn quan sát dưới H0; không dùng P(Data|H0) làm định nghĩa. Sửa cả khối thuật ngữ và khối liên hệ, giữ đáp án hợp lệ.

3. Sinh lại Markdown Đề02 và HTML sau khi nội dung đúng. Chạy các kiểm tra hiện có; kiểm tra thủ công 60 quan hệ. Không mở rộng đề hoặc đổi seed, điểm, option order.

4. Viết lại bảng 60 câu trong BAO_CAO_SUA_SAU_AUDIT từ JSON thật. M01 là Bayes, M02 Binomial, M03 p-value, M04 PCA; không phải ma trận như bảng cũ. Đối chiếu đúng số và tên § với heading giáo trình. Không lấy bảng sai làm nguồn sửa JSON đúng.

5. Báo PASS kỹ thuật đúng phạm vi; ID tồn tại không đồng nghĩa liên hệ đúng chủ đề. Ghi UNVALIDATED cho độ sát VOAI2025 cho đến khi có đối chiếu thực tế. Trả bảng 60 câu có prompt nguồn + prompt đích rút gọn và lý do liên quan để người khác kiểm tra được.
```

**Để ôn ngay:** câu hỏi và phần thuật ngữ mới đã có tiến bộ rõ ràng; dùng bản hiện tại nhưng tạm bỏ các liên hệ câu cũ. Chỉ cần sửa nốt những điểm xác nhận ở trên, không mở rộng thêm bộ đề. Lượt verify này không phải chứng nhận toàn bộ 184 lời giải đúng học thuật.

## Phụ lục: câu nguồn và câu đích thật của 60 liên hệ

Bảng dưới lấy từ JSON đang kiểm tra, không dựa vào bảng nghiệm thu Gemini. Đây là bằng chứng để rà quan hệ; không tự động kết luận mọi dòng đều sai.

| ID nguồn | Đầu prompt nguồn | ID liên hệ | Đầu prompt đích |
|---|---|---|---|
| VOAI02-M01 | Một căn bệnh hiếm gặp có tỉ lệ mắc trong cộng đồng là $P(D) = 0.5\%$. Một bộ kit xét nghiệm y tế có độ nhạy (Sensitivity / True Po… | OLP01-A01 | Một căn bệnh có tỉ lệ mắc trong cộng đồng là 2%. Một xét nghiệm y tế có độ nhạy (Sensitivity) 95% và tỉ lệ dương tính giả (False P… |
| VOAI02-M02 | Cho biến ngẫu nhiên rời rạc $X \sim \text{Binomial}(n = 20, p = 0.4)$. Kỳ vọng $\mathbb{E}[X]$ và phương sai $\text{Var}(X)$ của $… | OLP01-A03 | Cho biến ngẫu nhiên rời rạc $X \sim \text{Bernoulli}(p = 0.3)$. Kỳ vọng $\mathbb{E}[X]$ và phương sai $\text{Var}(X)$ của biến ngẫ… |
| VOAI02-M03 | Trong một nghiên cứu A/B Testing đánh giá thuật toán gợi ý mới, giả thuyết không $H_0$ là 'Thuật toán mới không làm tăng tỉ lệ cli… | OLP01-A04 | Tung một đồng xu cân đối và đồng chất liên tiếp 10 lần độc lập. Xác suất để cả 10 lần tung đều xuất hiện mặt sấp (S) là bao nhiêu?… |
| VOAI02-M04 | Cho ma trận dữ liệu đã chuẩn hóa chuẩn (zero-mean) $X \in \mathbb{R}^{N \times D}$. Trong thuật toán Phân tích Thành phần Chính (P… | OLP01-B04 | Một nút (node) trong cây quyết định đang chứa 8 mẫu dữ liệu, gồm 4 mẫu thuộc lớp Đỏ và 4 mẫu thuộc lớp Xanh. Độ hỗn loạn thông tin… |
| VOAI02-M05 | Cho hàm số hai biến $f(x, y) = x^2 - 4xy + y^3$. Điểm dừng $P_0(0, 0)$ có gradient $\nabla f(0, 0) = [0, 0]^T$. Tính chất của điểm… | OLP01-A05 | Một tổng đài chăm sóc khách hàng nhận trung bình $\lambda = 3$ cuộc gọi mỗi phút theo mô hình phân phối Poisson. Xác suất để trong… |
| VOAI02-M06 | Cho vector logit $z = [z_1, z_2, \dots, z_C]^T$, xác suất dự đoán $p_i = \text{Softmax}(z)_i = \frac{e^{z_i}}{\sum_{k=1}^C e^{z_k}… | OLP01-B12 | Trong PyTorch, khi giải bài toán phân loại nhị phân (Binary Classification), vì sao lập trình viên luôn được khuyến nghị sử dụng `… |
| VOAI02-M07 | Khoảng cách Mahalanobis giữa hai điểm $u, v \in \mathbb{R}^D$ được định nghĩa là $d_M(u, v) = \sqrt{(u - v)^T \Sigma^{-1} (u - v)}… | OLP01-B02 | Một ảnh đầu vào có kích thước $28 \times 28$ (ảnh chữ số MNIST) được đưa qua một tầng tích chập Conv2D với kernel $K = 5 \times 5$… |
| VOAI02-M08 | Trong học máy, việc tối đa hóa hàm hợp lý hậu nghiệm (Maximum A Posteriori - MAP) trên trọng số $w$ tương đương với việc thêm số h… | OLP01-B03 | Một ảnh đầu vào kích thước $224 \times 224$ (chuẩn ImageNet) được đưa qua tầng Conv2D đầu tiên với kích thước kernel $K = 7 \times… |
| VOAI02-M09 | Cho hai phân phối xác suất rời rạc $P$ và $Q$ trên cùng không gian mẫu. Phân kỳ Kullback-Leibler được định nghĩa là $D_{KL}(P \par… | OLP01-B13 | Trong một vòng lặp huấn luyện PyTorch tiêu chuẩn cho một batch dữ liệu, thứ tự các dòng lệnh bắt buộc phải thực hiện là gì?… |
| VOAI02-M10 | Hàm kích hoạt SiLU (Sigmoid Linear Unit / Swish) được định nghĩa là $f(x) = x \cdot \sigma(x)$, trong đó $\sigma(x) = \frac{1}{1 +… | OLP01-B08 | Từ kết quả của mô hình ở câu B07 (Precision $P = 0.8$, Recall $R = 0.667 \approx 2/3$), chỉ số F1-Score (trung bình điều hòa giữa … |
| VOAI02-M11 | Cho $Q \in \mathbb{R}^{n \times n}$ là một ma trận trực giao (orthogonal matrix, thỏa mãn $Q^T Q = Q Q^T = I$). Với bất kỳ vector … | OLP01-A06 | Theo Định lý Giới hạn Trung tâm (Central Limit Theorem — CLT), khi kích thước mẫu $n$ đủ lớn ($n \ge 30$), giá trị trung bình mẫu … |
| VOAI02-M12 | Khi cần tính xấp xỉ kỳ vọng $\mathbb{E}_{x \sim P}[f(x)]$ nhưng việc lấy mẫu trực tiếp từ phân phối $P(x)$ quá khó khăn hoặc tốn k… | OLP01-A07 | Cho biến ngẫu nhiên $X$ có kỳ vọng $\mathbb{E}[X] = 5$ và phương sai $\text{Var}(X) = 4$. Đặt biến ngẫu nhiên $Y = 2X + 3$. Kỳ vọn… |
| VOAI02-M13 | Vì sao thuật toán k-Nearest Neighbors (k-NN) được xếp vào nhóm 'Lazy Learner' (người học lười biếng), và độ phức tạp tính toán tại… | OLP01-B01 | Một ảnh đầu vào có kích thước không gian $32 \times 32$ được đưa qua một tầng tích chập Conv2D với kích thước kernel $K = 3 \times… |
| VOAI02-M14 | Trong thuật toán Soft-Margin SVM, hàm mục tiêu tối thiểu hóa là $\min_{w, b, \xi} \frac{1}{2} \\|w\\|_2^2 + C \sum_{i=1}^N \xi_i$.… | OLP01-B05 | Từ nút ban đầu ở câu B04 (Entropy = 1 bit), ta phân chia dữ liệu theo một đặc trưng và thu được 2 nút lá: Nút trái chứa toàn bộ 4 … |
| VOAI02-M15 | Kernel RBF (Radial Basis Function / Gaussian Kernel) trong SVM có dạng $K(x, z) = \exp(-\gamma \\|x - z\\|^2)$. Nếu ta chọn giá tr… | OLP01-B06 | Cho bounding box dự đoán $B_p$ và bounding box nhãn thực tế $B_g$ có diện tích phần giao nhau (Intersection) là 30 pixel vuông, và… |
| VOAI02-M16 | Tại một nút lá của bài toán phân loại nhị phân ($K = 2$), tỉ lệ mẫu của hai lớp là $p_1 = 0.8$ và $p_2 = 0.2$. Giá trị của chỉ số … | OLP01-B07 | Một mô hình phân loại nhị phân dự đoán trên 200 bệnh nhân cho ra ma trận nhầm lẫn (Confusion Matrix): $TP = 80$, $FP = 20$, $FN = … |
| VOAI02-M17 | Trong thuật toán Random Forest, mỗi cây con được xây dựng trên một tập mẫu Bootstrap kích thước $N$ (lấy mẫu có hoàn lại từ tập dữ… | OLP01-B10 | Trong thiết kế khối mạng nơ-ron tích chập (Conv Block) hoặc tầng kết nối đầy đủ (Dense Block) hiện đại trong PyTorch, thứ tự chuẩn… |
| VOAI02-M18 | Trong thuật toán AdaBoost phân loại nhị phân ($y_i \in \{-1, +1\}$), tại vòng lặp $t$, bộ phân loại yếu $h_t(x)$ có tỉ lệ lỗi có t… | OLP01-B11 | Khi sử dụng hàm mất mát `torch.nn.CrossEntropyLoss()` trong PyTorch cho bài toán phân loại đa lớp, đầu vào mô hình đưa vào hàm mất… |
| VOAI02-M19 | Khác biệt cốt lõi trong thuật toán tối ưu hóa giữa Gradient Boosting truyền thống (GBM của Friedman) và XGBoost (Chen & Guestrin) … | VOAI03-M08 | Thuật toán Random Forest kết hợp nhiều cây quyết định bằng phương pháp Ensemble nào?… |
| VOAI02-M20 | LightGBM đạt tốc độ huấn luyện vượt trội trên các tập dữ liệu lớn so với XGBoost truyền thống chủ yếu nhờ vào hai kỹ thuật nào sau… | VOAI03-M09 | Chỉ số $F_1$-Score là trung bình điều hòa của hai đại lượng nào?… |
| VOAI02-M21 | Khi mã hóa biến phân loại (Categorical Features) bằng Target Encoding thông thường trên toàn bộ tập dữ liệu, mô hình thường bị hiệ… | VOAI03-M10 | Trong Hồi quy tuyến tính, nếu các biến độc lập có tương quan tuyến tính rất mạnh với nhau, hiện tượng này gọi là:… |
| VOAI02-M22 | Khi áp dụng kỹ thuật sinh mẫu nhân tạo SMOTE (Synthetic Minority Over-sampling Technique) để xử lý dữ liệu mất cân bằng lớp kết hợ… | VOAI03-M12 | Cho ma trận nhầm lẫn: $\text{TP}=80, \text{FP}=10, \text{FN}=20, \text{TN}=90$. Precision của mô hình là:… |
| VOAI02-M23 | Trong bài toán phân tích cụm không gian biểu diễn (Representation Space Clustering), nhận định nào sau đây là **CHÍNH XÁC** khi so… | OLP01-B14 | Khi khởi tạo trọng số cho các tầng ẩn sử dụng hàm kích hoạt ReLU trong mạng Deep Learning, phương pháp khởi tạo nào sau đây là TỐI… |
| VOAI02-M24 | Khi xây dựng mô hình dự báo chuỗi thời gian (ví dụ: dự báo giá cổ phiếu hoặc lưu lượng truy cập theo giờ), vì sao việc sử dụng `KF… | OLP01-B15 | Trong NumPy, cho một mảng hai chiều `arr` có kích thước `shape = (3, 4)`. Khi thực hiện phép chuyển vị `arr.T` (hoặc `np.transpose… |
| VOAI02-M25 | Trong PyTorch, đoạn mã nào sau đây biểu diễn **ĐÚNG VÀ ĐẦY ĐỦ** thứ tự các bước trong một vòng lặp huấn luyện (Training Step) chuẩ… | OLP01-BC1 | Viết hàm Python/NumPy `compute_metrics(y_true, y_pred)` nhận vào hai mảng nhị phân 1D (chỉ chứa 0 và 1) có cùng kích thước, tính t… |
| VOAI02-M26 | Nếu khởi tạo tất cả các trọng số $W$ của một mạng nơ-ron sâu bằng giá trị **0 (Zeros)**, hiện tượng gì sẽ xảy ra? Và đối với các m… | OLP01-B09 | Cho hai vector đặc trưng (embeddings) trong không gian 2 chiều: $\mathbf{u} = [1, 1]$ và $\mathbf{v} = [0, 2]$. Độ tương đồng Cosi… |
| VOAI02-M27 | Trong lớp Batch Normalization (`nn.BatchNorm2d`), sự khác biệt căn bản về mặt toán học giữa pha huấn luyện (`model.train()`) và ph… | OLP01-B16 | Trong NumPy, cho mảng `A` có kích thước `(4, 1)` và mảng `B` có kích thước `(4,)`. Khi thực hiện phép cộng `C = A + B`, theo quy t… |
| VOAI02-M28 | Vì sao các kiến trúc Transformer và mô hình xử lý chuỗi ngôn ngữ tự nhiên (NLP) hầu như luôn sử dụng **Layer Normalization** thay … | VOAI03-M20 | Một nơ-ron có 3 đầu vào $(1, 2, 3)$, trọng số tương ứng $(0.5, -1, 2)$ và bias là 0.5. Nếu dùng ReLU, đầu ra là:… |
| VOAI02-M29 | Khi huấn luyện mạng học sâu nhiều lớp hoặc mô hình RNN chuỗi dài, hiện tượng bùng nổ gradient (Exploding Gradient) thường khiến gi… | VOAI03-M21 | Phương pháp 'Bag of Words' (BoW) có nhược điểm lớn nhất là gì?… |
| VOAI02-M30 | Trong PyTorch, lớp `nn.CrossEntropyLoss()` đã tự động tích hợp sẵn phép biến đổi toán học nào bên trong, và thí sinh cần đưa đầu v… | OLP01-BC2 | Viết hàm huấn luyện PyTorch chuẩn cho 1 epoch: `train_one_epoch(model, dataloader, criterion, optimizer, device)`. Hàm cần chuyển … |
| VOAI02-M31 | Vì sao trong bài toán phân loại nhị phân hoặc phân loại đa nhãn (Multi-label), PyTorch khuyến nghị mạnh mẽ sử dụng `nn.BCEWithLogi… | VOAI03-M22 | Kiến trúc 'BERT' (Devlin et al.) được xây dựng dựa trên thành phần nào của Transformer?… |
| VOAI02-M32 | Nghiên cứu của Loshchilov & Hutter (ICLR 2019) đã chỉ ra rằng việc cài đặt Weight Decay thông thường (thêm $\lambda w$ vào gradien… | VOAI03-M23 | Hệ thống RAG (Retrieval-Augmented Generation) giúp mô hình LLM giải quyết vấn đề gì cốt lõi?… |
| VOAI02-M33 | Kỹ thuật **Learning Rate Warmup** (tăng dần tốc độ học từ 0 lên giá trị cực đại trong một số bước đầu tiên) trước khi áp dụng Cosi… | VOAI03-M24 | Phép toán 'Max Pooling' trong mạng CNN có tác dụng cốt lõi là:… |
| VOAI02-M34 | Trong hầu hết các thư viện Deep Learning hiện đại (bao gồm PyTorch), kỹ thuật **Inverted Dropout** (với tỉ lệ drop $p$) được thực … | VOAI03-M25 | Thuật toán phát hiện vật thể YOLO (You Only Look Once) thuộc nhóm kiến trúc nào?… |
| VOAI02-M35 | Xét bài toán tối ưu hóa có điều kiện: $\min_w L(w)$ với ràng buộc $\\|w\\|_1 \le C$ (L1) hoặc $\\|w\\|_2^2 \le C$ (L2). Về mặt hìn… | OLP01-B03 | Một ảnh đầu vào kích thước $224 \times 224$ (chuẩn ImageNet) được đưa qua tầng Conv2D đầu tiên với kích thước kernel $K = 7 \times… |
| VOAI02-M36 | Khi triển khai cơ chế Dừng Sớm (Early Stopping) trong quá trình huấn luyện mạng nơ-ron sâu, nhận định nào sau đây là **CHÍNH XÁC N… | VOAI03-M26 | Thuật toán NMS (Non-Maximum Suppression) trong Object Detection dùng để làm gì?… |
| VOAI02-M37 | Cho ảnh đầu vào kích thước vuông $W_{in} = 224$. Áp dụng lớp tích chập Conv2D với kích thước kernel $K = 7$, padding $P = 3$, và s… | OLP01-C01 | Thuật toán k-NN (k-Nearest Neighbors) được xếp vào nhóm thuật toán 'Lazy Learner' (người học lười) và phi tham số (non-parametric)… |
| VOAI02-M38 | Trong thiết kế mạng VGG và ResNet, vì sao người ta luôn ưu tiên xếp chồng hai lớp tích chập kích thước $3 \times 3$ liên tiếp (str… | OLP01-C02 | Trong thuật toán k-NN, siêu tham số $k$ (số lượng láng giềng gần nhất) ảnh hưởng như thế nào đến sự đánh đổi giữa Độ chệch (Bias) … |
| VOAI02-M39 | Kỹ thuật Global Average Pooling (GAP) được giới thiệu trong mạng Network In Network (Lin et al.) và chuẩn hóa trong ResNet nhằm mụ… | OLP01-C03 | Trong thuật toán Support Vector Machine (SVM) tuyến tính dạng lề cứng (Hard-margin), khoảng cách lề (Margin) giữa hai siêu phẳng h… |
| VOAI02-M40 | Trong khối Residual Block của kiến trúc ResNet, đầu ra được tính bằng phép cộng $y = \mathcal{F}(x, \{W_i\}) + x$. Về mặt giải tíc… | OLP01-C04 | Khi sử dụng SVM với hàm nhân RBF (Radial Basis Function Kernel), nếu siêu tham số $\gamma$ (Gamma) được thiết lập ở giá trị quá lớ… |
| VOAI02-M41 | Trong bài toán phân đoạn ảnh ngữ nghĩa (Semantic Segmentation), kiến trúc U-Net (Ronneberger et al.) sử dụng Skip Connections để k… | OLP01-C05 | Trong thuật toán cây quyết định ID3 và lý thuyết thông tin Shannon, độ hỗn loạn thông tin (Entropy) của phân phối xác suất rời rạc… |
| VOAI02-M42 | Cho ảnh đầu vào kích thước $224 \times 224 \times 3$. Trong kiến trúc Vision Transformer (ViT-Base, Dosovitskiy et al.) với kích t… | OLP01-C06 | Khi xây dựng cây quyết định (Decision Tree), tại mỗi nút phân chia, thuật toán ID3 lựa chọn thuộc tính nào để rẽ nhánh tiếp theo?… |
| VOAI02-M43 | Cho hai bounding box hình chữ nhật trong mặt phẳng tọa độ theo định dạng $[x_1, y_1, x_2, y_2]$ (tọa độ góc trên-trái và góc dưới-… | OLP01-C07 | Một kỹ sư AI huấn luyện mô hình phân loại ảnh và ghi nhận kết quả: Độ chính xác trên tập Train đạt 99.2%, nhưng độ chính xác trên … |
| VOAI02-M44 | Trong pipeline phát hiện đối tượng (Object Detection), thuật toán NMS chuẩn mực hoạt động tuần tự theo các bước nào sau đây để loạ… | OLP01-C08 | Khi đánh giá hiệu năng mô hình trên tập dữ liệu phân loại có mất cân bằng lớp nghiêm trọng (Imbalanced Data), kỹ thuật Cross-Valid… |
| VOAI02-M45 | Trong đánh giá mô hình Object Detection chuẩn COCO, kí hiệu **mAP@[0.5:0.95]** (hay mAP@[.5:.95]) biểu thị điều gì?… | OLP01-C09 | Điểm khác biệt cốt lõi về mặt toán học và ứng dụng của kỹ thuật điều chuẩn L1 Regularization (Lasso) so với L2 Regularization (Rid… |
| VOAI02-M46 | Khi triển khai hệ thống Computer Vision trên thiết bị nhúng hoặc yêu cầu thời gian thực (Real-time $\ge 30$ FPS), mô hình phát hiệ… | OLP01-C10 | Trong trường hợp tập dữ liệu chứa nhiều đặc trưng có độ tương quan tuyến tính rất cao với nhau (hiện tượng Đa cộng tuyến — Multico… |
| VOAI02-M47 | Trong bài toán phát hiện ảnh giả mạo/DeepFake (Bài toán 'Kẻ mạo danh' trong video AI Vietnam và IOAI 2026), vì sao việc kết hợp **… | VOAI03-M35 | Kỹ thuật SMOTE (Synthetic Minority Over-sampling Technique) giải quyết vấn đề mất cân bằng lớp bằng cách:… |
| VOAI02-M48 | Trong kỹ thuật **MixUp** (Zhang et al.), hai ảnh $(x_i, x_j)$ và nhãn One-hot $(y_i, y_j)$ được kết hợp theo công thức nào với $\l… | VOAI03-M36 | Khi đánh giá một mô hình phân loại trên tập dữ liệu cực kỳ mất cân bằng (ví dụ gian lận thẻ tín dụng chỉ chiếm 0.1%), độ đo nào sa… |
| VOAI02-M49 | Trong xử lý ngôn ngữ tự nhiên cổ điển, thứ tự chuẩn mực logic của các bước tiền xử lý văn bản thô (Text Preprocessing) nào sau đây… | OLP01-C16 | So sánh đúng đắn nhất giữa hai họ mô hình phát hiện vật thể: 1-stage detector (như YOLO, SSD) và 2-stage detector (như Faster R-CN… |
| VOAI02-M50 | Trong thuật toán biểu diễn từ Word2Vec (Mikolov et al.), phát biểu nào sau đây phân biệt **CHÍNH XÁC** giữa hai kiến trúc CBOW (Co… | OLP01-C17 | Vì sao mô hình Rừng ngẫu nhiên (Random Forest) có khả năng chống hiện tượng Overfitting vượt trội hơn hẳn so với một Cây quyết địn… |
| VOAI02-M51 | Cho hai vector embedding biểu diễn ngữ nghĩa của hai từ: $u = [1, 2, 2]$ và $v = [2, 0, 1]$. Độ tương đồng Cosine (Cosine Similari… | OLP01-C18 | Khi đánh giá chất lượng phân cụm của thuật toán K-Means mà không có nhãn thực tế, chỉ số Silhouette Score được sử dụng như thế nào… |
| VOAI02-M52 | Trong mạng LSTM (Long Short-Term Memory), cổng nào chịu trách nhiệm quyết định tỉ lệ thông tin nào từ ô nhớ trạng thái cũ ($C_{t-1… | OLP01-C19 | Trong một bài toán phát hiện giao dịch gian lận với tỉ lệ mất cân bằng cực hạn (1 ca gian lận trên 99 ca bình thường), giải pháp k… |
| VOAI02-M53 | Trong cơ chế tính toán Self-Attention của Transformer (Vaswani et al.): $\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K… | OLP01-C20 | Trong thiết kế mạng nơ-ron sâu hiện đại, lựa chọn hàm kích hoạt (Activation Function) nào sau đây là CHUẨN XÁC NHẤT cho các tầng ẩ… |
| VOAI02-M54 | Vì sao kiến trúc Transformer chia không gian biểu diễn thành $h$ đầu chú ý song song (Multi-Head Attention với $d_v = d_{model} / … | OLP01-C21 | Vì sao trong các kiến trúc Transformer và mô hình xử lý ngôn ngữ tự nhiên (NLP), chuẩn hóa tầng (Layer Normalization) luôn được ưu… |
| VOAI02-M55 | Trong Transformer nguyên bản, công thức mã hóa vị trí Sinusoidal được định nghĩa là $PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{… | OLP01-C22 | Khi tăng số lượng tầng của mạng CNN lên rất sâu (từ 20 tầng lên 56 tầng), hiện tượng suy thoái hiệu năng (Degradation Problem) xảy… |
| VOAI02-M56 | Sự khác biệt căn bản về mặt cấu trúc chú ý (Attention Mechanism) và bài toán huấn luyện trước (Pre-training Objective) giữa BERT v… | OLP01-C23 | Trong kiến trúc mạng U-Net dùng cho phân vùng ảnh y tế (Medical Image Segmentation), các đường nối tắt (Skip Connections) từ Encod… |
| VOAI02-M57 | Trong đánh giá dịch máy (Bài toán Dịch Hoa - Việt đề thi OLP AI 2025), công thức SacreBLEU kết hợp hệ số phạt độ ngắn: $\text{BP} … | OLP01-C24 | Phát biểu nào sau đây là CHÍNH XÁC NHẤT về cơ chế hoạt động của mô hình Vision Transformer (ViT — Dosovitskiy et al., 2020)?… |
| VOAI02-M58 | Khác biệt cốt lõi về triết lý đo lường giữa chỉ số **BLEU** và chỉ số **ROUGE** trong xử lý ngôn ngữ tự nhiên là gì?… | OLP01-C25 | Điểm khác biệt bản chất giữa Phân vùng theo ngữ nghĩa (Semantic Segmentation) và Phân vùng theo thực thể (Instance Segmentation) l… |
| VOAI02-M59 | Trong một hệ thống RAG doanh nghiệp hiện đại, pipeline truy xuất kết hợp 2 giai đoạn (Two-Stage Retrieval) thường bao gồm:… | VOAI03-M45 | Khi xây dựng một cây quyết định đơn lẻ trong thuật toán Random Forest, tại mỗi nút chia, thuật toán sẽ:… |
| VOAI02-M60 | Trong quá trình sinh văn bản tự hồi quy (Autoregressive Generation) của các mô hình LLM (như GPT-4, LLaMA, DeepSeek), kỹ thuật **K… | VOAI03-M46 | Mô hình FT-Transformer (Feature Tokenizer + Transformer, Gorishniy et al.) dành cho dữ liệu bảng áp dụng cơ chế Self-Attention vào… |

SHA-256 JSON Đề02 tại thời điểm kiểm tra: `f362a4728ebbb6034015a1477df160c6580bb7c4e4f4e147ce0b8f73fdb9a3c5`.

Artifact tạo thêm: báo cáo này và hai ảnh `tmp/pdfs/verify_lan4_2026-10-09/handbook_page21.png`, `handbook_page41.png`. Không sửa file nguồn hoặc sản phẩm học tập.
