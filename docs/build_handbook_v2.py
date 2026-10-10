# -*- coding: utf-8 -*-
"""
Script biên soạn Sổ tay Ôn thi Toàn diện Olympic AI HCMUS 2026 (Phiên bản Mở rộng Toàn diện V2)
Tích hợp:
- §1 -> §5: 5 Chương lý thuyết cốt lõi & toán học chuyên sâu (Ma trận trực giao, Hessian, Conv2D, ViT, NLP, Time-Series)
- §6: Bảng 24 Bẫy Đề Thi Kinh Điển (SAI -> ĐÚNG)
- §7: Chuyên đề 4 Tác vụ Thực chiến OLP AI 2025 & 2026 (Khung 5 bước)
- §8: Trọn bộ 50 Câu Trắc Nghiệm Đề Thi Thử VOAI 2026 Kèm Đáp Án & Lời Giải Chi Tiết Từng Câu
- §9: Ma Trận Đối Chiếu Tra Cứu Web App & Hướng Dẫn Ôn Luyện Nước Rút
"""

import os
import sys
import subprocess
import shutil

# Nạp dữ liệu 50 câu VOAI
sys.path.insert(0, os.path.dirname(__file__))
from voai_50_questions_data import VOAI_QUESTIONS

def escape_tex_text(text):
    """Xử lý ký tự an toàn nhưng giữ nguyên công thức toán học"""
    return text

