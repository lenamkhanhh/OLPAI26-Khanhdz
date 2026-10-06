import { useCallback, useEffect, useMemo, useState } from 'react';
import type { AnswerState, Exam, Question, QuizMode } from '../types/exam';
import { saveProgress, loadProgress, clearProgress, saveResult } from '../utils/storage';
import { summarizeExam } from '../utils/scoring';
import { QuestionCard } from './QuestionCard';
import { QuestionPalette } from './QuestionPalette';
import { QuizTopBar } from './QuizTopBar';
import { QuizBottomBar } from './QuizBottomBar';
import { ResultSummary } from './ResultSummary';

interface Props {
  exam: Exam;
  mode: QuizMode;
  timerEnabled: boolean;
  onHome: () => void;
}

export function isQuestionAnswered(question: Question, answer?: AnswerState): boolean {
  if (!answer) return false;
  if (question.type === 'mcq') return Boolean(answer.selected);
  return Boolean(answer.text?.trim()) || answer.essayScore !== undefined;
}

export function QuizRunner({ exam, mode, timerEnabled, onHome }: Props) {
  const [answers, setAnswers] = useState<Record<string, AnswerState>>(() => loadProgress(exam.id));
  const [current, setCurrent] = useState(0);
  const [submitted, setSubmitted] = useState(false);
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [confirmSubmit, setConfirmSubmit] = useState(false);

  const currentQuestion = exam.questions[current];

  const answeredIds = useMemo(() => {
    const set = new Set<string>();
    for (const q of exam.questions) {
      if (isQuestionAnswered(q, answers[q.id])) set.add(q.id);
    }
    return set;
  }, [answers, exam.questions]);

  const unansweredCount = exam.questions.length - answeredIds.size;

  useEffect(() => {
    saveProgress(exam.id, answers);
  }, [answers, exam.id]);

  const doSubmit = useCallback(() => {
    setConfirmSubmit(false);
    setPaletteOpen(false);
    setSubmitted(true);
  }, []);

  // Lưu kết quả để màn chọn đề hiện tiến độ/điểm.
  useEffect(() => {
    if (!submitted) return;
    const s = summarizeExam(exam, answers);
    saveResult(exam.id, {
      percent: s.percent,
      correct: s.correct,
      total: s.totalQuestions,
      essayEarned: s.essayEarned,
      essayTotal: s.essayTotal,
      at: new Date().toISOString()
    });
  }, [submitted, exam, answers]);

  const goNext = useCallback(() => setCurrent((x) => Math.min(exam.questions.length - 1, x + 1)), [exam.questions.length]);
  const goPrev = useCallback(() => setCurrent((x) => Math.max(0, x - 1)), []);

  // Phím tắt desktop: 1-4 chọn đáp án, ←/→ chuyển câu, Enter mở nộp bài.
  useEffect(() => {
    if (submitted) return;
    const onKey = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement | null;
      if (target && (target.tagName === 'TEXTAREA' || target.tagName === 'INPUT')) return;
      if (e.key >= '1' && e.key <= '4' && currentQuestion.type === 'mcq') {
        const key = ['A', 'B', 'C', 'D'][Number(e.key) - 1];
        const prev = answers[currentQuestion.id];
        setAnswers((p) => ({ ...p, [currentQuestion.id]: { ...prev, selected: prev?.selected === key ? undefined : key } }));
      } else if (e.key === 'ArrowRight') {
        goNext();
      } else if (e.key === 'ArrowLeft') {
        goPrev();
      } else if (e.key === 'Enter') {
        setConfirmSubmit(true);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [submitted, currentQuestion, answers, goNext, goPrev]);

  const updateAnswer = (answer: AnswerState) => {
    setAnswers((prev) => ({ ...prev, [currentQuestion.id]: answer }));
  };

  if (submitted) {
    return (
      <ResultSummary
        exam={exam}
        answers={answers}
        onReview={(idx) => { setSubmitted(false); setCurrent(idx); }}
        onRestart={() => { clearProgress(exam.id); setAnswers({}); setCurrent(0); setSubmitted(false); }}
        onHome={onHome}
      />
    );
  }

  return (
    <div className="quiz-screen">
      <QuizTopBar
        title={exam.title}
        index={current}
        total={exam.questions.length}
        timerEnabled={timerEnabled}
        durationMinutes={exam.durationMinutes}
        onTimeUp={doSubmit}
        onHome={onHome}
        onOpenPalette={() => setPaletteOpen(true)}
      />

      <main className="quiz-body">
        <QuestionCard
          question={currentQuestion}
          index={current}
          total={exam.questions.length}
          answer={answers[currentQuestion.id]}
          mode={mode}
          submitted={false}
          hasNext={current < exam.questions.length - 1}
          onAnswer={updateAnswer}
          onNext={goNext}
        />
      </main>

      <QuizBottomBar
        hasPrev={current > 0}
        hasNext={current < exam.questions.length - 1}
        answeredCount={answeredIds.size}
        total={exam.questions.length}
        onPrev={goPrev}
        onNext={goNext}
        onSubmit={() => setConfirmSubmit(true)}
      />

      <QuestionPalette
        questions={exam.questions}
        answeredIds={answeredIds}
        current={current}
        open={paletteOpen}
        onClose={() => setPaletteOpen(false)}
        onJump={setCurrent}
      />

      {confirmSubmit && (
        <div className="palette-backdrop" role="presentation" onMouseDown={(e) => { if (e.target === e.currentTarget) setConfirmSubmit(false); }}>
          <section className="confirm-dialog card" role="dialog" aria-modal="true" aria-label="Xác nhận nộp bài">
            <h2>Nộp bài?</h2>
            <p>
              Đã làm {answeredIds.size}/{exam.questions.length} câu.
              {unansweredCount > 0 ? ` Còn ${unansweredCount} câu chưa làm.` : ' Đã làm hết, kiểm tra lại rồi nộp nhé.'}
            </p>
            <div className="confirm-actions">
              <button type="button" className="secondary" onClick={() => setConfirmSubmit(false)}>Tiếp tục làm</button>
              <button type="button" className="primary" onClick={doSubmit}>Nộp bài</button>
            </div>
          </section>
        </div>
      )}
    </div>
  );
}
