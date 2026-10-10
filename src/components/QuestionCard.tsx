import { memo, useEffect, useState } from 'react';
import type { AnswerState, Question } from '../types/exam';
import { MathText } from './MathText';
import { AnswerOption, type OptionState } from './AnswerOption';
import { extractSectionRef, getVideoForSection, type VideoResource } from '../data/videoData';
import { EssayStudio } from './EssayStudio';

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
  onOpenTheory?: (sectionId: string) => void;
  onOpenVideo?: (video: VideoResource) => void;
  onOpenAI?: () => void;
}

const TYPE_LABEL: Record<Question['type'], string> = {
  mcq: 'Trắc nghiệm',
  code: 'Code tay',
  essay: 'Tự luận giải pháp'
};

export const QuestionCard = memo(function QuestionCard({
  question, index, total, answer, mode, submitted, hasNext, onAnswer, onNext, onOpenTheory, onOpenVideo, onOpenAI
}: Props) {
  const [showHint, setShowHint] = useState(false);
  const [showModelAnswer, setShowModelAnswer] = useState(false);
  const isMcq = question.type === 'mcq';
  const openQuestion = isMcq ? null : question;
  const revealMcq = submitted || (mode === 'practice' && Boolean(answer?.selected));
  const canUseOpenHelp = !isMcq && (mode === 'practice' || submitted);
  const checks = answer?.rubricChecks ?? [];

  // Trich xuat ref ly thuyet (§x.y) va video tuong ung
  const sectionRef = extractSectionRef((isMcq ? question.explanation : question.modelAnswer) || '');
  const video = sectionRef ? getVideoForSection(sectionRef) : undefined;

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
        <div className="question-header__right">
          {sectionRef && onOpenTheory && (
            <button
              type="button"
              className="badge-theory-jump"
              onClick={() => onOpenTheory(sectionRef)}
              title="Nhảy tới mục lý thuyết trong sổ tay"
            >
              📖 {sectionRef}
            </button>
          )}
          {onOpenAI && (
            <button
              type="button"
              className="badge-ai-trigger"
              onClick={onOpenAI}
              title="Mở Trợ lý AI cho câu hỏi này"
            >
              ⚡ AI Trợ lý
            </button>
          )}
          <strong>{question.points} điểm</strong>
        </div>
      </header>

      <div className="question-stem"><MathText text={question.prompt} /></div>

      {question.image && (
        <div className="question-image" style={{ textAlign: 'center', margin: '16px 0' }}>
          <img
            src={question.image}
            alt="Question Diagram"
            style={{ maxWidth: '100%', maxHeight: '360px', borderRadius: '8px', border: '1px solid var(--border-subtle, #333)', background: '#fff', padding: '6px' }}
          />
        </div>
      )}

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
        <EssayStudio
          question={question}
          answer={answer}
          canUseOpenHelp={canUseOpenHelp}
          showHint={showHint}
          showModelAnswer={showModelAnswer}
          onToggleHint={() => setShowHint((v) => !v)}
          onToggleModelAnswer={() => setShowModelAnswer((v) => !v)}
          onAnswer={onAnswer}
          onOpenAI={onOpenAI}
          sectionRef={sectionRef}
          onOpenTheory={onOpenTheory}
          videoButton={
            video && onOpenVideo ? (
              <button
                type="button"
                className="secondary btn-video-quick"
                onClick={() => onOpenVideo(video)}
              >
                🎬 Video giảng ({video.timestampLabel})
              </button>
            ) : null
          }
        />
      )}

      {revealMcq && isMcq && answer?.selected && (
        <section className={`feedback${answer.selected === question.answer ? ' feedback--ok' : ' feedback--bad'}`}>
          <strong>{answer.selected === question.answer ? '✓ Đúng.' : `✗ Sai. Đáp án đúng là ${question.answer}.`}</strong>
          <div className="feedback-body"><MathText text={question.explanation} /></div>

          {/* Thanh cong cu ho tro hoc tap khi giai thich hien ra */}
          <div className="feedback-learning-tools">
            {sectionRef && onOpenTheory && (
              <button
                type="button"
                className="secondary btn-feedback-tool"
                onClick={() => onOpenTheory(sectionRef)}
              >
                📖 Xem lý thuyết {sectionRef}
              </button>
            )}
            {video && onOpenVideo && (
              <button
                type="button"
                className="secondary btn-feedback-tool btn-feedback-video"
                onClick={() => onOpenVideo(video)}
              >
                🎬 Video giải thích ({video.channel} · {video.timestampLabel})
              </button>
            )}
            {onOpenAI && (
              <button
                type="button"
                className="secondary btn-feedback-tool btn-feedback-ai"
                onClick={onOpenAI}
              >
                🤖 Hỏi AI về câu này
              </button>
            )}
          </div>

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
