# KIỂM ĐỊNH ĐỘC LẬP BẢN 600 CÂU — CHƯA ĐỦ ĐIỀU KIỆN NGHIỆM THU NỘI DUNG

- Thực hiện: đêm 09/10 sang 10/10/2026, giờ Việt Nam.
- Báo cáo được kiểm tra: docs/BAO_CAO_NANG_CAP_600_CAU_VA_CHONG_BAY_DAP_AN_2026-10-09.md.
- Phạm vi: 6 JSON, 6 Markdown canonical, HTML public/dist/bản server đang phục vụ, 10 suite và kiểm tra bổ sung độc lập.
- Đây là audit: không sửa JSON, Markdown học tập, generator hay HTML. Chỉ tạo báo cáo, prompt sửa và bằng chứng trong tmp/audit_600_2026-10-09/.
- Đối chiếu thay đổi với 6 JSON đã lưu ở tmp/audit_nghiem_thu_lan_3_2026-10-09/source_snapshot/. Không coi kết luận nghiệm thu bản 448 câu là chứng nhận cho bản 600 câu.

## 1. Kết luận thực tế

**Đủ 600 MCQ và các sản phẩm đồng bộ là đúng. “100% verified / hoàn hảo / triệt tiêu hoàn toàn bẫy / sẵn sàng nghiệm thu học thuật” là chưa đúng.**

Đã chạy độc lập cả 10 suite: tất cả exit 0, Vitest 17/17, KaTeX 4.857 đoạn và 0 lỗi parser. Tuy nhiên:

1. Ít nhất **27 câu Đề 04 có bộ lựa chọn lệch chủ đề**, nhiều câu không có phương án trả lời đúng cho đề bài.
2. **OLP01-C10 bị đổi khóa A → B sai**, dù lựa chọn A và lời giải vẫn nói đúng về Ridge.
3. **OLP01-M65 nhầm điều kiện đủ với điều kiện cần và đủ**.
4. **VOAI25-079 bị làm hỏng chuỗi thiết bị PyTorch**, từ 'cuda' thành ' cuda '.
5. Đáp án Q21–Q100 của Đề 04 có quy luật cố định; chiến lược chọn lựa chọn dài nhất vẫn trúng **296/600 = 49,33%** theo khóa hiện tại.
6. Bộ gọi là “đề chính thức” đã thay bộ lựa chọn ở **29/100 câu**; trong đó **8 câu thay cả văn bản phương án được đánh dấu đúng**. Một số là sửa khoảng trắng/OCR, một số thêm nội dung; không thể tuyên bố chỉ sửa ba lựa chọn sai và giữ nguyên 100%.
7. Cache vẫn dùng version cũ dù đổi đề; kết quả cũ có thể khác kết quả chọn lại cùng một phương án.
8. Phần đầu của **5 Markdown đề luyện** vẫn ghi quy mô/thang điểm cũ.

**Khuyến nghị ôn thi:** ưu tiên PDF đề VOAI 2025 nguyên bản và lời giải đã đối chiếu. Tạm tránh dùng các câu lỗi liệt kê bên dưới để học thuộc đáp án. Chưa dùng điểm bộ 600 câu làm bằng chứng về mức sẵn sàng thi ngày 11/10. Không cần mở rộng thêm ngân hàng trước kỳ thi; sửa và khóa bản hiện có.

## 2. Những điểm xác nhận PASS

| Ngân hàng | MCQ | Điểm tối đa | A / B / C / D |
|---|---:|---:|---|
| olp-01 | 100 | 100 | 29 / 32 / 22 / 17 |
| olp-02 | 100 | 100 | 26 / 37 / 18 / 19 |
| olp-03 | 100 | 100 | 30 / 18 / 28 / 24 |
| olp-04 | 100 | 100 | 25 / 25 / 25 / 25 |
| olp-05 | 100 | 100 | 27 / 21 / 37 / 15 |
| voai-2025 | 100 | 100 | 19 / 32 / 21 / 28 |
| Tổng | **600** | **600** | |

