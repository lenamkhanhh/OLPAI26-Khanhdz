# -*- coding: utf-8 -*-
"""
Database Seeder:
Automatically syncs all exam JSON files from src/data/exams/ into SQLite database,
and creates default test accounts for immediate demonstration.
"""

import json
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from backend.config import EXAMS_DIR, DB_PATH
from backend.database import get_connection, init_db
from backend.auth import hash_password

def seed_database() -> None:
    print("[Seed] Khởi tạo cơ sở dữ liệu SQLite...")
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Tạo tài khoản mẫu
    cursor.execute("SELECT id FROM users WHERE username = 'admin';")
    if not cursor.fetchone():
        pw_hash, salt = hash_password("hcmus2026")
        cursor.execute("""
            INSERT INTO users (username, display_name, team_name, role, password_hash, salt)
            VALUES ('admin', 'Quản Trị Viên OLP AI', 'HCMUS Ban Chuyên Môn', 'admin', ?, ?);
        """, (pw_hash, salt))
        print("  -> Đã tạo tài khoản quản trị: admin / hcmus2026")

    cursor.execute("SELECT id FROM users WHERE username = 'student';")
    if not cursor.fetchone():
        pw_hash, salt = hash_password("hcmus2026")
        cursor.execute("""
            INSERT INTO users (username, display_name, team_name, role, password_hash, salt)
            VALUES ('student', 'Thí Sinh OLP AI 2026', 'HCMUS AI Team 01', 'student', ?, ?);
        """, (pw_hash, salt))
        print("  -> Đã tạo tài khoản mẫu: student / hcmus2026")

    # 2. Quét và đồng bộ tất cả đề thi từ src/data/exams/
    if EXAMS_DIR.exists():
        exam_files = list(EXAMS_DIR.glob("*.json"))
        print(f"[Seed] Tìm thấy {len(exam_files)} file đề thi trong {EXAMS_DIR}")

        for ef in exam_files:
            try:
                with open(ef, "r", encoding="utf-8") as f:
                    exam_data = json.load(f)

                exam_id = exam_data.get("id") or ef.stem
                title = exam_data.get("title", f"Đề thi {exam_id.upper()}")
                desc = exam_data.get("description", "")
                dur = exam_data.get("durationMinutes", 90)
                questions = exam_data.get("questions", [])
                total_pts = sum(q.get("points", 1.0) for q in questions)
                total_qs = len(questions)

                cursor.execute("""
                    INSERT INTO exams (id, title, description, duration_minutes, total_points, total_questions, data_json, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(id) DO UPDATE SET
                        title = excluded.title,
                        description = excluded.description,
                        duration_minutes = excluded.duration_minutes,
                        total_points = excluded.total_points,
                        total_questions = excluded.total_questions,
                        data_json = excluded.data_json,
                        updated_at = CURRENT_TIMESTAMP;
                """, (
                    exam_id,
                    title,
                    desc,
                    dur,
                    total_pts,
                    total_qs,
                    json.dumps(exam_data, ensure_ascii=False)
                ))
                print(f"  -> Đồng bộ thành công: [{exam_id}] {title} ({total_qs} câu, {total_pts:.1f} điểm)")
            except Exception as e:
                print(f"  [!] Lỗi khi nạp file {ef.name}: {e}")

    conn.commit()
    conn.close()
    print("[Seed] Hoàn tất nạp dữ liệu E2E!")

if __name__ == "__main__":
    seed_database()
