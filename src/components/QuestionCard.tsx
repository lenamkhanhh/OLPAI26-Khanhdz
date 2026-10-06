import { memo, useEffect, useState } from 'react';
import type { AnswerState, Question } from '../types/exam';
import { MathText } from './MathText';
import { AnswerOption, type OptionState } from './AnswerOption';

interface Props {
  question: Question;
  index: number;
  total: number;
  answer?: AnswerState;
  mode: 'practice' | 'exam';
  submitted: boolean;
  hasNext: boolean;
  onAnswer: (answer: AnswerState) => void;
  onNext: () => void;
}

const TYPE_LABEL: Record<Question['type'], string> = {
  mcq: 'Trắc nghiệm',
  code: 'Code tay',
  essay: 'Tự luận giải pháp'
};

export const QuestionCard = memo(function QuestionCard({
  question, index, total, answer, mode, submitted, hasNext, onAnswer, onNext
}: Props) {
  const [showHint, setShowHint] = useState(false);
  const [showModelAnswer, setShowModelAnswer] = useState(false);
  const isMcq = question.type === 'mcq';
  const openQuestion = isMcq ? null : question;
  const revealMcq = submitted || (mode === 'practice' && Boolean(answer?.selected));
  const canUseOpenHelp = !isMcq && (mode === 'practice' || submitted);
  const checks = answer?.rubricChecks ?? [];

  useEffect(() => {
    setShowHint(false);
    setShowModelAnswer(false);
  }, [question.id]);

  const optionState = (key: string): OptionState => {
    if (question.type !== 'mcq') return 'idle';
    const selected = answer?.selected === key;
    if (revealMcq) {
      if (key === question.answer) return 'correct';
      if (selected) return 'wrong';
      return 'dimmed';
    }
    return selected ? 'selected' : 'idle';
  };

  return (
    <article className="question-card card">
      <header className="question-header">
        <div>
          <span className="module-tag">Module {question.module}</span>
          <h2>{TYPE_LABEL[question.type]}</h2>
        </div>
        <strong>{question.points} điểm</strong>
      </header>

      <div className="question-stem"><MathText text={question.prompt} /></div>

      {isMcq ? (
        <div className="options">
          {question.options.map((option) => (
            <AnswerOption
              key={option.key}
              optionKey={option.key}
              text={option.text}
              state={optionState(option.key)}
              onSelect={() => {
                // Tap lại đáp án đang chọn để bỏ chọn.
                const next = answer?.selected === option.key ? undefined : option.key;
                onAnswer({ ...answer, selected: next });
              }}
            />
          ))}
        </div>
      ) : (
        <div className="open-answer">
          <textarea
            placeholder={question.type === 'code' ? 'Gõ code/pseudo-code của bạn...' : 'Trình bày giải pháp theo khung 5 bước...'}
            value={answer?.text ?? ''}
            onChange={(event) => onAnswer({ ...answer, text: event.target.value })}
          />

          {canUseOpenHelp ? (
            <div className="open-answer-tools">
              <button type="button" className="secondary" aria-expanded={showHint} onClick={() => setShowHint((v) => !v)}>
                {showHint ? 'Ẩn gợi ý' : 'Gợi ý'}
              </button>
              <button type="button" className="secondary" aria-expanded={showModelAnswer} onClick={() => setShowModelAnswer((v) => !v)}>
                {showModelAnswer ? 'Ẩn đáp án mẫu' : 'Xem đáp án mẫu'}
              </button>
            </div>
          ) : (
            <p className="open-help-note">Gợi ý và đáp án mẫu được ẩn trong Exam mode.</p>
          )}
        </div>
      )}

      {revealMcq && isMcq && answer?.selected && (
        <section className={`feedback${answer.selected === question.answer ? ' feedback--ok' : ' feedback--bad'}`}>
          <strong>{answer.selected === question.answer ? '✓ Đúng.' : `✗ Sai. Đáp án đúng là ${question.answer}.`}</strong>
          <div className="feedback-body"><MathText text={question.explanation} /></div>
          {mode === 'practice' && hasNext && (
            <button type="button" className="primary feedback-next" onClick={onNext}>Câu tiếp →</button>
          )}
        </section>
      )}

      {canUseOpenHelp && showHint && openQuestion && (
        <section className="feedback hint-panel">
          <strong>Gợi ý — checklist rubric (tick từng ý đã làm được)</strong>
          <ul className="rubric-checklist">
            {openQuestion.rubric.map((item, i) => (
              <li key={item}>
                <label>
                  <input
                    type="checkbox"
                    checked={Boolean(checks[i])}
                    onChange={(e) => {
                      const next = [...checks];
                      next[i] = e.target.checked;
                      onAnswer({ ...answer, rubricChecks: next });
                    }}
                  />
                  <MathText text={item} />
                </label>
              </li>
            ))}
          </ul>
        </section>
      )}

      {canUseOpenHelp && showModelAnswer && openQuestion && (
        <section className="feedback model-answer-panel">
          <strong>Đáp án mẫu</strong>
          <div className="model-answer-body"><MathText text={openQuestion.modelAnswer} /></div>
          <div className="essay-score">
            <label htmlFor={`essay-score-${question.id}`}>
              Tự chấm: <strong>{answer?.essayScore ?? 0}/{openQuestion.points} điểm</strong> (kéo theo số ý rubric làm được)
            </label>
            <input
              id={`essay-score-${question.id}`}
              type="range"
              min={0}
              max={openQuestion.points}
              step={1}
              value={answer?.essayScore ?? 0}
              onChange={(e) => onAnswer({ ...answer, essayScore: Number(e.target.value) })}
            />
          </div>
        </section>
      )}
    </article>
  );
});
