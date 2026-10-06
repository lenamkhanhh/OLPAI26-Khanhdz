// Validator cho bo de OLP AI HCMUS 2026 (module A/B/C, khong co D).
// Moi de: 60 cau trac nghiem/code (thang 100 diem) + 4-5 cau tu luan (cham rieng).
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const ROOT = process.cwd();
const EXAMS_DIR = path.join(ROOT, 'src', 'data', 'exams');

const GRADED_COUNT = 60; // mcq + code
const ESSAY_MIN = 4;
const ESSAY_MAX = 5;
const EXPECTED_POINTS = 100; // tong diem trac nghiem + code
const ESSAY_POINTS = 10; // moi cau tu luan thang 10, cham rieng
const EXPECTED_MODULES = { A: 12, B: 18, C: 30 }; // dem tren cau graded (mcq+code)
const EXPECTED_CODE = 2; // nam trong B
const VALID_MODULES = new Set(['A', 'B', 'C']);
const VALID_TYPES = new Set(['mcq', 'code', 'essay']);
const VALID_ANSWERS = new Set(['A', 'B', 'C', 'D']);

function fail(message) {
  console.error(`ASSERT ${message}`);
  process.exitCode = 1;
}

function assert(condition, message) {
  if (!condition) fail(message);
}

function readJson(file) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (error) {
    fail(`${path.relative(ROOT, file)} is not valid JSON: ${error.message}`);
    return null;
  }
}

function validateExam(exam, displayFile) {
  assert(typeof exam.id === 'string' && exam.id.length > 0, `${displayFile}: missing id`);
  assert(typeof exam.title === 'string' && exam.title.length > 0, `${displayFile}: missing title`);
  assert(typeof exam.description === 'string' && exam.description.trim().length > 0, `${displayFile}: missing description`);
  assert(typeof exam.durationMinutes === 'number' && exam.durationMinutes > 0, `${displayFile}: durationMinutes invalid`);
  assert(Math.abs(exam.totalPoints - EXPECTED_POINTS) < 0.001, `${displayFile}: totalPoints must be ${EXPECTED_POINTS}`);
  assert(typeof exam.disclaimer === 'string' && exam.disclaimer.trim().length > 0, `${displayFile}: missing disclaimer`);
  assert(Array.isArray(exam.questions), `${displayFile}: questions must be an array`);
  if (!Array.isArray(exam.questions)) return { graded: 0 };

  if (exam.moduleOverview !== undefined) {
    assert(
      Array.isArray(exam.moduleOverview) &&
        exam.moduleOverview.length === 3 &&
        exam.moduleOverview.every((item) => typeof item === 'string' && item.trim().length > 0),
      `${displayFile}: moduleOverview must contain 3 non-empty strings (A/B/C)`
    );
  }
  if (exam.moduleLabels !== undefined) {
    for (const module of VALID_MODULES) {
      assert(typeof exam.moduleLabels[module] === 'string' && exam.moduleLabels[module].trim().length > 0, `${displayFile}: moduleLabels.${module} missing`);
    }
    assert(exam.moduleLabels.D === undefined, `${displayFile}: moduleLabels must not contain D`);
  }

  const questionIds = new Set();
  const answerDist = { A: 0, B: 0, C: 0, D: 0 };
  const gradedCounts = { A: 0, B: 0, C: 0 };
  let gradedPoints = 0;
  let gradedTotal = 0;
  let codeTotal = 0;
  const essays = [];

  for (const [idx, q] of exam.questions.entries()) {
    const loc = `${displayFile} question #${idx + 1}`;
    assert(q && typeof q === 'object' && !Array.isArray(q), `${loc}: question must be an object`);
    if (!q || typeof q !== 'object') continue;
    assert(typeof q.id === 'string' && q.id.length > 0, `${loc}: missing id`);
    assert(!questionIds.has(q.id), `${loc}: duplicate question id ${q.id}`);
    questionIds.add(q.id);
    assert(VALID_MODULES.has(q.module), `${loc}: invalid module ${q.module} (chi chap nhan A/B/C)`);
    assert(VALID_TYPES.has(q.type), `${loc}: invalid type ${q.type}`);
    assert(typeof q.points === 'number' && q.points > 0, `${loc}: points must be positive`);
    assert(typeof q.prompt === 'string' && q.prompt.trim().length >= 8, `${loc}: prompt too short`);

    if (q.type === 'mcq') {
      assert(Array.isArray(q.options) && q.options.length === 4, `${loc}: MCQ must have exactly 4 options`);
      if (Array.isArray(q.options)) {
        const keys = q.options.map((o) => o?.key);
        assert(keys.join('') === 'ABCD', `${loc}: option keys must be A/B/C/D`);
        const texts = q.options.map((o) => String(o?.text ?? '').trim().toLowerCase());
        assert(new Set(texts).size === texts.length, `${loc}: duplicate option text`);
      }
      assert(VALID_ANSWERS.has(q.answer), `${loc}: answer must be A/B/C/D`);
      assert(typeof q.explanation === 'string' && q.explanation.trim().length >= 8, `${loc}: explanation too short`);
      answerDist[q.answer] += 1;
      gradedTotal += 1;
      gradedPoints += q.points;
      if (VALID_MODULES.has(q.module)) gradedCounts[q.module] += 1;
    } else if (q.type === 'code') {
      assert(q.module === 'B', `${loc}: code questions must be in module B`);
      assert(typeof q.modelAnswer === 'string' && q.modelAnswer.trim().length >= 12, `${loc}: code needs modelAnswer`);
      assert(Array.isArray(q.rubric) && q.rubric.length >= 3, `${loc}: code needs >= 3 rubric items`);
      codeTotal += 1;
      gradedTotal += 1;
      gradedPoints += q.points;
      if (VALID_MODULES.has(q.module)) gradedCounts[q.module] += 1;
    } else if (q.type === 'essay') {
      assert(q.module === 'C', `${loc}: essay questions must be in module C`);
      assert(Math.abs(q.points - ESSAY_POINTS) < 0.001, `${loc}: essay points must be ${ESSAY_POINTS} (cham rieng)`);
      assert(typeof q.modelAnswer === 'string' && q.modelAnswer.trim().length >= 12, `${loc}: essay needs modelAnswer`);
      assert(Array.isArray(q.rubric) && q.rubric.length >= 3, `${loc}: essay needs >= 3 rubric items`);
      essays.push(q);
    }
  }

  assert(gradedTotal === GRADED_COUNT, `${displayFile}: expected ${GRADED_COUNT} graded questions (mcq+code), found ${gradedTotal}`);
  assert(codeTotal === EXPECTED_CODE, `${displayFile}: expected ${EXPECTED_CODE} code questions, found ${codeTotal}`);
  assert(essays.length >= ESSAY_MIN && essays.length <= ESSAY_MAX, `${displayFile}: expected ${ESSAY_MIN}-${ESSAY_MAX} essays, found ${essays.length}`);
  for (const [module, expected] of Object.entries(EXPECTED_MODULES)) {
    assert(gradedCounts[module] === expected, `${displayFile}: graded module ${module} expected ${expected}, found ${gradedCounts[module]}`);
  }
  assert(Math.abs(gradedPoints - EXPECTED_POINTS) < 0.001, `${displayFile}: graded points must sum to ${EXPECTED_POINTS}, found ${gradedPoints}`);
  for (const [key, count] of Object.entries(answerDist)) {
    assert(count <= 24, `${displayFile}: answer ${key} appears ${count} times (>40% of 60, dap an lech)`);
    assert(count >= 6, `${displayFile}: answer ${key} appears only ${count} times (<10% of 60, dap an lech)`);
  }
  console.log(`PASS ${displayFile}: ${gradedTotal} graded + ${essays.length} essays`);
  return { graded: gradedTotal, essays: essays.length };
}

