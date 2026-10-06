import type { ChangeEvent } from 'react';
import type { Exam, QuizMode } from '../types/exam';
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
}

const ABC_OVERVIEW = [
  'A: 12 câu Toán & Xác suất – Thống kê',
  'B: 18 câu Python/NumPy/Tính tay, gồm 2 câu code',
  'C: 30 câu ML/DL/CV/NLP + 4 câu tự luận giải pháp AI (chấm riêng)'
];

export function ExamSelector({
  exams,
  selectedExamId,
  mode,
  timerEnabled,
  onExamChange,
  onModeChange,
  onTimerChange,
  onStart
}: Props) {
  const selected = exams.find((exam) => exam.id === selectedExamId) ?? exams[0];
  const overview = selected.moduleOverview ?? ABC_OVERVIEW;

  return (
    <main className="home page-shell">
      <section className="hero card">
        <span className="eyebrow">OLP AI HCMUS 2026 · vòng loại cấp trường</span>
        <h1>Ôn thi Olympic AI HCMUS 2026</h1>
        <p>
          Web thi thử với {exams.length} đề. Mỗi đề 60 câu trắc nghiệm/code (thang 100 điểm)
          + 4 câu tự luận giải pháp AI chấm riêng theo rubric.
        </p>
        <Disclaimer text={selected.disclaimer} />
      </section>

      <section className="setup card">
        <label>
          <span>Chọn đề</span>
          <select value={selectedExamId} onChange={(event: ChangeEvent<HTMLSelectElement>) => onExamChange(event.target.value)}>
            {exams.map((exam) => <option key={exam.id} value={exam.id}>{exam.title}</option>)}
          </select>
        </label>

        <div className="mode-grid">
          <button className={mode === 'practice' ? 'active mode-card' : 'mode-card'} onClick={() => onModeChange('practice')}>
            Practice mode
            <span>Chọn xong hiện đúng/sai, đáp án và giải thích.</span>
          </button>
          <button className={mode === 'exam' ? 'active mode-card' : 'mode-card'} onClick={() => onModeChange('exam')}>
            Exam mode
            <span>Làm xong mới hiện đáp án, giống tự bấm giờ.</span>
          </button>
        </div>

        <label className="checkbox-row">
          <input type="checkbox" checked={timerEnabled} onChange={(event: ChangeEvent<HTMLInputElement>) => onTimerChange(event.target.checked)} />
          Bật timer {selected.durationMinutes} phút
        </label>

        <div className="overview">
          <strong>{selected.title}</strong>
          <span>{selected.description}</span>
          <ul>
            {overview.map((item) => <li key={item}>{item}</li>)}
          </ul>
        </div>

        <button className="primary" onClick={onStart}>Bắt đầu làm bài</button>
      </section>
    </main>
  );
}
