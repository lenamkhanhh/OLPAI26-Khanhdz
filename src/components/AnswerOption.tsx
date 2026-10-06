import { memo } from 'react';
import { MathText } from './MathText';

export type OptionState = 'idle' | 'selected' | 'correct' | 'wrong' | 'dimmed';

interface Props {
  optionKey: string;
  text: string;
  state: OptionState;
  disabled?: boolean;
  onSelect: () => void;
}

// Nút đáp án full-width: tap 1 lần chọn, tap lại để bỏ.
export const AnswerOption = memo(function AnswerOption({ optionKey, text, state, disabled, onSelect }: Props) {
  return (
    <button
      type="button"
      className={['answer-option', `answer-option--${state}`].join(' ')}
      disabled={disabled}
      onClick={onSelect}
      aria-pressed={state === 'selected' || state === 'correct'}
    >
      <span className="answer-option__key" aria-hidden="true">{optionKey}</span>
      <span className="answer-option__text"><MathText text={text} /></span>
      {state === 'correct' && <span className="answer-option__mark" aria-hidden="true">✓</span>}
      {state === 'wrong' && <span className="answer-option__mark" aria-hidden="true">✗</span>}
    </button>
  );
});
