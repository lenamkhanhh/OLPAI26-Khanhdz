# -*- coding: utf-8 -*-
"""
Pydantic data schemas for request validation and response formatting.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

# 1. User Schemas
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Tên đăng nhập duy nhất")
    password: str = Field(..., min_length=6, description="Mật khẩu tối thiểu 6 ký tự")
    display_name: str = Field(..., min_length=2, max_length=100, description="Họ và tên thí sinh")
    team_name: Optional[str] = Field(default="", max_length=100, description="Tên đội thi đấu / Lớp / Trường")

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    display_name: str
    team_name: str
    role: str
    created_at: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

# 2. Exam Schemas (Generic & Data-Agnostic)
class ExamSummary(BaseModel):
    id: str
    title: str
    description: str
    category: str
    duration_minutes: int
    total_points: float
    total_questions: int
    updated_at: str

class ExamDetail(ExamSummary):
    questions: List[Dict[str, Any]]
    modules: Optional[Dict[str, Any]] = None

class ExamImportRequest(BaseModel):
    id: str = Field(..., description="Mã định danh đề thi (vd: olp-06, icpc-2026, exam-midterm)")
    title: str = Field(..., description="Tiêu đề đề thi")
    description: Optional[str] = ""
    category: Optional[str] = "Olympic AI / Competitive Examination"
    duration_minutes: Optional[int] = 90
    questions: List[Dict[str, Any]]

# 3. Submission Schemas
class AnswerPayload(BaseModel):
    selected: Optional[str] = None
    text: Optional[str] = None
    code: Optional[str] = None
    selfScore: Optional[float] = None
    timestamp: Optional[str] = None

class SubmissionRequest(BaseModel):
    exam_id: str
    time_spent_seconds: int = 0
    answers: Dict[str, AnswerPayload]

class VerdictDetail(BaseModel):
    question_id: str
    verdict: str  # AC, WA, PARTIAL, ESSAY_SELF
    earned_points: float
    max_points: float
    correct_answer: Optional[str] = None
    user_answer: Optional[str] = None

class SubmissionResult(BaseModel):
    submission_id: int
    exam_id: str
    score: float
    max_score: float
    graded_score: float
    essay_score: float
    correct_count: int
    total_questions: int
    accuracy_percentage: float
    time_spent_seconds: int
    submitted_at: str
    breakdown: List[VerdictDetail]

class SubmissionHistoryItem(BaseModel):
    id: int
    exam_id: str
    exam_title: str
    score: float
    max_score: float
    correct_count: int
    total_questions: int
    time_spent_seconds: int
    submitted_at: str

# 4. Leaderboard Schemas
class LeaderboardEntry(BaseModel):
    rank: int
    user_id: int
    username: str
    display_name: str
    team_name: str
    exam_id: str
    score: float
    max_score: float
    accuracy_percentage: float
    time_spent_seconds: int
    submitted_at: str
