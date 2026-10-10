// scripts/verify_html_dom_e2e.mjs
// Kiểm thử E2E trực tiếp trên DOM của public/olympic_ai_study_hub.html bằng JSDOM

import fs from 'fs';
import { JSDOM } from 'jsdom';
import assert from 'assert';

const htmlContent = fs.readFileSync('public/olympic_ai_study_hub.html', 'utf8');

const dom = new JSDOM(htmlContent, {
  runScripts: 'dangerously'
});

const { window } = dom;
const { document } = window;

console.log('✓ JSDOM đã nạp thành công public/olympic_ai_study_hub.html');

// 1. Kiểm tra ALL_EXAMS trong HTML
const registry = window.eval('ALL_EXAMS');
assert(registry, 'ALL_EXAMS phải tồn tại trong window');
const examIds = Object.keys(registry);
console.log(`-> Đã nạp ${examIds.length} đề thi trong HTML: ${examIds.join(', ')}`);
assert.strictEqual(examIds.length, 6, 'Phải có đủ 6 đề thi');

// 2. Kiểm tra VOAI 2025
window.switchExam('voai-2025');
const voaiExam = window.eval('EXAM');
assert.strictEqual(voaiExam.id, 'voai-2025');
assert.strictEqual(voaiExam.questions.length, 100);

// Kiểm tra ticker VOAI 2025
window.renderHeaderStats();
const voaiGraded = document.getElementById('tickerTotalScore').textContent;
const voaiEssayEl = document.getElementById('tickerEssayScore');
console.log(`VOAI 2025 Ticker: Graded = ${voaiGraded}, Essay Display = ${voaiEssayEl.style.display}`);
assert(voaiGraded.includes('100.0đ'), 'VOAI 2025 phải có mẫu số 100.0đ');
assert.strictEqual(voaiEssayEl.style.display, 'none', 'VOAI 2025 không có tự luận, ticker phải bị ẩn (display: none)');

// Kiểm tra các câu đặc biệt trong VOAI 2025
const qMap = new Map(voaiExam.questions.map(q => [q.id, q]));

// Q10
const q10 = qMap.get('VOAI25-010');
assert(q10.prompt.includes('Tọa độ $(x_1, y_1, x_2, y_2)$'), 'Q10 phải có bảng tọa độ B1, B2, B3');
assert(q10.prompt.includes('0.95'), 'Q10 phải có điểm tin cậy 0.95');
assert.strictEqual(q10.answer, 'C', 'Q10 đáp án phải là C');
console.log('✓ VOAI25-010: Bảng NMS và options chuẩn xác (Key C)');

// Q24
const q24 = qMap.get('VOAI25-024');
assert.strictEqual(q24.answer, 'B', 'Q24 đáp án đề gốc phải là B');
assert(q24.options.find(o => o.key === 'B').text.includes('d(x, a)'), 'Q24 Option B phải là d(x, a)');
console.log('✓ VOAI25-024: 1-NN đo d(x, a) chuẩn đề gốc (Key B)');

// Q25
const q25 = qMap.get('VOAI25-025');
assert(q25.prompt.includes('S1 | 2 | 2 | 0 | Đỏ'), 'Q25 phải có bảng 8 mẫu k-NN');
assert(q25.prompt.includes('Q = (6, 2, 6)'), 'Q25 phải có điểm truy vấn Q');
assert.strictEqual(q25.answer, 'C', 'Q25 đáp án phải là C (Xanh lá)');
console.log('✓ VOAI25-025: Bảng 8 mẫu k-NN chuẩn xác (Key C)');

// Q32
const q32 = qMap.get('VOAI25-032');
assert(q32.prompt.includes('10,  20,  30,  40'), 'Q32 ma trận phải là 4x4, không phải 3x3');
assert.strictEqual(q32.answer, 'C', 'Q32 đáp án phải là C (60)');
console.log('✓ VOAI25-032: Ma trận 4x4 Average Pooling chuẩn xác (Key C)');

// Q37
const q37 = qMap.get('VOAI25-037');
assert(q37.prompt.includes('Bảng 1'), 'Q37 phải có Bảng 1 sinh viên');
assert(q37.prompt.includes('Qua môn (Passed)'), 'Q37 phải có cột Passed');
assert.strictEqual(q37.answer, 'C', 'Q37 đáp án phải là C (0.92)');
console.log('✓ VOAI25-037: Bảng 6 sinh viên entropy chuẩn xác (Key C - 0.92)');

