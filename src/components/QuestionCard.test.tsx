// @vitest-environment jsdom
import { act } from 'react';
import { createRoot, type Root } from 'react-dom/client';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { Question } from '../types/exam';
import { QuestionCard } from './QuestionCard';

const essayQuestion: Question = {
  id: 'TEST-C10',
  module: 'C',
  type: 'essay',
  points: 8,
  prompt: 'Hãy trình bày cách triển khai một pipeline AI cơ bản.',
  modelAnswer: 'Đây là đáp án mẫu chỉ được hiện khi người học chủ động yêu cầu.',
  rubric: ['Nêu được pipeline chính.', 'Có ví dụ cụ thể.', 'Có cách đánh giá.'],
  tags: ['essay']
};

let container: HTMLDivElement;
let root: Root;

function setTextareaValue(textarea: HTMLTextAreaElement, value: string) {
  Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value')?.set?.call(textarea, value);
  textarea.dispatchEvent(new Event('input', { bubbles: true }));
}

function setSliderValue(slider: HTMLInputElement, value: string) {
  Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value')?.set?.call(slider, value);
  slider.dispatchEvent(new Event('input', { bubbles: true }));
}

beforeEach(() => {
  (globalThis as typeof globalThis & { IS_REACT_ACT_ENVIRONMENT: boolean }).IS_REACT_ACT_ENVIRONMENT = true;
  container = document.createElement('div');
  document.body.append(container);
  root = createRoot(container);
});

afterEach(async () => {
  await act(async () => root.unmount());
  container.remove();
});

function renderCard(onAnswer: (a: never) => void, extra?: Partial<Parameters<typeof QuestionCard>[0]>) {
  return act(async () => {
    root.render(
      <QuestionCard
        question={essayQuestion}
        index={9}
        total={60}
        mode="practice"
        submitted={false}
        hasNext
        onAnswer={onAnswer as (a: object) => void}
        onNext={() => {}}
        {...extra}
      />
    );
  });
}

describe('QuestionCard open answers', () => {
  it('does not reveal hints or the model answer just because the learner starts typing', async () => {
    const onAnswer = vi.fn();
    await renderCard(onAnswer);

    const textarea = container.querySelector<HTMLTextAreaElement>('textarea')!;
    await act(async () => setTextareaValue(textarea, 'Câu trả lời của tôi'));

    expect(onAnswer).toHaveBeenCalled();
    expect(container.textContent).not.toContain(essayQuestion.modelAnswer);
    expect(container.textContent).not.toContain(essayQuestion.rubric[0]);
    expect(container.textContent).toContain('Gợi ý');
    expect(container.textContent).toContain('Xem đáp án mẫu');
  });

  it('reveals rubric checklist and model answer independently through explicit buttons', async () => {
    await renderCard(vi.fn());

    const buttons = [...container.querySelectorAll<HTMLButtonElement>('.open-answer-tools button')];
    const hintButton = buttons.find((button) => button.textContent === 'Gợi ý')!;
    const modelButton = buttons.find((button) => button.textContent === 'Xem đáp án mẫu')!;

    await act(async () => hintButton.click());
    expect(container.textContent).toContain(essayQuestion.rubric[0]);
    expect(container.textContent).not.toContain(essayQuestion.modelAnswer);
    expect(container.querySelectorAll('.rubric-checklist input[type="checkbox"]').length).toBe(3);

    await act(async () => modelButton.click());
    expect(container.textContent).toContain(essayQuestion.modelAnswer);
    expect(container.textContent).toContain('Tự chấm:');
  });

  it('reports slider self-grade through onAnswer', async () => {
    const onAnswer = vi.fn();
    await renderCard(onAnswer);

    const modelButton = [...container.querySelectorAll<HTMLButtonElement>('.open-answer-tools button')]
      .find((button) => button.textContent === 'Xem đáp án mẫu')!;
    await act(async () => modelButton.click());

    const slider = container.querySelector<HTMLInputElement>('.essay-score input[type="range"]')!;
    await act(async () => setSliderValue(slider, '6'));
    expect(onAnswer).toHaveBeenCalledWith(expect.objectContaining({ essayScore: 6 }));
  });

  it('keeps hints and model answers hidden in exam mode', async () => {
    await renderCard(vi.fn(), { mode: 'exam' });

    expect(container.textContent).not.toContain(essayQuestion.modelAnswer);
    expect(container.textContent).not.toContain(essayQuestion.rubric[0]);
    expect(container.textContent).toContain('Gợi ý và đáp án mẫu được ẩn trong Exam mode.');
  });
});
