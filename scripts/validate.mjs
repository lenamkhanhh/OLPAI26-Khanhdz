// Validator cho bo de OLP AI HCMUS 2026 (module A/B/C, khong co D).
// Kiem tra cau truc thuc te cua tung de theo dac ta audit 2026-10-08:
// - De 01: 60 graded (58 mcq + 2 code, thang 100), 4 essay (cham rieng), modules A:12, B:18, C:30.
// - De 02: 60 graded (60 mcq, thang 90), 6 essay (cham rieng), modules A:12, B:24, C:24.
// - De 03: 50 graded (50 mcq, thang 100), 4 essay (cham rieng), modules A:25, B:25, C:0.
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const ROOT = process.cwd();
const EXAMS_DIR = path.join(ROOT, 'src', 'data', 'exams');

const EXAM_SPECS = {
  'olp-01': {
    gradedCount: 100,
    expectedPoints: 100,
    expectedCode: 0,
    essayMin: 0,
    essayMax: 0,
    expectedModules: { A: 25, B: 33, C: 42 }
  },
  'olp-02': {
    gradedCount: 100,
    expectedPoints: 100,
    expectedCode: 0,
    essayMin: 0,
    essayMax: 0,
    expectedModules: { A: 25, B: 35, C: 40 }
  },
  'olp-03': {
    gradedCount: 100,
    expectedPoints: 100,
    expectedCode: 0,
    essayMin: 0,
    essayMax: 0,
    expectedModules: { A: 32, B: 39, C: 29 }
  },
  'olp-04': {
    gradedCount: 100,
    expectedPoints: 100,
    expectedCode: 0,
    essayMin: 0,
    essayMax: 0,
    expectedModules: { A: 25, B: 35, C: 40 }
  },
  'voai-2025': {
    gradedCount: 100,
    expectedPoints: 100,
    expectedCode: 0,
    essayMin: 0,
    essayMax: 0,
    expectedModules: { A: 12, B: 48, C: 40 }
  },
  'olp-05': {
    gradedCount: 100,
    expectedPoints: 100,
    expectedCode: 0,
    essayMin: 0,
    essayMax: 0,
    expectedModules: { A: 0, B: 35, C: 65 }
  }
};


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
  const spec = EXAM_SPECS[exam.id];
  assert(Boolean(spec), `${displayFile}: unknown exam id '${exam.id}' without specification`);
  if (!spec) return { graded: 0, essays: 0 };

  assert(typeof exam.title === 'string' && exam.title.length > 0, `${displayFile}: missing title`);
  assert(typeof exam.description === 'string' && exam.description.trim().length > 0, `${displayFile}: missing description`);
  assert(typeof exam.durationMinutes === 'number' && exam.durationMinutes > 0, `${displayFile}: durationMinutes invalid`);
  assert(Math.abs(exam.totalPoints - spec.expectedPoints) < 0.001, `${displayFile}: totalPoints must be ${spec.expectedPoints}, found ${exam.totalPoints}`);
  assert(typeof exam.disclaimer === 'string' && exam.disclaimer.trim().length > 0, `${displayFile}: missing disclaimer`);
  assert(Array.isArray(exam.questions), `${displayFile}: questions must be an array`);
  if (!Array.isArray(exam.questions)) return { graded: 0, essays: 0 };

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
  const promptKeys = new Set();
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

    const pKey = String(q.prompt ?? '').replace(/\s+/g, ' ').trim().toLowerCase();
    const isOfficialDuplicateAllowed = (exam.id === 'voai-2025' && q.id === 'VOAI25-062');
    assert(isOfficialDuplicateAllowed || !promptKeys.has(pKey), `${loc}: duplicate prompt within exam: ${q.id}`);
    promptKeys.add(pKey);

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
      assert(!/<(?:div|span|table|tr|td)\b[^>]*>/i.test(q.explanation), `${loc}: explanation contains raw HTML tags`);
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
      assert(typeof q.modelAnswer === 'string' && q.modelAnswer.trim().length >= 12, `${loc}: essay needs modelAnswer`);
      assert(Array.isArray(q.rubric) && q.rubric.length >= 3, `${loc}: essay needs >= 3 rubric items`);
      essays.push(q);
    }
  }

  assert(gradedTotal === spec.gradedCount, `${displayFile}: expected ${spec.gradedCount} graded questions (mcq+code), found ${gradedTotal}`);
  assert(codeTotal === spec.expectedCode, `${displayFile}: expected ${spec.expectedCode} code questions, found ${codeTotal}`);
  assert(essays.length >= spec.essayMin && essays.length <= spec.essayMax, `${displayFile}: expected ${spec.essayMin}-${spec.essayMax} essays, found ${essays.length}`);
  
  for (const [module, expected] of Object.entries(spec.expectedModules)) {
    assert(gradedCounts[module] === expected, `${displayFile}: graded module ${module} expected ${expected}, found ${gradedCounts[module]}`);
  }
  assert(Math.abs(gradedPoints - spec.expectedPoints) < 0.001, `${displayFile}: graded points must sum to ${spec.expectedPoints}, found ${gradedPoints}`);

  const maxAllowed = Math.ceil(spec.gradedCount * 0.45);
  const minAllowed = Math.floor(spec.gradedCount * 0.08);
  for (const [key, count] of Object.entries(answerDist)) {
    assert(count <= maxAllowed, `${displayFile}: answer ${key} appears ${count} times (>${maxAllowed}, dap an lech)`);
    assert(count >= minAllowed, `${displayFile}: answer ${key} appears only ${count} times (<${minAllowed}, dap an lech)`);
  }
  console.log(`PASS ${displayFile}: ${gradedTotal} graded (${gradedPoints}đ) + ${essays.length} essays. Answers: A=${answerDist.A}, B=${answerDist.B}, C=${answerDist.C}, D=${answerDist.D}`);
  return { graded: gradedTotal, essays: essays.length };
}

const files = fs.existsSync(EXAMS_DIR)
  ? fs.readdirSync(EXAMS_DIR).filter((f) => f.endsWith('.json')).sort()
  : [];
assert(files.length >= 3, 'cần ít nhất 3 đề trong src/data/exams');

const examIds = new Set();
let gradedSum = 0;
let essaySum = 0;

for (const file of files) {
  const displayFile = `exams/${file}`;
  const exam = readJson(path.join(EXAMS_DIR, file));
  if (!exam) continue;
  assert(!examIds.has(exam.id), `${displayFile}: duplicate exam id ${exam.id}`);
  examIds.add(exam.id);
  const { graded, essays } = validateExam(exam, displayFile);
  gradedSum += graded;
  essaySum += essays;
}

if (process.exitCode) {
  console.error('\nValidation failed. Fix the errors above.');
  process.exit(process.exitCode);
}
console.log(`\nAll ${files.length} exams valid! Graded questions: ${gradedSum}. Essays: ${essaySum}. Total: ${gradedSum + essaySum}.`);