- Cả 600 câu đều type=mcq, mỗi câu 1 điểm.
- Kiểm tra độc lập từng block Markdown: prompt, nội dung bốn phương án, khóa và explanation khớp JSON ở cả 600 câu. Đây là **đồng bộ nội dung**, không chứng minh nội dung đúng.
- Kiểm tra dữ liệu chạy trong HTML qua VM: 600/600 câu khớp JSON ở prompt/options/answer/explanation/points/type.
- Public, dist, bản HTML trong thư mục server và HTTP localhost:8080 trả cùng nội dung:
  - 2.848.826 bytes.
  - SHA-256: e3cf40d10bd2843b4887b4e999affe005ae9d6fc3b292dddcd2e45aff3121058.
- VOAI25-026 vẫn có ảnh PNG Base64, 754.987 bytes, SHA-256 396b065dbfdfc0d4dfdb314a53e0621bd734a4828b1b23c62823e7f897d42db5; đề bài không chứa dấu hiệu spoiler đã quét.
- Không mở lại browser để đánh giá giao diện/responsive trong đợt này; các kiểm tra HTML mới là dữ liệu và VM, không phải kiểm thử trình duyệt thật.

Thay đổi quy mô so với snapshot 448: thêm 160 ID, bỏ 8 ID essay, chuyển 12 ID cũ từ code/essay sang MCQ. Do vậy 448 + 160 − 8 = 600. Đây là thay đổi lớn của ngân hàng, không phải chỉ cân bằng độ dài đáp án.

## 3. P0 — 27 câu Đề 04 bị lệch bộ lựa chọn

File: src/data/exams/olp-04.json; lỗi được nhúng nguyên vào Markdown và HTML.

| ID | Nội dung cần trả lời | Bộ lựa chọn hiện tại / lỗi |
|---|---|---|
| OLP04-Q22 | ArcFace: cộng margin vào góc của lớp đích, s cos(theta_y+m) | Toàn bộ lựa chọn nói CBR/VBR/B-frame/macroblock; khóa B là VBR |
| OLP04-Q23 | ST-GCN: liên kết không gian giữa khớp và thời gian giữa frame | Lựa chọn là Cosine/Mahalanobis/Wasserstein/KL; khóa C là Wasserstein |
| OLP04-Q30 | Tạo codebook BoVW bằng clustering, thường K-Means | Không có K-Means; B nói chiếu ngẫu nhiên rồi phân loại SVM |
| OLP04-Q51 | ViT: chia patch, flatten và linear embedding thành chuỗi token | Lựa chọn là các cách sinh/giải mã văn bản; khóa C non-autoregressive decoding |
| OLP04-Q52 | CLS token làm biểu diễn ảnh để phân loại | Lựa chọn nói top-k/top-p sampling |
| OLP04-Q53 | CLIP: contrastive loss giữa ảnh và văn bản | Lựa chọn nói random orthogonal / fine-tuning / LoRA / binary weights |
| OLP04-Q54 | CLIP zero-shot: so sánh image embedding với text embedding các nhãn | Lựa chọn nói QLoRA/pruning/CPU/pipeline parallelism |
| OLP04-Q55 | SAM: spatial prompts như điểm, bounding box, mask | Lựa chọn nói reward model và văn bản |
| OLP04-Q56 | DDPM forward: Gaussian transition từng bước | Lựa chọn nói PPO và DPO |
| OLP04-Q57 | U-Net trong DDPM chuẩn dự đoán nhiễu | Lựa chọn nói RAG và cách xử lý LLM |
| OLP04-Q59 | Stable Diffusion: diffusion trong latent space của autoencoder | Lựa chọn về truy vấn/nén vector, khóa C Hamming/XOR |
| OLP04-Q60 | GCN: D^(-1/2)(A+I)D^(-1/2) | Lựa chọn là các cặp thành phần hệ thống khác; khóa D CNN + K-Means |
| OLP04-Q61 | GAT: learnable attention và softmax trên láng giềng | Lựa chọn nói reranker; khóa A bi-encoder |
| OLP04-Q62 | MPNN: message function và update function | Lựa chọn nói dense retrieval/BM25, Fourier, SVD, CNN |
| OLP04-Q76 | HNSW: đồ thị small-world phân cấp | Không có cấu trúc graph; khóa B cắt ngẫu nhiên 90% chiều |
| OLP04-Q77 | Chunk size: đánh đổi context với độ chính xác truy xuất | Lựa chọn nói IVF/KD-tree/LSH/L2 ordering |
| OLP04-Q78 | Bi-encoder nhanh, cross-encoder mô hình hóa tương tác Query–Doc | Lựa chọn là metric/latency/diversity; khóa B NDCG |
| OLP04-Q79 | DPO: tối ưu preference trực tiếp, tránh reward model/PPO riêng | Lựa chọn nói hạn chế của DDPM; khóa B hàng trăm bước diffusion |
| OLP04-Q80 | AWQ: dùng activation bảo vệ các trọng số/kênh quan trọng | Lựa chọn toàn bộ nói DDIM |
| OLP04-Q81 | GQA: nhóm query heads dùng chung key/value heads | Lựa chọn nói conditioning U-Net |
| OLP04-Q82 | Speculative decoding: draft model + target verification/accept-reject | Lựa chọn nói CFG/Fourier/ảnh |
| OLP04-Q83 | DINO: attention thể hiện vùng đối tượng không cần nhãn | Lựa chọn nói VAE/JPEG/diffusion |
| OLP04-Q84 | MAE: masking khoảng 75%, ảnh dư thừa thông tin không gian | Lựa chọn nói cách thay đổi U-Net/Fourier |
| OLP04-Q85 | YOLOv8 anchor-free | Lựa chọn nói tự giám sát/gradient; khóa C xấp xỉ Jacobi |
| OLP04-Q86 | Soft-NMS: giảm score theo overlap thay vì xóa cứng | Lựa chọn nói representation collapse/gradient explosion |
| OLP04-Q87 | COCO AP trung bình qua 10 ngưỡng IoU .50:.05:.95 | Lựa chọn nói contrastive learning/mẫu âm |
| OLP04-Q88 | ControlNet: giữ backbone, nhánh học và zero-initialized convolutions | Lựa chọn nói BYOL/covariance/SVD/normalization |

