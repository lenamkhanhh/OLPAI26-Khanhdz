import type { AnswerState } from '../types/exam';

const key = (examId: string) => `ai-test-progress:${examId}`;

export function saveProgress(examId: string, answers: Record<string, AnswerState>) {
  localStorage.setItem(key(examId), JSON.stringify({ answers, savedAt: new Date().toISOString() }));
}

export function loadProgress(examId: string): Record<string, AnswerState> {
  const raw = localStorage.getItem(key(examId));
  if (!raw) return {};
  try {
    const parsed = JSON.parse(raw);
    return parsed.answers ?? {};
  } catch {
    return {};
  }
}

export function clearProgress(examId: string) {
  localStorage.removeItem(key(examId));
}

export interface ExamResult {
  percent: number;
  correct: number;
  total: number;
  essayEarned: number;
  essayTotal: number;
  at: string;
}

const resultsKey = 'olp-ai-results';
const modeKey = 'olp-ai-mode';

export function saveResult(examId: string, result: ExamResult) {
  try {
    const all = loadResults();
    all[examId] = result;
    localStorage.setItem(resultsKey, JSON.stringify(all));
  } catch {
    // Bỏ qua khi localStorage đầy/không dùng được.
  }
}

export function loadResults(): Record<string, ExamResult> {
  try {
    const raw = localStorage.getItem(resultsKey);
    return raw ? (JSON.parse(raw) as Record<string, ExamResult>) : {};
  } catch {
    return {};
  }
}

export function loadMode(): 'practice' | 'exam' {
  return localStorage.getItem(modeKey) === 'exam' ? 'exam' : 'practice';
}

export function saveMode(mode: 'practice' | 'exam') {
  localStorage.setItem(modeKey, mode);
}
