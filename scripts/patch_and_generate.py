# -*- coding: utf-8 -*-
"""
scripts/patch_and_generate.py
Patch docs/generate_full_hub.py according to VERIFY_LAN_2_2026-10-08:
1. Fix partial score calculation for code questions across header, footer, submit modal, and history/matrix.
2. Fix essay rubric keyword check: strip boilerplate, score 0 for empty/template, reset state on empty.
3. Add .matrix-item.partial styling for code partial scores.
4. Regenerate all 3 HTML files.
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

# PATCH 1: CSS for matrix-item.partial
old_css_wa = """    .matrix-item.wa {{
      background: rgba(244, 63, 94, 0.15);
      border-color: rgba(244, 63, 94, 0.4);
      color: #fb7185;
    }}"""

new_css_wa = """    .matrix-item.wa {{
      background: rgba(244, 63, 94, 0.15);
      border-color: rgba(244, 63, 94, 0.4);
      color: #fb7185;
    }}
    .matrix-item.partial {{
      background: rgba(245, 158, 11, 0.15);
      border-color: rgba(245, 158, 11, 0.4);
      color: #fbbf24;
    }}"""

if old_css_wa in content:
    content = content.replace(old_css_wa, new_css_wa)
    print("[OK] Patched CSS for matrix-item.partial")
else:
    print("[SKIP] old_css_wa not found or already patched")

# PATCH 2: renderHeaderStats - calculate exact codePts for code questions
old_stats_block = """          }} else {{
            if (a.selected || a.codeSubmitted) {{
              answeredCount++;
              if (a.verdict === 'AC') {{
                acCount++;
                gradedPts += q.points;
              }} else if (a.verdict === 'WA') {{
                waCount++;
              }} else if (a.selfScore !== undefined) {{
                gradedPts += a.selfScore;
              }}
            }}
          }}"""

new_stats_block = """          }} else {{
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
          }}"""

if old_stats_block in content:
    content = content.replace(old_stats_block, new_stats_block)
    print("[OK] Patched renderHeaderStats for partial code score")
else:
    print("[SKIP] old_stats_block not found or already patched")

# PATCH 3: matrix statusCls in renderSidebar
old_matrix_status = """          if (a) {{
            if (a.verdict === 'AC') statusCls = 'ac';
            else if (a.verdict === 'WA') statusCls = 'wa';
            else if (a.selected || (a.text && a.text.trim()) || a.codePassed) statusCls = 'ac';
          }}"""

new_matrix_status = """          if (a) {{
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
          }}"""

if old_matrix_status in content:
    content = content.replace(old_matrix_status, new_matrix_status)
    print("[OK] Patched matrix statusCls in renderSidebar")
else:
    print("[SKIP] old_matrix_status not found or already patched")

# PATCH 4: history log in renderSidebar (sidebarTab === 'sub')
old_history_log = """            }} else if (isCode) {{
              statusText = (a.selfScore !== undefined) ? `${{a.selfScore.toFixed(1)}}đ` : (a.verdict || 'DONE');
              statusColor = (a.verdict === 'AC') ? 'var(--color-ac)' : '#60a5fa';
            }}"""

new_history_log = """            }} else if (isCode) {{
              const codePts = a.selfScore !== undefined ? a.selfScore : (a.points !== undefined ? a.points : 0);
              statusText = `${{codePts.toFixed(1)}}/${{q.points}}.0đ (${{a.verdict || (codePts === q.points ? 'AC' : codePts > 0 ? 'PARTIAL' : 'WA')}})`;
              statusColor = (codePts === q.points) ? 'var(--color-ac)' : (codePts > 0 ? '#fbbf24' : 'var(--color-wa)');
            }}"""

if old_history_log in content:
    content = content.replace(old_history_log, new_history_log)
    print("[OK] Patched history log in renderSidebar for code items")
else:
    print("[SKIP] old_history_log not found or already patched")

# PATCH 5: setCodeSelfScore & submitContestConfirm
old_code_sub_block = """    function setCodeSelfScore(qid, pts) {{
      answers[qid] = {{
        ...(answers[qid] || {{}}),
        selfScore: pts,
        verdict: pts > 0 ? 'AC' : 'WA',
        points: pts,
        codeSubmitted: true,
        timestamp: new Date().toLocaleTimeString()
      }};
      saveState();
      renderSidebar();
      renderHeaderStats();
    }}

    function submitContestConfirm() {{
      const total = EXAM.questions.length;
      let answeredGraded = 0;
      let answeredEssay = 0;
      let gradedPts = 0;
      let essaySelfPts = 0;

      const maxGradedPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;
      const maxEssayPts = (EXAM.id === 'olp-02') ? 60.0 : 40.0;

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
              if (a.verdict === 'AC') gradedPts += q.points;
              else if (a.selfScore !== undefined) gradedPts += a.selfScore;
            }}
          }}
        }}
      }});"""

new_code_sub_block = """    function setCodeSelfScore(qid, pts) {{
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

      const maxGradedPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;
      const maxEssayPts = (EXAM.id === 'olp-02') ? 60.0 : 40.0;

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
      }});"""

if old_code_sub_block in content:
    content = content.replace(old_code_sub_block, new_code_sub_block)
    print("[OK] Patched setCodeSelfScore and submitContestConfirm")
else:
    print("[SKIP] old_code_sub_block not found or already patched")

# PATCH 6: runEssayKeywordCheck - strip boilerplate, reset on empty/short text
marker_start = "    function runEssayKeywordCheck(qid) {{"
marker_end = "    function insertEssayTemplate(qid) {{"

if marker_start in content and marker_end in content:
    start_pos = content.find(marker_start)
    end_pos = content.find(marker_end)
    old_func = content[start_pos:end_pos]

    new_func = """    function runEssayKeywordCheck(qid) {{
      const ta = document.getElementById('essayInput_' + qid);
      const rawText = ta ? ta.value : (answers[qid]?.text || '');
      const q = EXAM.questions[currentIndex];
      const rubricList = q.rubric || [];
      const ptsPerCrit = q.points / Math.max(1, rubricList.length);

      // Lo\\u1ea1i b\\u1ecf c\\u00e1c d\\u00f2ng ti\\u00eau \\u0111\\u1ec1 v\\u00e0 nh\\u00e3n m\\u1eb7c \\u0111\\u1ecbnh c\\u1ee7a khung m\\u1eabu 5 b\\u01b0\\u1edbc \\u0111\\u1ec3 ki\\u1ec3m tra n\\u1ed9i dung th\\u1ef1c t\\u1ebf
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
      userContent = userContent.replace(/[#\\-\\*:;\\s]/g, '').trim();

      // N\\u1ebfu b\\u00e0i l\\u00e0m tr\\u1ed1ng ho\\u1eb7c ch\\u1ec9 c\\u00f3 khung template ch\\u01b0a \\u0111i\\u1ec1n n\\u1ed9i dung (d\\u01b0\\u1edbi 20 k\\u00fd t\\u1ef1 th\\u1ef1c t\\u1ebf)
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

      // Qu\\u00e9t t\\u1eeb kh\\u00f3a tr\\u00ean n\\u1ed9i dung th\\u1ef1c t\\u1ebf c\\u1ee7a th\\u00ed sinh
      const lowerText = userContent.toLowerCase();
      let checkedMap = {{}};
      let matchedCount = 0;

      rubricList.forEach((crit, idx) => {{
        const words = crit.toLowerCase().replace(/[^a-z0-9àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ\\s]/g, ' ')
          .split(/\\s+/).filter(w => w.length > 3);
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

"""
    content = content[:start_pos] + new_func + content[end_pos:]
    print("[OK] Patched runEssayKeywordCheck")
else:
    print("[ERR] Could not locate start or end of runEssayKeywordCheck")

with open(GEN_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCESS] Successfully updated docs/generate_full_hub.py")
