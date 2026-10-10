import fs from 'fs';

// 1. Fix olp-05.json SKILL-CV-47
const olp05Path = 'src/data/exams/olp-05.json';
const d5 = JSON.parse(fs.readFileSync(olp05Path, 'utf8'));
const q47 = d5.questions.find(q => q.id === 'SKILL-CV-47');
if (q47) {
  q47.prompt = 'Giả sử một phép tích chập chuẩn có $C_{in} = 32$, $C_{out} = 64$, $\\text{kernel\\_size} = 3 \\times 3$. Tổng số tham số (không tính bias) là $3 \\times 3 \\times 32 \\times 64 = 18.432$. Nếu thay thế bằng kiến trúc Tích chập Tách rời theo Độ sâu (Depthwise Separable) của MobileNet, tổng số tham số (không bias) sẽ xấp xỉ là bao nhiêu?';
  fs.writeFileSync(olp05Path, JSON.stringify(d5, null, 2), 'utf8');
  console.log('Fixed SKILL-CV-47 in olp-05.json successfully!');
}

// 2. Fix olp-04.json OLP04-Q04 & Q19
const olp04Path = 'src/data/exams/olp-04.json';
const d4 = JSON.parse(fs.readFileSync(olp04Path, 'utf8'));
const q04 = d4.questions.find(q => q.id === 'OLP04-Q04');
if (q04) {
  q04.explanation = q04.explanation.replace(/1\.200\$s = 20 phút/g, '1.200\\text{ s} = 20\\text{ phút}');
  q04.explanation = q04.explanation.replace(/1\.200\$s/g, '1.200\\text{ s}');
}
const q19 = d4.questions.find(q => q.id === 'OLP04-Q19');
if (q19) {
  q19.explanation = q19.explanation.replace(/\$0\.05 \\times 3 = 0\.15\\text\{ s\}\$\$ s\$s \/ ảnh/g, '$0.05 \\times 3 = 0.15\\text{ s}$ / ảnh');
  q19.explanation = q19.explanation.replace(/\$2\.500 \\times 0\.15\$ s = 375\$ giây/g, '$2.500 \\times 0.15 = 375$ giây');
}
fs.writeFileSync(olp04Path, JSON.stringify(d4, null, 2), 'utf8');
console.log('Fixed OLP04-Q04 & Q19 successfully!');
