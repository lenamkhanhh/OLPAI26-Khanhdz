import { useState, useMemo } from 'react';
import { THEORY_SECTIONS } from '../data/theoryData';
import { getVideoForSection, type VideoResource } from '../data/videoData';
import { MathText } from './MathText';

interface Props {
  onBack: () => void;
  onOpenVideo: (video: VideoResource) => void;
}

export function TheoryHandbook({ onBack, onOpenVideo }: Props) {
  const [searchTerm, setSearchTerm] = useState('');
  const [activeChapter, setActiveChapter] = useState<string>('all');

  const filteredSections = useMemo(() => {
    let list = THEORY_SECTIONS;
    if (activeChapter !== 'all') {
      list = list.filter((sec) => sec.secId.startsWith(activeChapter));
    }
    const term = searchTerm.trim().toLowerCase();
    if (!term) return list;
    return list.filter((sec) => {
      const matchId = sec.secId.toLowerCase().includes(term);
      const matchTitle = sec.title.toLowerCase().includes(term);
      const matchBody = sec.body.toLowerCase().includes(term);
      return matchId || matchTitle || matchBody;
    });
  }, [searchTerm, activeChapter]);

  const scrollToSection = (secId: string) => {
    const domId = 'sec-' + secId.replace('§', '').replace('.', '-');
    const el = document.getElementById(domId);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      el.classList.add('theory-section--highlight');
      setTimeout(() => {
        el.classList.remove('theory-section--highlight');
      }, 2500);
    }
  };

  return (
    <div className="handbook-page page-shell">
      <header className="handbook-header">
        <div className="handbook-header__nav">
          <button type="button" className="secondary handbook-back-btn" onClick={onBack}>
            ← Quay lại Luyện đề thi
          </button>
          <span className="eyebrow">OLP AI HCMUS 2026 · Tài liệu ôn thi chính thức</span>
        </div>
        <h1 className="handbook-title">📚 Sổ tay Lý thuyết & Công thức Toán AI (Full LaTeX KaTeX)</h1>
        <p className="handbook-subtitle">
          Bao quát 5 chương trọng tâm, 24 bẫy đề thi kinh điển, cùng 4 bài toán thực chiến OLP AI 2025 & 2026 kèm video bài giảng tua sẵn timestamp.
        </p>
      </header>

      {/* Thanh tim kiem & Bo loc chuong */}
      <div className="handbook-controls card">
        <div className="handbook-search-row">
          <input
            type="text"
            className="handbook-search-input"
            placeholder="🔍 Tìm kiếm công thức, thuật toán (vd: Conv2D, Bayes, ResNet, IoU, Adam, SMOTE)..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          {searchTerm && (
            <button type="button" className="handbook-clear-btn" onClick={() => setSearchTerm('')}>
              ✕ Xóa tìm kiếm
            </button>
          )}
        </div>

        <div className="handbook-chapter-tabs" role="tablist" aria-label="Lọc theo chương">
          {[
            { id: 'all', label: 'Tất cả (53 mục)' },
            { id: '§1', label: '§1 ML Cổ điển' },
            { id: '§2', label: '§2 Deep Learning' },
            { id: '§3', label: '§3 Thị giác máy tính (CV)' },
            { id: '§4', label: '§4 NLP' },
            { id: '§5', label: '§5 Toán & Xác suất' },
            { id: '§6', label: '§6 Bảng 24 Bẫy lỗi' },
            { id: '§7', label: '§7 Tác vụ OLP 2025-2026' },
          ].map((tab) => (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={activeChapter === tab.id}
              className={`handbook-tab${activeChapter === tab.id ? ' handbook-tab--active' : ''}`}
              onClick={() => {
                setActiveChapter(tab.id);
                if (tab.id !== 'all') scrollToSection(tab.id);
              }}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {/* Danh sach cac muc ly thuyet */}
      <main className="handbook-content">
        {filteredSections.length === 0 ? (
          <div className="handbook-empty card">
            <p>Không tìm thấy mục nào khớp với <strong>"{searchTerm}"</strong>.</p>
            <button type="button" className="secondary" onClick={() => { setSearchTerm(''); setActiveChapter('all'); }}>
              Hiển thị lại toàn bộ
            </button>
          </div>
        ) : (
          filteredSections.map((sec) => {
            const video = getVideoForSection(sec.secId);
            return (
              <article key={sec.id} id={sec.id} className="handbook-section card">
                <header className="handbook-section__header">
                  <div className="handbook-section__meta">
                    <span className="handbook-section__sec-id">{sec.secId}</span>
                    <h2 className="handbook-section__title">{sec.title}</h2>
                  </div>
                  {video && (
                    <button
                      type="button"
                      className="primary handbook-video-btn"
                      onClick={() => onOpenVideo(video)}
                    >
                      🎬 Video bài giảng ({video.timestampLabel})
                    </button>
                  )}
                </header>

                {video && (
                  <div className="handbook-video-callout">
                    <div className="video-callout-icon">📺</div>
                    <div className="video-callout-info">
                      <strong>Nguồn giảng giải tuyển chọn:</strong> {video.channel} — <em>"{video.title}"</em>
                      <p>{video.highlightNote}</p>
                    </div>
                    <button
                      type="button"
                      className="secondary video-callout-play"
                      onClick={() => onOpenVideo(video)}
                    >
                      ▶ Xem ngay (tua sẵn tới {video.timestampLabel})
                    </button>
                  </div>
                )}

                <div className="handbook-section__body">
                  <MathText text={sec.body} />
                </div>
              </article>
            );
          })
        )}
      </main>

      <footer className="handbook-footer">
        <button type="button" className="primary" onClick={onBack}>
          ← Quay lại Luyện đề thi OLP AI
        </button>
      </footer>
    </div>
  );
}
