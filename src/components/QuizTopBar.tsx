import { useEffect, useRef, useState } from 'react';

interface Props {
  title: string;
  index: number;
  total: number;
  timerEnabled: boolean;
  durationMinutes: number;
  onTimeUp: () => void;
  onHome: () => void;
  onOpenPalette: () => void;
  onToggleTheory?: () => void;
  theoryOpen?: boolean;
  currentSection?: string;
}

// Sticky top bar: thoát · Câu n/N · Sổ tay lý thuyết · timer · palette.
export function QuizTopBar({
  title,
  index,
  total,
  timerEnabled,
  durationMinutes,
  onTimeUp,
  onHome,
  onOpenPalette,
  onToggleTheory,
  theoryOpen,
  currentSection
}: Props) {
  const [label, setLabel] = useState('');
  const deadlineRef = useRef(0);
  const lastSecondRef = useRef(-1);
  const timeUpRef = useRef(onTimeUp);
  timeUpRef.current = onTimeUp;

  useEffect(() => {
    if (!timerEnabled) return;
    deadlineRef.current = Date.now() + durationMinutes * 60 * 1000;
    lastSecondRef.current = -1;
    let raf = 0;
    const tick = () => {
      const left = Math.max(0, Math.round((deadlineRef.current - Date.now()) / 1000));
      if (left !== lastSecondRef.current) {
        lastSecondRef.current = left;
        const mm = Math.floor(left / 60).toString().padStart(2, '0');
        const ss = (left % 60).toString().padStart(2, '0');
        setLabel(`${mm}:${ss}`);
        if (left === 0) {
          timeUpRef.current();
          return;
        }
      }
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [timerEnabled, durationMinutes]);

  const urgent = timerEnabled && label !== '' && label <= '05:00';

  return (
    <header className="quiz-topbar">
      <button type="button" className="topbar-btn" aria-label="Về trang chọn đề" onClick={onHome}>←</button>
      <div className="topbar-center">
        <strong>Câu {index + 1}/{total}</strong>
        <span className="topbar-title">{title}</span>
      </div>

      <div className="topbar-right-controls">
        {onToggleTheory && (
          <button
            type="button"
            className={`topbar-btn topbar-theory-toggle${theoryOpen ? ' topbar-theory-toggle--active' : ''}`}
            aria-label="Mở sổ tay lý thuyết"
            onClick={onToggleTheory}
            title="Mở thanh lý thuyết & video bên cạnh"
          >
            📖 <span className="topbar-theory-text">{currentSection ? `${currentSection}` : 'Lý thuyết'}</span>
          </button>
        )}

        {timerEnabled && <span className={`topbar-timer${urgent ? ' topbar-timer--urgent' : ''}`} role="timer">⏱ {label || '--:--'}</span>}
        <button type="button" className="topbar-btn" aria-label="Mở danh sách câu hỏi" onClick={onOpenPalette}>▦</button>
      </div>
    </header>
  );
}
