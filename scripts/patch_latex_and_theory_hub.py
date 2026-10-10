# -*- coding: utf-8 -*-
"""
Script scripts/patch_latex_and_theory_hub.py
Sửa dứt điểm hiển thị LaTeX và giao diện Giáo trình/Luận giải trong docs/generate_full_hub.py:
1. Đồng bộ KaTeX sync loading kèm CDN fallback (bỏ defer tránh race condition).
2. Bổ sung đầy đủ 4 delimiters KaTeX: $$, $, \\[, \\(.
3. Thêm bộ parser Markdown formatTheoryMarkdown(mdText) với math protection, callout box ⭐.
4. Thêm Section Selector trong Cửa sổ tra cứu song song (chuyển đổi nhanh 30+ mục giáo trình).
5. Gọi renderMath(container) sau TẤT CẢ các thao tác cập nhật DOM (split pane, explanation, rubric, formulas).
6. formatExplanationHtml an toàn tuyệt đối với math chứa <, > và phân tách 4 khối chuẩn màu sắc Binance Jet Black.
"""

import os
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
gen_path = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")

with open(gen_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Thay thế KaTeX script trong <head>
old_head_katex = '''  <!-- KaTeX CSS (Local + Fallback CDN) -->
  <link rel="stylesheet" href="katex/katex.min.css">
  
  <!-- KaTeX Script (Local + Fallback CDN) -->
  <script defer src="katex/katex.min.js"></script>
  <script defer src="katex/contrib/auto-render.min.js"></script>'''

new_head_katex = '''  <!-- KaTeX CSS (Local + Fallback CDN) -->
  <link rel="stylesheet" href="katex/katex.min.css" onerror="this.onerror=null;this.href='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css'">
  
  <!-- KaTeX Script (Local + Fallback CDN) -->
  <script src="katex/katex.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js'"></script>
  <script src="katex/contrib/auto-render.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js'"></script>'''

if old_head_katex in code:
    code = code.replace(old_head_katex, new_head_katex)
    print("✓ Đã cập nhật KaTeX scripts trong <head> (Synchronous + Fallback CDN)")
else:
    print("! Không tìm thấy khối old_head_katex chuẩn, thử regex...")
    code = re.sub(
        r'<link rel="stylesheet" href="katex/katex\.min\.css">[\s\S]*?<script defer src="katex/contrib/auto-render\.min\.js"></script>',
        new_head_katex,
        code
    )

# 2. Cập nhật thanh tiêu đề Split Pane với Section Selector
old_split_header = '''        <div style="display:flex; align-items:center; gap:6px;">
          <span style="font-size:11px; font-weight:700; color:var(--text-secondary); text-transform:uppercase;">Tra cứu song song:</span>
          <button class="btn" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('pdf')">PDF Handbook</button>
          <button class="btn" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('theory')">Giáo trình</button>
          <button class="btn" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('formulas')">Công thức</button>
        </div>'''

new_split_header = '''        <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
          <span style="font-size:11px; font-weight:700; color:var(--text-secondary); text-transform:uppercase;">Tra cứu song song:</span>
          <button class="btn" id="btnSplitPdf" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('pdf')">PDF Handbook</button>
          <button class="btn" id="btnSplitTheory" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('theory')">Giáo trình</button>
          <button class="btn" id="btnSplitFormulas" style="height:22px; font-size:10px; padding:0 6px;" onclick="setSplitType('formulas')">Công thức</button>
          <select id="splitTheorySecSelect" style="height:22px; font-size:10.5px; background:#141414; color:#f0b90b; border:1px solid var(--border-subtle); border-radius:3px; padding:0 4px; display:none;" onchange="switchTheorySection(this.value)" title="Chọn chuyên đề lý thuyết để tra cứu"></select>
        </div>'''

if old_split_header in code:
    code = code.replace(old_split_header, new_split_header)
    print("✓ Đã cập nhật thanh tiêu đề Split Pane với Section Selector Dropdown")
else:
    print("! Không tìm thấy old_split_header, tìm cách thay thế...")

# 3. Cập nhật renderMath
old_render_math = '''    function renderMath(targetEl) {
      const el = targetEl || document.body;
      const doRender = () => {
        if (window.renderMathInElement) {
          try {
            renderMathInElement(el, {
              delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false }
              ],
              ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
              throwOnError: false,
              strict: false
            });
          } catch(err) {
            console.warn('KaTeX render warning:', err);
          }
        }
      };

      if (window.renderMathInElement) {
        doRender();
      } else {
        let count = 0;
        const it = setInterval(() => {
          count++;
          if (window.renderMathInElement) {
            clearInterval(it);
            doRender();
          } else if (count > 25) {
            clearInterval(it);
          }
        }, 100);
      }
    }'''

new_render_math = '''    function renderMath(targetEl) {
      const el = targetEl || document.body;
      const doRender = () => {
        if (window.renderMathInElement) {
          try {
            renderMathInElement(el, {
              delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false },
                { left: '\\\\[', right: '\\\\]', display: true },
                { left: '\\\\(', right: '\\\\)', display: false }
              ],
              ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
              throwOnError: false,
              strict: false
            });
          } catch(err) {
            console.warn('KaTeX render warning:', err);
          }
        }
      };

      if (window.renderMathInElement) {
        doRender();
      } else {
        let count = 0;
        const it = setInterval(() => {
          count++;
          if (window.renderMathInElement) {
            clearInterval(it);
            doRender();
          } else if (count > 30) {
            clearInterval(it);
          }
        }, 50);
      }
    }'''

if old_render_math in code:
    code = code.replace(old_render_math, new_render_math)
    print("✓ Đã mở rộng KaTeX delimiters ($, $$, \\[, \\() và tăng tốc interval")
else:
    print("! Thay thế renderMath theo regex...")
    code = re.sub(
        r'function renderMath\(targetEl\)[\s\S]*?setInterval\(\(\) => \{[\s\S]*?\}, 100\);\s*\}\s*\}',
        new_render_math,
        code
    )

# 4. Thêm formatTheoryMarkdown và cập nhật renderSplitContent
new_theory_and_split_code = '''    let currentTheorySecId = '§1.1';
    let currentTheorySecIdUserSelected = false;

    function switchTheorySection(secId) {
      currentTheorySecId = secId;
      currentTheorySecIdUserSelected = true;
      renderSplitContent();
    }

    // Beautiful Theory Markdown Parser with Full Math & Callout Protection
    function formatTheoryMarkdown(mdText) {
      if (!mdText) return '';
      const mathPlaceholders = [];

      // 1. Protect Display Math: $$...$$
      let s = mdText.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (match) => {
        const idx = mathPlaceholders.length;
        const safeTex = match.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        mathPlaceholders.push(safeTex);
        return '%%%MATH_DISPLAY_' + idx + '%%%';
      });

      // 2. Protect Inline Math: $...$
      s = s.replace(/\\$([^\\$\\n]+?)\\$/g, (match) => {
        const idx = mathPlaceholders.length;
        const safeTex = match.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        mathPlaceholders.push(safeTex);
        return '%%%MATH_INLINE_' + idx + '%%%';
      });

      // 3. Bold, Code, Headers
      s = s.replace(/\\*\\*([^\\*]+)\\*\\*/g, '<strong>$1</strong>');
      s = s.replace(/`([^`]+)`/g, '<code style="background:rgba(255,255,255,0.08); padding:1px 5px; border-radius:3px; font-family:var(--font-mono); font-size:12px; color:#f0b90b;">$1</code>');

      // 4. Lines, Lists, Callouts
      const lines = s.split(String.fromCharCode(10));
      const res = [];
      let inList = false;
      let inVipCard = false;

      for (let line of lines) {
        let trimmed = line.trim();
        if (!trimmed) {
          if (inList) { res.push('</ul>'); inList = false; }
          continue;
        }

        // Special Callout: Hay ra thi
        if (trimmed.indexOf('⭐') !== -1 || trimmed.indexOf('Hay ra thi') !== -1) {
          if (inList) { res.push('</ul>'); inList = false; }
          if (inVipCard) { res.push('</div>'); inVipCard = false; }
          res.push('<div style="background:rgba(240, 185, 11, 0.08); border:1px solid rgba(240, 185, 11, 0.35); border-radius:6px; padding:10px 12px; margin:12px 0;"><div style="font-weight:700; color:#f0b90b; font-size:12px; margin-bottom:6px;">⭐ TRỌNG TÂM HAY RA THI (EXAM TIPS)</div>');
          inVipCard = true;
          continue;
        }

        if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
          if (!inList) {
            res.push('<ul style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
            inList = true;
          }
          res.push('<li style="margin-bottom:4px;">' + trimmed.substring(2) + '</li>');
        } else if (/^\\d+\\.\\s/.test(trimmed)) {
          if (!inList) {
            res.push('<ol style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
            inList = true;
          }
          res.push('<li style="margin-bottom:4px;">' + trimmed.replace(/^\\d+\\.\\s*/, '') + '</li>');
        } else {
          if (inList) { res.push('</ul>'); inList = false; }
          if (trimmed.startsWith('### ')) {
            res.push('<h4 style="font-size:14px; font-weight:700; color:#60a5fa; margin:14px 0 6px 0;">' + trimmed.substring(4) + '</h4>');
          } else {
            res.push('<p style="margin:6px 0; line-height:1.7;">' + trimmed + '</p>');
          }
        }
      }
      if (inList) res.push('</ul>');
      if (inVipCard) res.push('</div>');

      let html = res.join('');

      // 5. Restore Math placeholders using split().join() (No $$ JS quirk!)
      for (let i = 0; i < mathPlaceholders.length; i++) {
        html = html.split('%%%MATH_DISPLAY_' + i + '%%%').join(mathPlaceholders[i]);
        html = html.split('%%%MATH_INLINE_' + i + '%%%').join(mathPlaceholders[i]);
      }

      return html;
    }

    function renderSplitContent() {
      const container = document.getElementById('splitPaneBody');
      const selectEl = document.getElementById('splitTheorySecSelect');
      
      // Update select element options once
      if (selectEl && selectEl.options.length === 0 && THEORY && THEORY.length > 0) {
        THEORY.forEach(s => {
          const opt = document.createElement('option');
          opt.value = s.secId;
          const shortTit = (s.title || '').length > 28 ? s.title.substring(0, 28) + '...' : s.title;
          opt.textContent = `${s.secId} ${shortTit}`;
          selectEl.appendChild(opt);
        });
      }

      if (selectEl) {
        selectEl.style.display = (splitType === 'theory') ? 'inline-block' : 'none';
        selectEl.value = currentTheorySecId;
      }

      const btnPdf = document.getElementById('btnSplitPdf');
      const btnTheory = document.getElementById('btnSplitTheory');
      const btnFormulas = document.getElementById('btnSplitFormulas');
      if (btnPdf) btnPdf.className = splitType === 'pdf' ? 'btn btn-primary' : 'btn';
      if (btnTheory) btnTheory.className = splitType === 'theory' ? 'btn btn-primary' : 'btn';
      if (btnFormulas) btnFormulas.className = splitType === 'formulas' ? 'btn btn-primary' : 'btn';

      if (splitType === 'pdf') {
        container.innerHTML = `<iframe src="olp_ai_handbook_2026.pdf" style="width:100%; height:100%; border:none;"></iframe>`;
      } else if (splitType === 'theory') {
        // Smart match: if user hasn't explicitly picked a section, link to current problem section
        const q = EXAM.questions[currentIndex];
        let targetSecId = currentTheorySecId;
        if (!currentTheorySecIdUserSelected && q && q.explanation) {
          const matchSec = q.explanation.match(/§[\\d\\.]+/);
          if (matchSec) {
            targetSecId = matchSec[0];
            currentTheorySecId = targetSecId;
            if (selectEl) selectEl.value = targetSecId;
          }
        }

        const sec = THEORY.find(s => s.secId === targetSecId) || THEORY.find(s => s.secId.startsWith(targetSecId)) || THEORY[1] || THEORY[0];
        container.innerHTML = `
          <div style="height:100%; overflow-y:auto; padding:16px; font-size:13px; line-height:1.7; color:var(--text-secondary); background:var(--bg-surface);">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; border-bottom:1px solid var(--border-subtle); padding-bottom:8px;">
              <div>
                <span style="font-size:11px; font-weight:700; color:#f0b90b; text-transform:uppercase;">GIÁO TRÌNH TRỌNG TÂM OLP AI</span>
                <h3 style="font-size:15px; font-weight:700; color:#ffffff; margin-top:2px;">${sec.secId} ${sec.title}</h3>
              </div>
            </div>
            <div class="theory-body-content">${formatTheoryMarkdown(sec.body)}</div>
          </div>
        `;
        renderMath(container);
      } else if (splitType === 'formulas') {
        let html = `<div style="height:100%; overflow-y:auto; padding:14px; display:flex; flex-direction:column; gap:10px;">`;
        FORMULAS.forEach(f => {
          html += `
            <div class="cp-formula-box">
              <div class="formula-title">${f.title}</div>
              <div class="formula-desc">${f.desc}</div>
              <div class="formula-tex">$$${f.tex}$$</div>
            </div>
          `;
        });
        html += `</div>`;
        container.innerHTML = html;
        renderMath(container);
      }
    }

    function openChapterTheory(prefix) {
      currentTheorySecIdUserSelected = true;
      const matchingSec = THEORY.find(s => s.secId.startsWith(prefix));
      if (matchingSec) {
        currentTheorySecId = matchingSec.secId;
      }
      openSplitWith('theory');
    }'''

old_render_split = '''    function renderSplitContent() {
      const container = document.getElementById('splitPaneBody');
      if (splitType === 'pdf') {
        container.innerHTML = `<iframe src="olp_ai_handbook_2026.pdf" style="width:100%; height:100%; border:none;"></iframe>`;
      } else if (splitType === 'theory') {
        const sec = THEORY[1] || THEORY[0];
        container.innerHTML = `
          <div style="height:100%; overflow-y:auto; padding:14px; font-size:12.5px; line-height:1.7; color:var(--text-secondary); background:var(--bg-surface);">
            <div style="font-size:15px; font-weight:700; color:#fff; margin-bottom:8px;">${sec.secId} ${sec.title}</div>
            <div style="white-space:pre-wrap;">${sec.body}</div>
          </div>
        `;
      } else if (splitType === 'formulas') {
        let html = `<div style="height:100%; overflow-y:auto; padding:14px; display:flex; flex-direction:column; gap:10px;">`;
        FORMULAS.forEach(f => {
          html += `
            <div class="cp-formula-box">
              <div class="formula-title">${f.title}</div>
              <div class="formula-desc">${f.desc}</div>
              <div class="formula-tex">$$${f.tex}$$</div>
            </div>
          `;
        });
        html += `</div>`;
        container.innerHTML = html;
        renderMath(container);
      }
    }

    function openChapterTheory(prefix) {
      openSplitWith('theory');
      const container = document.getElementById('splitPaneBody');
      const filtered = THEORY.filter(s => s.secId.startsWith(prefix));
      if (filtered.length > 0) {
        let html = `<div style="height:100%; overflow-y:auto; padding:14px; display:flex; flex-direction:column; gap:14px; background:var(--bg-surface);">`;
        filtered.forEach(s => {
          html += `
            <div style="border-bottom:1px solid var(--border-subtle); padding-bottom:12px;">
              <h4 style="font-size:14px; font-weight:700; color:#60a5fa; margin-bottom:6px;">${s.secId} ${s.title}</h4>
              <div style="font-size:12.5px; line-height:1.6; color:var(--text-secondary); white-space:pre-wrap;">${s.body}</div>
            </div>
          `;
        });
        html += `</div>`;
        container.innerHTML = html;
        renderMath(container);
      }
    }'''

if old_render_split in code:
    code = code.replace(old_render_split, new_theory_and_split_code)
    print("✓ Đã cập nhật formatTheoryMarkdown và renderSplitContent với KaTeX hoàn hảo")
else:
    print("! Thử regex thay thế khối renderSplitContent...")
    code = re.sub(
        r'function renderSplitContent\(\)[\s\S]*?function openChapterTheory\(prefix\)[\s\S]*?renderMath\(container\);\s*\}\s*\}',
        new_theory_and_split_code,
        code
    )

# 5. Cập nhật formatExplanationHtml để bảo vệ math tuyệt đối
new_format_explanation = '''    // Safe Math & Rich 4-Block Formatter
    function formatExplanationHtml(expText) {
      if (!expText) return '<div class="eli5-block" style="color:var(--text-muted); font-style:italic;">Đang cập nhật lời giải chi tiết.</div>';

      function safeMdToHtml(str) {
        if (!str) return '';
        const mathBlocks = [];
        
        // Protect Display Math
        let s = str.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (m) => {
          const idx = mathBlocks.length;
          const safeM = m.replace(/</g, '&lt;').replace(/>/g, '&gt;');
          mathBlocks.push(safeM);
          return '%%%MATH_DISP_' + idx + '%%%';
        });

        // Protect Inline Math
        s = s.replace(/\\$([^\\$\\n]+?)\\$/g, (m) => {
          const idx = mathBlocks.length;
          const safeM = m.replace(/</g, '&lt;').replace(/>/g, '&gt;');
          mathBlocks.push(safeM);
          return '%%%MATH_INL_' + idx + '%%%';
        });

        // Bold & Code
        s = s.replace(/\\*\\*([^\\*]+)\\*\\*/g, '<strong>$1</strong>');
        s = s.replace(/`([^`]+)`/g, '<code style="background:rgba(255,255,255,0.08); padding:1px 5px; border-radius:3px; font-family:var(--font-mono); font-size:12px; color:#f0b90b;">$1</code>');

        const lines = s.split(String.fromCharCode(10));
        let inList = false;
        let res = [];
        for (let line of lines) {
          let trimmed = line.trim();
          if (!trimmed) {
            if (inList) { res.push('</ul>'); inList = false; }
            continue;
          }
          if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
            if (!inList) {
              res.push('<ul style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
              inList = true;
            }
            res.push('<li style="margin-bottom:4px;">' + trimmed.substring(2) + '</li>');
          } else if (/^\\d+\\.\\s/.test(trimmed)) {
            if (!inList) {
              res.push('<ol style="margin:6px 0 6px 18px; padding-left:0; line-height:1.7;">');
              inList = true;
            }
            res.push('<li style="margin-bottom:4px;">' + trimmed.replace(/^\\d+\\.\\s*/, '') + '</li>');
          } else {
            if (inList) {
              res.push('</ul>');
              inList = false;
            }
            res.push('<p style="margin:6px 0; line-height:1.7;">' + trimmed + '</p>');
          }
        }
        if (inList) res.push('</ul>');
        
        let outHtml = res.join('');
        for (let i = 0; i < mathBlocks.length; i++) {
          outHtml = outHtml.split('%%%MATH_DISP_' + i + '%%%').join(mathBlocks[i]);
          outHtml = outHtml.split('%%%MATH_INL_' + i + '%%%').join(mathBlocks[i]);
        }
        return outHtml;
      }

      // Chuẩn hóa phân tách theo Markdown ### 1., ### 2., ### 3., ### 4.
      if (expText.indexOf('### 1.') !== -1 || expText.indexOf('### 2.') !== -1 || expText.indexOf('### 3.') !== -1) {
        const rawParts = expText.split('### ');
        let out = '';
        for (let i = 1; i < rawParts.length; i++) {
          const part = rawParts[i].trim();
          if (!part) continue;
          let header = '';
          let body = '';
          const nlIdx = part.indexOf(String.fromCharCode(10));
          if (nlIdx !== -1) {
            header = part.substring(0, nlIdx).trim();
            body = part.substring(nlIdx + 1).trim();
          } else {
            header = part;
          }

          let cls = 'eli5-block';
          let titleColor = '#60a5fa';
          let icon = '👶';
          if (header.indexOf('1.') !== -1 || header.toLowerCase().indexOf('eli5') !== -1) {
            cls = 'eli5-block';
            titleColor = '#60a5fa';
            icon = '👶';
          } else if (header.indexOf('2.') !== -1 || header.toLowerCase().indexOf('toán') !== -1 || header.toLowerCase().indexOf('đạo hàm') !== -1 || header.toLowerCase().indexOf('chứng minh') !== -1) {
            cls = 'eli5-block math';
            titleColor = '#34d399';
            icon = '📐';
          } else if (header.indexOf('3.') !== -1 || header.toLowerCase().indexOf('bẫy') !== -1 || header.toLowerCase().indexOf('sai') !== -1) {
            cls = 'eli5-block trap';
            titleColor = '#fbbf24';
            icon = '⚠️';
          } else if (header.indexOf('4.') !== -1 || header.toLowerCase().indexOf('mắt xích') !== -1 || header.toLowerCase().indexOf('căn cứ') !== -1 || header.toLowerCase().indexOf('lý thuyết') !== -1 || header.toLowerCase().indexOf('liên hệ') !== -1) {
            cls = 'eli5-block ref';
            titleColor = '#a78bfa';
            icon = '📚';
          }

          out += '<div class="' + cls + '" style="margin-top:10px;">' +
            '<div style="font-weight:700; color:' + titleColor + '; margin-bottom:6px;">' + icon + ' [' + header + ']</div>' +
            '<div style="font-size:13px; line-height:1.7;">' + safeMdToHtml(body) + '</div>' +
          '</div>';
        }
        return out || '<div class="eli5-block">' + safeMdToHtml(expText) + '</div>';
      }

      return '<div class="eli5-block">' + safeMdToHtml(expText) + '</div>';
    }'''

old_format_exp_block = '''    // Format Explanation into 4 Beautiful Blocks
    function formatExplanationHtml(expText) {'''

if old_format_exp_block in code:
    code = re.sub(
        r'// Format Explanation into 4 Beautiful Blocks[\s\S]*?return out \|\| \'<div class="eli5-block"><div style="font-size:13px; line-height:1.6;">\' \+ mdToHtml\(expText\) \+ \'</div></div>\';\s*\}',
        new_format_explanation,
        code
    )
    print("✓ Đã cập nhật formatExplanationHtml chuẩn mực")

# 6. Gọi renderMath sau khi renderInspector rubric
old_rubric_render = "container.innerHTML = html;"
if "if (inspectorTab === 'rubric') {" in code:
    # Đảm bảo sau container.innerHTML = html của rubric có renderMath(container);
    code = code.replace(
        "container.innerHTML = html;\n\n      } else if (inspectorTab === 'explanation') {",
        "container.innerHTML = html;\n        renderMath(container);\n\n      } else if (inspectorTab === 'explanation') {"
    )
    print("✓ Đã thêm renderMath(container) cho tab Rubric trong Inspector")

with open(gen_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Đã lưu toàn bộ bản vá vào docs/generate_full_hub.py thành công!")
