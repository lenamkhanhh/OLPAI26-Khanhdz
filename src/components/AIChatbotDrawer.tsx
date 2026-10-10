import { useState, useEffect, useRef } from 'react';
import type { Question, AnswerState } from '../types/exam';
import { MathText } from './MathText';
import { evaluateOpenAnswer, getSocraticAdvice, type EvaluationResult } from '../utils/aiEvaluator';

interface Props {
  isOpen: boolean;
  question: Question;
  answer?: AnswerState;
  onClose: () => void;
  onApplyScore?: (score: number, rubricChecks: boolean[]) => void;
}

interface ChatMessage {
  id: string;
  sender: 'assistant' | 'user';
  text: string;
  timestamp: string;
}

export function AIChatbotDrawer({ isOpen, question, answer, onClose, onApplyScore }: Props) {
  const [activeTab, setActiveTab] = useState<'evaluator' | 'tutor'>('evaluator');
  const [isEvaluating, setIsEvaluating] = useState(false);
  const [evaluation, setEvaluation] = useState<EvaluationResult | null>(null);
  
  // Chat state
  const [inputMessage, setInputMessage] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>(() => [
    {
      id: 'welcome',
      sender: 'assistant',
      text: `👋 Chào bạn! Tôi là **Trợ lý AI Olympic**.\nTôi có thể giúp bạn:\n1. **Chấm điểm tự luận theo Rubric 5 bước** và chỉ ra các thiếu sót kỹ thuật.\n2. **Gợi ý tư duy Socratic** và giải thích các công thức toán/lý thuyết.\n\nHãy chọn tab hoặc đặt câu hỏi bất kỳ nhé!`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }
  ]);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto scroll to bottom when messages update
  useEffect(() => {
    if (activeTab === 'tutor') {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, activeTab]);

  // Handle run AI grading
  const handleEvaluate = () => {
    setIsEvaluating(true);
    // Tạo delay ngắn 400ms để tạo cảm giác suy nghĩ tự nhiên
    setTimeout(() => {
      const result = evaluateOpenAnswer(question, answer?.text || '');
      setEvaluation(result);
      setIsEvaluating(false);
    }, 400);
  };

  // Handle apply score to quiz state
  const handleApply = () => {
    if (!evaluation || !onApplyScore) return;
    const checks = evaluation.breakdown.map((b) => b.pass);
    onApplyScore(evaluation.score, checks);
  };

  // Handle send message
  const handleSendMessage = (textToSend?: string) => {
    const text = (textToSend || inputMessage).trim();
    if (!text) return;

    const userMsg: ChatMessage = {
      id: `user-${Date.now()}`,
      sender: 'user',
      text,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputMessage('');

    // Generate AI response
    setTimeout(() => {
      const reply = getSocraticAdvice(question, text);
      const aiMsg: ChatMessage = {
        id: `ai-${Date.now()}`,
        sender: 'assistant',
        text: reply,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages((prev) => [...prev, aiMsg]);
    }, 350);
  };

  const quickPrompts = [
    { label: '💡 Gợi ý cách làm', query: 'Gợi ý cách giải bài này' },
    { label: '📋 Khung 5 bước', query: 'Khung 5 bước giải tự luận chuẩn OLP là gì?' },
    { label: '📐 Công thức liên quan', query: 'Các công thức toán học liên quan đến câu này' },
    { label: '🛡️ Tránh rò rỉ dữ liệu', query: 'Làm sao tránh data leakage trong bài toán này?' }
  ];

  return (
    <>
      <div
        className={`ai-chatbot-backdrop${isOpen ? ' open' : ''}`}
        onClick={onClose}
        aria-hidden={!isOpen}
      />

      <aside className={`ai-chatbot-drawer${isOpen ? ' open' : ''}`} aria-label="AI Chatbot Drawer">
        {/* Header */}
        <header className="ai-drawer-header">
          <div className="ai-header-title">
            <div className="ai-avatar-badge">⚡</div>
            <div className="ai-title-text">
              <h3>Olympic AI Assistant</h3>
              <span>● Sẵn sàng hỗ trợ ({question.id})</span>
            </div>
          </div>
          <div className="ai-header-actions">
            <button
              type="button"
              className="ai-icon-btn"
              onClick={onClose}
              title="Đóng bảng AI"
              aria-label="Đóng"
            >
              ✕
            </button>
          </div>
        </header>

        {/* Tab Switcher */}
        <nav className="ai-drawer-tabs" role="tablist">
          <button
            type="button"
            className={`ai-tab-btn${activeTab === 'evaluator' ? ' active' : ''}`}
            onClick={() => setActiveTab('evaluator')}
            role="tab"
            aria-selected={activeTab === 'evaluator'}
          >
            📊 Chấm Rubric Tự Luận
          </button>
          <button
            type="button"
            className={`ai-tab-btn${activeTab === 'tutor' ? ' active' : ''}`}
            onClick={() => setActiveTab('tutor')}
            role="tab"
            aria-selected={activeTab === 'tutor'}
          >
            🤖 Gia Sư AI Socratic
          </button>
        </nav>

        {/* Body content */}
        <div className="ai-drawer-body">
          {activeTab === 'evaluator' ? (
            <div className="evaluator-tab-pane">
              {/* Banner intro */}
              <div className="evaluator-banner">
                <h4>🎯 Đánh giá tự động theo Rubric</h4>
                <p>
                  AI sẽ đối chiếu bài làm của bạn với 5 tiêu chí chuẩn của Hội đồng thi OLP AI (kiến trúc, pipeline, metrics, chống leakage, phương án mở rộng).
                </p>

                <button
                  type="button"
                  className="btn-grade-now"
                  onClick={handleEvaluate}
                  disabled={isEvaluating}
                >
                  {isEvaluating ? '⏳ Đang phân tích bài làm...' : '⚡ Chấm điểm bài làm ngay'}
                </button>
              </div>

              {/* Kết quả đánh giá */}
              {evaluation && (
                <div className="evaluation-result-card">
                  <div className="score-display-row">
                    <div>
                      <span style={{ fontSize: '0.8rem', color: '#94a3b8', textTransform: 'uppercase' }}>
                        Điểm số AI đánh giá
                      </span>
                      <div className="score-big">
                        {evaluation.score} / {evaluation.maxScore} điểm
                      </div>
                    </div>
                    <div>
                      <span
                        className="badge-level"
                        style={{
                          padding: '4px 10px',
                          borderRadius: '6px',
                          fontSize: '0.78rem',
                          fontWeight: 700,
                          background: evaluation.percentage >= 65 ? 'rgba(16, 185, 129, 0.2)' : 'rgba(244, 63, 94, 0.2)',
                          color: evaluation.percentage >= 65 ? '#10b981' : '#f43f5e'
                        }}
                      >
                        {evaluation.level}
                      </span>
                    </div>
                  </div>

                  {/* Nhận xét tổng quan */}
                  <div className="evaluation-summary-text">
                    <strong>Đánh giá chung:</strong> {evaluation.summary}
                  </div>

                  {/* Chi tiết từng tiêu chí */}
                  <div className="rubric-breakdown-list">
                    <h5 style={{ fontSize: '0.85rem', color: '#cbd5e1', margin: '4px 0 2px' }}>
                      Chi tiết từng tiêu chí Rubric:
                    </h5>
                    {evaluation.breakdown.map((item, idx) => (
                      <div
                        key={idx}
                        className={`rubric-item-row ${item.pass ? 'pass' : 'fail'}`}
                      >
                        <span className={`rubric-item-status ${item.pass ? 'pass' : 'fail'}`}>
                          {item.pass ? '✓' : '✗'}
                        </span>
                        <div className="rubric-item-content">
                          <span className="rubric-item-title">
                            {item.criterion} ({item.earnedPoints}/{item.maxPoints} đ)
                          </span>
                          <span className="rubric-item-note">{item.feedback}</span>
                        </div>
                      </div>
                    ))}
                  </div>

                  {/* Nút lưu điểm vào bài làm */}
                  {onApplyScore && (
                    <button
                      type="button"
                      className="btn-apply-score"
                      onClick={handleApply}
                      title="Lưu số điểm này vào kết quả tự chấm của bạn"
                    >
                      💾 Áp dụng điểm này ({evaluation.score}đ) vào bài thi
                    </button>
                  )}
                </div>
              )}
            </div>
          ) : (
            <div className="tutor-tab-pane">
              {/* Chat thread */}
              <div className="chat-messages-container">
                {messages.map((msg) => (
                  <div key={msg.id} className={`chat-bubble ${msg.sender}`}>
                    <div className="chat-bubble-avatar">
                      {msg.sender === 'assistant' ? '⚡' : '👤'}
                    </div>
                    <div className="chat-bubble-content">
                      <MathText text={msg.text} />
                      <div
                        style={{
                          fontSize: '0.7rem',
                          color: 'rgba(255, 255, 255, 0.4)',
                          marginTop: '4px',
                          textAlign: msg.sender === 'user' ? 'right' : 'left'
                        }}
                      >
                        {msg.timestamp}
                      </div>
                    </div>
                  </div>
                ))}
                <div ref={messagesEndRef} />
              </div>

              {/* Quick Prompts */}
              <div style={{ marginTop: '14px' }}>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Gợi ý nhanh:</span>
                <div className="quick-prompt-chips">
                  {quickPrompts.map((qp, idx) => (
                    <button
                      key={idx}
                      type="button"
                      className="prompt-chip"
                      onClick={() => handleSendMessage(qp.query)}
                    >
                      {qp.label}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Footer (Chat input if in tutor tab) */}
        {activeTab === 'tutor' && (
          <footer className="ai-drawer-footer">
            <form
              className="chat-input-form"
              onSubmit={(e) => {
                e.preventDefault();
                handleSendMessage();
              }}
            >
              <textarea
                className="chat-input-textarea"
                rows={1}
                placeholder="Hỏi AI về cách làm, công thức KaTeX..."
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSendMessage();
                  }
                }}
              />
              <button
                type="submit"
                className="chat-send-btn"
                disabled={!inputMessage.trim()}
                title="Gửi câu hỏi"
              >
                ➤
              </button>
            </form>
          </footer>
        )}
      </aside>
    </>
  );
}
