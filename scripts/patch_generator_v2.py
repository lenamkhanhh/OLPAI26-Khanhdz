# -*- coding: utf-8 -*-
"""
scripts/patch_generator_v2.py
Cập nhật docs/generate_full_hub.py theo đúng audit VERIFY_LAN_2_2026-10-08:
1. Sửa tổng điểm code:
   - renderHeaderStats, submitContestConfirm, footer, sidebar matrix:
     Với câu type=code, gradedPts cộng đúng a.selfScore (hoặc a.points), KHÔNG lấy q.points chỉ vì verdict AC.
   - setCodeSelfScore: verdict là 'AC' khi pts == q.points, 'PARTIAL' khi 0 < pts < q.points, 'WA' khi pts == 0.
2. Sửa gợi ý từ khóa rubric:
   - Tách/loại bỏ template boilerplate trước khi đếm từ khóa.
   - Khung template chưa điền (hoặc text < 20 ký tự thực tế) -> điểm đề xuất 0.0đ.
   - Khi bài làm bị xóa/trống, RESET điểm tự chấm về 0, không giữ điểm 10 cũ.
"""

import os
import re

ROOT_DIR = r"D:\Code\Code\AIO\Code\olp-ai-hcmus26"
GEN_FILE = os.path.join(ROOT_DIR, "docs", "generate_full_hub.py")

with open(GEN_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Cập nhật renderHeaderStats để tính đúng điểm partial cho code questions
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
    print("✓ Đã cập nhật renderHeaderStats (tính đúng partial code score)")
else:
    print("! Cảnh báo: Không tìm thấy old_stats_block trong generate_full_hub.py")

# 2. Cập nhật submitContestConfirm và setCodeSelfScore
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
    print("✓ Đã cập nhật setCodeSelfScore và submitContestConfirm")
else:
    print("! Cảnh báo: Không tìm thấy old_code_sub_block")

# 3. Cập nhật runEssayKeywordCheck
old_essay_check_pattern = r'function runEssayKeywordCheck\(qid\) \{[\s\S]*?function insertEssayTemplate'

new_essay_check_code = """function runEssayKeywordCheck(qid) {{
      const ta = document.getElementById('essayInput_' + qid);
      const rawText = ta ? ta.value : (answers[qid]?.text || '');
      const q = EXAM.questions[currentIndex];
      const rubricList = q.rubric || [];
      const ptsPerCrit = q.points / Math.max(1, rubricList.length);

      // Loại bỏ các dòng tiêu đề và nhãn mặc định của khung mẫu 5 bước để kiểm tra nội dung thực tế
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

      // Nếu bài làm trống hoặc chỉ có khung template chưa điền nội dung (dưới 20 ký tự thực tế)
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

      // Quét từ khóa trên nội dung thực tế của thí sinh
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

    function insertEssayTemplate"""

if re.search(old_essay_check_pattern, content):
    content = re.sub(old_essay_check_pattern, lambda m: new_essay_check_code, content)
    print("✓ Đã cập nhật runEssayKeywordCheck (chống cho điểm template trống, reset điểm khi xóa)")
else:
    print("! Cảnh báo: Không match old_essay_check_pattern")

with open(GEN_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Hoàn tất cập nhật docs/generate_full_hub.py!")
