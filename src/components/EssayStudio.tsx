import { useState, useMemo } from 'react';
import type { Question, AnswerState } from '../types/exam';
import { MathText } from './MathText';

interface Props {
  question: Question;
  answer?: AnswerState;
  canUseOpenHelp: boolean;
  showHint: boolean;
  showModelAnswer: boolean;
  onToggleHint: () => void;
  onToggleModelAnswer: () => void;
  onAnswer: (answer: AnswerState) => void;
  onOpenAI?: () => void;
  sectionRef?: string;
  onOpenTheory?: (sectionId: string) => void;
  videoButton?: React.ReactNode;
}

const TEMPLATE_5_STEPS = `### 1. Phân tích bài toán & Dữ liệu
- Đặc thù đầu vào/đầu ra:
- Khó khăn cốt lõi (mất cân bằng lớp / nhiễu / tài nguyên):

### 2. Thiết kế mô hình & Luận giải
- Mô hình baseline:
- Mô hình đề xuất chính:
- Lý do kỹ thuật lựa chọn:

### 3. Pipeline xử lý & Chống rò rỉ dữ liệu (Leakage)
- Tiền xử lý & Augmentation:
- Chiến lược phân chia dữ liệu (Train/Val/Test):
- Hậu xử lý & Giải mã:

### 4. Metric đánh giá chuẩn xác
- Thước đo chính và lý do chọn:
- Chỉ số đánh giá theo từng lớp/ngoại lệ:

### 5. Phương án cải tiến & Tối ưu triển khai
- Kỹ thuật nâng cao (Pretrain / Ensemble / TTA):
- Tối ưu hóa suy luận (Quantization / Distillation):
`;

export function EssayStudio({
  question,
  answer,
  canUseOpenHelp,
  showHint,
  showModelAnswer,
  onToggleHint,
  onToggleModelAnswer,
  onAnswer,
  onOpenAI,
  sectionRef,
  onOpenTheory,
  videoButton
}: Props) {
  const [viewMode, setViewMode] = useState<'editor' | 'preview'>('editor');
  const isCode = question.type === 'code';
  const text = answer?.text ?? '';

  const stats = useMemo(() => {
    const chars = text.length;
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    return { chars, words };
  }, [text]);

  const handleInsertTemplate = () => {
    if (text.trim() && !window.confirm('Nạp khung mẫu sẽ chèn thêm cấu trúc 5 bước vào nội dung. Tiếp tục?')) {
      return;
    }
    const nextText = text.trim() ? `${text}\n\n${TEMPLATE_5_STEPS}` : TEMPLATE_5_STEPS;
    onAnswer({ ...answer, text: nextText });
  };

  return (
    <div className="open-answer essay-studio">
      {/* Studio Header: Tab soạn thảo & Thống kê */}
      <div className="essay-studio-bar">
        <div className="essay-mode-tabs">
          <button
            type="button"
            className={`essay-tab-toggle${viewMode === 'editor' ? ' active' : ''}`}
            onClick={() => setViewMode('editor')}
          >
            ✏️ {isCode ? 'Soạn thảo Code' : 'Soạn thảo bài làm'}
          </button>
          <button
            type="button"
            className={`essay-tab-toggle${viewMode === 'preview' ? ' active' : ''}`}
            onClick={() => setViewMode('preview')}
            disabled={!text.trim()}
          >
            👁️ Xem trước (KaTeX)
          </button>
        </div>

        <div className="essay-stats-pill">
          <span>{stats.words} từ</span>
          <span>·</span>
          <span>{stats.chars} ký tự</span>
          {answer?.essayScore !== undefined && (
            <>
              <span>·</span>
              <span className="badge-saved-score">Đã chấm: {answer.essayScore}/{question.points}đ</span>
            </>
          )}
        </div>
      </div>

      {/* Vùng nhập liệu / Xem trước */}
      {viewMode === 'editor' ? (
        <textarea
          placeholder={isCode ? 'Gõ code/pseudo-code của bạn...' : 'Trình bày giải pháp theo khung 5 bước...'}
          value={text}
          onChange={(event) => onAnswer({ ...answer, text: event.target.value })}
        />
      ) : (
        <div className="essay-preview-box">
          <MathText text={text} />
        </div>
      )}

      {/* Thanh công cụ mở rộng */}
      {canUseOpenHelp ? (
        <div className="open-answer-tools">
          <button
            type="button"
            className="secondary"
            aria-expanded={showHint}
            onClick={onToggleHint}
          >
            {showHint ? 'Ẩn gợi ý' : 'Gợi ý'}
          </button>
          
          <button
            type="button"
            className="secondary"
            aria-expanded={showModelAnswer}
            onClick={onToggleModelAnswer}
          >
            {showModelAnswer ? 'Ẩn đáp án mẫu' : 'Xem đáp án mẫu'}
          </button>

          {!isCode && (
            <button
              type="button"
              className="secondary btn-template"
              onClick={handleInsertTemplate}
              title="Chèn khung 5 bước chuẩn OLP AI"
            >
              📋 Nạp khung 5 bước
            </button>
          )}

          {onOpenAI && (
            <button
              type="button"
              className="secondary btn-ai-evaluate-trigger"
              onClick={onOpenAI}
              title="Mở AI Evaluator để chấm điểm bài làm này"
            >
              ⚡ AI Chấm Bài
            </button>
          )}

          {sectionRef && onOpenTheory && (
            <button
              type="button"
              className="secondary"
              onClick={() => onOpenTheory(sectionRef)}
            >
              📖 Lý thuyết {sectionRef}
            </button>
          )}

          {videoButton}
        </div>
      ) : (
        <p className="open-help-note">Gợi ý và đáp án mẫu được ẩn trong Exam mode.</p>
      )}
    </div>
  );
}
