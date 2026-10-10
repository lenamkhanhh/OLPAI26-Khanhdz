# -*- coding: utf-8 -*-
"""
Exam Management Router (Data-Agnostic):
List, fetch, and import exams dynamically for any competition or test.
"""

import json
import sqlite3
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from backend.database import get_db
from backend.auth import get_optional_user, get_current_user
from backend.schemas import ExamSummary, ExamDetail, ExamImportRequest

router = APIRouter(prefix="/api/exams", tags=["Exams Management"])

@router.get("", response_model=List[ExamSummary])
def list_exams(conn: sqlite3.Connection = Depends(get_db)):
    """List all available exams and competitions."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, description, category, duration_minutes, total_points, total_questions, updated_at
        FROM exams
        ORDER BY id ASC;
    """)
    rows = cursor.fetchall()
    return [ExamSummary(**dict(r)) for r in rows]

@router.get("/{exam_id}", response_model=ExamDetail)
def get_exam(exam_id: str, conn: sqlite3.Connection = Depends(get_db)):
    """Get full exam content with questions and metadata."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, description, category, duration_minutes, total_points, total_questions, updated_at, data_json
        FROM exams
        WHERE id = ?;
    """, (exam_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Đề thi '{exam_id}' không tồn tại trong hệ thống."
        )

    data = dict(row)
    full_data = json.loads(data["data_json"])
    return ExamDetail(
        id=data["id"],
        title=data["title"],
        description=data["description"],
        category=data["category"],
        duration_minutes=data["duration_minutes"],
        total_points=data["total_points"],
        total_questions=data["total_questions"],
        updated_at=data["updated_at"],
        questions=full_data.get("questions", []),
        modules=full_data.get("modules", None)
    )

@router.post("/import", response_model=ExamSummary, status_code=status.HTTP_201_CREATED)
def import_exam(payload: ExamImportRequest, conn: sqlite3.Connection = Depends(get_db)):
    """
    Import or replace an exam from a generic JSON format.
    Allows reusing the platform for ANY future competition (ICPC, VOI, Final Exams, etc.).
    """
    total_pts = sum(q.get("points", 1.0) for q in payload.questions)
    total_qs = len(payload.questions)
    data_dict = {
        "id": payload.id,
        "title": payload.title,
        "description": payload.description,
        "durationMinutes": payload.duration_minutes,
        "totalPoints": total_pts,
        "questions": payload.questions
    }

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO exams (id, title, description, category, duration_minutes, total_points, total_questions, data_json, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(id) DO UPDATE SET
            title = excluded.title,
            description = excluded.description,
            category = excluded.category,
            duration_minutes = excluded.duration_minutes,
            total_points = excluded.total_points,
            total_questions = excluded.total_questions,
            data_json = excluded.data_json,
            updated_at = CURRENT_TIMESTAMP;
    """, (
        payload.id,
        payload.title,
        payload.description or "",
        payload.category or "Olympic AI / Competitive Examination",
        payload.duration_minutes or 90,
        total_pts,
        total_qs,
        json.dumps(data_dict, ensure_ascii=False)
    ))
    conn.commit()

    cursor.execute("SELECT id, title, description, category, duration_minutes, total_points, total_questions, updated_at FROM exams WHERE id = ?;", (payload.id,))
    row = dict(cursor.fetchone())
    return ExamSummary(**row)

@router.delete("/{exam_id}", status_code=status.HTTP_200_OK)
def delete_exam(exam_id: str, current_user: dict = Depends(get_current_user), conn: sqlite3.Connection = Depends(get_db)):
    """Delete an exam (Admin only)."""
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Chỉ quản trị viên mới có quyền xóa đề thi.")

    cursor = conn.cursor()
    cursor.execute("DELETE FROM exams WHERE id = ?;", (exam_id,))
    conn.commit()
    return {"message": f"Đã xóa thành công đề thi '{exam_id}'."}
