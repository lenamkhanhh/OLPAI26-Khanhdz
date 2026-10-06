# 03 — Đáp án & lời giải OLP AI HCMUS 2026

> Mỗi câu: đáp án + vì sao đúng + vì sao 3 đáp án còn lại sai + trích dẫn lý thuyết.
> Tự luận: bài giải mẫu theo khung 5 bước + rubric tự chấm (đạt/không đạt từng ý).

---

# ĐỀ 01 — Đáp án

## Bảng đáp án nhanh (60 câu chấm điểm)

| Câu | ĐA | Câu | ĐA | Câu | ĐA | Câu | ĐA |
|---|---|---|---|---|---|---|---|
| A01 | B | B03 | C | C01 | A | C16 | D |
| A02 | C | B04 | D | C02 | B | C17 | A |
| A03 | A | B05 | A | C03 | C | C18 | B |
| A04 | D | B06 | B | C04 | D | C19 | C |
| A05 | B | B07 | C | C05 | A | C20 | D |
| A06 | C | B08 | D | C06 | B | C21 | A |
| A07 | A | B09 | A | C07 | C | C22 | B |
| A08 | D | B10 | B | C08 | D | C23 | C |
| A09 | B | B11 | C | C09 | A | C24 | D |
| A10 | A | B12 | D | C10 | B | C25 | A |
| A11 | C | B13 | A | C11 | C | C26 | B |
| A12 | D | B14 | B | C12 | D | C27 | C |
| B01 | A | B15 | C | C13 | A | C28 | D |
| B02 | B | B16 | D | C14 | B | C29 | A |
| | | | | C15 | C | C30 | B |

Phân bố đáp án: A×15, B×14, C×15, D×14 (không đoán mò được).

## Lời giải chi tiết

**A01 → B.** Đúng: Bayes = 0.019/0.0582 ≈ 32.6%. Sai: A nhầm độ nhạy với hậu nghiệm; C là prior; D không có cơ sở. → Xem §5.1.
**A02 → C.** Đúng: base rate 0.1% khiến số người khỏe dương tính giả áp đảo. Sai: A/B test đã 99%; D sai bản chất. → Xem §5.1.
**A03 → A.** Đúng: E=p, Var=p(1-p). Sai: B là p=0.5; C nhầm Var=p²; D nhầm E=1-p. → Xem §5.2.
**A04 → D.** Đúng: 0.5^10 ≈ 0.001. Sai: A là 1 lần tung; B/C ước lượng bừa. → Xem §5.2.
**A05 → B.** Đúng: e^-3 ≈ 0.05. Sai: A (vẫn có xác suất), C/D quá lớn. → Xem §5.2.
**A06 → C.** Đúng: CLT → xấp xỉ Normal. Sai: A/B/D là phân phối cụ thể, không phải giới hạn. → Xem §5.2.
**A07 → A.** Đúng: E=13, Var=4×4=16. Sai: B quên bình phương hệ số; C sai E; D cộng thay vì nhân. → Xem §5.3.
**A08 → D.** Đúng: MAP = dữ liệu + prior. Sai: A đảo ngược; B sai; C MAP dùng mọi nơi. → Xem §5.4.
**A09 → B.** Đúng: 0.03 < 0.05 → bác bỏ H0. Sai: A ngược; C p-value không phải P(H0); D p-value không đo hiệu ứng. → Xem §5.5.
**A10 → A.** Đúng: mùa hè là confounder. Sai: B đảo nhân quả; C phủ nhận tương quan có thật; D lảng tránh. → Xem §5.6.
**A11 → C.** Đúng: stratified giữ tỉ lệ nhóm. Sai: A bỏ nhóm thiểu số; B ngẫu nhiên đơn giản có thể mất nhóm hiếm; D tăng test không sửa lệch. → Xem §5.6.
**A12 → D.** Đúng: 4/36 = 1/9. Sai: A là P(tổng 7); B là 5/36 (tổng 8); C không có cơ sở. → Xem §5.1.
**B01 → A.** Đúng: (32−3+2)+1 = 32. Sai: B trừ kernel không bù pad; C nhầm stride 2; D cộng pad sai. → Xem §3.1.
**B02 → B.** Đúng: 28−5+1 = 24. Sai: A quên valid trừ kernel; C nhầm pooling /2; D off-by-one. → Xem §3.1.
**B03 → C.** Đúng: floor(223/2)+1 = 112. Sai: A quên stride; B floor nhưng quên +1; D chia 4. → Xem §3.1.
**B04 → D.** Đúng: −2×0.5×log2(0.5) = 1 bit. Sai: A là node sạch; B/C tính sai log. → Xem §1.3.
**B05 → A.** Đúng: IG = 1 − 0 = 1 (tối đa). Sai: B/C/D tính sai trung bình con. → Xem §1.3.
**B06 → B.** Đúng: 30/120 = 0.25 < 0.5 → sai. Sai: A nhầm công thức; C là 30/150; D đảo tử mẫu. → Xem §3.6.
**B07 → C.** Đúng: P = 80/100 = 0.8, R = 80/120 ≈ 0.667. Sai: A đảo P/R; B quên FN; D sai tử số. → Xem §1.7.
**B08 → D.** Đúng: 2×0.32/1.2 ≈ 0.533. Sai: A là trung bình cộng; B là max; C là min. → Xem §1.7.
**B09 → A.** Đúng: 1/√2 ≈ 0.707. Sai: B nhầm trực giao; C nhầm cùng hướng; D là trung bình. → Xem §4.3.
**B10 → B.** Đúng: Linear → BN → ReLU. Sai: A/C đảo Norm với activation; D Norm trước Linear vô nghĩa. → Xem §2.8.
**B11 → C.** Đúng: loss đã gồm Softmax, đưa logit. Sai: A double-softmax; B sai kiểu; D bịa. → Xem §2.4.
**B12 → D.** Đúng: BCEWithLogitsLoss nhận logit, ổn định số. Sai: A BCE cần xác suất; B MSE không hợp; C double-sigmoid. → Xem §2.4.
**B13 → A.** Đúng: zero_grad trước backward (grad cộng dồn). Sai: B grad bị xóa sau khi tính; C/D sai thứ tự, thiếu zero. → Xem §2.3.
**B14 → B.** Đúng: He cho ReLU. Sai: A/C vỡ đối xứng; D Xavier hợp Tanh/Sigmoid hơn. → Xem §2.7.
**B15 → C.** Đúng: transpose đảo (3,4)→(4,3). Sai các đáp án còn lại sai chiều. → Xem §1.10.
**B16 → D.** Đúng: broadcast (4,1)+(4,)→(4,4). Sai: A NumPy broadcast được; B/C sai luật broadcast. → Xem §1.10.

