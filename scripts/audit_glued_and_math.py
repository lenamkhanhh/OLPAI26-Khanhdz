import json
import re

exams = ['olp-01', 'olp-02', 'olp-03', 'olp-04', 'olp-05', 'voai-2025']

# 1. Sửa 4 từ dính chữ OCR
fixed_count = 0
for exam_id in exams:
    path = f'src/data/exams/{exam_id}.json'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    # Sửa các từ dính chữ cụ thể đã phát hiện
    replacements = [
        ('Độchính xác', 'Độ chính xác'),
        ('độchính xác', 'độ chính xác'),
        ('độlệch (bias)', 'độ lệch (bias)'),
        ('sẽdự đoán độlệch', 'sẽ dự đoán độ lệch'),
        ('độlệch (offset)', 'độ lệch (offset)')
    ]
    for old, new in replacements:
        if old in new_content:
            new_content = new_content.replace(old, new)
            fixed_count += 1
            print(f"Fixed '{old}' -> '{new}' in {exam_id}")
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Total glued word fixes applied: {fixed_count}")

# 2. Kiểm tra lại toàn bộ từ dính chữ sau khi sửa
VN_CHARS = r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]'
remaining_glued = []

OCR_PATTERNS = [
    r'đểlưu', r'sẽtự', r'độchính', r'trởthành', r'cắtghép', r'đượctạo',
    r'phépnhân', r'tínhchất', r'môtả', r'trọngsố', r'họcsâu', r'mạngnơ',
    r'bảnchất', r'khoảngcách', r'hàmmất', r'quầnthể', r'phânphối',
    r'khônggian', r'kếtquả', r'xácliệu', r'xácsuất', r'độlệch',
    r'tươngquan', r'chuẩnhoá', r'chuẩnhóa', r'hộitụ', r'đạohàm'
]

for exam_id in exams:
    with open(f'src/data/exams/{exam_id}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data['questions']:
        texts = [q['prompt'], q.get('explanation', '')] + [o['text'] for o in q.get('options', [])]
        for t in texts:
            for p in OCR_PATTERNS:
                m = re.search(p, t, re.IGNORECASE)
                if m:
                    remaining_glued.append((exam_id, q['id'], m.group(0), t[max(0, m.start()-10):m.end()+15]))

print(f"Remaining true OCR glued words: {len(remaining_glued)}")
if remaining_glued:
    print(remaining_glued)