Danh sách đầy đủ 27 câu này có trong tmp/audit_600_2026-10-09/grafted_option_evidence.json, lưu nguyên prompt/options/answer.

Ví dụ Q22: lời giải nói đúng về góc ArcFace, nhưng kết thúc “Chọn B”, trong khi B hiện là VBR. Vì vậy kiểm tra chữ “Chọn B” trùng khóa B **vẫn pass**. Cần kiểm tra nội dung lựa chọn, không chỉ chữ cái.

Không khẳng định đã truy được script/câu nguồn gây ghép nhầm. Kết luận dựa trên nội dung hiện tại rõ ràng lệch nhau. Sửa **cả bốn lựa chọn**, khóa, lời giải phân tích từng phương án và artifact đồng bộ; không chữa bằng đổi một chữ cái.

Các nguồn chính dùng để đối chiếu mẫu:
- [ArcFace, CVPR 2019](https://openaccess.thecvf.com/content_CVPR_2019/papers/Deng_ArcFace_Additive_Angular_Margin_Loss_for_Deep_Face_Recognition_CVPR_2019_paper.pdf): additive angular margin vào góc lớp đích.
- [ViT, ICLR 2021](https://openreview.net/pdf?id=YicbFdNTTy): ảnh thành chuỗi patch embedding; class token dùng cho classification.
- [GCN, tác giả Thomas Kipf](https://tkipf.github.io/graph-convolutional-networks/): graph convolution với adjacency đã chuẩn hóa.

## 4. P1 — Khóa sai và sai kiến thức

### 4.1 OLP01-C10: Ridge bị chấm sai

src/data/exams/olp-01.json, ID ở dòng 1213 tại snapshot audit.

- Khóa hiện tại: B — “Vì L2 tính toán không cần ma trận”.
- A trình bày Ridge giúp ổn định đa cộng tuyến và X^T X + lambda I khả nghịch.
- Lời giải hiện tại dẫn đúng công thức Ridge, lambda>0 và ghi “Chọn A”.
- Snapshot trước nâng cấp: khóa A.
- Đã thử engine HTML thực tế trong VM: chọn A → WA/0; chọn B → AC/1.

**Sửa khóa về A** và diễn đạt A/lời giải chính xác hơn: Ridge co trọng số; X^T X+lambda I xác định dương khi lambda>0. Lasso có xu hướng chọn một vài biến trong nhóm tương quan, không diễn đạt thành định luật luôn chọn ngẫu nhiên đúng một biến.

Đây cũng là phản ví dụ trực tiếp với báo cáo “khóa bảo toàn 100%”. Các ID essay/code được chuyển sang MCQ đương nhiên cần khóa mới; không tính chúng là lỗi đổi khóa. C10 là câu MCQ cũ có khóa thực sự bị đổi sai.

### 4.2 OLP01-M65: xác định dương là đủ, không cần

Đề hỏi điều kiện **cần và đủ** cho cực tiểu toàn cục duy nhất, chọn Hessian xác định dương.

Phản ví dụ: f(w)=w^4 trên R, f'(0)=0, f''(0)=0; 0 vẫn là cực tiểu toàn cục duy nhất. Do đó positive definite Hessian không phải điều kiện cần.

Sửa câu hỏi thành **điều kiện đủ**, làm rõ f lồi, miền mở lồi và điểm dừng nằm trong miền; H(w*) xác định dương. Sửa lời giải tránh đồng nhất “unique minimum” với “mọi hướng luôn có độ cong dương”.

Nguồn: [Boyd & Vandenberghe, Convex Optimization, §3.1.4](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), có chính phản ví dụ x^4.

### 4.3 VOAI25-079: sửa OCR làm hỏng string literal

Phương án được chấm B hiện là model.to(' cuda '), khác model.to('cuda'). Khoảng trắng nằm **trong** string literal nên thay đổi tên thiết bị; không phải chỉ khác cách trình bày.

[Mã nguồn parser thiết bị PyTorch](https://github.com/pytorch/pytorch/blob/main/c10/core/Device.cpp) chỉ nhận tên thiết bị với ký tự chữ/underscore và index tùy chọn; space làm parser báo invalid device string. Runtime Python dùng trong audit không có torch nên **không tuyên bố đã chạy PyTorch**; kết luận dựa trên parser chính thức và chuỗi hiện tại.

Sửa B về model.to('cuda'); bảo vệ code/string literals khi làm sạch OCR. Quét lại những đoạn code sau sửa, không thay spacing bên trong literal theo quy tắc văn xuôi.

### 4.4 Câu mới cần chỉnh chính xác thêm

- VOAI02-M80: B nói TN lớn khiến FPR “luôn” rất nhỏ và ROC-AUC cao giả tạo. Sai về tính tất yếu. FPR=FP/(FP+TN); nếu dự đoán tất cả âm thành dương thì FPR=1 dù lớp âm rất lớn. Chỉ một confusion matrix ở một threshold không suy ra ROC-AUC=0.98. Viết lại: FPR nhỏ vẫn có thể đi cùng FP nhiều hơn TP, khiến precision thấp; PR hữu ích để thấy điều này. Không tự gán AUC nếu không có ranked scores/đường cong.
- VOAI02-M92: “mở rộng receptive field theo cấp số” không chính xác nếu nói về một lớp với dilation d. Công thức ngay trong lời giải là K_eff=1+(K−1)d, tuyến tính theo d. Bỏ “theo cấp số”; nếu muốn nói tăng theo cấp số phải nêu mạng nhiều tầng và lịch dilation tăng tương ứng.
- OLP04-Q92: biểu thức (z−mu)^T Sigma^-1(z−mu) là **squared Mahalanobis distance**. Có thể dùng làm score như paper; đổi ký hiệu sang d_M^2 hoặc ghi rõ bình phương, tránh gọi nhầm distance không có sqrt. Không kết luận lựa chọn A/B/C là các phương pháp OOD vô dụng; chúng sai vì không mô tả cơ chế Mahalanobis được hỏi. [Paper Lee et al., NeurIPS 2018](https://papers.neurips.cc/paper_files/paper/2018/file/abdeb6f575ac5c6676b747bca8d09cc2-Paper.pdf).

## 5. P1 — Chống đoán đáp án chưa đạt

### 5.1 Khóa Đề 04 có cấu trúc cố định

- Q21–Q60: ABCD lặp đúng 10 lần.
- Q61–Q70: A cả 10.
- Q71–Q80: B cả 10.
- Q81–Q90: C cả 10.
- Q91–Q100: D cả 10.

Quy tắc này khớp **80/80 câu mới**, không cần hiểu đề. Tổng A=B=C=D=25 không chứng minh thứ tự đáp án khó đoán. Đảo lựa chọn theo seed cố định trong **đề luyện**, cập nhật khóa và mọi chữ cái trong lời giải. Đề nguyên bản chính thức phải giữ thứ tự gốc.

### 5.2 Chọn câu dài nhất vẫn trúng cao

Đo bằng độ dài ký tự thô của option text, chọn lựa chọn dài nhất; khi hòa chọn thứ tự A→D:

| Đề | Trúng /100 | Đúng là lựa chọn dài nhất duy nhất |
|---|---:|---:|
| 01 | 55 | 50 |
| 02 | 56 | 50 |
| 03 | 54 | 48 |
| 04 | 47 | 46 |
| 05 | 44 | 39 |
| VOAI 2025 hiện tại | 40 | 37 |
| Tổng | **296/600 (49,33%)** | **270/600 (45%)** |

Đây là thống kê mô tả theo khóa hiện tại, không phải ước lượng chất lượng học hay xác suất trúng một đề tương lai. Nhưng nó đủ bác bỏ tuyên bố “triệt tiêu hoàn toàn bẫy chọn câu dài”.

Scanner chỉ bắt correct dài hơn wrong dài nhất >35% và chênh >=20 ký tự. Correct dài hơn ít hơn ngưỡng vẫn có thể giúp đoán. Với cách hiểu cả bốn lựa chọn nằm trong ±15% độ dài trung bình của câu, **208/600 câu không đạt**. Báo cáo chưa định nghĩa tâm dung sai; không nên gọi ±15% là yêu cầu đã được kiểm định khi test dùng 35%.

Không kéo dài phương án sai bằng câu vô nghĩa. Ưu tiên tính đúng/sai rõ ràng và độ hợp lý của distractor. Với đề gốc, giữ nguyên wording để ôn đúng nguồn.

### 5.3 Scanner không làm pipeline fail

scratch/inspect_all_giveaways.py chỉ in số lượng, không assert / sys.exit(1) khi phát hiện cue. Wrapper chạy theo exit code nên có cue vẫn có thể báo suite PASS.

Sửa gate thật và thêm thống kê run/periodic pattern, longest-option heuristic. Mẫu hình thức không chứng minh câu đúng kiến thức; vẫn cần nội dung chuyên môn.

## 6. P1 — “Đề chính thức” đã biến thành bản chỉnh biên

Đối chiếu snapshot đã lưu:
- 29/100 câu thay options.
- 10/100 câu thay prompt.
- 0/100 đổi letter key.
- 8 câu thay text của option được đánh dấu đúng: 006, 021, 024, 029, 042, 057, 079, 088.
- Ví dụ 029 thêm Momentum vào đáp án đúng; 079 thêm space vào literal cuda.
- Trong 8 thay đổi, một số là khôi phục OCR/công thức, không phải tất cả đều sai. Tuy nhiên tuyên bố “giữ nguyên đúng option, chỉ nâng ba option sai” không phù hợp dữ liệu.

Cần giữ bộ **nguyên bản đối chiếu PDF** để luyện đúng format năm trước. Nếu cần phiên bản distractor nâng cấp thì tạo/đặt tên **VOAI 2025 chỉnh biên**, công khai các khác biệt, không gắn nhãn “100% nguyên bản BTC”. Không tự gọi lời giải đối chiếu của tác giả bên ngoài là đáp án chính thức BTC.

## 7. P1/P2 — Cache và mô tả cũ

### Cache version chưa tăng

Version hiện tại vẫn 01=2, 02=2, 03=3, 04=2, 05=2, VOAI=2.

Thử cùng cache C10 version 2 từ khóa cũ:
- selected=A, verdict=AC: load được 1/100; chọn lại A bị 0/100 theo khóa B hiện tại.
- selected=B, verdict=WA: load được 0/100; chọn lại B được 1/100.
- Khi sửa khóa về A, cache đã tạo bởi bản sai B vẫn phải bị vô hiệu/regrade.

Engine MCQ cộng q.points hiện tại, **không** cộng điểm cũ lưu trong cache; lỗi đã chứng minh là **verdict cũ**, không khẳng định cache points gây tổng điểm vượt 100.

Sửa version cho ngân hàng thay đổi hoặc sử dụng fingerprint của dữ liệu chấm, đảm bảo lời giải/chọn đáp án được cập nhật đồng bộ. Thêm test cache từ bản 448 đã chốt và bản 600 lỗi, thay vì chỉ v1→v2.

### Header 5 Markdown sai

- Đề01 vẫn ghi 60 auto/2 code/4 essay.
- Đề02 vẫn 66 câu, 150 điểm, 6 essay.
- Đề03 vẫn 104 câu và 4 essay.
- Đề04 vẫn 20 MCQ +4 essay.
- Đề05 vẫn 90 câu/90 điểm.
- Nội dung thân các file có đủ 100 câu; cập nhật phần đầu và bảng phân bố theo dữ liệu mới.

### Reference tồn tại nhưng không đúng chủ đề

OLP01-M65 và VOAI02-M67 dẫn §1.1 với tên “Cơ Sở Tối Ưu Hóa & Gradient Descent”, nhưng §1.1 trong giáo trình hiện tại là **k-NN**. Suite check_section_refs chỉ chứng minh ID section tồn tại. Cần dẫn tới đúng mục thực tế hoặc bổ sung mục lý thuyết rõ ràng và đúng nội dung.

## 8. Các kiểm thử đã chạy và giới hạn

Thực thi tương đương 10 mục trong báo cáo bằng runtime Node/Python có đường dẫn tuyệt đối:

1. Python -X utf8 scratch/inspect_all_giveaways.py — exit0, ba cue=0 trên 6 đề; scanner chưa có fail gate.
2. Node scripts/audit_katex_syntax.mjs — 4.857 công thức, 0 lỗi cú pháp.
3. Node scripts/validate.mjs — 600 MCQ, 6×100 điểm.
4. Python -X utf8 scripts/check_markdown_sync.py — exit0; script hiện chủ yếu kiểm ID/key/nhãn A–D.
5. Python -X utf8 scripts/check_section_refs.py — 59 section, 0 missing reference.
6. Python -X utf8 scripts/test_quality_all.py — exit0.
7. Node scripts/test_academic_rigor.mjs — numerical Focal Loss khớp, escape/placeholder checks pass; không chứng minh toàn bộ 600 câu khoa học đúng.
8. Node scripts/test_html_logic.mjs — 5 nhóm kiểm thử VM pass.
9. Node node_modules/vitest/vitest.mjs run src — 4 file, 17 tests pass.
10. Node node_modules/typescript/bin/tsc --noEmit — exit0.

Runtime:
- Node: C:\Users\HP\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe
- Python: C:\Users\HP\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe

Bổ sung:
- Python tmp/audit_600_2026-10-09/independent_checks.py — full text sync, thống kê 600 câu, bias, manifest và HTTP.
- Node tmp/audit_600_2026-10-09/cache_probe.mjs — tái hiện cache/khóa C10.
- Node tmp/audit_600_2026-10-09/runtime_data_probe.mjs — dữ liệu HTML và ảnh Q26.
- Các lượt đọc file/scoped rg và Python inline để đối chiếu snapshot, đọc câu mới, kiểm key/explanation, trích header/line number. Hai lượt phân tích đầu dùng nhầm cấu trúc option (list và trường key) bị lỗi, đã sửa và chạy lại thành công; không tạo kết luận từ đầu ra chưa hoàn tất.
- Đọc nguồn sơ cấp web nêu trong các mục phát hiện. Không cài torch; không chạy generator, build hay script tự sửa.

Chi tiết lệnh và stdout của 10 suite: tmp/audit_600_2026-10-09/test_runs.json. Manifest/thống kê: independent_results.json. Bằng chứng cache: cache_proof.json. Dữ liệu HTML/ảnh: runtime_data_proof.json.

Chỉ tạo:
- docs/VERIFY_NANG_CAP_600_CAU_2026-10-10.md (file này).
- docs/PROMPT_GEMINI_SUA_600_CAU_2026-10-10.md.
- Các file audit/source_snapshot trong tmp/audit_600_2026-10-09/.

Giới hạn: đã kiểm cấu trúc/đồng bộ toàn bộ 600; đã đọc prompt và text phương án được chấm của 172 câu mới/chuyển loại, kiểm cả bốn phương án ở các nhóm lỗi. Chưa chứng nhận từng distractor và mọi lời giải của toàn bộ 600 câu là chính xác. Những lỗi đã chứng minh đủ để bác bỏ nghiệm thu 100%; số lỗi khoa học thực tế có thể lớn hơn danh sách này.

