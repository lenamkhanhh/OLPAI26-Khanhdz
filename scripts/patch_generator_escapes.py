# -*- coding: utf-8 -*-
import os
import sys
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"

def double_braces(s):
    s = re.sub(r'(?<!\{)\{(?!\{)', '{{', s)
    s = re.sub(r'(?<!\})\}(?!\})', '}}', s)
    return s

def patch():
    gen_file = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")
    with open(gen_file, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Đoạn Rubric functions (Không dùng bất kỳ \n nào, dùng String.fromCharCode(10))
    pattern_rubric = r'// Rubric Evaluator & Checklist[\s\S]*?function insertEssayTemplate'
    
    new_rubric_raw = '''// Rubric Evaluator & Checklist (Tự đối chiếu thật - P0-1)
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
        alert([
          '⚠️ Bài làm hiện đang để trống hoặc quá ngắn (dưới 20 ký tự).',
          'Điểm đề xuất: 0.0/' + q.points + 'đ.',
          'Hãy nhấn "Nạp khung mẫu 5 bước" và điền chi tiết các phân tích kỹ thuật.'
        ].join(String.fromCharCode(10)));
        return;
      }

      const lowerText = text.toLowerCase();
      let checkedMap = {};
      let matchedCount = 0;

      rubricList.forEach((crit, idx) => {
        const words = crit.toLowerCase().replace(/[^a-z0-9àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ\\s]/g, ' ')
          .split(/\\s+/).filter(w => w.length > 3);
        let matches = 0;
        for (const w of words) {
          if (lowerText.indexOf(w) !== -1) matches++;
        }
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
        summary: 'Hệ thống gợi ý từ khóa phát hiện ' + matchedCount + '/' + rubricList.length + ' tiêu chí có xuất hiện thuật ngữ liên quan trong bài làm. (Lưu ý: Đây là gợi ý tự động hỗ trợ tự đối chiếu, không phải điểm chấm chính thức của hội đồng).'
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
      alert([
        '⚡ [Gợi ý Từ khóa Tự động]',
        'Đã đối chiếu bài làm với ' + rubricList.length + ' tiêu chí.',
        'Điểm đề xuất: ' + proposedScore + '/' + q.points + 'đ.',
        'Bạn có thể điều chỉnh các ô đánh dấu bên bảng Inspector bên phải để hoàn thiện điểm tự đánh giá.'
      ].join(String.fromCharCode(10)));
    }

    function insertEssayTemplate'''

    code = re.sub(pattern_rubric, lambda m: double_braces(new_rubric_raw), code)

    # 2. Đoạn runCustomCode & submitContestConfirm (Dùng String.fromCharCode(10))
    pattern_code_sub = r'function runCustomCode\(qid\) \{[\s\S]*?// Keyboard Shortcuts'
    new_code_sub_raw = '''function runCustomCode(qid) {
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
      alert([
        'ℹ️ [Sandbox Cục Bộ Trình Duyệt]',
        'Trình duyệt hiện tại chưa tích hợp runtime Python/PyTorch trực tiếp.',
        '',
        'Mã nguồn của bạn đã được ghi nhận. Vui lòng mở rộng mục "ĐÁP ÁN MẪU & GIẢI PHÁP CHUẨN" bên dưới để đối chiếu logic thuật toán và các trường hợp kiểm thử.'
      ].join(String.fromCharCode(10)));
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
    }

    function submitContestConfirm() {
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

      if (confirm(reportLines.join(String.fromCharCode(10)))) {
        alert('🎉 Bạn đã nộp bài thành công!' + String.fromCharCode(10) + 'Graded: ' + gradedPts.toFixed(1) + '/' + maxGradedPts.toFixed(1) + 'đ | Tự luận: ' + essaySelfPts.toFixed(1) + '/' + maxEssayPts.toFixed(1) + 'đ');
      }
    }

    // Keyboard Shortcuts'''

    code = re.sub(pattern_code_sub, lambda m: double_braces(new_code_sub_raw), code)

    with open(gen_file, "w", encoding="utf-8") as f:
        f.write(code)
    print("✓ Đã cập nhật docs/generate_full_hub.py sạch bóng escape lỗi!")

if __name__ == "__main__":
    patch()
