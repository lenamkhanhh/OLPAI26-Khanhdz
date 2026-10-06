import type { AnswerState, Exam } from '../types/exam';
import { summarizeExam, isQuestionCorrect } from '../utils/scoring';
import { isQuestionAnswered } from './QuizRunner';
import { MathText } from './MathText';
import { ModuleStats } from './ModuleStats';
import { Disclaimer } from './Disclaimer';

interface Props {
  exam: Exam;
  answers: Record<string, AnswerState>;
  onReview: (questionIndex: number) => void;
  onRestart: () => void;
  onHome: () => void;
}

const PASS_PERCENT = 70;

type CellStatus = 'right' | 'wrong' | 'todo';

function cellStatus(exam: Exam, answers: Record<string, AnswerState>, index: number): CellStatus {
  const q = exam.questions[index];
  const a = answers[q.id];
  if (!isQuestionAnswered(q, a)) return 'todo';
  return isQuestionCorrect(q, a) ? 'right' : 'wrong';
}

// Màn kết quả kiểu thi lái xe: ĐẠT/KHÔNG ĐẠT cỡ lớn + lưới review xanh/đỏ/vàng.
export function ResultSummary({ exam, answers, onReview, onRestart, onHome }: Props) {
  const summary = summarizeExam(exam, answers);
  const pass = summary.percent >= PASS_PERCENT;
  const firstWrong = exam.questions.findIndex((_, i) => cellStatus(exam, answers, i) === 'wrong');

  return (
    <main className="result page-shell">
      <section className="result-hero card">
        <div className={`result-badge ${pass ? 'result-badge--pass' : 'result-badge--fail'}`}>
          {pass ? '✓' : '✗'}
        </div>
        <div>
          <span className="eyebrow">Kết quả · {exam.title}</span>
          <h1>{pass ? 'ĐẠT' : 'CHƯA ĐẠT'}</h1>
          <p>
            Trắc nghiệm: {summary.earned.toFixed(1)}/{summary.total} điểm · đúng {summary.correct}/{summary.totalQuestions} câu ({summary.percent}%)
          </p>
          <p>Tự luận (chấm riêng): {summary.essayEarned.toFixed(1)}/{summary.essayTotal} điểm · đạt {summary.essayPass}/{summary.essayCount} câu</p>
          <Disclaimer text={exam.disclaimer} />
        </div>
      </section>

      <ModuleStats scores={summary.moduleScores} labels={exam.moduleLabels} />

      <section className="card review-panel">
        <h2>Xem lại từng câu</h2>
        <div className="palette-legend">
          <span><i className="dot dot--done" /> Đúng</span>
          <span><i className="dot dot--wrong" /> Sai</span>
          <span><i className="dot dot--todo" /> Chưa làm</span>
        </div>
        <div className="review-grid">
          {exam.questions.map((q, idx) => {
            const st = cellStatus(exam, answers, idx);
            return (
              <button
                key={q.id}
                type="button"
                className={`review-cell review-cell--${st}`}
                aria-label={`Xem lại câu ${idx + 1}`}
                onClick={() => onReview(idx)}
              >
                {idx + 1}
              </button>
            );
          })}
        </div>
        {summary.review.length > 0 && (
          <div className="review-wrong">
            <h3>Câu cần ôn ({summary.review.length})</h3>
            <ul>
              {summary.review.map((q) => {
                const idx = exam.questions.findIndex((item) => item.id === q.id);
                return (
                  <li key={q.id}>
                    <button type="button" className="link" onClick={() => onReview(idx)}>
                      Câu {idx + 1} · Module {q.module} · {q.type === 'mcq' ? 'trắc nghiệm' : q.type === 'code' ? 'code' : 'tự luận'}
                    </button>
                    <span className="review-wrong__stem"><MathText text={q.prompt.slice(0, 120) + (q.prompt.length > 120 ? '…' : '')} /></span>
                  </li>
                );
              })}
            </ul>
          </div>
        )}
      </section>

      <div className="actions result-actions">
        {firstWrong >= 0 && (
          <button type="button" className="primary" onClick={() => onReview(firstWrong)}>↻ Ôn lại từ câu sai đầu tiên</button>
        )}
        <button type="button" className="secondary" onClick={onRestart}>Làm lại đề</button>
        <button type="button" className="secondary" onClick={onHome}>Trang chủ</button>
      </div>
    </main>
  );
}
