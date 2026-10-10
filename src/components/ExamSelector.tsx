import type { Exam, QuizMode } from '../types/exam';
import { loadProgress, loadResults, loadMode, saveMode } from '../utils/storage';
import { isQuestionAnswered } from './QuizRunner';
import { Disclaimer } from './Disclaimer';

interface Props {
  exams: Exam[];
  selectedExamId: string;
  mode: QuizMode;
  timerEnabled: boolean;
  onExamChange: (id: string) => void;
  onModeChange: (mode: QuizMode) => void;
  onTimerChange: (enabled: boolean) => void;
  onStart: () => void;
  onOpenHandbook?: () => void;
}

// Màn chọn đề kiểu app thi lái xe: segmented mode + card từng đề + CTA sticky.
export function ExamSelector({
  exams,
  selectedExamId,
  mode,
  timerEnabled,
  onExamChange,
  onModeChange,
  onTimerChange,
  onStart,
  onOpenHandbook
}: Props) {
  const selected = exams.find((exam) => exam.id === selectedExamId) ?? exams[0];
  const results = loadResults();
  const initialMode = loadMode();
  const activeMode = mode ?? initialMode;

  const pickMode = (m: QuizMode) => {
    saveMode(m);
    onModeChange(m);
  };

  return (
    <main className="deck page-shell">
      <header className="deck-head">
        <span className="eyebrow">OLP AI HCMUS 2026 · vòng loại cấp trường</span>
        <h1>Ôn thi Olympic AI</h1>
      </header>

      <div className="deck-handbook-banner" style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '14px' }}>
        {onOpenHandbook && (
          <button type="button" className="secondary deck-handbook-btn" style={{ flex: 1, minWidth: '220px' }} onClick={onOpenHandbook}>
            📚 Sổ tay Lý thuyết & Video Bài giảng →
          </button>
        )}
        <a
          href="/olympic_ai_study_hub.html"
          className="secondary deck-handbook-btn"
          style={{
            flex: 1,
            minWidth: '220px',
            textDecoration: 'none',
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            background: 'linear-gradient(135deg, rgba(37,99,235,0.2), rgba(30,58,138,0.3))',
            borderColor: '#3b82f6',
            color: '#93c5fd',
            fontWeight: 600
          }}
        >
          ⚡ Olympic AI Study Hub (Giao diện 3 Cột E2E) →
        </a>
      </div>

      <div className="segmented" role="tablist" aria-label="Chế độ làm bài">
        {(['practice', 'exam'] as QuizMode[]).map((m) => (
          <button
            key={m}
            type="button"
            role="tab"
            aria-selected={activeMode === m}
            className={activeMode === m ? 'segmented__btn segmented__btn--active' : 'segmented__btn'}
            onClick={() => pickMode(m)}
          >
            {m === 'practice' ? 'Practice' : 'Exam'}
          </button>
        ))}
      </div>
      <p className="segmented-hint">
        {activeMode === 'practice' ? 'Chọn đáp án hiện đúng/sai + giải thích ngay.' : 'Làm xong mới chấm, giống thi thật.'}
      </p>

      <div className="deck-list">
        {exams.map((exam) => {
          const progress = loadProgress(exam.id);
          const done = exam.questions.filter((q) => isQuestionAnswered(q, progress[q.id])).length;
          const pct = Math.round((done / exam.questions.length) * 100);
          const last = results[exam.id];
          const active = exam.id === selected.id;
          return (
            <button
              key={exam.id}
              type="button"
              className={active ? 'deck-card deck-card--active' : 'deck-card'}
              onClick={() => onExamChange(exam.id)}
              aria-pressed={active}
            >
              <span className="deck-card__main">
                <strong>{exam.title}</strong>
                <span>{exam.questions.length} câu · {exam.durationMinutes} phút</span>
              </span>
              <span className="deck-card__meta">
                {done > 0 && <span className="deck-progress"><span style={{ width: `${pct}%` }} /></span>}
                <span className="deck-stats">
                  {done > 0 ? `${pct}%` : 'Chưa làm'}
                  {last ? ` · Gần nhất ${last.percent}%` : ''}
                </span>
              </span>
            </button>
          );
        })}
      </div>

      <label className="checkbox-row deck-timer">
        <input type="checkbox" checked={timerEnabled} onChange={(e) => onTimerChange(e.target.checked)} />
        Bật timer {selected.durationMinutes} phút
      </label>

      <div className="deck-cta">
        <button type="button" className="primary deck-start" onClick={onStart}>▶ BẮT ĐẦU — {selected.title}</button>
      </div>

      <Disclaimer text={selected.disclaimer} />
    </main>
  );
}