// Q58
const q58 = qMap.get('VOAI25-058');
assert(q58.prompt.includes('Train Set Confusion Matrix'), 'Q58 phải có Confusion Matrix Train Set');
assert(q58.prompt.includes('Test Set Confusion Matrix'), 'Q58 phải có Confusion Matrix Test Set');
assert.strictEqual(q58.answer, 'A', 'Q58 đáp án phải là A (Overfitting)');
console.log('✓ VOAI25-058: 2 Confusion Matrix phục hồi đầy đủ (Key A)');

// Q68
const q68 = qMap.get('VOAI25-068');
assert(q68.prompt.includes('Random Forest gồm $K$ cây'), 'Q68 prompt KaTeX chuẩn');
assert.strictEqual(q68.answer, 'D', 'Q68 đáp án phải là D (1/K sum)');
console.log('✓ VOAI25-068: KaTeX Random Forest chuẩn xác (Key D)');

// Q73
const q73 = qMap.get('VOAI25-073');
assert(q73.prompt.includes('def identity_block'), 'Q73 phải có code identity_block');
assert(q73.prompt.includes('21     X = Add()([X_shortcut, X])'), 'Q73 phải có dòng 21 Add()');
assert.strictEqual(q73.answer, 'D', 'Q73 đáp án phải là D');
console.log('✓ VOAI25-073: Code 24 dòng identity_block chuẩn xác (Key D)');

// Q80
const q80 = qMap.get('VOAI25-080');
assert(q80.prompt.includes('15, 17, 10, 26, 14, 12, 11, 13'), 'Q80 phải đủ 8 cặp số');
assert.strictEqual(q80.answer, 'D', 'Q80 đáp án phải là D (7.5)');
console.log('✓ VOAI25-080: Đủ 8 cặp số MSE = 7.5 (Key D)');

// 3. Kiểm tra Dropdown Selector Đã Đồng Bộ (100c)
const examSelector = document.getElementById('examSelector');
assert(examSelector, 'examSelector phải tồn tại trong DOM');
const options = Array.from(examSelector.options);
console.log(`Dropdown Options (${options.length} tùy chọn):`);
options.forEach(opt => console.log(`   - [${opt.value}] ${opt.text}`));
assert.strictEqual(options.length, 6, 'Dropdown phải có đủ 6 đề thi');
options.forEach(opt => {
  assert(opt.text.includes('(100c)'), `Option ${opt.value} phải hiển thị (100c), thực tế: ${opt.text}`);
});
console.log('✓ Dropdown selector: 100% options đều hiển thị (100c) đồng bộ chuẩn xác!');

// 4. Kiểm tra Đề 04
window.switchExam('olp-04');
const olp04Exam = window.eval('EXAM');
assert.strictEqual(olp04Exam.id, 'olp-04');
assert.strictEqual(olp04Exam.questions.length, 100);

window.renderHeaderStats();
const olp04Graded = document.getElementById('tickerTotalScore').textContent;
const olp04EssayEl = document.getElementById('tickerEssayScore');
console.log(`Đề 04 Ticker: Graded = ${olp04Graded}, Essay Display = ${olp04EssayEl.style.display}`);
assert(olp04Graded.includes('100.0đ'), 'Đề 04 phải có mẫu số graded 100.0đ');
assert.strictEqual(olp04EssayEl.style.display, 'none', 'Đề 04 100% trắc nghiệm, ticker tự luận phải bị ẩn (display: none)');
console.log('✓ Đề 04: Chuẩn hóa 100 câu trắc nghiệm khách quan (100.0đ)');

// 5. Kiểm tra Đề 05
window.switchExam('olp-05');
const olp05Exam = window.eval('EXAM');
assert.strictEqual(olp05Exam.id, 'olp-05');
assert.strictEqual(olp05Exam.questions.length, 100);

window.renderHeaderStats();
const olp05Graded = document.getElementById('tickerTotalScore').textContent;
const olp05EssayEl = document.getElementById('tickerEssayScore');
console.log(`Đề 05 Ticker: Graded = ${olp05Graded}, Essay Display = ${olp05EssayEl.style.display}`);
assert(olp05Graded.includes('100.0đ'), 'Đề 05 phải có mẫu số graded 100.0đ');
assert.strictEqual(olp05EssayEl.style.display, 'none', 'Đề 05 không có tự luận, ticker phải bị ẩn (display: none)');
console.log('✓ Đề 05: Graded 100.0đ và Tự luận bị ẩn chuẩn xác');

console.log('\n=== TẤT CẢ KIỂM THỬ E2E TRỰC TIẾP TRÊN DOM ĐỀU PASS 100% ===');
