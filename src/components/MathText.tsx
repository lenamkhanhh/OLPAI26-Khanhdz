import { useMemo } from 'react';
import katex from 'katex';

interface Props {
  text: string;
  className?: string;
}

// Render text thường lẫn công thức $...$ (inline) và $$...$$ (display).
// Công thức lỗi cú pháp → fallback text thô, không crash.
export function MathText({ text, className }: Props) {
  const html = useMemo(() => renderMixed(text), [text]);
  return <span className={className} dangerouslySetInnerHTML={{ __html: html }} />;
}

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function renderMath(src: string, displayMode: boolean): string {
  try {
    return katex.renderToString(src, { displayMode, throwOnError: false, strict: false });
  } catch {
    return `<code>${escapeHtml(src)}</code>`;
  }
}

function renderInlineMixed(segment: string): string {
  // Tách $...$ trong đoạn text (đoạn $$...$$ đã tách trước đó).
  const parts = segment.split(/(\$[^$\n]+?\$)/g);
  return parts
    .map((part) => {
      if (part.startsWith('$') && part.endsWith('$') && part.length > 2) {
        return renderMath(part.slice(1, -1), false);
      }
      return escapeHtml(part).replace(/\n/g, '<br/>');
    })
    .join('');
}

function renderMixed(text: string): string {
  // Ưu tiên tách display $$...$$ trước (có thể nhiều dòng).
  const parts = text.split(/(\$\$[\s\S]+?\$\$)/g);
  return parts
    .map((part) => {
      if (part.startsWith('$$') && part.endsWith('$$') && part.length > 4) {
        return `<div class="math-display">${renderMath(part.slice(2, -2), true)}</div>`;
      }
      // Hỗ trợ code block ```...```: giữ nguyên <pre>, không render KaTeX bên trong.
      return part
        .split(/(```[\s\S]*?```)/g)
        .map((chunk) => {
          if (chunk.startsWith('```') && chunk.endsWith('```')) {
            const cleaned = chunk.slice(3, -3).replace(/^\w+\n/, '').trim();
            return `<pre><code>${escapeHtml(cleaned)}</code></pre>`;
          }
          return renderInlineMixed(chunk);
        })
        .join('');
    })
    .join('');
}
