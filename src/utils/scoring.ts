import type { AnswerState, Exam, ModuleId, Question } from '../types/exam';

export interface ModuleScore {
  module: ModuleId;
  earned: number;
  total: number;
  correct: number;
  totalQuestions: number;
}

export function isQuestionCorrect(question: Question, answer?: AnswerState): boolean {
  if (!answer) return false;
  if (question.type === 'mcq') return answer.selected === question.answer;
  if (answer.essayScore !== undefined) return answer.essayScore >= question.points / 2;
  return answer.selfGrade === 'pass';
}

export function scoreQuestion(question: Question, answer?: AnswerState): number {
  if (!answer) return 0;
  if (question.type !== 'mcq' && answer.essayScore !== undefined) {
    return Math.max(0, Math.min(question.points, answer.essayScore));
  }
  return isQuestionCorrect(question, answer) ? question.points : 0;
}

export function summarizeExam(exam: Exam, answers: Record<string, AnswerState>) {
  const moduleScores: Record<ModuleId, ModuleScore> = {
    A: { module: 'A', earned: 0, total: 0, correct: 0, totalQuestions: 0 },
    B: { module: 'B', earned: 0, total: 0, correct: 0, totalQuestions: 0 },
    C: { module: 'C', earned: 0, total: 0, correct: 0, totalQuestions: 0 }
  };

  // Trắc nghiệm + code: tính vào thang 100 điểm.
  let earned = 0;
  let correct = 0;
  // Tự luận: chấm riêng, không cộng vào thang 100.
  let essayEarned = 0;
  let essayTotal = 0;
  let essayPass = 0;
  let essayCount = 0;
  const review: Question[] = [];

  for (const question of exam.questions) {
    const answer = answers[question.id];
    const ok = isQuestionCorrect(question, answer);
    if (question.type === 'essay') {
      essayCount += 1;
      essayTotal += question.points;
      const partial = scoreQuestion(question, answer);
      essayEarned += partial;
      if (ok) essayPass += 1;
      if (!ok) review.push(question);
      continue;
    }
    const qScore = ok ? question.points : 0;
    earned += qScore;
    if (ok) correct += 1;
    else review.push(question);

    const bucket = moduleScores[question.module];
    bucket.earned += qScore;
    bucket.total += question.points;
    bucket.totalQuestions += 1;
    if (ok) bucket.correct += 1;
  }

  const gradedTotal = exam.totalPoints;
  return {
    earned,
    total: gradedTotal,
    correct,
    totalQuestions: exam.questions.filter((q) => q.type !== 'essay').length,
    percent: gradedTotal > 0 ? Math.round((earned / gradedTotal) * 100) : 0,
    essayEarned,
    essayTotal,
    essayPass,
    essayCount,
    moduleScores: Object.values(moduleScores),
    review
  };
}
