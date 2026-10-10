# -*- coding: utf-8 -*-
"""
Script biên soạn Tài liệu Ôn tập Toàn diện Olympic AI HCMUS 2026
Phiên bản Mở rộng Chuyên sâu: Giải thích Chi tiết Từng Tham số & Ký hiệu Toán học
Định dạng Bài báo Khoa học (Paper VBS / Academic Reference Monograph)
"""

import os
import subprocess
import shutil

TEX_CONTENT = r'''\documentclass[10pt,a4paper]{article}

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

% Cấu hình Hyperref
\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=secondaryblue,
    urlcolor=primaryblue,
    pdftitle={Tai lieu On tap Toan dien Olympic AI HCMUS 2026},
    pdfauthor={Ban Huan luyen Olympic AI}
}

% Cấu hình Header và Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\textcolor{darkslate}{\textbf{Olympic AI HCMUS 2026} --- Tài liệu Ôn thi Vòng loại Cấp trường}}
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
    arc=2.5mm,
    boxrule=0.8pt,
    left=3mm, right=3mm, top=2mm, bottom=2mm
}

\newtcolorbox{trapbox}[1]{
    colback=trapbg,
    colframe=trapborder,
    coltitle=traptit,
    fonttitle=\bfseries\small,
    title={\textbf{[BẪY THI CẦN TRÁNH]} --- #1},
    arc=2.5mm,
    boxrule=0.8pt,
    left=3mm, right=3mm, top=2mm, bottom=2mm
}

\newtcolorbox{examplebox}[1]{
    colback=exambg,
    colframe=examborder,
    coltitle=examtit,
    fonttitle=\bfseries\small,
    title={\textbf{[VÍ DỤ TÍNH TOÁN TAY]} --- #1},
    arc=2.5mm,
    boxrule=0.8pt,
    left=3mm, right=3mm, top=2mm, bottom=2mm
}

% Cấu hình Code listings
\lstset{
    backgroundcolor=\color{codebg},
    basicstyle=\ttfamily\footnotesize,
    breaklines=true,
    frame=single,
    rulecolor=\color{gray!30},
    keywordstyle=\color{primaryblue}\bfseries,
    commentstyle=\color{gray},
    stringstyle=\color{examtit},
    showstringspaces=false,
    tabsize=4
}

\setlength{\parskip}{0.4em}
\setlength{\parindent}{0pt}

\begin{document}

% ----------------- TIÊU ĐỀ BÀI BÁO / TÀI LIỆU -----------------
\begin{center}
    {\Huge \textbf{\color{primaryblue} TÀI LIỆU ÔN TẬP TOÀN DIỆN VÒNG LOẠI OLYMPIC AI 2026}} \\[0.5em]
    {\LARGE \textbf{\color{secondaryblue} Lý thuyết Cốt lõi, Đạo hàm Toán học, Chi tiết Từng Tham số \& Phân tích Thực chiến}} \\[0.8em]
    {\normalsize \textbf{Biên soạn phục vụ Kỳ thi Tuyển chọn Đội tuyển Olympic Trí tuệ Nhân tạo HCMUS (Vòng loại 11/10/2026)}} \\[0.4em]
    {\small \textit{Tham chiếu Chuẩn kiến thức: Olympic Tin học \& AI Việt Nam (VOAI), International Olympiad in AI (IOAI 2026) \& OLP AI 2025}}
\end{center}

\vspace{0.5em}
\hrule height 1.2pt
\vspace{0.8em}

\begin{abstract}
\noindent Tài liệu này được thiết kế theo cấu trúc chuyên khảo học thuật chuyên sâu chuẩn bài báo khoa học (Paper VBS / Academic Reference Monograph), nhằm cung cấp toàn bộ hệ thống lý thuyết, công thức toán học, \textbf{giải thích chi tiết từng biến số, tham số, chiều dữ liệu và trực giác cơ chế} cho thí sinh tham dự Vòng loại Olympic AI HCMUS 2026. Nội dung bao quát 5 chương trọng tâm: \textbf{Machine Learning Cổ điển}, \textbf{Deep Learning \& PyTorch Framework}, \textbf{Thị giác Máy tính (CV)}, \textbf{Xử lý Ngôn ngữ Tự nhiên (NLP)} và \textbf{Toán \& Xác suất Thống kê cho AI}. Toàn bộ các công thức toán học, bài toán tính tay kinh điển (Conv2D output dimension, Bayes base-rate fallacy, Entropy, Information Gain, IoU, F1-score, Cosine similarity) và 24 bẫy đề thi trắc nghiệm được đối chiếu minh bạch. Cuối cùng, tài liệu giải trình 4 bài toán tự luận thực chiến theo \textbf{Khung chuẩn 5 bước giải pháp AI} (Nhận diện ngôn ngữ ký hiệu video, Dịch máy thương mại điện tử Hoa--Việt, Object Detection nông nghiệp trên Mobile và Dự đoán sinh viên bỏ học với Explainable AI).
\end{abstract}

\vspace{0.5em}
\tableofcontents
\vspace{1em}
\hrule
\vspace{1em}

% =========================================================================
% CHƯƠNG 1: MACHINE LEARNING CỔ ĐIỂN
% =========================================================================
\section{Machine Learning Cổ Điển (Classical Machine Learning)}

\subsection{Thuật toán k-NN (k-Nearest Neighbors) \& Bản chất Lazy Learner}
\textbf{Định nghĩa hình thức:} k-NN là thuật toán phi tham số (non-parametric), thuộc lớp \textit{Instance-based Learning} hay \textit{Lazy Learner}. Thuật toán \textbf{không có pha huấn luyện tham số} (không tối ưu trọng số $\mathbf{w}, b$). Tại pha suy luận (Inference), với một truy vấn $\mathbf{x}_q \in \mathbb{R}^d$, mô hình tính khoảng cách từ $\mathbf{x}_q$ tới toàn bộ $N$ điểm trong tập huấn luyện $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$, xác định tập $k$ láng giềng gần nhất $\mathcal{N}_k(\mathbf{x}_q)$, và thực hiện biểu quyết:
\begin{equation}
    \hat{y} = \arg\max_{c \in \mathcal{C}} \sum_{i \in \mathcal{N}_k(\mathbf{x}_q)} \mathbb{I}(y_i = c) \quad \text{hoặc} \quad \hat{y} = \arg\max_{c \in \mathcal{C}} \sum_{i \in \mathcal{N}_k(\mathbf{x}_q)} \frac{1}{D(\mathbf{x}_q, \mathbf{x}_i) + \epsilon} \mathbb{I}(y_i = c)
\end{equation}

\textbf{Giải thích chi tiết các ký hiệu và tham số trong công thức:}
\begin{itemize}[leftmargin=*]
    \item $\mathbf{x}_q \in \mathbb{R}^d$: Điểm dữ liệu truy vấn cần dự đoán (Query vector) với $d$ đặc trưng số thực.
    \item $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$: Tập dữ liệu huấn luyện gồm $N$ mẫu đã gán nhãn.
    \item $y_i \in \mathcal{C}$: Nhãn lớp thực tế của mẫu huấn luyện thứ $i$. $\mathcal{C} = \{1, 2, \dots, C\}$ là tập hợp các lớp phân loại.
    \item $\mathcal{N}_k(\mathbf{x}_q)$: Tập hợp chỉ số của đúng $k$ điểm trong tập huấn luyện có khoảng cách $D(\mathbf{x}_q, \mathbf{x}_i)$ nhỏ nhất tới $\mathbf{x}_q$.
    \item $\mathbb{I}(\cdot)$: Hàm chỉ thị (Indicator function), nhận giá trị $1$ nếu mệnh đề bên trong đúng ($y_i = c$), và $0$ nếu sai.
    \item $D(\mathbf{x}_q, \mathbf{x}_i)$: Khoảng cách toán học giữa hai điểm dữ liệu.
    \item $\epsilon > 0$: Số thực dương cực nhỏ (ví dụ $\epsilon = 10^{-6}$) nhằm triệt tiêu nguy cơ chia cho 0 khi mẫu truy vấn trùng khít với mẫu train.
    \item $\hat{y}$: Nhãn lớp đầu ra được dự đoán cho $\mathbf{x}_q$.
\end{itemize}

\textbf{Không gian khoảng cách (Minkowski Metric $L_p$):}
\begin{equation}
    D_p(\mathbf{x}, \mathbf{z}) = \left( \sum_{j=1}^d |x_j - z_j|^p \right)^{1/p}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $x_j, z_j$: Giá trị tại chiều đặc trưng thứ $j$ của hai vector $\mathbf{x}$ và $\mathbf{z}$.
    \item $p=1$: Khoảng cách \textbf{Manhattan ($L_1$)}, tổng khoảng cách dịch chuyển dọc theo các trục tọa độ.
    \item $p=2$: Khoảng cách \textbf{Euclid ($L_2$)}, đường thẳng nối ngắn nhất trong không gian Euclid.
    \item $p \to \infty$: Khoảng cách \textbf{Chebyshev ($L_\infty$)}, lấy giá trị chênh lệch lớn nhất trên từng chiều đơn lẻ: $\max_j |x_j - z_j|$.
\end{itemize}

\begin{trapbox}{k-NN không có Training Phase \& Bắt buộc Feature Scaling}
\begin{itemize}[leftmargin=*]
    \item \textbf{Độ phức tạp tính toán:} Pha huấn luyện tốn $\mathcal{O}(1)$ thời gian (chỉ nạp dữ liệu vào RAM). Pha dự đoán tốn $\mathcal{O}(N \cdot d)$ phép toán vì phải duyệt qua toàn bộ $N$ điểm trong cơ sở dữ liệu. Do đó khi $N$ lên tới hàng triệu mẫu, k-NN cực kỳ chậm khi inference nếu không có cấu trúc chỉ mục cây không gian (KD-Tree, Ball-Tree).
    \item \textbf{Bắt buộc chuẩn hóa đặc trưng (Feature Scaling):} Nếu thuộc tính thu nhập $x_1 \in [0, 100\,000\,000]$ và độ tuổi $x_2 \in [18, 65]$, khoảng cách Euclid sẽ bị áp đảo hoàn toàn bởi $x_1$, triệt tiêu sức ảnh hưởng của $x_2$. Do đó bắt buộc phải chuẩn hóa thang đo (StandardScaler hoặc MinMaxScaler).
    \item \textbf{Ảnh hưởng của siêu tham số $k$:}
    \begin{itemize}
        \item $k=1$: Ranh giới quyết định (Voronoi tessellation) ôm chặt từng điểm nhiễu $\implies$ \textbf{Overfitting} (High Variance).
        \item $k$ lớn tiến tới $N$: Ranh giới phẳng lì, dự đoán nghiêng về lớp chiếm đa số $\implies$ \textbf{Underfitting} (High Bias).
    \end{itemize}
\end{itemize}
\end{trapbox}

\subsection{Support Vector Machines (SVM) \& Kernel Trick}
\textbf{Mô hình hình học:} Xét bài toán phân lớp nhị phân với siêu phẳng $\mathbf{w}^T \mathbf{x} + b = 0$. Khoảng cách hình học từ điểm bất kỳ đến siêu phẳng là $\gamma = \frac{|\mathbf{w}^T \mathbf{x} + b|}{\|\mathbf{w}\|_2}$. Để tối đa hóa lề hình học phân tách giữa hai lớp $\gamma_{\text{margin}} = \frac{2}{\|\mathbf{w}\|_2}$, bài toán quy về tối thiểu hóa $\|\mathbf{w}\|_2^2$.

\textbf{Bài toán Soft-Margin Primal:} Cho phép các điểm vi phạm lề thông qua biến bù $\xi_i \ge 0$:
\begin{equation}
    \min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2} \|\mathbf{w}\|_2^2 + C \sum_{i=1}^N \xi_i \quad \text{thỏa mãn} \quad y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0, \; \forall i
\end{equation}

\textbf{Giải thích chi tiết các thành phần:}
\begin{itemize}[leftmargin=*]
    \item $\mathbf{w} \in \mathbb{R}^d$: Vector trọng số pháp tuyến vuông góc với siêu phẳng phân cách. Tối thiểu hóa $\frac{1}{2}\|\mathbf{w}\|_2^2$ tương đương với tối đa hóa độ rộng lề $\frac{2}{\|\mathbf{w}\|_2}$.
    \item $b \in \mathbb{R}$: Hệ số chệch (bias / intercept), xác định độ dịch chuyển vị trí của siêu phẳng so với gốc tọa độ.
    \item $\mathbf{x}_i \in \mathbb{R}^d, y_i \in \{-1, +1\}$: Vector đặc trưng và nhãn nhị phân của mẫu huấn luyện thứ $i$.
    \item $\xi_i \ge 0$ (Slack Variable --- Biến bù vi phạm): Đo lường khoảng cách mà mẫu thứ $i$ vi phạm vùng an toàn:
    \begin{itemize}
        \item $\xi_i = 0$: Mẫu nằm hoàn toàn ngoài lề (phân loại đúng, chuẩn xác tuyệt đối).
        \item $0 < \xi_i \le 1$: Mẫu nằm lọt vào trong vùng lề an toàn nhưng vẫn ở đúng phía siêu phẳng (phân loại đúng nhưng lấn lề).
        \item $\xi_i > 1$: Mẫu nằm sai phía siêu phẳng (mô hình phân loại sai).
    \end{itemize}
    \item $C > 0$: Siêu tham số điều hòa (Regularization penalty). Kiểm soát sự đánh đổi giữa độ rộng lề và sai số:
    \begin{itemize}
        \item $C \to \infty$ (Hard-Margin): Phạt cực nặng mọi vi phạm $\implies$ lề hẹp $\implies$ Dễ \textbf{Overfitting}.
        \item $C$ nhỏ: Chấp nhận bỏ qua nhiều điểm vi phạm để mở rộng lề $\implies$ lề rộng $\implies$ Dễ \textbf{Underfitting}.
    \end{itemize}
\end{itemize}

\textbf{Dạng đối ngẫu (Dual Formulation) \& Kernel Trick:}
\begin{equation}
    \max_{\boldsymbol{\alpha}} \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j K(\mathbf{x}_i, \mathbf{x}_j) \quad \text{thỏa mãn} \quad 0 \le \alpha_i \le C, \; \sum_{i=1}^N \alpha_i y_i = 0
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $\alpha_i \ge 0$: Nhân tử Lagrange (Lagrange Multiplier) ứng với ràng buộc của mẫu thứ $i$.
    \item \textbf{Support Vectors (Vectơ hỗ trợ):} Là các mẫu có $\alpha_i > 0$. Siêu phẳng tối ưu \textbf{chỉ phụ thuộc duy nhất vào các Support Vectors này}: $\mathbf{w} = \sum_{i \in \text{SV}} \alpha_i y_i \mathbf{x}_i$. Mọi điểm có $\alpha_i = 0$ nếu bị xóa khỏi tập train thì siêu phẳng hoàn toàn không thay đổi!
    \item $K(\mathbf{x}_i, \mathbf{x}_j) = \langle \Phi(\mathbf{x}_i), \Phi(\mathbf{x}_j) \rangle$: Hàm nhân (Kernel function), cho phép tính tích vô hướng trong không gian chiếu đặc trưng nhiều chiều/vô hạn chiều mà không cần ánh xạ tường minh $\Phi$.
\end{itemize}

\textbf{Hàm nhân RBF (Radial Basis Function / Gaussian Kernel):}
\begin{equation}
    K(\mathbf{x}, \mathbf{z}) = \exp\left( -\gamma \|\mathbf{x} - \mathbf{z}\|_2^2 \right) = \exp\left( -\frac{\|\mathbf{x} - \mathbf{z}\|_2^2}{2\sigma^2} \right), \quad \gamma = \frac{1}{2\sigma^2}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $\sigma$: Độ lệch chuẩn (bán kính chuông Gaussian).
    \item $\gamma$: Tham số điều chỉnh bán kính ảnh hưởng của từng điểm dữ liệu:
    \begin{itemize}
        \item $\gamma$ rất lớn: $\sigma$ rất hẹp, mỗi điểm dữ liệu chỉ ảnh hưởng cục bộ ngay sát nó $\implies$ biên quyết định uốn lượn ôm sát từng điểm dữ liệu $\implies$ \textbf{Overfitting nghiêm trọng}.
        \item $\gamma$ nhỏ: $\sigma$ rất rộng, ảnh hưởng lan tỏa phẳng mượt $\implies$ biên quyết định thẳng đều $\implies$ \textbf{Underfitting}.
    \end{itemize}
\end{itemize}

\subsection{Cây Quyết Định (Decision Tree), Entropy \& Information Gain}
\textbf{Đo lường độ hỗn loạn (Shannon Entropy):} Cho tập dữ liệu $S$ gồm $C$ lớp với xác suất xuất hiện lớp $i$ là $p_i$:
\begin{equation}
    H(S) = -\sum_{i=1}^C p_i \log_2(p_i) \quad \text{(đơn vị: bit)}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $S$: Tập hợp dữ liệu tại nút đang xét.
    \item $C$: Tổng số lớp mục tiêu.
    \item $p_i = \frac{|S_i|}{|S|}$: Tỷ lệ (xác suất) các mẫu thuộc lớp $i$ trong tập $S$.
    \item Cơ sở $\log_2$: Đo lường lượng thông tin theo đơn vị \textbf{bit}. Nếu $p_i = 0$, quy ước $p_i \log_2(p_i) = 0$.
    \item $H(S) = 0$ khi nút thuần khiết hoàn toàn (tất cả các mẫu thuộc về đúng 1 lớp).
    \item $H(S) = \log_2(C)$ khi các lớp phân bố đều hoàn toàn (độ hỗn loạn đạt cực đại).
\end{itemize}

\textbf{Chỉ số độ tinh khiết Gini (Gini Impurity --- Dùng trong thuật toán CART):}
\begin{equation}
    \text{Gini}(S) = 1 - \sum_{i=1}^C p_i^2
\end{equation}

\textbf{Độ lợi thông tin (Information Gain --- Dùng trong thuật toán ID3):}
\begin{equation}
    IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $A$: Thuộc tính (Feature) được đưa ra để phân nhánh.
    \item $\text{Values}(A)$: Tập hợp tất cả các giá trị rời rạc có thể có của thuộc tính $A$.
    \item $S_v$: Tập con các mẫu trong $S$ có giá trị thuộc tính $A$ bằng $v$, tức $S_v = \{\mathbf{x} \in S \mid A(\mathbf{x}) = v\}$.
    \item $|S|, |S_v|$: Lực lượng (số lượng phần tử) của tập $S$ và tập con $S_v$.
    \item Thuật toán chọn phân nhánh tại thuộc tính $A$ có $IG(S, A)$ lớn nhất (làm giảm độ hỗn loạn nhiều nhất).
\end{itemize}

\begin{examplebox}{Tính toán Entropy \& Information Gain từng bước}
Cho node cha gồm 12 mẫu: 6 mẫu Đỏ ($p_1 = 0.5$) và 6 mẫu Xanh ($p_2 = 0.5$).
\begin{itemize}[leftmargin=*]
    \item Entropy node cha: $H(\text{Cha}) = -(0.5 \log_2 0.5 + 0.5 \log_2 0.5) = -(-0.5 - 0.5) = 1.0\text{ bit}$.
    \item Giả sử thuộc tính $A$ chia tập thành 2 node con:
    \begin{itemize}
        \item Nhánh trái ($S_1$, 6 mẫu): 5 Đỏ, 1 Xanh $\implies p_1 = \frac{5}{6}, p_2 = \frac{1}{6}$.
        $H(S_1) = -(\frac{5}{6}\log_2 \frac{5}{6} + \frac{1}{6}\log_2 \frac{1}{6}) \approx 0.650\text{ bit}$.
        \item Nhánh phải ($S_2$, 6 mẫu): 1 Đỏ, 5 Xanh $\implies p_1 = \frac{1}{6}, p_2 = \frac{5}{6}$.
        $H(S_2) = -(\frac{1}{6}\log_2 \frac{1}{6} + \frac{5}{6}\log_2 \frac{5}{6}) \approx 0.650\text{ bit}$.
    \end{itemize}
    \item Entropy kỳ vọng sau phân nhánh:
    $H(S, A) = \frac{6}{12} H(S_1) + \frac{6}{12} H(S_2) = 0.5(0.650) + 0.5(0.650) = 0.650\text{ bit}$.
    \item Độ lợi thông tin: $IG(S, A) = H(\text{Cha}) - H(S, A) = 1.0 - 0.650 = 0.350\text{ bit}$.
\end{itemize}
\end{examplebox}

\subsection{Random Forest \& Phương Pháp Ensemble Learning}
\begin{itemize}[leftmargin=*]
    \item \textbf{Bagging (Bootstrap Aggregating):} Rút mẫu ngẫu nhiên \textbf{có hoàn lại} (Bootstrap) từ $N$ mẫu ban đầu để tạo ra $B$ tập huấn luyện khác nhau cho $B$ cây con.
    \item \textbf{Bản chất toán học của Out-of-Bag (OOB):} Xác suất một mẫu bất kỳ KHÔNG được rút trúng trong 1 lần chọn là $1 - \frac{1}{N}$. Khi rút $N$ lần độc lập, xác suất mẫu đó hoàn toàn không rơi vào tập train của một cây là:
    \begin{equation}
        \lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = e^{-1} \approx 0.3679 \approx 36.8\%
    \end{equation}
    $\implies$ Trung bình $36.8\%$ dữ liệu không được huấn luyện trên cây con đó (gọi là mẫu OOB), dùng làm tập kiểm thử nội bộ tự nhiên để tính \textbf{OOB Error} mà không cần tốn riêng tập validation.
    \item \textbf{Feature Randomness:} Tại mỗi node của cây quyết định, chỉ chọn ngẫu nhiên $m$ thuộc tính trong tổng số $d$ thuộc tính để tìm điểm cắt tối ưu ($m = \lfloor \sqrt{d} \rfloor$ cho bài toán phân loại; $m = \lfloor d/3 \rfloor$ cho hồi quy). Điều này làm triệt tiêu sự tương quan giữa các cây, giúp giảm mạnh \textbf{Variance}.
\end{itemize}

\subsection{Bias-Variance Tradeoff \& Kỹ thuật Cross-Validation}
\textbf{Phân rã sai số kỳ vọng (Expected Prediction Error):}
\begin{equation}
    \mathbb{E}[(y - \hat{f}(x))^2] = \underbrace{\left( f(x) - \mathbb{E}[\hat{f}(x)] \right)^2}_{\text{Bias}^2 \text{ (Độ chệch)}} + \underbrace{\mathbb{E}\left[ (\hat{f}(x) - \mathbb{E}[\hat{f}(x)])^2 \right]}_{\text{Variance (Phương sai)}} + \underbrace{\sigma_\epsilon^2}_{\text{Nhiễu không thể khử}}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $f(x)$: Hàm chân lý thực tế sinh dữ liệu: $y = f(x) + \epsilon$.
    \item $\hat{f}(x)$: Hàm dự đoán do mô hình học được trên một tập dữ liệu ngẫu nhiên.
    \item $\mathbb{E}[\hat{f}(x)]$: Giá trị dự đoán trung bình của mô hình khi huấn luyện qua vô số tập dữ liệu độc lập.
    \item $\text{Bias}^2$: Đo lường sai khác giữa kỳ vọng của mô hình và chân lý khách quan. Bias cao $\implies$ mô hình quá cứng nhắc, bỏ sót quy luật $\implies$ \textbf{Underfitting}.
    \item $\text{Variance}$: Đo lường độ biến động của dự đoán mô hình khi tập huấn luyện thay đổi. Variance cao $\implies$ mô hình quá nhạy cảm với từng điểm dữ liệu ngẫu nhiên $\implies$ \textbf{Overfitting}.
    \item $\sigma_\epsilon^2$: Nhiễu ngẫu nhiên thực tế (Irreducible Error) không thể triệt tiêu.
    \item \textbf{Stratified K-Fold:} Bắt buộc sử dụng cho bài toán lệch lớp (Imbalanced Data) để đảm bảo tỉ lệ phân bố giữa các nhãn ở mỗi Fold giống hệt phân phối trên toàn bộ tập dữ liệu gốc.
\end{itemize}

\subsection{Regularization: L2 (Ridge) vs L1 (Lasso) vs ElasticNet}
\begin{align}
    \text{Ridge } (L_2): \quad \mathcal{L}_{\text{Ridge}}(\mathbf{w}) &= \mathcal{L}_0(\mathbf{w}) + \frac{\lambda}{2} \|\mathbf{w}\|_2^2 = \mathcal{L}_0(\mathbf{w}) + \frac{\lambda}{2} \sum_{j=1}^d w_j^2 \\
    \text{Lasso } (L_1): \quad \mathcal{L}_{\text{Lasso}}(\mathbf{w}) &= \mathcal{L}_0(\mathbf{w}) + \lambda \|\mathbf{w}\|_1 = \mathcal{L}_0(\mathbf{w}) + \lambda \sum_{j=1}^d |w_j| \\
    \text{ElasticNet}: \quad \mathcal{L}_{\text{EN}}(\mathbf{w}) &= \mathcal{L}_0(\mathbf{w}) + r \lambda \|\mathbf{w}\|_1 + \frac{1-r}{2} \lambda \|\mathbf{w}\|_2^2
\end{align}
\textbf{Giải thích chi tiết các thành phần:}
\begin{itemize}[leftmargin=*]
    \item $\mathcal{L}_0(\mathbf{w})$: Hàm mất mát nguyên bản trên tập dữ liệu huấn luyện (MSE trong hồi quy tuyến tính hoặc Cross-Entropy trong Logistic Regression).
    \item $\mathbf{w} = [w_1, w_2, \dots, w_d]^T \in \mathbb{R}^d$: Vector trọng số của mô hình.
    \item $\lambda > 0$: Hệ số điều hòa (Regularization Strength). $\lambda$ càng lớn, hàm phạt càng ép các trọng số phải co nhỏ lại để chống Overfitting.
    \item $r \in [0, 1]$: Tỷ lệ hòa trộn giữa chuẩn L1 và L2 trong ElasticNet.
    \item \textbf{Cơ chế hình học của Lasso ($L_1$):} Vùng ràng buộc của chuẩn $L_1$ là một hình khối đa diện (Polyhedron) có các góc nhọn nằm chính xác trên các trục tọa độ. Khi đường mức của hàm mất mát tiếp xúc với khối đa diện, điểm tiếp xúc tối ưu có xác suất cực cao rơi đúng vào các đỉnh góc nhọn này. Tại đó, một loạt các tọa độ $w_j = 0$ chính xác tuyệt đối $\implies$ \textbf{Lasso thực hiện Lựa chọn đặc trưng tự động (Feature Selection), tạo tính thưa (Sparsity)}.
    \item \textbf{Cơ chế hình học của Ridge ($L_2$):} Vùng ràng buộc là hình cầu trơn nhẵn, ép các trọng số co nhỏ dần về tiệm cận 0 nhưng \textbf{không bao giờ triệt tiêu hoàn toàn bằng 0}. Công thức nghiệm đóng của Ridge: $\mathbf{w}_{\text{Ridge}} = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$, số hạng $\lambda \mathbf{I}$ đảm bảo ma trận luôn khả nghịch ngay cả khi các cột bị đa cộng tuyến (Multicollinearity).
\end{itemize}

\subsection{Các Độ Đo Đánh Giá Phân Lớp (Classification Metrics)}
\textbf{Bảng Ma trận nhầm lẫn (Confusion Matrix):}
\begin{itemize}[leftmargin=*]
    \item $TP$ (True Positive): Mẫu thực tế Dương, mô hình đoán Dương (Đúng).
    \item $FP$ (False Positive): Mẫu thực tế Âm, mô hình đoán Dương (Báo động giả / Sai lầm Loại I).
    \item $FN$ (False Negative): Mẫu thực tế Dương, mô hình đoán Âm (Bỏ sót tội phạm / Sai lầm Loại II).
    \item $TN$ (True Negative): Mẫu thực tế Âm, mô hình đoán Âm (Đúng).
\end{itemize}

\textbf{Công thức các chỉ số cơ bản:}
\begin{equation}
    \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}, \quad \text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}
\end{equation}
\begin{equation}
    F_1\text{-score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 TP}{2 TP + FP + FN}
\end{equation}
\begin{equation}
    F_\beta\text{-score} = (1 + \beta^2) \cdot \frac{\text{Precision} \cdot \text{Recall}}{\beta^2 \cdot \text{Precision} + \text{Recall}}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $\beta = 1$: $F_1$-score coi trọng Precision và Recall ngang nhau.
    \item $\beta = 2$: $F_2$-score coi trọng \textbf{Recall gấp đôi Precision} (ưu tiên tối đa việc không bỏ sót mẫu dương: phát hiện bệnh hiểm nghèo, an ninh).
    \item $\beta = 0.5$: $F_{0.5}$-score coi trọng \textbf{Precision gấp đôi Recall} (ưu tiên độ chuẩn xác khi đưa ra quyết định: lọc spam mail, cấp tín dụng).
\end{itemize}

\textbf{Chiến lược tổng hợp F1 trong bài toán đa lớp ($C$ lớp):}
\begin{itemize}[leftmargin=*]
    \item \textbf{Macro F1:} $\text{Macro-F1} = \frac{1}{C} \sum_{c=1}^C F_{1, c}$. Tính trung bình không trọng số của F1 từng lớp. Coi mọi lớp có vai trò ngang nhau $\implies$ \textbf{Rất nhạy cảm với lớp thiểu số}.
    \item \textbf{Micro F1:} Tính tổng toàn cục $\sum TP, \sum FP, \sum FN$ rồi áp dụng công thức F1. Bằng chính xác Accuracy trên bài toán phân loại đơn nhãn.
    \item \textbf{Weighted F1:} Tính trung bình có trọng số theo số lượng mẫu thực tế của từng lớp: $\sum_{c=1}^C \frac{N_c}{N} F_{1, c}$.
    \item \textbf{Đường cong PR (Precision-Recall Curve):} Khi dữ liệu bị mất cân bằng trầm trọng (ví dụ gian lận thẻ tín dụng $0.1\%$), đường cong ROC-AUC sẽ bị lạc quan giả tạo do $TN$ quá lớn. Bắt buộc phải dùng \textbf{PR-AUC} để đánh giá chính xác năng lực mô hình.
\end{itemize}

\subsection{K-Means Clustering \& Silhouette Analysis}
\textbf{Hàm mục tiêu Inertia (Within-Cluster Sum of Squares):}
\begin{equation}
    J = \sum_{k=1}^K \sum_{\mathbf{x}_i \in \mathcal{C}_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|_2^2
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $K$: Số lượng cụm cần phân chia.
    \item $\mathcal{C}_k$: Tập hợp các điểm dữ liệu được gán vào cụm thứ $k$.
    \item $\boldsymbol{\mu}_k = \frac{1}{|\mathcal{C}_k|} \sum_{\mathbf{x} \in \mathcal{C}_k} \mathbf{x}$: Tọa độ trọng tâm (Centroid) của cụm thứ $k$.
    \item \textbf{Thuật toán K-Means++:} Khởi tạo trọng tâm đầu tiên ngẫu nhiên; các trọng tâm tiếp theo được chọn với xác suất tỷ lệ thuận với bình phương khoảng cách tới trọng tâm gần nhất đã chọn ($P(x) \propto D(x)^2$). Giúp tránh tối tiểu cục bộ tồi tệ.
\end{itemize}

\textbf{Hệ số Silhouette đánh giá độ gắn kết của cụm:}
\begin{equation}
    s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} \in [-1, 1]
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $a(i)$: Khoảng cách trung bình từ điểm $i$ tới tất cả các điểm khác trong cùng cụm (độ kết tụ nội cụm, muốn càng nhỏ càng tốt).
    \item $b(i)$: Khoảng cách trung bình từ điểm $i$ tới tất cả các điểm trong cụm láng giềng gần nhất tiếp theo (độ phân tách liên cụm, muốn càng lớn càng tốt).
    \item $s(i) \to +1$: Điểm nằm sâu trong cụm phù hợp; $s(i) \approx 0$: Điểm nằm ngay ranh giới giữa 2 cụm; $s(i) < 0$: Điểm đã bị gán sai cụm.
\end{itemize}

\subsection{Kỹ thuật Xử lý Mất Cân Bằng Lớp (Imbalanced Data)}
\begin{enumerate}[leftmargin=*]
    \item \textbf{SMOTE (Synthetic Minority Over-sampling Technique):} Không sao chép trùng lặp, mà \textbf{nội suy sinh mẫu mới} trên đoạn thẳng nối mẫu thiểu số $\mathbf{x}_i$ với 1 láng giềng gần nhất $\mathbf{x}_{zi}$ cùng lớp:
    \begin{equation}
        \mathbf{x}_{\text{new}} = \mathbf{x}_i + \lambda (\mathbf{x}_{zi} - \mathbf{x}_i), \quad \lambda \sim U(0, 1)
    \end{equation}
    \item \textbf{Class Weighting / Cost-Sensitive Learning:} Nhân trọng số phạt lớn hơn vào hàm mất mát khi mô hình đoán sai mẫu thiểu số: $w_c = \frac{N}{C \cdot N_c}$.
    \item \textbf{Focal Loss:} Giảm thiểu hàm phạt trên các mẫu dễ phân loại, dồn toàn bộ sự chú ý của gradient vào các mẫu thiểu số khó.
\end{enumerate}

% =========================================================================
% CHƯƠNG 2: DEEP LEARNING & PYTORCH FRAMEWORK
% =========================================================================
\section{Deep Learning Cơ Bản \& PyTorch Framework}

\subsection{Perceptron, MLP \& Định Lý Xấp Xỉ Phổ Quát}
Mạng Perceptron Đa tầng (Multi-Layer Perceptron --- MLP) ánh xạ đầu vào $\mathbf{x} \in \mathbb{R}^d$ qua các tầng ẩn:
\begin{equation}
    \mathbf{h}^{(1)} = \sigma(\mathbf{W}_1 \mathbf{x} + \mathbf{b}_1), \quad \mathbf{h}^{(2)} = \sigma(\mathbf{W}_2 \mathbf{h}^{(1)} + \mathbf{b}_2), \quad \dots, \quad \hat{\mathbf{y}} = g(\mathbf{W}_L \mathbf{h}^{(L-1)} + \mathbf{b}_L)
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $\mathbf{W}_l$: Ma trận trọng số tại tầng $l$.
    \item $\mathbf{b}_l$: Vector độ lệch bias tại tầng $l$.
    \item $\sigma(\cdot)$: Hàm kích hoạt phi tuyến (Non-linear Activation Function).
    \item \textbf{Định lý Xấp xỉ Phổ quát (Cybenko, 1989):} Một mạng nơ-ron chỉ cần duy nhất 1 tầng ẩn với số lượng neuron hữu hạn và hàm kích hoạt phi tuyến liên tục có khả năng xấp xỉ bất kỳ hàm liên tục nào trên không gian compact với độ chính xác tùy ý. Tuy nhiên, việc tăng chiều sâu mạng (Deep Architecture) giúp giảm số lượng neuron theo cấp số mũ so với mạng chỉ mở rộng chiều ngang (Wide Architecture).
    \item \textbf{Nếu không có hàm kích hoạt phi tuyến:} Mạng sâu $L$ tầng sẽ thu gọn thành một phép biến đổi tuyến tính đơn lẻ: $\mathbf{y} = \mathbf{W}_L \dots \mathbf{W}_1 \mathbf{x} = \mathbf{W}_{\text{eff}} \mathbf{x} + \mathbf{b}_{\text{eff}}$, mất hoàn toàn khả năng giải quyết các bài toán phi tuyến (như cổng XOR).
\end{itemize}

\subsection{Phân Tích Chi Tiết Các Hàm Kích Hoạt (Activation Functions)}
\begin{itemize}[leftmargin=*]
    \item \textbf{Sigmoid:} $\sigma(z) = \frac{1}{1 + e^{-z}}$. Đạo hàm: $\sigma'(z) = \sigma(z)(1 - \sigma(z))$.
    \begin{itemize}
        \item Đạo hàm cực đại chỉ bằng $0.25$ tại $z=0$, tiệm cận $0$ khi $|z|$ lớn.
        \item \textbf{Nhược điểm:} Gây triệt tiêu gradient nghiêm trọng (Vanishing Gradient) trong mạng nhiều tầng; đầu ra không đối xứng quanh 0 (Not zero-centered), làm cập nhật gradient bị zig-zag.
    \end{itemize}
    \item \textbf{Tanh (Hyperbolic Tangent):} $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$. Đạo hàm: $\tanh'(z) = 1 - \tanh^2(z) \le 1$.
    \begin{itemize}
        \item Miền giá trị $(-1, 1)$, đối xứng quanh 0 (Zero-centered). Hội tụ nhanh hơn Sigmoid nhưng vẫn bị hiện tượng bão hòa ở hai đầu biên.
    \end{itemize}
    \item \textbf{ReLU (Rectified Linear Unit):} $f(z) = \max(0, z)$. Đạo hàm: $f'(z) = 1$ khi $z > 0$; $f'(z) = 0$ khi $z \le 0$.
    \begin{itemize}
        \item Tốc độ tính toán siêu nhanh, gradient bằng đúng 1 ở miền dương giúp giảm thiểu triệt tiêu gradient.
        \item \textbf{Nhược điểm: Dying ReLU}. Nếu một neuron nhận trọng số khiến $z \le 0$ trên toàn bộ tập dữ liệu, gradient của nó vĩnh viễn bằng 0 và neuron đó "chết" hoàn toàn, không thể cập nhật tiếp.
    \end{itemize}
    \item \textbf{Leaky ReLU:} $f(z) = \max(\alpha z, z)$ với $\alpha \approx 0.01$. Khắc phục hiện tượng Dying ReLU nhờ duy trì một độ dốc nhỏ $\alpha$ ở vùng âm.
    \item \textbf{GELU (Gaussian Error Linear Unit):} $f(z) = z \Phi(z) = z \cdot P(X \le z)$ với $X \sim \mathcal{N}(0, 1)$. Kích hoạt mượt mà phi tuyến, là chuẩn mực trong các mô hình Transformer hiện đại (BERT, GPT-3, ViT).
\end{itemize}

\subsection{Quy Trình Huấn Luyện Chuẩn PyTorch (Training Loop)}
\begin{lstlisting}[language=Python]
model.train() # 1. Bat che do train (bat Dropout, BatchNorm cap nhat running stats)
for inputs, targets in dataloader:
    optimizer.zero_grad()       # 2. XOA GRADIENT CU (mac dinh PyTorch cong don)
    outputs = model(inputs)     # 3. Forward pass (tinh du doan)
    loss = criterion(outputs, targets) # 4. Tinh gia tri ham mat mat Loss
    loss.backward()             # 5. Backward pass (tinh dao ham rieng luu vao param.grad)
    optimizer.step()            # 6. Cap nhat trong so theo thuat toan toi uu
\end{lstlisting}

\begin{trapbox}{Tại sao bắt buộc phải gọi optimizer.zero\_grad() trước loss.backward()?}
Trong PyTorch, nhằm tối ưu bộ nhớ và phục vụ kỹ thuật \textbf{Tích lũy Gradient (Gradient Accumulation)} khi GPU có VRAM nhỏ, hàm \texttt{backward()} mặc định thực hiện phép toán cộng dồn:
\begin{equation*}
    \texttt{param.grad} \leftarrow \texttt{param.grad} + \frac{\partial \mathcal{L}_{\text{batch}}}{\partial \mathbf{w}}
\end{equation*}
Nếu không gọi \texttt{optimizer.zero\_grad()}, gradient của batch hiện tại sẽ bị cộng dồn chồng chất với toàn bộ các batch trước đó, dẫn đến bước cập nhật trọng số khổng lồ, làm bùng nổ gradient và phá hủy toàn bộ quá trình hội tụ của mô hình!
\end{trapbox}

\subsection{Các Hàm Mất Mát (Loss Functions) \& Bẫy Double-Softmax}
\begin{itemize}[leftmargin=*]
    \item \textbf{Binary Cross-Entropy (BCE):} $\mathcal{L} = -\frac{1}{N}\sum [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]$, nhận đầu vào là xác suất $\hat{y}_i \in (0, 1)$.
    \item \textbf{\texttt{nn.BCEWithLogitsLoss}:} Tích hợp Sigmoid và BCE bằng kỹ thuật toán học Log-Sum-Exp ổn định số:
    \begin{equation}
        \mathcal{L}(z, y) = \max(z, 0) - z y + \log(1 + e^{-|z|})
    \end{equation}
    $\implies$ \textbf{Nhận đầu vào là Logit thô $z$ (chưa qua Sigmoid)}, triệt tiêu hoàn toàn nguy cơ tràn số (numerical overflow/underflow).
    \item \textbf{\texttt{nn.CrossEntropyLoss} (Đa lớp):} Tích hợp gộp \texttt{nn.LogSoftmax()} và \texttt{nn.NLLLoss()}:
    \begin{equation}
        \mathcal{L}_{\text{CE}}(\mathbf{z}, y) = -\log\left( \frac{e^{z_y}}{\sum_{j=1}^C e^{z_j}} \right) = -z_y + \log\left( \sum_{j=1}^C e^{z_j} \right)
    \end{equation}
    \begin{itemize}[leftmargin=*]
        \item $\mathbf{z} = (z_1, z_2, \dots, z_C) \in \mathbb{R}^C$: Vector Logit thô đầu ra từ tầng Linear cuối cùng.
        \item $y \in \{1, 2, \dots, C\}$: Nhãn số nguyên của lớp ground-truth thực tế.
        \item $z_y$: Giá trị logit tại vị trí lớp đúng $y$.
        \item $\implies$ \textbf{Nhận đầu vào là Logit thô $\mathbf{z}$ (CHƯA qua Softmax)}.
    \end{itemize}
    \item \textbf{Focal Loss (Lin et al., 2017):} Xử lý mất cân bằng lớp cực đoan:
    \begin{equation}
        \text{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)
    \end{equation}
    Trong đó $p_t$ là xác suất dự đoán cho lớp đúng, $\gamma \ge 0$ là siêu tham số focusing. Khi mẫu dễ phân loại ($p_t \approx 0.9$), thừa số $(1 - p_t)^\gamma = (0.1)^2 = 0.01$, làm triệt tiêu $99\%$ trọng số mất mát của mẫu dễ, ép gradient tập trung vào các mẫu khó.
\end{itemize}

\begin{trapbox}{Lỗi Double-Softmax trong PyTorch}
Nếu tầng cuối của mạng nơ-ron khai báo \texttt{nn.Softmax()} hoặc gọi \texttt{torch.softmax(out, dim=-1)} trước khi truyền vào \texttt{nn.CrossEntropyLoss()}, mô hình sẽ bị áp dụng hàm Softmax 2 lần liên tiếp. Khi đó xác suất đầu vào bị nén phẳng, gradient tính ra bị sai lệch trầm trọng và làm mô hình không thể hội tụ.
\end{trapbox}

\subsection{Thuật Toán Tối Ưu Hóa: SGD, Momentum, RMSProp \& Adam}
\textbf{Adam (Adaptive Moment Estimation):} Khởi tạo $\mathbf{m}_0 = \mathbf{0}, \mathbf{v}_0 = \mathbf{0}, t = 0$. Tại bước lặp thứ $t$:
\begin{align}
    \mathbf{g}_t &= \nabla_\mathbf{w} \mathcal{L}(\mathbf{w}_t) \\
    \mathbf{m}_t &= \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \mathbf{g}_t \quad \text{(Moment bậc 1 --- Hướng di chuyển trung bình có quán tính)} \\
    \mathbf{v}_t &= \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) \mathbf{g}_t^2 \quad \text{(Moment bậc 2 --- Độ biến động bình phương trung bình)} \\
    \hat{\mathbf{m}}_t &= \frac{\mathbf{m}_t}{1 - \beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t} \quad \text{(Hiệu chỉnh độ chệch khởi tạo --- Bias Correction)} \\
    \mathbf{w}_{t+1} &= \mathbf{w}_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \odot \hat{\mathbf{m}}_t \quad \text{(Cập nhật vector trọng số mô hình)}
\end{align}

\textbf{Giải thích chi tiết từng biến số và tham số trong thuật toán Adam:}
\begin{itemize}[leftmargin=*]
    \item $t \in \{1, 2, 3, \dots\}$: Chỉ số bước lặp tối ưu hóa (Iteration / Step counter).
    \item $\mathbf{w}_t \in \mathbb{R}^P$: Vector toàn bộ $P$ tham số trọng số của mô hình tại bước $t$.
    \item $\mathcal{L}(\mathbf{w}_t)$: Giá trị hàm mất mát tính trên batch dữ liệu hiện tại.
    \item $\mathbf{g}_t \in \mathbb{R}^P$: Vector Gradient bậc 1 của hàm mất mát theo trọng số: $\mathbf{g}_t = \left[ \frac{\partial \mathcal{L}}{\partial w_1}, \dots, \frac{\partial \mathcal{L}}{\partial w_P} \right]^T$.
    \item $\mathbf{m}_t \in \mathbb{R}^P$: Vector Moment bậc 1 (Trung bình trượt hàm mũ của gradient). Đóng vai trò như vận tốc quán tính trong vật lý, giúp vượt qua các điểm yên ngựa (Saddle Points) và cực tiểu địa phương nông.
    \item $\mathbf{v}_t \in \mathbb{R}^P$: Vector Moment bậc 2 (Trung bình trượt hàm mũ của bình phương gradient). Đo lường mức độ dao động mạnh hay yếu của gradient theo từng chiều tọa độ. Phép toán $\mathbf{g}_t^2$ là bình phương từng phần tử.
    \item $\beta_1 \in [0, 1)$: Hệ số suy giảm của moment bậc 1. Giá trị chuẩn mực công nghiệp: $\beta_1 = 0.9$.
    \item $\beta_2 \in [0, 1)$: Hệ số suy giảm của moment bậc 2. Giá trị chuẩn mực công nghiệp: $\beta_2 = 0.999$.
    \item $\beta_1^t, \beta_2^t$: Lũy thừa bậc $t$ của $\beta_1$ và $\beta_2$.
    \item $\hat{\mathbf{m}}_t, \hat{\mathbf{v}}_t$: Các moment đã được \textbf{Hiệu chỉnh độ chệch (Bias Correction)}. Do ban đầu $\mathbf{m}_0 = \mathbf{0}, \mathbf{v}_0 = \mathbf{0}$, trong những bước đầu tiên $\mathbf{m}_t$ và $\mathbf{v}_t$ bị co cụm thiên vị về gần 0. Chia cho $(1 - \beta^t)$ đưa kỳ vọng không chệch trở về đúng giá trị thực: $\mathbb{E}[\hat{\mathbf{m}}_t] = \mathbb{E}[\mathbf{g}_t]$. Khi $t \to \infty$, $1 - \beta^t \to 1$, hiệu chỉnh này tự động mờ dần.
    \item $\eta$: Tốc độ học (Learning Rate), thường đặt từ $10^{-4}$ đến $10^{-3}$.
    \item $\epsilon$: Hằng số làm mịn dương cực nhỏ (thường chọn $10^{-8}$) nằm ở mẫu số để triệt tiêu lỗi chia cho 0 khi độ biến động $\hat{\mathbf{v}}_t$ quá nhỏ.
    \item $\odot$: Phép nhân Hadamard (Element-wise multiplication --- nhân từng phần tử tương ứng).
\end{itemize}

\subsection{Khởi Tạo Trọng Số (Weight Initialization)}
\begin{itemize}[leftmargin=*]
    \item \textbf{Khởi tạo Zeros (Tất cả bằng 0):} \textbf{HOÀN TOÀN SAI}. Mọi neuron trong cùng một lớp nhận tín hiệu giống nhau và có gradient y hệt nhau $\implies$ không phá vỡ tính đối xứng (Symmetry Problem), khiến mạng sâu bị thoái hóa về 1 neuron đơn lẻ.
    \item \textbf{Xavier / Glorot Initialization (Glorot \& Bengio, 2010):}
    \begin{equation}
        \text{Var}(W) = \frac{2}{n_{\text{in}} + n_{\text{out}}} \quad \implies \text{Bắt buộc dùng cho Tanh và Sigmoid}
    \end{equation}
    $n_{\text{in}}$ là số lượng kết nối vào (fan-in), $n_{\text{out}}$ là số lượng kết nối ra (fan-out). Giữ cho phương sai tín hiệu không bị bùng nổ hay triệt tiêu qua các hàm kích hoạt đối xứng quanh 0.
    \item \textbf{He / Kaiming Initialization (He et al., 2015):}
    \begin{equation}
        \text{Var}(W) = \frac{2}{n_{\text{in}}} \quad \implies \text{Bắt buộc dùng cho ReLU và Leaky ReLU}
    \end{equation}
    Do ReLU triệt tiêu một nửa tín hiệu âm ($z \le 0$), phương sai của trọng số cần phải tăng gấp đôi lên $\frac{2}{n_{\text{in}}}$ để bù đắp phần năng lượng tín hiệu bị mất.
\end{itemize}

\subsection{Batch Normalization vs Layer Normalization}
\textbf{Batch Normalization (Ioffe \& Szegedy, 2015):} Chuẩn hóa trên mini-batch $\mathcal{B} = \{x_1, \dots, x_m\}$:
\begin{equation}
    \mu_B = \frac{1}{m} \sum_{i=1}^m x_i, \quad \sigma_B^2 = \frac{1}{m} \sum_{i=1}^m (x_i - \mu_B)^2, \quad \hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}, \quad y_i = \gamma \hat{x}_i + \beta
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $m$: Kích thước mini-batch (batch size).
    \item $\mu_B, \sigma_B^2$: Giá trị trung bình và phương sai tính toán trên mini-batch hiện tại.
    \item $\epsilon > 0$: Hằng số chống chia cho 0 (thường là $10^{-5}$).
    \item $\gamma$ (Scale) và $\beta$ (Shift): \textbf{Hai tham số học được (Learnable parameters)} được tối ưu qua backpropagation. Giúp mạng có năng lực khôi phục lại phân phối gốc nếu việc ép về chuẩn hóa làm suy giảm năng lực biểu diễn phi tuyến.
    \item Thứ tự chuẩn trong kiến trúc mạng: \textbf{Linear / Conv $\to$ BatchNorm $\to$ ReLU}.
    \item Trong pha kiểm thử (Inference): Sử dụng giá trị trung bình tích lũy \texttt{running\_mean} và phương sai \texttt{running\_var} tính bằng trung bình trượt trong quá trình train.
    \item \textbf{Layer Normalization (Ba et al., 2016):} Chuẩn hóa độc lập trên từng mẫu riêng lẻ dọc theo chiều đặc trưng (Features). Không phụ thuộc batch size $\implies$ \textbf{Chuẩn mực bắt buộc cho Transformer, RNN và dữ liệu chuỗi NLP}.
\end{itemize}

\subsection{Cơ Chế Inverted Dropout}
Trong pha Train, ngẫu nhiên ngắt neuron với xác suất ngắt $p$, đồng thời nhân hệ số phóng đại $\frac{1}{1-p}$:
\begin{equation}
    \mathbf{h}_{\text{train}} = \frac{1}{1 - p} (\mathbf{h} \odot \mathbf{m}), \quad \mathbf{m} \sim \text{Bernoulli}(1 - p)
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $\mathbf{h} \in \mathbb{R}^d$: Vector kích hoạt đầu ra của một tầng.
    \item $p \in [0, 1)$: Xác suất neuron bị loại bỏ (Drop probability, thường đặt $0.5$ cho FC layer và $0.1$ cho Attention).
    \item $\mathbf{m} \in \{0, 1\}^d$: Mặt nạ nhị phân ngẫu nhiên (Binary mask) tuân theo phân phối Bernoulli với xác suất giữ lại là $1 - p$.
    \item Thừa số $\frac{1}{1-p}$: Đảm bảo kỳ vọng toán học của tín hiệu không thay đổi: $\mathbb{E}[\mathbf{h}_{\text{train}}] = \mathbf{h}$. Nhờ vậy, trong pha Test/Inference, ta chỉ cần tắt Dropout (\texttt{model.eval()}) và chuyển thẳng $\mathbf{h}_{\text{test}} = \mathbf{h}$ mà không cần nhân lại trọng số.
\end{itemize}

% =========================================================================
% CHƯƠNG 3: THỊ GIÁC MÁY TÍNH (COMPUTER VISION)
% =========================================================================
\section{Thị Giác Máy Tính (Computer Vision)}

\subsection{Công Thức Kích Thước Không Gian Tầng Conv2D}
\begin{equation}
    O = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1
\end{equation}
\textbf{Giải thích chi tiết các ký hiệu:}
\begin{itemize}[leftmargin=*]
    \item $W$: Kích thước chiều không gian đầu vào (Chiều rộng $W$ hoặc Chiều cao $H$).
    \item $K$: Kích thước cạnh của bộ lọc tích chập (Kernel / Filter size, ví dụ kernel $3 \times 3 \implies K = 3$).
    \item $P$: Độ dày viền chèn thêm xung quanh ma trận (Padding).
    \item $S$: Bước nhảy trượt của kernel qua mỗi lần tính tích chập (Stride).
    \item $O$: Kích thước chiều không gian đầu ra (Output feature map dimension).
    \item $\lfloor \cdot \rfloor$: Phép lấy phần nguyên sàn (Floor).
\end{itemize}

\textbf{Các chế độ Padding phổ biến:}
\begin{itemize}[leftmargin=*]
    \item \textbf{Valid Padding ($P = 0$):} Không thêm viền $\implies O = \lfloor \frac{W - K}{S} \rfloor + 1$. Kích thước luôn bị thu nhỏ sau phép tích chập.
    \item \textbf{Same Padding ($S = 1$):} Chọn $P = \frac{K - 1}{2}$ (khi $K$ lẻ) để kích thước đầu ra giữ nguyên bằng đầu vào: $O = W$.
\end{itemize}

\textbf{Công thức tính Tổng số lượng tham số học được (Learnable Parameters):}
\begin{equation}
    \text{Params} = (K_H \times K_W \times C_{\text{in}} + 1) \times C_{\text{out}}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $K_H, K_W$: Chiều cao và chiều rộng của nhân kernel (ví dụ $3 \times 3$).
    \item $C_{\text{in}}$: Số kênh của ảnh hoặc feature map đầu vào (ví dụ ảnh RGB thì $C_{\text{in}} = 3$).
    \item $+1$: Tham số Bias tương ứng cho mỗi bộ lọc (Filter).
    \item $C_{\text{out}}$: Số lượng bộ lọc kernel, đồng thời là số kênh của feature map đầu ra.
\end{itemize}

\begin{examplebox}{Tính toán kích thước Conv2D thường gặp trong đề thi}
\begin{enumerate}[leftmargin=*]
    \item Ảnh $32 \times 32$, kernel $3 \times 3$, stride 1, padding 1:
    $O = \lfloor \frac{32 - 3 + 2(1)}{1} \rfloor + 1 = 31 + 1 = 32 \implies 32 \times 32$.
    \item Ảnh $28 \times 28$, kernel $5 \times 5$, stride 1, không padding ($P=0$):
    $O = \lfloor \frac{28 - 5 + 0}{1} \rfloor + 1 = 23 + 1 = 24 \implies 24 \times 24$.
    \item Ảnh $224 \times 224$, kernel $7 \times 7$, stride 2, padding 3:
    $O = \lfloor \frac{224 - 7 + 2(3)}{2} \rfloor + 1 = \lfloor \frac{223}{2} \rfloor + 1 = 111 + 1 = 112 \implies 112 \times 112$.
    \item Tính số tham số: Lớp Conv2D nhận đầu vào 64 kênh, xuất ra 128 kênh, kernel $3 \times 3$:
    $\text{Params} = (3 \times 3 \times 64 + 1) \times 128 = (576 + 1) \times 128 = 577 \times 128 = 73\,856\text{ tham số}$.
\end{enumerate}
\end{examplebox}

\subsection{Pooling, Global Average Pooling (GAP) \& Receptive Field}
\begin{itemize}[leftmargin=*]
    \item \textbf{Pooling:} Max Pooling giữ đặc trưng kích hoạt mạnh nhất; Average Pooling làm mượt. \textbf{Lớp Pooling hoàn toàn không chứa tham số học được (0 learnable parameters)}.
    \item \textbf{Global Average Pooling (GAP):} Ép toàn bộ không gian $H \times W$ của mỗi channel thành 1 giá trị vô hướng duy nhất ($H \times W \times C \to 1 \times 1 \times C$). Thay thế hoàn toàn lớp Fully Connected cồng kềnh, giảm hàng triệu tham số và chống Overfitting mạnh mẽ.
    \item \textbf{Receptive Field (RF --- Vùng cảm thụ):} Kích thước vùng trên ảnh gốc tác động tới giá trị kích hoạt của một neuron ở tầng sâu. Công thức tích lũy qua tầng $l$:
    \begin{equation}
        RF_l = RF_{l-1} + (K_l - 1) \cdot \prod_{i=1}^{l-1} S_i
    \end{equation}
    Xếp chồng hai lớp $3 \times 3$ với stride 1 liên tiếp tạo ra $RF = 1 + (3-1) + (3-1) = 5 \times 5$, nhưng số tham số chỉ là $2 \times (3^2) = 18$ (so với $5^2 = 25$ của một tầng $5 \times 5$ đơn lẻ), đồng thời bổ sung thêm 2 lần kích hoạt phi tuyến ReLU.
\end{itemize}

\subsection{Kiến Trúc CNN Kinh Điển \& Đột Phá ResNet}
\textbf{Cơ chế Residual Learning của ResNet (He et al., 2015):}
Thay vì ép mạng học trực tiếp hàm ánh xạ $\mathcal{H}(\mathbf{x})$, mạng học phần dư $\mathcal{F}(\mathbf{x}) = \mathcal{H}(\mathbf{x}) - \mathbf{x}$:
\begin{equation}
    \mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}
\end{equation}
Khi lan truyền ngược tính gradient theo đầu vào $\mathbf{x}$:
\begin{equation}
    \frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \left( \frac{\partial \mathcal{F}}{\partial \mathbf{x}} + \mathbf{I} \right)
\end{equation}
Nhờ số hạng ma trận đơn vị $\mathbf{I}$, gradient luôn có một "đường cao tốc" chảy thẳng ngược về các tầng nông đầu tiên mà không bao giờ bị triệt tiêu hoàn toàn, giải quyết triệt để hiện tượng thoái hóa mô hình (Degradation Problem) khi đào sâu mạng lên tới 152 tầng.

\subsection{Phân Biệt Skip Connection: ResNet (ADD) vs U-Net (CONCAT)}
\begin{itemize}[leftmargin=*]
    \item \textbf{ResNet (ADD):} Thực hiện phép \textbf{CỘNG theo từng phần tử (Element-wise ADD)}. Yêu cầu số kênh và kích thước không gian hai nhánh phải giống nhau. Mục tiêu: Học phần dư để đào sâu mạng.
    \item \textbf{U-Net (CONCAT):} Thực hiện phép \textbf{GHÉP NỐI theo chiều kênh (Channel-wise CONCAT)}. Ghép trực tiếp feature map độ phân giải cao từ Encoder sang Decoder. Mục tiêu: Giữ lại chi tiết không gian chính xác phục vụ bài toán Phân vùng ảnh (Segmentation).
\end{itemize}

\subsection{Object Detection: IoU, NMS, mAP, YOLO vs Faster R-CNN}
\textbf{Intersection over Union (IoU):}
\begin{equation}
    \text{IoU} = \frac{\text{Diện tích vùng Giao}}{\text{Diện tích vùng Hợp}} = \frac{|B_{\text{pred}} \cap B_{\text{gt}}|}{|B_{\text{pred}} \cup B_{\text{gt}}|}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $B_{\text{pred}}$: Bounding box do mô hình dự đoán.
    \item $B_{\text{gt}}$: Bounding box nhãn thực tế (Ground Truth).
    \item Một dự đoán được công nhận là True Positive ($TP$) nếu $\text{IoU} \ge \text{ngưỡng}$ (thường là $0.5$) và đúng nhãn lớp.
\end{itemize}

\textbf{Thuật toán Non-Maximum Suppression (NMS) 4 bước:}
\begin{enumerate}[leftmargin=*]
    \item Loại bỏ toàn bộ các box có Confidence Score nhỏ hơn ngưỡng tin cậy $T_{\text{conf}}$ (ví dụ $0.25$).
    \item Chọn box $B_{\text{max}}$ có Confidence Score cao nhất trong danh sách còn lại, lưu vào danh sách giữ lại.
    \item Tính IoU giữa $B_{\text{max}}$ và tất cả các box còn lại trong danh sách. Xóa bỏ toàn bộ các box có $\text{IoU} \ge T_{\text{NMS}}$ (thường đặt $0.5$) vì chúng cùng dự đoán trùng lặp một vật thể.
    \item Lặp lại bước 2 và 3 cho đến khi không còn box nào trong danh sách ứng viên.
\end{enumerate}

\textbf{Độ đo mAP (Mean Average Precision):}
\begin{equation}
    \text{AP} = \int_0^1 P(R) dR, \quad \text{mAP} = \frac{1}{C} \sum_{c=1}^C \text{AP}_c
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $\text{AP}$: Diện tích dưới đường cong Precision-Recall của một lớp.
    \item $\text{mAP@0.5}$: Giá trị mAP tính tại ngưỡng $\text{IoU} = 0.5$.
    \item $\text{mAP@[0.5:0.95]}$: Trung bình cộng mAP tại 10 mức ngưỡng IoU từ $0.50$ đến $0.95$ với bước nhảy $0.05$ (chuẩn benchmark COCO).
\end{itemize}

% =========================================================================
% CHƯƠNG 4: XỬ LÝ NGÔN NGỮ TỰ NHIÊN (NLP)
% =========================================================================
\section{Xử Lý Ngôn Ngữ Tự Nhiên (Natural Language Processing)}

\subsection{Pipeline Tiền Xử Lý Văn Bản Chuẩn 5 Bước}
\begin{enumerate}[leftmargin=*]
    \item \textbf{Tokenization:} Tách chuỗi văn bản thành các đơn vị cơ sở (Word, Subword: BPE, WordPiece).
    \item \textbf{Normalization:} Chuyển chữ thường, chuẩn hóa dấu tiếng Việt (NFC vs NFD), xóa URL/HTML/ký tự lạ.
    \item \textbf{Lemmatization vs Stemming:} Stemming chặt đuôi từ bằng quy tắc cơ học (bị lỗi chính tả); Lemmatization đưa về từ nguyên mẫu theo từ điển và ngữ pháp.
    \item \textbf{POS Tagging:} Gán nhãn từ loại (Danh từ, Động từ, Tính từ).
    \item \textbf{Stopwords Removal:} Loại bỏ các từ dừng có tần suất cao nhưng ít giá trị thông tin.
\end{enumerate}

\subsection{Các Phương Pháp Biểu Diễn Từ (Word Representations)}
\begin{itemize}[leftmargin=*]
    \item \textbf{TF-IDF:} Tần suất từ $\text{TF}(t, d)$ nhân với nghịch đảo tần suất tài liệu $\text{IDF}(t, D) = \log\left(\frac{|D|}{|\{d \in D: t \in d\}|}\right)$.
    \item \textbf{Word2Vec (Mikolov et al., 2013):} Gồm 2 kiến trúc: \textbf{CBOW} (dự đoán từ trung tâm dựa vào ngữ cảnh xung quanh) và \textbf{Skip-gram} (dự đoán ngữ cảnh xung quanh dựa vào từ trung tâm, kết hợp Negative Sampling).
    \item \textbf{FastText (Bojanowski et al., 2017):} Biểu diễn từ bằng tập hợp các \textbf{ký tự n-gram (Subwords)}. Giải quyết triệt để vấn đề \textbf{Từ ngoài từ điển (OOV --- Out-of-Vocabulary)}.
\end{itemize}

\subsection{Độ Đo Cosine Similarity}
\begin{equation}
    \cos(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum_{i=1}^d u_i^2} \sqrt{\sum_{i=1}^d v_i^2}} \in [-1, 1]
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $\mathbf{u}, \mathbf{v} \in \mathbb{R}^d$: Hai vector nhúng embedding cần so khớp độ tương đồng ngữ nghĩa.
    \item $\mathbf{u} \cdot \mathbf{v}$: Tích vô hướng (Dot product) giữa hai vector.
    \item $\|\mathbf{u}\|_2, \|\mathbf{v}\|_2$: Chuẩn Euclid (độ dài hình học) của các vector.
    \item \textbf{Bản chất:} Chỉ đo lường góc nghiêng giữa hai vector, triệt tiêu hoàn toàn ảnh hưởng của độ dài văn bản $\implies$ \textbf{Chuẩn mực bắt buộc trong Information Retrieval và Vector Search}.
\end{itemize}

\subsection{Mạng Hồi Quy Tuần Tự: RNN, LSTM \& GRU}

\subsubsection{Mạng Nơ-ron Hồi Quy Cổ Điển (Vanilla RNN)}
Với chuỗi đầu vào $(\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_T)$, tại mỗi bước thời gian $t \in \{1, \dots, T\}$:
\begin{equation}
    \mathbf{h}_t = \tanh(\mathbf{W}_{hh} \mathbf{h}_{t-1} + \mathbf{W}_{xh} \mathbf{x}_t + \mathbf{b}_h)
\end{equation}
\textbf{Giải thích chi tiết các ký hiệu:}
\begin{itemize}[leftmargin=*]
    \item $t$: Chỉ số bước thời gian (Time step), ứng với vị trí của từ thứ $t$ trong câu.
    \item $\mathbf{x}_t \in \mathbb{R}^{d_{\text{in}}}$: Vector đầu vào tại thời điểm $t$ (vector word embedding của từ thứ $t$).
    \item $\mathbf{h}_t \in \mathbb{R}^{d_h}$: Vector trạng thái ẩn (Hidden state) tại thời điểm $t$, đóng vai trò trí nhớ ngắn hạn tổng hợp ngữ cảnh từ bước $1$ đến bước $t$.
    \item $\mathbf{h}_{t-1} \in \mathbb{R}^{d_h}$: Vector trạng thái ẩn được truyền lại từ bước liền trước $t-1$ ($\mathbf{h}_0 = \mathbf{0}$).
    \item $\mathbf{W}_{hh} \in \mathbb{R}^{d_h \times d_h}$: Ma trận trọng số kết nối giữa ẩn quá khứ và ẩn hiện tại (dùng chung qua mọi bước).
    \item $\mathbf{W}_{xh} \in \mathbb{R}^{d_h \times d_{\text{in}}}$: Ma trận trọng số kết nối giữa đầu vào hiện tại và trạng thái ẩn.
    \item $\mathbf{b}_h \in \mathbb{R}^{d_h}$: Vector bias độ lệch.
    \item \textbf{Nhược điểm chí mạng:} Khi chuỗi dài, phép nhân ma trận liên tiếp $\prod \mathbf{W}_{hh}$ khi lan truyền ngược qua thời gian (BPTT) khiến gradient bị co về 0 theo hàm mũ $\implies$ \textbf{Vanishing Gradient}, mất khả năng ghi nhớ dài hạn.
\end{itemize}

\subsubsection{Mạng LSTM (Long Short-Term Memory --- Hochreiter \& Schmidhuber, 1997)}
LSTM bổ sung đường truyền \textbf{Cell State ($\mathbf{C}_t$)} chạy xuyên suốt như một "băng chuyền trí nhớ dài hạn", được điều tiết bởi 3 cổng (Gates) sử dụng hàm kích hoạt Sigmoid $\sigma \in (0, 1)$:
\begin{align}
    \text{1. Cổng Quên (Forget Gate):} \quad \mathbf{f}_t &= \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f) \\
    \text{2. Cổng Nhớ (Input Gate):} \quad \mathbf{i}_t &= \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i) \\
    \text{Ứng viên Cell State mới:} \quad \tilde{\mathbf{C}}_t &= \tanh(\mathbf{W}_c [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_c) \\
    \text{3. Cập nhật Cell State Băng chuyền:} \quad \mathbf{C}_t &= \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t \\
    \text{4. Cổng Xuất (Output Gate):} \quad \mathbf{o}_t &= \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o) \\
    \text{Trạng thái ẩn đầu ra:} \quad \mathbf{h}_t &= \mathbf{o}_t \odot \tanh(\mathbf{C}_t)
\end{align}

\textbf{Mổ xẻ chi tiết từng tham số và ký hiệu toán học:}
\begin{itemize}[leftmargin=*]
    \item $t$: Chỉ số thời gian (bước thứ $t$, từ thứ $t$).
    \item $\mathbf{x}_t \in \mathbb{R}^{d_{\text{in}}}$: Vector đầu vào của từ tại vị trí $t$.
    \item $\mathbf{h}_{t-1} \in \mathbb{R}^{d_h}$: Vector trạng thái ẩn (ngữ cảnh ngắn hạn) từ bước trước truyền sang.
    \item $[\mathbf{h}_{t-1}, \mathbf{x}_t] \in \mathbb{R}^{d_h + d_{\text{in}}}$: Phép ghép nối vector (Concatenation) đặt hai vector nằm cạnh nhau.
    \item $\mathbf{f}_t \in (0, 1)^{d_h}$: Vector \textbf{Cổng Quên}. Đi qua hàm $\sigma$ nên các phần tử mang giá trị từ 0 đến 1. Giá trị tiến về 0 nghĩa là "quên sạch thông tin cũ tương ứng", tiến về 1 nghĩa là "bảo tồn hoàn toàn thông tin cũ".
    \item $\mathbf{i}_t \in (0, 1)^{d_h}$: Vector \textbf{Cổng Nhớ}, quyết định mức độ bao nhiêu phần trăm thông tin mới được phép ghi vào bộ nhớ dài hạn.
    \item $\tilde{\mathbf{C}}_t \in (-1, 1)^{d_h}$: Vector \textbf{Ứng viên Cell State mới}, chứa lượng thông tin mới tinh chất được chắt lọc qua hàm $\tanh$.
    \item $\mathbf{C}_t \in \mathbb{R}^{d_h}$: Vector \textbf{Cell State (Trạng thái ô / Bộ nhớ dài hạn)} tại bước $t$. Phép toán $\mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$ là phép tổ hợp tuyến tính: phần quá khứ được giữ lại cộng với phần kiến thức mới được nạp vào.
    \item $\mathbf{o}_t \in (0, 1)^{d_h}$: Vector \textbf{Cổng Xuất}, quyết định phần nào của bộ nhớ dài hạn $\mathbf{C}_t$ sẽ được bộc lộ ra làm trạng thái ẩn $\mathbf{h}_t$.
    \item $\mathbf{h}_t \in (-1, 1)^{d_h}$: Trạng thái ẩn đầu ra tại bước $t$, vừa dùng để đưa vào tầng phân loại, vừa truyền sang bước tiếp theo $t+1$.
    \item $\mathbf{W}_f, \mathbf{W}_i, \mathbf{W}_c, \mathbf{W}_o \in \mathbb{R}^{d_h \times (d_h + d_{\text{in}})}$: Các ma trận trọng số huấn luyện của từng cổng tương ứng.
    \item $\mathbf{b}_f, \mathbf{b}_i, \mathbf{b}_c, \mathbf{b}_o \in \mathbb{R}^{d_h}$: Các vector bias độ lệch tương ứng với từng cổng.
    \item $\odot$: Phép nhân Hadamard (Element-wise multiplication --- nhân từng phần tử tương ứng giữa hai vector cùng số chiều).
    \item $\sigma$: Hàm Sigmoid nén giá trị về $(0, 1)$, đóng vai trò công tắc van điều tiết tỷ lệ đóng mở cổng.
\end{itemize}

\begin{trapbox}{Tại sao LSTM triệt tiêu được Vanishing Gradient?}
Đạo hàm riêng của băng chuyền Cell State: $\frac{\partial \mathbf{C}_t}{\partial \mathbf{C}_{t-1}} = \mathbf{f}_t$. Khi mô hình học được việc duy trì cổng quên mở ($\mathbf{f}_t \approx 1$), gradient lan truyền ngược dọc theo $\mathbf{C}$ sẽ được nhân với số 1, bảo toàn nguyên vẹn độ lớn qua hàng trăm bước thời gian mà không bị suy giảm theo cấp số nhân như phép nhân ma trận trọng số $\mathbf{W}_{hh}$ trong Vanilla RNN!
\end{trapbox}

\subsubsection{Mạng GRU (Gated Recurrent Unit --- Cho et al., 2014)}
GRU rút gọn cấu trúc còn 2 cổng, gộp chung Cell State vào Hidden State $\mathbf{h}_t$:
\begin{align}
    \text{Cổng Tái lập (Reset Gate):} \quad \mathbf{r}_t &= \sigma(\mathbf{W}_r [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_r) \\
    \text{Cổng Cập nhật (Update Gate):} \quad \mathbf{z}_t &= \sigma(\mathbf{W}_z [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_z) \\
    \text{Trạng thái ứng viên:} \quad \tilde{\mathbf{h}}_t &= \tanh(\mathbf{W}_h [\mathbf{r}_t \odot \mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_h) \\
    \text{Cập nhật Trạng thái ẩn:} \quad \mathbf{h}_t &= (1 - \mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t
\end{align}
\begin{itemize}[leftmargin=*]
    \item $\mathbf{z}_t$: Gộp chức năng của cả Cổng Quên và Cổng Nhớ trong LSTM: thông tin cũ giữ lại là $(1 - \mathbf{z}_t)$, thông tin mới nạp vào là $\mathbf{z}_t$.
    \item Giảm khoảng $25\%$ số lượng tham số so với LSTM, tốc độ huấn luyện nhanh hơn trên các tập dữ liệu kích thước vừa và nhỏ.
\end{itemize}

\subsection{Kiến Trúc Transformer (Vaswani et al., 2017)}
\textbf{Scaled Dot-Product Attention:}
\begin{equation}
    \text{Attention}(Q, K, V) = \text{softmax}\left( \frac{QK^T}{\sqrt{d_k}} \right) V
\end{equation}
\textbf{Giải thích bản chất chi tiết của từng thành phần:}
\begin{itemize}[leftmargin=*]
    \item $Q \in \mathbb{R}^{N \times d_k}$ (Query Matrix): Ma trận truy vấn. Mỗi hàng đại diện cho một từ đang "đi tìm kiếm" thông tin liên quan từ các từ khác. Tạo bởi $Q = X W^Q$.
    \item $K \in \mathbb{R}^{M \times d_k}$ (Key Matrix): Ma trận chìa khóa. Mỗi hàng đóng vai trò như nhãn định danh / tiêu đề của từng từ để khớp với Query. Tạo bởi $K = X W^K$.
    \item $V \in \mathbb{R}^{M \times d_v}$ (Value Matrix): Ma trận giá trị. Mỗi hàng chứa đựng nội dung ngữ nghĩa thực sự mà từ đó mang theo. Tạo bởi $V = X W^V$.
    \item $d_k$: Số chiều của vector Query và Key (trong Transformer gốc, $d_{\text{model}} = 512, h = 8 \implies d_k = 64$).
    \item $QK^T \in \mathbb{R}^{N \times M}$: Ma trận tích vô hướng đo độ tương đồng ngữ nghĩa giữa mọi cặp từ.
    \item $\text{softmax}(\cdot)$: Chuẩn hóa từng hàng thành phân phối xác suất tổng bằng 1 (Attention Weights --- Trọng số chú ý).
    \item Nhân với $V$: Tính tổng có trọng số của các vector Value, cho ra biểu diễn ngữ cảnh hoàn toàn mới tích hợp thông tin từ toàn bộ câu.
\end{itemize}

\begin{trapbox}{Tại sao bắt buộc phải chia cho $\sqrt{d_k}$?}
Giả sử các phần tử của $Q$ và $K$ là các biến ngẫu nhiên độc lập có kỳ vọng bằng 0 và phương sai bằng 1. Khi đó tích vô hướng $q \cdot k = \sum_{j=1}^{d_k} q_j k_j$ có phương sai bằng đúng $d_k$. Khi $d_k$ lớn (ví dụ $d_k = 64$), giá trị tích vô hướng trở nên cực lớn, đẩy hàm Softmax vào vùng bão hòa cực đoan nơi đạo hàm tiệm cận về 0 $\implies$ \textbf{Vanishing Gradient}. Phép chia cho $\sqrt{d_k}$ kéo phương sai trở về 1, giữ cho gradient ổn định.
\end{trapbox}

\textbf{Positional Encoding (Sinusoidal):}
Do cơ chế Self-Attention xử lý toàn bộ các từ song song và có tính chất bất biến hoán vị (Permutation Invariant), bắt buộc phải cộng vector vị trí vào embedding:
\begin{equation}
    PE_{(pos, 2i)} = \sin\left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right), \quad PE_{(pos, 2i+1)} = \cos\left( \frac{pos}{10000^{2i/d_{\text{model}}}} \right)
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $pos$: Vị trí thứ tự của từ trong câu ($pos = 0, 1, 2, \dots$).
    \item $i$: Chỉ số chiều trong không gian vector embedding ($i \in [0, d_{\text{model}}/2 - 1]$).
    \item $d_{\text{model}}$: Tổng số chiều của vector embedding (ví dụ 512 hoặc 768).
    \item Các bước sóng hình sin trải dài từ $2\pi$ đến $10\,000 \cdot 2\pi$, cho phép mô hình dễ dàng học cách tham chiếu các vị trí tương đối thông qua công thức lượng giác cộng góc: $PE_{pos + k} = f(PE_{pos})$.
\end{itemize}

\subsection{Các Độ Đo Đánh Giá NLP: BLEU, SacreBLEU, ROUGE \& Perplexity}
\textbf{BLEU (Bilingual Evaluation Understudy):}
\begin{equation}
    \text{BLEU} = BP \cdot \exp\left( \sum_{n=1}^N w_n \log p_n \right), \quad BP = \min\left(1, e^{1 - r/c}\right)
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $p_n$: Modified n-gram precision (tỉ lệ các cụm $n$ từ trong câu sinh ra xuất hiện trong câu tham chiếu, có cắt bớt tần suất xuất hiện cực đại để tránh gian lận lặp từ).
    \item $w_n$: Trọng số của từng bậc n-gram (thường dùng $N=4$ và $w_n = 1/4$).
    \item $c$: Độ dài của câu do mô hình sinh ra (Candidate length).
    \item $r$: Độ dài của câu dịch tham chiếu chuẩn của con người (Reference length).
    \item $BP$ (Brevity Penalty): Hệ số phạt câu sinh ra quá ngắn. Nếu $c > r$, $BP = 1$; nếu $c \le r$, $BP = e^{1 - r/c} < 1$.
    \item \textbf{ROUGE:} Định hướng \textbf{Recall}, đo lường mức độ bao phủ thông tin, là chuẩn mực cho bài toán \textbf{Tóm tắt văn bản (Summarization)}.
    \item \textbf{Perplexity (PPL):} $\text{PPL} = \exp(\mathcal{L}_{\text{CE}})$, đo lường độ bối rối của mô hình ngôn ngữ. \textbf{PPL càng thấp mô hình càng xuất sắc}.
\end{itemize}

% =========================================================================
% CHƯƠNG 5: TOÁN & XÁC SUẤT THỐNG KÊ CHO AI
% =========================================================================
\section{Toán \& Xác Suất Thống Kê Cho Trí Tuệ Nhân Tạo}

\subsection{Định Lý Bayes \& Ngụy Biện Tỷ Lệ Cơ Sở (Base-Rate Fallacy)}
\begin{equation}
    P(A | B) = \frac{P(B | A) P(A)}{P(B)} = \frac{P(B | A) P(A)}{P(B | A)P(A) + P(B | \neg A)P(\neg A)}
\end{equation}
\begin{itemize}[leftmargin=*]
    \item $P(A)$: Xác suất Tiên nghiệm (Prior Probability) --- niềm tin ban đầu khi chưa có dữ liệu.
    \item $P(B | A)$: Khả năng xảy ra (Likelihood) --- xác suất quan sát thấy bằng chứng $B$ khi giả thuyết $A$ đúng.
    \item $P(B)$: Biên bằng chứng (Evidence / Marginal Probability) --- xác suất toàn phần xuất hiện bằng chứng $B$.
    \item $P(A | B)$: Xác suất Hậu nghiệm (Posterior Probability) --- niềm tin được cập nhật về $A$ sau khi đã quan sát thấy bằng chứng $B$.
\end{itemize}

\begin{examplebox}{Bài toán Chẩn đoán Y tế Xét nghiệm Bệnh Hiếm (Base-Rate Fallacy)}
Giả sử một căn bệnh hiếm có tỉ lệ mắc trong dân số là $2\%$ ($P(\text{Bệnh}) = 0.02 \implies P(\text{Khỏe}) = 0.98$). Một xét nghiệm có độ nhạy $95\%$ ($P(+ | \text{Bệnh}) = 0.95$) và tỉ lệ dương tính giả là $4\%$ ($P(+ | \text{Khỏe}) = 0.04$). Một người ngẫu nhiên có kết quả xét nghiệm Dương tính ($+$). Xác suất người đó thực sự mắc bệnh là bao nhiêu?
\begin{itemize}[leftmargin=*]
    \item Tử số (Likelihood $\times$ Prior): $P(+ | \text{Bệnh}) \cdot P(\text{Bệnh}) = 0.95 \times 0.02 = 0.019$.
    \item Mẫu số (Xác suất toàn phần $P(+)$):
    $P(+) = 0.019 + P(+ | \text{Khỏe}) \cdot P(\text{Khỏe}) = 0.019 + (0.04 \times 0.98) = 0.019 + 0.0392 = 0.0582$.
    \item Xác suất hậu nghiệm thực sự mắc bệnh:
    \begin{equation*}
        P(\text{Bệnh} | +) = \frac{0.019}{0.0582} \approx 32.65\%
    \end{equation*}
\end{itemize}
\textbf{Kết luận:} Dù xét nghiệm có độ nhạy rất cao ($95\%$), nhưng do tỷ lệ bệnh trong dân số quá thấp ($2\%$), xác suất một người dương tính thực sự mắc bệnh \textbf{chỉ khoảng 32.6\%}! Hơn 67\% những người nhận kết quả dương tính thực chất là dương tính giả.
\end{examplebox}

\subsection{Tính Chất của Kỳ Vọng, Phương Sai \& Ma Trận Tương Quan}
\begin{align}
    \mathbb{E}[aX + b] &= a\mathbb{E}[X] + b \\
    \text{Var}(X) &= \mathbb{E}[X^2] - (\mathbb{E}[X])^2 \\
    \text{Var}(aX + b) &= a^2 \text{Var}(X) \quad \text{(hằng số cộng } b \text{ không làm đổi độ biến động)}
\end{align}
Nếu $X$ và $Y$ là hai biến ngẫu nhiên độc lập:
\begin{equation}
    \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y), \quad \text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y)
\end{equation}
\textbf{Hiệp phương sai (Covariance) \& Hệ số tương quan Pearson:}
\begin{equation}
    \text{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])], \quad r_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \in [-1, 1]
\end{equation}

\subsection{Ước Lượng Tham Số: MLE vs MAP \& Mối Liên Hệ Với Regularization}
\begin{itemize}[leftmargin=*]
    \item \textbf{Maximum Likelihood Estimation (MLE):} Tối đa hóa hàm hợp lý dựa thuần túy trên dữ liệu quan sát:
    \begin{equation}
        \hat{\theta}_{\text{MLE}} = \arg\max_\theta \sum_{i=1}^N \log P(x_i | \theta)
    \end{equation}
    \item \textbf{Maximum A Posteriori (MAP):} Tích hợp phân phối niềm tin tiên nghiệm (Prior) $P(\theta)$:
    \begin{equation}
        \hat{\theta}_{\text{MAP}} = \arg\max_\theta \left[ \sum_{i=1}^N \log P(x_i | \theta) + \log P(\theta) \right]
    \end{equation}
    \item \textbf{Cầu nối toán học với Regularization:}
    \begin{itemize}
        \item Tiên nghiệm phân phối Chuẩn $\theta \sim \mathcal{N}(0, \sigma_0^2) \implies \log P(\theta) = -\frac{1}{2\sigma_0^2} \|\theta\|_2^2 + \text{const} \iff$ \textbf{Regularization L2 (Ridge)}.
        \item Tiên nghiệm phân phối Laplace $P(\theta) \propto \exp(-\lambda \|\theta\|_1) \implies \log P(\theta) = -\lambda \|\theta\|_1 \iff$ \textbf{Regularization L1 (Lasso)}.
    \end{itemize}
\end{itemize}

\subsection{Kiểm Định Giả Thuyết Thống Kê \& Ý Nghĩa Của p-value}
\begin{itemize}[leftmargin=*]
    \item Giả thuyết vô hiệu $H_0$ (mặc định không có sự khác biệt), Giả thuyết đối $H_1$.
    \item \textbf{Định nghĩa chuẩn mực của p-value:}
    \begin{equation}
        p\text{-value} = P(\text{Quan sát được kết quả cực đoan như thế hoặc hơn thế} \mid H_0 \text{ đúng})
    \end{equation}
    \item Nếu $p\text{-value} < \alpha$ (thường là $0.05$), ta bác bỏ giả thuyết $H_0$ ở mức ý nghĩa thống kê $\alpha$.
    \item \textbf{Bẫy đề thi:} $p$-value \textbf{KHÔNG PHẢI} là xác suất giả thuyết $H_0$ đúng ($P(H_0 | \text{Data})$); $p$-value cũng không đo lường độ lớn hiệu ứng thực tế (Effect size).
\end{itemize}

% =========================================================================
% CHƯƠNG 6: BẢNG 24 BẪY ĐỀ THI KINH ĐIỂN
% =========================================================================
\section{Bảng 24 Bẫy Đề Thi Kinh Điển (Lỗi Hay Mắc: SAI $\to$ ĐÚNG)}

\begin{xltabular}{\textwidth}{lp{6.2cm}X}
\toprule
\textbf{\#} & \textbf{Quan niệm SAI (Bẫy đề thi)} & \textbf{Kiến thức ĐÚNG \& Cơ chế hoạt động} \\
\midrule
\endfirsthead
\toprule
\textbf{\#} & \textbf{Quan niệm SAI (Bẫy đề thi)} & \textbf{Kiến thức ĐÚNG \& Cơ chế hoạt động} \\
\midrule
\endhead
\bottomrule
\endfoot
1 & \texttt{BatchNorm} đặt sau hàm kích hoạt \texttt{ReLU} & Chuẩn mực là: \textbf{Linear / Conv $\to$ BatchNorm $\to$ ReLU}. \\ \addlinespace
2 & Thêm \texttt{Softmax} trước \texttt{nn.CrossEntropyLoss} & \texttt{CrossEntropyLoss} đã tích hợp sẵn LogSoftmax, nhận \textbf{Logit thô}. \\ \addlinespace
3 & Thêm \texttt{Sigmoid} trước \texttt{nn.BCEWithLogitsLoss} & \texttt{BCEWithLogitsLoss} đã có sẵn sigmoid bên trong, nhận \textbf{Logit thô}. \\ \addlinespace
4 & Thuật toán k-NN có giai đoạn cập nhật trọng số & k-NN là \textbf{Lazy Learner}, chỉ lưu dữ liệu, không có phase train. \\ \addlinespace
5 & $\text{IoU} = \text{Diện tích Giao} / \text{Diện tích toàn ảnh}$ & $\text{IoU} = \frac{\text{Giao}}{\text{Hợp}}$ của 2 bounding box. \\ \addlinespace
6 & Entropy trong Decision Tree dùng $\log_{10}$ hoặc $\ln$ & Lý thuyết thông tin dùng \textbf{$\log_2$}, đơn vị là \textbf{bit}. \\ \addlinespace
7 & Stable Diffusion là một biến thể nâng cấp của GAN & Là \textbf{Diffusion Model} (khử nhiễu từng bước), không phải GAN. \\ \addlinespace
8 & Gọi \texttt{optimizer.zero\_grad()} sau \texttt{loss.backward()} & Phải gọi \texttt{zero\_grad()} \textbf{trước \texttt{backward()}} vì grad mặc định cộng dồn. \\ \addlinespace
9 & Skip connection trong U-Net là phép cộng \texttt{ADD} & U-Net dùng phép \textbf{ghép nối kênh (\texttt{CONCAT})}; \texttt{ADD} là của ResNet. \\ \addlinespace
10 & Dùng Accuracy để đánh giá bài toán lệch lớp & Bị đánh lừa bởi lớp đa số; bắt buộc dùng \textbf{F1-score, PR-AUC}. \\ \addlinespace
11 & Khởi tạo toàn bộ ma trận trọng số bằng $0$ & Gây \textbf{hiện tượng đối xứng (Symmetry)}, neuron cập nhật y hệt nhau. \\ \addlinespace
12 & Giữ Dropout bật trong giai đoạn Test / Inference & Phải \textbf{tắt Dropout khi inference (\texttt{model.eval()})}. \\ \addlinespace
13 & So sánh vector embedding bằng khoảng cách Euclid & Chuẩn là dùng \textbf{Cosine Similarity} (bỏ qua độ lớn norm vector). \\ \addlinespace
14 & $p$-value là xác suất giả thuyết $H_0$ đúng & $p$-value là $P(\text{dữ liệu cực đoan} \mid H_0 \text{ đúng})$. \\ \addlinespace
15 & Vision Transformer (ViT) dùng các lớp Conv $3 \times 3$ & ViT \textbf{không dùng Conv}, cắt patches và đưa vào Transformer Encoder. \\ \addlinespace
16 & Siêu tham số $\gamma$ của SVM RBF lớn thì biên mượt & $\gamma$ càng lớn thì biên \textbf{càng cong ôm sát từng điểm $\implies$ Overfitting}. \\ \addlinespace
17 & Regularization L1 (Lasso) chỉ co nhỏ trọng số & L1 triệt tiêu trọng số về chính xác bằng 0 $\implies$ \textbf{Tạo tính thưa (Sparsity)}. \\ \addlinespace
18 & Dùng metric BLEU để chấm bài toán Tóm tắt văn bản & \textbf{BLEU dùng cho Dịch máy}; Tóm tắt văn bản dùng \textbf{ROUGE}. \\ \addlinespace
19 & Áp dụng Data Augmentation trên toàn bộ tập Test & \textbf{Chỉ augment trên tập Train}, tập Validation/Test giữ nguyên. \\ \addlinespace
20 & Trong Self-Attention không cần chia cho $\sqrt{d_k}$ & Phải chia $\sqrt{d_k}$ để tránh Softmax rơi vào vùng bão hòa gradient. \\ \addlinespace
21 & Dùng mô hình BERT để sinh văn bản dài tự do & BERT dùng cho \textbf{Hiểu (NLU)}; sinh văn bản tự hồi quy dùng \textbf{GPT}. \\ \addlinespace
22 & Lớp Pooling (Max, Avg) có tham số huấn luyện & Lớp Pooling \textbf{hoàn toàn không có tham số học được (0 params)}. \\ \addlinespace
23 & Thuật toán SMOTE nhân bản y nguyên mẫu thiểu số & SMOTE \textbf{nội suy sinh điểm mới} trên đoạn thẳng nối với láng giềng. \\ \addlinespace
24 & $\text{Var}(aX + b) = a \cdot \text{Var}(X)$ & Đúng là $\mathbf{\text{Var}(aX + b) = a^2 \cdot \text{Var}(X)}$. \\
\end{xltabular}

% =========================================================================
% CHƯƠNG 7: CHUYÊN ĐỀ TÁC VỤ THỰC CHIẾN (KHUNG 5 BƯỚC)
% =========================================================================
\section{Chuyên Đề Tác Vụ Thực Chiến OLP AI 2025 \& 2026 (Khung 5 Bước)}

Trong các kỳ thi Olympic AI, phần tự luận yêu cầu thí sinh đề xuất phương án giải quyết bài toán thực tế theo \textbf{Khung chuẩn 5 bước}:
\begin{enumerate}[leftmargin=*]
    \item \textbf{Bước 1: Phân tích Dữ liệu \& Đặc thù Bài toán} (Kiểu dữ liệu, độ lệch lớp, rủi ro Data Leakage, ràng buộc phần cứng).
    \item \textbf{Bước 2: Lựa chọn Mô hình (Baseline $\to$ SOTA) \& Luận chứng} (Mô hình cơ sở $\to$ Mô hình đề xuất chính).
    \item \textbf{Bước 3: Pipeline Xử lý \& Chiến lược Validation} (Tiền xử lý, Augmentation, chia Fold chống rò rỉ, hậu xử lý).
    \item \textbf{Bước 4: Metric Đánh giá Phù hợp} (Chỉ số đo lường phản ánh đúng mục tiêu nghiệp vụ).
    \item \textbf{Bước 5: Phương án Cải tiến \& Tối ưu Hóa Thực tế} (Kỹ thuật nâng cao: Distillation, Quantization, Ensemble).
\end{enumerate}

\subsection{Tác vụ 1 (Đề OLP AI 2025): Nhận Diện Ngôn Ngữ Ký Hiệu từ Video}
\textbf{Bối cảnh bài toán:} 10.000 video clip ngắn ghi lại 50 cử chỉ ngôn ngữ ký hiệu, thực hiện bởi 100 người trong các môi trường ánh sáng và nền phức tạp. Yêu cầu chạy real-time trên laptop.

\begin{enumerate}[leftmargin=*]
    \item \textbf{Phân tích dữ liệu:} Video có số frame biến thiên theo thời gian. Rủi ro \textbf{Data Leakage nghiêm trọng} nếu các frame của cùng một người xuất hiện ở cả Train và Val (mô hình sẽ học nhận diện khuôn mặt người thay vì cử chỉ tay). Cần xử lý bất biến nền.
    \item \textbf{Lựa chọn mô hình:}
    \begin{itemize}
        \item \textit{Baseline:} Trích xuất đặc trưng từng frame bằng MobileNetV3 + trượt cửa sổ thời gian.
        \item \textit{Đề xuất chính:} Kết hợp trích xuất đặc trưng không gian nhẹ (ConvNeXt-Tiny hoặc MediaPipe Holistic trích xuất 3D Landmark bàn tay/khớp xương) kết hợp \textbf{Temporal Transformer Encoder / Bi-GRU + Attention Pooling}.
    \end{itemize}
    \item \textbf{Pipeline xử lý:} Lấy mẫu cố định 32 frames/clip bằng uniform sampling. Augmentation không gian (Random crop, color jitter) và thời gian (Time masking, co giãn tốc độ $\pm 20\%$). Validation: \textbf{Person-independent GroupKFold theo ID người thực hiện}. Huấn luyện bằng hàm mất mát CTC Loss hoặc Cross-Entropy sau Temporal Pooling.
    \item \textbf{Metric đánh giá:} \textbf{Sequence-level Accuracy}, Word Error Rate (WER), Character Error Rate (CER). Tuyệt đối không dùng Frame-level Accuracy.
    \item \textbf{Phương án cải tiến:} Tận dụng tọa độ Landmark từ MediaPipe để chuyển đổi bài toán từ ảnh pixel sang vector khớp xương, tăng tốc độ xử lý $10\times$; Lượng tử hóa INT8 bằng ONNX Runtime để đạt 30+ FPS trên CPU laptop.
\end{enumerate}

\subsection{Tác vụ 2 (Đề OLP AI 2025): Dịch Máy Thương Mại Điện Tử Hoa --- Việt}
\textbf{Bối cảnh bài toán:} 200.000 cặp câu song ngữ chuyên ngành thương mại điện tử. Yêu cầu dịch chính xác tên sản phẩm và tuyệt đối không làm sai lệch số lượng, đơn vị tính và mệnh giá tiền tệ.

\begin{enumerate}[leftmargin=*]
    \item \textbf{Phân tích dữ liệu:} Cặp câu song ngữ bất đối xứng: Tiếng Trung viết liền không khoảng trắng; Tiếng Việt nhiều từ ghép đa âm tiết. Chứa nhiều mã model sản phẩm, giá tiền (¥, VND), số đo ($cm, kg$).
    \item \textbf{Lựa chọn mô hình:}
    \begin{itemize}
        \item \textit{Baseline:} Seq2Seq GRU 2 lớp với Luong Attention.
        \item \textit{Đề xuất chính:} \textbf{Transformer tiêu chuẩn (6 Encoder layers, 6 Decoder layers)} hoặc Fine-tune từ mô hình dịch máy tiền huấn luyện đa ngữ mạnh như \textbf{NLLB-200 (No Language Left Behind)} hoặc \textbf{mBART-50}.
    \end{itemize}
    \item \textbf{Pipeline xử lý:} Tách từ chuyên biệt bằng Jieba (tiếng Trung) và VnCoreNLP (tiếng Việt). Huấn luyện Joint Byte-Pair Encoding (BPE) chung với vocab 32.000 tokens. \textbf{Bảo vệ thực thể số/tiền tệ:} Dùng Regex gán nhãn placeholder (ví dụ \texttt{<NUM\_1>}, \texttt{<CURR\_VND>}) trước khi dịch, sau đó đối chiếu ánh xạ ngược lại vào câu dịch tiếng Việt. Giải mã bằng Beam Search (Width = 5) kết hợp Label Smoothing = 0.1.
    \item \textbf{Metric đánh giá:} \textbf{SacreBLEU} (chuẩn hóa tokenization) và \textbf{chrF++} (độ đo ký tự nhạy với ngữ pháp tiếng Việt). Đánh giá thủ công trên tập 200 câu khó chứa nhiều thông số kỹ thuật.
    \item \textbf{Phương án cải tiến:} Back-translation trên dữ liệu đơn ngữ tiếng Việt để nhân đôi tập train; Reranking các kết quả sinh từ Beam Search bằng mô hình PhoBERT.
\end{enumerate}

\subsection{Tác vụ 3 (Đề xuất OLP 2026): Phát Hiện Bệnh Lá Cây Trồng Trên Thiết Bị Di Động}
\textbf{Bối cảnh bài toán:} 8.000 ảnh chụp lá cây ngoài đồng ruộng thực tế, 4 nhóm bệnh (trong đó 2 nhóm bệnh hiếm). Yêu cầu khoanh vùng vết bệnh và chạy mượt mà offline trên điện thoại nông dân.

\begin{enumerate}[leftmargin=*]
    \item \textbf{Phân tích dữ liệu:} Bài toán Object Detection thực địa với phông nền đất ruộng và bóng râm rất phức tạp. Mất cân bằng lớp nặng giữa bệnh phổ biến và bệnh hiếm. Ràng buộc phần cứng: Dung lượng mô hình $< 20\text{ MB}$, độ trễ $< 50\text{ ms}$.
    \item \textbf{Lựa chọn mô hình:}
    \begin{itemize}
        \item \textit{Baseline:} EfficientNet-B0 làm bộ phân loại toàn ảnh (không khoanh vùng).
        \item \textit{Đề xuất chính:} \textbf{YOLOv8n (Nano) hoặc YOLOv11n}. Kiến trúc 1-stage với số tham số chỉ $\approx 3\text{ triệu}$, tối ưu hóa cao cho bộ xử lý di động NPU/GPU.
    \end{itemize}
    \item \textbf{Pipeline xử lý:} Augmentation: Mosaic, Mixup, Random HSV. Validation: \textbf{GroupKFold theo thửa ruộng và ngày chụp ảnh}. Áp dụng \textbf{Focal Loss} để giảm ảnh hưởng của vùng nền dễ phát hiện, tập trung vào các vết bệnh nhỏ và hiếm. Ngưỡng NMS IoU $\ge 0.5$.
    \item \textbf{Metric đánh giá:} $\text{mAP@0.5}$ và $\text{mAP@[0.5:0.95]}$. Báo cáo riêng Precision và Recall cho 2 nhóm bệnh hiếm.
    \item \textbf{Phương án cải tiến:} Lượng tử hóa sau huấn luyện (Post-Training Quantization --- INT8) xuất sang TFLite/CoreML giúp giảm $4\times$ dung lượng và tăng tốc $3\times$ trên CPU điện thoại.
\end{enumerate}

\subsection{Tác vụ 4 (Đề xuất OLP 2026): Dự Đoán Sinh Viên Bỏ Học \& Explainable AI (XAI)}
\textbf{Bối cảnh bài toán:} Dữ liệu dạng bảng 50.000 sinh viên với 40 trường thông tin (điểm học phần, số tín chỉ trễ, tình trạng đóng học phí, điểm rèn luyện). Tỉ lệ bỏ học là $8\%$. Phòng đào tạo cần mô hình dự đoán chính xác và \textbf{giải thích được nguyên nhân cụ thể cho từng sinh viên} để can thiệp kịp thời.

\begin{enumerate}[leftmargin=*]
    \item \textbf{Phân tích dữ liệu:} Dữ liệu dạng bảng (Tabular Data) với $8\%$ nhãn dương (Imbalanced Data). Chứa cả biến số và biến danh mục. Nghiệp vụ đòi hỏi tính minh bạch và khả năng giải thích (Explainability).
    \item \textbf{Lựa chọn mô hình:}
    \begin{itemize}
        \item \textit{Baseline:} Logistic Regression sau khi chuẩn hóa StandardScaler.
        \item \textit{Đề xuất chính:} \textbf{LightGBM hoặc XGBoost}. Vượt trội trên dữ liệu dạng bảng, xử lý tự nhiên giá trị khuyết và tương tác phi tuyến, không cần Deep Learning phức tạp.
    \end{itemize}
    \item \textbf{Pipeline xử lý:} Điền trung vị cho biến số, tạo nhãn \texttt{Missing} cho biến danh mục. Feature Engineering: Tạo các đặc trưng vi phân biểu thị xu hướng: $\Delta \text{GPA} = \text{GPA}_{\text{kỳ này}} - \text{GPA}_{\text{kỳ trước}}$, tỉ lệ tín chỉ nợ $/ \text{tổng tín chỉ}$. Validation: \textbf{Stratified 5-Fold Cross Validation}. Thiết lập \texttt{scale\_pos\_weight = 11.5}. Tối ưu ngưỡng cắt $p^*$ theo F1-score.
    \item \textbf{Metric đánh giá:} \textbf{PR-AUC} và \textbf{F1-score}. Ma trận chi phí (Cost Matrix) phạt nặng việc bỏ sót sinh viên bỏ học ($FN$).
    \item \textbf{Phương án cải tiến \& Giải thích mô hình (XAI):} Tích hợp \textbf{SHAP (SHapley Additive exPlanations)}:
    \begin{itemize}
        \item \textit{Global Feature Importance:} Xác định các yếu tố cốt lõi dẫn đến nguy cơ bỏ học trên toàn trường.
        \item \textit{Local Waterfall Plot:} Vẽ đồ thị đóng góp cụ thể của từng chỉ số cho từng sinh viên cụ thể để gửi cho cố vấn học tập lên phương án hỗ trợ.
    \end{itemize}
\end{enumerate}

\vspace{1em}
\hrule
\vspace{0.8em}
\begin{center}
    {\small \textbf{--- HẾT TÀI LIỆU ÔN TẬP TOÀN DIỆN OLYMPIC AI HCMUS 2026 ---}} \\
    {\footnotesize \textit{Chúc các thí sinh ôn tập tập trung, nắm chắc bản chất toán học và đạt thành tích cao nhất!}}
\end{center}

\end{document}
'''

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def build_pdf():
    docs_dir = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26\docs"
    os.makedirs(docs_dir, exist_ok=True)
    tex_path = os.path.join(docs_dir, "olp_ai_handbook_2026.tex")
    pdf_path = os.path.join(docs_dir, "olp_ai_handbook_2026.pdf")
    public_pdf = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26\public\olp_ai_handbook_2026.pdf"
    artifact_pdf = r"C:\Users\HP\.gemini\antigravity-ide\brain\fd518ebc-4364-4d84-87e7-831d5592335b\olp_ai_handbook_2026.pdf"

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(TEX_CONTENT)
    print(f"Da ghi file TeX: {tex_path} ({len(TEX_CONTENT)} ky tu)")

    cmd = ["xelatex", "-interaction=nonstopmode", "olp_ai_handbook_2026.tex"]
    print("Dang bien dich lan 1...")
    res1 = subprocess.run(cmd, cwd=docs_dir, capture_output=True)
    print(f"Lan 1 returncode: {res1.returncode}")

    print("Dang bien dich lan 2 (cap nhat Muc luc va lien ket)...")
    res2 = subprocess.run(cmd, cwd=docs_dir, capture_output=True)
    print(f"Lan 2 returncode: {res2.returncode}")

    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"XUAT THANH CONG PDF: {pdf_path} ({size_kb:.2f} KB)")
        shutil.copy2(pdf_path, public_pdf)
        shutil.copy2(pdf_path, artifact_pdf)
        print("Da sao chep vao public/ va thu muc artifact.")

if __name__ == "__main__":
    build_pdf()
