// @vitest-environment jsdom
import { describe, it, expect } from 'vitest';
import { evaluateOpenAnswer } from './aiEvaluator';
import olp01Raw from '../data/exams/olp-01.json';
import olp02Raw from '../data/exams/olp-02.json';
import type { Exam, McqQuestion } from '../types/exam';

const olp01 = olp01Raw as unknown as Exam;
const olp02 = olp02Raw as unknown as Exam;

describe('aiEvaluator Rubric Evaluation Regressions (P0-1, P1-1)', () => {
  const e01 = olp01.questions.find((q) => q.id === 'OLP01-E01')!;
  const e02 = olp01.questions.find((q) => q.id === 'OLP01-E02')!;

  it('Empty or too short answer returns 0 points and level "Chưa đạt"', () => {
    const resEmpty = evaluateOpenAnswer(e01, '');
    expect(resEmpty.score).toBe(0);
    expect(resEmpty.level).toBe('Chưa đạt');

    const resShort = evaluateOpenAnswer(e01, 'bài làm ngắn');
    expect(resShort.score).toBe(0);
    expect(resShort.level).toBe('Chưa đạt');
  });

  it('Gibberish repetition returns 0 points (never gives free 8.5đ or AC)', () => {
    const gibberish = 'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij';
    const res = evaluateOpenAnswer(e01, gibberish);
    expect(res.score).toBe(0);
    for (const item of res.breakdown) {
      expect(item.earnedPoints).toBe(0);
      expect(item.pass).toBe(false);
    }
  });

  it('OLP01-E01: Evaluates sign language clip classification with Macro-F1 and GroupKFold', () => {
    const validEssay = `
      1. Phân tích bài toán: Phân loại 50 cử chỉ video độc lập (clip classification) cho người khiếm thính.
      2. Tiền xử lý & Trích xuất đặc trưng: Sử dụng MediaPipe trích xuất 21 điểm mốc bàn tay hoặc 3D-CNN.
      3. Chống rò rỉ (Leakage): Chia fold theo người thực hiện bằng GroupKFold (person-independent) để tránh overfit theo nhân dạng người làm mẫu.
      4. Huấn luyện mô hình: Spatial-Temporal Graph Convolution (ST-GCN) kết hợp Cross-Entropy Loss và Cosine Annealing.
      5. Đánh giá: Sử dụng Macro-F1 và Confusion Matrix trên 50 lớp cử chỉ để đo lường độ chính xác cân bằng giữa các cử chỉ.
    `;
    const res = evaluateOpenAnswer(e01, validEssay);
    expect(res.score).toBeGreaterThan(0);
    // Không bao giờ chứa nhắc nhở lạc đề CER/WER/CTC
    const allFeedback = res.breakdown.map((b) => b.feedback).join(' ');
    expect(allFeedback).not.toContain('CTC');
    expect(allFeedback).not.toContain('CER');
    expect(allFeedback).not.toContain('WER');
  });

  it('OLP01-E02: NMT from scratch enforces Transformer from scratch without pretrained models', () => {
    const validEssay = `
      1. Bối cảnh & Ràng buộc: Dịch máy NMT Hoa - Việt, tuân thủ nghiêm ngặt cấm sử dụng mô hình pretrained MT.
      2. Tokenization: Sử dụng SentencePiece BPE huấn luyện từ đầu trên tập train.zh và train.vi.
      3. Kiến trúc: Transformer Encoder-Decoder from scratch với 6 encoder layers, 6 decoder layers, Multi-Head Attention.
      4. Huấn luyện & Tối ưu: AdamW với Noam scheduler (warmup), Label Smoothing 0.1, Dropout 0.1.
      5. Giải mã & Metric: Beam search với length penalty; đánh giá bằng SacreBLEU với hệ số phạt độ dài Brevity Penalty (BP).
    `;
    const res = evaluateOpenAnswer(e02, validEssay);
    expect(res.score).toBeGreaterThan(0);
    // Không chứa gợi ý vi phạm pretrained mBART/NLLB
    const allFeedback = res.breakdown.map((b) => b.feedback).join(' ');
    expect(allFeedback).not.toContain('mBART');
    expect(allFeedback).not.toContain('NLLB');
  });

  it('VOAI02-M49: Question key C, options, and explanation are fully consistent', () => {
    const m49 = olp02.questions.find((q) => q.id === 'VOAI02-M49') as McqQuestion;
    expect(m49).toBeDefined();
    expect(m49.answer).toBe('C');
    const optC = m49.options?.find((o: { key: string }) => o.key === 'C');
    expect(optC).toBeDefined();
    expect(optC!.text).toMatch(/Tách từ.*Chuẩn hóa.*từ dừng.*Rút (?:gọn|gốc).*Vector hóa/i);
    // Lời giải phải nhất quán chọn C và không mâu thuẫn
    expect(m49.explanation).toContain('Đáp án chính xác là **C**');
  });
});
