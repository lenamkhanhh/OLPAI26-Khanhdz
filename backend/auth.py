# -*- coding: utf-8 -*-
"""
Authentication utilities for Olympic AI Study Hub.
PBKDF2-HMAC-SHA256 password hashing and secure token management.
Zero external library issues, works on any Python environment.
"""

import hashlib
import hmac
import secrets
from datetime import datetime, timedelta, timezone
import sqlite3
from typing import Optional, Tuple
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.config import TOKEN_EXPIRE_DAYS
from backend.database import get_db

security_bearer = HTTPBearer(auto_error=False)

def hash_password(password: str, salt: Optional[str] = None) -> Tuple[str, str]:
    """Generate salt and PBKDF2-HMAC-SHA256 hash."""
    if not salt:
        salt = secrets.token_hex(16)
    pw_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100_000
    ).hex()
    return pw_hash, salt

def verify_password(password: str, password_hash: str, salt: str) -> bool:
    """Verify password against stored hash using constant-time comparison."""
    test_hash, _ = hash_password(password, salt)
    return hmac.compare_digest(test_hash, password_hash)

def create_user_token(conn: sqlite3.Connection, user_id: int) -> str:
    """Generate a secure cryptographically random token and record in database."""
    token = secrets.token_urlsafe(36)
    expires_at = datetime.now(timezone.utc) + timedelta(days=TOKEN_EXPIRE_DAYS)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tokens (token, user_id, expires_at) VALUES (?, ?, ?);",
        (token, user_id, expires_at.isoformat())
    )
    conn.commit()
    return token

def get_current_user(
    auth: Optional[HTTPAuthorizationCredentials] = Security(security_bearer),
    conn: sqlite3.Connection = Depends(get_db)
) -> dict:
    """FastAPI dependency to retrieve currently authenticated user from Bearer token."""
    if not auth or not auth.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Yêu cầu đăng nhập để thực hiện thao tác này.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    token = auth.credentials.strip()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.id, u.username, u.display_name, u.team_name, u.role, u.created_at, t.expires_at
        FROM tokens t
        JOIN users u ON t.user_id = u.id
        WHERE t.token = ?;
    """, (token,))
    row = cursor.fetchone()
    
    if not row:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Phiên đăng nhập không hợp lệ hoặc đã hết hạn.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    user = dict(row)
    # Check expiration
    expires_at = datetime.fromisoformat(user["expires_at"])
    if expires_at < datetime.now(timezone.utc):
        cursor.execute("DELETE FROM tokens WHERE token = ?;", (token,))
        conn.commit()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return user

def get_optional_user(
    auth: Optional[HTTPAuthorizationCredentials] = Security(security_bearer),
    conn: sqlite3.Connection = Depends(get_db)
) -> Optional[dict]:
    """Retrieve user if token is provided, otherwise return None without error."""
    if not auth or not auth.credentials:
        return None
    try:
        return get_current_user(auth, conn)
    except HTTPException:
        return None
