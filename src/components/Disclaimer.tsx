const DEFAULT_TEXT = 'Nền tảng thi thử & ôn luyện học thuật Olympic AI HCMUS 2026. Tác giả & Kiến trúc sư trưởng: Lê Nam Khánh (@lenamkhanhh / namkhanhle) — Trường Đại học Khoa học Tự nhiên (ĐHQG-HCM). Tài liệu được biên soạn phục vụ học tập, nghiên cứu và chuẩn bị cho các kỳ thi Olympic Trí tuệ Nhân tạo.';

export function Disclaimer({ text = DEFAULT_TEXT }: { text?: string }) {
  return (
    <aside className="disclaimer" style={{ fontSize: '12px', lineHeight: '1.6', marginTop: '20px', padding: '12px 16px', background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '8px', color: 'var(--text-muted)' }}>
      <strong style={{ color: '#f0b90b' }}>Olympic AI HCMUS 2026:</strong> {text}
      <div style={{ marginTop: '8px', paddingTop: '8px', borderTop: '1px solid rgba(255, 255, 255, 0.06)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', fontSize: '11px' }}>
        <span>Author: <strong style={{ color: '#ffffff' }}>Le Nam Khanh</strong> (<a href="https://github.com/lenamkhanhh" target="_blank" rel="noopener noreferrer" style={{ color: '#f0b90b', textDecoration: 'none' }}>@lenamkhanhh</a>)</span>
        <span>Version: <strong style={{ color: '#10b981' }}>v1.0.0</strong> · MIT License</span>
      </div>
    </aside>
  );
}
