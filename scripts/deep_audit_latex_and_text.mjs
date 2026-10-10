// scripts/deep_audit_latex_and_text.mjs
// Kiểm toán chuyên sâu toàn diện 600 câu hỏi:
// 1. KaTeX render thực tế (throwOnError: true)
// 2. Delimiter toán học không đóng / lỗi cú pháp
// 3. Lỗi dính chữ OCR tiếng Việt & thiếu khoảng trắng quanh dấu câu / ký hiệu toán
// 4. Độ hoàn thiện của lời giải (ELI5, Toán, Bẫy, Mắt xích) & khớp key đáp án

import fs from 'fs';
import path from 'path';
import katex from 'katex';

const exams = ['olp-01', 'olp-02', 'olp-03', 'olp-04', 'olp-05', 'voai-2025'];
const ROOT = process.cwd();

let totalSnippets = 0;
const katexErrors = [];
const unclosedDelimiters = [];
const gluedWordIssues = [];
const mathSpacingIssues = [];
const explanationKeyMismatches = [];
const incompleteExplanations = [];

// Các mẫu dính chữ phổ biến từ OCR đề thi gốc
const KNOWN_GLUED_PATTERNS = [
  /đểlưu/i, /sẽtự/i, /độchính/i, /trởthành/i, /cắtghép/i, /đượctạo/i,
  /phépnhân/i, /tínhchất/i, /môtả/i, /trọngsố/i, /họcsâu/i, /mạngnơ/i,
  /bảnchất/i, /khoảngcách/i, /hàmmất/i, /quầnthể/i, /phânphối/i,
  /khônggian/i, /kếtquả/i, /xácliệu/i, /xácsuất/i, /độlệch/i,
  /tươngquan/i, /chuẩnhoá/i, /chuẩnhóa/i, /hộitụ/i, /đạohàm/i
];

exams.forEach(id => {
  const filePath = path.join(ROOT, 'src', 'data', 'exams', `${id}.json`);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  data.questions.forEach((q, idx) => {
    const fields = [
      { name: 'prompt', text: q.prompt || '' },
      ...(q.options || []).map(o => ({ name: `option_${o.key}`, text: o.text || '' })),
      { name: 'explanation', text: q.explanation || '' }
    ];

    // 1. Kiểm tra từng trường văn bản
    fields.forEach(f => {
      const text = f.text;
      if (!text) return;

      // 1.1 Kiểm tra unclosed $$ hoặc lẻ $
      const dollarCount = (text.match(/\$/g) || []).length;
      if (dollarCount % 2 !== 0) {
        unclosedDelimiters.push({
          exam: id,
          qId: q.id,
          field: f.name,
          snippet: text.slice(0, 100),
          dollars: dollarCount
        });
      }

      // 1.2 KaTeX Render: Display math $$...$$
      const displayMatches = text.match(/\$\$([\s\S]*?)\$\$/g) || [];
      displayMatches.forEach(raw => {
        totalSnippets++;
        const math = raw.slice(2, -2).trim();
        try {
          katex.renderToString(math, { displayMode: true, throwOnError: true });
        } catch (e) {
          katexErrors.push({
            exam: id,
            qId: q.id,
            field: f.name,
            raw: raw.slice(0, 80),
            error: e.message
          });
        }
      });

      // 1.3 KaTeX Render: Inline math $...$
      const textWithoutDisplay = text.replace(/\$\$[\s\S]*?\$\$/g, '');
      const inlineMatches = textWithoutDisplay.match(/\$([^\$\n]+?)\$/g) || [];
      inlineMatches.forEach(raw => {
        totalSnippets++;
        const math = raw.slice(1, -1).trim();
        try {
          katex.renderToString(math, { displayMode: false, throwOnError: true });
        } catch (e) {
          katexErrors.push({
            exam: id,
            qId: q.id,
            field: f.name,
            raw: raw.slice(0, 80),
            error: e.message
          });
        }
      });

      // 1.4 Kiểm tra dính chữ OCR phổ biến
      KNOWN_GLUED_PATTERNS.forEach(pat => {
        const m = text.match(pat);
        if (m) {
          gluedWordIssues.push({
            exam: id,
            qId: q.id,
            field: f.name,
            matched: m[0],
            snippet: text.slice(Math.max(0, m.index - 20), m.index + 40)
          });
        }
      });

      // 1.5 Kiểm tra dính chữ giữa từ tiếng Việt và dấu câu (loại bỏ code identifiers như torch.nn, v.v.)
      // Tìm từ tiếng Việt có dấu đi liền sau dấu chấm/phẩy mà không có dấu cách: ví dụ "đúng.Chọn"
      const vnWordGlued = text.match(/([a-zA-ZÀ-ỹ]{2,})([,\.?!;:])([À-ỹA-Z][a-zA-ZÀ-ỹ]{2,})/g) || [];
      vnWordGlued.forEach(match => {
        if (/v\.v|e\.g|i\.e|etc/i.test(match)) return;
        gluedWordIssues.push({
          exam: id,
          qId: q.id,
          field: f.name,
          matched: match,
          snippet: text.slice(0, 100)
        });
      });

      // 1.6 Kiểm tra dính chữ sát ký hiệu toán ($):
      // - Chữ cái đứng ngay trước opening $: ví dụ "từ$x$"
      // - Chữ cái đứng ngay sau closing $: ví dụ "$x$thì"
      const leadingMathGlued = textWithoutDisplay.match(/([a-zA-ZÀ-ỹ0-9])\$(?!\$)/g) || [];
      // Với closing $, kiểm tra $ theo sau ngay lập tức là chữ cái tiếng Việt hoặc từ
      const trailingMathGlued = textWithoutDisplay.match(/\$([a-zA-ZÀ-ỹ])/g) || [];
      // Để phân biệt opening và closing, ta duyệt qua các khối math đã trích xuất:
      const mathTokens = textWithoutDisplay.match(/\$([^\$\n]+?)\$/g) || [];
      mathTokens.forEach(mToken => {
        const idx = textWithoutDisplay.indexOf(mToken);
        if (idx > 0) {
          const charBefore = textWithoutDisplay[idx - 1];
          if (/[a-zA-ZÀ-ỹ]/.test(charBefore)) {
            mathSpacingIssues.push({
              exam: id,
              qId: q.id,
              field: f.name,
              issue: `Dính chữ trước math: '${charBefore}${mToken}'`
            });
          }
        }
        const afterIdx = idx + mToken.length;
        if (afterIdx < textWithoutDisplay.length) {
          const charAfter = textWithoutDisplay[afterIdx];
          if (/[a-zA-ZÀ-ỹ]/.test(charAfter)) {
            mathSpacingIssues.push({
              exam: id,
              qId: q.id,
              field: f.name,
              issue: `Dính chữ sau math: '${mToken}${charAfter}'`
            });
          }
        }
      });
    });

    // 2. Kiểm tra độ hoàn thiện của lời giải (Explanation)
    const exp = q.explanation || '';
    if (exp.length < 150) {
      incompleteExplanations.push({
        exam: id,
        qId: q.id,
        length: exp.length,
        reason: 'Lời giải quá ngắn (<150 ký tự)'
      });
    }

    // 3. Kiểm tra xem lời giải có kết luận khớp q.answer không
    // Tìm các cụm: "Chọn đáp án **X**", "Chọn **X**", "Đáp án đúng là **X**", "Đáp án chính xác là **X**"
    const conclusionMatch = exp.match(/(?:Chọn|Đáp án|kết quả)(?: chính xác| đúng)?(?: là)?(?:\s+phương án|\s+đáp án)?\s+\*\*([A-D])\*\*/i);
    if (conclusionMatch) {
      const concludedKey = conclusionMatch[1].toUpperCase();
      if (concludedKey !== q.answer) {
        explanationKeyMismatches.push({
          exam: id,
          qId: q.id,
          qAnswer: q.answer,
          concludedKey,
          snippet: conclusionMatch[0]
        });
      }
    }
  });
});