**C01 → A.** Đúng: lazy = dồn tính toán lúc predict. Sai: B mô tả parametric; C là kernel; D không bắt buộc. → Xem §1.1.
**C02 → B.** Đúng: k nhỏ overfit, k lớn underfit. Sai: A k=1 nhớ cả nhiễu; C ngược; D sai. → Xem §1.1.
**C03 → C.** Đúng: margin = 2/||w||. Sai: A/B/D không quyết định độ rộng. → Xem §1.2.
**C04 → D.** Đúng: gamma lớn → ôm sát → overfit. Sai: A/B/C ngược bản chất gamma. → Xem §1.2.
**C05 → A.** Đúng: log2, bit. Sai: B/C sai cơ số; D sai công thức. → Xem §1.3.
**C06 → B.** Đúng: Gain lớn nhất. Sai: A nhiều nhánh dễ overfit; C/D không phải tiêu chí. → Xem §1.3.
**C07 → C.** Đúng: chênh 29% = overfit. Sai: A ngược; B/D phủ nhận. → Xem §1.5.
**C08 → D.** Đúng: stratified giữ tỉ lệ lớp. Sai: A có thể mất lớp hiếm; B tốn kém; C một lần thiếu ổn định. → Xem §1.5.
**C09 → A.** Đúng: L1 sinh sparse, loại feature. Sai: B L2 không về 0 hẳn; C/D sai. → Xem §1.6.
**C10 → B.** Đúng: L2 co đều, ổn định. Sai: A L1 giật cục khi tương quan; C/D sai. → Xem §1.6.
**C11 → C.** Đúng: Adam nhanh, ít tune. Sai: A sai sự thật; B Adagrad không chuẩn vision; D sai. → Xem §2.5.
**C12 → D.** Đúng: warmup + giảm dần. Sai: A càng diverge; B quá chậm; C sai (layer-wise LR hợp lệ). → Xem §2.6.
**C13 → A.** Đúng: VGG = chồng 3x3. Sai: B 11x11 là AlexNet; C residual là ResNet; D LeNet không attention. → Xem §3.3.
**C14 → B.** Đúng: ADD + compound scaling. Sai: A CONCAT là U-Net; C scale cả 3 chiều; D ngược degradation. → Xem §3.3.
**C15 → C.** Đúng: giữ box mạnh nhất, xóa trùng. Sai: A trùng lặp; B/D không phải NMS. → Xem §3.6.
**C16 → D.** Đúng: 1-stage nhanh vs 2-stage chính xác. Sai: A/B ngược; C cả hai đều dùng NMS. → Xem §3.6.
**C17 → A.** Đúng: bagging + random feature. Sai: B vẫn overfit được; C ngược; D ngược hoàn toàn. → Xem §1.4.
**C18 → B.** Đúng: gần 1 là tốt. Sai: A âm là gán nhầm; C dùng cho clustering; D phải chuẩn hóa. → Xem §1.8.
**C19 → C.** Đúng: SMOTE + F1. Sai: A accuracy lừa; B undersampling nhầm lớp; D copy gây overfit. → Xem §1.9.
**C20 → D.** Đúng: hidden ReLU/GELU, output theo task. Sai: A Sigmoid bão hòa; B Softmax hidden vô nghĩa; C thiếu activation thì tuyến tính. → Xem §2.2.
**C21 → A.** Đúng: LayerNorm độc lập batch. Sai: B BN tệ khi batch nhỏ; C mất ổn định; D sai chuẩn. → Xem §2.8.
**C22 → B.** Đúng: residual trị degradation. Sai: A kernel lớn không trị; C Sigmoid tệ hơn; D không liên quan. → Xem §2.10.
**C23 → C.** Đúng: U-Net CONCAT. Sai: A là ResNet; B/D sai kiến trúc. → Xem §3.4.
**C24 → D.** Đúng: patch + [CLS], không conv. Sai: A có conv; B cần positional; C cần data lớn. → Xem §3.5.
**C25 → A.** Đúng: semantic không tách vật thể. Sai: B instance không phải classification; C ngược; D sai. → Xem §3.7.
**C26 → B.** Đúng: diffusion khử nhiễu dần. Sai: A nhầm GAN; C GAN hay collapse; D ngược. → Xem §3.8.
**C27 → C.** Đúng: đóng băng + head lr nhỏ. Sai: A data nhỏ train mới overfit; B lr lớn phá pretrain; D sai. → Xem §3.9.
**C28 → D.** Đúng: đúng thứ tự pipeline. Sai: A/C/B đảo bước, stemming không thay tokenization. → Xem §4.1.
**C29 → A.** Đúng: FastText n-gram trị OOV. Sai: B one-hot không ngữ nghĩa; C TF-IDF không ngữ cảnh; D sai. → Xem §4.2.
**C30 → B.** Đúng: BERT hiểu, GPT sinh. Sai: A đảo; C khác nhau căn bản; D ngược. → Xem §4.6.

