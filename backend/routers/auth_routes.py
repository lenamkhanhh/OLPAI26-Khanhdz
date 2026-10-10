# -*- coding: utf-8 -*-
"""
Authentication router: Register, Login, Get Current User Profile.
"""

import sqlite3
from fastapi import APIRouter, Depends, HTTPException, status
from backend.database import get_db
from backend.auth import hash_password, verify_password, create_user_token, get_current_user
from backend.schemas import UserRegister, UserLogin, TokenResponse, UserResponse

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserRegister, conn: sqlite3.Connection = Depends(get_db)):
    """Register a new student/contestant account."""
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?;", (payload.username,))
    if cursor.fetchone():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tên đăng nhập này đã được sử dụng. Vui lòng chọn tên khác."
        )

    pw_hash, salt = hash_password(payload.password)
    cursor.execute(
        """
        INSERT INTO users (username, display_name, team_name, role, password_hash, salt)
        VALUES (?, ?, ?, 'student', ?, ?);
        """,
        (payload.username, payload.display_name, payload.team_name or "", pw_hash, salt)
    )
    user_id = cursor.lastrowid
    conn.commit()

    token = create_user_token(conn, user_id)
    cursor.execute("SELECT id, username, display_name, team_name, role, created_at FROM users WHERE id = ?;", (user_id,))
    user_row = dict(cursor.fetchone())

    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=UserResponse(**user_row)
    )

@router.post("/login", response_model=TokenResponse)
def login_user(payload: UserLogin, conn: sqlite3.Connection = Depends(get_db)):
    """Log in with username and password."""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, display_name, team_name, role, password_hash, salt, created_at FROM users WHERE username = ?;",
        (payload.username,)
    )
    row = cursor.fetchone()
    if not row:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tên đăng nhập hoặc mật khẩu không chính xác."
        )

    user = dict(row)
    if not verify_password(payload.password, user["password_hash"], user["salt"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tên đăng nhập hoặc mật khẩu không chính xác."
        )

    token = create_user_token(conn, user["id"])
    return TokenResponse(
        access_token=token,
        token_type="bearer",
        user=UserResponse(
            id=user["id"],
            username=user["username"],
            display_name=user["display_name"],
            team_name=user["team_name"],
            role=user["role"],
            created_at=user["created_at"]
        )
    )

@router.get("/me", response_model=UserResponse)
def get_me(current_user: dict = Depends(get_current_user)):
    """Get profile of current logged-in user."""
    return UserResponse(
        id=current_user["id"],
        username=current_user["username"],
        display_name=current_user["display_name"],
        team_name=current_user["team_name"],
        role=current_user["role"],
        created_at=current_user["created_at"]
    )
