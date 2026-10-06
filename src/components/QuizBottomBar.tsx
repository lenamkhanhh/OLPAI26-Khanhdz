interface Props {
  hasPrev: boolean;
  hasNext: boolean;
  answeredCount: number;
  total: number;
  onPrev: () => void;
  onNext: () => void;
  onSubmit: () => void;
}

// Sticky bottom bar: Trước / Sau / Nộp bài (hiện số câu đã làm).
export function QuizBottomBar({ hasPrev, hasNext, answeredCount, total, onPrev, onNext, onSubmit }: Props) {
  return (
    <footer className="quiz-bottombar">
      <div className="bottombar-nav">
        <button type="button" className="secondary" disabled={!hasPrev} onClick={onPrev}>← Trước</button>
        <button type="button" className="secondary" disabled={!hasNext} onClick={onNext}>Sau →</button>
      </div>
      <button type="button" className="primary bottombar-submit" onClick={onSubmit}>
        NỘP BÀI ({answeredCount}/{total})
      </button>
    </footer>
  );
}
