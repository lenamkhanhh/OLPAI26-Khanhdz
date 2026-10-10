# -*- coding: utf-8 -*-
"""
Script docs/generate_full_hub.py
Tạo hoàn chỉnh file olympic_ai_study_hub.html với tất cả tính năng, giao diện học thuật chuẩn,
không lỗi KaTeX, đầy đủ 2 đề thi và lời giải ELI5 step-by-step.
"""

import os
import sys
import json
import re
import base64

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
TEMP_DIR = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26"

sys.path.append(os.path.join(ROOT_DIR, "docs"))
# Đã chuyển sang đọc trực tiếp 3 đề JSON chuẩn hóa

# 1. Đọc cả 6 đề thi đã chuẩn hóa từ src/data/exams/
olp01_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-01.json")
olp02_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-02.json")
olp03_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-03.json")
olp04_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-04.json")
voai2025_path = os.path.join(ROOT_DIR, "src", "data", "exams", "voai-2025.json")
olp05_path = os.path.join(ROOT_DIR, "src", "data", "exams", "olp-05.json")

with open(olp01_path, "r", encoding="utf-8") as f:
    olp01_data = json.load(f)
with open(olp02_path, "r", encoding="utf-8") as f:
    olp02_data = json.load(f)
with open(olp03_path, "r", encoding="utf-8") as f:
    olp03_data = json.load(f)
with open(olp04_path, "r", encoding="utf-8") as f:
    olp04_data = json.load(f)
with open(voai2025_path, "r", encoding="utf-8") as f:
    voai2025_data = json.load(f)
with open(olp05_path, "r", encoding="utf-8") as f:
    olp05_data = json.load(f)

# Tự động inline base64 cho các câu hỏi có hình ảnh để HTML chạy offline 100% không vỡ ảnh
for exam_data in [olp01_data, olp02_data, olp03_data, olp04_data, voai2025_data, olp05_data]:
    for q in exam_data.get("questions", []):
        if q.get("image"):
            img_rel = q["image"]
            img_path = os.path.join(ROOT_DIR, "public", img_rel)
            if not os.path.exists(img_path):
                img_path = os.path.join(ROOT_DIR, img_rel)
            if os.path.exists(img_path):
                with open(img_path, "rb") as imf:
                    b64_str = base64.b64encode(imf.read()).decode("ascii")
                    ext = "png" if img_path.lower().endswith(".png") else "jpeg"
                    q["image"] = f"data:image/{ext};base64,{b64_str}"

# 2. Đọc lý thuyết từ 01-ly-thuyet-olp-ai.md
theory_path = os.path.join(ROOT_DIR, "content", "01-ly-thuyet-olp-ai.md")
with open(theory_path, "r", encoding="utf-8") as f:
    theory_md = f.read()

pattern = r'(###?\s+(§[\d\.]+.*?)\n)([\s\S]*?)(?=(?:###?\s+§|\Z))'
matches = re.findall(pattern, theory_md)
theory_sections = []
for full_header, header_text, body_text in matches:
    m_id = re.match(r'(§[\d\.]+)\s*(.*)', header_text.strip())
    if m_id:
        sec_id = m_id.group(1).strip()
        title = m_id.group(2).strip()
    else:
        sec_id = header_text.strip().split()[0]
        title = header_text.strip()
    clean_id = "sec-" + sec_id.replace("§", "").replace(".", "-")
    theory_sections.append({
        "id": clean_id,
        "secId": sec_id,
        "title": title if title else sec_id,
        "body": body_text.strip()
    })

# Video Mapping: Tự động trích xuất toàn bộ kho 46 video tuyển chọn từ src/data/videoData.ts
video_data_path = os.path.join(ROOT_DIR, "src", "data", "videoData.ts")
with open(video_data_path, "r", encoding="utf-8") as f:
    vts_content = f.read()

v_pattern = re.compile(
    r"'([§\d\.]+)':\s*\{\s*sectionId:\s*'([^']+)',\s*topic:\s*'([^']+)',\s*channel:\s*'([^']+)',\s*title:\s*'([^']+)',\s*youtubeId:\s*'([^']+)',\s*startSeconds:\s*(\d+),\s*timestampLabel:\s*'([^']+)',\s*highlightNote:\s*'([^']+)'",
    re.DOTALL
)
videos_map = {}
for sec, sec_id, topic, chan, tit, ytid, start, tlabel, note in v_pattern.findall(vts_content):
    videos_map[sec] = {
        "sectionId": sec_id,
        "topic": topic,
        "channel": chan,
        "title": tit,
        "youtubeId": ytid,
        "startSeconds": int(start),
        "timestampLabel": tlabel,
        "highlightNote": note
    }
print(f"-> Đã nạp thành công {len(videos_map)} video chuẩn học thuật từ videoData.ts")

# Clean TeX Function
def clean_tex_string(s):
    if not s:
        return ""
    
    def repl_text(m):
        inner = m.group(1)
        subs = {
            "bệnh": "benh", "khỏe": "khoe", "dương tính": "duong_tinh",
            "âm tính": "am_tinh", "chính xác": "chinh_xac", "tổng": "tong",
            "cha": "cha", "con": "con", "Giao": "Giao", "Hợp": "Hop"
        }
        for k, v in subs.items():
            inner = inner.replace(k, v)
        return f"\\text{{{inner}}}"
    
    def repl_math(m):
        tex = m.group(0)
        tex = re.sub(r'\\text\{([^}]+)\}', repl_text, tex)
        tex = re.sub(r'(?<!\\)%', r'\\%', tex)
        return tex
    
    s = re.sub(r'\$\$([\s\S]*?)\$\$', repl_math, s)
    s = re.sub(r'\$([^\$\n]+?)\$', repl_math, s)
    return s

# Danh mục công thức cốt lõi
FORMULAS = [
    {
        "title": "Công thức kích thước đầu ra tầng Conv2D",
        "desc": "Tính chiều rộng và chiều cao tensor đầu ra (lấy hàm sàn floor trước khi cộng 1):",
        "tex": "O = \\left\\lfloor \\frac{W - K + 2P}{S} \\right\\rfloor + 1"
    },
    {
        "title": "Định lý Bayes & Xác suất toàn phần",
        "desc": "Tính xác suất hậu nghiệm (Posterior) từ tiền nghiệm (Prior) và hợp lý (Likelihood):",
        "tex": "P(A \\mid B) = \\frac{P(B \\mid A) \\cdot P(A)}{P(B \\mid A) \\cdot P(A) + P(B \\mid \\neg A) \\cdot P(\\neg A)}"
    },
    {
        "title": "Độ hỗn loạn thông tin Shannon Entropy",
        "desc": "Đo độ bất định của phân phối xác suất rời rạc (cơ số 2, đơn vị bit):",
        "tex": "H(S) = - \\sum_{i=1}^C p_i \\log_2(p_i)"
    },
    {
        "title": "Mức tăng thông tin (Information Gain - ID3)",
        "desc": "Độ giảm entropy sau khi phân chia theo thuộc tính A:",
        "tex": "\\text{IG}(S, A) = H(S) - \\sum_{v \\in \\text{Values}(A)} \\frac{|S_v|}{|S|} H(S_v)"
    },
    {
        "title": "Chỉ số giao trên hợp (Intersection over Union - IoU)",
        "desc": "Độ trùng khớp giữa bounding box dự đoán và nhãn thực tế:",
        "tex": "\\text{IoU} = \\frac{\\text{Area}(B_p \\cap B_g)}{\\text{Area}(B_p \\cup B_g)}"
    },
    {
        "title": "Chỉ số F1-Score (Trung bình điều hòa)",
        "desc": "Cân bằng giữa độ chính xác (Precision) và độ bao phủ (Recall):",
        "tex": "F_1 = 2 \\cdot \\frac{\\text{Precision} \\cdot \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2 \\cdot \\text{TP}}{2 \\cdot \\text{TP} + \\text{FP} + \\text{FN}}"
    },
    {
        "title": "Độ tương đồng Cosine Similarity",
        "desc": "Đo góc định hướng giữa hai vector đặc trưng trong không gian vector:",
        "tex": "\\cos(\\theta) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\|_2 \\|\\mathbf{v}\\|_2} = \\frac{\\sum_{i} u_i v_i}{\\sqrt{\\sum_{i} u_i^2} \\sqrt{\\sum_{i} v_i^2}}"
    },
    {
        "title": "Cơ chế Scaled Dot-Product Attention (Transformer)",
        "desc": "Ma trận trọng số chú ý giữa Query, Key và Value:",
        "tex": "\\text{Attention}(Q, K, V) = \\text{softmax}\\left( \\frac{Q K^T}{\\sqrt{d_k}} \\right) V"
    },
    {
        "title": "Hàm mất mát Cross-Entropy (Phân loại đa lớp)",
        "desc": "Hàm mất mát trên vector phân phối xác suất sau Softmax:",
        "tex": "\\mathcal{L}_{\\text{CE}} = - \\sum_{c=1}^C y_c \\log(\\hat{y}_c)"
    },
    {
        "title": "Ma trận Hessian & Cực trị địa phương bậc 2",
        "desc": "Khai triển Taylor bậc 2 quanh điểm dừng; xác định dương tương ứng cực tiểu địa phương:",
        "tex": "f(\\mathbf{x}) \\approx f(\\mathbf{x}^*) + \\frac{1}{2}(\\mathbf{x} - \\mathbf{x}^*)^T H (\\mathbf{x} - \\mathbf{x}^*), \\quad H = \\nabla^2 f(\\mathbf{x}^*)"
    }
]

# Tập hợp dữ liệu 6 đề thi chuẩn
all_exams_data = {
    "olp-01": olp01_data,
    "olp-02": olp02_data,
    "olp-03": olp03_data,
    "olp-04": olp04_data,
    "voai-2025": voai2025_data,
    "olp-05": olp05_data
}

# 3. Đọc dữ liệu khóa học OLP Sinh Viên & VOAI Nâng Cao
courses_path = os.path.join(ROOT_DIR, "src", "data", "courses_data.json")
if os.path.exists(courses_path):
    with open(courses_path, "r", encoding="utf-8") as f:
        courses_data = json.load(f)
else:
    courses_data = {"olp_course": {"lessons": []}, "voai_course": {"lessons": []}}

all_exams_json_str = json.dumps(all_exams_data, ensure_ascii=False)
theory_json_str = json.dumps(theory_sections, ensure_ascii=False)
videos_json_str = json.dumps(videos_map, ensure_ascii=False)
formulas_json_str = json.dumps(FORMULAS, ensure_ascii=False)
courses_json_str = json.dumps(courses_data, ensure_ascii=False)

