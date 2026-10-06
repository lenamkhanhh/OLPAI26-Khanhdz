import { useState, useEffect, useRef, useMemo } from 'react';
import { THEORY_SECTIONS, type TheorySection } from '../data/theoryData';
import { getVideoForSection, type VideoResource } from '../data/videoData';
import { MathText } from './MathText';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  targetSectionId?: string;
  onOpenVideo: (video: VideoResource) => void;
}

export function TheorySidebar({ isOpen, onClose, targetSectionId, onOpenVideo }: Props) {
  const [searchTerm, setSearchTerm] = useState('');
  const [autoSync, setAutoSync] = useState(true);
  const containerRef = useRef<HTMLDivElement>(null);

  // Tim kiem va loc cac section
  const filteredSections = useMemo(() => {
    const term = searchTerm.trim().toLowerCase();
    if (!term) return THEORY_SECTIONS;
    return THEORY_SECTIONS.filter((sec) => {
      const matchId = sec.secId.toLowerCase().includes(term);
      const matchTitle = sec.title.toLowerCase().includes(term);
      const matchBody = sec.body.toLowerCase().includes(term);
      return matchId || matchTitle || matchBody;
    });
  }, [searchTerm]);

  // Cuon toi section chi dinh
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

  // Tu dong cuon khi targetSectionId thay doi va autoSync bat
  useEffect(() => {
    if (isOpen && autoSync && targetSectionId) {
      const timer = setTimeout(() => {
        scrollToSection(targetSectionId);
      }, 150);
      return () => clearTimeout(timer);
    }
  }, [isOpen, autoSync, targetSectionId]);

  if (!isOpen) return null;

  return (
    <aside className="theory-sidebar card" aria-label="Sổ tay lý thuyết và video OLP AI">
      <header className="theory-sidebar__header">
        <div className="theory-sidebar__title-row">
          <span className="eyebrow">Tra cứu lý thuyết OLP AI</span>
          <h2>📖 Sổ tay Lý thuyết & Video</h2>
        </div>
        <button type="button" className="theory-sidebar__close" onClick={onClose} aria-label="Đóng sidebar">
          ✕
        </button>
      </header>

      {/* Thanh dieu huong va tim kiem */}
      <div className="theory-sidebar__controls">
        <div className="theory-search-box">
          <input
            type="text"
            className="theory-search-input"
            placeholder="🔍 Gõ §x.y (vd: §3.1) hoặc từ khóa (Conv, Bayes, ResNet...)"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && filteredSections.length > 0) {
                scrollToSection(filteredSections[0].secId);
              }
            }}
          />
          {searchTerm && (
            <button type="button" className="theory-search-clear" onClick={() => setSearchTerm('')}>
              ✕
            </button>
          )}
        </div>

        {targetSectionId && (
          <div className="theory-jump-row">
            <button
              type="button"
              className="theory-jump-btn primary"
              onClick={() => scrollToSection(targetSectionId)}
            >
              📍 Nhảy tới lý thuyết câu hiện tại ({targetSectionId})
            </button>
            <label className="theory-autosync-toggle">
              <input
                type="checkbox"
                checked={autoSync}
                onChange={(e) => setAutoSync(e.target.checked)}
              />
              Tự cuộn theo câu
            </label>
          </div>
        )}

        {/* Quick Chapters */}
        <div className="theory-quick-pills">
          {['§1', '§2', '§3', '§4', '§5', '§6', '§7'].map((ch) => (
            <button
              key={ch}
              type="button"
              className="theory-pill"
              onClick={() => scrollToSection(ch)}
            >
              {ch === '§1' && '§1 ML'}
              {ch === '§2' && '§2 DL'}
              {ch === '§3' && '§3 CV'}
              {ch === '§4' && '§4 NLP'}
              {ch === '§5' && '§5 Toán/Xác suất'}
              {ch === '§6' && '§6 Bẫy lỗi'}
              {ch === '§7' && '§7 Đề 25-26'}
            </button>
          ))}
        </div>
      </div>

      {/* Danh sach noi dung cac section */}
      <div className="theory-sidebar__content" ref={containerRef}>
        {filteredSections.length === 0 ? (
          <div className="theory-empty-state">
            <p>Không tìm thấy mục lý thuyết nào khớp với <strong>"{searchTerm}"</strong>.</p>
            <button type="button" className="secondary" onClick={() => setSearchTerm('')}>Xem toàn bộ lý thuyết</button>
          </div>
        ) : (
          filteredSections.map((sec) => {
            const video = getVideoForSection(sec.secId);
            const isTarget = targetSectionId === sec.secId;
            return (
              <section
                key={sec.id}
                id={sec.id}
                className={`theory-section${isTarget ? ' theory-section--active' : ''}`}
              >
                <div className="theory-section__header">
                  <div className="theory-section__badge-title">
                    <span className="theory-section__sec-id">{sec.secId}</span>
                    <h3 className="theory-section__title">{sec.title}</h3>
                  </div>
                  {video && (
                    <button
                      type="button"
                      className="theory-video-btn"
                      onClick={() => onOpenVideo(video)}
                      title={`Xem video: ${video.title} (tua sẵn ${video.timestampLabel})`}
                    >
                      🎬 Video ({video.timestampLabel})
                    </button>
                  )}
                </div>

                {video && (
                  <div className="theory-section__video-banner">
                    <span className="video-banner-icon">📺</span>
                    <div className="video-banner-info">
                      <strong>{video.channel}:</strong> {video.topic}
                    </div>
                    <button
                      type="button"
                      className="video-banner-play"
                      onClick={() => onOpenVideo(video)}
                    >
                      ▶ Xem ngay ({video.timestampLabel})
                    </button>
                  </div>
                )}

                <div className="theory-section__body">
                  <MathText text={sec.body} />
                </div>
              </section>
            );
          })
        )}
      </div>
    </aside>
  );
}
