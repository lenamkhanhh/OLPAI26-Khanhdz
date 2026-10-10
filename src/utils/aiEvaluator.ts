import type { Question, OpenQuestion } from '../types/exam';

export interface RubricEvaluationItem {
  criterion: string;
  maxPoints: number;
  earnedPoints: number;
  pass: boolean;
  feedback: string;
}

export interface EvaluationResult {
  score: number;
  maxScore: number;
  percentage: number;
  level: 'Xuất sắc' | 'Đạt yêu cầu' | 'Cần hoàn thiện' | 'Chưa đạt';
  summary: string;
  breakdown: RubricEvaluationItem[];
  improvementTips: string[];
}

/**
 * Danh sách tiêu chí đặc thù cho từng câu tự luận đề Olympic AI
 */
interface CriterionRule {
  keywords: string[];
  requiredPatterns?: RegExp[];
  maxPoints: number;
  passFeedback: string;
  failFeedback: string;
}

const QUESTION_RULES: Record<string, CriterionRule[]> = {
  'OLP01-E01': [
    {
      keywords: ['thời gian', 'time', 'temporal', 'người quay', '100 người', 'nền', 'ánh sáng', 'background', 'tốc độ', 'fps', 'real-time', 'độ dài'],
      maxPoints: 2,
      passFeedback: 'Phân tích tốt đặc thù video: chuỗi thời gian, đa dạng người thực hiện/ánh sáng và ràng buộc độ trễ.',
      failFeedback: 'Cần nêu rõ ràng hơn đặc thù chuỗi theo thời gian, tính đa dạng của 100 người quay và yêu cầu chạy real-time.'
    },
    {
      keywords: ['crnn', 'cnn', 'rnn', 'lstm', 'gru', 'transformer', 'conformer', 'convnext', 'resnet', 'backbone', 'baseline', '3d-cnn', 'st-gcn', 'keypoint', 'mediapipe'],
      maxPoints: 2,
      passFeedback: 'Lựa chọn mô hình chuỗi/không gian-thời gian hợp lý, có phân biệt baseline (CRNN/CNN+RNN/3D-CNN) và kiến trúc nâng cao (Keypoints ST-GCN/Transformer).',
      failFeedback: 'Thiếu so sánh giữa mô hình baseline cơ sở và mô hình cải tiến, hoặc chưa nêu rõ vai trò backbone trích đặc trưng.'
    },
    {
      keywords: ['trích frame', 'frame', 'keypoint', 'mediapipe', 'leakage', 'person-independent', 'chia theo người', 'cross-validation', 'subject', 'groupkfold', 'group'],
      maxPoints: 2,
      passFeedback: 'Pipeline chặt chẽ từ trích khung hình/keypoints -> temporal model -> head phân loại 50 lớp; đặc biệt lưu ý chia train/val theo người (GroupKFold / person-independent) chống rò rỉ dữ liệu.',
      failFeedback: 'Pipeline còn thiếu hoặc chưa nhấn mạnh việc chia tập kiểm thử theo người quay (person-independent split / GroupKFold theo subject).'
    },
    {
      keywords: ['f1', 'macro-f1', 'macro f1', 'accuracy', 'chính xác', 'confusion matrix', 'ma trận nhầm lẫn', 'nhầm lẫn'],
      maxPoints: 2,
      passFeedback: 'Sử dụng đúng metric phân loại clip đa lớp: Macro-F1 (chuẩn theo đề SOLOAI) và Confusion Matrix thay vì chỉ dùng accuracy frame rời rạc.',
      failFeedback: 'Bài toán phân loại 50 cử chỉ độc lập cần dùng Macro-F1 (đánh giá cân bằng các lớp) và Confusion Matrix để phân tích nhầm lẫn.'
    },
    {
      keywords: ['pretrain', 'tổng hợp', 'synthetic', 'augment', 'pseudo-label', 'ensemble', 'distill', 'chưng cất', 'quantization', 'keypoints'],
      maxPoints: 2,
      passFeedback: 'Đề xuất phương án cải tiến thực tiễn: Pretrain/Augmentation, Pseudo-labeling và Knowledge Distillation/Quantization cho thiết bị nhẹ.',
      failFeedback: 'Cần bổ sung thêm ít nhất 2 giải pháp cải tiến thực tế (như kiến trúc nén Distillation để chạy real-time hoặc Augmentation đa dạng nền).'
    }
  ],
  'OLP01-E02': [
    {
      keywords: ['lệch độ dài', 'chiều dài', 'chuyên ngành', 'thương mại', 'số lượng', 'tiền tệ', 'currency', 'bpe', 'từ điển', 'token'],
      maxPoints: 2,
      passFeedback: 'Phân tích sắc bén đặc thù song ngữ Trung-Việt: ngữ pháp, lệch độ dài, từ ngữ thương mại và bảo toàn số/tiền tệ.',
      failFeedback: 'Cần phân tích sâu hơn vấn đề từ vựng chuyên ngành thương mại điện tử và bảo tồn thực thể số/tiền tệ.'
    },
    {
      keywords: ['transformer', 'seq2seq', 'attention', 'encoder-decoder', 'from scratch', 'từ đầu', 'cấm pretrained', 'không dùng pretrained', 'scratch'],
      maxPoints: 2,
      passFeedback: 'Lựa chọn kiến trúc Transformer Encoder-Decoder chuẩn xác và tuân thủ quy chế cấm mô hình pre-trained MT của đề gốc (huấn luyện from scratch).',
      failFeedback: 'Cần làm rõ kiến trúc Transformer Encoder-Decoder (Vaswani et al.) huấn luyện từ đầu (from scratch) theo đúng quy chế cấm mô hình pre-trained của đề bài.'
    },
    {
      keywords: ['bpe', 'subword', 'sentencepiece', 'beam search', 'label smoothing', 'tokenize', 'leakage', 'miền'],
      maxPoints: 2,
      passFeedback: 'Pipeline hoàn chỉnh: BPE/SentencePiece chung, Beam Search giải mã, Label Smoothing và phân chia validation theo phân khúc miền.',
      failFeedback: 'Chưa làm rõ kỹ thuật tách từ con (BPE/SentencePiece) hoặc chiến thuật giải mã Beam Search.'
    },
    {
      keywords: ['sacrebleu', 'bleu', 'chrf', 'comet', 'human eval', 'đánh giá người', 'độ dài', 'length penalty', 'brevity penalty'],
      maxPoints: 2,
      passFeedback: 'Sử dụng SacreBLEU chuẩn mực (tránh sai lệch tokenizer, tính Brevity Penalty) kết hợp kiểm tra tính toàn vẹn số lượng/tiền tệ.',
      failFeedback: 'Cần nêu rõ việc dùng SacreBLEU chuẩn hóa và bổ sung đánh giá định tính/đánh giá người cho các câu phức tạp.'
    },
    {
      keywords: ['back-translation', 'dịch ngược', 'ensemble', 'rerank', 'post-edit', 'quy tắc số', 'checkpoint'],
      maxPoints: 2,
      passFeedback: 'Có giải pháp cải tiến chất lượng cao: Back-translation tạo dữ liệu song ngữ nhân tạo, Reranking/Ensemble và post-editing cho số tiền.',
      failFeedback: 'Cần đề xuất kỹ thuật mở rộng dữ liệu hợp lệ như Dịch ngược (Back-translation), Ensemble nhiều checkpoint hoặc Reranking giả thuyết tốt nhất.'
    }
  ],
  'OLP01-E03': [
    {
      keywords: ['ngoài đồng', 'nhiễu nền', 'ánh sáng', 'lá', 'khoanh vùng', 'localization', 'vùng bệnh', 'lệch lớp', 'bệnh hiếm'],
      maxPoints: 2,
      passFeedback: 'Nhận thức chính xác bài toán Object Detection (cần định vị vùng bệnh) chứ không đơn thuần là Classification, chỉ rõ hiện tượng lệch lớp.',
      failFeedback: 'Cần phân biệt rõ việc phải phát hiện tọa độ/vị trí tổn thương (Detection) và hiện tượng mất cân bằng lớp ở bệnh hiếm.'
    },
    {
      keywords: ['yolo', 'rt-detr', 'faster r-cnn', 'ssd', 'efficientdet', '1-stage', '2-stage', 'edge', 'di động', 'mobile'],
      maxPoints: 2,
      passFeedback: 'Lựa chọn bộ phát hiện 1-stage (YOLO/RT-DETR) hợp lý với ràng buộc triển khai trên thiết bị di động của nông dân.',
      failFeedback: 'Chưa lý giải rõ ràng việc chọn mô hình 1-stage hay 2-stage dựa trên cán cân độ trễ di động vs độ chính xác.'
    },
    {
      keywords: ['augment', 'mosaic', 'nms', 'iou', 'crop', 'leakage', 'ruộng', 'ngày chụp', 'split'],
      maxPoints: 2,
      passFeedback: 'Pipeline chi tiết: Augmentation thực địa, NMS hậu xử lý, và chia fold theo luống ruộng/ngày chụp để chống rò rỉ dữ liệu.',
      failFeedback: 'Thiếu khâu chống rò rỉ dữ liệu (chia fold theo vườn/ruộng) hoặc khâu khử trùng lặp NMS.'
    },
    {
      keywords: ['map', 'map@0.5', 'map@0.5:0.95', 'precision', 'recall', 'f1', 'lớp hiếm'],
      maxPoints: 2,
      passFeedback: 'Sử dụng hệ metric chuẩn mAP@0.5 và mAP@0.5:0.95 kèm theo chỉ số Recall/Precision riêng cho 2 loại bệnh hiếm.',
      failFeedback: 'Tuyệt đối tránh dùng Accuracy đơn giản cho bài toán Detection; cần nêu mAP@0.5 và phân tích lớp thiểu số.'
    },
    {
      keywords: ['focal loss', 'class weights', 'tổng hợp', 'tta', 'quantize', 'onnx', 'tflite', 'distillation'],
      maxPoints: 2,
      passFeedback: 'Có phương án đặc trị mất cân bằng (Focal Loss / Class Weights) và nén mô hình sang TFLite/ONNX để suy luận mượt trên điện thoại.',
      failFeedback: 'Cần bổ sung giải pháp xử lý mất cân bằng lớp (như Focal Loss) và tối ưu hóa suy luận nhẹ trên smartphone.'
    }
  ],
  'OLP01-E04': [
    {
      keywords: ['dữ liệu bảng', 'tabular', '8%', 'lệch', 'imbalance', 'giải thích', 'explainable', 'xai', 'phòng đào tạo', 'can thiệp'],
      maxPoints: 2,
      passFeedback: 'Nắm chắc bản chất dữ liệu bảng, tỷ lệ mất cân bằng nghiêm trọng (8%) và yêu cầu bắt buộc về tính minh bạch/giải thích được cho nhà quản lý.',
      failFeedback: 'Chưa nhấn mạnh tỷ lệ lệch lớp 8% và tính giải thích được (Explainability) phục vụ can thiệp sớm.'
    },
    {
      keywords: ['xgboost', 'lightgbm', 'catboost', 'random forest', 'gradient boosting', 'logistic', 'baseline', 'bảng'],
      maxPoints: 2,
      passFeedback: 'Lựa chọn GBDT (XGBoost/LightGBM) làm chủ đạo kết hợp Logistic Regression làm baseline; tránh lạm dụng Deep Learning không phù hợp với dữ liệu bảng nhỏ.',
      failFeedback: 'Thiếu mô hình baseline so sánh hoặc chưa giải thích tại sao Tree-based Boosting vượt trội Deep Learning trên dữ liệu bảng dạng này.'
    },
    {
      keywords: ['missing', 'outlier', 'encoding', 'smote', 'class weight', 'scale', 'stratified', 'k-fold'],
      maxPoints: 2,
      passFeedback: 'Quy trình xử lý dữ liệu bảng chuẩn: khuyết thiếu, mã hóa danh mục, kiểm soát mất cân bằng bằng Class Weights/SMOTE và Stratified K-Fold.',
      failFeedback: 'Cần mô tả đầy đủ các bước tiền xử lý đặc trưng bảng (Imputation, Encoding) và kỹ thuật phân tầng Stratified K-Fold.'
    },
    {
      keywords: ['pr-auc', 'roc-auc', 'f1', 'ngưỡng', 'threshold', 'precision', 'recall', 'chi phí', 'cost'],
      maxPoints: 2,
      passFeedback: 'Đề xuất đúng metric PR-AUC và F1-score tối ưu theo ngưỡng ra quyết định, phân tích bài toán chi phí giữa can thiệp sót và can thiệp nhầm.',
      failFeedback: 'Cần dùng PR-AUC/F1 thay cho Accuracy, và làm rõ việc điều chỉnh ngưỡng xác suất quyết định (decision threshold).'
    },
    {
      keywords: ['shap', 'lime', 'feature importance', 'drift', 'a/b', 'giám sát', 'theo dõi', 'cảnh báo sớm'],
      maxPoints: 2,
      passFeedback: 'Ý tưởng ứng dụng thực tế xuất sắc: sử dụng SHAP value để chỉ rõ nguyên nhân cho từng sinh viên, thiết lập hệ thống giám sát Data Drift theo kỳ.',
      failFeedback: 'Cần nêu rõ công cụ giải thích mô hình cụ thể (SHAP/LIME) để phòng đào tạo biết nguyên nhân hành động.'
    }
  ],
  'OLP01-BC1': [
    {
      keywords: ['tp', 'fp', 'fn', 'confusion', 'ma trận', 'nhầm lẫn'],
      maxPoints: 2.5,
      passFeedback: 'Trích xuất chính xác TP, FP, FN từ ma trận nhầm lẫn hoặc so sánh mảng vector.',
      failFeedback: 'Cần chỉ rõ cách tính hoặc trích xuất TP, FP, FN (ví dụ: cm[1,1], cm[0,1], cm[1,0]).'
    },
    {
      keywords: ['precision', 'recall', 'f1', 'chia cho 0', 'zero', 'eps', '0.0'],
      maxPoints: 2.5,
      passFeedback: 'Công thức Precision, Recall, F1 chính xác và có xử lý trường hợp ngoại lệ chia cho 0 (ZeroDivision).',
      failFeedback: 'Thiếu công thức tính đầy đủ hoặc quên xử lý trường hợp mẫu số bằng 0 (khi TP+FP=0 hoặc P+R=0).'
    },
    {
      keywords: ['lệch lớp', 'accuracy', 'imbalance', 'đánh lừa', 'thiểu số', 'ngộ nhận'],
      maxPoints: 2,
      passFeedback: 'Giải thích thấu đáo vì sao Accuracy gây hiểu lầm nghiêm trọng trên phân phối dữ liệu bị lệch lớp.',
      failFeedback: 'Chưa giải thích rõ nhược điểm của Accuracy khi một lớp chiếm đại đa số (ví dụ dự đoán toàn bộ âm tính vẫn đạt accuracy cao).'
    }
  ],
  'OLP01-BC2': [
    {
      keywords: ['zero_grad', 'backward', 'step', 'thứ tự'],
      maxPoints: 3,
      passFeedback: 'Thực hiện đúng chuẩn chu trình PyTorch: zero_grad() -> forward -> backward() -> step().',
      failFeedback: 'Sai thứ tự các hàm hoặc gọi thiếu một trong ba hàm cốt lõi: zero_grad, backward, step.'
    },
    {
      keywords: ['loss.backward', 'optimizer.step', 'optimizer.zero_grad', 'criterion', 'loader'],
      maxPoints: 2,
      passFeedback: 'Bố cục cú pháp chuẩn xác trong vòng lặp mini-batch và tính toán hàm mất mát.',
      failFeedback: 'Cần thể hiện đầy đủ vòng lặp for batch, tính toán loss = criterion(out, y).'
    },
    {
      keywords: ['cộng dồn', 'accumulate', 'tích lũy', 'gradient', 'đạo hàm', 'xóa'],
      maxPoints: 2,
      passFeedback: 'Giải thích chuẩn xác cơ chế PyTorch mặc định cộng dồn gradient nên bắt buộc phải reset zero_grad trước backward.',
      failFeedback: 'Chưa giải thích được nguyên nhân gốc rễ (PyTorch tự động cộng dồn tensor gradient ở thuộc tính .grad).'
    }
  ]
};

