import { useEffect } from 'react';
import type { VideoResource } from '../data/videoData';

interface Props {
  video: VideoResource;
  onClose: () => void;
}

export function VideoModal({ video, onClose }: Props) {
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [onClose]);

  // Tao URL nhung YouTube voi start timestamp
  const embedUrl = `https://www.youtube-nocookie.com/embed/${video.youtubeId}?autoplay=1&start=${video.startSeconds}&rel=0`;

  return (
    <div className="palette-backdrop video-modal-backdrop" role="presentation" onMouseDown={(e) => { if (e.target === e.currentTarget) onClose(); }}>
      <section className="video-dialog card" role="dialog" aria-modal="true" aria-label={`Video bài giảng ${video.sectionId}`}>
        <header className="video-dialog__header">
          <div>
            <div className="video-badge-row">
              <span className="video-badge video-badge--section">{video.sectionId}</span>
              <span className="video-badge video-badge--channel">{video.channel}</span>
              <span className="video-badge video-badge--time">⏱️ Tua sẵn tới {video.timestampLabel}</span>
            </div>
            <h3 className="video-dialog__title">{video.topic}</h3>
          </div>
          <button type="button" className="video-dialog__close" onClick={onClose} aria-label="Đóng video">✕</button>
        </header>

        <div className="video-player-container">
          <iframe
            src={embedUrl}
            title={video.title}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowFullScreen
            className="video-iframe"
          />
        </div>

        <div className="video-dialog__footer">
          <div className="video-note">
            <strong>💡 Điểm trọng tâm cần chú ý:</strong>
            <p>{video.highlightNote}</p>
          </div>
          <div className="video-actions">
            <a
              href={`https://www.youtube.com/watch?v=${video.youtubeId}&t=${video.startSeconds}s`}
              target="_blank"
              rel="noopener noreferrer"
              className="secondary btn-external-link"
            >
              Mở trên YouTube ↗
            </a>
            <button type="button" className="primary" onClick={onClose}>Đã hiểu, quay lại làm tiếp</button>
          </div>
        </div>
      </section>
    </div>
  );
}
