# -*- coding: utf-8 -*-
"""
Submissions & Grading Router:
Automated evaluation engine, score calculation, submission persistence, and history review.
"""

import json
import sqlite3
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from backend.database import get_db
from backend.auth import get_current_user
from backend.schemas import SubmissionRequest, SubmissionResult, SubmissionHistoryItem, VerdictDetail

router = APIRouter(prefix="/api/submissions", tags=["Submissions & Evaluation Engine"])

@router.post("", response_model=SubmissionResult, status_code=status.HTTP_201_CREATED)
def submit_exam(
    payload: SubmissionRequest,
    current_user: dict = Depends(get_current_user),
    conn: sqlite3.Connection = Depends(get_db)
):
    """
    Submit an exam for automated grading.
    Evaluates MCQ answers server-side, calculates score, and stores history.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, total_points, data_json FROM exams WHERE id = ?;", (payload.exam_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Đề thi '{payload.exam_id}' không tồn tại."
        )

    exam_dict = dict(row)
    exam_data = json.loads(exam_dict["data_json"])
    questions = exam_data.get("questions", [])

    total_questions = len(questions)
    max_score = sum(q.get("points", 1.0) for q in questions)
    
    graded_score = 0.0
    essay_score = 0.0
    correct_count = 0
    breakdown: List[VerdictDetail] = []

    user_answers = payload.answers or {}

    for q in questions:
        qid = q["id"]
        q_type = q.get("type", "multiple-choice")
        q_max_pts = float(q.get("points", 1.0))
        q_ans_key = q.get("answer")
        ans_payload = user_answers.get(qid)

        if q_type == "essay":
            self_pts = float(ans_payload.selfScore if (ans_payload and ans_payload.selfScore is not None) else 0.0)
            self_pts = min(self_pts, q_max_pts)
            essay_score += self_pts
            breakdown.append(VerdictDetail(
                question_id=qid,
                verdict="ESSAY_SELF",
                earned_points=self_pts,
                max_points=q_max_pts,
                user_answer=ans_payload.text if ans_payload else None
            ))
        elif q_type == "code":
            code_pts = float(ans_payload.selfScore if (ans_payload and ans_payload.selfScore is not None) else 0.0)
            code_pts = min(code_pts, q_max_pts)
            graded_score += code_pts
            verdict = "AC" if code_pts == q_max_pts else ("PARTIAL" if code_pts > 0 else "WA")
            if verdict == "AC":
                correct_count += 1
            breakdown.append(VerdictDetail(
                question_id=qid,
                verdict=verdict,
                earned_points=code_pts,
                max_points=q_max_pts,
                user_answer=ans_payload.code if ans_payload else None
            ))
        else:
            # Multiple Choice Question
            user_choice = ans_payload.selected if ans_payload else None
            if user_choice and str(user_choice).strip().upper() == str(q_ans_key).strip().upper():
                graded_score += q_max_pts
                correct_count += 1
                breakdown.append(VerdictDetail(
                    question_id=qid,
                    verdict="AC",
                    earned_points=q_max_pts,
                    max_points=q_max_pts,
                    correct_answer=q_ans_key,
                    user_answer=user_choice
                ))
            else:
                breakdown.append(VerdictDetail(
                    question_id=qid,
                    verdict="WA",
                    earned_points=0.0,
                    max_points=q_max_pts,
                    correct_answer=q_ans_key,
                    user_answer=user_choice
                ))

    final_score = round(graded_score + essay_score, 2)
    accuracy_pct = round((correct_count / total_questions) * 100, 1) if total_questions > 0 else 0.0

    # Store in database
    cursor.execute("""
        INSERT INTO submissions (
            user_id, exam_id, score, max_score, graded_score, essay_score,
            correct_count, total_questions, time_spent_seconds, answers_json, breakdown_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        current_user["id"],
        payload.exam_id,
        final_score,
        max_score,
        graded_score,
        essay_score,
        correct_count,
        total_questions,
        payload.time_spent_seconds,
        json.dumps({k: v.dict() for k, v in user_answers.items()}, ensure_ascii=False),
        json.dumps([b.dict() for b in breakdown], ensure_ascii=False)
    ))
    submission_id = cursor.lastrowid
    conn.commit()

    cursor.execute("SELECT submitted_at FROM submissions WHERE id = ?;", (submission_id,))
    submitted_at = cursor.fetchone()["submitted_at"]

    return SubmissionResult(
        submission_id=submission_id,
        exam_id=payload.exam_id,
        score=final_score,
        max_score=max_score,
        graded_score=round(graded_score, 2),
        essay_score=round(essay_score, 2),
        correct_count=correct_count,
        total_questions=total_questions,
        accuracy_percentage=accuracy_pct,
        time_spent_seconds=payload.time_spent_seconds,
        submitted_at=submitted_at,
        breakdown=breakdown
    )

@router.get("/my-history", response_model=List[SubmissionHistoryItem])
def get_my_submission_history(
    current_user: dict = Depends(get_current_user),
    conn: sqlite3.Connection = Depends(get_db)
):
    """Get all past exam submissions for currently authenticated student."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.id, s.exam_id, e.title as exam_title, s.score, s.max_score, s.correct_count,
               s.total_questions, s.time_spent_seconds, s.submitted_at
        FROM submissions s
        JOIN exams e ON s.exam_id = e.id
        WHERE s.user_id = ?
        ORDER BY s.submitted_at DESC;
    """, (current_user["id"],))
    rows = cursor.fetchall()
    return [SubmissionHistoryItem(**dict(r)) for r in rows]

@router.get("/{submission_id}", response_model=SubmissionResult)
def get_submission_detail(
    submission_id: int,
    current_user: dict = Depends(get_current_user),
    conn: sqlite3.Connection = Depends(get_db)
):
    """Get full details and breakdown of a specific submission."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, user_id, exam_id, score, max_score, graded_score, essay_score,
               correct_count, total_questions, time_spent_seconds, breakdown_json, submitted_at
        FROM submissions
        WHERE id = ?;
    """, (submission_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy bài nộp này.")

    item = dict(row)
    if item["user_id"] != current_user["id"] and current_user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Bạn không có quyền xem bài nộp của người khác.")

    breakdown_list = [VerdictDetail(**b) for b in json.loads(item["breakdown_json"])]
    acc_pct = round((item["correct_count"] / item["total_questions"]) * 100, 1) if item["total_questions"] > 0 else 0.0

    return SubmissionResult(
        submission_id=item["id"],
        exam_id=item["exam_id"],
        score=item["score"],
        max_score=item["max_score"],
        graded_score=item["graded_score"],
        essay_score=item["essay_score"],
        correct_count=item["correct_count"],
        total_questions=item["total_questions"],
        accuracy_percentage=acc_pct,
        time_spent_seconds=item["time_spent_seconds"],
        submitted_at=item["submitted_at"],
        breakdown=breakdown_list
    )