/**
 * Đánh giá bài làm mở (essay hoặc code) theo rubric
 */
export function evaluateOpenAnswer(question: Question, text: string): EvaluationResult {
  const isCode = question.type === 'code';
  const openQ = question as OpenQuestion;
  const maxScore = question.points || 10;
  const trimmed = (text || '').trim();

  // Nếu bài làm quá ngắn hoặc rỗng
  if (trimmed.length < 15) {
    const emptyBreakdown: RubricEvaluationItem[] = (openQ.rubric || []).map((rubricItem) => ({
      criterion: rubricItem,
      maxPoints: Number((maxScore / Math.max(1, openQ.rubric.length)).toFixed(1)),
      earnedPoints: 0,
      pass: false,
      feedback: 'Chưa có nội dung trình bày cho tiêu chí này.'
    }));

    return {
      score: 0,
      maxScore,
      percentage: 0,
      level: 'Chưa đạt',
      summary: 'Bài làm hiện đang để trống hoặc quá ngắn. Hãy bắt đầu trình bày lời giải của bạn theo khung cấu trúc chuẩn.',
      breakdown: emptyBreakdown,
      improvementTips: [
        'Sử dụng nút "Nạp khung mẫu 5 bước" để có sườn bài chuẩn chỉnh.',
        'Mỗi bước nên viết ít nhất 2-3 gạch đầu dòng phân tích kỹ thuật cụ thể.',
        'Tránh viết quá vắn tắt; hãy gọi tên chính xác các thuật toán, kiến trúc và hàm mất mát.'
      ]
    };
  }

  const normalizedText = trimmed.toLowerCase();
  const rules = QUESTION_RULES[question.id];

  const breakdown: RubricEvaluationItem[] = [];
  let totalEarned = 0;

  if (rules && rules.length > 0) {
    rules.forEach((rule, idx) => {
      const criterionName = openQ.rubric?.[idx] || `Tiêu chí ${idx + 1}`;
      
      // Đếm số từ khóa match
      let matchCount = 0;
      for (const kw of rule.keywords) {
        if (normalizedText.includes(kw.toLowerCase())) {
          matchCount++;
        }
      }

      let pass = false;
      let earned = 0;

      if (matchCount >= 3 || (matchCount >= 2 && trimmed.length > 250)) {
        pass = true;
        earned = rule.maxPoints;
      } else if (matchCount >= 1) {
        pass = false;
        earned = Number((rule.maxPoints * 0.5).toFixed(1));
      } else {
        pass = false;
        earned = 0;
      }

      totalEarned += earned;
      breakdown.push({
        criterion: criterionName,
        maxPoints: rule.maxPoints,
        earnedPoints: earned,
        pass,
        feedback: pass ? rule.passFeedback : rule.failFeedback
      });
    });
  } else {
    // Thuật toán heuristic tổng quát cho các câu hỏi khác
    const rubricList = openQ.rubric || ['Nêu phương pháp luận', 'Giải thích chi tiết', 'Biện pháp đánh giá'];
    const ptsPerCriterion = Number((maxScore / rubricList.length).toFixed(1));

    rubricList.forEach((criterion) => {
      // Tách từ khóa quan trọng từ câu rubric
      const words = criterion.split(/\s+/).filter((w) => w.length > 3);
      let matched = 0;
      for (const w of words) {
        if (normalizedText.includes(w.toLowerCase())) matched++;
      }
      const ratio = words.length > 0 ? matched / words.length : 0;

      let pass = false;
      let earned = 0;
      if (ratio >= 0.25 || (ratio >= 0.15 && trimmed.length > 300)) {
        pass = true;
        earned = ptsPerCriterion;
      } else if (matched > 0) {
        pass = false;
        earned = Number((ptsPerCriterion * 0.4).toFixed(1));
      } else {
        pass = false;
        earned = 0;
      }

      totalEarned += earned;
      breakdown.push({
        criterion,
        maxPoints: ptsPerCriterion,
        earnedPoints: earned,
        pass,
        feedback: pass
          ? 'Bài làm đã đề cập thỏa đáng nội dung yêu cầu.'
          : 'Cần phân tích cụ thể hơn các luận điểm liên quan đến tiêu chí này.'
      });
    });
  }

  // Chuẩn hóa điểm không vượt quá maxScore
  const finalScore = Math.min(maxScore, Math.max(0, Math.round(totalEarned * 10) / 10));
  const percentage = Math.round((finalScore / maxScore) * 100);

  let level: EvaluationResult['level'] = 'Chưa đạt';
  if (percentage >= 85) level = 'Xuất sắc';
  else if (percentage >= 65) level = 'Đạt yêu cầu';
  else if (percentage >= 40) level = 'Cần hoàn thiện';

  // Tổng hợp nhận xét và mẹo cải tiến
  const failedItems = breakdown.filter((b) => !b.pass);
  const passedItems = breakdown.filter((b) => b.pass);

  let summary = '';
  if (level === 'Xuất sắc') {
    summary = `Bài giải rất chất lượng (${finalScore}/${maxScore} điểm)! Bạn đã nắm vững bản chất bài toán, lập luận logic và đề xuất giải pháp có tính khả thi cao trong thực tế thi đấu.`;
  } else if (level === 'Đạt yêu cầu') {
    summary = `Bài làm khá tốt (${finalScore}/${maxScore} điểm), đáp ứng được phần lớn cấu trúc cốt lõi. Cần bổ sung thêm một số chi tiết kỹ thuật chuyên sâu để đạt điểm tuyệt đối.`;
  } else if (level === 'Cần hoàn thiện') {
    summary = `Bài làm mới chỉ phác thảo ý tưởng cơ bản (${finalScore}/${maxScore} điểm). Một số tiêu chí quan trọng về pipeline, xử lý rò rỉ dữ liệu hoặc metric đánh giá còn mờ nhạt.`;
  } else {
    summary = `Bài làm chưa đạt yêu cầu (${finalScore}/${maxScore} điểm). Bạn cần bám sát hơn vào khung cấu trúc và nêu tên các kỹ thuật AI cụ thể thay vì viết khái quát.`;
  }

  const improvementTips: string[] = [];
  if (failedItems.length > 0) {
    failedItems.forEach((f) => {
      improvementTips.push(f.feedback);
    });
  } else {
    improvementTips.push('Bài giải đã rất đầy đủ. Bạn có thể mở rộng thêm phần phân tích đánh giá độ phức tạp tính toán (FLOPs/FPS) hoặc phân tích các edge case ngoại lệ.');
  }

  if (!isCode && trimmed.length < 350) {
    improvementTips.push('Độ dài bài tự luận còn khá ngắn. Nên mở rộng giải thích "vì sao lại chọn giải pháp đó" để thuyết phục giám khảo chấm thi.');
  }

  return {
    score: finalScore,
    maxScore,
    percentage,
    level,
    summary,
    breakdown,
    improvementTips
  };
}

