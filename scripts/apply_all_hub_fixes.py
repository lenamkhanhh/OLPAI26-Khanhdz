# -*- coding: utf-8 -*-
"""
Script scripts/apply_all_hub_fixes.py
Áp dụng toàn diện các sửa đổi cho docs/generate_full_hub.py:
- KaTeX sync scripts + CDN fallback
- renderMath delimiters
- formatExplanationHtml an toàn tuyệt đối
- formatTheoryMarkdown + renderSplitContent với Section Selector
- renderMath cho mọi tab và container
"""

import os

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
gen_path = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")

with open(gen_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Khối KaTeX trong <head>
old_head = '''  <!-- KaTeX CSS (Local + Fallback CDN) -->
  <link rel="stylesheet" href="katex/katex.min.css">
  
  <!-- KaTeX Script (Local + Fallback CDN) -->
  <script defer src="katex/katex.min.js"></script>
  <script defer src="katex/contrib/auto-render.min.js"></script>'''

new_head = '''  <!-- KaTeX CSS (Local + Fallback CDN) -->
  <link rel="stylesheet" href="katex/katex.min.css" onerror="this.onerror=null;this.href='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css'">
  
  <!-- KaTeX Script (Local + Fallback CDN) -->
  <script src="katex/katex.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js'"></script>
  <script src="katex/contrib/auto-render.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js'"></script>'''

if old_head in code:
    code = code.replace(old_head, new_head)
    print("✓ Đã cập nhật KaTeX trong <head>")
elif new_head in code:
    print("✓ KaTeX trong <head> đã là phiên bản mới")

# 2. Khối tiêu đề Split Pane
old_sp_head = '''        <div style="display:flex; align-items:center; gap:6px;">
          <span style="font-size:11px; font-weight:700; color:var(--text-secondary); text-transform:uppercase;">Tra cứu song song:</span>
          <button class="btn" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('pdf')">PDF Handbook</button>
          <button class="btn" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('theory')">Giáo trình</button>
          <button class="btn" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('formulas')">Công thức</button>
        </div>'''

new_sp_head = '''        <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
          <span style="font-size:11px; font-weight:700; color:var(--text-secondary); text-transform:uppercase;">Tra cứu song song:</span>
          <button class="btn" id="btnSplitPdf" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('pdf')">PDF Handbook</button>
          <button class="btn" id="btnSplitTheory" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('theory')">Giáo trình</button>
          <button class="btn" id="btnSplitFormulas" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('formulas')">Công thức</button>
          <select id="splitTheorySecSelect" style="height:22px; font-size:10.5px; background:#141414; color:#f0b90b; border:1px solid var(--border-subtle); border-radius:3px; padding:0 4px; display:none;" onchange="switchTheorySection(this.value)" title="Chọn chuyên đề lý thuyết để tra cứu"></select>
        </div>'''

if old_sp_head in code:
    code = code.replace(old_sp_head, new_sp_head)
    print("✓ Đã cập nhật thanh tiêu đề Split Pane")

# 3. Khối renderMath
new_render_math_code = '''    function renderMath(targetEl) {{
      const el = targetEl || document.body;
      const doRender = () => {{
        if (window.renderMathInElement) {{
          try {{
            renderMathInElement(el, {{
              delimiters: [
                {{ left: '$$', right: '$$', display: true }},
                {{ left: '$', right: '$', display: false }},
                {{ left: '\\\\[', right: '\\\\]', display: true }},
                {{ left: '\\\\(', right: '\\\\)', display: false }}
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
    }}'''

idx_rm_start = code.find('function renderMath(targetEl) {{')
idx_rm_end = code.find('// Navigation\n    function jumpToQuestion(')
if idx_rm_start != -1 and idx_rm_end != -1:
    code = code[:idx_rm_start] + new_render_math_code + "\n\n    " + code[idx_rm_end:]
    print("✓ Đã thay thế renderMath thành công")

# 4. Khối formatExplanationHtml
new_exp_code = '''// Format Explanation into 4 Beautiful Blocks
    function formatExplanationHtml(expText) {{
      if (!expText) return '<div class="eli5-block" style="color:var(--text-muted); font-style:italic;">Đang cập nhật lời giải chi tiết.</div>';

      function safeMdToHtml(str) {{
        if (!str) return '';
        const mathBlocks = [];
        
        // 1. Protect Display Math: $$...$$
        let s = str.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (m) => {{
          const idx = mathBlocks.length;
          const safeM = m.replace(/</g, '&lt;').replace(/>/g, '&gt;');
          mathBlocks.push(safeM);
          return '%%%MATH_DISP_' + idx + '%%%';
        }});

        // 2. Protect Inline Math: $...$
        const inlReg = new RegExp('\\\\$([^$\\\\n\\\\r]+?)\\\\$', 'g');
        s = s.replace(inlReg, (m) => {{
          const idx = mathBlocks.length;
          const safeM = m.replace(/</g, '&lt;').replace(/>/g, '&gt;');
          mathBlocks.push(safeM);
          return '%%%MATH_INL_' + idx + '%%%';
        }});

        // 3. Bold & Code
        s = s.replace(/\\*\\*([^\\*]+)\\*\\*/g, '<strong>$1</strong>');
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
          }} else if (/^\\d+\\.\\s/.test(trimmed)) {{
            if (!inList) {{
              res.push('<ol style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
              inList = true;
            }}
            res.push('<li style="margin-bottom:4px;">' + trimmed.replace(/^\\d+\\.\\s*/, '') + '</li>');
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
    }}'''

idx_exp_start = code.find('// Format Explanation into 4 Beautiful Blocks')
idx_exp_end = code.find('// Render Center Viewport\n    function renderCenter() {{')
if idx_exp_start != -1 and idx_exp_end != -1:
    code = code[:idx_exp_start] + new_exp_code + "\n\n    " + code[idx_exp_end:]
    print("✓ Đã thay thế formatExplanationHtml thành công")

# 5. Khối formatTheoryMarkdown và renderSplitContent
new_split_code = '''let currentTheorySecId = '§1.1';
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
      let s = mdText.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (match) => {{
        const idx = mathPlaceholders.length;
        const safeTex = match.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        mathPlaceholders.push(safeTex);
        return '%%%MATH_DISPLAY_' + idx + '%%%';
      }});

      // 2. Protect Inline Math: $...$
      const inlReg = new RegExp('\\\\$([^$\\\\n\\\\r]+?)\\\\$', 'g');
      s = s.replace(inlReg, (match) => {{
        const idx = mathPlaceholders.length;
        const safeTex = match.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        mathPlaceholders.push(safeTex);
        return '%%%MATH_INLINE_' + idx + '%%%';
      }});

      // 3. Bold, Code, Headers
      s = s.replace(/\\*\\*([^\\*]+)\\*\\*/g, '<strong>$1</strong>');
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
        }} else if (/^\\d+\\.\\s/.test(trimmed)) {{
          if (!inList) {{
            res.push('<ol style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
            inList = true;
          }}
          res.push('<li style="margin-bottom:4px;">' + trimmed.replace(/^\\d+\\.\\s*/, '') + '</li>');
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
          const matchSec = q.explanation.match(/§[\\d\\.]+/);
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
    }}'''

idx_split_start = code.find('function renderSplitContent() {{')
if idx_split_start == -1:
    idx_split_start = code.find('let currentTheorySecId = ')
idx_split_end = code.find('// Rubric Evaluator & Checklist (Tự đối chiếu thật - P0-1)\n    function toggleRubricCriterion(')
if idx_split_start != -1 and idx_split_end != -1:
    code = code[:idx_split_start] + new_split_code + "\n\n    " + code[idx_split_end:]
    print("✓ Đã thay thế formatTheoryMarkdown và renderSplitContent thành công")

with open(gen_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Hoàn tất cập nhật docs/generate_full_hub.py!")
