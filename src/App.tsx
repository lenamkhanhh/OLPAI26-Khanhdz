import { useState } from 'react';
import { exams } from './data/exams';
import type { QuizMode } from './types/exam';
import type { VideoResource } from './data/videoData';
import { loadMode } from './utils/storage';
import { ExamSelector } from './components/ExamSelector';
import { QuizRunner } from './components/QuizRunner';
import { TheoryHandbook } from './components/TheoryHandbook';
import { VideoModal } from './components/VideoModal';
import './styles/global.css';
import './styles/quiz.css';
import './styles/ai-chatbot.css';

export default function App() {
  const [selectedExamId, setSelectedExamId] = useState(exams[0]?.id ?? '');
  const [mode, setMode] = useState<QuizMode>(() => loadMode());
  const [timerEnabled, setTimerEnabled] = useState(false);
  const [view, setView] = useState<'selector' | 'quiz' | 'handbook'>('selector');
  const [activeVideo, setActiveVideo] = useState<VideoResource | null>(null);

  const exam = exams.find((item) => item.id === selectedExamId) ?? exams[0];

  if (!exam) return <main className="page-shell"><h1>Chưa có đề nào</h1></main>;

  if (view === 'handbook') {
    return (
      <>
        <TheoryHandbook
          onBack={() => setView('selector')}
          onOpenVideo={(video) => setActiveVideo(video)}
        />
        {activeVideo && (
          <VideoModal video={activeVideo} onClose={() => setActiveVideo(null)} />
        )}
      </>
    );
  }

  if (view === 'selector') {
    return (
      <>
        <ExamSelector
          exams={exams}
          selectedExamId={selectedExamId}
          mode={mode}
          timerEnabled={timerEnabled}
          onExamChange={setSelectedExamId}
          onModeChange={setMode}
          onTimerChange={setTimerEnabled}
          onStart={() => setView('quiz')}
          onOpenHandbook={() => setView('handbook')}
        />
        {activeVideo && (
          <VideoModal video={activeVideo} onClose={() => setActiveVideo(null)} />
        )}
      </>
    );
  }

  return (
    <>
      <QuizRunner
        exam={exam}
        mode={mode}
        timerEnabled={timerEnabled}
        onHome={() => setView('selector')}
      />
      {activeVideo && (
        <VideoModal video={activeVideo} onClose={() => setActiveVideo(null)} />
      )}
    </>
  );
}
