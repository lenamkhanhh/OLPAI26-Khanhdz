// scripts/audit_katex_syntax.mjs
// Kiểm toán cú pháp KaTeX toàn diện cho 3 đề thi (prompt, options, explanation, modelAnswer, rubric),
// toàn văn giáo trình (toàn bộ nội dung đến EOF), và bảng công thức cốt lõi.
import fs from 'fs';
import katex from 'katex';

function stripCodeBlocks(text) {
  if (!text) return '';
  // Xóa fenced code blocks: ```...```
  let s = text.replace(/```[\s\S]*?```/g, '');
  // Xóa inline code blocks: `...`
  s = s.replace(/`[^`\n]*?`/g, '');
  return s;
}

function extractLatex(text, sourceLocation) {
  if (!text) return { snippets: [], delimiterErrors: [] };
  
  const clean = stripCodeBlocks(text);
  const snippets = [];
  const delimiterErrors = [];

  // Kiểm tra delimiter chẵn lẻ
  // Đếm $$
  const doubleDollarMatches = clean.match(/\$\$/g);
  if (doubleDollarMatches && doubleDollarMatches.length % 2 !== 0) {
    delimiterErrors.push({
      source: sourceLocation,
      error: `Số lượng delimiter display math ($$) lẻ: ${doubleDollarMatches.length}`
    });
  }

  // 1. Trích xuất Display math: $$...$$
  const displayRegex = /\$\$([\s\S]*?)\$\$/g;
  let match;
  while ((match = displayRegex.exec(clean)) !== null) {
    const tex = match[1].trim();
    if (tex) {
      snippets.push({ tex, display: true, raw: match[0] });
    }
  }

  // 2. Trích xuất LaTeX brackets: \[...\]
  const bracketRegex = /\\\[([\s\S]*?)\\\]/g;
  while ((match = bracketRegex.exec(clean)) !== null) {
    const tex = match[1].trim();
    if (tex) {
      snippets.push({ tex, display: true, raw: match[0] });
    }
  }

  // Xóa display math trước khi tìm inline
  const textNoDisplay = clean.replace(/\$\$[\s\S]*?\$\$/g, '').replace(/\\\[[\s\S]*?\\\]/g, '');

  // Kiểm tra single $ không thoát
  const singleDollarCount = (textNoDisplay.match(/(^|[^\\])\$/g) || []).length;
  if (singleDollarCount % 2 !== 0) {
    delimiterErrors.push({
      source: sourceLocation,
      error: `Số lượng delimiter inline math ($) lẻ: ${singleDollarCount}`
    });
  }

  // 3. Trích xuất Inline math: $...$
  const inlineRegex = /(?:^|[^\\])\$([^$\n\r]+?)\$/g;
  while ((match = inlineRegex.exec(textNoDisplay)) !== null) {
    const tex = match[1].trim();
    if (tex) {
      snippets.push({ tex, display: false, raw: match[0] });
    }
  }

  // 4. Trích xuất LaTeX parens: \(...\)
  const parenRegex = /\\\(([\s\S]*?)\\\)/g;
  while ((match = parenRegex.exec(textNoDisplay)) !== null) {
    const tex = match[1].trim();
    if (tex) {
      snippets.push({ tex, display: false, raw: match[0] });
    }
  }

  return { snippets, delimiterErrors };
}

function testLatexSnippet(item, sourceLocation) {
  const { tex, display, raw } = item;
  if (!tex) return null;
  try {
    katex.renderToString(tex, {
      displayMode: display,
      throwOnError: true,
      strict: false
    });
    return null; // Cú pháp KaTeX hợp lệ
  } catch (err) {
    return {
      source: sourceLocation,
      raw,
      tex,
      error: err.message
    };
  }
}

const errors = [];
let totalSnippetsCount = 0;

// 1. Audit toàn bộ các đề thi JSON trong src/data/exams
const examsDir = 'src/data/exams';
const exams = fs.readdirSync(examsDir).filter(f => f.endsWith('.json')).sort();
console.log(`-> Quét động ${exams.length} ngân hàng đề thi: ${exams.join(', ')}`);
for (const examFile of exams) {
  const path = `${examsDir}/${examFile}`;
  const data = JSON.parse(fs.readFileSync(path, 'utf8'));
  for (const q of data.questions) {
    // Prompt
    const promptRes = extractLatex(q.prompt, `${examFile} -> ${q.id} [prompt]`);
    errors.push(...promptRes.delimiterErrors);
    for (const item of promptRes.snippets) {
      totalSnippetsCount++;
      const err = testLatexSnippet(item, `${examFile} -> ${q.id} [prompt]`);
      if (err) errors.push(err);
    }

    // Options
    if (q.options) {
      for (const opt of q.options) {
        const optRes = extractLatex(opt.text, `${examFile} -> ${q.id} [option ${opt.key}]`);
        errors.push(...optRes.delimiterErrors);
        for (const item of optRes.snippets) {
          totalSnippetsCount++;
          const err = testLatexSnippet(item, `${examFile} -> ${q.id} [option ${opt.key}]`);
          if (err) errors.push(err);
        }
      }
    }

    // Explanation
    if (q.explanation) {
      const expRes = extractLatex(q.explanation, `${examFile} -> ${q.id} [explanation]`);
      errors.push(...expRes.delimiterErrors);
      for (const item of expRes.snippets) {
        totalSnippetsCount++;
        const err = testLatexSnippet(item, `${examFile} -> ${q.id} [explanation]`);
        if (err) errors.push(err);
      }
    }

    // ModelAnswer (Essay)
    if (q.modelAnswer) {
      const maRes = extractLatex(q.modelAnswer, `${examFile} -> ${q.id} [modelAnswer]`);
      errors.push(...maRes.delimiterErrors);
      for (const item of maRes.snippets) {
        totalSnippetsCount++;
        const err = testLatexSnippet(item, `${examFile} -> ${q.id} [modelAnswer]`);
        if (err) errors.push(err);
      }
    }

    // Rubric (Essay)
    if (q.rubric && Array.isArray(q.rubric)) {
      q.rubric.forEach((r, idx) => {
        const rubRes = extractLatex(r, `${examFile} -> ${q.id} [rubric ${idx + 1}]`);
        errors.push(...rubRes.delimiterErrors);
        for (const item of rubRes.snippets) {
          totalSnippetsCount++;
          const err = testLatexSnippet(item, `${examFile} -> ${q.id} [rubric ${idx + 1}]`);
          if (err) errors.push(err);
        }
      });
    }
  }
}

// 2. Audit toàn bộ giáo trình content/01-ly-thuyet-olp-ai.md
if (fs.existsSync('content/01-ly-thuyet-olp-ai.md')) {
  const theoryMd = fs.readFileSync('content/01-ly-thuyet-olp-ai.md', 'utf8');
  const theoryRes = extractLatex(theoryMd, 'content/01-ly-thuyet-olp-ai.md [toàn văn]');
  errors.push(...theoryRes.delimiterErrors);
  for (const item of theoryRes.snippets) {
    totalSnippetsCount++;
    const err = testLatexSnippet(item, 'content/01-ly-thuyet-olp-ai.md');
    if (err) errors.push(err);
  }
}

// 3. Audit Bảng công thức thật từ generator / HTML
if (fs.existsSync('docs/generate_full_hub.py')) {
  const genPy = fs.readFileSync('docs/generate_full_hub.py', 'utf8');
  // Match "tex": "..." hoặc "tex": r"..." trên từng dòng
  const texRegex = /"tex":\s*r?["']([^"'\r\n]+)["']/g;
  let fm;
  while ((fm = texRegex.exec(genPy)) !== null) {
    const texStr = fm[1];
    totalSnippetsCount++;
    const err = testLatexSnippet({ tex: texStr, display: true, raw: texStr }, 'generate_full_hub.py [FORMULAS]');
    if (err) errors.push(err);
  }
}

console.log('=== KẾT QUẢ AUDIT KATEX SYNTAX ===');
console.log(`Đã quét và kiểm thử tổng cộng: ${totalSnippetsCount} đoạn công thức toán học.`);
console.log(`Tổng số lỗi cú pháp hoặc delimiter phát hiện: ${errors.length}`);

if (errors.length > 0) {
  console.log('\nDANH SÁCH LỖI:');
  errors.forEach((e, idx) => {
    console.log(`\n[${idx + 1}] Nguồn: ${e.source}`);
    if (e.tex) console.log(`    TeX: ${e.tex}`);
    console.log(`    Lỗi: ${e.error}`);
  });
  process.exit(1);
} else {
  console.log('Tất cả công thức KaTeX đều hợp lệ 100% về mặt cú pháp parser!');
  console.log('Ghi chú: Kiểm toán cú pháp đảm bảo KaTeX không quăng ngoại lệ render; không thay thế thẩm định khoa học.');
  process.exit(0);
}
