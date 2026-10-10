# -*- coding: utf-8 -*-
"""
scripts/update_hub_generator_clean.py
Cập nhật docs/generate_full_hub.py theo đúng các yêu cầu P0-1, P0-2, P0-3 và P2:
1. P0-1: Chuyển chấm tự luận và code sang Tự đánh giá / Rubric đối chiếu thật, bỏ alert 100% AC giả.
2. P0-2: Tách biệt hoàn toàn Graded (MCQ/Code: /100đ hoặc /90đ) và Essay (Tự luận: /40đ hoặc /60đ).
3. P0-3: Thêm DATA_VERSIONS và migration tự động xóa cache đề cũ mà bảo toàn Đề 01.
4. P2: Chuẩn hóa nhãn từ ngữ (LỜI GIẢI THAM KHẢO, BÀI GIẢI MẪU THAM KHẢO).
"""

import os
import sys
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
TEMP_DIR = r"C:\Users\HP\AppData\Local\Temp\opencode\olp-ai-hcmus26"

def update():
    gen_file = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")
    with open(gen_file, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Cập nhật Score Ticker trong Header (Tách Graded và Tự luận)
    old_ticker = '''      <div class="score-ticker">
        <span style="color:var(--text-muted);">ĐIỂM:</span>
        <strong style="color:#60a5fa;" id="tickerTotalScore">0.0 / 100.0</strong>
        <div style="display:flex; gap:6px;">
          <span class="badge-ac-count" id="tickerAcCount">0 AC</span>
          <span class="badge-wa-count" id="tickerWaCount">0 WA</span>
        </div>
      </div>'''

    new_ticker = '''      <div class="score-ticker">
        <span style="color:var(--text-muted);">GRADED:</span>
        <strong style="color:#60a5fa;" id="tickerTotalScore">0.0 / 100.0đ</strong>
        <div style="display:flex; gap:6px;">
          <span class="badge-ac-count" id="tickerAcCount">0 AC</span>
          <span class="badge-wa-count" id="tickerWaCount">0 WA</span>
        </div>
        <span style="color:var(--text-dim); margin:0 2px;">|</span>
        <span style="color:var(--text-muted); font-size:11px;" id="tickerEssayScore">Tự luận: 0.0/40.0đ</span>
      </div>'''
    code = code.replace(old_ticker, new_ticker)

    # 2. Cập nhật nhãn ngữ nghĩa P2
    code = code.replace("OFFICIAL EDITORIAL & LUẬN CHỨNG TOÁN HỌC", "LỜI GIẢI THAM KHẢO & PHÂN TÍCH CHI TIẾT")
    code = code.replace("BÀI GIẢI MẪU THAM CHIẾU CỦA HỘI ĐỒNG THI", "BÀI GIẢI MẪU THAM KHẢO (KHUNG 5 BƯỚC)")
    code = code.replace("HỆ THỐNG ĐÁNH GIÁ THEO TIÊU CHÍ RUBRIC", "BẢNG TIÊU CHÍ RUBRIC TỰ ĐỐI CHIẾU")
    code = code.replace("TIÊU CHÍ RUBRIC CHÍNH THỨC", "TIÊU CHÍ RUBRIC THAM KHẢO")

    # 3. Thêm DATA_VERSIONS và cập nhật loadSavedState / saveState (P0-3)
    old_storage_block = '''    // Application State
    let currentExamId = 'olp-01';
    let EXAM = ALL_EXAMS[currentExamId];
    let currentIndex = 0;
    let answers = {};
    let editorialOpen = {};
    let rubricEvalResults = {};
    let filterModule = 'all';
    let sidebarTab = 'grid';
    let inspectorTab = 'rubric';
    let isInspectorOpen = true;
    let isSplitOpen = false;
    let splitType = 'pdf';
    let timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;
    let timerInterval = null;

    // Load LocalStorage
    function loadSavedState() {
      try {
        const saved = localStorage.getItem('olp-ai-answers-' + currentExamId);
        if (saved) answers = JSON.parse(saved);
        else answers = {};
      } catch(e) { answers = {}; }
    }

    function saveState() {
      try {
        localStorage.setItem('olp-ai-answers-' + currentExamId, JSON.stringify(answers));
      } catch(e) {}
    }'''

    new_storage_block = '''    // Application State
    const DATA_VERSIONS = {
      'olp-01': '1.0',
      'olp-02': '2.0',
      'olp-03': '2.0'
    };

    let currentExamId = 'olp-01';
    let EXAM = ALL_EXAMS[currentExamId];
    let currentIndex = 0;
    let answers = {};
    let editorialOpen = {};
    let rubricEvalResults = {};
    let filterModule = 'all';
    let sidebarTab = 'grid';
    let inspectorTab = 'rubric';
    let isInspectorOpen = true;
    let isSplitOpen = false;
    let splitType = 'pdf';
    let timerSeconds = ((EXAM && EXAM.durationMinutes) ? EXAM.durationMinutes : 90) * 60;
    let timerInterval = null;

    // Load LocalStorage with Migration Versioning (P0-3)
    function loadSavedState() {
      try {
        const storedVer = localStorage.getItem('olp-ai-version-' + currentExamId);
        const targetVer = DATA_VERSIONS[currentExamId] || '1.0';
        if (storedVer !== targetVer) {
          // Xóa cache của đề bị đổi version (Đề 02, Đề 03 sau khi shuffle), giữ nguyên Đề 01
          localStorage.removeItem('olp-ai-answers-' + currentExamId);
          localStorage.setItem('olp-ai-version-' + currentExamId, targetVer);
          answers = {};
          console.log(`[Storage Migration] Đề ${currentExamId} nâng cấp lên version ${targetVer}. Đã dọn cache cũ.`);
        } else {
          const saved = localStorage.getItem('olp-ai-answers-' + currentExamId);
          if (saved) answers = JSON.parse(saved);
          else answers = {};
        }
      } catch(e) { answers = {}; }
    }

    function saveState() {
      try {
        localStorage.setItem('olp-ai-answers-' + currentExamId, JSON.stringify(answers));
        localStorage.setItem('olp-ai-version-' + currentExamId, DATA_VERSIONS[currentExamId] || '1.0');
      } catch(e) {}
    }'''

    code = code.replace(old_storage_block, new_storage_block)

    # 4. Tách biệt hoàn toàn Graded vs Essay trong renderHeaderStats và submitContestConfirm (P0-2)
    old_render_stats = '''    // Render Stats
    function renderHeaderStats() {
      let totalPts = 0;
      let acCount = 0;
      let waCount = 0;
      let answeredCount = 0;

      EXAM.questions.forEach(q => {
        const a = answers[q.id];
        if (a) {
          if (a.verdict === 'AC') {
            acCount++;
            totalPts += (a.points !== undefined ? a.points : q.points);
            answeredCount++;
          } else if (a.verdict === 'WA') {
            waCount++;
            answeredCount++;
          } else if (a.selected || (a.text && a.text.trim()) || a.codePassed) {
            answeredCount++;
          }
        }
      });

      const maxExamPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;
      document.getElementById('tickerTotalScore').textContent = `${totalPts.toFixed(1)} / ${maxExamPts.toFixed(1)}`;
      document.getElementById('tickerAcCount').textContent = `${acCount} AC`;
      document.getElementById('tickerWaCount').textContent = `${waCount} WA`;

      const pct = Math.round((answeredCount / EXAM.questions.length) * 100);
      document.getElementById('footerProgressLabel').textContent = `Tiến độ: ${answeredCount}/${EXAM.questions.length} (${pct}% hoàn thành · ${totalPts.toFixed(1)}đ)`;
    }'''

    new_render_stats = '''    // Render Stats (Tách Graded và Essay - P0-2)
    function renderHeaderStats() {
      let gradedPts = 0;
      let essaySelfPts = 0;
      let acCount = 0;
      let waCount = 0;
      let answeredGraded = 0;
      let answeredEssay = 0;

      const maxGradedPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;
      const maxEssayPts = (EXAM.id === 'olp-02') ? 60.0 : 40.0;

      EXAM.questions.forEach(q => {
        const a = answers[q.id];
        if (a) {
          if (q.type === 'essay') {
            if (a.selfScore !== undefined) {
              essaySelfPts += a.selfScore;
              answeredEssay++;
            } else if (a.text && a.text.trim().length > 0) {
              answeredEssay++;
            }
          } else {
            if (a.verdict === 'AC') {
              acCount++;
              gradedPts += (a.points !== undefined ? a.points : q.points);
              answeredGraded++;
            } else if (a.verdict === 'WA') {
              waCount++;
              answeredGraded++;
            } else if (a.selected || a.codeSubmitted) {
              answeredGraded++;
              if (a.selfScore !== undefined) gradedPts += a.selfScore;
            }
          }
        }
      });

      document.getElementById('tickerTotalScore').textContent = `${gradedPts.toFixed(1)} / ${maxGradedPts.toFixed(1)}đ`;
      document.getElementById('tickerAcCount').textContent = `${acCount} AC`;
      document.getElementById('tickerWaCount').textContent = `${waCount} WA`;

      const tickerEssayEl = document.getElementById('tickerEssayScore');
      if (tickerEssayEl) {
        tickerEssayEl.textContent = `Tự luận: ${essaySelfPts.toFixed(1)}/${maxEssayPts.toFixed(1)}đ`;
      }

      const totalAnswered = answeredGraded + answeredEssay;
      const totalQuestions = EXAM.questions.length;
      const pct = Math.round((totalAnswered / totalQuestions) * 100);
      document.getElementById('footerProgressLabel').textContent = 
        `Tiến độ: ${totalAnswered}/${totalQuestions} (${pct}%) · Graded: ${gradedPts.toFixed(1)}/${maxGradedPts.toFixed(1)}đ · Tự luận: ${essaySelfPts.toFixed(1)}/${maxEssayPts.toFixed(1)}đ`;
    }'''

    code = code.replace(old_render_stats, new_render_stats)

    # 5. Cập nhật submitContestConfirm (Tách bạch Graded vs Essay - P0-2)
    old_submit = '''    function submitContestConfirm() {
      const total = EXAM.questions.length;
      let answered = 0;
      let totalPts = 0;
      EXAM.questions.forEach(q => {
        const a = answers[q.id];
        if (a && (a.selected || (a.text && a.text.trim()) || a.codePassed)) {
          answered++;
          totalPts += (a.points || 0);
        }
      });

      if (confirm(`Bạn đã hoàn thành ${answered}/${total} bài.\\nTổng điểm dự kiến: ${totalPts.toFixed(1)}/${EXAM.id === 'olp-02' ? '90.0' : '100.0'} điểm.\\n\\nBạn có chắc chắn muốn nộp bài thi không?`)) {
        alert(`🎉 Chúc mừng! Bạn đã nộp bài thành công cho ${EXAM.title}.\\nKết quả: ${totalPts.toFixed(1)} điểm!`);
      }
    }'''

    new_submit = '''    function submitContestConfirm() {
      const total = EXAM.questions.length;
      let answeredGraded = 0;
      let answeredEssay = 0;
      let gradedPts = 0;
      let essaySelfPts = 0;

      const maxGradedPts = (EXAM.id === 'olp-02') ? 90.0 : 100.0;
      const maxEssayPts = (EXAM.id === 'olp-02') ? 60.0 : 40.0;

      EXAM.questions.forEach(q => {
        const a = answers[q.id];
        if (a) {
          if (q.type === 'essay') {
            if (a.selfScore !== undefined || (a.text && a.text.trim().length > 0)) {
              answeredEssay++;
              if (a.selfScore !== undefined) essaySelfPts += a.selfScore;
            }
          } else {
            if (a.selected || a.codeSubmitted) {
              answeredGraded++;
              if (a.verdict === 'AC') gradedPts += q.points;
              else if (a.selfScore !== undefined) gradedPts += a.selfScore;
            }
          }
        }
      });

      const totalAnswered = answeredGraded + answeredEssay;
      const reportMsg = `BÁO CÁO TỔNG HỢP KẾT QUẢ [${EXAM.title}]:\\n\\n` +
        `1. PHẦN TRẮC NGHIỆM & CODE (GRADED):\\n` +
        `   • Điểm đạt được: ${gradedPts.toFixed(1)} / ${maxGradedPts.toFixed(1)} điểm\\n` +
        `   • Đã trả lời: ${answeredGraded} câu\\n\\n` +
        `2. PHẦN TỰ LUẬN THIẾT KẾ GIẢI PHÁP AI (TỰ ĐỐI CHIẾU RUBRIC):\\n` +
        `   • Điểm tự đánh giá: ${essaySelfPts.toFixed(1)} / ${maxEssayPts.toFixed(1)} điểm\\n` +
        `   • Đã làm: ${answeredEssay} bài\\n\\n` +
        `Tổng tiến độ hoàn thành: ${totalAnswered}/${total} bài.\\n` +
        `Bạn có chắc chắn muốn nộp bài thi không?`;

      if (confirm(reportMsg)) {
        alert(`🎉 Bạn đã nộp bài thành công!\\nGraded: ${gradedPts.toFixed(1)}/${maxGradedPts.toFixed(1)}đ | Tự luận: ${essaySelfPts.toFixed(1)}/${maxEssayPts.toFixed(1)}đ`);
      }
    }'''

    code = code.replace(old_submit, new_submit)

    # 6. Sửa runCustomCode: Bỏ thông báo giả 100% AC (P0-1)
    old_run_code = '''    function runCustomCode(qid) {
      const ta = document.getElementById('codeInput_' + qid);
      const code = ta ? ta.value : '';
      answers[qid] = { ...(answers[qid] || {}), code: code, verdict: 'AC', points: 7, codePassed: true };
      saveState();
      alert('✓ [Judge] Toàn bộ 3 Test Cases chạy thành công! Điểm: 7.0/7.0đ.');
      renderCenter();
      renderSidebar();
      renderHeaderStats();
    }'''

    new_run_code = '''    function runCustomCode(qid) {
      const ta = document.getElementById('codeInput_' + qid);
      const code = ta ? ta.value.trim() : '';
      if (!code || code === '# Viết mã nguồn Python / PyTorch tại đây...') {
        alert('⚠️ Vui lòng viết giải pháp mã nguồn trước khi kiểm tra.');
        return;
      }
      answers[qid] = {
        ...(answers[qid] || {}),
        code: code,
        codeSubmitted: true,
        selfScore: answers[qid]?.selfScore || 0,
        timestamp: new Date().toLocaleTimeString()
      };
      saveState();
      alert('ℹ️ [Sandbox Cục Bộ Trình Duyệt]\\nTrình duyệt hiện tại chưa tích hợp runtime Python/PyTorch trực tiếp.\\n\\nMã nguồn của bạn đã được ghi nhận. Vui lòng mở rộng mục "ĐÁP ÁN MẪU & GIẢI PHÁP CHUẨN" bên dưới để đối chiếu logic thuật toán và các trường hợp kiểm thử.');
      renderCenter();
      renderSidebar();
      renderHeaderStats();
    }

    function setCodeSelfScore(qid, pts) {
      answers[qid] = {
        ...(answers[qid] || {}),
        selfScore: pts,
        verdict: pts > 0 ? 'AC' : 'WA',
        points: pts,
        codeSubmitted: true,
        timestamp: new Date().toLocaleTimeString()
      };
      saveState();
      renderSidebar();
      renderHeaderStats();
    }'''

    code = code.replace(old_run_code, new_run_code)

    # 7. Sửa runEssayRubric: Bỏ chấm theo độ dài, chuyển sang Rubric Checklist & Gợi ý từ khóa (P0-1)
    pattern_rubric_fn = r'// Rubric Evaluator Function[\s\S]*?function insertEssayTemplate'

    new_rubric_fn = '''// Rubric Evaluator & Checklist (Tự đối chiếu thật - P0-1)
    function toggleRubricCriterion(qid, critIdx) {
      const q = EXAM.questions[currentIndex];
      const rubricList = q.rubric || [];
      const ptsPerCrit = q.points / Math.max(1, rubricList.length);

      if (!rubricEvalResults[qid]) {
        rubricEvalResults[qid] = { checked: {} };
      }
      const checkedMap = rubricEvalResults[qid].checked || {};
      checkedMap[critIdx] = !checkedMap[critIdx];
      rubricEvalResults[qid].checked = checkedMap;

      let earnedPts = 0;
      rubricList.forEach((_, idx) => {
        if (checkedMap[idx]) earnedPts += ptsPerCrit;
      });
      rubricEvalResults[qid].score = Number(earnedPts.toFixed(1));

      const ta = document.getElementById('essayInput_' + qid);
      const text = ta ? ta.value.trim() : (answers[qid]?.text || '');

      answers[qid] = {
        ...(answers[qid] || {}),
        text: text,
        selfScore: Number(earnedPts.toFixed(1)),
        points: Number(earnedPts.toFixed(1)),
        verdict: earnedPts > 0 ? 'AC' : 'WA',
        submitted: true,
        timestamp: new Date().toLocaleTimeString()
      };
      saveState();
      renderInspector();
      renderSidebar();
      renderHeaderStats();
    }

    function runEssayKeywordCheck(qid) {
      const ta = document.getElementById('essayInput_' + qid);
      const text = ta ? ta.value.trim() : '';
      const q = EXAM.questions[currentIndex];
      const rubricList = q.rubric || [];
      const ptsPerCrit = q.points / Math.max(1, rubricList.length);

      if (text.length < 20) {
        alert('⚠️ Bài làm hiện đang để trống hoặc quá ngắn (dưới 20 ký tự).\\nĐiểm đề xuất: 0.0/' + q.points + 'đ.\\nHãy nhấn "Nạp khung mẫu 5 bước" và điền chi tiết các phân tích kỹ thuật.');
        return;
      }

      const lowerText = text.toLowerCase();
      let checkedMap = {};
      let matchedCount = 0;

      rubricList.forEach((crit, idx) => {
        // Tách các từ khóa có nghĩa từ tiêu chí
        const words = crit.toLowerCase().replace(/[^a-z0-9àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ\\s]/g, ' ')
          .split(/\\s+/).filter(w => w.length > 3);
        let matches = 0;
        for (const w of words) {
          if (lowerText.indexOf(w) !== -1) matches++;
        }
        // Yêu cầu match ít nhất 2 từ khóa hoặc tỷ lệ >= 20%
        if (matches >= 2 || (words.length > 0 && matches / words.length >= 0.2)) {
          checkedMap[idx] = true;
          matchedCount++;
        } else {
          checkedMap[idx] = false;
        }
      });

      const proposedScore = Number((matchedCount * ptsPerCrit).toFixed(1));
      rubricEvalResults[qid] = {
        checked: checkedMap,
        score: proposedScore,
        summary: `Hệ thống gợi ý từ khóa phát hiện ${matchedCount}/${rubricList.length} tiêu chí có xuất hiện thuật ngữ liên quan trong bài làm. (Lưu ý: Đây là gợi ý tự động hỗ trợ tự đối chiếu, không phải điểm chấm chính thức của hội đồng).`
      };

      answers[qid] = {
        ...(answers[qid] || {}),
        text: text,
        selfScore: proposedScore,
        points: proposedScore,
        verdict: proposedScore > 0 ? 'AC' : 'WA',
        submitted: true,
        timestamp: new Date().toLocaleTimeString()
      };
      saveState();
      switchInspectorTab('rubric');
      renderCenter();
      renderSidebar();
      renderHeaderStats();
      alert(`⚡ [Gợi ý Từ khóa Tự động]\\nĐã đối chiếu bài làm với ${rubricList.length} tiêu chí.\\nĐiểm đề xuất: ${proposedScore}/${q.points}đ.\\nBạn có thể điều chỉnh các ô đánh dấu bên bảng Inspector bên phải để hoàn thiện điểm tự đánh giá.`);
    }

    function insertEssayTemplate'''

    code = re.sub(pattern_rubric_fn, lambda m: new_rubric_fn, code)

    # 8. Sửa hiển thị Rubric trong Inspector: Cho phép tương tác Checkbox tự chấm (P0-1)
    old_inspector_rubric = '''      if (inspectorTab === 'rubric') {
        const evalRes = rubricEvalResults[q.id];
        let html = `
          <div style="background:var(--bg-card); border:1px solid var(--border-subtle); padding:12px; border-radius:var(--radius-sm); display:flex; flex-direction:column; gap:8px;">
            <div style="font-weight:700; font-size:12px; color:#93c5fd;">BẢNG TIÊU CHÍ RUBRIC TỰ ĐỐI CHIẾU</div>
            <p style="font-size:11px; color:var(--text-muted); line-height:1.5;">
              Hội đồng đánh giá đối chiếu bài làm với 5 tiêu chí chuẩn: Nhận diện bài toán, Lựa chọn kiến trúc mô hình, Pipeline chống rò rỉ dữ liệu, Chỉ số đánh giá và Phương án mở rộng thực tế.
            </p>
            ${q.rubric && Array.isArray(q.rubric) && q.rubric.length > 0 ? `
              <div style="margin-top:8px; display:flex; flex-direction:column; gap:6px;">
                <div style="font-size:11px; font-weight:700; color:#60a5fa; text-transform:uppercase;">5 TIÊU CHÍ RUBRIC THAM KHẢO (${q.points} ĐIỂM):</div>
                ${q.rubric.map(r => `
                  <div style="font-size:11px; color:var(--text-secondary); background:rgba(0,0,0,0.25); padding:6px 8px; border-radius:4px; border-left:2px solid #3b82f6; line-height:1.4;">
                    ${sanitizeTex(r)}
                  </div>
                `).join('')}
              </div>
            ` : ''}
            ${q.type === 'essay' ? `
              <button class="btn btn-primary" style="justify-content:center; height:30px;" onclick="runEssayRubric('${q.id}')">⚡ Chấm điểm Rubric ngay</button>
            ` : q.type === 'code' ? `
              <button class="btn btn-primary" style="justify-content:center; height:30px;" onclick="runCustomCode('${q.id}')">▶ Kiểm tra Rubric Code</button>
            ` : `
              <div style="font-size:11px; color:#34d399; background:rgba(16,185,129,0.08); padding:8px; border-radius:4px; border-1px solid rgba(16,185,129,0.2);">
                ✓ <strong>Tiêu chuẩn trắc nghiệm:</strong> Đúng +${q.points}đ, Sai 0.0đ. Phân loại nhận thức: Vận dụng cao / Tính toán bản chất.
              </div>
            `}
          </div>
        `;

        if (evalRes) {
          html += `
            <div style="background:var(--bg-card); border:1px solid var(--border-strong); border-radius:var(--radius-sm); padding:12px; display:flex; flex-direction:column; gap:8px;">
              <div style="display:flex; justify-content:space-between; align-items:baseline;">
                <span style="font-size:11px; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Kết quả chấm:</span>
                <span style="font-family:var(--font-mono); font-size:15px; font-weight:700; color:#60a5fa;">${evalRes.score}/${q.points} điểm</span>
              </div>
              <div style="font-size:11.5px; color:var(--text-main); line-height:1.5; padding:6px 8px; background:rgba(0,0,0,0.25); border-radius:var(--radius-xs); border-left:2px solid #3b82f6;">
                ${evalRes.summary}
              </div>
              <div style="display:flex; flex-direction:column; gap:6px; margin-top:4px;">
                ${evalRes.breakdown.map(b => `
                  <div style="padding:6px 8px; border-radius:var(--radius-xs); background:rgba(0,0,0,0.15); border-left:2px solid ${b.pass ? 'var(--color-ac)' : 'var(--color-wa)'}};">
                    <div style="display:flex; justify-content:space-between; font-size:11px; font-weight:600; color:var(--text-main);">
                      <span>${b.criterion}</span>
                      <span style="font-family:var(--font-mono);">${b.earned}/${b.max}đ</span>
                    </div>
                    <div style="font-size:10.5px; color:var(--text-muted); margin-top:2px;">${b.feedback}</div>
                  </div>
                `).join('')}
              </div>
            </div>
          `;
        }

        container.innerHTML = html;'''

    new_inspector_rubric = '''      if (inspectorTab === 'rubric') {
        const evalRes = rubricEvalResults[q.id] || { checked: {} };
        const checkedMap = evalRes.checked || {};
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

        if (q.type === 'essay') {
          html += `
            <div style="background:var(--bg-card); border:1px solid var(--border-strong); border-radius:var(--radius-sm); padding:12px; display:flex; flex-direction:column; gap:10px;">
              <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle); padding-bottom:8px;">
                <span style="font-size:11px; font-weight:700; color:#60a5fa; text-transform:uppercase;">ĐIỂM TỰ ĐÁNH GIÁ:</span>
                <span style="font-family:var(--font-mono); font-size:15px; font-weight:700; color:#10b981;">${currentSelfPts.toFixed(1)} / ${q.points}.0đ</span>
              </div>

              <div style="display:flex; flex-direction:column; gap:8px;">
                ${rubricList.map((r, idx) => {
                  const isChecked = !!checkedMap[idx];
                  return `
                    <div style="display:flex; align-items:flex-start; gap:8px; padding:8px; border-radius:4px; background:${isChecked ? 'rgba(16,185,129,0.08)' : 'rgba(0,0,0,0.2)'}; border:1px solid ${isChecked ? 'rgba(16,185,129,0.3)' : 'var(--border-subtle)'}; cursor:pointer;" onclick="toggleRubricCriterion('${q.id}', ${idx})">
                      <input type="checkbox" style="margin-top:2px; cursor:pointer;" ${isChecked ? 'checked' : ''} onclick="event.stopPropagation(); toggleRubricCriterion('${q.id}', ${idx})">
                      <div style="flex:1;">
                        <div style="font-size:11.5px; font-weight:600; color:${isChecked ? '#34d399' : 'var(--text-secondary)'}; line-height:1.4;">
                          ${sanitizeTex(r)}
                        </div>
                        <div style="font-size:10px; color:var(--text-muted); margin-top:2px;">
                          ${isChecked ? `✓ Đạt (+${ptsPerCrit.toFixed(1)}đ)` : `Chưa tích (+0.0đ / tối đa ${ptsPerCrit.toFixed(1)}đ)`}
                        </div>
                      </div>
                    </div>
                  `;
                }).join('')}
              </div>

              <div style="display:flex; flex-direction:column; gap:6px; margin-top:4px;">
                <button class="btn btn-primary" style="justify-content:center; height:32px; font-size:11.5px;" onclick="runEssayKeywordCheck('${q.id}')">
                  ⚡ Gợi ý kiểm tra từ khóa tự động
                </button>
                <div style="font-size:10px; color:var(--text-muted); text-align:center;">
                  (Gợi ý từ khóa hỗ trợ phát hiện nội dung; điểm số do thí sinh tự đối chiếu quyết định)
                </div>
              </div>
            </div>
          `;

          if (evalRes.summary) {
            html += `
              <div style="background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.25); border-radius:var(--radius-sm); padding:10px; font-size:11px; color:#cbd5e1; line-height:1.5;">
                <strong style="color:#60a5fa;">Nhận xét từ khóa:</strong> ${evalRes.summary}
              </div>
            `;
          }

        } else if (q.type === 'code') {
          const curCodePts = answers[q.id]?.selfScore !== undefined ? answers[q.id].selfScore : 0;
          html += `
            <div style="background:var(--bg-card); border:1px solid var(--border-strong); border-radius:var(--radius-sm); padding:12px; display:flex; flex-direction:column; gap:10px;">
              <div style="font-size:11px; font-weight:700; color:#60a5fa; text-transform:uppercase;">ĐỐI CHIẾU MÃ NGUỒN PYTHON (${q.points}.0 ĐIỂM)</div>
              <p style="font-size:11px; color:var(--text-muted); line-height:1.5;">
                Môi trường trình duyệt tĩnh không chạy code trực tiếp. Sau khi viết code và xem đáp án mẫu, hãy tự cho điểm mức độ hoàn thiện của bài làm:
              </p>
              <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:4px;">
                ${[0, 2, 4, 5, 7].map(pt => `
                  <button class="btn ${curCodePts === pt ? 'btn-primary' : ''}" style="height:26px; font-size:11px;" onclick="setCodeSelfScore('${q.id}', ${pt})">
                    ${pt}.0đ ${pt === q.points ? '(Full AC)' : pt === 0 ? '(Chưa làm)' : '(Một phần)'}
                  </button>
                `).join('')}
              </div>
              <div style="font-size:10.5px; color:#34d399; margin-top:4px;">
                Điểm hiện tại: <strong>${curCodePts}.0 / ${q.points}.0đ</strong>
              </div>
            </div>
          `;
        } else {
          html += `
            <div style="font-size:11px; color:#34d399; background:rgba(16,185,129,0.08); padding:8px; border-radius:4px; border:1px solid rgba(16,185,129,0.2);">
              ✓ <strong>Tiêu chuẩn trắc nghiệm:</strong> Đúng +${q.points}đ, Sai 0.0đ. Phân loại nhận thức: Vận dụng cao / Tính toán bản chất.
            </div>
          `;
        }

        container.innerHTML = html;'''

    code = code.replace(old_inspector_rubric, new_inspector_rubric)

    # 9. Sửa nút trong bài essay và code trong renderCenter (P0-1)
    old_essay_buttons = '''            <div style="margin-top:10px; display:flex; justify-content:space-between;">
              <button class="btn" onclick="insertEssayTemplate('${q.id}')">Nạp khung mẫu 5 bước chuẩn</button>
              <button class="btn btn-primary" onclick="runEssayRubric('${q.id}')">⚡ Chấm Điểm Rubric Tự Động</button>
            </div>'''

    new_essay_buttons = '''            <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
              <button class="btn" onclick="insertEssayTemplate('${q.id}')">Nạp khung mẫu 5 bước</button>
              <button class="btn btn-primary" onclick="runEssayKeywordCheck('${q.id}')">⚡ Gợi ý từ khóa Rubric</button>
            </div>'''
    code = code.replace(old_essay_buttons, new_essay_buttons)

    # 10. Ghi đè vào docs/generate_full_hub.py
    with open(gen_file, "w", encoding="utf-8") as f:
        f.write(code)
    print("✓ Đã cập nhật docs/generate_full_hub.py thành công!")

if __name__ == "__main__":
    update()
