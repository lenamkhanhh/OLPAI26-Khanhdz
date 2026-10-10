// @vitest-environment jsdom
import { describe, it, expect, beforeEach } from 'vitest';
import { summarizeExam, isQuestionCorrect, scoreQuestion } from './scoring';
import { loadProgress, saveProgress, clearProgress, getStorage, DATA_VERSION } from './storage';
import type { AnswerState, Exam } from '../types/exam';

import olp01Raw from '../data/exams/olp-01.json';
import olp02Raw from '../data/exams/olp-02.json';
import olp03Raw from '../data/exams/olp-03.json';

const olp01 = olp01Raw as unknown as Exam;
const olp02 = olp02Raw as unknown as Exam;
const olp03 = olp03Raw as unknown as Exam;

describe('Audit Scoring Regressions', () => {
  it('OLP-01: 100 MCQ correct gives 100/100 (100%), totalPoints = 100', () => {
    const mcqAnswers: Record<string, AnswerState> = {};
    for (const q of olp01.questions) {
      if (q.type === 'mcq') {
        mcqAnswers[q.id] = { selected: q.answer };
      }
    }
    const summaryMcq = summarizeExam(olp01, mcqAnswers);
    expect(summaryMcq.earned).toBe(100);
    expect(summaryMcq.total).toBe(100);
    expect(summaryMcq.percent).toBe(100);
    expect(summaryMcq.correct).toBe(100);
  });

  it('OLP-02: 100 MCQ correct gives 100/100 (100%), no undefined earned error', () => {
    const answers: Record<string, AnswerState> = {};
    for (const q of olp02.questions) {
      if (q.type === 'mcq') {
        answers[q.id] = { selected: q.answer };
      }
    }
    const summary = summarizeExam(olp02, answers);
    expect(summary.earned).toBe(100);
    expect(summary.total).toBe(100);
    expect(summary.percent).toBe(100);
    expect(summary.correct).toBe(100);
    // Module scores must exist and have no undefined
    expect(summary.moduleScores.length).toBe(3);
    for (const ms of summary.moduleScores) {
      expect(typeof ms.earned).toBe('number');
      expect(typeof ms.total).toBe('number');
    }
  });

  it('OLP-03: 100 MCQ correct gives 100/100 (100%), totalPoints exists', () => {
    const answers: Record<string, AnswerState> = {};
    for (const q of olp03.questions) {
      if (q.type === 'mcq') {
        answers[q.id] = { selected: q.answer };
      }
    }
    const summary = summarizeExam(olp03, answers);
    expect(summary.earned).toBe(100);
    expect(summary.total).toBe(100);
    expect(summary.percent).toBe(100);
    expect(summary.correct).toBe(100);
  });

  it('Essay questions do not alter graded denominator across all exams', () => {
    for (const exam of [olp01, olp02, olp03]) {
      const summaryEmpty = summarizeExam(exam, {});
      expect(summaryEmpty.total).toBe(exam.totalPoints);
      expect(summaryEmpty.percent).toBe(0);
      expect(summaryEmpty.earned).toBe(0);
    }
  });
});

describe('Storage Version Invalidation', () => {
  beforeEach(() => {
    getStorage().clear();
  });

  it('Invalidates progress of reshuffled exam if version is old or missing', () => {
    // Lưu dữ liệu giả lập từ phiên bản cũ không có version field
    getStorage().setItem('ai-test-progress:olp-02', JSON.stringify({ answers: { 'VOAI02-M01': { selected: 'B' } } }));
    
    // Khi load, do olp-02 yêu cầu version 2.0, dữ liệu cũ phải bị xóa và trả về {}
    const loaded = loadProgress('olp-02');
    expect(loaded).toEqual({});

    // Nhưng olp-01 yêu cầu version 1.0 (không đổi), nếu lưu version 1.0 sẽ load được
    saveProgress('olp-01', { 'OLP01-A01': { selected: 'B' } });
    const loaded01 = loadProgress('olp-01');
    expect(loaded01['OLP01-A01']?.selected).toBe('B');
  });
});
