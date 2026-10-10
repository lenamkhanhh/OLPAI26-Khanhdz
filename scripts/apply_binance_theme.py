# -*- coding: utf-8 -*-
"""
scripts/apply_binance_theme.py
Re-styles olympic_ai_study_hub into an ultra-luxury, high-contrast monochrome
black-and-white base with RGB trading neon accents (Binance Pro / TradingView aesthetic).
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
GEN_FILE = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")

with open(GEN_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the <style> section with the Luxury Binance Pro RGB Dark Theme
old_style_marker_start = "  <style>"
old_style_marker_end = "  </style>"

start_idx = content.find(old_style_marker_start)
end_idx = content.find(old_style_marker_end) + len(old_style_marker_end)

if start_idx == -1 or end_idx == -1:
    print("[ERROR] Could not find <style> block in generate_full_hub.py")
    sys.exit(1)

new_style_block = """  <style>
    :root {{
      /* Ultra-Luxury Binance Pro Dark Theme */
      --bg-base: #06080c;
      --bg-surface: #0a0e17;
      --bg-card: #101420;
      --bg-elevated: #161b2a;
      --bg-hover: #1e2436;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-strong: rgba(255, 255, 255, 0.16);
      --border-gold: rgba(240, 185, 11, 0.5);
      --border-cyan: rgba(0, 240, 255, 0.5);
      --border-green: rgba(14, 203, 129, 0.5);
      --border-red: rgba(246, 70, 93, 0.5);
      
      /* Vibrant RGB Trading Accents */
      --color-gold: #f0b90b;
      --color-gold-hover: #ffd700;
      --color-ac: #0ecb81;
      --color-wa: #f6465d;
      --color-partial: #f0b90b;
      --color-cyan: #00f0ff;
      --color-purple: #b026ff;
      --color-accent: #f0b90b;
      
      /* Pure Crisp White & High-Contrast Typography */
      --text-main: #ffffff;
      --text-secondary: #eaecef;
      --text-muted: #848e9c;
      --text-dim: #4e5765;
      
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
      --font-serif: 'STIX Two Text', 'Cambria', 'Times New Roman', serif;
      
      --radius-sm: 4px;
      --radius-md: 6px;
      --radius-lg: 10px;
      
      --sidebar-w: 285px;
      --inspector-w: 395px;
      --header-h: 54px;
      --footer-h: 48px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    /* Sleek Custom Trading Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #080a0f;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1c2233;
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #f0b90b;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-base);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      font-size: 13px;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }}

    /* 1. TOP HEADER (BINANCE PRO TRADING BAR) */
    .arena-header {{
      height: var(--header-h);
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      user-select: none;
      z-index: 40;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .contest-badge {{
      background: linear-gradient(135deg, rgba(240, 185, 11, 0.18) 0%, rgba(240, 185, 11, 0.04) 100%);
      color: #f0b90b;
      font-family: var(--font-mono);
      font-weight: 800;
      font-size: 11px;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(240, 185, 11, 0.55);
      letter-spacing: 0.8px;
      box-shadow: 0 0 14px rgba(240, 185, 11, 0.25);
      text-shadow: 0 0 8px rgba(240, 185, 11, 0.4);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .exam-select-box {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #101420;
      border: 1px solid rgba(255, 255, 255, 0.14);
      padding: 3px 10px;
      border-radius: var(--radius-sm);
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.5);
      transition: border-color 0.2s ease;
    }}
    .exam-select-box:hover {{
      border-color: rgba(240, 185, 11, 0.5);
    }}

    .exam-select {{
      background: transparent;
      color: #ffffff;
      border: none;
      font-size: 12px;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }}
    .exam-select option {{
      background: #0a0e17;
      color: #ffffff;
    }}

    .header-center {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .timer-pill {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #06080e;
      border: 1px solid rgba(240, 185, 11, 0.4);
      padding: 4px 14px;
      border-radius: 20px;
      font-family: var(--font-mono);
      font-size: 13.5px;
      font-weight: 700;
      color: #f0b90b;
      box-shadow: 0 0 16px rgba(240, 185, 11, 0.22), inset 0 0 10px rgba(0, 0, 0, 0.6);
      text-shadow: 0 0 8px rgba(240, 185, 11, 0.35);
    }}

    .live-dot {{
      width: 7px;
      height: 7px;
      background: #0ecb81;
      border-radius: 50%;
      box-shadow: 0 0 10px #0ecb81, 0 0 18px #0ecb81;
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
      gap: 10px;
      font-family: var(--font-mono);
      font-size: 12px;
    }}

    .ticker-gold-val {{
      color: #f0b90b;
      font-weight: 800;
      text-shadow: 0 0 10px rgba(240, 185, 11, 0.4);
    }}

    .badge-ac-count {{
      background: rgba(14, 203, 129, 0.16);
      color: #0ecb81;
      border: 1px solid #0ecb81;
      padding: 2px 8px;
      border-radius: 12px;
      font-weight: 700;
      box-shadow: 0 0 12px rgba(14, 203, 129, 0.35);
      text-shadow: 0 0 6px rgba(14, 203, 129, 0.3);
    }}

    .badge-wa-count {{
      background: rgba(246, 70, 93, 0.16);
      color: #f6465d;
      border: 1px solid #f6465d;
      padding: 2px 8px;
      border-radius: 12px;
      font-weight: 700;
      box-shadow: 0 0 12px rgba(246, 70, 93, 0.35);
      text-shadow: 0 0 6px rgba(246, 70, 93, 0.3);
    }}

    .badge-essay-score {{
      background: rgba(0, 240, 255, 0.12);
      color: #00f0ff;
      border: 1px solid rgba(0, 240, 255, 0.4);
      padding: 2px 8px;
      border-radius: 12px;
      font-weight: 700;
      box-shadow: 0 0 12px rgba(0, 240, 255, 0.3);
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* BUTTONS: ULTRA-LUXURY RGB TRADING SUITE */
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      font-size: 12px;
      font-weight: 600;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: linear-gradient(180deg, #181d29 0%, #10141e 100%);
      color: #e2e8f0;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
      position: relative;
      overflow: hidden;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
    }}

    .btn:hover {{
      background: linear-gradient(180deg, #242b3d 0%, #171c2a 100%);
      color: #ffffff;
      border-color: rgba(240, 185, 11, 0.5);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6), 0 0 12px rgba(240, 185, 11, 0.25);
      transform: translateY(-1px);
    }}

    /* Binance Signature Gold VIP Button */
    .btn-primary {{
      background: linear-gradient(135deg, #f0b90b 0%, #fcd535 50%, #e0a500 100%) !important;
      border: 1px solid #fcd535 !important;
      color: #0b0e14 !important;
      font-weight: 700 !important;
      box-shadow: 0 0 18px rgba(240, 185, 11, 0.4), 0 2px 4px rgba(0, 0, 0, 0.6) !important;
      text-shadow: none !important;
    }}
    .btn-primary:hover {{
      background: linear-gradient(135deg, #ffe066 0%, #f0b90b 100%) !important;
      border-color: #ffe066 !important;
      box-shadow: 0 0 26px rgba(240, 185, 11, 0.65), 0 4px 12px rgba(0, 0, 0, 0.7) !important;
      transform: translateY(-1.5px);
    }}

    /* Trading Long Green RGB Button */
    .btn-success {{
      background: linear-gradient(135deg, #0ecb81 0%, #059669 100%) !important;
      border: 1px solid #0ecb81 !important;
      color: #ffffff !important;
      font-weight: 700 !important;
      box-shadow: 0 0 16px rgba(14, 203, 129, 0.45) !important;
    }}
    .btn-success:hover {{
      background: linear-gradient(135deg, #18e697 0%, #0ecb81 100%) !important;
      box-shadow: 0 0 24px rgba(14, 203, 129, 0.7) !important;
      transform: translateY(-1.5px);
    }}

    /* Trading Short Red RGB Button */
    .btn-danger {{
      background: linear-gradient(135deg, #f6465d 0%, #dc2626 100%) !important;
      border: 1px solid #f6465d !important;
      color: #ffffff !important;
      font-weight: 700 !important;
      box-shadow: 0 0 16px rgba(246, 70, 93, 0.45) !important;
    }}
    .btn-danger:hover {{
      background: linear-gradient(135deg, #ff6075 0%, #f6465d 100%) !important;
      box-shadow: 0 0 24px rgba(246, 70, 93, 0.7) !important;
      transform: translateY(-1.5px);
    }}

    /* Cyber Pro Cyan RGB Button */
    .btn-cyan {{
      background: linear-gradient(135deg, #00f0ff 0%, #0072ff 100%) !important;
      border: 1px solid #00f0ff !important;
      color: #ffffff !important;
      font-weight: 700 !important;
      box-shadow: 0 0 16px rgba(0, 240, 255, 0.45) !important;
    }}
    .btn-cyan:hover {{
      background: linear-gradient(135deg, #33f3ff 0%, #00f0ff 100%) !important;
      box-shadow: 0 0 24px rgba(0, 240, 255, 0.7) !important;
      transform: translateY(-1.5px);
    }}

    .btn-active {{
      background: rgba(0, 240, 255, 0.12) !important;
      border-color: rgba(0, 240, 255, 0.55) !important;
      color: #00f0ff !important;
      box-shadow: 0 0 14px rgba(0, 240, 255, 0.3) !important;
    }}

    /* 2. MAIN 3-COLUMN ARENA */
    .arena-main {{
      flex: 1;
      display: flex;
      overflow: hidden;
      position: relative;
    }}

    /* 2.1 LEFT SIDEBAR */
    .arena-sidebar {{
      width: var(--sidebar-w);
      min-width: var(--sidebar-w);
      background: var(--bg-surface);
      border-right: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    .sidebar-tabs {{
      display: flex;
      background: var(--bg-base);
      border-bottom: 1px solid var(--border-subtle);
    }}

    .s-tab {{
      flex: 1;
      padding: 11px 4px;
      font-size: 11px;
      font-weight: 700;
      text-align: center;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.2s ease;
      letter-spacing: 0.5px;
    }}
    .s-tab:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.03);
    }}
    .s-tab.active {{
      color: #00f0ff;
      border-bottom-color: #00f0ff;
      background: rgba(0, 240, 255, 0.05);
      text-shadow: 0 0 8px rgba(0, 240, 255, 0.4);
    }}

    .sidebar-content {{
      flex: 1;
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
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.3);
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
      height: 6px;
      background: #080a10;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 3px;
      overflow: hidden;
    }}
    .prog-bar {{
      height: 100%;
      background: linear-gradient(90deg, #f0b90b 0%, #0ecb81 100%);
      box-shadow: 0 0 10px rgba(14, 203, 129, 0.5);
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
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 3px;
      border: 1px solid var(--border-subtle);
      background: #10141f;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-btn:hover {{
      background: #182030;
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }}
    .filter-btn.active {{
      background: #182030;
      color: #f0b90b;
      border-color: #f0b90b;
      box-shadow: 0 0 10px rgba(240, 185, 11, 0.25);
    }}

    .cp-matrix-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 5px;
    }}

    .matrix-item {{
      height: 34px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: #0f131d;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 600;
      color: #848e9c;
      cursor: pointer;
      position: relative;
      transition: all 0.15s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .matrix-item:hover {{
      border-color: #f0b90b;
      color: #ffffff;
      transform: translateY(-1.5px);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5), 0 0 10px rgba(240, 185, 11, 0.3);
    }}
    .matrix-item.active {{
      border: 2px solid #00f0ff !important;
      background: #0c1b2b !important;
      color: #00f0ff !important;
      box-shadow: 0 0 16px rgba(0, 240, 255, 0.5) !important;
      text-shadow: 0 0 8px rgba(0, 240, 255, 0.6);
    }}
    .matrix-item.ac {{
      background: rgba(14, 203, 129, 0.16) !important;
      border-color: #0ecb81 !important;
      color: #0ecb81 !important;
      box-shadow: 0 0 10px rgba(14, 203, 129, 0.3);
    }}
    .matrix-item.wa {{
      background: rgba(246, 70, 93, 0.16) !important;
      border-color: #f6465d !important;
      color: #f6465d !important;
      box-shadow: 0 0 10px rgba(246, 70, 93, 0.3);
    }}
    .matrix-item.partial {{
      background: rgba(240, 185, 11, 0.16) !important;
      border-color: #f0b90b !important;
      color: #f0b90b !important;
      box-shadow: 0 0 10px rgba(240, 185, 11, 0.3);
    }}

    /* 2.2 CENTER WORKSPACE */
    .arena-center {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: var(--bg-base);
    }}

    .problem-viewport {{
      flex: 1;
      overflow-y: auto;
      padding: 24px 32px;
      max-width: 980px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .problem-header-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }}

    .problem-title-row {{
      display: flex;
      align-items: baseline;
      gap: 12px;
      margin-bottom: 8px;
    }}
    .problem-id-badge {{
      font-family: var(--font-mono);
      font-size: 16px;
      font-weight: 800;
      color: #00f0ff;
      text-shadow: 0 0 10px rgba(0, 240, 255, 0.4);
    }}
    .problem-title {{
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.01em;
    }}

    .problem-meta-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      font-size: 11.5px;
      color: var(--text-muted);
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 10px;
      margin-top: 8px;
    }}
    .meta-val {{
      font-family: var(--font-mono);
      font-weight: 600;
      color: #ffffff;
    }}

    .statement-section {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 22px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }}
    .section-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #f0b90b;
      margin-bottom: 14px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .statement-text {{
      font-size: 14.5px;
      line-height: 1.75;
      color: #ffffff;
    }}

    /* Options Grid (Trading style) */
    .options-grid {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .cp-option-card {{
      background: #0d111a;
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
    }}
    .cp-option-card:hover {{
      background: #141926;
      border-color: rgba(240, 185, 11, 0.5);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6), 0 0 14px rgba(240, 185, 11, 0.2);
    }}
    .cp-option-card.selected {{
      border-color: #00f0ff !important;
      background: rgba(0, 240, 255, 0.08) !important;
      box-shadow: 0 0 18px rgba(0, 240, 255, 0.35) !important;
    }}
    .cp-option-card.correct {{
      border-color: #0ecb81 !important;
      background: rgba(14, 203, 129, 0.14) !important;
      box-shadow: 0 0 22px rgba(14, 203, 129, 0.45) !important;
    }}
    .cp-option-card.wrong {{
      border-color: #f6465d !important;
      background: rgba(246, 70, 93, 0.14) !important;
      box-shadow: 0 0 22px rgba(246, 70, 93, 0.45) !important;
    }}

    .option-key-badge {{
      width: 28px;
      height: 28px;
      min-width: 28px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.15);
      display: grid;
      place-items: center;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: #848e9c;
      background: #131824;
      transition: all 0.2s ease;
    }}
    .cp-option-card.selected .option-key-badge {{
      border-color: #00f0ff;
      background: linear-gradient(135deg, #00f0ff, #0072ff);
      color: #ffffff;
      box-shadow: 0 0 12px rgba(0, 240, 255, 0.6);
    }}
    .cp-option-card.correct .option-key-badge {{
      border-color: #0ecb81;
      background: linear-gradient(135deg, #0ecb81, #059669);
      color: #ffffff;
      box-shadow: 0 0 14px rgba(14, 203, 129, 0.6);
    }}
    .cp-option-card.wrong .option-key-badge {{
      border-color: #f6465d;
      background: linear-gradient(135deg, #f6465d, #dc2626);
      color: #ffffff;
      box-shadow: 0 0 14px rgba(246, 70, 93, 0.6);
    }}

    .option-text-content {{
      font-size: 14px;
      line-height: 1.6;
      color: #ffffff;
      flex: 1;
    }}

    /* Verdict Banner */
    .verdict-banner {{
      padding: 14px 18px;
      border-radius: var(--radius-sm);
      display: flex;
      flex-direction: column;
      gap: 4px;
      animation: fadeIn 0.2s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(-4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .verdict-banner.ac {{
      background: linear-gradient(90deg, rgba(14, 203, 129, 0.18) 0%, rgba(14, 203, 129, 0.04) 100%);
      border: 1px solid rgba(14, 203, 129, 0.5);
      box-shadow: 0 0 20px rgba(14, 203, 129, 0.3);
    }}
    .verdict-banner.wa {{
      background: linear-gradient(90deg, rgba(246, 70, 93, 0.18) 0%, rgba(246, 70, 93, 0.04) 100%);
      border: 1px solid rgba(246, 70, 93, 0.5);
      box-shadow: 0 0 20px rgba(246, 70, 93, 0.3);
    }}
    .verdict-title {{
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 13.5px;
    }}
    .verdict-banner.ac .verdict-title {{
      color: #0ecb81;
      text-shadow: 0 0 10px rgba(14, 203, 129, 0.4);
    }}
    .verdict-banner.wa .verdict-title {{
      color: #f6465d;
      text-shadow: 0 0 10px rgba(246, 70, 93, 0.4);
    }}
    .verdict-meta {{
      font-size: 11.5px;
      color: var(--text-muted);
    }}

    /* Official Editorial Card */
    .editorial-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }}
    .editorial-header {{
      padding: 12px 18px;
      background: #111522;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: background 0.15s ease;
    }}
    .editorial-header:hover {{
      background: #161b2a;
    }}
    .editorial-title {{
      font-size: 12px;
      font-weight: 700;
      color: #f0b90b;
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: 0.5px;
    }}
    .editorial-body {{
      padding: 18px;
      font-size: 13.5px;
      line-height: 1.7;
      color: #eaecef;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    /* 4 ELI5 BLOCKS WITH GLOWING ACCENTS */
    .eli5-block {{
      padding: 14px 16px;
      border-radius: var(--radius-sm);
      border-left: 3px solid #00f0ff;
      background: rgba(0, 240, 255, 0.05);
      box-shadow: 0 0 14px rgba(0, 240, 255, 0.1);
    }}
    .eli5-block.math {{
      border-left-color: #0ecb81;
      background: rgba(14, 203, 129, 0.05);
      box-shadow: 0 0 14px rgba(14, 203, 129, 0.1);
    }}
    .eli5-block.trap {{
      border-left-color: #f0b90b;
      background: rgba(240, 185, 11, 0.05);
      box-shadow: 0 0 14px rgba(240, 185, 11, 0.1);
    }}
    .eli5-block.ref {{
      border-left-color: #b026ff;
      background: rgba(176, 38, 255, 0.05);
      box-shadow: 0 0 14px rgba(176, 38, 255, 0.1);
    }}

    /* Bottom Navigation Bar */
    .arena-footer {{
      height: var(--footer-h);
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 30;
      box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.4);
    }}

    /* 2.3 RIGHT INSPECTOR PANEL */
    .arena-inspector {{
      width: var(--inspector-w);
      min-width: var(--inspector-w);
      background: var(--bg-surface);
      border-left: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transition: margin-right 0.25s ease;
    }}
    .arena-inspector.collapsed {{
      margin-right: calc(-1 * var(--inspector-w));
    }}

    .inspector-top-bar {{
      padding: 10px 14px;
      background: var(--bg-base);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .inspector-title-group {{
      display: flex;
      flex-direction: column;
    }}
    .inspector-eyebrow {{
      font-size: 9.5px;
      font-weight: 700;
      color: #00f0ff;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      text-shadow: 0 0 6px rgba(0, 240, 255, 0.4);
    }}
    .inspector-title {{
      font-size: 13px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.4px;
    }}

    .inspector-tabs {{
      display: flex;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-subtle);
    }}
    .i-tab {{
      flex: 1;
      padding: 10px 4px;
      font-size: 11px;
      font-weight: 700;
      text-align: center;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.2s ease;
      white-space: nowrap;
      letter-spacing: 0.4px;
    }}
    .i-tab:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.03);
    }}
    .i-tab.active {{
      color: #f0b90b !important;
      border-bottom-color: #f0b90b !important;
      background: rgba(240, 185, 11, 0.06) !important;
      text-shadow: 0 0 10px rgba(240, 185, 11, 0.4);
    }}

    .inspector-content {{
      flex: 1;
      overflow-y: auto;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* Formula Box */
    .cp-formula-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }}
    .formula-title {{
      font-size: 11.5px;
      font-weight: 700;
      color: #00f0ff;
      letter-spacing: 0.4px;
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
      transition: transform 0.3s ease, opacity 0.3s ease;
    }}
    .video-thumb-box:hover .video-thumb-img {{
      transform: scale(1.04);
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
      background: rgba(0, 0, 0, 0.35);
    }}
    .play-btn-circle {{
      width: 46px;
      height: 46px;
      background: linear-gradient(135deg, #f0b90b, #e0a500);
      border-radius: 50%;
      display: grid;
      place-items: center;
      color: #000000;
      font-size: 17px;
      box-shadow: 0 0 20px rgba(240, 185, 11, 0.65);
    }}
    .timestamp-badge {{
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.9);
      color: #f0b90b;
      font-family: var(--font-mono);
      font-size: 10.5px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 3px;
      border: 1px solid rgba(240, 185, 11, 0.4);
    }}

    /* KaTeX Safe Styles */
    .katex-display {{
      margin: 0.6em 0 !important;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 4px 0;
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

    /* Responsive */
    @media (max-width: 1200px) {{
      .arena-inspector {{
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        z-index: 50;
        box-shadow: -8px 0 24px rgba(0, 0, 0, 0.7);
      }}
    }}
  </style>"""

content = content[:start_idx] + new_style_block + content[end_idx:]
print("[OK] Replaced <style> with Luxury Binance Pro RGB Dark Theme")

# Replace header contest badge with Binance Pro label
old_badge = '<span class="contest-badge">OLP-AI-2026</span>'
new_badge = '<span class="contest-badge"><span>⚡</span> OLP AI 2026 · PRO ARENA</span>'
if old_badge in content:
    content = content.replace(old_badge, new_badge)
    print("[OK] Updated contest badge to Pro Arena")

# Replace ticker total score element to use ticker-gold-val class
old_ticker_score = '<strong style="color:#60a5fa;" id="tickerTotalScore">0.0 / 100.0đ</strong>'
new_ticker_score = '<strong class="ticker-gold-val" id="tickerTotalScore">0.0 / 100.0đ</strong>'
if old_ticker_score in content:
    content = content.replace(old_ticker_score, new_ticker_score)
    print("[OK] Updated ticker total score styling")

# Replace code self score buttons to give them proper RGB status colors
old_code_buttons = """                ${{[0, 2, 4, 5, 7].map(pt => `
                  <button class="btn ${{curCodePts === pt ? 'btn-primary' : ''}}" style="height:26px; font-size:11px;" onclick="setCodeSelfScore('${{q.id}}', ${{pt}})">
                    ${{pt}}.0đ ${{pt === q.points ? '(Full AC)' : pt === 0 ? '(Chưa làm)' : '(Một phần)'}}
                  </button>
                `).join('')}}"""

new_code_buttons = """                ${{[0, 2, 4, 5, 7].map(pt => {{
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
                }}).join('')}}"""

if old_code_buttons in content:
    content = content.replace(old_code_buttons, new_code_buttons)
    print("[OK] Updated code self scoring buttons with RGB classes")

# Update colors in problem header meta
old_meta_pts = '<span class="meta-val" style="color:#60a5fa;">${{q.points}} điểm</span>'
new_meta_pts = '<span class="meta-val" style="color:#f0b90b; font-weight:700;">${{q.points}} điểm</span>'
if old_meta_pts in content:
    content = content.replace(old_meta_pts, new_meta_pts)
    print("[OK] Updated problem meta points color to Gold")

with open(GEN_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Successfully updated docs/generate_full_hub.py with Luxury Binance Trading RGB Dark Theme!")
