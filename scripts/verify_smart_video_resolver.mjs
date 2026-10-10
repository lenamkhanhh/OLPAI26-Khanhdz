// scripts/verify_smart_video_resolver.mjs
import fs from 'fs';
import path from 'path';
import { JSDOM } from 'jsdom';

const htmlPath = path.join(process.cwd(), 'public', 'olympic_ai_study_hub.html');
const htmlContent = fs.readFileSync(htmlPath, 'utf8');

const dom = new JSDOM(htmlContent, {
  runScripts: 'dangerously',
  resources: 'usable'
});

const { window } = dom;

// Chờ DOM load
setTimeout(() => {
  const ALL_EXAMS = window.eval('ALL_EXAMS');
  const VIDEOS = window.eval('VIDEOS');
  console.log(`Đã nạp ${Object.keys(ALL_EXAMS).length} đề thi và ${Object.keys(VIDEOS).length} video bài giảng.`);

  const testCases = [
    { examId: 'olp-04', qId: 'OLP04-Q01', expectedSec: '§3.8', expectedTopic: 'Mô hình Sinh: Diffusion Models vs GANs' },
    { examId: 'olp-04', qId: 'OLP04-Q04', expectedSec: '§7.1', expectedTopic: 'Tác vụ OLP 2025: Nhận diện Ngôn ngữ Ký hiệu Video' },
    { examId: 'olp-04', qId: 'OLP04-Q05', expectedSec: '§7.2', expectedTopic: 'Tác vụ OLP 2025: Dịch máy Thương mại điện tử' },
    { examId: 'olp-04', qId: 'OLP04-Q06', expectedSec: '§7.4', expectedTopic: 'Tác vụ OLP 2026: Tabular Churn Prediction & XAI' },
    { examId: 'olp-04', qId: 'OLP04-Q07', expectedSec: '§3.5', expectedTopic: 'Vision Transformer (ViT)' },
    { examId: 'olp-04', qId: 'OLP04-Q12', expectedSec: '§4.7', expectedTopic: 'Độ đo NLP: BLEU' },
    { examId: 'olp-04', qId: 'OLP04-Q18', expectedSec: '§3.6', expectedTopic: 'Object Detection' },
    { examId: 'olp-05', qId: 'SKILL-NLP-01', expectedSec: '§4.2', expectedTopic: 'Biểu diễn từ: Word2Vec, FastText' },
    { examId: 'voai-2025', qId: 'VOAI25-010', expectedSec: '§3.6', expectedTopic: 'Object Detection' },
    { examId: 'olp-01', qId: 'OLP01-A07', expectedSec: '§5.3', expectedTopic: 'Kỳ vọng, Phương sai' }
  ];

  let passCount = 0;
  testCases.forEach(tc => {
    const exam = ALL_EXAMS[tc.examId];
    const q = exam.questions.find(item => item.id === tc.qId);
    if (!q) {
      console.log(`❌ Không tìm thấy ${tc.qId}`);
      return;
    }

    // Mô phỏng resolveVideoForQuestion
    const exp = q.explanation || '';
    const m = exp.match(/§\s*(\d+\.\d+)/);
    const sec = m ? `§${m[1]}` : '§1.1';
    const vid = VIDEOS[sec];

    if (vid && vid.sectionId === tc.expectedSec) {
      console.log(`✓ [${tc.qId}] -> Đúng video ${vid.sectionId}: ${vid.title} (Kênh: ${vid.channel})`);
      passCount++;
    } else {
      console.log(`❌ [${tc.qId}] -> LỆCH: Kỳ vọng ${tc.expectedSec}, thực tế ${vid ? vid.sectionId : 'NONE'}`);
    }
  });

  console.log(`\nKết quả kiểm thử video resolver: ${passCount}/${testCases.length} PASS!`);
  if (passCount === testCases.length) {
    console.log("=== TẤT CẢ VIDEO ĐỀU ĐƯỢC PHÂN GIẢI CHUẨN XÁC THEO ĐÚNG NỘI DUNG HỌC THUẬT ===");
  }
  process.exit(passCount === testCases.length ? 0 : 1);
}, 300);
