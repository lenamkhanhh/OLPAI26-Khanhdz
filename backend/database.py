# -*- coding: utf-8 -*-
"""
Database connection and schema initialization for Olympic AI Arena.
Uses Python built-in sqlite3 for 100% portable zero-dependency reliability.
"""

import sqlite3
from typing import Generator
from backend.config import DB_PATH

def get_connection() -> sqlite3.Connection:
    """Create a new SQLite connection with dict-like row factory and foreign keys enabled."""
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def get_db() -> Generator[sqlite3.Connection, None, None]:
    """FastAPI dependency yielding a managed SQLite connection."""
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()

def init_db() -> None:
    """Initialize database tables if they do not exist."""
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        display_name TEXT NOT NULL,
        team_name TEXT DEFAULT '',
        role TEXT DEFAULT 'student',
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Auth Tokens Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tokens (
        token TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP NOT NULL
    );
    """)

    # 3. Generic Exams Table (Data-Agnostic)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT DEFAULT '',
        category TEXT DEFAULT 'AI / Machine Learning',
        duration_minutes INTEGER DEFAULT 90,
        total_points REAL DEFAULT 100.0,
        total_questions INTEGER DEFAULT 0,
        data_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 4. Submissions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        exam_id TEXT NOT NULL REFERENCES exams(id) ON DELETE CASCADE,
        score REAL NOT NULL,
        max_score REAL NOT NULL,
        graded_score REAL NOT NULL,
        essay_score REAL NOT NULL,
        correct_count INTEGER DEFAULT 0,
        total_questions INTEGER DEFAULT 0,
        time_spent_seconds INTEGER DEFAULT 0,
        answers_json TEXT NOT NULL,
        breakdown_json TEXT NOT NULL,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Indexes for performance
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_submissions_user_id ON submissions(user_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_submissions_exam_id ON submissions(exam_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_submissions_score ON submissions(score DESC);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_tokens_token ON tokens(token);")

    conn.commit()
    conn.close()