def generate_tex():
    tex_parts = []
    
    # ------------------ PREAMBLE ------------------
    tex_parts.append(r'''\documentclass[10pt,a4paper]{article}

\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Consolas}

\usepackage[top=2cm, bottom=2.2cm, left=2cm, right=2cm]{geometry}
\usepackage{amsmath,amssymb,amsfonts,mathtools}
\usepackage{booktabs,tabularx,xltabular,array}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{hyperref}
\usepackage[most]{tcolorbox}
\usepackage{listings}

% Định nghĩa màu sắc học thuật
\definecolor{primaryblue}{RGB}{15, 45, 105}
\definecolor{secondaryblue}{RGB}{30, 90, 180}
\definecolor{darkslate}{RGB}{35, 45, 60}
\definecolor{boxbg}{RGB}{245, 248, 255}
\definecolor{boxborder}{RGB}{180, 205, 240}
\definecolor{trapbg}{RGB}{255, 245, 245}
\definecolor{trapborder}{RGB}{235, 160, 160}
\definecolor{traptit}{RGB}{170, 30, 30}
\definecolor{exambg}{RGB}{245, 255, 248}
\definecolor{examborder}{RGB}{160, 220, 180}
\definecolor{examtit}{RGB}{20, 120, 60}
\definecolor{codebg}{RGB}{248, 250, 252}
\definecolor{ansbg}{RGB}{240, 250, 245}
\definecolor{ansborder}{RGB}{120, 200, 150}
\definecolor{anstit}{RGB}{10, 110, 50}

% Cấu hình Hyperref
\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=secondaryblue,
    urlcolor=primaryblue,
    pdftitle={Cam Nang On Tap Toan Dien Olympic AI HCMUS 2026},
    pdfauthor={Ban Huan Luyen Olympic AI}
}

% Cấu hình Header và Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\textcolor{darkslate}{\textbf{Olympic AI HCMUS 2026} --- Cẩm Nang Ôn Thi Vòng Loại Cấp Trường}}
\fancyhead[R]{\small\textcolor{darkslate}{\thepage}}
\fancyfoot[C]{\footnotesize\textcolor{gray}{Lưu hành nội bộ học thuật --- Chuẩn bị cho Kỳ thi Vòng loại 11/10/2026}}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.3pt}

% Cấu hình Section Heading
\titleformat{\section}
  {\normalfont\Large\bfseries\color{primaryblue}}{\S\thesection}{0.8em}{}[\titlerule]
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{secondaryblue}}{\S\thesubsection}{0.6em}{}
\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries\color{darkslate}}{\S\thesubsubsection}{0.5em}{}

% Cấu hình tcolorbox
\newtcolorbox{takeawaybox}[1]{
    colback=boxbg,
    colframe=boxborder,
    coltitle=primaryblue,
    fonttitle=\bfseries\small,
    title={#1},
    arc=2mm,
    boxrule=0.8pt,
    left=3mm, right=3mm, top=2mm, bottom=2mm
}

\newtcolorbox{trapbox}[1]{
    colback=trapbg,
    colframe=trapborder,
    coltitle=traptit,
    fonttitle=\bfseries\small,
    title={\textbf{[BẪY THI CẦN TRÁNH]} --- #1},
    arc=2mm,
    boxrule=0.8pt,
    left=3mm, right=3mm, top=2mm, bottom=2mm
}

\newtcolorbox{examplebox}[1]{
    colback=exambg,
    colframe=examborder,
    coltitle=examtit,
    fonttitle=\bfseries\small,
    title={\textbf{[VÍ DỤ TÍNH TOÁN TAY]} --- #1},
    arc=2mm,
    boxrule=0.8pt,
    left=3mm, right=3mm, top=2mm, bottom=2mm
}

\newtcolorbox{solbox}[1]{
    colback=ansbg,
    colframe=ansborder,
    coltitle=anstit,
    fonttitle=\bfseries\small,
    title={\textbf{[ĐÁP ÁN \& LỜI GIẢI CHI TIẾT]} --- #1},
    arc=2mm,
    boxrule=0.8pt,
    left=3mm, right=3mm, top=2mm, bottom=2mm
}

\setlength{\parskip}{0.4em}
\setlength{\parindent}{0pt}

\begin{document}

% ----------------- TIÊU ĐỀ TÀI LIỆU -----------------
\begin{center}
    {\Huge \textbf{\color{primaryblue} CẨM NANG ÔN TẬP TOÀN DIỆN VÒNG LOẠI OLYMPIC AI 2026}} \\[0.5em]
    {\LARGE \textbf{\color{secondaryblue} Lý thuyết Cốt lõi, Đạo hàm Toán học, 50 Câu Đề Thi VOAI Kèm Lời Giải \& Ma Trận Tra Cứu Web}} \\[0.8em]
    {\normalsize \textbf{Biên soạn phục vụ Kỳ thi Tuyển chọn Đội tuyển Olympic Trí tuệ Nhân tạo HCMUS (Vòng loại 11/10/2026)}} \\[0.4em]
    {\small \textit{Tham chiếu Chuẩn kiến thức: Olympic Tin học \& AI Việt Nam (VOAI 2026), International Olympiad in AI (IOAI 2026) \& OLP AI 2025}}
\end{center}

\vspace{0.5em}
\hrule height 1.2pt
\vspace{0.8em}

\begin{abstract}
\noindent Cẩm nang học thuật này được thiết kế theo cấu trúc chuyên khảo toàn diện chuẩn bài báo khoa học (Academic Reference Monograph), nhằm cung cấp toàn bộ hệ thống lý thuyết, công thức toán học, \textbf{giải thích chi tiết từng biến số, tham số, chiều dữ liệu và trực giác cơ chế} cho thí sinh tham dự Vòng loại Olympic AI HCMUS 2026. Nội dung bao quát 5 chương trọng tâm: \textbf{Machine Learning Cổ điển}, \textbf{Deep Learning \& PyTorch Framework}, \textbf{Thị giác Máy tính (CV)}, \textbf{Xử lý Ngôn ngữ Tự nhiên (NLP)} và \textbf{Toán \& Xác suất Thống kê cho AI}. Toàn bộ các công thức toán học, bài toán tính tay kinh điển (Ma trận trực giao, Hessian, Conv2D dimensions, Bayes base-rate fallacy, Entropy, Information Gain, IoU, F1-score, Cosine similarity) và 24 bẫy đề thi trắc nghiệm được đối chiếu minh bạch. Đặc biệt, tài liệu bổ sung \textbf{Trọn bộ 50 câu trắc nghiệm thực chiến đề thi thử VOAI 2026 kèm đáp án và lời giải chi tiết 100\% từng câu}, cùng \textbf{Bảng Ma Trận Tra Cứu Nhanh kết nối trực tiếp với Web App Ôn Thi} (\url{https://lenamkhanhh.github.io/OLPAI26-Khanhdz/}) để thí sinh luyện đề và tra cứu cơ sở đáp án tức thì.
\end{abstract}

\vspace{0.5em}
\tableofcontents
\vspace{1em}
\hrule
\vspace{1em}
''')

    # ------------------ ĐỌC CÁC CHƯƠNG LÝ THUYẾT GỐC TỪ build_handbook_pdf.py ------------------
    # Ta sẽ trích xuất các section từ file build_handbook_pdf.py hiện có (từ section 1 đến section 7)
    with open(r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26\docs\build_handbook_pdf.py", "r", encoding="utf-8") as f:
        old_code = f.read()
    
    # Tìm đoạn từ \section{Machine Learning Cổ Điển đến trước \end{document}
    start_sec1 = old_code.find(r"\section{Machine Learning Cổ Điển (Classical Machine Learning)}")
    end_sec7 = old_code.find(r"\begin{center}" + "\n" + r"    {\small \textbf{--- HẾT TÀI LIỆU")
    if end_sec7 == -1:
        end_sec7 = old_code.find(r"\end{document}")
    
    body_content = old_code[start_sec1:end_sec7].strip()
    
    # Bổ sung lý thuyết toán học chuyên sâu vào mục Toán & Xác suất Thống kê nếu chưa có
    # Kiểm tra xem đã có Ma trận trực giao và Hessian chưa:
    if r"Ma trận Trực Giao \& Ma Trận Hessian" not in body_content:
        extra_math = r'''
\subsection{Đại Số Tuyến Tính Nâng Cao Cho AI: Ma Trận Trực Giao \& Ma Trận Hessian}
\textbf{1. Ma trận Trực Giao (Orthogonal Matrix):}
Ma trận vuông $A \in \mathbb{R}^{n \times n}$ được gọi là ma trận trực giao nếu tích với chuyển vị của nó bằng ma trận đơn vị:
\begin{equation}
    A^T A = A A^T = I_n \implies A^{-1} = A^T
\end{equation}
\begin{itemize}[leftmargin=*]
    \item \textbf{Định thức:} $\det(A^T A) = \det(A)^2 = \det(I) = 1 \implies \det(A) = \pm 1 \neq 0$. Do đó $A$ luôn khả nghịch (không bao giờ suy biến).
    \item \textbf{Bảo toàn tích vô hướng và độ dài vector:} $\langle A\mathbf{x}, A\mathbf{y} \rangle = (A\mathbf{x})^T (A\mathbf{y}) = \mathbf{x}^T A^T A \mathbf{y} = \mathbf{x}^T \mathbf{y} = \langle \mathbf{x}, \mathbf{y} \rangle$. Do đó $\|A\mathbf{x}\|_2 = \|\mathbf{x}\|_2$, phép biến đổi trực giao giữ nguyên khoảng cách Euclid và góc giữa các vector (ứng dụng trong phép quay và phản xạ không gian).
\end{itemize}

\textbf{2. Ma trận Hessian \& Điều Kiện Cực Trị Bậc Hai (Second-Order Optimality):}
Cho hàm số khả vi hai lần $f: \mathbb{R}^n \to \mathbb{R}$. Ma trận Hessian $H(\mathbf{x}) = \nabla^2 f(\mathbf{x}) \in \mathbb{R}^{n \times n}$ chứa toàn bộ các đạo hàm riêng bậc hai:
\begin{equation}
    H_{ij}(\mathbf{x}) = \frac{\partial^2 f(\mathbf{x})}{\partial x_i \partial x_j}
\end{equation}
Tại điểm dừng $\mathbf{x}^*$ (nơi gradient triệt tiêu $\nabla f(\mathbf{x}^*) = \mathbf{0}$):
\begin{itemize}[leftmargin=*]
    \item \textbf{Xác định dương ($H \succ 0$, mọi trị riêng $\lambda_i > 0$):} $\mathbf{u}^T H \mathbf{u} > 0, \; \forall \mathbf{u} \neq \mathbf{0} \implies \mathbf{x}^*$ là \textbf{Điểm cực tiểu địa phương (Local Minimum)}.
    \item \textbf{Xác định âm ($H \prec 0$, mọi trị riêng $\lambda_i < 0$):} $\mathbf{u}^T H \mathbf{u} < 0, \; \forall \mathbf{u} \neq \mathbf{0} \implies \mathbf{x}^*$ là \textbf{Điểm cực đại địa phương (Local Maximum)}.
    \item \textbf{Không xác định dấu (Indefinite, có cả $\lambda_i > 0$ và $\lambda_j < 0$):} $\mathbf{x}^*$ là \textbf{Điểm yên ngựa (Saddle Point)}.
\end{itemize}

\subsection{Kỹ Thuật Cross-Validation Cho Time-Series \& Chống Rò Rỉ Dữ Liệu (Data Leakage)}
\begin{trapbox}{Tuyệt đối không dùng K-Fold ngẫu nhiên cho Dữ liệu Chuỗi thời gian}
Dữ liệu chuỗi thời gian có tính phụ thuộc thời gian (Temporal Autocorrelation). Nếu dùng K-Fold ngẫu nhiên, mô hình sẽ sử dụng dữ liệu ở tương lai để dự đoán cho quá khứ (Look-ahead bias / Target leakage), dẫn đến điểm validation cao ảo nhưng mô hình sụp đổ hoàn toàn khi triển khai thực tế.
\begin{itemize}[leftmargin=*]
    \item \textbf{Chiến lược đúng:} Dùng \textbf{Time-Series Split} (Rolling Window hoặc Expanding Window), trong đó tập Train luôn diễn ra trước tập Validation theo dòng thời gian.
    \item \textbf{Quy tắc chống Data Leakage:} Mọi thao tác tính toán đặc trưng (Fit StandardScaler, Imputer, Target Encoding) \textbf{chỉ được thực hiện trên tập Train}, sau đó dùng các tham số đó áp dụng (Transform) lên tập Test/Validation. Tuyệt đối không gọi `fit` trên toàn bộ tập dữ liệu trước khi chia train/test!
\end{itemize}
\end{trapbox}
'''
        # Chèn vào trước Section 6
        idx_sec6 = body_content.find(r"\section{Bảng 24 Bẫy Đề Thi Kinh Điển")
        if idx_sec6 != -1:
            body_content = body_content[:idx_sec6] + extra_math + "\n\n" + body_content[idx_sec6:]
        else:
            body_content += "\n\n" + extra_math

    tex_parts.append(body_content)

    # ------------------ CHƯƠNG 8: BỘ 50 CÂU THỰC CHIẾN VOAI 2026 ------------------
    tex_parts.append(r'''
\newpage
% =========================================================================
% CHƯƠNG 8: TRỌN BỘ 50 CÂU TRẮC NGHIỆM ĐỀ THI THỬ VOAI 2026 (KÈM ĐÁP ÁN & GIẢI THÍCH CHI TIẾT)
% =========================================================================
\section{Bộ Đề Luyện Thi Thực Chiến Chuẩn VOAI 2026 (50 Câu) --- Kèm Đáp Án \& Giải Thích Chi Tiết}

\begin{abstract}
\noindent Chương này tập hợp trọn vẹn \textbf{50 câu hỏi trắc nghiệm của Đề thi thử Vòng loại VOAI 2026} (Đỗ Đình Luật). Đây là bộ đề được đánh giá bám sát nhất cấu trúc kiến thức và phong cách ra đề của kỳ thi Olympic AI. Toàn bộ 50 câu đều được trình bày kèm \textbf{đáp án chính thức}, \textbf{chứng minh/tính toán toán học chi tiết}, \textbf{mục tra cứu lý thuyết tương ứng trong Handbook (§x.y)} và \textbf{các bẫy đề thi cần phòng tránh}, tạo thành công cụ đối chiếu tuyệt đối cho thí sinh khi luyện đề trên Web App.
\end{abstract}
''')

    import re
    def sanitize_tex(text):
        if not text:
            return ""
        text = re.sub(r'(?<!\\)%', r'\%', text)
        text = re.sub(r'(?<!\\)&', r'\&', text)
        tokens = text.split('$')
        for i in range(0, len(tokens), 2):
            tokens[i] = re.sub(r'(?<!\\)_', r'\_', tokens[i])
        return '$'.join(tokens)

    for q in VOAI_QUESTIONS:
        qid = q["id"]
        qtext = sanitize_tex(q["question"])
        opts = [sanitize_tex(o) for o in q["options"]]
        ans = q["correct"]
        expl = sanitize_tex(q["explanation"])
        sec = sanitize_tex(q["section_ref"])
        trap = sanitize_tex(q["trap"])

        opt_items = "\n".join([f"    \\item {opt[3:]}" for opt in opts])

        q_tex = f'''
\\subsection*{{Câu {qid} (Đề thi thử VOAI 2026)}}
\\textbf{{Đề bài:}} {qtext}

\\begin{{enumerate}}[label=\\textbf{{\\Alph*.}}]
{opt_items}
\\end{{enumerate}}

\\begin{{solbox}}{{Đáp án đúng: \\textbf{{{ans}}}}}
\\textbf{{Phân tích \\& Chứng minh chi tiết:}} \\\\
{expl}

\\vspace{{0.4em}}
\\textbf{{Căn cứ tra cứu trong Handbook:}} Tham chiếu mục \\textbf{{{sec}}}.

\\vspace{{0.4em}}
\\textbf{{Bẫy đề thi cần tránh:}} \\textit{{{trap}}}
\\end{{solbox}}
\\vspace{{0.5em}}
'''
        tex_parts.append(q_tex)

    # ------------------ CHƯƠNG 9: MA TRẬN ĐỐI CHIẾU TRA CỨU WEB APP ------------------
    tex_parts.append(r'''
\newpage
% =========================================================================
% CHƯƠNG 9: MA TRẬN ĐỐI CHIẾU TRA CỨU WEB APP & HƯỚNG DẪN ÔN LUYỆN NƯỚC RÚT
% =========================================================================
\section{Ma Trận Đối Chiếu Tra Cứu Web App \& Lộ Trình Ôn Luyện Nước Rút}

\subsection{Phương Pháp Kết Hợp Web App Thi Thử \& Handbook PDF}
Web App Ôn Thi OLP AI HCMUS 2026 (\url{https://lenamkhanhh.github.io/OLPAI26-Khanhdz/}) được thiết kế tối ưu cho việc rèn luyện phản xạ làm bài thi kiểu app GPLX 600 câu. Để đạt hiệu quả tối đa:
\begin{enumerate}[leftmargin=*]
    \item \textbf{Pha 1 --- Luyện tập có phản hồi (Practice Mode trên Web):} Khi làm từng câu hỏi trong chế độ Practice, nếu trả lời sai hoặc chưa chắc chắn, đọc phần giải thích inline ngay dưới câu hỏi, đồng thời ghi chú mã mục lý thuyết (ví dụ \S1.4, \S3.1, \S5.2).
    \item \textbf{Pha 2 --- Đọc sâu bản chất trong Handbook PDF:} Mở tài liệu này tại đúng mục \S tương ứng để nắm vững công thức toán học, trực giác hình học, các tham số và các biến thể bẫy đề thi.
    \item \textbf{Pha 3 --- Thi thử tính giờ (Exam Mode trên Web):} Làm trọn vẹn đề thi 60 câu trắc nghiệm/code trong 90 phút mà không xem tài liệu. Đạt từ 70\% điểm trở lên (ĐẠT) để đảm bảo năng lực vào đội tuyển.
\end{enumerate}

\subsection{Bảng Ma Trận Ánh Xạ Chủ Đề Giữa Web App Và Handbook PDF}
\begin{center}
\small
\begin{tabularx}{\textwidth}{l p{7cm} X}
\toprule
\textbf{Module} & \textbf{Chủ đề / Kỹ năng trên Web App} & \textbf{Mục Tra Cứu Trong PDF} \\
\midrule
\textbf{Module A} & Ma trận trực giao, nghịch đảo, định thức, chuẩn vector & \S5.1 (Đại số tuyến tính nâng cao) \\
(Toán \& Xác suất) & Cực trị hàm nhiều biến, Gradient, Ma trận Hessian & \S5.2 (Tối ưu hóa \& Hessian) \\
& Đạo hàm hàm kích hoạt, Softplus, Sigmoid & \S2.2, \S5.2 (Đạo hàm phi tuyến) \\
& Định lý Bayes, Xác suất hậu nghiệm, Base-rate fallacy & \S5.1 (Định lý Bayes) \\
& Kỳ vọng, Phương sai, Quy tắc biến đổi tuyến tính & \S5.3 (Kỳ vọng \& Phương sai) \\
& MLE, MAP, Ước lượng hợp lý cực đại, Prior Gaussian & \S5.4 (MLE vs MAP) \\
& Kiểm định giả thuyết, p-value, Ý nghĩa thống kê & \S5.5 (Kiểm định giả thuyết) \\
\midrule
\textbf{Module B} & NumPy Vectorization, Broadcasting, Slicing mảng & \S1.1, \S1.9 (NumPy mảng đa chiều) \\
(Python / Tính tay) & Tính toán kích thước đầu ra Conv2D: $(W - K + 2P)/S + 1$ & \S3.1 (Công thức tầng Conv2D) \\
& Tính toán số lượng tham số lớp Conv2D & \S3.1, Câu 14 VOAI \\
& Tính toán chỉ số IoU giữa hai bounding box & \S3.6 (Object Detection IoU) \\
& Tính toán giá trị đầu ra nơ-ron: ReLU$(\mathbf{w}^T \mathbf{x} + b)$ & \S2.1, Câu 20 VOAI \\
& Tính toán Precision, Recall, F1-score từ ma trận nhầm lẫn & \S1.7, Câu 12 VOAI \\
\midrule
\textbf{Module C} & k-NN (Lazy learner, Curse of dimensionality) & \S1.1 (k-NN) \\
(ML / DL / CV / NLP) & SVM (Margin $2/\|\mathbf{w}\|$, Support vectors, RBF Kernel) & \S1.2 (SVM) \\
& Cây quyết định, Entropy $\log_2$, Information Gain & \S1.3 (Decision Tree) \\
& Random Forest (Bagging), GBDT/XGBoost/LightGBM/CatBoost & \S1.4 (Ensemble Learning) \\
& L1 (Lasso - Sparsity) vs L2 (Ridge - Co cụm) & \S1.6 (Regularization) \\
& Imbalanced Data, SMOTE, Stratified K-Fold & \S1.9, Câu 33, 35, 36 VOAI \\
& BatchNorm (Linear $\to$ Norm $\to$ ReLU) vs LayerNorm & \S2.8, Bẫy số 1 \\
& Double-Softmax Trap trong CrossEntropyLoss & \S2.4, Bẫy số 2 \\
& ResNet (Skip ADD) vs U-Net (Skip CONCAT) & \S3.4, Bẫy số 9 \\
& Vision Transformer (ViT, Patch embedding, không conv) & \S3.5 (ViT) \\
& Object Detection: NMS, YOLO Single-stage vs R-CNN & \S3.6 (Detection) \\
& NLP Pipeline, BoW, TF-IDF, Word2Vec, FastText, BERT & \S4.1 -- \S4.6 (NLP) \\
& Self-Attention Transformer: $\text{softmax}(QK^T/\sqrt{d_k})V$ & \S4.5 (Transformer) \\
& RAG (Retrieval-Augmented Generation), Hallucination & \S4.6, Câu 23 VOAI \\
\midrule
\textbf{Tự luận (C)} & Khung giải pháp 5 bước chuẩn OLP AI cho 4 bài toán thực chiến & \S7.1 -- \S7.4 (Chuyên đề thực chiến) \\
\bottomrule
\end{tabularx}
\end{center}

\subsection{Rubric Tự Chấm Điểm 4 Bài Tự Luận OLP AI (10 Điểm/Câu)}
\begin{enumerate}[leftmargin=*]
    \item \textbf{Khối 1: Phân tích bài toán \& Mục tiêu (2.0 điểm):} Xác định chuẩn xác dạng bài (Classification, Object Detection, Seq2Seq, Tabular Regression); phân tích đặc thù dữ liệu (mất cân bằng, độ phân giải, độ trễ thời gian thực) và ràng buộc tài nguyên.
    \item \textbf{Khối 2: Xử lý dữ liệu \& Validation Strategy (2.0 điểm):} Đề xuất quy trình tiền xử lý phù hợp (chuẩn hóa, tokenization, data augmentation không rò rỉ); phương pháp chia tập nghiêm ngặt (Stratified K-Fold hoặc Time-Series Split, chống Data Leakage).
    \item \textbf{Khối 3: Lựa chọn mô hình \& Kiến trúc (2.5 điểm):} Đưa ra mô hình cơ sở (Baseline) $\to$ Đề xuất kiến trúc chính (YOLO, ResNet, U-Net, BERT, LightGBM/CatBoost); giải thích rõ tại sao kiến trúc này tối ưu cho bài toán.
    \item \textbf{Khối 4: Chiến lược Huấn luyện \& Tối ưu (2.0 điểm):} Lựa chọn Loss function chuyên biệt (Focal Loss, Cross-Entropy, CTC Loss); Optimizer (AdamW + Cosine Decay Warmup); kỹ thuật kiểm soát Overfitting (Dropout, Weight Decay, Early Stopping).
    \item \textbf{Khối 5: Đánh giá, Phân tích Lỗi \& Triển khai (1.5 điểm):} Sử dụng đúng metric chuẩn (mAP@0.5:0.95, F1-macro, BLEU, PR-AUC); phương án Error Analysis; kỹ thuật nén mô hình (Quantization INT8, ONNX Runtime, TensorRT) khi triển khai thực tế.
\end{enumerate}

\vspace{1.5em}
\begin{center}
    {\small \textbf{--- HẾT CẨM NANG ÔN TẬP TOÀN DIỆN OLYMPIC AI HCMUS 2026 ---}} \\
    {\footnotesize \textit{Chúc các thí sinh ôn tập vững vàng, làm chủ bản chất toán học và đạt kết quả xuất sắc trong kỳ thi Vòng loại 11/10/2026!}}
\end{center}

\end{document}
''')

    return "\n".join(tex_parts)

def build_pdf():
    docs_dir = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26\docs"
    os.makedirs(docs_dir, exist_ok=True)
    tex_path = os.path.join(docs_dir, "olp_ai_handbook_2026.tex")
    pdf_path = os.path.join(docs_dir, "olp_ai_handbook_2026.pdf")
    public_pdf = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26\public\olp_ai_handbook_2026.pdf"
    artifact_pdf1 = r"C:\Users\HP\.gemini\antigravity-ide\brain\fd518ebc-4364-4d84-87e7-831d5592335b\olp_ai_handbook_2026.pdf"
    artifact_pdf2 = r"C:\Users\HP\.gemini\antigravity-ide\brain\5ae3ffb4-4e73-4869-b5e0-27f67608b6b1\olp_ai_handbook_2026.pdf"

    print("Dang tao noi dung TeX V2...")
    tex_content = generate_tex()
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
    print(f"Da ghi file TeX: {tex_path} ({len(tex_content)} ky tu)")

    cmd = ["xelatex", "-interaction=nonstopmode", "olp_ai_handbook_2026.tex"]
    print("Dang bien dich XeLaTeX lan 1...")
    res1 = subprocess.run(cmd, cwd=docs_dir, capture_output=True)
    print(f"Lan 1 returncode: {res1.returncode}")

    print("Dang bien dich XeLaTeX lan 2 (cap nhat Muc luc va lien ket)...")
    res2 = subprocess.run(cmd, cwd=docs_dir, capture_output=True)
    print(f"Lan 2 returncode: {res2.returncode}")

    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"XUAT THANH CONG PDF: {pdf_path} ({size_kb:.2f} KB)")
        shutil.copy2(pdf_path, public_pdf)
        if os.path.exists(os.path.dirname(artifact_pdf1)):
            shutil.copy2(pdf_path, artifact_pdf1)
        if os.path.exists(os.path.dirname(artifact_pdf2)):
            shutil.copy2(pdf_path, artifact_pdf2)
        print("Da sao chep vao public/ va cac thu muc artifact thanh cong!")
    else:
        print("Loi: Khong tim thay file PDF dau ra!")

if __name__ == "__main__":
    build_pdf()