const files = fs.existsSync(EXAMS_DIR)
  ? fs.readdirSync(EXAMS_DIR).filter((f) => f.endsWith('.json')).sort()
  : [];
assert(files.length >= 1, 'cần ít nhất 1 đề trong src/data/exams');

const examIds = new Set();
const questionIds = new Set();
const promptKeys = new Set();
let gradedSum = 0;
let essaySum = 0;

for (const file of files) {
  const displayFile = `exams/${file}`;
  const exam = readJson(path.join(EXAMS_DIR, file));
  if (!exam) continue;
  assert(!examIds.has(exam.id), `${displayFile}: duplicate exam id ${exam.id}`);
  examIds.add(exam.id);
  for (const q of Array.isArray(exam.questions) ? exam.questions : []) {
    assert(!questionIds.has(q.id), `${displayFile}: globally duplicate question id ${q.id}`);
    questionIds.add(q.id);
    const key = String(q.prompt ?? '').replace(/\s+/g, ' ').trim().toLowerCase();
    assert(!promptKeys.has(key), `${displayFile}: duplicate prompt across exams: ${q.id}`);
    promptKeys.add(key);
  }
  const { graded, essays } = validateExam(exam, displayFile);
  gradedSum += graded;
  essaySum += essays;
}

if (process.exitCode) {
  console.error('\nValidation failed. Fix the errors above.');
  process.exit(process.exitCode);
}
console.log(`\nAll ${files.length} exams valid. Graded: ${gradedSum}. Essays: ${essaySum}.`);