console.log('====================================================');
console.log('       KẾT QUẢ KIỂM TOÁN CHUYÊN SÂU TOÀN DIỆN        ');
console.log('====================================================');
console.log(`1. Tổng số công thức KaTeX đã render thử: ${totalSnippets}`);
console.log(`   - Số lỗi KaTeX render (throwOnError: true): ${katexErrors.length}`);
if (katexErrors.length > 0) {
  console.log('   Chi tiết lỗi KaTeX:', katexErrors);
}

console.log(`2. Lỗi lẻ dấu phân cách ($): ${unclosedDelimiters.length}`);
if (unclosedDelimiters.length > 0) {
  console.log('   Chi tiết unclosed $:', unclosedDelimiters);
}

console.log(`3. Lỗi dính chữ OCR & Dấu câu: ${gluedWordIssues.length}`);
if (gluedWordIssues.length > 0) {
  console.log(`   (Hiển thị tối đa 10 lỗi tiêu biểu):`);
  console.log(gluedWordIssues.slice(0, 10));
}

console.log(`4. Dính chữ sát ký hiệu toán ($): ${mathSpacingIssues.length}`);
if (mathSpacingIssues.length > 0) {
  console.log(`   (Hiển thị tối đa 5 lỗi tiêu biểu):`);
  console.log(mathSpacingIssues.slice(0, 5));
}

console.log(`5. Lệch đáp án giữa q.answer và lời giải: ${explanationKeyMismatches.length}`);
if (explanationKeyMismatches.length > 0) {
  console.log('   Chi tiết lệch key:', explanationKeyMismatches);
}

console.log(`6. Lời giải chưa đủ độ sâu: ${incompleteExplanations.length}`);
if (incompleteExplanations.length > 0) {
  console.log('   Chi tiết lời giải ngắn:', incompleteExplanations);
}
console.log('====================================================');
