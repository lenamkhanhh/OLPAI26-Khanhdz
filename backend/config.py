# -*- coding: utf-8 -*-
"""
Configuration module for Olympic AI Study Hub Backend.
Data-agnostic and environment-friendly.
"""

import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
EXAMS_DIR = BASE_DIR / "src" / "data" / "exams"
PUBLIC_DIR = BASE_DIR / "public"

# On Vercel Serverless, root filesystem is read-only, writable directory is /tmp
if os.getenv("VERCEL"):
    DATA_DIR = Path("/tmp/olp_data")
    DB_PATH = DATA_DIR / "arena.db"
else:
    DATA_DIR = BASE_DIR / "data"
    DB_PATH = DATA_DIR / "arena.db"

# Ensure data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Security
SECRET_KEY = os.getenv("ARENA_SECRET_KEY", "olp-ai-hcmus-secret-key-super-secure-2026")
TOKEN_EXPIRE_DAYS = int(os.getenv("TOKEN_EXPIRE_DAYS", "30"))

# Server settings
PORT = int(os.getenv("PORT", "8080"))
HOST = os.getenv("HOST", "0.0.0.0")
APP_ENV = os.getenv("APP_ENV", "production")