/**
 * Trả lời câu hỏi Socratic của gia sư AI
 */
export function getSocraticAdvice(question: Question, userQuery: string): string {
  const query = userQuery.toLowerCase();
  const prompt = question.prompt;

  if (query.includes('5 bước') || query.includes('khung') || query.includes('cấu trúc')) {
    return `### Khung 5 bước giải bài toán AI chuẩn Olympic:
1. **Phân tích dữ liệu & Bài toán**: Xác định đặc thù input/output, tỷ lệ lệch lớp, kích thước dữ liệu, ràng buộc thời gian/phần cứng.
2. **Lựa chọn mô hình & Luận giải**: Đưa ra mô hình baseline đơn giản trước, sau đó đề xuất mô hình nâng cao và lý giải vì sao chọn nó.
3. **Pipeline xử lý toàn diện**: Tiền xử lý, augment, chiến lược chia tập train/val/test (chống data leakage), giải mã/hậu xử lý.
4. **Metric đánh giá chuẩn xác**: Chọn đúng metric chuyên biệt cho bài toán (không dùng accuracy bừa bãi khi lệch lớp), giải thích lý do.
5. **Đề xuất cải tiến & Thực tiễn**: Pre-training, Transfer Learning, Ensemble, nén mô hình (Quantization/Distillation), xử lý edge case.`;
  }

  if (query.includes('gợi ý') || query.includes('cách giải') || query.includes('hint')) {
    if (question.type === 'essay') {
      const openQ = question as OpenQuestion;
      const rubrics = openQ.rubric.map((r, i) => `${i + 1}. ${r}`).join('\n');
      return `**Gợi ý định hướng cho câu này:**\nBài toán này kiểm tra năng lực thiết kế giải pháp thực tế. Hãy đảm bảo bạn trả lời được các trọng tâm sau:\n${rubrics}\n\n*Mẹo nhỏ:* Hãy bắt đầu bằng cách xác định rõ các ràng buộc kỹ thuật trong đề bài (ví dụ: chạy trên thiết bị nào, dữ liệu lệch ra sao).`;
    }
    if (question.type === 'code') {
      return `**Gợi ý code:**\n- Nhớ kiểm tra trường hợp mẫu số bằng 0.\n- Viết hàm theo phong cách vectorized của NumPy để tối ưu tốc độ.\n- Nếu là PyTorch, nhớ thứ tự bất di bất dịch: \`optimizer.zero_grad()\` -> \`loss.backward()\` -> \`optimizer.step()\`.`;
    }
  }

  if (query.includes('công thức') || query.includes('toán') || query.includes('latex')) {
    if (question.id === 'OLP01-BC1') {
      return `### Các công thức đánh giá phân loại:
- **Precision**: $P = \\frac{TP}{TP + FP}$
- **Recall**: $R = \\frac{TP}{TP + FN}$
- **F1-Score**: $F_1 = \\frac{2 \\times P \\times R}{P + R} = \\frac{2TP}{2TP + FP + FN}$`;
    }
    if (question.id.includes('A01') || prompt.includes('xác suất')) {
      return `### Công thức Bayes:
$$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)} = \\frac{P(B|A) \\cdot P(A)}{P(B|A)P(A) + P(B|\\neg A)P(\\neg A)}$$`;
    }
    return `Bạn có thể dùng cú pháp KaTeX: kẹp giữa hai dấu \`$\` cho inline (ví dụ \`$x^2$\`) hoặc \`$$\` cho công thức riêng một dòng.`;
  }

  if (query.includes('leakage') || query.includes('rò rỉ')) {
    return `### Chống rò rỉ dữ liệu (Data Leakage):
- Với bài toán theo người/chủ thể (như nhận diện ngôn ngữ ký hiệu): Phải chia fold theo **ID người quay** (person-independent split), không được để cùng 1 người vừa xuất hiện ở train vừa xuất hiện ở val.
- Với bài toán chụp ảnh thực địa: Chia fold theo **ruộng/ngày chụp**.
- Với bài toán bảng: Thực hiện chuẩn hóa (StandardScaler) và SMOTE **bên trong từng fold** của Cross-Validation, không thực hiện trên toàn bộ dataset trước khi chia!`;
  }

  // Phản hồi ngữ cảnh thông minh mặc định
  return `Chào bạn! Tôi là Trợ lý AI Olympic. Về câu hỏi "${question.id}":\n\nBạn đang gặp khó khăn ở phần nào nhất?\n- 💡 Gõ "gợi ý" để nhận định hướng giải quyết.\n- 📐 Gõ "công thức" để xem biểu thức toán học liên quan.\n- 📋 Gõ "5 bước" để xem cấu trúc bài tự luận chuẩn điểm cao.\n\nNgoài ra, bạn có thể tự tin viết bài làm ở khung soạn thảo bên trái và bấm **"AI Chấm Bài"** để tôi nhận xét chi tiết từng tiêu chí nhé!`;
}
