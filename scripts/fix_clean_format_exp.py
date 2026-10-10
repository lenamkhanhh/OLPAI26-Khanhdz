# -*- coding: utf-8 -*-
import os
import sys
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

def fix():
    script_path = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_func = '''    // Format Explanation into 4 Beautiful Blocks
    function formatExplanationHtml(expText) {{
      if (!expText) return '<div class="eli5-block" style="color:var(--text-muted); font-style:italic;">Đang cập nhật lời giải chi tiết.</div>';

      function mdToHtml(str) {{
        if (!str) return '';
        let s = str.trim();
        s = s.replace(/\\*\\*([^\\*]+)\\*\\*/g, '<strong>$1</strong>');
        const lines = s.split(String.fromCharCode(10));
        let inList = false;
        let res = [];
        for (let line of lines) {{
          let trimmed = line.trim();
          if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {{
            if (!inList) {{
              res.push('<ul style="margin:6px 0; padding-left:20px; line-height:1.6;">');
              inList = true;
            }}
            res.push('<li>' + trimmed.substring(2) + '</li>');
          }} else {{
            if (inList) {{
              res.push('</ul>');
              inList = false;
            }}
            if (trimmed) {{
              res.push('<p style="margin:6px 0; line-height:1.6;">' + trimmed + '</p>');
            }}
          }}
        }}
        if (inList) res.push('</ul>');
        return res.join('');
      }}

      // Đề 02 & 03: Phân tách theo Markdown ### 1., ### 2., ### 3., ### 4.
      if (expText.indexOf('### 1.') !== -1 || expText.indexOf('### 2.') !== -1) {{
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
          }} else if (header.indexOf('2.') !== -1 || header.toLowerCase().indexOf('đạo hàm') !== -1 || header.toLowerCase().indexOf('chứng minh') !== -1 || header.toLowerCase().indexOf('toán') !== -1) {{
            cls = 'eli5-block math';
            titleColor = '#34d399';
            icon = '📐';
          }} else if (header.indexOf('3.') !== -1 || header.toLowerCase().indexOf('bẫy') !== -1 || header.toLowerCase().indexOf('sai') !== -1) {{
            cls = 'eli5-block trap';
            titleColor = '#fbbf24';
            icon = '⚠️';
          }} else if (header.indexOf('4.') !== -1 || header.toLowerCase().indexOf('căn cứ') !== -1 || header.toLowerCase().indexOf('lý thuyết') !== -1 || header.toLowerCase().indexOf('ứng dụng') !== -1) {{
            cls = 'eli5-block ref';
            titleColor = '#a78bfa';
            icon = '📚';
          }}

          out += '<div class="' + cls + '" style="margin-top:10px;">' +
            '<div style="font-weight:700; color:' + titleColor + '; margin-bottom:6px;">' + icon + ' [' + header + ']</div>' +
            '<div style="font-size:13px; line-height:1.6;">' + mdToHtml(body) + '</div>' +
          '</div>';
        }}
        return out || '<div class="eli5-block">' + mdToHtml(expText) + '</div>';
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
        out += '<div class="eli5-block">' +
          '<div style="font-weight:700; color:#60a5fa; margin-bottom:6px;">👶 [ELI5 — Giải thích như cho em bé]</div>' +
          '<div style="font-size:13px; line-height:1.6;">' + mdToHtml(p1) + '</div>' +
        '</div>';
      }}
      if (p2) {{
        out += '<div class="eli5-block math" style="margin-top:10px;">' +
          '<div style="font-weight:700; color:#34d399; margin-bottom:6px;">📐 [Đạo hàm & Luận chứng Step-by-Step]</div>' +
          '<div style="font-size:13px; line-height:1.6;">' + mdToHtml(p2) + '</div>' +
        '</div>';
      }}
      if (p3) {{
        out += '<div class="eli5-block trap" style="margin-top:10px;">' +
          '<div style="font-weight:700; color:#fbbf24; margin-bottom:6px;">⚠️ [Phân tích Bẫy đề thi & Các phương án sai]</div>' +
          '<div style="font-size:13px; line-height:1.6;">' + mdToHtml(p3) + '</div>' +
        '</div>';
      }}
      if (p4) {{
        out += '<div class="eli5-block ref" style="margin-top:10px;">' +
          '<div style="font-weight:700; color:#a78bfa; margin-bottom:6px;">📚 [Căn cứ lý thuyết & Ứng dụng thực tế]</div>' +
          '<div style="font-size:13px; line-height:1.6;">' + mdToHtml(p4) + '</div>' +
        '</div>';
      }}
      return out || '<div class="eli5-block"><div style="font-size:13px; line-height:1.6;">' + mdToHtml(expText) + '</div></div>';
    }}'''

    pattern = r'// Format Explanation into 4 Beautiful Blocks[\s\S]*?return out \|\| `[\s\S]*?`\;\s*\}\}'
    content = re.sub(pattern, lambda m: new_func, content)

    with open(script_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced formatExplanationHtml with clean escaping-free version")

if __name__ == "__main__":
    fix()
