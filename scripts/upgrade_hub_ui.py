# -*- coding: utf-8 -*-
"""
scripts/upgrade_hub_ui.py
Nâng cấp giao diện Luận giải 4 khối và Hiển thị Rubric/ModelAnswer trong docs/generate_full_hub.py
"""

import os
import sys
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

def upgrade():
    gen_file = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")
    with open(gen_file, "r", encoding="utf-8") as f:
        code = f.read()

    # Sửa q.points.0 thành q.points
    code = code.replace("${{q.points}}.0 điểm", "${{q.points}} điểm")
    code = code.replace("+${{q.points}}.0đ", "+${{q.points}}đ")

    # Hàm formatExplanationHtml toàn diện
    new_format_exp = '''    // Format Explanation into 4 Beautiful Blocks (Supports both ### 1. Markdown and Emoji style)
    function formatExplanationHtml(expText) {{
      if (!expText) return '<div class="eli5-block" style="color:var(--text-muted); font-style:italic;">Đang cập nhật lời giải chi tiết.</div>';

      function mdToHtml(str) {{
        if (!str) return '';
        let s = str.trim();
        s = s.replace(/\\*\\*([^\\*]+)\\*\\*/g, '<strong>$1</strong>');
        const lines = s.split('\\n');
        let inList = false;
        let res = [];
        for (let line of lines) {{
          let trimmed = line.trim();
          if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {{
            if (!inList) {{
              res.push('<ul style="margin:6px 0; padding-left:20px; line-height:1.6;">');
              inList = true;
            }}
            res.push(`<li>${{trimmed.substring(2)}}</li>`);
          }} else {{
            if (inList) {{
              res.push('</ul>');
              inList = false;
            }}
            if (trimmed) {{
              res.push(`<p style="margin:6px 0; line-height:1.6;">${{trimmed}}</p>`);
            }}
          }}
        }}
        if (inList) res.push('</ul>');
        return res.join('');
      }}

      // Đề 02 & 03: Phân tách theo Markdown ### 1., ### 2., ### 3., ### 4.
      if (expText.indexOf('### 1.') !== -1 || expText.indexOf('### 2.') !== -1) {{
        const sections = expText.split(/(?=###\\s+\\d+\\.)/);
        let out = '';
        for (let sec of sections) {{
          let trimmed = sec.trim();
          if (!trimmed) continue;
          let header = '';
          let body = trimmed;
          const m = trimmed.match(/^###\\s+(\\d+\\.[^\\n]+)\\n([\\s\\S]*)$/);
          if (m) {{
            header = m[1].trim();
            body = m[2].trim();
          }}
          let cls = 'eli5-block';
          let titleColor = '#60a5fa';
          let icon = '👶';
          if (header.includes('1.') || header.toLowerCase().includes('eli5')) {{
            cls = 'eli5-block';
            titleColor = '#60a5fa';
            icon = '👶';
          }} else if (header.includes('2.') || header.toLowerCase().includes('đạo hàm') || header.toLowerCase().includes('chứng minh') || header.toLowerCase().includes('toán')) {{
            cls = 'eli5-block math';
            titleColor = '#34d399';
            icon = '📐';
          }} else if (header.includes('3.') || header.toLowerCase().includes('bẫy') || header.toLowerCase().includes('sai')) {{
            cls = 'eli5-block trap';
            titleColor = '#fbbf24';
            icon = '⚠️';
          }} else if (header.includes('4.') || header.toLowerCase().includes('căn cứ') || header.toLowerCase().includes('lý thuyết') || header.toLowerCase().includes('ứng dụng')) {{
            cls = 'eli5-block ref';
            titleColor = '#a78bfa';
            icon = '📚';
          }}

          out += `
            <div class="${{cls}}" style="margin-top:10px;">
              <div style="font-weight:700; color:${{titleColor}}; margin-bottom:6px;">${{icon}} [${{header || 'Luận chứng'}}]</div>
              <div style="font-size:13px; line-height:1.6;">${{mdToHtml(body)}}</div>
            </div>
          `;
        }}
        return out;
      }}

      // Đề 01: Phân tách theo Emoji (👶, 📐, ⚠️, 📚)
      let p1 = '', p2 = '', p3 = '', p4 = '';
      if (expText.indexOf('👶') !== -1) {{
        const partsBaby = expText.split('👶');
        if (partsBaby.length > 1) {{
          const rem = partsBaby[1];
          p1 = (rem.indexOf('📐') !== -1) ? rem.split('📐')[0] : rem;
        }}
      }} else {{
        p1 = expText;
      }}

      if (expText.indexOf('📐') !== -1) {{
        const partsMath = expText.split('📐');
        if (partsMath.length > 1) {{
          const rem = partsMath[1];
          p2 = (rem.indexOf('⚠️') !== -1) ? rem.split('⚠️')[0] : rem;
        }}
      }}

      if (expText.indexOf('⚠️') !== -1) {{
        const partsTrap = expText.split('⚠️');
        if (partsTrap.length > 1) {{
          const rem = partsTrap[1];
          p3 = (rem.indexOf('📚') !== -1) ? rem.split('📚')[0] : rem;
        }}
      }}

      if (expText.indexOf('📚') !== -1) {{
        const partsRef = expText.split('📚');
        if (partsRef.length > 1) {{
          p4 = partsRef[1];
        }}
      }}

      p1 = p1.replace(/\\*\\*\\[ELI5[^\\]]*\\]:\\*\\*/g, '').replace(/\\[ELI5[^\\]]*\\]:?/g, '').trim();
      p2 = p2.replace(/\\*\\*\\[Đạo hàm[^\\]]*\\]:\\*\\*/g, '').replace(/\\[Đạo hàm[^\\]]*\\]:?/g, '').trim();
      p3 = p3.replace(/\\*\\*\\[Phân tích[^\\]]*\\]:\\*\\*/g, '').replace(/\\[Phân tích[^\\]]*\\]:?/g, '').trim();
      p4 = p4.replace(/\\*\\*\\[Căn cứ[^\\]]*\\]:\\*\\*/g, '').replace(/\\[Căn cứ[^\\]]*\\]:?/g, '').trim();

      let out = '';
      if (p1) {{
        out += `<div class="eli5-block">
          <div style="font-weight:700; color:#60a5fa; margin-bottom:6px;">👶 [ELI5 — Giải thích như cho em bé]</div>
          <div style="font-size:13px; line-height:1.6;">${{mdToHtml(p1)}}</div>
        </div>`;
      }}
      if (p2) {{
        out += `<div class="eli5-block math" style="margin-top:10px;">
          <div style="font-weight:700; color:#34d399; margin-bottom:6px;">📐 [Đạo hàm & Luận chứng Step-by-Step]</div>
          <div style="font-size:13px; line-height:1.6;">${{mdToHtml(p2)}}</div>
        </div>`;
      }}
      if (p3) {{
        out += `<div class="eli5-block trap" style="margin-top:10px;">
          <div style="font-weight:700; color:#fbbf24; margin-bottom:6px;">⚠️ [Phân tích Bẫy đề thi & Các phương án sai]</div>
          <div style="font-size:13px; line-height:1.6;">${{mdToHtml(p3)}}</div>
        </div>`;
      }}
      if (p4) {{
        out += `<div class="eli5-block ref" style="margin-top:10px;">
          <div style="font-weight:700; color:#a78bfa; margin-bottom:6px;">📚 [Căn cứ lý thuyết & Ứng dụng thực tế]</div>
          <div style="font-size:13px; line-height:1.6;">${{mdToHtml(p4)}}</div>
        </div>`;
      }}
      return out || `<div class="eli5-block"><div style="font-size:13px; line-height:1.6;">${{mdToHtml(expText)}}</div></div>`;
    }}'''

    # Thay thế hàm formatExplanationHtml cũ
    pattern_exp = r'// Format Explanation into 4 Beautiful Blocks[\s\S]*?return out;\s*\}\}'
    code = re.sub(pattern_exp, lambda m: new_format_exp, code)

    # Hiển thị Rubric tiêu chí thực tế trong Inspector
    rubric_display_hook = '''            ${{q.rubric && Array.isArray(q.rubric) && q.rubric.length > 0 ? `
              <div style="margin-top:8px; display:flex; flex-direction:column; gap:6px;">
                <div style="font-size:11px; font-weight:700; color:#60a5fa; text-transform:uppercase;">5 TIÊU CHÍ RUBRIC CHÍNH THỨC (${{q.points}} ĐIỂM):</div>
                ${{q.rubric.map(r => `
                  <div style="font-size:11px; color:var(--text-secondary); background:rgba(0,0,0,0.25); padding:6px 8px; border-radius:4px; border-left:2px solid #3b82f6; line-height:1.4;">
                    ${{sanitizeTex(r)}}
                  </div>
                `).join('')}}
              </div>
            ` : ''}}'''

    old_rubric_header = '''            <div style="font-weight:700; font-size:12px; color:#93c5fd;">HỆ THỐNG ĐÁNH GIÁ THEO TIÊU CHÍ RUBRIC</div>
            <p style="font-size:11px; color:var(--text-muted); line-height:1.5;">
              Hội đồng đánh giá đối chiếu bài làm với 5 tiêu chí chuẩn: Nhận diện bài toán, Lựa chọn kiến trúc mô hình, Pipeline chống rò rỉ dữ liệu, Chỉ số đánh giá và Phương án mở rộng thực tế.
            </p>'''

    new_rubric_header = old_rubric_header + '\n' + rubric_display_hook
    code = code.replace(old_rubric_header, new_rubric_header)

    with open(gen_file, "w", encoding="utf-8") as f:
        f.write(code)
    print("Nâng cấp giao diện docs/generate_full_hub.py thành công!")

if __name__ == "__main__":
    upgrade()