print("Đang tiến hành tạo file HTML hoàn chỉnh...")

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Olympic AI HCMUS 2026 — Academic Arena & Study Hub</title>
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  
  <!-- Typography: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- KaTeX CSS (Local + Fallback CDN) -->
  <link rel="stylesheet" href="katex/katex.min.css" onerror="this.onerror=null;this.href='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css'">
  
  <!-- KaTeX Script (Local + Fallback CDN) -->
  <script src="katex/katex.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js'"></script>
  <script src="katex/contrib/auto-render.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js'"></script>

  <style>
    :root {{
      /* PURE OLED / AMOLED LUXURY JET BLACK THEME (ZERO BLUE TINT) */
      --bg-base: #000000;
      --bg-surface: #0a0a0a;
      --bg-card: #121212;
      --bg-elevated: #181818;
      --bg-hover: #222222;
      
      --border-subtle: #1c1c1c;
      --border-strong: #2a2a2a;
      --border-focus: #f0b90b;
      
      /* Binance VIP Gold & Financial Accents */
      --color-gold: #f0b90b;
      --color-gold-hover: #fcd535;
      --color-ac: #0ecb81;
      --color-wa: #f6465d;
      --color-partial: #f0b90b;
      
      /* High-Contrast Neutral Typography */
      --text-main: #f5f5f5;
      --text-secondary: #cccccc;
      --text-muted: #888888;
      --text-dim: #444444;
      
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
      --font-serif: 'STIX Two Text', 'Cambria', 'Times New Roman', serif;
      
      --radius-sm: 4px;
      --radius-md: 6px;
      --radius-lg: 8px;
      
      --sidebar-w: 280px;
      --split-w: 420px;
      --inspector-w: 380px;
      --header-h: 46px;
      --footer-h: 44px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      height: 100vh;
      max-height: 100vh;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: var(--bg-base);
    }}

    /* Sleek Academic Matte Scrollbar (Highly Visible & Responsive) */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(0, 0, 0, 0.4);
    }}
    ::-webkit-scrollbar-thumb {{
      background: #333333;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #f0b90b;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-base);
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      font-size: 13px;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }}

    /* 1. TOP HEADER (BINANCE PRO VIP TRADING BAR) */
    .arena-header {{
      height: var(--header-h);
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 12px;
      user-select: none;
      z-index: 40;
      gap: 8px;
      flex-wrap: nowrap;
      overflow: hidden;
      flex-shrink: 0;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    .contest-badge {{
      background: rgba(240, 185, 11, 0.08);
      color: #f0b90b;
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 11px;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(240, 185, 11, 0.3);
      letter-spacing: 0.5px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
      flex-shrink: 0;
    }}

    .exam-select-box {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #0e0e0e;
      border: 1px solid var(--border-subtle);
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      max-width: 220px;
      flex-shrink: 1;
      min-width: 140px;
      transition: border-color 0.15s ease;
    }}
    .exam-select-box:hover {{
      border-color: var(--border-strong);
    }}

    .exam-select {{
      background: transparent;
      color: var(--text-main);
      border: none;
      font-size: 12px;
      font-weight: 600;
      outline: none;
      cursor: pointer;
      width: 100%;
      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;
    }}
    .exam-select option {{
      background: #0a0a0a;
      color: #f5f5f5;
    }}

    .header-center {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }}

    .timer-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #0e0e0e;
      border: 1px solid var(--border-subtle);
      padding: 3px 10px;
      border-radius: 14px;
      font-family: var(--font-mono);
      font-size: 12.5px;
      font-weight: 600;
      color: #f0b90b;
      white-space: nowrap;
    }}

    .live-dot {{
      width: 6px;
      height: 6px;
      background: #0ecb81;
      border-radius: 50%;
      box-shadow: 0 0 6px #0ecb81;
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.9); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    .score-ticker {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      white-space: nowrap;
    }}

    .ticker-gold-val {{
      color: #f0b90b;
      font-weight: 700;
    }}

    .badge-ac-count {{
      background: rgba(14, 203, 129, 0.12);
      color: #0ecb81;
      border: 1px solid rgba(14, 203, 129, 0.3);
      padding: 1px 7px;
      border-radius: 10px;
      font-weight: 600;
      font-size: 11px;
    }}

    .badge-wa-count {{
      background: rgba(246, 70, 93, 0.12);
      color: #f6465d;
      border: 1px solid rgba(246, 70, 93, 0.3);
      padding: 1px 7px;
      border-radius: 10px;
      font-weight: 600;
      font-size: 11px;
    }}

    .badge-essay-score {{
      background: rgba(255, 255, 255, 0.05);
      color: #cccccc;
      border: 1px solid var(--border-subtle);
      padding: 1px 7px;
      border-radius: 10px;
      font-weight: 600;
      font-size: 11px;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    /* BUTTONS: PURE JET BLACK SUITE */
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 5px 12px;
      font-size: 12px;
      font-weight: 500;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-strong);
      background: #141414;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
      position: relative;
      white-space: nowrap;
    }}

    .btn:hover {{
      background: #222222;
      border-color: #3e3e3e;
      color: #ffffff;
    }}

    /* Binance Signature Primary Gold Button */
    .btn-primary {{
      background: #f0b90b !important;
      border: 1px solid #f0b90b !important;
      color: #000000 !important;
      font-weight: 600 !important;
    }}
    .btn-primary:hover {{
      background: #fcd535 !important;
      border-color: #fcd535 !important;
    }}

    /* Active Tool Button */
    .btn-active {{
      background: rgba(240, 185, 11, 0.12) !important;
      border-color: #f0b90b !important;
      color: #f0b90b !important;
    }}

    /* Binance Green Action */
    .btn-success {{
      background: rgba(14, 203, 129, 0.15) !important;
      border: 1px solid rgba(14, 203, 129, 0.4) !important;
      color: #0ecb81 !important;
      font-weight: 600 !important;
    }}
    .btn-success:hover {{
      background: rgba(14, 203, 129, 0.25) !important;
    }}

    /* Binance Red Action */
    .btn-danger {{
      background: rgba(246, 70, 93, 0.15) !important;
      border: 1px solid rgba(246, 70, 93, 0.4) !important;
      color: #f6465d !important;
      font-weight: 600 !important;
    }}
    .btn-danger:hover {{
      background: rgba(246, 70, 93, 0.25) !important;
    }}

    .btn-icon {{
      padding: 5px 9px;
      font-size: 13px;
    }}

    /* 2. MAIN 3-COLUMN ARENA */
    .arena-main {{
      flex: 1;
      min-height: 0;
      height: calc(100vh - var(--header-h));
      display: flex;
      overflow: hidden;
      position: relative;
    }}

    /* 2.1 LEFT SIDEBAR */
    .arena-sidebar {{
      width: var(--sidebar-w);
      min-width: 0;
      height: 100%;
      min-height: 0;
      background: var(--bg-surface);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      flex-shrink: 0;
    }}
    .arena-sidebar.collapsed {{
      display: none !important;
    }}

    .sidebar-tabs {{
      display: flex;
      background: var(--bg-base);
      border-bottom: 1px solid var(--border-subtle);
      flex-shrink: 0;
    }}

    .s-tab {{
      flex: 1;
      padding: 10px 4px;
      font-size: 11px;
      font-weight: 600;
      text-align: center;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.15s ease;
      letter-spacing: 0.3px;
    }}
    .s-tab:hover {{
      color: #f5f5f5;
      background: rgba(255, 255, 255, 0.02);
    }}
    .s-tab.active {{
      color: #f0b90b;
      border-bottom-color: #f0b90b;
      background: rgba(240, 185, 11, 0.05);
    }}

    .sidebar-content {{
      flex: 1;
      min-height: 0;
      overflow-y: auto;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .contest-progress-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 10px;
      border-radius: var(--radius-sm);
    }}
    .prog-text {{
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      font-family: var(--font-mono);
      margin-bottom: 6px;
      color: var(--text-secondary);
    }}
    .prog-track {{
      height: 5px;
      background: #000000;
      border: 1px solid var(--border-subtle);
      border-radius: 3px;
      overflow: hidden;
    }}
    .prog-bar {{
      height: 100%;
      background: #f0b90b;
      width: 0%;
      transition: width 0.3s ease;
    }}

    .problem-filter-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }}
    .filter-btn {{
      font-size: 10px;
      font-weight: 500;
      padding: 3px 8px;
      border-radius: 3px;
      border: 1px solid var(--border-subtle);
      background: #111111;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-btn:hover {{
      background: #1a1a1a;
      color: #f5f5f5;
      border-color: var(--border-strong);
    }}
    .filter-btn.active {{
      background: #1a1a1a;
      color: #f0b90b;
      border-color: #f0b90b;
    }}

    .cp-matrix-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(42px, 1fr));
      gap: 5px;
    }}

    .matrix-item {{
      height: 32px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      background: #0d0d0d;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .matrix-item:hover {{
      border-color: #f0b90b;
      color: #f5f5f5;
      background: #161616;
    }}
    .matrix-item.active {{
      border: 1.5px solid #f0b90b !important;
      background: #1c1c1c !important;
      color: #f0b90b !important;
    }}
    .matrix-item.ac {{
      background: rgba(14, 203, 129, 0.12) !important;
      border-color: rgba(14, 203, 129, 0.4) !important;
      color: #0ecb81 !important;
    }}
    .matrix-item.wa {{
      background: rgba(246, 70, 93, 0.12) !important;
      border-color: rgba(246, 70, 93, 0.4) !important;
      color: #f6465d !important;
    }}
    .matrix-item.partial {{
      background: rgba(240, 185, 11, 0.12) !important;
      border-color: rgba(240, 185, 11, 0.4) !important;
      color: #f0b90b !important;
    }}

    /* RESIZABLE SPLITTERS */
    .splitter-gutter {{
      width: 6px;
      min-width: 6px;
      cursor: col-resize;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-subtle);
      border-right: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      user-select: none;
      z-index: 35;
      flex-shrink: 0;
      transition: background 0.15s ease, border-color 0.15s ease;
    }}
    .splitter-gutter:hover,
    .splitter-gutter.active {{
      background: rgba(240, 185, 11, 0.25);
      border-color: #f0b90b;
    }}
    .splitter-handle {{
      width: 2px;
      height: 28px;
      border-radius: 1px;
      background: #333333;
      transition: background 0.15s ease;
    }}
    .splitter-gutter:hover .splitter-handle,
    .splitter-gutter.active .splitter-handle {{
      background: #f0b90b;
    }}

    body.is-resizing {{
      cursor: col-resize !important;
      user-select: none !important;
    }}
    body.is-resizing iframe {{
      pointer-events: none !important;
    }}

    /* 2.2 CENTER WORKSPACE */
    .arena-center {{
      flex: 1 1 0%;
      min-width: 260px;
      min-height: 0;
      height: 100%;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: var(--bg-base);
    }}

    /* SCROLLABLE VIEWPORT (FIXED 100% RELIABLE SCROLLING) */
    .problem-viewport {{
      flex: 1 1 0%;
      min-height: 0;
      height: 100%;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 22px 30px 48px 30px;
      max-width: 1020px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 18px;
      scroll-behavior: smooth;
    }}
    .problem-viewport > * {{
      flex-shrink: 0;
    }}

    .problem-header-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
    }}

    .problem-title-row {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 6px;
      flex-wrap: wrap;
    }}
    .problem-id-badge {{
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 700;
      color: #f0b90b;
    }}
    .problem-title {{
      font-size: 17px;
      font-weight: 600;
      color: var(--text-main);
      letter-spacing: -0.01em;
    }}

    .problem-meta-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 11.5px;
      color: var(--text-muted);
      border-top: 1px solid var(--border-subtle);
      padding-top: 8px;
      margin-top: 6px;
    }}
    .meta-val {{
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--text-main);
    }}

    .statement-section {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px;
    }}
    .section-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-muted);
      margin-bottom: 12px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .statement-text {{
      font-size: 14px;
      line-height: 1.7;
      color: var(--text-main);
    }}

    /* Options Grid */
    .options-grid {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .cp-option-card {{
      background: #0d0d0d;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }}
    .cp-option-card:hover {{
      background: #161616;
      border-color: #333333;
    }}
    .cp-option-card.selected {{
      border-color: #f0b90b !important;
      background: rgba(240, 185, 11, 0.06) !important;
    }}
    .cp-option-card.correct {{
      border-color: #0ecb81 !important;
      background: rgba(14, 203, 129, 0.08) !important;
    }}
    .cp-option-card.wrong {{
      border-color: #f6465d !important;
      background: rgba(246, 70, 93, 0.08) !important;
    }}

    .option-key-badge {{
      width: 26px;
      height: 26px;
      min-width: 26px;
      border-radius: 4px;
      border: 1px solid var(--border-strong);
      display: grid;
      place-items: center;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      background: #141414;
      transition: all 0.15s ease;
    }}
    .cp-option-card.selected .option-key-badge {{
      border-color: #f0b90b;
      background: #f0b90b;
      color: #000000;
    }}
    .cp-option-card.correct .option-key-badge {{
      border-color: #0ecb81;
      background: #0ecb81;
      color: #000000;
    }}
    .cp-option-card.wrong .option-key-badge {{
      border-color: #f6465d;
      background: #f6465d;
      color: #ffffff;
    }}

    .option-text-content {{
      font-size: 13.5px;
      line-height: 1.6;
      color: var(--text-main);
      flex: 1;
      min-width: 0;
    }}
    .option-text-content .katex {{
      font-size: 1.05em;
    }}

    /* Verdict Banner */
    .verdict-banner {{
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      display: flex;
      flex-direction: column;
      gap: 3px;
      animation: fadeIn 0.15s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(-3px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .verdict-banner.ac {{
      background: rgba(14, 203, 129, 0.08);
      border: 1px solid rgba(14, 203, 129, 0.35);
    }}
    .verdict-banner.wa {{
      background: rgba(246, 70, 93, 0.08);
      border: 1px solid rgba(246, 70, 93, 0.35);
    }}
    .verdict-title {{
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 13px;
    }}
    .verdict-banner.ac .verdict-title {{
      color: #0ecb81;
    }}
    .verdict-banner.wa .verdict-title {{
      color: #f6465d;
    }}
    .verdict-meta {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    /* Official Editorial Card */
    .editorial-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      flex-shrink: 0;
    }}
    .editorial-header {{
      padding: 12px 16px;
      background: #111111;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: background 0.15s ease;
    }}
    .editorial-header:hover {{
      background: #1a1a1a;
    }}
    .editorial-title {{
      font-size: 12px;
      font-weight: 700;
      color: #f0b90b;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .editorial-body {{
      padding: 16px;
      font-size: 13px;
      line-height: 1.65;
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* ELI5 BLOCKS WITH PURE ACCENTS */
    .eli5-block {{
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      border-left: 3px solid #888888;
      background: #111111;
      color: var(--text-main);
    }}
    .eli5-block.math {{
      border-left-color: #0ecb81;
      background: rgba(14, 203, 129, 0.04);
    }}
    .eli5-block.trap {{
      border-left-color: #f0b90b;
      background: rgba(240, 185, 11, 0.04);
    }}
    .eli5-block.ref {{
      border-left-color: #5b8def;
      background: rgba(91, 141, 239, 0.04);
    }}

    /* Bottom Navigation Bar */
    .arena-footer {{
      height: var(--footer-h);
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 12px;
      z-index: 30;
      flex-shrink: 0;
      overflow: hidden;
      gap: 6px;
    }}

    .footer-left {{
      display: flex;
      align-items: center;
      gap: 6px;
      min-width: 0;
      overflow: hidden;
    }}

    .footer-prog-tag {{
      font-size: 11px;
      color: var(--text-muted);
      margin-left: 4px;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }}

    .footer-right {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }}

    /* 2.3 SECONDARY SPLIT PANE */
    .arena-split-pane {{
      height: 100%;
      min-height: 0;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      flex-shrink: 0;
    }}

    /* 2.4 RIGHT INSPECTOR PANEL */
    .arena-inspector {{
      width: var(--inspector-w);
      min-width: 0;
      height: 100%;
      min-height: 0;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      flex-shrink: 0;
    }}
    .arena-inspector.collapsed {{
      display: none !important;
    }}

    .inspector-top-bar {{
      padding: 8px 12px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-shrink: 0;
    }}
    .inspector-title-group {{
      display: flex;
      flex-direction: column;
    }}
    .inspector-eyebrow {{
      font-size: 9.5px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .inspector-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-main);
    }}

    .inspector-tabs {{
      display: flex;
      background: var(--bg-base);
      border-bottom: 1px solid var(--border-subtle);
      flex-shrink: 0;
    }}
    .i-tab {{
      flex: 1;
      padding: 9px 4px;
      font-size: 11px;
      font-weight: 600;
      text-align: center;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .i-tab:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.02);
    }}
    .i-tab.active {{
      color: #f0b90b !important;
      border-bottom-color: #f0b90b !important;
      background: rgba(240, 185, 11, 0.05) !important;
    }}

    .inspector-content {{
      flex: 1;
      min-height: 0;
      overflow-y: auto;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    /* Formula Box */
    .cp-formula-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .formula-title {{
      font-size: 11.5px;
      font-weight: 700;
      color: #f0b90b;
    }}

    /* Video Card */
    .video-card-cp {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    .video-thumb-box {{
      position: relative;
      width: 100%;
      padding-top: 56.25%;
      background: #000;
      cursor: pointer;
      overflow: hidden;
    }}
    .video-thumb-img {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.85;
      transition: transform 0.2s ease, opacity 0.2s ease;
    }}
    .video-thumb-box:hover .video-thumb-img {{
      transform: scale(1.03);
      opacity: 1;
    }}
    .video-play-overlay {{
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      display: grid;
      place-items: center;
      background: rgba(0, 0, 0, 0.4);
    }}
    .play-btn-circle {{
      width: 46px;
      height: 46px;
      background: #f0b90b;
      border-radius: 50%;
      display: grid;
      place-items: center;
      color: #000000;
      font-size: 18px;
      font-weight: 900;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.7);
      transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
    }}
    .video-thumb-box:hover .play-btn-circle {{
      transform: scale(1.15);
      background: #fde047;
      box-shadow: 0 0 22px rgba(240, 185, 11, 0.85);
    }}
    .video-iframe-embed {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
      background: #000000;
    }}
    .timestamp-badge {{
      position: absolute;
      bottom: 6px;
      right: 6px;
      background: rgba(0, 0, 0, 0.9);
      color: #f0b90b;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 600;
      padding: 1px 6px;
      border-radius: 2px;
    }}

    /* KaTeX Safe Styles */
    .katex-display {{
      margin: 0.5em 0 !important;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 2px 0;
    }}
    .katex {{
      font-size: 1.05em !important;
      text-rendering: geometricPrecision;
      color: #ffffff;
    }}
    .katex-error {{
      color: #f87171 !important;
      font-style: italic;
      background: rgba(248, 113, 113, 0.08);
      padding: 1px 4px;
      border-radius: 2px;
    }}
  </style>
</head>
<body>

  <!-- 1. TOP HEADER (BINANCE PRO TRADING BAR) -->
  <header class="arena-header">
    <div class="header-left">
      <button class="btn btn-icon btn-active" id="btnToggleSidebar" onclick="toggleSidebar()" title="Đóng / Mở Danh sách câu hỏi [B]">☰</button>
      <span class="contest-badge">⚡ OLP AI '26</span>
      <div class="exam-select-box">
        <select class="exam-select" id="examSelector" onchange="switchExam(this.value)">
          <option value="olp-01">Đề 01 · Toàn diện (100c)</option>
          <option value="olp-02">Đề 02 · Format VOAI (100c)</option>
          <option value="olp-03">Đề 03 · Mô phỏng Quốc gia (100c)</option>
          <option value="olp-04">Đề 04 · Insight Video VOAI (100c)</option>
          <option value="voai-2025">Đề 006 · Gốc VOAI 2025 (100c)</option>
          <option value="olp-05">Đề 05 · Chuyên đề CV & NLP (100c)</option>
        </select>
      </div>
    </div>

    <div class="header-center">
      <div class="timer-pill">
        <span class="live-dot"></span>
        <span id="contestClock">⏱ 01:00:00</span>
      </div>

      <div class="score-ticker">
        <strong class="ticker-gold-val" id="tickerTotalScore">0.0 / 100.0đ</strong>
        <span class="badge-ac-count" id="tickerAcCount">0 AC</span>
        <span class="badge-wa-count" id="tickerWaCount">0 WA</span>
        <span class="badge-essay-score" id="tickerEssayScore" style="display:none;">Tự luận: 0.0đ</span>
      </div>
    </div>

    <div class="header-right">
      <div id="userAccountBox" style="display:inline-flex; align-items:center; margin-right:6px;"></div>
      <button class="btn" id="btnToggleSplit" onclick="toggleSplitMode()" title="Chia đôi cửa sổ tra cứu">◫ Chia đôi</button>
      <button class="btn btn-active" id="btnToggleInspector" onclick="toggleInspector()" title="Đóng / Mở Bảng tra cứu & Đánh giá [I]">🔍 Tra cứu [I]</button>
      <button class="btn btn-primary" onclick="submitContestConfirm()" title="Nộp bài thi [Ctrl+S]">Nộp bài</button>
    </div>
  </header>

  <!-- 2. ARENA MAIN 3 COLUMNS -->
  <main class="arena-main" id="arenaMain">

    <!-- 2.1 LEFT SIDEBAR -->
    <aside class="arena-sidebar" id="arenaSidebar">
      <div class="sidebar-tabs">
        <div class="s-tab active" id="sTabGrid" onclick="switchSidebarTab('grid')">ĐỀ THI</div>
        <div class="s-tab" id="sTabDoc" onclick="switchSidebarTab('doc')">GIÁO TRÌNH</div>
        <div class="s-tab" id="sTabSub" onclick="switchSidebarTab('sub')">LỊCH SỬ NỘP</div>
      </div>

      <div class="sidebar-content" id="sidebarContent">
        <!-- Rendered by JS -->
      </div>
    </aside>

    <!-- LEFT SPLITTER RESIZER -->
    <div class="splitter-gutter" id="splitterLeft" title="Kéo để chỉnh kích thước Sidebar (kéo hết sang trái để ẩn)">
      <div class="splitter-handle"></div>
    </div>

    <!-- 2.2 CENTER WORKSPACE -->
    <section class="arena-center" id="arenaCenter">
      <div class="problem-viewport" id="problemViewport">
        <!-- Rendered by JS -->
      </div>

      <footer class="arena-footer">
        <div class="footer-left">
          <button class="btn" onclick="prevQuestion()" title="Câu trước [A]">← Trước</button>
          <button class="btn" onclick="nextQuestion()" title="Câu sau [D]">Sau →</button>
          <span class="footer-prog-tag" id="footerProgressLabel">Tiến độ bài thi</span>
        </div>

        <div class="footer-right">
          <button class="btn" onclick="toggleEditorialManual()" title="Xem lời giải [E]">📖 Lời giải [E]</button>
          <button class="btn btn-primary" onclick="submitContestConfirm()" title="Nộp bài thi [Ctrl+S]">Nộp bài</button>
        </div>
      </footer>
    </section>

    <!-- SPLIT PANE SPLITTER RESIZER (BETWEEN CENTER AND SPLIT PANE) -->
    <div class="splitter-gutter" id="splitterSplit" style="display:none;" title="Kéo để chỉnh độ rộng Cửa sổ tra cứu song song (kéo sát sang phải để tắt)">
      <div class="splitter-handle"></div>
    </div>

    <!-- 2.3 SECONDARY SPLIT PANE -->
    <section class="arena-split-pane" id="arenaSplitPane" style="display:none; width:420px;">
      <div style="padding:8px 12px; background:#0e0e0e; border-bottom:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center; flex-shrink:0;">
        <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
          <span style="font-size:11px; font-weight:700; color:var(--text-secondary); text-transform:uppercase;">Tra cứu song song:</span>
          <button class="btn" id="btnSplitPdf" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('pdf')">PDF Handbook</button>
          <button class="btn" id="btnSplitTheory" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('theory')">Giáo trình</button>
          <button class="btn" id="btnSplitFormulas" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('formulas')">Công thức</button>
          <select id="splitTheorySecSelect" style="height:22px; font-size:10.5px; background:#141414; color:#f0b90b; border:1px solid var(--border-subtle); border-radius:3px; padding:0 4px; display:none;" onchange="switchTheorySection(this.value)" title="Chọn chuyên đề lý thuyết để tra cứu"></select>
        </div>
        <button class="btn" style="height:22px; font-size:10px; padding:0 6px;" onclick="toggleSplitMode()">Đóng ✕</button>
      </div>
      <div id="splitPaneBody" style="flex:1; min-height:0; overflow-y:auto;"></div>
    </section>

    <!-- RIGHT SPLITTER RESIZER (BETWEEN WORKSPACE AND INSPECTOR) -->
    <div class="splitter-gutter" id="splitterRight" title="Kéo để chỉnh kích thước Bảng tra cứu (kéo sát mép phải để ẩn)">
      <div class="splitter-handle"></div>
    </div>

    <!-- 2.4 RIGHT INSPECTOR PANEL -->
    <aside class="arena-inspector" id="arenaInspector">
      <div class="inspector-top-bar">
        <div class="inspector-title-group">
          <span class="inspector-eyebrow">Hệ Thống Tra Cứu & Đánh Giá</span>
          <h3 class="inspector-title">ĐÁNH GIÁ & TRA CỨU</h3>
        </div>
        <button class="btn" style="padding:2px 7px; font-size:11px;" onclick="toggleInspector()" title="Thu gọn bảng điều khiển bên phải">✕</button>
      </div>

      <div class="inspector-tabs">
        <div class="i-tab active" id="iTabRubric" onclick="switchInspectorTab('rubric')">RUBRIC CHẤM</div>
        <div class="i-tab" id="iTabExplanation" onclick="switchInspectorTab('explanation')">LUẬN GIẢI</div>
        <div class="i-tab" id="iTabVideo" onclick="switchInspectorTab('video')">BÀI GIẢNG</div>
        <div class="i-tab" id="iTabFormulas" onclick="switchInspectorTab('formulas')">CÔNG THỨC</div>
      </div>

      <div class="inspector-content" id="inspectorContent">
        <!-- Rendered by JS -->
      </div>
    </aside>

  </main>

  <!-- 3. SCRIPT & LOGIC ENGINE -->
  <script>
    // Embedded Multi-Exam Data Store
    const ALL_EXAMS = {all_exams_json_str};
    const THEORY = {theory_json_str};
    const VIDEOS = {videos_json_str};
    const FORMULAS = {formulas_json_str};
    const COURSES = {courses_json_str};

    // Application State
    let currentExamId = 'olp-01';
    let EXAM = ALL_EXAMS[currentExamId];
    let currentIndex = 0;
    let answers = {{}};
    let editorialOpen = {{}};
    let rubricEvalResults = {{}};
    let filterModule = 'all';
    let sidebarTab = 'grid';
    let inspectorTab = 'rubric';
    let isInspectorOpen = true;
    let isSplitOpen = false;
    let splitType = 'theory';
    let timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;
    let timerInterval = null;

    // Storage Versioning & Migration (P0-3)
    const CURRENT_EXAM_VERSIONS = {{
      'olp-01': 2,
      'olp-02': 2,
      'olp-03': 3,
      'olp-04': 2,
      'voai-2025': 2,
      'olp-05': 2
    }};

    // UI Toast Notification
    function showToast(msg) {{
      try {{
        if (typeof document === 'undefined' || !document.createElement || !document.body) return;
        let toast = document.getElementById('hub-toast');
        if (!toast) {{
          toast = document.createElement('div');
          toast.id = 'hub-toast';
          toast.style.position = 'fixed';
          toast.style.bottom = '24px';
          toast.style.right = '24px';
          toast.style.background = '#181818';
          toast.style.color = '#f5f5f5';
          toast.style.border = '1px solid #333';
          toast.style.borderRadius = '6px';
          toast.style.padding = '10px 16px';
          toast.style.fontSize = '12px';
          toast.style.zIndex = '99999';
          toast.style.boxShadow = '0 4px 16px rgba(0,0,0,0.5)';
          toast.style.transition = 'opacity 0.25s ease';
          toast.style.display = 'none';
          document.body.appendChild(toast);
        }}
        toast.textContent = msg;
        toast.style.display = 'block';
        toast.style.opacity = '1';
        setTimeout(() => {{
          if (toast) toast.style.opacity = '0';
        }}, 3500);
      }} catch(e) {{}}
    }}

    // Load LocalStorage with Migration
    function loadSavedState() {{
      try {{
        const storedVer = parseInt(localStorage.getItem('olp-ai-version-' + currentExamId) || '1', 10);
        const currentVer = CURRENT_EXAM_VERSIONS[currentExamId] || 1;
        
        // Nếu đề chưa có version mới (dữ liệu cũ trước khi đảo phương án / sửa câu hỏi)
        if (currentVer > storedVer) {{
          console.warn('[Storage Migration] Reset cache cũ của ' + currentExamId + ' do cập nhật version ' + currentVer);
          localStorage.removeItem('olp-ai-answers-' + currentExamId);
          localStorage.setItem('olp-ai-version-' + currentExamId, currentVer);
          answers = {{}};
          showToast('Đề thi ' + currentExamId + ' đã cập nhật phiên bản mới (v' + currentVer + '). Dữ liệu cũ đã được làm mới.');
          return;
        }}
        
        const saved = localStorage.getItem('olp-ai-answers-' + currentExamId);
        if (saved) answers = JSON.parse(saved);
        else answers = {{}};
      }} catch(e) {{ answers = {{}}; }}
    }}

    function saveState() {{
      try {{
        localStorage.setItem('olp-ai-answers-' + currentExamId, JSON.stringify(answers));
        localStorage.setItem('olp-ai-version-' + currentExamId, CURRENT_EXAM_VERSIONS[currentExamId] || 1);
      }} catch(e) {{}}
    }}

    // Switch Exam Function
    function switchExam(examId) {{
      if (ALL_EXAMS[examId]) {{
        currentExamId = examId;
        EXAM = ALL_EXAMS[examId];
        currentIndex = 0;
        editorialOpen = {{}};
        rubricEvalResults = {{}};
        loadSavedState();
        timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;
        const sel = document.getElementById('examSelector');
        if (sel) sel.value = examId;
        renderSidebar();
        renderCenter();
        renderInspector();
        renderHeaderStats();
      }}
    }}

    // Toggle Sidebar & Inspector Panels with Splitter Sync
    let isSidebarOpen = true;
    function toggleSidebar() {{
      isSidebarOpen = !isSidebarOpen;
      const el = document.getElementById('arenaSidebar');
      const btn = document.getElementById('btnToggleSidebar');
      if (isSidebarOpen) {{
        if (el) {{
          el.classList.remove('collapsed');
          if (!el.style.width || parseInt(el.style.width, 10) < 140) {{
            el.style.width = '280px';
          }}
        }}
        if (btn) btn.classList.add('btn-active');
      }} else {{
        if (el) el.classList.add('collapsed');
        if (btn) btn.classList.remove('btn-active');
      }}
    }}

    function toggleInspector() {{
      isInspectorOpen = !isInspectorOpen;
      const el = document.getElementById('arenaInspector');
      const btn = document.getElementById('btnToggleInspector');
      if (isInspectorOpen) {{
        if (el) {{
          el.classList.remove('collapsed');
          if (!el.style.width || parseInt(el.style.width, 10) < 180) {{
            el.style.width = '380px';
          }}
        }}
        if (btn) btn.classList.add('btn-active');
      }} else {{
        if (el) el.classList.add('collapsed');
        if (btn) btn.classList.remove('btn-active');
      }}
    }}

    // Draggable Resizable Splitters (Precision Resizing, Low Collapse Threshold < 25px)
    function initSplitters() {{
      const leftSplitter = document.getElementById('splitterLeft');
      const splitSplitter = document.getElementById('splitterSplit');
      const rightSplitter = document.getElementById('splitterRight');

      const sidebar = document.getElementById('arenaSidebar');
      const splitPane = document.getElementById('arenaSplitPane');
      const inspector = document.getElementById('arenaInspector');

      const btnToggleSidebar = document.getElementById('btnToggleSidebar');
      const btnToggleInspector = document.getElementById('btnToggleInspector');

      // 1. Left Sidebar Splitter
      if (leftSplitter && typeof leftSplitter.addEventListener === 'function' && sidebar) {{
        let isDraggingLeft = false;

        leftSplitter.addEventListener('mousedown', (e) => {{
          e.preventDefault();
          isDraggingLeft = true;
          leftSplitter.classList.add('active');
          document.body.classList.add('is-resizing');
        }});

        window.addEventListener('mousemove', (e) => {{
          if (!isDraggingLeft) return;
          const newW = e.clientX;
          if (newW < 25) {{
            // Snap collapse only at extreme edge!
            sidebar.classList.add('collapsed');
            sidebar.style.width = '0px';
            isSidebarOpen = false;
            if (btnToggleSidebar) btnToggleSidebar.classList.remove('btn-active');
          }} else {{
            sidebar.classList.remove('collapsed');
            isSidebarOpen = true;
            const maxW = Math.max(200, window.innerWidth - 380);
            const clamped = Math.max(140, Math.min(newW, Math.min(600, maxW)));
            sidebar.style.width = clamped + 'px';
            if (btnToggleSidebar) btnToggleSidebar.classList.add('btn-active');
          }}
        }});

        window.addEventListener('mouseup', () => {{
          if (isDraggingLeft) {{
            isDraggingLeft = false;
            leftSplitter.classList.remove('active');
            document.body.classList.remove('is-resizing');
          }}
        }});
      }}

      // 2. Parallel Split Pane Splitter (Independent Resizing!)
      if (splitSplitter && typeof splitSplitter.addEventListener === 'function' && splitPane) {{
        let isDraggingSplit = false;

        splitSplitter.addEventListener('mousedown', (e) => {{
          e.preventDefault();
          isDraggingSplit = true;
          splitSplitter.classList.add('active');
          document.body.classList.add('is-resizing');
        }});

        window.addEventListener('mousemove', (e) => {{
          if (!isDraggingSplit) return;
          // Calculate right reference point
          const inspectorW = (isInspectorOpen && inspector && !inspector.classList.contains('collapsed'))
            ? inspector.offsetWidth : 0;
          const rightEdge = window.innerWidth - inspectorW;
          const newW = rightEdge - e.clientX;

          if (newW < 25) {{
            // Snap close split pane only if dragged all the way to right edge!
            toggleSplitMode();
          }} else {{
            const maxAllowed = Math.max(250, window.innerWidth - 500);
            const clamped = Math.max(200, Math.min(newW, maxAllowed));
            splitPane.style.width = clamped + 'px';
          }}
        }});

        window.addEventListener('mouseup', () => {{
          if (isDraggingSplit) {{
            isDraggingSplit = false;
            splitSplitter.classList.remove('active');
            document.body.classList.remove('is-resizing');
          }}
        }});
      }}

      // 3. Right Inspector Splitter
      if (rightSplitter && typeof rightSplitter.addEventListener === 'function' && inspector) {{
        let isDraggingRight = false;

        rightSplitter.addEventListener('mousedown', (e) => {{
          e.preventDefault();
          isDraggingRight = true;
          rightSplitter.classList.add('active');
          document.body.classList.add('is-resizing');
        }});

        window.addEventListener('mousemove', (e) => {{
          if (!isDraggingRight) return;
          const newW = window.innerWidth - e.clientX;
          if (newW < 25) {{
            // Snap collapse only at extreme right edge!
            inspector.classList.add('collapsed');
            inspector.style.width = '0px';
            isInspectorOpen = false;
            if (btnToggleInspector) btnToggleInspector.classList.remove('btn-active');
          }} else {{
            inspector.classList.remove('collapsed');
            isInspectorOpen = true;
            const maxW = Math.max(250, window.innerWidth - 380);
            const clamped = Math.max(180, Math.min(newW, Math.min(750, maxW)));
            inspector.style.width = clamped + 'px';
            if (btnToggleInspector) btnToggleInspector.classList.add('btn-active');
          }}
        }});

        window.addEventListener('mouseup', () => {{
          if (isDraggingRight) {{
            isDraggingRight = false;
            rightSplitter.classList.remove('active');
            document.body.classList.remove('is-resizing');
          }}
        }});
      }}
    }}

    // Safe KaTeX Render Engine (100% Bug-Free)
    function sanitizeTex(raw) {{
      if (!raw) return '';
      const math = [];
      let s = raw.replace(/\$\$([\s\S]*?)\$\$/g, (m) => {{
        const idx = math.length;
        math.push(m.replace(/</g, '&lt;').replace(/>/g, '&gt;'));
        return '%%%M_D_' + idx + '%%%';
      }});
      s = s.replace(/\$([^\$\\r\\n]+?)\$/g, (m) => {{
        const idx = math.length;
        math.push(m.replace(/</g, '&lt;').replace(/>/g, '&gt;'));
        return '%%%M_I_' + idx + '%%%';
      }});
      s = s.replace(/</g, '&lt;').replace(/>/g, '&gt;');
      for (let i = 0; i < math.length; i++) {{
        s = s.split('%%%M_D_' + i + '%%%').join(math[i]);
        s = s.split('%%%M_I_' + i + '%%%').join(math[i]);
      }}
      return s;
    }}

            function renderMath(targetEl) {{
      const el = targetEl || document.body;
      const doRender = () => {{
        if (window.renderMathInElement) {{
          try {{
            renderMathInElement(el, {{
              delimiters: [
                {{ left: '$$', right: '$$', display: true }},
                {{ left: '$', right: '$', display: false }},
                {{ left: String.fromCharCode(92) + '[', right: String.fromCharCode(92) + ']', display: true }},
                {{ left: String.fromCharCode(92) + '(', right: String.fromCharCode(92) + ')', display: false }}
              ],
              ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
              throwOnError: false,
              strict: false
            }});
          }} catch(err) {{
            console.warn('KaTeX render warning:', err);
          }}
        }}
      }};

      if (window.renderMathInElement) {{
        doRender();
      }} else {{
        let count = 0;
        const it = setInterval(() => {{
          count++;
          if (window.renderMathInElement) {{
            clearInterval(it);
            doRender();
          }} else if (count > 30) {{
            clearInterval(it);
          }}
        }}, 60);
      }}
    }}

    // Navigation
    function jumpToQuestion(idx) {{
      if (idx >= 0 && idx < EXAM.questions.length) {{
        currentIndex = idx;
        renderCenter();
        renderSidebar();
        renderInspector();
      }}
    }}

    function nextQuestion() {{
      if (currentIndex < EXAM.questions.length - 1) {{
        jumpToQuestion(currentIndex + 1);
      }}
    }}

    function prevQuestion() {{
      if (currentIndex > 0) {{
        jumpToQuestion(currentIndex - 1);
      }}
    }}

    // Selection & Verdict
    function selectOption(key) {{
      const q = EXAM.questions[currentIndex];
      const isCorrect = (key === q.answer);
      answers[q.id] = {{
        selected: key,
        verdict: isCorrect ? 'AC' : 'WA',
        points: isCorrect ? q.points : 0,
        timestamp: new Date().toLocaleTimeString()
      }};
      saveState();
      editorialOpen[q.id] = true;
      renderCenter();
      renderSidebar();
      renderInspector();
      renderHeaderStats();
    }}

    // Toggle Editorial
    function toggleEditorialManual() {{
      const q = EXAM.questions[currentIndex];
      editorialOpen[q.id] = !editorialOpen[q.id];
      renderCenter();
      if (editorialOpen[q.id]) {{
        setTimeout(() => {{
          const card = document.querySelector('.editorial-card');
          if (card) card.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}, 50);
      }}
    }}

    // Render Stats (Phân định rạch ròi Graded vs Essay - P0-2)
    function renderHeaderStats() {{
      let gradedPts = 0;
      let essaySelfPts = 0;
      let acCount = 0;
      let waCount = 0;
      let answeredCount = 0;

      const maxGradedPts = EXAM.questions.filter(q => q.type !== 'essay').reduce((acc, q) => acc + (q.points || 0), 0);
      const maxEssayPts = EXAM.questions.filter(q => q.type === 'essay').reduce((acc, q) => acc + (q.points || 0), 0);

      EXAM.questions.forEach(q => {{
        const a = answers[q.id];
        if (a) {{
          if (q.type === 'essay') {{
            if (a.selfScore !== undefined || (a.text && a.text.trim())) {{
              answeredCount++;
              if (a.selfScore !== undefined) {{
                essaySelfPts += a.selfScore;
              }}
            }}
          }} else {{
            if (a.selected || a.codeSubmitted) {{
              answeredCount++;
              if (q.type === 'code') {{
                const codePts = a.selfScore !== undefined ? a.selfScore : (a.points !== undefined ? a.points : 0);
                gradedPts += codePts;
                if (codePts === q.points) {{
                  acCount++;
                }} else if (codePts === 0) {{
                  waCount++;
                }}
              }} else {{
                if (a.verdict === 'AC') {{
                  acCount++;
                  gradedPts += q.points;
                }} else if (a.verdict === 'WA') {{
                  waCount++;
                }}
              }}
            }}
          }}
        }}
      }});

      const tickerTotalScoreEl = document.getElementById('tickerTotalScore');
      if (tickerTotalScoreEl) {{
        tickerTotalScoreEl.textContent = `${{gradedPts.toFixed(1)}} / ${{maxGradedPts.toFixed(1)}}đ`;
      }}
      const tickerAcCountEl = document.getElementById('tickerAcCount');
      if (tickerAcCountEl) {{
        tickerAcCountEl.textContent = `${{acCount}} AC`;
      }}
      const tickerWaCountEl = document.getElementById('tickerWaCount');
      if (tickerWaCountEl) {{
        tickerWaCountEl.textContent = `${{waCount}} WA`;
      }}
      const tickerEssayScoreEl = document.getElementById('tickerEssayScore');
      if (tickerEssayScoreEl) {{
        if (maxEssayPts > 0) {{
          tickerEssayScoreEl.style.display = 'inline-block';
          tickerEssayScoreEl.textContent = `Tự luận: ${{essaySelfPts.toFixed(1)}}/${{maxEssayPts.toFixed(1)}}đ`;
        }} else {{
          tickerEssayScoreEl.style.display = 'none';
        }}
      }}

      const pct = Math.round((answeredCount / EXAM.questions.length) * 100);
      const footerProgressLabelEl = document.getElementById('footerProgressLabel');
      if (footerProgressLabelEl) {{
        footerProgressLabelEl.textContent = `Tiến độ: ${{answeredCount}}/${{EXAM.questions.length}} (${{pct}}%) · Graded: ${{gradedPts.toFixed(1)}}/${{maxGradedPts.toFixed(1)}}đ · Tự luận: ${{essaySelfPts.toFixed(1)}}/${{maxEssayPts.toFixed(1)}}đ`;
      }}
    }}

            // Format Explanation into 4 Beautiful Blocks
    function formatExplanationHtml(expText) {{
      if (!expText) return '<div class="eli5-block" style="color:var(--text-muted); font-style:italic;">Đang cập nhật lời giải chi tiết.</div>';

      function safeMdToHtml(str) {{
        if (!str) return '';
        const mathBlocks = [];
        
        // 1. Protect Display Math: $$...$$
        let s = str.replace(/\$\$([\s\S]*?)\$\$/g, (m) => {{
          const idx = mathBlocks.length;
          const safeM = m.replace(/</g, '&lt;').replace(/>/g, '&gt;');
          mathBlocks.push(safeM);
          return '%%%MATH_DISP_' + idx + '%%%';
        }});

        // 2. Protect Inline Math: $...$
        s = s.replace(/\$([^\$\\r\\n]+?)\$/g, (m) => {{
          const idx = mathBlocks.length;
          const safeM = m.replace(/</g, '&lt;').replace(/>/g, '&gt;');
          mathBlocks.push(safeM);
          return '%%%MATH_INL_' + idx + '%%%';
        }});

        // Escape < and > in regular text to prevent broken HTML tags (e.g. 10 > 0 và 90 < 100)
        s = s.replace(/</g, '&lt;').replace(/>/g, '&gt;');

        // 3. Bold & Code
        s = s.replace(/\*\*([^\*]+)\*\*/g, '<strong>$1</strong>');
        s = s.replace(/`([^`]+)`/g, '<code style="background:rgba(255,255,255,0.08); padding:1px 5px; border-radius:3px; font-family:var(--font-mono); font-size:12px; color:#f0b90b;">$1</code>');

        const lines = s.split(String.fromCharCode(10));
        let inList = false;
        let res = [];
        for (let line of lines) {{
          let trimmed = line.trim();
          if (!trimmed) {{
            if (inList) {{ res.push('</ul>'); inList = false; }}
            continue;
          }}
          if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {{
            if (!inList) {{
              res.push('<ul style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
              inList = true;
            }}
            res.push('<li style="margin-bottom:4px;">' + trimmed.substring(2) + '</li>');
          }} else if (/^\d+\.\s/.test(trimmed)) {{
            if (!inList) {{
              res.push('<ol style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
              inList = true;
            }}
            res.push('<li style="margin-bottom:4px;">' + trimmed.replace(/^\d+\.\s*/, '') + '</li>');
          }} else {{
            if (inList) {{
              res.push('</ul>');
              inList = false;
            }}
            res.push('<p style="margin:6px 0; line-height:1.7;">' + trimmed + '</p>');
          }}
        }}
        if (inList) res.push('</ul>');
        
        let outHtml = res.join('');
        for (let i = 0; i < mathBlocks.length; i++) {{
          outHtml = outHtml.split('%%%MATH_DISP_' + i + '%%%').join(mathBlocks[i]);
          outHtml = outHtml.split('%%%MATH_INL_' + i + '%%%').join(mathBlocks[i]);
        }}
        return outHtml;
      }}

      // Chuẩn hóa phân tách theo Markdown ### 1., ### 2., ### 3., ### 4.
      if (expText.indexOf('### 1.') !== -1 || expText.indexOf('### 2.') !== -1 || expText.indexOf('### 3.') !== -1) {{
        const rawParts = expText.split('### ');
        let out = '';
        for (let i = 1; i < rawParts.length; i++) {{
          const part = rawParts[i].trim();
          if (!part) continue;
          let header = '';
          let body = '';
          const nlIdx = part.indexOf(String.fromCharCode(10));
          if (nlIdx !== -1) {{
            header = part.substring(0, nlIdx).trim();
            body = part.substring(nlIdx + 1).trim();
          }} else {{
            header = part;
          }}

          let cls = 'eli5-block';
          let titleColor = '#60a5fa';
          let icon = '👶';
          if (header.indexOf('1.') !== -1 || header.toLowerCase().indexOf('eli5') !== -1) {{
            cls = 'eli5-block';
            titleColor = '#60a5fa';
            icon = '👶';
          }} else if (header.indexOf('2.') !== -1 || header.toLowerCase().indexOf('toán') !== -1 || header.toLowerCase().indexOf('đạo hàm') !== -1 || header.toLowerCase().indexOf('chứng minh') !== -1) {{
            cls = 'eli5-block math';
            titleColor = '#34d399';
            icon = '📐';
          }} else if (header.indexOf('3.') !== -1 || header.toLowerCase().indexOf('bẫy') !== -1 || header.toLowerCase().indexOf('sai') !== -1) {{
            cls = 'eli5-block trap';
            titleColor = '#fbbf24';
            icon = '⚠️';
          }} else if (header.indexOf('4.') !== -1 || header.toLowerCase().indexOf('mắt xích') !== -1 || header.toLowerCase().indexOf('căn cứ') !== -1 || header.toLowerCase().indexOf('lý thuyết') !== -1 || header.toLowerCase().indexOf('liên hệ') !== -1) {{
            cls = 'eli5-block ref';
            titleColor = '#a78bfa';
            icon = '📚';
          }}

          out += '<div class="' + cls + '" style="margin-top:10px;">' +
            '<div style="font-weight:700; color:' + titleColor + '; margin-bottom:6px;">' + icon + ' [' + header + ']</div>' +
            '<div style="font-size:13px; line-height:1.7;">' + safeMdToHtml(body) + '</div>' +
          '</div>';
        }}
        return out || '<div class="eli5-block">' + safeMdToHtml(expText) + '</div>';
      }}

      return '<div class="eli5-block">' + safeMdToHtml(expText) + '</div>';
    }}

    // Render Center Viewport
    function renderCenter() {{
      const vp = document.getElementById('problemViewport');
      const q = EXAM.questions[currentIndex];
      const ans = answers[q.id] || {{}};
      const isEditorialOpen = !!editorialOpen[q.id] || !!ans.selected;

      let html = `
        <div class="problem-header-card">
          <div class="problem-title-row">
            <span class="problem-id-badge">Problem ${{q.id}}.</span>
            <h1 class="problem-title">${{q.cpTitle || q.id}}</h1>
          </div>

          <div class="problem-meta-row">
            <div class="meta-item"><span>Thời gian:</span> <span class="meta-val">2.0s</span></div>
            <div class="meta-item"><span>Bộ nhớ:</span> <span class="meta-val">256 MB</span></div>
            <div class="meta-item"><span>Thang điểm:</span> <span class="meta-val" style="color:#f0b90b; font-weight:700;">${{q.points}} điểm</span></div>
            <div class="meta-item"><span>Phân hệ:</span> <span class="meta-val">Module ${{q.module}}</span></div>
            <div class="meta-item"><span>Dạng câu:</span> <span class="meta-val">${{q.type === 'mcq' ? 'Trắc nghiệm bản chất' : q.type === 'code' ? 'Lập trình thuật toán' : 'Tự luận giải pháp AI'}}</span></div>
          </div>
        </div>

        <div class="statement-section">
          <div class="section-title">Problem Statement</div>
          <div class="statement-text">${{sanitizeTex(q.prompt)}}</div>
          ${{q.image ? `<div class="statement-image-box" style="margin:16px 0; text-align:center;"><img src="${{q.image}}" alt="Hình minh họa" style="max-width:100%; max-height:380px; border-radius:8px; border:1px solid var(--border-subtle); background:#ffffff; padding:6px; box-shadow:0 4px 12px rgba(0,0,0,0.4);" /></div>` : ''}}
        </div>
      `;

      if (q.type === 'mcq') {{
        html += `<div class="options-grid">`;
        (q.options || []).forEach(opt => {{
          let cls = 'cp-option-card';
          if (ans.selected === opt.key) {{
            cls += ' selected';
            cls += (opt.key === q.answer ? ' correct' : ' wrong');
          }} else if (ans.selected && opt.key === q.answer) {{
            cls += ' correct';
          }}

          html += `
            <div class="${{cls}}" onclick="selectOption('${{opt.key}}')">
              <div class="option-key-badge">${{opt.key}}</div>
              <div class="option-text-content">${{sanitizeTex(opt.text)}}</div>
            </div>
          `;
        }});
        html += `</div>`;

        if (ans.selected) {{
          const isAC = (ans.selected === q.answer);
          html += `
            <div class="verdict-banner ${{isAC ? 'ac' : 'wa'}}">
              <div class="verdict-title">
                ${{isAC ? '✓ JUDGE VERDICT: ACCEPTED (AC)' : `✗ JUDGE VERDICT: WRONG ANSWER (WA) — Đáp án chính xác là: ${{q.answer}}`}}
              </div>
              <div class="verdict-meta">
                Điểm số: ${{isAC ? `+${{q.points}}đ` : '0.0đ'}} · Thời gian suy luận: 0.04s · Nộp lúc: ${{ans.timestamp || 'Vừa xong'}}
              </div>
            </div>
          `;
        }}

        // Official Editorial
        html += `
          <div class="editorial-card">
            <div class="editorial-header" onclick="toggleEditorialManual()">
              <div class="editorial-title">
                <span>📖 LỜI GIẢI THAM KHẢO & PHÂN TÍCH CHI TIẾT (ELI5 + STEP-BY-STEP)</span>
              </div>
              <span style="font-size:11px; color:var(--text-muted);">${{isEditorialOpen ? 'Thu gọn ▲' : 'Xem chi tiết ▼'}}</span>
            </div>
            ${{isEditorialOpen ? `
              <div class="editorial-body">
                ${{formatExplanationHtml(q.explanation)}}
              </div>
            ` : ''}}
          </div>
        `;

      }} else if (q.type === 'code') {{
        html += `
          <div class="statement-section">
            <div class="section-title">PYTHON / PYTORCH WORKBENCH</div>
            <textarea style="width:100%; height:180px; background:#07090e; color:#a5d6ff; font-family:var(--font-mono); padding:10px; border:1px solid var(--border-strong); border-radius:4px;" id="codeInput_${{q.id}}">${{ans.code || '# Viết mã nguồn Python / PyTorch tại đây...'}}</textarea>
            <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:11px; color:var(--text-muted);">Môi trường ghi nhận mã nguồn · Tự đối chiếu giải pháp mẫu</span>
              <button class="btn btn-primary" onclick="runCustomCode('${{q.id}}')">💾 Lưu & Đối Chiếu Giải Pháp</button>
            </div>
          </div>
          <div class="editorial-card">
            <div class="editorial-header" onclick="toggleEditorialManual()">
              <div class="editorial-title"><span>📖 BÀI GIẢI MẪU THAM KHẢO & TEST CASES MINH HỌA</span></div>
              <span style="font-size:11px; color:var(--text-muted);">${{isEditorialOpen ? 'Thu gọn ▲' : 'Xem chi tiết ▼'}}</span>
            </div>
            ${{isEditorialOpen ? `
              <div class="editorial-body">
                <pre style="background:#07090e; padding:12px; border-radius:4px; font-family:var(--font-mono); font-size:12px; color:#93c5fd; overflow-x:auto;">${{q.modelAnswer || ''}}</pre>
              </div>
            ` : ''}}
          </div>
        `;

      }} else {{
        html += `
          <div class="statement-section">
            <div class="section-title">KHÔNG GIAN TRÌNH BÀY BÀI TỰ LUẬN GIẢI PHÁP AI</div>
            <textarea style="width:100%; height:220px; background:#07090e; color:#f1f5f9; font-family:var(--font-sans); padding:12px; border:1px solid var(--border-strong); border-radius:4px; font-size:13px; line-height:1.6;" id="essayInput_${{q.id}}" placeholder="Trình bày luận điểm 5 bước: 1. Phân tích bài toán -> 2. Thiết kế mô hình -> 3. Pipeline chống leakage -> 4. Metrics -> 5. Mở rộng...">${{ans.text || ''}}</textarea>
            <div style="margin-top:10px; display:flex; justify-content:space-between;">
              <button class="btn" onclick="insertEssayTemplate('${{q.id}}')">Nạp khung mẫu 5 bước chuẩn</button>
              <button class="btn btn-primary" onclick="runEssayKeywordCheck('${{q.id}}')">⚡ Gợi Ý Kiểm Tra Từ Khóa Rubric</button>
            </div>
          </div>
          <div class="editorial-card">
            <div class="editorial-header" onclick="toggleEditorialManual()">
              <div class="editorial-title"><span>📖 BÀI GIẢI MẪU THAM KHẢO (KHUNG 5 BƯỚC)</span></div>
              <span style="font-size:11px; color:var(--text-muted);">${{isEditorialOpen ? 'Thu gọn ▲' : 'Xem chi tiết ▼'}}</span>
            </div>
            ${{isEditorialOpen ? `
              <div class="editorial-body" style="white-space:pre-wrap;">${{q.modelAnswer || ''}}</div>
            ` : ''}}
          </div>
        `;
      }}

      vp.innerHTML = html;
      renderMath(vp);
    }}

    // Render Left Sidebar
    function renderSidebar() {{
      const container = document.getElementById('sidebarContent');

      if (sidebarTab === 'grid') {{
        const answeredCount = Object.keys(answers).filter(k => answers[k] && (answers[k].selected || (answers[k].text && answers[k].text.trim()) || answers[k].codePassed)).length;
        const total = EXAM.questions.length;
        const pct = Math.round((answeredCount / total) * 100);

        let html = `
          <div class="contest-progress-box">
            <div class="prog-text">
              <span>TIẾN ĐỘ THI ĐẤU</span>
              <strong>${{answeredCount}}/${{total}} (${{pct}}%)</strong>
            </div>
            <div class="prog-track">
              <div class="prog-bar" style="width:${{pct}}%;"></div>
            </div>
          </div>

          <div class="problem-filter-row">
            <button class="filter-btn ${{filterModule === 'all' ? 'active' : ''}}" onclick="setFilter('all')">Tất cả (${{total}})</button>
            <button class="filter-btn ${{filterModule === 'A' ? 'active' : ''}}" onclick="setFilter('A')">Mod A</button>
            <button class="filter-btn ${{filterModule === 'B' ? 'active' : ''}}" onclick="setFilter('B')">Mod B</button>
            <button class="filter-btn ${{filterModule === 'C' ? 'active' : ''}}" onclick="setFilter('C')">Mod C</button>
            <button class="filter-btn ${{filterModule === 'ac' ? 'active' : ''}}" onclick="setFilter('ac')">AC</button>
            <button class="filter-btn ${{filterModule === 'wa' ? 'active' : ''}}" onclick="setFilter('wa')">WA</button>
          </div>

          <div class="cp-matrix-grid">
        `;

        EXAM.questions.forEach((q, idx) => {{
          const a = answers[q.id];
          let statusCls = '';
          if (a) {{
            if (q.type === 'code') {{
              const codePts = a.selfScore !== undefined ? a.selfScore : 0;
              if (codePts === q.points) statusCls = 'ac';
              else if (codePts > 0) statusCls = 'partial';
              else if (a.codeSubmitted) statusCls = 'wa';
            }} else {{
              if (a.verdict === 'AC') statusCls = 'ac';
              else if (a.verdict === 'WA') statusCls = 'wa';
              else if (a.selected || (a.text && a.text.trim()) || a.codePassed) statusCls = 'ac';
            }}
          }}
          if (idx === currentIndex) statusCls += ' active';

          // Bộ lọc
          if (filterModule === 'A' && q.module !== 'A') return;
          if (filterModule === 'B' && q.module !== 'B') return;
          if (filterModule === 'C' && q.module !== 'C') return;
          if (filterModule === 'ac' && (!a || a.verdict !== 'AC')) return;
          if (filterModule === 'wa' && (!a || a.verdict !== 'WA')) return;

          const shortLabel = q.id.split('-').pop();
          html += `
            <div class="matrix-item ${{statusCls}}" onclick="jumpToQuestion(${{idx}})" title="${{q.cpTitle || q.id}}">
              ${{shortLabel}}
            </div>
          `;
        }});

        html += `</div>`;
        container.innerHTML = html;

      }} else if (sidebarTab === 'doc') {{
        let html = `
          <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase;">
            GIÁO TRÌNH 7 CHƯƠNG TRỌNG TÂM
          </div>
          <div style="display:flex; flex-direction:column; gap:6px;">
        `;
        [
          {{ id: '§1', title: 'Chương 1: Machine Learning Cổ Điển' }},
          {{ id: '§2', title: 'Chương 2: Deep Learning & PyTorch' }},
          {{ id: '§3', title: 'Chương 3: Thị Giác Máy Tính (CV)' }},
          {{ id: '§4', title: 'Chương 4: Xử Lý Ngôn Ngữ Tự Nhiên (NLP)' }},
          {{ id: '§5', title: 'Chương 5: Xác Suất & Thống Kê' }},
          {{ id: '§6', title: 'Chương 6: Bảng 24 Bẫy Đề Thi Kinh Điển' }},
          {{ id: '§7', title: 'Chương 7: Bài Toán Thực Chiến OLP AI' }}
        ].forEach(ch => {{
          html += `
            <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:10px; border-radius:4px; cursor:pointer;" onclick="openChapterTheory('${{ch.id}}')">
              <div style="font-weight:700; font-size:12px; color:#93c5fd;">${{ch.title}}</div>
              <div style="font-size:10.5px; color:var(--text-muted); margin-top:3px;">Nhấn để xem lý thuyết & công thức chi tiết ↗</div>
            </div>
          `;
        }});
        html += `</div>`;

        // Danh mục Khóa học OLP Sinh Viên (16 Buổi)
        const olpLessons = (COURSES && COURSES.olp_course && COURSES.olp_course.lessons) ? COURSES.olp_course.lessons : [];
        if (olpLessons.length > 0) {{
          html += `
            <div style="font-size:11px; font-weight:700; color:#f0b90b; text-transform:uppercase; margin-top:16px; margin-bottom:6px; display:flex; align-items:center; gap:6px;">
              <span>🎓</span> KHÓA HỌC OLP SINH VIÊN (16 BUỔI)
            </div>
            <div style="display:flex; flex-direction:column; gap:6px;">
          `;
          olpLessons.forEach(ls => {{
            const hasVid = Boolean(ls.videoIframe);
            const hasSlide = Boolean(ls.slide);
            const hasLab = Boolean(ls.lab);
            const hasTrans = Boolean(ls.transcript);
            const safeTitle = (ls.title || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');

            html += `
              <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:8px 10px; border-radius:4px;">
                <div style="font-size:11.5px; font-weight:600; color:#e2e8f0; line-height:1.4;">${{ls.title}}</div>
                ${{ls.date ? `<div style="font-size:10px; color:var(--text-muted); margin-top:2px;">📅 ${{ls.date}}</div>` : ''}}
                <div style="display:flex; flex-wrap:wrap; gap:4px; margin-top:6px;">
                  ${{hasVid ? `<button type="button" class="btn" style="height:22px; font-size:10px; padding:0 6px; background:rgba(240,185,11,0.15); color:#f0b90b; border:1px solid rgba(240,185,11,0.3);" onclick="playCourseVideo('${{ls.videoIframe}}', '${{safeTitle}}')">▶ Video</button>` : ''}}
                  ${{hasSlide ? `<a href="${{ls.slide}}" target="_blank" class="btn" style="height:22px; font-size:10px; padding:0 6px; text-decoration:none; display:inline-flex; align-items:center;" title="Mở Slide Drive">📑 Slide</a>` : ''}}
                  ${{hasLab ? `<a href="${{ls.lab}}" target="_blank" class="btn" style="height:22px; font-size:10px; padding:0 6px; text-decoration:none; display:inline-flex; align-items:center;" title="Mở Lab Code Drive">💻 Lab</a>` : ''}}
                  ${{hasTrans ? `<a href="${{ls.transcript}}" target="_blank" class="btn" style="height:22px; font-size:10px; padding:0 6px; text-decoration:none; display:inline-flex; align-items:center;" title="Mở Transcript Docs">📝 Docs</a>` : ''}}
                </div>
              </div>
            `;
          }});
          html += `</div>`;
        }}

        container.innerHTML = html;

      }} else if (sidebarTab === 'sub') {{
        let html = `
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase;">
              LỊCH SỬ BÀI THI & NỘP BÀI
            </div>
            <button class="btn" style="height:20px; font-size:10px; padding:0 6px;" onclick="fetchSubmissionsHistory()" title="Đồng bộ lại từ Server">🔄 Đồng bộ</button>
          </div>
        `;

        if (!currentUser) {{
          html += `
            <div style="background:rgba(59,130,246,0.1); border:1px solid rgba(59,130,246,0.3); border-radius:4px; padding:10px; margin-bottom:10px;">
              <div style="font-size:11.5px; font-weight:600; color:#93c5fa; margin-bottom:4px;">🔑 Lưu bài nộp vào tài khoản</div>
              <div style="font-size:10.5px; color:#cbd5e1; line-height:1.4; margin-bottom:8px;">
                Đăng nhập để lưu vĩnh viễn kết quả vào cơ sở dữ liệu server và xếp hạng Leaderboard.
              </div>
              <button class="btn btn-primary" style="height:26px; font-size:11px; width:100%; justify-content:center; background:linear-gradient(135deg, #2563eb, #1d4ed8); color:#fff; border:none;" onclick="openAuthModal()">
                Đăng nhập / Đăng ký ngay
              </button>
            </div>
          `;
        }}

        // Danh sách bài nộp từ Server
        if (serverSubmissions && serverSubmissions.length > 0) {{
          html += `
            <div style="font-size:10.5px; font-weight:700; color:#10b981; margin-bottom:6px; display:flex; align-items:center; gap:4px;">
              <span>●</span> KẾT QUẢ ĐÃ LƯU TRÊN SERVER (${{serverSubmissions.length}} BÀI)
            </div>
            <div style="display:flex; flex-direction:column; gap:6px; margin-bottom:12px;">
          `;
          serverSubmissions.forEach(sub => {{
            const accPct = Math.round((sub.score / (sub.max_score || 100)) * 100);
            const scoreColor = accPct >= 80 ? '#34d399' : (accPct >= 50 ? '#fbbf24' : '#f87171');
            html += `
              <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:10px; border-radius:5px; display:flex; flex-direction:column; gap:4px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                  <span style="font-size:11px; font-weight:700; color:#93c5fd; font-family:var(--font-mono);">${{sub.exam_id.toUpperCase()}}</span>
                  <span style="font-family:var(--font-mono); font-size:13px; font-weight:800; color:${{scoreColor}};">${{sub.score.toFixed(1)}}/${{sub.max_score.toFixed(1)}}đ</span>
                </div>
                <div style="font-size:11px; color:#e2e8f0; font-weight:600;">${{sub.exam_title || sub.exam_id}}</div>
                <div style="font-size:10px; color:var(--text-muted); display:flex; justify-content:space-between; margin-top:2px;">
                  <span>Đúng: <strong>${{sub.correct_count}}/${{sub.total_questions}} câu</strong> (${{accPct}}%)</span>
                  <span>${{sub.submitted_at ? sub.submitted_at.replace('T', ' ').substring(0, 16) : ''}}</span>
                </div>
              </div>
            `;
          }});
          html += `</div>`;
        }}

        // Tiến độ chi tiết từng câu trong phiên làm bài hiện tại
        html += `
          <div style="font-size:10.5px; font-weight:700; color:var(--text-muted); margin-bottom:4px; margin-top:6px;">
            CHI TIẾT PHIÊN LÀM BÀI HIỆN TẠI
          </div>
          <div style="display:flex; flex-direction:column; gap:5px;">
        `;
        const ansKeys = Object.keys(answers);
        if (ansKeys.length === 0) {{
          html += `<div style="font-size:11px; color:var(--text-muted); font-style:italic;">Chưa có câu hỏi nào được trả lời trong phiên này.</div>`;
        }} else {{
          ansKeys.forEach(k => {{
            const a = answers[k];
            const q = EXAM.questions.find(item => item.id === k);
            const isEssay = q && q.type === 'essay';
            const isCode = q && q.type === 'code';
            let statusText = a.verdict || 'DONE';
            let statusColor = (a.verdict === 'AC') ? 'var(--color-ac)' : 'var(--color-wa)';
            if (isEssay) {{
              statusText = (a.selfScore !== undefined) ? `${{a.selfScore.toFixed(1)}}đ (Tự chấm)` : 'Đã nộp';
              statusColor = '#60a5fa';
            }} else if (isCode) {{
              const codePts = a.selfScore !== undefined ? a.selfScore : (a.points !== undefined ? a.points : 0);
              statusText = `${{codePts.toFixed(1)}}/${{q.points}}.0đ (${{a.verdict || (codePts === q.points ? 'AC' : codePts > 0 ? 'PARTIAL' : 'WA')}})`;
              statusColor = (codePts === q.points) ? 'var(--color-ac)' : (codePts > 0 ? '#fbbf24' : 'var(--color-wa)');
            }}
            html += `
              <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:6px 9px; border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <strong style="color:#60a5fa; font-family:var(--font-mono); font-size:11px;">${{k}}</strong>
                  <span style="font-size:10px; color:var(--text-muted); margin-left:6px;">${{a.timestamp || ''}}</span>
                </div>
                <span style="font-family:var(--font-mono); font-size:10.5px; font-weight:700; color:${{statusColor}};">
                  ${{statusText}}
                </span>
              </div>
            `;
          }});
        }}
        html += `</div>`;
        container.innerHTML = html;
      }}
    }}

    function setFilter(mod) {{
      filterModule = mod;
      renderSidebar();
    }}

    function switchSidebarTab(tab) {{
      sidebarTab = tab;
      document.querySelectorAll('.s-tab').forEach(t => t.classList.remove('active'));
      if (tab === 'grid') document.getElementById('sTabGrid').classList.add('active');
      if (tab === 'doc') document.getElementById('sTabDoc').classList.add('active');
      if (tab === 'sub') document.getElementById('sTabSub').classList.add('active');
      renderSidebar();
    }}

    // Inspector Tabs Switcher
    function switchInspectorTab(tab) {{
      inspectorTab = tab;
      document.querySelectorAll('.i-tab').forEach(t => t.classList.remove('active'));
      if (tab === 'rubric') document.getElementById('iTabRubric').classList.add('active');
      if (tab === 'explanation') document.getElementById('iTabExplanation').classList.add('active');
      if (tab === 'video') document.getElementById('iTabVideo').classList.add('active');
      if (tab === 'formulas') document.getElementById('iTabFormulas').classList.add('active');
      renderInspector();
    }}

    // Render Right Inspector Content
    function renderInspector() {{
      const container = document.getElementById('inspectorContent');
      const q = EXAM.questions[currentIndex];

      if (inspectorTab === 'rubric') {{
        const evalRes = rubricEvalResults[q.id] || {{ checked: {{}} }};
        const checkedMap = evalRes.checked || {{}};
        const rubricList = q.rubric || [];
        const ptsPerCrit = q.points / Math.max(1, rubricList.length);
        const currentSelfPts = answers[q.id]?.selfScore !== undefined ? answers[q.id].selfScore : (evalRes.score || 0);

        let html = `
          <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:12px; border-radius:var(--radius-sm); display:flex; flex-direction:column; gap:8px;">
            <div style="font-weight:700; font-size:12px; color:#93c5fa;">BẢNG TIÊU CHÍ RUBRIC TỰ ĐỐI CHIẾU</div>
            <p style="font-size:11px; color:var(--text-muted); line-height:1.5;">
              Tự đánh giá giải pháp AI theo khung chuẩn 5 bước. Tích chọn các tiêu chí bạn đã hoàn thiện hoặc nhấn nút "Gợi ý kiểm tra từ khóa" để rà soát tự động.
            </p>
          </div>
        `;

        if (q.type === 'essay') {{
          html += `
            <div style="background:var(--bg-card); border:1px solid var(--border-strong); border-radius:var(--radius-sm); padding:12px; display:flex; flex-direction:column; gap:10px;">
              <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:8px;">
                <span style="font-size:11px; font-weight:700; color:#60a5fa; text-transform:uppercase;">ĐIỂM TỰ ĐÁNH GIÁ:</span>
                <span style="font-family:var(--font-mono); font-size:15px; font-weight:700; color:#10b981;">${{currentSelfPts.toFixed(1)}} / ${{q.points}}.0đ</span>
              </div>

              <div style="display:flex; flex-direction:column; gap:8px;">
                ${{rubricList.map((r, idx) => {{
                  const isChecked = !!checkedMap[idx];
                  return `
                    <div style="display:flex; align-items:flex-start; gap:8px; padding:8px; border-radius:4px; background:${{isChecked ? 'rgba(16,185,129,0.08)' : 'rgba(0,0,0,0.2)'}}; border:1px solid ${{isChecked ? 'rgba(16,185,129,0.3)' : 'var(--border-subtle)'}}; cursor:pointer;" onclick="toggleRubricCriterion('${{q.id}}', ${{idx}})">
                      <input type="checkbox" style="margin-top:2px; cursor:pointer;" ${{isChecked ? 'checked' : ''}} onclick="event.stopPropagation(); toggleRubricCriterion('${{q.id}}', ${{idx}})">
                      <div style="flex:1;">
                        <div style="font-size:11.5px; font-weight:600; color:${{isChecked ? '#34d399' : 'var(--text-secondary)'}}; line-height:1.4;">
                          ${{sanitizeTex(r)}}
                        </div>
                        <div style="font-size:10px; color:var(--text-muted); margin-top:2px;">
                          ${{isChecked ? `✓ Đạt (+${{ptsPerCrit.toFixed(1)}}đ)` : `Chưa tích (+0.0đ / tối đa ${{ptsPerCrit.toFixed(1)}}đ)`}}
                        </div>
                      </div>
                    </div>
                  `;
                }}).join('')}}
              </div>

              <div style="display:flex; flex-direction:column; gap:6px; margin-top:4px;">
                <button class="btn btn-primary" style="justify-content:center; height:32px; font-size:11.5px;" onclick="runEssayKeywordCheck('${{q.id}}')">
                  ⚡ Gợi ý kiểm tra từ khóa tự động
                </button>
                <div style="font-size:10px; color:var(--text-muted); text-align:center;">
                  (Gợi ý từ khóa hỗ trợ phát hiện nội dung; điểm số do thí sinh tự đối chiếu quyết định)
                </div>
              </div>
            </div>
          `;

          if (evalRes.summary) {{
            html += `
              <div style="background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.25); border-radius:var(--radius-sm); padding:10px; font-size:11px; color:#cbd5e1; line-height:1.5;">
                <strong style="color:#60a5fa;">Nhận xét từ khóa:</strong> ${{evalRes.summary}}
              </div>
            `;
          }}

        }} else if (q.type === 'code') {{
          const curCodePts = answers[q.id]?.selfScore !== undefined ? answers[q.id].selfScore : 0;
          html += `
            <div style="background:var(--bg-card); border:1px solid var(--border-strong); border-radius:var(--radius-sm); padding:12px; display:flex; flex-direction:column; gap:10px;">
              <div style="font-size:11px; font-weight:700; color:#60a5fa; text-transform:uppercase;">ĐỐI CHIẾU MÃ NGUỒN PYTHON (${{q.points}}.0 ĐIỂM)</div>
              <p style="font-size:11px; color:var(--text-muted); line-height:1.5;">
                Môi trường trình duyệt tĩnh không chạy code trực tiếp. Sau khi viết code và xem đáp án mẫu, hãy tự cho điểm mức độ hoàn thiện của bài làm:
              </p>
              <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:4px;">
                ${{[0, 2, 4, 5, 7].map(pt => {{
                  let btnCls = 'btn';
                  if (curCodePts === pt) {{
                    if (pt === q.points) btnCls += ' btn-success';
                    else if (pt > 0) btnCls += ' btn-primary';
                    else btnCls += ' btn-danger';
                  }}
                  return `
                    <button class="${{btnCls}}" style="height:26px; font-size:11px;" onclick="setCodeSelfScore('${{q.id}}', ${{pt}})">
                      ${{pt}}.0đ ${{pt === q.points ? '(Full AC)' : pt === 0 ? '(Chưa làm)' : '(Một phần)'}}
                    </button>
                  `;
                }}).join('')}}
              </div>
              <div style="font-size:10.5px; color:#34d399; margin-top:4px;">
                Điểm hiện tại: <strong>${{curCodePts}}.0 / ${{q.points}}.0đ</strong>
              </div>
            </div>
          `;
        }} else {{
          html += `
            <div style="font-size:11px; color:#34d399; background:rgba(16,185,129,0.08); padding:8px; border-radius:4px; border:1px solid rgba(16,185,129,0.2);">
              ✓ <strong>Tiêu chuẩn trắc nghiệm:</strong> Đúng +${{q.points}}đ, Sai 0.0đ. Phân loại nhận thức: Vận dụng cao / Tính toán bản chất.
            </div>
          `;
        }}

        container.innerHTML = html;

      }} else if (inspectorTab === 'explanation') {{
        // TAB LUẬN GIẢI ĐỒNG BỘ CÂU HỎI
        container.innerHTML = `
          <div style="display:flex; flex-direction:column; gap:10px;">
            <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase;">
              LUẬN GIẢI CHI TIẾT (PROBLEM ${{q.id}})
            </div>
            ${{formatExplanationHtml(q.explanation)}}
          </div>
        `;
        renderMath(container);

      }} else if (inspectorTab === 'video') {{
        // BỘ PHÂN GIẢI VIDEO THÔNG MINH ĐA TẦNG (Smart Context-Aware Video Resolver)
        function resolveVideoForQuestion(question) {{
          if (!question || typeof VIDEOS === 'undefined') return null;
          
          // Tầng 1: Quét ký hiệu §x.y tường minh trong explanation, prompt, hoặc tags
          const textToScan = (question.explanation || '') + ' ' + (question.prompt || '') + ' ' + (question.tags || []).join(' ');
          const secMatch = textToScan.match(/§\s*(\d+\.\d+)/);
          if (secMatch) {{
            const foundSec = '§' + secMatch[1];
            if (VIDEOS[foundSec]) return VIDEOS[foundSec];
          }}

          // Tầng 2: Đối soát theo Tags và Từ khóa học thuật chuyên sâu
          const tags = (question.tags || []).map(t => t.toLowerCase());
          const lowerPrompt = (question.prompt || '').toLowerCase();
          const lowerExp = (question.explanation || '').toLowerCase();
          const allText = lowerPrompt + ' ' + lowerExp + ' ' + tags.join(' ');

          // Nhóm 1: Tác vụ Olympic & Video Contest VOAI
          if (tags.some(t => ['sign-language', 'st-gcn', 'video-ai'].includes(t)) || allText.includes('ngôn ngữ ký hiệu') || allText.includes('st-gcn') || allText.includes('mediapipe') || allText.includes('3d-cnn') || allText.includes('i3d') || allText.includes('slowfast')) {{
            if (VIDEOS['§7.1']) return VIDEOS['§7.1'];
          }}
          if (tags.some(t => ['nmt', 'bpe', 'translation', 'sacrebleu'].includes(t)) || allText.includes('dịch máy') || allText.includes('sacrebleu') || allText.includes('bpe') || allText.includes('bleu') || allText.includes('subword')) {{
            if (VIDEOS['§7.2']) return VIDEOS['§7.2'];
            if (VIDEOS['§4.7']) return VIDEOS['§4.7'];
          }}
          if (tags.some(t => ['tabular', 'shap', 'churn', 'catboost'].includes(t)) || allText.includes('dữ liệu bảng') || allText.includes('shap') || allText.includes('lightgbm') || allText.includes('catboost') || allText.includes('target encoding')) {{
            if (VIDEOS['§7.4']) return VIDEOS['§7.4'];
          }}
          if (tags.some(t => ['yolo', 'object-detection', 'iou', 'nms', 'ciou'].includes(t)) || allText.includes('yolo') || allText.includes('iou') || allText.includes('non-maximum') || allText.includes('nms') || allText.includes('bounding box') || allText.includes('phát hiện đối tượng') || allText.includes('phát hiện vật thể') || allText.includes('ciou')) {{
            if (allText.includes('nano') || allText.includes('mobile') || allText.includes('edge')) {{
              if (VIDEOS['§7.3']) return VIDEOS['§7.3'];
            }}
            if (VIDEOS['§3.6']) return VIDEOS['§3.6'];
          }}
          if (tags.some(t => ['deepfake', 'diffusion', 'gan'].includes(t)) || allText.includes('diffusion') || allText.includes('gan') || allText.includes('kẻ mạo danh') || allText.includes('real vs fake') || allText.includes('tạo ảnh')) {{
            if (VIDEOS['§3.8']) return VIDEOS['§3.8'];
          }}
          if (tags.some(t => ['table-extraction', 'tsr', 'docvqa', 'docvivqa', 'ocr'].includes(t)) || allText.includes('bảng tài liệu') || allText.includes('ocr') || allText.includes('tsr') || allText.includes('docvivqa') || allText.includes('teds')) {{
            if (VIDEOS['§4.1']) return VIDEOS['§4.1'];
          }}

          // Nhóm 2: Kiến trúc Deep Learning & Computer Vision
          if (tags.some(t => ['vit', 'vision-transformer'].includes(t)) || allText.includes('vision transformer') || allText.includes('vit') || allText.includes('patch') || allText.includes('[cls]')) {{
            if (VIDEOS['§3.5']) return VIDEOS['§3.5'];
          }}
          if (tags.some(t => ['transformer', 'attention'].includes(t)) || allText.includes('transformer') || allText.includes('self-attention') || allText.includes('query') || allText.includes('multi-head')) {{
            if (VIDEOS['§4.5']) return VIDEOS['§4.5'];
          }}
          if (tags.some(t => ['u-net', 'segmentation'].includes(t)) || allText.includes('u-net') || allText.includes('semantic segmentation') || allText.includes('phân vùng')) {{
            if (allText.includes('semantic') || allText.includes('instance')) {{
              if (VIDEOS['§3.7']) return VIDEOS['§3.7'];
            }}
            if (VIDEOS['§3.4']) return VIDEOS['§3.4'];
          }}
          if (tags.some(t => ['resnet', 'skip-connection'].includes(t)) || allText.includes('resnet') || allText.includes('skip connection') || allText.includes('residual') || allText.includes('shortcut')) {{
            if (VIDEOS['§3.3']) return VIDEOS['§3.3'];
          }}
          if (allText.includes('conv2d') || allText.includes('tích chập') || allText.includes('receptive field') || allText.includes('stride') || allText.includes('padding')) {{
            if (VIDEOS['§3.1']) return VIDEOS['§3.1'];
          }}
          if (allText.includes('pooling') || allText.includes('max-pooling') || allText.includes('average pooling')) {{
            if (VIDEOS['§3.2']) return VIDEOS['§3.2'];
          }}
          if (allText.includes('transfer learning') || allText.includes('fine-tuning') || allText.includes('backbone') || allText.includes('đóng băng')) {{
            if (VIDEOS['§3.9']) return VIDEOS['§3.9'];
          }}

          // Nhóm 3: Tối ưu hóa & Huấn luyện Mạng
          if (allText.includes('cross-entropy') || allText.includes('bce') || allText.includes('logsoftmax') || allText.includes('hàm loss') || allText.includes('hàm mất mát')) {{
            if (VIDEOS['§2.4']) return VIDEOS['§2.4'];
          }}
          if (allText.includes('adam') || allText.includes('momentum') || allText.includes('rmsprop') || allText.includes('optimizer') || allText.includes('tối ưu hóa')) {{
            if (VIDEOS['§2.5']) return VIDEOS['§2.5'];
          }}
          if (allText.includes('backprop') || allText.includes('autograd') || allText.includes('zero_grad') || allText.includes('backward') || allText.includes('lan truyền ngược')) {{
            if (VIDEOS['§2.3']) return VIDEOS['§2.3'];
          }}
          if (allText.includes('learning rate') || allText.includes('warmup') || allText.includes('scheduler') || allText.includes('cosine annealing')) {{
            if (VIDEOS['§2.6']) return VIDEOS['§2.6'];
          }}
          if (allText.includes('khởi tạo trọng số') || allText.includes('he (kaiming)') || allText.includes('xavier') || allText.includes('weight initialization')) {{
            if (VIDEOS['§2.7']) return VIDEOS['§2.7'];
          }}
          if (allText.includes('batch norm') || allText.includes('batchnorm') || allText.includes('layer norm') || allText.includes('layernorm') || allText.includes('group norm')) {{
            if (VIDEOS['§2.8']) return VIDEOS['§2.8'];
          }}
          if (allText.includes('dropout')) {{
            if (VIDEOS['§2.9']) return VIDEOS['§2.9'];
          }}
          if (allText.includes('vanishing gradient') || allText.includes('triệt tiêu gradient') || allText.includes('bùng nổ gradient')) {{
            if (VIDEOS['§2.10']) return VIDEOS['§2.10'];
          }}
          if (allText.includes('relu') || allText.includes('sigmoid') || allText.includes('softmax') || allText.includes('gelu') || allText.includes('hàm kích hoạt')) {{
            if (VIDEOS['§2.2']) return VIDEOS['§2.2'];
          }}
          if (allText.includes('mạng nơ-ron') || allText.includes('neural network') || allText.includes('neuron')) {{
            if (VIDEOS['§2.1']) return VIDEOS['§2.1'];
          }}

          // Nhóm 4: NLP & Chuỗi
          if (allText.includes('bert') || allText.includes('gpt') || allText.includes('llm') || allText.includes('kv-cache')) {{
            if (VIDEOS['§4.6']) return VIDEOS['§4.6'];
          }}
          if (allText.includes('lstm') || allText.includes('gru') || allText.includes('rnn') || allText.includes('chuỗi thời gian') || allText.includes('time-series')) {{
            if (VIDEOS['§4.4']) return VIDEOS['§4.4'];
          }}
          if (allText.includes('cosine similarity') || allText.includes('độ tương đồng')) {{
            if (VIDEOS['§4.3']) return VIDEOS['§4.3'];
          }}
          if (allText.includes('word2vec') || allText.includes('fasttext') || allText.includes('word embedding')) {{
            if (VIDEOS['§4.2']) return VIDEOS['§4.2'];
          }}
          if (allText.includes('token') || allText.includes('lemmatization') || allText.includes('stemming') || allText.includes('tiền xử lý văn bản')) {{
            if (VIDEOS['§4.1']) return VIDEOS['§4.1'];
          }}

          // Nhóm 5: Toán & Xác suất Thống kê
          if (allText.includes('bayes') || allText.includes('tiền nghiệm') || allText.includes('hậu nghiệm') || allText.includes('base rate')) {{
            if (VIDEOS['§5.1']) return VIDEOS['§5.1'];
          }}
          if (allText.includes('phương sai') || allText.includes('kỳ vọng') || allText.includes('var(') || allText.includes('variance')) {{
            if (VIDEOS['§5.3']) return VIDEOS['§5.3'];
          }}
          if (allText.includes('phân phối') || allText.includes('gaussian') || allText.includes('clt') || allText.includes('giới hạn trung tâm')) {{
            if (VIDEOS['§5.2']) return VIDEOS['§5.2'];
          }}
          if (allText.includes('mle') || allText.includes('map') || allText.includes('hợp lý cực đại')) {{
            if (VIDEOS['§5.4']) return VIDEOS['§5.4'];
          }}
          if (allText.includes('p-value') || allText.includes('kiểm định giả thuyết') || allText.includes('mức ý nghĩa')) {{
            if (VIDEOS['§5.5']) return VIDEOS['§5.5'];
          }}
          if (allText.includes('tương quan') || allText.includes('nhân quả') || allText.includes('causation') || allText.includes('confounder')) {{
            if (VIDEOS['§5.6']) return VIDEOS['§5.6'];
          }}

          // Nhóm 6: Học máy Cổ điển
          if (allText.includes('precision') || allText.includes('recall') || allText.includes('f1') || allText.includes('roc') || allText.includes('confusion matrix') || allText.includes('pr-auc')) {{
            if (VIDEOS['§1.7']) return VIDEOS['§1.7'];
          }}
          if (allText.includes('svm') || allText.includes('rbf') || allText.includes('support vector')) {{
            if (VIDEOS['§1.2']) return VIDEOS['§1.2'];
          }}
          if (allText.includes('decision tree') || allText.includes('cây quyết định') || allText.includes('entropy') || allText.includes('information gain')) {{
            if (VIDEOS['§1.3']) return VIDEOS['§1.3'];
          }}
          if (allText.includes('random forest') || allText.includes('bagging') || allText.includes('bootstrap')) {{
            if (VIDEOS['§1.4']) return VIDEOS['§1.4'];
          }}
          if (allText.includes('k-means') || allText.includes('silhouette') || allText.includes('phân cụm')) {{
            if (VIDEOS['§1.8']) return VIDEOS['§1.8'];
          }}
          if (allText.includes('smote') || allText.includes('mất cân bằng')) {{
            if (VIDEOS['§1.9']) return VIDEOS['§1.9'];
          }}
          if (allText.includes('lasso') || allText.includes('ridge') || allText.includes('regularization') || allText.includes('l1') || allText.includes('l2')) {{
            if (VIDEOS['§1.6']) return VIDEOS['§1.6'];
          }}
          if (allText.includes('broadcasting') || allText.includes('numpy')) {{
            if (VIDEOS['§1.10']) return VIDEOS['§1.10'];
          }}

          // Tầng 3: Phân loại theo Module của đề thi
          if (question.module === 'C') return VIDEOS['§3.3'] || VIDEOS['§4.5'];
          if (question.module === 'B') return VIDEOS['§2.3'] || VIDEOS['§2.5'];
          if (question.module === 'A') return VIDEOS['§1.5'] || VIDEOS['§5.1'];

          return VIDEOS['§1.1'];
        }}

        const vid = resolveVideoForQuestion(q) || VIDEOS['§1.1'] || {{
          sectionId: '§1.1',
          title: 'Machine Learning Fundamentals',
          channel: 'VietAI / StatQuest',
          youtubeId: 'HVXime0nQeI',
          startSeconds: 135,
          timestampLabel: '02:15',
          highlightNote: 'Nắm vững bản chất thuật toán và cách chọn siêu tham số tối ưu.'
        }};

        const ytDirectUrl = 'https://www.youtube.com/watch?v=' + vid.youtubeId + '&t=' + vid.startSeconds + 's';
        const cleanTitle = (vid.title || 'Bài giảng OLP AI').replace(/'/g, "\\'").replace(/"/g, '&quot;');
        const isFileProtocol = window.location.protocol === 'file:';

        let fileProtocolAlertHtml = '';
        if (isFileProtocol) {{
          fileProtocolAlertHtml = `
            <div style="background:rgba(239,68,68,0.12); border:1px solid rgba(239,68,68,0.35); border-radius:6px; padding:10px; font-size:11.5px; color:#fca5a5; line-height:1.5; display:flex; flex-direction:column; gap:6px; margin-bottom:8px;">
              <div style="font-weight:700; color:#f87171; display:flex; align-items:center; gap:6px;">
                <span>⚠️ Bạn đang mở qua file:/// (YouTube chặn nhúng - Lỗi 153)</span>
              </div>
              <div style="color:#e2e8f0; font-size:11px;">
                Chính sách bảo mật Google YouTube chặn phát nhúng trên file cục bộ (gây <strong>Lỗi 153</strong>). Hãy dùng 1 trong 2 cách sau:
              </div>
              <div style="display:flex; flex-direction:column; gap:5px; margin-top:2px;">
                <a href="http://localhost:8080/olympic_ai_study_hub.html" style="background:#2563eb; color:#fff; padding:6px 10px; border-radius:4px; font-weight:700; font-size:11px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:5px;">
                  🚀 Mở qua Localhost (Xem trực tiếp 100% không lỗi)
                </a>
                <a href="${{ytDirectUrl}}" target="_blank" style="background:#f59e0b; color:#000; padding:6px 10px; border-radius:4px; font-weight:700; font-size:11px; text-decoration:none; display:inline-flex; align-items:center; justify-content:center; gap:5px;">
                  ↗ Mở trên YouTube (Tua sẵn [${{vid.timestampLabel}}])
                </a>
              </div>
            </div>
          `;
        }}

        container.innerHTML = `
          <div class="video-card-cp">
            ${{fileProtocolAlertHtml}}
            <div id="videoPlayerBox" class="video-thumb-box" onclick="playVideoInline('${{vid.youtubeId}}', ${{vid.startSeconds}}, '${{cleanTitle}}')" title="Nhấp vào đây để phát video trực tiếp trên trang web">
              <img class="video-thumb-img" src="https://img.youtube.com/vi/${{vid.youtubeId}}/hqdefault.jpg" alt="${{cleanTitle}}" onerror="this.src='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800'">
              <div class="video-play-overlay">
                <div class="play-btn-circle">▶</div>
              </div>
              <div class="timestamp-badge">Mốc tua: ${{vid.timestampLabel}}</div>
              <div style="position:absolute; top:6px; left:6px; background:rgba(0,0,0,0.85); color:#34d399; font-size:10px; font-weight:700; padding:2px 7px; border-radius:3px; border:1px solid rgba(52,211,153,0.35); display:flex; align-items:center; gap:4px; z-index:2;">
                <span style="display:inline-block; width:6px; height:6px; border-radius:50%; background:#10b981;"></span>
                Phát trực tiếp trên web
              </div>
            </div>

            <div style="padding:12px; display:flex; flex-direction:column; gap:8px;">
              <div style="font-size:12.5px; font-weight:700; color:#fff; line-height:1.4;">${{vid.title}}</div>
              <div style="font-size:11px; color:var(--text-muted); display:flex; justify-content:space-between;">
                <span>Kênh: <strong>${{vid.channel}}</strong></span>
                <span style="font-family:var(--font-mono); color:#60a5fa;">Tua [${{vid.timestampLabel}}]</span>
              </div>
              <div style="font-size:11px; color:var(--text-secondary); background:rgba(0,0,0,0.25); padding:8px; border-radius:3px; border-left:2px solid #3b82f6; line-height:1.5;">
                <strong>Trọng tâm (${{vid.sectionId}}):</strong> ${{vid.highlightNote}}
              </div>
              <div style="display:grid; grid-template-columns: 1fr auto; gap:6px; margin-top:4px;">
                <button id="btnPlayInline" onclick="playVideoInline('${{vid.youtubeId}}', ${{vid.startSeconds}}, '${{cleanTitle}}')" class="btn btn-primary" style="justify-content:center; height:34px; font-size:12px; font-weight:700; background:linear-gradient(135deg, #f0b90b, #d97706); color:#000; border:none; cursor:pointer;">
                  ▶ Phát ngay trên Web (${{vid.timestampLabel}})
                </button>
                <a href="${{ytDirectUrl}}" target="_blank" class="btn btn-secondary" style="justify-content:center; text-decoration:none; height:34px; font-size:11px; padding:0 10px; display:inline-flex; align-items:center;" title="Mở trong tab mới trên YouTube">
                  ↗ YouTube
                </a>
              </div>
              <div style="font-size:10px; color:var(--text-muted); text-align:center;">
                (Nếu gặp Lỗi 153 do mở file cục bộ, bấm nút ↗ YouTube hoặc chạy trên Localhost)
              </div>
            </div>
          </div>
        `;

      }} else if (inspectorTab === 'formulas') {{
        let html = `
          <div style="display:flex; flex-direction:column; gap:8px;">
            <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase;">
              BẢNG CÔNG THỨC TOÁN & HỌC MÁY CỐT LÕI
            </div>
        `;
        FORMULAS.forEach(f => {{
          html += `
            <div class="cp-formula-box">
              <div class="formula-title">${{f.title}}</div>
              <div class="formula-desc">${{f.desc}}</div>
              <div class="formula-tex">$$${{f.tex}}$$</div>
            </div>
          `;
        }});
        html += `</div>`;
        container.innerHTML = html;
        renderMath(container);
      }}
    }}

    // Phát video nhúng trực tiếp ngay trên trang web (hỗ trợ cả YouTube & iframe BunnyCDN)
    window.playVideoInline = function(source, startSeconds, title, isDirectUrl) {{
      const box = document.getElementById('videoPlayerBox');
      if (!box) return;
      box.onclick = null;
      box.title = '';
      
      if (window.location.protocol === 'file:' && !isDirectUrl && typeof source === 'string' && !source.startsWith('http')) {{
        const ytDirectUrl = 'https://www.youtube.com/watch?v=' + source + '&t=' + (startSeconds || 0) + 's';
        box.innerHTML = `
          <div style="width:100%; height:200px; background:#0f172a; border-radius:6px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:16px; text-align:center; gap:8px; border:1px solid #334155;">
            <div style="font-size:20px;">⚠️</div>
            <div style="font-size:12px; font-weight:700; color:#f87171;">
              YouTube chặn nhúng video trên file:/// (Lỗi 153)
            </div>
            <div style="font-size:11px; color:#cbd5e1; max-width:280px; line-height:1.4;">
              Google yêu cầu chạy qua tên miền/localhost để phát nhúng.
            </div>
            <div style="display:flex; flex-direction:column; gap:6px; width:100%; max-width:260px; margin-top:4px;">
              <a href="http://localhost:8080/olympic_ai_study_hub.html" style="background:#2563eb; color:#fff; padding:6px 10px; border-radius:4px; font-weight:700; font-size:11px; text-decoration:none; display:block;">
                🚀 Mở trên Localhost (Xem trực tiếp OK)
              </a>
              <a href="${{ytDirectUrl}}" target="_blank" style="background:#f59e0b; color:#000; padding:6px 10px; border-radius:4px; font-weight:700; font-size:11px; text-decoration:none; display:block;">
                ↗ Xem trên YouTube (Tua sẵn đúng phút)
              </a>
            </div>
          </div>
        `;
        window.open(ytDirectUrl, '_blank');
        return;
      }}

      let embedSrc = '';
      if (isDirectUrl || (typeof source === 'string' && source.startsWith('http'))) {{
        embedSrc = source;
      }} else {{
        const originParam = window.location.protocol.startsWith('http') ? '&origin=' + encodeURIComponent(window.location.origin) : '';
        embedSrc = 'https://www.youtube-nocookie.com/embed/' + source + '?autoplay=1&start=' + (startSeconds || 0) + '&rel=0&enablejsapi=1' + originParam;
      }}

      box.innerHTML = `
        <iframe 
          class="video-iframe-embed" 
          src="${{embedSrc}}" 
          title="${{title || 'Bài giảng OLP AI'}}" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen
        ></iframe>
      `;
      const btn = document.getElementById('btnPlayInline');
      if (btn) {{
        btn.innerHTML = '🔴 Đang phát trực tiếp trên Web';
        btn.style.background = '#15803d';
        btn.style.color = '#ffffff';
      }}
    }};
    window.playVideo = window.playVideoInline;

    // Phát video bài giảng chính thức của khóa học từ sidebar Giáo trình
    window.playCourseVideo = function(videoUrl, title) {{
      switchInspectorTab('video');
      if (!isInspectorOpen) {{
        toggleInspector();
      }}
      setTimeout(() => {{
        playVideoInline(videoUrl, 0, title, true);
      }}, 100);
    }};

    // Split Mode Toggle & Content with Splitter Sync
    function toggleSplitMode() {{
      isSplitOpen = !isSplitOpen;
      const splitEl = document.getElementById('arenaSplitPane');
      const splitSplitter = document.getElementById('splitterSplit');
      const btn = document.getElementById('btnToggleSplit');
      if (isSplitOpen) {{
        if (splitEl) {{
          splitEl.style.display = 'flex';
          if (!splitEl.style.width || parseInt(splitEl.style.width, 10) < 250) {{
            splitEl.style.width = '480px';
          }}
        }}
        if (splitSplitter) splitSplitter.style.display = 'flex';
        if (btn) btn.classList.add('btn-active');
        renderSplitContent();
      }} else {{
        if (splitEl) splitEl.style.display = 'none';
        if (splitSplitter) splitSplitter.style.display = 'none';
        if (btn) btn.classList.remove('btn-active');
      }}
    }}

    function setSplitType(type) {{
      splitType = type;
      renderSplitContent();
    }}

    let currentTheorySecId = '§1.1';
    let currentTheorySecIdUserSelected = false;

    function switchTheorySection(secId) {{
      currentTheorySecId = secId;
      currentTheorySecIdUserSelected = true;
      renderSplitContent();
    }}

    // Beautiful Theory Markdown Parser with Full Math & Callout Protection
    function formatTheoryMarkdown(mdText) {{
      if (!mdText) return '';
      const mathPlaceholders = [];

      // 1. Protect Display Math: $$...$$
      let s = mdText.replace(/\$\$([\s\S]*?)\$\$/g, (match) => {{
        const idx = mathPlaceholders.length;
        const safeTex = match.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        mathPlaceholders.push(safeTex);
        return '%%%MATH_DISPLAY_' + idx + '%%%';
      }});

      // 2. Protect Inline Math: $...$
      s = s.replace(/\$([^\$\\r\\n]+?)\$/g, (match) => {{
        const idx = mathPlaceholders.length;
        const safeTex = match.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        mathPlaceholders.push(safeTex);
        return '%%%MATH_INLINE_' + idx + '%%%';
      }});

      // 3. Bold, Code, Headers
      s = s.replace(/\*\*([^\*]+)\*\*/g, '<strong>$1</strong>');
      s = s.replace(/`([^`]+)`/g, '<code style="background:rgba(255,255,255,0.08); padding:1px 5px; border-radius:3px; font-family:var(--font-mono); font-size:12px; color:#f0b90b;">$1</code>');

      // 4. Lines, Lists, Callouts
      const lines = s.split(String.fromCharCode(10));
      const res = [];
      let inList = false;
      let inVipCard = false;

      for (let line of lines) {{
        let trimmed = line.trim();
        if (!trimmed) {{
          if (inList) {{ res.push('</ul>'); inList = false; }}
          continue;
        }}

        // Special Callout: Hay ra thi
        if (trimmed.indexOf('⭐') !== -1 || trimmed.indexOf('Hay ra thi') !== -1) {{
          if (inList) {{ res.push('</ul>'); inList = false; }}
          if (inVipCard) {{ res.push('</div>'); inVipCard = false; }}
          res.push('<div style="background:rgba(240, 185, 11, 0.08); border:1px solid rgba(240, 185, 11, 0.35); border-radius:6px; padding:10px 12px; margin:12px 0;"><div style="font-weight:700; color:#f0b90b; font-size:12px; margin-bottom:6px;">⭐ TRỌNG TÂM HAY RA THI (EXAM TIPS)</div>');
          inVipCard = true;
          continue;
        }}

        if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {{
          if (!inList) {{
            res.push('<ul style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
            inList = true;
          }}
          res.push('<li style="margin-bottom:4px;">' + trimmed.substring(2) + '</li>');
        }} else if (/^\d+\.\s/.test(trimmed)) {{
          if (!inList) {{
            res.push('<ol style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
            inList = true;
          }}
          res.push('<li style="margin-bottom:4px;">' + trimmed.replace(/^\d+\.\s*/, '') + '</li>');
        }} else {{
          if (inList) {{ res.push('</ul>'); inList = false; }}
          if (trimmed.startsWith('### ')) {{
            res.push('<h4 style="font-size:14px; font-weight:700; color:#60a5fa; margin:14px 0 6px 0;">' + trimmed.substring(4) + '</h4>');
          }} else {{
            res.push('<p style="margin:6px 0; line-height:1.7;">' + trimmed + '</p>');
          }}
        }}
      }}
      if (inList) res.push('</ul>');
      if (inVipCard) res.push('</div>');

      let html = res.join('');

      // 5. Restore Math placeholders using split().join() (No $$ JS quirk!)
      for (let i = 0; i < mathPlaceholders.length; i++) {{
        html = html.split('%%%MATH_DISPLAY_' + i + '%%%').join(mathPlaceholders[i]);
        html = html.split('%%%MATH_INLINE_' + i + '%%%').join(mathPlaceholders[i]);
      }}

      return html;
    }}

    function renderSplitContent() {{
      const container = document.getElementById('splitPaneBody');
      const selectEl = document.getElementById('splitTheorySecSelect');
      
      // Update select element options once
      if (selectEl && selectEl.options.length === 0 && THEORY && THEORY.length > 0) {{
        THEORY.forEach(s => {{
          const opt = document.createElement('option');
          opt.value = s.secId;
          const shortTit = (s.title || '').length > 28 ? s.title.substring(0, 28) + '...' : s.title;
          opt.textContent = `${{s.secId}} ${{shortTit}}`;
          selectEl.appendChild(opt);
        }});
      }}

      if (selectEl) {{
        selectEl.style.display = (splitType === 'theory') ? 'inline-block' : 'none';
        selectEl.value = currentTheorySecId;
      }}

      const btnPdf = document.getElementById('btnSplitPdf');
      const btnTheory = document.getElementById('btnSplitTheory');
      const btnFormulas = document.getElementById('btnSplitFormulas');
      if (btnPdf) btnPdf.className = splitType === 'pdf' ? 'btn btn-primary' : 'btn';
      if (btnTheory) btnTheory.className = splitType === 'theory' ? 'btn btn-primary' : 'btn';
      if (btnFormulas) btnFormulas.className = splitType === 'formulas' ? 'btn btn-primary' : 'btn';

      if (splitType === 'pdf') {{
        container.innerHTML = `<iframe src="olp_ai_handbook_2026.pdf" style="width:100%; height:100%; border:none;"></iframe>`;
      }} else if (splitType === 'theory') {{
        // Smart match: if user hasn't explicitly picked a section, link to current problem section
        const q = EXAM.questions[currentIndex];
        let targetSecId = currentTheorySecId;
        if (!currentTheorySecIdUserSelected && q && q.explanation) {{
          const matchSec = q.explanation.match(/§[\d\.]+/);
          if (matchSec) {{
            targetSecId = matchSec[0];
            currentTheorySecId = targetSecId;
            if (selectEl) selectEl.value = targetSecId;
          }}
        }}

        const sec = THEORY.find(s => s.secId === targetSecId) || THEORY.find(s => s.secId.startsWith(targetSecId)) || THEORY[1] || THEORY[0];
        container.innerHTML = `
          <div style="height:100%; overflow-y:auto; padding:16px; font-size:13px; line-height:1.7; color:var(--text-secondary); background:var(--bg-surface);">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1px solid var(--border-subtle); padding-bottom:8px;">
              <div>
                <span style="font-size:11px; font-weight:700; color:#f0b90b; text-transform:uppercase;">GIÁO TRÌNH TRỌNG TÂM OLP AI</span>
                <h3 style="font-size:15px; font-weight:700; color:#ffffff; margin-top:2px;">${{sec.secId}} ${{sec.title}}</h3>
              </div>
            </div>
            <div class="theory-body-content">${{formatTheoryMarkdown(sec.body)}}</div>
          </div>
        `;
        renderMath(container);
      }} else if (splitType === 'formulas') {{
        let html = `<div style="height:100%; overflow-y:auto; padding:14px; display:flex; flex-direction:column; gap:10px;">`;
        FORMULAS.forEach(f => {{
          html += `
            <div class="cp-formula-box">
              <div class="formula-title">${{f.title}}</div>
              <div class="formula-desc">${{f.desc}}</div>
              <div class="formula-tex">$$${{f.tex}}$$</div>
            </div>
          `;
        }});
        html += `</div>`;
        container.innerHTML = html;
        renderMath(container);
      }}
    }}

    function openChapterTheory(prefix) {{
      currentTheorySecIdUserSelected = true;
      const matchingSec = THEORY.find(s => s.secId.startsWith(prefix));
      if (matchingSec) {{
        currentTheorySecId = matchingSec.secId;
      }}
      openSplitWith('theory');
    }}

    function openSplitWith(type) {{
      splitType = type;
      if (!isSplitOpen) toggleSplitMode();
      else renderSplitContent();
    }}

    // Rubric Evaluator & Checklist (Tự đối chiếu thật - P0-1)
    function toggleRubricCriterion(qid, critIdx) {{
      const q = EXAM.questions[currentIndex];
      const rubricList = q.rubric || [];
      const ptsPerCrit = q.points / Math.max(1, rubricList.length);

      if (!rubricEvalResults[qid]) {{
        rubricEvalResults[qid] = {{ checked: {{}} }};
      }}
      const checkedMap = rubricEvalResults[qid].checked || {{}};
      checkedMap[critIdx] = !checkedMap[critIdx];
      rubricEvalResults[qid].checked = checkedMap;

      let earnedPts = 0;
      rubricList.forEach((_, idx) => {{
        if (checkedMap[idx]) earnedPts += ptsPerCrit;
      }});
      rubricEvalResults[qid].score = Number(earnedPts.toFixed(1));

      const ta = document.getElementById('essayInput_' + qid);
      const text = ta ? ta.value.trim() : (answers[qid]?.text || '');

      answers[qid] = {{
        ...(answers[qid] || {{}}),
        text: text,
        selfScore: Number(earnedPts.toFixed(1)),
        points: Number(earnedPts.toFixed(1)),
        verdict: earnedPts > 0 ? 'AC' : 'WA',
        submitted: true,
        timestamp: new Date().toLocaleTimeString()
      }};
      saveState();
      renderInspector();
      renderSidebar();
      renderHeaderStats();
    }}

    function runEssayKeywordCheck(qid) {{
      const ta = document.getElementById('essayInput_' + qid);
      const rawText = ta ? ta.value : (answers[qid]?.text || '');
      const q = EXAM.questions[currentIndex];
      const rubricList = q.rubric || [];
      const ptsPerCrit = q.points / Math.max(1, rubricList.length);

      // Lo\u1ea1i b\u1ecf c\u00e1c d\u00f2ng ti\u00eau \u0111\u1ec1 v\u00e0 nh\u00e3n m\u1eb7c \u0111\u1ecbnh c\u1ee7a khung m\u1eabu 5 b\u01b0\u1edbc \u0111\u1ec3 ki\u1ec3m tra n\u1ed9i dung th\u1ef1c t\u1ebf
      const templateBoilerplate = [
        '### 1. Phân tích bài toán & Ràng buộc dữ liệu',
        '- Bản chất bài toán:',
        '- Đặc thù đầu vào/đầu ra:',
        '- Khó khăn cốt lõi (Mất cân bằng / Ánh sáng / Độ trễ):',
        '### 2. Thiết kế mô hình & Luận giải kỹ thuật',
        '- Baseline tham chiếu:',
        '- Kiến trúc đề xuất chính (Backbone + Head):',
        '- Lý do lựa chọn vượt trội:',
        '### 3. Pipeline xử lý & Chống rò rỉ dữ liệu (Leakage)',
        '- Tiền xử lý & Augmentation:',
        '- Chiến lược phân chia Validation (Group K-Fold / TimeSeries):',
        '- Hậu xử lý / Giải mã:',
        '### 4. Chỉ số đánh giá & Phân tích lỗi',
        '- Metric chính và lý do lựa chọn:',
        '- Xử lý các ca lỗi biên (Edge cases):',
        '### 5. Phương án mở rộng & Tối ưu hóa thực tế',
        '- Tăng cường mô hình (Pretrain, Pseudo-label, Ensemble):',
        '- Tối ưu hóa tốc độ (ONNX Runtime, FP16/INT8, Pruning):'
      ];
      let userContent = rawText;
      templateBoilerplate.forEach(bp => {{
        userContent = userContent.split(bp).join('');
      }});
      userContent = userContent.replace(/[#\-\*:;\s]/g, '').trim();

      // N\u1ebfu b\u00e0i l\u00e0m tr\u1ed1ng ho\u1eb7c ch\u1ec9 c\u00f3 khung template ch\u01b0a \u0111i\u1ec1n n\u1ed9i dung (d\u01b0\u1edbi 20 k\u00fd t\u1ef1 th\u1ef1c t\u1ebf)
      if (userContent.length < 20) {{
        rubricEvalResults[qid] = {{
          checked: {{}},
          score: 0,
          summary: 'Bài làm hiện đang để trống hoặc khung mẫu chưa được điền nội dung phân tích kỹ thuật (dưới 20 ký tự thực tế). Điểm đề xuất: 0.0/' + q.points + 'đ.'
        }};
        answers[qid] = {{
          ...(answers[qid] || {{}}),
          text: rawText,
          selfScore: 0,
          points: 0,
          verdict: 'WA',
          submitted: false,
          timestamp: new Date().toLocaleTimeString()
        }};
        saveState();
        switchInspectorTab('rubric');
        renderCenter();
        renderSidebar();
        renderHeaderStats();
        alert([
          '⚠️ Bài làm hiện đang để trống hoặc khung mẫu chưa được điền nội dung phân tích kỹ thuật (dưới 20 ký tự thực tế).',
          'Điểm đề xuất: 0.0/' + q.points + 'đ.',
          'Vui lòng điền các phân tích kỹ thuật cụ thể dưới từng mục trước khi kiểm tra.'
        ].join(String.fromCharCode(10)));
        return;
      }}

      // Qu\u00e9t t\u1eeb kh\u00f3a tr\u00ean n\u1ed9i dung th\u1ef1c t\u1ebf c\u1ee7a th\u00ed sinh
      const lowerText = userContent.toLowerCase();
      let checkedMap = {{}};
      let matchedCount = 0;

      rubricList.forEach((crit, idx) => {{
        const words = crit.toLowerCase().replace(/[^a-z0-9àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ\s]/g, ' ')
          .split(/\s+/).filter(w => w.length > 3);
        let matches = 0;
        for (const w of words) {{
          if (lowerText.indexOf(w) !== -1) matches++;
        }}
        if (matches >= 2 || (words.length > 0 && matches / words.length >= 0.2)) {{
          checkedMap[idx] = true;
          matchedCount++;
        }} else {{
          checkedMap[idx] = false;
        }}
      }});

      const proposedScore = Number((matchedCount * ptsPerCrit).toFixed(1));
      rubricEvalResults[qid] = {{
        checked: checkedMap,
        score: proposedScore,
        summary: 'Hệ thống gợi ý từ khóa phát hiện ' + matchedCount + '/' + rubricList.length + ' tiêu chí có xuất hiện thuật ngữ liên quan trong bài làm. (Lưu ý: Đây là gợi ý tự động hỗ trợ tự đối chiếu, không phải điểm chấm chính thức của hội đồng).'
      }};

      answers[qid] = {{
        ...(answers[qid] || {{}}),
        text: rawText,
        selfScore: proposedScore,
        points: proposedScore,
        verdict: proposedScore > 0 ? 'AC' : 'WA',
        submitted: true,
        timestamp: new Date().toLocaleTimeString()
      }};
      saveState();
      switchInspectorTab('rubric');
      renderCenter();
      renderSidebar();
      renderHeaderStats();
      alert([
        '⚡ [Gợi ý Từ khóa Tự động]',
        'Đã đối chiếu bài làm với ' + rubricList.length + ' tiêu chí.',
        'Điểm đề xuất: ' + proposedScore + '/' + q.points + 'đ.',
        'Bạn có thể điều chỉnh các ô đánh dấu bên bảng Inspector bên phải để hoàn thiện điểm tự đánh giá.'
      ].join(String.fromCharCode(10)));
    }}

    function insertEssayTemplate(qid) {{
      const template = [
        '### 1. Phân tích bài toán & Ràng buộc dữ liệu',
        '- Bản chất bài toán:',
        '- Đặc thù đầu vào/đầu ra:',
        '- Khó khăn cốt lõi (Mất cân bằng / Ánh sáng / Độ trễ):',
        '',
        '### 2. Thiết kế mô hình & Luận giải kỹ thuật',
        '- Baseline tham chiếu:',
        '- Kiến trúc đề xuất chính (Backbone + Head):',
        '- Lý do lựa chọn vượt trội:',
        '',
        '### 3. Pipeline xử lý & Chống rò rỉ dữ liệu (Leakage)',
        '- Tiền xử lý & Augmentation:',
        '- Chiến lược phân chia Validation (Group K-Fold / TimeSeries):',
        '- Hậu xử lý / Giải mã:',
        '',
        '### 4. Chỉ số đánh giá & Phân tích lỗi',
        '- Metric chính và lý do lựa chọn:',
        '- Xử lý các ca lỗi biên (Edge cases):',
        '',
        '### 5. Phương án mở rộng & Tối ưu hóa thực tế',
        '- Tăng cường mô hình (Pretrain, Pseudo-label, Ensemble):',
        '- Tối ưu hóa tốc độ (ONNX Runtime, FP16/INT8, Pruning):'
      ].join(String.fromCharCode(10));

      const ta = document.getElementById('essayInput_' + qid);
      if (ta) {{
        ta.value = ta.value.trim() ? ta.value + String.fromCharCode(10, 10) + template : template;
        answers[qid] = {{ ...(answers[qid] || {{}}), text: ta.value }};
        saveState();
      }}
    }}

    function runCustomCode(qid) {{
      const ta = document.getElementById('codeInput_' + qid);
      const code = ta ? ta.value.trim() : '';
      if (!code || code === '# Viết mã nguồn Python / PyTorch tại đây...') {{
        alert('⚠️ Vui lòng viết giải pháp mã nguồn trước khi kiểm tra.');
        return;
      }}
      answers[qid] = {{
        ...(answers[qid] || {{}}),
        code: code,
        codeSubmitted: true,
        selfScore: answers[qid]?.selfScore || 0,
        timestamp: new Date().toLocaleTimeString()
      }};
      saveState();
      alert([
        'ℹ️ [Sandbox Cục Bộ Trình Duyệt]',
        'Trình duyệt hiện tại chưa tích hợp runtime Python/PyTorch trực tiếp.',
        '',
        'Mã nguồn của bạn đã được ghi nhận. Vui lòng mở rộng mục "BÀI GIẢI MẪU THAM KHẢO & TEST CASES MINH HỌA" bên dưới để đối chiếu logic thuật toán và các trường hợp kiểm thử.'
      ].join(String.fromCharCode(10)));
      renderCenter();
      renderSidebar();
      renderHeaderStats();
    }}

    function setCodeSelfScore(qid, pts) {{
      const q = EXAM.questions.find(item => item.id === qid);
      const maxPts = q ? q.points : 7;
      answers[qid] = {{
        ...(answers[qid] || {{}}),
        selfScore: pts,
        verdict: pts === maxPts ? 'AC' : (pts > 0 ? 'PARTIAL' : 'WA'),
        points: pts,
        codeSubmitted: true,
        timestamp: new Date().toLocaleTimeString()
      }};
      saveState();
      renderInspector();
      renderSidebar();
      renderHeaderStats();
    }}

    function submitContestConfirm() {{
      const total = EXAM.questions.length;
      let answeredGraded = 0;
      let answeredEssay = 0;
      let gradedPts = 0;
      let essaySelfPts = 0;

      const maxGradedPts = EXAM.questions.filter(q => q.type !== 'essay').reduce((acc, q) => acc + (q.points || 0), 0);
      const maxEssayPts = EXAM.questions.filter(q => q.type === 'essay').reduce((acc, q) => acc + (q.points || 0), 0);

      EXAM.questions.forEach(q => {{
        const a = answers[q.id];
        if (a) {{
          if (q.type === 'essay') {{
            if (a.selfScore !== undefined || (a.text && a.text.trim().length > 0)) {{
              answeredEssay++;
              if (a.selfScore !== undefined) essaySelfPts += a.selfScore;
            }}
          }} else {{
            if (a.selected || a.codeSubmitted) {{
              answeredGraded++;
              if (q.type === 'code') {{
                const codePts = a.selfScore !== undefined ? a.selfScore : (a.points !== undefined ? a.points : 0);
                gradedPts += codePts;
              }} else {{
                if (a.verdict === 'AC') gradedPts += q.points;
              }}
            }}
          }}
        }}
      }});

      const totalAnswered = answeredGraded + answeredEssay;
      const reportLines = [
        'BÁO CÁO TỔNG HỢP KẾT QUẢ [' + EXAM.title + ']:',
        '',
        '1. PHẦN TRẮC NGHIỆM & CODE (GRADED):',
        '   • Điểm đạt được: ' + gradedPts.toFixed(1) + ' / ' + maxGradedPts.toFixed(1) + ' điểm',
        '   • Đã trả lời: ' + answeredGraded + ' câu'
      ];

      if (maxEssayPts > 0) {{
        reportLines.push(
          '',
          '2. PHẦN TỰ LUẬN THIẾT KẾ GIẢI PHÁP AI (TỰ ĐỐI CHIẾU RUBRIC):',
          '   • Điểm tự đánh giá: ' + essaySelfPts.toFixed(1) + ' / ' + maxEssayPts.toFixed(1) + ' điểm',
          '   • Đã làm: ' + answeredEssay + ' bài'
        );
      }}

      reportLines.push(
        '',
        'Tổng tiến độ hoàn thành: ' + totalAnswered + '/' + total + ' bài.',
        'Bạn có chắc chắn muốn nộp bài thi không?'
      );

      if (confirm(reportLines.join(String.fromCharCode(10)))) {{
        const token = localStorage.getItem('olp-token');
        if (token && window.location.protocol.startsWith('http')) {{
          fetch('/api/submissions', {{
            method: 'POST',
            headers: {{
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + token
            }},
            body: JSON.stringify({{
              exam_id: currentExamId,
              time_spent_seconds: Math.max(1, (((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60) - timerSeconds),
              answers: answers
            }})
          }})
          .then(res => res.json())
          .then(data => {{
            if (data.submission_id) {{
              const msg = [
                '🎉 [KẾT QUẢ ĐÃ LƯU VÀO DATABASE SERVER]',
                'Mã bài nộp: #' + data.submission_id + ' (' + data.exam_id.toUpperCase() + ')',
                'Điểm chính thức: ' + data.score + ' / ' + data.max_score + ' điểm (' + data.accuracy_percentage + '%)',
                'Số câu đúng: ' + data.correct_count + ' / ' + data.total_questions + ' câu',
                'Bài thi đã được ghi nhận vào lịch sử tài khoản của bạn!'
              ].join(String.fromCharCode(10));
              alert(msg);
              fetchSubmissionsHistory();
              switchSidebarTab('sub');
            }} else {{
              fallbackAlert();
            }}
          }})
          .catch(err => {{
            console.warn('[Backend Submit Error]', err);
            fallbackAlert();
          }});
        }} else {{
          fallbackAlert();
        }}

        function fallbackAlert() {{
          const successMsg = (maxEssayPts > 0)
            ? '🎉 Bạn đã nộp bài thành công (Lưu trên máy cục bộ)!' + String.fromCharCode(10) + 'Graded: ' + gradedPts.toFixed(1) + '/' + maxGradedPts.toFixed(1) + 'đ | Tự luận: ' + essaySelfPts.toFixed(1) + '/' + maxEssayPts.toFixed(1) + 'đ'
            : '🎉 Bạn đã nộp bài thành công (Lưu trên máy cục bộ)!' + String.fromCharCode(10) + 'Graded: ' + gradedPts.toFixed(1) + '/' + maxGradedPts.toFixed(1) + 'đ';
          alert(successMsg);
          switchSidebarTab('sub');
        }}
      }}
    }}

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {{
      const tag = e.target.tagName;
      if (tag === 'TEXTAREA' || tag === 'INPUT') return;

      if (e.key >= '1' && e.key <= '4') {{
        const keys = ['A', 'B', 'C', 'D'];
        selectOption(keys[parseInt(e.key) - 1]);
      }} else if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') {{
        nextQuestion();
      }} else if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') {{
        prevQuestion();
      }} else if (e.key === 'b' || e.key === 'B') {{
        toggleSidebar();
      }} else if (e.key === 'e' || e.key === 'E') {{
        toggleEditorialManual();
      }} else if (e.key === 'i' || e.key === 'I') {{
        toggleInspector();
      }} else if ((e.ctrlKey || e.metaKey) && e.key === 's') {{
        e.preventDefault();
        submitContestConfirm();
      }}
    }});

    // Clock Interval
    function startClock() {{
      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(() => {{
        if (isNaN(timerSeconds)) {{
          timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;
        }}
        if (timerSeconds > 0) {{
          timerSeconds--;
          const hrs = Math.floor(timerSeconds / 3600);
          const mins = Math.floor((timerSeconds % 3600) / 60);
          const secs = timerSeconds % 60;
          document.getElementById('contestClock').textContent = 
            `⏱ ${{String(hrs).padStart(2, '0')}}:${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;
        }}
      }}, 1000);
    }}

    // Sync Exam Selector Labels dynamically with ALL_EXAMS
    function syncExamSelectorLabels() {{
      const sel = document.getElementById('examSelector');
      if (!sel || typeof ALL_EXAMS === 'undefined') return;
      const labels = {{
        'olp-01': 'Đề 01 · Toàn diện',
        'olp-02': 'Đề 02 · Format VOAI',
        'olp-03': 'Đề 03 · Mô phỏng Quốc gia',
        'olp-04': 'Đề 04 · Insight Video VOAI',
        'voai-2025': 'Đề 006 · Gốc VOAI 2025',
        'olp-05': 'Đề 05 · Chuyên đề CV & NLP'
      }};
      Array.from(sel.options).forEach(opt => {{
        const exam = ALL_EXAMS[opt.value];
        if (exam && exam.questions) {{
          const base = labels[opt.value] || exam.title || opt.value;
          opt.textContent = `${{base}} (${{exam.questions.length}}c)`;
        }}
      }});
    }}

    // -------------------------------------------------------------
    // 4. BACKEND AUTHENTICATION & SERVER SYNC (E2E)
    // -------------------------------------------------------------
    let currentUser = null;
    let serverSubmissions = [];
    let currentAuthTab = 'login';

    function renderUserAccountBox() {{
      const box = document.getElementById('userAccountBox');
      if (!box) return;
      if (currentUser) {{
        const shortTeam = currentUser.team_name ? ' · ' + currentUser.team_name : '';
        box.innerHTML = `
          <div style="display:inline-flex; align-items:center; gap:6px; background:#18181b; border:1px solid #3f3f46; padding:2px 8px; border-radius:4px; font-size:11px;">
            <span style="color:#10b981; font-size:10px;">●</span>
            <span style="font-weight:700; color:#f4f4f5;" title="Tài khoản: ${{currentUser.username}}${{shortTeam}}">${{currentUser.display_name}}</span>
            <button onclick="logoutUser()" style="background:none; border:none; color:#f87171; font-size:11px; cursor:pointer; padding:0 2px; margin-left:2px;" title="Đăng xuất tài khoản">⎋</button>
          </div>
        `;
      }} else {{
        box.innerHTML = `
          <button class="btn" onclick="openAuthModal()" style="height:24px; font-size:11px; padding:0 8px; border-color:#3b82f6; color:#60a5fa;" title="Đăng nhập để lưu tiến độ vào cơ sở dữ liệu server">
            🔑 Đăng nhập
          </button>
        `;
      }}
    }}

    function initAuth() {{
      renderUserAccountBox();
      const token = localStorage.getItem('olp-token');
      if (!token || !window.location.protocol.startsWith('http')) return;

      fetch('/api/auth/me', {{
        headers: {{ 'Authorization': 'Bearer ' + token }}
      }})
      .then(res => {{
        if (res.ok) return res.json();
        throw new Error('Token expired');
      }})
      .then(user => {{
        currentUser = user;
        renderUserAccountBox();
        fetchSubmissionsHistory();
      }})
      .catch(() => {{
        localStorage.removeItem('olp-token');
        currentUser = null;
        renderUserAccountBox();
      }});
    }}

    function logoutUser() {{
      localStorage.removeItem('olp-token');
      currentUser = null;
      serverSubmissions = [];
      renderUserAccountBox();
      renderSidebar();
      showToast('Đã đăng xuất tài khoản.');
    }}

    function openAuthModal() {{
      const modal = document.getElementById('authModal');
      if (modal) {{
        modal.style.display = 'flex';
        switchAuthTab('login');
      }}
    }}

    function closeAuthModal() {{
      const modal = document.getElementById('authModal');
      if (modal) modal.style.display = 'none';
    }}

    function switchAuthTab(tab) {{
      currentAuthTab = tab;
      const btnLogin = document.getElementById('authTabLogin');
      const btnReg = document.getElementById('authTabRegister');
      const body = document.getElementById('authFormBody');
      if (!body) return;

      if (tab === 'login') {{
        if (btnLogin) {{ btnLogin.classList.add('btn-primary'); btnLogin.style.background = '#2563eb'; }}
        if (btnReg) {{ btnReg.classList.remove('btn-primary'); btnReg.style.background = '#1f2937'; }}
        body.innerHTML = `
          <form onsubmit="handleAuthSubmit(event)" style="display:flex; flex-direction:column; gap:10px;">
            <div>
              <label style="font-size:11px; color:#9ca3af; display:block; margin-bottom:4px;">Tên đăng nhập:</label>
              <input type="text" id="authUsername" required style="width:100%; height:30px; background:#1f2937; border:1px solid #374151; color:#fff; padding:0 8px; border-radius:4px; font-size:12px;" placeholder="Ví dụ: student hoặc admin">
            </div>
            <div>
              <label style="font-size:11px; color:#9ca3af; display:block; margin-bottom:4px;">Mật khẩu:</label>
              <input type="password" id="authPassword" required style="width:100%; height:30px; background:#1f2937; border:1px solid #374151; color:#fff; padding:0 8px; border-radius:4px; font-size:12px;" placeholder="Nhập mật khẩu">
            </div>
            <div id="authErrorMsg" style="font-size:11px; color:#f87171; display:none;"></div>
            <button type="submit" class="btn btn-primary" style="height:32px; font-size:12px; margin-top:4px; background:#2563eb; color:#fff; border:none; border-radius:4px; font-weight:600; cursor:pointer;">
              Đăng nhập ngay
            </button>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:6px; font-size:11px;">
              <span style="color:#6b7280;">Chưa có tài khoản?</span>
              <a href="javascript:void(0)" onclick="quickFillDemo()" style="color:#f59e0b; text-decoration:none;">⚡ Điền tài khoản demo (student)</a>
            </div>
          </form>
        `;
      }} else {{
        if (btnLogin) {{ btnLogin.classList.remove('btn-primary'); btnLogin.style.background = '#1f2937'; }}
        if (btnReg) {{ btnReg.classList.add('btn-primary'); btnReg.style.background = '#10b981'; }}
        body.innerHTML = `
          <form onsubmit="handleAuthSubmit(event)" style="display:flex; flex-direction:column; gap:8px;">
            <div>
              <label style="font-size:11px; color:#9ca3af; display:block; margin-bottom:3px;">Tên đăng nhập:</label>
              <input type="text" id="authUsername" required minlength="3" style="width:100%; height:28px; background:#1f2937; border:1px solid #374151; color:#fff; padding:0 8px; border-radius:4px; font-size:12px;" placeholder="Tối thiểu 3 ký tự">
            </div>
            <div>
              <label style="font-size:11px; color:#9ca3af; display:block; margin-bottom:3px;">Họ và tên thí sinh:</label>
              <input type="text" id="authDisplayName" required style="width:100%; height:28px; background:#1f2937; border:1px solid #374151; color:#fff; padding:0 8px; border-radius:4px; font-size:12px;" placeholder="Ví dụ: Lê Nam Khánh">
            </div>
            <div>
              <label style="font-size:11px; color:#9ca3af; display:block; margin-bottom:3px;">Đội thi / Lớp / Trường:</label>
              <input type="text" id="authTeamName" style="width:100%; height:28px; background:#1f2937; border:1px solid #374151; color:#fff; padding:0 8px; border-radius:4px; font-size:12px;" placeholder="Ví dụ: HCMUS AI Team 01">
            </div>
            <div>
              <label style="font-size:11px; color:#9ca3af; display:block; margin-bottom:3px;">Mật khẩu:</label>
              <input type="password" id="authPassword" required minlength="6" style="width:100%; height:28px; background:#1f2937; border:1px solid #374151; color:#fff; padding:0 8px; border-radius:4px; font-size:12px;" placeholder="Tối thiểu 6 ký tự">
            </div>
            <div id="authErrorMsg" style="font-size:11px; color:#f87171; display:none;"></div>
            <button type="submit" class="btn btn-primary" style="height:32px; font-size:12px; margin-top:4px; background:#10b981; color:#fff; border:none; border-radius:4px; font-weight:600; cursor:pointer;">
              Tạo tài khoản & Đăng nhập
            </button>
          </form>
        `;
      }}
    }}

    function quickFillDemo() {{
      const u = document.getElementById('authUsername');
      const p = document.getElementById('authPassword');
      if (u) u.value = 'student';
      if (p) p.value = 'hcmus2026';
    }}

    function handleAuthSubmit(e) {{
      e.preventDefault();
      const errBox = document.getElementById('authErrorMsg');
      if (errBox) errBox.style.display = 'none';

      const username = (document.getElementById('authUsername')?.value || '').trim();
      const password = (document.getElementById('authPassword')?.value || '').trim();
      const isReg = (currentAuthTab === 'register');

      const url = isReg ? '/api/auth/register' : '/api/auth/login';
      const payload = isReg ? {{
        username: username,
        password: password,
        display_name: (document.getElementById('authDisplayName')?.value || '').trim(),
        team_name: (document.getElementById('authTeamName')?.value || '').trim()
      }} : {{
        username: username,
        password: password
      }};

      fetch(url, {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify(payload)
      }})
      .then(res => {{
        if (!res.ok) {{
          return res.json().then(j => {{ throw new Error(j.detail || 'Thao tác thất bại'); }});
        }}
        return res.json();
      }})
      .then(data => {{
        if (data.access_token) {{
          localStorage.setItem('olp-token', data.access_token);
          currentUser = data.user;
          closeAuthModal();
          renderUserAccountBox();
          fetchSubmissionsHistory();
          showToast('Xin chào, ' + (currentUser.display_name || currentUser.username) + '! Đăng nhập thành công.');
        }}
      }})
      .catch(err => {{
        if (errBox) {{
          errBox.textContent = err.message || 'Lỗi kết nối máy chủ.';
          errBox.style.display = 'block';
        }}
      }});
    }}

    function fetchSubmissionsHistory() {{
      const token = localStorage.getItem('olp-token');
      if (!token || !window.location.protocol.startsWith('http')) return;

      fetch('/api/submissions/my-history', {{
        headers: {{ 'Authorization': 'Bearer ' + token }}
      }})
      .then(res => res.ok ? res.json() : [])
      .then(list => {{
        serverSubmissions = list || [];
        if (sidebarTab === 'sub') renderSidebar();
      }})
      .catch(() => {{}});
    }}

    // Boot App
    window.addEventListener('DOMContentLoaded', () => {{
      loadSavedState();
      syncExamSelectorLabels();
      renderSidebar();
      renderCenter();
      renderInspector();
      renderHeaderStats();
      startClock();
      initSplitters();
      initAuth();
    }});

  </script>

  <!-- AUTH MODAL -->
  <div id="authModal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.75); z-index:100000; align-items:center; justify-content:center; backdrop-filter:blur(4px);">
    <div style="background:#111827; border:1px solid #374151; width:90%; max-width:400px; border-radius:8px; padding:20px; box-shadow:0 10px 25px rgba(0,0,0,0.5); color:#f3f4f6;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid #1f2937; padding-bottom:10px;">
        <div style="display:flex; gap:8px;">
          <button id="authTabLogin" class="btn btn-primary" style="height:26px; font-size:11px; background:#2563eb; color:#fff; border:none;" onclick="switchAuthTab('login')">Đăng nhập</button>
          <button id="authTabRegister" class="btn" style="height:26px; font-size:11px; background:#1f2937; color:#9ca3af; border:1px solid #374151;" onclick="switchAuthTab('register')">Đăng ký</button>
        </div>
        <button class="btn" style="height:24px; padding:0 6px; font-size:11px;" onclick="closeAuthModal()">✕</button>
      </div>
      <div id="authFormBody"></div>
    </div>
  </div>
</body>
</html>
"""

# Ghi ra cả 3 thư mục: public, dist, và temp/public
out_public = os.path.join(ROOT_DIR, "public", "olympic_ai_study_hub.html")
out_dist = os.path.join(ROOT_DIR, "dist", "olympic_ai_study_hub.html")
out_temp = os.path.join(TEMP_DIR, "public", "olympic_ai_study_hub.html")

for p in [out_public, out_dist, out_temp]:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Đã ghi thành công vào: {p} ({os.path.getsize(p)} bytes)")

print("=== HOÀN TẤT TẠO FILE STUDY HUB ===")
