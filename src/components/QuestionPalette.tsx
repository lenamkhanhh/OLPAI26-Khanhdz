import type { Question } from '../types/exam';

export type PaletteStatus = 'todo' | 'done' | 'current';

interface Props {
  questions: Question[];
  answeredIds: Set<string>;
  current: number;
  open: boolean;
  onClose: () => void;
  onJump: (index: number) => void;
}

// Bottom sheet lưới số câu: xám = chưa làm, xanh = đã làm, viền đậm = đang làm.
export function QuestionPalette({ questions, answeredIds, current, open, onClose, onJump }: Props) {
  if (!open) return null;
  return (
    <div className="palette-backdrop" role="presentation" onMouseDown={(e) => { if (e.target === e.currentTarget) onClose(); }}>
      <section className="palette-sheet" role="dialog" aria-modal="true" aria-label="Danh sách câu hỏi">
        <header className="palette-head">
          <strong>Danh sách câu hỏi</strong>
          <button type="button" className="palette-close" aria-label="Đóng danh sách" onClick={onClose}>×</button>
        </header>
        <div className="palette-legend">
          <span><i className="dot dot--todo" /> Chưa làm</span>
          <span><i className="dot dot--done" /> Đã làm</span>
          <span><i className="dot dot--current" /> Đang làm</span>
        </div>
        <div className="palette-grid">
          {questions.map((q, idx) => {
            const done = answeredIds.has(q.id);
            const cls = idx === current ? 'palette-cell palette-cell--current' : done ? 'palette-cell palette-cell--done' : 'palette-cell';
            return (
              <button
                key={q.id}
                type="button"
                className={cls}
                aria-label={`Câu ${idx + 1}${done ? ' đã làm' : ' chưa làm'}`}
                onClick={() => { onJump(idx); onClose(); }}
              >
                {idx + 1}
              </button>
            );
          })}
        </div>
      </section>
    </div>
  );
}