## Tự luận Đề 01 — bài giải mẫu (khung 5 bước)

**E01 (ký hiệu, CV).** (1) Dữ liệu video theo thời gian, 100 người → chia train/val theo người (person-independent) tránh leakage; mất cân bằng 50 lớp; cần augment thời gian + không gian. (2) Baseline CRNN/frame-classifier + smoothing; chính: backbone ConvNeXt/ResNet + Transformer encoder + attention pooling, vì cần quan hệ xa giữa frame. (3) Trích frame → backbone → sequence → CTC/attention pooling → decode chuỗi. (4) Metric chuỗi (accuracy chuỗi, CER/WER) + confusion các ký hiệu giống nhau, không dùng accuracy frame. (5) Pretrain, pseudo-label, ensemble, distill bản nhẹ real-time. *Tự chấm: mỗi ý rubric 2đ, đủ 5 ý = 10đ.* → Xem §3.3, §3.9, §4.5.

**E02 (Hoa–Việt, NLP).** (1) Cặp song ngữ lệch độ dài, từ TMĐT, số/tiền tệ phải giữ nghĩa; BPE chung; chia val theo miền. (2) Baseline Seq2Seq+attention; chính Transformer (multi-head + positional) hoặc fine-tune MT pretrain. (3) Tiền xử lý → BPE → label smoothing → beam search. (4) SacreBLEU + đánh giá người câu khó + giám sát độ dài. (5) Back-translation, pretrain đa ngữ, ensemble, rerank, từ điển số/riêng. *Tự chấm tương tự.* → Xem §4.5, §4.7.

**E03 (lá khoai tây, detection).** (1) Cần localization + lớp hiếm + nền đồng phức tạp + chạy điện thoại. (2) Baseline EfficientNet classifier; chính YOLO (1-stage, nhẹ, real-time) vì ràng buộc di động; 2-stage chỉ khi cần chính xác vùng nhỏ. (3) Augment → detector + NMS (IoU ≥ 0.5) → lọc ngưỡng; fold theo ruộng. (4) mAP@0.5 (+mAP@[.5:.95]) + P/R lớp hiếm, không accuracy. (5) Focal loss/class weights, pseudo-label, TTA, distill. → Xem §3.6, §3.9.

**E04 (bỏ học, tabular).** (1) Bảng 50k×40, lệch 8%, cần giải thích được. (2) Baseline logistic; chính XGBoost/LightGBM/RF (bảng nhỏ, cần giải thích; không DL vô lý). (3) Missing/outlier → encoding → class weights/SMOTE đúng trong CV → stratified k-fold → hiệu chuẩn ngưỡng theo F1. (4) PR-AUC/F1 + P/R ở ngưỡng vận hành. (5) Feature xu hướng điểm, SHAP, giám sát drift, A/B cảnh báo sớm. → Xem §1.5, §1.7, §1.9.

---
*Đề 02–20: đáp án bổ sung dần theo tiến độ soạn đề.*
