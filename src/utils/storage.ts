import type { AnswerState } from '../types/exam';

export const DATA_VERSION: Record<string, string> = {
  'olp-01': '1.0',
  'olp-02': '2.0',
  'olp-03': '2.0'
};

class MemoryStorage {
  private data = new Map<string, string>();
  getItem(k: string) { return this.data.get(k) ?? null; }
  setItem(k: string, v: string) { this.data.set(k, String(v)); }
  removeItem(k: string) { this.data.delete(k); }
  clear() { this.data.clear(); }
}
const fallbackStorage = new MemoryStorage();

export const getStorage = (): Storage => {
  try {
    if (typeof window !== 'undefined' && window.localStorage && typeof window.localStorage.getItem === 'function') {
      return window.localStorage;
    }
    if (typeof localStorage !== 'undefined' && typeof localStorage.getItem === 'function') {
      return localStorage;
    }
  } catch {
    // ignore
  }
  return fallbackStorage as unknown as Storage;
};

const key = (examId: string) => `ai-test-progress:${examId}`;

export function saveProgress(examId: string, answers: Record<string, AnswerState>) {
  const version = DATA_VERSION[examId] || '1.0';
  const s = getStorage();
  if (s) {
    s.setItem(key(examId), JSON.stringify({ answers, savedAt: new Date().toISOString(), version }));
  }
}

export function loadProgress(examId: string): Record<string, AnswerState> {
  const s = getStorage();
  if (!s) return {};
  const raw = s.getItem(key(examId));
  if (!raw) return {};
  try {
    const parsed = JSON.parse(raw);
    const expectedVersion = DATA_VERSION[examId] || '1.0';
    if (parsed.version && parsed.version !== expectedVersion) {
      clearProgress(examId);
      return {};
    }
    // Nếu là đề đã đảo options (v2.0) mà bản lưu không có trường version, invalidate riêng đề này
    if (!parsed.version && expectedVersion !== '1.0') {
      clearProgress(examId);
      return {};
    }
    return parsed.answers ?? {};
  } catch {
    return {};
  }
}

export function clearProgress(examId: string) {
  const s = getStorage();
  if (s) {
    s.removeItem(key(examId));
  }
}

export interface ExamResult {
  percent: number;
  correct: number;
  total: number;
  essayEarned: number;
  essayTotal: number;
  at: string;
  version?: string;
}

const resultsKey = 'olp-ai-results';
const modeKey = 'olp-ai-mode';

export function saveResult(examId: string, result: ExamResult) {
  try {
    const all = loadResults();
    result.version = DATA_VERSION[examId] || '1.0';
    all[examId] = result;
    const s = getStorage();
    if (s) s.setItem(resultsKey, JSON.stringify(all));
  } catch {
    // Bỏ qua khi localStorage đầy/không dùng được.
  }
}

export function loadResults(): Record<string, ExamResult> {
  try {
    const s = getStorage();
    if (!s) return {};
    const raw = s.getItem(resultsKey);
    if (!raw) return {};
    const parsed = JSON.parse(raw) as Record<string, ExamResult>;
    let changed = false;
    for (const [id, res] of Object.entries(parsed)) {
      const expectedVersion = DATA_VERSION[id] || '1.0';
      if (expectedVersion !== '1.0' && res.version !== expectedVersion) {
        delete parsed[id];
        changed = true;
      }
    }
    if (changed && s) {
      s.setItem(resultsKey, JSON.stringify(parsed));
    }
    return parsed;
  } catch {
    return {};
  }
}

export function loadMode(): 'practice' | 'exam' {
  const s = getStorage();
  return s?.getItem(modeKey) === 'exam' ? 'exam' : 'practice';
}

export function saveMode(mode: 'practice' | 'exam') {
  const s = getStorage();
  if (s) s.setItem(modeKey, mode);
}
