import { useMemo } from 'react';
import katex from 'katex';

interface Props {
  text: string;
  className?: string;
}

// Render text thường lẫn công thức $...$ (inline) và $$...$$ (display) kèm markdown cơ bản (**bold**, `code`).
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
      let html = escapeHtml(part);
      // Ho tro markdown co ban: **bold**, *italic*, `code`, bullet points
      html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
      html = html.replace(/(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)/g, '<em>$1</em>');
      html = html.replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>');
      html = html.replace(/(?:^|\n)-\s+/g, '\n<span class="bullet-dot">•</span> ');
      return html.replace(/\n/g, '<br/>');
    })
    .join('');
}

function renderMixed(text: string): string {
  // Ưu tiên tách display $$...$$ trước (có thể nhiều dòng).
  const parts = text.split(/(\$\$[\s\S]+?\$\$)/g);
  return parts
    .map((part) => {
      if (part.startsWith('$$') && part.endsWith('$$') && part.length > 4) {
        return `<div class="math-display">${renderMath(part.slice(2, -2).trim(), true)}</div>`;
      }
      // Hỗ trợ code block ```...```: giữ nguyên <pre>, không render KaTeX bên trong.
      return part
        .split(/(```[\s\S]*?```)/g)
        .map((chunk) => {
          if (chunk.startsWith('```') && chunk.endsWith('```')) {
            const cleaned = chunk.slice(3, -3).replace(/^\w+\n/, '').trim();
            return `<pre class="code-block"><code>${escapeHtml(cleaned)}</code></pre>`;
          }
          return renderInlineMixed(chunk);
        })
        .join('');
    })
    .join('');
}
