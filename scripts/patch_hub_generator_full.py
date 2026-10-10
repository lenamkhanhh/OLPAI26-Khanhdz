# -*- coding: utf-8 -*-
"""
scripts/patch_hub_generator_full.py
Sửa toàn diện docs/generate_full_hub.py theo đúng audit VERIFY_SAU_SUA_2026-10-08:
- P0-1: Không giả lập test AC/điểm tự động cho Essay & Code.
- P0-2: Tách biệt hoàn toàn Graded (MCQ & Code: /90đ hoặc /100đ) và Essay (Tự luận: /60đ hoặc /40đ) ở header ticker, footer, lịch sử nộp và modal nộp bài.
- P0-3: Thêm storage version migration cho HTML (reset olp-02 & olp-03 phiên bản 2 do đảo phương án, bảo toàn nguyên vẹn olp-01).
- P2: Chuẩn hóa nhãn "Lời giải tham khảo / Bài giải mẫu tham khảo / Bảng rubric tự đối chiếu".
- Loại bỏ 100% lỗi escape ký tự xuống dòng (\\n) trong JS bằng String.fromCharCode(10).
"""

import os
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
GEN_FILE = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")

with open(GEN_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Cập nhật Storage (P0-3)
old_storage_block = """    // Load LocalStorage
    function loadSavedState() {{
      try {{
        const saved = localStorage.getItem('olp-ai-answers-' + currentExamId);
        if (saved) answers = JSON.parse(saved);
        else answers = {{}};
      }} catch(e) {{ answers = {{}}; }}
    }}

    function saveState() {{
      try {{
        localStorage.setItem('olp-ai-answers-' + currentExamId, JSON.stringify(answers));
      }} catch(e) {{}}
    }}"""

new_storage_block = """    // Storage Versioning & Migration (P0-3)
    const CURRENT_EXAM_VERSIONS = {{
      'olp-01': 1,
      'olp-02': 2,
      'olp-03': 2
    }};

    // Load LocalStorage with Migration
    function loadSavedState() {{
      try {{
        const storedVer = parseInt(localStorage.getItem('olp-ai-version-' + currentExamId) || '1', 10);
        const currentVer = CURRENT_EXAM_VERSIONS[currentExamId] || 1;
        
        // Nếu đề 02 hoặc 03 chưa có version 2 (dữ liệu cũ trước khi đảo phương án / sửa câu hỏi)
        if (currentVer > storedVer) {{
          console.warn('[Storage Migration] Reset cache cũ của ' + currentExamId + ' do cập nhật version ' + currentVer);
          localStorage.removeItem('olp-ai-answers-' + currentExamId);
          localStorage.setItem('olp-ai-version-' + currentExamId, currentVer);
          answers = {{}};
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
    }}"""

if old_storage_block in content:
    content = content.replace(old_storage_block, new_storage_block)
    print("✓ Đã cập nhật Storage Migration (P0-3)")
else:
    print("! Cảnh báo: Không tìm thấy old_storage_block chính xác")

# 2. Cập nhật renderHeaderStats (P0-2)
old_header_stats = """    // Render Stats
    function renderHeaderStats() {{
      let totalPts = 0;
      let acCount = 0;
      let waCount = 0;
      let answeredCount = 0;

      EXAM.questions.forEach(q => {{
        const a = answers[q.id];
        if (a) {{
          if (a.verdict === 'AC') {{
            acCount++;
            totalPts += (a.points !== undefined ? a.points : q.points);
            answeredCount++;
          }} else if (a.verdict === 'WA') {{
            waCount++;
            answeredCount++;
          }} else if (a.selected || (a.text && a.text.trim()) || a.codePassed) {{
            answeredCount++;
          }}
        }}
      }});

      const maxExamPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;
      document.getElementById('tickerTotalScore').textContent = `${{totalPts.toFixed(1)}} / ${{maxExamPts.toFixed(1)}}`;
      document.getElementById('tickerAcCount').textContent = `${{acCount}} AC`;
      document.getElementById('tickerWaCount').textContent = `${{waCount}} WA`;

      const pct = Math.round((answeredCount / EXAM.questions.length) * 100);
      document.getElementById('footerProgressLabel').textContent = `Tiến độ: ${{answeredCount}}/${{EXAM.questions.length}} (${{pct}}% hoàn thành · ${{totalPts.toFixed(1)}}đ)`;
    }}"""

new_header_stats = """    // Render Stats (Phân định rạch ròi Graded vs Essay - P0-2)
    function renderHeaderStats() {{
      let gradedPts = 0;
      let essaySelfPts = 0;
      let acCount = 0;
      let waCount = 0;
      let answeredCount = 0;

      const maxGradedPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;
      const maxEssayPts = (EXAM.id === 'olp-02') ? 60.0 : 40.0;

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
              if (a.verdict === 'AC') {{
                acCount++;
                gradedPts += q.points;
              }} else if (a.verdict === 'WA') {{
                waCount++;
              }} else if (a.selfScore !== undefined) {{
                gradedPts += a.selfScore;
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
        tickerEssayScoreEl.textContent = `Tự luận: ${{essaySelfPts.toFixed(1)}}/${{maxEssayPts.toFixed(1)}}đ`;
      }}

      const pct = Math.round((answeredCount / EXAM.questions.length) * 100);
      const footerProgressLabelEl = document.getElementById('footerProgressLabel');
      if (footerProgressLabelEl) {{
        footerProgressLabelEl.textContent = `Tiến độ: ${{answeredCount}}/${{EXAM.questions.length}} (${{pct}}%) · Graded: ${{gradedPts.toFixed(1)}}/${{maxGradedPts.toFixed(1)}}đ · Tự luận: ${{essaySelfPts.toFixed(1)}}/${{maxEssayPts.toFixed(1)}}đ`;
      }}
    }}"""

if old_header_stats in content:
    content = content.replace(old_header_stats, new_header_stats)
    print("✓ Đã cập nhật renderHeaderStats (P0-2)")
else:
    print("! Cảnh báo: Không tìm thấy old_header_stats chính xác")

# 3. Cập nhật Code Workbench & Essay nút bấm trong renderCenter
content = content.replace(
    '<span style="font-size:11px; color:var(--text-muted);">Hệ thống chấm tự động kiểm thử 3 test cases</span>\n              <button class="btn btn-primary" onclick="runCustomCode(\'${{q.id}}\')">▶ Chạy Thử Test Case</button>',
    '<span style="font-size:11px; color:var(--text-muted);">Môi trường ghi nhận mã nguồn · Tự đối chiếu giải pháp mẫu</span>\n              <button class="btn btn-primary" onclick="runCustomCode(\'${{q.id}}\')">💾 Lưu & Đối Chiếu Giải Pháp</button>'
)

content = content.replace(
    '<div class="editorial-title"><span>📖 ĐÁP ÁN MẪU & GIẢI PHÁP CHUẨN</span></div>',
    '<div class="editorial-title"><span>📖 BÀI GIẢI MẪU THAM KHẢO & TEST CASES MINH HỌA</span></div>'
)

content = content.replace(
    '<button class="btn btn-primary" onclick="runEssayRubric(\'${{q.id}}\')">⚡ Chấm Điểm Rubric Tự Động</button>',
    '<button class="btn btn-primary" onclick="runEssayKeywordCheck(\'${{q.id}}\')">⚡ Gợi Ý Kiểm Tra Từ Khóa Rubric</button>'
)

# 4. Cập nhật Sidebar Lịch sử nộp bài (không fake AC cho essay)
old_sub_history = """          ansKeys.forEach(k => {{
            const a = answers[k];
            html += `
              <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:8px 10px; border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <strong style="color:#60a5fa; font-family:var(--font-mono);">${{k}}</strong>
                  <span style="font-size:11px; color:var(--text-muted); margin-left:6px;">${{a.timestamp || ''}}</span>
                </div>
                <span style="font-family:var(--font-mono); font-size:11px; font-weight:700; color:${{a.verdict === 'AC' ? 'var(--color-ac)' : 'var(--color-wa)'}};">
                  ${{a.verdict || 'DONE'}}
                </span>
              </div>
            `;
          }});"""

new_sub_history = """          ansKeys.forEach(k => {{
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
              statusText = (a.selfScore !== undefined) ? `${{a.selfScore.toFixed(1)}}đ` : (a.verdict || 'DONE');
              statusColor = (a.verdict === 'AC') ? 'var(--color-ac)' : '#60a5fa';
            }}
            html += `
              <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:8px 10px; border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <strong style="color:#60a5fa; font-family:var(--font-mono);">${{k}}</strong>
                  <span style="font-size:11px; color:var(--text-muted); margin-left:6px;">${{a.timestamp || ''}}</span>
                </div>
                <span style="font-family:var(--font-mono); font-size:11px; font-weight:700; color:${{statusColor}};">
                  ${{statusText}}
                </span>
              </div>
            `;
          }});"""

if old_sub_history in content:
    content = content.replace(old_sub_history, new_sub_history)
    print("✓ Đã cập nhật Lịch sử nộp bài trung thực (P0-1, P0-2)")
else:
    print("! Cảnh báo: Không tìm thấy old_sub_history chính xác")

# 5. Cập nhật các hàm Rubric, Code, và SubmitContestConfirm (Loại bỏ triệt để \\n gây lỗi)
rubric_and_submit_pattern = r'// Rubric Evaluator & Checklist[\s\S]*?// Keyboard Shortcuts'

new_rubric_and_submit = """// Rubric Evaluator & Checklist (Tự đối chiếu thật - P0-1)
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
      const text = ta ? ta.value.trim() : '';
      const q = EXAM.questions[currentIndex];
      const rubricList = q.rubric || [];
      const ptsPerCrit = q.points / Math.max(1, rubricList.length);

      if (text.length < 20) {{
        alert([
          '⚠️ Bài làm hiện đang để trống hoặc quá ngắn (dưới 20 ký tự).',
          'Điểm đề xuất: 0.0/' + q.points + 'đ.',
          'Hãy nhấn "Nạp khung mẫu 5 bước" và điền chi tiết các phân tích kỹ thuật.'
        ].join(String.fromCharCode(10)));
        return;
      }}

      const lowerText = text.toLowerCase();
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
        text: text,
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
      }});

      const totalAnswered = answeredGraded + answeredEssay;
      const reportLines = [
        'BÁO CÁO TỔNG HỢP KẾT QUẢ [' + EXAM.title + ']:',
        '',
        '1. PHẦN TRẮC NGHIỆM & CODE (GRADED):',
        '   • Điểm đạt được: ' + gradedPts.toFixed(1) + ' / ' + maxGradedPts.toFixed(1) + ' điểm',
        '   • Đã trả lời: ' + answeredGraded + ' câu',
        '',
        '2. PHẦN TỰ LUẬN THIẾT KẾ GIẢI PHÁP AI (TỰ ĐỐI CHIẾU RUBRIC):',
        '   • Điểm tự đánh giá: ' + essaySelfPts.toFixed(1) + ' / ' + maxEssayPts.toFixed(1) + ' điểm',
        '   • Đã làm: ' + answeredEssay + ' bài',
        '',
        'Tổng tiến độ hoàn thành: ' + totalAnswered + '/' + total + ' bài.',
        'Bạn có chắc chắn muốn nộp bài thi không?'
      ];

      if (confirm(reportLines.join(String.fromCharCode(10)))) {{
        alert('🎉 Bạn đã nộp bài thành công!' + String.fromCharCode(10) + 'Graded: ' + gradedPts.toFixed(1) + '/' + maxGradedPts.toFixed(1) + 'đ | Tự luận: ' + essaySelfPts.toFixed(1) + '/' + maxEssayPts.toFixed(1) + 'đ');
      }}
    }}

    // Keyboard Shortcuts"""

if re.search(rubric_and_submit_pattern, content):
    content = re.sub(rubric_and_submit_pattern, lambda m: new_rubric_and_submit, content)
    print("✓ Đã cập nhật Rubric / Code / Submit functions không lỗi newline (P0-1, P0-2)")
else:
    print("! Cảnh báo: Không match rubric_and_submit_pattern")

with open(GEN_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Hoàn tất cập nhật docs/generate_full_hub.py!")
