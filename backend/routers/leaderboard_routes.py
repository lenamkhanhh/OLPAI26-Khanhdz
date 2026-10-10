# -*- coding: utf-8 -*-
"""
Leaderboard and Global Analytics Router:
Rankings, hall of fame, and contest statistics.
"""

import sqlite3
from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from backend.database import get_db
from backend.schemas import LeaderboardEntry

router = APIRouter(prefix="/api/leaderboard", tags=["Leaderboard & Rankings"])

@router.get("", response_model=List[LeaderboardEntry])
def get_leaderboard(
    exam_id: Optional[str] = Query(None, description="Lọc theo mã đề thi cụ thể"),
    limit: int = Query(50, ge=1, le=100),
    conn: sqlite3.Connection = Depends(get_db)
):
    """Get competitive rankings / leaderboard."""
    cursor = conn.cursor()
    query = """
        SELECT s.user_id, u.username, u.display_name, u.team_name, s.exam_id,
               s.score, s.max_score, s.correct_count, s.total_questions,
               s.time_spent_seconds, s.submitted_at
        FROM submissions s
        JOIN users u ON s.user_id = u.id
    """
    params = []
    if exam_id:
        query += " WHERE s.exam_id = ?"
        params.append(exam_id)

    query += " ORDER BY s.score DESC, s.time_spent_seconds ASC, s.submitted_at ASC LIMIT ?;"
    params.append(limit)

    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()

    entries = []
    for idx, r in enumerate(rows, start=1):
        d = dict(r)
        acc_pct = round((d["correct_count"] / d["total_questions"]) * 100, 1) if d["total_questions"] > 0 else 0.0
        entries.append(LeaderboardEntry(
            rank=idx,
            user_id=d["user_id"],
            username=d["username"],
            display_name=d["display_name"],
            team_name=d["team_name"],
            exam_id=d["exam_id"],
            score=d["score"],
            max_score=d["max_score"],
            accuracy_percentage=acc_pct,
            time_spent_seconds=d["time_spent_seconds"],
            submitted_at=d["submitted_at"]
        ))
    return entries

@router.get("/summary")
def get_platform_summary(conn: sqlite3.Connection = Depends(get_db)):
    """Summary counts for arena stats banner."""
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as count FROM users;")
    total_users = cursor.fetchone()["count"]

    cursor.execute("SELECT COUNT(*) as count FROM exams;")
    total_exams = cursor.fetchone()["count"]

    cursor.execute("SELECT COUNT(*) as count, AVG(score) as avg_score FROM submissions;")
    sub_row = cursor.fetchone()
    total_subs = sub_row["count"]
    avg_score = round(sub_row["avg_score"] or 0.0, 1)

    return {
        "total_users": total_users,
        "total_exams": total_exams,
        "total_submissions": total_subs,
        "average_score": avg_score
    }
